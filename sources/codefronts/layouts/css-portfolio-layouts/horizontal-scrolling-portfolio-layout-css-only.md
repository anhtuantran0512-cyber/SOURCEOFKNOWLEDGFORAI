---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/horizontal-scrolling-portfolio-layout-css-only/"
title: "Horizontal Scrolling Portfolio Layout CSS Only"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "A side-scrolling showcase the way agencies build them: grid-auto-flow:column lays the panels in a row, scroll-snap lands each one crisply, and a…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Scrolling Portfolio Layout CSS Only
Source: https://codefronts.com/layouts/css-portfolio-layouts/horizontal-scrolling-portfolio-layout-css-only/

A side-scrolling showcase the way agencies build them: grid-auto-flow:column lays the panels in a row, scroll-snap lands each one crisply, and a scroll-driven progress bar (pure CSS animation-timeline: scroll()) fills as you traverse — zero JavaScript anywhere. The scroller is keyboard-operable out of the box (tabindex + arrow keys), momentum-friendly on trackpads, and each panel numbers itself with a CSS counter.
## HTML
```html
<section class="cpl-06" aria-label="Horizontal scrolling portfolio demo">
  <div class="cpl-06__stage">
    <header class="cpl-06__head">
      <h2>Recent Work</h2>
      <p>Scroll sideways — trackpad, arrows or drag</p>
    </header>
    <div class="cpl-06__rail" tabindex="0" role="region" aria-label="Projects, horizontally scrollable">
      <a class="cpl-06__panel" href="#solace" style="--img:url('https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?q=80&w=900&auto=format&fit=crop');--a:oklch(0.76 0.12 280);--b:oklch(0.45 0.15 250)">
        <figure></figure><div><h3>Solace Sleep</h3><p>DTC brand &amp; storefront</p></div>
      </a>
      <a class="cpl-06__panel" href="#granite" style="--img:url('https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=900&auto=format&fit=crop');--a:oklch(0.8 0.1 50);--b:oklch(0.52 0.14 30)">
        <figure></figure><div><h3>Granite Supply</h3><p>B2B ordering platform</p></div>
      </a>
      <a class="cpl-06__panel" href="#murmur" style="--img:url('https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.11 330);--b:oklch(0.48 0.15 310)">
        <figure></figure><div><h3>Murmur Audio</h3><p>Product launch site</p></div>
      </a>
      <a class="cpl-06__panel" href="#alpine" style="--img:url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.09 150);--b:oklch(0.52 0.12 180)">
        <figure></figure><div><h3>Alpine Journal</h3><p>Editorial platform</p></div>
      </a>
      <a class="cpl-06__panel" href="#quartz" style="--img:url('https://images.unsplash.com/photo-1522542550221-31fd19575a2d?q=80&w=900&auto=format&fit=crop');--a:oklch(0.84 0.07 220);--b:oklch(0.55 0.11 250)">
        <figure></figure><div><h3>Quartz Studio</h3><p>Portfolio &amp; CMS</p></div>
      </a>
    </div>
    <div class="cpl-06__track" aria-hidden="true"><i class="cpl-06__bar"></i></div>
  </div>
</section>
```
## CSS
```css
.cpl-06,
.cpl-06 *,
.cpl-06 *::before,
.cpl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-06 {
  --bg: oklch(0.21 0.02 275);
  --ink: oklch(0.95 0.005 90);
  --mut: oklch(0.66 0.015 275);
  --line: oklch(0.31 0.02 275);
  --acc: oklch(0.78 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-06__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(18px,4cqi,28px) 0;
  timeline-scope: --cpl06;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-06__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 14px;
  padding: 0 24px;
  margin-bottom: 18px;
}

.cpl-06__head h2 {
  font-size: 24px;
  letter-spacing: -.02em;
}

.cpl-06__head p {
  font-size: 12.5px;
  color: var(--mut);
}

.cpl-06__rail {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: min(520px,80%);
  gap: 16px;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: 24px;
  padding: 4px 24px 18px;
  counter-reset: cpl06;
  scroll-timeline: --cpl06 x;
  scrollbar-width: thin;
  scrollbar-color: oklch(0.45 0.02 275) transparent;
}

.cpl-06__rail:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 12px;
}

.cpl-06__panel {
  scroll-snap-align: start;
  counter-increment: cpl06;
  display: grid;
  gap: 0;
  border-radius: 16px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  background: oklch(0.26 0.02 275);
  border: 1px solid var(--line);
  transition: translate .3s cubic-bezier(.2,.7,.2,1),border-color .3s;
}

.cpl-06__panel:hover,
.cpl-06__panel:focus-visible {
  translate: 0 -4px;
  border-color: oklch(0.45 0.04 75);
}

.cpl-06__panel:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-06__panel figure {
  position: relative;
  aspect-ratio: 16/10;
  background-image: var(--img,none),linear-gradient(140deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.cpl-06__panel figure::after {
  content: "0" counter(cpl06);
  position: absolute;
  top: 12px;
  left: 14px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .08em;
  color: oklch(1 0 0/.85);
  font-variant-numeric: tabular-nums;
}

.cpl-06__panel div {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 16px;
}

.cpl-06__panel h3 {
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.cpl-06__panel p {
  font-size: 12px;
  color: var(--mut);
  white-space: nowrap;
}

.cpl-06__track {
  display: none;
}

@supports (animation-timeline: scroll()) {
  .cpl-06__track {
    display: block;
    height: 3px;
    margin: 14px 24px 0;
    border-radius: 99px;
    background: oklch(0.32 0.02 275);
  }

  .cpl-06__bar {
    display: block;
    height: 100%;
    border-radius: 99px;
    background: var(--acc);
    transform-origin: left;
    animation: cpl06-grow linear both;
    animation-timeline: --cpl06;
  }

  @keyframes cpl06-grow {
    from {
      transform: scaleX(.06);
    }

    to {
      transform: scaleX(1);
    }
  }
}

.cpl-06__panel figure::after {
  text-shadow: 0 1px 10px oklch(0.1 0 0/.6);
}

@media (prefers-reduced-motion: reduce) {
  .cpl-06__panel {
    transition-duration: .01ms !important;
  }
}
```
