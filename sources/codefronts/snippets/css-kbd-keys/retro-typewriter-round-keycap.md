---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/retro-typewriter-round-keycap/"
title: "Retro Typewriter Round Keycap"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Circular caps ringed in nickel, set with a serif label on a warm paper ground."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Typewriter Round Keycap
Source: https://codefronts.com/snippets/css-kbd-keys/retro-typewriter-round-keycap/

Circular caps ringed in nickel, set with a serif label on a warm paper ground. The shadow is deep and hard rather than soft and modern, because a 1930s key sat on a metal arm and cast an edge, not a blur. Pressing a cap sinks it into the plate with the ring compressing on the way down.
## HTML
```html
<div class="kbd-18">
  <div class="kbd-18__stage">
    <div class="kbd-18__plate">
      <p class="kbd-18__brand">Wickfield · No. 5</p>
      <div class="kbd-18__rowset">
        <div class="kbd-18__row">
          <kbd class="kbd-18__key" tabindex="0">Q</kbd>
          <kbd class="kbd-18__key" tabindex="0">W</kbd>
          <kbd class="kbd-18__key" tabindex="0">E</kbd>
          <kbd class="kbd-18__key" tabindex="0">R</kbd>
          <kbd class="kbd-18__key" tabindex="0">T</kbd>
        </div>
        <div class="kbd-18__row kbd-18__row--offset">
          <kbd class="kbd-18__key" tabindex="0">A</kbd>
          <kbd class="kbd-18__key" tabindex="0">S</kbd>
          <kbd class="kbd-18__key" tabindex="0">D</kbd>
          <kbd class="kbd-18__key kbd-18__key--word" tabindex="0">Shift</kbd>
        </div>
      </div>
      <p class="kbd-18__note">Hard offset shadow · nickel ring · serif label</p>
    </div>
    <div class="kbd-18__theme">
      <input class="kbd-18__themebox" type="checkbox" id="kbd-18-theme">
      <label class="kbd-18__themelabel" for="kbd-18-theme">
        <span class="kbd-18__themedot" aria-hidden="true"></span>
        <span class="kbd-18__themebase">Light</span><span class="kbd-18__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --paper: #e8dcc4;
  --paper-2: #d8c8a8;
  --plate: #2a201a;
  --ink: #f3e9d6;
  --muted: #a9977a;
  --cap: #f6efe0;
  --cap-ink: #2b211a;
  --ring: #b9ad96;
  --ring-in: #1a120d;
  --size: 58px;
  --font-key: "Iowan Old Style", Palatino, Georgia, serif;
  background: repeating-linear-gradient(92deg, rgba(120, 96, 60, 0.05) 0 2px, rgba(120, 96, 60, 0) 2px 5px), linear-gradient(168deg, var(--paper) 0%, var(--paper-2) 100%);
  color: var(--plate);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-18__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-18__plate {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: linear-gradient(180deg, #35281f 0%, #221a14 100%);
  border-radius: 10px;
  padding: 26px 22px 22px;
  color: var(--ink);
  box-shadow: 0 8px 0 #150f0a, 0 14px 26px -10px rgba(30, 20, 10, 0.65);
}

.kbd-18__brand {
  margin: 0 0 22px;
  font-size: 12px;
  font-style: italic;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
}

.kbd-18__rowset {
  display: grid;
  gap: 16px;
}

.kbd-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}

.kbd-18__row--offset {
  padding-inline-start: calc(var(--size) * 0.4);
}

.kbd-18__key {
  inline-size: var(--size);
  block-size: var(--size);
  min-inline-size: 44px;
  min-block-size: 44px;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: inherit;
  font-size: 19px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.04em;
  line-height: 1;
  color: var(--cap-ink);
  background: radial-gradient(72% 62% at 42% 30%, #fffaf0 0%, var(--cap) 62%, #e2d6bf 100%);
  border: 2px solid var(--ring);
  border-radius: 50%;
  cursor: pointer;
  user-select: none;
  box-shadow: inset 0 0 0 2px var(--ring-in), 0 5px 0 #12100c, 0 7px 6px -3px rgba(0, 0, 0, 0.55);
  transition: transform 90ms linear, box-shadow 90ms linear;
}

.kbd-18__key--word {
  font-size: 12px;
  letter-spacing: 0.06em;
}

.kbd-18__key:active,
.kbd-18__key:focus-visible {
  transform: translateY(4px);
  box-shadow: inset 0 0 0 2px var(--ring-in), 0 1px 0 #12100c, 0 2px 3px -1px rgba(0, 0, 0, 0.6);
}

.kbd-18__key:focus-visible {
  outline: 3px solid #d8a24a;
  outline-offset: 3px;
}

.kbd-18__note {
  margin: 22px 0 0;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 11px;
  font-style: italic;
  letter-spacing: 0.14em;
  color: var(--muted);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-18__key {
    transition: none;
  }
}

.kbd-18[data-theme="dark"],
[data-theme="dark"] .kbd-18 {
  --paper: #241d14;
  --paper-2: #1a150e;
  --ink: #f0e6d2;
  --muted: #9b8a6d;
  --cap: #e6dcc6;
  --ring: #8e836e;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-18__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-18__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-18__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-18__themelabel {
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

.kbd-18__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-18__themebox:focus-visible + .kbd-18__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-18__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}
/* This demo's --ink belongs to the dark plate, not the paper ground the switch
   sits on, so the control takes an opaque plate chip and the plate's own edge
   token rather than inheriting the root text colour. */

.kbd-18__themelabel {
  background: var(--plate);
  color: var(--ink);
}

.kbd-18__themeflip {
  display: none;
}

.kbd-18:has(.kbd-18__themebox:checked) {
  --paper: #241d14;
  --paper-2: #1a150e;
  --ink: #f0e6d2;
  --muted: #9b8a6d;
  --cap: #e6dcc6;
  --ring: #8e836e;
}

.kbd-18:has(.kbd-18__themebox:checked) .kbd-18__themebase {
  display: none;
}

.kbd-18:has(.kbd-18__themebox:checked) .kbd-18__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-18:not(:has(.kbd-18__themebox:checked)) {
    --paper: #241d14;
    --paper-2: #1a150e;
    --ink: #f0e6d2;
    --muted: #9b8a6d;
    --cap: #e6dcc6;
    --ring: #8e836e;
  }

  .kbd-18:has(.kbd-18__themebox:checked) {
    --paper: #e8dcc4;
    --paper-2: #d8c8a8;
    --ink: #f3e9d6;
    --muted: #a9977a;
    --cap: #f6efe0;
    --ring: #b9ad96;
  }

  .kbd-18:not(:has(.kbd-18__themebox:checked)) .kbd-18__themebase {
    display: none;
  }

  .kbd-18:not(:has(.kbd-18__themebox:checked)) .kbd-18__themeflip {
    display: inline;
  }

  .kbd-18:has(.kbd-18__themebox:checked) .kbd-18__themebase {
    display: inline;
  }

  .kbd-18:has(.kbd-18__themebox:checked) /* This demo's --ink belongs to the dark plate, not the paper ground the switch
     sits on, so the control takes an opaque plate chip and the plate's own edge token rather than inheriting the root text colour. */ .kbd-18__themelabel {
    background: var(--plate);
    color: var(--ink);
  }

  .kbd-18__themeflip {
    display: none;
  }
}
```
