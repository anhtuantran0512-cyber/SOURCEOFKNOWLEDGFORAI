---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/css-grid-portfolio-layout-example-html-css/"
title: "CSS Grid Portfolio Layout Example HTML CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The canonical portfolio grid, done the 2026 way: one line of repeat(auto-fill, minmax()) generates every breakpoint for free, a featured project spans a 2×2…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Portfolio Layout Example HTML CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/css-grid-portfolio-layout-example-html-css/

The canonical portfolio grid, done the 2026 way: one line of repeat(auto-fill, minmax()) generates every breakpoint for free, a featured project spans a 2×2 block, and a container query — not a media query — collapses the feature when the grid gets pasted somewhere narrow. Cards lift on hover with a compositor-only translate, covers zoom inside an overflow clip, and the whole thing is 100% CSS.
## HTML
```html
<section class="cpl-01" aria-label="CSS Grid portfolio layout demo">
  <div class="cpl-01__stage">
    <header class="cpl-01__head">
      <div>
        <h2>Selected Work</h2>
        <p>Product, brand &amp; motion — 2024 to 2026</p>
      </div>
      <nav class="cpl-01__filters" aria-label="Filter projects">
        <a href="#all" aria-current="true">All</a>
        <a href="#web">Web</a>
        <a href="#brand">Brand</a>
        <a href="#motion">Motion</a>
      </nav>
    </header>
    <div class="cpl-01__grid">
      <a class="cpl-01__card cpl-01__card--feat" href="#aurora">
        <figure style="--img:url('https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.12 300);--b:oklch(0.5 0.19 265)"><span>Featured</span></figure>
        <div class="cpl-01__meta"><h3>Aurora Design System</h3><p>Web · 2026</p></div>
      </a>
      <a class="cpl-01__card" href="#nomad">
        <figure style="--img:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.85 0.09 80);--b:oklch(0.62 0.15 45)"></figure>
        <div class="cpl-01__meta"><h3>Nomad Banking</h3><p>Product · 2025</p></div>
      </a>
      <a class="cpl-01__card" href="#meridian">
        <figure style="--img:url('https://images.unsplash.com/photo-1487958449943-2429e8be8625?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.1 160);--b:oklch(0.5 0.13 200)"></figure>
        <div class="cpl-01__meta"><h3>Meridian Rebrand</h3><p>Brand · 2025</p></div>
      </a>
      <a class="cpl-01__card" href="#pulse">
        <figure style="--img:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.1 20);--b:oklch(0.55 0.19 350)"></figure>
        <div class="cpl-01__meta"><h3>Pulse Data Viz</h3><p>Web · 2024</p></div>
      </a>
      <a class="cpl-01__card" href="#kinfolk">
        <figure style="--img:url('https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=900&auto=format&fit=crop');--a:oklch(0.86 0.06 250);--b:oklch(0.6 0.12 280)"></figure>
        <div class="cpl-01__meta"><h3>Kinfolk Commerce</h3><p>Web · 2025</p></div>
      </a>
      <a class="cpl-01__card" href="#drift">
        <figure style="--img:url('https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.83 0.11 120);--b:oklch(0.55 0.14 150)"></figure>
        <div class="cpl-01__meta"><h3>Drift Motion Reel</h3><p>Motion · 2026</p></div>
      </a>
      <a class="cpl-01__card" href="#solstice">
        <figure style="--img:url('https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=900&auto=format&fit=crop');--a:oklch(0.85 0.05 270);--b:oklch(0.6 0.1 290)"></figure>
        <div class="cpl-01__meta"><h3>Solstice Studio</h3><p>Web · 2024</p></div>
      </a>
      <a class="cpl-01__card" href="#halcyondocs">
        <figure style="--img:url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.08 200);--b:oklch(0.55 0.11 230)"></figure>
        <div class="cpl-01__meta"><h3>Halcyon Docs</h3><p>Product · 2024</p></div>
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-01,
.cpl-01 *,
.cpl-01 *::before,
.cpl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-01 {
  --bg: oklch(0.98 0.004 260);
  --ink: oklch(0.22 0.02 260);
  --mut: oklch(0.55 0.015 260);
  --line: oklch(0.9 0.008 260);
  --acc: oklch(0.58 0.2 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-01__stage {
  width: 100%;
  container: cpl01/inline-size;
  background: var(--bg);
  padding: clamp(18px,4cqi,30px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-01__head {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 22px;
}

.cpl-01__head h2 {
  font-size: 26px;
  letter-spacing: -.02em;
}

.cpl-01__head p {
  font-size: 13px;
  color: var(--mut);
  margin-top: 4px;
}

.cpl-01__filters {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.cpl-01__filters a {
  display: inline-grid;
  place-items: center;
  min-height: 36px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  border: 1px solid var(--line);
  transition: color .2s,border-color .2s,background .2s;
}

.cpl-01__filters a[aria-current],
.cpl-01__filters a:hover,
.cpl-01__filters a:focus-visible {
  color: oklch(0.99 0 0);
  background: var(--ink);
  border-color: var(--ink);
}

.cpl-01__filters a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cpl-01__grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fill,minmax(min(200px,100%),1fr));
}

.cpl-01__card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  overflow: hidden;
  transition: translate .3s cubic-bezier(.2,.7,.2,1),box-shadow .3s,border-color .3s;
}

.cpl-01__card:hover,
.cpl-01__card:focus-visible {
  translate: 0 -4px;
  box-shadow: 0 18px 36px -20px oklch(0.35 0.05 265/.5);
  border-color: oklch(0.82 0.02 265);
}

.cpl-01__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-01__card figure {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
}

.cpl-01__card figure::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none),linear-gradient(135deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .6s cubic-bezier(.2,.7,.2,1);
}

.cpl-01__card:hover figure::before,
.cpl-01__card:focus-visible figure::before {
  scale: 1.07;
}

.cpl-01__card figure span {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 5px 11px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  background: oklch(1 0 0/.85);
  backdrop-filter: blur(6px);
}

.cpl-01__meta {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  padding: 14px 16px;
}

.cpl-01__meta h3 {
  font-size: 15px;
  letter-spacing: -.01em;
}

.cpl-01__meta p {
  font-size: 12px;
  color: var(--mut);
  white-space: nowrap;
}

.cpl-01__card--feat {
  grid-column: span 2;
  grid-row: span 2;
}

.cpl-01__card--feat figure {
  aspect-ratio: auto;
  flex: 1;
  min-height: 200px;
}

.cpl-01__card--feat h3 {
  font-size: 19px;
}

@container cpl01 (width < 460px) {
  .cpl-01__card--feat {
    grid-column: span 1;
    grid-row: span 1;
  }

  .cpl-01__card--feat figure {
    aspect-ratio: 4/3;
    flex: none;
    min-height: 0;
  }

  .cpl-01__card--feat h3 {
    font-size: 15px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-01 *,
    .cpl-01 *::before {
    transition-duration: .01ms !important;
  }
}
```
