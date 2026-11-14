---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/minimalist-bento-grid-stacked-cards/"
title: "Minimalist Bento Grid Stacked Cards"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A dark, dashboard-style bento grid where one tile embeds a stacked mini-card component to conserve space — channel breakdowns sit collapsed inside a single…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Bento Grid Stacked Cards
Source: https://codefronts.com/components/css-stacked-cards/minimalist-bento-grid-stacked-cards/

A dark, dashboard-style bento grid where one tile embeds a stacked mini-card component to conserve space — channel breakdowns sit collapsed inside a single cell and fan open on hover, while neighboring tiles show stats, a sparkline, and glow accents. Built for analytics dashboards and content-dense grids where stacking saves container real estate.
## HTML
```html
<div class="scd-32">
  <div class="scd-32__stage">
    <div class="scd-32__tile scd-32__tile--tall scd-32__tile--channels">
      <span class="scd-32__lbl">Channels</span>
      <div class="scd-32__substack">
        <div class="scd-32__mini scd-32__mini--m1"><span class="scd-32__lbl">Organic</span><b>62%</b></div>
        <div class="scd-32__mini scd-32__mini--m2"><span class="scd-32__lbl">Paid</span><b>24%</b></div>
        <div class="scd-32__mini scd-32__mini--m3"><span class="scd-32__lbl">Referral</span><b>14%</b></div>
      </div>
    </div>
    <div class="scd-32__tile scd-32__tile--wide"><div class="scd-32__glow" style="background:#34d399"></div><span class="scd-32__lbl">Revenue</span><div class="scd-32__val">$48.2k <small>+12%</small></div><div class="scd-32__spark"><span style="height:40%"></span><span style="height:55%"></span><span style="height:45%"></span><span style="height:70%"></span><span style="height:60%"></span><span style="height:85%"></span><span style="height:100%"></span></div></div>
    <div class="scd-32__tile"><span class="scd-32__lbl">Users</span><div class="scd-32__val">9.1k</div></div>
    <div class="scd-32__tile"><span class="scd-32__lbl">Churn</span><div class="scd-32__val" style="color:#fca5a5">1.8%</div></div>
    <div class="scd-32__tile"><div class="scd-32__glow" style="background:#818cf8"></div><span class="scd-32__lbl">NPS</span><div class="scd-32__val">72</div></div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.scd-32,
.scd-32 *,
.scd-32 *::before,
.scd-32 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-32 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0e0f13;
  font-family: 'Geist', sans-serif;
  padding: 20px;
}

.scd-32__stage {
  display: grid;
  grid-template-columns: repeat(3, 118px);
  grid-template-rows: repeat(3, 118px);
  gap: 12px;
}

.scd-32__tile {
  background: #191b22;
  border: 1px solid #262934;
  border-radius: 18px;
  padding: 16px;
  position: relative;
  overflow: hidden;
  transition: border-color .3s;
}

.scd-32__tile:hover {
  border-color: #3a4050;
}

.scd-32__lbl {
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #6b7280;
}

.scd-32__val {
  font-size: 1.6rem;
  font-weight: 700;
  color: #f3f4f6;
  margin-top: 4px;
}

.scd-32__val small {
  font-size: .8rem;
  color: #34d399;
}

.scd-32__tile--wide {
  grid-column: span 2;
}

.scd-32__tile--tall {
  grid-row: span 2;
}

.scd-32__tile--channels {
  overflow: visible;
  z-index: 5;
}

.scd-32__tile--channels:hover {
  z-index: 20;
}

.scd-32__substack {
  position: absolute;
  bottom: 14px;
  left: 16px;
  right: 16px;
  height: 54px;
}

.scd-32__mini {
  position: absolute;
  left: 0;
  right: 0;
  height: 54px;
  border-radius: 12px;
  padding: 8px 12px;
  font-size: .72rem;
  color: #fff;
  box-shadow: 0 8px 18px rgba(0,0,0,.55);
  transition: transform .45s cubic-bezier(.3,.9,.3,1);
}

.scd-32__mini .scd-32__lbl {
  color: rgba(255,255,255,.85);
}

.scd-32__mini b {
  font-size: .95rem;
  display: block;
  margin-top: 2px;
}

.scd-32__mini--m1 {
  background: linear-gradient(135deg,#6366f1,#818cf8);
  z-index: 3;
  transform: translateY(0);
}

.scd-32__mini--m2 {
  background: linear-gradient(135deg,#ec4899,#f472b6);
  z-index: 2;
  transform: translateY(8px) scale(.95);
}

.scd-32__mini--m3 {
  background: linear-gradient(135deg,#14b8a6,#2dd4bf);
  z-index: 1;
  transform: translateY(16px) scale(.9);
}

.scd-32__tile--channels:hover .scd-32__mini--m1 {
  transform: translateY(-120px);
}

.scd-32__tile--channels:hover .scd-32__mini--m2 {
  transform: translateY(-58px) scale(1);
}

.scd-32__tile--channels:hover .scd-32__mini--m3 {
  transform: translateY(4px) scale(1);
}

.scd-32__spark {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 34px;
  margin-top: 10px;
}

.scd-32__spark span {
  flex: 1;
  background: linear-gradient(#34d399,#059669);
  border-radius: 3px;
}

.scd-32__glow {
  position: absolute;
  width: 90px;
  height: 90px;
  border-radius: 50%;
  filter: blur(40px);
  opacity: .5;
  top: -20px;
  right: -20px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-32__tile,
    .scd-32__mini {
    transition: none !important;
  }
}
```
