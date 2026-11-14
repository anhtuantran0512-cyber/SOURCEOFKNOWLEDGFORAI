---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/apple-style-product-feature-showcase/"
title: "Apple-Style Product Feature Showcase"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "The keynote-style responsive CSS bento grid layout everyone searches for after an Apple launch: a large hero cell for the product story, flanked by smaller…"
has_js: "false"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Apple-Style Product Feature Showcase
Source: https://codefronts.com/layouts/css-bento-grid-layouts/apple-style-product-feature-showcase/

The keynote-style responsive CSS bento grid layout everyone searches for after an Apple launch: a large hero cell for the product story, flanked by smaller 1×1 stat cards with oversized numerals and micro-copy. Built with grid-template-areas-free spans on a 12-column CSS Grid, a conic-gradient border sweep on hover, and container queries so it collapses to a clean single-column stack on mobile.
## HTML
```html
<div class="bgl-01-group">
<section class="bgl-01a" aria-labelledby="bgl-01a-h">
  <div class="bgl-01a__grid">
    <article class="bgl-01a__card bgl-01a__hero">
      <p class="bgl-01a__kicker">Introducing</p>
      <h2 class="bgl-01a__title" id="bgl-01a-h">Titan&nbsp;X</h2>
      <p class="bgl-01a__sub">The thinnest chassis we have ever machined, forged from a single block of aerospace-grade titanium.</p>
      <a class="bgl-01a__cta" href="#">Watch the film</a>
    </article>
    <article class="bgl-01a__card"><p class="bgl-01a__stat">A19</p><p class="bgl-01a__cap">Neural engine. 2&times; faster on-device AI.</p></article>
    <article class="bgl-01a__card"><p class="bgl-01a__stat">29h</p><p class="bgl-01a__cap">Video playback on a single charge.</p></article>
    <article class="bgl-01a__card"><p class="bgl-01a__stat">48MP</p><p class="bgl-01a__cap">Fusion camera with 5&times; optical zoom.</p></article>
    <article class="bgl-01a__card"><p class="bgl-01a__stat">120Hz</p><p class="bgl-01a__cap">ProMotion display, 1&ndash;120 adaptive.</p></article>
    <article class="bgl-01a__card"><p class="bgl-01a__stat">Ti</p><p class="bgl-01a__cap">Grade-5 titanium. 19&nbsp;g lighter.</p></article>
  </div>
</section>
<section class="bgl-01b" aria-labelledby="bgl-01b-h">
  <div class="bgl-01b__grid">
    <article class="bgl-01b__card bgl-01b__img">
      <img src="https://picsum.photos/seed/bglspec/900/620" alt="Titan X product photography on a studio background" loading="lazy">
      <div class="bgl-01b__imgcap"><h2 id="bgl-01b-h">Titan&nbsp;X &mdash; every spec, one glance</h2></div>
    </article>
    <article class="bgl-01b__card"><p class="bgl-01b__num">5.9<small>mm</small></p><p class="bgl-01b__cap">Thinnest profile in its class</p></article>
    <article class="bgl-01b__card"><p class="bgl-01b__num">187<small>g</small></p><p class="bgl-01b__cap">Featherweight titanium frame</p></article>
    <article class="bgl-01b__card"><p class="bgl-01b__num">3&times;</p><p class="bgl-01b__cap">GPU performance vs. last gen</p></article>
    <article class="bgl-01b__card"><p class="bgl-01b__num">IP69</p><p class="bgl-01b__cap">Rated for dust and high-pressure water</p></article>
    <article class="bgl-01b__card bgl-01b__wide"><p class="bgl-01b__cap"><strong>Carbon neutral.</strong> 100% recycled aluminium sub-frame, 50% recycled rare-earth magnets, zero plastic packaging.</p></article>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-01-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-01-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-01a,
.bgl-01a *,
.bgl-01a *::before,
.bgl-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --bgl01a-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.bgl-01a {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.72 0.14 265);
  --gap: 16px;
  --radius: 24px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #0a0a0f;
  color: #f5f5f7;
}

.bgl-01a__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(150px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-01a__card {
  position: relative;
  isolation: isolate;
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 8px;
  padding: 28px;
  border-radius: var(--radius);
  background: radial-gradient(140% 140% at 20% 0%,#1c1c26,#101016);
  border: 1px solid rgba(255,255,255,.08);
  transition: transform .35s cubic-bezier(.2,.9,.2,1);
}

.bgl-01a__card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: conic-gradient(from var(--bgl01a-a),transparent,var(--accent),transparent 32%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity .4s;
  z-index: -1;
}

.bgl-01a__card:hover {
  transform: translateY(-4px);
}

.bgl-01a__card:hover::before {
  opacity: 1;
  animation: bgl-01a-spin 2.6s linear infinite;
}

.bgl-01a__hero {
  grid-column: span 8;
  grid-row: span 2;
  justify-content: flex-end;
  gap: 12px;
  padding: 40px;
  background: radial-gradient(90% 110% at 75% 10%,color-mix(in oklab,var(--accent) 32%,transparent),transparent 60%),radial-gradient(140% 140% at 20% 0%,#1a1a26,#0e0e14);
}

.bgl-01a__kicker {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--accent) 80%,white);
}

.bgl-01a__title {
  font-size: clamp(44px,7cqw,76px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
}

.bgl-01a__sub {
  max-width: 42ch;
  font-size: 16px;
  line-height: 1.55;
  color: rgba(245,245,247,.65);
  text-wrap: pretty;
}

.bgl-01a__cta {
  align-self: flex-start;
  margin-top: 8px;
  font-size: 15px;
  font-weight: 700;
  color: #0a0a0f;
  text-decoration: none;
  padding: 12px 26px;
  border-radius: 9999px;
  background: #f5f5f7;
  transition: transform .25s,background .25s;
}

.bgl-01a__cta:hover {
  transform: translateY(-2px);
  background: #fff;
}

.bgl-01a__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.bgl-01a__stat {
  font-size: clamp(32px,4cqw,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  background: linear-gradient(180deg,#fff,color-mix(in oklab,var(--accent) 55%,white));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.bgl-01a__cap {
  font-size: 13.5px;
  line-height: 1.5;
  color: rgba(245,245,247,.55);
  text-wrap: pretty;
}

@keyframes bgl-01a-spin {
  to {
    --bgl01a-a: 360deg;
  }
}

@container (max-width: 880px) {
  .bgl-01a__hero {
    grid-column: span 12;
  }

  .bgl-01a__card {
    grid-column: span 6;
  }
}

@container (max-width: 560px) {
  .bgl-01a__card,
    .bgl-01a__hero {
    grid-column: span 12;
  }

  .bgl-01a__grid {
    grid-auto-rows: auto;
  }

  .bgl-01a__hero {
    min-height: 320px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-01a__card,
    .bgl-01a__cta {
    transition: none;
  }

  .bgl-01a__card:hover {
    transform: none;
  }

  .bgl-01a__card:hover::before {
    animation: none;
  }
}

.bgl-01b,
.bgl-01b *,
.bgl-01b *::before,
.bgl-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-01b {
  width: 100%;
  min-height: 100vh;
  --ink: #1d1d1f;
  --accent: oklch(0.6 0.18 262);
  --gap: 16px;
  --radius: 22px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 24px;
  background: #f5f4f0;
  color: var(--ink);
}

.bgl-01b__grid {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: minmax(140px,auto);
  gap: var(--gap);
  max-width: 1080px;
  margin: 0 auto;
}

.bgl-01b__card {
  grid-column: span 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  padding: 26px;
  border-radius: var(--radius);
  background: #fff;
  border: 1px solid rgba(0,0,0,.07);
  transition: transform .3s,box-shadow .3s;
}

.bgl-01b__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 34px -20px rgba(0,0,0,.25);
}

.bgl-01b__img {
  grid-column: span 6;
  grid-row: span 2;
  position: relative;
  overflow: hidden;
  padding: 0;
  justify-content: flex-end;
}

.bgl-01b__img img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s cubic-bezier(.2,.9,.2,1);
}

.bgl-01b__img:hover img {
  transform: scale(1.05);
}

.bgl-01b__imgcap {
  position: relative;
  padding: 26px;
  background: linear-gradient(transparent,rgba(0,0,0,.55));
}

.bgl-01b__imgcap h2 {
  font-size: clamp(20px,2.4cqw,26px);
  font-weight: 700;
  color: #fff;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.bgl-01b__num {
  font-size: clamp(34px,4cqw,46px);
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.bgl-01b__num small {
  font-size: .45em;
  font-weight: 700;
  color: var(--accent);
  margin-left: 2px;
}

.bgl-01b__cap {
  font-size: 14px;
  line-height: 1.55;
  color: rgba(29,29,31,.62);
  text-wrap: pretty;
}

.bgl-01b__wide {
  grid-column: span 6;
}

.bgl-01b__wide .bgl-01b__cap {
  font-size: 15px;
}

.bgl-01b__wide strong {
  color: var(--ink);
}

@container (max-width: 880px) {
  .bgl-01b__img,
    .bgl-01b__wide {
    grid-column: span 12;
  }

  .bgl-01b__card {
    grid-column: span 6;
  }

  .bgl-01b__img {
    grid-column: span 12;
  }
}

@container (max-width: 560px) {
  .bgl-01b__card,
    .bgl-01b__wide,
    .bgl-01b__img {
    grid-column: span 12;
  }

  .bgl-01b__img {
    min-height: 260px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bgl-01b__card,
    .bgl-01b__img img {
    transition: none;
  }

  .bgl-01b__card:hover {
    transform: none;
  }

  .bgl-01b__img:hover img {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 12-column CSS Grid with span recipes; the hover border is a registered @property angle spinning a masked conic-gradient ring. */

/* No JavaScript — a light spec-sheet bento: 6-col hero image with object-fit cover and a hover zoom, plus tabular-nums stat cards on a 12-column grid. */
```
