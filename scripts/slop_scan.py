#!/usr/bin/env python3
"""
slop_scan.py: find common "AI slop" design tells in web source files.

Usage:
  python slop_scan.py PATH [PATH ...] [--json] [--all] [--min-severity high|medium|info]

Scans markup, styles, scripts, templates and content files (HTML, CSS/SCSS, JS/TS/JSX/TSX,
Vue, Svelte, Astro, Liquid/Nunjucks/Handlebars/EJS/ERB/PHP/Twig/Jinja, MD/MDX, JSON, YAML).
Skips node_modules, build output, lockfiles, configs, tests, stories and *.min.* files.

The output is a list of pointers, not a verdict. Each hit is something to look at,
and a few may be intentional (for example, a brand that really is purple). It can't
see layout, imagery or chart quality, so screenshot the page and look too.

Exit code: 0 by default. With --check it exits 1 while any high/medium finding or
off-grid spacing value remains, which makes it the done-condition of a fix-and-rescan loop.

Deliberate exceptions (a brand color, something the user asked for): put `slop-ok: <reason>`
on the line, or in a comment on the line above. They're listed separately so the reasons
stay visible. Never use it just to make the scan pass.
"""

from __future__ import annotations

import argparse
import colorsys
import json
import os
import re
import sys
from collections import Counter, defaultdict

EXTS = {
    ".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts",
    ".tsx", ".vue", ".svelte", ".astro", ".mdx", ".md", ".json", ".yaml", ".yml",
    ".liquid", ".njk", ".hbs", ".ejs", ".erb", ".php", ".twig", ".jinja", ".j2",
}
# config / docs that aren't user-facing site content
SKIP_FILES = re.compile(
    r"^(?:package(?:-lock)?\.json|.*lock\.(?:json|yaml)|pnpm-lock\.yaml|yarn\.lock|tsconfig.*\.json|jsconfig.*\.json|"
    r"\.?eslintrc.*|\.?prettierrc.*|composer\.json|.*\.config\.(?:js|ts|mjs|cjs|json)|vercel\.json|netlify\.toml|"
    r"manifest\.json|README.*|CHANGELOG.*|LICENSE.*|CONTRIBUTING.*|CODE_OF_CONDUCT.*|SKILL\.md|.*\.d\.ts|"
    r".*\.(?:test|spec)\.[jt]sx?|.*\.stories\.[jt]sx?)$", re.I)
IGNORE_MARK = re.compile(r"slop-ok\b", re.I)
SKIP_DIRS = {"node_modules", "dist", "build", ".next", ".git", "vendor", ".nuxt",
             ".svelte-kit", "out", "coverage", "__pycache__", ".turbo", ".vercel"}
SEV_ORDER = {"high": 0, "medium": 1, "info": 2}

# --------------------------------------------------------------------------- #
# Color helpers
# --------------------------------------------------------------------------- #
HEX_RE = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
RGB_RE = re.compile(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})")
HSL_RE = re.compile(r"hsla?\(\s*(\d{1,3}(?:\.\d+)?)(?:deg)?[\s,]+(\d{1,3}(?:\.\d+)?)%[\s,]+(\d{1,3}(?:\.\d+)?)%")


def _hls_from_rgb(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return h * 360, l, s


def colors_in(text):
    """Yield (hue_deg, lightness, saturation) for every color literal in text."""
    for m in HEX_RE.finditer(text):
        h = m.group(1)
        if len(h) in (3, 4):
            r, g, b = (int(c * 2, 16) for c in h[:3])
        else:
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        yield _hls_from_rgb(r, g, b)
    for m in RGB_RE.finditer(text):
        r, g, b = (min(255, int(x)) for x in m.groups())
        yield _hls_from_rgb(r, g, b)
    for m in HSL_RE.finditer(text):
        yield float(m.group(1)) % 360, float(m.group(3)) / 100, float(m.group(2)) / 100


def is_ai_hue(h, l, s):
    """Purple / violet / indigo / magenta / electric blue, saturated: the vibecode spectrum."""
    return 215 <= h <= 335 and s >= 0.40 and 0.15 <= l <= 0.85


def is_saturated(h, l, s):
    return s >= 0.45 and 0.15 <= l <= 0.85


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #
AI_TW_HUES = r"(?:purple|violet|indigo|fuchsia|pink)"
GLOW_TW_HUES = r"(?:purple|violet|indigo|fuchsia|pink|blue|cyan|sky|emerald|teal|rose)"

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA70-\U0001FAFF"  # symbols & pictographs ext-A
    "☀-⛿"          # misc symbols (⚡ ⚠ ☀ ...)
    "✨⭐✅❌❤➡⬆⬇"  # ✨ ⭐ ✅ ❌ ❤ ➡
    "]"
)

BUZZWORDS = [
    r"supercharg\w*", r"turbocharg\w*", r"skyrocket\w*", r"unlock(?:s|ing)?", r"unleash\w*",
    r"harness(?:es|ing)? the power", r"elevat(?:e|es|ing) your", r"revolutioni[sz]\w*",
    r"reimagin\w*", r"seamless(?:ly)?", r"effortless(?:ly)?", r"frictionless",
    r"cutting[- ]edge", r"next[- ]gen(?:eration)?", r"state[- ]of[- ]the[- ]art",
    r"game[- ]chang\w*", r"world[- ]class", r"best[- ]in[- ]class", r"empower\w*",
    r"leverag\w*", r"streamlin\w*", r"all[- ]in[- ]one", r"one[- ]stop",
    r"lightning[- ]fast", r"blazing(?:ly)?[- ]fast", r"next level", r"in seconds",
    r"ai[- ]powered", r"powered by ai", r"transform(?:s|ing)? (?:the way|your)",
    r"say goodbye to", r"delve", r"embark", r"magic(?:al)?(?:ly)?\b",
]
BUZZ_RE = re.compile(r"\b(?:" + "|".join(BUZZWORDS) + r")\b", re.I)

RULES = [
    # ---------------- HIGH: almost always slop ----------------
    dict(id="gradient-text", sev="high", cat="Gradient text",
         rx=re.compile(r"bg-clip-text|(?:-webkit-)?background-clip:\s*text|text-transparent"),
         why="Gradient-filled headline text is the most recognizable vibecoded tell.",
         fix="Use solid text. Get emphasis from size and weight, not color tricks."),
    dict(id="tw-ai-gradient", sev="high", cat="Purple/blue gradient",
         rx=re.compile(rf"\b(?:from|via|to)-{AI_TW_HUES}-\d{{2,3}}\b"),
         why="Purple-blue-pink gradients are the default AI accent.",
         fix="Use solid surfaces. If the brief wants a gradient, keep it subtle, single-hue, and in one place."),
    dict(id="tw-glow", sev="high", cat="Colored glow",
         rx=re.compile(rf"\bshadow-{GLOW_TW_HUES}-\d{{2,3}}(?:/\d+)?\b|shadow-\[0_0_\d+px"),
         why="Colored glows fake hierarchy and come straight from crypto/gaming templates.",
         fix="Remove them. Use small neutral shadows only on floating layers (menus, dialogs)."),
    dict(id="blob", sev="high", cat="Blurred blob / orb",
         rx=re.compile(r"\bblur-(?:2xl|3xl)\b|\bblur-\[\d{2,}px\]|filter:\s*blur\(\s*(?:[4-9]\d|\d{3,})px"),
         why="Big blurred color circles are filler for empty space.",
         fix="Delete them. If the area feels empty, fix the layout or content."),
    dict(id="sparkles", sev="high", cat="Sparkles = AI",
         rx=re.compile(r"✨|<Sparkles\b|\bSparkles\s*[,}]|sparkle", re.I),
         why="✨ as shorthand for AI/new/magic is the iconic slop emoji.",
         fix="Remove it. Describe what the feature does."),
    dict(id="double-bang", sev="high", cat="Exclamation marks in UI",
         rx=re.compile(r"[A-Za-z0-9%)\]]!!+(?![=])"),
         why="'!!' tries to supply excitement the content doesn't have.",
         fix="No exclamation marks in interface copy. Add a baseline instead ('+12% vs last month')."),

    # ---------------- MEDIUM: usually slop, needs judgment ----------------
    dict(id="emoji", sev="medium", cat="Emoji in UI",
         rx=EMOJI_RE,
         why="Emoji used as icons or status signals means there's no icon system.",
         fix="Use one icon family (one stroke, one size, currentColor). Use colored dots for categories."),
    dict(id="glass", sev="medium", cat="Glassmorphism",
         rx=re.compile(r"\bbackdrop-blur(?:-\w+)?\b|backdrop-filter:\s*blur|\bbg-white/(?:5|10|15)\b|\bborder-white/(?:5|10|20)\b"),
         why="Translucent blurred cards with white borders are a stock AI recipe.",
         fix="Use solid surfaces with a 1px subtle border. Keep blur only where content scrolls under a sticky bar, if at all."),
    dict(id="tw-ai-color", sev="medium", cat="Default AI purple/indigo",
         rx=re.compile(rf"\b(?:bg|text|border|ring|fill|stroke|outline|decoration|accent|caret)-{AI_TW_HUES}-\d{{2,3}}(?:/\d+)?\b"),
         why="Tailwind violet/indigo/purple is the demo accent every model reaches for.",
         fix="Pick the accent from the subject or brand. Use one accent for actions and selection only."),
    dict(id="caps-tracking", sev="medium", cat="ALL-CAPS tracked labels",
         rx=re.compile(r"\buppercase\b.*\btracking-(?:wide|wider|widest|\[)|\btracking-(?:wide|wider|widest|\[).*\buppercase\b|text-transform:\s*uppercase"),
         why="Tracked-out caps eyebrows above everything are template chrome.",
         fix="Use sentence case. Add a label only if it says something the heading doesn't."),
    dict(id="caps-literal", sev="medium", cat="ALL-CAPS tracked labels",
         rx=re.compile(r">\s*(?:[^\sA-Za-z<]{1,3}\s*)?[A-Z][A-Z0-9&/'\-]+(?:\s+[A-Z0-9&/'\-]+)*\s*<"),
         why="Hard-coded caps labels ('PAID THIS MONTH') shout and read as template.",
         fix="Write them in sentence case."),
    dict(id="bang", sev="medium", cat="Exclamation marks in UI",
         rx=re.compile(r"[A-Za-z0-9%)\]]!(?=\s*(?:<|[\"'`]\s*[,;)}\]\n]|\s*$))(?!important)"),
         why="Exclamation marks in interface copy read as forced enthusiasm.",
         fix="End with a period, or with nothing."),
    dict(id="buzzword", sev="medium", cat="Buzzword copy",
         rx=BUZZ_RE,
         why="Marketing filler words that say nothing specific.",
         fix="Say what actually happens for whom. See the replacement table in Appendix B of the skill."),
    dict(id="welcome", sev="medium", cat="Generic greeting / filler copy",
         rx=re.compile(r"Welcome back|Good (?:morning|afternoon|evening),|Ready to (?:get started|transform|take)|Join (?:thousands|millions)|Search anything", re.I),
         why="Greetings and filler instead of telling the user what they're looking at.",
         fix="Orient: page name, period, status, next action ('October 2026', 'Search')."),
    dict(id="ai-name", sev="medium", cat="'AI' in name/tagline",
         rx=re.compile(r"\b[A-Z][a-z]+AI\b|\bAI[- ]powered\b|\b[Pp]owered by AI\b|\b[Ww]ith AI\b"),
         why="'AI' in the name or tagline is filler unless it's the actual point.",
         fix="Name the product plainly. Describe the outcome, not the technology."),
    dict(id="badge-words", sev="medium", cat="Hype badges",
         rx=re.compile(r">\s*(?:[^\sA-Za-z<]{1,3}\s*)?(?:PRO|NEW|BETA|HOT)\s*(?:[^\sA-Za-z<]{1,3}\s*)?<"),
         why="'PRO' / 'New ✨' pills decorate instead of inform.",
         fix="Keep a badge only if it changes what the user does."),
    dict(id="vanity-stat", sev="medium", cat="Unverified stats / fake proof",
         rx=re.compile(r"\b\d[\d,.]*\s*[kKmM]?\+\s*(?:happy\s+|satisfied\s+|active\s+)?(?:users|customers|teams|developers|companies|businesses|creators|clients|members)\b|\b99\.9+%|\b10x\b|\b4\.9\s*/\s*5\b|\b#1\b", re.I),
         why="Invented numbers are fake proof, and visitors can tell.",
         fix="Use the user's real figures, or a clearly marked placeholder: [Add real stat]."),
    dict(id="placeholder-people", sev="medium", cat="Unverified stats / fake proof",
         rx=re.compile(r"\b(?:John|Jane) Doe\b|\bSarah (?:Johnson|Chen|Miller|Williams)\b|\bAlex (?:Chen|Johnson|Rivera|Morgan)\b|\bMichael (?:Chen|Brown|Scott)\b|\bEmily (?:Davis|Chen|Rodriguez)\b|\bDavid (?:Kim|Park|Lee)\b|\b(?:Acme|Globex|TechCorp|TechFlow|Initech)\b|lorem ipsum", re.I),
         why="Invented testimonials, people, and companies.",
         fix="Use real quotes and names, or a marked placeholder: [Customer quote]."),
    dict(id="hover-scale", sev="medium", cat="Hover bounce / attention motion",
         rx=re.compile(r"hover:scale-1\d\d|hover:-translate-y-|group-hover:scale-|animate-(?:bounce|ping)\b|:hover[^{]*\{[^}]*transform:\s*(?:scale\(1\.\d+\)|translateY\(-\d)"),
         why="Every card lifting or scaling on hover is template motion.",
         fix="Show hover with color or border. Save motion for responses to user actions."),
    dict(id="pulse", sev="medium", cat="Hover bounce / attention motion",
         rx=re.compile(r"\banimate-pulse\b"),
         why="Pulsing is fine for loading skeletons. Elsewhere it's fake liveness.",
         fix="Keep it only on loading placeholders."),
    dict(id="css-gradient", sev="medium", cat="Decorative gradient",
         rx=re.compile(r"\b(?:linear|radial|conic)-gradient\(|\bbg-(?:gradient-to-\w+|linear-to-\w+|linear-\d+|radial\b|conic\b)"),
         why="Gradients as decoration (backgrounds, buttons, borders).",
         fix="Use solid colors unless the gradient carries meaning (a heatmap) or the brief asks for it."),

    # ---------------- AI-sounding copy ----------------
    dict(id="chatbot-residue", sev="high", cat="Chatbot residue in copy",
         rx=re.compile(r"\bCertainly!|\bI hope this helps\b|\bGreat question\b|\bAs an AI\b|\bHere['’]s (?:a|an|the) (?:revised|updated|improved) ", re.I),
         why="Leftover assistant phrasing on a live page.",
         fix="Delete it. Keep only the content."),
    dict(id="not-x-but-y", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"\b(?:not just|not only|not merely|more than just|isn['’]t just|is not just|isn['’]t (?:just )?(?:another|your average|your typical))\b|\bIt['’]s not\b[^.<]{1,60}\bit['’]s\b|\bmore than an? \w+[^.<]{0,10}[:—–-]\s*(?:it['’]s|a|an)\b", re.I),
         why="'Not just X, it's Y' rejects a claim nobody made so the real claim sounds bigger.",
         fix="State the positive claim directly, with a specific detail."),
    dict(id="slogan-triad", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"(?:^|>|[\"'`])\s*(?:[A-Z][a-z]+\.\s+){2,}[A-Z][a-z]+\.(?=\s*(?:<|[\"'`]|$))|(?:\bNo [a-z]+\.\s+){2,}"),
         why="'Fast. Simple. Powerful.' style fragment stacks are slogan filler.",
         fix="Write one specific sentence about what actually happens."),
    dict(id="rhetorical-opener", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"(?:^|>|[\"'`])\s*(?:Tired of|Sick of|Ever (?:wish|wonder|feel)\w*|What if|Imagine (?:a|if|your|having)|Struggling (?:to|with)|Looking for an?)\b"),
         why="Rhetorical-question openers stall instead of saying the point.",
         fix="Answer the question. Lead with the claim."),
    dict(id="whether-youre", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"\bWhether you['’]re\b", re.I),
         why="'Whether you're X or Y' speaks to everyone and therefore no one.",
         fix="Name the real audience."),
    dict(id="hype-phrase", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"we['’]ve got you covered|look no further|say (?:goodbye|hello) to|you['’]ll love|in today['’]s|fast[- ]paced world|the future of \w+|that['’]s the \w+(?: \w+)? difference|it['’]s that simple|the choice is clear|work smarter|thank you later|take (?:it|your \w+) to the next level|ready to (?:transform|elevate|take)", re.I),
         why="Stock hype phrases that fit any product.",
         fix="Cut them, or replace with a concrete fact about this product."),
    dict(id="ai-words", sev="medium", cat="AI-sounding copy",
         rx=re.compile(r"\b(?:nestled|in the heart of|crafted with|made with love|passion(?:ate(?:ly)?)?(?! ?fruit)|curated|artisanal|elevated|rich (?:history|heritage|tradition)|vibrant|testament|tapestry|delv\w+|robust|crucial|pivotal|showcas\w+|breathtaking|stunning|indulge|meticulous\w*|bespoke|solutions?\b(?= for| that))\b", re.I),
         why="Words models use far more often than people do; they read as generated or as a brochure.",
         fix="Use plain words and specific facts: where, what, since when, made how."),
    dict(id="em-dash", sev="medium", cat="Em dashes in copy",
         rx=re.compile(r"\S\s*(?:—|&mdash;)\s*\S|\s(?:–|&ndash;)\s|\s--\s"),
         why="Em dashes (and spaced en dashes) everywhere are a strong AI writing tell.",
         fix="Use a period, comma, colon, or parentheses. One dash on a whole page is fine. Unspaced en dashes in ranges (Tue–Sun, 7–3) are correct and not flagged."),
    dict(id="generic-cta", sev="info", cat="Generic button text",
         rx=re.compile(r">\s*(?:Get [Ss]tarted(?: [Ff]or [Ff]ree| [Ff]ree| [Nn]ow| [Tt]oday)?|Learn [Mm]ore|Submit|Click [Hh]ere|Sign [Uu]p [Nn]ow|Try [Ii]t [Nn]ow)\s*(?:→|->|&rarr;)?\s*<"),
         why="Buttons that don't say what happens.",
         fix="Name the action: 'Book a table', 'Add to a meeting', 'Download the menu'."),

    # ---------------- INFO: check it's deliberate ----------------
    dict(id="default-font", sev="info", cat="Default AI font",
         rx=re.compile(r"(?:font-family|fontFamily|family=|font-sans|fonts\.googleapis)[^;\n]*\b(Inter|Poppins|Space\+?\s?Grotesk|Plus\+?\s?Jakarta\+?\s?Sans|DM\+?\s?Sans|Outfit|Manrope|Sora|Geist)\b"),
         why="The fonts models pick when no one picks.",
         fix="Fine if chosen on purpose for this subject. Otherwise choose a face that fits the subject's voice."),
    dict(id="transition-all", sev="info", cat="transition-all",
         rx=re.compile(r"\btransition-all\b|transition:\s*all\b"),
         why="Animating 'all' is the lazy default and can animate layout.",
         fix="Transition only the properties that change (color, background, opacity), at 120-200ms."),
    dict(id="arrow-cta", sev="info", cat="Arrow-suffixed CTAs",
         rx=re.compile(r"\s→\s*<|\s->\s*<"),
         why="'Get started →' on every button is template chrome.",
         fix="Name the action. Use an arrow only where it means 'goes somewhere'."),
    dict(id="icon-tile", sev="info", cat="Tinted icon tiles",
         rx=re.compile(r"\bbg-\w+-\d{3}/(?:10|15|20)\b"),
         why="An icon in a tinted rounded square, a different color per feature card.",
         fix="Use one neutral treatment or none, and one color with one meaning."),
    dict(id="bg-pattern", sev="info", cat="Decorative grid/dot backdrop",
         rx=re.compile(r"mask-image:\s*radial-gradient|\[mask-image:radial|bg-\[radial-gradient|bg-grid|bg-dot"),
         why="Faded grid/dot patterns behind heroes.",
         fix="Remove them unless the grid means something."),
]

# Things we count instead of listing line by line
COUNTERS = {
    "big radius (rounded-2xl/3xl/full, radius ≥ 20px)": re.compile(
        r"\brounded-(?:2xl|3xl|full)\b|border-radius:\s*(?:[2-9]\d|\d{3,})px|border-radius:\s*9999px|border-radius:\s*50%"),
    "heavy weights (font-bold/extrabold/black, weight ≥ 700)": re.compile(
        r"\bfont-(?:bold|extrabold|black)\b|font-weight:\s*(?:[7-9]00|bold|bolder)"),
}

# Spacing extraction
TW_ARB_SPACE = re.compile(
    r"(?<![\w-])-?(?:p|px|py|pt|pr|pb|pl|ps|pe|m|mx|my|mt|mr|mb|ml|ms|me|gap|gap-x|gap-y|space-x|space-y|top|left|right|bottom|inset|inset-x|inset-y)-\[(\d+(?:\.\d+)?)px\]")
CSS_SPACE = re.compile(
    r"(?<![\w-])(?:padding|margin|gap|row-gap|column-gap|inset|top|left|right|bottom)(?:-(?:top|right|bottom|left|inline|block|inline-start|inline-end|block-start|block-end))?\s*:\s*([^;}\n]+)")
PX_VAL = re.compile(r"(-?\d+(?:\.\d+)?)px")


def extra_color_checks(line):
    """CSS-level checks that need color parsing."""
    hits = []
    low = line.lower()
    if "gradient(" in low:
        cols = list(colors_in(line))
        if any(is_ai_hue(*c) for c in cols):
            hits.append(("css-ai-gradient", "high", "Purple/blue gradient",
                         "Gradient in the purple/indigo/blue range: the default AI accent.",
                         "Use solid surfaces. If a gradient is wanted, keep it subtle and single-hue."))
    for m in re.finditer(r"<(h[1-6]|button|title)\b[^>]*>\s*([^<]{6,})\s*</\1>", line, re.I):
        text = m.group(2)
        words = re.findall(r"[A-Za-z][A-Za-z'’]*", text)
        big = [w for w in words if len(w) > 3]
        if len(big) >= 3 and all(w[0].isupper() for w in big) and not text.isupper():
            hits.append(("title-case", "medium", "Title Case headings",
                         "Every Word Capitalized reads as template copy.",
                         "Use sentence case for headings, buttons and page titles."))
            break
    if re.search(r"(?:box|text)-shadow\s*:", low) or "drop-shadow(" in low:
        # a glow = saturated color AND a real blur (>= 8px). Focus rings (0 0 0 3px blue) are fine.
        cols = list(colors_in(line))
        blurs = [int(b) for b in re.findall(r"(?:-?\d*\.?\d+(?:px)?\s+){2}(\d+)px", line)]
        if any(is_saturated(*c) for c in cols) and blurs and max(blurs) >= 8:
            hits.append(("css-glow", "high", "Colored glow",
                         "A colored shadow or glow fakes hierarchy.",
                         "Remove it. Use small neutral shadows only on floating layers."))
    return hits


def snippet(line, start, end, width=150):
    line = line.rstrip("\n")
    if len(line) <= width:
        return line.strip()
    s = max(0, start - width // 3)
    e = min(len(line), s + width)
    return ("…" if s > 0 else "") + line[s:e].strip() + ("…" if e < len(line) else "")


def nice_path(p):
    r = os.path.relpath(p)
    return p if r.startswith("..") else r


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for f in files:
                if ".min." in f or SKIP_FILES.match(f):
                    continue
                if os.path.splitext(f)[1].lower() in EXTS:
                    yield os.path.join(root, f)


def scan(paths):
    findings = []
    counters = Counter()
    counter_locs = defaultdict(list)
    spacing = Counter()
    spacing_locs = defaultdict(list)
    exceptions = []
    files = list(iter_files(paths))

    for path in files:
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        except OSError as e:
            print(f"warn: cannot read {path}: {e}", file=sys.stderr)
            continue
        rel = nice_path(path)
        in_hover = False
        for i, line in enumerate(lines, 1):
            if ":hover" in line and "{" in line and "}" not in line:
                in_hover = True
            elif in_hover:
                if re.search(r"transform:\s*(?:scale\(1\.\d+\)|translateY\(-\d)", line):
                    findings.append(dict(rule="hover-scale", severity="medium", category="Hover bounce / attention motion",
                                         why="Every card lifting or scaling on hover is template motion.",
                                         fix="Show hover with color or border. Save motion for responses to user actions.",
                                         file=rel, line=i, match="", snippet=snippet(line, 0, 0)))
                if "}" in line:
                    in_hover = False
            if len(line) > 5000:  # minified bundle line
                continue
            prev = lines[i - 2] if i > 1 else ""
            prev_is_marker_comment = bool(re.match(r"\s*(?://|/\*|<!--|\{/\*|#)\s*slop-ok", prev, re.I))
            if IGNORE_MARK.search(line) or prev_is_marker_comment:
                exceptions.append(f"{rel}:{i}  {line.strip()[:120]}")
                continue
            seen_ids = set()
            for r in RULES:
                m = r["rx"].search(line)
                if not m:
                    continue
                # gradient-text 'text-transparent' alone is fine (e.g. transparent text for a11y);
                # require a clip hint for that case
                if r["id"] == "gradient-text" and "text-transparent" in m.group(0) and "clip" not in line:
                    continue
                # sparkles also matches emoji rule; avoid double-reporting the same char
                if r["id"] == "emoji" and "✨" in line and "sparkles" in seen_ids and len(EMOJI_RE.findall(line)) == 1:
                    continue
                # don't flag a single-bang line already flagged as double-bang
                if r["id"] == "bang" and "double-bang" in seen_ids:
                    continue
                # caps-literal: ignore short acronyms / code-ish lines
                if r["id"] == "caps-literal" and len(re.sub(r"[^A-Z]", "", m.group(0))) < 5:
                    continue
                # css-gradient is generic; skip if already a high-severity gradient hit on this line
                if r["id"] == "css-gradient" and ({"tw-ai-gradient", "gradient-text"} & seen_ids):
                    continue
                seen_ids.add(r["id"])
                findings.append(dict(rule=r["id"], severity=r["sev"], category=r["cat"],
                                     why=r["why"], fix=r["fix"], file=rel, line=i,
                                     match=m.group(0), snippet=snippet(line, m.start(), m.end())))
            for rid, sev, cat, why, fix in extra_color_checks(line):
                if rid == "css-ai-gradient":
                    # replace the generic gradient hit on this line with the specific one
                    findings[:] = [f for f in findings if not (f["file"] == rel and f["line"] == i and f["rule"] == "css-gradient")]
                findings.append(dict(rule=rid, severity=sev, category=cat, why=why, fix=fix,
                                     file=rel, line=i, match="", snippet=snippet(line, 0, 0)))
            for name, rx in COUNTERS.items():
                n = len(rx.findall(line))
                if n:
                    counters[name] += n
                    if len(counter_locs[name]) < 5:
                        counter_locs[name].append(f"{rel}:{i}")
            for m in TW_ARB_SPACE.finditer(line):
                v = float(m.group(1))
                spacing[v] += 1
                spacing_locs[v].append(f"{rel}:{i}")
            for m in CSS_SPACE.finditer(line):
                for pv in PX_VAL.findall(m.group(1)):
                    v = abs(float(pv))
                    spacing[v] += 1
                    spacing_locs[v].append(f"{rel}:{i}")

    # ignore off-screen hacks (left: -9999px for skip links) and 1-4px hairlines
    off_grid = sorted(v for v in spacing if 4 < v < 1000 and v % 4 != 0)
    return dict(
        files_scanned=len(files),
        files=[nice_path(f) for f in files],
        exceptions=exceptions,
        findings=findings,
        counters={k: dict(count=v, examples=counter_locs[k]) for k, v in counters.items()},
        spacing=dict(
            values={(int(k) if k == int(k) else k): c for k, c in sorted(spacing.items())},
            distinct=len(spacing),
            off_grid=[(int(v) if v == int(v) else v) for v in off_grid],
            off_grid_locations={str(int(v) if v == int(v) else v): spacing_locs[v][:4] for v in off_grid},
        ),
    )


def print_report(res, show_all=False, min_sev="info"):
    fnd = [f for f in res["findings"] if SEV_ORDER[f["severity"]] <= SEV_ORDER[min_sev]]
    by_sev = Counter(f["severity"] for f in fnd)
    print(f"AI-slop scan: {res['files_scanned']} file(s), {len(fnd)} finding(s) "
          f"({by_sev.get('high', 0)} high, {by_sev.get('medium', 0)} medium, {by_sev.get('info', 0)} info)\n")

    for sev in ("high", "medium", "info"):
        group = [f for f in fnd if f["severity"] == sev]
        if not group:
            continue
        print(sev.upper())
        cats = defaultdict(list)
        for f in group:
            cats[f["category"]].append(f)
        for cat, items in sorted(cats.items(), key=lambda kv: -len(kv[1])):
            print(f"  {cat}  ({len(items)})")
            print(f"    why: {items[0]['why']}")
            print(f"    fix: {items[0]['fix']}")
            shown = items if show_all else items[:6]
            for f in shown:
                print(f"    {f['file']}:{f['line']}  {f['snippet']}")
            if len(items) > len(shown):
                print(f"    … {len(items) - len(shown)} more (use --all)")
        print()

    sp = res["spacing"]
    if sp["distinct"]:
        vals = ", ".join(f"{k}×{v}" for k, v in sp["values"].items())
        print("SPACING")
        print(f"  px values used: {vals}")
        msg = f"  {sp['distinct']} distinct value(s)"
        if sp["off_grid"]:
            msg += f"; off a 4px grid: {', '.join(str(v) for v in sp['off_grid'])}"
        print(msg)
        for v, locs in sp["off_grid_locations"].items():
            print(f"    {v}px  {', '.join(locs)}")
        if sp["distinct"] > 12 or sp["off_grid"]:
            print("  → Pick a scale (e.g. 4 8 12 16 24 32 48 64), put it in variables, and snap every value to it.")
        print()

    if res["counters"]:
        print("COUNTS (look at these in a screenshot; high counts usually mean defaults)")
        for k, v in res["counters"].items():
            print(f"  {k}: {v['count']}   e.g. {', '.join(v['examples'][:3])}")
        print()

    per_file = Counter(f["file"] for f in fnd)
    clean_files = [f for f in res["files"] if f not in per_file]
    print("FILES")
    for f, n in per_file.most_common():
        print(f"  {n:>4}  {f}")
    if clean_files:
        print(f"  clean: {len(clean_files)} file(s)" + ("" if len(clean_files) > 12 else ": " + ", ".join(clean_files)))
    print()

    if res["exceptions"]:
        print(f"EXCEPTIONS marked slop-ok ({len(res['exceptions'])}). Each needs a real reason (brief or brand):")
        for e in res["exceptions"][:20]:
            print(f"  {e}")
        print()

    blocking = [f for f in fnd if f["severity"] in ("high", "medium")]
    if not blocking and not sp["off_grid"]:
        print("CLEAN: no high/medium code-level tells. Still screenshot every page: layout, imagery and charts need eyes.")
    else:
        print(f"NOT CLEAN: {len(blocking)} high/medium finding(s)"
              + (f", {len(sp['off_grid'])} off-grid spacing value(s)" if sp["off_grid"] else "")
              + ". Fix, then scan again.")


def main():
    ap = argparse.ArgumentParser(description="Scan web source files for AI-slop design tells.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--all", action="store_true", help="show every hit, not the first 6 per category")
    ap.add_argument("--min-severity", choices=["high", "medium", "info"], default="info")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any high/medium finding or off-grid spacing remains (for fix-and-rescan loops)")
    a = ap.parse_args()
    res = scan(a.paths)
    blocking = [f for f in res["findings"] if f["severity"] in ("high", "medium")]
    dirty = bool(blocking or res["spacing"]["off_grid"])
    if a.json:
        res["findings"] = [f for f in res["findings"]
                           if SEV_ORDER[f["severity"]] <= SEV_ORDER[a.min_severity]]
        res["summary"] = dict(Counter(f["severity"] for f in res["findings"]))
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print_report(res, show_all=a.all, min_sev=a.min_severity)
    if a.check and dirty:
        sys.exit(1)


if __name__ == "__main__":
    main()
