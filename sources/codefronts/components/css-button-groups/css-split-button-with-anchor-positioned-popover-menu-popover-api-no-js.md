---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-split-button-with-anchor-positioned-popover-menu-popover-api-no-js/"
title: "CSS Split Button with Anchor-Positioned Popover Menu (Popover API, No JS)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A split button whose dropdown is tethered with pure CSS Anchor Positioning and opened by the native Popover API — the menu docks perfectly under the caret,…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Button with Anchor-Positioned Popover Menu (Popover API, No JS)
Source: https://codefronts.com/components/css-button-groups/css-split-button-with-anchor-positioned-popover-menu-popover-api-no-js/

A split button whose dropdown is tethered with pure CSS Anchor Positioning and opened by the native Popover API — the menu docks perfectly under the caret, escapes every overflow/clipping ancestor via the top layer, and needs zero JavaScript. The cutting-edge 'CSS anchor positioning dropdown button with Popover API' pattern front-end devs are adopting in 2027.
## HTML
```html
<section class="btn-01" aria-label="Anchor-positioned popover split button demo">
  <div class="btn-01__split">
    <button type="button" class="btn-01__primary">Export CSV</button>
    <button type="button" class="btn-01__caret" popovertarget="btn-01-menu" aria-label="More export formats"></button>
    <div id="btn-01-menu" popover class="btn-01__menu" role="menu">
      <button type="button" class="btn-01__item" role="menuitem">Export as JSON</button>
      <button type="button" class="btn-01__item" role="menuitem">Export as Excel</button>
      <button type="button" class="btn-01__item" role="menuitem">Export as PDF</button>
      <div class="btn-01__sep"></div>
      <button type="button" class="btn-01__item" role="menuitem">Copy to clipboard</button>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-01,
.btn-01 *,
.btn-01 *::before,
.btn-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-01 {
  --accent: oklch(0.63 0.21 30);
  --accent-d: oklch(0.54 0.2 30);
  --ink: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: linear-gradient(160deg,#eef0f4,#e0e3ea);
  padding: 120px 20px;
}

.btn-01__split {
  display: inline-flex;
  border-radius: 14px;
  box-shadow: 0 14px 34px -16px rgba(120,30,10,.5);
}

.btn-01__primary {
  border: none;
  background: var(--accent);
  color: var(--ink);
  font-size: 15.5px;
  font-weight: 750;
  padding: 0 22px;
  height: 50px;
  border-radius: 14px 0 0 14px;
  cursor: pointer;
  transition: filter .15s;
}

.btn-01__primary:hover {
  filter: brightness(1.06);
}

.btn-01__caret {
  anchor-name: --btn-01-anc;
  position: relative;
  border: none;
  width: 48px;
  height: 50px;
  background: var(--accent-d);
  border-radius: 0 14px 14px 0;
  cursor: pointer;
  border-left: 1px solid rgba(90,20,5,.3);
}

.btn-01__caret::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid var(--ink);
  border-bottom: 2.5px solid var(--ink);
  translate: -50% -70%;
  rotate: 45deg;
  transition: rotate .25s,translate .25s;
}

.btn-01__caret:hover {
  filter: brightness(1.08);
}

.btn-01__menu {
  position: fixed;
  margin: 0;
  inset: auto;
  position-anchor: --btn-01-anc;
  top: anchor(bottom);
  right: anchor(right);
  margin-top: 8px;
  position-try-fallbacks: flip-block;
  min-width: 220px;
  background: #fff;
  border: 1px solid #e6dcd8;
  border-radius: 14px;
  padding: 7px;
  box-shadow: 0 26px 54px -22px rgba(120,40,20,.5);
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  translate: 0 -6px;
  transition: opacity .2s,translate .2s,display .2s allow-discrete,overlay .2s allow-discrete;
}

.btn-01__menu:popover-open {
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  .btn-01__menu:popover-open {
    opacity: 0;
    translate: 0 -6px;
  }
}

.btn-01__item {
  text-align: left;
  border: none;
  background: none;
  font-size: 14.5px;
  font-weight: 650;
  color: #4a2a20;
  padding: 11px 13px;
  border-radius: 9px;
  cursor: pointer;
  transition: background .12s;
}

.btn-01__item:hover {
  background: #fbeeea;
}

.btn-01__sep {
  height: 1px;
  background: #f0e2dd;
  margin: 5px 6px;
}

.btn-01__primary:focus-visible,
.btn-01__caret:focus-visible,
.btn-01__item:focus-visible {
  outline: 3px solid var(--accent-d);
  outline-offset: 2px;
}

@supports not (anchor-name: --x) {
  .btn-01__menu {
    top: auto;
    bottom: 16px;
    right: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .btn-01__menu,
    .btn-01__caret::after {
    transition: opacity .12s,display .12s allow-discrete,overlay .12s allow-discrete;
  }
}
```
