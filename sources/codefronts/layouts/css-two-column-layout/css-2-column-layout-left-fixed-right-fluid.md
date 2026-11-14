---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-left-fixed-right-fluid/"
title: "CSS 2 Column Layout Left Fixed Right Fluid"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "The classic app shell: a fixed 280px left sidebar with a fluid main column that absorbs every remaining pixel — grid-template-columns: 280px minmax(0,1fr) in…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 2 Column Layout Left Fixed Right Fluid
Source: https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-left-fixed-right-fluid/

The classic app shell: a fixed 280px left sidebar with a fluid main column that absorbs every remaining pixel — grid-template-columns: 280px minmax(0,1fr) in one line. Styled as a real admin dashboard with nav states, stat cards on an auto-fit grid, and a mobile collapse.
## HTML
```html
<section class="tcl-04" aria-label="Fixed sidebar with fluid main column demo">
  <div class="tcl-04__shell">
    <nav class="tcl-04__side" aria-label="Dashboard navigation">
      <div class="tcl-04__logo"><i></i>Northbeam</div>
      <span class="tcl-04__track">280px — fixed track</span>
      <ul class="tcl-04__nav">
        <li><a href="#overview" aria-current="page">Overview</a></li>
        <li><a href="#orders">Orders <em>24</em></a></li>
        <li><a href="#customers">Customers</a></li>
        <li><a href="#inventory">Inventory</a></li>
        <li><a href="#settings">Settings</a></li>
      </ul>
      <div class="tcl-04__user"><b>AT</b><span>Alex Tan<br><small>Store admin</small></span></div>
    </nav>
    <main class="tcl-04__main">
      <header class="tcl-04__head">
        <div><h2>Good morning, Alex</h2><p>Here’s what changed while you were away.</p></div>
        <span class="tcl-04__track tcl-04__track--light">minmax(0, 1fr) — fluid</span>
      </header>
      <div class="tcl-04__cards">
        <div class="tcl-04__card"><span>Revenue today</span><strong>$8,412</strong><em>+18% vs yesterday</em></div>
        <div class="tcl-04__card"><span>Open orders</span><strong>247</strong><em>36 need review</em></div>
        <div class="tcl-04__card"><span>Conversion</span><strong>4.1%</strong><em>+0.3 pts</em></div>
        <div class="tcl-04__card"><span>Refund rate</span><strong>0.9%</strong><em>steady</em></div>
      </div>
      <div class="tcl-04__panel">
        <h3>Orders needing review</h3>
        <div class="tcl-04__rowline"><b>#10482</b><span>2 × Field Jacket</span><i>Flagged: address</i><a href="#o1">Review</a></div>
        <div class="tcl-04__rowline"><b>#10479</b><span>1 × Trail Pack 30L</span><i>Flagged: payment</i><a href="#o2">Review</a></div>
        <div class="tcl-04__rowline"><b>#10475</b><span>3 × Merino Crew</span><i>Flagged: stock</i><a href="#o3">Review</a></div>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.tcl-04,
.tcl-04 *,
.tcl-04 *::before,
.tcl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-04 {
  width: 100%;
  min-height: 100vh;
  --side: oklch(0.21 0.03 265);
  --accent: oklch(0.7 0.15 210);
  --ink: oklch(0.25 0.02 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.955 0.008 265);
  color: var(--ink);
}

.tcl-04__shell {
  display: grid;
  grid-template-columns: 280px minmax(0,1fr);
  min-height: 540px;
  max-width: 1100px;
  margin-inline: auto;
}

.tcl-04__side {
  background: var(--side);
  color: oklch(0.9 0.01 265);
  padding: 24px 18px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tcl-04__logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 16px;
  letter-spacing: -.01em;
  color: #fff;
}

.tcl-04__logo i {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: conic-gradient(from 220deg,var(--accent),oklch(0.55 0.2 280));
}

.tcl-04__track {
  align-self: flex-start;
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .05em;
  color: var(--accent);
  border: 1px dashed color-mix(in oklab,var(--accent) 55%,transparent);
  border-radius: 99px;
  padding: 5px 9px;
}

.tcl-04__track--light {
  color: oklch(0.5 0.1 210);
  border-color: oklch(0.75 0.06 210);
}

.tcl-04__nav {
  list-style: none;
  display: grid;
  gap: 4px;
}

.tcl-04__nav a {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: oklch(0.78 0.02 265);
  text-decoration: none;
  padding: 10px 12px;
  border-radius: 9px;
  transition: background .15s,color .15s;
}

.tcl-04__nav a:hover {
  background: rgba(255,255,255,.07);
  color: #fff;
}

.tcl-04__nav a[aria-current="page"] {
  background: color-mix(in oklab,var(--accent) 22%,transparent);
  color: #fff;
  font-weight: 600;
}

.tcl-04__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.tcl-04__nav em {
  font: 600 11px/1 inherit;
  font-style: normal;
  background: var(--accent);
  color: var(--side);
  border-radius: 99px;
  padding: 3px 8px;
}

.tcl-04__user {
  margin-top: auto;
  display: flex;
  gap: 10px;
  align-items: center;
  padding: 12px;
  border-radius: 12px;
  background: rgba(255,255,255,.06);
  font-size: 13px;
  line-height: 1.3;
}

.tcl-04__user b {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: var(--accent);
  color: var(--side);
  font-size: 12.5px;
}

.tcl-04__user small {
  color: oklch(0.65 0.02 265);
}

.tcl-04__main {
  padding: clamp(20px,3vw,32px);
  display: grid;
  gap: 20px;
  align-content: start;
}

.tcl-04__head {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: space-between;
  align-items: start;
}

.tcl-04__head h2 {
  font-size: clamp(19px,2.4vw,24px);
  letter-spacing: -.02em;
}

.tcl-04__head p {
  font-size: 13.5px;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
}

.tcl-04__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
  gap: 14px;
}

.tcl-04__card {
  display: grid;
  gap: 4px;
  background: #fff;
  border: 1px solid oklch(0.9 0.01 265);
  border-radius: 14px;
  padding: 16px;
}

.tcl-04__card span {
  font-size: 12px;
  color: color-mix(in oklab,var(--ink) 58%,transparent);
}

.tcl-04__card strong {
  font-size: 22px;
  letter-spacing: -.02em;
}

.tcl-04__card em {
  font: 500 11.5px/1.2 inherit;
  font-style: normal;
  color: oklch(0.52 0.13 160);
}

.tcl-04__panel {
  background: #fff;
  border: 1px solid oklch(0.9 0.01 265);
  border-radius: 14px;
  padding: 18px;
  display: grid;
  gap: 10px;
}

.tcl-04__panel h3 {
  font-size: 15px;
  letter-spacing: -.01em;
  margin-bottom: 4px;
}

.tcl-04__rowline {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  gap: 14px;
  align-items: center;
  font-size: 13px;
  padding: 10px 12px;
  border-radius: 10px;
  background: oklch(0.97 0.005 265);
}

.tcl-04__rowline b {
  font: 600 12.5px ui-monospace,monospace;
}

.tcl-04__rowline i {
  font-style: normal;
  font-size: 12px;
  color: oklch(0.55 0.16 30);
}

.tcl-04__rowline a {
  font: 600 12.5px/1 inherit;
  color: oklch(0.5 0.12 210);
  text-decoration: none;
}

.tcl-04__rowline a:hover {
  text-decoration: underline;
}

.tcl-04__rowline a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}

@media (max-width: 820px) {
  .tcl-04__shell {
    grid-template-columns: 1fr;
  }

  .tcl-04__side {
    flex-direction: row;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }

  .tcl-04__nav {
    grid-auto-flow: column;
    overflow-x: auto;
    width: 100%;
  }

  .tcl-04__user {
    margin: 0;
    display: none;
  }

  .tcl-04__rowline {
    grid-template-columns: auto 1fr;
    grid-auto-rows: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-columns:280px minmax(0,1fr) pins the sidebar and lets main absorb the rest; minmax(0,…) stops wide content from breaking the shell. */
```
