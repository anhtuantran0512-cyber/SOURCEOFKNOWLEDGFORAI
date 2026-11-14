---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/tab-stack/"
title: "Tab Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "Styled exactly like file-cabinet divider folders: the card bodies hide behind the front folder while custom-coloured top tabs stay clickable, letting you…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tab Stack
Source: https://codefronts.com/components/css-stacked-cards/tab-stack/

Styled exactly like file-cabinet divider folders: the card bodies hide behind the front folder while custom-coloured top tabs stay clickable, letting you flip between layers instantly. A nostalgic, information-dense organiser pattern.
## HTML
```html
<section class="scd-18" aria-label="File folder tab stack">
  <div class="scd-18__cab">
    <input type="radio" name="scd-18" id="scd-18-1" class="scd-18__r" checked>
    <input type="radio" name="scd-18" id="scd-18-2" class="scd-18__r">
    <input type="radio" name="scd-18" id="scd-18-3" class="scd-18__r">
    <label class="scd-18__tab" for="scd-18-1" style="--c:oklch(0.72 0.14 60);--l:0">2024</label>
    <label class="scd-18__tab" for="scd-18-2" style="--c:oklch(0.72 0.13 150);--l:1">2025</label>
    <label class="scd-18__tab" for="scd-18-3" style="--c:oklch(0.72 0.13 250);--l:2">2026</label>
    <article class="scd-18__file" style="--c:oklch(0.72 0.14 60)"><h3>FY2024</h3><p>Revenue $2.1M · 14 clients · 3 new hires. The year we found product-market fit.</p></article>
    <article class="scd-18__file" style="--c:oklch(0.72 0.13 150)"><h3>FY2025</h3><p>Revenue $5.4M · 38 clients · shipped the platform rewrite on time.</p></article>
    <article class="scd-18__file" style="--c:oklch(0.72 0.13 250)"><h3>FY2026</h3><p>Revenue $9.0M projected · expanding to EU · Series A closed in Q1.</p></article>
  </div>
</section>
```
## CSS
```css
.scd-18,
.scd-18 *,
.scd-18 *::before,
.scd-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-18 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #2a2620;
}

.scd-18__cab {
  position: relative;
  width: min(420px,100%);
  height: 260px;
  padding-top: 38px;
}

.scd-18__r {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.scd-18__tab {
  position: absolute;
  top: 0;
  left: calc(var(--l) * 33.3%);
  width: 32%;
  height: 42px;
  padding-bottom: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 14px;
  color: #3a3020;
  background: var(--c);
  clip-path: polygon(8% 0,92% 0,100% 100%,0 100%);
  cursor: pointer;
  filter: brightness(.82);
  transition: filter .25s,transform .25s;
  z-index: 5;
}

.scd-18__tab:hover {
  filter: brightness(.94);
}

.scd-18__file {
  position: absolute;
  left: 0;
  right: 0;
  top: 36px;
  height: 220px;
  padding: 26px;
  border-radius: 2px 8px 8px 8px;
  background: var(--c);
  color: #2a2415;
  box-shadow: 0 20px 40px -24px rgba(0,0,0,.7);
  z-index: 1;
  opacity: .5;
}

.scd-18__file h3 {
  font-size: 24px;
  font-weight: 900;
  margin-bottom: 10px;
}

.scd-18__file p {
  font-size: 15px;
  line-height: 1.6;
  max-width: 36ch;
}

.scd-18__r:nth-of-type(1):checked ~ .scd-18__tab:nth-of-type(1),
.scd-18__r:nth-of-type(2):checked ~ .scd-18__tab:nth-of-type(2),
.scd-18__r:nth-of-type(3):checked ~ .scd-18__tab:nth-of-type(3) {
  filter: brightness(1);
  transform: translateY(-4px);
}

.scd-18__r:nth-of-type(1):checked ~ .scd-18__file:nth-of-type(1),
.scd-18__r:nth-of-type(2):checked ~ .scd-18__file:nth-of-type(2),
.scd-18__r:nth-of-type(3):checked ~ .scd-18__file:nth-of-type(3) {
  z-index: 4;
  opacity: 1;
}

.scd-18__r:nth-of-type(1):focus-visible ~ .scd-18__tab:nth-of-type(1),
.scd-18__r:nth-of-type(2):focus-visible ~ .scd-18__tab:nth-of-type(2),
.scd-18__r:nth-of-type(3):focus-visible ~ .scd-18__tab:nth-of-type(3) {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-18__tab {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — clip-path shapes the manila tabs; a radio :checked state machine raises one folder body to the front while all tabs stay clickable. */
```
