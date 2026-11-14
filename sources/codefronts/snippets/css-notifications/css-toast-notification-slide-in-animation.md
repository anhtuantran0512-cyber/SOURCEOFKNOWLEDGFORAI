---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-toast-notification-slide-in-animation/"
title: "CSS Toast Notification Slide In Animation"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The definitive slide-in toast, three ways: a zero-JavaScript version where @starting-style and transition-behavior:allow-discrete animate the toast in AND…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toast Notification Slide In Animation
Source: https://codefronts.com/snippets/css-notifications/css-toast-notification-slide-in-animation/

The definitive slide-in toast, three ways: a zero-JavaScript version where @starting-style and transition-behavior:allow-discrete animate the toast in AND out of display:none, a production JS spawner with a linear() spring entry, auto fade-out and aria-live wiring, and an easing taster that races the same slide under three timing functions so you can feel the difference.
## HTML
```html
<div class="ntf-01-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-01a" aria-label="Slide-in toast with @starting-style, zero JavaScript">
  <input class="ntf-01a__toggle" type="checkbox" id="ntf-01a-show">
  <div class="ntf-01a__card">
    <p class="ntf-01a__badge">@starting-style · 0 lines of JS</p>
    <h2 class="ntf-01a__title">Deploy finished</h2>
    <p class="ntf-01a__sub">Toggle the toast — it slides in from the right and fades away through <b>display:none</b>, both directions pure CSS.</p>
    <label class="ntf-01a__btn" for="ntf-01a-show"><span class="ntf-01a__btn-show">Show toast</span><span class="ntf-01a__btn-hide">Dismiss toast</span></label>
  </div>
  <aside class="ntf-01a__toast" role="status">
    <span class="ntf-01a__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
    <span class="ntf-01a__body"><b>Build #4021 is live</b><small>production · 12s ago</small></span>
    <label class="ntf-01a__close" for="ntf-01a-show" aria-label="Dismiss notification">&#10005;</label>
  </aside>
</section>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<section class="ntf-01b" aria-label="Re-triggerable slide-in toast with spring easing and ARIA">
  <div class="ntf-01b__card">
    <h2 class="ntf-01b__title">Ship your <em>changes</em></h2>
    <p class="ntf-01b__sub">Every click spawns a fresh toast: spring in, hold 3 seconds, fade out, node removed on animationend.</p>
    <button class="ntf-01b__btn" id="ntf-01b-btn" type="button">Publish post</button>
  </div>
  <div class="ntf-01b__region" id="ntf-01b-region" role="status" aria-live="polite"></div>
  <template id="ntf-01b-tpl">
    <div class="ntf-01b__toast">
      <span class="ntf-01b__dot" aria-hidden="true"></span>
      <span class="ntf-01b__text"><b>Post published</b><small>Visible to everyone · just now</small></span>
    </div>
  </template>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="ntf-01c" aria-label="Compare three slide-in easing curves">
  <div class="ntf-01c__stage">
    <h2 class="ntf-01c__title">Same slide, three personalities</h2>
    <div class="ntf-01c__lanes" id="ntf-01c-lanes">
      <div class="ntf-01c__lane"><code class="ntf-01c__tag">ease-out</code><div class="ntf-01c__toast ntf-01c__toast--a"><b>Calm</b><small>gets there, no drama</small></div></div>
      <div class="ntf-01c__lane"><code class="ntf-01c__tag">cubic-bezier(.22,1.4,.36,1)</code><div class="ntf-01c__toast ntf-01c__toast--b"><b>Overshoot</b><small>one confident bounce</small></div></div>
      <div class="ntf-01c__lane"><code class="ntf-01c__tag">linear(… spring …)</code><div class="ntf-01c__toast ntf-01c__toast--c"><b>Spring</b><small>physical wobble settle</small></div></div>
    </div>
    <button class="ntf-01c__btn" id="ntf-01c-btn" type="button">Replay all</button>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-01-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-01-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-01a,
.ntf-01a *,
.ntf-01a *::before,
.ntf-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-01a {
  --ok: oklch(0.78 0.16 160);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 90% at 50% 0%,#131a27,#0a0e16);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-01a__toggle {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-01a__card {
  width: min(420px,100%);
  text-align: center;
}

.ntf-01a__badge {
  display: inline-block;
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-weight: 600;
  color: var(--ok);
  background: oklch(0.78 0.16 160 / .1);
  border: 1px solid oklch(0.78 0.16 160 / .25);
  padding: 5px 10px;
  border-radius: 999px;
  margin-bottom: 18px;
}

.ntf-01a__title {
  font-size: 26px;
  font-weight: 600;
  color: #eef3ff;
  letter-spacing: -.01em;
}

.ntf-01a__sub {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(210,222,245,.55);
}

.ntf-01a__sub b {
  color: rgba(230,238,255,.85);
}

.ntf-01a__btn {
  display: inline-block;
  margin-top: 22px;
  padding: 13px 26px;
  font-size: 14px;
  font-weight: 600;
  color: #0a0e16;
  background: #e8eefc;
  border-radius: 12px;
  cursor: pointer;
  user-select: none;
  transition: scale .15s,background .2s;
}

.ntf-01a__btn:hover {
  background: #fff;
}

.ntf-01a__btn:active {
  scale: .96;
}

.ntf-01a__btn-hide {
  display: none;
}

.ntf-01a__toggle:checked ~ .ntf-01a__card .ntf-01a__btn-show {
  display: none;
}

.ntf-01a__toggle:checked ~ .ntf-01a__card .ntf-01a__btn-hide {
  display: inline;
}

.ntf-01a__toast {
  position: absolute;
  top: 26px;
  inset-inline-end: 26px;
  width: min(340px,calc(100% - 48px));
  display: none;
  align-items: center;
  gap: 12px;
  padding: 14px 14px 14px 16px;
  border-radius: 16px;
  background: linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.04));
  border: 1px solid rgba(160,190,235,.22);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.85);
  opacity: 0;
  translate: calc(100% + 40px) 0;
  transition: translate .55s cubic-bezier(.22,1.2,.36,1),opacity .35s ease,display .55s allow-discrete;
}

.ntf-01a__toggle:checked ~ .ntf-01a__toast {
  display: flex;
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  .ntf-01a__toggle:checked ~ .ntf-01a__toast {
    opacity: 0;
    translate: calc(100% + 40px) 0;
  }
}

.ntf-01a__icon {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #08110c;
  background: var(--ok);
}

.ntf-01a__icon svg {
  width: 18px;
  height: 18px;
}

.ntf-01a__body {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-01a__body b {
  font-size: 13.5px;
  font-weight: 600;
  color: #eef3ff;
}

.ntf-01a__body small {
  font-size: 11.5px;
  color: rgba(210,222,245,.5);
}

.ntf-01a__close {
  margin-left: auto;
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  font-size: 12px;
  color: rgba(210,222,245,.55);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-01a__close:hover {
  background: rgba(255,255,255,.08);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-01a__toast {
    transition: opacity .3s ease,display .3s allow-discrete;
    translate: 0 0;
  }

  @starting-style {
    .ntf-01a__toggle:checked ~ .ntf-01a__toast {
      translate: 0 0;
    }
  }
}

.ntf-01b,
.ntf-01b *,
.ntf-01b *::before,
.ntf-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-01b {
  --ink: #22201b;
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#faf7f0,#f0eadb);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ntf-01b__card {
  width: min(440px,100%);
  text-align: center;
}

.ntf-01b__title {
  font-family: 'Instrument Serif',Georgia,serif;
  font-weight: 400;
  font-size: clamp(36px,5vw,48px);
  color: var(--ink);
  letter-spacing: -.01em;
}

.ntf-01b__title em {
  font-style: italic;
  color: oklch(0.58 0.12 60);
}

.ntf-01b__sub {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(34,32,27,.55);
}

.ntf-01b__btn {
  margin-top: 24px;
  padding: 14px 30px;
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  color: #faf7f0;
  background: var(--ink);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 14px 30px -14px rgba(34,32,27,.5);
  transition: scale .15s,background .2s;
}

.ntf-01b__btn:hover {
  background: #37342c;
}

.ntf-01b__btn:active {
  scale: .96;
}

.ntf-01b__region {
  position: absolute;
  top: 24px;
  inset-inline-end: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: min(320px,calc(100% - 48px));
}

.ntf-01b__toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid rgba(34,32,27,.1);
  box-shadow: 0 18px 40px -20px rgba(34,32,27,.4);
  animation: ntf-01b-in .6s linear(0,0.32 9%,0.72 18.5%,0.96 27%,1.08 35.5%,1.1 40%,1.03 55%,0.99 68%,1) both,ntf-01b-out .3s ease-in 3.2s forwards;
}

.ntf-01b__dot {
  flex: none;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.62 0.16 150);
  box-shadow: 0 0 0 4px oklch(0.62 0.16 150 / .16);
}

.ntf-01b__text {
  display: grid;
  gap: 1px;
}

.ntf-01b__text b {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
}

.ntf-01b__text small {
  font-size: 11.5px;
  color: rgba(34,32,27,.5);
}

@keyframes ntf-01b-in {
  from {
    translate: calc(100% + 40px) 0;
  }

  to {
    translate: 0 0;
  }
}

@keyframes ntf-01b-out {
  to {
    opacity: 0;
    translate: 0 -8px;
    scale: .97;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-01b__toast {
    animation: ntf-01b-fade .25s ease both,ntf-01b-out .3s ease-in 3.2s forwards;
  }

  @keyframes ntf-01b-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }
}

.ntf-01c,
.ntf-01c *,
.ntf-01c *::before,
.ntf-01c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-01c {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#15171c,#0c0d11);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-01c__stage {
  width: min(560px,100%);
}

.ntf-01c__title {
  font-size: 22px;
  font-weight: 600;
  color: #edf1fa;
  letter-spacing: -.01em;
  text-align: center;
}

.ntf-01c__lanes {
  margin-top: 26px;
  display: grid;
  gap: 14px;
}

.ntf-01c__lane {
  display: grid;
  gap: 7px;
  padding: 14px;
  border-radius: 16px;
  background: rgba(255,255,255,.035);
  border: 1px solid rgba(160,180,220,.13);
  overflow: hidden;
}

.ntf-01c__tag {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11px;
  color: oklch(0.75 0.13 200);
}

.ntf-01c__toast {
  justify-self: end;
  display: grid;
  gap: 1px;
  width: min(250px,80%);
  padding: 11px 16px;
  border-radius: 11px;
  background: #eef2fb;
  translate: calc(100% + 40px) 0;
}

.ntf-01c__toast b {
  font-size: 13px;
  font-weight: 600;
  color: #15171c;
}

.ntf-01c__toast small {
  font-size: 11px;
  color: rgba(21,23,28,.55);
}

.is-play .ntf-01c__toast--a {
  animation: ntf-01c-in .6s ease-out .15s both;
}

.is-play .ntf-01c__toast--b {
  animation: ntf-01c-in .6s cubic-bezier(.22,1.4,.36,1) .15s both;
}

.is-play .ntf-01c__toast--c {
  animation: ntf-01c-in .8s linear(0,0.35 8%,0.78 17%,1.05 26%,1.14 32%,1.06 42%,0.98 52%,1.01 66%,1) .15s both;
}

@keyframes ntf-01c-in {
  to {
    translate: 0 0;
  }
}

.ntf-01c__btn {
  margin: 26px auto 0;
  display: block;
  padding: 12px 26px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  color: #0c0d11;
  background: oklch(0.75 0.13 200);
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  transition: filter .15s,scale .12s;
}

.ntf-01c__btn:hover {
  filter: brightness(1.1);
}

.ntf-01c__btn:active {
  scale: .96;
}

@media (prefers-reduced-motion: reduce) {
  .is-play .ntf-01c__toast {
    animation: ntf-01c-fade .3s ease both;
  }

  @keyframes ntf-01c-fade {
    from {
      opacity: 0;
      translate: 0 0;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — the checkbox holds the open/closed state, @starting-style provides the slide-in 'from' values, and transition-behavior:allow-discrete keeps display:flex alive until the exit transition finishes. */

(function(){
  var btn=document.getElementById('ntf-01b-btn'); if(!btn) return;
  var region=document.getElementById('ntf-01b-region'),tpl=document.getElementById('ntf-01b-tpl');
  btn.addEventListener('click',function(){
    var toast=tpl.content.firstElementChild.cloneNode(true);
    region.appendChild(toast);
    toast.addEventListener('animationend',function(e){
      if(e.animationName==='ntf-01b-out') toast.remove(); /* CSS times the exit; JS only cleans up */
    });
  });
})();

(function(){
  var lanes=document.getElementById('ntf-01c-lanes'); if(!lanes) return;
  var btn=document.getElementById('ntf-01c-btn');
  function play(){
    lanes.classList.remove('is-play');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ lanes.classList.add('is-play'); }); });
  }
  btn.addEventListener('click',play);
  play();
})();
```
