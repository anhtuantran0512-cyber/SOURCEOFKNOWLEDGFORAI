---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/one-bit-bevel-borders-with-box-shadow/"
title: "One Bit Bevel Borders with Box Shadow"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "Every raised or sunken control of the 16-bit desktop era is the same object: four box-shadow insets in a fixed order &mdash; outer light, outer dark, inner…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: One Bit Bevel Borders with Box Shadow
Source: https://codefronts.com/design-styles/css-retro-designs/one-bit-bevel-borders-with-box-shadow/

Every raised or sunken control of the 16-bit desktop era is the same object: four box-shadow insets in a fixed order &mdash; outer light, outer dark, inner light, inner dark &mdash; with the order reversed for the pressed state. One rule set produces raised, sunken, pressed and disabled here, with the shadow order printed next to an exploded diagram of the four edges.
## HTML
```html
<section class="rt-04" aria-labelledby="rt-04-title">
  <h2 class="rt-04__sr" id="rt-04-title">One-bit bevel border states</h2>

  <div class="rt-04__theme">
    <input class="rt-04__theme-input" type="checkbox" id="rt-04-theme">
    <label class="rt-04__theme-label" for="rt-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-04__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-04__stage">
    <header class="rt-04__head">
      <p class="rt-04__kicker">Windows 95 &middot; system metrics, 3D objects</p>
      <h3 class="rt-04__h">Four insets, one fixed order</h3>
    </header>

    <div class="rt-04__board">
      <article class="rt-04__group" aria-labelledby="rt-04-g1">
        <h4 class="rt-04__group-h" id="rt-04-g1">States</h4>
        <div class="rt-04__states">
          <div class="rt-04__demo">
            <button class="rt-04__btn" type="button">Raised</button>
            <p class="rt-04__lbl">default &middot; light outer top-left</p>
          </div>
          <div class="rt-04__demo">
            <button class="rt-04__btn rt-04__btn--pressed" type="button" aria-pressed="true">Pressed</button>
            <p class="rt-04__lbl">order reversed &middot; caption offset 1px</p>
          </div>
          <div class="rt-04__demo">
            <div class="rt-04__well">Sunken well</div>
            <p class="rt-04__lbl">reversed, no caption offset</p>
          </div>
          <div class="rt-04__demo">
            <button class="rt-04__btn rt-04__btn--off" type="button" disabled>Disabled</button>
            <p class="rt-04__lbl">etched caption &middot; shadow + highlight</p>
          </div>
        </div>
      </article>

      <article class="rt-04__group" aria-labelledby="rt-04-g2">
        <h4 class="rt-04__group-h" id="rt-04-g2">Exploded edge</h4>
        <div class="rt-04__explode">
          <div class="rt-04__layer rt-04__layer--1"><span>1</span> inset 1px 1px 0 #ffffff</div>
          <div class="rt-04__layer rt-04__layer--2"><span>2</span> inset -1px -1px 0 #000000</div>
          <div class="rt-04__layer rt-04__layer--3"><span>3</span> inset 2px 2px 0 #dfdfdf</div>
          <div class="rt-04__layer rt-04__layer--4"><span>4</span> inset -2px -2px 0 #808080</div>
        </div>
        <p class="rt-04__cap">Painted first to last, top to bottom. Later layers sit underneath.</p>
      </article>
    </div>

    <article class="rt-04__group rt-04__group--wide" aria-labelledby="rt-04-g3">
      <h4 class="rt-04__group-h" id="rt-04-g3">Applied &mdash; a dialog built only from insets</h4>
      <div class="rt-04__win">
        <div class="rt-04__title">
          <span class="rt-04__title-t">Display Properties</span>
          <span class="rt-04__title-btns">
            <button class="rt-04__sysbtn" type="button" aria-label="Minimise"><span aria-hidden="true">_</span></button>
            <button class="rt-04__sysbtn" type="button" aria-label="Maximise"><span aria-hidden="true">&#9633;</span></button>
            <button class="rt-04__sysbtn" type="button" aria-label="Close"><span aria-hidden="true">&#215;</span></button>
          </span>
        </div>
        <div class="rt-04__body">
          <p class="rt-04__text">Bevel unit is a single custom property. Every control below shares it.</p>
          <div class="rt-04__field">
            <span class="rt-04__field-l" id="rt-04-fl">Colour palette</span>
            <span class="rt-04__well rt-04__well--sm" role="status" aria-labelledby="rt-04-fl">256 Colour</span>
          </div>
          <div class="rt-04__actions">
            <button class="rt-04__btn" type="button">OK</button>
            <button class="rt-04__btn" type="button">Cancel</button>
            <button class="rt-04__btn" type="button">Apply</button>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.rt-04 {
  --rt-04-b: 2px;
  --rt-04-face: #c0c0c0;
  --rt-04-hilite: #ffffff;
  --rt-04-light: #dfdfdf;
  --rt-04-shadow: #808080;
  --rt-04-dark: #000000;
  --rt-04-title-a: #000080;
  --rt-04-title-b: #1084d0;
  --rt-04-sans: system-ui, -apple-system, "Segoe UI", Tahoma, "Helvetica Neue", Arial, sans-serif;
  --rt-04-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --rt-04-bg: #008080;
  --rt-04-ink: #101214;
  --rt-04-ink: oklch(18% 0.006 240);
  --rt-04-ink-2: #3d4348;
  --rt-04-ink-2: oklch(38% 0.01 240);
  --rt-04-panel: #d8d8d0;
  --rt-04-acc: #0a3fa8;
  --rt-04-acc: oklch(40% 0.19 262);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-04-bg);
  color: var(--rt-04-ink);
  font-family: var(--rt-04-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-04 *,
.rt-04 *::before,
.rt-04 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-04 {
    --rt-04-bg: #0a2c2c;
    --rt-04-bg: oklch(26% 0.045 195);
    --rt-04-panel: #cfcfc7;
  }
}

.rt-04[data-theme="dark"],
.rt-04:has(.rt-04__theme-input:checked) {
  --rt-04-bg: #0a2c2c;
  --rt-04-bg: oklch(26% 0.045 195);
  --rt-04-panel: #cfcfc7;
}

@media (prefers-color-scheme: light) {
  .rt-04:has(.rt-04__theme-input:checked) {
    --rt-04-bg: #0a2c2c;
    --rt-04-bg: oklch(26% 0.045 195);
    --rt-04-panel: #cfcfc7;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-04:has(.rt-04__theme-input:checked) {
    --rt-04-bg: #008080;
    --rt-04-panel: #d8d8d0;
  }
}

.rt-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-04__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-04__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-04-face);
  color: #101010;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-light), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-shadow);
}

.rt-04__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-04__theme-input:focus-visible + .rt-04__theme-label {
  outline: 2px dotted var(--rt-04-dark);
  outline-offset: -6px;
}

.rt-04__stage {
  max-inline-size: 70rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.rt-04__head {
  display: grid;
  gap: 0.35rem;
  min-inline-size: 0;
}

.rt-04__kicker {
  margin: 0;
  font-family: var(--rt-04-mono);
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #f2fbfb;
}

.rt-04__h {
  margin: 0;
  font-size: clamp(1.3rem, 1rem + 1.9vw, 2.1rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  font-weight: 700;
  color: #ffffff;
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.45);
  min-inline-size: 0;
  text-wrap: balance;
}

.rt-04__board {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.rt-04__group {
  min-inline-size: 0;
  background: var(--rt-04-panel);
  padding: 1rem;
  display: grid;
  gap: 0.9rem;
  align-content: start;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-light), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-shadow);
}

.rt-04__group-h {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-04-ink-2);
}

.rt-04__states {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: 1rem;
}

.rt-04__demo {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  justify-items: start;
}

.rt-04__lbl {
  margin: 0;
  font-family: var(--rt-04-mono);
  font-size: 0.66rem;
  line-height: 1.45;
  color: var(--rt-04-ink-2);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-04__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.5rem 1.1rem;
  font: inherit;
  font-size: 0.9rem;
  cursor: pointer;
  background: var(--rt-04-face);
  color: #101010;
  border: 0;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-light), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-shadow);
}

.rt-04__btn:focus-visible {
  outline: 2px dotted #000000;
  outline-offset: -6px;
}

.rt-04__btn:active,
.rt-04__btn--pressed {
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-shadow), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-light);
  padding-block-start: calc(0.5rem + 1px);
  padding-inline-start: calc(1.1rem + 1px);
  padding-block-end: calc(0.5rem - 1px);
  padding-inline-end: calc(1.1rem - 1px);
}

.rt-04__btn--off {
  color: var(--rt-04-shadow);
  cursor: not-allowed;
  text-shadow: 1px 1px 0 var(--rt-04-hilite);
}

.rt-04__well {
  min-block-size: 44px;
  display: flex;
  align-items: center;
  padding: 0.5rem 0.85rem;
  background: #ffffff;
  color: #101010;
  font-size: 0.9rem;
  min-inline-size: 0;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-shadow), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-light);
}

.rt-04__well--sm {
  font-family: var(--rt-04-mono);
  font-size: 0.82rem;
  flex: 1 1 10rem;
}

.rt-04__explode {
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.rt-04__layer {
  min-inline-size: 0;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-family: var(--rt-04-mono);
  font-size: 0.72rem;
  padding: 0.6rem 0.7rem;
  background: var(--rt-04-face);
  color: #101010;
  overflow-wrap: anywhere;
}

.rt-04__layer span {
  inline-size: 22px;
  block-size: 22px;
  flex: none;
  display: grid;
  place-items: center;
  background: #101010;
  color: var(--rt-04-face);
  font-size: 0.7rem;
}

.rt-04__layer--1 {
  box-shadow: inset 0 3px 0 0 var(--rt-04-hilite), inset 3px 0 0 0 var(--rt-04-hilite);
}

.rt-04__layer--2 {
  box-shadow: inset 0 -3px 0 0 var(--rt-04-dark), inset -3px 0 0 0 var(--rt-04-dark);
}

.rt-04__layer--3 {
  box-shadow: inset 0 3px 0 0 var(--rt-04-light), inset 3px 0 0 0 var(--rt-04-light);
}

.rt-04__layer--4 {
  box-shadow: inset 0 -3px 0 0 var(--rt-04-shadow), inset -3px 0 0 0 var(--rt-04-shadow);
}

.rt-04__cap {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.5;
  color: var(--rt-04-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-04__win {
  min-inline-size: 0;
  background: var(--rt-04-face);
  padding: 3px;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-light), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-shadow);
}

.rt-04__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin: 3px;
  padding: 0.3rem 0.3rem 0.3rem 0.6rem;
  min-inline-size: 0;
  background: linear-gradient(90deg, var(--rt-04-title-a), var(--rt-04-title-b));
}

.rt-04__title-t {
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 700;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-04__title-btns {
  display: flex;
  gap: 3px;
  flex: none;
}

.rt-04__sysbtn {
  inline-size: 44px;
  block-size: 44px;
  padding: 0;
  border: 0;
  cursor: pointer;
  display: grid;
  place-items: center;
  font: inherit;
  font-size: 0.8rem;
  line-height: 1;
  background: var(--rt-04-face);
  color: #101010;
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-light), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-shadow);
}

.rt-04__sysbtn:active {
  box-shadow: inset var(--rt-04-b) var(--rt-04-b) 0 0 var(--rt-04-dark), inset calc(var(--rt-04-b) * -1) calc(var(--rt-04-b) * -1) 0 0 var(--rt-04-hilite), inset calc(var(--rt-04-b) * 2) calc(var(--rt-04-b) * 2) 0 0 var(--rt-04-shadow), inset calc(var(--rt-04-b) * -2) calc(var(--rt-04-b) * -2) 0 0 var(--rt-04-light);
}

.rt-04__sysbtn:focus-visible {
  outline: 2px dotted #000000;
  outline-offset: -7px;
}

.rt-04__body {
  padding: 1rem 0.75rem 0.85rem;
  display: grid;
  gap: 0.85rem;
  min-inline-size: 0;
}

.rt-04__text {
  margin: 0;
  font-size: 0.88rem;
  line-height: 1.5;
  color: #101010;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-04__field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.6rem;
  min-inline-size: 0;
}

.rt-04__field-l {
  font-size: 0.85rem;
  color: #101010;
  min-inline-size: 0;
}

.rt-04__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

@media (min-width: 54rem) {
  .rt-04__board {
    grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
  }
}
```
