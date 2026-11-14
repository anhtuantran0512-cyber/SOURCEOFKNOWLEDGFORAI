---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/add-to-cart-hover-pulse/"
title: "Add to Cart Hover Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "An artisan e-commerce product card with an Add-to-Cart button that pulses continuously while the pointer is hovering — a hover-gated micro-interaction…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add to Cart Hover Pulse
Source: https://codefronts.com/motion/css-pulse-animation/add-to-cart-hover-pulse/

An artisan e-commerce product card with an Add-to-Cart button that pulses continuously while the pointer is hovering — a hover-gated micro-interaction confirming interactive readiness without the always-on infinite pulse of standalone CTAs. Cream #fdf6e3 + forest green #166534 palette (Everlane / Allbirds / artisan e-commerce convention) with Playfair Display serif product name. Hover-triggered means resting state is calm; pulse activates only when the user signals intent by hovering, and continues for as long as the pointer stays.
## HTML
```html
<div class="pl-04">
  <article class="pl-04__card">
    <div class="pl-04__image" role="img" aria-label="Terra Runner leather crossbody, camel">
      <span aria-hidden="true">👜</span>
    </div>
    <div class="pl-04__details">
      <p class="pl-04__brand">Terra Studio</p>
      <h3 class="pl-04__name">Everyday Crossbody</h3>
      <p class="pl-04__price">
        <span>$128</span>
        <span class="pl-04__was">$168</span>
      </p>
      <p class="pl-04__desc">Vegetable-tanned leather · Fits a 13-inch laptop.</p>
      <button class="pl-04__cta" type="button">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="9" cy="21" r="1"/>
          <circle cx="20" cy="21" r="1"/>
          <path d="M1 1h4l2.7 13.4a2 2 0 002 1.6h9.7a2 2 0 002-1.6L23 6H6"/>
        </svg>
        <span>Add to cart</span>
      </button>
      <p class="pl-04__ship">Free carbon-neutral shipping · Ships in 2 days</p>
    </div>
  </article>
</div>
```
## CSS
```css
.pl-04 {
  --bg: #fdf6e3;
  --paper: #faf1d1;
  --card: #fffcf0;
  --ink: #3a2e1a;
  --sub: #7a6b4e;
  --accent: #166534;
  --accent-dark: #14532d;
  --line: #e8dcb8;
  --gold: #a67c3a;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(70% 80% at 30% 30%, rgba(166,124,58,.05) 0%, transparent 60%), var(--bg);
  color: var(--ink);
}

.pl-04 *,
.pl-04 *::before,
.pl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-04 ::selection {
  background: var(--accent);
  color: var(--card);
}

.pl-04__card {
  display: grid;
  grid-template-columns: 190px 1fr;
  gap: 24px;
  width: min(560px,100%);
  padding: 22px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 20px 40px -20px rgba(58,46,26,.2);
}

@media (max-width: 520px) {
  .pl-04__card {
    grid-template-columns: 1fr;
  }
}

.pl-04__image {
  aspect-ratio: 1/1;
  border-radius: 10px;
  background: linear-gradient(135deg,#e8dcb8,#c9b78c);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 76px;
}

.pl-04__details {
  display: flex;
  flex-direction: column;
}

.pl-04__brand {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 6px;
}

.pl-04__name {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.15;
  color: var(--ink);
  margin-bottom: 8px;
}

.pl-04__price {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 10px;
}

.pl-04__price > span:first-child {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--accent);
}

.pl-04__was {
  font-size: .9rem;
  color: var(--sub);
  text-decoration: line-through;
  font-weight: 500;
}

.pl-04__desc {
  font-size: .82rem;
  color: var(--sub);
  line-height: 1.5;
  margin-bottom: 14px;
}
/* CTA with hover-triggered double-pulse */

.pl-04__cta {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 22px;
  border: none;
  border-radius: 8px;
  background: var(--accent);
  color: var(--card);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 700;
  letter-spacing: -.005em;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
  margin-bottom: 10px;
  z-index: 1;
}

.pl-04__cta > span,
.pl-04__cta svg {
  position: relative;
  z-index: 1;
}

.pl-04__cta:hover {
  background: var(--accent-dark);
  transform: translateY(-1px);
}

.pl-04__cta:active {
  transform: translateY(1px);
}

.pl-04__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
/* Pulse ring defined here (in resting state) but PAUSED — only runs on hover.
   Uses animation-play-state so the timeline pauses when the pointer leaves
   and RESUMES from where it left off on the next hover — no restart flicker.
   Set to infinite so the pulse continues for as long as the user is hovering. */

.pl-04__cta::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 8px;
  pointer-events: none;
  z-index: 0;
  animation: pl-04-pulse .8s ease-out infinite;
  animation-play-state: paused;
}

@media (hover: hover) {
  .pl-04__cta:hover::after {
    animation-play-state: running;
  }
}

@keyframes pl-04-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(22,101,52,.5);
  }

  70% {
    box-shadow: 0 0 0 14px rgba(22,101,52,0);
  }

  100% {
    box-shadow: 0 0 0 14px rgba(22,101,52,0);
  }
}

.pl-04__ship {
  font-size: .72rem;
  color: var(--sub);
  padding-top: 8px;
  border-top: 1px solid var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .pl-04__cta::after {
    animation: none!important;
  }
}
```
