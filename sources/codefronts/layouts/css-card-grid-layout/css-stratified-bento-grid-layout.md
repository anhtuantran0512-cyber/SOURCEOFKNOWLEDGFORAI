---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-stratified-bento-grid-layout/"
title: "CSS Stratified Bento Grid Layout"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A real product-feature bento grid on a deep carmine canvas — every tile carries a real SaaS dashboard metric, feature pill, or CTA, with a two-tone vertical…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stratified Bento Grid Layout
Source: https://codefronts.com/layouts/css-card-grid-layout/css-stratified-bento-grid-layout/

A real product-feature bento grid on a deep carmine canvas — every tile carries a real SaaS dashboard metric, feature pill, or CTA, with a two-tone vertical duotone backdrop that swaps tones on hover via a clip-path wipe. Drop-in for marketing pages, pricing hero sections, and feature showcases.
## HTML
```html
<div class="cg-07">
  <div class="cg-07__grid">

    <a class="cg-07__tile cg-07__tile--a" style="--top:#f4a572;--bot:#d97f4f">
      <span class="cg-07__kicker">Active users</span>
      <span class="cg-07__metric">247,318</span>
      <span class="cg-07__delta">▲ 12.4% this week</span>
    </a>

    <a class="cg-07__tile cg-07__tile--b" style="--top:#1f8c6e;--bot:#0f5b48">
      <span class="cg-07__icon">✓</span>
      <span class="cg-07__title">99.98% uptime</span>
    </a>

    <a class="cg-07__tile cg-07__tile--c" style="--top:#c4b5fd;--bot:#9b87e5">
      <span class="cg-07__kicker">Plan</span>
      <span class="cg-07__title">Pro</span>
      <span class="cg-07__price">$24<small>/mo</small></span>
      <span class="cg-07__cta">Upgrade →</span>
    </a>

    <a class="cg-07__tile cg-07__tile--d" style="--top:#34d399;--bot:#0f7a52">
      <span class="cg-07__icon">⚡</span>
      <span class="cg-07__title">Edge cache</span>
    </a>

    <a class="cg-07__tile cg-07__tile--e" style="--top:#f0bb91;--bot:#cc8a5e">
      <span class="cg-07__icon">⌘</span>
      <span class="cg-07__title">⌘K Search</span>
    </a>

    <a class="cg-07__tile cg-07__tile--f" style="--top:#f9c1cf;--bot:#e187a0">
      <span class="cg-07__kicker">Customer story</span>
      <span class="cg-07__title">"It paid back in 6 weeks."</span>
      <span class="cg-07__byline">Maya Chen · Linear</span>
    </a>

    <a class="cg-07__tile cg-07__tile--g" style="--top:#c5da9c;--bot:#94b864">
      <span class="cg-07__icon">★</span>
      <span class="cg-07__title">4.9 / 5</span>
    </a>

    <a class="cg-07__tile cg-07__tile--h" style="--top:#fff4a3;--bot:#e8d558">
      <span class="cg-07__kicker">Monthly revenue</span>
      <span class="cg-07__metric cg-07__metric--dark">$2.4M</span>
      <span class="cg-07__delta cg-07__delta--dark">▲ 38% YoY</span>
    </a>

    <a class="cg-07__tile cg-07__tile--i" style="--top:#1f8c6e;--bot:#0f5b48">
      <span class="cg-07__icon">⚙</span>
      <span class="cg-07__title">API v3</span>
    </a>

    <a class="cg-07__tile cg-07__tile--j" style="--top:#f4a572;--bot:#d97f4f">
      <span class="cg-07__icon">☾</span>
      <span class="cg-07__title">Dark mode</span>
    </a>

    <a class="cg-07__tile cg-07__tile--k" style="--top:#c4b5fd;--bot:#9b87e5">
      <span class="cg-07__icon">⟳</span>
      <span class="cg-07__title">Auto sync</span>
    </a>

    <a class="cg-07__tile cg-07__tile--l" style="--top:#f9c1cf;--bot:#e187a0">
      <span class="cg-07__kicker">Get started</span>
      <span class="cg-07__title">Start your 14-day free trial</span>
      <span class="cg-07__cta">Create account →</span>
    </a>

  </div>
</div>
```
## CSS
```css
.cg-07,
.cg-07 *,
.cg-07 *::before,
.cg-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-07 ::selection {
  background: #fff;
  color: #c93a4a;
}

.cg-07 {
  --bg: #c93a4a;
  --ink: #1a1414;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 36px;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  color: var(--ink);
}

.cg-07__grid {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  grid-auto-rows: 110px;
  gap: 14px;
  width: 100%;
  max-width: 1100px;
}

.cg-07__tile {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  background: linear-gradient(to bottom,var(--top) 0 50%,var(--bot) 50% 100%);
  cursor: pointer;
  isolation: isolate;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 16px 18px;
  text-decoration: none;
  color: inherit;
  gap: 4px;
}

.cg-07__tile::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom,var(--bot) 0 50%,var(--top) 50% 100%);
  clip-path: inset(0 0 100% 0);
  transition: clip-path .38s cubic-bezier(.65,.05,.35,1);
  z-index: 0;
}

.cg-07__tile > * {
  position: relative;
  z-index: 1;
}

.cg-07__tile:hover::before {
  clip-path: inset(0);
}

.cg-07__icon {
  font-size: 1.8rem;
  line-height: 1;
  margin-top: auto;
  margin-bottom: auto;
  color: #fff;
  text-shadow: 0 1px 2px rgba(0,0,0,.18);
}

.cg-07__kicker {
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(0,0,0,.55);
  font-weight: 600;
}

.cg-07__title {
  font-size: .95rem;
  font-weight: 700;
  line-height: 1.25;
  color: #fff;
  text-shadow: 0 1px 2px rgba(0,0,0,.22);
}

.cg-07__metric {
  font-size: 1.8rem;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #fff;
  text-shadow: 0 1px 2px rgba(0,0,0,.22);
  line-height: 1;
}

.cg-07__metric--dark {
  color: #1a1414;
  text-shadow: none;
}

.cg-07__delta {
  font-size: .72rem;
  font-weight: 600;
  color: rgba(255,255,255,.92);
}

.cg-07__delta--dark {
  color: rgba(0,0,0,.65);
}

.cg-07__price {
  font-size: 1.5rem;
  font-weight: 800;
  color: #fff;
  line-height: 1;
  text-shadow: 0 1px 2px rgba(0,0,0,.22);
}

.cg-07__price small {
  font-size: .7rem;
  font-weight: 600;
  opacity: .85;
  margin-left: 2px;
}

.cg-07__byline {
  font-size: .68rem;
  font-weight: 600;
  color: rgba(0,0,0,.5);
}

.cg-07__cta {
  font-size: .74rem;
  font-weight: 700;
  color: #fff;
  background: rgba(0,0,0,.22);
  padding: 5px 9px;
  border-radius: 6px;
  align-self: flex-start;
  margin-top: 4px;
  transition: background .25s;
}

.cg-07__tile:hover .cg-07__cta {
  background: rgba(0,0,0,.38);
}
/* Asymmetric span placement — drives the bento weighting */

.cg-07__tile--a {
  grid-column: span 2;
  grid-row: span 1;
}

.cg-07__tile--b {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--c {
  grid-column: span 1;
  grid-row: span 2;
}

.cg-07__tile--d {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--e {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--f {
  grid-column: span 3;
  grid-row: span 1;
}

.cg-07__tile--g {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--h {
  grid-column: span 2;
  grid-row: span 1;
}

.cg-07__tile--i {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--j {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--k {
  grid-column: span 1;
  grid-row: span 1;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.cg-07__tile--l {
  grid-column: span 3;
  grid-row: span 1;
}

@media (max-width: 640px) {
  .cg-07__grid {
    grid-template-columns: repeat(3,1fr);
  }

  .cg-07__tile {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }

  .cg-07__tile--c {
    grid-row: span 2 !important;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-07__tile::before,
    .cg-07__cta {
    transition: none;
  }
}
```
