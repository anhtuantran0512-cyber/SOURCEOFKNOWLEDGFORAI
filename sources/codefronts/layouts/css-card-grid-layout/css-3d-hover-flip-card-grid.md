---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-3d-hover-flip-card-grid/"
title: "CSS 3D Hover Flip Card Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A dense flashcard-style spec grid where hovering any tile cleanly rotates it 180 degrees on the Y axis to reveal a vivid accent-coloured backside of metrics,…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Hover Flip Card Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-3d-hover-flip-card-grid/

A dense flashcard-style spec grid where hovering any tile cleanly rotates it 180 degrees on the Y axis to reveal a vivid accent-coloured backside of metrics, with the grid layout itself never shifting.
## HTML
```html
<div class="cg-06">
  <div class="cg-06__grid">
    <div class="cg-06__flip">
      <div class="cg-06__inner">
        <div class="cg-06__front"><span class="cg-06__label">Latency</span><h3>API</h3></div>
        <div class="cg-06__back" style="--accent:#7c6af7"><span class="cg-06__metric">42ms</span><p>p95 response time</p></div>
      </div>
    </div>
    <div class="cg-06__flip">
      <div class="cg-06__inner">
        <div class="cg-06__front"><span class="cg-06__label">Uptime</span><h3>SLA</h3></div>
        <div class="cg-06__back" style="--accent:#00c2a8"><span class="cg-06__metric">99.98%</span><p>last 90 days</p></div>
      </div>
    </div>
    <div class="cg-06__flip">
      <div class="cg-06__inner">
        <div class="cg-06__front"><span class="cg-06__label">Throughput</span><h3>Requests</h3></div>
        <div class="cg-06__back" style="--accent:#ff6b9d"><span class="cg-06__metric">12k/s</span><p>peak sustained</p></div>
      </div>
    </div>
    <div class="cg-06__flip">
      <div class="cg-06__inner">
        <div class="cg-06__front"><span class="cg-06__label">Storage</span><h3>Database</h3></div>
        <div class="cg-06__back" style="--accent:#ffb454"><span class="cg-06__metric">4.2TB</span><p>across all shards</p></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cg-06,
.cg-06 *,
.cg-06 *::before,
.cg-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-06 ::selection {
  background: #7c6af7;
  color: #fff;
}

.cg-06 {
  background: #0d0d12;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  padding: 48px 24px;
  color: #fff;
}

.cg-06__grid {
  max-width: 780px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(160px,1fr));
  gap: 20px;
}

.cg-06__flip {
  perspective: 1000px;
  height: 160px;
}

.cg-06__inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.4,.2,.2,1);
}

.cg-06__flip:hover .cg-06__inner {
  transform: rotateY(180deg);
}
/* First card stays flipped at idle so the gallery thumbnail
   demonstrates the back-face metric pattern — visitors immediately
   see the 3D-flip identity without needing to hover. The other 3
   cards still flip on :hover for the full interaction demo. */

.cg-06__flip:first-child .cg-06__inner {
  transform: rotateY(180deg);
}

.cg-06__flip:first-child:hover .cg-06__inner {
  transform: rotateY(0);
}

.cg-06__front,
.cg-06__back {
  position: absolute;
  inset: 0;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 14px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.cg-06__front {
  background: #16161d;
  border: 1px solid rgba(255,255,255,.08);
}

.cg-06__label {
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.45);
}

.cg-06__front h3 {
  font-size: 1.2rem;
  font-weight: 700;
  margin-top: 6px;
}

.cg-06__back {
  background: var(--accent);
  color: #0d0d12;
  transform: rotateY(180deg);
}

.cg-06__metric {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cg-06__back p {
  font-size: .78rem;
  font-weight: 600;
  opacity: .75;
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cg-06__inner {
    transition: none;
  }
}
```
