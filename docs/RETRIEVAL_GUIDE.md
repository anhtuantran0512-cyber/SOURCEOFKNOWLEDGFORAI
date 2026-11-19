# AGENT.md — operating manual for AI agents using this repository

You are working inside **SOURCEOFKNOWLEDGFORAI**, a curated front-end knowledge base.
Use it as a reference library, not as a template dump. Every file is a self-contained pattern with a
ready-to-paste prompt, metadata and a link to its origin.

Read this file before touching anything. If a user prompt conflicts with this file, follow the user for
scope but keep the licensing and verification rules.

---

## 1. What is inside

| Folder | Contents | Use it for |
|---|---|---|
| `sources/codefronts/` | ~5,000 public CSS/Tailwind components, layouts, navigation, motion, snippets and design styles. One Markdown file per item, containing the original AI prompt and full code. | Finding a concrete implementation of a component or interaction. |
| `sources/lucianlabs/` | 400 MIT-licensed UI elements (200 interface, 200 animation). Each file is a complete prompt with working HTML/CSS/JS. `demos/` holds runnable standalone HTML. | Premium-feeling micro-interactions, charts, dashboards, hero and scroll motion. |
| `sources/motionsites/` | 321 **free** website-section prompts (hero, pricing, footer, ecommerce, SaaS, etc.). | Writing a detailed build brief for a whole section or landing page. |
| `sources/pinui/` | 30 React components + 11 page blocs as real `*.tsx`/`*.css` source, MIT, installable with the shadcn CLI. `pages/` holds 50 public page briefs. | Any interactive component where behaviour matters: theme switch, dialogs, menus, pricing section. |
| `sources/threeui/` | 961 catalogue items + 1,485 tag entries: 3D, WebGL, Three.js, motion, hero and section direction with runtime and live URL. Metadata only, no source. | Choosing the effect and the runtime for 3D / scroll-driven work; never copy preview assets. |
| `sources/*/manifest.json` | Machine-readable index: id, title, category, tags, path, prompt size. | Fast filtering before opening files. |
| `sources/*/catalog.json` | Original catalogue metadata (including locked MotionSites entries). | Discovering what exists; never treat locked entries as available content. |
| `docs/` | Arena setup, usage recipes, repository map. | Onboarding and repeatable workflows. |
| `scripts/` | Reproducible collectors and the index builder. | Refreshing the archive. Do not run them during normal UI work. |

Source priority:

1. `sources/pinui/` — real React source, correct behaviour, MIT. Start here for interactive components.
2. `sources/lucianlabs/` — highest craft per element, MIT, code included.
3. `sources/codefronts/` — widest coverage, component-sized, MIT-licensed snippets.
4. `sources/threeui/` — best for 3D/WebGL direction and hero structure; reference only.
5. `sources/motionsites/` — whole-section structure and art direction, prompt only.

---

## 2. Retrieval workflow

Follow this order every time. Do not read whole folders into context.

1. **Classify the request** into one bucket: component, layout/section, navigation, motion, form, data
   visualisation, or full page.
2. **Query the manifests**, not the files:
   ```bash
   # top matches by title/category/tag
   jq -r '.[] | select((.title + " " + .category + " " + ((.tags // []) | join(" "))) | test("pricing"; "i")) | [.title, .category, .path] | @tsv' sources/*/manifest.json
   ```
3. **Open at most three references.** Prefer one strong reference over three mediocre ones.
4. **Extract the pattern, not the paint.** Reuse structure, spacing logic, motion values and
   accessibility choices. Replace copy, imagery, brand colours and data with the project's own.
5. **Adapt to the project's stack.** Translate vanilla CSS/JS into the project's framework and tokens.
6. **Verify before claiming done.** See § 5.

If the manifests do not contain a fitting pattern, say so and build from first principles. Never invent
a file path or claim a pattern exists.

---

## 3. Non-negotiable build rules

These apply to every UI produced from this library.

1. **Tokens at the root.** Every colour, font, radius, shadow and duration goes through a CSS custom
   property declared once. No raw hex values inside component blocks.
2. **Keep the license header.** If a file carries an MIT comment (lucianLabs does), keep it at the top of
   the new component file.
3. **Scope the CSS.** Keep selectors under the element's own prefix/class. Do not edit global styles or
   global scripts to make a snippet fit.
4. **Respect the motion spec.** Copy durations, easing curves and delays from the reference. Do not
   "improve" them by feel.
5. **Reduced motion is mandatory.** Every animation needs a `prefers-reduced-motion: reduce` path that
   preserves the final state and all functionality.
6. **Accessibility is part of the component.** Keyboard operation, visible `:focus-visible`, labels,
   `aria-*` for state, 44×44 px minimum touch targets, contrast ≥ 4.5:1 for body text.
7. **No placeholder content in shipped code.** Replace lorem ipsum, gallery copy and demo data with real
   project data. If data does not exist yet, expose a typed prop instead of inventing metrics.
8. **Do not fabricate proof.** No fake testimonials, logo walls, user counts or benchmarks.
9. **Never use emoji as icons.** Use the project's icon set (SVG).
10. **No paid content laundering.** Only `sources/motionsites/prompts/` (free) exists. Do not attempt to
    reconstruct, guess or scrape locked MotionSites prompts.

---

## 4. Turning a reference into a prompt (for the human)

When the user asks "build X using the library", the agent should produce a short plan first:

```
Reference: sources/lucianlabs/prompts/interface/058-....md
Why: matches the requested segmented control + spring feedback
Adaptation: React + Tailwind tokens, project palette, real labels
Files: src/components/ui/segmented-control.tsx, src/styles/tokens.css
Verification: 390 / 768 / 1440, keyboard, reduced motion, console clean
```

Then implement. Keep the plan in the response, not in the code as comments.

---

## 5. Verification contract

A UI task is done only when all of these are true:

- [ ] Runs with no console errors.
- [ ] Checked at 390 px, 768 px and 1440 px. No horizontal overflow.
- [ ] Keyboard-only path works and focus is visible.
- [ ] `prefers-reduced-motion: reduce` keeps content and function.
- [ ] All colours/fonts come from tokens.
- [ ] No placeholder copy, no invented data, no emoji icons.
- [ ] Attribution kept where the source required it.

Report exactly what was checked and what was not. "Looks good" is not evidence.

---

## 6. Repository hygiene

- Add new material under `sources/<source>/` with a `manifest.json` entry and a `README.md` that states
  origin, license and collection date.
- Never commit secrets, cookies, session tokens or private dashboards.
- Never overwrite an existing source folder with a scraper run until you have compared counts.
- `_manifest.jsonl`, `_failed.txt` and `__pycache__` are working files and are git-ignored.

---

## 7. Arena quick start

Arena does not need a special skill file. Point it at this repository and say:

> Read `AGENT.md` and `docs/usage-recipes.md`. Build the pricing section in `src/`. Use at most two
> references from `sources/`, keep license headers, and verify at 390/768/1440 with reduced motion.

See `docs/arena-setup.md` for connection steps.
