---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-toast-progress-bar-countdown/"
title: "CSS Toast Progress Bar Countdown"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Countdown you can see: an undo-toast whose shrinking bottom bar IS the timer (hover pauses it, the bar's animationend dismisses the toast, so bar and…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toast Progress Bar Countdown
Source: https://codefronts.com/snippets/css-notifications/css-toast-progress-bar-countdown/

Countdown you can see: an undo-toast whose shrinking bottom bar IS the timer (hover pauses it, the bar's animationend dismisses the toast, so bar and lifetime can never drift), and a pure-CSS ring countdown where @property animates a conic-gradient and a registered integer counts the seconds down inside the close button.
## HTML
```html
<div class="ntf-03-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-03a" aria-label="Undo toast with shrinking progress bar countdown">
  <div class="ntf-03a__card">
    <h2 class="ntf-03a__title">One clock, zero drift</h2>
    <p class="ntf-03a__sub">The shrinking bar is the only timer — its <b>animationend</b> dismisses the toast. Hover or focus the toast to pause everything.</p>
    <button class="ntf-03a__btn" id="ntf-03a-btn" type="button">Delete recording.wav</button>
    <p class="ntf-03a__status" id="ntf-03a-status" aria-live="polite"></p>
  </div>
  <template id="ntf-03a-tpl">
    <div class="ntf-03a__toast" tabindex="0">
      <span class="ntf-03a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m3 0v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/></svg></span>
      <span class="ntf-03a__body"><b>recording.wav deleted</b><small>Gone when the bar runs out</small></span>
      <button class="ntf-03a__undo" type="button">Undo</button>
      <i class="ntf-03a__bar" aria-hidden="true"></i>
    </div>
  </template>
  <div class="ntf-03a__region" id="ntf-03a-region"></div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&family=JetBrains+Mono:wght@600&display=swap" rel="stylesheet">
<section class="ntf-03b" aria-label="Toast with conic-gradient ring countdown, pure CSS">
  <input class="ntf-03b__fire" type="checkbox" id="ntf-03b-fire">
  <div class="ntf-03b__card">
    <h2 class="ntf-03b__title">The ring <em>is</em> the countdown</h2>
    <p class="ntf-03b__sub">A registered @property sweeps the conic-gradient while a registered integer counts the seconds — all CSS.</p>
    <label class="ntf-03b__btn" for="ntf-03b-fire">Send test email</label>
  </div>
  <aside class="ntf-03b__toast" role="status">
    <span class="ntf-03b__ring" aria-hidden="true"><i class="ntf-03b__num"></i></span>
    <span class="ntf-03b__body"><b>Test email sent</b><small>to [email protected]</small></span>
    <label class="ntf-03b__close" for="ntf-03b-fire" aria-label="Dismiss">&#10005;</label>
  </aside>
</section>
</div>
```
## CSS
```css
.ntf-03-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-03-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-03a,
.ntf-03a *,
.ntf-03a *::before,
.ntf-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-03a {
  --rose: oklch(0.72 0.17 15);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#1b1420,#100b14);
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.ntf-03a__card {
  width: min(440px,100%);
  text-align: center;
}

.ntf-03a__title {
  font-size: 24px;
  font-weight: 600;
  color: #f4edf7;
  letter-spacing: -.01em;
}

.ntf-03a__sub {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(233,219,240,.55);
}

.ntf-03a__sub b {
  color: rgba(244,237,247,.9);
}

.ntf-03a__btn {
  margin-top: 22px;
  padding: 13px 26px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  background: var(--rose);
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  transition: filter .15s,scale .12s;
}

.ntf-03a__btn:hover {
  filter: brightness(1.08);
}

.ntf-03a__btn:active {
  scale: .96;
}

.ntf-03a__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.ntf-03a__status {
  margin-top: 14px;
  font-size: 12.5px;
  min-height: 18px;
  color: rgba(233,219,240,.6);
}

.ntf-03a__region {
  position: absolute;
  bottom: 30px;
  inset-inline-end: 30px;
  width: min(350px,calc(100% - 60px));
}

.ntf-03a__toast {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 15px 16px 18px;
  border-radius: 15px;
  overflow: hidden;
  background: rgba(28,20,32,.95);
  border: 1px solid rgba(220,190,235,.2);
  box-shadow: 0 26px 55px -22px rgba(0,0,0,.85);
  animation: ntf-03a-in .45s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-03a__toast.is-leaving {
  animation: ntf-03a-out .3s ease-in forwards;
}

.ntf-03a__ico {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #fff;
  background: var(--rose);
}

.ntf-03a__ico svg {
  width: 17px;
  height: 17px;
}

.ntf-03a__body {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-03a__body b {
  font-size: 13px;
  font-weight: 600;
  color: #f4edf7;
}

.ntf-03a__body small {
  font-size: 11px;
  color: rgba(233,219,240,.5);
}

.ntf-03a__undo {
  margin-left: auto;
  flex: none;
  padding: 8px 14px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: #f4edf7;
  background: rgba(255,255,255,.09);
  border: 1px solid rgba(220,190,235,.25);
  border-radius: 9px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-03a__undo:hover {
  background: rgba(255,255,255,.16);
}

.ntf-03a__bar {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 4px;
  background: linear-gradient(90deg,var(--rose),oklch(0.78 0.14 55));
  transform-origin: left;
  animation: ntf-03a-drain 5s linear forwards;
}

.ntf-03a__toast:hover .ntf-03a__bar,
.ntf-03a__toast:focus-within .ntf-03a__bar,
.ntf-03a__toast:focus .ntf-03a__bar {
  animation-play-state: paused;
}

@keyframes ntf-03a-drain {
  to {
    scale: 0 1;
  }
}

@keyframes ntf-03a-in {
  from {
    opacity: 0;
    translate: 0 24px;
    scale: .96;
  }
}

@keyframes ntf-03a-out {
  to {
    opacity: 0;
    translate: 0 12px;
    scale: .97;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-03a__toast {
    animation: ntf-03a-rmfade .25s ease both;
  }

  .ntf-03a__toast.is-leaving {
    animation: ntf-03a-rmout .25s ease forwards;
  }

  @keyframes ntf-03a-rmfade {
    from {
      opacity: 0;
    }
  }

  @keyframes ntf-03a-rmout {
    to {
      opacity: 0;
    }
  }
}

.ntf-03b,
.ntf-03b *,
.ntf-03b *::before,
.ntf-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --ntf-03b-p {
  syntax: "<percentage>";
  inherits: true;
  initial-value: 100%;
}

@property --ntf-03b-s {
  syntax: "<integer>";
  inherits: true;
  initial-value: 6;
}

.ntf-03b {
  --ink: #1f1d18;
  --acc: oklch(0.6 0.13 155);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f7f4ec,#eee8da);
  font-family: 'Newsreader',Georgia,serif;
}

.ntf-03b__fire {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-03b__card {
  width: min(460px,100%);
  text-align: center;
}

.ntf-03b__title {
  font-size: clamp(30px,4.5vw,40px);
  font-weight: 500;
  letter-spacing: -.01em;
  color: var(--ink);
}

.ntf-03b__title em {
  font-style: italic;
  color: var(--acc);
}

.ntf-03b__sub {
  margin-top: 10px;
  font-size: 15px;
  line-height: 1.6;
  color: rgba(31,29,24,.55);
}

.ntf-03b__btn {
  display: inline-block;
  margin-top: 22px;
  padding: 13px 28px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: #f7f4ec;
  background: var(--ink);
  border-radius: 999px;
  cursor: pointer;
  user-select: none;
  transition: background .2s,scale .12s;
}

.ntf-03b__btn:hover {
  background: #35322a;
}

.ntf-03b__btn:active {
  scale: .96;
}

.ntf-03b__toast {
  position: absolute;
  top: 26px;
  inset-inline-end: 26px;
  width: min(330px,calc(100% - 52px));
  display: none;
  align-items: center;
  gap: 13px;
  padding: 13px 14px 13px 13px;
  border-radius: 16px;
  background: #fffdf8;
  border: 1px solid rgba(31,29,24,.12);
  box-shadow: 0 22px 48px -22px rgba(31,29,24,.45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  --ntf-03b-p: 100%;
  --ntf-03b-s: 6;
}

.ntf-03b__fire:checked ~ .ntf-03b__toast {
  display: flex;
  animation: ntf-03b-count 6s linear forwards,ntf-03b-in .45s cubic-bezier(.22,1.2,.36,1),ntf-03b-gone 0s linear 6s forwards;
}

.ntf-03b__ring {
  flex: none;
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: conic-gradient(var(--acc) var(--ntf-03b-p),rgba(31,29,24,.12) 0);
}

.ntf-03b__ring::before {
  content: "";
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: #fffdf8;
}

.ntf-03b__num {
  position: relative;
  counter-reset: ntf03bs var(--ntf-03b-s);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-style: normal;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
}

.ntf-03b__num::after {
  content: counter(ntf03bs);
}

.ntf-03b__body {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-03b__body b {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
}

.ntf-03b__body small {
  font-size: 11.5px;
  color: rgba(31,29,24,.55);
}

.ntf-03b__close {
  margin-left: auto;
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  font-size: 12px;
  color: rgba(31,29,24,.5);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-03b__close:hover {
  background: rgba(31,29,24,.07);
  color: var(--ink);
}

@keyframes ntf-03b-count {
  from {
    --ntf-03b-p: 100%;
    --ntf-03b-s: 6;
  }

  to {
    --ntf-03b-p: 0%;
    --ntf-03b-s: 0;
  }
}

@keyframes ntf-03b-in {
  from {
    opacity: 0;
    translate: calc(100% + 40px) 0;
  }
}

@keyframes ntf-03b-gone {
  to {
    opacity: 0;
    visibility: hidden;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-03b__fire:checked ~ .ntf-03b__toast {
    animation: ntf-03b-count 6s linear forwards,ntf-03b-rmin .25s ease,ntf-03b-gone .3s linear 6s forwards;
  }

  @keyframes ntf-03b-rmin {
    from {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ntf-03a-btn'); if(!btn) return;
  var region=document.getElementById('ntf-03a-region'),tpl=document.getElementById('ntf-03a-tpl'),
      status=document.getElementById('ntf-03a-status');
  btn.addEventListener('click',function(){
    region.textContent=''; btn.disabled=true; status.textContent='';
    var toast=tpl.content.firstElementChild.cloneNode(true);
    var bar=toast.querySelector('.ntf-03a__bar');
    bar.addEventListener('animationend',function(e){
      if(e.animationName!=='ntf-03a-drain') return;
      toast.classList.add('is-leaving');                 /* bar ran out -> commit */
      status.textContent='recording.wav permanently deleted.';
      done();
    });
    toast.querySelector('.ntf-03a__undo').addEventListener('click',function(){
      toast.classList.add('is-leaving');
      status.textContent='Restored — nothing was deleted.';
      done();
    });
    toast.addEventListener('animationend',function(e){
      if(e.animationName==='ntf-03a-out'||e.animationName==='ntf-03a-rmout') toast.remove();
    });
    function done(){ btn.disabled=false; }
    region.appendChild(toast);
  });
})();

/* No JavaScript — @property makes --p a real <percentage> and --s a real <integer>, so one keyframe pair sweeps the conic ring AND counts the digits down via counter(); a zero-duration 'gone' animation at the 6s mark retires the toast. */
```
