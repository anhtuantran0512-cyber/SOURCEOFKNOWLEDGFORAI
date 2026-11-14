---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-float/"
title: "CSS 2 Column Layout Float"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "The legacy float two column layout, done properly: float: left + float: right with percentage widths, a modern .clearfix::after, and a desktop-first collapse…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 2 Column Layout Float
Source: https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-float/

The legacy float two column layout, done properly: float: left + float: right with percentage widths, a modern .clearfix::after, and a desktop-first collapse — for HTML email templates, ancient-browser support and maintaining pre-flexbox codebases. Styled as a classic newsletter so the technique’s natural habitat is obvious.
## HTML
```html
<section class="tcl-11" aria-label="Float two column layout demo">
  <div class="tcl-11__paper">
    <header class="tcl-11__mast">
      <b>The Weekly Ledger</b>
      <span>Issue 214 · Thursday edition</span>
    </header>
    <div class="tcl-11__cols tcl-11__clearfix">
      <main class="tcl-11__mainCol">
        <span class="tcl-11__float">float: left · width: 62%</span>
        <h2>Floats never really left — they moved to your inbox</h2>
        <p>Every responsive HTML email you received this week almost certainly used floated columns. Where flexbox and grid support is unreliable — legacy webmail clients, old enterprise browsers — the float pattern remains the bulletproof answer.</p>
        <p>The recipe is unchanged since 2008: two percentage-width floats, a clearfix on the parent, and a media query that resets both to full width. What has changed is the clearfix itself: one modern line, <code>display: flow-root</code>, now does the same job.</p>
      </main>
      <aside class="tcl-11__sideCol">
        <span class="tcl-11__float">float: right · width: 34%</span>
        <h3>In this issue</h3>
        <ul>
          <li>Why flow-root replaced the clearfix</li>
          <li>Float bugs that still bite in 2026</li>
          <li>Hybrid table + float email recipes</li>
        </ul>
        <a class="tcl-11__sub" href="#subscribe">Subscribe free</a>
      </aside>
    </div>
    <footer class="tcl-11__foot">You’re reading the demo of a cleared float layout — this footer sits below both columns because the wrapper contains its floats.</footer>
  </div>
</section>
```
## CSS
```css
.tcl-11,
.tcl-11 *,
.tcl-11 *::before,
.tcl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-11 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.28 0.02 60);
  --paper: oklch(0.985 0.008 90);
  --rule: oklch(0.85 0.02 80);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
  background: oklch(0.93 0.015 85);
  padding: clamp(20px,3.5vw,48px);
}

.tcl-11__paper {
  max-width: 860px;
  margin-inline: auto;
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: clamp(22px,3.5vw,40px);
  box-shadow: 0 20px 40px -30px rgba(80,60,20,.45);
}

.tcl-11__mast {
  text-align: center;
  border-bottom: 3px double var(--ink);
  padding-bottom: 14px;
  margin-bottom: 22px;
}

.tcl-11__mast b {
  display: block;
  font-size: clamp(24px,3.4vw,34px);
  letter-spacing: -.01em;
}

.tcl-11__mast span {
  font: italic 13px/1.6 inherit;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
}
/* the layout: two floats + a clearfix (or display:flow-root on the wrapper) */

.tcl-11__cols {
  /* modern one-liner alternative: display:flow-root */
}

.tcl-11__clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.tcl-11__mainCol {
  float: left;
  width: 62%;
}

.tcl-11__sideCol {
  float: right;
  width: 34%;
}

.tcl-11__float {
  display: inline-block;
  font: 700 10px/1 'Courier New',monospace;
  letter-spacing: .04em;
  color: oklch(0.45 0.1 60);
  border: 1px dashed oklch(0.7 0.06 70);
  padding: 5px 8px;
  margin-bottom: 12px;
  background: oklch(0.96 0.015 90);
}

.tcl-11__mainCol h2 {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.25;
  margin-bottom: 12px;
  text-wrap: balance;
}

.tcl-11__mainCol p {
  font-size: 14.5px;
  line-height: 1.75;
  margin-bottom: 12px;
  text-wrap: pretty;
}

.tcl-11__mainCol code {
  font: 700 12.5px 'Courier New',monospace;
  background: oklch(0.94 0.02 90);
  padding: 1px 5px;
}

.tcl-11__sideCol {
  background: oklch(0.955 0.015 90);
  border: 1px solid var(--rule);
  padding: 16px;
}

.tcl-11__sideCol h3 {
  font-size: 15px;
  border-bottom: 1px solid var(--rule);
  padding-bottom: 8px;
  margin-bottom: 10px;
}

.tcl-11__sideCol ul {
  list-style: none;
}

.tcl-11__sideCol li {
  font-size: 13px;
  line-height: 1.5;
  padding: 7px 0 7px 16px;
  position: relative;
}

.tcl-11__sideCol li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: color-mix(in oklab,var(--ink) 50%,transparent);
}

.tcl-11__sub {
  display: block;
  text-align: center;
  font: 700 13px/1 inherit;
  color: var(--paper);
  background: var(--ink);
  text-decoration: none;
  padding: 12px;
  margin-top: 12px;
}

.tcl-11__sub:hover {
  background: oklch(0.4 0.06 50);
}

.tcl-11__sub:focus-visible {
  outline: 3px solid oklch(0.5 0.1 60);
  outline-offset: 2px;
}

.tcl-11__foot {
  clear: both;
  font: italic 12.5px/1.6 inherit;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
  border-top: 1px solid var(--rule);
  padding-top: 14px;
  margin-top: 22px;
}

@media (max-width: 620px) {
  .tcl-11__mainCol,
    .tcl-11__sideCol {
    float: none;
    width: auto;
  }

  .tcl-11__sideCol {
    margin-top: 18px;
  }
}
```

## JavaScript
```js
/* No JavaScript — float:left 62% + float:right 34% with a .clearfix::after on the wrapper; the media query resets float:none/width:auto to stack. */
```
