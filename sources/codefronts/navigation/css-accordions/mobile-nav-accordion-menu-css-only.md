---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/mobile-nav-accordion-menu-css-only/"
title: "Mobile Navigation Accordion Menu (CSS-Only Hamburger + Drill-Down)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "A complete mobile nav in pure CSS: a checkbox-driven hamburger that morphs into an X, opening a slide-down panel where each category is a <details> accordion…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Navigation Accordion Menu (CSS-Only Hamburger + Drill-Down)
Source: https://codefronts.com/navigation/css-accordions/mobile-nav-accordion-menu-css-only/

A complete mobile nav in pure CSS: a checkbox-driven hamburger that morphs into an X, opening a slide-down panel where each category is a <details> accordion with 48px touch targets, rotating indicators and indented child links — the exact 'hamburger menu without JavaScript' pattern devs search for.
## HTML
```html
<section class="acc-02" aria-label="Mobile navigation accordion demo">
  <nav class="acc-02__nav">
    <div class="acc-02__bar">
      <span class="acc-02__logo">north<b>peak</b></span>
      <input type="checkbox" id="acc-02-burger" class="acc-02__check">
      <label for="acc-02-burger" class="acc-02__burger" aria-label="Toggle menu"><span></span><span></span><span></span></label>
    </div>
    <div class="acc-02__panel">
      <div class="acc-02__panel-in">
        <details class="acc-02__cat">
          <summary class="acc-02__row">Gear</summary>
          <ul class="acc-02__sub">
            <li><a href="#" class="acc-02__link">Backpacks</a></li>
            <li><a href="#" class="acc-02__link">Tents &amp; shelter</a></li>
            <li><a href="#" class="acc-02__link">Trail footwear</a></li>
          </ul>
        </details>
        <details class="acc-02__cat">
          <summary class="acc-02__row">Apparel</summary>
          <ul class="acc-02__sub">
            <li><a href="#" class="acc-02__link">Jackets</a></li>
            <li><a href="#" class="acc-02__link">Base layers</a></li>
          </ul>
        </details>
        <details class="acc-02__cat">
          <summary class="acc-02__row">Guides</summary>
          <ul class="acc-02__sub">
            <li><a href="#" class="acc-02__link">Route planning</a></li>
            <li><a href="#" class="acc-02__link">Winter safety</a></li>
          </ul>
        </details>
        <a href="#" class="acc-02__row acc-02__row--plain">About</a>
        <a href="#" class="acc-02__cta">Find a store</a>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
.acc-02,
.acc-02 *,
.acc-02 *::before,
.acc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-02 {
  --accent: oklch(0.62 0.15 155);
  --ink: #14201a;
  --row: 52px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: #e9efe9;
  padding: 40px 20px;
}

.acc-02__nav {
  width: min(400px,100%);
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 24px 60px -34px rgba(20,50,30,.4);
  overflow: hidden;
}

.acc-02__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
}

.acc-02__logo {
  font-size: 19px;
  font-weight: 400;
  letter-spacing: -.02em;
  color: var(--ink);
}

.acc-02__logo b {
  font-weight: 800;
  color: var(--accent);
}

.acc-02__check {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-02__burger {
  width: 48px;
  height: 48px;
  display: grid;
  place-content: center;
  gap: 5px;
  cursor: pointer;
  border-radius: 12px;
  transition: background .15s;
}

.acc-02__burger:hover {
  background: #f0f4f0;
}

.acc-02__burger span {
  display: block;
  width: 22px;
  height: 2.5px;
  border-radius: 2px;
  background: var(--ink);
  transition: transform .3s cubic-bezier(.4,0,.2,1),opacity .2s;
}

.acc-02__nav:has(.acc-02__check:checked) .acc-02__burger span:nth-child(1) {
  transform: translateY(7.5px) rotate(45deg);
}

.acc-02__nav:has(.acc-02__check:checked) .acc-02__burger span:nth-child(2) {
  opacity: 0;
}

.acc-02__nav:has(.acc-02__check:checked) .acc-02__burger span:nth-child(3) {
  transform: translateY(-7.5px) rotate(-45deg);
}

.acc-02__check:focus-visible + .acc-02__burger {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.acc-02__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.4,0,.2,1);
}

.acc-02__nav:has(.acc-02__check:checked) .acc-02__panel {
  grid-template-rows: 1fr;
}

.acc-02__panel-in {
  min-height: 0;
  overflow: hidden;
  padding: 0 10px;
}

.acc-02__cat {
  border-top: 1px solid #edf1ed;
}

.acc-02__row {
  list-style: none;
  display: flex;
  align-items: center;
  min-height: var(--row);
  padding: 0 10px;
  font-size: 16px;
  font-weight: 650;
  color: var(--ink);
  cursor: pointer;
  position: relative;
  border-radius: 10px;
  transition: background .15s;
  text-decoration: none;
}

.acc-02__row::-webkit-details-marker {
  display: none;
}

.acc-02__row::marker {
  content: "";
}

.acc-02__row:hover {
  background: #f2f6f2;
}

summary.acc-02__row::after {
  content: "";
  position: absolute;
  right: 16px;
  width: 12px;
  height: 12px;
  background: linear-gradient(currentColor,currentColor) center/12px 2.5px no-repeat,linear-gradient(currentColor,currentColor) center/2.5px 12px no-repeat;
  color: var(--accent);
  transition: transform .3s;
}

.acc-02__cat[open] > summary.acc-02__row::after {
  transform: rotate(135deg);
}

.acc-02__sub {
  list-style: none;
  margin: 2px 0 10px 20px;
  border-left: 2px solid #dfe8df;
}

.acc-02__link {
  display: flex;
  align-items: center;
  min-height: 48px;
  padding: 0 14px;
  font-size: 15px;
  color: #43554a;
  text-decoration: none;
  border-radius: 8px;
}

.acc-02__link:hover {
  color: var(--accent);
  background: #f2f6f2;
}

.acc-02__row--plain {
  border-top: 1px solid #edf1ed;
  border-radius: 0;
}

.acc-02__cta {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 50px;
  margin: 10px 10px 16px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  border-radius: 12px;
  transition: filter .15s;
}

.acc-02__cta:hover {
  filter: brightness(1.08);
}

.acc-02__row:focus-visible,
.acc-02__link:focus-visible,
.acc-02__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-02__panel,
    .acc-02__burger span,
    summary.acc-02__row::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a visually-hidden checkbox + :has(:checked) drives the hamburger morph and the grid-template-rows 0fr→1fr panel slide; each nav category is a native <details> accordion. */
```
