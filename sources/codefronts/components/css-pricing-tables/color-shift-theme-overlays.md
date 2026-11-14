---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/color-shift-theme-overlays/"
title: "Color Shift Theme Overlays"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Each tier carries its own brand hue: hovering a card floods its accent color through the price, checkmarks, divider and CTA at once — and gently tints the…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color Shift Theme Overlays
Source: https://codefronts.com/components/css-pricing-tables/color-shift-theme-overlays/

Each tier carries its own brand hue: hovering a card floods its accent color through the price, checkmarks, divider and CTA at once — and gently tints the whole section's backdrop to match — all by transitioning a single custom property per card.
## HTML
```html
<section class="prc-09" aria-label="Pricing cards with per-plan color themes">
  <div class="prc-09__wash" aria-hidden="true"></div>
  <div class="prc-09__grid">
    <article class="prc-09__card" style="--h:160"><h3>Mint</h3><p class="prc-09__price">$12<small>/mo</small></p><hr class="prc-09__rule"><ul><li>Personal license</li><li>20 exports / mo</li><li>720p renders</li></ul><a href="#" class="prc-09__cta">Get Mint</a></article>
    <article class="prc-09__card" style="--h:280"><h3>Violet</h3><p class="prc-09__price">$32<small>/mo</small></p><hr class="prc-09__rule"><ul><li>Commercial license</li><li>Unlimited exports</li><li>4K renders</li><li>Brand kits</li></ul><a href="#" class="prc-09__cta">Get Violet</a></article>
    <article class="prc-09__card" style="--h:40"><h3>Amber</h3><p class="prc-09__price">$79<small>/mo</small></p><hr class="prc-09__rule"><ul><li>Team license</li><li>Shared libraries</li><li>8K renders</li></ul><a href="#" class="prc-09__cta">Get Amber</a></article>
  </div>
</section>
```
## CSS
```css
.prc-09,
.prc-09 *,
.prc-09 *::before,
.prc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-09 {
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #101014;
  color: #ecedf2;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  overflow: hidden;
}

.prc-09__wash {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 80% at 50% 110%,oklch(0.45 0.16 var(--wash,280)/.35),transparent 70%);
  opacity: 0;
  transition: opacity .6s;
  pointer-events: none;
}

.prc-09:has(.prc-09__card:hover) .prc-09__wash {
  opacity: 1;
}

.prc-09:has(.prc-09__card[style*="--h:160"]:hover) {
  --wash: 160;
}

.prc-09:has(.prc-09__card[style*="--h:280"]:hover) {
  --wash: 280;
}

.prc-09:has(.prc-09__card[style*="--h:40"]:hover) {
  --wash: 40;
}

.prc-09__grid {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 20px;
  width: min(880px,100%);
}

.prc-09__card {
  --c: 0.02;
  --tone: oklch(0.72 var(--c) var(--h));
  background: #17171d;
  border: 1.5px solid oklch(0.35 calc(var(--c)*2) var(--h));
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition: border-color .45s,transform .3s;
}

.prc-09__card:hover,
.prc-09__card:focus-within {
  --c: 0.17;
  transform: translateY(-5px);
}

.prc-09__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--tone);
  transition: color .45s;
}

.prc-09__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-09__price small {
  font-size: 15px;
  font-weight: 600;
  color: #878b9c;
}

.prc-09__rule {
  border: none;
  height: 1.5px;
  background: oklch(0.4 calc(var(--c)*1.6) var(--h));
  transition: background-color .45s;
}

.prc-09__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 13.5px;
  color: #b4b8c8;
  flex: 1;
}

.prc-09__card li::before {
  content: "✓";
  color: var(--tone);
  font-weight: 700;
  margin-right: 9px;
  transition: color .45s;
}

.prc-09__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  background: oklch(0.3 calc(var(--c)*1.2) var(--h));
  color: #fff;
  transition: background-color .45s;
}

.prc-09__card:hover .prc-09__cta {
  background: oklch(0.55 var(--c) var(--h));
}

.prc-09__cta:focus-visible {
  outline: 3px solid var(--tone);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-09__card,
    .prc-09__card *,
    .prc-09__wash {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — each card declares only --h (its hue); every accent derives via oklch(L C var(--h)), and hover raises the chroma variable so the whole card saturates in one transition. A :has() rule retints the page wash to match. */
```
