---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/social-proof-pricing/"
title: "Social Proof Pricing"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "A scrolling logo wall above the pricing tiers — social proof first, decision second."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Proof Pricing
Source: https://codefronts.com/layouts/css-pricing-sections/social-proof-pricing/

A scrolling logo wall above the pricing tiers — social proof first, decision second. Slate background with lime accent on the recommended plan. Logos scroll in a seamless marquee using a duplicated track.
## HTML
```html
<section class="ps-18" aria-label="Pricing">
  <div class="ps-18__marquee" aria-label="Customers using this product">
    <div class="ps-18__track">
      <span class="ps-18__logo">◇ NORTHWIND</span>
      <span class="ps-18__logo">▲ APEX.IO</span>
      <span class="ps-18__logo">★ PULSE</span>
      <span class="ps-18__logo">⬣ HEXLAB</span>
      <span class="ps-18__logo">◯ ORBITA</span>
      <span class="ps-18__logo">◤ FLINT</span>
      <span class="ps-18__logo">⬢ MERIDIAN</span>
      <span class="ps-18__logo">◇ NORTHWIND</span>
      <span class="ps-18__logo">▲ APEX.IO</span>
      <span class="ps-18__logo">★ PULSE</span>
      <span class="ps-18__logo">⬣ HEXLAB</span>
      <span class="ps-18__logo">◯ ORBITA</span>
      <span class="ps-18__logo">◤ FLINT</span>
      <span class="ps-18__logo">⬢ MERIDIAN</span>
    </div>
  </div>
  <header class="ps-18__head">
    <span class="ps-18__rating" aria-label="Rated 4.9 out of 5">★★★★★ 4.9 from 12,400 teams</span>
    <h2>Pricing teams actually pay for.</h2>
  </header>
  <div class="ps-18__grid">
    <article class="ps-18__card">
      <h3>Free</h3>
      <div class="ps-18__price"><em>$</em>0<span>forever</span></div>
      <ul>
        <li>1 project</li>
        <li>5 GB storage</li>
        <li>Community</li>
      </ul>
      <a class="ps-18__cta" href="#free">Start free</a>
    </article>
    <article class="ps-18__card ps-18__best">
      <span class="ps-18__tag">Most teams pick this</span>
      <h3>Team</h3>
      <div class="ps-18__price"><em>$</em>32<span>/mo</span></div>
      <ul>
        <li>Unlimited projects</li>
        <li>Priority support</li>
        <li>SSO + roles</li>
      </ul>
      <a class="ps-18__cta ps-18__cta-pri" href="#team">Choose Team</a>
    </article>
    <article class="ps-18__card">
      <h3>Enterprise</h3>
      <div class="ps-18__price"><em>$</em>0<span>custom</span></div>
      <ul>
        <li>Everything in Team</li>
        <li>Dedicated CSM</li>
        <li>SLA 99.99%</li>
      </ul>
      <a class="ps-18__cta" href="#ent">Talk to sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-18 {
  position: relative;
  overflow: hidden;
  contain: layout paint;
  padding: clamp(20px, 4vw, 36px) clamp(20px, 4vw, 40px) clamp(28px, 5vw, 48px);
  width: 100%;
  min-height: 100vh;
  background: #0f172a;
  color: #e2e8f0;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-18__marquee {
  position: relative;
  overflow: hidden;
  contain: layout paint;
  border-block: 1px solid rgba(163,230,53,0.18);
  margin: 0 calc(-1 * clamp(20px, 4vw, 40px)) clamp(20px, 4vw, 32px);
  padding: 14px 0;
  background: rgba(15,23,42,0.6);
  /* max-width containment: without this, the child .ps-18__track's
       width: max-content (needed for the seamless marquee loop) propagates
       up through this block wrapper — some layout engines size the wrapper
       to child's intrinsic width instead of parent's content-box, causing
       the whole section to grow to ~2045px and triggering horizontal body
       scroll. Locking max-width to 100vw + min-width to 0 keeps the marquee
       bounded regardless of child intrinsic width. overflow: hidden then
       clips the marquee correctly. */
  max-width: 100vw;
  min-width: 0;
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent);
  mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent);
}

.ps-18__track {
  display: flex;
  gap: 56px;
  white-space: nowrap;
  animation: ps-18-roll 28s linear infinite;
  width: max-content;
  will-change: transform;
}

@keyframes ps-18-roll {
  to {
    transform: translateX(-50%);
  }
}

.ps-18__logo {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #94a3b8;
  flex-shrink: 0;
}

.ps-18__head {
  text-align: center;
  margin-bottom: clamp(20px, 4vw, 32px);
}

.ps-18__rating {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: #a3e635;
  margin-bottom: 10px;
}

.ps-18__head h2 {
  font-size: clamp(24px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0;
  color: #fff;
}

.ps-18__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  max-width: 940px;
  margin: 0 auto;
  align-items: center;
}

.ps-18__card {
  position: relative;
  background: #1e293b;
  border: 1px solid rgba(163,230,53,0.12);
  border-radius: 12px;
  padding: 22px 20px 18px;
  display: flex;
  flex-direction: column;
}

.ps-18__best {
  background: linear-gradient(180deg, #1e293b, #243f1a);
  border-color: #a3e635;
  box-shadow: 0 0 0 1px #a3e635 inset, 0 14px 36px rgba(163,230,53,0.18);
}

.ps-18__tag {
  position: absolute;
  top: -11px;
  left: 50%;
  transform: translateX(-50%);
  background: #a3e635;
  color: #0f172a;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 999px;
}

.ps-18__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #cbd5e1;
}

.ps-18__best h3 {
  color: #d9f99d;
}

.ps-18__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  color: #fff;
}

.ps-18__price em {
  font-size: 0.5em;
  font-style: normal;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-18__price span {
  font-size: 0.32em;
  font-weight: 500;
  opacity: 0.65;
  margin-left: 6px;
}

.ps-18__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 18px;
  flex: 1;
  font-size: 13px;
  line-height: 1.95;
  color: #b8c1d1;
}

.ps-18__card ul li::before {
  content: '✓';
  color: #a3e635;
  display: inline-block;
  width: 20px;
  font-weight: 700;
}

.ps-18__cta {
  display: block;
  text-align: center;
  padding: 10px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  background: rgba(163,230,53,0.1);
  color: #a3e635;
  border: 1px solid rgba(163,230,53,0.28);
  transition: background 0.18s, color 0.18s;
}

.ps-18__cta-pri {
  background: #a3e635;
  color: #0f172a;
  border-color: #a3e635;
}

.ps-18__cta:hover {
  background: #a3e635;
  color: #0f172a;
}

.ps-18__cta-pri:hover {
  background: #d9f99d;
}

.ps-18__cta:focus-visible {
  outline: 2px solid #a3e635;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-18__grid {
    grid-template-columns: 1fr;
    max-width: 360px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-18__track {
    animation: none;
  }
}
```
