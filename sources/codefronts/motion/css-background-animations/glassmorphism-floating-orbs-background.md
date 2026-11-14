---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/glassmorphism-floating-orbs-background/"
title: "Floating Glassmorphism Orbs"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Glass spheres, not frosted circles."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Glassmorphism Orbs
Source: https://codefronts.com/motion/css-background-animations/glassmorphism-floating-orbs-background/

Glass spheres, not frosted circles. Each orb layers four things a real glass ball has — a backdrop-filter refraction, an inner rim light from a conic gradient, a specular highlight offset toward the light source, and a contact shadow — and they drift on a slow 3D path so the refraction under them visibly changes. This is the glassmorphism that still looks current, because it is doing optics rather than applying a blur.
## HTML
```html
<section class="bga-19" aria-label="Floating glassmorphism orbs background demo">
  <div class="bga-19__field" aria-hidden="true">
    <img class="bga-19__photo" src="https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?q=80&w=1800&auto=format&fit=crop" alt="" width="1800" height="1200" loading="lazy" decoding="async">
  </div>
  <div class="bga-19__orbs" aria-hidden="true">
    <span class="bga-19__orb" style="--bga-19-x:14%;--bga-19-y:24%;--bga-19-s:26vmin;--bga-19-t:19s"></span>
    <span class="bga-19__orb" style="--bga-19-x:76%;--bga-19-y:18%;--bga-19-s:17vmin;--bga-19-t:25s"></span>
    <span class="bga-19__orb" style="--bga-19-x:62%;--bga-19-y:72%;--bga-19-s:31vmin;--bga-19-t:31s"></span>
    <span class="bga-19__orb" style="--bga-19-x:22%;--bga-19-y:80%;--bga-19-s:14vmin;--bga-19-t:16s"></span>
    <span class="bga-19__orb" style="--bga-19-x:90%;--bga-19-y:52%;--bga-19-s:11vmin;--bga-19-t:23s"></span>
  </div>

  <div class="bga-19__stage">
    <div class="bga-19__card">
      <p class="bga-19__eyebrow">Optical glass · 19</p>
      <h1 class="bga-19__title">Refraction, rim, specular, shadow.</h1>
      <p class="bga-19__sub">Four layers per sphere and one consistent light direction. Skip any of them and it reads as a frosted circle — which is why most glassmorphism aged badly.</p>
      <ol class="bga-19__stack">
        <li><b>1</b>backdrop-filter blur + saturate</li>
        <li><b>2</b>inset rim light 1px</li>
        <li><b>3</b>specular at 32% / 26%</li>
        <li><b>4</b>back-face bounce + contact shadow</li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-19,
.bga-19 *,
.bga-19 *::before,
.bga-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-19-bg: oklch(0.24 0.07 288);
  background: var(--bga-19-bg);
  color: oklch(0.98 0.008 300);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-19__field {
  position: absolute;
  inset: -10%;
  filter: blur(30px);
  background: radial-gradient(38% 46% at 18% 24%,oklch(0.68 0.2 22),transparent 64%), radial-gradient(42% 40% at 82% 20%,oklch(0.66 0.19 300),transparent 62%), radial-gradient(46% 48% at 62% 82%,oklch(0.72 0.16 200),transparent 64%), radial-gradient(40% 44% at 26% 86%,oklch(0.78 0.17 88),transparent 62%), var(--bga-19-bg);
  animation: bga-19-field 34s ease-in-out infinite alternate;
}

@keyframes bga-19-field {
  to {
    translate: -4% 3%;
    scale: 1.1;
    filter: blur(38px) hue-rotate(22deg);
  }
}

.bga-19__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: .55;
  mix-blend-mode: overlay;
}

.bga-19__orbs {
  position: absolute;
  inset: 0;
}

.bga-19__orb {
  position: absolute;
  left: var(--bga-19-x);
  top: var(--bga-19-y);
  width: var(--bga-19-s);
  aspect-ratio: 1;
  translate: -50% -50%;
  border-radius: 50%;
  backdrop-filter: blur(14px) saturate(1.7) brightness(1.05);
  -webkit-backdrop-filter: blur(14px) saturate(1.7) brightness(1.05);
  background: radial-gradient(circle at 32% 26%,
      oklch(1 0 0/.6) 0 10%,oklch(1 0 0/.16) 26%,oklch(1 0 0/.04) 48%,transparent 64%);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.34), inset -16px -20px 40px oklch(1 0 0/.14), inset 12px 16px 34px oklch(0.4 0.1 300/.18), 0 34px 64px -24px oklch(0.1 0.04 290/.6);
  animation: bga-19-float var(--bga-19-t) ease-in-out infinite alternate;
}

@keyframes bga-19-float {
  from {
    translate: -54% -46%;
    rotate: -6deg;
    scale: .96;
  }

  to {
    translate: -46% -56%;
    rotate: 8deg;
    scale: 1.05;
  }
}

.bga-19__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-19__card {
  width: min(100%,660px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 28px;
  background: oklch(1 0 0/.09);
  border: 1px solid oklch(1 0 0/.2);
  backdrop-filter: blur(30px) saturate(1.5);
  -webkit-backdrop-filter: blur(30px) saturate(1.5);
  box-shadow: 0 44px 100px -50px oklch(0.1 0.04 290/.85),inset 0 1px 0 oklch(1 0 0/.4);
}

.bga-19__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.94 0.06 300/.9);
}

.bga-19__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 620;
  line-height: 1.04;
  letter-spacing: -.05em;
  text-wrap: balance;
  text-shadow: 0 2px 30px oklch(0.15 0.05 290/.4);
}

.bga-19__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(1 0 0/.8);
  text-wrap: pretty;
}

.bga-19__stack {
  list-style: none;
  display: grid;
  gap: 6px;
  width: min(100%,420px);
  margin-top: 6px;
  text-align: left;
}

.bga-19__stack li {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 9px 14px;
  border-radius: 12px;
  font-size: 12.5px;
  color: oklch(1 0 0/.82);
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.12);
}

.bga-19__stack b {
  display: grid;
  place-items: center;
  width: 21px;
  height: 21px;
  flex: none;
  border-radius: 7px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  background: oklch(1 0 0/.9);
  color: oklch(0.26 0.07 290);
}

@media (prefers-reduced-motion: reduce) {
  .bga-19__orb,
    .bga-19__field {
    animation: none;
  }
}
```
