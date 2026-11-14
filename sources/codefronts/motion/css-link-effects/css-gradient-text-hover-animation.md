---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-gradient-text-hover-animation/"
title: "CSS Gradient Text Hover Animation"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Three ways to pour a gradient into link text on hover: a solid-to-gradient slide driven by background-position, a rotating gradient angle animated with…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text Hover Animation
Source: https://codefronts.com/motion/css-link-effects/css-gradient-text-hover-animation/

Three ways to pour a gradient into link text on hover: a solid-to-gradient slide driven by background-position, a rotating gradient angle animated with @property (the modern trick — gradient angles aren't animatable without it), and a light shimmer that sweeps across the letters while hovered. All real, selectable text via background-clip: text.
## HTML
```html
<section class="cle-02" aria-label="Gradient text hover demo">
  <div class="cle-02__stage">
    <div class="cle-02__var"><a href="#a" class="cle-02__slide">Design systems</a><small class="cle-02__cap">A · solid → gradient slide</small></div>
    <div class="cle-02__var"><a href="#b" class="cle-02__spin">Motion studio</a><small class="cle-02__cap">B · @property angle spin</small></div>
    <div class="cle-02__var"><a href="#c" class="cle-02__shine">Case studies</a><small class="cle-02__cap">C · shimmer while hovered</small></div>
  </div>
</section>
```
## CSS
```css
.cle-02,
.cle-02 *,
.cle-02 *::before,
.cle-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --clh02-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 135deg;
}

.cle-02 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.22 0.02 280);
  --g1: oklch(0.62 0.25 335);
  --g2: oklch(0.55 0.24 280);
  --g3: oklch(0.7 0.17 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-02__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 44px;
  border: 1px solid oklch(0.9 0.015 300);
  background: radial-gradient(120% 140% at 15% 0%,oklch(0.97 0.02 335 / .6),transparent 45%),radial-gradient(120% 140% at 90% 100%,oklch(0.96 0.025 200 / .7),transparent 45%),oklch(0.99 0.004 300);
  padding: 44px 32px;
}

.cle-02__var {
  display: grid;
  gap: 12px;
  justify-items: center;
}

.cle-02__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 300);
}

.cle-02 a {
  font-size: clamp(30px,5vw,44px);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.15;
  text-decoration: none;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}

.cle-02 a::selection {
  background: oklch(0.85 0.08 280 / .5);
  color: var(--ink);
  -webkit-text-fill-color: var(--ink);
}

.cle-02 a:focus-visible {
  outline: 3px solid var(--g2);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-02__slide {
  background-image: linear-gradient(90deg,var(--ink) 0 32%,var(--g1) 46%,var(--g2) 62%,var(--g3) 80%);
  background-size: 300% 100%;
  background-position: 0% 0;
  transition: background-position .6s cubic-bezier(.3,.7,.2,1);
}

.cle-02__slide:hover,
.cle-02__slide:focus-visible {
  background-position: 100% 0;
}

.cle-02__spin {
  background-image: linear-gradient(var(--clh02-a),var(--g2),var(--g1) 55%,var(--g3));
  transition: --clh02-a .7s cubic-bezier(.4,0,.2,1);
}

.cle-02__spin:hover,
.cle-02__spin:focus-visible {
  --clh02-a: 495deg;
}

.cle-02__shine {
  background-image: linear-gradient(115deg,transparent 0 42%,oklch(1 0 0 / .95) 50%,transparent 58% 100%),linear-gradient(100deg,var(--g2),var(--g1) 50%,var(--g3));
  background-size: 250% 100%,100% 100%;
  background-position: 230% 0,0 0;
}

.cle-02__shine:hover,
.cle-02__shine:focus-visible {
  animation: clh02-shimmer 1.4s ease-in-out infinite;
}

@keyframes clh02-shimmer {
  from {
    background-position: 230% 0,0 0;
  }

  to {
    background-position: -130% 0,0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-02 * {
    transition-duration: .01s !important;
    animation: none !important;
  }
}
```
