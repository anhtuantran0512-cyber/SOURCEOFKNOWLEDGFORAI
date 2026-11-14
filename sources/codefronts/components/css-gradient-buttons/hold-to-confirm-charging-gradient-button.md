---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/hold-to-confirm-charging-gradient-button/"
title: "Hold To Confirm Charging Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A destructive-action button that must be pressed and held while a conic gradient ring charges around it — it jitters nervously near completion, fires only at…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hold To Confirm Charging Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/hold-to-confirm-charging-gradient-button/

A destructive-action button that must be pressed and held while a conic gradient ring charges around it — it jitters nervously near completion, fires only at 100%, and drains the charge back down if released early.
## HTML
```html
<div class="gx-19">
  <div class="gx-19__card">
    <p class="gx-19__kicker">Danger zone</p>
    <h3 class="gx-19__title">Purge the edge cache</h3>
    <p class="gx-19__copy">This clears every cached asset across all <code>142</code> edge nodes. It cannot be undone — hold the button to confirm.</p>
    <button class="gx-19__btn" type="button" id="gx-19-btn">
      <span class="gx-19__labs">
        <span class="gx-19__lab gx-19__lab--idle">Hold to purge cache</span>
        <span class="gx-19__lab gx-19__lab--done" aria-hidden="true">✓ Cache purged</span>
      </span>
    </button>
    <p class="gx-19__status" id="gx-19-status" aria-live="polite">Hold 1.2 s to confirm</p>
  </div>
</div>
```
## CSS
```css
.gx-19,
.gx-19 *,
.gx-19 *::before,
.gx-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gx-19 ::selection {
  background: #a78bfa;
  color: #0b0e1a;
}

@property --gx-19-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.gx-19 {
  --bg: #0b0e1a;
  --panel: #131a2e;
  --line: rgba(148,163,184,.14);
  --c1: #22d3ee;
  --c2: #a78bfa;
  --c3: #f472b6;
  --ink: #e2e8f0;
  --mut: #8b93ab;
  --hold: 1.2s;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(120% 140% at 82% -20%,#1a2142 0%,var(--bg) 55%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gx-19__card {
  width: min(400px,100%);
  background: linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)) ,var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 28px 28px 24px;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
}

.gx-19__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #fb7185;
  display: flex;
  align-items: center;
  gap: 8px;
}

.gx-19__kicker::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #fb7185;
  box-shadow: 0 0 10px rgba(251,113,133,.8);
}

.gx-19__title {
  margin-top: 12px;
  font-size: 19px;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.01em;
}

.gx-19__copy {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--mut);
}

.gx-19__copy code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 12px;
  background: rgba(148,163,184,.12);
  padding: 1px 6px;
  border-radius: 6px;
  color: #cbd5f5;
}
/* The button. --gx-19-p (0–100) is written every animation frame by JS
   and drives BOTH the conic ring fill and the vivid core opacity. */

.gx-19__btn {
  --gx-19-p: 0;
  position: relative;
  width: 100%;
  margin-top: 22px;
  padding: 16px 24px;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(120deg,#242c4c,#1a2140);
  color: var(--ink);
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .02em;
  cursor: pointer;
  isolation: isolate;
  touch-action: none;
  -webkit-user-select: none;
  user-select: none;
  box-shadow: 0 0 calc(var(--gx-19-p)*.4px) rgba(167,139,250,calc(var(--gx-19-p)*.006));
}
/* Charging ring: conic gradient hollowed into a ring with a two-layer mask */

.gx-19__btn::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: inherit;
  padding: 3px;
  background: conic-gradient(from -90deg,
      var(--c1) 0%,
      var(--c2) calc(var(--gx-19-p)*.5%),
      var(--c3) calc(var(--gx-19-p)*1%),
      rgba(148,163,184,.16) calc(var(--gx-19-p)*1%));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  z-index: -1;
}
/* Vivid core that saturates as the charge rises */

.gx-19__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(120deg,var(--c1),var(--c2) 50%,var(--c3));
  opacity: calc(var(--gx-19-p)/130);
  z-index: -1;
}

.gx-19__btn:focus-visible {
  outline: 2px solid var(--c1);
  outline-offset: 5px;
}
/* Nervous jitter as the charge nears completion */

@keyframes gx-19-jitter {
  0%,
    100% {
    transform: translateX(0);
  }

  25% {
    transform: translateX(-1.5px);
  }

  75% {
    transform: translateX(1.5px);
  }
}

.gx-19__btn.is-arming {
  animation: gx-19-jitter .12s linear infinite;
}
/* Stacked labels crossfade on completion */

.gx-19__labs {
  position: relative;
  display: block;
  pointer-events: none;
}

.gx-19__lab {
  display: block;
  transition: opacity .3s ease,transform .3s ease;
}

.gx-19__lab--done {
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: translateY(6px);
  color: #0b0e1a;
  font-weight: 700;
}

.gx-19__btn.is-done {
  background: linear-gradient(120deg,var(--c1),var(--c2) 50%,var(--c3));
}

.gx-19__btn.is-done .gx-19__lab--idle {
  opacity: 0;
  transform: translateY(-6px);
}

.gx-19__btn.is-done .gx-19__lab--done {
  opacity: 1;
  transform: translateY(0);
}

.gx-19__status {
  margin-top: 14px;
  text-align: center;
  font-size: 12px;
  letter-spacing: .04em;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
  min-height: 1.2em;
}

@media (prefers-reduced-motion: reduce) {
  .gx-19__btn.is-arming {
    animation: none;
  }

  .gx-19__lab {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('gx-19-btn');
  if(!btn)return;
  var status=document.getElementById('gx-19-status');
  var HOLD=1200;      /* ms to fully charge */
  var DRAIN=2.4;      /* drain speed multiplier when released */
  var p=0,raf=null,last=0,holding=false,done=false;
  function set(v){
    p=Math.max(0,Math.min(100,v));
    btn.style.setProperty('--gx-19-p',p.toFixed(2));
  }
  function frame(t){
    if(!last)last=t;
    var dt=t-last;last=t;
    if(holding){
      set(p+dt/HOLD*100);
      btn.classList.toggle('is-arming',p>78);
      if(p>=100){finish();return}
    }else{
      set(p-dt/HOLD*100*DRAIN);
      btn.classList.remove('is-arming');
      if(p<=0){stopLoop();status.textContent='Hold 1.2 s to confirm';return}
    }
    raf=requestAnimationFrame(frame);
  }
  function startLoop(){if(!raf){last=0;raf=requestAnimationFrame(frame)}}
  function stopLoop(){cancelAnimationFrame(raf);raf=null;last=0}
  function start(){
    if(done)return;
    holding=true;
    status.textContent='Charging\u2026 keep holding';
    startLoop();
  }
  function release(){
    if(done||!holding)return;
    holding=false;
    if(p>0)status.textContent='Released \u2014 charge draining';
    startLoop();
  }
  function finish(){
    done=true;holding=false;stopLoop();set(100);
    btn.classList.remove('is-arming');
    btn.classList.add('is-done');
    status.textContent='Cache purged across 142 nodes.';
    setTimeout(function(){
      done=false;
      btn.classList.remove('is-done');
      set(0);
      status.textContent='Hold 1.2 s to confirm';
    },2600);
  }
  btn.addEventListener('pointerdown',function(e){
    btn.setPointerCapture(e.pointerId);
    start();
  });
  btn.addEventListener('pointerup',release);
  btn.addEventListener('pointercancel',release);
  btn.addEventListener('keydown',function(e){
    if((e.key===' '||e.key==='Enter')&&!e.repeat){e.preventDefault();start()}
  });
  btn.addEventListener('keyup',function(e){
    if(e.key===' '||e.key==='Enter')release();
  });
})();
```
