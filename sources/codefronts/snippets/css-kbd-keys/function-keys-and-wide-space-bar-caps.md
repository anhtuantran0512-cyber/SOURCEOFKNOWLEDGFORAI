---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/function-keys-and-wide-space-bar-caps/"
title: "Function Keys and Wide Space Bar Caps"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Real keyboards specify key widths in units, and so does this demo."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Function Keys and Wide Space Bar Caps
Source: https://codefronts.com/snippets/css-kbd-keys/function-keys-and-wide-space-bar-caps/

Real keyboards specify key widths in units, and so does this demo. A single --u custom property defines one unit, and each wide cap multiplies it with its own --w value, exactly the way physical layouts are described. The function row, Tab, Backspace, Shift, Enter and a full-width Space bar all come from the same rule with one number changed.
## HTML
```html
<div class="kbd-09">
  <div class="kbd-09__stage">
    <section class="kbd-09__board">
      <p class="kbd-09__eyebrow">Function row · 1u each</p>
      <div class="kbd-09__row">
        <kbd class="kbd-09__key">Esc</kbd>
        <kbd class="kbd-09__key">F1</kbd>
        <kbd class="kbd-09__key">F2</kbd>
        <kbd class="kbd-09__key">F3</kbd>
        <kbd class="kbd-09__key">F4</kbd>
        <kbd class="kbd-09__key">F5</kbd>
        <kbd class="kbd-09__key">F6</kbd>
        <kbd class="kbd-09__key">F7</kbd>
        <kbd class="kbd-09__key">F8</kbd>
        <kbd class="kbd-09__key">F9</kbd>
        <kbd class="kbd-09__key">F10</kbd>
        <kbd class="kbd-09__key">F11</kbd>
        <kbd class="kbd-09__key">F12</kbd>
      </div>
      <p class="kbd-09__eyebrow">Wide caps · width equals unit times multiplier</p>
      <div class="kbd-09__row">
        <kbd class="kbd-09__key" style="--w: 1.5">Tab</kbd>
        <kbd class="kbd-09__key" style="--w: 2">Backspace</kbd>
        <kbd class="kbd-09__key" style="--w: 2.25">Shift</kbd>
        <kbd class="kbd-09__key" style="--w: 1.75">Enter</kbd>
      </div>
      <div class="kbd-09__row">
        <kbd class="kbd-09__key" style="--w: 1.25">Ctrl</kbd>
        <kbd class="kbd-09__key" style="--w: 1.25">Alt</kbd>
        <kbd class="kbd-09__key kbd-09__key--space" style="--w: 6.25">Space</kbd>
        <kbd class="kbd-09__key" style="--w: 1.25">Alt</kbd>
      </div>
      <dl class="kbd-09__legend">
        <div class="kbd-09__lrow"><dt class="kbd-09__lk">1u</dt><dd class="kbd-09__lv">letter, digit, function key</dd></div>
        <div class="kbd-09__lrow"><dt class="kbd-09__lk">1.5u</dt><dd class="kbd-09__lv">Tab</dd></div>
        <div class="kbd-09__lrow"><dt class="kbd-09__lk">2.25u</dt><dd class="kbd-09__lv">left Shift</dd></div>
        <div class="kbd-09__lrow"><dt class="kbd-09__lk">6.25u</dt><dd class="kbd-09__lv">Space bar</dd></div>
      </dl>
    </section>
    <div class="kbd-09__theme">
      <input class="kbd-09__themebox" type="checkbox" id="kbd-09-theme">
      <label class="kbd-09__themelabel" for="kbd-09-theme">
        <span class="kbd-09__themedot" aria-hidden="true"></span>
        <span class="kbd-09__themebase">Light</span><span class="kbd-09__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #e7eaee;
  --board: #f6f7f9;
  --ink: #1f242b;
  --muted: #737d8a;
  --rule: #d6dbe2;
  --cap: #fcfdfe;
  --cap-border: #b8c0cb;
  --cap-edge: #98a2b0;
  --cap-ink: #262c34;
  --u: clamp(30px, 7.2vw, 46px);
  --gap: 6px;
  --radius: 7px;
  --font-key: "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 16px;
}

.kbd-09__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-09__board {
  inline-size: 100%;
  max-inline-size: 38rem;
  min-inline-size: 0;
  background: var(--board);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 22px 18px 18px;
}

.kbd-09__eyebrow {
  margin: 0 0 10px;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--gap);
  margin: 0 0 18px;
  justify-content: flex-start;
}

.kbd-09__key {
  --w: 1;
  inline-size: calc(var(--u) * var(--w));
  min-inline-size: 0;
  block-size: var(--u);
  min-block-size: 30px;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0 4px;
  overflow: hidden;
  font-family: inherit;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  box-shadow: 0 2px 0 var(--cap-edge), 0 3px 5px -2px rgba(31, 36, 43, 0.25);
  white-space: nowrap;
  text-overflow: ellipsis;
}

.kbd-09__key--space {
  letter-spacing: 0.3em;
}

.kbd-09__legend {
  margin: 4px 0 0;
  padding-top: 16px;
  border-top: 1px solid var(--rule);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
  gap: 8px 20px;
}

.kbd-09__lrow {
  display: flex;
  gap: 10px;
  align-items: baseline;
  min-inline-size: 0;
}

.kbd-09__lk {
  margin: 0;
  inline-size: 2.6rem;
  flex: none;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--ink);
}

.kbd-09__lv {
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.kbd-09[data-theme="dark"],
[data-theme="dark"] .kbd-09 {
  --page: #14181d;
  --board: #1b2027;
  --ink: #e8ecf2;
  --muted: #8b96a4;
  --rule: #2a3138;
  --cap: #262d36;
  --cap-border: #3d4652;
  --cap-edge: #0e1216;
  --cap-ink: #eef2f7;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-09__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-09__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-09__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-09__themelabel {
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

.kbd-09__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-09__themebox:focus-visible + .kbd-09__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-09__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-09__themeflip {
  display: none;
}

.kbd-09:has(.kbd-09__themebox:checked) {
  --page: #14181d;
  --board: #1b2027;
  --ink: #e8ecf2;
  --muted: #8b96a4;
  --rule: #2a3138;
  --cap: #262d36;
  --cap-border: #3d4652;
  --cap-edge: #0e1216;
  --cap-ink: #eef2f7;
}

.kbd-09:has(.kbd-09__themebox:checked) .kbd-09__themebase {
  display: none;
}

.kbd-09:has(.kbd-09__themebox:checked) .kbd-09__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-09:not(:has(.kbd-09__themebox:checked)) {
    --page: #14181d;
    --board: #1b2027;
    --ink: #e8ecf2;
    --muted: #8b96a4;
    --rule: #2a3138;
    --cap: #262d36;
    --cap-border: #3d4652;
    --cap-edge: #0e1216;
    --cap-ink: #eef2f7;
  }

  .kbd-09:has(.kbd-09__themebox:checked) {
    --page: #e7eaee;
    --board: #f6f7f9;
    --ink: #1f242b;
    --muted: #737d8a;
    --rule: #d6dbe2;
    --cap: #fcfdfe;
    --cap-border: #b8c0cb;
    --cap-edge: #98a2b0;
    --cap-ink: #262c34;
  }

  .kbd-09:not(:has(.kbd-09__themebox:checked)) .kbd-09__themebase {
    display: none;
  }

  .kbd-09:not(:has(.kbd-09__themebox:checked)) .kbd-09__themeflip {
    display: inline;
  }

  .kbd-09:has(.kbd-09__themebox:checked) .kbd-09__themebase {
    display: inline;
  }

  .kbd-09:has(.kbd-09__themebox:checked) .kbd-09__themeflip {
    display: none;
  }
}
```
