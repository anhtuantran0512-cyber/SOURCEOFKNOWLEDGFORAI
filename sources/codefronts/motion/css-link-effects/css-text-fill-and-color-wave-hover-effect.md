---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-text-fill-and-color-wave-hover-effect/"
title: "CSS Text Fill & Color Wave Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Liquid typography: ink that rises inside the glyphs when you hover."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Fill & Color Wave Hover Effect
Source: https://codefronts.com/motion/css-link-effects/css-text-fill-and-color-wave-hover-effect/

Liquid typography: ink that rises inside the glyphs when you hover. A flat fill that climbs from the baseline, a wavy crest version that actually looks like liquid (an inline SVG wave, no canvas), and a color wave that flows through the letters for as long as the pointer stays. All three are one gradient trick wearing different costumes.
## HTML
```html
<section class="cle-05" aria-label="Text fill and color wave hover demo">
  <div class="cle-05__stage">
    <div class="cle-05__var"><a href="#a" class="cle-05__rise">Reservoir</a><small class="cle-05__cap">A · flat fill rises</small></div>
    <div class="cle-05__var"><a href="#b" class="cle-05__wave">High tide</a><small class="cle-05__cap">B · liquid crest (SVG wave)</small></div>
    <div class="cle-05__var"><a href="#c" class="cle-05__flow">Spectrum</a><small class="cle-05__cap">C · color wave while hovered</small></div>
  </div>
</section>
```
## CSS
```css
.cle-05,
.cle-05 *,
.cle-05 *::before,
.cle-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-05 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.26 0.02 240);
  --brand: oklch(0.58 0.14 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-05__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 42px;
  border: 1px solid oklch(0.9 0.012 240);
  background: linear-gradient(180deg,oklch(0.985 0.005 220),oklch(0.945 0.015 230));
  padding: 44px 32px;
}

.cle-05__var {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.cle-05__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 235);
}

.cle-05 a {
  font-size: clamp(34px,5.6vw,52px);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.1;
  text-decoration: none;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  background-repeat: repeat-x;
}

.cle-05 a::selection {
  background: oklch(0.85 0.06 230 / .5);
  color: var(--ink);
  -webkit-text-fill-color: var(--ink);
}

.cle-05 a:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-05__rise {
  background-image: linear-gradient(to top,var(--brand) 0 50%,var(--ink) 50% 100%);
  background-size: 100% 200%;
  background-position: 0 0;
  transition: background-position .55s cubic-bezier(.3,.7,.3,1);
}

.cle-05__rise:hover,
.cle-05__rise:focus-visible {
  background-position: 0 100%;
}

.cle-05__wave {
  background-color: var(--ink);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 90 100' preserveAspectRatio='none'%3E%3Cpath d='M0 51 Q11.25 44 22.5 51 T45 51 T67.5 51 T90 51 V101 H0 Z' fill='%230284c7'/%3E%3C/svg%3E");
  background-size: 90px 200%;
  background-position: 0 0;
  transition: background-position .8s cubic-bezier(.34,1.3,.4,1);
}

.cle-05__wave:hover,
.cle-05__wave:focus-visible {
  background-position: 0 100%;
}

.cle-05__flow {
  background-image: repeating-linear-gradient(100deg,oklch(0.58 0.14 230) 0,oklch(0.6 0.19 300) 70px,oklch(0.72 0.17 60) 140px,oklch(0.58 0.14 230) 210px);
  background-size: 210px 100%;
  animation: clh05-flow 2.2s linear infinite paused;
}

.cle-05__flow:hover,
.cle-05__flow:focus-visible {
  animation-play-state: running;
}

@keyframes clh05-flow {
  to {
    background-position: -210px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-05 * {
    transition-duration: .01s !important;
    animation: none !important;
  }
}
```
