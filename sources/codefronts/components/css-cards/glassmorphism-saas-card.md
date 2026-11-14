---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/glassmorphism-saas-card/"
title: "Glassmorphism SaaS Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Frosted-glass tile on a violet/cyan/magenta aurora backdrop. Rounded icon tile, Premium chip, headline, description, and a gradient-bordered Upgrade CTA."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism SaaS Card
Source: https://codefronts.com/components/css-cards/glassmorphism-saas-card/

Frosted-glass tile on a violet/cyan/magenta aurora backdrop. Rounded icon tile, Premium chip, headline, description, and a gradient-bordered Upgrade CTA.
## HTML
```html
<section class="card-17">
  <div class="card-17__stage" aria-hidden="true">
    <div class="card-17__aurora card-17__aurora--1"></div>
    <div class="card-17__aurora card-17__aurora--2"></div>
    <div class="card-17__aurora card-17__aurora--3"></div>
    <div class="card-17__grain"></div>
    <div class="card-17__caustic"></div>
  </div>

  <article class="card-17__card">
    <div class="card-17__layer card-17__layer--1" aria-hidden="true"></div>
    <div class="card-17__layer card-17__layer--2" aria-hidden="true"></div>

    <div class="card-17__inner">
      <header class="card-17__head">
        <div class="card-17__brand">
          <span class="card-17__brand-mark" aria-hidden="true"></span>
          <span class="card-17__brand-text">
            LUMEN OS
            <span class="card-17__brand-ver">v2.6</span>
          </span>
        </div>
        <button type="button" class="card-17__close" aria-label="Dismiss">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></svg>
        </button>
      </header>

      <div class="card-17__body">
        <div class="card-17__icon-stack" aria-hidden="true">
          <span class="card-17__icon-glow"></span>
          <span class="card-17__icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fef3c7" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v6M12 22v-6M4.93 4.93l4.24 4.24M19.07 19.07l-4.24-4.24M2 12h6M22 12h-6M4.93 19.07l4.24-4.24M19.07 4.93l-4.24 4.24"/></svg>
          </span>
        </div>
        <div class="card-17__badges">
          <span class="card-17__badge card-17__badge--live">
            <span class="card-17__badge-dot" aria-hidden="true"></span>
            LIVE
          </span>
          <span class="card-17__badge">PREMIUM · v2.6</span>
        </div>

        <h3 class="card-17__title">Realtime intelligence, everywhere.</h3>
        <p class="card-17__desc">Custom dashboards, predictive alerts, and voice-driven exports. Deploy across your entire stack in under a minute.</p>

        <dl class="card-17__specs">
          <div class="card-17__spec">
            <dt>Latency</dt>
            <dd>&lt;12ms</dd>
          </div>
          <div class="card-17__spec">
            <dt>Signals</dt>
            <dd>2.4M/s</dd>
          </div>
          <div class="card-17__spec">
            <dt>Uptime</dt>
            <dd>99.99</dd>
          </div>
        </dl>

        <div class="card-17__ctas">
          <a class="card-17__cta card-17__cta--primary" href="#upgrade">
            <span>Upgrade to Pro</span>
            <span class="card-17__cta-arrow" aria-hidden="true">→</span>
          </a>
          <a class="card-17__cta card-17__cta--ghost" href="#learn">
            Watch demo
          </a>
        </div>

        <footer class="card-17__foot">
          <div class="card-17__avatars" aria-hidden="true">
            <span class="card-17__av card-17__av--1">AR</span>
            <span class="card-17__av card-17__av--2">JL</span>
            <span class="card-17__av card-17__av--3">MK</span>
          </div>
          <span class="card-17__foot-text">Trusted by <strong>4,832</strong> teams</span>
        </footer>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-17 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: #0a0710;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #f5d97b;
  --gold: #f5d97b;
  --gold-2: #d4a574;
  --champagne: #fef3c7;
  overflow: hidden;
}

.card-17 *,
.card-17 *::before,
.card-17 *::after {
  box-sizing: border-box;
}
/* ── ambient stage: warm champagne/rose aurora on deep aubergine ── */

.card-17__stage {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-17__aurora {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.5;
  animation: card-17-drift 24s ease-in-out infinite;
}

.card-17__aurora--1 {
  top: -15%;
  left: -10%;
  width: 480px;
  height: 480px;
  background: radial-gradient(circle, #f5d97b, transparent 60%);
}

.card-17__aurora--2 {
  top: 30%;
  right: -20%;
  width: 540px;
  height: 540px;
  background: radial-gradient(circle, #d4718b, transparent 60%);
  animation-delay: -8s;
}

.card-17__aurora--3 {
  bottom: -25%;
  left: 25%;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, #a78bfa, transparent 60%);
  animation-delay: -16s;
}
/* film grain overlay */

.card-17__grain {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle at 15% 25%, rgba(245,217,123,0.06) 0.5px, transparent 1px), radial-gradient(circle at 65% 45%, rgba(212,113,139,0.05) 0.5px, transparent 1px), radial-gradient(circle at 35% 75%, rgba(167,139,250,0.05) 0.5px, transparent 1px), radial-gradient(circle at 85% 85%, rgba(255,255,255,0.04) 0.5px, transparent 1px);
  background-size: 4px 4px, 5px 5px, 3px 3px, 6px 6px;
  mix-blend-mode: overlay;
  opacity: 0.6;
}
/* caustic light shimmer band moving across the stage */

.card-17__caustic {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(115deg,
      transparent 40%,
      rgba(245, 217, 123, 0.05) 47%,
      rgba(255, 255, 255, 0.08) 50%,
      rgba(212, 113, 139, 0.05) 53%,
      transparent 60%);
  animation: card-17-caustic 12s linear infinite;
  mix-blend-mode: screen;
  pointer-events: none;
}
/* ── card: multi-layer refractive glass with chromatic edge ── */

.card-17__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 380px;
  isolation: isolate;
  border-radius: 28px;
  transform: perspective(1200px) rotateX(2deg) rotateY(-2deg);
  transition: transform 0.6s cubic-bezier(0.34, 1.2, 0.64, 1);
}

.card-17__card:hover {
  transform: perspective(1200px) rotateX(0deg) rotateY(0deg) translateY(-4px);
}
/* chromatic edge halo — subtle RGB fringe */

.card-17__card::before {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 30px;
  background: linear-gradient(135deg,
        rgba(245, 217, 123, 0.55) 0%,
        rgba(212, 113, 139, 0.4) 30%,
        rgba(167, 139, 250, 0.4) 60%,
        rgba(245, 217, 123, 0.55) 100%);
  filter: blur(1px);
  opacity: 0.5;
  z-index: -1;
  transition: opacity 0.4s;
}

.card-17__card:hover::before {
  opacity: 0.85;
}
/* outer soft glow bloom */

.card-17__card::after {
  content: '';
  position: absolute;
  inset: -30px;
  border-radius: 55px;
  background: radial-gradient(ellipse, rgba(245, 217, 123, 0.14) 0%, transparent 65%);
  filter: blur(30px);
  z-index: -2;
  pointer-events: none;
}
/* multiple stacked glass layers for depth (visionOS convention) */

.card-17__layer {
  position: absolute;
  inset: 0;
  border-radius: 28px;
  pointer-events: none;
}

.card-17__layer--1 {
  background: linear-gradient(160deg,
        rgba(255, 255, 255, 0.10) 0%,
        rgba(255, 255, 255, 0.02) 40%,
        rgba(255, 255, 255, 0.06) 100%);
  -webkit-backdrop-filter: blur(24px) saturate(1.5) brightness(1.05);
  backdrop-filter: blur(24px) saturate(1.5) brightness(1.05);
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.22), inset 0 -1px 0 rgba(0, 0, 0, 0.14), 0 30px 60px -20px rgba(0, 0, 0, 0.55);
  z-index: 1;
}

.card-17__layer--2 {
  background: radial-gradient(ellipse at 30% 15%, rgba(245, 217, 123, 0.14) 0%, transparent 55%), radial-gradient(ellipse at 80% 90%, rgba(212, 113, 139, 0.10) 0%, transparent 55%);
  z-index: 2;
}

.card-17__inner {
  position: relative;
  z-index: 3;
  padding: 22px 22px 20px;
  color: rgba(255, 255, 255, 0.95);
}
/* ── head: brand + close button ── */

.card-17__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.card-17__brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-17__brand-mark {
  position: relative;
  width: 22px;
  height: 22px;
  border-radius: 7px;
  background: linear-gradient(135deg, #f5d97b 0%, #d4a574 50%, #7c4a3e 100%);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), inset 0 -1px 0 rgba(0, 0, 0, 0.3), 0 3px 8px rgba(212, 165, 116, 0.4);
}

.card-17__brand-mark::after {
  content: '';
  position: absolute;
  inset: 4px;
  border-radius: 3px;
  background: linear-gradient(135deg, transparent 40%, rgba(255, 255, 255, 0.5) 55%, transparent 65%);
}

.card-17__brand-text {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.16em;
  color: rgba(255, 255, 255, 0.9);
  display: inline-flex;
  align-items: baseline;
  gap: 6px;
}

.card-17__brand-ver {
  font-size: 8.5px;
  color: rgba(245, 217, 123, 0.75);
  letter-spacing: 0.10em;
  font-weight: 700;
}

.card-17__close {
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.55);
  cursor: pointer;
  transition: color 0.18s, background 0.18s;
}

.card-17__close:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.10);
}

.card-17__close:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── icon: layered golden orb with glow ── */

.card-17__icon-stack {
  position: relative;
  width: 56px;
  height: 56px;
  margin-bottom: 14px;
}

.card-17__icon-glow {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(245, 217, 123, 0.4) 0%, transparent 65%);
  filter: blur(8px);
  animation: card-17-pulse 3.5s ease-in-out infinite;
}

.card-17__icon {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: radial-gradient(circle at 30% 25%, rgba(255, 255, 255, 0.35) 0%, transparent 50%), linear-gradient(135deg, #f5d97b 0%, #d4a574 60%, #8b5a3c 100%);
  box-shadow: inset 0 2px 0 rgba(255, 255, 255, 0.5), inset 0 -2px 0 rgba(80, 40, 20, 0.4), 0 8px 20px -4px rgba(212, 165, 116, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.12);
}
/* ── badges ── */

.card-17__badges {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

.card-17__badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.16em;
  color: rgba(245, 217, 123, 0.9);
  padding: 3px 8px;
  background: rgba(245, 217, 123, 0.10);
  border: 1px solid rgba(245, 217, 123, 0.25);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-17__badge--live {
  color: #f5d97b;
  background: rgba(255, 255, 255, 0.10);
  border-color: rgba(255, 255, 255, 0.14);
}

.card-17__badge-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #f5d97b;
  box-shadow: 0 0 6px #f5d97b;
  animation: card-17-blink 1.6s ease-in-out infinite;
}
/* ── title + desc ── */

.card-17__title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.2;
  margin: 0 0 8px;
  color: #fff;
  background: linear-gradient(180deg, #ffffff 0%, rgba(245, 217, 123, 0.85) 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-17__desc {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.70);
  margin: 0 0 18px;
  line-height: 1.55;
  letter-spacing: -0.005em;
}
/* ── specs grid ── */

.card-17__specs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4px;
  margin: 0 0 18px;
  padding: 12px 4px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
}

.card-17__spec {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  position: relative;
}

.card-17__spec + .card-17__spec::before {
  content: '';
  position: absolute;
  left: 0;
  top: 20%;
  bottom: 20%;
  width: 1px;
  background: rgba(255, 255, 255, 0.10);
}

.card-17__spec dt {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  margin: 0;
}

.card-17__spec dd {
  font-size: 14px;
  font-weight: 800;
  color: rgba(245, 217, 123, 0.95);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
  margin: 0;
}
/* ── CTAs ── */

.card-17__ctas {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 6px;
  margin-bottom: 16px;
}

.card-17__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 42px;
  padding: 10px 16px;
  border-radius: 14px;
  font: 700 13px 'Inter', sans-serif;
  text-decoration: none;
  letter-spacing: -0.01em;
  transition: transform 0.2s, box-shadow 0.2s;
}

.card-17__cta--primary {
  background: linear-gradient(180deg, #fef3c7 0%, #f5d97b 50%, #d4a574 100%);
  color: #3a1f15;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.6), inset 0 -1px 0 rgba(80, 40, 20, 0.4), 0 4px 12px rgba(245, 217, 123, 0.4), 0 0 0 1px rgba(245, 217, 123, 0.3);
}

.card-17__cta--primary:hover {
  transform: translateY(-1px);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7), inset 0 -1px 0 rgba(80, 40, 20, 0.4), 0 6px 18px rgba(245, 217, 123, 0.6), 0 0 0 1px rgba(245, 217, 123, 0.5);
}

.card-17__cta-arrow {
  display: inline-block;
  transition: transform 0.2s;
}

.card-17__cta--primary:hover .card-17__cta-arrow {
  transform: translateX(3px);
}

.card-17__cta--ghost {
  padding: 10px 12px;
  background: rgba(255, 255, 255, 0.06);
  color: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.card-17__cta--ghost:hover {
  background: rgba(255, 255, 255, 0.10);
  color: #fff;
}

.card-17__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── foot: social proof ── */

.card-17__foot {
  display: flex;
  align-items: center;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.card-17__avatars {
  display: flex;
}

.card-17__av {
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: rgba(58, 31, 21, 0.9);
  font-size: 8.5px;
  font-weight: 800;
  border: 1.5px solid rgba(10, 7, 16, 0.6);
  margin-left: -6px;
  letter-spacing: -0.02em;
}

.card-17__av:first-child {
  margin-left: 0;
}

.card-17__av--1 {
  background: linear-gradient(135deg, #f5d97b, #d4a574);
}

.card-17__av--2 {
  background: linear-gradient(135deg, #f4a2b8, #d4718b);
}

.card-17__av--3 {
  background: linear-gradient(135deg, #c1a3f5, #a78bfa);
}

.card-17__foot-text {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.6);
  letter-spacing: -0.005em;
}

.card-17__foot-text strong {
  color: rgba(245, 217, 123, 0.9);
  font-weight: 700;
}

@keyframes card-17-drift {
  0%,
    100% {
    transform: translate(0, 0) scale(1);
  }

  33% {
    transform: translate(30px, -20px) scale(1.05);
  }

  66% {
    transform: translate(-20px, 30px) scale(0.95);
  }
}

@keyframes card-17-caustic {
  from {
    transform: translate(-30%, -30%) rotate(0deg);
  }

  to {
    transform: translate(-30%, -30%) rotate(360deg);
  }
}

@keyframes card-17-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.8);
  }
}

@keyframes card-17-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 0.8;
  }

  50% {
    transform: scale(1.2);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-17__aurora,
    .card-17__caustic,
    .card-17__badge-dot,
    .card-17__icon-glow {
    animation: none;
  }

  .card-17__card,
    .card-17__card::before,
    .card-17__cta {
    transition: none;
  }

  .card-17__card:hover {
    transform: perspective(1200px) rotateX(2deg) rotateY(-2deg);
  }

  .card-17__cta--primary:hover {
    transform: none;
  }

  .card-17__cta--primary:hover .card-17__cta-arrow {
    transform: none;
  }
}
```
