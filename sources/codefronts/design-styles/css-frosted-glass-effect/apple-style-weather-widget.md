---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/apple-style-weather-widget/"
title: "Apple Style Weather Widget"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "An iOS-inspired compact weather widget with a night-sky gradient, 20 individually timed twinkling CSS star spans, a floating cloud-and-sun icon, a large…"
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Apple Style Weather Widget
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/apple-style-weather-widget/

An iOS-inspired compact weather widget with a night-sky gradient, 20 individually timed twinkling CSS star spans, a floating cloud-and-sun icon, a large temperature display, H/L gradient temperature bar, and a 5-day forecast grid — zero JavaScript.
## HTML
```html
<div class="fg-12">
  <div class="fg-07__stars" aria-hidden="true">
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
  </div>
  <div class="fg-07__widget">
    <div class="fg-07__top">
      <div>
        <p class="fg-07__city">San Francisco</p>
        <p class="fg-07__time">Mon, 6:42 PM &middot; PST</p>
      </div>
      <div class="fg-07__badge"><span class="fg-07__dot"></span>Live</div>
    </div>
    <div class="fg-07__main">
      <div class="fg-07__icon-wrap" aria-hidden="true">
        <svg viewBox="0 0 88 56" width="88" height="56" fill="none">
          <circle cx="16" cy="24" r="13" fill="#fbbf24"/>
          <circle cx="16" cy="24" r="9" fill="#f59e0b"/>
          <ellipse cx="58" cy="34" rx="24" ry="17" fill="rgba(255,255,255,.88)"/>
          <ellipse cx="38" cy="38" rx="28" ry="15" fill="rgba(255,255,255,.92)"/>
          <ellipse cx="28" cy="31" rx="16" ry="13" fill="rgba(255,255,255,.82)"/>
        </svg>
      </div>
      <div>
        <p class="fg-07__temp">72<span>&deg;F</span></p>
        <p class="fg-07__cond">Partly Cloudy</p>
        <p class="fg-07__feels">Feels like 69&deg; &middot; Humidity 64%</p>
      </div>
    </div>
    <div class="fg-07__meta" aria-label="Weather details">
      <div class="fg-07__meta-item">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        <span>UV 5 — Moderate</span>
      </div>
      <div class="fg-07__meta-item">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/></svg>
        <span>12 mph NW</span>
      </div>
      <div class="fg-07__meta-item">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/></svg>
        <span>64% RH</span>
      </div>
    </div>
    <div class="fg-07__hl" aria-label="High and low temperature">
      <span>H: 78&deg;</span>
      <div class="fg-07__hl-bar" aria-hidden="true"><div class="fg-07__hl-dot" style="left:40%"></div></div>
      <span>L: 61&deg;</span>
    </div>
    <div class="fg-07__forecast" aria-label="5-day forecast">
      <div class="fg-07__day fg-07__day--today">
        <p>Today</p>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Partly cloudy"><circle cx="10" cy="10" r="5" fill="#fbbf24"/><ellipse cx="16" cy="14" rx="7" ry="5" fill="rgba(255,255,255,.85)"/><ellipse cx="11" cy="16" rx="7" ry="5" fill="rgba(255,255,255,.9)"/></svg>
        <p>72&deg;</p>
      </div>
      <div class="fg-07__day">
        <p>Tue</p>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Sunny"><circle cx="12" cy="12" r="5" fill="#fbbf24"/><g stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="22"/><line x1="2" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="22" y2="12"/><line x1="4.93" y1="4.93" x2="7.05" y2="7.05"/><line x1="16.95" y1="16.95" x2="19.07" y2="19.07"/><line x1="4.93" y1="19.07" x2="7.05" y2="16.95"/><line x1="16.95" y1="7.05" x2="19.07" y2="4.93"/></g></svg>
        <p>85&deg;</p>
      </div>
      <div class="fg-07__day">
        <p>Wed</p>
        <svg width="24" height="26" viewBox="0 0 24 26" fill="none" aria-label="Rainy"><ellipse cx="16" cy="10" rx="7" ry="5.5" fill="rgba(180,180,210,.9)"/><ellipse cx="10" cy="13" rx="9" ry="6" fill="rgba(160,160,200,.9)"/><line x1="8" y1="19" x2="6" y2="25" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round"/><line x1="13" y1="19" x2="11" y2="25" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round"/><line x1="18" y1="19" x2="16" y2="25" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round"/></svg>
        <p>63&deg;</p>
      </div>
      <div class="fg-07__day">
        <p>Thu</p>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Partly cloudy"><circle cx="9" cy="10" r="5" fill="#fbbf24" opacity=".7"/><ellipse cx="16" cy="14" rx="7" ry="5" fill="rgba(200,200,220,.9)"/><ellipse cx="11" cy="16" rx="8" ry="5" fill="rgba(220,220,240,.9)"/></svg>
        <p>72&deg;</p>
      </div>
      <div class="fg-07__day">
        <p>Fri</p>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Sunny"><circle cx="12" cy="12" r="5" fill="#fbbf24"/><g stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="22"/><line x1="2" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="22" y2="12"/><line x1="4.93" y1="4.93" x2="7.05" y2="7.05"/><line x1="16.95" y1="16.95" x2="19.07" y2="19.07"/><line x1="4.93" y1="19.07" x2="7.05" y2="16.95"/><line x1="16.95" y1="7.05" x2="19.07" y2="4.93"/></g></svg>
        <p>81&deg;</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-12,
.fg-12 *,
.fg-12 *::before,
.fg-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-12 ::selection {
  background: rgba(96,165,250,.5);
  color: #fff;
}

.fg-12 {
  --c-glass: rgba(255,255,255,.07);
  --c-border: rgba(255,255,255,.13);
  --c-text: #e8eeff;
  --c-muted: rgba(232,238,255,.55);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,#0a0a2e 0%,#1a0a3d 55%,#2d1466 100%);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}

.fg-07__stars {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.fg-07__stars span {
  position: absolute;
  border-radius: 50%;
  background: #fff;
  animation: fg-12-twinkle var(--tw,3s) ease-in-out var(--td,0s) infinite;
}

.fg-07__stars span:nth-child(1) {
  width: 2px;
  height: 2px;
  top: 7%;
  left: 11%;
  --tw: 2.5s;
  --td: .2s;
  opacity: .7;
}

.fg-07__stars span:nth-child(2) {
  width: 1px;
  height: 1px;
  top: 14%;
  left: 34%;
  --tw: 3.3s;
  --td: .8s;
  opacity: .5;
}

.fg-07__stars span:nth-child(3) {
  width: 2px;
  height: 2px;
  top: 5%;
  left: 63%;
  --tw: 2.1s;
  --td: .4s;
  opacity: .8;
}

.fg-07__stars span:nth-child(4) {
  width: 1px;
  height: 1px;
  top: 21%;
  left: 79%;
  --tw: 4s;
  --td: 1s;
  opacity: .6;
}

.fg-07__stars span:nth-child(5) {
  width: 2px;
  height: 2px;
  top: 28%;
  left: 48%;
  --tw: 2.8s;
  --td: .6s;
  opacity: .7;
}

.fg-07__stars span:nth-child(6) {
  width: 1px;
  height: 1px;
  top: 9%;
  left: 89%;
  --tw: 3.6s;
  --td: 1.4s;
  opacity: .5;
}

.fg-07__stars span:nth-child(7) {
  width: 2px;
  height: 2px;
  top: 38%;
  left: 18%;
  --tw: 2.3s;
  --td: .3s;
  opacity: .6;
}

.fg-07__stars span:nth-child(8) {
  width: 1px;
  height: 1px;
  top: 17%;
  left: 4%;
  --tw: 3.9s;
  --td: .9s;
  opacity: .4;
}

.fg-07__stars span:nth-child(9) {
  width: 2px;
  height: 2px;
  top: 49%;
  left: 73%;
  --tw: 2.7s;
  --td: .5s;
  opacity: .7;
}

.fg-07__stars span:nth-child(10) {
  width: 1px;
  height: 1px;
  top: 59%;
  left: 39%;
  --tw: 3.2s;
  --td: 1.2s;
  opacity: .5;
}

.fg-07__stars span:nth-child(11) {
  width: 2px;
  height: 2px;
  top: 68%;
  left: 9%;
  --tw: 2.4s;
  --td: .7s;
  opacity: .6;
}

.fg-07__stars span:nth-child(12) {
  width: 1px;
  height: 1px;
  top: 24%;
  left: 57%;
  --tw: 4.3s;
  --td: 1.6s;
  opacity: .4;
}

.fg-07__stars span:nth-child(13) {
  width: 2px;
  height: 2px;
  top: 79%;
  left: 84%;
  --tw: 2.9s;
  --td: .1s;
  opacity: .7;
}

.fg-07__stars span:nth-child(14) {
  width: 1px;
  height: 1px;
  top: 34%;
  left: 94%;
  --tw: 3.5s;
  --td: 1.1s;
  opacity: .5;
}

.fg-07__stars span:nth-child(15) {
  width: 2px;
  height: 2px;
  top: 87%;
  left: 29%;
  --tw: 2.2s;
  --td: .4s;
  opacity: .6;
}

.fg-07__stars span:nth-child(16) {
  width: 1px;
  height: 1px;
  top: 44%;
  left: 61%;
  --tw: 3.8s;
  --td: .8s;
  opacity: .4;
}

.fg-07__stars span:nth-child(17) {
  width: 2px;
  height: 2px;
  top: 11%;
  left: 43%;
  --tw: 2.6s;
  --td: .3s;
  opacity: .7;
}

.fg-07__stars span:nth-child(18) {
  width: 1px;
  height: 1px;
  top: 54%;
  left: 2%;
  --tw: 4.1s;
  --td: 1.3s;
  opacity: .5;
}

.fg-07__stars span:nth-child(19) {
  width: 2px;
  height: 2px;
  top: 74%;
  left: 54%;
  --tw: 2.8s;
  --td: .6s;
  opacity: .6;
}

.fg-07__stars span:nth-child(20) {
  width: 1px;
  height: 1px;
  top: 91%;
  left: 69%;
  --tw: 3.4s;
  --td: 1s;
  opacity: .4;
}

@keyframes fg-12-twinkle {
  0%,
    100% {
    opacity: .2;
    transform: scale(.8);
  }

  50% {
    opacity: 1;
    transform: scale(1.2);
  }
}

.fg-07__widget {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 360px;
  background: var(--c-glass);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 28px;
  padding: 22px;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.1) inset;
}

.fg-07__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 16px;
}

.fg-07__city {
  font-size: 16px;
  font-weight: 700;
  color: var(--c-text);
  margin-bottom: 2px;
}

.fg-07__time {
  font-size: 12px;
  color: var(--c-muted);
}

.fg-07__badge {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 600;
  color: #34d399;
  padding: 4px 10px;
  border-radius: 20px;
  background: rgba(16,185,129,.12);
  border: 1px solid rgba(16,185,129,.25);
}

.fg-07__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  animation: fg-12-blink 1.5s ease infinite;
}

@keyframes fg-12-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .2;
  }
}

.fg-07__main {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}

.fg-07__icon-wrap {
  animation: fg-12-float 4s ease-in-out infinite;
  flex-shrink: 0;
}

@keyframes fg-12-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}

.fg-07__temp {
  font-size: 54px;
  font-weight: 800;
  color: var(--c-text);
  line-height: 1;
  letter-spacing: -2px;
}

.fg-07__temp span {
  font-size: 26px;
  letter-spacing: 0;
  vertical-align: super;
}

.fg-07__cond {
  font-size: 15px;
  font-weight: 600;
  color: var(--c-text);
  margin-bottom: 3px;
}

.fg-07__feels {
  font-size: 12px;
  color: var(--c-muted);
}

.fg-07__meta {
  display: flex;
  margin-bottom: 14px;
  border-top: 1px solid rgba(255,255,255,.07);
  border-bottom: 1px solid rgba(255,255,255,.07);
  padding: 10px 0;
}

.fg-07__meta-item {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  font-size: 11px;
  color: var(--c-muted);
  padding: 4px;
}

.fg-07__meta-item:not(:last-child) {
  border-right: 1px solid rgba(255,255,255,.07);
}

.fg-07__meta-item svg {
  color: rgba(255,255,255,.4);
  flex-shrink: 0;
}

.fg-07__hl {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  font-size: 12px;
  font-weight: 700;
  color: var(--c-text);
}

.fg-07__hl-bar {
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: linear-gradient(to right,#93c5fd,#fbbf24,#f87171);
  position: relative;
}

.fg-07__hl-dot {
  position: absolute;
  top: 50%;
  transform: translate(-50%,-50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 6px rgba(255,255,255,.7);
}

.fg-07__forecast {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 2px;
}

.fg-07__day {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  padding: 8px 4px;
  border-radius: 12px;
  font-size: 11px;
}

.fg-07__day--today {
  background: rgba(255,255,255,.08);
}

.fg-07__day p:first-child {
  color: var(--c-muted);
  font-weight: 600;
  font-size: 10px;
  letter-spacing: .2px;
}

.fg-07__day p:last-child {
  font-weight: 700;
  color: var(--c-text);
}

@media (prefers-reduced-motion: reduce) {
  .fg-07__stars span,
    .fg-07__icon-wrap,
    .fg-07__dot {
    animation: none;
  }
}
```
