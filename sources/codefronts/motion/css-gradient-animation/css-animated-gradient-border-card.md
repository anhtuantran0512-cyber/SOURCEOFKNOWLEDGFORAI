---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-animated-gradient-border-card/"
title: "CSS Animated Gradient Border Card"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A pricing card trio where the featured tier sports a razor-thin rotating conic-gradient border driven by the CSS @property Houdini API, creating a…"
has_js: "false"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Gradient Border Card
Source: https://codefronts.com/motion/css-gradient-animation/css-animated-gradient-border-card/

A pricing card trio where the featured tier sports a razor-thin rotating conic-gradient border driven by the CSS @property Houdini API, creating a continuously spinning rainbow ring that highlights premium tiers.
## HTML
```html
<div class="ga-06">

  <!-- Free tier — no spinning border -->
  <div class="ga-06__card">
    <div class="ga-06__inner">
      <div class="ga-06__tier">
        <span class="ga-06__tier-name">Starter</span>
        <span class="ga-06__badge ga-06__badge--free">Free</span>
      </div>
      <div class="ga-06__price">
        <span class="ga-06__price-amt">$0</span>
        <span class="ga-06__price-per">/mo</span>
      </div>
      <div class="ga-06__divider"></div>
      <ul class="ga-06__features">
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>3 projects</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>5GB storage</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✗</span>Team access</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✗</span>Priority support</li>
      </ul>
      <button class="ga-06__cta ga-06__cta--free">Get Started</button>
    </div>
  </div>

  <!-- Pro tier — always-on spinning gradient border -->
  <div class="ga-06__card ga-06__card--active">
    <div class="ga-06__inner">
      <div class="ga-06__tier">
        <span class="ga-06__tier-name">Pro</span>
        <span class="ga-06__badge ga-06__badge--pro">Most Popular</span>
      </div>
      <div class="ga-06__price">
        <span class="ga-06__price-amt">$29</span>
        <span class="ga-06__price-per">/mo</span>
      </div>
      <div class="ga-06__divider"></div>
      <ul class="ga-06__features">
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Unlimited projects</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>100GB storage</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Team access (5 seats)</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Priority support</li>
      </ul>
      <button class="ga-06__cta ga-06__cta--pro">Upgrade to Pro</button>
    </div>
  </div>

  <!-- Elite tier — hover reveals border -->
  <div class="ga-06__card">
    <div class="ga-06__inner">
      <div class="ga-06__tier">
        <span class="ga-06__tier-name">Elite</span>
        <span class="ga-06__badge ga-06__badge--elite">Enterprise</span>
      </div>
      <div class="ga-06__price">
        <span class="ga-06__price-amt">$99</span>
        <span class="ga-06__price-per">/mo</span>
      </div>
      <div class="ga-06__divider"></div>
      <ul class="ga-06__features">
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Unlimited everything</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>1TB storage</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Unlimited seats</li>
        <li class="ga-06__feature"><span class="ga-06__feature-icon">✓</span>Dedicated SLA</li>
      </ul>
      <button class="ga-06__cta ga-06__cta--elite">Contact Sales</button>
    </div>
  </div>

</div>
```
## CSS
```css
.ga-06,
.ga-06 *,
.ga-06 *::before,
.ga-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-06 ::selection {
  background: rgba(168,85,247,.4);
  color: #fff;
}

.ga-06 {
  --bg: #0c0c14;
  --card-bg: #13131f;
  --dur: 3s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  padding: 48px 24px;
}
/* ── Rotating gradient border using conic-gradient on ::before ── */

.ga-06__card {
  position: relative;
  width: 240px;
  border-radius: 18px;
  padding: 2px;
  /* border width */
  background: var(--card-bg);
  isolation: isolate;
}
/* The spinning gradient ring */

.ga-06__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: conic-gradient(
      from var(--a, 0deg),
      #a855f7, #ec4899, #f97316, #eab308, #22d3ee, #6366f1, #a855f7
    );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: ga-06-spin var(--dur) linear infinite;
  opacity: 0;
  transition: opacity .4s ease;
}
/* Static subtle border at rest */

.ga-06__card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  border: 1.5px solid rgba(255,255,255,.07);
  pointer-events: none;
}
/* Spin via CSS custom property (Houdini) with JS fallback */

@keyframes ga-06-spin {
  to {
    --a: 360deg;
  }
}
/* Always-on card shows border always */

.ga-06__card--active::before {
  opacity: 1;
}
/* Hover reveals border on non-active cards */

.ga-06__card:not(.ga-06__card--active):hover::before {
  opacity: .7;
}
/* Glow behind active card */

.ga-06__card--active {
  filter: drop-shadow(0 0 18px rgba(168,85,247,.25));
}
/* Inner content */

.ga-06__inner {
  background: var(--card-bg);
  border-radius: 16px;
  padding: 28px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ga-06__tier {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ga-06__tier-name {
  font-size: .7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: rgba(255,255,255,.4);
}

.ga-06__badge {
  font-size: .6rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .09em;
  padding: 3px 9px;
  border-radius: 999px;
}

.ga-06__badge--free {
  background: rgba(255,255,255,.07);
  color: rgba(255,255,255,.4);
}

.ga-06__badge--pro {
  background: rgba(168,85,247,.15);
  color: #c084fc;
  border: 1px solid rgba(168,85,247,.25);
}

.ga-06__badge--elite {
  background: rgba(234,179,8,.12);
  color: #fbbf24;
  border: 1px solid rgba(234,179,8,.2);
}

.ga-06__price {
  display: flex;
  align-items: baseline;
  gap: 3px;
}

.ga-06__price-amt {
  font-size: 2.2rem;
  font-weight: 900;
  color: #fff;
  line-height: 1;
}

.ga-06__price-per {
  font-size: .75rem;
  color: rgba(255,255,255,.35);
}

.ga-06__divider {
  height: 1px;
  background: rgba(255,255,255,.06);
}

.ga-06__features {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ga-06__feature {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .8rem;
  color: rgba(255,255,255,.55);
}

.ga-06__feature-icon {
  font-size: .85rem;
  flex-shrink: 0;
}

.ga-06__card--active .ga-06__feature {
  color: rgba(255,255,255,.72);
}

.ga-06__cta {
  margin-top: 4px;
  width: 100%;
  padding: 11px;
  border-radius: 10px;
  border: none;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all .25s;
}

.ga-06__cta--free {
  background: rgba(255,255,255,.07);
  color: rgba(255,255,255,.5);
}

.ga-06__cta--free:hover {
  background: rgba(255,255,255,.11);
  color: rgba(255,255,255,.75);
}

.ga-06__cta--pro {
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: #fff;
}

.ga-06__cta--pro:hover {
  box-shadow: 0 4px 20px rgba(168,85,247,.4);
  transform: translateY(-1px);
}

.ga-06__cta--elite {
  background: linear-gradient(135deg, #92400e, #b45309);
  color: #fef3c7;
}

.ga-06__cta--elite:hover {
  box-shadow: 0 4px 20px rgba(234,179,8,.3);
  transform: translateY(-1px);
}

@property --a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@media (prefers-reduced-motion: reduce) {
  .ga-06__card::before {
    animation: none;
  }
}
```
