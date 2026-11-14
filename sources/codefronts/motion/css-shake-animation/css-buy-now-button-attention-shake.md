---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-buy-now-button-attention-shake/"
title: "CSS Buy Now Button Attention Shake"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Attention shakes that convert without harassing: a product card whose Buy Now wiggles for half a second every four seconds (the idle-loop trick — one…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Buy Now Button Attention Shake
Source: https://codefronts.com/motion/css-shake-animation/css-buy-now-button-attention-shake/

Attention shakes that convert without harassing: a product card whose Buy Now wiggles for half a second every four seconds (the idle-loop trick — one animation, mostly silence), and a flash-sale bar where the CTA pairs its shake with a shine sweep and a live countdown so urgency has a reason.
## HTML
```html
<div class="shk-12-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-12a" aria-label="Product card with periodically shaking buy button">
  <article class="shk-12a__card">
    <div class="shk-12a__imgwrap"><img class="shk-12a__img" src="https://picsum.photos/id/26/640/440" alt="Everyday carry flat lay: sunglasses, watch and leather accessories" loading="lazy"><span class="shk-12a__flag">Only 3 left</span></div>
    <div class="shk-12a__body">
      <h2 class="shk-12a__name">Field kit · No. 04</h2>
      <p class="shk-12a__meta">Waxed canvas & brass</p>
      <div class="shk-12a__row"><span class="shk-12a__price">$89</span><button class="shk-12a__buy" type="button">Buy now</button></div>
    </div>
  </article>
  <p class="shk-12a__hint" aria-hidden="true">wait ~4s — the button nudges, then goes quiet (hover pauses the loop)</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<section class="shk-12b" aria-label="Flash sale bar with synced shake and shine CTA">
  <div class="shk-12b__bar">
    <div class="shk-12b__left"><span class="shk-12b__pulse" aria-hidden="true"></span><p class="shk-12b__copy"><b>Flash drop</b> · 30% off everything</p></div>
    <p class="shk-12b__clock" id="shk-12b-clock" aria-live="off">09:41</p>
    <button class="shk-12b__cta" type="button"><span class="shk-12b__ctain">Shop the drop</span></button>
  </div>
  <p class="shk-12b__hint" aria-hidden="true">every 5s the CTA shakes as the shine sweeps — light and motion say “here” together</p>
</section>
</div>
```
## CSS
```css
.shk-12-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-12-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-12a,
.shk-12a *,
.shk-12a *::before,
.shk-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-12a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 20px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f4f0,#ebe7df);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-12a__card {
  width: min(330px,88vw);
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(30,27,22,.1);
  box-shadow: 0 30px 60px -35px rgba(30,27,22,.5);
  overflow: hidden;
}

.shk-12a__imgwrap {
  position: relative;
}

.shk-12a__img {
  display: block;
  width: 100%;
  height: 210px;
  object-fit: cover;
}

.shk-12a__flag {
  position: absolute;
  top: 12px;
  left: 12px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #fff;
  background: oklch(0.55 0.18 30 / .92);
  padding: 5px 10px;
  border-radius: 999px;
  backdrop-filter: blur(4px);
}

.shk-12a__body {
  padding: 18px 20px 20px;
}

.shk-12a__name {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #1e1b16;
}

.shk-12a__meta {
  margin-top: 3px;
  font-size: 12.5px;
  color: rgba(30,27,22,.5);
}

.shk-12a__row {
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.shk-12a__price {
  font-size: 22px;
  font-weight: 900;
  color: #1e1b16;
}

.shk-12a__buy {
  padding: 12px 24px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 800;
  color: #fff;
  background: #1e1b16;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  animation: shk-12a-nudge 4s ease-in-out 2s infinite;
  transition: background .2s,scale .12s;
}

.shk-12a__buy:hover {
  background: #3a352c;
  animation-play-state: paused;
}

.shk-12a__buy:active {
  scale: .96;
}

.shk-12a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(30,27,22,.45);
}

@keyframes shk-12a-nudge {
  0%,
    3% {
    rotate: 0deg;
    translate: 0 0;
  }

  4.5% {
    rotate: -3deg;
    translate: -2px 0;
  }

  6% {
    rotate: 2.5deg;
    translate: 2px 0;
  }

  7.5% {
    rotate: -1.5deg;
    translate: -1px 0;
  }

  9% {
    rotate: .8deg;
    translate: 1px 0;
  }

  12%,
    100% {
    rotate: 0deg;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-12a__buy {
    animation: none;
  }
}

.shk-12b,
.shk-12b *,
.shk-12b *::before,
.shk-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-12b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 18px;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 100%,#1c1030,#0d0916 60%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-12b__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 18px 26px;
  padding: 16px 22px;
  border-radius: 16px;
  background: rgba(255,255,255,.05);
  border: 1px solid oklch(0.75 0.16 320 / .35);
  box-shadow: 0 30px 70px -40px oklch(0.75 0.16 320 / .5);
}

.shk-12b__left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.shk-12b__pulse {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.75 0.18 320);
  box-shadow: 0 0 0 0 oklch(0.75 0.18 320 / .6);
  animation: shk-12b-ping 2.5s ease-out infinite;
}

.shk-12b__copy {
  font-size: 14.5px;
  color: rgba(240,230,255,.75);
}

.shk-12b__copy b {
  color: #fff;
  font-weight: 700;
}

.shk-12b__clock {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 16px;
  font-weight: 700;
  color: oklch(0.85 0.12 320);
  letter-spacing: .08em;
}

.shk-12b__cta {
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.shk-12b__ctain {
  display: inline-block;
  padding: 13px 26px;
  border-radius: 11px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 700;
  color: #14091f;
  background: linear-gradient(110deg,oklch(0.82 0.16 320),oklch(0.87 0.14 340) 45%,#fff 50%,oklch(0.87 0.14 340) 55%,oklch(0.82 0.16 320));
  background-size: 300% 100%;
  background-position: 0% 0;
  animation: shk-12b-burst 5s cubic-bezier(.36,.07,.19,.97) infinite;
}

.shk-12b__cta:active .shk-12b__ctain {
  scale: .96;
}

.shk-12b__cta:focus-visible {
  outline: none;
}

.shk-12b__cta:focus-visible .shk-12b__ctain {
  outline: 2px solid oklch(0.82 0.16 320);
  outline-offset: 3px;
}

.shk-12b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(240,230,255,.35);
}

@keyframes shk-12b-ping {
  0% {
    box-shadow: 0 0 0 0 oklch(0.75 0.18 320 / .6);
  }

  70%,
    100% {
    box-shadow: 0 0 0 12px oklch(0.75 0.18 320 / 0);
  }
}

@keyframes shk-12b-burst {
  0%,
    2% {
    translate: 0 0;
    background-position: 0% 0;
  }

  3.5% {
    translate: -4px 0;
  }

  5% {
    translate: 4px 0;
  }

  6.5% {
    translate: -2px 0;
  }

  8% {
    translate: 1px 0;
  }

  10% {
    translate: 0 0;
  }

  12% {
    background-position: -150% 0;
  }

  100% {
    translate: 0 0;
    background-position: -150% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-12b__ctain {
    animation: none;
    background-position: 0% 0;
  }

  .shk-12b__pulse {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a .5s wiggle stretched across a 4s timeline (burst in the first 12%, silence after). Hover pauses via animation-play-state: once the cursor arrives, the nudge has done its job. */

(function(){
  // One-line countdown; the shake/shine loop is pure CSS.
  var el=document.getElementById('shk-12b-clock'); if(!el) return;
  var t=9*60+41;
  setInterval(function(){ t=Math.max(0,t-1); el.textContent=String(Math.floor(t/60)).padStart(2,'0')+':'+String(t%60).padStart(2,'0'); },1000);
})();
```
