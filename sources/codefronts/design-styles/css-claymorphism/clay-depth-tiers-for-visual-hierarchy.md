---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-depth-tiers-for-visual-hierarchy/"
title: "Clay Depth Tiers for Visual Hierarchy"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Four elevation tiers — inset well, resting, raised, floating — driven by a single --elev number per element."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Depth Tiers for Visual Hierarchy
Source: https://codefronts.com/design-styles/css-claymorphism/clay-depth-tiers-for-visual-hierarchy/

Four elevation tiers — inset well, resting, raised, floating — driven by a single --elev number per element. Every shadow length, blur and highlight strength is computed from it with calc(), so a component changes tier by changing one integer. Hover promotes a card one tier, which is how clay communicates interactivity without borders or color changes.
## HTML
```html
<section class="cl-07" aria-label="Clay depth tiers for visual hierarchy demo">
  <div class="cl-07__stage">
    <header class="cl-07__head">
      <h2 class="cl-07__h">Four tiers, one number</h2>
      <p class="cl-07__lede">Hover any tile: it is promoted exactly one tier. Every length below is calc()-derived from <code>--elev</code>.</p>
    </header>
    <div class="cl-07__well">
      <p class="cl-07__wellLabel">Tier 0 — inset well · holds content</p>
      <div class="cl-07__row">
        <article class="cl-07__tile" style="--cl-07-elev:1">
          <b class="cl-07__t">Tier 1</b>
          <span class="cl-07__d">Resting surface</span>
          <span class="cl-07__use">lists, groups, rows</span>
        </article>
        <article class="cl-07__tile" style="--cl-07-elev:2">
          <b class="cl-07__t">Tier 2</b>
          <span class="cl-07__d">Raised surface</span>
          <span class="cl-07__use">cards, buttons, tabs</span>
        </article>
        <article class="cl-07__tile" style="--cl-07-elev:3">
          <b class="cl-07__t">Tier 3</b>
          <span class="cl-07__d">Floating surface</span>
          <span class="cl-07__use">menus, popovers, FABs</span>
        </article>
      </div>
    </div>
    <p class="cl-07__chip" aria-hidden="true">--elev drives shadow length + blur + highlight + translate</p>
  </div>
</section>
```
## CSS
```css
.cl-07,
.cl-07 *,
.cl-07 *::before,
.cl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-07-bg);
  --cl-07-bg: oklch(0.93 0.03 15);
  --cl-07-clay: oklch(0.88 0.06 20);
  --cl-07-shade: oklch(0.58 0.1 18/.55);
  --cl-07-light: oklch(1 0.015 40/.95);
  --cl-07-ink: oklch(0.3 0.05 20);
  --cl-07-mut: oklch(0.51 0.04 20);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-07-ink);
}

.cl-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,4vw,36px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(80% 55% at 50% 0%,oklch(0.97 0.03 30),transparent 66%);
}

.cl-07__head {
  text-align: center;
  max-width: 58ch;
  display: grid;
  gap: 9px;
}

.cl-07__h {
  font-size: clamp(24px,3.8vw,34px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-07__lede {
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-07-mut);
  text-wrap: pretty;
}

.cl-07__lede code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13.5px;
}

.cl-07__well {
  width: min(100%,900px);
  display: grid;
  gap: 16px;
  padding: clamp(20px,3vw,32px);
  border-radius: 44px;
  background: color-mix(in oklch,var(--cl-07-bg) 94%,oklch(0.7 0.06 20));
  box-shadow: inset 0 14px 26px -10px var(--cl-07-shade),inset 0 -12px 22px -12px var(--cl-07-light);
}

.cl-07__wellLabel {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--cl-07-mut);
  text-align: center;
}

.cl-07__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(196px,1fr));
  gap: clamp(16px,2.6vw,26px);
  align-items: center;
}

.cl-07__tile {
  --cl-07-elev: 2;
  display: grid;
  gap: 5px;
  align-content: center;
  min-height: 150px;
  padding: 24px;
  border-radius: 34px;
  background: var(--cl-07-clay);
  translate: 0 calc(var(--cl-07-elev) * -1px);
  box-shadow: 0 calc(var(--cl-07-elev) * 9px) calc(var(--cl-07-elev) * 18px) calc(var(--cl-07-elev) * -5px) var(--cl-07-shade),inset 0 calc(var(--cl-07-elev) * -5px) calc(var(--cl-07-elev) * 9px) -8px var(--cl-07-shade),inset 0 calc(var(--cl-07-elev) * 6px) calc(var(--cl-07-elev) * 9px) -6px var(--cl-07-light);
  transition: box-shadow .4s cubic-bezier(.4,0,.2,1),translate .4s cubic-bezier(.34,1.3,.5,1),scale .4s cubic-bezier(.34,1.3,.5,1);
  cursor: pointer;
}

.cl-07__tile:nth-child(1):hover,
.cl-07__tile:nth-child(1):focus-visible {
  --cl-07-elev: 2;
}

.cl-07__tile:nth-child(2):hover,
.cl-07__tile:nth-child(2):focus-visible {
  --cl-07-elev: 3;
}

.cl-07__tile:nth-child(3):hover,
.cl-07__tile:nth-child(3):focus-visible {
  --cl-07-elev: 4;
  scale: 1.02;
}

.cl-07__tile:active {
  --cl-07-elev: 0;
  translate: 0;
  box-shadow: inset 0 12px 22px -8px var(--cl-07-shade),inset 0 -10px 18px -10px var(--cl-07-light);
}

.cl-07__t {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--cl-07-ink) 60%,transparent);
}

.cl-07__d {
  font-size: 19px;
  font-weight: 740;
  letter-spacing: -.015em;
}

.cl-07__use {
  font-size: 13px;
  color: color-mix(in oklch,var(--cl-07-ink) 72%,transparent);
}

.cl-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-07-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-07-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-07 * {
    transition-duration: .01ms !important;
  }
}
```
