---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/bento-pricing-grid/"
title: "Bento Pricing Grid"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Apple-style bento layout — the recommended Pro tile dominates one large quadrant, with stat / quote / pill cells fanning out."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Pricing Grid
Source: https://codefronts.com/layouts/css-pricing-sections/bento-pricing-grid/

Apple-style bento layout — the recommended Pro tile dominates one large quadrant, with stat / quote / pill cells fanning out. Coral and rose tones. Each tile is its own <article> with semantic content; the layout uses CSS Grid named areas.
## HTML
```html
<section class="ps-07" aria-label="Pricing">
  <header class="ps-07__head">
    <h2>Pricing in tiles, not tiers.</h2>
    <p>One canvas, three offers, and the proof points that make the choice obvious.</p>
  </header>
  <div class="ps-07__grid">
    <article class="ps-07__tile ps-07__pro">
      <span class="ps-07__pill">Recommended</span>
      <h3>Pro</h3>
      <div class="ps-07__price"><em>$</em>34<span>/mo</span></div>
      <ul>
        <li>Unlimited projects</li>
        <li>100 GB storage</li>
        <li>Priority support</li>
        <li>Custom domains</li>
      </ul>
      <a class="ps-07__cta" href="#pro">Choose Pro →</a>
    </article>
    <article class="ps-07__tile ps-07__free">
      <h3>Free</h3>
      <div class="ps-07__price"><em>$</em>0<span>forever</span></div>
      <p>Build something small, ship it, keep it free.</p>
      <a class="ps-07__cta-sm" href="#free">Start free →</a>
    </article>
    <article class="ps-07__tile ps-07__stat">
      <span class="ps-07__stat-num">14k+</span>
      <span class="ps-07__stat-lbl">teams pay for Pro every month</span>
    </article>
    <article class="ps-07__tile ps-07__team">
      <h3>Team</h3>
      <div class="ps-07__price"><em>$</em>99<span>/mo</span></div>
      <p>Roles, billing, and audit logs for growing companies.</p>
      <a class="ps-07__cta-sm" href="#team">Choose Team →</a>
    </article>
    <article class="ps-07__tile ps-07__quote">
      <p>“We tried five tools. This was the only one priced like a partner, not a tax.”</p>
      <cite>— Lior, CTO at Pulse</cite>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-07 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #1a0d0d;
  color: #ffe7df;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-07__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-07__head h2 {
  font-size: clamp(22px, 3.4vw, 34px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #ffd0bf;
}

.ps-07__head p {
  color: #b89180;
  margin: 0 auto;
  max-width: 480px;
  font-size: 14px;
}

.ps-07__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: auto auto;
  grid-template-areas: "pro pro free stat" "pro pro team quote";
  gap: 14px;
  max-width: 980px;
  margin: 0 auto;
}

.ps-07__tile {
  background: #2a1612;
  border: 1px solid rgba(255,108,79,0.15);
  border-radius: 16px;
  padding: 22px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 130px;
}

.ps-07__pro {
  grid-area: pro;
  background: linear-gradient(135deg, #ff6b4a 0%, #f43f5e 100%);
  border: 0;
  color: #1a0d0d;
  position: relative;
  overflow: hidden;
}

.ps-07__pro::after {
  content: '';
  position: absolute;
  right: -40px;
  bottom: -40px;
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 70%);
  pointer-events: none;
}

.ps-07__pill {
  display: inline-block;
  align-self: flex-start;
  background: #1a0d0d;
  color: #ff6b4a;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 5px 11px;
  border-radius: 999px;
  margin-bottom: 8px;
}

.ps-07__tile h3 {
  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 6px;
  opacity: 0.8;
}

.ps-07__pro h3 {
  color: #1a0d0d;
  opacity: 1;
  font-weight: 700;
}

.ps-07__price {
  font-size: clamp(36px, 5vw, 56px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
  margin-bottom: 12px;
}

.ps-07__price em {
  font-size: 0.5em;
  font-style: normal;
  vertical-align: top;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-07__price span {
  font-size: 0.28em;
  font-weight: 500;
  opacity: 0.7;
  margin-left: 6px;
}

.ps-07__pro ul {
  list-style: none;
  padding: 0;
  margin: 0 0 18px;
  font-size: 13px;
  line-height: 1.9;
}

.ps-07__pro ul li::before {
  content: '✓';
  display: inline-block;
  width: 20px;
  font-weight: 700;
}

.ps-07__tile p {
  font-size: 13px;
  line-height: 1.5;
  color: #b89180;
  margin: 0 0 12px;
}

.ps-07__cta,
.ps-07__cta-sm {
  display: inline-block;
  padding: 10px 16px;
  border-radius: 8px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid currentColor;
  color: inherit;
  transition: background 0.18s, color 0.18s;
}

.ps-07__cta {
  background: #1a0d0d;
  color: #ff6b4a;
  border-color: #1a0d0d;
  align-self: flex-start;
}

.ps-07__cta:hover {
  background: transparent;
  color: #fff;
  border-color: #fff;
}

.ps-07__cta-sm {
  color: #ff6b4a;
  border-color: rgba(255,108,79,0.4);
  padding: 8px 14px;
  align-self: flex-start;
  font-size: 12.5px;
}

.ps-07__cta-sm:hover {
  background: #ff6b4a;
  color: #1a0d0d;
  border-color: #ff6b4a;
}

.ps-07__cta:focus-visible,
.ps-07__cta-sm:focus-visible {
  outline: 2px solid #ffe7df;
  outline-offset: 3px;
}

.ps-07__stat {
  grid-area: stat;
  align-items: flex-start;
  background: #2a1612;
}

.ps-07__stat-num {
  font-size: clamp(36px, 5vw, 50px);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #ff6b4a;
  background: linear-gradient(180deg, #ffb37a, #ff6b4a);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-07__stat-lbl {
  font-size: 12px;
  color: #b89180;
  line-height: 1.4;
}

.ps-07__team {
  grid-area: team;
}

.ps-07__free {
  grid-area: free;
}

.ps-07__quote {
  grid-area: quote;
  background: linear-gradient(135deg, #f43f5e 0%, #be123c 100%);
  color: #1a0d0d;
  border: 0;
}

.ps-07__quote p {
  font-style: italic;
  color: #1a0d0d;
  font-weight: 500;
  line-height: 1.5;
  font-size: 13px;
  opacity: 0.92;
}

.ps-07__quote cite {
  font-style: normal;
  font-size: 11px;
  color: rgba(26,13,13,0.7);
  letter-spacing: 0.05em;
}

@media (max-width: 820px) {
  .ps-07__grid {
    grid-template-columns: 1fr 1fr;
    grid-template-areas: "pro pro" "free team" "stat quote";
  }
}

@media (max-width: 520px) {
  .ps-07__grid {
    grid-template-columns: 1fr;
    grid-template-areas: "pro" "free" "team" "stat" "quote";
  }
}
```
