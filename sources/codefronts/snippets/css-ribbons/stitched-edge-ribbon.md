---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/stitched-edge-ribbon/"
title: "Stitched Edge Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "Craft and handmade brands live or die on texture."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stitched Edge Ribbon
Source: https://codefronts.com/snippets/css-ribbons/stitched-edge-ribbon/

Craft and handmade brands live or die on texture. This ribbon is stitched — a dashed thread line set inside the band with outline-offset, a woven twill pattern from two crossed repeating gradients, real paper grain from an inline SVG turbulence filter, and a slightly tilted seat so it looks pinned rather than pasted.
## HTML
```html
<section class="rib-16" aria-label="Stitched edge ribbon with dashed border demo">
  <div class="rib-16__stage">
    <article class="rib-16__card">
      <div class="rib-16__photo">
        <img class="rib-16__img" alt="Hand-thrown ceramic mugs drying on a wooden workbench" loading="lazy" decoding="async" width="620" height="440"
          src="https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?q=80&w=760&auto=format&fit=crop">
        <div class="rib-16__ribbon"><span class="rib-16__rtxt">Handmade in Devon</span></div>
      </div>
      <div class="rib-16__body">
        <p class="rib-16__maker">Studio Marlowe · Batch 14</p>
        <h3 class="rib-16__name">Speckled stoneware mug, 320ml</h3>
        <p class="rib-16__desc">Wheel-thrown, twice-fired and glazed by hand, so no two are identical. Dishwasher safe, oven safe to 180°C.</p>
        <div class="rib-16__row">
          <span class="rib-16__price">£34</span>
          <span class="rib-16__stitchtag">Only 9 made</span>
        </div>
        <button class="rib-16__cta" type="button">Add to basket</button>
      </div>
    </article>
    <p class="rib-16__chip" aria-hidden="true">outline-offset thread · crossed twill gradients · feTurbulence grain data URI</p>
  </div>
</section>
```
## CSS
```css
.rib-16,
.rib-16 *,
.rib-16 *::before,
.rib-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-16-bg: #e7e0d3;
  --rib-16-bg: oklch(0.91 0.018 88);
  --rib-16-card: #fdf9f0;
  --rib-16-card: oklch(0.98 0.014 90);
  --rib-16-ink: #2b2419;
  --rib-16-ink: oklch(0.27 0.02 72);
  --rib-16-mut: #6f6555;
  --rib-16-mut: oklch(0.55 0.022 82);
  --rib-16-acc: #3f6b52;
  --rib-16-acc: oklch(0.5 0.09 155);
  --rib-16-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.4'/%3E%3C/svg%3E");
  background: var(--rib-16-bg);
  color: var(--rib-16-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,3vw,24px);
  padding: clamp(20px,5vw,56px);
  background-image: var(--rib-16-grain);
  background-blend-mode: multiply;
}

.rib-16__card {
  position: relative;
  width: min(100%,400px);
  border-radius: 8px;
  background: var(--rib-16-card);
  background-image: var(--rib-16-grain);
  background-blend-mode: multiply;
  box-shadow: 0 1px 2px oklch(0 0 0/.08),0 20px 44px -22px oklch(0.3 0.03 72/.55);
  outline: 1px solid color-mix(in oklch,var(--rib-16-ink) 12%,transparent);
  outline-offset: -1px;
}

.rib-16__photo {
  position: relative;
  aspect-ratio: 31/22;
  overflow: hidden;
  border-radius: 8px 8px 0 0;
  background: linear-gradient(140deg,oklch(0.86 0.02 88),oklch(0.8 0.03 70));
}

.rib-16__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.rib-16__ribbon {
  position: absolute;
  z-index: 1;
  inset-inline: -22px;
  inset-block-start: clamp(20px,6vw,36px);
  display: grid;
  place-items: center;
  padding: 13px 30px;
  rotate: -1.4deg;
  color: oklch(0.99 0.01 155);
  background-color: #3f6b52;
  background-image: repeating-linear-gradient(45deg,oklch(1 0 0/.075) 0 2px,transparent 2px 5px),repeating-linear-gradient(-45deg,oklch(0 0 0/.07) 0 2px,transparent 2px 5px),linear-gradient(180deg,color-mix(in oklch,var(--rib-16-acc) 100%,white 12%),var(--rib-16-acc) 60%,color-mix(in oklch,var(--rib-16-acc) 86%,black 10%));
  outline: 2px dashed oklch(1 0 0/.66);
  outline-offset: -7px;
  box-shadow: 0 8px 18px -8px oklch(0.25 0.05 155/.75),inset 0 0 0 1px oklch(0 0 0/.12);
}

.rib-16__rtxt {
  font-size: clamp(13px,2.8vw,15px);
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  text-shadow: 0 1px 2px oklch(0 0 0/.3);
}

.rib-16__ribbon::before,
.rib-16__ribbon::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inline-size: 14px;
  block-size: 12px;
  background: color-mix(in oklch,var(--rib-16-acc) 55%,black);
  z-index: -1;
}

.rib-16__ribbon::before {
  inset-inline-start: 22px;
  clip-path: polygon(0 0,100% 0,0 100%);
}

.rib-16__ribbon::after {
  inset-inline-end: 22px;
  clip-path: polygon(0 0,100% 0,100% 100%);
}

.rib-16__body {
  display: grid;
  gap: 9px;
  padding: clamp(20px,4vw,26px);
}

.rib-16__maker {
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--rib-16-acc);
}

.rib-16__name {
  font-size: 20px;
  font-weight: 640;
  letter-spacing: -.02em;
  line-height: 1.28;
  text-wrap: balance;
}

.rib-16__desc {
  font-size: 13.5px;
  line-height: 1.58;
  color: var(--rib-16-mut);
  text-wrap: pretty;
}

.rib-16__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-block-start: 4px;
}

.rib-16__price {
  font-size: 25px;
  font-weight: 750;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.rib-16__stitchtag {
  padding: 7px 13px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--rib-16-acc) 80%,black);
  background: color-mix(in oklch,var(--rib-16-acc) 10%,transparent);
  border-radius: 5px;
  outline: 1.5px dashed color-mix(in oklch,var(--rib-16-acc) 45%,transparent);
  outline-offset: -4px;
}

.rib-16__cta {
  margin-block-start: 8px;
  min-height: 48px;
  border: 0;
  border-radius: 8px;
  background: var(--rib-16-ink);
  color: oklch(0.98 0.012 88);
  font: inherit;
  font-size: 15px;
  font-weight: 650;
  cursor: pointer;
  outline: 1.5px dashed oklch(1 0 0/.4);
  outline-offset: -6px;
  transition: background .25s,translate .2s;
}

.rib-16__cta:hover {
  translate: 0 -1px;
  background: color-mix(in oklch,var(--rib-16-ink) 80%,var(--rib-16-acc));
}

.rib-16__cta:focus-visible {
  outline: 3px solid var(--rib-16-acc);
  outline-offset: 3px;
}

.rib-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-16-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-16 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
