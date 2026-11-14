---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/keyboard-shortcut-cheatsheet-grid/"
title: "Keyboard Shortcut Cheatsheet Grid"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "A grouped shortcut reference where the key column lines up across every section regardless of how long the labels are."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Shortcut Cheatsheet Grid
Source: https://codefronts.com/snippets/css-kbd-keys/keyboard-shortcut-cheatsheet-grid/

A grouped shortcut reference where the key column lines up across every section regardless of how long the labels are. One shared grid track does the alignment, so Navigation, Editing and View sit on the same measure instead of each group finding its own. It is a page section, not an overlay — two columns on desktop collapsing to one on narrow screens.
## HTML
```html
<div class="kbd-12">
  <div class="kbd-12__stage">
    <section class="kbd-12__sheet">
      <header class="kbd-12__head">
        <h2 class="kbd-12__title">Keyboard shortcuts</h2>
        <p class="kbd-12__sub">Atlas editor · version 4.2</p>
      </header>
      <div class="kbd-12__cols">
        <section class="kbd-12__group">
          <h3 class="kbd-12__gh">Navigation</h3>
          <div class="kbd-12__rows">
            <div class="kbd-12__row"><span class="kbd-12__label">Go to file</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">P</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Go to symbol in file</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Shift</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">O</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Back</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Minus</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Next problem</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">F8</kbd></kbd></div>
          </div>
        </section>
        <section class="kbd-12__group">
          <h3 class="kbd-12__gh">Editing</h3>
          <div class="kbd-12__rows">
            <div class="kbd-12__row"><span class="kbd-12__label">Save</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">S</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Undo</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Z</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Duplicate line down</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Shift</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Alt</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Down</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Rename symbol</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">F2</kbd></kbd></div>
          </div>
        </section>
        <section class="kbd-12__group">
          <h3 class="kbd-12__gh">View</h3>
          <div class="kbd-12__rows">
            <div class="kbd-12__row"><span class="kbd-12__label">Toggle sidebar</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">B</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Split editor right</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Backslash</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Zen mode</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">K</kbd><span class="kbd-12__sep kbd-12__sep--then">then</span><kbd class="kbd-12__key">Z</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Toggle terminal</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Backtick</kbd></kbd></div>
          </div>
        </section>
        <section class="kbd-12__group">
          <h3 class="kbd-12__gh">Review</h3>
          <div class="kbd-12__rows">
            <div class="kbd-12__row"><span class="kbd-12__label">Add comment</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Alt</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">M</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Approve changes</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">Ctrl</kbd><span class="kbd-12__sep" aria-hidden="true">+</span><kbd class="kbd-12__key">Enter</kbd></kbd></div>
            <div class="kbd-12__row"><span class="kbd-12__label">Resolve thread</span><kbd class="kbd-12__combo"><kbd class="kbd-12__key">R</kbd><span class="kbd-12__sep kbd-12__sep--then">then</span><kbd class="kbd-12__key">T</kbd></kbd></div>
          </div>
        </section>
      </div>
      <footer class="kbd-12__foot">Key column stays aligned across all four groups — one shared measure, no per-group drift</footer>
    </section>
    <div class="kbd-12__theme">
      <input class="kbd-12__themebox" type="checkbox" id="kbd-12-theme">
      <label class="kbd-12__themelabel" for="kbd-12-theme">
        <span class="kbd-12__themedot" aria-hidden="true"></span>
        <span class="kbd-12__themebase">Dark</span><span class="kbd-12__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #0b1220;
  --sheet: #111a2b;
  --ink: #e7eefb;
  --muted: #7e90ad;
  --rule: #1e2b42;
  --cap: #1b2739;
  --cap-ink: #cfe0f7;
  --accent: #7dd3c0;
  --keycol: 10.5rem;
  --font-key: ui-monospace, "SFMono-Regular", Menlo, monospace;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 16px;
}

.kbd-12__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-12__sheet {
  inline-size: 100%;
  max-inline-size: 44rem;
  min-inline-size: 0;
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 24px 22px 18px;
}

.kbd-12__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--rule);
  margin-bottom: 20px;
}

.kbd-12__title {
  margin: 0;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.01em;
  min-inline-size: 0;
}

.kbd-12__sub {
  margin: 0;
  font-family: var(--font-key);
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.06em;
  min-inline-size: 0;
}

.kbd-12__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
  gap: 10px 34px;
}

.kbd-12__group {
  min-inline-size: 0;
  margin-bottom: 12px;
}

.kbd-12__gh {
  margin: 0 0 8px;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--accent);
}

.kbd-12__rows {
  display: grid;
}

.kbd-12__row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) var(--keycol);
  align-items: center;
  gap: 12px;
  min-block-size: 34px;
  padding: 4px 0;
  border-bottom: 1px dotted var(--rule);
}

.kbd-12__row:last-child {
  border-bottom: 0;
}

.kbd-12__label {
  font-size: 13px;
  min-inline-size: 0;
  overflow-wrap: break-word;
}

.kbd-12__combo {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  flex-wrap: nowrap;
  justify-self: end;
  font-family: var(--font-key);
  min-inline-size: 0;
}

.kbd-12__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 22px;
  padding: 4px 6px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11px;
  font-weight: 500;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 0;
  border-radius: 4px;
  white-space: nowrap;
}

.kbd-12__sep {
  font-family: var(--font-key);
  font-size: 10px;
  color: var(--muted);
  user-select: none;
}

.kbd-12__sep--then {
  font-style: italic;
  color: var(--accent);
  font-size: 9.5px;
}

.kbd-12__foot {
  margin-top: 8px;
  padding-top: 14px;
  border-top: 1px solid var(--rule);
  font-size: 11px;
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-12[data-theme="dark"],
[data-theme="dark"] .kbd-12 {
  --page: #080e18;
  --sheet: #0e1725;
  --ink: #e7eefb;
  --muted: #7e90ad;
  --rule: #1c2a40;
  --cap: #182333;
  --cap-ink: #cfe0f7;
  --accent: #7dd3c0;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-12__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-12__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-12__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-12__themelabel {
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

.kbd-12__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-12__themebox:focus-visible + .kbd-12__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-12__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-12__themeflip {
  display: none;
}

.kbd-12:has(.kbd-12__themebox:checked) {
  --page: #eef1f6;
  --sheet: #ffffff;
  --ink: #14202f;
  --muted: #5f7086;
  --rule: #dde3ec;
  --cap: #eff3f8;
  --cap-ink: #2a3a4d;
  --accent: #0f766e;
}

.kbd-12:has(.kbd-12__themebox:checked) .kbd-12__themebase {
  display: none;
}

.kbd-12:has(.kbd-12__themebox:checked) .kbd-12__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-12:not(:has(.kbd-12__themebox:checked)) {
    --page: #eef1f6;
    --sheet: #ffffff;
    --ink: #14202f;
    --muted: #5f7086;
    --rule: #dde3ec;
    --cap: #eff3f8;
    --cap-ink: #2a3a4d;
    --accent: #0f766e;
  }

  .kbd-12:has(.kbd-12__themebox:checked) {
    --page: #0b1220;
    --sheet: #111a2b;
    --ink: #e7eefb;
    --muted: #7e90ad;
    --rule: #1e2b42;
    --cap: #1b2739;
    --cap-ink: #cfe0f7;
    --accent: #7dd3c0;
  }

  .kbd-12:not(:has(.kbd-12__themebox:checked)) .kbd-12__themebase {
    display: none;
  }

  .kbd-12:not(:has(.kbd-12__themebox:checked)) .kbd-12__themeflip {
    display: inline;
  }

  .kbd-12:has(.kbd-12__themebox:checked) .kbd-12__themebase {
    display: inline;
  }

  .kbd-12:has(.kbd-12__themebox:checked) .kbd-12__themeflip {
    display: none;
  }
}
/* Responsive guard (Phase A): the stage centres its child with
   place-items:center, which sizes a grid item to max-content — so a
   wide group could exceed the viewport regardless of min-inline-size
   on the child. Clipping at the scoped root is the reliable stop. */

.kbd-12 {
  overflow-x: hidden;
}
```
