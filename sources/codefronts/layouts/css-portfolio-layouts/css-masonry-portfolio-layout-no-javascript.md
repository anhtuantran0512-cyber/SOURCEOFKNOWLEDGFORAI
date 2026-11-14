---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/css-masonry-portfolio-layout-no-javascript/"
title: "CSS Masonry Portfolio Layout No JavaScript"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "A Pinterest-style wall of mixed-height pieces with zero JavaScript and zero libraries: CSS multi-columns do the packing, break-inside:avoid keeps every card…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Portfolio Layout No JavaScript
Source: https://codefronts.com/layouts/css-portfolio-layouts/css-masonry-portfolio-layout-no-javascript/

A Pinterest-style wall of mixed-height pieces with zero JavaScript and zero libraries: CSS multi-columns do the packing, break-inside:avoid keeps every card whole, and captions slide up over the art on hover or keyboard focus. Column count is fluid — columns: 3 220px means 'up to three, never narrower than 220px' — so the wall re-packs itself for any container it lands in.
## HTML
```html
<section class="cpl-03" aria-label="CSS masonry portfolio layout demo">
  <div class="cpl-03__stage">
    <header class="cpl-03__head">
      <h2>Field Notes</h2>
      <p>35mm &amp; medium format — no JavaScript, no libraries</p>
    </header>
    <div class="cpl-03__wall">
      <a class="cpl-03__piece" href="#p1" style="--img:url('https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=900&auto=format&fit=crop');--r:3/4;--a:oklch(0.8 0.08 250);--b:oklch(0.45 0.1 270)"><figure></figure><figcaption>Fog over Hayes<span>SF · 2026</span></figcaption></a>
      <a class="cpl-03__piece" href="#p2" style="--img:url('https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=900&auto=format&fit=crop');--r:1/1;--a:oklch(0.85 0.09 90);--b:oklch(0.6 0.13 60)"><figure></figure><figcaption>Amber hour<span>Lisbon · 2025</span></figcaption></a>
      <a class="cpl-03__piece" href="#p3" style="--img:url('https://images.unsplash.com/photo-1505118380757-91f5f5632de0?q=80&w=900&auto=format&fit=crop');--r:4/5;--a:oklch(0.78 0.1 160);--b:oklch(0.5 0.11 190)"><figure></figure><figcaption>Sea wall study<span>Cornwall · 2025</span></figcaption></a>
      <a class="cpl-03__piece" href="#p4" style="--img:url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=900&auto=format&fit=crop');--r:3/2;--a:oklch(0.82 0.07 320);--b:oklch(0.55 0.13 340)"><figure></figure><figcaption>Neon district<span>Osaka · 2024</span></figcaption></a>
      <a class="cpl-03__piece" href="#p5" style="--img:url('https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=900&auto=format&fit=crop');--r:1/1;--a:oklch(0.86 0.05 200);--b:oklch(0.62 0.09 230)"><figure></figure><figcaption>Still harbour<span>Oslo · 2026</span></figcaption></a>
      <a class="cpl-03__piece" href="#p6" style="--img:url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=900&auto=format&fit=crop');--r:3/4;--a:oklch(0.8 0.1 40);--b:oklch(0.52 0.15 25)"><figure></figure><figcaption>Red canyon<span>Utah · 2024</span></figcaption></a>
      <a class="cpl-03__piece" href="#p7" style="--img:url('https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=900&auto=format&fit=crop');--r:4/3;--a:oklch(0.84 0.06 130);--b:oklch(0.55 0.1 150)"><figure></figure><figcaption>Terrace lines<span>Bali · 2025</span></figcaption></a>
      <a class="cpl-03__piece" href="#p8" style="--img:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=900&auto=format&fit=crop');--r:1/1;--a:oklch(0.77 0.09 280);--b:oklch(0.48 0.14 300)"><figure></figure><figcaption>Blue passage<span>Chefchaouen · 2026</span></figcaption></a>
      <a class="cpl-03__piece" href="#p9" style="--img:url('https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=900&auto=format&fit=crop');--r:3/4;--a:oklch(0.88 0.04 80);--b:oklch(0.65 0.08 100)"><figure></figure><figcaption>Wheat, late June<span>Alberta · 2025</span></figcaption></a>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-03,
.cpl-03 *,
.cpl-03 *::before,
.cpl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-03 {
  --bg: oklch(0.22 0.015 270);
  --ink: oklch(0.95 0.005 90);
  --mut: oklch(0.68 0.015 270);
  --line: oklch(0.32 0.02 270);
  --acc: oklch(0.8 0.14 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-03__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(18px,4cqi,30px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-03__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 14px;
  margin-bottom: 20px;
}

.cpl-03__head h2 {
  font-size: 24px;
  letter-spacing: -.02em;
}

.cpl-03__head p {
  font-size: 12.5px;
  color: var(--mut);
}

.cpl-03__wall {
  columns: 3 220px;
  column-gap: 14px;
}

.cpl-03__piece {
  position: relative;
  display: block;
  break-inside: avoid;
  margin-bottom: 14px;
  border-radius: 14px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
}

.cpl-03__piece figure {
  aspect-ratio: var(--r);
  background-image: var(--img,none),linear-gradient(145deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .55s cubic-bezier(.2,.7,.2,1);
}

.cpl-03__piece:hover figure,
.cpl-03__piece:focus-visible figure {
  scale: 1.05;
}

.cpl-03__piece figcaption {
  position: absolute;
  inset: auto 0 0 0;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  padding: 26px 14px 12px;
  font-size: 13.5px;
  font-weight: 600;
  background: linear-gradient(to top,oklch(0.15 0.02 270/.85),transparent);
  opacity: 0;
  translate: 0 10px;
  transition: opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

.cpl-03__piece figcaption span {
  font-size: 11px;
  font-weight: 400;
  color: oklch(0.82 0.02 90);
}

.cpl-03__piece:hover figcaption,
.cpl-03__piece:focus-visible figcaption {
  opacity: 1;
  translate: 0 0;
}

.cpl-03__piece:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@supports (grid-template-rows: masonry) {
  .cpl-03__wall {
    display: grid;
    columns: auto;
    grid-template-columns: repeat(auto-fill,minmax(min(220px,100%),1fr));
    grid-template-rows: masonry;
    gap: 14px;
  }

  .cpl-03__piece {
    margin-bottom: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-03 figure,
    .cpl-03 figcaption {
    transition-duration: .01ms !important;
  }
}
```
