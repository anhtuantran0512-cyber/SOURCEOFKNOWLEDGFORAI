---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/plasma-lava-lamp-fluid-effect/"
title: "Plasma / Lava Lamp Fluid Effect"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Metaballs with no maths, no canvas and no WebGL."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Plasma / Lava Lamp Fluid Effect
Source: https://codefronts.com/motion/css-background-animations/plasma-lava-lamp-fluid-effect/

Metaballs with no maths, no canvas and no WebGL. The gooey filter — blur() followed by a hard contrast() — turns overlapping blurred circles into a single fused fluid that stretches and snaps apart exactly like a real lava lamp. Six blobs on coprime orbits do the rest, and a screen-blended plasma layer underneath supplies the colour heat.
## HTML
```html
<section class="bga-08" aria-label="Plasma lava lamp fluid background demo">
  <div class="bga-08__heat" aria-hidden="true"></div>
  <div class="bga-08__goo" aria-hidden="true">
    <span class="bga-08__blob" style="--bga-08-t:19s;--bga-08-x:14%;--bga-08-y:22%;--bga-08-s:24vmax"></span>
    <span class="bga-08__blob" style="--bga-08-t:23s;--bga-08-x:72%;--bga-08-y:16%;--bga-08-s:19vmax"></span>
    <span class="bga-08__blob" style="--bga-08-t:29s;--bga-08-x:48%;--bga-08-y:64%;--bga-08-s:28vmax"></span>
    <span class="bga-08__blob" style="--bga-08-t:17s;--bga-08-x:86%;--bga-08-y:72%;--bga-08-s:16vmax"></span>
    <span class="bga-08__blob" style="--bga-08-t:31s;--bga-08-x:24%;--bga-08-y:82%;--bga-08-s:21vmax"></span>
    <span class="bga-08__blob" style="--bga-08-t:13s;--bga-08-x:60%;--bga-08-y:40%;--bga-08-s:13vmax"></span>
  </div>
  <div class="bga-08__tint" aria-hidden="true"></div>

  <div class="bga-08__stage">
    <div class="bga-08__card">
      <p class="bga-08__eyebrow">Metaballs · 08</p>
      <h1 class="bga-08__title">blur(28px) contrast(26)</h1>
      <p class="bga-08__sub">Two filter functions are the entire fluid simulation. Blur makes an alpha ramp, contrast snaps it to a threshold, and overlapping ramps fuse into one surface.</p>
      <div class="bga-08__pipe" aria-hidden="true">
        <span>6 blobs</span><b>→</b><span>blur 28px</span><b>→</b><span>contrast 26</span><b>→</b><span>screen tint</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-08,
.bga-08 *,
.bga-08 *::before,
.bga-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-08-bg: oklch(0.14 0.04 300);
  --bga-08-a: oklch(0.68 0.24 12);
  --bga-08-b: oklch(0.62 0.23 330);
  --bga-08-c: oklch(0.75 0.19 62);
  background: var(--bga-08-bg);
  color: oklch(0.98 0.01 320);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-08__heat {
  position: absolute;
  inset: 0;
  background: radial-gradient(70% 60% at 50% 100%,color-mix(in oklab,var(--bga-08-a) 32%,transparent),transparent 70%), radial-gradient(60% 50% at 20% 0%,color-mix(in oklab,var(--bga-08-b) 26%,transparent),transparent 72%);
}

.bga-08__goo {
  position: absolute;
  inset: -12%;
  filter: blur(28px) contrast(26);
  opacity: .92;
}

.bga-08__blob {
  position: absolute;
  left: var(--bga-08-x);
  top: var(--bga-08-y);
  width: var(--bga-08-s);
  aspect-ratio: 1;
  border-radius: 50%;
  translate: -50% -50%;
  background: oklch(0.72 0.22 340);
  animation: bga-08-orbit var(--bga-08-t) ease-in-out infinite alternate, bga-08-sway calc(var(--bga-08-t) * .61) ease-in-out infinite alternate;
}

.bga-08__blob:nth-child(2n) {
  background: oklch(0.7 0.23 20);
}

.bga-08__blob:nth-child(3n) {
  background: oklch(0.76 0.19 60);
}

@keyframes bga-08-orbit {
  from {
    translate: -70% -40%;
    scale: .86;
  }

  to {
    translate: -24% -66%;
    scale: 1.14;
  }
}

@keyframes bga-08-sway {
  from {
    margin-left: -6vmax;
  }

  to {
    margin-left: 7vmax;
  }
}

.bga-08__tint {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: screen;
  opacity: .55;
  background: conic-gradient(from 210deg at 40% 60%,color-mix(in oklab,var(--bga-08-c) 40%,transparent),transparent 30%,color-mix(in oklab,var(--bga-08-b) 45%,transparent) 62%,transparent 85%);
  animation: bga-08-spin 44s linear infinite;
}

@keyframes bga-08-spin {
  to {
    rotate: 360deg;
  }
}

.bga-08__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-08__card {
  width: min(100%,660px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 28px;
  background: oklch(0.1 0.03 300/.5);
  border: 1px solid oklch(1 0 0/.14);
  backdrop-filter: blur(26px) saturate(1.5);
  -webkit-backdrop-filter: blur(26px) saturate(1.5);
  box-shadow: 0 50px 110px -50px oklch(0 0 0/.95),inset 0 1px 0 oklch(1 0 0/.2);
}

.bga-08__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.85 0.14 40);
}

.bga-08__title {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(21px,4.4vw,44px);
  font-weight: 600;
  letter-spacing: -.04em;
  line-height: 1.1;
  text-wrap: balance;
}

.bga-08__sub {
  max-width: 48ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.94 0.01 320/.78);
  text-wrap: pretty;
}

.bga-08__pipe {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  align-items: center;
  justify-content: center;
  margin-top: 6px;
}

.bga-08__pipe span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 6px 11px;
  border-radius: 8px;
  background: oklch(1 0 0/.08);
  border: 1px solid oklch(1 0 0/.14);
  color: oklch(0.97 0 0/.85);
}

.bga-08__pipe b {
  font-size: 11px;
  color: oklch(1 0 0/.35);
}

@media (prefers-reduced-motion: reduce) {
  .bga-08__blob,
    .bga-08__tint {
    animation: none;
  }

  .bga-08__blob:nth-child(2n) {
    translate: -38% -58%;
  }

  .bga-08__blob:nth-child(3n) {
    translate: -62% -44%;
  }
}
```
