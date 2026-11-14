---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/floating-bottom-alert-bar-css/"
title: "Floating Bottom Alert Bar CSS"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two floating-bar temperaments: a cookie-consent bar that rises on an @starting-style transition, floats on a soft double shadow, and handles…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Bottom Alert Bar CSS
Source: https://codefronts.com/snippets/css-notifications/floating-bottom-alert-bar-css/

Two floating-bar temperaments: a cookie-consent bar that rises on an @starting-style transition, floats on a soft double shadow, and handles Accept/Preferences with a collapse exit — and a slim pill promo bar that shows the small-screen discipline: max-inline-size, safe-area-inset-bottom padding, and a snooze control that re-docks it as a corner chip instead of killing it.
## HTML
```html
<div class="ntf-17-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-17a" aria-label="Floating cookie consent bar">
  <div class="ntf-17a__page">
    <h2 class="ntf-17a__ghost">Your product UI</h2>
    <p class="ntf-17a__ghostsub">the bar floats over it, capped at 720px, lifted 16px off the bottom</p>
    <button class="ntf-17a__again" id="ntf-17a-again" type="button" hidden>Show the bar again</button>
  </div>
  <div class="ntf-17a__bar" id="ntf-17a-bar" role="region" aria-label="Cookie consent">
    <span class="ntf-17a__crumb" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01M16 15.5v.01M12 12v.01M11 17v.01M7 14v.01"/></svg></span>
    <p class="ntf-17a__tx"><b>We use cookies</b> for sign-in and anonymous usage stats — never for ads. <a href="#" onclick="return false">Cookie policy</a></p>
    <div class="ntf-17a__acts">
      <button class="ntf-17a__ghostbtn" data-ntf-17a="rejected" type="button">Reject non-essential</button>
      <button class="ntf-17a__solid" data-ntf-17a="accepted" type="button">Accept all</button>
    </div>
  </div>
  <p class="ntf-17a__verdict" id="ntf-17a-verdict" role="status" aria-live="polite"></p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..800&display=swap" rel="stylesheet">
<section class="ntf-17b" aria-label="Floating promo pill that snoozes into a corner chip">
  <div class="ntf-17b__page">
    <h2 class="ntf-17b__ghost">Storefront</h2>
    <p class="ntf-17b__ghostsub">“Later” doesn't kill the promo — it morphs the same element into a corner chip</p>
  </div>
  <div class="ntf-17b__pill" id="ntf-17b-pill" role="region" aria-label="Free shipping offer">
    <span class="ntf-17b__spark" aria-hidden="true">&#10022;</span>
    <p class="ntf-17b__tx"><b>Free shipping</b> on orders over $40 — ends Sunday</p>
    <button class="ntf-17b__go" type="button">Shop now</button>
    <button class="ntf-17b__later" id="ntf-17b-later" type="button" aria-label="Snooze offer to corner">Later</button>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-17-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.ntf-17-group > section {
  width: 100%;
}

.ntf-17a,
.ntf-17a *,
.ntf-17a *::before,
.ntf-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-17a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(130% 110% at 50% 0%,#181d2b,#0c0f16);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-17a__page {
  text-align: center;
  padding: 24px;
}

.ntf-17a__ghost {
  font-size: clamp(26px,4vw,38px);
  font-weight: 600;
  letter-spacing: -.02em;
  color: rgba(226,234,250,.25);
}

.ntf-17a__ghostsub {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(226,234,250,.18);
}

.ntf-17a__again {
  margin-top: 18px;
  padding: 10px 18px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #e2eafa;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(165,190,230,.25);
  border-radius: 10px;
  cursor: pointer;
}

.ntf-17a__bar {
  position: absolute;
  inset-inline: 16px;
  bottom: calc(16px + env(safe-area-inset-bottom,0px));
  margin-inline: auto;
  max-inline-size: 720px;
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  padding: 16px 18px;
  border-radius: 18px;
  background: #f8fafd;
  box-shadow: 0 2px 6px rgba(8,10,16,.35),0 30px 60px -20px rgba(8,10,16,.7);
  transition: translate .5s cubic-bezier(.22,1.2,.36,1),opacity .35s ease,display .5s allow-discrete;
}

@starting-style {
  .ntf-17a__bar {
    translate: 0 24px;
    opacity: 0;
  }
}

.ntf-17a__bar.is-gone {
  translate: 0 24px;
  opacity: 0;
  display: none;
}

.ntf-17a__crumb {
  flex: none;
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  color: #f8fafd;
  background: #20242f;
}

.ntf-17a__crumb svg {
  width: 20px;
  height: 20px;
}

.ntf-17a__tx {
  flex: 1 1 260px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(29,33,43,.8);
}

.ntf-17a__tx b {
  color: #171a22;
  font-weight: 700;
}

.ntf-17a__tx a {
  color: oklch(0.5 0.15 260);
  font-weight: 600;
}

.ntf-17a__tx a:hover {
  color: oklch(0.42 0.15 260);
}

.ntf-17a__acts {
  display: flex;
  gap: 9px;
  margin-left: auto;
}

.ntf-17a__ghostbtn,
.ntf-17a__solid {
  padding: 11px 16px;
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  border-radius: 11px;
  cursor: pointer;
  transition: scale .12s,background .2s;
}

.ntf-17a__ghostbtn {
  color: #20242f;
  background: transparent;
  border: 1.5px solid rgba(29,33,43,.25);
}

.ntf-17a__ghostbtn:hover {
  background: rgba(29,33,43,.06);
}

.ntf-17a__solid {
  color: #f8fafd;
  background: #20242f;
  border: 1.5px solid #20242f;
}

.ntf-17a__solid:hover {
  background: #333947;
}

.ntf-17a__ghostbtn:active,
.ntf-17a__solid:active {
  scale: .96;
}

.ntf-17a__verdict {
  position: absolute;
  bottom: 18px;
  inset-inline: 0;
  text-align: center;
  font-size: 12.5px;
  color: rgba(226,234,250,.55);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-17a__bar {
    transition-duration: .01s;
  }

  @starting-style {
    .ntf-17a__bar {
      translate: 0 0;
    }
  }
}

.ntf-17b,
.ntf-17b *,
.ntf-17b *::before,
.ntf-17b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-17b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,#f7f2e8,#eee5d1);
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.ntf-17b__page {
  text-align: center;
  padding: 24px;
}

.ntf-17b__ghost {
  font-size: clamp(28px,4.5vw,40px);
  font-weight: 700;
  letter-spacing: -.02em;
  color: rgba(37,32,24,.22);
}

.ntf-17b__ghostsub {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(37,32,24,.35);
}

.ntf-17b__pill {
  position: absolute;
  left: 50%;
  bottom: calc(18px + env(safe-area-inset-bottom,0px));
  translate: -50% 0;
  display: flex;
  align-items: center;
  gap: 12px;
  max-inline-size: min(560px,calc(100% - 32px));
  padding: 10px 10px 10px 18px;
  border-radius: 999px;
  background: #252018;
  color: #f7f2e8;
  box-shadow: 0 2px 6px rgba(37,32,24,.3),0 26px 50px -18px rgba(37,32,24,.55);
  transition: left .55s cubic-bezier(.4,0,.2,1),translate .55s cubic-bezier(.4,0,.2,1),padding .45s,gap .45s,bottom .45s;
  white-space: nowrap;
}

@starting-style {
  .ntf-17b__pill {
    translate: -50% 22px;
    opacity: 0;
  }
}

.ntf-17b__spark {
  flex: none;
  font-size: 17px;
  color: oklch(0.85 0.14 85);
  animation: ntf-17b-spin 5s linear infinite;
}

@keyframes ntf-17b-spin {
  to {
    rotate: 360deg;
  }
}

.ntf-17b__tx {
  font-size: 13.5px;
  overflow: hidden;
  max-inline-size: 340px;
  transition: max-inline-size .45s,opacity .3s;
}

.ntf-17b__tx b {
  font-weight: 800;
  color: oklch(0.9 0.11 85);
}

.ntf-17b__go {
  flex: none;
  padding: 10px 16px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 800;
  color: #252018;
  background: oklch(0.85 0.14 85);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  transition: scale .12s,max-inline-size .45s,padding .45s,opacity .3s;
  max-inline-size: 120px;
  overflow: hidden;
}

.ntf-17b__go:active {
  scale: .95;
}

.ntf-17b__later {
  flex: none;
  padding: 10px 12px;
  font: inherit;
  font-size: 12px;
  font-weight: 600;
  color: rgba(247,242,232,.65);
  background: transparent;
  border: 0;
  cursor: pointer;
  transition: color .15s,max-inline-size .45s,padding .45s,opacity .3s;
  max-inline-size: 80px;
  overflow: hidden;
}

.ntf-17b__later:hover {
  color: #f7f2e8;
}

.ntf-17b__pill.is-chip {
  left: calc(100% - 16px);
  translate: -100% 0;
  padding: 10px 14px;
  gap: 0;
}

.ntf-17b__pill.is-chip .ntf-17b__tx,
.ntf-17b__pill.is-chip .ntf-17b__go,
.ntf-17b__pill.is-chip .ntf-17b__later {
  max-inline-size: 0;
  padding-inline: 0;
  opacity: 0;
  pointer-events: none;
}

.ntf-17b__pill.is-chip .ntf-17b__spark {
  cursor: pointer;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-17b__pill,
    .ntf-17b__tx,
    .ntf-17b__go,
    .ntf-17b__later {
    transition-duration: .01s;
  }

  .ntf-17b__spark {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var bar=document.getElementById('ntf-17a-bar'); if(!bar) return;
  var verdict=document.getElementById('ntf-17a-verdict'),again=document.getElementById('ntf-17a-again');
  bar.querySelectorAll('[data-ntf-17a]').forEach(function(btn){
    btn.addEventListener('click',function(){
      bar.classList.add('is-gone');
      verdict.textContent='Choice recorded: '+btn.getAttribute('data-ntf-17a')+' (persist it in localStorage / a consent cookie).';
      again.hidden=false;
    });
  });
  again.addEventListener('click',function(){
    bar.classList.remove('is-gone'); verdict.textContent=''; again.hidden=true;
  });
})();

(function(){
  var pill=document.getElementById('ntf-17b-pill'); if(!pill) return;
  document.getElementById('ntf-17b-later').addEventListener('click',function(){
    pill.classList.add('is-chip');
    pill.setAttribute('aria-label','Snoozed offer — select to expand');
  });
  pill.addEventListener('click',function(){
    if(pill.classList.contains('is-chip')){
      pill.classList.remove('is-chip');
      pill.setAttribute('aria-label','Free shipping offer');
    }
  });
})();
```
