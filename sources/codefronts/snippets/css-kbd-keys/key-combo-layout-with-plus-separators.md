---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/key-combo-layout-with-plus-separators/"
title: "Key Combo Layout with Plus Separators"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Multi-key combos laid out as a flex row with a dimmed separator between the caps."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Key Combo Layout with Plus Separators
Source: https://codefronts.com/snippets/css-kbd-keys/key-combo-layout-with-plus-separators/

Multi-key combos laid out as a flex row with a dimmed separator between the caps. The separator sits outside the kbd elements, which is the whole point: a screen reader then announces Control plus C rather than reading punctuation trapped inside a key. Includes a second row for sequential shortcuts, where G then P is a sequence and not a chord.
## HTML
```html
<div class="kbd-03">
  <div class="kbd-03__stage">
    <section class="kbd-03__panel">
      <header class="kbd-03__head">
        <h2 class="kbd-03__title">Chords</h2>
        <p class="kbd-03__sub">Held together · separator reads as plus</p>
      </header>
      <ul class="kbd-03__list">
        <li class="kbd-03__item">
          <span class="kbd-03__label">Copy selection</span>
          <kbd class="kbd-03__combo"><kbd class="kbd-03__key">Ctrl</kbd><span class="kbd-03__sep" aria-hidden="true">+</span><kbd class="kbd-03__key">C</kbd></kbd>
        </li>
        <li class="kbd-03__item">
          <span class="kbd-03__label">Toggle sidebar</span>
          <kbd class="kbd-03__combo"><kbd class="kbd-03__key">Ctrl</kbd><span class="kbd-03__sep" aria-hidden="true">+</span><kbd class="kbd-03__key">B</kbd></kbd>
        </li>
        <li class="kbd-03__item">
          <span class="kbd-03__label">Split editor right</span>
          <kbd class="kbd-03__combo"><kbd class="kbd-03__key">Ctrl</kbd><span class="kbd-03__sep" aria-hidden="true">+</span><kbd class="kbd-03__key">Shift</kbd><span class="kbd-03__sep" aria-hidden="true">+</span><kbd class="kbd-03__key">Backslash</kbd></kbd>
        </li>
      </ul>
      <header class="kbd-03__head kbd-03__head--second">
        <h2 class="kbd-03__title">Sequences</h2>
        <p class="kbd-03__sub">Pressed in order · separator reads as then</p>
      </header>
      <ul class="kbd-03__list">
        <li class="kbd-03__item">
          <span class="kbd-03__label">Go to pull requests</span>
          <kbd class="kbd-03__combo"><kbd class="kbd-03__key">G</kbd><span class="kbd-03__sep kbd-03__sep--then">then</span><kbd class="kbd-03__key">P</kbd></kbd>
        </li>
        <li class="kbd-03__item">
          <span class="kbd-03__label">Go to issues</span>
          <kbd class="kbd-03__combo"><kbd class="kbd-03__key">G</kbd><span class="kbd-03__sep kbd-03__sep--then">then</span><kbd class="kbd-03__key">I</kbd></kbd>
        </li>
      </ul>
    </section>
    <div class="kbd-03__theme">
      <input class="kbd-03__themebox" type="checkbox" id="kbd-03-theme">
      <label class="kbd-03__themelabel" for="kbd-03-theme">
        <span class="kbd-03__themedot" aria-hidden="true"></span>
        <span class="kbd-03__themebase">Light</span><span class="kbd-03__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --bg: #eef2f8;
  --panel: #ffffff;
  --ink: #16243a;
  --muted: #6b7d99;
  --rule: #dde5f0;
  --cap: #f5f8fc;
  --cap-border: #c3d0e2;
  --cap-ink: #1d3557;
  --accent: #1f5fd0;
  --gap: 7px;
  --radius: 5px;
  --font-key: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-03__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-03__panel {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 24px 24px 26px;
  box-shadow: 0 1px 2px rgba(22, 36, 58, 0.06), 0 10px 30px -18px rgba(22, 36, 58, 0.28);
}

.kbd-03__head {
  margin: 0 0 14px;
}

.kbd-03__head--second {
  margin-top: 26px;
  padding-top: 20px;
  border-top: 1px solid var(--rule);
}

.kbd-03__title {
  margin: 0 0 4px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.kbd-03__sub {
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
  letter-spacing: 0.02em;
}

.kbd-03__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 2px;
}

.kbd-03__item {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 9px 0;
  border-bottom: 1px dotted var(--rule);
}

.kbd-03__item:last-child {
  border-bottom: 0;
}

.kbd-03__label {
  font-size: 13.5px;
  color: var(--ink);
  min-inline-size: 0;
  flex: 1 1 9rem;
}

.kbd-03__combo {
  display: inline-flex;
  align-items: center;
  gap: var(--gap);
  font-family: inherit;
  min-inline-size: 0;
  flex-wrap: wrap;
}

.kbd-03__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 26px;
  padding: 5px 8px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  line-height: 1;
  letter-spacing: 0.02em;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  white-space: nowrap;
}

.kbd-03__sep {
  font-size: 11px;
  font-weight: 600;
  color: var(--muted);
  line-height: 1;
  user-select: none;
}

.kbd-03__sep--then {
  font-style: italic;
  font-weight: 400;
  font-size: 10.5px;
  color: var(--accent);
  letter-spacing: 0.04em;
}

.kbd-03[data-theme="dark"],
[data-theme="dark"] .kbd-03 {
  --bg: #0d1420;
  --panel: #141d2c;
  --ink: #e9eff8;
  --muted: #8798b4;
  --rule: #24314a;
  --cap: #1e2a3e;
  --cap-border: #35476a;
  --cap-ink: #dce7f6;
  --accent: #78a9ff;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-03__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-03__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-03__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-03__themelabel {
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

.kbd-03__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-03__themebox:focus-visible + .kbd-03__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-03__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-03__themeflip {
  display: none;
}

.kbd-03:has(.kbd-03__themebox:checked) {
  --bg: #0d1420;
  --panel: #141d2c;
  --ink: #e9eff8;
  --muted: #8798b4;
  --rule: #24314a;
  --cap: #1e2a3e;
  --cap-border: #35476a;
  --cap-ink: #dce7f6;
  --accent: #78a9ff;
}

.kbd-03:has(.kbd-03__themebox:checked) .kbd-03__themebase {
  display: none;
}

.kbd-03:has(.kbd-03__themebox:checked) .kbd-03__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-03:not(:has(.kbd-03__themebox:checked)) {
    --bg: #0d1420;
    --panel: #141d2c;
    --ink: #e9eff8;
    --muted: #8798b4;
    --rule: #24314a;
    --cap: #1e2a3e;
    --cap-border: #35476a;
    --cap-ink: #dce7f6;
    --accent: #78a9ff;
  }

  .kbd-03:has(.kbd-03__themebox:checked) {
    --bg: #eef2f8;
    --panel: #ffffff;
    --ink: #16243a;
    --muted: #6b7d99;
    --rule: #dde5f0;
    --cap: #f5f8fc;
    --cap-border: #c3d0e2;
    --cap-ink: #1d3557;
    --accent: #1f5fd0;
  }

  .kbd-03:not(:has(.kbd-03__themebox:checked)) .kbd-03__themebase {
    display: none;
  }

  .kbd-03:not(:has(.kbd-03__themebox:checked)) .kbd-03__themeflip {
    display: inline;
  }

  .kbd-03:has(.kbd-03__themebox:checked) .kbd-03__themebase {
    display: inline;
  }

  .kbd-03:has(.kbd-03__themebox:checked) .kbd-03__themeflip {
    display: none;
  }
}
```
