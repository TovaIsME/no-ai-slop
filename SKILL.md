---
name: no-ai-slop
description: Removes and prevents "AI slop" in website and UI design, both the look and the words. Visual tells include purple-blue gradients, gradient text, glows, glassmorphism, blurred blobs, emoji used as icons, ✨ sparkles, ALL-CAPS labels, random spacing, decorative charts, and the template landing-page layout. Copy tells include buzzwords ("unlock", "seamless"), "not just X, it's Y", "Fast. Simple. Powerful.", em dashes, exclamation marks, and fake stats and testimonials. All site text gets rewritten so it reads like a person wrote it. Use whenever the user builds, designs, redesigns, reviews, or polishes a website, landing page, dashboard, or web app UI, or writes copy for one. Also use when they say it looks or sounds AI-generated, vibecoded, generic, templated, or cheap, or ask to "unslop" or humanize it, even if they never say "slop".
---

# No AI Slop

In web design, "AI slop" is the set of things a model produces when nobody actually decided anything. You get a purple-to-blue gradient because that is the default accent. An emoji shows up because there was no icon set, and "!!" appears because there was no real information to put in its place. A glow stands in for hierarchy that was never worked out. Each tell is small. Together they make a page read as "generated and never reviewed" within a second, and then visitors stop trusting everything else on it.

This skill removes those defaults and puts real decisions in their place. It is **not a house style**. The goal is not "make it black and gray". The goal is a page where you could explain out loud why each color, effect, word and spacing value is there.

## The brief always wins

If the user asks for a purple gradient, a playful emoji-heavy tone or a glassy look, build that, and do it well. Brand guidelines win too: a brand's own purple is not slop. This skill targets *defaults* and leaves alone anything someone deliberately chose. When you keep something that would normally count as a tell, say why ("kept the gradient, it's in your brand guide").

## Two modes

- **Cleaning up** an existing site, component or screenshot: audit, fix in pass order, verify. See "Workflow: cleaning up" below.
- **Building new**: make the decisions first, build, then run the same audit on your own output. See "Workflow: building new" below.

Both modes use the same seven-pass unslop process.

## The unslop pass

Do the passes in this order. Spacing comes first because it is structural and everything else sits on it. Color and effects come second because removing the glow shows whether the hierarchy actually works. After that come the details.

The running example is a real teardown of a vibecoded fintech dashboard called "EmberAI". The left column is what the AI produced and the right column is what a designer changed it to.

### 1. Spacing and alignment

| Slop | Fixed |
|---|---|
| Gaps picked one at a time: 26, 44, 46, 30, 38px | One scale: 16, 24, 32, 36px, reused |
| Nav rows unevenly spaced: some items got extra margin | Every row the same height |
| Left edges 2–3px apart from each other | Logo, search icon, nav icons, labels and dots all share one left edge |

- Pick a base unit: 4px, or 8px for airy marketing pages. Then pick a short scale such as 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96. Put it in CSS variables or the Tailwind theme and use only those values.
- Elements with the same role get the same spacing: same row height, same card padding, same rhythm between sections.
- Spacing shows grouping. Space inside a group should be smaller than space between groups, which should be smaller than space between sections.
- Align to shared edges. Picture a vertical line down the sidebar or content column: everything should start on it or on one consistent inset from it.

In the example, this pass alone made the page noticeably calmer, before any color changed.

### 2. Color, gradients and effects

| Slop | Fixed |
|---|---|
| Purple→blue gradient page background | Neutral near-black with 2 surface steps |
| Gradient-filled active nav item with a purple glow | One step lighter gray, faint 1px border |
| Glowing pill badges | Plain muted numbers |
| Gradient headline text | Solid text color |
| Translucent glass cards with luminous borders | Solid surface with a 1px subtle border |

- Start neutral: a background, 1–2 surface steps, a border color, primary text and muted text. You can tint the neutrals slightly toward the brand hue for warmth, but do not saturate them.
- Use at most one accent, and use it for the primary action and the current selection, not for decoration.
- Every color should *mean* something. Status: green for up, red for down. Category: one color per data series, reused everywhere that category appears. Interactive state. If you cannot say what a color means, make it neutral.
- Separate surfaces with a 1px border or one step of lightness. Use small, neutral shadows, and only on things that actually float, such as menus, popovers and dialogs. No colored glows.
- Remove gradient text, glass blur and blurred background orbs. If the page feels empty without them, the problem is content or layout, not missing decoration.

In the example, the only color left at the end is green on positive changes and five plan colors that double as the chart legend.

### 3. Icons, emoji and badges

| Slop | Fixed |
|---|---|
| Emoji as nav icons: 🏠 📥 🚀 👥 💸 📊 | One line-icon set, same stroke, same size |
| Emoji as status: 🔥 +12%, 😬 3 less | Green text, plus a comparison |
| Emoji per plan: 🏢 💼 ⚡ 🌱 🎁 | Small colored dots that match the chart lines |
| ✨ logo, "PRO" pill, "New ✨" pill, count pills with 👤 | Plain logomark, no pills, plain numbers, a chevron where a row expands |
| A bell that opens nothing | A sidebar-collapse control the screen actually needs |
| ⌘K inside a glowing pill | Two quiet keycaps: ⌘ K |

- Use one icon family (Lucide, Phosphor, Heroicons, Tabler or similar, but just one) with one stroke width and one size, inheriting the text color. Use inline SVG if there is no library.
- Emoji are content (a user's reaction, a chat message), not interface.
- Use badges only for states the user must notice, such as unread counts, and even then keep them quiet. Drop "New", "PRO", "Beta" and "Hot" unless they change what the user does.
- Every control should do something. Remove ornamental controls.
- ✨ never means "AI". If a feature uses AI, describe what it does.

### 4. Copy: write like a person

Text is where AI shows fastest. A visitor may not be able to say why a gradient looks generated, but almost everyone recognizes "Unlock the power of seamless collaboration." Every word on the page gets the same treatment as every pixel: headlines, buttons, labels, feature blurbs, About text, error messages, empty states, alt text, page titles and meta descriptions.

**Interface copy (the EmberAI example)**

| Slop | Fixed |
|---|---|
| "Welcome back, Damir! 👋" | "October 2026": what this screen is showing |
| "+12%!!" | "+12% vs last month" |
| "🚀 +4.2% this month!!" | "4.2% ↑ vs September" |
| "😬 3 less" | "3 fewer" |
| "Search anything..." | "Search" |
| "EmberAI" | "Ember" |

- Replace greetings with orientation: what is this screen, and what period or state is it showing?
- Every number needs a unit and a baseline. A bare "+12%" is noise.
- No exclamation marks in interface copy.
- Buttons name the action ("Book a table", "Export CSV"), not "Submit", "Learn more" or "Get started →".
- Errors say what happened and how to fix it. Empty states say what to do next. No "Oops!" and no 🎉.

**Marketing and content copy.** These are the patterns that make website text sound generated. Rewrite on sight:

| AI pattern | Example | Human version |
|---|---|---|
| Not X but Y | "It's not just a note app. It's your second brain." | "Murmur records your meetings and writes the summary." |
| Slogan triads and fragments | "Fast. Simple. Powerful." / "No setup. No hassle. Just results." | One specific sentence: "Install the app, join a call, get notes when it ends." |
| Rhetorical question openers | "Tired of endless meetings?" / "What if…?" / "Imagine a world where…" | Say the claim directly. |
| "Whether you're X or Y" | "Whether you're a startup or an enterprise…" | Name who it is actually for. |
| Inflated significance | "Redefining the way you work", "the future of baking" | What changes, concretely. |
| Sales and travel-brochure words | "nestled in the heart of", "crafted with passion", "rich heritage", "curated", "elevated experience", "journey" | Plain facts: where, what, since when, made how. |
| Stock AI words | unlock, elevate, seamless, effortless, robust, delve, vibrant, crucial, showcase, testament, tapestry, landscape | Plain verbs: is, has, makes, lets you, use. |
| One-line closers | "That's the Murmur difference." / "The choice is clear." | Cut. End on the last concrete fact. |
| Em dashes everywhere | "Meetings — summarized. Notes — handled." | Periods, commas, colons. At most one dash on a page, and only if it really reads best. |
| Bold-label lists | "**Fast:** Get notes instantly. **Secure:** Your data is safe." | Plain sentences, or a list without the bold labels. |
| Title Case Headings | "Everything You Need To Grow" | Sentence case: "What's included" |
| Hype filler | "We've got you covered", "You'll love it", "Say hello to…", "Look no further" | Cut. |

How to write it instead:

- **Be specific.** Specifics are what make text sound human: real names, numbers, places, times, prices, materials. "Open from 6:30. The cardamom buns are usually gone by 10" beats "Freshly baked goods made with love every day." If you don't have the specific, don't invent it. Use a marked placeholder (`[opening hours]`) and ask the user. But write true sentences from what you were given, and use a placeholder only for a fact you'd otherwise have to invent. A page that's half yellow boxes isn't finished either.
- **Write the way the owner talks to a customer.** Small businesses say "we" and "you". Developer tools talk like a developer. A law firm is calm and exact. Read each line aloud and ask whether a real person at this business would say it to a real customer.
- **Vary the rhythm.** Mix short sentences with longer ones. Don't make every feature blurb two sentences of the same length.
- **Headline = what it is. Subhead = who it's for or how it works.** Cleverness is fine only once the meaning is already clear.
- **Lead with the outcome, not the technology.** Drop "AI" from names and taglines unless it is the actual differentiator.
- **Never invent proof.** That means no made-up stats ("10,000+ teams", "99.9% uptime", "10x faster"), no fake customer logos, no fake testimonials ("Sarah Johnson, CEO at TechCorp") and no ★★★★★. Use the user's real ones, or a clearly marked placeholder (`[Customer quote: add a real one]`), and tell them.
- **Keep the meaning.** When rewriting existing copy, keep every real fact and claim. Only the dressing goes.

Appendix B has the full guide: the buzzword replacement table and before/after rewrites by page type (hero, features, About, pricing, CTAs, microcopy, meta tags). Read it whenever the page has more than a few lines of text.

### 5. Typography

| Slop | Fixed |
|---|---|
| ALL-CAPS letter-spaced labels: PAID THIS MONTH, NAVIGATION, REVENUE | Sentence case: Paid this month, Navigation, Revenue |
| Everything bold or extra-bold | Regular and medium weights; size carries the hierarchy |
| Hierarchy made with gradient color | Primary vs. muted text color ("October" bright, "2026" muted) |
| Counts in pills | Right-aligned tabular figures |

- Use sentence case for labels and headings.
- Use two or three weights at most. Big numbers can be regular weight because their size already carries them.
- Use `font-variant-numeric: tabular-nums` for numbers that line up in columns.
- Pick the typeface for the subject. A neutral grotesk suits a dense data tool. A bakery, law firm, kids' app or music festival each deserve a different voice. A mono face for data labels is a choice for a specific product, not a garnish.
- Body text should be at least 16px, with line-height around 1.5 and lines of roughly 75 characters or fewer.

### 6. Imagery and data visualization

| Slop | Fixed |
|---|---|
| Beige clip-art credit card that matches nothing | Card rendered in the product's own palette, with its logomark and "•••• 4821" |
| Rounded-pill bars, one bar highlighted for no reason, no axis, ALL-CAPS day labels | Lines with a labeled y-axis (0–160k), month labels, a comparison series, and colors that match the plan dots already in the sidebar |

- Imagery must match the palette and the subject, or it goes. A real photo of the actual product or place beats any illustration. Avoid stock 3D blobs, isometric scenes and generic people-at-laptops.
- Charts exist so people can read values: label the axes, show units, include a comparison, and use colors that map to a legend the page already has. Highlight something only when the user should notice it, and label why.
- If the data is not real, a chart is decoration. Use a table, a single number, or an honest empty state instead.

### 7. Layout and motion

The AI landing-page template runs in a fixed order: pill badge ("✨ Introducing…") → giant centered gradient headline → two buttons → "Trusted by" logo strip → three identical feature cards with icons in tinted rounded squares → testimonials → three pricing tiers with "Most popular" → FAQ accordion → gradient call-to-action band → four-column footer. Dashboards get the bento-grid equivalent. Every card shares the same large radius and the same shadow, everything is centered, every section fades up on scroll, and every card scales on hover.

- Order sections by what this audience needs to make a decision, not by the template. Cut any section you cannot fill with real content.
- Let the content shape the structure. Seven features are not three cards, and a comparison belongs in a table.
- Left-align most text. Center only short, standalone moments.
- Scale corner radius with hierarchy: small on inputs and buttons, a little larger on cards. Do not make everything a pill.
- Motion should respond to what the user does (open, close, confirm). Allow at most one intentional entrance. Respect `prefers-reduced-motion`. No `hover:scale-105` on every card.

## Workflow: cleaning up (sweep until clean)

The user wants *zero* slop left anywhere in the project, not a single pass over the obvious page. So work through the whole project and keep looping until a full round finds nothing. One pass is never enough: fixes introduce new problems (a rewritten headline with an em dash, a new gray that breaks contrast), and the second look always finds things the first missed.

### 0. Inventory everything users can see

List every place slop can live before fixing anything, so nothing gets skipped:

- **Pages and routes.** Every page, including the 404, login, signup, empty dashboard, settings, legal, and email templates.
- **Components and layouts.** Header, footer, nav, cards, modals, toasts, loading and empty states.
- **Styles.** Global CSS, the Tailwind config and theme, CSS variables, component styles, inline styles.
- **Copy, wherever it lives.** Markup, JS/TS string constants, locale and i18n JSON, markdown and CMS content, `<title>` and meta tags, Open Graph text, alt text, aria-labels, form validation messages, error strings, `manifest.json` name.
- **Assets.** Logo, favicon, OG image, illustrations, icons (check for emoji and ✨ in images and SVGs too).

The scanner (Appendix C) walks the whole project and covers code and content files (HTML, CSS, JS/TS/JSX/TSX, Vue, Svelte, Astro, templates, MD/MDX, JSON, YAML). It skips build output, `node_modules`, lockfiles and configs. Its FILES section shows which files have findings and which are clean, so use it as the checklist.

### Tools

**Scanner.** The code is in Appendix C at the end of this file. Extract it to a scratch folder outside the user's project rather than retyping it. This skill's base directory is shown when the skill loads:

```bash
python3 -c "import sys;s=open(sys.argv[1],encoding='utf-8').read();a='\n# === BEGIN slop_scan.py ===\n';b='\n# === END slop_scan.py ===\n';open(sys.argv[2],'w',encoding='utf-8').write(s[s.index(a)+1:s.index(b)+1])" "<skill-base-dir>/SKILL.md" /tmp/slop_scan.py
python3 /tmp/slop_scan.py <project-root> --check
```

If you can't read this file from disk, write the Appendix C code block to `slop_scan.py` yourself. It needs only the Python standard library. Options: `--check` (exit 1 while high/medium findings or off-grid spacing remain), `--all` (show every hit), `--json`, `--min-severity high|medium|info`.

**Screenshots.** Use Playwright if it's available (`pip install playwright && playwright install chromium`):

```python
from pathlib import Path
from playwright.sync_api import sync_playwright
def shoot(target, out_prefix):  # target: local .html path or URL
    url = target if target.startswith("http") else Path(target).resolve().as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in (1440, 390):
            pg = b.new_page(viewport={"width": w, "height": 900}, reduced_motion="reduce")
            pg.goto(url, wait_until="networkidle"); pg.wait_for_timeout(500)
            pg.screenshot(path=f"{out_prefix}-{w}.png", full_page=True); pg.close()
        b.close()
```

Look at every screenshot you take, using whatever image-viewing tool you have. If you can't render pages at all, say so in the report: the visual passes were then checked from code only.

### The loop

Repeat rounds until one full round finds nothing:

1. **Scan the whole project.** Run `python3 /tmp/slop_scan.py <project-root> --check`. Exit code 1 means slop remains.
2. **Fix every finding** in pass order (1→7). Keep the product's content, data, routes and behavior. When copy is slop, rewrite it with the same meaning plus the missing specifics (baselines, units, dates), following Appendix B.
3. **Rescan** until `--check` exits 0. Don't silence findings to get there. The only allowed escape is a `slop-ok: <reason>` comment for things the brief or brand actually requires (for example `/* slop-ok: brand purple, per style guide */`). The scanner lists every exception with its reason in the EXCEPTIONS section.
4. **Screenshot every page** at 1440px and 390px (see Tools) and look at each one against all seven passes. The scanner can't see uneven rhythm, misalignment, a template layout, clip-art, decorative charts, or three cards that all look the same. Fix what you find.
5. **Read every string aloud.** Go through every piece of copy in the inventory, including the boring ones (validation errors, toasts, meta descriptions, alt text), and check it against Appendix B.
6. **Get a fresh-eyes review.** The fixer is the worst judge of their own fixes. If you can spawn a subagent, give one that hasn't seen your work the screenshots, the scanner output and Appendices A and B of this file, and ask it to list every remaining tell with its location. If you can't, re-read Appendices A and B top to bottom and check each item against the project as if you were seeing it for the first time.
7. **If anything changed in steps 2–6, start a new round at step 1.** The project is clean only when a round passes every step with no changes: the scanner exits 0, every page has been screenshotted and reviewed, every string has been read, and the fresh-eyes review comes back empty.

If you're still finding new slop after five rounds, stop and report what is left and why it keeps coming back. For example, a component library that injects gradients means the fix belongs in the theme config, not page by page.

### Report

Keep the report short:

- What changed, grouped by pass
- How many rounds it took, and the final scanner result
- Every `slop-ok` exception and its reason
- Placeholders the user needs to fill (real quotes, stats, photos, opening hours)
- Anything you couldn't check (pages behind a login you couldn't reach, images you couldn't inspect)

Only say the project is clean when every step of the last round passed with nothing found, and say exactly what that round covered. "No slop" means "the scanner, a screenshot review of all N pages, a full copy read-through and an independent review found nothing". It doesn't mean "I looked at the homepage".

## Workflow: building new

1. **Decide before coding.** Write a short plan covering: subject and audience; spacing base and scale; palette with roles (background, surface, border, text, muted, one accent, semantic colors); type (family per role, scale, weights); icon set; and two or three voice rules.
2. **Run the generic test.** Would you have written the same plan for a different product? Any part that would repeat is a default, so change it. Real choices come from the subject: its materials, vocabulary, audience and place.
3. **Build with real content.** Use specific product nouns and the real numbers if you were given them. Where you need placeholders, label them as placeholders. No buzzwords, no invented proof.
4. **Run the full sweep-until-clean loop on your own output** before handing it over: scan, screenshot, read every string, fresh-eyes review, and repeat until a round finds nothing. New work needs this as much as old work, because the defaults creep back in while you build.

## Don't swap one slop for another

The fixed EmberAI dashboard is near-black and neutral gray, with sans and mono type. That is right for a dense financial tool. But if every "clean" site turns near-black, gray and mono, that is just the next template. Other overcorrection looks that are fine when the subject calls for them, and slop when used as the "safe, not-AI" default:

- a cream background with a serif display face and a terracotta accent
- a brutalist newspaper layout with hairline rules and zero radius
- black with one acid-green or vermilion accent
- tracked-out labels and "→" tacked onto every link

A bakery site should feel like that bakery. A kids' science app should feel like neither a fintech tool nor a magazine.

## Final check

Before handing over, answer each of these:

- Can I name the spacing scale, and does every value use it?
- Does every color have a job I can name?
- Is there any gradient text, glow, glass blur, blob or ✨ left? If so, was it requested?
- Is there any emoji in the interface chrome?
- Is there any "!" in interface copy, or any word from the buzzword list?
- Read every line of text aloud. Any not-X-but-Y, slogan triads, rhetorical-question openers, em dashes, one-line closers or Title Case headings left? Would someone who works there actually say each line to a customer?
- Does every number have a unit and a baseline? Does every chart have readable axes?
- Is any stat, logo, testimonial or person invented?
- Would a stranger guess this was made for *this* subject and not for any subject?

For the full catalog of visual tells, including the Tailwind and CSS recipes that produce them, see Appendix A. For copy, see Appendix B.

---

## Appendix A: Catalog of visual tells

This is the long list of tells. Each entry gives the tell, why it reads as AI, and what to do instead. You don't need to read it top to bottom. Jump to the section you are fixing.

### Contents
1. Color and effects
2. Code recipes that produce slop (Tailwind and CSS)
3. Typography
4. Icons, emoji, badges
5. Layout patterns
6. Fake proof and placeholder content
7. Data visualization
8. Imagery
9. Motion and interaction
10. Dashboards and app UI
11. Overcorrection looks (the next generation of slop)

For copy (words, phrases and sentence patterns), see Appendix B.

---

### 1. Color and effects

| Tell | Why it reads as AI | Instead |
|---|---|---|
| Purple, violet or indigo as the accent with no brand reason (`#8b5cf6`, `#7c3aed`, `#6366f1`, `#a855f7`, `#9333ea`) | It is the Tailwind and shadcn demo accent, and models reach for it by default | Derive the accent from the subject or the brand. If there isn't one, pick it on purpose and say why |
| Purple→blue, purple→pink or indigo→cyan gradients on backgrounds, buttons or text | The most recognizable vibecoded signature | Solid colors. If a gradient is wanted, keep it subtle, same hue family, and in a single place |
| Gradient text on headlines | Decoration standing in for hierarchy | Solid text. Use size and weight for emphasis |
| Colored glow shadows (`shadow-purple-500/50`, `0 0 40px rgba(139,92,246,.5)`) | Neon effects borrowed from crypto and gaming templates | No glow. Use small neutral shadows, and only on floating layers |
| Glassmorphism: `backdrop-blur` with `bg-white/10` and `border-white/20` | The 2021 Dribbble trend that models still overuse | Solid surfaces with a 1px border |
| Blurred blobs or orbs behind the hero (`blur-3xl` circles) | Filler for empty space | Remove them. Fix the empty space with content or tighter layout |
| Dark slate background (`#0f172a`, `slate-900/950`) with an indigo accent | The Tailwind default dark theme, used unchanged | Tune the neutrals yourself |
| Dot or grid background patterns with a radial fade | Template hero decoration | Remove, unless the grid means something (a canvas tool, a map) |
| Rainbow or animated gradient borders, shimmer buttons | "Magic UI" component-library flair | Plain borders and plain buttons |
| Many accent colors with no meaning | Color picked per element, not per role | One accent plus semantic colors. A color should answer "what does this mean?" |
| Tinted icon tiles (`bg-blue-500/10` rounded square holding an icon), a different color per feature | Feature-card template | One neutral treatment, or no tile at all |

### 2. Code recipes that produce slop

If you see these strings in code, look closer.

```
bg-gradient-to-r from-purple-600 to-blue-600           → gradient button or background
bg-clip-text text-transparent                          → gradient text
backdrop-blur-xl bg-white/10 border border-white/20     → glass card
shadow-2xl shadow-purple-500/50                        → glow
absolute -z-10 h-96 w-96 rounded-full bg-purple-500 blur-3xl opacity-30   → blob
text-xs uppercase tracking-widest                      → tracked caps label
hover:scale-105 transition-all duration-300            → hover bounce on everything
rounded-2xl / rounded-3xl on every element             → pill-everything
animate-pulse on non-loading content                   → fake liveness
animate-bounce on an arrow or icon                     → attention-begging
```

CSS equivalents: `-webkit-background-clip: text`, `backdrop-filter: blur(...)`, `box-shadow: 0 0 30px <saturated color>`, `filter: blur(80px)`, `text-transform: uppercase; letter-spacing: .1em`, `transition: all .3s`.

The scanner in Appendix C detects most of these automatically.

### 3. Typography

| Tell | Instead |
|---|---|
| ALL-CAPS tracked labels and eyebrows above every heading | Sentence case. Add a label only if it tells the reader something the heading doesn't |
| Everything bold or extra-bold (`font-bold`, `font-extrabold`, `font-black` everywhere) | Two or three weights. Let size do the hierarchy |
| One word in the headline colored, italic or gradient ("Build *faster* with AI") | Write a headline that doesn't need a trick |
| Inter, Poppins, Space Grotesk, Plus Jakarta Sans, DM Sans, Outfit or Manrope by default | Choose for the subject. Inter is fine when it's a decision (a dense UI), not when it's the absence of one |
| Huge hero headline (`text-7xl` and up) with a short, empty line ("The future of work") | A specific sentence at a size that fits it |
| Centered paragraphs longer than two lines | Left-align. Keep lines to roughly 75 characters or fewer |
| Proportional numbers in tables and stat columns | `font-variant-numeric: tabular-nums`, right-aligned |
| Mono font sprinkled on labels as "tech flavor" | Use mono only where it does a job (code, IDs, aligned figures) and only as a choice for this product |

### 4. Icons, emoji, badges

| Tell | Instead |
|---|---|
| Emoji as nav or feature icons (🏠 📊 🚀 💡 ⚡ 🔒 📈) | One icon set, one stroke width, one size, `currentColor` |
| ✨ for "AI", "new" or "magic" | Describe the feature. No sparkles |
| 🚀 for launch, growth or "get started" | Words |
| 🔥 / 🎉 / 👋 / 😬 in interface copy | Remove them |
| Icons from mixed sets, or mixed filled and outline | Pick one style |
| "PRO", "NEW", "BETA" or "HOT" pills next to things | Only when it changes what the user does, and quiet even then |
| Notification dot or count on every nav item | Only where action is needed |
| Decorative controls (a bell with no panel, a settings gear that goes nowhere) | Remove, or swap for a control the screen actually needs |
| ✓ checkmark emoji lists in pricing | A plain list, or a consistent SVG check |

### 5. Layout patterns

**The landing-page template.** It is slop when every section is present no matter what the product is:

1. Pill badge above the headline: "✨ Introducing X" or "🎉 Now with AI"
2. Giant centered headline, often with a gradient word
3. Subheadline promising speed or ease
4. Two buttons: a gradient "Get started free →" and a ghost "Watch demo"
5. "Trusted by" strip of grayscale logos (often invented)
6. Three identical feature cards: icon tile, title, two-line description
7. "How it works" with 01 / 02 / 03 steps, even when it isn't a sequence
8. Testimonial cards with avatar, name, title and ★★★★★
9. Three pricing tiers, the middle one labeled "Most popular" and scaled up
10. FAQ accordion
11. Full-width gradient CTA band: "Ready to transform your workflow?"
12. Four-column footer full of links that go nowhere

Instead, decide what the visitor needs in order to act: usually what the product is, who it is for, proof it works (real), what it costs, and how to start. Build those in the form the content takes. Show the product itself: a real screenshot, a live demo, a real example output.

**Other layout tells**
- Bento grids of identical rounded tiles for content that isn't tile-shaped
- Everything centered
- Every section the same height, padding and structure
- Identical card radius and shadow on every element regardless of hierarchy
- Sections with an eyebrow, an H2 and one paragraph, repeated down the page
- Spacing values that aren't on any scale (13px, 22px, 37px, `p-[18px]`)

### 6. Fake proof and placeholder content

Never invent these. Use real ones, or mark the placeholder clearly and tell the user.

- Vanity stats: "10,000+ happy customers", "99.9% uptime", "10x faster", "4.9/5 rating", "$2M saved"
- Logo walls of companies that aren't customers (or "Acme", "Globex", "TechCorp")
- Testimonials from invented people: "Sarah Johnson, Product Manager at TechFlow", "Alex Chen, CTO"
- Star ratings, review counts, "#1 rated" badges, award badges
- Team pages with invented names and stock headshots
- Lorem ipsum left in shipping code

A clearly marked placeholder looks like `[Quote from a real customer]`, `[Logo]` or `[Add real stat]`, styled so it is obviously unfinished.

### 7. Data visualization

| Tell | Instead |
|---|---|
| Bars drawn as fully rounded pills | Square or slightly rounded bar ends; the bar's length carries the value |
| One bar highlighted in a different color for no reason | Highlight only what matters, and label why |
| No axis, no gridline values, no units | A labeled axis with round ticks and units |
| ALL-CAPS day labels (MON TUE WED) | Mon, Tue, Wed, or dates |
| Gradient fills under lines, glowing lines | A solid line; a light fill only if area matters |
| Series colors unrelated to the rest of the UI | Reuse the category colors used elsewhere on the page |
| Sparklines and mini-charts on every stat card | Only where the trend changes a decision |
| A chart built from invented data on a "real" page | A table, a number, or an empty state |
| A delta with no baseline (+12%) | +12% vs last month |

### 8. Imagery

- Clip-art that doesn't match the palette (the beige credit card)
- 3D blobs, abstract gradient meshes, isometric illustrations of people at laptops
- Stock photos of diverse teams high-fiving
- AI-generated hero images with a glossy, uncanny look
- Fake product screenshots made of gray bars

Instead: real photos of the actual product, place or people (or a clear placeholder). Use product screenshots that show real states. Render illustrations in the page's own palette, or leave them out.

### 9. Motion and interaction

- Fade-and-slide-up on every section as it scrolls into view
- `hover:scale-105` or a lift on every card, button and image
- `transition-all duration-300` everywhere
- Typewriter headline effects, rotating words, marquee logo strips
- Pulsing dots, bouncing arrows, animated gradient borders
- Number counters that tick up on load
- Parallax that has no purpose

Instead: motion responds to what the user does (opening, closing, confirming, reordering). Allow one orchestrated entrance at most. Keep transitions short (120–200ms) and limited to the properties that change. Respect `prefers-reduced-motion`. Focus states must be visible.

### 10. Dashboards and app UI

- Greeting header ("Good morning, Alex! ☀️") instead of what the screen shows
- Stat cards with an emoji, a giant bold number and "+12%!!"
- "PRO" or "AI" badge next to the logo
- Sidebar items with emoji, gradient active state and glowing count pills
- A search field with "Search anything..." and a glowing ⌘K chip
- Uneven nav row heights and misaligned icon columns
- A chart card with no axes
- Avatar plus name plus email crammed in the sidebar footer with a gradient ring
- Empty states with 🎉 or a cartoon and "Nothing here yet!"

Instead: a header that orients the user (page name, period, filters). Numbers with baselines. Quiet navigation with one icon family. Even rows. Real controls. Charts you can read. Empty states that say what to do next.

### 11. Overcorrection looks (the next generation of slop)

When told "don't look AI", models tend to fall back to one of these. Each is legitimate for some briefs. Each is slop when it shows up for every brief:

- **Neutral dark "Linear clone"**: near-black (#0B0B0B, #111), gray borders, Inter plus a mono for tiny labels
- **Warm editorial**: cream (#F4F1EA), high-contrast serif, terracotta accent (#D97757)
- **Brutalist broadsheet**: hairline rules, zero radius, dense newspaper columns, tracked caps
- **Black with one acid accent**: acid green or vermilion on black
- **Template chrome**: "A · B · C" meta strings, "WORD — fragment" labels, "→" on every link

The cure is the same as for the original slop: start from the subject. What does this place, product or audience look like, sound like, and care about?

---

## Appendix B: Writing website copy that sounds like a person

AI copy sounds the way it does because a model picks the phrase that fits the most products. "Unlock your potential" fits a gym, a bank and a note-taking app equally well, which is exactly why it says nothing. A person writing for one business picks words that only fit that business. Every rule below is a version of one move: replace the phrase that fits any site with the one that fits only this site.

### Contents
1. The test
2. Structural tells (strongest first)
3. Word-level tells
4. Rewrites by page section
5. Microcopy: buttons, errors, empty states, forms
6. Page titles, meta descriptions, alt text
7. Voice by kind of site
8. Rules for rewriting someone else's copy

---

### 1. The test

Read each line aloud and ask three questions:

1. **Could this line appear on a competitor's site unchanged?** If yes, it's filler. Add the specific detail or cut the line.
2. **Would someone who works there say this to a customer?** A baker doesn't say "Indulge in our curated selection of artisanal delights." They say "The sourdough comes out at 7."
3. **Does it add something the reader didn't already have?** Repeating the headline in the subhead, or closing a section with "That's the difference", adds nothing.

### 2. Structural tells (strongest first)

These survive word-swapping, so fix the sentence shape, not just the vocabulary.

**Not X but Y.** "It's not just a CRM, it's a growth engine." "More than a bakery: a family tradition." "Not another to-do app." The negative half rejects something nobody claimed, so the positive half sounds bigger without saying more. State the positive half directly and make it concrete.
- Before: "Murmur isn't just a recorder. It's your meeting memory."
- After: "Murmur records your calls and sends a summary with action items when the call ends."

**Slogan triads and fragment stacks.** "Fast. Simple. Powerful." "Plan. Track. Ship." "No setup. No credit card. No hassle." Three beats sound complete whether or not there are three ideas. Keep a list of three only when there really are three distinct things, and write it as a sentence.
- Before: "Bake. Share. Smile."
- After: "We bake everything here, every morning, in the oven my grandfather bought in 1987."

**Rhetorical question openers.** "Tired of messy notes?" "Ever wished your meetings could summarize themselves?" "What if your website could sell for you?" "Imagine a world where…". Answer the question instead of asking it.
- Before: "Tired of scrambling to remember what was decided?"
- After: "Every decision and owner from the call, in one list, two minutes after you hang up."

**"Whether you're X or Y".** "Whether you're a solo founder or a Fortune 500 team…" This tries to include everyone and ends up addressing no one. Name the real audience.

**One-line closers.** "That's the Murmur difference." "The choice is clear." "It's that simple." "Your future self will thank you." Cut them. End on the last concrete fact.

**Inflated significance.** "Redefining how teams collaborate." "A new era of baking." "The future of work is here." Say what concretely changes for one person.

**Mirror headlines.** "Work smarter, not harder." "Less busywork, more real work." These are clever-sounding and empty. Write what the product does instead.

**Em-dash rhythm.** "Your meetings — finally organized." "Built for teams — loved by individuals." Use a period, comma or colon. One dash on a whole page is fine. One per section is a tell.

**Bold labels on every list item.** "**Lightning fast:** …", "**Secure by default:** …". Use plain sentences, or a plain list if the items are scannable.

**Same-shape blocks.** Every feature blurb is exactly two sentences of about the same length, each starting with a verb. Vary them. Some features need one line, some need a paragraph.

**Title Case Everywhere.** "Everything You Need To Grow Your Business". Use sentence case for headings and buttons.

**Chatbot residue.** "Certainly! Here's…", "I hope this helps", "Feel free to reach out!". Remove it wherever it appears in site content.

### 3. Word-level tells

Replace or cut. The right replacement is almost always a plain verb or a specific fact.

| Word or phrase | Replacement |
|---|---|
| unlock, unleash, empower, enable | lets you + the action |
| elevate, enhance, transform, revolutionize, reimagine, redefine | what changes |
| seamless, effortless, frictionless, hassle-free | name the step that's gone |
| robust, powerful, cutting-edge, state-of-the-art, next-gen, innovative | cut, or name the capability |
| leverage, utilize | use |
| streamline, optimize | name the saving |
| delve, dive into, explore, embark, journey | read, see, start |
| crucial, pivotal, vital, key (adjective) | important, or cut |
| vibrant, rich, stunning, breathtaking | describe the thing itself |
| showcase, highlight, feature (verb) | show, has |
| testament, tapestry, landscape, realm | cut |
| curated, crafted, artisanal, bespoke, elevated | made, chosen, by hand, custom, or describe how |
| passion, passionate, love (as in "made with love") | what the care actually looks like |
| nestled in the heart of | is on [street], [neighborhood] |
| world-class, best-in-class, premium, top-notch | evidence, or cut |
| solution(s) | the actual product noun |
| AI-powered, powered by AI, smart, intelligent, magic | what it does |
| in seconds, instantly, lightning-fast | a measured time, or cut |
| we've got you covered, look no further, say goodbye to, say hello to | cut |

Exclamation marks: none in headlines, buttons, labels or errors. One on a whole page is acceptable for a genuinely warm personal brand.

### 4. Rewrites by page section

#### Hero

- Slop: "✨ Supercharge Your Meetings With AI-Powered Notes" / "Effortlessly capture, organize, and share insights — so you can focus on what truly matters." / [Get Started Free →] [Watch Demo]
- Human: "Meeting notes that write themselves" / "Murmur joins your Zoom or Meet call, records it, and emails everyone the decisions and to-dos when it ends. Free for 10 calls a month." / [Add Murmur to a meeting] [See a sample summary]

The human version names the platforms, the outcome, the timing and the price. Each is a fact a visitor can check.

#### Features

- Slop: "**Smart Summaries:** Our cutting-edge AI distills hours of conversation into actionable insights."
- Human: "Summaries are a page long, at most. Decisions first, then to-dos with names attached, then open questions."

#### About / story

- Slop: "Nestled in the heart of downtown, Rosewood Bakery is more than a bakery — it's a celebration of tradition, community, and the timeless art of baking. Our passionate team crafts each item with love."
- Human: "Rosewood is a family bakery on Elm Street. Maria opened it in 2009 with her mother's recipes for bread and pastries. We still bake everything on site, starting at 4 a.m." (Every fact here must come from the user. If you don't have it, write `[year opened]`, `[founder's name]` and ask.)

#### Social proof

- Slop: "Trusted by 10,000+ teams worldwide" + six grayscale logos + "Sarah Johnson, VP Product at TechFlow: 'This tool completely transformed our workflow!' ★★★★★"
- Human: real numbers and real quotes from the user, attributed with permission. Otherwise leave the section out, or use visibly marked placeholders: `[Quote from a real customer]`, `[Customer name, role]`.

#### Pricing

- Slop: "Starter / Pro (Most Popular!) / Enterprise", "Everything you need to get started", "Unlock advanced features".
- Human: name tiers by who they're for or what they include. Describe each in terms of the limit that matters ("Up to 10 calls a month", "Unlimited calls, 5 seats"). Say the real price and what happens when you go over.

#### Final call to action

- Slop: "Ready to transform your workflow? Join thousands of happy customers today!"
- Human: "Try it on your next meeting. Free for 10 calls, no card needed." (Only claim "no card needed" if it's true.)

### 5. Microcopy: buttons, errors, empty states, forms

- **Buttons** say what happens: "Save changes", "Book a table for 4", "Download the menu (PDF)". Keep the same verb through the flow: a "Publish" button leads to a "Published" message.
- **Errors** say what went wrong and how to fix it, in the interface's voice, with no apology theater. "Card declined. Try another card or contact your bank." Not "Oops! Something went wrong 😕".
- **Empty states** give the next action. "No invoices yet. Create one, or import from CSV." Not "Nothing here yet! 🎉".
- **Form labels** are short nouns ("Email", "Company"). Put helper text under the field only when it prevents a mistake.
- **Confirmation** says what happened and what happens next: "Order placed. We'll text you when it's ready (usually 20 minutes)."
- **Loading** says what's loading if it takes long: "Generating summary… about 30 seconds for a 1-hour call."

### 6. Page titles, meta descriptions, alt text

- Title: "Rosewood Bakery: bread and pastries on Elm Street", not "Rosewood Bakery | Artisanal Baked Goods Crafted With Love".
- Meta description: one or two factual sentences a person would want to see in search results.
- Alt text: describe what's in the image, briefly ("Loaves of sourdough cooling on a rack"). Not "Beautiful vibrant image showcasing our delicious products", and never "image of".

### 7. Voice by kind of site

The rules above remove AI defaults. The voice comes from the subject:

- **Local business** (bakery, salon, garage): first person plural, concrete details (hours, street, prices, names), warm but plain.
- **Developer tool**: precise, technical nouns, code snippets that actually run, no hype. Developers distrust adjectives.
- **B2B software**: the job, the person doing it, the time or money saved (only if known), how it fits existing tools.
- **Professional services** (law, accounting, medical): calm, exact, credentials stated plainly, no "passionate about".
- **Personal site or portfolio**: first person singular, opinions allowed, real projects with real outcomes.
- **Non-profit**: what you do, where, for whom, with what result. Specific numbers if you have them, never invented.
- **Playful consumer brand**: personality is welcome, but it should be *this* brand's joke, not generic enthusiasm. Wit comes from specifics too.

If the user gives a writing sample, a brand voice guide or existing copy they like, match it. That overrides the defaults here, including the rule on dashes.

### 8. Rules for rewriting someone else's copy

- Keep every real fact, number, name, claim and promise. Remove only the dressing.
- Never add a fact, number, name, quote, credential or customer you weren't given. If a line needs a specific to work, use a marked placeholder and list the placeholders for the user at the end.
- Balance placeholders against finished copy. Write true sentences from what you were given ("Sourdough and croissants from 7am, Tuesday to Sunday") and use a placeholder only for a fact you'd otherwise have to invent (address, prices, founding story, photos). A page that's half yellow boxes isn't finished either. Group the placeholders where the owner will find them, and keep each one short.
- Keep legal text, prices and policy wording exact unless asked to change them.
- If the original has a genuine voice (odd details, jokes, opinions), keep it. Remove the AI patterns, not the personality.
- After rewriting, re-read the whole page in one go. Sections written one at a time drift toward the same shape, so vary them.

---

## Appendix C: Scanner source (slop_scan.py)

Extract this block with the command under "Tools" above. It needs only the Python standard library.

```python
# === BEGIN slop_scan.py ===
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
# === END slop_scan.py ===
```
