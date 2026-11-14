---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/gradient-border-glow-card/"
title: "Gradient Border Glow Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Dark card wrapped in a slowly rotating conic-gradient border with an outer bloom halo. Reduced-motion freezes the spin."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border Glow Card
Source: https://codefronts.com/components/css-cards/gradient-border-glow-card/

Dark card wrapped in a slowly rotating conic-gradient border with an outer bloom halo. Reduced-motion freezes the spin.
## HTML
```html
<section class="card-18">
  <div class="card-18__stage" aria-hidden="true">
    <div class="card-18__stars"></div>
    <div class="card-18__mesh"></div>
  </div>

  <article class="card-18__card">
    <div class="card-18__particles" aria-hidden="true">
      <span class="card-18__particle card-18__particle--1"></span>
      <span class="card-18__particle card-18__particle--2"></span>
      <span class="card-18__particle card-18__particle--3"></span>
      <span class="card-18__particle card-18__particle--4"></span>
      <span class="card-18__particle card-18__particle--5"></span>
    </div>

    <div class="card-18__inner">
      <header class="card-18__head">
        <div class="card-18__brand">
          <span class="card-18__brand-orb" aria-hidden="true"></span>
          <span class="card-18__brand-text">nova/generate</span>
          <span class="card-18__branch">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9v3a3 3 0 0 1-3 3H9"/></svg>
            main
          </span>
        </div>
        <div class="card-18__controls">
          <span class="card-18__dot card-18__dot--r"></span>
          <span class="card-18__dot card-18__dot--y"></span>
          <span class="card-18__dot card-18__dot--g"></span>
        </div>
      </header>

      <div class="card-18__body">
        <div class="card-18__terminal">
          <div class="card-18__line">
            <span class="card-18__prompt">$</span>
            <span class="card-18__cmd">nova generate <span class="card-18__cmd-flag">--style</span> <span class="card-18__cmd-val">"van gogh"</span></span>
          </div>
          <div class="card-18__line card-18__line--out">
            <span class="card-18__spinner" aria-hidden="true"></span>
            <span class="card-18__out">Loading diffusion model <span class="card-18__mono">nova-v4-turbo</span></span>
          </div>
          <div class="card-18__line card-18__line--out">
            <span class="card-18__tick" aria-hidden="true">
              <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            <span class="card-18__out card-18__out--done">12 styles ready in <span class="card-18__mono card-18__mono--hot">2.4s</span></span>
          </div>
          <div class="card-18__line card-18__line--cursor">
            <span class="card-18__prompt">$</span>
            <span class="card-18__caret" aria-hidden="true"></span>
          </div>
        </div>

        <div class="card-18__chips">
          <span class="card-18__chip">
            <span class="card-18__chip-dot" aria-hidden="true"></span>
            NEURAL v4
          </span>
          <span class="card-18__chip card-18__chip--alt">4K OUTPUT</span>
          <span class="card-18__chip card-18__chip--alt">MIT</span>
        </div>

        <h3 class="card-18__title">Neural Style Transfer</h3>
        <p class="card-18__desc">Diffusion models trained on 12 curated art movements. Brush-level control, in the terminal or on the canvas.</p>

        <div class="card-18__ctas">
          <a class="card-18__cta card-18__cta--primary" href="#try">
            <span class="card-18__cta-glow" aria-hidden="true"></span>
            <span class="card-18__cta-label">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              Try nova free
            </span>
            <span class="card-18__cta-arrow" aria-hidden="true">→</span>
          </a>
          <a class="card-18__cta card-18__cta--ghost" href="#docs">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            Docs
          </a>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-18 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: #050510;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #a5f3fc;
  --p-hot: #ff2d92;
  --p-cyan: #22d3ee;
  --p-lime: #a3ff5f;
  --code: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  overflow: hidden;
}

.card-18 *,
.card-18 *::before,
.card-18 *::after {
  box-sizing: border-box;
}
/* ── stage ── */

.card-18__stage {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-18__stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1px 1px at 15% 25%, rgba(255,255,255,0.5) 50%, transparent), radial-gradient(1px 1px at 78% 40%, rgba(255,255,255,0.6) 50%, transparent), radial-gradient(1px 1px at 42% 78%, rgba(255,255,255,0.4) 50%, transparent), radial-gradient(1.5px 1.5px at 25% 60%, rgba(255,255,255,0.4) 50%, transparent), radial-gradient(1px 1px at 62% 20%, rgba(255,255,255,0.5) 50%, transparent), radial-gradient(1px 1px at 5% 90%, rgba(255,255,255,0.3) 50%, transparent), radial-gradient(1px 1px at 95% 55%, rgba(255,255,255,0.4) 50%, transparent);
}

.card-18__mesh {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 800px;
  height: 800px;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 30% 30%, rgba(255, 45, 146, 0.16) 0%, transparent 45%), radial-gradient(circle at 70% 70%, rgba(34, 211, 238, 0.14) 0%, transparent 45%);
  filter: blur(60px);
}
/* ── card: terminal/console panel with animated laser border ── */

.card-18__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 400px;
  border-radius: 16px;
  isolation: isolate;
  overflow: hidden;
  padding: 1.5px;
  background: conic-gradient(from var(--angle, 0deg),
        transparent 0deg,
        var(--p-hot) 6deg,
        transparent 26deg,
        transparent 180deg,
        var(--p-cyan) 186deg,
        transparent 206deg,
        transparent 360deg);
  animation: card-18-arc 4s linear infinite;
  box-shadow: 0 30px 60px -20px rgba(0, 0, 0, 0.8), 0 20px 40px -20px rgba(255, 45, 146, 0.25);
  transition: transform 0.5s cubic-bezier(0.34, 1.2, 0.64, 1), box-shadow 0.5s;
}

.card-18__card::before {
  content: '';
  position: absolute;
  inset: 1.5px;
  border-radius: 14.5px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.03) 0%, transparent 30%), linear-gradient(160deg, #0d0d16 0%, #12121e 100%);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
  z-index: 0;
}

.card-18__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -20px rgba(0, 0, 0, 0.9), 0 28px 50px -20px rgba(255, 45, 146, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.12);
}
/* laser border on the card itself via padding + conic-gradient background */
/* particles rising from below (visible on hover) */

.card-18__particles {
  position: absolute;
  inset: 1.5px;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.4s;
  overflow: hidden;
  border-radius: 14.5px;
  z-index: 3;
}

.card-18__card:hover .card-18__particles {
  opacity: 1;
}

.card-18__particle {
  position: absolute;
  bottom: 0;
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--p-cyan);
  box-shadow: 0 0 8px currentColor;
  color: var(--p-cyan);
  animation: card-18-rise 3.5s ease-in-out infinite;
}

.card-18__particle--1 {
  left: 20%;
  animation-delay: 0s;
  color: var(--p-hot);
  background: var(--p-hot);
}

.card-18__particle--2 {
  left: 35%;
  animation-delay: 0.6s;
}

.card-18__particle--3 {
  left: 55%;
  animation-delay: 1.2s;
  color: var(--p-hot);
  background: var(--p-hot);
}

.card-18__particle--4 {
  left: 72%;
  animation-delay: 1.8s;
  color: var(--p-lime);
  background: var(--p-lime);
}

.card-18__particle--5 {
  left: 88%;
  animation-delay: 2.4s;
}

.card-18__inner {
  position: relative;
  z-index: 2;
  padding: 16px 18px 20px;
  color: #f4f4fb;
}
/* ── head: brand + traffic dots ── */

.card-18__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  margin-bottom: 14px;
}

.card-18__brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-18__brand-orb {
  position: relative;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #ff6bb1 0%, #ff2d92 40%, #7a1148 80%);
  box-shadow: 0 0 10px rgba(255, 45, 146, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.card-18__brand-text {
  font-family: var(--code);
  font-size: 12px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.85);
  letter-spacing: -0.005em;
}

.card-18__branch {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: var(--code);
  font-size: 10px;
  font-weight: 700;
  color: rgba(163, 255, 95, 0.85);
  padding: 2px 6px;
  background: rgba(163, 255, 95, 0.08);
  border: 1px solid rgba(163, 255, 95, 0.2);
  border-radius: 4px;
}

.card-18__controls {
  display: flex;
  gap: 5px;
}

.card-18__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.25);
}

.card-18__dot--r {
  background: #ff5f57;
}

.card-18__dot--y {
  background: #febc2e;
}

.card-18__dot--g {
  background: #28c840;
}
/* ── terminal ── */

.card-18__terminal {
  padding: 12px 12px;
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 10px;
  margin-bottom: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-family: var(--code);
  font-size: 11.5px;
  line-height: 1.5;
}

.card-18__line {
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-18__prompt {
  color: var(--p-hot);
  font-weight: 800;
}

.card-18__cmd {
  color: rgba(255, 255, 255, 0.92);
  letter-spacing: -0.005em;
}

.card-18__cmd-flag {
  color: var(--p-cyan);
}

.card-18__cmd-val {
  color: var(--p-lime);
}

.card-18__line--out {
  color: rgba(255, 255, 255, 0.55);
  padding-left: 2px;
}

.card-18__out {
  letter-spacing: -0.005em;
}

.card-18__out--done {
  color: rgba(255, 255, 255, 0.85);
}

.card-18__mono {
  color: var(--p-cyan);
}

.card-18__mono--hot {
  color: var(--p-hot);
  font-weight: 700;
}

.card-18__spinner {
  display: inline-block;
  width: 9px;
  height: 9px;
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  border-top-color: var(--p-cyan);
  border-radius: 50%;
  animation: card-18-spin 0.8s linear infinite;
}

.card-18__tick {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 12px;
  height: 12px;
  color: var(--p-lime);
}

.card-18__caret {
  display: inline-block;
  width: 7px;
  height: 13px;
  background: rgba(255, 255, 255, 0.85);
  animation: card-18-blink 1s step-end infinite;
}
/* ── chips row ── */

.card-18__chips {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

.card-18__chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: var(--code);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: var(--p-hot);
  padding: 3px 8px;
  background: rgba(255, 45, 146, 0.10);
  border: 1px solid rgba(255, 45, 146, 0.24);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-18__chip-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--p-hot);
  box-shadow: 0 0 6px currentColor;
  color: var(--p-hot);
  animation: card-18-pulse 2s ease-in-out infinite;
}

.card-18__chip--alt {
  color: rgba(255, 255, 255, 0.65);
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.10);
}
/* ── title + desc ── */

.card-18__title {
  font-size: 20px;
  font-weight: 800;
  color: #fff;
  margin: 0 0 6px;
  letter-spacing: -0.02em;
  line-height: 1.15;
  background: linear-gradient(135deg, #ffffff 0%, #ffb3d9 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-18__desc {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.6);
  margin: 0 0 16px;
  line-height: 1.55;
  letter-spacing: -0.005em;
}
/* ── CTAs ── */

.card-18__ctas {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 6px;
}

.card-18__cta {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 42px;
  padding: 10px 18px;
  border-radius: 12px;
  font: 700 12.5px 'Inter', sans-serif;
  text-decoration: none;
  letter-spacing: -0.01em;
  transition: transform 0.2s, box-shadow 0.2s;
  overflow: hidden;
  isolation: isolate;
}

.card-18__cta--primary {
  background: linear-gradient(180deg, #ff5cb1 0%, #ff2d92 100%);
  color: #12001a;
  box-shadow: 0 4px 12px rgba(255, 45, 146, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.14) inset, 0 -1px 0 rgba(122, 17, 72, 0.4) inset;
}

.card-18__cta--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 22px rgba(255, 45, 146, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.24) inset, 0 -1px 0 rgba(122, 17, 72, 0.4) inset;
}

.card-18__cta-label {
  position: relative;
  z-index: 2;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.card-18__cta-arrow {
  position: relative;
  z-index: 2;
  margin-left: 6px;
  transition: transform 0.2s;
}

.card-18__cta--primary:hover .card-18__cta-arrow {
  transform: translateX(4px);
}

.card-18__cta-glow {
  position: absolute;
  inset: -30px;
  background: radial-gradient(circle at center, rgba(255, 45, 146, 0.7) 0%, transparent 60%);
  filter: blur(12px);
  opacity: 0;
  transition: opacity 0.3s;
  z-index: 0;
}

.card-18__cta--primary:hover .card-18__cta-glow {
  opacity: 1;
}

.card-18__cta--ghost {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.04);
  color: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.10);
}

.card-18__cta--ghost:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
}

.card-18__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-18-arc {
  0% {
    --angle: 0deg;
  }

  100% {
    --angle: 360deg;
  }
}

@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@keyframes card-18-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes card-18-blink {
  50% {
    opacity: 0;
  }
}

@keyframes card-18-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.5;
  }
}

@keyframes card-18-rise {
  0% {
    bottom: 0;
    opacity: 0;
    transform: translateX(0);
  }

  15% {
    opacity: 1;
  }

  100% {
    bottom: 100%;
    opacity: 0;
    transform: translateX(20px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-18__border,
    .card-18__spinner,
    .card-18__caret,
    .card-18__particle,
    .card-18__chip-dot {
    animation: none;
  }

  .card-18__card,
    .card-18__cta,
    .card-18__cta-arrow,
    .card-18__cta-glow,
    .card-18__particles {
    transition: none;
  }

  .card-18__card:hover {
    transform: none;
  }

  .card-18__cta--primary:hover {
    transform: none;
  }

  .card-18__cta--primary:hover .card-18__cta-arrow {
    transform: none;
  }

  .card-18__caret {
    background: rgba(255, 255, 255, 0.5);
  }
}
```
