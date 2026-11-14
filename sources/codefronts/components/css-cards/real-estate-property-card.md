---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/real-estate-property-card/"
title: "Real Estate Property Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Property listing tile with a CSS-drawn townhouse under a golden-hour sky, NEW badge, save-heart, price, address, specs list, and listing agent block."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate Property Card
Source: https://codefronts.com/components/css-cards/real-estate-property-card/

Property listing tile with a CSS-drawn townhouse under a golden-hour sky, NEW badge, save-heart, price, address, specs list, and listing agent block.
## HTML
```html
<section class="card-04" aria-label="Property listing">
  <article class="card-04__card">
    <div class="card-04__hero">
      <img class="card-04__img" src="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=80&auto=format&fit=crop" alt="142 Elm Street exterior" loading="lazy" decoding="async">
      <div class="card-04__hero-shade" aria-hidden="true"></div>
      <div class="card-04__badges">
        <span class="card-04__badge card-04__badge--hot">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg>
          HOT LISTING
        </span>
        <span class="card-04__badge card-04__badge--tour">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 2"/></svg>
          3D TOUR
        </span>
      </div>
      <button type="button" class="card-04__save" aria-label="Save listing">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
        <span class="card-04__save-count">1,284</span>
      </button>
      <button type="button" class="card-04__share" aria-label="Share">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"/></svg>
      </button>
      <div class="card-04__gallery-dots" aria-hidden="true">
        <span class="card-04__gallery-dot card-04__gallery-dot--active"></span>
        <span class="card-04__gallery-dot"></span>
        <span class="card-04__gallery-dot"></span>
        <span class="card-04__gallery-dot"></span>
        <span class="card-04__gallery-count">1 / 24</span>
      </div>
      <div class="card-04__market">
        <span class="card-04__market-dot" aria-hidden="true"></span>
        3 days on market
      </div>
    </div>

    <div class="card-04__body">
      <div class="card-04__pricebar">
        <div>
          <div class="card-04__price-row">
            <span class="card-04__price">$1,285,000</span>
            <span class="card-04__delta">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
              −$15K
            </span>
          </div>
          <p class="card-04__zest">Zestimate® $1.31M · $758/mo est.</p>
        </div>
        <div class="card-04__mortgage">
          <span class="card-04__mortgage-label">Mo. payment</span>
          <span class="card-04__mortgage-val">$7,842</span>
        </div>
      </div>

      <address class="card-04__addr">
        <h4 class="card-04__addr-line">142 Elm Street, Unit 3B</h4>
        <p class="card-04__addr-city">Brooklyn Heights, NY 11201</p>
      </address>

      <ul class="card-04__specs">
        <li>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 20V8h20v12"/><path d="M2 16h20"/><rect x="6" y="10" width="4" height="4"/><rect x="14" y="10" width="4" height="4"/></svg>
          <strong>3</strong> bed
        </li>
        <li>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M4 10h16v4a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/></svg>
          <strong>2</strong> bath
        </li>
        <li>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3h18v18H3z"/><path d="M3 12h18M12 3v18"/></svg>
          <strong>1,240</strong> sqft
        </li>
        <li>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2s8 4 8 10-8 10-8 10S4 18 4 12s8-10 8-10z"/></svg>
          Built <strong>1899</strong>
        </li>
      </ul>

      <div class="card-04__scores">
        <div class="card-04__score">
          <div class="card-04__score-ring">
            <svg width="34" height="34" viewBox="0 0 36 36" aria-hidden="true">
              <circle cx="18" cy="18" r="15" fill="none" stroke="rgba(0,0,0,0.06)" stroke-width="3"/>
              <circle cx="18" cy="18" r="15" fill="none" stroke="#059669" stroke-width="3" stroke-dasharray="87 100" stroke-linecap="round" transform="rotate(-90 18 18)"/>
            </svg>
            <span class="card-04__score-num">92</span>
          </div>
          <div class="card-04__score-text">
            <span class="card-04__score-label">Walk score</span>
            <span class="card-04__score-sub">Walker's paradise</span>
          </div>
        </div>
        <div class="card-04__score">
          <div class="card-04__score-ring">
            <svg width="34" height="34" viewBox="0 0 36 36" aria-hidden="true">
              <circle cx="18" cy="18" r="15" fill="none" stroke="rgba(0,0,0,0.06)" stroke-width="3"/>
              <circle cx="18" cy="18" r="15" fill="none" stroke="#3b82f6" stroke-width="3" stroke-dasharray="78 100" stroke-linecap="round" transform="rotate(-90 18 18)"/>
            </svg>
            <span class="card-04__score-num">78</span>
          </div>
          <div class="card-04__score-text">
            <span class="card-04__score-label">Transit</span>
            <span class="card-04__score-sub">Excellent</span>
          </div>
        </div>
      </div>

      <div class="card-04__foot">
        <div class="card-04__agent">
          <span class="card-04__avatar">SC</span>
          <div class="card-04__agent-text">
            <span class="card-04__agent-name">
              Sarah Chen
              <svg class="card-04__verified" role="img" aria-label="Verified" width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="card-04__agent-role">Compass · Responds &lt; 1h</span>
          </div>
        </div>
        <div class="card-04__ctas">
          <button type="button" class="card-04__cta-alt">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            Tour
          </button>
          <button type="button" class="card-04__cta">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            Contact agent
          </button>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-04 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(59, 130, 246, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(234, 88, 12, 0.04) 0%, transparent 45%), linear-gradient(180deg, #fef3e1 0%, #f4dcb3 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #3b82f6;
  --accent: #3b82f6;
}

.card-04 *,
.card-04 *::before,
.card-04 *::after {
  box-sizing: border-box;
}

.card-04__card {
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(80, 60, 20, 0.24), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s;
}

.card-04__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -30px rgba(80, 60, 20, 0.32);
}
/* ── hero ── */

.card-04__hero {
  position: relative;
  aspect-ratio: 5/3;
  overflow: hidden;
  background: #f4dcb3;
}

.card-04__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}

.card-04__card:hover .card-04__img {
  transform: scale(1.05);
}

.card-04__hero-shade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0) 60%, rgba(0,0,0,0.4) 100%), linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.15) 20%, transparent 30%);
  pointer-events: none;
}

.card-04__badges {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  max-width: calc(100% - 100px);
}

.card-04__badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 8px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 5px;
}

.card-04__badge--hot {
  background: linear-gradient(180deg, #ea580c 0%, #c2410c 100%);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 0 2px 5px rgba(234, 88, 12, 0.35);
}

.card-04__badge--tour {
  background: rgba(59, 130, 246, 0.92);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.16);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.card-04__save {
  position: absolute;
  top: 12px;
  right: 12px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 5px 10px 5px 8px;
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #1a1a1a;
  font: 700 11px 'Inter', sans-serif;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, transform 0.18s;
}

.card-04__save:hover {
  color: #dc2626;
  transform: scale(1.05);
}

.card-04__save:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-04__save-count {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-variant-numeric: tabular-nums;
}

.card-04__share {
  position: absolute;
  top: 52px;
  right: 12px;
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 50%;
  color: #1a1a1a;
  cursor: pointer;
  transition: background 0.18s, color 0.18s;
}

.card-04__share:hover {
  color: #3b82f6;
}

.card-04__share:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* gallery pagination */

.card-04__gallery-dots {
  position: absolute;
  bottom: 12px;
  left: 12px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px 4px 6px;
  background: rgba(0, 0, 0, 0.55);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border-radius: 999px;
}

.card-04__gallery-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  transition: background 0.18s;
}

.card-04__gallery-dot--active {
  width: 16px;
  border-radius: 999px;
  background: #fff;
}

.card-04__gallery-count {
  margin-left: 4px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.02em;
  font-variant-numeric: tabular-nums;
}
/* days on market indicator */

.card-04__market {
  position: absolute;
  bottom: 12px;
  right: 12px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 9px;
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border-radius: 999px;
  color: #059669;
  font: 700 10px 'Inter', sans-serif;
  letter-spacing: -0.005em;
  border: 1px solid rgba(255, 255, 255, 0.6);
}

.card-04__market-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
  animation: card-04-pulse 2s ease-in-out infinite;
}
/* ── body ── */

.card-04__body {
  padding: 18px 20px 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
/* price row */

.card-04__pricebar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  background: linear-gradient(180deg, #fafafd 0%, #f4f4f0 100%);
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 14px;
}

.card-04__price-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 4px;
}

.card-04__price {
  font-size: 24px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.03em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-04__delta {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  color: #059669;
  padding: 2px 7px;
  background: rgba(52, 211, 153, 0.14);
  border-radius: 999px;
}

.card-04__zest {
  font-size: 10.5px;
  color: #6b6b7c;
  margin: 0;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}

.card-04__mortgage {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 1px;
}

.card-04__mortgage-label {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.10em;
  color: #9ca3af;
  text-transform: uppercase;
}

.card-04__mortgage-val {
  font-size: 15px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
/* address */

.card-04__addr {
  font-style: normal;
}

.card-04__addr-line {
  font-size: 16px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 2px;
  letter-spacing: -0.015em;
}

.card-04__addr-city {
  font-size: 12.5px;
  color: #6b6459;
  margin: 0;
}
/* specs */

.card-04__specs {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px 10px;
}

.card-04__specs li {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 12px;
  color: #4b4b57;
  padding: 5px 10px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 999px;
  font-variant-numeric: tabular-nums;
}

.card-04__specs li strong {
  color: #1a1a1a;
  font-weight: 800;
}

.card-04__specs svg {
  color: #9ca3af;
  flex-shrink: 0;
}
/* scores */

.card-04__scores {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding: 12px;
  background: linear-gradient(180deg, #fff 0%, #fafaf7 100%);
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 14px;
}

.card-04__score {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-04__score-ring {
  position: relative;
  width: 34px;
  height: 34px;
  flex-shrink: 0;
}

.card-04__score-num {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 11px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.card-04__score-text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.card-04__score-label {
  font-size: 11px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}

.card-04__score-sub {
  font-size: 10px;
  color: #6b6b7c;
  letter-spacing: -0.005em;
}
/* foot */

.card-04__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px dashed rgba(0, 0, 0, 0.08);
}

.card-04__agent {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.card-04__avatar {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #ea580c, #7c2d12);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  border: 1.5px solid #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  letter-spacing: -0.01em;
  flex-shrink: 0;
}

.card-04__agent-text {
  display: flex;
  flex-direction: column;
  gap: 0;
  min-width: 0;
}

.card-04__agent-name {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 12px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.005em;
}

.card-04__agent-role {
  font-size: 10px;
  color: #059669;
  font-weight: 700;
  letter-spacing: -0.005em;
}

.card-04__ctas {
  display: flex;
  gap: 4px;
  flex-shrink: 0;
}

.card-04__cta,
.card-04__cta-alt {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  min-height: 34px;
  padding: 7px 12px;
  border-radius: 999px;
  font: 700 11.5px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: transform 0.18s, background 0.18s;
  border: 0;
}

.card-04__cta {
  background: linear-gradient(180deg, #1e1e2c 0%, #06070c 100%);
  color: #fff;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.14) inset;
}

.card-04__cta:hover {
  background: linear-gradient(180deg, #3b82f6 0%, #1e40af 100%);
  transform: translateY(-1px);
}

.card-04__cta-alt {
  background: rgba(0, 0, 0, 0.04);
  color: #1a1a1a;
}

.card-04__cta-alt:hover {
  background: rgba(0, 0, 0, 0.08);
  transform: translateY(-1px);
}

.card-04__cta:focus-visible,
.card-04__cta-alt:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-04-pulse {
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
  .card-04__card,
    .card-04__img,
    .card-04__save,
    .card-04__cta,
    .card-04__cta-alt {
    transition: none;
  }

  .card-04__card:hover {
    transform: none;
  }

  .card-04__card:hover .card-04__img {
    transform: none;
  }

  .card-04__save:hover,
    .card-04__cta:hover,
    .card-04__cta-alt:hover {
    transform: none;
  }

  .card-04__market-dot {
    animation: none;
  }
}
```
