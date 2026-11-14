---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/corner-sale-ribbon-for-product-cards/"
title: "Corner Sale Ribbon for Product Cards"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The corner ribbon every storefront ships: a 45° discount band flush across the top-right of a product card, clipped perfectly to the card's rounded corner."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Sale Ribbon for Product Cards
Source: https://codefronts.com/snippets/css-ribbons/corner-sale-ribbon-for-product-cards/

The corner ribbon every storefront ships: a 45° discount band flush across the top-right of a product card, clipped perfectly to the card's rounded corner. The geometry is parametric rather than hardcoded — one --rib-01-size value drives the corner box, the band length and the offset, so the same ribbon works on a 200px thumbnail and a 600px hero. A one-shot sheen sweeps the band on load and replays on hover.
## HTML
```html
<section class="rib-01" aria-label="Corner sale ribbon demo">
  <div class="rib-01__stage">
    <article class="rib-01__card">
      <div class="rib-01__media">
        <img class="rib-01__img" alt="Pale grey and blue running shoe photographed on a light neutral backdrop" loading="lazy" decoding="async" width="640" height="480"
          src="https://images.unsplash.com/photo-1560769629-975ec94e6a86?q=80&w=800&auto=format&fit=crop">
      </div>
      <div class="rib-01__ribbon" id="rib-01-offer" role="img" aria-label="50 percent off this week">
        <span class="rib-01__band"><span class="rib-01__label">50% OFF</span></span>
      </div>
      <div class="rib-01__body">
        <p class="rib-01__brand">Meridian Athletics</p>
        <h3 class="rib-01__name" aria-describedby="rib-01-offer">Trailform GT Runner</h3>
        <p class="rib-01__price"><span class="rib-01__now">$89</span><s class="rib-01__was">$178</s><span class="rib-01__save">You save $89</span></p>
        <button class="rib-01__cta" type="button">Add to bag</button>
        <p class="rib-01__ship">Free returns · Ships tomorrow</p>
      </div>
    </article>
    <p class="rib-01__chip" aria-hidden="true">overflow clip · rotate: 45deg · S × √2 band · clip-path: inset(round)</p>
  </div>
</section>
```
## CSS
```css
.rib-01,
.rib-01 *,
.rib-01 *::before,
.rib-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-01-bg: #f2f0ec;
  --rib-01-bg: oklch(0.96 0.006 85);
  --rib-01-card: #fff;
  --rib-01-card: oklch(1 0 0);
  --rib-01-ink: #231f1d;
  --rib-01-ink: oklch(0.24 0.012 60);
  --rib-01-mut: #6f6862;
  --rib-01-mut: oklch(0.56 0.014 60);
  --rib-01-acc: #d8412f;
  --rib-01-acc: oklch(0.58 0.21 27);
  --rib-01-size: clamp(104px,26vw,148px);
  --rib-01-band: 38px;
  --rib-01-offset: 30px;
  --rib-01-len: calc(var(--rib-01-size) * 1.415 + var(--rib-01-band) * 2);
  --rib-01-r: 26px;
  background: var(--rib-01-bg);
  color: var(--rib-01-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,26px);
  padding: clamp(18px,5vw,56px);
  background: radial-gradient(120% 90% at 50% 0%,color-mix(in oklch,var(--rib-01-acc) 9%,transparent),transparent 62%);
}

.rib-01__card {
  position: relative;
  width: min(100%,380px);
  background: var(--rib-01-card);
  border-radius: var(--rib-01-r);
  clip-path: inset(0 round var(--rib-01-r));
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 22px 48px -18px oklch(0.35 0.03 60/.4);
  transition: box-shadow .45s cubic-bezier(.16,1,.3,1),translate .45s cubic-bezier(.16,1,.3,1);
}

.rib-01__card:hover {
  translate: 0 -4px;
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 34px 64px -20px oklch(0.35 0.06 27/.42);
}

.rib-01__media {
  aspect-ratio: 4/3;
  background: linear-gradient(140deg,oklch(0.9 0.03 70),oklch(0.83 0.05 40));
}

.rib-01__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.rib-01__ribbon {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  inline-size: var(--rib-01-size);
  aspect-ratio: 1;
  overflow: hidden;
  pointer-events: none;
  z-index: 2;
  filter: drop-shadow(0 5px 12px color-mix(in oklch,var(--rib-01-acc) 42%,transparent)) drop-shadow(0 1px 2px oklch(0 0 0/.22));
}

.rib-01__band {
  position: absolute;
  inset-block-start: var(--rib-01-offset);
  inset-inline-end: calc((var(--rib-01-len) - var(--rib-01-size)) / -2);
  inline-size: var(--rib-01-len);
  min-block-size: var(--rib-01-band);
  display: grid;
  place-items: center;
  overflow: hidden;
  rotate: 45deg;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-01-acc) 88%,white 12%),var(--rib-01-acc));
  box-shadow: inset 0 -1px 0 oklch(0 0 0/.18);
}

.rib-01__label {
  padding: 9px 14px;
  color: oklch(0.99 0 0);
  font-size: clamp(12px,3vw,14px);
  font-weight: 800;
  letter-spacing: .1em;
  line-height: 1;
  white-space: nowrap;
  text-shadow: 0 1px 2px oklch(0 0 0/.28);
}

.rib-01__band::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 30%,oklch(1 0 0/.55) 48%,transparent 62%);
  translate: -120% 0;
  animation: rib-01-sheen 1.5s cubic-bezier(.16,1,.3,1) .45s both;
}

.rib-01__card:hover .rib-01__band::after {
  animation: rib-01-sheen 1.1s cubic-bezier(.16,1,.3,1) both;
}

@keyframes rib-01-sheen {
  from {
    translate: -120% 0;
  }

  to {
    translate: 120% 0;
  }
}

.rib-01__body {
  display: grid;
  gap: 7px;
  padding: clamp(18px,4vw,24px);
}

.rib-01__brand {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--rib-01-mut);
}

.rib-01__name {
  font-size: clamp(19px,4vw,22px);
  font-weight: 640;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.rib-01__price {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 9px;
  margin-top: 2px;
  font-variant-numeric: tabular-nums;
}

.rib-01__now {
  font-size: 24px;
  font-weight: 750;
  letter-spacing: -.03em;
}

.rib-01__was {
  font-size: 15px;
  color: var(--rib-01-mut);
  text-decoration-thickness: 1.5px;
}

.rib-01__save {
  font-size: 12px;
  font-weight: 700;
  padding: 4px 9px;
  border-radius: 99px;
  color: color-mix(in oklch,var(--rib-01-acc) 72%,black);
  background: color-mix(in oklch,var(--rib-01-acc) 13%,transparent);
}

.rib-01__cta {
  margin-top: 10px;
  min-height: 48px;
  border: 0;
  border-radius: 14px;
  background: var(--rib-01-ink);
  color: oklch(0.99 0 0);
  font: inherit;
  font-size: 15px;
  font-weight: 660;
  cursor: pointer;
  transition: background .25s,translate .2s;
}

.rib-01__cta:hover {
  background: color-mix(in oklch,var(--rib-01-ink) 82%,var(--rib-01-acc));
  translate: 0 -1px;
}

.rib-01__cta:active {
  translate: 0 0;
  scale: .99;
}

.rib-01__cta:focus-visible {
  outline: 3px solid var(--rib-01-acc);
  outline-offset: 3px;
}

.rib-01__ship {
  font-size: 12px;
  color: var(--rib-01-mut);
}

.rib-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-01-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-01 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }

  .rib-01__band::after {
    display: none;
  }
}
```
