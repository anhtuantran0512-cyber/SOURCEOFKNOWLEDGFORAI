---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/pricing-tier-card/"
title: "Pricing Tier Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Three-tier SaaS pricing row with a lifted, glowing \"Most Popular\" middle plan. Stacks to one column under 640px, indigo accent, real feature lists."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pricing Tier Card
Source: https://codefronts.com/components/css-cards/pricing-tier-card/

Three-tier SaaS pricing row with a lifted, glowing "Most Popular" middle plan. Stacks to one column under 640px, indigo accent, real feature lists.
## HTML
```html
<section class="card-02" aria-label="Pricing">
  <header class="card-02__head">
    <div class="card-02__eyebrow">
      <span class="card-02__eye-dot" aria-hidden="true"></span>
      PRICING · 30-DAY MONEY-BACK GUARANTEE
    </div>
    <h3 class="card-02__title">Simple pricing, ship faster.</h3>
    <p class="card-02__sub">Start free, upgrade as you grow. Cancel anytime.</p>
    <div class="card-02__toggle-row">
      <div class="card-02__toggle" role="tablist" aria-label="Billing period">
        <button type="button" role="tab" aria-selected="false" class="card-02__toggle-btn">Monthly</button>
        <button type="button" role="tab" aria-selected="true" class="card-02__toggle-btn card-02__toggle-btn--active">
          Yearly
          <span class="card-02__toggle-badge">−20%</span>
        </button>
      </div>
    </div>
  </header>

  <div class="card-02__row">

    <article class="card-02__card">
      <div class="card-02__mark card-02__mark--starter" aria-hidden="true">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h18M3 6h18M3 14h18M3 18h18"/></svg>
      </div>
      <div class="card-02__tier-row">
        <p class="card-02__tier">Starter</p>
        <span class="card-02__free">Free forever</span>
      </div>
      <p class="card-02__sub-line">For solo builders shipping their first thing.</p>
      <div class="card-02__price-block">
        <div class="card-02__price">
          <span class="card-02__curr">$</span>
          <span class="card-02__amt">0</span>
          <span class="card-02__per">/mo</span>
        </div>
        <p class="card-02__price-note">No card required</p>
      </div>
      <a class="card-02__cta" href="#starter">
        Get started free
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <div class="card-02__divider" aria-hidden="true"><span>What's included</span></div>
      <ul class="card-02__feats">
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Up to 3 projects</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>5 GB storage</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Community support</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Basic analytics</li>
      </ul>
    </article>

    <article class="card-02__card card-02__card--pop">
      <div class="card-02__aura" aria-hidden="true"></div>
      <span class="card-02__badge">
        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        MOST POPULAR
      </span>
      <div class="card-02__mark card-02__mark--pop" aria-hidden="true">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      </div>
      <div class="card-02__tier-row">
        <p class="card-02__tier">Business</p>
        <span class="card-02__save">Save $84</span>
      </div>
      <p class="card-02__sub-line">Everything growing teams need to ship together.</p>
      <div class="card-02__price-block">
        <div class="card-02__price">
          <span class="card-02__curr">$</span>
          <span class="card-02__amt">23</span>
          <span class="card-02__per">/mo</span>
        </div>
        <p class="card-02__price-note">
          <span class="card-02__strike">$29/mo</span>
          <span>· billed $276/yr</span>
        </p>
      </div>
      <a class="card-02__cta card-02__cta--pop" href="#business">
        Start 14-day trial
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <div class="card-02__proof">
        <div class="card-02__avatars" aria-hidden="true">
          <span class="card-02__av card-02__av--1">AR</span>
          <span class="card-02__av card-02__av--2">JL</span>
          <span class="card-02__av card-02__av--3">MK</span>
          <span class="card-02__av card-02__av--4">+9k</span>
        </div>
        <span class="card-02__proof-text">12,483 teams shipping</span>
      </div>
      <div class="card-02__divider" aria-hidden="true"><span>Everything in Starter, plus</span></div>
      <ul class="card-02__feats">
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Unlimited projects</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>100 GB storage <span class="card-02__feat-new">NEW</span></li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Priority email support</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Team roles &amp; SSO</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>API access · 10k req/day</li>
      </ul>
    </article>

    <article class="card-02__card">
      <div class="card-02__mark card-02__mark--team" aria-hidden="true">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      </div>
      <div class="card-02__tier-row">
        <p class="card-02__tier">Team</p>
        <span class="card-02__custom">Custom</span>
      </div>
      <p class="card-02__sub-line">For scaling teams that need governance.</p>
      <div class="card-02__price-block">
        <div class="card-02__price">
          <span class="card-02__curr">$</span>
          <span class="card-02__amt">63</span>
          <span class="card-02__per">/mo</span>
        </div>
        <p class="card-02__price-note">
          <span class="card-02__strike">$79/mo</span>
          <span>· from 5 seats</span>
        </p>
      </div>
      <a class="card-02__cta" href="#team">
        Contact sales
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
      <div class="card-02__divider" aria-hidden="true"><span>Everything in Business, plus</span></div>
      <ul class="card-02__feats">
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>500 GB storage</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Dedicated success mgr</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Audit logs &amp; SOC 2</li>
        <li><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Custom SLA</li>
      </ul>
    </article>

  </div>

  <footer class="card-02__foot">
    <span class="card-02__trust">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      SOC 2
    </span>
    <span class="card-02__trust">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      GDPR
    </span>
    <span class="card-02__trust">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
      14-day trial · no card
    </span>
    <a href="#compare" class="card-02__compare">
      Compare all plans
      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
    </a>
  </footer>
</section>
```
## CSS
```css
.card-02 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 10%, rgba(99, 102, 241, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 90%, rgba(236, 72, 153, 0.04) 0%, transparent 45%), #faf7f2;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #6366f1;
  --accent: #6366f1;
  --accent-2: #ec4899;
}

.card-02 *,
.card-02 *::before,
.card-02 *::after {
  box-sizing: border-box;
}
/* ── header ── */

.card-02__head {
  width: 100%;
  max-width: 780px;
  margin: 0 auto 22px;
  text-align: center;
}

.card-02__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #6366f1;
  padding: 4px 10px;
  background: rgba(99, 102, 241, 0.08);
  border: 1px solid rgba(99, 102, 241, 0.16);
  border-radius: 999px;
  margin-bottom: 12px;
}

.card-02__eye-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #ec4899;
  box-shadow: 0 0 8px rgba(236, 72, 153, 0.5);
  animation: card-02-pulse 2.2s ease-in-out infinite;
}

.card-02__title {
  font-size: 22px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 4px;
  letter-spacing: -0.025em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-02__sub {
  font-size: 13px;
  color: #6b6b7c;
  margin: 0;
}

.card-02__toggle-row {
  display: flex;
  justify-content: center;
  margin-top: 14px;
}

.card-02__toggle {
  display: inline-flex;
  gap: 2px;
  padding: 3px;
  background: #ede8dc;
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 999px;
}

.card-02__toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 32px;
  padding: 6px 16px;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: #6b6b7c;
  font: 700 12px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: color 0.18s, background 0.18s, box-shadow 0.18s;
}

.card-02__toggle-btn:hover {
  color: #1a1a1a;
}

.card-02__toggle-btn--active {
  background: #fff;
  color: #1a1a1a;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.04);
}

.card-02__toggle-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-02__toggle-badge {
  display: inline-flex;
  align-items: center;
  padding: 1px 6px;
  background: linear-gradient(180deg, #34d399, #059669);
  color: #fff;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.06em;
  border-radius: 999px;
  box-shadow: 0 2px 4px rgba(52, 211, 153, 0.3);
}
/* ── row ── */

.card-02__row {
  width: 100%;
  max-width: 780px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
  align-items: stretch;
}
/* ── card ── */

.card-02__card {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 20px 20px 20px;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 20px;
  box-shadow: 0 12px 30px -18px rgba(80, 40, 80, 0.14), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s, border-color 0.35s;
}

.card-02__card:hover {
  transform: translateY(-3px);
  border-color: rgba(0, 0, 0, 0.1);
  box-shadow: 0 24px 44px -18px rgba(80, 40, 80, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}
/* ── popular card variant ── */

.card-02__card--pop {
  background: linear-gradient(180deg, rgba(99, 102, 241, 0.04) 0%, transparent 30%), #fff;
  border: 1.5px solid rgba(99, 102, 241, 0.28);
  box-shadow: 0 24px 44px -18px rgba(99, 102, 241, 0.24), 0 0 0 4px rgba(99, 102, 241, 0.06), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transform: translateY(-6px);
}

.card-02__card--pop:hover {
  transform: translateY(-9px);
  box-shadow: 0 36px 60px -18px rgba(99, 102, 241, 0.34), 0 0 0 4px rgba(99, 102, 241, 0.1), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-02__aura {
  position: absolute;
  top: -60px;
  left: -40px;
  right: -40px;
  height: 140px;
  background: radial-gradient(ellipse at center top, rgba(99, 102, 241, 0.14) 0%, transparent 60%);
  filter: blur(20px);
  pointer-events: none;
  z-index: -1;
}

.card-02__badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 12px;
  background: linear-gradient(180deg, #818cf8 0%, #6366f1 100%);
  color: #fff;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 999px;
  box-shadow: 0 6px 16px rgba(99, 102, 241, 0.35), 0 0 0 3px rgba(255, 255, 255, 0.85);
  white-space: nowrap;
}
/* ── mark icon ── */

.card-02__mark {
  width: 34px;
  height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: linear-gradient(180deg, #f5f4f0 0%, #ece8db 100%);
  color: #6b6b7c;
  border: 1px solid rgba(0, 0, 0, 0.05);
  margin-bottom: 12px;
}

.card-02__mark--pop {
  background: linear-gradient(180deg, #818cf8 0%, #6366f1 100%);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 6px 16px rgba(99, 102, 241, 0.28);
}

.card-02__mark--team {
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  color: #92400e;
  border-color: rgba(146, 64, 14, 0.14);
}
/* ── tier + free/save/custom badges ── */

.card-02__tier-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  margin-bottom: 4px;
}

.card-02__tier {
  font-size: 14px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.01em;
}

.card-02__free,
.card-02__custom {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #059669;
  padding: 2px 7px;
  background: rgba(52, 211, 153, 0.10);
  border: 1px solid rgba(52, 211, 153, 0.22);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-02__custom {
  color: #9a3412;
  background: rgba(234, 88, 12, 0.08);
  border-color: rgba(234, 88, 12, 0.18);
}

.card-02__save {
  display: inline-flex;
  align-items: center;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.10em;
  color: #fff;
  padding: 2px 7px;
  background: linear-gradient(180deg, #34d399, #059669);
  border-radius: 999px;
  box-shadow: 0 2px 4px rgba(52, 211, 153, 0.32);
}

.card-02__sub-line {
  font-size: 11.5px;
  color: #6b6b7c;
  margin: 0 0 14px;
  line-height: 1.4;
  min-height: 32px;
}
/* ── price ── */

.card-02__price-block {
  margin-bottom: 14px;
}

.card-02__price {
  display: inline-flex;
  align-items: flex-start;
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.card-02__curr {
  font-size: 16px;
  font-weight: 700;
  color: #4b4b57;
  margin-top: 6px;
  letter-spacing: -0.01em;
}

.card-02__amt {
  font-size: 42px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.04em;
  line-height: 1;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-02__per {
  font-size: 12.5px;
  color: #9ca3af;
  margin-top: 20px;
  margin-left: 3px;
  letter-spacing: -0.005em;
}

.card-02__price-note {
  font-size: 10.5px;
  color: #9ca3af;
  margin: 3px 0 0;
  letter-spacing: -0.005em;
  display: flex;
  align-items: center;
  gap: 4px;
}

.card-02__strike {
  color: #d4d4d8;
  text-decoration: line-through;
}
/* ── CTAs ── */

.card-02__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  min-height: 40px;
  padding: 10px 14px;
  border-radius: 12px;
  background: rgba(0, 0, 0, 0.04);
  color: #1a1a1a;
  font: 700 12.5px 'Inter', sans-serif;
  text-decoration: none;
  letter-spacing: -0.01em;
  border: 1px solid transparent;
  transition: background 0.18s, transform 0.18s, box-shadow 0.18s;
}

.card-02__cta:hover {
  background: rgba(0, 0, 0, 0.08);
  transform: translateY(-1px);
}

.card-02__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-02__cta--pop {
  background: linear-gradient(180deg, #1e1e2c 0%, #06070c 100%);
  color: #fff;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.14) inset, 0 -1px 0 rgba(255, 255, 255, 0.06) inset;
}

.card-02__cta--pop:hover {
  background: linear-gradient(180deg, #2a2a3c 0%, #0d0d16 100%);
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.32), 0 0 0 1px rgba(255, 255, 255, 0.2) inset, 0 -1px 0 rgba(255, 255, 255, 0.08) inset;
}
/* ── social proof row ── */

.card-02__proof {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 12px;
  padding: 8px 10px;
  background: rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.12);
  border-radius: 10px;
}

.card-02__avatars {
  display: flex;
}

.card-02__av {
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #fff;
  font-size: 8.5px;
  font-weight: 800;
  border: 1.5px solid #fff;
  margin-left: -6px;
  letter-spacing: -0.02em;
}

.card-02__av:first-child {
  margin-left: 0;
}

.card-02__av--1 {
  background: linear-gradient(135deg, #f472b6, #ec4899);
}

.card-02__av--2 {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-02__av--3 {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-02__av--4 {
  background: #4338ca;
  font-size: 8px;
}

.card-02__proof-text {
  font-size: 11px;
  font-weight: 700;
  color: #4338ca;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}
/* ── section divider ── */

.card-02__divider {
  position: relative;
  height: 1px;
  margin: 16px 0 12px;
  background: rgba(0, 0, 0, 0.06);
  text-align: center;
}

.card-02__divider span {
  position: relative;
  top: -7px;
  padding: 0 8px;
  background: #fff;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.10em;
  color: #9ca3af;
  text-transform: uppercase;
}

.card-02__card--pop .card-02__divider span {
  background: linear-gradient(0deg, #fff 50%, rgba(255,255,255,0.98) 100%);
}
/* ── feat list ── */

.card-02__feats {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.card-02__feats li {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: #4b4b57;
  letter-spacing: -0.005em;
}

.card-02__feats svg {
  color: #059669;
  flex-shrink: 0;
  padding: 2px;
  background: rgba(52, 211, 153, 0.14);
  border-radius: 4px;
}

.card-02__feat-new {
  display: inline-flex;
  align-items: center;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.10em;
  color: #ec4899;
  padding: 1px 5px;
  background: rgba(236, 72, 153, 0.10);
  border: 1px solid rgba(236, 72, 153, 0.20);
  border-radius: 4px;
}
/* ── footer trust bar ── */

.card-02__foot {
  width: 100%;
  max-width: 780px;
  margin: 22px auto 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.card-02__trust {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 10.5px;
  font-weight: 700;
  color: #6b6b7c;
  padding: 5px 10px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  letter-spacing: -0.005em;
}

.card-02__trust svg {
  color: #059669;
  flex-shrink: 0;
}

.card-02__compare {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10.5px;
  font-weight: 700;
  color: #4338ca;
  text-decoration: none;
  padding: 5px 10px;
  border-radius: 999px;
  transition: color 0.18s, background 0.18s;
}

.card-02__compare:hover {
  color: #312e81;
  background: rgba(99, 102, 241, 0.06);
}

.card-02__compare:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── mobile ── */

@media (max-width: 780px) {
  .card-02__row {
    grid-template-columns: 1fr;
    max-width: 340px;
  }

  .card-02__card--pop {
    transform: none;
  }

  .card-02__card--pop:hover {
    transform: translateY(-3px);
  }
}

@keyframes card-02-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-02__card,
    .card-02__cta,
    .card-02__toggle-btn,
    .card-02__compare {
    transition: none;
  }

  .card-02__card:hover,
    .card-02__cta:hover,
    .card-02__card--pop:hover {
    transform: none;
  }

  .card-02__eye-dot {
    animation: none;
  }
}
```
