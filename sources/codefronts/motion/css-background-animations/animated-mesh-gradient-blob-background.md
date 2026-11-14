---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-mesh-gradient-blob-background/"
title: "Animated Mesh Gradient Background"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The soft multi-colour wash that every modern SaaS front page now runs behind its hero — built as five independently orbiting radial gradients rather than one…"
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Mesh Gradient Background
Source: https://codefronts.com/motion/css-background-animations/animated-mesh-gradient-blob-background/

The soft multi-colour wash that every modern SaaS front page now runs behind its hero — built as five independently orbiting radial gradients rather than one baked image, so it moves, retheming is a five-token edit, and it costs one paint layer instead of a 400KB JPEG. Because the stops are registered <color> properties, the palette itself can cross-fade while the shapes drift.
## HTML
```html
<section class="bga-14" aria-label="Animated mesh gradient background demo">
  <div class="bga-14__mesh" aria-hidden="true"></div>
  <div class="bga-14__grain" aria-hidden="true"></div>

  <div class="bga-14__stage">
    <nav class="bga-14__nav" aria-label="Demo product navigation">
      <span class="bga-14__mark">◆ meshkit</span>
      <ul>
        <li><a href="#bga-14-main">Palette</a></li>
        <li><a href="#bga-14-main">Nodes</a></li>
        <li><a href="#bga-14-main">Export</a></li>
      </ul>
      <a class="bga-14__navBtn" href="#bga-14-main">Get the CSS</a>
    </nav>

    <div class="bga-14__hero" id="bga-14-main">
      <span class="bga-14__pill">14 · Five orbiting nodes</span>
      <h1 class="bga-14__title">A gradient mesh that is actually a gradient.</h1>
      <p class="bga-14__sub">No exported PNG, no canvas, no WebGL. Five radial stops on registered positions, one blur, one grain layer — and a palette you can retheme in five values.</p>
      <div class="bga-14__nodes" aria-hidden="true">
        <i style="background:oklch(0.72 0.19 12)"></i>
        <i style="background:oklch(0.7 0.17 320)"></i>
        <i style="background:oklch(0.74 0.15 250)"></i>
        <i style="background:oklch(0.8 0.14 190)"></i>
        <i style="background:oklch(0.84 0.16 82)"></i>
        <span>5 nodes · 26s · alternate</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@property --bga-14-p1x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 16%;
}

@property --bga-14-p1y {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 22%;
}

@property --bga-14-p2x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 82%;
}

@property --bga-14-p2y {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 18%;
}

@property --bga-14-p3x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 50%;
}

@property --bga-14-p3y {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 78%;
}

@property --bga-14-p4x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 88%;
}

@property --bga-14-p4y {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 72%;
}

@property --bga-14-p5x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 30%;
}

@property --bga-14-p5y {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 52%;
}

.bga-14,
.bga-14 *,
.bga-14 *::before,
.bga-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-14-c1: oklch(0.72 0.19 12);
  --bga-14-c2: oklch(0.7 0.17 320);
  --bga-14-c3: oklch(0.74 0.15 250);
  --bga-14-c4: oklch(0.8 0.14 190);
  --bga-14-c5: oklch(0.86 0.16 82);
  --bga-14-base: oklch(0.32 0.07 290);
  background: var(--bga-14-base);
  color: oklch(0.99 0.006 300);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-14__mesh {
  position: absolute;
  inset: 0;
  scale: 1.18;
  filter: blur(52px) saturate(1.28);
  background: radial-gradient(42% 52% at var(--bga-14-p1x) var(--bga-14-p1y),var(--bga-14-c1),transparent 62%), radial-gradient(46% 44% at var(--bga-14-p2x) var(--bga-14-p2y),var(--bga-14-c2),transparent 60%), radial-gradient(52% 50% at var(--bga-14-p3x) var(--bga-14-p3y),var(--bga-14-c3),transparent 62%), radial-gradient(38% 42% at var(--bga-14-p4x) var(--bga-14-p4y),var(--bga-14-c4),transparent 58%), radial-gradient(44% 46% at var(--bga-14-p5x) var(--bga-14-p5y),var(--bga-14-c5),transparent 60%), var(--bga-14-base);
  animation: bga-14-mesh 26s cubic-bezier(.45,0,.55,1) infinite alternate;
}

@keyframes bga-14-mesh {
  to {
    --bga-14-p1x: 34%;
    --bga-14-p1y: 56%;
    --bga-14-p2x: 62%;
    --bga-14-p2y: 34%;
    --bga-14-p3x: 28%;
    --bga-14-p3y: 62%;
    --bga-14-p4x: 66%;
    --bga-14-p4y: 86%;
    --bga-14-p5x: 56%;
    --bga-14-p5y: 24%;
  }
}

.bga-14__grain {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .22;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23g)'/%3E%3C/svg%3E");
  background-size: 180px 180px;
}

.bga-14__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: clamp(24px,5vh,60px);
  padding: clamp(18px,2.6vw,30px);
}

.bga-14__nav {
  display: flex;
  align-items: center;
  gap: clamp(12px,3vw,34px);
  padding: 11px 12px 11px 20px;
  border-radius: 99px;
  background: oklch(1 0 0/.1);
  border: 1px solid oklch(1 0 0/.2);
  backdrop-filter: blur(22px) saturate(1.5);
  -webkit-backdrop-filter: blur(22px) saturate(1.5);
}

.bga-14__mark {
  font-size: 14.5px;
  font-weight: 660;
  letter-spacing: -.02em;
  white-space: nowrap;
}

.bga-14__nav ul {
  list-style: none;
  display: flex;
  gap: clamp(10px,2vw,24px);
  margin-inline-end: auto;
}

.bga-14__nav a {
  font-size: 13.5px;
  color: oklch(1 0 0/.82);
  text-decoration: none;
  padding: 6px 2px;
  transition: color .2s;
}

.bga-14__nav a:hover {
  color: oklch(1 0 0);
}

.bga-14__nav a:focus-visible {
  outline: 2px solid oklch(1 0 0);
  outline-offset: 4px;
  border-radius: 4px;
}

.bga-14__navBtn {
  display: inline-flex;
  align-items: center;
  min-height: 40px;
  padding: 0 20px;
  border-radius: 99px;
  white-space: nowrap;
  font-size: 13.5px;
  font-weight: 620;
  text-decoration: none;
  color: oklch(0.24 0.05 300);
  background: oklch(0.99 0 0);
  transition: transform .35s cubic-bezier(.16,1,.3,1);
}

.bga-14__navBtn:hover {
  transform: translateY(-2px);
}

.bga-14__hero {
  display: grid;
  gap: 18px;
  justify-items: center;
  align-content: center;
  text-align: center;
  padding: clamp(10px,4vw,40px) 0;
}

.bga-14__pill {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  padding: 7px 14px;
  border-radius: 99px;
  background: oklch(1 0 0/.14);
  border: 1px solid oklch(1 0 0/.22);
  color: oklch(1 0 0/.9);
}

.bga-14__title {
  max-width: 16ch;
  font-size: clamp(32px,7vw,78px);
  font-weight: 620;
  line-height: .98;
  letter-spacing: -.055em;
  text-wrap: balance;
  text-shadow: 0 4px 60px oklch(0.2 0.05 300/.4);
}

.bga-14__sub {
  max-width: 56ch;
  font-size: clamp(14px,1.4vw,17.5px);
  line-height: 1.56;
  color: oklch(1 0 0/.82);
  text-wrap: pretty;
}

.bga-14__nodes {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
  padding: 9px 16px;
  border-radius: 99px;
  background: oklch(0.2 0.04 300/.3);
  border: 1px solid oklch(1 0 0/.18);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.bga-14__nodes i {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  box-shadow: 0 0 0 1px oklch(1 0 0/.3),0 0 14px -2px currentColor;
}

.bga-14__nodes span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.68);
  margin-inline-start: 6px;
}

@media (max-width: 620px) {
  .bga-14__nav ul {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bga-14__mesh {
    animation: none;
  }

  .bga-14__navBtn {
    transition: none;
  }
}
```
