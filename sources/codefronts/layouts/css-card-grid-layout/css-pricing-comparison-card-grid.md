---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-pricing-comparison-card-grid/"
title: "CSS Pricing Comparison Card Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A 3-tier SaaS pricing comparison grid with Starter / Pro / Enterprise plans — featured tier elevated via accent border and 'Most Popular' ribbon, every card…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pricing Comparison Card Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-pricing-comparison-card-grid/

A 3-tier SaaS pricing comparison grid with Starter / Pro / Enterprise plans — featured tier elevated via accent border and 'Most Popular' ribbon, every card with full feature checklist, price toggle hint, and a primary CTA. The exact pricing pattern Stripe, Linear, Vercel, and Notion all converged on.
## HTML
```html
<div class="cg-10">
  <div class="cg-10__head">
    <span class="cg-10__kicker">Pricing</span>
    <h2 class="cg-10__title">Simple plans. No surprises.</h2>
    <p class="cg-10__sub">Pick a plan that fits. Switch or cancel any time.</p>
  </div>
  <div class="cg-10__grid">

    <article class="cg-10__card">
      <header class="cg-10__cardhead">
        <span class="cg-10__plan">Starter</span>
        <span class="cg-10__planhint">For solo makers</span>
      </header>
      <div class="cg-10__price-wrap">
        <span class="cg-10__currency">$</span>
        <span class="cg-10__price">0</span>
        <span class="cg-10__period">/mo</span>
      </div>
      <p class="cg-10__tagline">Everything you need to get going.</p>
      <ul class="cg-10__features">
        <li><span class="cg-10__check">✓</span>1 project</li>
        <li><span class="cg-10__check">✓</span>10K monthly events</li>
        <li><span class="cg-10__check">✓</span>Community support</li>
        <li class="cg-10__features-off"><span class="cg-10__check cg-10__check--off">✕</span>Custom domains</li>
        <li class="cg-10__features-off"><span class="cg-10__check cg-10__check--off">✕</span>Team seats</li>
      </ul>
      <a href="#" class="cg-10__cta cg-10__cta--ghost">Start free</a>
    </article>

    <article class="cg-10__card cg-10__card--featured">
      <span class="cg-10__ribbon">Most Popular</span>
      <header class="cg-10__cardhead">
        <span class="cg-10__plan">Pro</span>
        <span class="cg-10__planhint">For growing teams</span>
      </header>
      <div class="cg-10__price-wrap">
        <span class="cg-10__currency">$</span>
        <span class="cg-10__price">24</span>
        <span class="cg-10__period">/mo</span>
      </div>
      <p class="cg-10__tagline">Everything in Starter, plus the good stuff.</p>
      <ul class="cg-10__features">
        <li><span class="cg-10__check">✓</span>Unlimited projects</li>
        <li><span class="cg-10__check">✓</span>1M monthly events</li>
        <li><span class="cg-10__check">✓</span>Priority support</li>
        <li><span class="cg-10__check">✓</span>Custom domains</li>
        <li><span class="cg-10__check">✓</span>5 team seats</li>
      </ul>
      <a href="#" class="cg-10__cta cg-10__cta--primary">Start 14-day trial →</a>
    </article>

    <article class="cg-10__card">
      <header class="cg-10__cardhead">
        <span class="cg-10__plan">Enterprise</span>
        <span class="cg-10__planhint">For scale</span>
      </header>
      <div class="cg-10__price-wrap">
        <span class="cg-10__custom">Custom</span>
      </div>
      <p class="cg-10__tagline">Everything in Pro, plus SLAs and SSO.</p>
      <ul class="cg-10__features">
        <li><span class="cg-10__check">✓</span>Unlimited everything</li>
        <li><span class="cg-10__check">✓</span>Dedicated CSM</li>
        <li><span class="cg-10__check">✓</span>99.99% SLA</li>
        <li><span class="cg-10__check">✓</span>SSO + SAML</li>
        <li><span class="cg-10__check">✓</span>Custom contracts</li>
      </ul>
      <a href="#" class="cg-10__cta cg-10__cta--ghost">Contact sales</a>
    </article>

  </div>
</div>
```
## CSS
```css
.cg-10,
.cg-10 *,
.cg-10 *::before,
.cg-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-10 ::selection {
  background: #7c3aed;
  color: #fff;
}

.cg-10 {
  --bg: #fafafa;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --accent: #7c3aed;
  --accent-soft: #ede9fe;
  --price-size: clamp(2.6rem,5.5vw,4rem);
  min-height: 100vh;
  background: var(--bg);
  padding: clamp(32px,4vw,64px) clamp(20px,3vw,48px);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.cg-10__head {
  text-align: center;
  margin-bottom: clamp(32px,4vw,56px);
  max-width: 600px;
}

.cg-10__kicker {
  display: inline-block;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 5px 12px;
  border-radius: 999px;
  margin-bottom: 14px;
}

.cg-10__title {
  font-size: clamp(1.8rem,3.4vw,2.6rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
}

.cg-10__sub {
  font-size: clamp(.92rem,1.1vw,1.05rem);
  color: var(--muted);
  margin-top: 10px;
  line-height: 1.5;
}

.cg-10__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: clamp(16px,2vw,28px);
  width: 100%;
  max-width: 1080px;
  align-items: stretch;
}

.cg-10__card {
  position: relative;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: clamp(24px,2.4vw,32px);
  display: flex;
  flex-direction: column;
  transition: transform .25s ease,box-shadow .25s ease;
}

.cg-10__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 32px -16px rgba(15,23,42,.18);
}

.cg-10__card--featured {
  border: 2px solid var(--accent);
  transform: scale(1.04);
  box-shadow: 0 24px 48px -20px rgba(124,58,237,.32);
  z-index: 1;
}

.cg-10__card--featured:hover {
  transform: scale(1.04) translateY(-4px);
}

.cg-10__ribbon {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--accent);
  color: #fff;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 999px;
  white-space: nowrap;
}

.cg-10__cardhead {
  margin-bottom: 18px;
}

.cg-10__plan {
  display: block;
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cg-10__planhint {
  display: block;
  font-size: .84rem;
  color: var(--muted);
  margin-top: 4px;
}

.cg-10__price-wrap {
  display: flex;
  align-items: baseline;
  gap: 2px;
  margin-bottom: 8px;
  line-height: 1;
}

.cg-10__currency {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--muted);
  align-self: flex-start;
  margin-top: 8px;
}

.cg-10__price {
  font-size: var(--price-size);
  font-weight: 900;
  letter-spacing: -.04em;
  line-height: 1;
}

.cg-10__period {
  font-size: 1rem;
  font-weight: 600;
  color: var(--muted);
}

.cg-10__custom {
  font-size: clamp(2rem,4vw,2.8rem);
  font-weight: 900;
  letter-spacing: -.02em;
  line-height: 1;
}

.cg-10__tagline {
  font-size: .92rem;
  color: var(--muted);
  margin: 14px 0 22px;
  line-height: 1.45;
}

.cg-10__features {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 11px;
  flex: 1;
  margin-bottom: 24px;
}

.cg-10__features li {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: .94rem;
  color: var(--ink);
}

.cg-10__features-off {
  color: var(--muted);
}

.cg-10__check {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: .72rem;
  font-weight: 800;
  flex-shrink: 0;
}

.cg-10__check--off {
  background: var(--line);
  color: var(--muted);
}

.cg-10__cta {
  display: block;
  text-align: center;
  padding: 13px 20px;
  border-radius: 10px;
  font-weight: 700;
  font-size: .94rem;
  text-decoration: none;
  transition: background .25s,color .25s,border-color .25s;
  margin-top: auto;
}

.cg-10__cta--primary {
  background: var(--accent);
  color: #fff;
}

.cg-10__cta--primary:hover {
  background: #6d28d9;
}

.cg-10__cta--ghost {
  background: transparent;
  color: var(--ink);
  border: 1.5px solid var(--line);
}

.cg-10__cta--ghost:hover {
  border-color: var(--accent);
  color: var(--accent);
}

@media (max-width: 860px) {
  .cg-10__grid {
    grid-template-columns: 1fr;
    max-width: 480px;
  }

  .cg-10__card--featured {
    transform: none;
    order: -1;
  }

  .cg-10__card--featured:hover {
    transform: translateY(-4px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-10__card,
    .cg-10__cta {
    transition: none;
  }
}
```
