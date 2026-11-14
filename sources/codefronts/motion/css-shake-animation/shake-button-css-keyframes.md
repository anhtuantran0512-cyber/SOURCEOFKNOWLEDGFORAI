---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/shake-button-css-keyframes/"
title: "Shake Button CSS Keyframes"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The keyframe cookbook: four buttons carrying the four base shakes (horizontal, vertical, rotate, chaos) with their frame tables on the card, and a tunable…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shake Button CSS Keyframes
Source: https://codefronts.com/motion/css-shake-animation/shake-button-css-keyframes/

The keyframe cookbook: four buttons carrying the four base shakes (horizontal, vertical, rotate, chaos) with their frame tables on the card, and a tunable specimen where amplitude and speed are CSS custom properties you flip live — one @keyframes rule, infinite variants.
## HTML
```html
<div class="shk-11-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-11a" aria-label="Four base shake keyframes on four buttons">
  <div class="shk-11a__grid">
    <div class="shk-11a__cell"><button class="shk-11a__btn shk-11a__btn--x" type="button">Shake X</button><code class="shk-11a__code">translate: ±8px 0</code></div>
    <div class="shk-11a__cell"><button class="shk-11a__btn shk-11a__btn--y" type="button">Shake Y</button><code class="shk-11a__code">translate: 0 ±6px</code></div>
    <div class="shk-11a__cell"><button class="shk-11a__btn shk-11a__btn--r" type="button">Rotate</button><code class="shk-11a__code">rotate: ±4deg</code></div>
    <div class="shk-11a__cell"><button class="shk-11a__btn shk-11a__btn--c" type="button">Chaos</button><code class="shk-11a__code">all three, phase-shifted</code></div>
  </div>
  <p class="shk-11a__hint" aria-hidden="true">hover each — every button shake ever shipped is one of these four</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-11b" aria-label="Shake with live-tunable amplitude and speed">
  <div class="shk-11b__panel" id="shk-11b-panel" style="--amp:6px;--speed:.5s">
    <div class="shk-11b__group" role="group" aria-label="Amplitude"><span class="shk-11b__lab">--amp</span><button class="shk-11b__chip" type="button" data-prop="--amp" data-val="3px">3px</button><button class="shk-11b__chip is-on" type="button" data-prop="--amp" data-val="6px">6px</button><button class="shk-11b__chip" type="button" data-prop="--amp" data-val="12px">12px</button></div>
    <button class="shk-11b__btn" id="shk-11b-btn" type="button">Run the shake</button>
    <div class="shk-11b__group" role="group" aria-label="Speed"><span class="shk-11b__lab">--speed</span><button class="shk-11b__chip" type="button" data-prop="--speed" data-val=".3s">.3s</button><button class="shk-11b__chip is-on" type="button" data-prop="--speed" data-val=".5s">.5s</button><button class="shk-11b__chip" type="button" data-prop="--speed" data-val=".9s">.9s</button></div>
    <code class="shk-11b__read" id="shk-11b-read">animation: shake .5s · translate peaks at 6px</code>
  </div>
</section>
</div>
```
## CSS
```css
.shk-11-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-11-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-11a,
.shk-11a *,
.shk-11a *::before,
.shk-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-11a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: #f2efe8;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-11a__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(170px,1fr));
  gap: 18px;
  width: min(760px,90vw);
}

.shk-11a__cell {
  display: grid;
  gap: 12px;
  justify-items: center;
  padding: 28px 18px;
  background: #fff;
  border: 2px solid #17150f;
  border-radius: 16px;
  box-shadow: 5px 5px 0 #17150f;
}

.shk-11a__btn {
  padding: 14px 26px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  border: 2px solid #17150f;
  border-radius: 12px;
  cursor: pointer;
  transition: scale .12s;
}

.shk-11a__btn:active {
  scale: .95;
}

.shk-11a__btn--x {
  background: oklch(0.85 0.16 85);
  color: #17150f;
}

.shk-11a__btn--y {
  background: oklch(0.8 0.14 200);
  color: #17150f;
}

.shk-11a__btn--r {
  background: oklch(0.78 0.16 340);
  color: #17150f;
}

.shk-11a__btn--c {
  background: #17150f;
  color: #f2efe8;
}

.shk-11a__btn--x:hover {
  animation: shk-11a-x .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-11a__btn--y:hover {
  animation: shk-11a-y .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-11a__btn--r:hover {
  animation: shk-11a-r .55s ease-in-out;
}

.shk-11a__btn--c:hover {
  animation: shk-11a-c .55s cubic-bezier(.36,.07,.19,.97);
}

.shk-11a__code {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11px;
  color: rgba(23,21,15,.6);
  background: rgba(23,21,15,.06);
  padding: 4px 9px;
  border-radius: 6px;
}

.shk-11a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(23,21,15,.5);
}

@keyframes shk-11a-x {
  12% {
    translate: -8px 0;
  }

  30% {
    translate: 7px 0;
  }

  48% {
    translate: -5px 0;
  }

  66% {
    translate: 3px 0;
  }

  84% {
    translate: -1px 0;
  }
}

@keyframes shk-11a-y {
  12% {
    translate: 0 -6px;
  }

  30% {
    translate: 0 5px;
  }

  48% {
    translate: 0 -4px;
  }

  66% {
    translate: 0 2px;
  }

  84% {
    translate: 0 -1px;
  }
}

@keyframes shk-11a-r {
  15% {
    rotate: -4deg;
  }

  35% {
    rotate: 3.5deg;
  }

  55% {
    rotate: -2.5deg;
  }

  75% {
    rotate: 1.5deg;
  }

  90% {
    rotate: -.5deg;
  }
}

@keyframes shk-11a-c {
  12% {
    translate: -6px 2px;
    rotate: -1.2deg;
  }

  30% {
    translate: 5px -2px;
    rotate: 1deg;
  }

  48% {
    translate: -4px 1px;
    rotate: -.7deg;
  }

  66% {
    translate: 2px -1px;
    rotate: .4deg;
  }

  84% {
    translate: -1px 0;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-11a__btn:hover {
    animation: none!important;
  }
}

.shk-11b,
.shk-11b *,
.shk-11b *::before,
.shk-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-11b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#101322,#0a0c16);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-11b__panel {
  display: grid;
  gap: 22px;
  justify-items: center;
  padding: 40px 36px;
  border-radius: 22px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(150,175,235,.16);
}

.shk-11b__group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.shk-11b__lab {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 12px;
  color: oklch(0.78 0.12 250);
  margin-right: 4px;
}

.shk-11b__chip {
  padding: 8px 14px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: rgba(225,232,250,.7);
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(150,175,235,.2);
  border-radius: 999px;
  cursor: pointer;
  transition: background .15s,color .15s,border-color .15s;
}

.shk-11b__chip:hover {
  background: rgba(255,255,255,.1);
}

.shk-11b__chip.is-on {
  background: oklch(0.78 0.12 250 / .18);
  border-color: oklch(0.78 0.12 250);
  color: #eaf0ff;
}

.shk-11b__btn {
  padding: 18px 42px;
  font: inherit;
  font-size: 17px;
  font-weight: 700;
  color: #0a0c16;
  background: linear-gradient(180deg,#e8efff,#bcd0f5);
  border: 0;
  border-radius: 14px;
  cursor: pointer;
  transition: transform .15s;
}

.shk-11b__btn:active {
  transform: scale(.97);
}

.shk-11b__btn.is-shaking {
  animation: shk-11b-shake var(--speed,.5s) cubic-bezier(.36,.07,.19,.97);
}

.shk-11b__read {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11.5px;
  color: rgba(225,232,250,.45);
}

@keyframes shk-11b-shake {
  12% {
    translate: calc(var(--amp) * -1) 0;
  }

  30% {
    translate: calc(var(--amp) * .9) 0;
  }

  48% {
    translate: calc(var(--amp) * -.65) 0;
  }

  66% {
    translate: calc(var(--amp) * .4) 0;
  }

  84% {
    translate: calc(var(--amp) * -.15) 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-11b__btn.is-shaking {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — four @keyframes, one per base motion. The chaos variant phase-shifts X, Y and rotation so no two axes peak on the same frame; that desync is what makes it read as chaos. */

(function(){
  var panel=document.getElementById('shk-11b-panel'); if(!panel) return;
  var btn=document.getElementById('shk-11b-btn'),read=document.getElementById('shk-11b-read');
  btn.addEventListener('animationend',function(){ btn.classList.remove('is-shaking'); });
  function play(){ btn.classList.remove('is-shaking'); requestAnimationFrame(function(){ requestAnimationFrame(function(){ btn.classList.add('is-shaking'); }); }); }
  panel.addEventListener('click',function(e){
    var chip=e.target.closest('.shk-11b__chip');
    if(chip){
      panel.style.setProperty(chip.dataset.prop,chip.dataset.val);
      chip.parentElement.querySelectorAll('.shk-11b__chip').forEach(function(c){ c.classList.toggle('is-on',c===chip); });
      read.textContent='animation: shake '+getComputedStyle(panel).getPropertyValue('--speed').trim()+' · translate peaks at '+getComputedStyle(panel).getPropertyValue('--amp').trim();
      play(); return;
    }
    if(e.target===btn) play();
  });
})();
```
