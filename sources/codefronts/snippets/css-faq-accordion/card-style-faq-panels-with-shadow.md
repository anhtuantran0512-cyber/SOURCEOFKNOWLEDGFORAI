---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/card-style-faq-panels-with-shadow/"
title: "Card-Style FAQ Panels with Shadow"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Separated FAQ cards with a real elevation system: three shadow levels (resting, hover, open) built from layered box-shadows that mimic how light actually…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card-Style FAQ Panels with Shadow
Source: https://codefronts.com/snippets/css-faq-accordion/card-style-faq-panels-with-shadow/

Separated FAQ cards with a real elevation system: three shadow levels (resting, hover, open) built from layered box-shadows that mimic how light actually falls — a tight dark contact shadow plus a wide soft ambient one — instead of the single fuzzy gray blob of tutorial CSS. Cards lift 2px on hover and rise to full elevation when open, and the tutorial covers the performance rule for animating shadows and why shadow color should come from your palette, not black.
## HTML
```html
<section class="cfa-17" aria-label="Card style FAQ with elevation shadows">
  <div class="cfa-17__wrap">
    <header class="cfa-17__head">
      <h1>Warranty &amp; repairs</h1>
      <p>Three elevations: resting, hover-lift, open. Every shadow is two layers — contact + ambient — in the page's own hue.</p>
    </header>
    <div class="cfa-17__list">
      <details class="cfa-17__item" open>
        <summary class="cfa-17__q">What does the warranty cover?<i aria-hidden="true"></i></summary>
        <div class="cfa-17__a"><p>Two years, parts and labor, covering manufacturing defects and battery health below 80%. Accidental damage is a separate care plan — but out-of-warranty repairs are flat-rate and published, never “send it in for a quote”.</p></div>
      </details>
      <details class="cfa-17__item">
        <summary class="cfa-17__q">How do I start a repair?<i aria-hidden="true"></i></summary>
        <div class="cfa-17__a"><p>Run the diagnostic in the app, which pre-fills the repair ticket with logs. A prepaid label arrives by email; most repairs turn around in 5 business days door to door, with a loaner option on the care plan.</p></div>
      </details>
      <details class="cfa-17__item">
        <summary class="cfa-17__q">Can I repair it myself?<i aria-hidden="true"></i></summary>
        <div class="cfa-17__a"><p>Yes — self-repair kits with genuine parts, tools and guides cover the battery, screen and buttons. DIY repairs with our parts don't void the warranty; third-party parts void only the affected subsystem.</p></div>
      </details>
      <details class="cfa-17__item">
        <summary class="cfa-17__q">Is water damage covered?<i aria-hidden="true"></i></summary>
        <div class="cfa-17__a"><p>IP67 failures within rating are warranty repairs — a pressure test tells us quickly. Beyond-rating exposure (diving, jacuzzi chemistry) falls to the care plan's accidental tier at the flat rate.</p></div>
      </details>
    </div>
    <p class="cfa-17__foot">Shadow recipe: tight contact layer + wide ambient layer, tinted oklch(0.35 0.04 265). Never plain black. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-17,
.cfa-17 *,
.cfa-17 *::before,
.cfa-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-17 {
  --bg: oklch(0.96 0.012 265);
  --panel: oklch(1 0 0);
  --ink: oklch(0.24 0.03 268);
  --mut: oklch(0.5 0.02 265);
  --line: oklch(0.9 0.012 265);
  --acc: oklch(0.52 0.17 268);
  --shadow-rest: 0 1px 2px oklch(0.35 0.04 265/.1),0 4px 12px oklch(0.35 0.04 265/.07);
  --shadow-hover: 0 2px 3px oklch(0.35 0.04 265/.12),0 8px 20px oklch(0.35 0.04 265/.1);
  --shadow-open: 0 2px 4px oklch(0.35 0.04 265/.12),0 12px 32px oklch(0.35 0.04 265/.14),0 24px 60px oklch(0.35 0.04 265/.1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-17__wrap {
  width: min(100%,620px);
}

.cfa-17__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-17__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-17__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  interpolate-size: allow-keywords;
}

.cfa-17__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: var(--shadow-rest);
  transition: box-shadow .35s cubic-bezier(.4,0,.2,1),translate .35s cubic-bezier(.4,0,.2,1),border-color .35s;
}

.cfa-17__item:not([open]):hover {
  box-shadow: var(--shadow-hover);
  translate: 0 -2px;
}

.cfa-17__item[open] {
  box-shadow: var(--shadow-open);
  border-color: transparent;
  translate: 0 -2px;
}

.cfa-17__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 18px 20px;
  cursor: pointer;
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  list-style: none;
  transition: color .2s;
}

.cfa-17__q::-webkit-details-marker {
  display: none;
}

.cfa-17__q:hover {
  color: var(--acc);
}

.cfa-17__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 18px;
}

.cfa-17__q i {
  flex: none;
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 10px;
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  position: relative;
  transition: rotate .4s cubic-bezier(.4,0,.2,1);
}

.cfa-17__q i::before {
  content: "";
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -1.5px;
}

.cfa-17__item[open] .cfa-17__q i {
  rotate: 180deg;
}

.cfa-17__a p {
  padding: 0 20px 19px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-17__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
  }

  .cfa-17__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-17__foot {
  margin-top: 24px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-17 *,
    .cfa-17 .cfa-17__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
