---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/freelance-web-developer-portfolio-layout-with-pricing-table/"
title: "Freelance Web Developer Portfolio Layout with Pricing Table"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "A portfolio that closes deals, not just compliments: proof first (client results as testimonial cards), then a three-tier pricing table with the middle plan…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Freelance Web Developer Portfolio Layout with Pricing Table
Source: https://codefronts.com/layouts/css-portfolio-layouts/freelance-web-developer-portfolio-layout-with-pricing-table/

A portfolio that closes deals, not just compliments: proof first (client results as testimonial cards), then a three-tier pricing table with the middle plan doing the featured-column trick — lifted, accent-bordered, 'Most booked' badge — and honest feature lists with real checkmarks drawn as CSS ::before glyphs. The tiers are one grid; the featured lift is one class; the whole section stacks cleanly when narrow.
## HTML
```html
<section class="cpl-12" aria-label="Freelance portfolio with pricing table demo">
  <div class="cpl-12__stage">
    <header class="cpl-12__head">
      <h2>Sites that pay for themselves.</h2>
      <p>I design and build marketing sites for founders — fixed scope, fixed price, two-week turnarounds.</p>
    </header>
    <div class="cpl-12__proof">
      <figure class="cpl-12__quote">
        <blockquote>"Paid for itself in five weeks. Conversion went from 1.1% to 2.9%."</blockquote>
        <figcaption><b>Dana W.</b> — founder, Saltbox Provisions</figcaption>
      </figure>
      <figure class="cpl-12__quote">
        <blockquote>"First contractor who shipped early. Lighthouse 100s across the board."</blockquote>
        <figcaption><b>Arjun M.</b> — CTO, Freightline</figcaption>
      </figure>
      <figure class="cpl-12__quote">
        <blockquote>"He rewrote our pricing page copy too. That page books 60% of demos now."</blockquote>
        <figcaption><b>Sofia R.</b> — CEO, Kettleworks</figcaption>
      </figure>
    </div>
    <h3 class="cpl-12__sub">Packages</h3>
    <div class="cpl-12__tiers">
      <article class="cpl-12__tier">
        <h4>Landing</h4>
        <p class="cpl-12__price">$2,400<small>/ project</small></p>
        <ul>
          <li>One page, custom design</li>
          <li>Copy polish included</li>
          <li>Analytics + SEO setup</li>
          <li class="cpl-12__no">CMS integration</li>
          <li class="cpl-12__no">A/B test setup</li>
        </ul>
        <a class="cpl-12__cta" href="#book-landing">Book Landing</a>
      </article>
      <article class="cpl-12__tier cpl-12__tier--feat">
        <span class="cpl-12__badge">Most booked</span>
        <h4>Marketing Site</h4>
        <p class="cpl-12__price">$6,800<small>/ project</small></p>
        <ul>
          <li>Up to 6 pages + blog</li>
          <li>CMS your team can use</li>
          <li>Copy polish included</li>
          <li>Analytics + SEO setup</li>
          <li class="cpl-12__no">A/B test setup</li>
        </ul>
        <a class="cpl-12__cta cpl-12__cta--feat" href="#book-site">Book Marketing Site</a>
      </article>
      <article class="cpl-12__tier">
        <h4>Growth Retainer</h4>
        <p class="cpl-12__price">$3,200<small>/ month</small></p>
        <ul>
          <li>Everything in Marketing Site</li>
          <li>A/B test setup + reporting</li>
          <li>2 experiments shipped monthly</li>
          <li>Same-week fixes</li>
          <li>Cancel anytime</li>
        </ul>
        <a class="cpl-12__cta" href="#book-retainer">Book Retainer</a>
      </article>
    </div>
    <p class="cpl-12__foot">Every package: performance budget ≤ 150KB, WCAG 2.2 AA, you own the repo. <a href="#call">Book a 20-minute intro call →</a></p>
  </div>
</section>
```
## CSS
```css
.cpl-12,
.cpl-12 *,
.cpl-12 *::before,
.cpl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-12 {
  --bg: oklch(0.975 0.005 260);
  --card: oklch(1 0 0);
  --ink: oklch(0.23 0.02 265);
  --mut: oklch(0.53 0.015 265);
  --line: oklch(0.89 0.008 265);
  --acc: oklch(0.55 0.19 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-12__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(20px,4cqi,32px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-12__head h2 {
  font-size: clamp(22px,3.6cqi,30px);
  letter-spacing: -.025em;
}

.cpl-12__head p {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 56ch;
}

.cpl-12__proof {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(215px,100%),1fr));
  margin-top: 22px;
}

.cpl-12__quote {
  display: grid;
  gap: 10px;
  align-content: space-between;
  padding: 18px;
  border-radius: 14px;
  background: var(--card);
  border: 1px solid var(--line);
}

.cpl-12__quote blockquote {
  font-size: 13.5px;
  line-height: 1.55;
  font-weight: 600;
  letter-spacing: -.005em;
  text-wrap: pretty;
}

.cpl-12__quote figcaption {
  font-size: 12px;
  color: var(--mut);
}

.cpl-12__quote b {
  color: var(--ink);
}

.cpl-12__sub {
  margin-top: 30px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mut);
}

.cpl-12__tiers {
  display: grid;
  gap: 14px;
  align-items: stretch;
  grid-template-columns: repeat(auto-fit,minmax(min(215px,100%),1fr));
  margin-top: 14px;
}

.cpl-12__tier {
  position: relative;
  display: grid;
  grid-template-rows: auto auto 1fr auto;
  gap: 12px;
  padding: 22px 20px;
  border-radius: 16px;
  background: var(--card);
  border: 1.5px solid var(--line);
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cpl-12__tier:hover {
  translate: 0 -3px;
  box-shadow: 0 18px 36px -24px oklch(0.35 0.05 265/.5);
}

.cpl-12__tier--feat {
  border-color: var(--acc);
  box-shadow: 0 24px 48px -28px oklch(0.55 0.19 265/.55);
}

.cpl-12__badge {
  position: absolute;
  top: -11px;
  left: 18px;
  padding: 4px 11px;
  border-radius: 99px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.99 0 0);
  background: var(--acc);
}

.cpl-12__tier h4 {
  font-size: 15px;
  letter-spacing: -.01em;
}

.cpl-12__price {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.cpl-12__price small {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  letter-spacing: 0;
  margin-left: 5px;
}

.cpl-12__tier ul {
  list-style: none;
  display: grid;
  gap: 9px;
  align-content: start;
}

.cpl-12__tier li {
  display: flex;
  gap: 9px;
  font-size: 13px;
  line-height: 1.45;
  color: oklch(0.38 0.015 265);
}

.cpl-12__tier li::before {
  content: "✓";
  font-weight: 800;
  color: var(--acc);
  flex: none;
}

.cpl-12__no {
  color: var(--mut) !important;
}

.cpl-12__no::before {
  content: "–" !important;
  color: oklch(0.75 0.01 265) !important;
}

.cpl-12__cta {
  display: grid;
  place-items: center;
  min-height: 44px;
  border-radius: 11px;
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid var(--line);
  transition: border-color .2s,background .2s,color .2s;
}

.cpl-12__cta:hover,
.cpl-12__cta:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.cpl-12__cta--feat {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.99 0 0);
}

.cpl-12__cta--feat:hover,
.cpl-12__cta--feat:focus-visible {
  background: oklch(0.48 0.19 265);
  color: oklch(0.99 0 0);
}

.cpl-12__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-12__foot {
  margin-top: 20px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cpl-12__foot a {
  color: var(--acc);
  font-weight: 700;
  text-decoration: none;
  padding: 4px 0;
}

.cpl-12__foot a:hover,
.cpl-12__foot a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cpl-12 * {
    transition-duration: .01ms !important;
  }
}
```
