---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/3d-tilt-glassmorphism-card-css-vanilla-js/"
title: "3D Tilt Glassmorphism Card CSS Vanilla JS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The definitive tilt, twice: ~20 lines of dependency-free vanilla JS driving rotateX/rotateY from the pointer with a glare highlight that follows the cursor…"
has_js: "true"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Tilt Glassmorphism Card CSS Vanilla JS
Source: https://codefronts.com/components/css-glassmorphism-cards/3d-tilt-glassmorphism-card-css-vanilla-js/

The definitive tilt, twice: ~20 lines of dependency-free vanilla JS driving rotateX/rotateY from the pointer with a glare highlight that follows the cursor and parallax layers at different translateZ depths — and the zero-JS alternative: a 9-zone pure-CSS tilt grid that snaps the same card toward whichever region you hover.
## HTML
```html
<div class="glz-21-group">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:[email protected]&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-21a" aria-label="3D tilt glassmorphism card demo">
  <div class="glz-21a__card" tabindex="0" role="img" aria-label="Aurora Pass membership card, tier Obsidian">
    <i class="glz-21a__glare" aria-hidden="true"></i>
    <header class="glz-21a__top glz-21a__lift1"><span>AURORA PASS</span><em>№ 0042</em></header>
    <div class="glz-21a__gem glz-21a__lift2" aria-hidden="true">◆</div>
    <footer class="glz-21a__bot glz-21a__lift1"><b>Obsidian tier</b><span>Holder · R. Vega — since 2024</span></footer>
  </div>
  <p class="glz-21a__hint" aria-hidden="true">move your pointer over the card</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-21b" aria-label="Pure CSS hover-zone tilt card">
  <div class="glz-21b__scene">
    <div class="glz-21b__zones" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
    <div class="glz-21b__card">
      <span class="glz-21b__tag">ZERO JS</span>
      <h3>Nine hover zones,<br>one posed card</h3>
      <p>Each invisible cell aims the card with a sibling selector — the whole “engine” is nine :hover rules.</p>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.glz-21-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-21-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-21a,
.glz-21a *,
.glz-21a *::before,
.glz-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-21a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: 48px 24px;
  background: #08070f;
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-21a::before {
  content: "";
  position: absolute;
  width: 56vmin;
  height: 56vmin;
  border-radius: 50%;
  background: oklch(0.55 0.24 300);
  filter: blur(95px);
  opacity: .55;
  top: -12%;
  left: 10%;
}

.glz-21a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.7 0.16 190);
  filter: blur(95px);
  opacity: .45;
  bottom: -12%;
  right: 8%;
}

.glz-21a__card {
  --rx: 0deg;
  --ry: 0deg;
  --mx: 50%;
  --my: 50%;
  position: relative;
  z-index: 1;
  width: min(380px,100%);
  aspect-ratio: 8/5;
  border-radius: 24px;
  padding: 24px 26px;
  display: flex;
  flex-direction: column;
  color: #f1eefc;
  overflow: hidden;
  transform: perspective(900px) rotateX(var(--rx)) rotateY(var(--ry));
  transform-style: preserve-3d;
  transition: transform .12s ease-out;
  background: linear-gradient(135deg,rgba(255,255,255,.15),rgba(255,255,255,.05));
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255,255,255,.25);
  box-shadow: 0 36px 72px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.3);
}

.glz-21a__card.glz-21a--rest {
  transition: transform .65s cubic-bezier(.2,.8,.25,1.1);
}

.glz-21a__card:focus-visible {
  outline: 2px solid oklch(0.8 0.15 300);
  outline-offset: 5px;
}

.glz-21a__glare {
  position: absolute;
  inset: -30%;
  pointer-events: none;
  background: radial-gradient(340px circle at var(--mx) var(--my),rgba(255,255,255,.35),rgba(160,200,255,.12) 38%,transparent 60%);
  opacity: 0;
  transition: opacity .3s ease;
}

.glz-21a__card:hover .glz-21a__glare {
  opacity: 1;
}

.glz-21a__lift1 {
  transform: translateZ(34px);
}

.glz-21a__lift2 {
  transform: translateZ(58px);
}

.glz-21a__top {
  display: flex;
  justify-content: space-between;
  font-size: 11.5px;
  letter-spacing: .3em;
  color: rgba(241,238,252,.75);
}

.glz-21a__top em {
  font-style: normal;
  letter-spacing: .1em;
}

.glz-21a__gem {
  margin: auto;
  font-size: 56px;
  background: linear-gradient(135deg,oklch(0.85 0.15 300),oklch(0.8 0.16 190));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 10px 24px oklch(0.7 0.2 300/.7));
}

.glz-21a__bot b {
  display: block;
  font-family: 'Unbounded',sans-serif;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -.01em;
}

.glz-21a__bot span {
  display: block;
  margin-top: 5px;
  font-size: 11.5px;
  letter-spacing: .06em;
  color: rgba(241,238,252,.55);
}

.glz-21a__hint {
  position: relative;
  z-index: 1;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(200,190,230,.4);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-21a__card {
    background: rgba(20,16,34,.93);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-21a__card {
    transform: none;
    transition: none;
  }
}

.glz-21b,
.glz-21b *,
.glz-21b *::before,
.glz-21b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-21b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(110% 100% at 50% 0%,#131b2c,#0a0d16 65%);
}

.glz-21b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(42% 36% at 22% 24%,oklch(0.6 0.16 220/.4),transparent 70%),radial-gradient(38% 34% at 80% 78%,oklch(0.62 0.18 320/.35),transparent 70%);
}

.glz-21b__scene {
  position: relative;
  z-index: 1;
  width: min(380px,100%);
  aspect-ratio: 8/5.4;
  perspective: 900px;
}

.glz-21b__zones {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: grid;
  grid-template: repeat(3,1fr)/repeat(3,1fr);
}

.glz-21b__card {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
  padding: 30px;
  border-radius: 24px;
  color: #eef2fc;
  font-family: 'Space Grotesk',system-ui,sans-serif;
  background: linear-gradient(135deg,rgba(255,255,255,.14),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(175%);
  -webkit-backdrop-filter: blur(22px) saturate(175%);
  border: 1px solid rgba(255,255,255,.24);
  box-shadow: 0 34px 68px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.28);
  transition: transform .45s cubic-bezier(.2,.8,.25,1);
}

.glz-21b__zones i:nth-child(1):hover ~ .glz-21b__card,
.glz-21b__zones:has(i:nth-child(1):hover) + .glz-21b__card {
  transform: rotateX(9deg) rotateY(-11deg);
}

.glz-21b__zones:has(i:nth-child(2):hover) + .glz-21b__card {
  transform: rotateX(10deg);
}

.glz-21b__zones:has(i:nth-child(3):hover) + .glz-21b__card {
  transform: rotateX(9deg) rotateY(11deg);
}

.glz-21b__zones:has(i:nth-child(4):hover) + .glz-21b__card {
  transform: rotateY(-12deg);
}

.glz-21b__zones:has(i:nth-child(5):hover) + .glz-21b__card {
  transform: translateZ(14px);
}

.glz-21b__zones:has(i:nth-child(6):hover) + .glz-21b__card {
  transform: rotateY(12deg);
}

.glz-21b__zones:has(i:nth-child(7):hover) + .glz-21b__card {
  transform: rotateX(-9deg) rotateY(-11deg);
}

.glz-21b__zones:has(i:nth-child(8):hover) + .glz-21b__card {
  transform: rotateX(-10deg);
}

.glz-21b__zones:has(i:nth-child(9):hover) + .glz-21b__card {
  transform: rotateX(-9deg) rotateY(11deg);
}

.glz-21b__tag {
  align-self: flex-start;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .24em;
  padding: 6px 11px;
  border-radius: 99px;
  color: oklch(0.85 0.14 190);
  background: oklch(0.85 0.14 190/.12);
  border: 1px solid oklch(0.85 0.14 190/.4);
}

.glz-21b__card h3 {
  font-size: clamp(20px,3.6vw,25px);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.02em;
}

.glz-21b__card p {
  font-size: 13px;
  line-height: 1.6;
  color: rgba(238,242,252,.6);
  text-wrap: pretty;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-21b__card {
    background: rgba(18,24,40,.93);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-21b__card {
    transition: none;
    transform: none!important;
  }
}
```

## JavaScript
```js
/* ~20 lines of dependency-free tilt: pointer position → CSS custom properties; CSS owns the transform and glare. */
(function(){
  var card=document.querySelector('.glz-21a__card');
  if(!card||!window.matchMedia('(prefers-reduced-motion: no-preference)').matches)return;
  var raf=0;
  card.addEventListener('pointermove',function(e){
    if(raf)return;
    raf=requestAnimationFrame(function(){
      raf=0;
      var r=card.getBoundingClientRect(),
          x=(e.clientX-r.left)/r.width,
          y=(e.clientY-r.top)/r.height;
      card.classList.remove('glz-21a--rest');
      card.style.setProperty('--ry',((x-.5)*16).toFixed(2)+'deg');
      card.style.setProperty('--rx',((.5-y)*12).toFixed(2)+'deg');
      card.style.setProperty('--mx',(x*100).toFixed(1)+'%');
      card.style.setProperty('--my',(y*100).toFixed(1)+'%');
    });
  });
  card.addEventListener('pointerleave',function(){
    card.classList.add('glz-21a--rest');
    card.style.setProperty('--rx','0deg');
    card.style.setProperty('--ry','0deg');
  });
})();

/* No JavaScript — a 3×3 grid of invisible hover cells sits over the card; :has(i:hover) + sibling rules pose it toward the hovered region. */
```
