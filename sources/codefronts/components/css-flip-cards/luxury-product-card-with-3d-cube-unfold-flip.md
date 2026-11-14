---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/luxury-product-card-with-3d-cube-unfold-flip/"
title: "Luxury Product Card with 3D Cube Unfold Flip"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A luxury watch product card that opens like a book — the back face hinges in from the right edge rather than the conventional spin-around-center flip."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Luxury Product Card with 3D Cube Unfold Flip
Source: https://codefronts.com/components/css-flip-cards/luxury-product-card-with-3d-cube-unfold-flip/

A luxury watch product card that opens like a book — the back face hinges in from the right edge rather than the conventional spin-around-center flip.
## HTML
```html
<div class="fc-19">
  <div class="fc-19__scene">
    <div class="fc-19__card">
      <div class="fc-19__front">
        <div class="fc-19__brand-row">
          <span class="fc-19__brand-mark">M</span>
          <span class="fc-19__brand-text">MERIDIAN</span>
        </div>
        <div class="fc-19__watch">
          <svg width="180" height="180" viewBox="0 0 200 200" fill="none">
            <defs>
              <linearGradient id="fc-19-bezel" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#fef3c7"/>
                <stop offset="50%" stop-color="#d4af37"/>
                <stop offset="100%" stop-color="#8c6917"/>
              </linearGradient>
              <radialGradient id="fc-19-dial" cx="0.5" cy="0.5" r="0.6">
                <stop offset="0%" stop-color="#1c1c1c"/>
                <stop offset="80%" stop-color="#0a0a0a"/>
              </radialGradient>
            </defs>
            <circle cx="100" cy="100" r="90" fill="url(#fc-19-bezel)"/>
            <circle cx="100" cy="100" r="78" fill="url(#fc-19-dial)"/>
            <circle cx="100" cy="100" r="76" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.4"/>
            <g stroke="#d4af37" stroke-width="2" stroke-linecap="round">
              <line x1="100" y1="32" x2="100" y2="42"/>
              <line x1="100" y1="158" x2="100" y2="168"/>
              <line x1="32" y1="100" x2="42" y2="100"/>
              <line x1="158" y1="100" x2="168" y2="100"/>
            </g>
            <g stroke="#fef3c7" stroke-width="1.2" stroke-linecap="round" opacity="0.7">
              <line x1="151" y1="65" x2="146" y2="69"/>
              <line x1="151" y1="135" x2="146" y2="131"/>
              <line x1="49" y1="65" x2="54" y2="69"/>
              <line x1="49" y1="135" x2="54" y2="131"/>
            </g>
            <line x1="100" y1="100" x2="100" y2="50" stroke="#fef3c7" stroke-width="2.4" stroke-linecap="round"/>
            <line x1="100" y1="100" x2="138" y2="120" stroke="#fef3c7" stroke-width="2" stroke-linecap="round"/>
            <line x1="100" y1="100" x2="80" y2="124" stroke="#d4af37" stroke-width="1" stroke-linecap="round"/>
            <circle cx="100" cy="100" r="3" fill="#d4af37"/>
            <text x="100" y="148" text-anchor="middle" font-family="serif" font-size="7" fill="#d4af37" letter-spacing="2">MERIDIAN</text>
          </svg>
        </div>
        <div class="fc-19__model-label">Heritage Chronograph 1957</div>
        <div class="fc-19__price-row">
          <span class="fc-19__price-amt">$12,400</span>
          <span class="fc-19__price-sub">Limited release</span>
        </div>
        <div class="fc-19__hint">Hover to open ›</div>
      </div>
      <div class="fc-19__back">
        <div class="fc-19__back-tag">Specifications</div>
        <div class="fc-19__back-title">Heritage Chronograph 1957</div>
        <div class="fc-19__spec-grid">
          <div class="fc-19__spec"><span class="fc-19__spec-key">Case</span><span class="fc-19__spec-val">18k Rose Gold · 40 mm</span></div>
          <div class="fc-19__spec"><span class="fc-19__spec-key">Movement</span><span class="fc-19__spec-val">Caliber M-29 Automatic</span></div>
          <div class="fc-19__spec"><span class="fc-19__spec-key">Reserve</span><span class="fc-19__spec-val">72-hour power reserve</span></div>
          <div class="fc-19__spec"><span class="fc-19__spec-key">Water</span><span class="fc-19__spec-val">100 m · screw-down crown</span></div>
          <div class="fc-19__spec"><span class="fc-19__spec-key">Crystal</span><span class="fc-19__spec-val">Domed sapphire · AR coated</span></div>
          <div class="fc-19__spec"><span class="fc-19__spec-key">Strap</span><span class="fc-19__spec-val">Alligator · pin buckle</span></div>
        </div>
        <a class="fc-19__cta" href="#">Reserve this piece ›</a>
        <div class="fc-19__back-foot">12 / 200 cast · made in Switzerland</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-19,
.fc-19 *,
.fc-19 *::before,
.fc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-19 ::selection {
  background: #d4af37;
  color: #0a0a0a;
}

.fc-19 {
  --bg: #080806;
  --gold: #d4af37;
  --gold-light: #fef3c7;
  --ivory: #f5f1e8;
  --card-w: 360px;
  --card-h: 500px;
  font-family: 'Cormorant Garamond','Playfair Display',Georgia,serif;
  background: radial-gradient(ellipse at 50% 30%,#1a1610,#080806 70%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--ivory);
}

.fc-19__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1600px;
}

.fc-19__card {
  width: 100%;
  height: 100%;
  position: relative;
}

.fc-19__front,
.fc-19__back {
  position: absolute;
  inset: 0;
  border-radius: 6px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 36px 32px;
}

.fc-19__front {
  background: linear-gradient(160deg,#1a1610 0%,#0c0a07 100%);
  border: 1px solid rgba(212,175,55,.25);
  box-shadow: inset 0 1px 0 rgba(254,243,199,.06),0 12px 30px rgba(0,0,0,.5);
  transition: opacity .8s cubic-bezier(.4,0,.2,1),transform .8s cubic-bezier(.4,0,.2,1);
  z-index: 1;
}

.fc-19__back {
  background: linear-gradient(160deg,#15110b 0%,#0a0805 100%);
  border: 1px solid rgba(212,175,55,.4);
  box-shadow: 0 16px 40px rgba(0,0,0,.6),inset 0 1px 0 rgba(254,243,199,.1);
  transform: rotateY(-90deg);
  transform-origin: left center;
  backface-visibility: visible;
  -webkit-backface-visibility: visible;
  transition: transform .9s cubic-bezier(.4,0,.2,1);
  z-index: 2;
}

.fc-19__scene:hover .fc-19__back {
  transform: rotateY(0deg);
}

.fc-19__scene:hover .fc-19__front {
  opacity: .5;
  transform: translateX(-3%);
}
/* FRONT styling */

.fc-19__brand-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.fc-19__brand-mark {
  width: 32px;
  height: 32px;
  border: 1px solid var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: serif;
  font-size: 18px;
  color: var(--gold);
  font-weight: 600;
}

.fc-19__brand-text {
  font-size: 11px;
  letter-spacing: .45em;
  color: var(--gold);
  font-family: serif;
  font-weight: 500;
}

.fc-19__watch {
  margin: 4px 0 16px;
}

.fc-19__model-label {
  font-size: 18px;
  color: var(--ivory);
  text-align: center;
  font-style: italic;
  letter-spacing: .02em;
}

.fc-19__price-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  margin-top: 14px;
}

.fc-19__price-amt {
  font-size: 28px;
  font-weight: 500;
  color: var(--gold);
  letter-spacing: .04em;
  font-family: serif;
}

.fc-19__price-sub {
  font-size: 10px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: rgba(245,241,232,.4);
}

.fc-19__hint {
  margin-top: auto;
  font-size: 10px;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: rgba(212,175,55,.5);
  font-family: system-ui,sans-serif;
}
/* BACK styling */

.fc-19__back-tag {
  font-size: 10px;
  letter-spacing: .4em;
  text-transform: uppercase;
  color: var(--gold);
  font-family: system-ui,sans-serif;
  font-weight: 600;
  margin-bottom: 8px;
}

.fc-19__back-title {
  font-size: 20px;
  font-style: italic;
  color: var(--ivory);
  text-align: center;
  margin-bottom: 18px;
  line-height: 1.2;
}

.fc-19__spec-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  margin-bottom: 18px;
}

.fc-19__spec {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(212,175,55,.12);
}

.fc-19__spec:last-child {
  border-bottom: none;
}

.fc-19__spec-key {
  font-size: 9px;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: rgba(212,175,55,.55);
  font-family: system-ui,sans-serif;
  font-weight: 600;
}

.fc-19__spec-val {
  font-size: 13px;
  color: var(--ivory);
  font-family: serif;
}

.fc-19__cta {
  display: block;
  width: 100%;
  padding: 13px 0;
  text-align: center;
  background: linear-gradient(135deg,#d4af37,#b8941f);
  color: #0a0a0a;
  font-size: 11px;
  letter-spacing: .3em;
  text-transform: uppercase;
  font-weight: 600;
  font-family: system-ui,sans-serif;
  text-decoration: none;
  transition: filter .2s,box-shadow .2s;
  box-shadow: 0 6px 18px rgba(212,175,55,.25);
}

.fc-19__cta:hover {
  filter: brightness(1.1);
  box-shadow: 0 10px 28px rgba(212,175,55,.4);
}

.fc-19__back-foot {
  margin-top: 14px;
  font-size: 9px;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: rgba(245,241,232,.3);
  font-family: system-ui,sans-serif;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .fc-19__front,
    .fc-19__back {
    transition: none;
  }
}
```
