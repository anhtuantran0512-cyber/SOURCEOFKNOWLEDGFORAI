---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/minimalist-graphic-design-portfolio-layout-html-css/"
title: "Minimalist Graphic Design Portfolio Layout HTML CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "Portfolio-as-index: no cards, no grid of thumbnails — just an oversized name, six hairline-ruled rows of work, and a thumbnail that blooms in at the row's…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Graphic Design Portfolio Layout HTML CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/minimalist-graphic-design-portfolio-layout-html-css/

Portfolio-as-index: no cards, no grid of thumbnails — just an oversized name, six hairline-ruled rows of work, and a thumbnail that blooms in at the row's edge only when you hover or focus it. The restraint is the design: two font sizes doing the work of six, one accent used exactly once, and white space measured in multiples of a 8px rhythm. Swiss typography rules, written in CSS.
## HTML
```html
<section class="cpl-11" aria-label="Minimalist graphic design portfolio demo">
  <div class="cpl-11__stage">
    <header class="cpl-11__masthead">
      <h2>Anselm<br>Reyes</h2>
      <p class="cpl-11__role">Graphic design<br>&amp; art direction</p>
      <p class="cpl-11__avail">Available from November<span aria-hidden="true"></span></p>
    </header>
    <nav class="cpl-11__index" aria-label="Selected work">
      <a class="cpl-11__row" href="#terra" style="--img:url('https://images.unsplash.com/photo-1483412033650-1015ddeb83d1?q=80&w=900&auto=format&fit=crop');--a:oklch(0.72 0.11 45);--b:oklch(0.5 0.13 25)">
        <i>01</i><h3>Terra Vinyl</h3><em>Identity, sleeves</em><span>2026</span><figure aria-hidden="true"></figure>
      </a>
      <a class="cpl-11__row" href="#brut" style="--img:url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.65 0.03 270);--b:oklch(0.4 0.05 280)">
        <i>02</i><h3>Brut Journal</h3><em>Editorial system</em><span>2026</span><figure aria-hidden="true"></figure>
      </a>
      <a class="cpl-11__row" href="#kelp" style="--img:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=900&auto=format&fit=crop');--a:oklch(0.7 0.12 165);--b:oklch(0.45 0.11 185)">
        <i>03</i><h3>Kelp Coast</h3><em>Wayfinding</em><span>2025</span><figure aria-hidden="true"></figure>
      </a>
      <a class="cpl-11__row" href="#nocturne" style="--img:url('https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?q=80&w=900&auto=format&fit=crop');--a:oklch(0.55 0.15 300);--b:oklch(0.35 0.12 320)">
        <i>04</i><h3>Nocturne Festival</h3><em>Campaign, print</em><span>2025</span><figure aria-hidden="true"></figure>
      </a>
      <a class="cpl-11__row" href="#stille" style="--img:url('https://images.unsplash.com/photo-1555041469-a586c61ea9bc?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.06 90);--b:oklch(0.6 0.09 70)">
        <i>05</i><h3>Stille Furniture</h3><em>Catalogue</em><span>2024</span><figure aria-hidden="true"></figure>
      </a>
      <a class="cpl-11__row" href="#argos" style="--img:url('https://images.unsplash.com/photo-1516031190212-da133013de50?q=80&w=900&auto=format&fit=crop');--a:oklch(0.68 0.13 250);--b:oklch(0.45 0.13 270)">
        <i>06</i><h3>Argos Type Specimen</h3><em>Typeface launch</em><span>2024</span><figure aria-hidden="true"></figure>
      </a>
    </nav>
    <footer class="cpl-11__foot">
      <a href="#email">[email protected]</a>
      <span>Rotterdam, NL</span>
    </footer>
  </div>
</section>
```
## CSS
```css
.cpl-11,
.cpl-11 *,
.cpl-11 *::before,
.cpl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-11 {
  --u: 8px;
  --bg: oklch(0.985 0.002 90);
  --ink: oklch(0.18 0.005 270);
  --mut: oklch(0.52 0.008 270);
  --line: oklch(0.87 0.004 270);
  --acc: oklch(0.62 0.21 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-11__stage {
  width: 100%;
  background: var(--bg);
  padding: calc(var(--u)*6) calc(var(--u)*5) calc(var(--u)*4);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-11__masthead {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: calc(var(--u)*2) calc(var(--u)*4);
  align-items: end;
  margin-bottom: calc(var(--u)*7);
}

.cpl-11__masthead h2 {
  font-size: clamp(44px,9cqi,76px);
  line-height: .94;
  letter-spacing: -.04em;
  font-weight: 700;
  grid-row: span 2;
}

.cpl-11__role {
  font-size: 13px;
  line-height: 1.5;
  color: var(--mut);
  text-align: right;
}

.cpl-11__avail {
  font-size: 13px;
  font-weight: 600;
  text-align: right;
  justify-self: end;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-bottom: 2px solid var(--acc);
  padding-bottom: 3px;
}

.cpl-11__index {
  display: block;
}

.cpl-11__row {
  position: relative;
  display: grid;
  grid-template-columns: 3ch 1fr auto auto;
  gap: calc(var(--u)*3);
  align-items: baseline;
  padding-block: calc(var(--u)*2.75);
  border-block-start: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
}

.cpl-11__row:last-child {
  border-block-end: 1px solid var(--line);
}

.cpl-11__row i {
  font-style: normal;
  font-size: 12px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.cpl-11__row h3 {
  font-size: clamp(19px,3cqi,25px);
  font-weight: 600;
  letter-spacing: -.02em;
  transition: translate .3s cubic-bezier(.2,.7,.2,1);
}

.cpl-11__row em {
  font-style: normal;
  font-size: 12.5px;
  color: var(--mut);
}

.cpl-11__row span {
  font-size: 12.5px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.cpl-11__row figure {
  --w: 150px;
  position: absolute;
  right: calc(var(--u)*14);
  top: 50%;
  width: var(--w);
  aspect-ratio: 4/3;
  translate: 0 -50%;
  border-radius: 8px;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  opacity: 0;
  scale: .6;
  clip-path: inset(50% round 8px);
  transition: opacity .25s,scale .4s cubic-bezier(.2,.7,.2,1),clip-path .4s cubic-bezier(.2,.7,.2,1);
  pointer-events: none;
  z-index: 1;
}

.cpl-11__row:hover figure,
.cpl-11__row:focus-visible figure {
  opacity: 1;
  scale: 1;
  clip-path: inset(0 round 8px);
}

.cpl-11__row:hover h3,
.cpl-11__row:focus-visible h3 {
  translate: calc(var(--u)*1.5) 0;
}

.cpl-11__row:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: -2px;
}

.cpl-11__foot {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 16px;
  margin-top: calc(var(--u)*6);
}

.cpl-11__foot a {
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 1px;
  padding: 6px 0;
}

.cpl-11__foot a:hover,
.cpl-11__foot a:focus-visible {
  color: var(--acc);
}

.cpl-11__foot a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-11__foot span {
  font-size: 12px;
  color: var(--mut);
}

@container (width < 560px) {
  .cpl-11__row {
    grid-template-columns: 3ch 1fr auto;
  }

  .cpl-11__row em {
    display: none;
  }

  .cpl-11__row figure {
    --w: 110px;
    right: calc(var(--u)*8);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cpl-11 * {
    transition-duration: .01ms !important;
  }
}
```
