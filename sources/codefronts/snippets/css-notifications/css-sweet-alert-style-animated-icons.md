---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-sweet-alert-style-animated-icons/"
title: "CSS Sweet Alert Style Animated Icons"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Library-free SweetAlert energy: a success dialog whose circle sweeps shut and checkmark draws on via stroke-dashoffset (with a celebratory ring burst), and…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sweet Alert Style Animated Icons
Source: https://codefronts.com/snippets/css-notifications/css-sweet-alert-style-animated-icons/

Library-free SweetAlert energy: a success dialog whose circle sweeps shut and checkmark draws on via stroke-dashoffset (with a celebratory ring burst), and an icon lab holding all three states — draw-on check, double-stroke cross with a head-shake, pulsing warning — each replayable and each annotated with the exact dash math that drives it.
## HTML
```html
<div class="ntf-24-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-24a" aria-label="Success dialog with self-drawing checkmark">
  <div class="ntf-24a__dialog is-play" id="ntf-24a-dialog" role="status">
    <span class="ntf-24a__icon" aria-hidden="true">
      <svg viewBox="0 0 64 64" fill="none">
        <circle class="ntf-24a__ring" cx="32" cy="32" r="27" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
        <path class="ntf-24a__tick" d="M20 33.5 28.5 42 45 24" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <i class="ntf-24a__burst"></i>
    </span>
    <h2 class="ntf-24a__title">Payment complete</h2>
    <p class="ntf-24a__sub">Receipt #8412 is on its way to your inbox.</p>
    <div class="ntf-24a__row"><button class="ntf-24a__ok" type="button">Done</button><button class="ntf-24a__replay" id="ntf-24a-replay" type="button">Replay</button></div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-24b" aria-label="Success error and warning animated icon set">
  <div class="ntf-24b__lab" id="ntf-24b-lab">
    <div class="ntf-24b__cells">
      <button class="ntf-24b__cell is-play" data-replay type="button" style="--c:oklch(0.72 0.15 155)" aria-label="Replay success icon">
        <svg viewBox="0 0 56 56" fill="none" aria-hidden="true"><circle class="ntf-24b__c" cx="28" cy="28" r="23" stroke="currentColor" stroke-width="3.5"/><path class="ntf-24b__s ntf-24b__s--tick" d="M18 29 25 36 39 21" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <code>dashoffset → 0</code>
      </button>
      <button class="ntf-24b__cell ntf-24b__cell--x is-play" data-replay type="button" style="--c:oklch(0.7 0.18 22)" aria-label="Replay error icon">
        <svg viewBox="0 0 56 56" fill="none" aria-hidden="true"><circle class="ntf-24b__c" cx="28" cy="28" r="23" stroke="currentColor" stroke-width="3.5"/><path class="ntf-24b__s ntf-24b__s--x1" d="M20 20 36 36" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><path class="ntf-24b__s ntf-24b__s--x2" d="M36 20 20 36" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>
        <code>two strokes + head-shake</code>
      </button>
      <button class="ntf-24b__cell is-play" data-replay type="button" style="--c:oklch(0.8 0.14 85)" aria-label="Replay warning icon">
        <svg viewBox="0 0 56 56" fill="none" aria-hidden="true"><circle class="ntf-24b__c ntf-24b__c--pulse" cx="28" cy="28" r="23" stroke="currentColor" stroke-width="3.5"/><path class="ntf-24b__s ntf-24b__s--bang" d="M28 16v16" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><circle class="ntf-24b__dotmark" cx="28" cy="40" r="2.6" fill="currentColor"/></svg>
        <code>draw + pulse loop</code>
      </button>
    </div>
    <p class="ntf-24b__cap">click any icon to replay it — dasharray equals each path's getTotalLength(), rounded up</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-24-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-24-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-24a,
.ntf-24a *,
.ntf-24a *::before,
.ntf-24a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-24a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#131a22,#0a0e13);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-24a__dialog {
  width: min(360px,100%);
  padding: 36px 30px 26px;
  border-radius: 22px;
  background: #f8fafc;
  box-shadow: 0 40px 90px -35px rgba(0,0,0,.9);
  text-align: center;
}

.ntf-24a__icon {
  position: relative;
  display: inline-grid;
  place-items: center;
  width: 88px;
  height: 88px;
  color: oklch(0.62 0.15 155);
}

.ntf-24a__icon svg {
  width: 88px;
  height: 88px;
  rotate: -90deg;
}

.ntf-24a__ring {
  stroke-dasharray: 170;
  stroke-dashoffset: 170;
}

.is-play .ntf-24a__ring {
  animation: ntf-24a-draw .5s cubic-bezier(.65,0,.45,1) .1s forwards;
}

.ntf-24a__tick {
  stroke-dasharray: 36;
  stroke-dashoffset: 36;
  rotate: 90deg;
  transform-origin: center;
}

.is-play .ntf-24a__tick {
  animation: ntf-24a-draw .45s cubic-bezier(.65,0,.45,1) .55s forwards;
}

@keyframes ntf-24a-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ntf-24a__burst {
  position: absolute;
  inset: 6px;
  border-radius: 50%;
  border: 3px solid oklch(0.62 0.15 155 / .5);
  opacity: 0;
  pointer-events: none;
}

.is-play .ntf-24a__burst {
  animation: ntf-24a-burst .55s ease-out .9s;
}

@keyframes ntf-24a-burst {
  0% {
    opacity: .9;
    scale: .8;
  }

  100% {
    opacity: 0;
    scale: 1.45;
  }
}

.ntf-24a__title {
  margin-top: 14px;
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #151a21;
  opacity: 0;
  translate: 0 8px;
}

.is-play .ntf-24a__title {
  animation: ntf-24a-up .4s ease .8s forwards;
}

.ntf-24a__sub {
  margin-top: 6px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(21,26,33,.55);
  opacity: 0;
  translate: 0 8px;
}

.is-play .ntf-24a__sub {
  animation: ntf-24a-up .4s ease .92s forwards;
}

@keyframes ntf-24a-up {
  to {
    opacity: 1;
    translate: 0 0;
  }
}

.ntf-24a__row {
  margin-top: 22px;
  display: flex;
  gap: 10px;
  justify-content: center;
}

.ntf-24a__ok {
  padding: 12px 30px;
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  color: #f8fafc;
  background: #151a21;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  transition: background .2s,scale .12s;
}

.ntf-24a__ok:hover {
  background: #2a3140;
}

.ntf-24a__ok:active {
  scale: .96;
}

.ntf-24a__replay {
  padding: 12px 18px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #151a21;
  background: transparent;
  border: 1.5px solid rgba(21,26,33,.2);
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-24a__replay:hover {
  background: rgba(21,26,33,.06);
}

@media (prefers-reduced-motion: reduce) {
  .is-play .ntf-24a__ring,
    .is-play .ntf-24a__tick {
    animation-duration: .01s;
    animation-delay: 0s;
  }

  .is-play .ntf-24a__burst {
    animation: none;
  }

  .is-play .ntf-24a__title,
    .is-play .ntf-24a__sub {
    animation-duration: .01s;
    animation-delay: 0s;
  }
}

.ntf-24b,
.ntf-24b *,
.ntf-24b *::before,
.ntf-24b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-24b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101216;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-24b__lab {
  display: grid;
  gap: 20px;
  justify-items: center;
}

.ntf-24b__cells {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.ntf-24b__cell {
  display: grid;
  gap: 12px;
  justify-items: center;
  padding: 24px 22px 16px;
  border-radius: 18px;
  background: rgba(255,255,255,.045);
  border: 1px solid color-mix(in oklch,var(--c),transparent 65%);
  color: var(--c);
  cursor: pointer;
  transition: background .2s,translate .2s;
}

.ntf-24b__cell:hover {
  background: rgba(255,255,255,.08);
  translate: 0 -2px;
}

.ntf-24b__cell:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 3px;
}

.ntf-24b__cell svg {
  width: 66px;
  height: 66px;
}

.ntf-24b__cell code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 9.5px;
  color: color-mix(in oklch,var(--c),transparent 35%);
}

.ntf-24b__c {
  stroke-dasharray: 145;
  stroke-dashoffset: 145;
  rotate: -90deg;
  transform-origin: center;
}

.is-play .ntf-24b__c {
  animation: ntf-24b-draw .5s cubic-bezier(.65,0,.45,1) forwards;
}

.ntf-24b__s {
  stroke-dasharray: 32;
  stroke-dashoffset: 32;
}

.is-play .ntf-24b__s--tick {
  animation: ntf-24b-draw .4s cubic-bezier(.65,0,.45,1) .45s forwards;
}

.is-play .ntf-24b__s--x1 {
  animation: ntf-24b-draw .3s cubic-bezier(.65,0,.45,1) .45s forwards;
}

.is-play .ntf-24b__s--x2 {
  animation: ntf-24b-draw .3s cubic-bezier(.65,0,.45,1) .57s forwards;
}

.is-play .ntf-24b__s--bang {
  animation: ntf-24b-draw .35s cubic-bezier(.65,0,.45,1) .45s forwards;
}

@keyframes ntf-24b-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ntf-24b__cell--x.is-play svg {
  animation: ntf-24b-no .5s cubic-bezier(.36,.07,.19,.97) .85s;
}

@keyframes ntf-24b-no {
  20% {
    translate: -6px 0;
  }

  40% {
    translate: 5px 0;
  }

  60% {
    translate: -3px 0;
  }

  80% {
    translate: 1px 0;
  }
}

.ntf-24b__c--pulse {
  transform-origin: center;
}

.is-play .ntf-24b__c--pulse {
  animation: ntf-24b-draw .5s cubic-bezier(.65,0,.45,1) forwards,ntf-24b-pulse 2.4s ease-in-out 1.2s infinite;
}

@keyframes ntf-24b-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .45;
  }
}

.ntf-24b__dotmark {
  opacity: 0;
}

.is-play .ntf-24b__dotmark {
  animation: ntf-24b-dot .25s ease .8s forwards;
}

@keyframes ntf-24b-dot {
  to {
    opacity: 1;
  }
}

.ntf-24b__cap {
  font-size: 12px;
  color: rgba(216,225,240,.4);
  text-align: center;
  max-inline-size: 46ch;
  line-height: 1.6;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .is-play .ntf-24b__c,
    .is-play .ntf-24b__s {
    animation-duration: .01s;
    animation-delay: 0s;
  }

  .ntf-24b__cell--x.is-play svg {
    animation: none;
  }

  .is-play .ntf-24b__c--pulse {
    animation: ntf-24b-draw .01s forwards;
  }

  .is-play .ntf-24b__dotmark {
    animation-duration: .01s;
    animation-delay: 0s;
  }
}
```

## JavaScript
```js
(function(){
  var dialog=document.getElementById('ntf-24a-dialog'); if(!dialog) return;
  document.getElementById('ntf-24a-replay').addEventListener('click',function(){
    dialog.classList.remove('is-play');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ dialog.classList.add('is-play'); }); });
  });
})();

(function(){
  var lab=document.getElementById('ntf-24b-lab'); if(!lab) return;
  lab.querySelectorAll('[data-replay]').forEach(function(cell){
    cell.addEventListener('click',function(){
      cell.classList.remove('is-play');
      requestAnimationFrame(function(){ requestAnimationFrame(function(){ cell.classList.add('is-play'); }); });
    });
  });
})();
```
