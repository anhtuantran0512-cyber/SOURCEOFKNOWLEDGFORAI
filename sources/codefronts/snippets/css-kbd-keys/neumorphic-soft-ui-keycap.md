---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/neumorphic-soft-ui-keycap/"
title: "Neumorphic Soft UI Keycap"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "The soft-UI treatment done honestly: a matched pair of light and dark shadows on a mid-tone surface, extruded at rest and genuinely inset when pressed."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft UI Keycap
Source: https://codefronts.com/snippets/css-kbd-keys/neumorphic-soft-ui-keycap/

The soft-UI treatment done honestly: a matched pair of light and dark shadows on a mid-tone surface, extruded at rest and genuinely inset when pressed. It also states the limitation plainly, because a shadow-only edge does not meet the WCAG non-text contrast requirement, so each cap here keeps a faint border and a high-contrast label.
## HTML
```html
<div class="kbd-16">
  <div class="kbd-16__stage">
    <div class="kbd-16__pad">
      <p class="kbd-16__eyebrow">Soft UI · press a cap</p>
      <div class="kbd-16__row">
        <kbd class="kbd-16__key" tabindex="0">⌘</kbd>
        <kbd class="kbd-16__key" tabindex="0">⌥</kbd>
        <kbd class="kbd-16__key" tabindex="0">⇧</kbd>
        <kbd class="kbd-16__key kbd-16__key--wide" tabindex="0">Return</kbd>
      </div>
      <p class="kbd-16__caveat">Shadow-only edges have no contrast ratio. Every cap here keeps a hairline border and a label above 4.5:1 so the control stays perceivable.</p>
    </div>
    <div class="kbd-16__theme">
      <input class="kbd-16__themebox" type="checkbox" id="kbd-16-theme">
      <label class="kbd-16__themelabel" for="kbd-16-theme">
        <span class="kbd-16__themedot" aria-hidden="true"></span>
        <span class="kbd-16__themebase">Light</span><span class="kbd-16__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --board: #e3e7ee;
  --hi: #ffffff;
  --shade: #b9c0cd;
  --ink: #38414f;
  --muted: #7a8493;
  --cap-ink: #2b333f;
  --cap-border: rgba(90, 100, 118, 0.22);
  --depth: 7px;
  --radius: 18px;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  background: var(--board);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-16__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-16__pad {
  inline-size: 100%;
  max-inline-size: 28rem;
  min-inline-size: 0;
  padding: 30px 26px 26px;
  border-radius: 26px;
  background: var(--board);
  box-shadow: calc(var(--depth) * -1) calc(var(--depth) * -1) calc(var(--depth) * 2.4) var(--hi), var(--depth) var(--depth) calc(var(--depth) * 2.4) var(--shade);
}

.kbd-16__eyebrow {
  margin: 0 0 22px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
}

.kbd-16__row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.kbd-16__key {
  min-inline-size: 58px;
  min-block-size: 58px;
  padding: 0 14px;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: inherit;
  font-size: 19px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--board);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  cursor: pointer;
  user-select: none;
  box-shadow: calc(var(--depth) * -0.7) calc(var(--depth) * -0.7) calc(var(--depth) * 1.7) var(--hi), calc(var(--depth) * 0.7) calc(var(--depth) * 0.7) calc(var(--depth) * 1.7) var(--shade);
  transition: box-shadow 150ms ease, color 150ms ease;
}

.kbd-16__key--wide {
  min-inline-size: 104px;
  font-size: 14px;
  letter-spacing: 0.04em;
}

.kbd-16__key:active,
.kbd-16__key:focus-visible {
  box-shadow: inset calc(var(--depth) * -0.6) calc(var(--depth) * -0.6) calc(var(--depth) * 1.4) var(--hi), inset calc(var(--depth) * 0.6) calc(var(--depth) * 0.6) calc(var(--depth) * 1.4) var(--shade);
}

.kbd-16__key:focus-visible {
  outline: 3px solid #4f6da8;
  outline-offset: 3px;
}

.kbd-16__caveat {
  margin: 24px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-16__key {
    transition: none;
  }
}

.kbd-16[data-theme="dark"],
[data-theme="dark"] .kbd-16 {
  --board: #2d323b;
  --hi: #3b424e;
  --shade: #1c2027;
  --ink: #dde3ec;
  --muted: #97a1b0;
  --cap-ink: #eef2f8;
  --cap-border: rgba(255, 255, 255, 0.12);
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-16__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-16__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-16__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-16__themelabel {
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

.kbd-16__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-16__themebox:focus-visible + .kbd-16__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-16__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-16__themeflip {
  display: none;
}

.kbd-16:has(.kbd-16__themebox:checked) {
  --board: #2d323b;
  --hi: #3b424e;
  --shade: #1c2027;
  --ink: #dde3ec;
  --muted: #97a1b0;
  --cap-ink: #eef2f8;
  --cap-border: rgba(255, 255, 255, 0.12);
}

.kbd-16:has(.kbd-16__themebox:checked) .kbd-16__themebase {
  display: none;
}

.kbd-16:has(.kbd-16__themebox:checked) .kbd-16__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-16:not(:has(.kbd-16__themebox:checked)) {
    --board: #2d323b;
    --hi: #3b424e;
    --shade: #1c2027;
    --ink: #dde3ec;
    --muted: #97a1b0;
    --cap-ink: #eef2f8;
    --cap-border: rgba(255, 255, 255, 0.12);
  }

  .kbd-16:has(.kbd-16__themebox:checked) {
    --board: #e3e7ee;
    --hi: #ffffff;
    --shade: #b9c0cd;
    --ink: #38414f;
    --muted: #7a8493;
    --cap-ink: #2b333f;
    --cap-border: rgba(90, 100, 118, 0.22);
  }

  .kbd-16:not(:has(.kbd-16__themebox:checked)) .kbd-16__themebase {
    display: none;
  }

  .kbd-16:not(:has(.kbd-16__themebox:checked)) .kbd-16__themeflip {
    display: inline;
  }

  .kbd-16:has(.kbd-16__themebox:checked) .kbd-16__themebase {
    display: inline;
  }

  .kbd-16:has(.kbd-16__themebox:checked) .kbd-16__themeflip {
    display: none;
  }
}
```
