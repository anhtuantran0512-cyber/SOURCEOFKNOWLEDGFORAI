---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/animated-gradient-border-card-conic-rotate/"
title: "Animated Gradient Border Card (Conic Rotate)"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The rotating neon outline, done three ways so you can pick your compatibility floor: a registered @property angle sweeping a conic gradient, a mask-composite…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Border Card (Conic Rotate)
Source: https://codefronts.com/components/css-animated-cards/animated-gradient-border-card-conic-rotate/

The rotating neon outline, done three ways so you can pick your compatibility floor: a registered @property angle sweeping a conic gradient, a mask-composite ring that keeps the card background transparent, and a padding-box fallback. Includes the glow-bloom variant where a blurred copy of the border sits behind the card.
## HTML
```html
<section class="ac-18" aria-label="Animated conic gradient border card demo">
  <div class="ac-18__stage">
    <div class="ac-18__row">
      <article class="ac-18__card ac-18__card--solid">
        <span class="ac-18__bloom" aria-hidden="true"></span>
        <p class="ac-18__eyebrow">Conic sweep</p>
        <h3 class="ac-18__title">Registered angle</h3>
        <p class="ac-18__copy">A single <code>@property &lt;angle&gt;</code> animated 0 → 360deg behind an opaque card. Cheapest possible route.</p>
        <p class="ac-18__meta">5 s linear · hover to accelerate</p>
      </article>
      <article class="ac-18__card ac-18__card--mask">
        <p class="ac-18__eyebrow">Mask composite</p>
        <h3 class="ac-18__title">True ring</h3>
        <p class="ac-18__copy">Two masks subtracted leave a real 2 px ring, so the card behind it can stay glassy and transparent.</p>
        <p class="ac-18__meta">mask-composite: exclude</p>
      </article>
      <article class="ac-18__card ac-18__card--comet">
        <p class="ac-18__eyebrow">Partial arc</p>
        <h3 class="ac-18__title">Comet trail</h3>
        <p class="ac-18__copy">Transparent stops turn the full sweep into a single travelling highlight — a status indicator that never sits still.</p>
        <p class="ac-18__meta">3.2 s linear · transparent stops</p>
      </article>
    </div>
    <p class="ac-18__chip" aria-hidden="true">@property &lt;angle&gt; · conic-gradient(from var(--a)) · mask-composite ring · blurred bloom copy · seam-free stop list</p>
  </div>
</section>
```
## CSS
```css
@property --ac-18-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.ac-18,
.ac-18 *,
.ac-18 *::before,
.ac-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-18-bg: oklch(0.14 0.016 275);
  --ac-18-card: oklch(0.19 0.018 275);
  --ac-18-ink: oklch(0.97 0.004 280);
  --ac-18-mut: oklch(0.70 0.02 280);
  --ac-18-1: oklch(0.78 0.19 300);
  --ac-18-2: oklch(0.82 0.16 200);
  --ac-18-3: oklch(0.85 0.17 88);
  background: var(--ac-18-bg);
  color: var(--ac-18-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,58px);
}

.ac-18__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(224px,1fr));
  gap: 18px;
  width: min(100%,880px);
}

.ac-18__card {
  position: relative;
  display: grid;
  gap: 9px;
  padding: 24px 22px;
  border-radius: 20px;
  background: var(--ac-18-card);
  isolation: isolate;
}

.ac-18__card::before {
  content: '';
  position: absolute;
  inset: -2px;
  z-index: -2;
  border-radius: 22px;
  background: conic-gradient(from var(--ac-18-a),var(--ac-18-1),var(--ac-18-2),var(--ac-18-3),var(--ac-18-1));
  animation: ac-18-spin 5s linear infinite;
}

.ac-18__card:hover::before {
  animation-duration: 1.6s;
}

@keyframes ac-18-spin {
  to {
    --ac-18-a: 360deg;
  }
}

.ac-18__card--solid::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: 20px;
  background: var(--ac-18-card);
}

.ac-18__bloom {
  position: absolute;
  inset: -6px;
  z-index: -3;
  border-radius: 26px;
  background: conic-gradient(from var(--ac-18-a),var(--ac-18-1),var(--ac-18-2),var(--ac-18-3),var(--ac-18-1));
  filter: blur(16px);
  opacity: .55;
  animation: ac-18-spin 5s linear infinite;
}

.ac-18__card--mask {
  background: oklch(1 0 0/.04);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.ac-18__card--mask::before {
  inset: 0;
  padding: 2px;
  border-radius: 20px;
  background: conic-gradient(from var(--ac-18-a),var(--ac-18-1),var(--ac-18-2),var(--ac-18-3),var(--ac-18-1));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation-duration: 6.5s;
  animation-direction: reverse;
}

.ac-18__card--comet::before {
  background: conic-gradient(from var(--ac-18-a),transparent 0 62%,var(--ac-18-2) 78%,var(--ac-18-1) 92%,transparent 100%);
  animation-duration: 3.2s;
}

.ac-18__card--comet::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: 20px;
  background: var(--ac-18-card);
}

.ac-18__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .17em;
  text-transform: uppercase;
  color: var(--ac-18-2);
}

.ac-18__title {
  font-size: 20px;
  font-weight: 660;
  letter-spacing: -.03em;
}

.ac-18__copy {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--ac-18-mut);
  text-wrap: pretty;
}

.ac-18__copy code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  background: oklch(1 0 0/.08);
  padding: 2px 5px;
  border-radius: 5px;
}

.ac-18__meta {
  margin-top: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--ac-18-mut);
}

.ac-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-18-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,780px);
}

@supports not (background: conic-gradient(from var(--ac-18-a),red,blue)) {
  .ac-18__card::before,
    .ac-18__bloom {
    animation: none;
    background: linear-gradient(120deg,var(--ac-18-1),var(--ac-18-2),var(--ac-18-3));
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-18__card::before,
    .ac-18__bloom {
    animation: none;
  }

  .ac-18__card:hover::before {
    animation: none;
  }
}
```
