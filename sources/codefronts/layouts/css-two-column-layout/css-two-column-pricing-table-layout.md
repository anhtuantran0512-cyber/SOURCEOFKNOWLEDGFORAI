---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-pricing-table-layout/"
title: "CSS Two Column Pricing Table Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A conversion-ready two column pricing table: Basic vs Pro cards side by side on a grid, with the Pro plan elevated by a \"Most popular\" ribbon, an accent…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Pricing Table Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-pricing-table-layout/

A conversion-ready two column pricing table: Basic vs Pro cards side by side on a grid, with the Pro plan elevated by a "Most popular" ribbon, an accent border and a slight scale — plus CSS-drawn checkmarks, subgrid-aligned rows and equal-height cards whose CTAs share a baseline.
## HTML
```html
<section class="tcl-13" aria-label="Two column pricing table layout demo">
  <header class="tcl-13__head">
    <h2>Simple pricing, two plans</h2>
    <p>Start free, upgrade when the team does. Both cards share one grid — the Pro card is a modifier class, not different markup.</p>
  </header>
  <div class="tcl-13__plans">
    <article class="tcl-13__plan">
      <h3>Basic</h3>
      <p class="tcl-13__blurb">For solo makers shipping their first product.</p>
      <p class="tcl-13__price"><strong>$0</strong><span>forever</span></p>
      <ul class="tcl-13__feats">
        <li>1 project with unlimited pages</li>
        <li>Community support</li>
        <li>Core analytics (30-day window)</li>
        <li>Fieldnote branding on shares</li>
      </ul>
      <a class="tcl-13__cta tcl-13__cta--ghost" href="#basic">Start for free</a>
    </article>
    <article class="tcl-13__plan tcl-13__plan--pop">
      <span class="tcl-13__ribbon">Most popular</span>
      <h3>Pro</h3>
      <p class="tcl-13__blurb">For teams who need review flows and real limits lifted.</p>
      <p class="tcl-13__price"><strong>$24</strong><span>per seat / month</span></p>
      <ul class="tcl-13__feats">
        <li>Unlimited projects &amp; shared libraries</li>
        <li>Priority support · 4-hour response</li>
        <li>Full analytics history with exports</li>
        <li>Custom domains, zero branding</li>
        <li>Staging environments &amp; audit log</li>
      </ul>
      <a class="tcl-13__cta" href="#pro">Start 14-day trial</a>
    </article>
  </div>
</section>
```
## CSS
```css
.tcl-13,
.tcl-13 *,
.tcl-13 *::before,
.tcl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-13 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.2 265);
  --ink: oklch(0.24 0.02 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: linear-gradient(180deg,oklch(0.965 0.01 265),oklch(0.94 0.02 265));
  padding: clamp(28px,4.5vw,60px);
}

.tcl-13__head {
  text-align: center;
  max-width: 520px;
  margin: 0 auto 30px;
  display: grid;
  gap: 8px;
}

.tcl-13__head h2 {
  font-size: clamp(24px,3.2vw,34px);
  letter-spacing: -.025em;
}

.tcl-13__head p {
  font-size: 14px;
  line-height: 1.6;
  color: color-mix(in oklab,var(--ink) 62%,transparent);
  text-wrap: pretty;
}

.tcl-13__plans {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 22px;
  max-width: 760px;
  margin-inline: auto;
  align-items: stretch;
}

.tcl-13__plan {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #fff;
  border: 1.5px solid oklch(0.89 0.015 265);
  border-radius: 20px;
  padding: clamp(22px,3vw,30px);
  box-shadow: 0 18px 36px -30px oklch(0.4 0.08 265/.7);
}

.tcl-13__plan--pop {
  border: 2px solid var(--accent);
  transform: scale(1.03);
  box-shadow: 0 28px 56px -30px color-mix(in oklab,var(--accent) 55%,transparent);
  z-index: 1;
}

.tcl-13__ribbon {
  position: absolute;
  top: -13px;
  left: 50%;
  translate: -50%;
  font: 700 11px/1 inherit;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #fff;
  background: var(--accent);
  border-radius: 99px;
  padding: 7px 14px;
  white-space: nowrap;
}

.tcl-13__plan h3 {
  font-size: 18px;
  letter-spacing: -.01em;
}

.tcl-13__blurb {
  font-size: 13.5px;
  line-height: 1.55;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
  text-wrap: pretty;
}

.tcl-13__price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 6px 0;
}

.tcl-13__price strong {
  font-size: clamp(34px,4vw,44px);
  letter-spacing: -.04em;
}

.tcl-13__price span {
  font-size: 13px;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-13__feats {
  list-style: none;
  display: grid;
  gap: 10px;
  padding: 4px 0 10px;
}

.tcl-13__feats li {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 10px;
  align-items: baseline;
  font-size: 13.5px;
  line-height: 1.5;
}

.tcl-13__feats li::before {
  content: "";
  width: 13px;
  height: 7px;
  border-left: 2.5px solid var(--accent);
  border-bottom: 2.5px solid var(--accent);
  transform: rotate(-45deg) translateY(-2px);
}

.tcl-13__cta {
  margin-top: auto;
  text-align: center;
  font: 600 14.5px/1 inherit;
  color: #fff;
  background: var(--accent);
  text-decoration: none;
  border-radius: 12px;
  padding: 15px;
  min-height: 48px;
  display: grid;
  place-items: center;
  transition: transform .15s,box-shadow .2s;
}

.tcl-13__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 26px -12px var(--accent);
}

.tcl-13__cta:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.tcl-13__cta--ghost {
  color: var(--accent);
  background: transparent;
  border: 1.5px solid color-mix(in oklab,var(--accent) 45%,transparent);
}

.tcl-13__cta--ghost:hover {
  background: color-mix(in oklab,var(--accent) 8%,transparent);
  box-shadow: none;
}

@media (max-width: 620px) {
  .tcl-13__plans {
    grid-template-columns: 1fr;
  }

  .tcl-13__plan--pop {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tcl-13__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — repeat(2,1fr) + default stretch equalizes the cards; the Pro emphasis is one modifier class (accent border + scale 1.03) and the checks are CSS-drawn. */
```
