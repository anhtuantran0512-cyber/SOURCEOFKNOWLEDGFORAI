---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-push-notification-browser-style-popup/"
title: "CSS Push Notification Browser Style Popup"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Both halves of web push, faked faithfully: the permission flow done RIGHT — a soft in-page pre-prompt asks first, and only a yes summons the…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Push Notification Browser Style Popup
Source: https://codefronts.com/snippets/css-notifications/css-push-notification-browser-style-popup/

Both halves of web push, faked faithfully: the permission flow done RIGHT — a soft in-page pre-prompt asks first, and only a yes summons the browser-chrome-style permission popup (the pattern that keeps your real permission un-burned), and a desktop OS-style push card — glass surface, app icon, actions that reveal on hover — sliding in from the top-right corner with a grouped second card behind it.
## HTML
```html
<div class="ntf-28-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-28a" aria-label="Two step notification permission flow mockup">
  <div class="ntf-28a__browser">
    <div class="ntf-28a__chrome" aria-hidden="true"><span class="ntf-28a__dots"><i></i><i></i><i></i></span><span class="ntf-28a__url">&#128274; shop.example.com/checkout</span></div>
    <div class="ntf-28a__view">
      <div class="ntf-28a__prompt" id="ntf-28a-prompt" hidden>
        <span class="ntf-28a__bell" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg></span>
        <div class="ntf-28a__ptx"><b>shop.example.com wants to</b><small>Show notifications</small><div class="ntf-28a__prow"><button class="ntf-28a__allow" id="ntf-28a-allow" type="button">Allow</button><button class="ntf-28a__block" id="ntf-28a-block" type="button">Block</button></div></div>
      </div>
      <div class="ntf-28a__pre" id="ntf-28a-pre">
        <h2>Know when your order moves</h2>
        <p>Shipping updates only — 2 or 3 pings per order, nothing else. You can switch off anytime.</p>
        <div class="ntf-28a__prebtns"><button class="ntf-28a__yes" id="ntf-28a-yes" type="button">Notify me</button><button class="ntf-28a__no" id="ntf-28a-no" type="button">Not now</button></div>
        <small class="ntf-28a__note">step 1: YOUR ui — free to dismiss, costs nothing</small>
      </div>
      <p class="ntf-28a__result" id="ntf-28a-result" role="status" aria-live="polite"></p>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-28b" aria-label="Desktop OS style push notification mockup">
  <div class="ntf-28b__desk">
    <div class="ntf-28b__stack" id="ntf-28b-stack">
      <div class="ntf-28b__card ntf-28b__card--peek" aria-hidden="true"></div>
      <div class="ntf-28b__card">
        <span class="ntf-28b__appicon" aria-hidden="true">&#9993;</span>
        <span class="ntf-28b__body"><span class="ntf-28b__toprow"><b>Courier</b><time>now</time></span><b class="ntf-28b__title">Sofia Marques</b><small>Contract v3 attached — can you sign before Friday?</small></span>
        <span class="ntf-28b__acts"><button type="button">Reply</button><button type="button">Archive</button></span>
      </div>
    </div>
    <button class="ntf-28b__replay" id="ntf-28b-replay" type="button">Replay arrival</button>
    <p class="ntf-28b__cap">hover the card — actions reveal; the peeking card behind suggests the group</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-28-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-28-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-28a,
.ntf-28a *,
.ntf-28a *::before,
.ntf-28a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-28a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#171b26,#0c0e15);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-28a__browser {
  width: min(520px,100%);
  border-radius: 16px;
  overflow: hidden;
  background: #f2f3f6;
  box-shadow: 0 34px 75px -35px rgba(0,0,0,.9);
}

.ntf-28a__chrome {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  background: #e0e3ea;
  border-bottom: 1px solid rgba(29,33,43,.1);
}

.ntf-28a__dots {
  display: flex;
  gap: 6px;
}

.ntf-28a__dots i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(29,33,43,.18);
}

.ntf-28a__url {
  flex: 1;
  font-size: 11.5px;
  color: rgba(29,33,43,.6);
  background: #f2f3f6;
  border-radius: 999px;
  padding: 6px 12px;
}

.ntf-28a__view {
  position: relative;
  min-height: 300px;
  padding: 22px;
  display: grid;
  place-items: center;
}

.ntf-28a__prompt {
  position: absolute;
  top: 10px;
  left: 14px;
  z-index: 3;
  display: flex;
  gap: 12px;
  width: min(320px,calc(100% - 28px));
  padding: 14px;
  border-radius: 12px;
  background: #fff;
  border: 1px solid rgba(29,33,43,.13);
  box-shadow: 0 18px 40px -18px rgba(29,33,43,.45);
  animation: ntf-28a-drop .35s cubic-bezier(.22,1.2,.36,1) both;
}

@keyframes ntf-28a-drop {
  from {
    opacity: 0;
    translate: 0 -10px;
  }
}

.ntf-28a__bell {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  color: #fff;
  background: #4a5468;
}

.ntf-28a__bell svg {
  width: 17px;
  height: 17px;
}

.ntf-28a__ptx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-28a__ptx b {
  font-size: 13px;
  font-weight: 600;
  color: #1d212b;
}

.ntf-28a__ptx small {
  font-size: 12px;
  color: rgba(29,33,43,.6);
}

.ntf-28a__prow {
  margin-top: 10px;
  display: flex;
  gap: 8px;
}

.ntf-28a__allow,
.ntf-28a__block {
  padding: 8px 18px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  border-radius: 8px;
  cursor: pointer;
  transition: filter .15s;
}

.ntf-28a__allow {
  color: #fff;
  background: #2f66d0;
  border: 0;
}

.ntf-28a__block {
  color: #1d212b;
  background: #eef0f4;
  border: 0;
}

.ntf-28a__allow:hover,
.ntf-28a__block:hover {
  filter: brightness(1.05);
}

.ntf-28a__pre {
  width: min(360px,100%);
  text-align: center;
  display: grid;
  gap: 10px;
  justify-items: center;
}

.ntf-28a__pre h2 {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #1d212b;
}

.ntf-28a__pre p {
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(29,33,43,.6);
  text-wrap: pretty;
}

.ntf-28a__prebtns {
  display: flex;
  gap: 9px;
  margin-top: 4px;
}

.ntf-28a__yes {
  padding: 12px 24px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: #fff;
  background: #1d212b;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  transition: background .2s,scale .12s;
}

.ntf-28a__yes:hover {
  background: #333a4a;
}

.ntf-28a__yes:active {
  scale: .96;
}

.ntf-28a__no {
  padding: 12px 18px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  color: #1d212b;
  background: transparent;
  border: 1.5px solid rgba(29,33,43,.2);
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-28a__no:hover {
  background: rgba(29,33,43,.05);
}

.ntf-28a__note {
  font-size: 10.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(29,33,43,.4);
}

.ntf-28a__result {
  font-size: 13.5px;
  font-weight: 600;
  color: #1d212b;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-28a__prompt {
    animation-duration: .01s;
  }
}

.ntf-28b,
.ntf-28b *,
.ntf-28b *::before,
.ntf-28b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-28b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,oklch(0.5 0.09 260),oklch(0.32 0.08 285) 60%,oklch(0.25 0.06 300));
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-28b__desk {
  display: grid;
  gap: 22px;
  justify-items: center;
}

.ntf-28b__stack {
  position: relative;
  width: min(360px,calc(100vw - 48px));
}

.ntf-28b__card {
  position: relative;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 13px 14px;
  border-radius: 18px;
  background: rgb(248 250 255 / .72);
  -webkit-backdrop-filter: blur(24px) saturate(1.6);
  backdrop-filter: blur(24px) saturate(1.6);
  border: 1px solid rgb(255 255 255 / .5);
  box-shadow: 0 22px 50px -22px rgb(10 12 30 / .55);
  animation: ntf-28b-in .6s cubic-bezier(.22,1.2,.36,1) both;
}

@supports not (backdrop-filter: blur(1px)) {
  .ntf-28b__card {
    background: rgb(244 247 253 / .96);
  }
}

.ntf-28b__card--peek {
  position: absolute;
  inset: 0;
  translate: 0 8px;
  scale: .94;
  z-index: -1;
  animation-delay: .08s;
  opacity: .7;
}

@keyframes ntf-28b-in {
  from {
    opacity: 0;
    translate: 110% 0;
  }
}

.ntf-28b__card--peek {
  animation-name: ntf-28b-inpeek;
}

@keyframes ntf-28b-inpeek {
  from {
    opacity: 0;
    translate: 110% 8px;
  }

  to {
    opacity: .7;
    translate: 0 8px;
  }
}

.ntf-28b__appicon {
  flex: none;
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  font-size: 17px;
  color: #fff;
  background: linear-gradient(150deg,oklch(0.62 0.16 265),oklch(0.5 0.17 290));
}

.ntf-28b__body {
  display: grid;
  gap: 1px;
  min-width: 0;
  flex: 1;
}

.ntf-28b__toprow {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.ntf-28b__toprow b {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgb(20 24 40 / .55);
}

.ntf-28b__toprow time {
  font-size: 10.5px;
  color: rgb(20 24 40 / .45);
}

.ntf-28b__title {
  font-size: 13.5px;
  font-weight: 700;
  color: #141828;
}

.ntf-28b__body>small {
  font-size: 12.5px;
  line-height: 1.45;
  color: rgb(20 24 40 / .75);
}

.ntf-28b__acts {
  position: absolute;
  inset-inline-end: 12px;
  bottom: 11px;
  display: flex;
  gap: 6px;
  opacity: 0;
  translate: 0 4px;
  transition: opacity .2s,translate .2s;
}

.ntf-28b__card:hover .ntf-28b__acts,
.ntf-28b__card:focus-within .ntf-28b__acts {
  opacity: 1;
  translate: 0 0;
}

.ntf-28b__acts button {
  padding: 6px 12px;
  font: inherit;
  font-size: 11px;
  font-weight: 700;
  color: #141828;
  background: rgb(255 255 255 / .85);
  border: 1px solid rgb(20 24 40 / .12);
  border-radius: 999px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-28b__acts button:hover {
  background: #fff;
}

.ntf-28b__replay {
  padding: 11px 20px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: #fff;
  background: rgb(255 255 255 / .14);
  border: 1px solid rgb(255 255 255 / .3);
  border-radius: 11px;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background .15s,scale .12s;
}

.ntf-28b__replay:hover {
  background: rgb(255 255 255 / .22);
}

.ntf-28b__replay:active {
  scale: .96;
}

.ntf-28b__cap {
  font-size: 12px;
  color: rgb(255 255 255 / .65);
  text-align: center;
  max-inline-size: 40ch;
  line-height: 1.6;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-28b__card {
    animation: ntf-28b-rm .25s ease both;
  }

  @keyframes ntf-28b-rm {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }

  .ntf-28b__card--peek {
    animation: ntf-28b-rmp .25s ease both;
  }

  @keyframes ntf-28b-rmp {
    from {
      opacity: 0;
    }

    to {
      opacity: .7;
      translate: 0 8px;
    }
  }
}
```

## JavaScript
```js
(function(){
  var pre=document.getElementById('ntf-28a-pre'); if(!pre) return;
  var prompt=document.getElementById('ntf-28a-prompt'),result=document.getElementById('ntf-28a-result');
  document.getElementById('ntf-28a-yes').addEventListener('click',function(){
    prompt.hidden=false;   /* only NOW would you call Notification.requestPermission() */
  });
  document.getElementById('ntf-28a-no').addEventListener('click',function(){
    pre.hidden=true; result.textContent='No harm done — the real permission was never requested. Ask again next session.';
  });
  document.getElementById('ntf-28a-allow').addEventListener('click',function(){
    prompt.hidden=true; pre.hidden=true;
    result.textContent='Granted \u2713 — shipping updates enabled.';
  });
  document.getElementById('ntf-28a-block').addEventListener('click',function(){
    prompt.hidden=true; pre.hidden=true;
    result.textContent='Blocked — and in a real browser, you can never ask this user again. This is why step 1 exists.';
  });
})();

(function(){
  var stack=document.getElementById('ntf-28b-stack'); if(!stack) return;
  document.getElementById('ntf-28b-replay').addEventListener('click',function(){
    stack.querySelectorAll('.ntf-28b__card').forEach(function(c){
      c.style.animation='none'; void c.offsetWidth; c.style.animation='';
    });
  });
})();
```
