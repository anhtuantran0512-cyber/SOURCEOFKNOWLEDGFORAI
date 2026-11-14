# lucianLabs UX/UI Prompt archive

400 MIT-licensed UI elements from <https://lucianlabs.dev/en/uxui-prompt/>. Every element is stored as a
complete, ready-to-paste prompt that includes the working code, the site's application guide and the
license line.

- Elements: **400** (200 interface, 200 animation)
- Prompts: `prompts/<collection>/<id>-<slug>.md`
- Runnable demos: `demos/<collection>/<id>-<slug>.html` (open directly in a browser)
- Theme tokens: [`tokens.css`](tokens.css)
- License: MIT (c) 2026 Seokwoooo — kept in every file
- Manifest: [`manifest.json`](manifest.json)

## Categories

- Layout, Schedule & Design — 25
- Document & Data Editing — 25
- Analytics & Data — 25
- Workflow & Systems — 25
- Sections & Content — 21
- App Screens — 20
- Data Motion — 18
- Commerce & Pricing — 18
- Hero & Backgrounds — 18
- Text Motion — 17
- Scroll Motion — 17
- Navigation — 16
- Site Builder Tools — 16
- Forms & Input — 15
- Cards & Content — 13
- Buttons — 12
- Toggles & Pickers — 12
- Inputs & Search — 12
- Menus & Tabs — 12
- Alerts & Feedback — 9
- Loading & Progress — 9
- Promos & Rewards — 9
- Sign-in & Sign-up — 8
- Cursor & Hover — 8
- Widgets & Charts — 7
- Social Proof — 7
- Empty & Error States — 6

## Use

```bash
jq -r '.[] | select((.title + " " + .category + " " + (.tags | join(" "))) | test("chart|dashboard"; "i")) | [.id, .title, .prompt_path] | @tsv' \
  sources/lucianlabs/manifest.json
```

Read the prompt file. The `[Element]` block and the code are the source of truth; do not rewrite the
motion values. Keep the license comment when you port the code.
