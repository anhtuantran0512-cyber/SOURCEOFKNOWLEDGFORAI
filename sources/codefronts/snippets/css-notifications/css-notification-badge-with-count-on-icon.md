---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-notification-badge-with-count-on-icon/"
title: "CSS Notification Badge With Count on Icon"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Badge anatomy that survives real numbers: a nav-bar bell whose counter grows from dot to 1-digit circle to 99+ pill without ever going oval (min-inline-size…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Notification Badge With Count on Icon
Source: https://codefronts.com/snippets/css-notifications/css-notification-badge-with-count-on-icon/

Badge anatomy that survives real numbers: a nav-bar bell whose counter grows from dot to 1-digit circle to 99+ pill without ever going oval (min-inline-size + padding, not width), popping on every change via an animationend re-trigger — plus a zero-JavaScript inbox where CSS counters literally count the :checked rows and :has() hides the badge at zero.
## HTML
```html
<div class="ntf-09-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-09a" aria-label="Bell icon badge that survives one to three digits">
  <div class="ntf-09a__wrap">
    <nav class="ntf-09a__nav" aria-label="Demo toolbar">
      <span class="ntf-09a__brand">codefronts</span>
      <button class="ntf-09a__bell" id="ntf-09a-bell" type="button" aria-label="Notifications, 3 unread">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>
        <span class="ntf-09a__badge" id="ntf-09a-badge" aria-hidden="true">3</span>
      </button>
    </nav>
    <div class="ntf-09a__row">
      <button class="ntf-09a__btn" data-ntf-09a="1" type="button">+1</button>
      <button class="ntf-09a__btn" data-ntf-09a="40" type="button">+40</button>
      <button class="ntf-09a__btn" data-ntf-09a="0" type="button">Mark all read</button>
    </div>
    <p class="ntf-09a__cap">min-inline-size grows the circle into a pill · tabular-nums stops digit wobble · aria-label carries the real count</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-09b" aria-label="Badge counting unread rows with CSS counters, zero JavaScript">
  <div class="ntf-09b__inbox">
    <header class="ntf-09b__head">
      <h2 class="ntf-09b__title">Inbox</h2>
      <span class="ntf-09b__bell" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg><i class="ntf-09b__badge"></i></span>
    </header>
    <label class="ntf-09b__row"><input type="checkbox" checked><span class="ntf-09b__tx"><b>Weekly digest</b><small>12 new snippets this week</small></span><i class="ntf-09b__dot" aria-hidden="true"></i></label>
    <label class="ntf-09b__row"><input type="checkbox" checked><span class="ntf-09b__tx"><b>Comment on “Glass toasts”</b><small>“the saturate() tip is gold”</small></span><i class="ntf-09b__dot" aria-hidden="true"></i></label>
    <label class="ntf-09b__row"><input type="checkbox"><span class="ntf-09b__tx"><b>Deploy note</b><small>v2.9 rolled out to all regions</small></span><i class="ntf-09b__dot" aria-hidden="true"></i></label>
    <p class="ntf-09b__cap">Checked = unread. CSS counters do the math; <b>:has()</b> collapses the badge at zero. No JavaScript anywhere.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-09-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-09-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-09a,
.ntf-09a *,
.ntf-09a *::before,
.ntf-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-09a {
  --nav: #141926;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#171d2c,#0c0f17);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-09a__wrap {
  width: min(420px,100%);
  display: grid;
  gap: 22px;
  justify-items: center;
}

.ntf-09a__nav {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  border-radius: 16px;
  background: var(--nav);
  border: 1px solid rgba(165,190,230,.16);
  box-shadow: 0 22px 48px -26px rgba(0,0,0,.85);
}

.ntf-09a__brand {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #edf2fc;
}

.ntf-09a__bell {
  position: relative;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 12px;
  color: #c9d5ec;
  background: rgba(255,255,255,.06);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-09a__bell:hover {
  background: rgba(255,255,255,.12);
  color: #fff;
}

.ntf-09a__bell:focus-visible {
  outline: 2px solid #c9d5ec;
  outline-offset: 2px;
}

.ntf-09a__bell svg {
  width: 21px;
  height: 21px;
}

.ntf-09a__badge {
  position: absolute;
  top: -5px;
  inset-inline-end: -5px;
  min-inline-size: 19px;
  block-size: 19px;
  display: grid;
  place-items: center;
  padding-inline: 5px;
  border-radius: 999px;
  font-size: 10.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #fff;
  background: oklch(0.63 0.21 25);
  border: 2px solid var(--nav);
  transition: scale .2s;
}

.ntf-09a__badge.is-zero {
  scale: 0;
}

.ntf-09a__badge.is-pop {
  animation: ntf-09a-pop .35s cubic-bezier(.22,1.6,.36,1);
}

@keyframes ntf-09a-pop {
  40% {
    scale: 1.35;
  }
}

.ntf-09a__row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
}

.ntf-09a__btn {
  padding: 10px 18px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #edf2fc;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(165,190,230,.2);
  border-radius: 10px;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-09a__btn:hover {
  background: rgba(255,255,255,.13);
}

.ntf-09a__btn:active {
  scale: .95;
}

.ntf-09a__cap {
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(210,222,245,.45);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-09a__badge.is-pop {
    animation: none;
  }
}

.ntf-09b,
.ntf-09b *,
.ntf-09b *::before,
.ntf-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-09b {
  --ink: #211f1a;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f8f5ee,#efe9db);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-09b__inbox {
  width: min(400px,100%);
  padding: 22px;
  border-radius: 20px;
  background: #fffdf8;
  border: 1px solid rgba(33,31,26,.1);
  box-shadow: 0 26px 60px -32px rgba(33,31,26,.5);
  counter-reset: ntf09b;
}

.ntf-09b__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.ntf-09b__title {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--ink);
}

.ntf-09b__bell {
  position: relative;
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  color: var(--ink);
  background: rgba(33,31,26,.06);
}

.ntf-09b__bell svg {
  width: 20px;
  height: 20px;
}

.ntf-09b__badge {
  position: absolute;
  top: -5px;
  inset-inline-end: -5px;
  min-inline-size: 18px;
  block-size: 18px;
  display: grid;
  place-items: center;
  padding-inline: 5px;
  border-radius: 999px;
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #fff;
  background: oklch(0.63 0.21 25);
  border: 2px solid #fffdf8;
  transition: scale .25s cubic-bezier(.22,1.4,.36,1);
}

.ntf-09b__badge::after {
  content: counter(ntf09b);
}

.ntf-09b:not(:has(.ntf-09b__row input:checked)) .ntf-09b__badge {
  scale: 0;
}

.ntf-09b__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 12px;
  border-radius: 13px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-09b__row:hover {
  background: rgba(33,31,26,.045);
}

.ntf-09b__row input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-09b__row:has(input:checked) {
  counter-increment: ntf09b;
}

.ntf-09b__tx {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-09b__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
  transition: color .2s;
}

.ntf-09b__tx small {
  font-size: 11.5px;
  color: rgba(33,31,26,.5);
}

.ntf-09b__dot {
  margin-left: auto;
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.63 0.21 25);
  transition: scale .2s,opacity .2s;
}

.ntf-09b__row:not(:has(input:checked)) .ntf-09b__dot {
  scale: 0;
  opacity: 0;
}

.ntf-09b__row:not(:has(input:checked)) b {
  color: rgba(33,31,26,.45);
  font-weight: 500;
}

.ntf-09b__row:has(input:focus-visible) {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.ntf-09b__cap {
  margin-top: 12px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(33,31,26,.45);
  text-wrap: pretty;
}

.ntf-09b__cap b {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-09b__badge,
    .ntf-09b__dot {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
(function(){
  var badge=document.getElementById('ntf-09a-badge'); if(!badge) return;
  var bell=document.getElementById('ntf-09a-bell'),count=3;
  badge.addEventListener('animationend',function(){ badge.classList.remove('is-pop'); });
  document.querySelectorAll('[data-ntf-09a]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var d=parseInt(btn.getAttribute('data-ntf-09a'),10);
      count=d===0?0:count+d;
      badge.textContent=count>99?'99+':String(count);   /* clamp the pixels, not the truth */
      badge.classList.toggle('is-zero',count===0);
      badge.classList.remove('is-pop'); if(count>0) badge.classList.add('is-pop');
      bell.setAttribute('aria-label','Notifications, '+count+' unread');
    });
  });
})();

/* No JavaScript — counter-reset on the card, counter-increment on every row:has(:checked), counter() rendered into the badge's ::after, and :has() zeroes the badge when nothing is unread. */
```
