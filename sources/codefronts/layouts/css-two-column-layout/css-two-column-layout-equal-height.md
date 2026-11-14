---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-equal-height/"
title: "CSS Two Column Layout Equal Height"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "The definitive fix for the classic \"columns don’t match height\" problem: grid’s default align-items: stretch makes both columns equal height automatically,…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Layout Equal Height
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-equal-height/

The definitive fix for the classic "columns don’t match height" problem: grid’s default align-items: stretch makes both columns equal height automatically, and flex-direction: column + margin-top: auto pins each card’s footer to the bottom — even when one column has three times the content. Annotated in-demo so you can see the stretch happening.
## HTML
```html
<section class="tcl-09" aria-label="Equal height two column layout demo">
  <header class="tcl-09__head">
    <h2>Both cards. One height.</h2>
    <p>The right card has far more content — the left card stretches to match, and both footers pin to the bottom.</p>
  </header>
  <div class="tcl-09__pair">
    <article class="tcl-09__card">
      <span class="tcl-09__tag">Short content</span>
      <h3>Starter workspace</h3>
      <p>One project, community support, and every core feature. Enough to ship something real.</p>
      <footer class="tcl-09__foot"><strong>$0</strong><a href="#start">Start free</a></footer>
    </article>
    <article class="tcl-09__card tcl-09__card--tall">
      <span class="tcl-09__tag">Long content</span>
      <h3>Team workspace</h3>
      <p>Unlimited projects with shared libraries, granular roles and review workflows built for real teams.</p>
      <p>Includes staging environments, audit history, priority support with a four-hour response target, and usage analytics your finance team will actually read.</p>
      <p>Everything syncs in real time, so designers, writers and engineers stop emailing files with “final-v3” in the name.</p>
      <footer class="tcl-09__foot"><strong>$24<span>/seat</span></strong><a href="#trial">Start trial</a></footer>
    </article>
    <span class="tcl-09__note" aria-hidden="true">align-items: stretch (default) · footer: margin-top auto</span>
  </div>
</section>
```
## CSS
```css
.tcl-09,
.tcl-09 *,
.tcl-09 *::before,
.tcl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-09 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.6 0.19 20);
  --ink: oklch(0.26 0.02 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.97 0.008 40);
  padding: clamp(24px,4vw,52px);
}

.tcl-09__head {
  max-width: 920px;
  margin: 0 auto 24px;
  display: grid;
  gap: 8px;
}

.tcl-09__head h2 {
  font-size: clamp(22px,3vw,30px);
  letter-spacing: -.02em;
}

.tcl-09__head p {
  font-size: 14.5px;
  color: color-mix(in oklab,var(--ink) 62%,transparent);
  text-wrap: pretty;
}

.tcl-09__pair {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  max-width: 920px;
  margin-inline: auto;
  padding-bottom: 34px;
}

.tcl-09__card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #fff;
  border: 1px solid oklch(0.9 0.015 40);
  border-radius: 18px;
  padding: clamp(20px,3vw,28px);
  box-shadow: 0 16px 32px -26px oklch(0.4 0.08 20 / .6);
}

.tcl-09__card--tall {
  border-color: color-mix(in oklab,var(--accent) 35%,transparent);
}

.tcl-09__tag {
  align-self: flex-start;
  font: 600 10.5px/1 ui-monospace,monospace;
  letter-spacing: .06em;
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  border-radius: 99px;
  padding: 5px 9px;
}

.tcl-09__card h3 {
  font-size: 19px;
  letter-spacing: -.015em;
}

.tcl-09__card p {
  font-size: 14px;
  line-height: 1.65;
  color: color-mix(in oklab,var(--ink) 72%,transparent);
  text-wrap: pretty;
}

.tcl-09__foot {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px dashed oklch(0.88 0.015 40);
}

.tcl-09__foot strong {
  font-size: 24px;
  letter-spacing: -.02em;
}

.tcl-09__foot strong span {
  font-size: 13px;
  font-weight: 500;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-09__foot a {
  font: 600 13.5px/1 inherit;
  color: #fff;
  background: var(--ink);
  text-decoration: none;
  border-radius: 9px;
  padding: 11px 18px;
  transition: background .15s;
}

.tcl-09__foot a:hover {
  background: var(--accent);
}

.tcl-09__foot a:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.tcl-09__note {
  position: absolute;
  bottom: 0;
  left: 50%;
  translate: -50%;
  font: 600 10.5px/1 ui-monospace,monospace;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
  white-space: nowrap;
}

@media (max-width: 640px) {
  .tcl-09__pair {
    grid-template-columns: 1fr;
  }

  .tcl-09__note {
    position: static;
    translate: 0;
    justify-self: center;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid's default align-items:stretch equalizes the columns, and margin-top:auto inside each flex-column card pins both footers to the bottom. */
```
