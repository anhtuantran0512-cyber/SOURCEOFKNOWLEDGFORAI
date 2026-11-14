---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/mediterranean-travel/"
title: "Mediterranean Travel"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Travel agency hero — Mediterranean blue + ochre + white limewash."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mediterranean Travel
Source: https://codefronts.com/layouts/css-split-screen/mediterranean-travel/

Travel agency hero — Mediterranean blue + ochre + white limewash. Parallax-feel split with layered cliff/sea/sun shapes on one side and a destination card on the other. Pure CSS animations drift the sun and sea slowly.
## HTML
```html
<section class="ss-trv" aria-label="Mediterranean travel destination">
  <aside class="ss-trv-scene" aria-hidden="true">
    <span class="ss-trv-sky"></span>
    <span class="ss-trv-sun"></span>
    <span class="ss-trv-sea"></span>
    <span class="ss-trv-cliff"></span>
    <span class="ss-trv-house"></span>
    <span class="ss-trv-house ss-trv-house-2"></span>
  </aside>
  <article class="ss-trv-card">
    <span class="ss-trv-tag">Greece · Cyclades</span>
    <h2>Folegandros<br /><em>in May.</em></h2>
    <p>
      Five days. One villa. Local meals at the kafenio. White-washed walls and a sea you'll never
      quite forget. Limited to 8 guests per departure.
    </p>
    <dl class="ss-trv-info">
      <dt>Departure</dt>
      <dd>14 — 19 May</dd>
      <dt>Group size</dt>
      <dd>8 guests</dd>
      <dt>Includes</dt>
      <dd>Villa, breakfasts, ferry</dd>
      <dt>From</dt>
      <dd>€2,400 / guest</dd>
    </dl>
    <button type="button" class="ss-trv-cta">Reserve a spot</button>
  </article>
</section>
```
## CSS
```css
.ss-trv {
  width: 100%;
  display: grid;
  grid-template-columns: 55% 45%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #f4ede0;
  color: #1a3a4a;
  border-radius: 0;
  overflow: hidden;
}

.ss-trv-scene {
  position: relative;
  overflow: hidden;
  isolation: isolate;
}

.ss-trv-sky {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, #c4e4f0 0%, #a4d4e8 50%, #5a8fa8 100%);
}

.ss-trv-sun {
  position: absolute;
  top: 18%;
  left: 22%;
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #fff8d8 0%, #ffd479 50%, #f5a623 100%);
  box-shadow: 0 0 80px rgba(255,212,121,0.6);
  animation: ss-trv-sun 22s ease-in-out infinite alternate;
}

@keyframes ss-trv-sun {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-12px);
  }
}

.ss-trv-sea {
  position: absolute;
  left: -10%;
  right: -10%;
  bottom: 0;
  height: 50%;
  background: repeating-linear-gradient(180deg, transparent 0 4px, rgba(255,255,255,0.18) 4px 5px), linear-gradient(180deg, #2c8cc4 0%, #1a5a8c 100%);
  border-top-left-radius: 50% 22%;
  border-top-right-radius: 50% 22%;
  animation: ss-trv-sea 18s ease-in-out infinite alternate;
}

@keyframes ss-trv-sea {
  from {
    transform: translateX(-2%);
  }

  to {
    transform: translateX(2%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-trv-sun,
    .ss-trv-sea {
    animation: none;
  }
}

.ss-trv-cliff {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 38%;
  height: 28%;
  background: linear-gradient(180deg, #f0e0c8 0%, #c8a878 100%);
  clip-path: polygon(0 60%, 28% 28%, 50% 50%, 78% 22%, 100% 50%, 100% 100%, 0 100%);
}

.ss-trv-house {
  position: absolute;
  bottom: 50%;
  width: 50px;
  height: 60px;
  background: #fff;
  box-shadow: 0 0 0 1px rgba(0,0,0,0.06);
}

.ss-trv-house::before {
  content: '';
  position: absolute;
  left: -6px;
  right: -6px;
  top: -10px;
  height: 14px;
  background: #2c8cc4;
  border-radius: 50% 50% 0 0;
}

.ss-trv-house::after {
  content: '';
  position: absolute;
  left: 30%;
  bottom: 0;
  width: 30%;
  height: 50%;
  background: #2c8cc4;
}

.ss-trv-house {
  left: 38%;
}

.ss-trv-house-2 {
  left: 56%;
  bottom: 56%;
  width: 38px;
  height: 48px;
}

.ss-trv-card {
  padding: 44px 40px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: radial-gradient(60% 60% at 100% 100%, rgba(245,166,35,0.1) 0%, transparent 70%), #fdf8eb;
  border-left: 1px solid rgba(0,0,0,0.06);
}

.ss-trv-tag {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #c45a1c;
}

.ss-trv-card h2 {
  margin: 4px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(36px, 5vw, 56px);
  font-weight: 500;
  line-height: 0.96;
  color: #1a3a4a;
  letter-spacing: -0.02em;
}

.ss-trv-card h2 em {
  font-style: italic;
  color: #2c8cc4;
}

.ss-trv-card p {
  margin: 0;
  font-size: 15px;
  line-height: 1.65;
  color: #4a5a6a;
  max-width: 380px;
}

.ss-trv-info {
  margin: 0;
  padding: 16px 0;
  border-top: 1px solid #c8b896;
  border-bottom: 1px solid #c8b896;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 10px 18px;
  font-size: 14px;
}

.ss-trv-info dt {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #8a6f4a;
  align-self: center;
}

.ss-trv-info dd {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 17px;
  font-style: italic;
  color: #1a3a4a;
}

.ss-trv-cta {
  align-self: flex-start;
  padding: 14px 26px;
  background: #2c8cc4;
  color: #fff;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(44,140,196,0.35);
  transition: background 0.16s;
}

.ss-trv-cta:hover {
  background: #1a5a8c;
}

@media (max-width: 720px) {
  .ss-trv {
    grid-template-columns: 1fr;
  }

  .ss-trv-scene {
    min-height: 280px;
  }
}
```
