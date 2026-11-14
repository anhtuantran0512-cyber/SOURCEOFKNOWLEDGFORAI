---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-infinite-scroll-ticker-animation/"
title: "CSS Infinite Scroll Ticker Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Stock price ticker, brand logo marquee, bidirectional word scroll rows and breaking-news headline ticker using CSS translateX keyframes on duplicated content."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Infinite Scroll Ticker Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-infinite-scroll-ticker-animation/

Stock price ticker, brand logo marquee, bidirectional word scroll rows and breaking-news headline ticker using CSS translateX keyframes on duplicated content.
## HTML
```html
<div class="kf-18">

  <!-- Stock ticker -->
  <div class="kf-18__ticker">
    <div class="kf-18__ticker-inner">
      <!-- Duplicate for seamless loop -->
      <div class="kf-18__stock"><span class="kf-18__stock-sym">AAPL</span><span class="kf-18__stock-price">$192.30</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+2.4%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">GOOG</span><span class="kf-18__stock-price">$145.80</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+0.9%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">TSLA</span><span class="kf-18__stock-price">$248.10</span><span class="kf-18__stock-chg kf-18__stock-chg--dn">-1.3%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">MSFT</span><span class="kf-18__stock-price">$420.55</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+1.7%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">NVDA</span><span class="kf-18__stock-price">$875.40</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+4.2%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">META</span><span class="kf-18__stock-price">$510.20</span><span class="kf-18__stock-chg kf-18__stock-chg--dn">-0.6%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">AMZN</span><span class="kf-18__stock-price">$185.90</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+1.1%</span></div>
      <!-- Duplicate -->
      <div class="kf-18__stock"><span class="kf-18__stock-sym">AAPL</span><span class="kf-18__stock-price">$192.30</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+2.4%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">GOOG</span><span class="kf-18__stock-price">$145.80</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+0.9%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">TSLA</span><span class="kf-18__stock-price">$248.10</span><span class="kf-18__stock-chg kf-18__stock-chg--dn">-1.3%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">MSFT</span><span class="kf-18__stock-price">$420.55</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+1.7%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">NVDA</span><span class="kf-18__stock-price">$875.40</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+4.2%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">META</span><span class="kf-18__stock-price">$510.20</span><span class="kf-18__stock-chg kf-18__stock-chg--dn">-0.6%</span></div>
      <div class="kf-18__stock"><span class="kf-18__stock-sym">AMZN</span><span class="kf-18__stock-price">$185.90</span><span class="kf-18__stock-chg kf-18__stock-chg--up">+1.1%</span></div>
    </div>
  </div>

  <!-- Brand logos -->
  <div class="kf-18__brands">
    <div class="kf-18__brand-row">
      <span class="kf-18__brand kf-18__brand--colored">CODEFRONTS</span>
      <span class="kf-18__brand">VERCEL</span><span class="kf-18__brand">NETLIFY</span>
      <span class="kf-18__brand">SUPABASE</span><span class="kf-18__brand">FIGMA</span>
      <span class="kf-18__brand">LINEAR</span><span class="kf-18__brand">NOTION</span>
      <span class="kf-18__brand kf-18__brand--colored">CODEFRONTS</span>
      <span class="kf-18__brand">VERCEL</span><span class="kf-18__brand">NETLIFY</span>
      <span class="kf-18__brand">SUPABASE</span><span class="kf-18__brand">FIGMA</span>
      <span class="kf-18__brand">LINEAR</span><span class="kf-18__brand">NOTION</span>
    </div>
  </div>

  <!-- Word scroll -->
  <div class="kf-18__words">
    <div class="kf-18__word-row kf-18__word-row--1">
      <span class="kf-18__word">DESIGN</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">CODE</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word">ANIMATE</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">SHIP</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word">DESIGN</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">CODE</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word">ANIMATE</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">SHIP</span><span class="kf-18__word--dot"></span>
    </div>
    <div class="kf-18__word-row kf-18__word-row--2">
      <span class="kf-18__word kf-18__word--outline">MOTION</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word" style="color:var(--orange)">CRAFT</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">BUILD</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word" style="color:var(--blue)">CREATE</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">MOTION</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word" style="color:var(--orange)">CRAFT</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word kf-18__word--outline">BUILD</span><span class="kf-18__word--dot"></span>
      <span class="kf-18__word" style="color:var(--blue)">CREATE</span><span class="kf-18__word--dot"></span>
    </div>
  </div>

  <!-- News ticker -->
  <div class="kf-18__news">
    <span class="kf-18__news-label">LIVE</span>
    <div class="kf-18__news-inner">
      <span class="kf-18__news-item"><strong>BREAKING:</strong> CSS animations performance improved in Chrome 124 · </span>
      <span class="kf-18__news-item"><strong>UPDATE:</strong> New @keyframes at-rules land in Firefox 130 · </span>
      <span class="kf-18__news-item"><strong>GUIDE:</strong> Infinite marquee ticker using pure CSS — no JavaScript · </span>
      <span class="kf-18__news-item"><strong>TIP:</strong> Use animation-play-state: paused on hover for better UX · </span>
      <span class="kf-18__news-item"><strong>BREAKING:</strong> CSS animations performance improved in Chrome 124 · </span>
      <span class="kf-18__news-item"><strong>UPDATE:</strong> New @keyframes at-rules land in Firefox 130 · </span>
    </div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');

.kf-18,
.kf-18 *,
.kf-18 *::before,
.kf-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-18 ::selection {
  background: #ff6b00;
  color: #fff;
}

.kf-18 {
  --bg: #f9f6f2;
  --dark: #111;
  --orange: #ff6b00;
  --yellow: #ffe135;
  --green: #00c896;
  --red: #ff3355;
  --blue: #0057ff;
  font-family: 'Inter',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;
  gap: 0;
  overflow: hidden;
  color: var(--dark);
}
/* ——— Stock ticker ——— */

.kf-18__ticker {
  background: var(--dark);
  color: #fff;
  padding: 12px 0;
  overflow: hidden;
  border-bottom: 3px solid var(--orange);
  position: relative;
}

.kf-18__ticker-inner {
  display: flex;
  width: max-content;
  animation: kf-18-scroll-l 30s linear infinite;
}

.kf-18__ticker-inner:hover {
  animation-play-state: paused;
}

.kf-18__stock {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 32px;
  white-space: nowrap;
  font-size: .9rem;
  border-right: 1px solid rgba(255,255,255,.1);
}

.kf-18__stock-sym {
  font-weight: 700;
  letter-spacing: .05em;
}

.kf-18__stock-price {
  font-family: monospace;
}

.kf-18__stock-chg {
  font-size: .8rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 3px;
}

.kf-18__stock-chg--up {
  background: rgba(0,200,150,.2);
  color: var(--green);
}

.kf-18__stock-chg--dn {
  background: rgba(255,51,85,.2);
  color: var(--red);
}

@keyframes kf-18-scroll-l {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}
/* ——— Logo / brand marquee ——— */

.kf-18__brands {
  padding: 32px 0;
  overflow: hidden;
  border-bottom: 1px solid rgba(0,0,0,.08);
  position: relative;
}

.kf-18__brands::before,
.kf-18__brands::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100px;
  z-index: 1;
  pointer-events: none;
}

.kf-18__brands::before {
  left: 0;
  background: linear-gradient(90deg,var(--bg),transparent);
}

.kf-18__brands::after {
  right: 0;
  background: linear-gradient(-90deg,var(--bg),transparent);
}

.kf-18__brand-row {
  display: flex;
  width: max-content;
  animation: kf-18-scroll-l 20s linear infinite;
}

.kf-18__brand-row--r {
  animation: kf-18-scroll-r 22s linear infinite;
}

@keyframes kf-18-scroll-r {
  from {
    transform: translateX(-50%);
  }

  to {
    transform: translateX(0);
  }
}

.kf-18__brand {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 40px;
  font-weight: 900;
  font-size: 1.1rem;
  letter-spacing: -.02em;
  white-space: nowrap;
  opacity: .3;
}

.kf-18__brand--colored {
  opacity: 1;
  color: var(--orange);
}
/* ——— Text word scroll ——— */

.kf-18__words {
  padding: 60px 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.kf-18__word-row {
  display: flex;
  width: max-content;
  gap: 32px;
  align-items: center;
}

.kf-18__word-row--1 {
  animation: kf-18-scroll-l 18s linear infinite;
}

.kf-18__word-row--2 {
  animation: kf-18-scroll-r 22s linear infinite;
}

.kf-18__word {
  font-size: clamp(2rem,6vw,4rem);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -.02em;
  white-space: nowrap;
}

.kf-18__word--outline {
  -webkit-text-stroke: 2px var(--dark);
  color: transparent;
}

.kf-18__word--dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--orange);
  flex: 0 0 10px;
}
/* ——— News ticker ——— */

.kf-18__news {
  background: var(--blue);
  color: #fff;
  padding: 14px 0;
  overflow: hidden;
  border-top: 3px solid var(--yellow);
}

.kf-18__news-label {
  position: absolute;
  left: 0;
  background: var(--yellow);
  color: var(--dark);
  font-weight: 900;
  font-size: .8rem;
  padding: 0 14px;
  height: 100%;
  display: flex;
  align-items: center;
  letter-spacing: .1em;
  text-transform: uppercase;
  z-index: 2;
}

.kf-18__news-inner {
  display: flex;
  width: max-content;
  padding-left: 120px;
  animation: kf-18-scroll-l 40s linear infinite;
}

.kf-18__news-item {
  padding: 0 48px;
  font-size: .88rem;
  white-space: nowrap;
  border-right: 1px solid rgba(255,255,255,.2);
}

.kf-18__news-item strong {
  color: var(--yellow);
}

.kf-18__news {
  position: relative;
}

@media (prefers-reduced-motion: reduce) {
  .kf-18 * {
    animation: none!important;
  }
}
```
