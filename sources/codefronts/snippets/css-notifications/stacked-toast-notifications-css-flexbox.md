---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/stacked-toast-notifications-css-flexbox/"
title: "Stacked Toast Notifications CSS Flexbox"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two stacking architectures: a flexbox column where new toasts land nearest the action and departures collapse their row with a grid-template-rows glide (no…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Toast Notifications CSS Flexbox
Source: https://codefronts.com/snippets/css-notifications/stacked-toast-notifications-css-flexbox/

Two stacking architectures: a flexbox column where new toasts land nearest the action and departures collapse their row with a grid-template-rows glide (no snap-reflow), and a layered deck where CSS :nth-last-child fans older toasts behind the newest — hover and the deck expands into a full flex list, exactly the pattern popularized by modern toast libraries.
## HTML
```html
<div class="ntf-04-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-04a" aria-label="Flexbox toast stack with smooth removal">
  <div class="ntf-04a__card">
    <h2 class="ntf-04a__title">Pile them up</h2>
    <p class="ntf-04a__sub">New toasts land at the bottom (column-reverse), each dismisses after 4.5s, and leavers <b>collapse their row</b> so the stack glides instead of snapping.</p>
    <div class="ntf-04a__row">
      <button class="ntf-04a__btn" data-ntf-04a="ok" type="button">+ Success</button>
      <button class="ntf-04a__btn" data-ntf-04a="warn" type="button">+ Warning</button>
      <button class="ntf-04a__btn" data-ntf-04a="info" type="button">+ Info</button>
    </div>
  </div>
  <div class="ntf-04a__region" id="ntf-04a-region" role="status" aria-live="polite"></div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-04b" aria-label="Layered toast deck that expands on hover">
  <div class="ntf-04b__card">
    <h2 class="ntf-04b__title">The deck</h2>
    <p class="ntf-04b__sub">DOM order is the z-order: <b>:nth-last-child(2)</b> is always “one behind the newest”, so CSS fans the pile with zero bookkeeping. Hover the stack to expand it.</p>
    <button class="ntf-04b__btn" id="ntf-04b-btn" type="button">Push notification</button>
  </div>
  <div class="ntf-04b__region" id="ntf-04b-region" role="status" aria-live="polite"></div>
</section>
</div>
```
## CSS
```css
.ntf-04-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-04-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-04a,
.ntf-04a *,
.ntf-04a *::before,
.ntf-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-04a {
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

.ntf-04a__card {
  width: min(430px,100%);
  text-align: center;
}

.ntf-04a__title {
  font-size: 25px;
  font-weight: 600;
  color: #edf2fc;
  letter-spacing: -.01em;
}

.ntf-04a__sub {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(212,224,246,.55);
}

.ntf-04a__sub b {
  color: rgba(237,242,252,.9);
}

.ntf-04a__row {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.ntf-04a__btn {
  padding: 11px 18px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #edf2fc;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(165,190,230,.2);
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-04a__btn:hover {
  background: rgba(255,255,255,.13);
}

.ntf-04a__btn:active {
  scale: .95;
}

.ntf-04a__region {
  position: absolute;
  bottom: 24px;
  inset-inline-end: 24px;
  display: flex;
  flex-direction: column-reverse;
  width: min(320px,calc(100% - 48px));
}

.ntf-04a__cell {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .35s cubic-bezier(.4,0,.2,1),opacity .3s ease;
}

.ntf-04a__cell.is-leaving {
  grid-template-rows: 0fr;
  opacity: 0;
}

.ntf-04a__cell:nth-last-child(n+5) {
  opacity: .35;
}

.ntf-04a__clip {
  overflow: hidden;
  display: grid;
}

.ntf-04a__toast {
  --acc: oklch(0.78 0.15 160);
  display: flex;
  align-items: center;
  gap: 11px;
  margin-top: 10px;
  padding: 13px 15px;
  border-radius: 14px;
  background: rgba(20,26,38,.95);
  border: 1px solid rgba(165,190,230,.18);
  border-inline-start: 3px solid var(--acc);
  box-shadow: 0 18px 40px -20px rgba(0,0,0,.85);
  animation: ntf-04a-in .45s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-04a__toast--warn {
  --acc: oklch(0.8 0.14 85);
}

.ntf-04a__toast--info {
  --acc: oklch(0.74 0.12 250);
}

.ntf-04a__mark {
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--acc);
}

.ntf-04a__toast span:last-of-type {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-04a__toast b {
  font-size: 13px;
  font-weight: 600;
  color: #edf2fc;
}

.ntf-04a__toast small {
  font-size: 11px;
  color: rgba(212,224,246,.5);
}

@keyframes ntf-04a-in {
  from {
    opacity: 0;
    translate: 0 18px;
    scale: .96;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-04a__toast {
    animation: ntf-04a-rm .2s ease both;
  }

  @keyframes ntf-04a-rm {
    from {
      opacity: 0;
    }
  }
}

.ntf-04b,
.ntf-04b *,
.ntf-04b *::before,
.ntf-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-04b {
  --ink: #211e19;
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f2e9,#ebe4d2);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-04b__card {
  width: min(430px,100%);
  text-align: center;
}

.ntf-04b__title {
  font-size: 26px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--ink);
}

.ntf-04b__sub {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(33,30,25,.55);
}

.ntf-04b__sub b {
  color: var(--ink);
}

.ntf-04b__btn {
  margin-top: 20px;
  padding: 13px 26px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #f6f2e9;
  background: var(--ink);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 14px 28px -14px rgba(33,30,25,.55);
  transition: background .2s,scale .12s;
}

.ntf-04b__btn:hover {
  background: #38342c;
}

.ntf-04b__btn:active {
  scale: .96;
}

.ntf-04b__region {
  position: absolute;
  top: 24px;
  inset-inline-end: 24px;
  width: min(310px,calc(100% - 48px));
  display: flex;
  flex-direction: column-reverse;
}

.ntf-04b__toast {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 14px 16px;
  border-radius: 15px;
  background: #fffdf7;
  border: 1px solid rgba(33,30,25,.11);
  box-shadow: 0 16px 36px -18px rgba(33,30,25,.5);
  transition: translate .4s cubic-bezier(.22,1.2,.36,1),scale .4s cubic-bezier(.22,1.2,.36,1),opacity .3s,margin .35s cubic-bezier(.4,0,.2,1);
  animation: ntf-04b-in .5s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-04b__region:not(:hover) .ntf-04b__toast {
  position: relative;
}

.ntf-04b__region:not(:hover) .ntf-04b__toast:not(:last-child) {
  margin-bottom: -58px;
}

.ntf-04b__region:not(:hover) .ntf-04b__toast:nth-last-child(2) {
  scale: .95;
  translate: 0 -12px;
  pointer-events: none;
}

.ntf-04b__region:not(:hover) .ntf-04b__toast:nth-last-child(3) {
  scale: .9;
  translate: 0 -24px;
  pointer-events: none;
}

.ntf-04b__region:not(:hover) .ntf-04b__toast:nth-last-child(n+4) {
  scale: .85;
  translate: 0 -34px;
  opacity: 0;
  pointer-events: none;
}

.ntf-04b__region:hover .ntf-04b__toast:not(:last-child) {
  margin-bottom: 10px;
}

.ntf-04b__ava {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 13px;
  font-weight: 700;
  color: #fffdf7;
  background: var(--c,oklch(0.6 0.12 250));
}

.ntf-04b__toast span:last-child {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-04b__toast b {
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
}

.ntf-04b__toast small {
  font-size: 11px;
  color: rgba(33,30,25,.5);
}

@keyframes ntf-04b-in {
  from {
    opacity: 0;
    translate: 0 -18px;
    scale: .94;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-04b__toast {
    animation: ntf-04b-rm .2s ease both;
    transition-duration: .01s;
  }

  @keyframes ntf-04b-rm {
    from {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
(function(){
  var region=document.getElementById('ntf-04a-region'); if(!region) return;
  var COPY={ok:['Changes saved','Synced to workspace'],warn:['Storage 90% full','Oldest exports purge in 7 days'],info:['New comment','Priya replied on “Q3 roadmap”']};
  var n=0;
  document.querySelectorAll('[data-ntf-04a]').forEach(function(btn){
    btn.addEventListener('click',function(){ spawn(btn.getAttribute('data-ntf-04a')); });
  });
  function spawn(kind){
    n++;
    var cell=document.createElement('div'); cell.className='ntf-04a__cell';
    cell.innerHTML='<div class="ntf-04a__clip"><div class="ntf-04a__toast ntf-04a__toast--'+kind+'"><i class="ntf-04a__mark" aria-hidden="true"></i><span><b>'+COPY[kind][0]+' #'+n+'</b><small>'+COPY[kind][1]+'</small></span></div></div>';
    region.appendChild(cell);
    setTimeout(function(){ leave(cell); },4500);
  }
  function leave(cell){
    if(!cell.isConnected||cell.classList.contains('is-leaving')) return;
    cell.classList.add('is-leaving');
    cell.addEventListener('transitionend',function(e){
      if(e.propertyName==='grid-template-rows') cell.remove(); /* collapse finished -> safe to remove */
    });
  }
})();

(function(){
  var btn=document.getElementById('ntf-04b-btn'); if(!btn) return;
  var region=document.getElementById('ntf-04b-region');
  var FEED=[['LC','Lena commented','“love the new spacing”','oklch(0.6 0.12 250)'],['CI','Build passing','main · 2m 41s','oklch(0.62 0.14 160)'],['DR','Design review at 3','starts in 15 min','oklch(0.65 0.14 60)'],['MK','Mark shared a file','pricing-v4.sketch','oklch(0.55 0.1 320)']];
  var i=0;
  btn.addEventListener('click',function(){
    var d=FEED[i++%FEED.length];
    var t=document.createElement('div'); t.className='ntf-04b__toast'; t.style.setProperty('--c',d[3]);
    t.innerHTML='<span class="ntf-04b__ava" aria-hidden="true">'+d[0]+'</span><span><b>'+d[1]+'</b><small>'+d[2]+'</small></span>';
    region.appendChild(t);
    if(region.children.length>6) region.firstElementChild.remove(); /* hard cap the pile */
  });
  btn.click(); btn.click(); btn.click();
})();
```
