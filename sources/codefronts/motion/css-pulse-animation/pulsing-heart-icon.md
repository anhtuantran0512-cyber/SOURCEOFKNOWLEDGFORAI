---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/pulsing-heart-icon/"
title: "Pulsing Heart Icon"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A wishlist / save-for-later heart button on a product card — the heart pulses with a natural cardiac rhythm (not a mechanical scale), giving the interaction…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulsing Heart Icon
Source: https://codefronts.com/motion/css-pulse-animation/pulsing-heart-icon/

A wishlist / save-for-later heart button on a product card — the heart pulses with a natural cardiac rhythm (not a mechanical scale), giving the interaction warmth and personality. Warm pink card (#fecaca to #fff1f2) with crimson heart (#dc2626) and a small saved-count badge. Pinterest / Airbnb / Instagram save button aesthetic. The keyframe uses cardiac timing (0% → 20% quick scale-up → 40% pull-back → 60% settle) that mimics a real heartbeat's systole-diastole rhythm — the reason this pattern feels alive, not robotic.
## HTML
```html
<div class="pl-14">
  <article class="pl-14__card">
    <div class="pl-14__image" role="img" aria-label="Artisan hand-poured soy candle, verbena and cedarwood">
      <span aria-hidden="true">🕯️</span>
    </div>
    <button class="pl-14__save" data-saved="true" aria-label="Saved · 3,200 people saved this" aria-pressed="true">
      <svg class="pl-14__heart" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
        <path d="M12 21s-8-4.5-8-11a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6.5-8 11-8 11H12z"/>
      </svg>
    </button>
    <div class="pl-14__details">
      <p class="pl-14__brand">Rowan &amp; Poppy</p>
      <h3 class="pl-14__name">Verbena, cedarwood &amp; sea salt</h3>
      <p class="pl-14__price">
        <span>$42</span>
        <span class="pl-14__unit">· 8oz hand-poured soy candle</span>
      </p>
      <p class="pl-14__saved">
        <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor" aria-hidden="true">
          <path d="M12 21s-8-4.5-8-11a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6.5-8 11-8 11H12z"/>
        </svg>
        <strong>3,247</strong> saved · <strong>412</strong> in the last week
      </p>
    </div>
  </article>
</div>
```
## CSS
```css
.pl-14 {
  --page-bg: #fdf2f8;
  --card-a: #fff1f2;
  --card-b: #fecaca;
  --ink: #4c0519;
  --sub: #8b5a68;
  --brand: #dc2626;
  --brand-soft: rgba(220,38,38,.35);
  --gold: #a67c3a;
  --line: #fecdd3;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(70% 90% at 30% 20%, rgba(254,205,211,.6) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.pl-14 *,
.pl-14 *::before,
.pl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-14 ::selection {
  background: var(--brand);
  color: #fff;
}

.pl-14__card {
  position: relative;
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 22px;
  width: min(560px,100%);
  padding: 22px;
  border-radius: 16px;
  background: linear-gradient(135deg,var(--card-a) 0%,var(--card-b) 100%);
  border: 1px solid rgba(220,38,38,.15);
  box-shadow: 0 20px 40px -20px rgba(76,5,25,.25);
}

@media (max-width: 520px) {
  .pl-14__card {
    grid-template-columns: 1fr;
  }
}

.pl-14__image {
  aspect-ratio: 1/1;
  border-radius: 11px;
  background: linear-gradient(135deg,#f9a8d4,#ec4899 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 76px;
  box-shadow: inset 0 0 40px rgba(76,5,25,.15);
}
/* Save button pinned to card top-right */

.pl-14__save {
  position: absolute;
  top: 14px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 50%;
  background: rgba(255,255,255,.9);
  color: var(--brand);
  cursor: pointer;
  box-shadow: 0 4px 12px -4px rgba(76,5,25,.25);
  backdrop-filter: blur(4px);
  transition: background .15s ease,transform .12s ease;
}

.pl-14__save:hover {
  background: #fff;
  transform: translateY(-1px);
}

.pl-14__save:active {
  transform: translateY(1px);
}

.pl-14__save:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}
/* Glow ring behind heart — scales with heartbeat */

.pl-14__save::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--brand-soft);
  pointer-events: none;
  animation: pl-14-glow 1.6s ease-in-out infinite;
  z-index: 0;
}

.pl-14__heart {
  position: relative;
  z-index: 1;
  animation: pl-14-heart 1.6s ease-in-out infinite;
  transform-origin: center;
}
/* Cardiac rhythm — hand-tuned keyframe mimics QRS complex */

@keyframes pl-14-heart {
  0% {
    transform: scale(1);
  }

  15% {
    transform: scale(1.22);
  }

  30% {
    transform: scale(1.05);
  }

  45% {
    transform: scale(1.15);
  }

  60% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes pl-14-glow {
  0% {
    transform: scale(1);
    opacity: .5;
  }

  15% {
    transform: scale(1.5);
    opacity: 0;
  }

  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

.pl-14__details {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.pl-14__brand {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--gold);
}

.pl-14__name {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  color: var(--ink);
  margin-bottom: 2px;
}

.pl-14__price {
  font-size: .85rem;
  font-weight: 700;
  color: var(--ink);
}

.pl-14__price > span:first-child {
  color: var(--brand);
  font-size: 1.05rem;
}

.pl-14__unit {
  color: var(--sub);
  font-weight: 500;
}

.pl-14__saved {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: .75rem;
  color: var(--sub);
  margin-top: auto;
  padding-top: 8px;
  border-top: 1px solid var(--line);
}

.pl-14__saved svg {
  color: var(--brand);
}

.pl-14__saved strong {
  color: var(--ink);
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .pl-14__heart,
    .pl-14__save::before {
    animation: none!important;
    transform: none!important;
    opacity: 0!important;
  }

  .pl-14__save::before {
    display: none!important;
  }
}
```
