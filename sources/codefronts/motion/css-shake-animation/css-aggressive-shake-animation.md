---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-aggressive-shake-animation/"
title: "CSS Aggressive Shake Animation"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Controlled violence: a hazard console whose panel shakes at full amplitude (±12px, ±3°, steps(2), high frequency) behind an arm/disarm switch — because…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aggressive Shake Animation
Source: https://codefronts.com/motion/css-shake-animation/css-aggressive-shake-animation/

Controlled violence: a hazard console whose panel shakes at full amplitude (±12px, ±3°, steps(2), high frequency) behind an arm/disarm switch — because aggressive motion must always be startable and stoppable — and a containment-breach alert that escalates through three intensity stages the longer it goes unacknowledged.
## HTML
```html
<div class="shk-25-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-25a" aria-label="Hazard console with armable aggressive shake">
  <div class="shk-25a__console">
    <div class="shk-25a__framewrap"><div class="shk-25a__panel"><span class="shk-25a__glyph" aria-hidden="true">⚠</span><p class="shk-25a__code">REACTOR-04</p></div></div>
    <label class="shk-25a__arm"><input class="shk-25a__switch" type="checkbox"><span class="shk-25a__track" aria-hidden="true"><span class="shk-25a__thumb"></span></span><span class="shk-25a__armtxt">Arm the alarm</span></label>
    <p class="shk-25a__note">±12px · ±2.5deg · steps(2) @ .12s — and a kill switch, always</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<section class="shk-25b" aria-label="Alert that escalates its shake until acknowledged">
  <div class="shk-25b__stack">
    <div class="shk-25b__alert" id="shk-25b-alert" data-stage="0" role="alert">
      <p class="shk-25b__head" id="shk-25b-head">SYSTEM NOMINAL</p>
      <p class="shk-25b__sub" id="shk-25b-sub">Trigger a breach to watch the escalation ladder.</p>
    </div>
    <div class="shk-25b__row">
      <button class="shk-25b__go" id="shk-25b-go" type="button">Trigger breach</button>
      <button class="shk-25b__ack" id="shk-25b-ack" type="button" disabled>Acknowledge</button>
    </div>
    <p class="shk-25b__meter" id="shk-25b-meter" aria-hidden="true">stage 0 · idle</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-25-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-25-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-25a,
.shk-25a *,
.shk-25a *::before,
.shk-25a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-25a {
  --haz: oklch(0.72 0.19 55);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #111013;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-25a__console {
  display: grid;
  justify-items: center;
  gap: 24px;
  padding: 40px 44px;
  border-radius: 20px;
  background: #1a181d;
  border: 1px solid rgba(220,200,180,.14);
}

.shk-25a__framewrap {
  padding: 26px;
  border-radius: 14px;
  background: repeating-linear-gradient(45deg,#26232a 0 14px,#1a181d 14px 28px);
}

.shk-25a__panel {
  display: grid;
  place-items: center;
  gap: 8px;
  width: 190px;
  height: 130px;
  border-radius: 10px;
  background: linear-gradient(180deg,#27242c,#1e1b22);
  border: 2px solid rgba(220,200,180,.2);
  color: rgba(240,230,220,.8);
}

.shk-25a__glyph {
  font-size: 40px;
  color: var(--haz);
  filter: drop-shadow(0 0 14px oklch(0.72 0.19 55 / .5));
}

.shk-25a__code {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 12px;
  letter-spacing: .22em;
}

.shk-25a__console:has(.shk-25a__switch:checked) .shk-25a__panel {
  border-color: var(--haz);
  animation: shk-25a-rage .12s steps(2,jump-none) infinite,shk-25a-pulse 1.6s ease-in-out infinite;
}

.shk-25a__arm {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  user-select: none;
}

.shk-25a__switch {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.shk-25a__track {
  width: 52px;
  height: 29px;
  border-radius: 999px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(220,200,180,.25);
  display: flex;
  align-items: center;
  padding: 3px;
  transition: background .2s;
}

.shk-25a__thumb {
  width: 21px;
  height: 21px;
  border-radius: 50%;
  background: #d8cec4;
  transition: translate .2s,background .2s;
}

.shk-25a__switch:checked+.shk-25a__track {
  background: oklch(0.72 0.19 55 / .35);
}

.shk-25a__switch:checked+.shk-25a__track .shk-25a__thumb {
  translate: 23px 0;
  background: var(--haz);
}

.shk-25a__switch:focus-visible+.shk-25a__track {
  outline: 2px solid var(--haz);
  outline-offset: 3px;
}

.shk-25a__armtxt {
  font-size: 14.5px;
  font-weight: 700;
  color: #efe8e0;
}

.shk-25a__note {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 10.5px;
  letter-spacing: .06em;
  color: rgba(240,230,220,.4);
}

@keyframes shk-25a-rage {
  0% {
    translate: -12px 4px;
    rotate: -2.5deg;
  }

  25% {
    translate: 10px -6px;
    rotate: 2deg;
  }

  50% {
    translate: -11px -3px;
    rotate: -1.5deg;
  }

  75% {
    translate: 12px 5px;
    rotate: 2.5deg;
  }

  100% {
    translate: -10px 2px;
    rotate: -2deg;
  }
}

@keyframes shk-25a-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 0 oklch(0.72 0.19 55 / 0);
  }

  50% {
    box-shadow: 0 0 34px 2px oklch(0.72 0.19 55 / .35);
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-25a__console:has(.shk-25a__switch:checked) .shk-25a__panel {
    animation: shk-25a-pulse 1.6s ease-in-out infinite;
  }
}

.shk-25b,
.shk-25b *,
.shk-25b *::before,
.shk-25b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-25b {
  --red: oklch(0.62 0.23 27);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 100% at 50% 100%,#190d0d,#0d0a0a 60%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-25b__stack {
  display: grid;
  gap: 18px;
  justify-items: center;
}

.shk-25b__alert {
  width: min(400px,86vw);
  padding: 26px 30px;
  text-align: center;
  border-radius: 14px;
  background: #161114;
  border: 2px solid rgba(230,210,210,.18);
  transition: border-color .3s,background .3s;
}

.shk-25b__alert[data-stage="1"] {
  border-color: oklch(0.72 0.16 65);
  animation: shk-25b-rage .14s steps(2,jump-none) infinite;
}

.shk-25b__alert[data-stage="2"] {
  border-color: var(--red);
  animation: shk-25b-rage .1s steps(2,jump-none) infinite;
}

.shk-25b__alert[data-stage="3"] {
  border-color: var(--red);
  background: oklch(0.62 0.23 27 / .12);
  animation: shk-25b-rage .07s steps(2,jump-none) infinite;
}

.shk-25b__head {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: .14em;
  color: #efe6e6;
}

.shk-25b__alert[data-stage="2"] .shk-25b__head,
.shk-25b__alert[data-stage="3"] .shk-25b__head {
  color: oklch(0.8 0.15 27);
}

.shk-25b__sub {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(235,222,222,.55);
}

.shk-25b__row {
  display: flex;
  gap: 10px;
}

.shk-25b__go,
.shk-25b__ack {
  padding: 12px 22px;
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  border-radius: 11px;
  cursor: pointer;
  transition: filter .2s,opacity .2s,scale .12s;
}

.shk-25b__go {
  border: 0;
  color: #0d0a0a;
  background: oklch(0.72 0.16 65);
}

.shk-25b__ack {
  border: 1.5px solid rgba(230,210,210,.3);
  color: #efe6e6;
  background: transparent;
}

.shk-25b__go:hover,
.shk-25b__ack:not(:disabled):hover {
  filter: brightness(1.12);
}

.shk-25b__go:active,
.shk-25b__ack:not(:disabled):active {
  scale: .96;
}

.shk-25b__ack:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.shk-25b__meter {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  color: rgba(235,222,222,.4);
}

@keyframes shk-25b-rage {
  0% {
    translate: -9px 3px;
    rotate: -1.6deg;
  }

  25% {
    translate: 8px -4px;
    rotate: 1.3deg;
  }

  50% {
    translate: -9px -2px;
    rotate: -1deg;
  }

  75% {
    translate: 9px 4px;
    rotate: 1.6deg;
  }

  100% {
    translate: -8px 2px;
    rotate: -1.3deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-25b__alert[data-stage="1"],
    .shk-25b__alert[data-stage="2"],
    .shk-25b__alert[data-stage="3"] {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a checkbox + :has() arms and disarms the full-violence shake. Irregular offsets (never symmetric) make it read as “breaking loose” rather than “vibrating”. Reduced-motion keeps only the 1.2Hz glow pulse. */

(function(){
  var alert=document.getElementById('shk-25b-alert'); if(!alert) return;
  var go=document.getElementById('shk-25b-go'),ack=document.getElementById('shk-25b-ack'),
      head=document.getElementById('shk-25b-head'),sub=document.getElementById('shk-25b-sub'),
      meter=document.getElementById('shk-25b-meter'),timer=null;
  var stages=[null,
    ['CONTAINMENT WARNING','Same keyframes, .14s period.'],
    ['CONTAINMENT CRITICAL','Same keyframes, .1s — only duration changed.'],
    ['BREACH IMMINENT','.07s ≈ one step every 2 frames at 60fps.']];
  function setStage(n){
    alert.dataset.stage=String(n);
    meter.textContent='stage '+n+' · '+(n?('period .'+[14,10,7][n-1]+'s'):'idle');
    if(n>0){ head.textContent=stages[n][0]; sub.textContent=stages[n][1]; }
  }
  go.addEventListener('click',function(){
    clearInterval(timer); var n=1; setStage(1); ack.disabled=false;
    timer=setInterval(function(){ if(n<3) setStage(++n); else clearInterval(timer); },2200);
  });
  ack.addEventListener('click',function(){
    clearInterval(timer); setStage(0); ack.disabled=true;
    head.textContent='SYSTEM NOMINAL'; sub.textContent='Acknowledged — motion stops the instant the state flips.';
  });
})();
```
