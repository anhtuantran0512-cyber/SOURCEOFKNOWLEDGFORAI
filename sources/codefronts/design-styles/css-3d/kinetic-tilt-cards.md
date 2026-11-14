---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/kinetic-tilt-cards/"
title: "Pointer Tilt Cards with Parallax Depth Layers"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Three pricing cards that lean toward the cursor, with two background plates drifting at different rates behind the content and a glare that tracks the pointer."
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pointer Tilt Cards with Parallax Depth Layers
Source: https://codefronts.com/design-styles/css-3d/kinetic-tilt-cards/

Three pricing cards that lean toward the cursor, with two background plates drifting at different rates behind the content and a glare that tracks the pointer. The tilt is not applied straight from the event &mdash; a requestAnimationFrame loop eases the current angle toward the target and back to rest, which is what separates a tilt that feels weighted from one that feels twitchy.
## HTML
```html
<section class="d3-14" aria-label="Kinetic tilt cards pricing demo">

  <div class="d3-14__theme">
    <input class="d3-14__theme-input" type="checkbox" id="d3-14-theme">
    <label class="d3-14__theme-label" for="d3-14-theme" aria-label="Toggle light and dark theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>
    </label>
  </div>

  <div class="card">
    <div class="tilt-grid">

      <div class="tcard" data-d3-14-card data-max="18">
        <div class="tcard-inner">
          <div class="tcard-body">
            <div class="layer-bg" data-d3-14-bg></div>
            <div class="layer-mid" data-d3-14-mid></div>
            <div class="layer-fg">
              <div class="plan-badge">Starter</div>
              <div class="price-wrap">
                <span class="price-currency">$</span>
                <span class="price-amount">19</span>
                <span class="price-period">/ mo</span>
              </div>
              <p class="plan-desc">Everything you need to get off the ground fast, without compromise.</p>
              <ul class="features">
                <li class="feature">3 active projects</li>
                <li class="feature">10k API calls / mo</li>
                <li class="feature">Community support</li>
                <li class="feature">Basic analytics</li>
                <li class="feature">1 team member</li>
              </ul>
              <button class="plan-cta" type="button">Get Started</button>
            </div>
          </div>
          <div class="tcard-border"></div>
          <div class="glare" data-d3-14-glare></div>
        </div>
      </div>

      <div class="tcard featured" data-d3-14-card data-max="14" data-raised="1">
        <div class="tcard-inner">
          <div class="tcard-body">
            <div class="layer-bg" data-d3-14-bg></div>
            <div class="layer-mid" data-d3-14-mid></div>
            <div class="layer-fg">
              <div class="plan-badge">Pro</div>
              <div class="price-wrap">
                <span class="price-currency">$</span>
                <span class="price-amount">79</span>
                <span class="price-period">/ mo</span>
              </div>
              <p class="plan-desc">For growing teams that need power, speed, and room to breathe.</p>
              <ul class="features">
                <li class="feature">Unlimited projects</li>
                <li class="feature">500k API calls / mo</li>
                <li class="feature">Priority support</li>
                <li class="feature">Advanced analytics</li>
                <li class="feature">Up to 12 members</li>
              </ul>
              <button class="plan-cta" type="button">Start Free Trial</button>
            </div>
          </div>
          <div class="tcard-border"></div>
          <div class="glare" data-d3-14-glare></div>
        </div>
      </div>

      <div class="tcard" data-d3-14-card data-max="18">
        <div class="tcard-inner">
          <div class="tcard-body">
            <div class="layer-bg" data-d3-14-bg></div>
            <div class="layer-mid" data-d3-14-mid></div>
            <div class="layer-fg">
              <div class="plan-badge">Enterprise</div>
              <div class="price-wrap">
                <span class="price-amount custom">Custom</span>
              </div>
              <p class="plan-desc">Tailored scale, SLA guarantees, and white-glove onboarding for your organization.</p>
              <ul class="features">
                <li class="feature">Unlimited everything</li>
                <li class="feature">Dedicated infrastructure</li>
                <li class="feature">24/7 SLA support</li>
                <li class="feature">SSO + SAML + SOC 2</li>
                <li class="feature">Custom contracts</li>
              </ul>
              <button class="plan-cta" type="button">Contact Sales</button>
            </div>
          </div>
          <div class="tcard-border"></div>
          <div class="glare" data-d3-14-glare></div>
        </div>
      </div>

    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Syne+Mono&display=swap');

.d3-14 {
  --d3-14-bg: #07080e;
  --d3-14-amb-blue: rgba(20,80,180,0.09);
  --d3-14-amb-violet: rgba(80,20,160,0.09);
  --d3-14-amb-teal: rgba(0,200,180,0.04);
  --d3-14-hairline: rgba(255,255,255,0.10);
  --d3-14-glare: rgba(255,255,255,0.18);
  --d3-14-ui-face: rgba(255,255,255,0.05);
  --d3-14-ui-line: rgba(255,255,255,0.14);
  --d3-14-ui-ink: #d6dcf0;
  --d3-14-a-surf-1: #111420;
  --d3-14-a-surf-2: #0d1018;
  --d3-14-a-surf-3: #131722;
  --d3-14-a-wash: rgba(40,100,200,0.12);
  --d3-14-a-accent: #5090ff;
  --d3-14-a-accent-soft: rgba(80,140,255,0.12);
  --d3-14-a-price: #c8d8ff;
  --d3-14-a-body: rgba(180,200,255,0.65);
  --d3-14-a-feature: rgba(180,200,255,0.75);
  --d3-14-a-cta-bg: rgba(80,140,255,0.15);
  --d3-14-a-cta-ink: #7090ff;
  --d3-14-a-cta-line: rgba(80,140,255,0.30);
  --d3-14-a-ring-fill: rgba(60,120,255,0.06);
  --d3-14-a-ring-line: rgba(60,120,255,0.08);
  --d3-14-b-surf-1: #0e1f0e;
  --d3-14-b-surf-2: #0a1808;
  --d3-14-b-surf-3: #101f10;
  --d3-14-b-wash: rgba(0,200,100,0.14);
  --d3-14-b-accent: #00d468;
  --d3-14-b-accent-soft: rgba(0,200,100,0.12);
  --d3-14-b-price: #c0ffd8;
  --d3-14-b-body: rgba(160,240,190,0.65);
  --d3-14-b-feature: rgba(160,240,190,0.75);
  --d3-14-b-cta-bg: #00c860;
  --d3-14-b-cta-ink: #001a0a;
  --d3-14-b-glow: rgba(0,200,80,0.08);
  --d3-14-b-drop: rgba(0,0,0,0.60);
  --d3-14-b-ring-fill: rgba(0,200,100,0.07);
  --d3-14-b-ring-line: rgba(0,200,100,0.10);
  --d3-14-c-surf-1: #1a0e1a;
  --d3-14-c-surf-2: #120a14;
  --d3-14-c-surf-3: #1c1020;
  --d3-14-c-wash: rgba(180,80,255,0.12);
  --d3-14-c-accent: #c060ff;
  --d3-14-c-accent-soft: rgba(180,80,255,0.12);
  --d3-14-c-price: #ecd8ff;
  --d3-14-c-body: rgba(220,180,255,0.65);
  --d3-14-c-feature: rgba(220,180,255,0.75);
  --d3-14-c-cta-bg: rgba(180,80,255,0.15);
  --d3-14-c-cta-ink: #c080ff;
  --d3-14-c-cta-line: rgba(180,80,255,0.30);
  --d3-14-c-ring-fill: rgba(180,80,255,0.06);
  --d3-14-c-ring-line: rgba(180,80,255,0.08);
  width: 100%;
  min-height: max(100vh, 500px);
  display: block;
  position: relative;
  background: var(--d3-14-bg);
  font-family: 'Syne', system-ui, sans-serif;
  overflow: hidden;
  box-sizing: border-box;
}

.d3-14 *,
.d3-14 *::before,
.d3-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.d3-14:has(.d3-14__theme-input:checked) {
  --d3-14-bg: #eceff6;
  --d3-14-amb-blue: rgba(20,80,180,0.12);
  --d3-14-amb-violet: rgba(110,40,200,0.10);
  --d3-14-amb-teal: rgba(0,170,160,0.07);
  --d3-14-hairline: rgba(12,22,52,0.16);
  --d3-14-glare: rgba(18,36,86,0.07);
  --d3-14-ui-face: rgba(255,255,255,0.75);
  --d3-14-ui-line: rgba(12,22,52,0.16);
  --d3-14-ui-ink: #16204a;
  --d3-14-a-surf-1: #ffffff;
  --d3-14-a-surf-2: #f3f7ff;
  --d3-14-a-surf-3: #e9f0ff;
  --d3-14-a-wash: rgba(40,100,200,0.10);
  --d3-14-a-accent: #1450c8;
  --d3-14-a-accent-soft: rgba(30,90,220,0.10);
  --d3-14-a-price: #0d1c3e;
  --d3-14-a-body: #0f1a36;
  --d3-14-a-feature: #101c3a;
  --d3-14-a-cta-bg: rgba(30,90,220,0.10);
  --d3-14-a-cta-ink: #103a94;
  --d3-14-a-cta-line: rgba(30,90,220,0.34);
  --d3-14-a-ring-fill: rgba(40,110,240,0.07);
  --d3-14-a-ring-line: rgba(40,110,240,0.16);
  --d3-14-b-surf-1: #ffffff;
  --d3-14-b-surf-2: #f1fbf5;
  --d3-14-b-surf-3: #e7f7ee;
  --d3-14-b-wash: rgba(0,150,80,0.12);
  --d3-14-b-accent: #00693a;
  --d3-14-b-accent-soft: rgba(0,160,85,0.14);
  --d3-14-b-price: #04301b;
  --d3-14-b-body: #062617;
  --d3-14-b-feature: #062617;
  --d3-14-b-cta-bg: #00713c;
  --d3-14-b-cta-ink: #ffffff;
  --d3-14-b-glow: rgba(0,140,70,0.16);
  --d3-14-b-drop: rgba(24,44,32,0.14);
  --d3-14-b-ring-fill: rgba(0,170,90,0.07);
  --d3-14-b-ring-line: rgba(0,170,90,0.18);
  --d3-14-c-surf-1: #ffffff;
  --d3-14-c-surf-2: #faf5ff;
  --d3-14-c-surf-3: #f2eaff;
  --d3-14-c-wash: rgba(150,60,230,0.10);
  --d3-14-c-accent: #7318c4;
  --d3-14-c-accent-soft: rgba(150,60,230,0.12);
  --d3-14-c-price: #260a44;
  --d3-14-c-body: #200936;
  --d3-14-c-feature: #200936;
  --d3-14-c-cta-bg: rgba(150,60,230,0.12);
  --d3-14-c-cta-ink: #64129f;
  --d3-14-c-cta-line: rgba(150,60,230,0.34);
  --d3-14-c-ring-fill: rgba(150,60,230,0.06);
  --d3-14-c-ring-line: rgba(150,60,230,0.16);
}

@media (prefers-color-scheme: light) {
  .d3-14:has(.d3-14__theme-input:checked) {
    --d3-14-bg: #eceff6;
    --d3-14-amb-blue: rgba(20,80,180,0.12);
    --d3-14-amb-violet: rgba(110,40,200,0.10);
    --d3-14-amb-teal: rgba(0,170,160,0.07);
    --d3-14-hairline: rgba(12,22,52,0.16);
    --d3-14-glare: rgba(18,36,86,0.07);
    --d3-14-ui-face: rgba(255,255,255,0.75);
    --d3-14-ui-line: rgba(12,22,52,0.16);
    --d3-14-ui-ink: #16204a;
    --d3-14-a-surf-1: #ffffff;
    --d3-14-a-surf-2: #f3f7ff;
    --d3-14-a-surf-3: #e9f0ff;
    --d3-14-a-wash: rgba(40,100,200,0.10);
    --d3-14-a-accent: #1450c8;
    --d3-14-a-accent-soft: rgba(30,90,220,0.10);
    --d3-14-a-price: #0d1c3e;
    --d3-14-a-body: #0f1a36;
    --d3-14-a-feature: #101c3a;
    --d3-14-a-cta-bg: rgba(30,90,220,0.10);
    --d3-14-a-cta-ink: #103a94;
    --d3-14-a-cta-line: rgba(30,90,220,0.34);
    --d3-14-a-ring-fill: rgba(40,110,240,0.07);
    --d3-14-a-ring-line: rgba(40,110,240,0.16);
    --d3-14-b-surf-1: #ffffff;
    --d3-14-b-surf-2: #f1fbf5;
    --d3-14-b-surf-3: #e7f7ee;
    --d3-14-b-wash: rgba(0,150,80,0.12);
    --d3-14-b-accent: #00693a;
    --d3-14-b-accent-soft: rgba(0,160,85,0.14);
    --d3-14-b-price: #04301b;
    --d3-14-b-body: #062617;
    --d3-14-b-feature: #062617;
    --d3-14-b-cta-bg: #00713c;
    --d3-14-b-cta-ink: #ffffff;
    --d3-14-b-glow: rgba(0,140,70,0.16);
    --d3-14-b-drop: rgba(24,44,32,0.14);
    --d3-14-b-ring-fill: rgba(0,170,90,0.07);
    --d3-14-b-ring-line: rgba(0,170,90,0.18);
    --d3-14-c-surf-1: #ffffff;
    --d3-14-c-surf-2: #faf5ff;
    --d3-14-c-surf-3: #f2eaff;
    --d3-14-c-wash: rgba(150,60,230,0.10);
    --d3-14-c-accent: #7318c4;
    --d3-14-c-accent-soft: rgba(150,60,230,0.12);
    --d3-14-c-price: #260a44;
    --d3-14-c-body: #200936;
    --d3-14-c-feature: #200936;
    --d3-14-c-cta-bg: rgba(150,60,230,0.12);
    --d3-14-c-cta-ink: #64129f;
    --d3-14-c-cta-line: rgba(150,60,230,0.34);
    --d3-14-c-ring-fill: rgba(150,60,230,0.06);
    --d3-14-c-ring-line: rgba(150,60,230,0.16);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-14:has(.d3-14__theme-input:checked) {
    --d3-14-bg: #eceff6;
    --d3-14-amb-blue: rgba(20,80,180,0.12);
    --d3-14-amb-violet: rgba(110,40,200,0.10);
    --d3-14-amb-teal: rgba(0,170,160,0.07);
    --d3-14-hairline: rgba(12,22,52,0.16);
    --d3-14-glare: rgba(18,36,86,0.07);
    --d3-14-ui-face: rgba(255,255,255,0.75);
    --d3-14-ui-line: rgba(12,22,52,0.16);
    --d3-14-ui-ink: #16204a;
    --d3-14-a-surf-1: #ffffff;
    --d3-14-a-surf-2: #f3f7ff;
    --d3-14-a-surf-3: #e9f0ff;
    --d3-14-a-wash: rgba(40,100,200,0.10);
    --d3-14-a-accent: #1450c8;
    --d3-14-a-accent-soft: rgba(30,90,220,0.10);
    --d3-14-a-price: #0d1c3e;
    --d3-14-a-body: #0f1a36;
    --d3-14-a-feature: #101c3a;
    --d3-14-a-cta-bg: rgba(30,90,220,0.10);
    --d3-14-a-cta-ink: #103a94;
    --d3-14-a-cta-line: rgba(30,90,220,0.34);
    --d3-14-a-ring-fill: rgba(40,110,240,0.07);
    --d3-14-a-ring-line: rgba(40,110,240,0.16);
    --d3-14-b-surf-1: #ffffff;
    --d3-14-b-surf-2: #f1fbf5;
    --d3-14-b-surf-3: #e7f7ee;
    --d3-14-b-wash: rgba(0,150,80,0.12);
    --d3-14-b-accent: #00693a;
    --d3-14-b-accent-soft: rgba(0,160,85,0.14);
    --d3-14-b-price: #04301b;
    --d3-14-b-body: #062617;
    --d3-14-b-feature: #062617;
    --d3-14-b-cta-bg: #00713c;
    --d3-14-b-cta-ink: #ffffff;
    --d3-14-b-glow: rgba(0,140,70,0.16);
    --d3-14-b-drop: rgba(24,44,32,0.14);
    --d3-14-b-ring-fill: rgba(0,170,90,0.07);
    --d3-14-b-ring-line: rgba(0,170,90,0.18);
    --d3-14-c-surf-1: #ffffff;
    --d3-14-c-surf-2: #faf5ff;
    --d3-14-c-surf-3: #f2eaff;
    --d3-14-c-wash: rgba(150,60,230,0.10);
    --d3-14-c-accent: #7318c4;
    --d3-14-c-accent-soft: rgba(150,60,230,0.12);
    --d3-14-c-price: #260a44;
    --d3-14-c-body: #200936;
    --d3-14-c-feature: #200936;
    --d3-14-c-cta-bg: rgba(150,60,230,0.12);
    --d3-14-c-cta-ink: #64129f;
    --d3-14-c-cta-line: rgba(150,60,230,0.34);
    --d3-14-c-ring-fill: rgba(150,60,230,0.06);
    --d3-14-c-ring-line: rgba(150,60,230,0.16);
  }
}

.d3-14 .d3-14__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 30;
}

.d3-14 .d3-14__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 1;
}

.d3-14 .d3-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-14-ui-line);
  border-radius: 12px;
  background: var(--d3-14-ui-face);
  color: var(--d3-14-ui-ink);
  pointer-events: none;
}

.d3-14 .d3-14__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-14 .d3-14__theme-input:focus-visible + .d3-14__theme-label {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.d3-14 .card {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 36px 24px;
}

.d3-14 .card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 55% 45% at 20% 30%, var(--d3-14-amb-blue) 0%, transparent 70%), radial-gradient(ellipse 50% 40% at 80% 70%, var(--d3-14-amb-violet) 0%, transparent 70%), radial-gradient(ellipse 40% 30% at 50% 50%, var(--d3-14-amb-teal) 0%, transparent 70%);
  pointer-events: none;
}

.d3-14 .tilt-grid {
  display: flex;
  gap: 28px;
  align-items: center;
  perspective: 2000px;
  position: relative;
  z-index: 1;
  flex-wrap: wrap;
  justify-content: center;
}

.d3-14 .tcard {
  width: 244px;
  height: 372px;
  position: relative;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.08s linear;
  border-radius: 22px;
}

.d3-14 .tcard-inner {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  overflow: hidden;
  transform-style: preserve-3d;
}

.d3-14 .tcard-body {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  padding: 26px 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
}

.d3-14 .glare {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  pointer-events: none;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.3s;
}

.d3-14 .tcard:hover .glare {
  opacity: 1;
}

.d3-14 .tcard-border {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  border: 1px solid transparent;
  pointer-events: none;
  z-index: 5;
  transition: border-color 0.3s;
}

.d3-14 .tcard:hover .tcard-border {
  border-color: var(--d3-14-hairline);
}

.d3-14 .layer-bg {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  transition: transform 0.08s linear;
}

.d3-14 .layer-mid {
  position: absolute;
  pointer-events: none;
  transition: transform 0.08s linear;
}

.d3-14 .layer-fg {
  position: relative;
  z-index: 3;
}

.d3-14 .plan-badge {
  display: inline-block;
  padding: 5px 12px;
  border-radius: 4px;
  font-family: 'Syne Mono', monospace;
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 14px;
  width: fit-content;
}

.d3-14 .price-wrap {
  margin-bottom: 18px;
}

.d3-14 .price-currency {
  font-size: 13px;
  font-weight: 600;
  vertical-align: top;
  line-height: 2.4;
}

.d3-14 .price-amount {
  font-size: 46px;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -2px;
}

.d3-14 .price-amount.custom {
  font-size: 32px;
  letter-spacing: -1px;
}

.d3-14 .price-period {
  font-size: 12px;
  font-weight: 400;
  opacity: 0.55;
  margin-left: 2px;
}

.d3-14 .plan-desc {
  font-size: 12px;
  font-weight: 400;
  opacity: 0.65;
  line-height: 1.6;
  margin-bottom: 20px;
}

.d3-14 .features {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.d3-14 .feature {
  font-size: 11px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
  opacity: 0.8;
}

.d3-14 .feature::before {
  content: '◆';
  font-size: 9px;
  opacity: 0.4;
}

.d3-14 .plan-cta {
  display: block;
  width: 100%;
  padding: 12px;
  border-radius: 10px;
  font-family: 'Syne', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  border: none;
  margin-top: 18px;
  transition: transform 0.15s, filter 0.15s;
}

.d3-14 .plan-cta:hover {
  filter: brightness(1.12);
  transform: translateY(-1px);
}

.d3-14 .plan-cta:active {
  transform: translateY(1px);
}

.d3-14 .tcard:nth-child(1) .tcard-body {
  background: linear-gradient(145deg, var(--d3-14-a-surf-1) 0%, var(--d3-14-a-surf-2) 55%, var(--d3-14-a-surf-3) 100%);
}

.d3-14 .tcard:nth-child(1) .layer-bg {
  background: radial-gradient(ellipse 80% 60% at 30% 20%, var(--d3-14-a-wash) 0%, transparent 70%);
}

.d3-14 .tcard:nth-child(1) .plan-badge {
  background: var(--d3-14-a-accent-soft);
  color: var(--d3-14-a-accent);
}

.d3-14 .tcard:nth-child(1) .price-currency,
.d3-14 .tcard:nth-child(1) .price-amount,
.d3-14 .tcard:nth-child(1) .price-period {
  color: var(--d3-14-a-price);
}

.d3-14 .tcard:nth-child(1) .plan-desc {
  color: var(--d3-14-a-body);
}

.d3-14 .tcard:nth-child(1) .feature {
  color: var(--d3-14-a-feature);
}

.d3-14 .tcard:nth-child(1) .plan-cta {
  background: var(--d3-14-a-cta-bg);
  color: var(--d3-14-a-cta-ink);
  border: 1px solid var(--d3-14-a-cta-line);
}

.d3-14 .tcard:nth-child(1) .layer-mid {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--d3-14-a-ring-fill) 0%, transparent 70%);
  border: 1px solid var(--d3-14-a-ring-line);
  top: -40px;
  right: -40px;
}

.d3-14 .tcard.featured .tcard-body {
  background: linear-gradient(145deg, var(--d3-14-b-surf-1) 0%, var(--d3-14-b-surf-2) 55%, var(--d3-14-b-surf-3) 100%);
}

.d3-14 .tcard.featured .layer-bg {
  background: radial-gradient(ellipse 80% 60% at 50% 25%, var(--d3-14-b-wash) 0%, transparent 70%);
}

.d3-14 .tcard.featured .plan-badge {
  background: var(--d3-14-b-accent-soft);
  color: var(--d3-14-b-accent);
}

.d3-14 .tcard.featured .price-currency,
.d3-14 .tcard.featured .price-amount,
.d3-14 .tcard.featured .price-period {
  color: var(--d3-14-b-price);
}

.d3-14 .tcard.featured .plan-desc {
  color: var(--d3-14-b-body);
}

.d3-14 .tcard.featured .feature {
  color: var(--d3-14-b-feature);
}

.d3-14 .tcard.featured .plan-cta {
  background: var(--d3-14-b-cta-bg);
  color: var(--d3-14-b-cta-ink);
  border: none;
  font-weight: 800;
}

.d3-14 .tcard.featured {
  transform: translateY(-12px);
  box-shadow: 0 40px 80px var(--d3-14-b-glow), 0 20px 40px var(--d3-14-b-drop);
}

.d3-14 .tcard.featured::after {
  content: 'MOST POPULAR';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--d3-14-b-cta-bg);
  color: var(--d3-14-b-cta-ink);
  font-family: 'Syne', sans-serif;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 2.5px;
  padding: 4px 12px;
  border-radius: 3px;
  z-index: 20;
  white-space: nowrap;
}

.d3-14 .tcard.featured .layer-mid {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--d3-14-b-ring-fill) 0%, transparent 70%);
  border: 1px solid var(--d3-14-b-ring-line);
  top: -60px;
  right: -60px;
}

.d3-14 .tcard:nth-child(3) .tcard-body {
  background: linear-gradient(145deg, var(--d3-14-c-surf-1) 0%, var(--d3-14-c-surf-2) 55%, var(--d3-14-c-surf-3) 100%);
}

.d3-14 .tcard:nth-child(3) .layer-bg {
  background: radial-gradient(ellipse 80% 60% at 70% 30%, var(--d3-14-c-wash) 0%, transparent 70%);
}

.d3-14 .tcard:nth-child(3) .plan-badge {
  background: var(--d3-14-c-accent-soft);
  color: var(--d3-14-c-accent);
}

.d3-14 .tcard:nth-child(3) .price-currency,
.d3-14 .tcard:nth-child(3) .price-amount,
.d3-14 .tcard:nth-child(3) .price-period {
  color: var(--d3-14-c-price);
}

.d3-14 .tcard:nth-child(3) .plan-desc {
  color: var(--d3-14-c-body);
}

.d3-14 .tcard:nth-child(3) .feature {
  color: var(--d3-14-c-feature);
}

.d3-14 .tcard:nth-child(3) .plan-cta {
  background: var(--d3-14-c-cta-bg);
  color: var(--d3-14-c-cta-ink);
  border: 1px solid var(--d3-14-c-cta-line);
}

.d3-14 .tcard:nth-child(3) .layer-mid {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--d3-14-c-ring-fill) 0%, transparent 70%);
  border: 1px solid var(--d3-14-c-ring-line);
  bottom: 10px;
  left: -30px;
}

@media (max-width: 720px) {
  .d3-14 {
    min-height: max(100vh, 1100px);
  }

  .d3-14 .tcard.featured {
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-14 .tcard,
    .d3-14 .layer-bg,
    .d3-14 .layer-mid {
    transition: none !important;
    transform: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.d3-14');
  if (!root) return;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  root.querySelectorAll('[data-d3-14-card]').forEach(card => {
    const maxTilt = parseFloat(card.dataset.max) || 16;
    const glare = card.querySelector('[data-d3-14-glare]');
    const layerBg = card.querySelector('[data-d3-14-bg]');
    const layerMid = card.querySelector('[data-d3-14-mid]');
    const raised = card.dataset.raised === '1';

    let animFrame = null;
    let targetRx = 0, targetRy = 0;
    let currentRx = 0, currentRy = 0;
    let active = false;

    function lerp(a, b, t) { return a + (b - a) * t; }

    function tick() {
      if (!active) {
        currentRx = lerp(currentRx, 0, 0.08);
        currentRy = lerp(currentRy, 0, 0.08);
      } else {
        currentRx = lerp(currentRx, targetRx, 0.12);
        currentRy = lerp(currentRy, targetRy, 0.12);
      }
      const baseY = raised ? -12 : 0;
      card.style.transform = 'perspective(1000px) rotateX(' + currentRx + 'deg) rotateY(' + currentRy + 'deg) translateY(' + baseY + 'px)';
      if (layerBg) layerBg.style.transform = 'translateX(' + (currentRy * 1.5) + 'px) translateY(' + (-currentRx * 1.5) + 'px)';
      if (layerMid) layerMid.style.transform = 'translateX(' + (currentRy * 3) + 'px) translateY(' + (-currentRx * 3) + 'px)';

      if (active || Math.abs(currentRx) > 0.05 || Math.abs(currentRy) > 0.05) {
        animFrame = requestAnimationFrame(tick);
      } else {
        animFrame = null;
      }
    }

    card.addEventListener('mouseenter', () => {
      active = true;
      if (!animFrame) tick();
    });
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) / (rect.width / 2);
      const dy = (e.clientY - cy) / (rect.height / 2);
      targetRy = dx * maxTilt;
      targetRx = -dy * maxTilt;
      const glareX = ((e.clientX - rect.left) / rect.width) * 100;
      const glareY = ((e.clientY - rect.top) / rect.height) * 100;
      if (glare) glare.style.background = 'radial-gradient(circle at ' + glareX + '% ' + glareY + '%, var(--d3-14-glare) 0%, transparent 55%)';
    });
    card.addEventListener('mouseleave', () => {
      active = false;
      targetRx = 0;
      targetRy = 0;
      if (glare) glare.style.background = 'none';
      if (!animFrame) tick();
    });
  });
})();
```
