---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-hit-damage-shake-effect-for-web-games/"
title: "CSS Hit Damage Shake Effect for Web Games"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Game feel in the DOM: a battle card that takes hits — knockback shake away from the blow, floating damage numbers, white hit-flash, HP draining to a knockout…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hit Damage Shake Effect for Web Games
Source: https://codefronts.com/motion/css-shake-animation/css-hit-damage-shake-effect-for-web-games/

Game feel in the DOM: a battle card that takes hits — knockback shake away from the blow, floating damage numbers, white hit-flash, HP draining to a knockout tilt — and a combo trainer where rapid hits scale the shake's amplitude through a CSS custom property, so the tenth hit rattles harder than the first.
## HTML
```html
<div class="shk-29-group">
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:[email protected]&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-29a" aria-label="Battle demo: attack a card, it shakes and loses HP">
  <div class="shk-29a__arena">
    <div class="shk-29a__target" id="shk-29a-target" style="--amp:8px">
      <div class="shk-29a__flash" aria-hidden="true"></div>
      <p class="shk-29a__mob" aria-hidden="true">◆</p>
      <p class="shk-29a__name">CRYSTAL GOLEM</p>
      <div class="shk-29a__hpwrap" role="img" aria-label="Golem health"><div class="shk-29a__hp" id="shk-29a-hp"></div></div>
      <p class="shk-29a__hptxt" id="shk-29a-hptxt" aria-live="off">100 / 100</p>
    </div>
    <div class="shk-29a__ctl">
      <button class="shk-29a__atk" id="shk-29a-atk" type="button">ATTACK</button>
      <button class="shk-29a__crit" id="shk-29a-crit" type="button">CRIT ×3</button>
      <button class="shk-29a__reset" id="shk-29a-reset" type="button">Reset</button>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:[email protected]&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-29b" aria-label="Combo demo where rapid hits increase shake intensity">
  <div class="shk-29b__stage">
    <p class="shk-29b__combo" id="shk-29b-combo" aria-live="off">COMBO ×0</p>
    <button class="shk-29b__pad" id="shk-29b-pad" type="button" style="--amp:0px">
      <span class="shk-29b__padtxt">HIT ME FAST</span>
    </button>
    <p class="shk-29b__meta" id="shk-29b-meta">amplitude 0px — each rapid hit adds 1.5px, idle 900ms resets</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-29-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-29-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-29a,
.shk-29a *,
.shk-29a *::before,
.shk-29a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-29a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 90% at 50% 20%,#1c1433,#0e0a1c 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-29a__arena {
  display: grid;
  justify-items: center;
  gap: 26px;
}

.shk-29a__target {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 10px;
  width: min(300px,80vw);
  padding: 30px 26px;
  border-radius: 18px;
  background: linear-gradient(180deg,#241b44,#1a1233);
  border: 2px solid oklch(0.7 0.14 300 / .5);
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.95);
}

.shk-29a__target.is-hit {
  animation: shk-29a-shake .4s cubic-bezier(.36,.07,.19,.97);
}

.shk-29a__target.is-ko {
  rotate: 5deg;
  translate: 0 8px;
  filter: saturate(.4) brightness(.75);
  transition: rotate .5s cubic-bezier(.34,1.56,.64,1),translate .5s,filter .5s;
}

.shk-29a__flash {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: #fff;
  opacity: 0;
  pointer-events: none;
}

.shk-29a__target.is-hit .shk-29a__flash {
  animation: shk-29a-flash .4s ease-out;
}

.shk-29a__mob {
  font-size: 64px;
  line-height: 1;
  color: oklch(0.78 0.16 300);
  filter: drop-shadow(0 0 18px oklch(0.78 0.16 300 / .6));
}

.shk-29a__name {
  font-family: 'Pixelify Sans',monospace;
  font-size: 17px;
  letter-spacing: .1em;
  color: #efeaff;
}

.shk-29a__hpwrap {
  width: 100%;
  height: 14px;
  border-radius: 999px;
  background: rgba(0,0,0,.5);
  border: 1.5px solid oklch(0.7 0.14 300 / .4);
  overflow: hidden;
}

.shk-29a__hp {
  width: 100%;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg,oklch(0.75 0.19 145),oklch(0.85 0.18 110));
  transform-origin: 0 50%;
  transition: scale .35s cubic-bezier(.2,.9,.3,1.2),background .35s;
}

.shk-29a__hp.low {
  background: linear-gradient(90deg,oklch(0.62 0.23 27),oklch(0.72 0.19 55));
}

.shk-29a__hptxt {
  font-family: 'Pixelify Sans',monospace;
  font-size: 13px;
  color: rgba(239,234,255,.65);
}

.shk-29a__ctl {
  display: flex;
  gap: 10px;
}

.shk-29a__atk,
.shk-29a__crit,
.shk-29a__reset {
  padding: 13px 22px;
  font-family: 'Pixelify Sans',monospace;
  font-size: 15px;
  letter-spacing: .08em;
  border-radius: 11px;
  cursor: pointer;
  transition: filter .15s,scale .12s;
}

.shk-29a__atk {
  border: 0;
  color: #0e0a1c;
  background: oklch(0.8 0.16 85);
}

.shk-29a__crit {
  border: 0;
  color: #fff;
  background: oklch(0.6 0.24 27);
}

.shk-29a__reset {
  border: 1.5px solid rgba(239,234,255,.3);
  color: #efeaff;
  background: transparent;
  font-size: 13px;
}

.shk-29a__atk:hover,
.shk-29a__crit:hover,
.shk-29a__reset:hover {
  filter: brightness(1.12);
}

.shk-29a__atk:active,
.shk-29a__crit:active,
.shk-29a__reset:active {
  scale: .95;
}

.shk-29a__dmg {
  position: absolute;
  top: 8px;
  left: 50%;
  font-family: 'Pixelify Sans',monospace;
  font-size: 26px;
  font-weight: 700;
  color: oklch(0.85 0.17 85);
  text-shadow: 0 2px 0 rgba(0,0,0,.5);
  pointer-events: none;
  animation: shk-29a-float .8s ease-out forwards;
}

.shk-29a__dmg.crit {
  font-size: 34px;
  color: oklch(0.72 0.22 27);
}

@keyframes shk-29a-shake {
  15% {
    translate: calc(var(--amp) * -1) 2px;
    rotate: -1.4deg;
  }

  30% {
    translate: calc(var(--amp) * .8) -3px;
    rotate: 1.1deg;
  }

  45% {
    translate: calc(var(--amp) * -.6) 1px;
    rotate: -.8deg;
  }

  60% {
    translate: calc(var(--amp) * .4) -1px;
    rotate: .5deg;
  }

  80% {
    translate: calc(var(--amp) * -.15) 0;
    rotate: 0deg;
  }
}

@keyframes shk-29a-flash {
  0% {
    opacity: .85;
  }

  100% {
    opacity: 0;
  }
}

@keyframes shk-29a-float {
  0% {
    opacity: 0;
    translate: -50% 6px;
    scale: .6;
  }

  18% {
    opacity: 1;
    scale: 1.15;
  }

  100% {
    opacity: 0;
    translate: -50% -46px;
    scale: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-29a__target.is-hit {
    animation: none;
  }

  .shk-29a__dmg {
    animation: shk-29a-fade .8s ease-out forwards;
  }
}

@keyframes shk-29a-fade {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

.shk-29b,
.shk-29b *,
.shk-29b *::before,
.shk-29b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-29b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#131018,#0c0a10);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-29b__stage {
  display: grid;
  justify-items: center;
  gap: 20px;
}

.shk-29b__combo {
  font-family: 'Pixelify Sans',monospace;
  font-size: 30px;
  letter-spacing: .1em;
  color: oklch(0.82 0.17 85);
  text-shadow: 0 0 24px oklch(0.82 0.17 85 / .4);
  transition: scale .12s;
}

.shk-29b__combo.bump {
  scale: 1.18;
}

.shk-29b__pad {
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.shk-29b__padtxt {
  display: grid;
  place-items: center;
  width: min(260px,70vw);
  height: 150px;
  border-radius: 20px;
  font-family: 'Pixelify Sans',monospace;
  font-size: 22px;
  letter-spacing: .08em;
  color: #f4f0ff;
  background: linear-gradient(180deg,#2b2140,#1e1730);
  border: 2px solid oklch(0.72 0.19 25 / .55);
  box-shadow: 0 30px 60px -35px rgba(0,0,0,.95);
}

.shk-29b__pad.is-hit .shk-29b__padtxt {
  animation: shk-29b-shake .3s cubic-bezier(.36,.07,.19,.97);
}

.shk-29b__pad:active .shk-29b__padtxt {
  scale: .97;
}

.shk-29b__meta {
  font-size: 12.5px;
  color: rgba(244,240,255,.45);
}

@keyframes shk-29b-shake {
  20% {
    translate: calc(var(--amp) * -1) calc(var(--amp) * .3);
    rotate: -1deg;
  }

  40% {
    translate: calc(var(--amp) * .85) calc(var(--amp) * -.25);
    rotate: .8deg;
  }

  60% {
    translate: calc(var(--amp) * -.6) calc(var(--amp) * .2);
    rotate: -.5deg;
  }

  80% {
    translate: calc(var(--amp) * .3) 0;
    rotate: .3deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-29b__pad.is-hit .shk-29b__padtxt {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var target=document.getElementById('shk-29a-target'); if(!target) return;
  var hpBar=document.getElementById('shk-29a-hp'),hpTxt=document.getElementById('shk-29a-hptxt'),
      atk=document.getElementById('shk-29a-atk'),crit=document.getElementById('shk-29a-crit'),
      reset=document.getElementById('shk-29a-reset'),max=100,hp=100;
  target.addEventListener('animationend',function(e){
    if(e.animationName==='shk-29a-shake') target.classList.remove('is-hit');   // guard: flash ends separately
  });
  function paint(){
    hpBar.style.scale=(hp/max)+' 1';
    hpBar.classList.toggle('low',hp/max<=.35);
    hpTxt.textContent=hp+' / '+max;
    target.classList.toggle('is-ko',hp===0);
  }
  function hit(dmg,isCrit){
    if(hp===0) return;
    hp=Math.max(0,hp-dmg);
    target.style.setProperty('--amp',Math.min(4+dmg/3,16)+'px');               // damage -> violence
    target.classList.remove('is-hit');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ target.classList.add('is-hit'); }); });
    var n=document.createElement('span');
    n.className='shk-29a__dmg'+(isCrit?' crit':''); n.textContent='-'+dmg+(isCrit?'!':'');
    n.style.left=(35+Math.random()*30)+'%';
    target.appendChild(n);
    n.addEventListener('animationend',function(){ n.remove(); });              // never leak spans
    paint();
    if(hp===0) hpTxt.textContent='KO — nice hit';
  }
  atk.addEventListener('click',function(){ hit(8+Math.floor(Math.random()*8),false); });
  crit.addEventListener('click',function(){ hit(3*(8+Math.floor(Math.random()*6)),true); });
  reset.addEventListener('click',function(){ hp=max; paint(); });
  paint();
})();

(function(){
  var pad=document.getElementById('shk-29b-pad'); if(!pad) return;
  var combo=document.getElementById('shk-29b-combo'),meta=document.getElementById('shk-29b-meta'),
      n=0,idleTimer=null;
  pad.addEventListener('animationend',function(){ pad.classList.remove('is-hit'); });
  pad.addEventListener('click',function(){
    n++;
    var amp=Math.min(2+n*1.5,18);                       // combo -> amplitude, clamped
    pad.style.setProperty('--amp',amp+'px');
    combo.textContent='COMBO ×'+n;
    combo.classList.add('bump'); setTimeout(function(){ combo.classList.remove('bump'); },110);
    meta.textContent='amplitude '+amp.toFixed(1)+'px — keep clicking to climb';
    pad.classList.remove('is-hit');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ pad.classList.add('is-hit'); }); });
    clearTimeout(idleTimer);
    idleTimer=setTimeout(function(){ n=0; pad.style.setProperty('--amp','0px'); combo.textContent='COMBO ×0'; meta.textContent='amplitude 0px — each rapid hit adds 1.5px, idle 900ms resets'; },900);
  });
})();
```
