---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/claymorphism-vs-neumorphism-side-by-side/"
title: "Claymorphism vs Neumorphism Side by Side"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "The comparison people actually search for, built as two identical cards that differ only in shadow strategy — extruded-from-the-page neumorphism on the left,…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Claymorphism vs Neumorphism Side by Side
Source: https://codefronts.com/design-styles/css-claymorphism/claymorphism-vs-neumorphism-side-by-side/

The comparison people actually search for, built as two identical cards that differ only in shadow strategy — extruded-from-the-page neumorphism on the left, lifted-object claymorphism on the right — with a swap toggle that applies one style to the other card so you can see the same content both ways, and a spec table covering fill, shadow, contrast and accessibility.
## HTML
```html
<section class="cl-04" aria-label="Claymorphism versus neumorphism side by side comparison">
  <div class="cl-04__stage">
    <header class="cl-04__head">
      <h2 class="cl-04__h">Clay vs Neu — same card, two depth models</h2>
      <div class="cl-04__swap">
        <input class="cl-04__chk" type="checkbox" id="cl-04-swap">
        <label class="cl-04__lab" for="cl-04-swap"><span class="cl-04__knob" aria-hidden="true"></span>Apply clay tokens to both</label>
      </div>
    </header>
    <div class="cl-04__pair">
      <article class="cl-04__card cl-04__card--neu">
        <p class="cl-04__kind">Neumorphism</p>
        <h3 class="cl-04__title">Soft UI</h3>
        <p class="cl-04__body">The object is the page, extruded. Fill matches the background; two mirrored outset shadows do all the work.</p>
        <dl class="cl-04__specs">
          <div><dt>Fill</dt><dd>= page color</dd></div>
          <div><dt>Shadows</dt><dd>2 outset, mirrored</dd></div>
          <div><dt>Radius</dt><dd>12–20px</dd></div>
          <div><dt>Contrast</dt><dd>shadow only · risky</dd></div>
        </dl>
        <button class="cl-04__btn" type="button">Press me</button>
      </article>
      <article class="cl-04__card cl-04__card--clay">
        <p class="cl-04__kind">Claymorphism</p>
        <h3 class="cl-04__title">Clay UI</h3>
        <p class="cl-04__body">A separate object on the page. Own fill, outer drop for mass, two insets for thickness and sheen.</p>
        <dl class="cl-04__specs">
          <div><dt>Fill</dt><dd>lighter than page</dd></div>
          <div><dt>Shadows</dt><dd>1 outset + 2 inset</dd></div>
          <div><dt>Radius</dt><dd>28–48px</dd></div>
          <div><dt>Contrast</dt><dd>real fill · testable</dd></div>
        </dl>
        <button class="cl-04__btn" type="button">Press me</button>
      </article>
    </div>
    <p class="cl-04__chip" aria-hidden="true">same markup · token-only difference · :has() swap</p>
  </div>
</section>
```
## CSS
```css
.cl-04,
.cl-04 *,
.cl-04 *::before,
.cl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-04-bg);
  --cl-04-bg: oklch(0.93 0.015 265);
  --cl-04-light: oklch(1 0 0/.92);
  --cl-04-shade: oklch(0.62 0.06 265/.55);
  --cl-04-ink: oklch(0.31 0.03 265);
  --cl-04-mut: oklch(0.53 0.03 265);
  --cl-04-clay: oklch(0.84 0.1 275);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-04-ink);
}

.cl-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,4vw,36px);
  padding: clamp(22px,5vw,60px);
}

.cl-04__head {
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  max-width: 60ch;
}

.cl-04__h {
  font-size: clamp(23px,3.6vw,34px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-04__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-04__lab {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  min-height: 48px;
  padding: 0 22px 0 12px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 620;
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-04-bg) 86%,white);
  box-shadow: 0 12px 22px -14px var(--cl-04-shade),inset 0 -8px 14px -10px var(--cl-04-shade),inset 0 10px 14px -8px var(--cl-04-light);
  transition: box-shadow .3s;
}

.cl-04__knob {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--cl-04-bg) 70%,white);
  box-shadow: inset 0 -6px 10px -7px var(--cl-04-shade),inset 0 8px 10px -6px var(--cl-04-light);
  transition: background .3s,scale .3s cubic-bezier(.34,1.4,.5,1);
}

.cl-04__chk:checked+.cl-04__lab .cl-04__knob {
  background: var(--cl-04-clay);
  scale: 1.06;
}

.cl-04__chk:focus-visible+.cl-04__lab {
  outline: 3px solid var(--cl-04-ink);
  outline-offset: 3px;
}

.cl-04__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(268px,1fr));
  gap: clamp(18px,3vw,32px);
  width: min(100%,880px);
}

.cl-04__card {
  display: grid;
  gap: 12px;
  align-content: start;
  padding: clamp(22px,3vw,32px);
  transition: translate .4s cubic-bezier(.34,1.3,.5,1),box-shadow .45s,background .45s,border-radius .45s;
}

.cl-04__card:hover {
  translate: 0 -6px;
}

.cl-04__card--neu {
  border-radius: 18px;
  background: var(--cl-04-bg);
  box-shadow: -9px -9px 18px var(--cl-04-light),9px 9px 20px var(--cl-04-shade);
}

.cl-04__card--clay {
  border-radius: 38px;
  background: var(--cl-04-clay);
  box-shadow: 0 26px 46px -16px var(--cl-04-shade),inset 0 -16px 26px -12px var(--cl-04-shade),inset 0 18px 26px -8px var(--cl-04-light);
}

.cl-04:has(#cl-04-swap:checked) .cl-04__card--neu {
  border-radius: 38px;
  background: var(--cl-04-clay);
  box-shadow: 0 26px 46px -16px var(--cl-04-shade),inset 0 -16px 26px -12px var(--cl-04-shade),inset 0 18px 26px -8px var(--cl-04-light);
}

.cl-04__kind {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--cl-04-mut);
}

.cl-04__title {
  font-size: 21px;
  font-weight: 740;
  letter-spacing: -.015em;
}

.cl-04__body {
  font-size: 14px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--cl-04-ink) 82%,transparent);
  text-wrap: pretty;
}

.cl-04__specs {
  display: grid;
  gap: 8px;
  margin-top: 4px;
  font-size: 13px;
}

.cl-04__specs div {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid color-mix(in oklch,var(--cl-04-ink) 12%,transparent);
}

.cl-04__specs dt {
  font-weight: 640;
  color: var(--cl-04-mut);
}

.cl-04__specs dd {
  text-align: right;
}

.cl-04__btn {
  justify-self: start;
  min-height: 46px;
  margin-top: 6px;
  padding: 0 24px;
  border: 0;
  border-radius: inherit;
  font: inherit;
  font-size: 14px;
  font-weight: 660;
  color: var(--cl-04-ink);
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-04-bg) 80%,white);
  box-shadow: 0 10px 18px -12px var(--cl-04-shade),inset 0 -8px 12px -9px var(--cl-04-shade),inset 0 9px 12px -7px var(--cl-04-light);
  transition: translate .18s,box-shadow .18s;
}

.cl-04__card--neu .cl-04__btn {
  border-radius: 14px;
}

.cl-04__card--clay .cl-04__btn {
  border-radius: 22px;
}

.cl-04__btn:active {
  translate: 0 3px;
  box-shadow: inset 0 8px 14px -8px var(--cl-04-shade),inset 0 -6px 12px -9px var(--cl-04-light);
}

.cl-04__btn:focus-visible {
  outline: 3px solid var(--cl-04-ink);
  outline-offset: 3px;
}

.cl-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-04-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-04-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-04 * {
    transition-duration: .01ms !important;
  }
}
```
