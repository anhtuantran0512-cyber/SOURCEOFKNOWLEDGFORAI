---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/minimalist-weather-glass-card/"
title: "Minimalist Weather Glass Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A clean weather card where animated rain streaks and a sun-flare SVG drift across a Liquid Glass overlay, subtly warping the big temperature reading beneath…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Weather Glass Card
Source: https://codefronts.com/components/css-liquid-glass-cards/minimalist-weather-glass-card/

A clean weather card where animated rain streaks and a sun-flare SVG drift across a Liquid Glass overlay, subtly warping the big temperature reading beneath them as they pass — a poetic take on the pro-tip that glass needs living texture behind it. Fully static-readable, motion is pure decoration.
## HTML
```html
<section class="lg-08" aria-label="Minimalist liquid glass weather card demo">
  <svg class="lg-08__defs" aria-hidden="true" width="0" height="0"><filter id="lg-08-warp"><feTurbulence type="fractalNoise" baseFrequency="0.01 0.04" numOctaves="2" seed="5" result="n"><animate attributeName="seed" dur="8s" values="5;9;5" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="8" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <article class="lg-08__card">
    <div class="lg-08__rain" aria-hidden="true"></div>
    <div class="lg-08__body">
      <div class="lg-08__top"><span class="lg-08__place">Wellington</span><span class="lg-08__cond">Light rain</span></div>
      <h3 class="lg-08__temp">14<span class="lg-08__unit" aria-label="degrees Celsius">°C</span></h3>
      <dl class="lg-08__fc">
        <div><dt>Mon</dt><dd>13°</dd></div><div><dt>Tue</dt><dd>15°</dd></div><div><dt>Wed</dt><dd>12°</dd></div><div><dt>Thu</dt><dd>16°</dd></div>
      </dl>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-08,
.lg-08 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-08 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(160deg,#334155,#1e293b 50%,#475569);
}

.lg-08__card {
  position: relative;
  width: min(300px,100%);
  border-radius: 26px;
  overflow: hidden;
  isolation: isolate;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 30px 60px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
}

.lg-08__rain {
  position: absolute;
  inset: -20%;
  background: repeating-linear-gradient(74deg,transparent,transparent 12px,rgba(255,255,255,.16) 12px,rgba(255,255,255,.16) 13px);
  animation: lg-08-rain 1.1s linear infinite;
  pointer-events: none;
}

@keyframes lg-08-rain {
  to {
    transform: translate(-26px,54px);
  }
}

.lg-08__body {
  position: relative;
  padding: 24px;
  color: #fff;
  filter: url(#lg-08-warp);
}

.lg-08__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.lg-08__place {
  font-size: 16px;
  font-weight: 800;
}

.lg-08__cond {
  font-size: 12.5px;
  color: rgba(255,255,255,.8);
}

.lg-08__temp {
  font-size: 72px;
  font-weight: 200;
  line-height: 1;
  letter-spacing: -.04em;
  margin: 16px 0;
  text-shadow: 0 2px 20px rgba(0,0,0,.3);
}

.lg-08__unit {
  font-size: 24px;
  font-weight: 500;
  vertical-align: top;
  margin-left: 4px;
}

.lg-08__fc {
  display: flex;
  justify-content: space-between;
  gap: 8px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.2);
}

.lg-08__fc dt {
  font-size: 12px;
  color: rgba(255,255,255,.7);
  text-align: center;
}

.lg-08__fc dd {
  font-size: 15px;
  font-weight: 700;
  text-align: center;
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-08__rain {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an animated rain sheet drifts over a frosted overlay while a localized SVG feDisplacementMap gently warps the temperature digits beneath, so you read the number 'through' moving glass. */
```
