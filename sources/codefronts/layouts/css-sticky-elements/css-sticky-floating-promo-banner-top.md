---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-floating-promo-banner-top/"
title: "CSS Sticky Floating Promo Banner Top"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The announcement bar above the store nav — free shipping, promo code, ends Sunday — pinned at top: 0 with the nav pinned beneath it, and a dismiss button…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Floating Promo Banner Top
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-floating-promo-banner-top/

The announcement bar above the store nav — free shipping, promo code, ends Sunday — pinned at top: 0 with the nav pinned beneath it, and a dismiss button that works with zero JavaScript: a hidden checkbox, a :has() selector, and one custom property that re-docks the nav to top: 0 the instant the banner disappears. The whole layout breathes through a single --bannerH variable.
## HTML
```html
<section class="cst-12" aria-label="Sticky promo banner above navigation demo">
  <div class="cst-12__stage" id="cst12-top">
    <input class="cst-12__hidecb" type="checkbox" id="cst12-hide">
    <div class="cst-12__banner">
      <p><strong>Free shipping over $75</strong><span class="cst-12__sep" aria-hidden="true">·</span>code <code>SUNDAY</code><span class="cst-12__sep" aria-hidden="true">·</span>ends Sunday midnight</p>
      <label class="cst-12__x" for="cst12-hide" role="button" aria-label="Dismiss announcement" tabindex="0">✕</label>
    </div>
    <header class="cst-12__nav">
      <a class="cst-12__brand" href="#cst12-top">Larder<span>&amp;Co</span></a>
      <nav aria-label="Shop"><a href="#cst12-shop" aria-current="true">Pantry</a><a href="#cst12-shop">Fresh</a><a href="#cst12-shop">Cellar</a><a href="#cst12-shop">Gifts</a></nav>
      <a class="cst-12__cart" href="#cst12-cart">Basket · $0</a>
    </header>
    <section class="cst-12__hero">
      <h1>Small-batch pantry, big-batch opinions.</h1>
      <p>Two sticky layers above: banner at <code>top: 0</code>, nav at <code>top: var(--bannerH)</code>. Hit the ✕ — the variable flips to 0 and the nav docks flush. Pure CSS.</p>
    </section>
    <section class="cst-12__shop" id="cst12-shop">
      <header><h2>This week's shelf</h2><a href="#cst12-all">View all 48 →</a></header>
      <div class="cst-12__grid">
        <a href="#cst12-p1"><figure style="--img:url('https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.09 90);--b:oklch(0.55 0.11 60)"></figure><div><h3>Single-orchard olive oil</h3><p>Picual, November press</p><span>$28</span></div></a>
        <a href="#cst12-p2"><figure style="--img:url('https://images.unsplash.com/photo-1467003909585-2f8a72700288?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.08 40);--b:oklch(0.52 0.1 20)"></figure><div><h3>Cedar-smoked salmon</h3><p>Wild-caught, BC coast</p><span>$19</span></div></a>
        <a href="#cst12-p3"><figure style="--img:url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=800&auto=format&fit=crop');--a:oklch(0.82 0.07 130);--b:oklch(0.55 0.09 150)"></figure><div><h3>Sunday roast box</h3><p>Feeds six, forgives four</p><span>$64</span></div></a>
        <a href="#cst12-p4"><figure style="--img:url('https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format&fit=crop');--a:oklch(0.84 0.08 140);--b:oklch(0.6 0.1 110)"></figure><div><h3>Harvest grain bowls</h3><p>Kit of four, 12-min prep</p><span>$22</span></div></a>
        <a href="#cst12-p5"><figure style="--img:url('https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.09 25);--b:oklch(0.55 0.12 350)"></figure><div><h3>Chili crisp, hot batch</h3><p>No. 14 — allegedly legal</p><span>$14</span></div></a>
        <a href="#cst12-p6"><figure style="--img:url('https://images.unsplash.com/photo-1481349518771-20055b2a7b24?q=80&w=800&auto=format&fit=crop');--a:oklch(0.85 0.06 100);--b:oklch(0.62 0.09 80)"></figure><div><h3>Breakfast board</h3><p>Sourdough, jam, the works</p><span>$31</span></div></a>
      </div>
    </section>
    <section class="cst-12__strip"><p>“The banner asked me to buy olive oil. I dismissed the banner. The olive oil remained excellent.” — <em>a customer, correctly</em></p></section>
    <footer class="cst-12__footer" id="cst12-cart"><p><strong>Larder &amp; Co</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst12-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-12,
.cst-12 *,
.cst-12 *::before,
.cst-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-12 {
  --bg: oklch(0.977 0.006 95);
  --ink: oklch(0.24 0.02 80);
  --mut: oklch(0.5 0.02 80);
  --line: oklch(0.89 0.012 90);
  --acc: oklch(0.55 0.15 145);
  --bannerH: 44px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-12__stage {
  width: 100%;
  container: cst12/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-padding-top: calc(var(--bannerH) + 66px);
}

.cst-12__hidecb {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.cst-12__stage:has(#cst12-hide:checked) {
  --bannerH: 0px;
}

.cst-12__stage:has(#cst12-hide:checked) .cst-12__banner {
  display: none;
}

.cst-12__banner {
  position: sticky;
  top: 0;
  z-index: 7;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  height: var(--bannerH);
  padding: 0 52px 0 16px;
  color: oklch(0.98 0.01 145);
  background: linear-gradient(100deg,oklch(0.42 0.11 150),oklch(0.5 0.13 130));
  font-size: 12.5px;
}

.cst-12__banner p {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cst-12__banner strong {
  font-weight: 800;
}

.cst-12__banner code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 700;
  background: oklch(1 0 0/.18);
  padding: 2px 8px;
  border-radius: 6px;
  letter-spacing: .06em;
}

.cst-12__sep {
  opacity: .6;
}

.cst-12__x {
  position: absolute;
  right: 6px;
  top: 50%;
  translate: 0 -50%;
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  border-radius: 9px;
  font-size: 14px;
  cursor: pointer;
  transition: background .2s;
}

.cst-12__x:hover,
.cst-12__x:focus-visible {
  background: oklch(1 0 0/.18);
}

.cst-12__x:focus-visible {
  outline: 2px solid oklch(0.98 0 0);
  outline-offset: 1px;
}

.cst-12__nav {
  position: sticky;
  top: var(--bannerH);
  z-index: 6;
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,26px);
  height: 60px;
  padding: 0 clamp(16px,4cqi,40px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}

.cst-12__brand {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.cst-12__brand span {
  color: var(--acc);
}

.cst-12__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-12__nav nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-12__nav nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-12__nav nav a:hover,
.cst-12__nav nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.92 0.015 95);
}

.cst-12__nav nav a[aria-current] {
  color: var(--ink);
  box-shadow: inset 0 -2px var(--acc);
}

.cst-12__nav nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-12__cart {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.98 0 0);
  background: var(--ink);
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.cst-12__cart:hover,
.cst-12__cart:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cst-12__cart:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-12__hero {
  padding: clamp(36px,7cqi,72px) clamp(16px,4cqi,40px) clamp(26px,4cqi,44px);
}

.cst-12__hero h1 {
  font-size: clamp(32px,6.5cqi,64px);
  line-height: 1;
  letter-spacing: -.035em;
  font-weight: 800;
  max-width: 18ch;
  text-wrap: balance;
}

.cst-12__hero p {
  margin-top: 16px;
  max-width: 58ch;
  font-size: 15px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-12__hero code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.91 0.015 95);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-12__shop {
  padding: 0 clamp(16px,4cqi,40px) clamp(36px,6cqi,64px);
}

.cst-12__shop header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 18px;
}

.cst-12__shop h2 {
  font-size: clamp(22px,3.6cqi,32px);
  letter-spacing: -.025em;
  font-weight: 800;
}

.cst-12__shop header a {
  font-size: 13px;
  font-weight: 700;
  color: var(--acc);
  text-decoration: none;
  padding: 8px 0;
}

.cst-12__shop header a:hover,
.cst-12__shop header a:focus-visible {
  text-decoration: underline;
}

.cst-12__shop header a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.cst-12__grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fill,minmax(min(215px,100%),1fr));
}

.cst-12__grid a {
  border-radius: 16px;
  overflow: hidden;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cst-12__grid a:hover,
.cst-12__grid a:focus-visible {
  translate: 0 -3px;
  box-shadow: 0 14px 30px oklch(0.35 0.04 90/.12);
}

.cst-12__grid a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-12__grid figure {
  aspect-ratio: 4/3;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .45s cubic-bezier(.2,.7,.2,1);
}

.cst-12__grid a:hover figure {
  scale: 1.05;
}

.cst-12__grid div {
  display: grid;
  gap: 2px;
  padding: 13px 15px 15px;
}

.cst-12__grid h3 {
  font-size: 14.5px;
  letter-spacing: -.01em;
}

.cst-12__grid p {
  font-size: 12px;
  color: var(--mut);
}

.cst-12__grid span {
  margin-top: 7px;
  font-size: 14px;
  font-weight: 800;
  color: var(--acc);
}

.cst-12__strip {
  padding: clamp(36px,7cqi,68px) clamp(16px,4cqi,40px);
  background: oklch(0.93 0.015 95);
}

.cst-12__strip p {
  max-width: 60ch;
  margin-inline: auto;
  text-align: center;
  font-size: clamp(16px,2.6cqi,21px);
  line-height: 1.5;
  font-weight: 600;
  letter-spacing: -.005em;
}

.cst-12__strip em {
  font-style: normal;
  font-weight: 400;
  font-size: .75em;
  color: var(--mut);
}

.cst-12__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 26px clamp(16px,4cqi,40px) 38px;
}

.cst-12__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-12__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-12__footer a:hover,
.cst-12__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-12__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst12 (width < 620px) {
  .cst-12__nav nav {
    display: none;
  }

  .cst-12__banner {
    font-size: 11.5px;
    justify-content: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-12 * {
    transition-duration: .01ms !important;
    scale: none !important;
  }
}
```
