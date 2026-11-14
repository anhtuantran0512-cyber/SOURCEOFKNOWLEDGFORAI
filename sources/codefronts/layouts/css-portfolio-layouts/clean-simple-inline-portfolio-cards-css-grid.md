---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/clean-simple-inline-portfolio-cards-css-grid/"
title: "Clean Simple Inline Portfolio Cards CSS Grid"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The beginner's demo, engineered on purpose: about 30 lines of CSS, every one of which earns a comment in the tutorial below."
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clean Simple Inline Portfolio Cards CSS Grid
Source: https://codefronts.com/layouts/css-portfolio-layouts/clean-simple-inline-portfolio-cards-css-grid/

The beginner's demo, engineered on purpose: about 30 lines of CSS, every one of which earns a comment in the tutorial below. One grid rule handles all screen sizes, one card recipe (cover, title, tag), one hover. No custom properties beyond five color tokens, no pseudo-element tricks, no queries of any kind — this is the smallest correct version of a portfolio card grid, and the base every other demo in this collection builds on.
## HTML
```html
<section class="cpl-13" aria-label="Simple portfolio cards demo">
  <div class="cpl-13__stage">
    <header class="cpl-13__head">
      <h2>Projects</h2>
      <p>Three cards, thirty lines of CSS</p>
    </header>
    <div class="cpl-13__grid">
      <a class="cpl-13__card" href="#driftwood" style="--img:url('https://images.unsplash.com/photo-1518780664697-55e3ad937233?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.1 230);--b:oklch(0.55 0.13 260)">
        <figure></figure>
        <div><h3>Driftwood Cabins</h3><span>Booking site</span></div>
      </a>
      <a class="cpl-13__card" href="#morningloaf" style="--img:url('https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.09 75);--b:oklch(0.6 0.13 50)">
        <figure></figure>
        <div><h3>Morning Loaf</h3><span>Bakery brand</span></div>
      </a>
      <a class="cpl-13__card" href="#trailmix" style="--img:url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.11 145);--b:oklch(0.52 0.12 170)">
        <figure></figure>
        <div><h3>Trailmix</h3><span>Hiking app</span></div>
      </a>
      <a class="cpl-13__card" href="#cedarsalt" style="--img:url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.08 50);--b:oklch(0.5 0.11 30)">
        <figure></figure>
        <div><h3>Cedar &amp; Salt</h3><span>Restaurant site</span></div>
      </a>
      <a class="cpl-13__card" href="#northlight" style="--img:url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.06 170);--b:oklch(0.56 0.1 195)">
        <figure></figure>
        <div><h3>Northlight Yoga</h3><span>Studio brand</span></div>
      </a>
      <a class="cpl-13__card" href="#paperplane" style="--img:url('https://images.unsplash.com/photo-1456735190827-d1262f71b8a3?q=80&w=900&auto=format&fit=crop');--a:oklch(0.86 0.05 90);--b:oklch(0.62 0.09 70)">
        <figure></figure>
        <div><h3>Paper Plane Co.</h3><span>Stationery shop</span></div>
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
/* tokens — the only custom properties in this demo */

.cpl-13,
.cpl-13 *,
.cpl-13 *::before,
.cpl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-13 {
  --bg: oklch(0.975 0.005 240);
  --card: oklch(1 0 0);
  --ink: oklch(0.24 0.02 250);
  --mut: oklch(0.54 0.015 250);
  --line: oklch(0.89 0.008 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-13__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(18px,4cqi,28px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-13__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 18px;
}

.cpl-13__head h2 {
  font-size: 22px;
  letter-spacing: -.02em;
}

.cpl-13__head p {
  font-size: 12.5px;
  color: var(--mut);
}
/* the one-line responsive grid */

.cpl-13__grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit,minmax(min(210px,100%),1fr));
}
/* the card: link > figure + text. no fixed heights anywhere */

.cpl-13__card {
  display: block;
  border-radius: 14px;
  overflow: hidden;
  background: var(--card);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: translate .25s ease,border-color .25s;
}

.cpl-13__card:hover,
.cpl-13__card:focus-visible {
  translate: 0 -3px;
  border-color: oklch(0.72 0.06 250);
}

.cpl-13__card:focus-visible {
  outline: 2px solid oklch(0.55 0.17 250);
  outline-offset: 3px;
}
/* aspect-ratio reserves the cover's space before any image loads */

.cpl-13__card figure {
  aspect-ratio: 3/2;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.cpl-13__card div {
  padding: 14px 16px;
}

.cpl-13__card h3 {
  font-size: 15px;
  letter-spacing: -.01em;
}

.cpl-13__card span {
  display: block;
  margin-top: 3px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cpl-13__card {
    transition: none;
  }
}
```
