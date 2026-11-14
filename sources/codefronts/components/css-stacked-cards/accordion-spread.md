---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/accordion-spread/"
title: "Accordion Spread"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A densely layered pile that, on toggle, smoothly expands the whole parent into a cleanly separated vertical list — functioning as an interactive slide-out…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Spread
Source: https://codefronts.com/components/css-stacked-cards/accordion-spread/

A densely layered pile that, on toggle, smoothly expands the whole parent into a cleanly separated vertical list — functioning as an interactive slide-out navigation menu. Collapse it and the items nest back into a compact stack.
## HTML
```html
<section class="scd-16" aria-label="Accordion-spread menu">
  <div class="scd-16__menu">
    <input type="checkbox" id="scd-16-t" class="scd-16__toggle">
    <label class="scd-16__bar" for="scd-16-t"><span>Menu</span><i class="scd-16__chev">⌄</i></label>
    <div class="scd-16__wrap"><nav class="scd-16__list">
      <a href="#" style="--n:0">Dashboard</a>
      <a href="#" style="--n:1">Projects</a>
      <a href="#" style="--n:2">Team</a>
      <a href="#" style="--n:3">Billing</a>
      <a href="#" style="--n:4">Settings</a>
    </nav></div>
  </div>
</section>
```
## CSS
```css
.scd-16,
.scd-16 *,
.scd-16 *::before,
.scd-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-16 {
  --accent: oklch(0.64 0.17 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 12vh 20px;
  background: #101018;
}

.scd-16__menu {
  width: min(300px,100%);
}

.scd-16__toggle {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.scd-16__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-radius: 14px;
  background: var(--accent);
  color: #fff;
  font-weight: 800;
  font-size: 16px;
  cursor: pointer;
  position: relative;
  z-index: 10;
  box-shadow: 0 14px 30px -16px rgba(0,0,0,.7);
}

.scd-16__chev {
  transition: transform .35s;
  font-size: 20px;
}

.scd-16__wrap {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.3,.9,.3,1);
}

.scd-16__list {
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 8px;
}

.scd-16__list a {
  padding: 15px 20px;
  border-radius: 12px;
  background: #1c1e2a;
  color: #c9cde0;
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  opacity: 0;
  transform: translateY(-8px);
  box-shadow: 0 10px 22px -14px rgba(0,0,0,.8);
  transition: opacity .3s,transform .3s;
  transition-delay: calc(var(--n) * .04s);
}

.scd-16__list a:hover {
  background: #262a3a;
  color: #fff;
}

.scd-16__toggle:checked ~ .scd-16__bar .scd-16__chev {
  transform: rotate(180deg);
}

.scd-16__toggle:checked ~ .scd-16__wrap {
  grid-template-rows: 1fr;
}

.scd-16__toggle:checked ~ .scd-16__wrap a {
  opacity: 1;
  transform: none;
}

.scd-16__toggle:focus-visible ~ .scd-16__bar {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.scd-16__list a:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .scd-16__list a {
    transition-delay: 0s!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — one checkbox toggles the whole menu; :checked sibling rules relax the negative margins and fade items in, staggered per item. */
```
