---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-secondary-header-tabs/"
title: "CSS Sticky Secondary Header Tabs"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "Two cooperating stickies: the main store header pins at top: 0, and a product tab bar (Overview · Specs · Reviews · FAQ) pins directly beneath it at top:…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Secondary Header Tabs
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-secondary-header-tabs/

Two cooperating stickies: the main store header pins at top: 0, and a product tab bar (Overview · Specs · Reviews · FAQ) pins directly beneath it at top: var(--h1) — the offset handshake that keeps stacked bars from overlapping or leapfrogging. Tab clicks highlight themselves with a pure-CSS :has(:target) scrollspy, and every section clears both bars via scroll-margin-top. The pattern behind every product page, app settings screen and API reference built this decade.
## HTML
```html
<section class="cst-04" aria-label="Sticky secondary header tabs demo">
  <div class="cst-04__stage" id="cst04-top">
    <header class="cst-04__header">
      <a class="cst-04__brand" href="#cst04-top"><i aria-hidden="true"></i>Meridian Audio</a>
      <nav aria-label="Store"><a href="#cst04-overview">Headphones</a><a href="#cst04-specs">Speakers</a><a href="#cst04-faq">Support</a></nav>
      <a class="cst-04__cart" href="#cst04-cart">Cart · 1</a>
    </header>
    <section class="cst-04__intro">
      <figure style="--img:url('https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1200&auto=format&fit=crop')"></figure>
      <div>
        <p class="cst-04__kicker">M1 · Over-ear · 2026</p>
        <h1>Meridian M1 Wireless</h1>
        <p class="cst-04__rating" aria-label="Rated 4.8 out of 5 from 1,204 reviews"><span aria-hidden="true">★★★★★</span> 4.8 · 1,204 reviews</p>
        <p class="cst-04__price">$349 <s>$399</s></p>
        <p class="cst-04__blurb">Adaptive ANC, 40-hour battery, and a tab bar below that docks under the store header while you read — two stickies, one <code>top</code> handshake.</p>
        <a class="cst-04__buy" href="#cst04-cart">Add to cart</a>
      </div>
    </section>
    <div class="cst-04__tabs">
      <nav aria-label="Product sections">
        <a href="#cst04-overview">Overview</a>
        <a href="#cst04-specs">Specs</a>
        <a href="#cst04-reviews">Reviews</a>
        <a href="#cst04-faq">FAQ</a>
      </nav>
    </div>
    <section class="cst-04__sec" id="cst04-overview">
      <h2>Overview</h2>
      <p>The M1 rebuilds our reference driver in beryllium and wraps it in memory foam that actually remembers. Adaptive ANC samples the room 48,000 times a second; transparency mode is one cup-tap away.</p>
      <ul class="cst-04__feats">
        <li><strong>40 hr</strong><span>battery, ANC on</span></li>
        <li><strong>12 min</strong><span>charge = 8 hours</span></li>
        <li><strong>248 g</strong><span>on the scale</span></li>
        <li><strong>3 pts</strong><span>multi-device pairing</span></li>
      </ul>
      <p>Every section on this page declares <code>scroll-margin-top: calc(var(--h1) + var(--h2) + 14px)</code>, so tapping a tab lands the heading just below the docked bars — never underneath them.</p>
    </section>
    <section class="cst-04__sec cst-04__sec--tint" id="cst04-specs">
      <h2>Specs</h2>
      <dl class="cst-04__specs">
        <div><dt>Driver</dt><dd>42mm beryllium dynamic</dd></div>
        <div><dt>ANC</dt><dd>Adaptive hybrid, 4 mics per cup</dd></div>
        <div><dt>Battery</dt><dd>40h ANC on · 60h off · USB-C</dd></div>
        <div><dt>Codecs</dt><dd>LDAC, aptX Lossless, AAC, SBC</dd></div>
        <div><dt>Bluetooth</dt><dd>5.4, multipoint ×3</dd></div>
        <div><dt>Weight</dt><dd>248 g with pads</dd></div>
      </dl>
    </section>
    <section class="cst-04__sec" id="cst04-reviews">
      <h2>Reviews</h2>
      <div class="cst-04__revs">
        <article><p class="cst-04__stars" aria-label="5 stars">★★★★★</p><p>“Returned my old pair the same week. The ANC doesn't hiss, it just deletes the plane.”</p><footer>Sophie R. · Toronto · Verified</footer></article>
        <article><p class="cst-04__stars" aria-label="5 stars">★★★★★</p><p>“Tab bar on this product page is smoother than the app it ships with. 10/10 would scroll again.”</p><footer>Marcus L. · Leeds · Verified</footer></article>
        <article><p class="cst-04__stars" aria-label="4 stars">★★★★☆</p><p>“Clamps a touch firm the first week. Sound is worth every day of it.”</p><footer>Priya D. · Melbourne · Verified</footer></article>
      </div>
    </section>
    <section class="cst-04__sec cst-04__sec--tint" id="cst04-faq">
      <h2>FAQ</h2>
      <details><summary>Do they work wired?</summary><p>Yes — USB-C lossless and a 3.5mm jack, ANC available on both, battery-free passive mode included.</p></details>
      <details><summary>What's in the box?</summary><p>M1, hard case, USB-C cable, 3.5mm cable, flight adapter, and spare pads in the first-run batch.</p></details>
      <details><summary>Returns?</summary><p>60 days, no questions, prepaid label — even if you just don't vibe with them.</p></details>
    </section>
    <footer class="cst-04__footer" id="cst04-cart"><p><strong>Meridian Audio</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst04-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-04,
.cst-04 *,
.cst-04 *::before,
.cst-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-04 {
  --h1: 56px;
  --h2: 48px;
  --bg: oklch(0.98 0.003 270);
  --ink: oklch(0.22 0.015 270);
  --mut: oklch(0.52 0.012 270);
  --line: oklch(0.9 0.006 270);
  --acc: oklch(0.55 0.19 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-04__stage {
  width: 100%;
  container: cst04/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.cst-04__header {
  position: sticky;
  top: 0;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,28px);
  height: var(--h1);
  padding: 0 clamp(18px,4cqi,40px);
  background: color-mix(in oklch,var(--bg) 85%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}

.cst-04__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.cst-04__brand i {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: conic-gradient(from 200deg,var(--acc),oklch(0.7 0.12 220),var(--acc));
}

.cst-04__header nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-04__header nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-04__header nav a:hover,
.cst-04__header nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.008 270);
}

.cst-04__header nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-04__cart {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid var(--line);
  transition: border-color .2s,color .2s;
}

.cst-04__cart:hover,
.cst-04__cart:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.cst-04__cart:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-04__intro {
  display: grid;
  grid-template-columns: minmax(0,5fr) minmax(0,4fr);
  gap: clamp(20px,4cqi,44px);
  align-items: center;
  padding: clamp(20px,4cqi,44px) clamp(18px,4cqi,40px);
}

.cst-04__intro figure {
  aspect-ratio: 4/3.4;
  border-radius: 20px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.85 0.03 290),oklch(0.65 0.08 290));
  background-size: cover;
  background-position: center;
}

.cst-04__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 10px;
}

.cst-04__intro h1 {
  font-size: clamp(28px,4.6cqi,46px);
  letter-spacing: -.03em;
  font-weight: 800;
  line-height: 1.04;
}

.cst-04__rating {
  margin-top: 10px;
  font-size: 13px;
  color: var(--mut);
}

.cst-04__rating span {
  color: oklch(0.75 0.15 85);
  letter-spacing: 2px;
}

.cst-04__price {
  margin-top: 12px;
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cst-04__price s {
  font-size: 16px;
  font-weight: 600;
  color: var(--mut);
  margin-left: 8px;
}

.cst-04__blurb {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 44ch;
}

.cst-04__blurb code,
.cst-04__sec code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.92 0.01 280);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-04__buy {
  display: inline-grid;
  place-items: center;
  min-height: 48px;
  margin-top: 18px;
  padding: 0 26px;
  border-radius: 13px;
  font-size: 14.5px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--ink);
  transition: background .2s,translate .2s;
}

.cst-04__buy:hover,
.cst-04__buy:focus-visible {
  background: var(--acc);
  translate: 0 -2px;
}

.cst-04__buy:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-04__tabs {
  position: sticky;
  top: var(--h1);
  z-index: 5;
  background: color-mix(in oklch,var(--bg) 90%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-block: 1px solid var(--line);
}

.cst-04__tabs nav {
  display: flex;
  gap: 4px;
  height: var(--h2);
  padding: 0 clamp(14px,3.5cqi,36px);
  overflow-x: auto;
  scrollbar-width: none;
}

.cst-04__tabs nav::-webkit-scrollbar {
  display: none;
}

.cst-04__tabs a {
  display: grid;
  place-items: center;
  padding: 0 15px;
  font-size: 13.5px;
  font-weight: 650;
  color: var(--mut);
  text-decoration: none;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: color .2s,border-color .2s;
}

.cst-04__tabs a:hover,
.cst-04__tabs a:focus-visible {
  color: var(--ink);
}

.cst-04__tabs a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -3px;
}

.cst-04__stage:not(:has(:target)) .cst-04__tabs a[href="#cst04-overview"],
.cst-04__stage:has(#cst04-overview:target) .cst-04__tabs a[href="#cst04-overview"],
.cst-04__stage:has(#cst04-specs:target) .cst-04__tabs a[href="#cst04-specs"],
.cst-04__stage:has(#cst04-reviews:target) .cst-04__tabs a[href="#cst04-reviews"],
.cst-04__stage:has(#cst04-faq:target) .cst-04__tabs a[href="#cst04-faq"] {
  color: var(--ink);
  border-bottom-color: var(--acc);
}

.cst-04__sec {
  padding: clamp(34px,6cqi,60px) clamp(18px,4cqi,40px);
  scroll-margin-top: calc(var(--h1) + var(--h2) + 14px);
}

.cst-04__sec--tint {
  background: oklch(0.955 0.006 275);
}

.cst-04__sec h2 {
  font-size: clamp(21px,3.4cqi,30px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-bottom: 16px;
}

.cst-04__sec>p {
  max-width: 66ch;
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--mut);
}

.cst-04__sec>p+p {
  margin-top: 14px;
}

.cst-04__feats {
  list-style: none;
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  margin: 22px 0;
}

.cst-04__feats li {
  display: grid;
  gap: 2px;
  padding: 16px;
  border-radius: 14px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-04__feats strong {
  font-size: 22px;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.cst-04__feats span {
  font-size: 12px;
  color: var(--mut);
}

.cst-04__specs {
  display: grid;
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  max-width: 640px;
}

.cst-04__specs div {
  display: grid;
  grid-template-columns: 130px 1fr;
  gap: 14px;
  padding: 13px 16px;
  background: oklch(1 0 0);
  font-size: 13.5px;
}

.cst-04__specs dt {
  font-weight: 700;
  color: var(--mut);
}

.cst-04__revs {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(230px,100%),1fr));
}

.cst-04__revs article {
  display: grid;
  gap: 10px;
  align-content: start;
  padding: 20px;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-04__stars {
  color: oklch(0.75 0.15 85);
  letter-spacing: 2px;
  font-size: 14px;
}

.cst-04__revs p {
  font-size: 13.5px;
  line-height: 1.6;
}

.cst-04__revs footer {
  font-size: 11.5px;
  color: var(--mut);
}

.cst-04__sec details {
  max-width: 640px;
  border-bottom: 1px solid var(--line);
}

.cst-04__sec summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 52px;
  padding: 14px 2px;
  font-size: 14.5px;
  font-weight: 650;
  cursor: pointer;
  list-style: none;
}

.cst-04__sec summary::-webkit-details-marker {
  display: none;
}

.cst-04__sec summary::after {
  content: "+";
  font-size: 20px;
  font-weight: 400;
  color: var(--mut);
  transition: rotate .25s;
}

.cst-04__sec details[open] summary::after {
  rotate: 45deg;
}

.cst-04__sec summary:hover {
  color: var(--acc);
}

.cst-04__sec summary:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 6px;
}

.cst-04__sec details p {
  padding: 0 2px 16px;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 60ch;
}

.cst-04__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 28px clamp(18px,4cqi,40px) 38px;
  border-top: 1px solid var(--line);
}

.cst-04__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-04__footer a {
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

.cst-04__footer a:hover,
.cst-04__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-04__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst04 (width < 640px) {
  .cst-04__header nav {
    display: none;
  }

  .cst-04__intro {
    grid-template-columns: 1fr;
  }

  .cst-04__intro figure {
    aspect-ratio: 16/10;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-04__stage {
    scroll-behavior: auto;
  }

  .cst-04 * {
    transition-duration: .01ms !important;
  }
}
```
