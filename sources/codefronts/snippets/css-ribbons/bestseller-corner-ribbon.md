---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/bestseller-corner-ribbon/"
title: "Bestseller Corner Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A corner ribbon that is tied on rather than printed on."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bestseller Corner Ribbon
Source: https://codefronts.com/snippets/css-ribbons/bestseller-corner-ribbon/

A corner ribbon that is tied on rather than printed on. Demo 01 clips its band flush to the card; this one crosses the top-left corner at 45° and keeps going, overhanging both card edges, with two darker triangles folding under the card where a real ribbon would disappear. Overhang plus fold is what makes it read as a physical band. Gold-foil gradient, slow animated shine, and a tilt that deepens on hover — all from two pseudo-elements and one rotate.
## HTML
```html
<section class="rib-03" aria-label="Featured product bestseller ribbon demo">
  <div class="rib-03__stage">
    <article class="rib-03__card">
      <div class="rib-03__ribbon" aria-hidden="true"><span class="rib-03__label">BESTSELLER</span></div>
      <div class="rib-03__media">
        <img class="rib-03__img" alt="Black and silver over-ear studio headphones on a near-black backdrop" loading="lazy" decoding="async" width="640" height="520"
          src="https://images.unsplash.com/photo-1487215078519-e21cc028cb29?q=80&w=800&auto=format&fit=crop">
      </div>
      <div class="rib-03__body">
        <p class="rib-03__rank">Bestseller · #1 in Studio Headphones</p>
        <h3 class="rib-03__name">Auralis One Reference</h3>
        <p class="rib-03__stars"><span class="rib-03__starrow" aria-hidden="true">★★★★★</span><span class="rib-03__rate">4.9</span><span class="rib-03__count">2,418 reviews</span></p>
        <p class="rib-03__price">$249<span class="rib-03__unit">or $21/mo</span></p>
        <button class="rib-03__cta" type="button">View product</button>
      </div>
    </article>
    <p class="rib-03__chip" aria-hidden="true">corner wrap · rotate:-45deg · S×√2 + overhang · clip-path fold tails · foil sweep</p>
  </div>
</section>
```
## CSS
```css
.rib-03,
.rib-03 *,
.rib-03 *::before,
.rib-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-03-bg: #14120f;
  --rib-03-bg: oklch(0.19 0.014 75);
  --rib-03-card: #221f1a;
  --rib-03-card: oklch(0.26 0.016 78);
  --rib-03-ink: #f7f3ec;
  --rib-03-ink: oklch(0.97 0.012 85);
  --rib-03-mut: #a8a096;
  --rib-03-mut: oklch(0.72 0.018 82);
  --rib-03-acc: #e2b357;
  --rib-03-acc: oklch(0.81 0.14 82);
  --rib-03-cut: 118px;
  --rib-03-band: 38px;
  --rib-03-over: 17px;
  --rib-03-fold: 14px;
  --rib-03-top: 30px;
  --rib-03-len: calc(var(--rib-03-cut) * 1.415 + var(--rib-03-over) * 2);
  --rib-03-r: 22px;
  background: var(--rib-03-bg);
  color: var(--rib-03-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(24px,6vw,64px);
  background: radial-gradient(90% 70% at 50% 8%,color-mix(in oklch,var(--rib-03-acc) 13%,transparent),transparent 66%);
}

.rib-03__card {
  position: relative;
  width: min(100%,376px);
  overflow: visible;
  border-radius: var(--rib-03-r);
  background: var(--rib-03-card);
  border: 1px solid oklch(1 0 0/.09);
  box-shadow: 0 30px 70px -28px oklch(0 0 0/.85);
  transition: translate .45s cubic-bezier(.16,1,.3,1);
}

.rib-03__card:hover {
  translate: 0 -5px;
}

.rib-03__card:hover .rib-03__ribbon {
  rotate: -47deg;
  translate: -2px -2px;
}

.rib-03__ribbon {
  position: absolute;
  z-index: 3;
  inset-block-start: var(--rib-03-top);
  inset-inline-start: calc((var(--rib-03-len) - var(--rib-03-cut)) / -2);
  inline-size: var(--rib-03-len);
  min-block-size: var(--rib-03-band);
  display: grid;
  place-items: center;
  rotate: -45deg;
  transition: rotate .5s cubic-bezier(.16,1,.3,1),translate .5s cubic-bezier(.16,1,.3,1);
  background: #e2b357;
  background: linear-gradient(100deg,color-mix(in oklch,var(--rib-03-acc) 72%,black 6%) 0%,color-mix(in oklch,var(--rib-03-acc) 100%,white 22%) 34%,var(--rib-03-acc) 52%,color-mix(in oklch,var(--rib-03-acc) 74%,black 8%) 100%);
  background-size: 220% 100%;
  box-shadow: 0 10px 24px -10px oklch(0 0 0/.7),inset 0 1px 0 oklch(1 0 0/.45),inset 0 -1px 0 oklch(0 0 0/.22);
  animation: rib-03-foil 7s ease-in-out infinite;
}

@keyframes rib-03-foil {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

.rib-03__label {
  padding: 0 16px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .18em;
  line-height: 1;
  color: oklch(0.24 0.03 78);
  text-shadow: 0 1px 0 oklch(1 0 0/.32);
}

.rib-03__ribbon::before,
.rib-03__ribbon::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inline-size: var(--rib-03-over);
  block-size: var(--rib-03-fold);
  background: #8a6a25;
  background: color-mix(in oklch,var(--rib-03-acc) 58%,black);
  z-index: -1;
}

.rib-03__ribbon::before {
  inset-inline-start: 0;
  clip-path: polygon(0 0,100% 0,100% 100%);
}

.rib-03__ribbon::after {
  inset-inline-end: 0;
  clip-path: polygon(0 0,100% 0,0 100%);
}

.rib-03__media {
  aspect-ratio: 5/4;
  border-radius: var(--rib-03-r) var(--rib-03-r) 0 0;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.4 0.03 80),oklch(0.3 0.02 60));
}

.rib-03__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .7s cubic-bezier(.16,1,.3,1);
}

.rib-03__card:hover .rib-03__img {
  scale: 1.045;
}

.rib-03__body {
  display: grid;
  gap: 8px;
  padding: clamp(18px,4vw,24px);
}

.rib-03__rank {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--rib-03-acc);
}

.rib-03__name {
  font-size: 22px;
  font-weight: 640;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.rib-03__stars {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 13px;
  color: var(--rib-03-mut);
}

.rib-03__starrow {
  color: var(--rib-03-acc);
  letter-spacing: .08em;
  font-size: 14px;
}

.rib-03__rate {
  font-weight: 700;
  color: var(--rib-03-ink);
  font-variant-numeric: tabular-nums;
}

.rib-03__price {
  margin-top: 4px;
  font-size: 26px;
  font-weight: 750;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.rib-03__unit {
  font-size: 13px;
  font-weight: 400;
  color: var(--rib-03-mut);
}

.rib-03__cta {
  margin-top: 8px;
  min-height: 48px;
  border: 0;
  border-radius: 13px;
  background: var(--rib-03-acc);
  color: oklch(0.24 0.03 78);
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .25s,translate .2s;
}

.rib-03__cta:hover {
  filter: brightness(1.08);
  translate: 0 -1px;
}

.rib-03__cta:focus-visible {
  outline: 3px solid var(--rib-03-ink);
  outline-offset: 3px;
}

.rib-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-03-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-03 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```
