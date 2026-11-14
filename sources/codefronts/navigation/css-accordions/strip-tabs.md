---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/strip-tabs/"
title: "Horizontal Strip Tabs Accordion — Vertical Text Columns with flex-grow"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The foundational horizontal accordion: collapsed columns show their titles rotated with writing-mode: vertical-rl; selecting a strip animates flex-grow so it…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Strip Tabs Accordion — Vertical Text Columns with flex-grow
Source: https://codefronts.com/navigation/css-accordions/strip-tabs/

The foundational horizontal accordion: collapsed columns show their titles rotated with writing-mode: vertical-rl; selecting a strip animates flex-grow so it expands sideways while siblings compress. Radio-driven (arrow-key navigable), with content that fades in only after the column has room.
## HTML
```html
<section class="acc-15" aria-label="Horizontal strip tabs accordion demo">
  <div class="acc-15__row" role="group" aria-label="Choose a studio location">
    <div class="acc-15__panel">
      <input type="radio" name="acc-15" id="acc-15-a" checked>
      <label class="acc-15__face" for="acc-15-a"><span class="acc-15__strip">Copenhagen</span>
        <span class="acc-15__content"><b>Copenhagen</b><i>HQ · est. 2019</i><p>Fourteen people over a bike shop in Nørrebro. Product, engineering and the espresso machine that started the company.</p></span>
      </label>
    </div>
    <div class="acc-15__panel">
      <input type="radio" name="acc-15" id="acc-15-b">
      <label class="acc-15__face" for="acc-15-b"><span class="acc-15__strip">Toronto</span>
        <span class="acc-15__content"><b>Toronto</b><i>Americas · est. 2022</i><p>Customer engineering and support, covering every timezone from UTC−8 to −3. The office dog is named Pixel.</p></span>
      </label>
    </div>
    <div class="acc-15__panel">
      <input type="radio" name="acc-15" id="acc-15-c">
      <label class="acc-15__face" for="acc-15-c"><span class="acc-15__strip">Melbourne</span>
        <span class="acc-15__content"><b>Melbourne</b><i>APAC · est. 2024</i><p>Our newest studio: three engineers, one designer, and the best coffee of the three offices — a contested claim.</p></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-15,
.acc-15 *,
.acc-15 *::before,
.acc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-15 {
  --accent: oklch(0.55 0.15 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef1f6;
  padding: 44px 24px;
}

.acc-15__row {
  display: flex;
  gap: 10px;
  width: min(720px,100%);
  height: 380px;
}

.acc-15__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 64px;
  transition: flex-grow .5s cubic-bezier(.4,0,.2,1);
}

.acc-15__panel:has(input:checked) {
  flex-grow: 6;
}

.acc-15__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-15__face {
  position: relative;
  flex: 1;
  display: block;
  background: #fff;
  border: 1.5px solid #dde2ec;
  border-radius: 16px;
  cursor: pointer;
  overflow: hidden;
  transition: border-color .3s,background .3s;
}

.acc-15__panel:has(input:checked) .acc-15__face {
  border-color: var(--accent);
  background: #fff;
}

.acc-15__face:hover {
  border-color: #b9c3d8;
}

.acc-15__strip {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  writing-mode: vertical-rl;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #8a93ab;
  transition: opacity .25s;
  padding: 18px 0;
}

.acc-15__panel:has(input:checked) .acc-15__strip {
  opacity: 0;
}

.acc-15__content {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 6px;
  padding: 26px;
  opacity: 0;
  transition: opacity .3s .18s;
}

.acc-15__panel:has(input:checked) .acc-15__content {
  opacity: 1;
}

.acc-15__content b {
  font-size: 24px;
  font-weight: 800;
  color: #1b2338;
  letter-spacing: -.02em;
}

.acc-15__content i {
  font-style: normal;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--accent);
}

.acc-15__content p {
  font-size: 14px;
  line-height: 1.6;
  color: #4c5674;
  max-width: 38ch;
}

.acc-15__panel:has(input:focus-visible) .acc-15__face {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 560px) {
  .acc-15__row {
    flex-direction: column;
    height: auto;
  }

  .acc-15__panel {
    min-height: 64px;
  }

  .acc-15__panel:has(input:checked) {
    min-height: 240px;
  }

  .acc-15__strip {
    writing-mode: horizontal-tb;
    justify-content: flex-start;
    padding: 0 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-15__panel,
    .acc-15__strip,
    .acc-15__content {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hidden radios drive :has(input:checked) panel expansion via a flex-grow transition; arrow keys navigate the radio group natively, and content opacity is delayed until the column has width. */
```
