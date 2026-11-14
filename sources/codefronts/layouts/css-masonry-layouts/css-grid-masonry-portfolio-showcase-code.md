---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-grid-masonry-portfolio-showcase-code/"
title: "CSS Grid Masonry Portfolio Showcase Code"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "An agency-grade work wall where masonry is art direction, not chance: a 2×2 hero, wide and tall tiles at deliberate beats, and grid-auto-flow: dense knitting…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Masonry Portfolio Showcase Code
Source: https://codefronts.com/layouts/css-masonry-layouts/css-grid-masonry-portfolio-showcase-code/

An agency-grade work wall where masonry is art direction, not chance: a 2×2 hero, wide and tall tiles at deliberate beats, and grid-auto-flow: dense knitting the field tight around them. Hovering any project dims and desaturates the rest of the wall via one :has() rule — the spotlight effect agencies pay for — and every overlay fires identically for keyboard focus. Dark, cinematic, zero scripts.
## HTML
```html
<section class="msn-07" aria-label="CSS grid masonry portfolio showcase demo">
  <div class="msn-07__stage" tabindex="0">
    <header class="msn-07__head">
      <div><h2>Studio Norr — Selected Work</h2><p>Brand, product & film · 2024–2026</p></div>
      <a class="msn-07__cta" href="#contact">Start a project</a>
    </header>
    <div class="msn-07__wall">
      <a class="msn-07__tile msn-07__tile--hero" href="#w1" style="--img:url('https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=1200&auto=format&fit=crop');--a:oklch(0.7 0.12 300);--b:oklch(0.42 0.15 330)"><div class="msn-07__ov"><span class="msn-07__ix">01</span><h3>Meridian Identity</h3><p><span>Brand</span><span>Type design</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile" href="#w2" style="--img:url('https://images.unsplash.com/photo-1557682250-33bd709cbe85?q=80&w=800&auto=format&fit=crop');--a:oklch(0.65 0.14 280);--b:oklch(0.4 0.13 260)"><div class="msn-07__ov"><span class="msn-07__ix">02</span><h3>Gradient OS</h3><p><span>Product</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile msn-07__tile--tall" href="#w3" style="--img:url('https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800&auto=format&fit=crop');--a:oklch(0.6 0.12 40);--b:oklch(0.35 0.1 20)"><div class="msn-07__ov"><span class="msn-07__ix">03</span><h3>Arcade Rewind</h3><p><span>Campaign</span><span>Film</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile" href="#w4" style="--img:url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=800&auto=format&fit=crop');--a:oklch(0.72 0.1 220);--b:oklch(0.45 0.12 250)"><div class="msn-07__ov"><span class="msn-07__ix">04</span><h3>Liquid Type Reel</h3><p><span>Motion</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile msn-07__tile--wide" href="#w5" style="--img:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.55 0.1 260);--b:oklch(0.32 0.09 280)"><div class="msn-07__ov"><span class="msn-07__ix">05</span><h3>Ledger Analytics</h3><p><span>Product</span><span>Data viz</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile" href="#w6" style="--img:url('https://images.unsplash.com/photo-1541701494587-cb58502866ab?q=80&w=800&auto=format&fit=crop');--a:oklch(0.68 0.13 350);--b:oklch(0.42 0.13 320)"><div class="msn-07__ov"><span class="msn-07__ix">06</span><h3>Bloom Records</h3><p><span>Brand</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile" href="#w7" style="--img:url('https://images.unsplash.com/photo-1579546929518-9e396f3cc809?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.11 180);--b:oklch(0.45 0.1 160)"><div class="msn-07__ov"><span class="msn-07__ix">07</span><h3>Tidal Streams</h3><p><span>Web</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile msn-07__tile--tall" href="#w8" style="--img:url('https://images.unsplash.com/photo-1550859492-d5da9d8e45f3?q=80&w=800&auto=format&fit=crop');--a:oklch(0.6 0.14 300);--b:oklch(0.35 0.12 280)"><div class="msn-07__ov"><span class="msn-07__ix">08</span><h3>Nightshift Fashion</h3><p><span>E-comm</span><span>Art dir.</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
      <a class="msn-07__tile" href="#w9" style="--img:url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=800&auto=format&fit=crop');--a:oklch(0.55 0.08 240);--b:oklch(0.32 0.08 260)"><div class="msn-07__ov"><span class="msn-07__ix">09</span><h3>Compiler Conf</h3><p><span>Event</span></p></div><span class="msn-07__go" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-07,
.msn-07 *,
.msn-07 *::before,
.msn-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-07 {
  --bg: oklch(0.17 0.012 285);
  --ink: oklch(0.95 0.008 285);
  --mut: oklch(0.66 0.015 285);
  --line: oklch(0.29 0.015 285);
  --acc: oklch(0.78 0.14 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-07__stage {
  width: 100%;
  container: msn07/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-07__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 18px clamp(16px,3cqi,30px);
  background: color-mix(in oklch,var(--bg) 80%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-07__head h2 {
  font-size: clamp(17px,2.5cqi,23px);
  letter-spacing: -.02em;
}

.msn-07__head p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-07__cta {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 17px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.15 0.02 85);
  background: var(--acc);
  transition: background .2s,translate .2s;
}

.msn-07__cta:hover,
.msn-07__cta:focus-visible {
  background: oklch(0.85 0.13 85);
  translate: 0 -1px;
}

.msn-07__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.msn-07__wall {
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(auto-fill,minmax(min(220px,100%),1fr));
  grid-auto-rows: 190px;
  grid-auto-flow: row dense;
  padding: clamp(16px,3cqi,30px);
}

.msn-07__tile {
  position: relative;
  display: block;
  border-radius: 14px;
  overflow: clip;
  text-decoration: none;
  color: var(--ink);
  background: linear-gradient(150deg,var(--a),var(--b));
  transition: opacity .35s,filter .35s,translate .3s;
}

.msn-07__tile::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none);
  background-size: cover;
  background-position: center;
  transition: scale .5s cubic-bezier(.2,.7,.2,1);
}

.msn-07__tile::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(185deg,transparent 42%,oklch(0.13 0.015 285/.82));
}

.msn-07__tile:hover::before,
.msn-07__tile:focus-visible::before {
  scale: 1.05;
}

.msn-07__tile:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.msn-07__tile--hero {
  grid-area: span 2/span 2;
}

.msn-07__tile--wide {
  grid-column: span 2;
}

.msn-07__tile--tall {
  grid-row: span 2;
}

.msn-07__wall:has(.msn-07__tile:hover) .msn-07__tile:not(:hover),
.msn-07__wall:has(.msn-07__tile:focus-visible) .msn-07__tile:not(:focus-visible) {
  opacity: .45;
  filter: saturate(.55);
}

.msn-07__ov {
  position: absolute;
  left: 16px;
  right: 52px;
  bottom: 14px;
  z-index: 1;
  display: grid;
  gap: 5px;
}

.msn-07__ix {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  color: var(--acc);
}

.msn-07__ov h3 {
  font-size: clamp(15px,1.8cqi,19px);
  letter-spacing: -.015em;
  text-wrap: balance;
}

.msn-07__tile--hero .msn-07__ov h3 {
  font-size: clamp(19px,2.6cqi,27px);
}

.msn-07__ov p {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.msn-07__ov p span {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .04em;
  padding: 4px 9px;
  border-radius: 99px;
  border: 1px solid oklch(0.95 0.008 285/.28);
  color: oklch(0.9 0.01 285);
  backdrop-filter: blur(3px);
}

.msn-07__go {
  position: absolute;
  right: 14px;
  bottom: 14px;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: oklch(0.95 0.008 285/.14);
  backdrop-filter: blur(4px);
  font-size: 15px;
  translate: 0 6px;
  opacity: 0;
  transition: translate .3s,opacity .3s;
}

.msn-07__tile:hover .msn-07__go,
.msn-07__tile:focus-visible .msn-07__go {
  translate: 0 0;
  opacity: 1;
}

@media (hover: none) {
  .msn-07__go {
    opacity: 1;
    translate: 0 0;
  }
}

@container msn07 (width < 520px) {
  .msn-07__wall {
    grid-template-columns: repeat(2,1fr);
    grid-auto-rows: 150px;
    gap: 8px;
  }

  .msn-07__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-07 *,
    .msn-07 *::before {
    transition-duration: .01ms !important;
  }
}
```
