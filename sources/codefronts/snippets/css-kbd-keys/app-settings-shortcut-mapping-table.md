---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/app-settings-shortcut-mapping-table/"
title: "App Settings Shortcut Mapping Table"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "A real settings surface built as a semantic table, because shortcut mappings are tabular data — action, binding, scope, source — and a flex list throws all…"
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: App Settings Shortcut Mapping Table
Source: https://codefronts.com/snippets/css-kbd-keys/app-settings-shortcut-mapping-table/

A real settings surface built as a semantic table, because shortcut mappings are tabular data — action, binding, scope, source — and a flex list throws all of that structure away. Includes a reset affordance per customised row and one row in a conflict state, flagged with an icon and a word rather than a red background alone.
## HTML
```html
<div class="kbd-14">
  <div class="kbd-14__stage">
    <section class="kbd-14__panel">
      <header class="kbd-14__head">
        <h2 class="kbd-14__title">Keyboard</h2>
        <p class="kbd-14__sub">Settings · Shortcuts</p>
      </header>
      <div class="kbd-14__scroll">
        <table class="kbd-14__table">
          <caption class="kbd-14__caption">Shortcut bindings for Atlas editor. One binding conflicts and is flagged in the Status column.</caption>
          <thead>
            <tr>
              <th class="kbd-14__th" scope="col">Action</th>
              <th class="kbd-14__th" scope="col">Binding</th>
              <th class="kbd-14__th" scope="col">Scope</th>
              <th class="kbd-14__th kbd-14__th--status" scope="col">Status</th>
              <th class="kbd-14__th kbd-14__th--action" scope="col"><span class="kbd-14__vh">Reset</span></th>
            </tr>
          </thead>
          <tbody>
            <tr class="kbd-14__tr">
              <th class="kbd-14__rowh" scope="row">Save file</th>
              <td class="kbd-14__td"><kbd class="kbd-14__combo"><kbd class="kbd-14__key">Ctrl</kbd><span class="kbd-14__sep" aria-hidden="true">+</span><kbd class="kbd-14__key">S</kbd></kbd></td>
              <td class="kbd-14__td">Global</td>
              <td class="kbd-14__td"><span class="kbd-14__state">Default</span></td>
              <td class="kbd-14__td kbd-14__td--action"></td>
            </tr>
            <tr class="kbd-14__tr">
              <th class="kbd-14__rowh" scope="row">Toggle sidebar</th>
              <td class="kbd-14__td"><kbd class="kbd-14__combo"><kbd class="kbd-14__key">Ctrl</kbd><span class="kbd-14__sep" aria-hidden="true">+</span><kbd class="kbd-14__key">Shift</kbd><span class="kbd-14__sep" aria-hidden="true">+</span><kbd class="kbd-14__key">E</kbd></kbd></td>
              <td class="kbd-14__td">Workbench</td>
              <td class="kbd-14__td"><span class="kbd-14__state kbd-14__state--custom">Customised</span></td>
              <td class="kbd-14__td kbd-14__td--action"><button class="kbd-14__reset" type="button">Reset<span class="kbd-14__vh"> toggle sidebar to default</span></button></td>
            </tr>
            <tr class="kbd-14__tr kbd-14__tr--conflict">
              <th class="kbd-14__rowh" scope="row">Split editor right</th>
              <td class="kbd-14__td"><kbd class="kbd-14__combo"><kbd class="kbd-14__key">Ctrl</kbd><span class="kbd-14__sep" aria-hidden="true">+</span><kbd class="kbd-14__key">K</kbd></kbd></td>
              <td class="kbd-14__td">Editor</td>
              <td class="kbd-14__td">
                <span class="kbd-14__state kbd-14__state--conflict">
                  <svg class="kbd-14__warn" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4 L21 19 L3 19 Z"/><path d="M12 10 L12 14"/><path d="M12 16.4 L12 16.5"/></svg>
                  Conflict
                </span>
                <span class="kbd-14__conflictnote">also bound to Open command bar</span>
              </td>
              <td class="kbd-14__td kbd-14__td--action"><button class="kbd-14__reset" type="button">Reset<span class="kbd-14__vh"> split editor right to default</span></button></td>
            </tr>
            <tr class="kbd-14__tr">
              <th class="kbd-14__rowh" scope="row">Go to file</th>
              <td class="kbd-14__td"><kbd class="kbd-14__combo"><kbd class="kbd-14__key">Ctrl</kbd><span class="kbd-14__sep" aria-hidden="true">+</span><kbd class="kbd-14__key">P</kbd></kbd></td>
              <td class="kbd-14__td">Global</td>
              <td class="kbd-14__td"><span class="kbd-14__state">Default</span></td>
              <td class="kbd-14__td kbd-14__td--action"></td>
            </tr>
            <tr class="kbd-14__tr">
              <th class="kbd-14__rowh" scope="row">Rename symbol</th>
              <td class="kbd-14__td"><kbd class="kbd-14__combo"><kbd class="kbd-14__key">F2</kbd></kbd></td>
              <td class="kbd-14__td">Editor</td>
              <td class="kbd-14__td"><span class="kbd-14__state">Default</span></td>
              <td class="kbd-14__td kbd-14__td--action"></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="kbd-14__foot">Reviewed by Priya Sharma · 6 of 214 bindings customised</p>
    </section>
    <div class="kbd-14__theme">
      <input class="kbd-14__themebox" type="checkbox" id="kbd-14-theme">
      <label class="kbd-14__themelabel" for="kbd-14-theme">
        <span class="kbd-14__themedot" aria-hidden="true"></span>
        <span class="kbd-14__themebase">Light</span><span class="kbd-14__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #f2ede4;
  --panel: #fbf8f2;
  --ink: #2e2721;
  --muted: #857767;
  --rule: #e0d7c9;
  --zebra: #f6f2ea;
  --cap: #ffffff;
  --cap-border: #cfc3ae;
  --cap-ink: #3a3128;
  --accent: #7a5c2e;
  --warn: #a5551b;
  --warn-bg: #fbeedc;
  --font-key: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 16px;
}

.kbd-14__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-14__panel {
  inline-size: 100%;
  max-inline-size: 42rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 22px 20px 18px;
}

.kbd-14__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 16px;
}

.kbd-14__title {
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -0.01em;
  min-inline-size: 0;
}

.kbd-14__sub {
  margin: 0;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.kbd-14__scroll {
  overflow-x: auto;
  border: 1px solid var(--rule);
  border-radius: 4px;
  -webkit-overflow-scrolling: touch;
}

.kbd-14__table {
  inline-size: 100%;
  min-inline-size: 34rem;
  border-collapse: collapse;
  text-align: start;
}

.kbd-14__caption {
  caption-side: bottom;
  padding: 10px 12px;
  font-size: 11px;
  line-height: 1.5;
  color: var(--muted);
  text-align: start;
  text-wrap: pretty;
}

.kbd-14__th {
  padding: 9px 12px;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: start;
  background: var(--zebra);
  border-bottom: 1px solid var(--rule);
  white-space: nowrap;
}

.kbd-14__th--action {
  inline-size: 5.5rem;
}

.kbd-14__tr:nth-child(even) {
  background: var(--zebra);
}

.kbd-14__tr--conflict {
  background: var(--warn-bg);
}

.kbd-14__rowh,
.kbd-14__td {
  padding: 11px 12px;
  font-size: 13px;
  font-weight: 400;
  text-align: start;
  vertical-align: middle;
  border-bottom: 1px solid var(--rule);
  min-inline-size: 0;
}

.kbd-14__rowh {
  font-weight: 600;
  white-space: nowrap;
}

.kbd-14__td--action {
  text-align: end;
}

.kbd-14__combo {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: inherit;
  flex-wrap: wrap;
  min-inline-size: 0;
}

.kbd-14__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 24px;
  padding: 4px 7px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 3px;
  box-shadow: 0 1px 0 var(--cap-border);
  white-space: nowrap;
}

.kbd-14__sep {
  font-size: 10.5px;
  color: var(--muted);
  user-select: none;
}

.kbd-14__state {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  white-space: nowrap;
}

.kbd-14__state--custom {
  color: var(--accent);
}

.kbd-14__state--conflict {
  color: var(--warn);
}

.kbd-14__warn {
  inline-size: 14px;
  block-size: 14px;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.kbd-14__conflictnote {
  display: block;
  margin-top: 3px;
  font-size: 11px;
  line-height: 1.4;
  color: var(--warn);
  text-transform: none;
  letter-spacing: 0;
  text-wrap: pretty;
}

.kbd-14__reset {
  min-inline-size: 44px;
  min-block-size: 44px;
  padding: 0 12px;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--accent);
  background: transparent;
  border: 1px solid var(--cap-border);
  border-radius: 4px;
  cursor: pointer;
  white-space: nowrap;
  transition: background 140ms ease;
}

.kbd-14__reset:hover {
  background: rgba(122, 92, 46, 0.1);
}

.kbd-14__reset:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.kbd-14__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
  padding: 0;
  margin: -1px;
}

.kbd-14__foot {
  margin: 14px 0 0;
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.02em;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-14__reset {
    transition: none;
  }
}

.kbd-14[data-theme="dark"],
[data-theme="dark"] .kbd-14 {
  --page: #1a1611;
  --panel: #221d17;
  --ink: #f1e9dd;
  --muted: #a6947e;
  --rule: #3a3227;
  --zebra: #282218;
  --cap: #302921;
  --cap-border: #514535;
  --cap-ink: #f4ece0;
  --accent: #d7a86a;
  --warn: #f0a35e;
  --warn-bg: #35240f;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-14__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-14__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-14__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-14__themelabel {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-block-size: 44px;
  padding: 0 16px;
  box-sizing: border-box;
  font-family: var(--font-key, ui-sans-serif, system-ui, sans-serif);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  line-height: 1;
  color: var(--ink, var(--cap-ink, currentColor));
  background: transparent;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  user-select: none;
}

.kbd-14__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-14__themebox:focus-visible + .kbd-14__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-14__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-14__themeflip {
  display: none;
}

.kbd-14:has(.kbd-14__themebox:checked) {
  --page: #1a1611;
  --panel: #221d17;
  --ink: #f1e9dd;
  --muted: #a6947e;
  --rule: #3a3227;
  --zebra: #282218;
  --cap: #302921;
  --cap-border: #514535;
  --cap-ink: #f4ece0;
  --accent: #d7a86a;
  --warn: #f0a35e;
  --warn-bg: #35240f;
}

.kbd-14:has(.kbd-14__themebox:checked) .kbd-14__themebase {
  display: none;
}

.kbd-14:has(.kbd-14__themebox:checked) .kbd-14__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-14:not(:has(.kbd-14__themebox:checked)) {
    --page: #1a1611;
    --panel: #221d17;
    --ink: #f1e9dd;
    --muted: #a6947e;
    --rule: #3a3227;
    --zebra: #282218;
    --cap: #302921;
    --cap-border: #514535;
    --cap-ink: #f4ece0;
    --accent: #d7a86a;
    --warn: #f0a35e;
    --warn-bg: #35240f;
  }

  .kbd-14:has(.kbd-14__themebox:checked) {
    --page: #f2ede4;
    --panel: #fbf8f2;
    --ink: #2e2721;
    --muted: #857767;
    --rule: #e0d7c9;
    --zebra: #f6f2ea;
    --cap: #ffffff;
    --cap-border: #cfc3ae;
    --cap-ink: #3a3128;
    --accent: #7a5c2e;
    --warn: #a5551b;
    --warn-bg: #fbeedc;
  }

  .kbd-14:not(:has(.kbd-14__themebox:checked)) .kbd-14__themebase {
    display: none;
  }

  .kbd-14:not(:has(.kbd-14__themebox:checked)) .kbd-14__themeflip {
    display: inline;
  }

  .kbd-14:has(.kbd-14__themebox:checked) .kbd-14__themebase {
    display: inline;
  }

  .kbd-14:has(.kbd-14__themebox:checked) .kbd-14__themeflip {
    display: none;
  }
}
/* Responsive guard (Phase A): the shortcut table carries a deliberate
   34rem min-inline-size and lives in a .kbd-14__scroll wrapper, which is
   correct — but the wrapper sits in a place-items:center grid item, and a
   centred grid item is sized to max-content, so the wrapper inherited the
   table's width instead of the panel's. Constrain the chain and clip at
   the root; the table still scrolls inside its wrapper below 768px. */

.kbd-14 {
  overflow-x: hidden;
}

.kbd-14__stage {
  max-inline-size: 100%;
  min-inline-size: 0;
}

.kbd-14__panel {
  max-inline-size: min(42rem, 100%);
}

.kbd-14__scroll {
  max-inline-size: 100%;
  min-inline-size: 0;
}
```
