---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/color-block/"
title: "Color Block Horizontal Accordion — Bold Flat Panels for Feature Sections"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Four saturated color fields, edge to edge, each owning one product pillar: the active block expands and reveals its manifesto line in huge type while…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color Block Horizontal Accordion — Bold Flat Panels for Feature Sections
Source: https://codefronts.com/navigation/css-accordions/color-block/

Four saturated color fields, edge to edge, each owning one product pillar: the active block expands and reveals its manifesto line in huge type while collapsed blocks show only a rotated word. Flat, loud and grid-tight — a landing-page feature section disguised as an accordion.
## HTML
```html
<section class="acc-17" aria-label="Color block horizontal accordion demo">
  <div class="acc-17__row" role="group" aria-label="Product pillars">
    <div class="acc-17__panel" style="--c:oklch(0.62 0.21 30);--ink:#fff">
      <input type="radio" name="acc-17" id="acc-17-a" checked>
      <label class="acc-17__face" for="acc-17-a"><span class="acc-17__word">Fast</span>
        <span class="acc-17__big"><b>Fast</b><p>Cold start to first byte in 40ms, everywhere on earth.</p></span>
      </label>
    </div>
    <div class="acc-17__panel" style="--c:oklch(0.85 0.16 90);--ink:#3a2c00">
      <input type="radio" name="acc-17" id="acc-17-b">
      <label class="acc-17__face" for="acc-17-b"><span class="acc-17__word">Simple</span>
        <span class="acc-17__big"><b>Simple</b><p>One config file. Twelve keys. You'll memorize all of them.</p></span>
      </label>
    </div>
    <div class="acc-17__panel" style="--c:oklch(0.45 0.13 260);--ink:#fff">
      <input type="radio" name="acc-17" id="acc-17-c">
      <label class="acc-17__face" for="acc-17-c"><span class="acc-17__word">Safe</span>
        <span class="acc-17__big"><b>Safe</b><p>Every deploy is a snapshot. Rollback is one click, always.</p></span>
      </label>
    </div>
    <div class="acc-17__panel" style="--c:oklch(0.55 0.14 165);--ink:#fff">
      <input type="radio" name="acc-17" id="acc-17-d">
      <label class="acc-17__face" for="acc-17-d"><span class="acc-17__word">Open</span>
        <span class="acc-17__big"><b>Open</b><p>MIT licensed, self-hostable, and the cloud runs the same code.</p></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-17,
.acc-17 *,
.acc-17 *::before,
.acc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-17 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #16151a;
  padding: 44px 24px;
}

.acc-17__row {
  display: flex;
  width: min(860px,100%);
  height: 400px;
  border-radius: 18px;
  overflow: hidden;
}

.acc-17__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 60px;
  container-type: inline-size;
  transition: flex-grow .5s cubic-bezier(.4,0,.2,1);
}

.acc-17__panel:has(input:checked) {
  flex-grow: 5;
}

.acc-17__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-17__face {
  position: relative;
  flex: 1;
  display: block;
  background: var(--c);
  color: var(--ink);
  cursor: pointer;
  overflow: hidden;
  box-shadow: inset -1px 0 0 rgba(0,0,0,.15);
  transition: filter .25s;
}

.acc-17__face:hover {
  filter: brightness(1.06);
}

.acc-17__word {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 20px 0;
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  opacity: .85;
  transition: opacity .25s;
}

.acc-17__panel:has(input:checked) .acc-17__word {
  opacity: 0;
}

.acc-17__big {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 10px;
  padding: 30px;
  opacity: 0;
  translate: 0 10px;
  transition: opacity .3s .18s,translate .3s .18s;
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--ink) 30%,transparent);
}

.acc-17__panel:has(input:checked) .acc-17__big {
  opacity: 1;
  translate: 0 0;
}

.acc-17__big b {
  font-size: clamp(28px,14cqw,54px);
  font-weight: 850;
  letter-spacing: -.03em;
  line-height: 1;
}

.acc-17__big p {
  font-size: 15px;
  line-height: 1.55;
  max-width: 34ch;
  opacity: .9;
}

.acc-17__panel:has(input:focus-visible) .acc-17__face {
  outline: 3px solid #fff;
  outline-offset: -6px;
}

@media (max-width: 600px) {
  .acc-17__row {
    flex-direction: column;
    height: auto;
  }

  .acc-17__panel {
    min-height: 60px;
  }

  .acc-17__panel:has(input:checked) {
    min-height: 240px;
  }

  .acc-17__word {
    writing-mode: horizontal-tb;
    rotate: none;
    align-items: center;
    justify-content: flex-start;
    padding: 0 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-17__panel,
    .acc-17__word,
    .acc-17__big {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — gapless flex stripes expand via flex-grow on :has(input:checked); each stripe carries a hand-contrast-checked --c/--ink pair, and headlines scale with panel width using cqw container units. */
```
