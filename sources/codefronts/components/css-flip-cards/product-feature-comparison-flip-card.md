---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/product-feature-comparison-flip-card/"
title: "Product Feature Comparison Flip Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows a styled product render; back reveals a full technical specification grid with an Add to Cart CTA."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Feature Comparison Flip Card
Source: https://codefronts.com/components/css-flip-cards/product-feature-comparison-flip-card/

Front shows a styled product render; back reveals a full technical specification grid with an Add to Cart CTA.
## HTML
```html
<div class="fc-01">
  <div class="fc-01__scene">
    <div class="fc-01__card">
      <div class="fc-01__front">
        <div class="fc-01__badge">New 2025</div>
        <div class="fc-01__img">
          <svg class="fc-01__product-svg" width="140" height="140" viewBox="0 0 140 140" fill="none">
            <rect x="30" y="50" width="80" height="60" rx="8" fill="url(#g1)" opacity=".9"/>
            <rect x="38" y="58" width="64" height="44" rx="4" fill="#0a0a1a"/>
            <rect x="40" y="60" width="60" height="40" rx="3" fill="url(#g2)" opacity=".8"/>
            <circle cx="70" cy="80" r="10" fill="none" stroke="#7c3aed" stroke-width="2"/>
            <circle cx="70" cy="80" r="4" fill="#06b6d4"/>
            <line x1="55" y1="115" x2="85" y2="115" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
            <rect x="62" y="110" width="16" height="5" rx="2" fill="#1a1a2e"/>
            <defs>
              <linearGradient id="g1" x1="30" y1="50" x2="110" y2="110" gradientUnits="userSpaceOnUse">
                <stop stop-color="#2d1b69"/>
                <stop offset="1" stop-color="#0e7490"/>
              </linearGradient>
              <linearGradient id="g2" x1="40" y1="60" x2="100" y2="100" gradientUnits="userSpaceOnUse">
                <stop stop-color="#7c3aed" stop-opacity=".3"/>
                <stop offset="1" stop-color="#06b6d4" stop-opacity=".2"/>
              </linearGradient>
            </defs>
          </svg>
        </div>
        <div class="fc-01__info">
          <div class="fc-01__brand">NovaTech</div>
          <div class="fc-01__name">ProVision X7 Monitor</div>
          <div class="fc-01__price">$649 <span>/ unit</span></div>
          <div class="fc-01__hint">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
            Hover to view specs
          </div>
        </div>
      </div>
      <div class="fc-01__back">
        <div class="fc-01__back-title">Technical Specifications</div>
        <div class="fc-01__spec">
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Display</div><div class="fc-01__spec-val">27" IPS</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Resolution</div><div class="fc-01__spec-val">4K UHD</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Refresh Rate</div><div class="fc-01__spec-val fc-01__spec-val--accent">165 Hz</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Response</div><div class="fc-01__spec-val">1 ms GTG</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Panel</div><div class="fc-01__spec-val">Nano IPS</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Ports</div><div class="fc-01__spec-val">2× DP 1.4</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">HDR</div><div class="fc-01__spec-val fc-01__spec-val--accent">HDR 600</div></div>
          <div class="fc-01__spec-item"><div class="fc-01__spec-label">Coverage</div><div class="fc-01__spec-val">98% DCI-P3</div></div>
        </div>
        <button class="fc-01__cta">Add to Cart</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-01,
.fc-01 *,
.fc-01 *::before,
.fc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-01 ::selection {
  background: #6c63ff;
  color: #fff;
}

.fc-01 {
  --bg: #0d0d14;
  --accent: #7c3aed;
  --accent2: #06b6d4;
  --gold: #f59e0b;
  --white: #f1f5f9;
  --card-w: 340px;
  --card-h: 480px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-01__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
}

.fc-01__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-01__scene:hover .fc-01__card {
  transform: rotateY(180deg);
}

.fc-01__front,
.fc-01__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}

.fc-01__front {
  background: linear-gradient(145deg,#1a1a2e,#16213e);
  border: 1px solid rgba(124,58,237,.3);
  display: flex;
  flex-direction: column;
}

.fc-01__back {
  background: linear-gradient(145deg,#0f172a,#1e1b4b);
  border: 1px solid rgba(6,182,212,.3);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
}
/* front */

.fc-01__badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: var(--gold);
  color: #000;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 20px;
}

.fc-01__img {
  height: 220px;
  background: linear-gradient(135deg,#1a0533,#0c1a4f);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
  position: relative;
}

.fc-01__img::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 70%,rgba(124,58,237,.4),transparent 70%);
}

.fc-01__product-svg {
  position: relative;
  z-index: 1;
}

.fc-01__info {
  padding: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fc-01__brand {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--accent2);
  font-weight: 600;
}

.fc-01__name {
  font-size: 22px;
  font-weight: 700;
  color: var(--white);
  line-height: 1.2;
}

.fc-01__price {
  font-size: 28px;
  font-weight: 800;
  color: var(--accent);
}

.fc-01__price span {
  font-size: 14px;
  font-weight: 400;
  color: rgba(241,245,249,.5);
}

.fc-01__hint {
  margin-top: auto;
  font-size: 11px;
  color: rgba(241,245,249,.35);
  letter-spacing: .08em;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.fc-01__hint svg {
  opacity: .5;
}
/* back */

.fc-01__back-title {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}

.fc-01__spec {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  flex: 1;
}

.fc-01__spec-item {
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
  padding: 14px;
}

.fc-01__spec-label {
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(241,245,249,.4);
  margin-bottom: 4px;
}

.fc-01__spec-val {
  font-size: 15px;
  font-weight: 600;
  color: var(--white);
}

.fc-01__spec-val--accent {
  color: var(--gold);
}

.fc-01__cta {
  margin-top: 20px;
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: opacity .2s;
}

.fc-01__cta:hover {
  opacity: .85;
}

@media (prefers-reduced-motion: reduce) {
  .fc-01__card {
    transition: none;
  }
}
```
