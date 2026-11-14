---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/saas-pricing-table-slide-in-animation/"
title: "SaaS Pricing Table Slide-In Animation"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Three SaaS pricing tiers (Starter / Pro / Team) that slide up from below with the middle tier scaled and highlighted — the canonical B2B SaaS pricing layout…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Pricing Table Slide-In Animation
Source: https://codefronts.com/motion/css-slide-in-animation/saas-pricing-table-slide-in-animation/

Three SaaS pricing tiers (Starter / Pro / Team) that slide up from below with the middle tier scaled and highlighted — the canonical B2B SaaS pricing layout used by Stripe, Linear, Vercel, Notion, and every subscription product.
## HTML
```html
<div class="sl-03">
  <div class="sl-03__inner">
    <p class="sl-03__kicker">Pricing</p>
    <h2 class="sl-03__title">Simple, transparent pricing</h2>
    <p class="sl-03__sub">14-day free trial · No credit card required · Cancel anytime</p>
    <div class="sl-03__row">
      <div class="sl-03__tier">
        <h3>Starter</h3>
        <div class="sl-03__price">$0<small>/mo</small></div>
        <p class="sl-03__forwho">For solo developers</p>
        <ul>
          <li>Up to 3 projects</li>
          <li>Basic analytics</li>
          <li>Community support</li>
        </ul>
        <button class="sl-03__btn">Start free</button>
      </div>
      <div class="sl-03__tier sl-03__tier--featured">
        <span class="sl-03__badge">Most popular</span>
        <h3>Pro</h3>
        <div class="sl-03__price">$29<small>/mo</small></div>
        <p class="sl-03__forwho">For growing teams</p>
        <ul>
          <li>Unlimited projects</li>
          <li>Advanced analytics + API</li>
          <li>Priority support</li>
          <li>Custom integrations</li>
        </ul>
        <button class="sl-03__btn sl-03__btn--primary">Start 14-day trial</button>
      </div>
      <div class="sl-03__tier">
        <h3>Team</h3>
        <div class="sl-03__price">$99<small>/mo</small></div>
        <p class="sl-03__forwho">For established orgs</p>
        <ul>
          <li>Everything in Pro</li>
          <li>10-seat pool</li>
          <li>SSO + audit logs</li>
          <li>Dedicated CSM</li>
        </ul>
        <button class="sl-03__btn">Contact sales</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-03 {
  --bg: #0a0e1c;
  --card: #141a2e;
  --accent: #8b5cf6;
  --accent2: #6366f1;
  --text: #f0eeff;
  --sub: #9d97c8;
  --line: rgba(148,163,184,.14);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(80% 100% at 50% 0%, rgba(139,92,246,.14) 0%, transparent 60%), var(--bg);
  color: var(--text);
}

.sl-03 *,
.sl-03 *::before,
.sl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-03 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-03__inner {
  width: 100%;
  max-width: 1000px;
  text-align: center;
}

.sl-03__kicker {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}

.sl-03__title {
  font-size: clamp(1.7rem,3.5vw,2.3rem);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 8px;
}

.sl-03__sub {
  font-size: .9rem;
  color: var(--sub);
  margin-bottom: 36px;
}

.sl-03__row {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 18px;
  align-items: stretch;
}

.sl-03__tier {
  position: relative;
  padding: 28px 26px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: linear-gradient(180deg,rgba(255,255,255,.02),rgba(255,255,255,0)),var(--card);
  display: flex;
  flex-direction: column;
  text-align: left;
  opacity: 0;
  transform: translateY(40px);
  animation: sl-03-tier .55s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-03__tier:nth-child(1) {
  animation-delay: .15s;
}

.sl-03__tier:nth-child(2) {
  animation-delay: .3s;
  animation-name: sl-03-featured;
  border-color: rgba(139,92,246,.4);
  background: linear-gradient(180deg,rgba(139,92,246,.08),rgba(255,255,255,0)),var(--card);
  box-shadow: 0 24px 48px -16px rgba(139,92,246,.4);
}

.sl-03__tier:nth-child(3) {
  animation-delay: .45s;
}

.sl-03__badge {
  position: absolute;
  top: -11px;
  left: 50%;
  transform: translateX(-50%);
  padding: 4px 14px;
  border-radius: 999px;
  background: linear-gradient(135deg,#a78bfa,#8b5cf6);
  color: #fff;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  box-shadow: 0 6px 14px -4px rgba(139,92,246,.5);
}

.sl-03__tier h3 {
  font-size: .85rem;
  font-weight: 700;
  color: var(--sub);
  letter-spacing: .06em;
  text-transform: uppercase;
  margin-bottom: 14px;
}

.sl-03__price {
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 6px;
  font-variant-numeric: tabular-nums;
}

.sl-03__price small {
  font-size: .85rem;
  font-weight: 500;
  color: var(--sub);
  margin-left: 4px;
}

.sl-03__forwho {
  font-size: .8rem;
  color: var(--sub);
  margin-bottom: 22px;
}

.sl-03__tier ul {
  list-style: none;
  margin-bottom: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sl-03__tier li {
  font-size: .88rem;
  color: var(--text);
  padding-left: 22px;
  position: relative;
  line-height: 1.4;
}

.sl-03__tier li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 5px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(139,92,246,.2) url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3e%3cpath fill='%238b5cf6' d='M4.5 8.5L2 6l.7-.7L4.5 7.1l4.8-4.8.7.7z'/%3e%3c/svg%3e") center/70% no-repeat;
}

.sl-03__btn {
  padding: 11px 20px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: rgba(255,255,255,.04);
  color: var(--text);
  font-family: inherit;
  font-size: .88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.sl-03__btn:hover {
  background: rgba(255,255,255,.08);
}

.sl-03__btn--primary {
  background: linear-gradient(135deg,#8b5cf6,#6366f1);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 8px 20px -6px rgba(139,92,246,.55);
}

.sl-03__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -6px rgba(139,92,246,.7);
}

@keyframes sl-03-tier {
  from {
    opacity: 0;
    transform: translateY(40px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes sl-03-featured {
  from {
    opacity: 0;
    transform: translateY(40px) scale(1.05);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1.05);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-03__tier {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }

  .sl-03__tier:nth-child(2) {
    transform: scale(1.05)!important;
  }
}

@media (max-width: 720px) {
  .sl-03__row {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .sl-03__tier:nth-child(2) {
    animation-name: sl-03-tier;
    transform: none;
  }
}
```
