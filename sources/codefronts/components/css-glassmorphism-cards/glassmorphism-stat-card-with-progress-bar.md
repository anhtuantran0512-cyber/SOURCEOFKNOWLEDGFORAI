---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-stat-card-with-progress-bar/"
title: "Glassmorphism Stat Card with Progress Bar"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Progress two ways: a savings-goal card whose striped bar shimmers as it fills to a CSS-variable percentage, and a fitness ring card where a conic gradient…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Stat Card with Progress Bar
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-stat-card-with-progress-bar/

Progress two ways: a savings-goal card whose striped bar shimmers as it fills to a CSS-variable percentage, and a fitness ring card where a conic gradient sweeps to its target angle while the center percentage counts up — both driven by ONE --p custom property.
## HTML
```html
<div class="glz-14-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="glz-14a" aria-label="Stat card with striped progress bar">
  <article class="glz-14a__card" style="--p:68%">
    <header class="glz-14a__head"><span class="glz-14a__ic" aria-hidden="true">⌂</span><div><h3>House deposit</h3><p>Goal · $40,000 by June</p></div><span class="glz-14a__pct">68%</span></header>
    <div class="glz-14a__bar" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Savings progress"><i></i></div>
    <footer class="glz-14a__foot"><span><b>$27,200</b> saved</span><span><b>$12,800</b> to go</span></footer>
    <p class="glz-14a__streak">🔥 9-month streak · avg $3,020/mo</p>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-14b" aria-label="Circular progress stat card">
  <article class="glz-14b__card">
    <div class="glz-14b__ringbox">
      <div class="glz-14b__ring" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Weekly goal progress"></div>
      <div class="glz-14b__mid"><b></b><em>of weekly goal</em></div>
    </div>
    <div class="glz-14b__side">
      <h3>Move goal</h3>
      <p>412 / 600 min active</p>
      <ul>
        <li><i style="--c:oklch(0.8 0.17 150)"></i>Cardio <b>3h 10m</b></li>
        <li><i style="--c:oklch(0.78 0.15 220)"></i>Strength <b>2h 25m</b></li>
        <li><i style="--c:oklch(0.8 0.13 320)"></i>Mobility <b>1h 17m</b></li>
      </ul>
    </div>
  </article>
</section>
</div>
```
## CSS
```css
.glz-14-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-14-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-14a,
.glz-14a *,
.glz-14a *::before,
.glz-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --glz-14a-w {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.glz-14a {
  --gold: oklch(0.8 0.14 80);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #12100c;
  font-family: 'Manrope',system-ui,sans-serif;
}

.glz-14a::before {
  content: "";
  position: absolute;
  width: 58vmin;
  height: 58vmin;
  border-radius: 50%;
  background: oklch(0.6 0.13 80);
  filter: blur(95px);
  opacity: .45;
  top: -14%;
  right: -6%;
}

.glz-14a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.5 0.12 150);
  filter: blur(95px);
  opacity: .4;
  bottom: -12%;
  left: -6%;
}

.glz-14a__card {
  position: relative;
  z-index: 1;
  width: min(400px,100%);
  padding: 26px;
  border-radius: 24px;
  color: #f4efe4;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(160%);
  -webkit-backdrop-filter: blur(22px) saturate(160%);
  border: 1px solid rgba(255,240,200,.22);
  box-shadow: 0 32px 66px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-14a__head {
  display: flex;
  align-items: center;
  gap: 14px;
}

.glz-14a__ic {
  width: 44px;
  height: 44px;
  flex: none;
  display: grid;
  place-items: center;
  font-size: 18px;
  border-radius: 14px;
  color: var(--gold);
  background: oklch(0.8 0.14 80/.14);
  border: 1px solid oklch(0.8 0.14 80/.35);
}

.glz-14a__head h3 {
  font-size: 16.5px;
  font-weight: 800;
}

.glz-14a__head p {
  margin-top: 2px;
  font-size: 12px;
  color: rgba(244,239,228,.55);
}

.glz-14a__pct {
  margin-left: auto;
  font-size: 24px;
  font-weight: 800;
  color: var(--gold);
  font-variant-numeric: tabular-nums;
}

.glz-14a__bar {
  margin-top: 20px;
  height: 14px;
  border-radius: 99px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.14);
  overflow: hidden;
}

.glz-14a__bar i {
  display: block;
  height: 100%;
  width: var(--glz-14a-w);
  border-radius: inherit;
  background: linear-gradient(90deg,oklch(0.72 0.14 60),var(--gold)),repeating-linear-gradient(-55deg,transparent 0 10px,rgba(255,255,255,.28) 10px 20px);
  background-blend-mode: overlay;
  animation: glz-14a-fill 1.4s cubic-bezier(.2,.7,.2,1) .3s forwards,glz-14a-stripe 1.2s linear 1.7s infinite;
  box-shadow: 0 0 18px oklch(0.8 0.14 80/.5);
}

.glz-14a__foot {
  display: flex;
  justify-content: space-between;
  margin-top: 14px;
  font-size: 12.5px;
  color: rgba(244,239,228,.6);
}

.glz-14a__foot b {
  color: #fff;
  font-variant-numeric: tabular-nums;
}

.glz-14a__streak {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px dashed rgba(255,240,200,.2);
  font-size: 12px;
  color: rgba(244,239,228,.65);
}

@keyframes glz-14a-fill {
  from {
    --glz-14a-w: 0%;
  }

  to {
    --glz-14a-w: var(--p);
  }
}

@keyframes glz-14a-stripe {
  to {
    background-position: 0 0,28px 0;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-14a__card {
    background: rgba(30,26,18,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-14a__bar i {
    animation: none;
    width: var(--p);
  }
}

.glz-14b,
.glz-14b *,
.glz-14b *::before,
.glz-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --glz-14b-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

@property --glz-14b-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.glz-14b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(110% 100% at 20% 0%,#12271f,#0b1214 60%);
}

.glz-14b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(42% 36% at 82% 22%,oklch(0.6 0.16 150/.35),transparent 70%),radial-gradient(38% 32% at 12% 84%,oklch(0.55 0.14 220/.35),transparent 70%);
}

.glz-14b__card {
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 26px;
  width: min(440px,100%);
  padding: 28px;
  border-radius: 26px;
  color: #ecf6ef;
  font-family: 'Manrope',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(220,255,235,.2);
  box-shadow: 0 32px 66px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-14b__ringbox {
  position: relative;
  width: 148px;
  height: 148px;
  margin: 0 auto;
}

.glz-14b__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(oklch(0.8 0.17 150) var(--glz-14b-p),rgba(255,255,255,.1) 0);
  -webkit-mask: radial-gradient(closest-side,transparent 58%,#000 59%);
  mask: radial-gradient(closest-side,transparent 58%,#000 59%);
  animation: glz-14b-sweep 1.5s cubic-bezier(.2,.7,.2,1) .3s forwards;
  filter: drop-shadow(0 0 14px oklch(0.8 0.17 150/.5));
}

.glz-14b__mid {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  text-align: center;
  gap: 2px;
}

.glz-14b__mid b {
  font-family: 'JetBrains Mono',monospace;
  font-size: 34px;
  font-weight: 700;
  --glz-14b-n: 0;
  animation: glz-14b-count 1.5s cubic-bezier(.2,.7,.2,1) .3s forwards;
}

.glz-14b__mid b::after {
  counter-reset: glz14b calc(var(--glz-14b-n));
  content: counter(glz14b) "%";
}

.glz-14b__mid em {
  font-style: normal;
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(236,246,239,.5);
}

.glz-14b__side {
  flex: 1 1 190px;
}

.glz-14b__side h3 {
  font-size: 17px;
  font-weight: 800;
}

.glz-14b__side>p {
  margin-top: 4px;
  font-size: 12.5px;
  color: rgba(236,246,239,.55);
}

.glz-14b__side ul {
  list-style: none;
  margin-top: 16px;
  display: grid;
  gap: 10px;
  font-size: 13px;
}

.glz-14b__side li {
  display: flex;
  align-items: center;
  gap: 9px;
}

.glz-14b__side i {
  width: 9px;
  height: 9px;
  border-radius: 3px;
  background: var(--c);
  box-shadow: 0 0 10px color-mix(in oklab,var(--c) 70%,transparent);
}

.glz-14b__side b {
  margin-left: auto;
  font-variant-numeric: tabular-nums;
  color: rgba(236,246,239,.85);
}

@keyframes glz-14b-sweep {
  to {
    --glz-14b-p: 68%;
  }
}

@keyframes glz-14b-count {
  to {
    --glz-14b-n: 68;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-14b__card {
    background: rgba(16,26,22,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-14b__ring {
    animation-duration: .001s;
  }

  .glz-14b__mid b {
    animation-duration: .001s;
  }
}
```

## JavaScript
```js
/* No JavaScript — one --p custom property feeds the width; @property lets it tween from 0 while a repeating-gradient stripe layer drifts over the fill. */

/* No JavaScript — the conic stop and the counter() label animate to 68% on the same curve and delay, so ring and number arrive together. */
```
