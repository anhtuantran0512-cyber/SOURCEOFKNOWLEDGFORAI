---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/overlay-with-backdrop/"
title: "Off-Canvas Sidebar Overlay Layout with Blur Backdrop"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The modal-grade overlay drawer done with the element built for it: <dialog>."
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Off-Canvas Sidebar Overlay Layout with Blur Backdrop
Source: https://codefronts.com/layouts/css-sidebar-layouts/overlay-with-backdrop/

The modal-grade overlay drawer done with the element built for it: <dialog>. showModal()-free — this variant opens purely via the checkbox pattern for a zero-JS page — but keeps the dialog's visual grammar: content dims AND blurs behind a translucent scrim, the drawer lifts on a soft shadow, and pointer-events discipline means the dimmed page is genuinely inert to clicks.
## HTML
```html
<section class="sbl-19">
  <input type="checkbox" id="sbl19-o" class="sbl-19__state">
  <header class="sbl-19__bar"><strong>Alpine Supply Co.</strong><label for="sbl19-o" class="sbl-19__cartbtn"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>Cart · 2</label></header>
  <main class="sbl-19__page"><h1>New arrivals</h1><div class="sbl-19__grid"><div></div><div></div><div></div><div></div><div></div><div></div></div></main>
  <label for="sbl19-o" class="sbl-19__scrim" aria-hidden="true"></label>
  <aside class="sbl-19__drawer" aria-label="Shopping cart">
    <div class="sbl-19__head"><h2>Your cart</h2><label for="sbl19-o" class="sbl-19__close" aria-label="Close cart"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></label></div>
    <div class="sbl-19__item"><span class="sbl-19__thumb" aria-hidden="true"></span><span><strong>Ridge shell jacket</strong><small>Moss · M</small></span><data>$168</data></div>
    <div class="sbl-19__item"><span class="sbl-19__thumb" aria-hidden="true"></span><span><strong>Trail merino crew</strong><small>Ash · L</small></span><data>$74</data></div>
    <div class="sbl-19__total"><span>Subtotal</span><data>$242</data><button type="button">Checkout</button></div>
  </aside>
</section>
```
## CSS
```css
.sbl-19,
.sbl-19 *,
.sbl-19 *::before,
.sbl-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-19 {
  --panel: #fff;
  --ink: oklch(0.26 0.015 145);
  --mut: oklch(0.52 0.012 145);
  --line: oklch(0.9 0.008 145);
  --accent: oklch(0.45 0.12 150);
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.975 0.004 120);
  color: var(--ink);
}

.sbl-19__state {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-19__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
  padding: 0 20px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  font: 700 15px/1 system-ui,sans-serif;
}

.sbl-19__cartbtn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  padding: 9px 14px;
  border-radius: 10px;
  border: 1px solid var(--line);
  font: 600 13px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background-color .2s ease;
}

.sbl-19__cartbtn:hover {
  background: color-mix(in oklab,var(--ink) 5%,transparent);
}

.sbl-19:has(#sbl19-o:focus-visible) .sbl-19__cartbtn {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-19__cartbtn svg,
.sbl-19__close svg {
  width: 17px;
  height: 17px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-19__page {
  padding: 26px;
  overflow-y: auto;
}

.sbl-19__page h1 {
  font: 650 21px/1.2 system-ui,sans-serif;
  margin-bottom: 18px;
}

.sbl-19__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(140px,1fr));
  gap: 14px;
}

.sbl-19__grid div {
  aspect-ratio: 3/4;
  border-radius: 12px;
  background: linear-gradient(150deg,oklch(0.93 0.01 145),oklch(0.87 0.015 145));
}

.sbl-19__scrim {
  position: absolute;
  inset: 0;
  background: oklch(0 0 0 / .45);
  backdrop-filter: blur(4px);
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s ease;
  z-index: 3;
}

.sbl-19:has(#sbl19-o:checked) .sbl-19__scrim {
  opacity: 1;
  pointer-events: auto;
}

.sbl-19__drawer {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: min(340px,92vw);
  display: flex;
  flex-direction: column;
  background: var(--panel);
  border-left: 1px solid var(--line);
  padding: 18px;
  transform: translate3d(100%,0,0);
  transition: transform .32s cubic-bezier(.4,0,.2,1),box-shadow .32s ease;
  z-index: 4;
}

.sbl-19:has(#sbl19-o:checked) .sbl-19__drawer {
  transform: translate3d(0,0,0);
  box-shadow: -16px 0 48px oklch(0 0 0 / .18);
}

.sbl-19__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 16px;
}

.sbl-19__head h2 {
  font: 700 16px/1 system-ui,sans-serif;
}

.sbl-19__close {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 9px;
  color: var(--mut);
  cursor: pointer;
  transition: background-color .2s ease;
}

.sbl-19__close:hover {
  background: color-mix(in oklab,var(--ink) 6%,transparent);
  color: var(--ink);
}

.sbl-19__item {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 12px 0;
  border-top: 1px solid var(--line);
}

.sbl-19__thumb {
  width: 52px;
  height: 52px;
  border-radius: 10px;
  background: linear-gradient(150deg,oklch(0.9 0.012 145),oklch(0.84 0.018 145));
}

.sbl-19__item strong {
  display: block;
  font: 600 13.5px/1.25 system-ui,sans-serif;
}

.sbl-19__item small {
  font: 400 12px/1.4 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-19__item data,
.sbl-19__total data {
  font: 600 13.5px/1 system-ui,sans-serif;
  font-variant-numeric: tabular-nums;
}

.sbl-19__total {
  margin-top: auto;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 14px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-19__total button {
  grid-column: 1/-1;
  padding: 13px;
  border: none;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  font: 700 14px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: filter .2s ease;
}

.sbl-19__total button:hover {
  filter: brightness(1.12);
}

.sbl-19__total button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-19__drawer,
    .sbl-19__scrim {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the scrim dims AND blurs (backdrop-filter) with opacity+pointer-events toggling; the drawer slides on translate3d from the right. */
```
