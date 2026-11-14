---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-responsive-two-column-layout/"
title: "CSS Responsive Two Column Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A mobile-first responsive two column layout that stacks vertically on phones and snaps side-by-side at 768px — with a live breakpoint badge that announces…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Responsive Two Column Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-responsive-two-column-layout/

A mobile-first responsive two column layout that stacks vertically on phones and snaps side-by-side at 768px — with a live breakpoint badge that announces the current mode. Built with CSS Grid, one media query, and alternating image/text rows for the classic marketing "zig-zag" pattern.
## HTML
```html
<section class="tcl-03" aria-label="Responsive two column layout demo">
  <div class="tcl-03__badge" aria-hidden="true">Layout mode</div>
  <div class="tcl-03__rows">
    <article class="tcl-03__row">
      <div class="tcl-03__copy">
        <span class="tcl-03__kicker">01 · Mobile-first</span>
        <h2 class="tcl-03__h">Stacks on phones, splits at 768px</h2>
        <p class="tcl-03__p">The single-column stack is the default — the two column layout is the enhancement. One media query flips every row from a vertical flow to a side-by-side grid.</p>
      </div>
      <div class="tcl-03__ph tcl-03__ph--a" role="img" aria-label="Placeholder visual: layered app cards"><i></i><i></i><i></i></div>
    </article>
    <article class="tcl-03__row tcl-03__row--alt">
      <div class="tcl-03__copy">
        <span class="tcl-03__kicker">02 · Zig-zag rhythm</span>
        <h2 class="tcl-03__h">Alternate sides without duplicate markup</h2>
        <p class="tcl-03__p">Even rows pull their visual to the left with a single <code>order:-1</code> — the DOM keeps text first for accessibility and SEO while the eye gets the editorial zig-zag.</p>
      </div>
      <div class="tcl-03__ph tcl-03__ph--b" role="img" aria-label="Placeholder visual: concentric rings"><i></i><i></i><i></i></div>
    </article>
  </div>
</section>
```
## CSS
```css
.tcl-03,
.tcl-03 *,
.tcl-03 *::before,
.tcl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-03 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.62 0.18 30);
  --ink: oklch(0.24 0.02 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.975 0.008 60);
  padding: clamp(24px,4vw,52px);
  position: relative;
}

.tcl-03__badge {
  position: absolute;
  top: 14px;
  right: 14px;
  font: 600 11px/1 ui-monospace,monospace;
  color: #fff;
  background: var(--ink);
  border-radius: 99px;
  padding: 7px 12px;
  display: flex;
  gap: 6px;
  align-items: center;
}

.tcl-03__badge::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: oklch(0.75 0.17 145);
}

.tcl-03__badge::after {
  content: "1 column · stacked";
}

.tcl-03__rows {
  display: grid;
  gap: clamp(36px,6vw,72px);
  max-width: 1000px;
  margin-inline: auto;
}

.tcl-03__row {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(20px,3.5vw,56px);
  align-items: center;
}

.tcl-03__copy {
  display: grid;
  gap: 12px;
  min-width: 0;
}

.tcl-03__kicker {
  font: 700 11px/1 inherit;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.tcl-03__h {
  font-size: clamp(21px,2.8vw,30px);
  line-height: 1.15;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.tcl-03__p {
  font-size: 14.5px;
  line-height: 1.65;
  color: color-mix(in oklab,var(--ink) 72%,transparent);
  text-wrap: pretty;
}

.tcl-03__p code {
  font: 600 12.5px ui-monospace,monospace;
  background: color-mix(in oklab,var(--accent) 12%,transparent);
  border-radius: 5px;
  padding: 2px 5px;
}

.tcl-03__ph {
  position: relative;
  min-height: 190px;
  border-radius: 16px;
  overflow: hidden;
}

.tcl-03__ph--a {
  background: linear-gradient(135deg,oklch(0.9 0.06 30),oklch(0.82 0.1 55));
}

.tcl-03__ph--a i {
  position: absolute;
  border-radius: 10px;
  background: rgba(255,255,255,.75);
  box-shadow: 0 14px 28px -14px rgba(120,50,10,.4);
}

.tcl-03__ph--a i:nth-child(1) {
  inset: 22% 42% 30% 10%;
  transform: rotate(-4deg);
}

.tcl-03__ph--a i:nth-child(2) {
  inset: 32% 24% 20% 30%;
  transform: rotate(2deg);
  background: rgba(255,255,255,.9);
}

.tcl-03__ph--a i:nth-child(3) {
  inset: 18% 10% 42% 52%;
  transform: rotate(6deg);
  background: rgba(255,255,255,.6);
}

.tcl-03__ph--b {
  background: linear-gradient(135deg,oklch(0.32 0.04 280),oklch(0.45 0.1 300));
}

.tcl-03__ph--b i {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  border: 2px solid rgba(255,255,255,.5);
  border-radius: 50%;
}

.tcl-03__ph--b i:nth-child(1) {
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,.85);
}

.tcl-03__ph--b i:nth-child(2) {
  width: 120px;
  height: 120px;
}

.tcl-03__ph--b i:nth-child(3) {
  width: 180px;
  height: 180px;
  border-color: rgba(255,255,255,.25);
}

@media (min-width: 768px) {
  .tcl-03__badge::after {
    content: "2 columns · side-by-side";
  }

  .tcl-03__row {
    grid-template-columns: 1fr 1fr;
  }

  .tcl-03__row--alt .tcl-03__ph {
    order: -1;
  }
}
```

## JavaScript
```js
/* No JavaScript — the mobile stack is the default and one min-width:768px media query switches rows to two columns; even the "layout mode" badge text is swapped in CSS. */
```
