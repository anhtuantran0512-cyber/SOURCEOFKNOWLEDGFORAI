---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/sketch-dividers/"
title: "Hand-Drawn Doodle SVG Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "A wobbly marker line that draws itself when it scrolls into view — the signature move of personal blogs and illustrated portfolios."
has_js: "true"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hand-Drawn Doodle SVG Divider CSS
Source: https://codefronts.com/snippets/css-dividers/sketch-dividers/

A wobbly marker line that draws itself when it scrolls into view — the signature move of personal blogs and illustrated portfolios. The path is deliberately imperfect, the stroke uses a round cap and a slight rotation so it never looks machined, and an IntersectionObserver measures the real path length with getTotalLength() so the animation is exact regardless of how you edit the curve.
## HTML
```html
<section class="div-26" aria-label="Hand-drawn doodle SVG divider demo">
  <div class="div-26__stage" id="div-26-stage">
    <p class="div-26__eyebrow">getTotalLength() · IntersectionObserver</p>
    <h2 class="div-26__title">Drawn, not rendered</h2>
    <div class="div-26__doodle" aria-hidden="true">
      <svg viewBox="0 0 540 46" fill="none" focusable="false">
        <path class="div-26__ghost" d="M14 30C74 12 118 38 176 24S296 8 350 26s112 2 176-8" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>
        <path class="div-26__ink" d="M12 27C72 9 116 35 174 21S294 5 348 23s112 2 178-9" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <p class="div-26__sub">Two overlapping strokes, a round nib, and six tenths of a degree of tilt. That is the entire recipe for &ldquo;hand-made&rdquo;.</p>
    <div class="div-26__doodle div-26__doodle--sm" aria-hidden="true">
      <svg viewBox="0 0 300 30" fill="none" focusable="false">
        <path class="div-26__ink" d="M10 18c26-11 44 8 68-1s40-9 62 2 46 4 70-6 44 7 68-2" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      </svg>
    </div>
    <p class="div-26__chip">stroke-dashoffset · round linecap · rotate(-0.6deg)</p>
  </div>
</section>
```
## CSS
```css
.div-26 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-26-bg);
  --div-26-bg: oklch(0.975 0.016 95);
  --div-26-ink: oklch(0.26 0.03 55);
  --div-26-mut: oklch(0.54 0.03 55);
  --div-26-acc: oklch(0.58 0.16 250);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-26-ink);
}

.div-26 *,
.div-26 *::before,
.div-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-26__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,3vw,28px);
  text-align: center;
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(100% 70% at 50% 0%,oklch(0.995 0.01 95),transparent);
}

.div-26__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--div-26-acc);
}

.div-26__title {
  font-family: Georgia,'Iowan Old Style',serif;
  font-size: clamp(30px,6.2vw,58px);
  line-height: 1.04;
  letter-spacing: -.02em;
  font-weight: 400;
}

.div-26__doodle {
  width: min(92vw,540px);
  line-height: 0;
  color: var(--div-26-acc);
  rotate: -.6deg;
}

.div-26__doodle--sm {
  width: min(64vw,300px);
  rotate: .5deg;
  opacity: .65;
}

.div-26__doodle svg {
  width: 100%;
  height: auto;
  display: block;
  overflow: visible;
}

.div-26__ink,
.div-26__ghost {
  vector-effect: non-scaling-stroke;
  stroke-dasharray: var(--div-26-len,600);
  stroke-dashoffset: var(--div-26-len,600);
}

.div-26__ghost {
  opacity: .22;
}

.div-26 .is-drawn .div-26__ink {
  animation: div-26-draw 1.5s cubic-bezier(.35,.6,.35,1) forwards;
}

.div-26 .is-drawn .div-26__ghost {
  animation: div-26-draw 1.7s cubic-bezier(.35,.6,.35,1) .08s forwards;
}

@keyframes div-26-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.div-26__sub {
  max-width: 44ch;
  font-size: clamp(14px,1.85vw,17.5px);
  line-height: 1.65;
  color: var(--div-26-mut);
  text-wrap: pretty;
}

.div-26__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-26-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.26 0.03 55/.18);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-26__ink,
    .div-26__ghost {
    animation: none !important;
    stroke-dashoffset: 0;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.getElementById('div-26-stage');
  if (!stage || stage.dataset.ppWired) return;
  stage.dataset.ppWired = '1';
  const paths = stage.querySelectorAll('.div-26__ink, .div-26__ghost');
  paths.forEach((p) => {
    const len = Math.ceil(p.getTotalLength() || 600);
    p.style.setProperty('--div-26-len', len);
  });
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)');
  const draw = (el) => el.classList.add('is-drawn');
  if (calm.matches || !('IntersectionObserver' in window)) { draw(stage); return; }
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      draw(e.target);
      obs.unobserve(e.target);
    });
  }, { threshold: 0.25 });
  stage.querySelectorAll('.div-26__doodle').forEach((d) => io.observe(d));
  io.observe(stage);
})();
```
