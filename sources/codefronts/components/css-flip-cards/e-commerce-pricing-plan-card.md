---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/e-commerce-pricing-plan-card/"
title: "E-commerce Pricing Plan Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front displays tier name and monthly price with gradient text; back reveals the complete feature breakdown and a CTA button."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Pricing Plan Card
Source: https://codefronts.com/components/css-flip-cards/e-commerce-pricing-plan-card/

Front displays tier name and monthly price with gradient text; back reveals the complete feature breakdown and a CTA button.
## HTML
```html
<div class="fc-02">
  <div class="fc-02__scene">
    <div class="fc-02__card">
      <div class="fc-02__front">
        <div class="fc-02__front-glow"></div>
        <div class="fc-02__front-head">
          <div class="fc-02__tier-icon">🚀</div>
          <div class="fc-02__tier">Pro Plan</div>
          <div class="fc-02__price-wrap">
            <span class="fc-02__price-cur">$</span>
            <span class="fc-02__price-num">49</span>
          </div>
          <div class="fc-02__price-per">per month, billed annually</div>
        </div>
        <div class="fc-02__divider"></div>
        <div class="fc-02__preview">
          <div class="fc-02__preview-label">Includes</div>
          <div class="fc-02__dot-list">
            <div class="fc-02__dot">Unlimited projects</div>
            <div class="fc-02__dot">Advanced analytics</div>
            <div class="fc-02__dot">Priority support</div>
            <div class="fc-02__dot">Custom domains</div>
          </div>
        </div>
        <div class="fc-02__hint">Hover for full feature breakdown</div>
      </div>
      <div class="fc-02__back">
        <div class="fc-02__back-title">Everything in Pro</div>
        <div class="fc-02__feature-list">
          <div class="fc-02__feature"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>Unlimited projects & workspaces</div>
          <div class="fc-02__feature"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>Advanced real-time analytics</div>
          <div class="fc-02__feature"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>Custom domain mapping</div>
          <div class="fc-02__feature"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>API access (10k req/day)</div>
          <div class="fc-02__feature"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>Priority 4h support SLA</div>
          <div class="fc-02__feature fc-02__feature--gold"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>AI content generation (50/mo)</div>
          <div class="fc-02__feature fc-02__feature--gold"><span class="fc-02__feature-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3"/></svg></span>White-label exports</div>
        </div>
        <button class="fc-02__cta">Get Started — $49/mo</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-02,
.fc-02 *,
.fc-02 *::before,
.fc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-02 ::selection {
  background: #10b981;
  color: #000;
}

.fc-02 {
  --bg: #050d0a;
  --accent: #10b981;
  --accent2: #f59e0b;
  --purple: #8b5cf6;
  --white: #f0fdf4;
  --card-w: 320px;
  --card-h: 460px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 0%,#0a2e1e,#050d0a 70%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 32px;
  flex-wrap: wrap;
  color: var(--white);
}
/* scene */

.fc-02__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-02__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform-origin: center bottom;
  transition: transform .85s cubic-bezier(.34,1.2,.4,1);
}
/* Flip-UP from the base — the card's top edge appears to lift toward the
   camera while the bottom edge stays anchored. Rotating around the bottom
   would normally push the rendered card downward by its full height
   (because the top swings into the space below); the translateY(-100%)
   at the end keeps the visual position fixed by counter-translating the
   card by exactly its height. Reads as "lifting the curtain on the plan." */

.fc-02__scene:hover .fc-02__card {
  transform: translateY(-100%) rotateX(180deg);
}

.fc-02__front,
.fc-02__back {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-02__front {
  background: linear-gradient(160deg,#071a12,#0a2e1e);
  border: 1px solid rgba(16,185,129,.25);
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 40px rgba(16,185,129,.08);
}

.fc-02__front-glow {
  position: absolute;
  top: -60px;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 200px;
  background: radial-gradient(circle,rgba(16,185,129,.25),transparent 70%);
  pointer-events: none;
}

.fc-02__front-head {
  padding: 32px 28px 24px;
  text-align: center;
  position: relative;
}

.fc-02__tier-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: linear-gradient(135deg,rgba(16,185,129,.2),rgba(16,185,129,.05));
  border: 1px solid rgba(16,185,129,.3);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  font-size: 24px;
}

.fc-02__tier {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 8px;
}

.fc-02__price-wrap {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 4px;
  margin-top: 4px;
}

.fc-02__price-cur {
  font-size: 20px;
  font-weight: 700;
  color: rgba(240,253,244,.6);
  margin-top: 6px;
}

.fc-02__price-num {
  font-size: 52px;
  font-weight: 900;
  background: linear-gradient(135deg,#10b981,#34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}

.fc-02__price-per {
  font-size: 13px;
  color: rgba(240,253,244,.4);
  margin-top: 6px;
}

.fc-02__divider {
  height: 1px;
  background: linear-gradient(90deg,transparent,rgba(16,185,129,.2),transparent);
  margin: 0 28px;
}

.fc-02__preview {
  padding: 24px 28px;
  flex: 1;
}

.fc-02__preview-label {
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(240,253,244,.35);
  margin-bottom: 14px;
}

.fc-02__dot-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fc-02__dot {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: rgba(240,253,244,.6);
}

.fc-02__dot::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  flex-shrink: 0;
}

.fc-02__hint {
  padding: 0 28px 24px;
  text-align: center;
  font-size: 11px;
  color: rgba(240,253,244,.25);
  letter-spacing: .08em;
}
/* BACK */

.fc-02__back {
  background: linear-gradient(160deg,#0a0a1e,#0d1533);
  border: 1px solid rgba(139,92,246,.25);
  /* Pre-rotated on X so the upward flip-from-base brings it forward. */
  transform: rotateX(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
  box-shadow: 0 0 40px rgba(139,92,246,.08);
}

.fc-02__back-title {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--purple);
  margin-bottom: 20px;
}

.fc-02__feature-list {
  display: flex;
  flex-direction: column;
  gap: 11px;
  flex: 1;
}

.fc-02__feature {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 10px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.06);
  font-size: 13px;
  color: rgba(240,253,244,.8);
}

.fc-02__feature-check {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(16,185,129,.15);
  border: 1px solid rgba(16,185,129,.3);
}

.fc-02__feature-check svg {
  width: 11px;
  height: 11px;
  stroke: var(--accent);
  stroke-width: 2.5;
  fill: none;
}

.fc-02__feature--gold .fc-02__feature-check {
  background: rgba(245,158,11,.15);
  border-color: rgba(245,158,11,.3);
}

.fc-02__feature--gold .fc-02__feature-check svg {
  stroke: var(--accent2);
}

.fc-02__cta {
  margin-top: 20px;
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg,var(--accent),#059669);
  color: #000;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: .04em;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: transform .15s;
}

.fc-02__cta:hover {
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .fc-02__card {
    transition: none;
  }
}
```
