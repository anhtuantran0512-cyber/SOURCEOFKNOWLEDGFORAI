---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/accessible-css-toast-notification-aria-live/"
title: "Accessible CSS Toast Notification Aria Live"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The accessibility contract made visible: a polite-vs-assertive lab where two buttons fire the same toast through role=status and role=alert while an…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible CSS Toast Notification Aria Live
Source: https://codefronts.com/snippets/css-notifications/accessible-css-toast-notification-aria-live/

The accessibility contract made visible: a polite-vs-assertive lab where two buttons fire the same toast through role=status and role=alert while an on-screen announcement log shows exactly what a screen reader would say (and why the region must exist BEFORE the message) — plus an annotated specimen toast with numbered pins tying each WCAG checkpoint to the physical part of the toast that satisfies it.
## HTML
```html
<div class="ntf-25-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<section class="ntf-25a" aria-label="Compare polite and assertive toast announcements">
  <div class="ntf-25a__lab">
    <div class="ntf-25a__controls">
      <button class="ntf-25a__btn" id="ntf-25a-polite" type="button">Save draft <small>role="status" · polite</small></button>
      <button class="ntf-25a__btn ntf-25a__btn--hot" id="ntf-25a-assertive" type="button">Drop connection <small>role="alert" · assertive</small></button>
    </div>
    <div class="ntf-25a__log" aria-hidden="true">
      <p class="ntf-25a__loghead">SCREEN READER QUEUE (simulated)</p>
      <div class="ntf-25a__lines" id="ntf-25a-lines"><p class="ntf-25a__line ntf-25a__line--idle">reading: “…paragraph text under the cursor…”</p></div>
    </div>
    <div class="ntf-25a__region" role="status" aria-live="polite" id="ntf-25a-status"></div>
    <div class="ntf-25a__region" role="alert" id="ntf-25a-alert"></div>
    <div class="ntf-25a__toasts" id="ntf-25a-toasts" aria-hidden="true"></div>
    <p class="ntf-25a__cap">Both live regions exist <b>before</b> any message — injecting text into them is what triggers speech. Polite waits its turn; assertive interrupts the current sentence.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-25b" aria-label="Toast anatomy annotated with accessibility checkpoints">
  <div class="ntf-25b__board">
    <div class="ntf-25b__toast" role="status">
      <span class="ntf-25b__pin" style="--x:-11px;--y:-11px" aria-hidden="true">1</span>
      <span class="ntf-25b__pin" style="--x:calc(100% - 13px);--y:-11px" aria-hidden="true">2</span>
      <span class="ntf-25b__pin" style="--x:38%;--y:calc(100% - 13px)" aria-hidden="true">3</span>
      <span class="ntf-25b__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <span class="ntf-25b__tx"><b>2 photos uploaded</b><small>Album “Coast” · just now</small></span>
      <button class="ntf-25b__undo" type="button">Undo</button>
      <i class="ntf-25b__bar" aria-hidden="true"></i>
    </div>
    <ul class="ntf-25b__key">
      <li><b>1</b><span><code>role="status"</code> on a pre-rendered region — announced politely, no focus stolen</span></li>
      <li><b>2</b><span>text 13.5px at 10.2:1 contrast — passes AA at any zoom level</span></li>
      <li><b>3</b><span>≥ 5s lifetime, and <code>:hover</code>/<code>:focus-within</code> pause the timer — magnification users get time to find it</span></li>
      <li><b>+</b><span><code>prefers-reduced-motion</code> swaps the slide for a fade — same info, no vestibular trigger</span></li>
    </ul>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-25-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-25-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-25a,
.ntf-25a *,
.ntf-25a *::before,
.ntf-25a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-25a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#141a26,#0b0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-25a__lab {
  width: min(520px,100%);
  display: grid;
  gap: 18px;
}

.ntf-25a__controls {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.ntf-25a__btn {
  display: grid;
  gap: 3px;
  padding: 14px 16px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #edf2fc;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(165,190,230,.22);
  border-radius: 13px;
  cursor: pointer;
  text-align: left;
  transition: background .15s,scale .12s;
}

.ntf-25a__btn small {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10px;
  font-weight: 400;
  color: rgba(212,224,246,.5);
}

.ntf-25a__btn:hover {
  background: rgba(255,255,255,.11);
}

.ntf-25a__btn:active {
  scale: .98;
}

.ntf-25a__btn--hot {
  border-color: oklch(0.68 0.21 25 / .5);
}

.ntf-25a__btn--hot small {
  color: oklch(0.75 0.15 25);
}

.ntf-25a__log {
  padding: 16px;
  border-radius: 14px;
  background: #0a0d13;
  border: 1px solid rgba(165,190,230,.14);
}

.ntf-25a__loghead {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 9.5px;
  letter-spacing: .18em;
  color: rgba(212,224,246,.4);
}

.ntf-25a__lines {
  margin-top: 10px;
  display: grid;
  gap: 6px;
  min-height: 66px;
  align-content: start;
}

.ntf-25a__line {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11.5px;
  line-height: 1.5;
  color: #cdd9f0;
  animation: ntf-25a-line .3s ease both;
}

.ntf-25a__line--idle {
  color: rgba(205,217,240,.35);
}

.ntf-25a__line--polite {
  color: oklch(0.8 0.12 200);
}

.ntf-25a__line--alert {
  color: oklch(0.78 0.15 25);
  font-weight: 600;
}

@keyframes ntf-25a-line {
  from {
    opacity: 0;
    translate: 0 4px;
  }
}

.ntf-25a__region {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ntf-25a__toasts {
  position: absolute;
  bottom: 24px;
  inset-inline-end: 24px;
  display: grid;
  gap: 10px;
  width: min(300px,calc(100% - 48px));
}

.ntf-25a__toast {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 13px 15px;
  border-radius: 13px;
  background: #171d2b;
  border: 1px solid rgba(165,190,230,.2);
  box-shadow: 0 20px 44px -22px rgba(0,0,0,.9);
  animation: ntf-25a-in .4s cubic-bezier(.22,1.2,.36,1) both,ntf-25a-out .3s ease-in 4.7s forwards;
}

.ntf-25a__toast i {
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--c,oklch(0.72 0.15 200));
}

.ntf-25a__toast b {
  font-size: 13px;
  font-weight: 600;
  color: #edf2fc;
}

@keyframes ntf-25a-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }
}

@keyframes ntf-25a-out {
  to {
    opacity: 0;
    translate: 0 -8px;
  }
}

.ntf-25a__cap {
  font-size: 12px;
  line-height: 1.65;
  color: rgba(212,224,246,.45);
  text-wrap: pretty;
}

.ntf-25a__cap b {
  color: rgba(237,242,252,.85);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-25a__toast {
    animation: ntf-25a-rmin .2s ease both,ntf-25a-out .3s ease-in 4.7s forwards;
  }

  @keyframes ntf-25a-rmin {
    from {
      opacity: 0;
    }
  }
}

.ntf-25b,
.ntf-25b *,
.ntf-25b *::before,
.ntf-25b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-25b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f5f4f0,#eae7de);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-25b__board {
  width: min(440px,100%);
  display: grid;
  gap: 24px;
}

.ntf-25b__toast {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 15px 16px 18px;
  border-radius: 15px;
  background: #22252d;
  box-shadow: 0 26px 55px -28px rgba(34,37,45,.65);
  animation: ntf-25b-in .5s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-25b__toast:hover .ntf-25b__bar,
.ntf-25b__toast:focus-within .ntf-25b__bar {
  animation-play-state: paused;
}

@keyframes ntf-25b-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }
}

.ntf-25b__pin {
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: 24px;
  height: 24px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: 11.5px;
  font-weight: 800;
  color: #22252d;
  background: oklch(0.85 0.14 85);
  border: 2px solid #f5f4f0;
  z-index: 2;
}

.ntf-25b__ico {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #122016;
  background: oklch(0.8 0.15 160);
}

.ntf-25b__ico svg {
  width: 17px;
  height: 17px;
}

.ntf-25b__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-25b__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #f2f4f9;
}

.ntf-25b__tx small {
  font-size: 11.5px;
  color: rgba(242,244,249,.6);
}

.ntf-25b__undo {
  margin-left: auto;
  flex: none;
  padding: 8px 14px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: #f2f4f9;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 9px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-25b__undo:hover {
  background: rgba(255,255,255,.18);
}

.ntf-25b__undo:focus-visible {
  outline: 2px solid oklch(0.85 0.14 85);
  outline-offset: 2px;
}

.ntf-25b__bar {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 4px;
  border-radius: 0 0 15px 15px;
  background: oklch(0.8 0.15 160);
  transform-origin: left;
  animation: ntf-25b-drain 6s linear infinite;
}

@keyframes ntf-25b-drain {
  to {
    scale: 0 1;
  }
}

.ntf-25b__key {
  list-style: none;
  display: grid;
  gap: 11px;
}

.ntf-25b__key li {
  display: flex;
  gap: 11px;
  align-items: baseline;
}

.ntf-25b__key b {
  flex: none;
  width: 22px;
  height: 22px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 800;
  color: #22252d;
  background: oklch(0.85 0.14 85);
  translate: 0 3px;
}

.ntf-25b__key span {
  font-size: 13px;
  line-height: 1.6;
  color: rgba(34,37,45,.75);
  text-wrap: pretty;
}

.ntf-25b__key code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: rgba(34,37,45,.08);
  padding: 1.5px 6px;
  border-radius: 6px;
  color: #22252d;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-25b__toast {
    animation: ntf-25b-rm .2s ease both;
  }

  @keyframes ntf-25b-rm {
    from {
      opacity: 0;
    }
  }

  .ntf-25b__bar {
    animation-duration: 12s;
  }
}
```

## JavaScript
```js
(function(){
  var lines=document.getElementById('ntf-25a-lines'); if(!lines) return;
  var statusR=document.getElementById('ntf-25a-status'),alertR=document.getElementById('ntf-25a-alert'),
      toasts=document.getElementById('ntf-25a-toasts');
  function toast(msg,color){
    var t=document.createElement('div'); t.className='ntf-25a__toast'; t.style.setProperty('--c',color);
    t.innerHTML='<i></i><b>'+msg+'</b>';
    t.addEventListener('animationend',function(e){ if(e.animationName==='ntf-25a-out') t.remove(); });
    toasts.appendChild(t);
  }
  function logLine(txt,cls){
    var p=document.createElement('p'); p.className='ntf-25a__line '+cls; p.textContent=txt;
    lines.appendChild(p);
    while(lines.children.length>4) lines.firstElementChild.remove();
  }
  document.getElementById('ntf-25a-polite').addEventListener('click',function(){
    statusR.textContent='';
    setTimeout(function(){ statusR.textContent='Draft saved'; },30);   /* inject INTO the waiting region */
    toast('Draft saved','oklch(0.72 0.15 200)');
    logLine('…finishes current sentence… then: “Draft saved”','ntf-25a__line--polite');
  });
  document.getElementById('ntf-25a-assertive').addEventListener('click',function(){
    alertR.textContent='';
    setTimeout(function(){ alertR.textContent='Connection lost. Changes are not being saved.'; },30);
    toast('Connection lost','oklch(0.68 0.21 25)');
    logLine('INTERRUPTS: “Connection lost. Changes are not being saved.”','ntf-25a__line--alert');
  });
})();

/* No JavaScript — a teaching specimen: every numbered pin maps a WCAG checkpoint to the exact pixels that satisfy it. The drain bar loops for demo purposes and pauses on hover/focus-within like a real one. */
```
