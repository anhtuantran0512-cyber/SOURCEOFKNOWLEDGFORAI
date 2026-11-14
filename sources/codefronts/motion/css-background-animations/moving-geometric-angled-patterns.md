---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/moving-geometric-angled-patterns/"
title: "Floating Geometric Shapes"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Triangles, hexagons, crosses and rings drifting through three depth planes, each plane with its own speed, blur and opacity — so the composition has actual…"
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Geometric Shapes
Source: https://codefronts.com/motion/css-background-animations/moving-geometric-angled-patterns/

Triangles, hexagons, crosses and rings drifting through three depth planes, each plane with its own speed, blur and opacity — so the composition has actual foreground and background rather than being a flat scatter. Every shape is one element with a clip-path, and each one rotates on its own axis while its plane translates, which is what keeps the motion from looking like a single sliding sheet.
## HTML
```html
<section class="bga-23" aria-label="Floating geometric shapes background demo">
  <div class="bga-23__wash" aria-hidden="true"></div>

  <div class="bga-23__plane bga-23__plane--back" aria-hidden="true">
    <span class="bga-23__s bga-23__s--tri" style="--bga-23-x:12%;--bga-23-y:22%;--bga-23-w:16vmin;--bga-23-f:1.2;--bga-23-c:oklch(0.72 0.16 24)"></span>
    <span class="bga-23__s bga-23__s--hex" style="--bga-23-x:78%;--bga-23-y:16%;--bga-23-w:20vmin;--bga-23-f:.8;--bga-23-c:oklch(0.7 0.14 250)"></span>
    <span class="bga-23__s bga-23__s--ring" style="--bga-23-x:56%;--bga-23-y:74%;--bga-23-w:24vmin;--bga-23-f:1.35;--bga-23-c:oklch(0.78 0.15 160)"></span>
    <span class="bga-23__s bga-23__s--cross" style="--bga-23-x:26%;--bga-23-y:82%;--bga-23-w:13vmin;--bga-23-f:.95;--bga-23-c:oklch(0.8 0.15 88)"></span>
  </div>

  <div class="bga-23__plane bga-23__plane--mid" aria-hidden="true">
    <span class="bga-23__s bga-23__s--hex" style="--bga-23-x:34%;--bga-23-y:38%;--bga-23-w:14vmin;--bga-23-f:1.1;--bga-23-c:oklch(0.66 0.19 330)"></span>
    <span class="bga-23__s bga-23__s--tri" style="--bga-23-x:88%;--bga-23-y:58%;--bga-23-w:11vmin;--bga-23-f:.75;--bga-23-c:oklch(0.74 0.17 200)"></span>
    <span class="bga-23__s bga-23__s--sq" style="--bga-23-x:8%;--bga-23-y:56%;--bga-23-w:12vmin;--bga-23-f:1.3;--bga-23-c:oklch(0.76 0.16 60)"></span>
    <span class="bga-23__s bga-23__s--ring" style="--bga-23-x:64%;--bga-23-y:26%;--bga-23-w:9vmin;--bga-23-f:.9;--bga-23-c:oklch(0.68 0.18 300)"></span>
  </div>

  <div class="bga-23__plane bga-23__plane--front" aria-hidden="true">
    <span class="bga-23__s bga-23__s--cross" style="--bga-23-x:18%;--bga-23-y:12%;--bga-23-w:7vmin;--bga-23-f:1.15;--bga-23-c:oklch(0.62 0.21 20)"></span>
    <span class="bga-23__s bga-23__s--tri" style="--bga-23-x:72%;--bga-23-y:88%;--bga-23-w:8vmin;--bga-23-f:.85;--bga-23-c:oklch(0.58 0.2 268)"></span>
    <span class="bga-23__s bga-23__s--sq" style="--bga-23-x:92%;--bga-23-y:34%;--bga-23-w:6vmin;--bga-23-f:1.25;--bga-23-c:oklch(0.66 0.19 150)"></span>
  </div>

  <div class="bga-23__stage">
    <div class="bga-23__card">
      <p class="bga-23__eyebrow">Three depth planes · 23</p>
      <h1 class="bga-23__title">Blur and speed are<br>the same variable.</h1>
      <p class="bga-23__sub">Each plane carries one trio of tokens — scale, blur, opacity — and every shape inside inherits it. That correlation is what your eye reads as distance.</p>
      <div class="bga-23__planes">
        <span><i style="filter:blur(2.4px)"></i>back · 64s</span>
        <span><i style="filter:blur(.8px)"></i>mid · 44s</span>
        <span><i></i>front · 28s</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-23,
.bga-23 *,
.bga-23 *::before,
.bga-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-23-bg: oklch(0.96 0.012 250);
  --bga-23-ink: oklch(0.22 0.03 265);
  background: var(--bga-23-bg);
  color: var(--bga-23-ink);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-23__wash {
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 100% at 76% 4%,oklch(0.99 0.01 240),oklch(0.92 0.02 258) 76%);
}

.bga-23__plane {
  position: absolute;
  inset: -14%;
}

.bga-23__plane--back {
  filter: blur(3px);
  opacity: .34;
  --bga-23-spd: 64s;
  animation: bga-23-pan 64s ease-in-out infinite alternate;
}

.bga-23__plane--mid {
  filter: blur(1px);
  opacity: .6;
  --bga-23-spd: 44s;
  animation: bga-23-pan 44s ease-in-out infinite alternate-reverse;
}

.bga-23__plane--front {
  opacity: .9;
  --bga-23-spd: 28s;
  animation: bga-23-pan 28s ease-in-out infinite alternate;
}

@keyframes bga-23-pan {
  from {
    translate: -2% 1%;
  }

  to {
    translate: 3% -2%;
  }
}

.bga-23__s {
  position: absolute;
  left: var(--bga-23-x);
  top: var(--bga-23-y);
  width: var(--bga-23-w);
  aspect-ratio: 1;
  background: var(--bga-23-c);
  animation: bga-23-bob calc(var(--bga-23-spd) * var(--bga-23-f,1) * .34) ease-in-out infinite alternate, bga-23-spin calc(var(--bga-23-spd) * var(--bga-23-f,1) * 1.7) linear infinite;
}

@keyframes bga-23-bob {
  from {
    translate: -50% -42%;
  }

  to {
    translate: -50% -62%;
  }
}

@keyframes bga-23-spin {
  to {
    rotate: 360deg;
  }
}

.bga-23__s--tri {
  clip-path: polygon(50% 0%,100% 100%,0% 100%);
}

.bga-23__s--hex {
  clip-path: polygon(25% 0%,75% 0%,100% 50%,75% 100%,25% 100%,0% 50%);
}

.bga-23__s--sq {
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%);
  border-radius: 14%;
}

.bga-23__s--cross {
  clip-path: polygon(35% 0,65% 0,65% 35%,100% 35%,100% 65%,65% 65%,65% 100%,35% 100%,35% 65%,0 65%,0 35%,35% 35%);
}

.bga-23__s--ring {
  background: none;
  border-radius: 50%;
  box-shadow: inset 0 0 0 min(2.2vmin,16px) var(--bga-23-c);
}

.bga-23__stage {
  position: relative;
  z-index: 4;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-23__card {
  width: min(100%,660px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 26px;
  background: oklch(1 0 0/.78);
  border: 1px solid oklch(0.22 0.03 265/.1);
  backdrop-filter: blur(20px) saturate(1.4);
  -webkit-backdrop-filter: blur(20px) saturate(1.4);
  box-shadow: 0 40px 90px -52px oklch(0.24 0.05 265/.5);
}

.bga-23__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.55 0.2 268);
}

.bga-23__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 640;
  line-height: 1.03;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-23__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: color-mix(in oklab,var(--bga-23-ink) 76%,transparent);
  text-wrap: pretty;
}

.bga-23__planes {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 6px;
}

.bga-23__planes span {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: color-mix(in oklab,var(--bga-23-ink) 62%,transparent);
  background: oklch(0.22 0.03 265/.05);
  border: 1px solid oklch(0.22 0.03 265/.1);
}

.bga-23__planes i {
  width: 11px;
  height: 11px;
  background: oklch(0.55 0.2 268);
  clip-path: polygon(50% 0%,100% 100%,0% 100%);
}

@media (prefers-reduced-motion: reduce) {
  .bga-23__s,
    .bga-23__plane {
    animation: none;
  }
}
```
