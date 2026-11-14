---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/glitch-split/"
title: "CSS Glitch Text Hover Animation"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Signal corruption on demand: hover and the link splits into magenta/cyan ghosts, horizontal slices tear out of register, and the whole word jitters like a…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitch Text Hover Animation
Source: https://codefronts.com/motion/css-link-effects/glitch-split/

Signal corruption on demand: hover and the link splits into magenta/cyan ghosts, horizontal slices tear out of register, and the whole word jitters like a bad transmission — then snaps pristine the instant you leave. Three intensities: chromatic shift only, slice tearing, and full skew-jitter with a rolling scanline band.
## HTML
```html
<section class="cle-20" aria-label="Glitch text hover demo">
  <div class="cle-20__stage">
    <div class="cle-20__var"><a href="#a" class="cle-20__rgb" data-text="SYSTEM://LOG">SYSTEM://LOG</a><small class="cle-20__cap">A · chromatic split</small></div>
    <div class="cle-20__var"><a href="#b" class="cle-20__slice" data-text="NIGHT_CITY">NIGHT_CITY</a><small class="cle-20__cap">B · slice tear</small></div>
    <div class="cle-20__var"><a href="#c" class="cle-20__full" data-text="ENTER GRID">ENTER GRID</a><small class="cle-20__cap">C · jitter + scanline</small></div>
  </div>
</section>
```
## CSS
```css
.cle-20,
.cle-20 *,
.cle-20 *::before,
.cle-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-20 {
  width: 100%;
  min-height: 100vh;
  --r: oklch(0.65 0.26 350);
  --b: oklch(0.8 0.15 210);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}

.cle-20__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 48px;
  background: linear-gradient(180deg,oklch(0.17 0.02 300),oklch(0.13 0.015 280));
  padding: 44px 32px;
}

.cle-20__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-20__cap {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-20 a {
  position: relative;
  color: oklch(0.93 0.01 300);
  text-decoration: none;
  font-size: clamp(24px,3.4vw,32px);
  font-weight: 700;
  letter-spacing: .08em;
}

.cle-20 a:focus-visible {
  outline: 2px solid var(--b);
  outline-offset: 6px;
}

.cle-20 a::before,
.cle-20 a::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  opacity: 0;
  pointer-events: none;
}

.cle-20 a::before {
  color: var(--r);
  mix-blend-mode: screen;
}

.cle-20 a::after {
  color: var(--b);
  mix-blend-mode: screen;
}

.cle-20__rgb:hover::before,
.cle-20__rgb:focus-visible::before {
  opacity: 1;
  animation: clh20-jitA .3s steps(1,end) infinite;
}

.cle-20__rgb:hover::after,
.cle-20__rgb:focus-visible::after {
  opacity: 1;
  animation: clh20-jitB .3s steps(1,end) infinite;
}

@keyframes clh20-jitA {
  0% {
    translate: -2px -1px;
  }

  50% {
    translate: -3px 1px;
  }

  100% {
    translate: -2px -1px;
  }
}

@keyframes clh20-jitB {
  0% {
    translate: 2px 1px;
  }

  50% {
    translate: 3px -1px;
  }

  100% {
    translate: 2px 1px;
  }
}

.cle-20__slice:hover::before,
.cle-20__slice:focus-visible::before {
  opacity: 1;
  translate: -2px 0;
}

.cle-20__slice:hover::after,
.cle-20__slice:focus-visible::after {
  opacity: 1;
  animation: clh20-slice .55s steps(1,end) infinite;
}

@keyframes clh20-slice {
  0% {
    clip-path: inset(12% 0 78% 0);
    translate: -3px 0;
  }

  25% {
    clip-path: inset(64% 0 22% 0);
    translate: 3px 0;
  }

  50% {
    clip-path: inset(32% 0 56% 0);
    translate: -2px 0;
  }

  75% {
    clip-path: inset(80% 0 6% 0);
    translate: 2px 0;
  }

  100% {
    clip-path: inset(12% 0 78% 0);
    translate: -3px 0;
  }
}

.cle-20__full {
  isolation: isolate;
  overflow: hidden;
  padding: 6px 10px;
}

.cle-20__full::before {
  inset: 6px 10px;
}

.cle-20__full::before {
  inset: 6px 10px;
}

.cle-20__full:hover,
.cle-20__full:focus-visible {
  animation: clh20-skew .5s steps(1,end) infinite;
}

.cle-20__full:hover::before,
.cle-20__full:focus-visible::before {
  opacity: 1;
  animation: clh20-jitA .3s steps(1,end) infinite;
}

.cle-20__full:hover::after,
.cle-20__full:focus-visible::after {
  content: "";
  inset: auto 0;
  height: 22%;
  background: linear-gradient(oklch(1 0 0 / .12),oklch(1 0 0 / .02));
  mix-blend-mode: screen;
  opacity: 1;
  animation: clh20-scan .7s linear infinite;
}

@keyframes clh20-skew {
  0% {
    transform: skewX(0);
  }

  30% {
    transform: skewX(-1.5deg);
  }

  60% {
    transform: skewX(1deg);
  }

  100% {
    transform: skewX(0);
  }
}

@keyframes clh20-scan {
  from {
    top: -24%;
  }

  to {
    top: 104%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-20 a,
    .cle-20 a::before,
    .cle-20 a::after {
    animation: none !important;
  }

  .cle-20 a:hover,
    .cle-20 a:focus-visible {
    color: var(--b);
  }

  .cle-20 a:hover::before,
    .cle-20 a:hover::after {
    opacity: 0;
  }
}
```
