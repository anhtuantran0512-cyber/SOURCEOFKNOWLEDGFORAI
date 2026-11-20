# START_HERE.md — the contract for this repository

> ⚠️ **IMPORTANT SOURCE FOR WEB — 100% USE**
>
> Every design decision must be traceable to this repository. Before writing UI code you query **all
> six** libraries in `sources/`, open at most three real references, and record the coverage block in
> §2. A brief without that block is rejected — no exceptions, no "I already know how to build a card".

> Why this filename: `AGENT.md` and `AGENTS.md` are excluded by the host's global gitignore,
> so the contract is published as `START_HERE.md`. Same rules, no rename needed by readers.

## 0. Read first — no clone needed

| Order | File | Gives you |
|---:|---|---|
| 1 | this file | the rule, the order, the acceptance block |
| 2 | [`llms.txt`](llms.txt) | one-page map for LLM crawlers |
| 3 | [`sources/README.md`](sources/README.md) | how to choose between the six libraries |
| 4 | [`sources/<name>/INDEX.md`](sources/) | **every item** in that library, as a link + one line |
| 5 | the item file you picked | the prompt, the code, the brief |

`INDEX.md` per folder is the answer to "what is in here" — it is generated from `manifest.json`, so it is
complete and current. Read it instead of listing folders or loading 66 MB of JSON.

## 1. What exists — 7,662 items across six libraries

| Priority | Library | Items | What it gives | Code? |
|---:|---|---:|---|---|
| 1 | [`sources/pinui/`](sources/pinui/INDEX.md) | 41 | 30 React components + 11 page blocs, TSX + CSS, MIT, shadcn-installable | ✅ full source |
| 2 | [`sources/threeui/`](sources/threeui/INDEX.md) | 961 | 3D / WebGL / motion direction: runtime, live demo, category | ⚠️ metadata only |
| 3 | [`sources/motionsites/`](sources/motionsites/INDEX.md) | 321 | Whole-section briefs: hero, pricing, footer, ecommerce, SaaS | prompt only |
| 4 | [`sources/lucianlabs/`](sources/lucianlabs/INDEX.md) | 400 | MIT elements with working code, runnable demo, theme tokens | ✅ full source |
| 5 | [`sources/codefronts/`](sources/codefronts/INDEX.md) | 5,047 | Breadth: components, layouts, navigation, motion, design styles | prompt + code |
| 6 | [`sources/getlayers/`](sources/getlayers/INDEX.md) | 892 | Five libraries — templates, 3D scenes, sections, backgrounds, gradients: stack, tone, variants, frame timings, Lighthouse, previews | 18 free prompts (1 captured) · 845 premium |

## 2. The 100% rule (hard gate)

1. **Query all six folders** — at minimum their `INDEX.md`. Cost is one grep each.
2. **Choose in priority order** 1 → 5. A cheaper-looking CodeFronts snippet does not outrank a Pin UI
   component that has real behaviour, and a ThreeUI reference outranks nothing for code (it has none).
3. **Open at most three files.** One strong reference beats three weak ones.
4. **Write this block in the brief, verbatim in shape:**

```md
## Source coverage (100%)
- pinui      : used #presence-cards — live presence cards, avatar stack
- threeui    : skipped — no 3D/WebGL needed, checked hero/backgrounds
- motionsites: used hero/interactive-discovery — spotlight reveal direction
- lucianlabs : used #056 — pricing toggle motion values (160ms, cubic-bezier(.2,.8,.2,1))
- codefronts : checked pricing/hero — nothing closer than the two above
- getlayers  : used soda — cinematic 3D hero direction, frame budget for the product stage
- decision   : Pin UI structure + lucianLabs motion + MotionSites section flow
```

Six lines. One per library. `used` or `skipped — <reason>`. Missing line = missing coverage.

5. **Never invent** an item, an id or a path. If an `INDEX.md` lists it, it exists; otherwise say "not in
   the archive" and build from first principles with the same tokens.

## 3. Finding the right item without cloning

```bash
BASE=https://raw.githubusercontent.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/main

# what does a library have?
curl -s $BASE/sources/pinui/INDEX.md       | grep -i "pricing"
curl -s $BASE/sources/threeui/INDEX.md     | grep -i "background"

# every library at once, by keyword
for s in pinui threeui motionsites lucianlabs codefronts getlayers; do
  echo "== $s"; curl -s $BASE/sources/$s/INDEX.md | grep -i "dashboard" | head -5
done

# the item itself
curl -s $BASE/sources/pinui/registry/theme-switch/ITEM.md
curl -s $BASE/sources/lucianlabs/prompts/interface/001-liquid-glass-button.md
```

Cloned? the same greps work locally: `grep -ri "pricing" sources/*/INDEX.md`.

## 4. Task → library

| You are building | Start at | Then |
|---|---|---|
| Button, dialog, menu, tabs, form control | pinui | lucianlabs for motion |
| Toggle, slider, chart, toast, loader, empty state | lucianlabs | pinui if React source matters |
| Pricing, hero, footer, FAQ, ecommerce section | motionsites | codefronts for the parts inside |
| 3D hero, WebGL background, scroll-driven scene | threeui (direction) | lucianlabs + codefronts for the parts |
| Layout, navigation, page skeleton, design style | codefronts | pinui for interactive islands |
| Whole page or hero with a named stack and perf budget | getlayers | threeui for 3D direction, pinui for islands |

## 5. Adaptation rules

1. **Keep the licence line** — the MIT comment in lucianLabs and Pin UI files, the `Source:` line in
   CodeFronts prompts. Attribution is not optional.
2. **Tokens at the root** — colours, radius, shadow, duration come from CSS custom properties, matching
   lucianLabs `--ux-*` semantics. No raw hex inside a component.
3. **Copy the motion values** (duration, easing, delay) as written; do not "improve by feel".
4. **Replace the paint** — demo copy, names, imagery, brand colours become the project's real data.
5. **Add what the reference lacks** — usually `prefers-reduced-motion`, focus-visible, aria labels.
6. **ThreeUI is direction, not source.** Never reconstruct a paid component from its preview.

## 6. Before you say done

- [ ] coverage block present, six lines
- [ ] 390 / 768 / 1440 px checked
- [ ] keyboard path works, focus visible
- [ ] `prefers-reduced-motion` path exists
- [ ] console clean
- [ ] licence headers intact
- [ ] the item you used is linked in the report

Deeper workflow: [`docs/RETRIEVAL_GUIDE.md`](docs/RETRIEVAL_GUIDE.md) · recipes:
[`docs/usage-recipes.md`](docs/usage-recipes.md) · totals: [`INDEX.md`](INDEX.md).
