---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-comic-book-dot-halftone-wave/"
title: "Animated Halftone Dot Pattern"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Real halftone: dot size carries the tone, exactly as it does on a printing plate."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Halftone Dot Pattern
Source: https://codefronts.com/motion/css-background-animations/animated-comic-book-dot-halftone-wave/

Real halftone: dot size carries the tone, exactly as it does on a printing plate. A radial-gradient dot grid is masked by a moving luminance ramp, so dots grow toward the dark end and shrink to nothing in the highlights — and because the ramp animates, the tonal wave sweeps across the plate like a press sheet being pulled. Two colour separations at different screen angles complete the CMYK illusion.
## HTML
```html
<section class="bga-17" aria-label="Animated halftone dot pattern background demo">
  <div class="bga-17__paper" aria-hidden="true"></div>
  <div class="bga-17__plate bga-17__plate--c" aria-hidden="true"></div>
  <div class="bga-17__plate bga-17__plate--m" aria-hidden="true"></div>
  <div class="bga-17__plate bga-17__plate--k" aria-hidden="true"></div>
  <div class="bga-17__photo" role="img" aria-label="Portrait rendered as a halftone dot screen"></div>

  <div class="bga-17__stage">
    <div class="bga-17__sheet">
      <div class="bga-17__regmarks" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
      <p class="bga-17__eyebrow">Separation · 17</p>
      <h1 class="bga-17__title">Tone is dot size.<br>Nothing else.</h1>
      <p class="bga-17__sub">A mask eats each dot from its soft edge inward, so the grid appears to grow and shrink. Two plates at 15° and −30° overprint like real ink.</p>
      <dl class="bga-17__specs">
        <div><dt>Screen ruling</dt><dd>14 px</dd></div>
        <div><dt>Angles</dt><dd>15° / −30° / 60°</dd></div>
        <div><dt>Blend</dt><dd>multiply</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-17,
.bga-17 *,
.bga-17 *::before,
.bga-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-17-paper: oklch(0.96 0.017 92);
  --bga-17-c: oklch(0.72 0.15 205);
  --bga-17-m: oklch(0.66 0.23 350);
  --bga-17-k: oklch(0.35 0.03 60);
  background: var(--bga-17-paper);
  color: oklch(0.22 0.02 60);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-17__paper {
  position: absolute;
  inset: 0;
  background: radial-gradient(110% 90% at 50% 0%,oklch(0.99 0.012 92),oklch(0.93 0.022 84) 78%);
}

.bga-17__plate {
  position: absolute;
  inset: -40%;
  mix-blend-mode: multiply;
  -webkit-mask-size: 240% 100%;
  mask-size: 240% 100%;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}

.bga-17__plate--c {
  rotate: 15deg;
  background-image: radial-gradient(var(--bga-17-c) 46%,transparent 52%);
  background-size: 14px 14px;
  -webkit-mask-image: linear-gradient(115deg,oklch(0 0 0) 6%,oklch(0 0 0/.45) 34%,transparent 66%);
  mask-image: linear-gradient(115deg,oklch(0 0 0) 6%,oklch(0 0 0/.45) 34%,transparent 66%);
  animation: bga-17-sweep 14s linear infinite;
}

.bga-17__plate--m {
  rotate: -30deg;
  opacity: .9;
  background-image: radial-gradient(var(--bga-17-m) 44%,transparent 50%);
  background-size: 17px 17px;
  -webkit-mask-image: linear-gradient(70deg,transparent 24%,oklch(0 0 0/.6) 52%,oklch(0 0 0) 88%);
  mask-image: linear-gradient(70deg,transparent 24%,oklch(0 0 0/.6) 52%,oklch(0 0 0) 88%);
  animation: bga-17-sweep-r 19s linear infinite;
}

.bga-17__plate--k {
  rotate: 60deg;
  opacity: .35;
  background-image: radial-gradient(var(--bga-17-k) 38%,transparent 44%);
  background-size: 7px 7px;
  -webkit-mask-image: radial-gradient(90% 80% at 50% 50%,transparent 34%,oklch(0 0 0) 92%);
  mask-image: radial-gradient(90% 80% at 50% 50%,transparent 34%,oklch(0 0 0) 92%);
  -webkit-mask-size: 130% 130%;
  mask-size: 130% 130%;
  -webkit-mask-position: center;
  mask-position: center;
  animation: bga-17-turn 90s linear infinite;
}

@keyframes bga-17-sweep {
  from {
    -webkit-mask-position: -70% 0;
    mask-position: -70% 0;
  }

  to {
    -webkit-mask-position: 170% 0;
    mask-position: 170% 0;
  }
}

@keyframes bga-17-sweep-r {
  from {
    -webkit-mask-position: 170% 0;
    mask-position: 170% 0;
  }

  to {
    -webkit-mask-position: -70% 0;
    mask-position: -70% 0;
  }
}

@keyframes bga-17-turn {
  to {
    rotate: 420deg;
  }
}

.bga-17__photo {
  position: absolute;
  inset: 0;
  opacity: .62;
  mix-blend-mode: multiply;
  background-image: radial-gradient(var(--bga-17-k) 44%,transparent 50%);
  background-size: 9px 9px;
  -webkit-mask-image: url("https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=1200&auto=format&fit=crop");
  mask-image: url("https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=1200&auto=format&fit=crop");
  -webkit-mask-size: cover;
  mask-size: cover;
  -webkit-mask-position: center;
  mask-position: center;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  animation: bga-17-breathe 24s ease-in-out infinite alternate;
}

@keyframes bga-17-breathe {
  to {
    background-size: 13px 13px;
    opacity: .42;
  }
}

.bga-17__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-17__sheet {
  position: relative;
  width: min(100%,700px);
  display: grid;
  gap: 15px;
  padding: clamp(28px,4vw,54px);
  background: oklch(0.99 0.008 92/.94);
  border: 1px solid oklch(0.22 0.02 60/.16);
  box-shadow: 0 30px 70px -40px oklch(0.3 0.04 60/.5),0 2px 0 oklch(0.22 0.02 60/.08);
}

.bga-17__regmarks {
  position: absolute;
  inset: 9px;
  pointer-events: none;
}

.bga-17__regmarks span {
  position: absolute;
  width: 15px;
  height: 15px;
  border: 1px solid oklch(0.22 0.02 60/.4);
  border-radius: 50%;
}

.bga-17__regmarks span::before,
.bga-17__regmarks span::after {
  content: '';
  position: absolute;
  background: oklch(0.22 0.02 60/.4);
}

.bga-17__regmarks span::before {
  left: 50%;
  top: -5px;
  width: 1px;
  height: 25px;
  translate: -50% 0;
}

.bga-17__regmarks span::after {
  top: 50%;
  left: -5px;
  height: 1px;
  width: 25px;
  translate: 0 -50%;
}

.bga-17__regmarks span:nth-child(1) {
  left: 0;
  top: 0;
}

.bga-17__regmarks span:nth-child(2) {
  right: 0;
  top: 0;
}

.bga-17__regmarks span:nth-child(3) {
  left: 0;
  bottom: 0;
}

.bga-17__regmarks span:nth-child(4) {
  right: 0;
  bottom: 0;
}

.bga-17__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--bga-17-m);
}

.bga-17__title {
  font-size: clamp(28px,5.6vw,58px);
  font-weight: 700;
  line-height: .98;
  letter-spacing: -.055em;
  text-wrap: balance;
}

.bga-17__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.22 0.02 60/.76);
  text-wrap: pretty;
}

.bga-17__specs {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 28px;
  margin-top: 8px;
  padding-top: 16px;
  border-top: 2px solid oklch(0.22 0.02 60/.14);
}

.bga-17__specs div {
  display: grid;
  gap: 3px;
}

.bga-17__specs dt {
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.22 0.02 60/.5);
}

.bga-17__specs dd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14px;
  font-weight: 600;
  color: var(--bga-17-c);
}

@media (prefers-reduced-motion: reduce) {
  .bga-17__plate,
    .bga-17__photo {
    animation: none;
  }
}
```
