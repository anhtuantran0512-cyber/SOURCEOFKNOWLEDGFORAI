---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/three-tier-feature-parity-comparison-stack/"
title: "Three Tier Feature Parity Comparison Stack"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Three tier columns — Free, Pro, Enterprise — compared on feature availability rather than price, so it can sit above the pricing block without duplicating it."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Three Tier Feature Parity Comparison Stack
Source: https://codefronts.com/layouts/css-feature-sections/three-tier-feature-parity-comparison-stack/

Three tier columns — Free, Pro, Enterprise — compared on feature availability rather than price, so it can sit above the pricing block without duplicating it. Each column runs the same feature list with a ✓ or an em dash per row, the middle tier is raised and ringed, and subgrid keeps every row aligned across all three columns as text wraps.
## HTML
```html
<section class="fs-08" aria-labelledby="fs-08-heading">
  <div class="fs-08__hero" aria-hidden="true">
    <span class="fs-08__wordmark">Ranger</span>
    <span class="fs-08__heronav">Spend controls for engineering teams</span>
  </div>

  <div class="fs-08__stage">
    <div class="fs-08__head">
      <p class="fs-08__eyebrow">Feature parity</p>
      <h2 class="fs-08__heading" id="fs-08-heading">What each tier actually includes</h2>
      <p class="fs-08__sub">Prices are one scroll down. This is the capability list, so you can see where your team lands before you look at a number.</p>
    </div>

    <div class="fs-08__cols">
      <article class="fs-08__col">
        <header class="fs-08__chead">
          <h3 class="fs-08__ctitle">Free</h3>
          <p class="fs-08__cnote">Solo builders and side projects</p>
        </header>
        <ul class="fs-08__rows">
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Unlimited virtual cards</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Receipt capture and matching</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--no" aria-hidden="true">—</span><span class="fs-08__sr">Not included.</span>Approval policies</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--no" aria-hidden="true">—</span><span class="fs-08__sr">Not included.</span>Accounting sync</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--no" aria-hidden="true">—</span><span class="fs-08__sr">Not included.</span>SSO and SCIM</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--no" aria-hidden="true">—</span><span class="fs-08__sr">Not included.</span>Audit log export</li>
        </ul>
        <a class="fs-08__cta" href="#fs-08-heading">Start free</a>
      </article>

      <article class="fs-08__col" data-featured>
        <p class="fs-08__flag">Most teams</p>
        <header class="fs-08__chead">
          <h3 class="fs-08__ctitle">Pro</h3>
          <p class="fs-08__cnote">Five to two hundred people</p>
        </header>
        <ul class="fs-08__rows">
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Unlimited virtual cards</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Receipt capture and matching</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Approval policies</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Accounting sync</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>SSO and SCIM</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--no" aria-hidden="true">—</span><span class="fs-08__sr">Not included.</span>Audit log export</li>
        </ul>
        <a class="fs-08__cta fs-08__cta--solid" href="#fs-08-heading">Compare Pro pricing</a>
      </article>

      <article class="fs-08__col">
        <header class="fs-08__chead">
          <h3 class="fs-08__ctitle">Enterprise</h3>
          <p class="fs-08__cnote">Procurement and security reviews</p>
        </header>
        <ul class="fs-08__rows">
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Unlimited virtual cards</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Receipt capture and matching</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Approval policies</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Accounting sync</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>SSO and SCIM</li>
          <li class="fs-08__row"><span class="fs-08__mk fs-08__mk--yes" aria-hidden="true">✓</span><span class="fs-08__sr">Included.</span>Audit log export</li>
        </ul>
        <a class="fs-08__cta" href="#fs-08-heading">Talk to sales</a>
      </article>
    </div>
  </div>

  <div class="fs-08__below" aria-hidden="true">Pricing · Security · Status</div>
</section>
```
## CSS
```css
.fs-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #eef1f2;
  --page: oklch(0.945 0.006 200);
  --card: #ffffff;
  --ink: #12232a;
  --ink: oklch(0.24 0.021 215);
  --muted: #5a6d75;
  --muted: oklch(0.51 0.019 215);
  --rule: #d5dcdf;
  --rule: oklch(0.88 0.008 210);
  --accent: #0fb08a;
  --accent: oklch(0.7 0.13 168);
  --lift: 14px;
  --font-display: "Inter Tight", "Geist", system-ui, -apple-system, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-08 *,
.fs-08 *::before,
.fs-08 *::after {
  box-sizing: border-box;
}

.fs-08__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 20px;
  background: var(--card);
  border-block-end: 1px solid var(--rule);
}

.fs-08__wordmark {
  font: 700 15px/1 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-08__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-08__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 5vw, 60px) 16px calc(clamp(30px, 5vw, 60px) + var(--lift));
}

.fs-08__head {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  margin: 0 0 clamp(26px, 4vw, 44px);
  text-align: center;
}

.fs-08__eyebrow {
  margin: 0 0 12px;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #0a7d62;
  color: color-mix(in oklab, var(--accent) 78%, black);
}

.fs-08__heading {
  margin: 0 0 12px;
  font: 700 clamp(25px, 4.6vw, 38px)/1.12 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-08__sub {
  margin: 0 auto;
  max-inline-size: 52ch;
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-08__cols {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  grid-template-rows: auto auto repeat(6, auto) auto;
  gap: 14px;
  align-items: start;
}

.fs-08__col {
  min-inline-size: 0;
  display: grid;
  grid-row: span 9;
  gap: 0;
  padding: 22px 20px 20px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 12px;
  box-shadow: 0 6px 0 -1px color-mix(in oklab, var(--ink) 8%, transparent);
}

@supports (grid-template-rows: subgrid) {
  .fs-08__col {
    grid-template-rows: subgrid;
  }
}

.fs-08__col[data-featured] {
  margin-block-start: calc(var(--lift) * -1);
  padding-block-end: calc(20px + var(--lift));
  border-color: var(--accent);
  box-shadow: 0 10px 0 -2px color-mix(in oklab, var(--accent) 30%, transparent), 0 0 0 1px var(--accent) inset;
}

.fs-08__cols:has(.fs-08__col:hover) .fs-08__col:not(:hover) {
  opacity: 0.72;
}

.fs-08__flag {
  margin: 0 0 8px;
  justify-self: start;
  align-self: start;
  padding: 4px 10px;
  font: 700 10px/1.3 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #06563f;
  color: color-mix(in oklab, var(--accent) 82%, black);
  background: color-mix(in oklab, var(--accent) 18%, var(--card));
  border-radius: 999px;
}

.fs-08__col:not([data-featured]) .fs-08__flag {
  visibility: hidden;
}

.fs-08__chead {
  margin: 0 0 16px;
}

.fs-08__ctitle {
  margin: 0 0 4px;
  font: 700 clamp(19px, 2.4vw, 23px)/1.2 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-08__cnote {
  margin: 0;
  font-size: 12.5px;
  color: var(--muted);
}

.fs-08__rows {
  display: grid;
  grid-row: span 6;
  grid-template-rows: subgrid;
  margin: 0 0 18px;
  padding: 0;
  list-style: none;
  gap: 0;
}

@supports not (grid-template-rows: subgrid) {
  .fs-08__rows {
    grid-template-rows: repeat(6, minmax(44px, auto));
  }
}

.fs-08__row {
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr);
  align-items: center;
  gap: 10px;
  padding: 11px 0;
  border-block-end: 1px solid color-mix(in oklab, var(--rule) 70%, transparent);
  font-size: 13.5px;
  line-height: 1.45;
  min-inline-size: 0;
}

.fs-08__row:last-child {
  border-block-end: 0;
}

.fs-08__mk {
  font-size: 14px;
  font-weight: 700;
  text-align: center;
}

.fs-08__mk--yes {
  color: #0a7d62;
  color: color-mix(in oklab, var(--accent) 80%, black);
}

.fs-08__mk--no {
  color: var(--muted);
  opacity: 0.6;
}

.fs-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.fs-08__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  font: 650 13.5px/1 var(--font-display);
  text-decoration: none;
  color: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 9px;
  align-self: end;
}

.fs-08__cta:hover {
  background: color-mix(in oklab, var(--ink) 6%, var(--card));
}

.fs-08__cta--solid {
  color: #fff;
  background: var(--ink);
}

.fs-08__cta--solid:hover {
  background: color-mix(in oklab, var(--ink) 85%, var(--accent));
}

.fs-08__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fs-08__below {
  padding: 16px 20px;
  background: var(--card);
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@media (max-width: 800px) {
  .fs-08__cols {
    grid-template-rows: none;
  }

  .fs-08__col {
    grid-row: auto;
    grid-template-rows: none;
  }

  .fs-08__rows {
    grid-row: auto;
    grid-template-rows: none;
  }

  .fs-08__col[data-featured] {
    margin-block-start: 0;
    padding-block-end: 20px;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-08 {
    --page: #0e1518;
    --card: #151e22;
    --ink: #e9f2f3;
    --muted: #93a5ab;
    --rule: #243136;
    --accent: #2ad4a8;
  }

  .fs-08__cta {
    color: var(--ink);
    border-color: color-mix(in oklab, var(--ink) 40%, transparent);
  }

  .fs-08__cta--solid {
    color: #0e1518;
    background: var(--accent);
    border-color: var(--accent);
  }

  .fs-08__mk--yes,
    .fs-08__eyebrow,
    .fs-08__flag {
    color: var(--accent);
  }
}

[data-theme="dark"] .fs-08 {
  --page: #0e1518;
  --card: #151e22;
  --ink: #e9f2f3;
  --muted: #93a5ab;
  --rule: #243136;
  --accent: #2ad4a8;
}

[data-theme="dark"] .fs-08 .fs-08__cta--solid {
  color: #0e1518;
  background: var(--accent);
  border-color: var(--accent);
}
```
