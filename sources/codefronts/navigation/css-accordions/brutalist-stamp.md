---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/brutalist-stamp/"
title: "Brutalist Stamp Accordion — Bold Borders, Hard Shadows, Zero Subtlety"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Neo-brutalism for disclosure: 3px black borders, an offset hard shadow that the open item physically 'presses' flat, uppercase mono labels, a stamped index…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Stamp Accordion — Bold Borders, Hard Shadows, Zero Subtlety
Source: https://codefronts.com/navigation/css-accordions/brutalist-stamp/

Neo-brutalism for disclosure: 3px black borders, an offset hard shadow that the open item physically 'presses' flat, uppercase mono labels, a stamped index chip and an unapologetic yellow page. The open interaction feels mechanical — click, CLUNK — perfect for portfolios, zines and dev-tool brands.
## HTML
```html
<section class="acc-11" aria-label="Brutalist stamp accordion demo">
  <div class="acc-11__wrap">
    <h3 class="acc-11__title">FAQ_</h3>
    <details class="acc-11__item" open>
      <summary class="acc-11__sum"><span class="acc-11__chip">01</span>WHAT IS THIS?<span class="acc-11__arrow">▼</span></summary>
      <div class="acc-11__body"><p>A weekly zine about the unpolished web — view-source culture, personal sites, and software with opinions. Printed badly on purpose.</p></div>
    </details>
    <details class="acc-11__item">
      <summary class="acc-11__sum"><span class="acc-11__chip">02</span>HOW MUCH?<span class="acc-11__arrow">▼</span></summary>
      <div class="acc-11__body"><p>Free online. $5 for the paper edition, which is photocopied, stapled crooked, and mailed with a sticker.</p></div>
    </details>
    <details class="acc-11__item">
      <summary class="acc-11__sum"><span class="acc-11__chip">03</span>CAN I SUBMIT?<span class="acc-11__arrow">▼</span></summary>
      <div class="acc-11__body"><p>Yes. 500 words max, no pitches, no PDFs. Send plain text or a URL. If it needs a cookie banner, it's a no.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-11,
.acc-11 *,
.acc-11 *::before,
.acc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-11 {
  --ink: #111;
  --paper: #ffe14d;
  --shadow: 6px;
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--paper);
  padding: 44px 24px;
}

.acc-11__wrap {
  width: min(560px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.acc-11__title {
  font-size: 34px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.02em;
}

.acc-11__item {
  background: #fff;
  border: 3px solid var(--ink);
  box-shadow: var(--shadow) var(--shadow) 0 var(--ink);
  transition: translate .12s ease-out,box-shadow .12s ease-out;
}

.acc-11__item:hover {
  translate: 2px 2px;
  box-shadow: 4px 4px 0 var(--ink);
}

.acc-11__item[open] {
  translate: 4px 4px;
  box-shadow: 2px 2px 0 var(--ink);
}

.acc-11__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 8px 16px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .08em;
  color: var(--ink);
  cursor: pointer;
}

.acc-11__sum::-webkit-details-marker {
  display: none;
}

.acc-11__sum::marker {
  content: "";
}

.acc-11__chip {
  display: grid;
  place-content: center;
  width: 34px;
  height: 34px;
  border: 3px solid var(--ink);
  font-size: 13px;
  background: #fff;
  transition: background .12s,color .12s;
  flex: none;
}

.acc-11__item[open] .acc-11__chip {
  background: var(--ink);
  color: var(--paper);
}

.acc-11__arrow {
  margin-left: auto;
  font-size: 13px;
  transition: rotate .18s ease-out;
}

.acc-11__item[open] .acc-11__arrow {
  rotate: 180deg;
}

.acc-11__body {
  border-top: 3px solid var(--ink);
  padding: 16px;
  font-size: 14px;
  line-height: 1.7;
  color: #2a2a2a;
  background: repeating-linear-gradient(0deg,#fff 0 27px,#f4f0e4 27px 28px);
}

.acc-11__sum:focus-visible {
  outline: 4px solid var(--ink);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-11__item,
    .acc-11__arrow {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details[open] translates the slab 4px while its hard shadow shrinks the same amount, so the card visually presses into the page like a mechanical key. */
```
