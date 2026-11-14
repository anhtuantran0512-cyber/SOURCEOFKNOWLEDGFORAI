---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/glass-bento-grid-layout/"
title: "Glass Bento Grid Layout"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A modern responsive bento grid of Liquid Glass tiles at varying sizes, each using a different level of refraction — some tiles are flat frosted panels,…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Bento Grid Layout
Source: https://codefronts.com/layouts/css-card-grid-layout/glass-bento-grid-layout/

A modern responsive bento grid of Liquid Glass tiles at varying sizes, each using a different level of refraction — some tiles are flat frosted panels, others have pronounced lensed edges that bend the mesh background at their corners. A single CSS grid that reflows cleanly from desktop bento to a mobile stack.
## HTML
```html
<section class="cg-15" aria-label="Liquid glass bento grid demo">
  <div class="cg-15__grid">
    <a class="cg-15__t cg-15__t--hero" href="#cg-15" style="--edge:1"><span class="cg-15__k">Featured</span><h3>Design system v3</h3><p>72 components shipped this quarter with full Liquid Glass theming.</p></a>
    <a class="cg-15__t cg-15__t--tall" href="#cg-15" style="--edge:.6"><span class="cg-15__k">Guide</span><h3>Refraction 101</h3></a>
    <a class="cg-15__t" href="#cg-15" style="--edge:0"><span class="cg-15__big">21</span><p>Demos</p></a>
    <a class="cg-15__t" href="#cg-15" style="--edge:0"><span class="cg-15__big">0</span><p>CLS score</p></a>
    <a class="cg-15__t cg-15__t--wide" href="#cg-15" style="--edge:.4"><span class="cg-15__k">Perf</span><h3>60fps, GPU-composited</h3></a>
  </div>
</section>
```
## CSS
```css
.cg-15,
.cg-15 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-15 {
  width: 100%;
  min-height: 100vh;
  padding: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 20deg at 40% 30%,#7c3aed,#2563eb,#0891b2,#7c3aed);
  background-size: 200% 200%;
  animation: cg-15-bg 24s ease-in-out infinite;
}

@keyframes cg-15-bg {
  50% {
    background-position: 100% 100%;
  }
}

.cg-15__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: 96px;
  gap: 12px;
  max-width: 640px;
  margin: 0 auto;
}

.cg-15__t {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 16px;
  border-radius: 20px;
  overflow: hidden;
  isolation: isolate;
  text-decoration: none;
  color: #fff;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 20px 44px -28px rgba(0,0,0,.6);
  backdrop-filter: blur(18px) saturate(180%);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  transition: transform .3s;
}

.cg-15__t::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 20px;
  pointer-events: none;
  box-shadow: inset 0 0 calc(var(--edge,0)*26px) calc(var(--edge,0)*6px) rgba(255,255,255,.35);
  opacity: var(--edge,0);
}

.cg-15__t:hover {
  transform: translateY(-3px);
}

.cg-15__t:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.cg-15__t--hero {
  grid-column: span 2;
  grid-row: span 2;
}

.cg-15__t--tall {
  grid-column: span 2;
  grid-row: span 2;
}

.cg-15__t--wide {
  grid-column: span 2;
}

.cg-15__k {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .8;
  margin-bottom: auto;
}

.cg-15__t h3 {
  font-size: 18px;
  font-weight: 800;
  margin-top: 8px;
  line-height: 1.2;
}

.cg-15__t--hero h3 {
  font-size: 24px;
}

.cg-15__t p {
  font-size: 12.5px;
  color: rgba(255,255,255,.82);
  margin-top: 6px;
}

.cg-15__big {
  font-size: 36px;
  font-weight: 900;
  line-height: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cg-15 {
    animation: none;
  }

  .cg-15__t {
    transition: none;
  }
}

@media (max-width: 520px) {
  .cg-15__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .cg-15__t--hero,
    .cg-15__t--tall,
    .cg-15__t--wide {
    grid-column: span 2;
  }
}
```

## JavaScript
```js
/* No JavaScript — a single CSS grid with named spans builds the bento rhythm; each tile sets its own --edge to control how strong its lensed refractive rim is. Reflows to fewer columns on narrow widths. */
```
