---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-screen-shake-effect-keyframes/"
title: "CSS Screen Shake Effect Keyframes"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Full-screen impact, engineered safely: a detonation stage where the entire scene shakes on multi-axis keyframes with a flash and vignette pulse (shaking a…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Screen Shake Effect Keyframes
Source: https://codefronts.com/motion/css-shake-animation/css-screen-shake-effect-keyframes/

Full-screen impact, engineered safely: a detonation stage where the entire scene shakes on multi-axis keyframes with a flash and vignette pulse (shaking a wrapper div, never body), and a rumble lab with a live intensity slider — @property-registered custom properties driving amplitude and rotation so you can dial the earthquake from 0 to 10.
## HTML
```html
<div class="shk-30-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=Pixelify+Sans:[email protected]&display=swap" rel="stylesheet">
<section class="shk-30a" aria-label="Full stage screen shake on detonation">
  <div class="shk-30a__clip">
    <div class="shk-30a__screen" id="shk-30a-screen">
      <div class="shk-30a__grid" aria-hidden="true"></div>
      <p class="shk-30a__mission">SECTOR 7 · DEMOLITION RANGE</p>
      <p class="shk-30a__big" id="shk-30a-big">ARMED</p>
      <button class="shk-30a__btn" id="shk-30a-btn" type="button">DETONATE</button>
      <p class="shk-30a__note">the wrapper shakes — <b>body never moves</b>, overlays stay outside</p>
    </div>
    <div class="shk-30a__flash" id="shk-30a-flash" aria-hidden="true"></div>
    <div class="shk-30a__vig" id="shk-30a-vig" aria-hidden="true"></div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-30b" aria-label="Continuous screen rumble with intensity slider">
  <div class="shk-30b__clip">
    <div class="shk-30b__world" id="shk-30b-world" style="--amp:0px;--rot:0deg">
      <div class="shk-30b__skyline" aria-hidden="true"><i style="--h:64px"></i><i style="--h:110px"></i><i style="--h:84px"></i><i style="--h:140px"></i><i style="--h:96px"></i><i style="--h:120px"></i><i style="--h:70px"></i></div>
      <p class="shk-30b__label">RICHTER LAB</p>
    </div>
    <div class="shk-30b__panel">
      <label class="shk-30b__row" for="shk-30b-dial"><span>Intensity</span><input class="shk-30b__dial" id="shk-30b-dial" type="range" min="0" max="10" step="1" value="0"><output class="shk-30b__out" id="shk-30b-out" for="shk-30b-dial">0</output></label>
      <code class="shk-30b__code" id="shk-30b-code">--amp: 0px · --rot: 0deg</code>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.shk-30-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.shk-30-group > section {
  width: 100%;
}

.shk-30a,
.shk-30a *,
.shk-30a *::before,
.shk-30a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-30a {
  width: 100%;
  min-height: 100vh;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-30a__clip {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: #0a0b0f;
}

.shk-30a__screen {
  position: absolute;
  inset: -24px;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 18px;
  text-align: center;
  background: radial-gradient(110% 110% at 50% 100%,#181b26,#0a0b0f 65%);
  padding: 24px;
}

.shk-30a__screen.is-quaking {
  animation: shk-30a-quake .55s steps(2,jump-none);
}

.shk-30a__grid {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(120,150,220,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(120,150,220,.07) 1px,transparent 1px);
  background-size: 44px 44px;
  pointer-events: none;
}

.shk-30a__mission {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .3em;
  color: rgba(200,215,245,.5);
}

.shk-30a__big {
  font-family: 'Pixelify Sans',monospace;
  font-size: clamp(44px,9vw,92px);
  letter-spacing: .06em;
  color: #eef2ff;
  text-shadow: 0 0 40px rgba(140,170,255,.35);
}

.shk-30a__big.boom {
  color: oklch(0.78 0.18 55);
  text-shadow: 0 0 50px oklch(0.72 0.19 55 / .7);
}

.shk-30a__btn {
  padding: 16px 40px;
  font-family: 'Pixelify Sans',monospace;
  font-size: 18px;
  letter-spacing: .12em;
  color: #0a0b0f;
  background: oklch(0.72 0.19 55);
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  transition: filter .15s,scale .12s;
}

.shk-30a__btn:hover {
  filter: brightness(1.1);
}

.shk-30a__btn:active {
  scale: .95;
}

.shk-30a__note {
  font-size: 12px;
  color: rgba(200,215,245,.45);
}

.shk-30a__note b {
  color: rgba(230,240,255,.8);
}

.shk-30a__flash {
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  pointer-events: none;
}

.shk-30a__flash.go {
  animation: shk-30a-flash .5s ease-out;
}

.shk-30a__vig {
  position: absolute;
  inset: 0;
  box-shadow: inset 0 0 0 0 transparent;
  pointer-events: none;
}

.shk-30a__vig.go {
  animation: shk-30a-vig .8s ease-out;
}

@keyframes shk-30a-quake {
  0% {
    translate: -14px 8px;
    rotate: -.7deg;
  }

  20% {
    translate: 12px -10px;
    rotate: .6deg;
  }

  40% {
    translate: -10px -6px;
    rotate: -.45deg;
  }

  60% {
    translate: 12px 8px;
    rotate: .5deg;
  }

  80% {
    translate: -6px 4px;
    rotate: -.25deg;
  }

  100% {
    translate: 0 0;
    rotate: 0deg;
  }
}

@keyframes shk-30a-flash {
  0% {
    opacity: .9;
  }

  100% {
    opacity: 0;
  }
}

@keyframes shk-30a-vig {
  0% {
    box-shadow: inset 0 0 120px 40px oklch(0.6 0.21 40 / .55);
  }

  100% {
    box-shadow: inset 0 0 0 0 transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-30a__screen.is-quaking {
    animation: none;
  }

  .shk-30a__flash.go {
    animation: shk-30a-flash 1.2s ease-out;
  }
}

.shk-30b,
.shk-30b *,
.shk-30b *::before,
.shk-30b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --shk-30b-amp {
  syntax: "<length>";
  inherits: true;
  initial-value: 0px;
}

@property --shk-30b-rot {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}

.shk-30b {
  width: 100%;
  min-height: 100vh;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-30b__clip {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: #0b0d13;
  display: grid;
}

.shk-30b__world {
  position: absolute;
  inset: -26px;
  display: grid;
  place-content: center;
  gap: 26px;
  justify-items: center;
  background: linear-gradient(180deg,#10131c 55%,#171c29);
  --shk-30b-amp: var(--amp);
  --shk-30b-rot: var(--rot);
  transition: --shk-30b-amp .4s ease,--shk-30b-rot .4s ease;
  animation: shk-30b-rumble .14s steps(2,jump-none) infinite;
}

.shk-30b__skyline {
  display: flex;
  align-items: flex-end;
  gap: 10px;
}

.shk-30b__skyline i {
  width: 34px;
  height: var(--h);
  background: linear-gradient(180deg,#232a3d,#181e2d);
  border: 1px solid rgba(140,165,220,.2);
  border-bottom: 0;
  border-radius: 4px 4px 0 0;
  box-shadow: inset 0 8px 0 rgba(140,165,220,.12);
}

.shk-30b__label {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .34em;
  color: rgba(205,220,248,.55);
}

.shk-30b__panel {
  position: absolute;
  left: 50%;
  bottom: 36px;
  translate: -50% 0;
  display: grid;
  gap: 10px;
  justify-items: center;
  padding: 16px 22px;
  border-radius: 16px;
  background: rgba(10,12,18,.75);
  border: 1px solid rgba(150,175,230,.2);
  backdrop-filter: blur(10px);
}

.shk-30b__row {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 13.5px;
  font-weight: 600;
  color: #dde6f8;
}

.shk-30b__dial {
  width: min(240px,50vw);
  accent-color: oklch(0.72 0.17 45);
}

.shk-30b__out {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 14px;
  font-weight: 700;
  color: oklch(0.78 0.15 45);
  min-width: 2ch;
  text-align: right;
}

.shk-30b__code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11px;
  color: rgba(205,220,248,.5);
}

@keyframes shk-30b-rumble {
  0% {
    translate: calc(var(--shk-30b-amp) * -1) calc(var(--shk-30b-amp) * .6);
    rotate: calc(var(--shk-30b-rot) * -1);
  }

  100% {
    translate: var(--shk-30b-amp) calc(var(--shk-30b-amp) * -.6);
    rotate: var(--shk-30b-rot);
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-30b__world {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var screen=document.getElementById('shk-30a-screen'); if(!screen) return;
  var btn=document.getElementById('shk-30a-btn'),big=document.getElementById('shk-30a-big'),
      flash=document.getElementById('shk-30a-flash'),vig=document.getElementById('shk-30a-vig');
  screen.addEventListener('animationend',function(){ screen.classList.remove('is-quaking'); });
  flash.addEventListener('animationend',function(){ flash.classList.remove('go'); });
  vig.addEventListener('animationend',function(){ vig.classList.remove('go'); });
  btn.addEventListener('click',function(){
    big.textContent='BOOM'; big.classList.add('boom');
    screen.classList.remove('is-quaking'); flash.classList.remove('go'); vig.classList.remove('go');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){
      screen.classList.add('is-quaking'); flash.classList.add('go'); vig.classList.add('go');
    }); });
    setTimeout(function(){ big.textContent='ARMED'; big.classList.remove('boom'); },1400);
  });
})();

(function(){
  var world=document.getElementById('shk-30b-world'); if(!world) return;
  var dial=document.getElementById('shk-30b-dial'),out=document.getElementById('shk-30b-out'),
      code=document.getElementById('shk-30b-code');
  dial.addEventListener('input',function(){
    var v=parseInt(dial.value,10);
    var amp=(v*1.4).toFixed(1)+'px', rot=(v*.08).toFixed(2)+'deg';
    world.style.setProperty('--amp',amp);
    world.style.setProperty('--rot',rot);
    out.textContent=String(v);
    code.textContent='--amp: '+amp+' · --rot: '+rot;
  });
})();
```
