---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-weather-card-ui-html-css/"
title: "Glassmorphism Weather Card UI HTML CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The genre's mascot, done twice: a golden-hour “now” card over a real sky photo with a CSS-drawn sun and drifting cloud plus an hourly strip, and a night…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Weather Card UI HTML CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-weather-card-ui-html-css/

The genre's mascot, done twice: a golden-hour “now” card over a real sky photo with a CSS-drawn sun and drifting cloud plus an hourly strip, and a night storm card where CSS rain falls behind the glass and a lightning flash fires on a randomized-feeling loop.
## HTML
```html
<div class="glz-12-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="glz-12a" aria-label="Glassmorphism weather card demo">
  <article class="glz-12a__card">
    <div class="glz-12a__sky" aria-hidden="true"><i class="glz-12a__sun"></i><i class="glz-12a__cloud"></i></div>
    <header class="glz-12a__head"><div><h3>Queenstown</h3><p>Saturday · 5:42 PM</p></div><span class="glz-12a__cond">Partly sunny</span></header>
    <p class="glz-12a__temp">18<span>°C</span></p>
    <p class="glz-12a__range">H 21° · L 9° · Feels like 17°</p>
    <div class="glz-12a__hours" tabindex="0" aria-label="Hourly forecast">
      <span><em>6PM</em>☀<b>17°</b></span><span><em>7PM</em>🌤<b>15°</b></span><span><em>8PM</em>☁<b>13°</b></span><span><em>9PM</em>☁<b>12°</b></span><span><em>10PM</em>🌙<b>10°</b></span><span><em>11PM</em>🌙<b>9°</b></span>
    </div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="glz-12b" aria-label="Storm weather card with CSS rain">
  <article class="glz-12b__card">
    <div class="glz-12b__rain" aria-hidden="true"></div>
    <div class="glz-12b__flash" aria-hidden="true"></div>
    <header class="glz-12b__head"><div><h3>Seattle</h3><p>Tonight · thunderstorm</p></div><span class="glz-12b__aq">⛈ Severe</span></header>
    <p class="glz-12b__temp">7<span>°C</span></p>
    <ul class="glz-12b__stats">
      <li><em>Precip</em><b>92%</b></li>
      <li><em>Wind</em><b>34 km/h</b></li>
      <li><em>Humidity</em><b>88%</b></li>
    </ul>
    <p class="glz-12b__note">Rain easing by 4 AM · lightning within 8 km</p>
  </article>
</section>
</div>
```
## CSS
```css
.glz-12-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-12-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-12a,
.glz-12a *,
.glz-12a *::before,
.glz-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-12a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f4a55f,#d96f5b 55%,#8d5a8f) url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=1600&auto=format&fit=crop') center/cover;
  background-blend-mode: overlay;
  font-family: 'Outfit',system-ui,sans-serif;
}

.glz-12a__card {
  position: relative;
  width: min(360px,100%);
  padding: 26px 26px 22px;
  border-radius: 26px;
  overflow: hidden;
  color: #fff;
  background: linear-gradient(165deg,rgba(30,20,40,.38),rgba(30,20,40,.24));
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: 0 34px 70px -26px rgba(60,20,40,.7),inset 0 1px 0 rgba(255,255,255,.35);
}

.glz-12a__sky {
  position: absolute;
  top: 126px;
  right: 24px;
  width: 150px;
  height: 110px;
  pointer-events: none;
  z-index: 0;
}

.glz-12a__sun {
  position: absolute;
  top: 12px;
  right: 52px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 35%,#ffe9a8,#ffb347 70%);
  box-shadow: 0 0 34px rgba(255,190,90,.9),0 0 90px rgba(255,160,70,.5);
  animation: glz-12a-glow 5s ease-in-out infinite alternate;
}

.glz-12a__cloud {
  position: absolute;
  top: 42px;
  right: 14px;
  width: 78px;
  height: 28px;
  border-radius: 99px;
  background: rgba(255,245,238,.95);
  box-shadow: 0 4px 14px rgba(120,60,60,.25);
  animation: glz-12a-drift 9s ease-in-out infinite alternate;
}

.glz-12a__cloud::before {
  content: "";
  position: absolute;
  left: 14px;
  top: -14px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: inherit;
}

.glz-12a__cloud::after {
  content: "";
  position: absolute;
  right: 16px;
  top: -10px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: inherit;
}

.glz-12a__head,
.glz-12a__temp,
.glz-12a__range,
.glz-12a__hours {
  position: relative;
  z-index: 1;
}

.glz-12a__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 10px;
}

.glz-12a__head h3 {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.glz-12a__head p {
  margin-top: 3px;
  font-size: 12px;
  color: rgba(255,255,255,.75);
}

.glz-12a__cond {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 6px 11px;
  border-radius: 99px;
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.35);
}

.glz-12a__temp {
  margin-top: 22px;
  font-size: clamp(64px,15vw,92px);
  font-weight: 200;
  line-height: .95;
  letter-spacing: -.04em;
}

.glz-12a__temp span {
  font-size: .32em;
  font-weight: 400;
  vertical-align: super;
}

.glz-12a__range {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(255,255,255,.8);
}

.glz-12a__hours {
  display: flex;
  gap: 8px;
  margin-top: 20px;
  padding: 6px 2px 10px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
}

.glz-12a__hours::-webkit-scrollbar {
  display: none;
}

.glz-12a__hours:focus-visible {
  outline: 2px solid rgba(255,255,255,.8);
  outline-offset: 3px;
  border-radius: 12px;
}

.glz-12a__hours span {
  scroll-snap-align: start;
  flex: none;
  display: grid;
  justify-items: center;
  gap: 5px;
  min-width: 56px;
  padding: 11px 8px;
  border-radius: 14px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.25);
  font-size: 15px;
}

.glz-12a__hours em {
  font-style: normal;
  font-size: 10px;
  letter-spacing: .08em;
  color: rgba(255,255,255,.7);
}

.glz-12a__hours b {
  font-size: 13px;
  font-weight: 700;
}

@keyframes glz-12a-glow {
  to {
    box-shadow: 0 0 44px rgba(255,190,90,1),0 0 110px rgba(255,160,70,.65);
  }
}

@keyframes glz-12a-drift {
  to {
    transform: translateX(-16px);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-12a__card {
    background: rgba(44,30,52,.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-12a__sun,
    .glz-12a__cloud {
    animation: none;
  }
}

.glz-12b,
.glz-12b *,
.glz-12b *::before,
.glz-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-12b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 90% at 50% -10%,#2a3550,#101527 55%,#0a0d18);
  font-family: 'Outfit',system-ui,sans-serif;
}

.glz-12b__card {
  position: relative;
  width: min(360px,100%);
  padding: 26px;
  border-radius: 26px;
  overflow: hidden;
  color: #e8eefb;
  background: linear-gradient(165deg,rgba(150,175,230,.16),rgba(150,175,230,.05));
  backdrop-filter: blur(22px) saturate(160%);
  -webkit-backdrop-filter: blur(22px) saturate(160%);
  border: 1px solid rgba(190,210,255,.28);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.25);
}

.glz-12b__rain {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  border-radius: inherit;
  transform: skewX(-10deg);
  transform-origin: top;
}

.glz-12b__rain,
.glz-12b__rain::before,
.glz-12b__rain::after {
  background-repeat: repeat;
}

.glz-12b__rain {
  background-image: radial-gradient(ellipse 1px 8px at 50% 50%,rgba(210,225,255,.9),transparent 70%);
  background-size: 14px 30px;
  animation: glz-12b-fall-fg .55s linear infinite;
}

.glz-12b__rain::before,
.glz-12b__rain::after {
  content: "";
  position: absolute;
  inset: -10%;
  pointer-events: none;
}

.glz-12b__rain::before {
  background-image: radial-gradient(ellipse 1px 10px at 50% 50%,rgba(180,210,255,.65),transparent 70%);
  background-size: 22px 46px;
  background-position: 7px 0;
  animation: glz-12b-fall-mid .9s linear infinite;
}

.glz-12b__rain::after {
  background-image: radial-gradient(ellipse 1px 12px at 50% 50%,rgba(150,180,240,.45),transparent 70%);
  background-size: 34px 68px;
  background-position: 15px 0;
  animation: glz-12b-fall-bg 1.4s linear infinite;
}

.glz-12b__flash {
  position: absolute;
  inset: 0;
  background: radial-gradient(80% 60% at 70% 0%,rgba(220,230,255,.9),transparent 60%);
  opacity: 0;
  pointer-events: none;
  animation: glz-12b-flash 7s linear infinite;
}

.glz-12b__head {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 10px;
}

.glz-12b__head h3 {
  font-size: 20px;
  font-weight: 700;
}

.glz-12b__head p {
  margin-top: 3px;
  font-size: 12px;
  color: rgba(232,238,251,.65);
}

.glz-12b__aq {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 6px 11px;
  border-radius: 99px;
  color: oklch(0.85 0.13 85);
  background: oklch(0.85 0.13 85/.14);
  border: 1px solid oklch(0.85 0.13 85/.4);
}

.glz-12b__temp {
  position: relative;
  margin-top: 18px;
  font-size: clamp(64px,15vw,92px);
  font-weight: 200;
  line-height: .95;
  letter-spacing: -.04em;
}

.glz-12b__temp span {
  font-size: .32em;
  font-weight: 400;
  vertical-align: super;
}

.glz-12b__stats {
  position: relative;
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin-top: 20px;
  border-radius: 16px;
  background: rgba(10,14,26,.35);
  border: 1px solid rgba(190,210,255,.18);
  padding: 14px 0;
}

.glz-12b__stats li {
  text-align: center;
}

.glz-12b__stats li+li {
  border-left: 1px solid rgba(190,210,255,.18);
}

.glz-12b__stats em {
  display: block;
  font-style: normal;
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(232,238,251,.5);
}

.glz-12b__stats b {
  display: block;
  margin-top: 4px;
  font-size: 15px;
  font-weight: 700;
}

.glz-12b__note {
  position: relative;
  margin-top: 16px;
  font-size: 12.5px;
  color: rgba(232,238,251,.65);
}

@keyframes glz-12b-fall-fg {
  to {
    background-position: 0 30px;
  }
}

@keyframes glz-12b-fall-mid {
  to {
    background-position: 7px 46px;
  }
}

@keyframes glz-12b-fall-bg {
  to {
    background-position: 15px 68px;
  }
}

@keyframes glz-12b-flash {
  0%,
    89%,
    93%,
    100% {
    opacity: 0;
  }

  90%,
    92.5% {
    opacity: .9;
  }

  91.5% {
    opacity: .25;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-12b__card {
    background: rgba(22,29,50,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-12b__rain,
    .glz-12b__rain::before,
    .glz-12b__rain::after,
    .glz-12b__flash {
    animation: none;
  }

  .glz-12b__flash {
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — the sun/cloud are CSS shapes on gentle loops; the hourly strip is a scroll-snap flex row; the glass carries a dark scrim for contrast over the photo. */

/* No JavaScript — rain is two repeating gradients scrolling their background-position; lightning is an opacity keyframe with a long quiet span so it feels random. */
```
