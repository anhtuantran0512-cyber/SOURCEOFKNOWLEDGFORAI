---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/neo-brutalist-ui-components-examples/"
title: "Neo Brutalist Component Board"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A single board of components in the hard-edged neo-brutalist style &mdash; 3px black borders, solid offset shadows, clashing flats, no gradients and no radius."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo Brutalist Component Board
Source: https://codefronts.com/design-styles/css-retro-designs/neo-brutalist-ui-components-examples/

A single board of components in the hard-edged neo-brutalist style &mdash; 3px black borders, solid offset shadows, clashing flats, no gradients and no radius. It is deliberately one board rather than a component library, because the point here is the lineage: this is what the era's chunky, unapologetic chrome turned into once designers stopped apologising for it.
## HTML
```html
<section class="rt-12" aria-labelledby="rt-12-title">
  <h2 class="rt-12__sr" id="rt-12-title">Neo brutalist component board</h2>

  <div class="rt-12__theme">
    <input class="rt-12__theme-input" type="checkbox" id="rt-12-theme">
    <label class="rt-12__theme-label" for="rt-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-12__sr">Toggle dark ground</span>
    </label>
  </div>

  <div class="rt-12__stage">
    <header class="rt-12__head">
      <p class="rt-12__kicker">Lineage &middot; thick borders, flat fills, no ornament</p>
      <h3 class="rt-12__h">ONE BOARD.<br>NOT A KIT.</h3>
    </header>

    <div class="rt-12__board">
      <article class="rt-12__card rt-12__card--a">
        <h4 class="rt-12__card-h">Buttons</h4>
        <div class="rt-12__row">
          <button class="rt-12__btn" type="button">PRIMARY</button>
          <button class="rt-12__btn rt-12__btn--b" type="button">SECOND</button>
          <button class="rt-12__btn rt-12__btn--ghost" type="button">GHOST</button>
        </div>
        <p class="rt-12__note">Press translates by the shadow offset and drops the shadow. Footprint unchanged.</p>
      </article>

      <article class="rt-12__card rt-12__card--b">
        <h4 class="rt-12__card-h">Switch and tags</h4>
        <div class="rt-12__row">
          <span class="rt-12__switch">
            <input class="rt-12__switch-cb" type="checkbox" id="rt-12-sw" checked>
            <label class="rt-12__switch-lb" for="rt-12-sw"><span class="rt-12__knob" aria-hidden="true"></span>NOTIFY</label>
          </span>
        </div>
        <ul class="rt-12__tags">
          <li>FLAT</li><li>3PX</li><li>NO RADIUS</li><li>NO BLUR</li>
        </ul>
      </article>

      <article class="rt-12__card rt-12__card--c">
        <h4 class="rt-12__card-h">Stat</h4>
        <p class="rt-12__stat">147</p>
        <p class="rt-12__note">Offset shadows read as ink misregistration, not elevation.</p>
      </article>

      <article class="rt-12__card rt-12__card--d">
        <h4 class="rt-12__card-h">Notice</h4>
        <p class="rt-12__body">Every fill carries its own verified text colour. A single ink across five grounds does not pass.</p>
        <p class="rt-12__ratio">4.9:1 &middot; 8.2:1 &middot; 11.4:1</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-12 {
  --rt-12-off: 6px;
  --rt-12-bord: 3px;
  --rt-12-k: #0c0c0c;
  --rt-12-w: #ffffff;
  --rt-12-ink: #0c0c0c;
  --rt-12-ink-2: #43413a;
  --rt-12-a: #ffe500;
  --rt-12-b: #ff4d2d;
  --rt-12-c: #00d3c1;
  --rt-12-d: #b7a6ff;
  --rt-12-sans: ui-sans-serif, "Helvetica Neue", Helvetica, "Arial Black", Arial, sans-serif;
  --rt-12-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-12-bg: #f4f1e8;
  --rt-12-bg: oklch(95% 0.014 92);
  --rt-12-acc: #1f3bd8;
  --rt-12-acc: oklch(45% 0.22 265);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-12-bg);
  color: var(--rt-12-ink);
  font-family: var(--rt-12-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-12 *,
.rt-12 *::before,
.rt-12 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-12 {
    --rt-12-bg: #16150f;
    --rt-12-bg: oklch(19% 0.01 92);
    --rt-12-ink: #f4f1e8;
    --rt-12-ink-2: #cfcabb;
  }
}

.rt-12[data-theme="dark"],
.rt-12:has(.rt-12__theme-input:checked) {
  --rt-12-bg: #16150f;
  --rt-12-bg: oklch(19% 0.01 92);
  --rt-12-ink: #f4f1e8;
  --rt-12-ink-2: #cfcabb;
}

@media (prefers-color-scheme: light) {
  .rt-12:has(.rt-12__theme-input:checked) {
    --rt-12-bg: #16150f;
    --rt-12-bg: oklch(19% 0.01 92);
    --rt-12-ink: #f4f1e8;
    --rt-12-ink-2: #cfcabb;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-12:has(.rt-12__theme-input:checked) {
    --rt-12-bg: #f4f1e8;
    --rt-12-bg: oklch(95% 0.014 92);
  }
}

.rt-12__sr {
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

.rt-12__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-12__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-12-a);
  color: var(--rt-12-k);
  border: var(--rt-12-bord) solid var(--rt-12-k);
  box-shadow: var(--rt-12-off) var(--rt-12-off) 0 0 var(--rt-12-k);
}

.rt-12__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-12__theme-input:focus-visible + .rt-12__theme-label {
  outline: 3px solid var(--rt-12-acc);
  outline-offset: 3px;
}

.rt-12__stage {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(3.75rem, 3rem + 3vw, 5rem) clamp(0.9rem, 0.6rem + 2vw, 2rem) calc(4rem + var(--rt-12-off));
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.75rem;
}

.rt-12__head {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
}

.rt-12__kicker {
  margin: 0;
  font-family: var(--rt-12-mono);
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.rt-12__h {
  margin: 0;
  font-size: clamp(2rem, 1rem + 6vw, 4rem);
  line-height: 0.94;
  font-weight: 900;
  letter-spacing: -0.045em;
  text-transform: uppercase;
  text-wrap: balance;
  min-inline-size: 0;
}

.rt-12__board {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: calc(var(--rt-12-off) * 2.5);
}

.rt-12__card {
  min-inline-size: 0;
  border: var(--rt-12-bord) solid var(--rt-12-k);
  box-shadow: var(--rt-12-off) var(--rt-12-off) 0 0 var(--rt-12-k);
  padding: clamp(1rem, 0.75rem + 1.2vw, 1.4rem);
  display: grid;
  gap: 0.85rem;
  align-content: start;
}

.rt-12__card--a {
  background: var(--rt-12-a);
  color: var(--rt-12-k);
}

.rt-12__card--b {
  background: var(--rt-12-w);
  color: var(--rt-12-k);
}

.rt-12__card--c {
  background: var(--rt-12-b);
  color: var(--rt-12-k);
}

.rt-12__card--d {
  background: var(--rt-12-c);
  color: var(--rt-12-k);
}

.rt-12__card-h {
  margin: 0;
  font-size: 0.75rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 800;
}

.rt-12__row {
  display: flex;
  flex-wrap: wrap;
  gap: calc(var(--rt-12-off) * 2);
}

.rt-12__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 0.65rem 1.1rem;
  cursor: pointer;
  font: inherit;
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  background: var(--rt-12-k);
  color: var(--rt-12-w);
  border: var(--rt-12-bord) solid var(--rt-12-k);
  box-shadow: var(--rt-12-off) var(--rt-12-off) 0 0 var(--rt-12-k);
  transition: transform 60ms linear, box-shadow 60ms linear;
}

.rt-12__btn--b {
  background: var(--rt-12-d);
  color: var(--rt-12-k);
}

.rt-12__btn--ghost {
  background: transparent;
  color: var(--rt-12-k);
}

.rt-12__btn:hover {
  transform: translate(2px, 2px);
  box-shadow: calc(var(--rt-12-off) - 2px) calc(var(--rt-12-off) - 2px) 0 0 var(--rt-12-k);
}

.rt-12__btn:active {
  transform: translate(var(--rt-12-off), var(--rt-12-off));
  box-shadow: none;
}

.rt-12__btn:focus-visible {
  outline: 3px solid var(--rt-12-acc);
  outline-offset: 3px;
}

.rt-12__switch {
  position: relative;
  display: inline-block;
}

.rt-12__switch-cb {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 44px;
  block-size: 44px;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.rt-12__switch-lb {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 44px;
  padding: 0.4rem 0.8rem 0.4rem 0.4rem;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  border: var(--rt-12-bord) solid var(--rt-12-k);
  background: var(--rt-12-w);
  box-shadow: var(--rt-12-off) var(--rt-12-off) 0 0 var(--rt-12-k);
}

.rt-12__knob {
  inline-size: 44px;
  block-size: 26px;
  flex: none;
  background: var(--rt-12-w);
  border: var(--rt-12-bord) solid var(--rt-12-k);
  position: relative;
}

.rt-12__knob::after {
  content: "";
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 50%;
  background: var(--rt-12-k);
  transition: inset-inline-start 80ms linear;
}

.rt-12__switch-cb:checked + .rt-12__switch-lb .rt-12__knob {
  background: var(--rt-12-c);
}

.rt-12__switch-cb:checked + .rt-12__switch-lb .rt-12__knob::after {
  inset-inline-start: 50%;
}

.rt-12__switch-cb:focus-visible + .rt-12__switch-lb {
  outline: 3px solid var(--rt-12-acc);
  outline-offset: 3px;
}

.rt-12__tags {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.rt-12__tags li {
  font-family: var(--rt-12-mono);
  font-size: 0.68rem;
  letter-spacing: 0.08em;
  padding: 0.35rem 0.55rem;
  border: var(--rt-12-bord) solid var(--rt-12-k);
  background: var(--rt-12-a);
  color: var(--rt-12-k);
}

.rt-12__stat {
  margin: 0;
  font-size: clamp(3rem, 2rem + 6vw, 5rem);
  line-height: 0.85;
  font-weight: 900;
  letter-spacing: -0.05em;
}

.rt-12__note,
.rt-12__body {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.5;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-12__ratio {
  margin: 0;
  font-family: var(--rt-12-mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
}

@media (min-width: 44rem) {
  .rt-12__board {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (prefers-reduced-motion: reduce) {
  .rt-12__btn,
    .rt-12__knob::after {
    transition: none;
  }
}
```
