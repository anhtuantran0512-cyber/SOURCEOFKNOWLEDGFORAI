---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/fluid-kbd-sizing-with-em-units/"
title: "Fluid Kbd Sizing with Em Units"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "One class, three contexts."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fluid Kbd Sizing with Em Units
Source: https://codefronts.com/snippets/css-kbd-keys/fluid-kbd-sizing-with-em-units/

One class, three contexts. Every dimension on the cap — padding, radius, border, minimum width — is expressed in em, so the same markup renders correctly inside a large heading, ordinary body copy, and a small caption without a single size override. The demo puts all three on screen at once so the scaling is visible rather than asserted.
## HTML
```html
<div class="kbd-05">
  <div class="kbd-05__stage">
    <div class="kbd-05__sheet">
      <p class="kbd-05__eyebrow">Same markup · three contexts</p>
      <h2 class="kbd-05__h">Press <kbd class="kbd-05__key">Ctrl</kbd> <span class="kbd-05__plus">+</span> <kbd class="kbd-05__key">P</kbd> to jump</h2>
      <p class="kbd-05__p">In body copy the same cap settles down to something you can read past: <kbd class="kbd-05__key">Ctrl</kbd> <span class="kbd-05__plus">+</span> <kbd class="kbd-05__key">P</kbd> opens the file switcher, and <kbd class="kbd-05__key">Esc</kbd> closes it again.</p>
      <p class="kbd-05__caption">Even in a caption it stays centred and legible — <kbd class="kbd-05__key">Ctrl</kbd> <span class="kbd-05__plus">+</span> <kbd class="kbd-05__key">P</kbd> · figure 2</p>
      <ul class="kbd-05__metrics">
        <li class="kbd-05__metric"><span class="kbd-05__mk">padding</span><span class="kbd-05__mv">0.3em 0.55em</span></li>
        <li class="kbd-05__metric"><span class="kbd-05__mk">radius</span><span class="kbd-05__mv">0.32em</span></li>
        <li class="kbd-05__metric"><span class="kbd-05__mk">border</span><span class="kbd-05__mv">0.07em</span></li>
        <li class="kbd-05__metric"><span class="kbd-05__mk">label</span><span class="kbd-05__mv">0.85em</span></li>
      </ul>
    </div>
    <div class="kbd-05__theme">
      <input class="kbd-05__themebox" type="checkbox" id="kbd-05-theme">
      <label class="kbd-05__themelabel" for="kbd-05-theme">
        <span class="kbd-05__themedot" aria-hidden="true"></span>
        <span class="kbd-05__themebase">Light</span><span class="kbd-05__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #f3efe7;
  --sheet: #fdfbf6;
  --ink: #3a2f24;
  --muted: #8b7a64;
  --rule: #e3d9c8;
  --cap: #f7f1e4;
  --cap-border: #c9b998;
  --cap-ink: #4a3b2a;
  --pad-y: 0.3em;
  --pad-x: 0.55em;
  --radius: 0.32em;
  --key-size: 0.85em;
  --font-key: ui-monospace, "SFMono-Regular", Menlo, monospace;
  --font-body: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-body);
  padding: 40px 20px;
}

.kbd-05__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-05__sheet {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: 3px;
  padding: 28px 26px 24px;
}

.kbd-05__eyebrow {
  margin: 0 0 14px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-05__h {
  margin: 0 0 18px;
  font-size: clamp(22px, 5.4vw, 34px);
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.kbd-05__p {
  margin: 0 0 18px;
  font-size: 16px;
  line-height: 1.75;
  text-wrap: pretty;
}

.kbd-05__caption {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--muted);
}

.kbd-05__key {
  display: inline-block;
  padding: var(--pad-y) var(--pad-x);
  min-inline-size: 1em;
  font-family: var(--font-key);
  font-size: var(--key-size);
  font-weight: 500;
  line-height: 1;
  text-align: center;
  color: var(--cap-ink);
  background: var(--cap);
  border: 0.07em solid var(--cap-border);
  border-radius: var(--radius);
  box-shadow: 0 0.07em 0 var(--cap-border);
  vertical-align: 0.06em;
  white-space: nowrap;
}

.kbd-05__plus {
  font-family: var(--font-key);
  font-size: 0.8em;
  color: var(--muted);
}

.kbd-05__metrics {
  margin: 24px 0 0;
  padding: 18px 0 0;
  border-top: 1px solid var(--rule);
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(8rem, 1fr));
  gap: 10px 18px;
}

.kbd-05__metric {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  min-inline-size: 0;
  border-bottom: 1px dotted var(--rule);
  padding-bottom: 6px;
}

.kbd-05__mk {
  font-size: 10px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.kbd-05__mv {
  font-family: var(--font-key);
  font-size: 11.5px;
  color: var(--ink);
  min-inline-size: 0;
}

.kbd-05[data-theme="dark"],
[data-theme="dark"] .kbd-05 {
  --page: #1c1710;
  --sheet: #241e16;
  --ink: #f0e6d6;
  --muted: #a89a80;
  --rule: #3b3225;
  --cap: #322a1f;
  --cap-border: #574a34;
  --cap-ink: #f6ecd9;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-05__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-05__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-05__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-05__themelabel {
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

.kbd-05__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-05__themebox:focus-visible + .kbd-05__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-05__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-05__themeflip {
  display: none;
}

.kbd-05:has(.kbd-05__themebox:checked) {
  --page: #1c1710;
  --sheet: #241e16;
  --ink: #f0e6d6;
  --muted: #a89a80;
  --rule: #3b3225;
  --cap: #322a1f;
  --cap-border: #574a34;
  --cap-ink: #f6ecd9;
}

.kbd-05:has(.kbd-05__themebox:checked) .kbd-05__themebase {
  display: none;
}

.kbd-05:has(.kbd-05__themebox:checked) .kbd-05__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-05:not(:has(.kbd-05__themebox:checked)) {
    --page: #1c1710;
    --sheet: #241e16;
    --ink: #f0e6d6;
    --muted: #a89a80;
    --rule: #3b3225;
    --cap: #322a1f;
    --cap-border: #574a34;
    --cap-ink: #f6ecd9;
  }

  .kbd-05:has(.kbd-05__themebox:checked) {
    --page: #f3efe7;
    --sheet: #fdfbf6;
    --ink: #3a2f24;
    --muted: #8b7a64;
    --rule: #e3d9c8;
    --cap: #f7f1e4;
    --cap-border: #c9b998;
    --cap-ink: #4a3b2a;
  }

  .kbd-05:not(:has(.kbd-05__themebox:checked)) .kbd-05__themebase {
    display: none;
  }

  .kbd-05:not(:has(.kbd-05__themebox:checked)) .kbd-05__themeflip {
    display: inline;
  }

  .kbd-05:has(.kbd-05__themebox:checked) .kbd-05__themebase {
    display: inline;
  }

  .kbd-05:has(.kbd-05__themebox:checked) .kbd-05__themeflip {
    display: none;
  }
}
```
