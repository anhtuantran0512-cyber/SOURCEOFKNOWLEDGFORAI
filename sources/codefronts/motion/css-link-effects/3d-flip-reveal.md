---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/3d-flip-reveal/"
title: "CSS 3D Text Flip Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Text with a physical edge: hover rolls the label 90° like the face of a cube, revealing an accent copy that was hiding on top."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Text Flip Hover Effect
Source: https://codefronts.com/motion/css-link-effects/3d-flip-reveal/

Text with a physical edge: hover rolls the label 90° like the face of a cube, revealing an accent copy that was hiding on top. One word rolling whole, a per-letter cascade that ripples across the label 50ms at a time, and a hinge variant that swings down a translation ('Hello' → 'Bonjour'). Real perspective, two text nodes, zero JS.
## HTML
```html
<section class="cle-25" aria-label="3D text flip hover demo">
  <div class="cle-25__stage">
    <div class="cle-25__var"><a href="#a" class="cle-25__flip"><span class="cle-25__box" data-text="Portfolio"><span class="cle-25__f">Portfolio</span></span></a><small class="cle-25__cap">A · whole-word roll</small></div>
    <div class="cle-25__var">
      <a href="#b" class="cle-25__cascade" aria-label="Showreel"><span class="cle-25__w" aria-hidden="true"><span class="cle-25__box" data-text="S" style="--i:0"><span class="cle-25__f">S</span></span><span class="cle-25__box" data-text="H" style="--i:1"><span class="cle-25__f">H</span></span><span class="cle-25__box" data-text="O" style="--i:2"><span class="cle-25__f">O</span></span><span class="cle-25__box" data-text="W" style="--i:3"><span class="cle-25__f">W</span></span><span class="cle-25__box" data-text="R" style="--i:4"><span class="cle-25__f">R</span></span><span class="cle-25__box" data-text="E" style="--i:5"><span class="cle-25__f">E</span></span><span class="cle-25__box" data-text="E" style="--i:6"><span class="cle-25__f">E</span></span><span class="cle-25__box" data-text="L" style="--i:7"><span class="cle-25__f">L</span></span></span></a>
      <small class="cle-25__cap">B · per-letter cascade</small>
    </div>
    <div class="cle-25__var"><a href="#c" class="cle-25__hinge"><span class="cle-25__h1">Hello</span><span class="cle-25__h2" aria-hidden="true">Bonjour</span></a><small class="cle-25__cap">C · hinge swap</small></div>
  </div>
</section>
```
## CSS
```css
.cle-25,
.cle-25 *,
.cle-25 *::before,
.cle-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-25 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.93 0.01 80);
  --accent: oklch(0.8 0.16 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-25__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 52px;
  background: linear-gradient(170deg,oklch(0.26 0.02 60),oklch(0.18 0.015 50));
  padding: 44px 32px;
}

.cle-25__var {
  display: grid;
  gap: 15px;
  justify-items: center;
}

.cle-25__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.6 0.04 70);
}

.cle-25 a {
  display: inline-block;
  perspective: 600px;
  color: var(--ink);
  text-decoration: none;
  font-size: clamp(28px,4.4vw,40px);
  font-weight: 800;
  letter-spacing: -.01em;
  line-height: 1.1;
}

.cle-25 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 8px;
  border-radius: 4px;
}

.cle-25__box {
  position: relative;
  display: inline-block;
  transform-style: preserve-3d;
  transition: transform .5s cubic-bezier(.35,1.2,.35,1);
}

.cle-25__f {
  display: inline-block;
  transform: translateZ(.55em);
  opacity: 1;
  transition: opacity .2s .12s;
}

.cle-25__box::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--accent);
  transform: rotateX(90deg) translateZ(.55em);
  opacity: 0;
  transition: opacity .2s .12s;
}

.cle-25__flip:hover .cle-25__box::before,
.cle-25__flip:focus-visible .cle-25__box::before,
.cle-25__cascade:hover .cle-25__box::before,
.cle-25__cascade:focus-visible .cle-25__box::before {
  opacity: 1;
}

.cle-25__flip:hover .cle-25__f,
.cle-25__flip:focus-visible .cle-25__f,
.cle-25__cascade:hover .cle-25__f,
.cle-25__cascade:focus-visible .cle-25__f {
  opacity: 0;
}

.cle-25__cascade .cle-25__box::before,
.cle-25__cascade .cle-25__f {
  transition-delay: calc(var(--i) * 50ms + 120ms);
}

.cle-25__flip:hover .cle-25__box,
.cle-25__flip:focus-visible .cle-25__box {
  transform: rotateX(-90deg);
}

.cle-25__cascade .cle-25__w {
  display: inline-block;
  letter-spacing: .05em;
}

.cle-25__cascade .cle-25__box {
  transition-delay: calc(var(--i) * 50ms);
}

.cle-25__cascade:hover .cle-25__box,
.cle-25__cascade:focus-visible .cle-25__box {
  transform: rotateX(-90deg);
}

.cle-25__hinge {
  display: inline-grid;
}

.cle-25__hinge > span {
  grid-area: 1/1;
  display: inline-block;
  backface-visibility: hidden;
  transition: transform .45s cubic-bezier(.35,1.1,.35,1),opacity .3s;
}

.cle-25__h1 {
  transform-origin: 50% 0;
  transform: rotateX(0);
}

.cle-25__h2 {
  color: var(--accent);
  transform-origin: 50% 100%;
  transform: rotateX(-90deg);
  opacity: 0;
}

.cle-25__hinge:hover .cle-25__h1,
.cle-25__hinge:focus-visible .cle-25__h1 {
  transform: rotateX(90deg);
  opacity: 0;
}

.cle-25__hinge:hover .cle-25__h2,
.cle-25__hinge:focus-visible .cle-25__h2 {
  transform: rotateX(0);
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cle-25 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
