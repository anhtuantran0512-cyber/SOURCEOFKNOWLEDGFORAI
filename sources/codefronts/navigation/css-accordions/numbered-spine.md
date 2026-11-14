---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/numbered-spine/"
title: "Numbered Spine Horizontal Accordion — Editorial Magazine Index"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "A magazine table-of-contents turned interactive: cream paper, hairline column rules, and giant ghosted numerals 1–4 stacked in each collapsed spine."
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Numbered Spine Horizontal Accordion — Editorial Magazine Index
Source: https://codefronts.com/navigation/css-accordions/numbered-spine/

A magazine table-of-contents turned interactive: cream paper, hairline column rules, and giant ghosted numerals 1–4 stacked in each collapsed spine. The open column lays its numeral behind a serif headline and dek like an art-directed spread. Quiet, typographic, and unlike any card-based accordion.
## HTML
```html
<section class="acc-18" aria-label="Numbered spine editorial accordion demo">
  <div class="acc-18__row" role="group" aria-label="Issue contents">
    <div class="acc-18__panel">
      <input type="radio" name="acc-18" id="acc-18-a" checked>
      <label class="acc-18__face" for="acc-18-a"><span class="acc-18__num">1</span><span class="acc-18__spine">The Interview</span>
        <span class="acc-18__spread"><b>The last typesetter of Fleet Street</b><p>Sixty years of hot metal, and what the craft knew that the software forgot.</p><i>By M. Okafor · 18 min</i></span>
      </label>
    </div>
    <div class="acc-18__panel">
      <input type="radio" name="acc-18" id="acc-18-b">
      <label class="acc-18__face" for="acc-18-b"><span class="acc-18__num">2</span><span class="acc-18__spine">Field Report</span>
        <span class="acc-18__spread"><b>Notes from the seed vault</b><p>Inside the arctic archive where every harvest on earth keeps a backup copy.</p><i>By T. Lindqvist · 12 min</i></span>
      </label>
    </div>
    <div class="acc-18__panel">
      <input type="radio" name="acc-18" id="acc-18-c">
      <label class="acc-18__face" for="acc-18-c"><span class="acc-18__num">3</span><span class="acc-18__spine">Essay</span>
        <span class="acc-18__spread"><b>In defence of the long way</b><p>On slowness as a design material, and why the fastest path is rarely the best one.</p><i>By A. Fontaine · 9 min</i></span>
      </label>
    </div>
    <div class="acc-18__panel">
      <input type="radio" name="acc-18" id="acc-18-d">
      <label class="acc-18__face" for="acc-18-d"><span class="acc-18__num">4</span><span class="acc-18__spine">Archive</span>
        <span class="acc-18__spread"><b>The 1961 letters</b><p>A rediscovered correspondence between two rival foundries, annotated.</p><i>Edited by the staff · 15 min</i></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-18,
.acc-18 *,
.acc-18 *::before,
.acc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-18 {
  --ink: #211d16;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f1e8;
  padding: 44px 24px;
}

.acc-18__row {
  display: flex;
  width: min(860px,100%);
  height: 420px;
  border-block: 2px solid var(--ink);
}

.acc-18__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 76px;
  transition: flex-grow .55s cubic-bezier(.4,0,.2,1);
}

.acc-18__panel + .acc-18__panel {
  border-left: 1px solid #d8d0bd;
}

.acc-18__panel:has(input:checked) {
  flex-grow: 5;
}

.acc-18__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-18__face {
  position: relative;
  flex: 1;
  display: block;
  cursor: pointer;
  overflow: hidden;
  transition: background .3s;
}

.acc-18__face:hover {
  background: #efe9dc;
}

.acc-18__num {
  position: absolute;
  left: 10px;
  top: 0;
  font-family: Georgia,serif;
  font-size: 140px;
  line-height: 1;
  font-weight: 700;
  color: color-mix(in oklab,var(--ink) 9%,transparent);
  transition: font-size .55s cubic-bezier(.4,0,.2,1),left .55s;
  z-index: 0;
}

.acc-18__panel:has(input:checked) .acc-18__num {
  font-size: 230px;
  left: 18px;
}

.acc-18__spine {
  position: absolute;
  bottom: 18px;
  left: 50%;
  translate: -50% 0;
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #8a8069;
  transition: opacity .25s;
}

.acc-18__panel:has(input:checked) .acc-18__spine {
  opacity: 0;
}

.acc-18__spread {
  position: absolute;
  inset: 0;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 10px;
  padding: 28px;
  opacity: 0;
  translate: 0 10px;
  transition: opacity .35s .2s,translate .35s .2s;
}

.acc-18__panel:has(input:checked) .acc-18__spread {
  opacity: 1;
  translate: 0 0;
}

.acc-18__spread b {
  font-family: Georgia,serif;
  font-size: clamp(22px,3vw,30px);
  font-weight: 700;
  line-height: 1.15;
  color: var(--ink);
  letter-spacing: -.01em;
  max-width: 22ch;
}

.acc-18__spread p {
  font-size: 14px;
  line-height: 1.6;
  color: #5c5443;
  max-width: 44ch;
}

.acc-18__spread i {
  font-style: normal;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: #8a8069;
}

.acc-18__panel:has(input:focus-visible) .acc-18__face {
  outline: 3px solid var(--ink);
  outline-offset: -6px;
}

@media (max-width: 620px) {
  .acc-18__row {
    flex-direction: column;
    height: auto;
    border-block: none;
  }

  .acc-18__panel {
    min-height: 70px;
  }

  .acc-18__panel + .acc-18__panel {
    border-left: none;
    border-top: 1px solid #d8d0bd;
  }

  .acc-18__panel:has(input:checked) {
    min-height: 280px;
  }

  .acc-18__spine {
    writing-mode: horizontal-tb;
    rotate: none;
    left: auto;
    right: 18px;
    bottom: auto;
    top: 24px;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-18__panel,
    .acc-18__num,
    .acc-18__spread {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one persistent ghost numeral per panel transitions its font-size as the flex column expands, so the number appears to grow into the open editorial spread. */
```
