---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-bounce-notification-animation/"
title: "CSS Bounce Notification Animation"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Animation-principles class disguised as a badge: a push-notification badge that arrives with real squash & stretch (drop, splat wide, rebound tall, settle —…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Bounce Notification Animation
Source: https://codefronts.com/snippets/css-notifications/css-bounce-notification-animation/

Animation-principles class disguised as a badge: a push-notification badge that arrives with real squash & stretch (drop, splat wide, rebound tall, settle — each frame annotated in the keyframes), and a pure-CSS bounce built from NOTHING but easing — one translate pair driven by a linear() bounce curve, with a ground shadow that squashes in sync.
## HTML
```html
<div class="ntf-23-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-23a" aria-label="Badge landing with squash and stretch">
  <div class="ntf-23a__wrap">
    <div class="ntf-23a__stage">
      <span class="ntf-23a__app" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>
      <b class="ntf-23a__badge" id="ntf-23a-badge" aria-hidden="true">1</b>
    </div>
    <div class="ntf-23a__frames" aria-hidden="true">
      <code>0% &nbsp;falling — stretch tall</code><code>45% impact — splat wide</code><code>62% rebound</code><code>100% settle</code>
    </div>
    <button class="ntf-23a__btn" id="ntf-23a-btn" type="button">Simulate push</button>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-23b" aria-label="Bounce made only from easing curves">
  <div class="ntf-23b__lab">
    <h2 class="ntf-23b__title">Same two keyframes, different curve</h2>
    <div class="ntf-23b__lanes">
      <div class="ntf-23b__lane"><span class="ntf-23b__chip ntf-23b__chip--bez" aria-hidden="true">1</span><i class="ntf-23b__shadow ntf-23b__shadow--bez" aria-hidden="true"></i><code class="ntf-23b__lbl">cubic-bezier(.34,1.56,.64,1)<br><span>one overshoot — beziers can't re-bounce</span></code></div>
      <div class="ntf-23b__lane"><span class="ntf-23b__chip ntf-23b__chip--lin" aria-hidden="true">2</span><i class="ntf-23b__shadow ntf-23b__shadow--lin" aria-hidden="true"></i><code class="ntf-23b__lbl">linear(0,.47 14%,.84 28%,1 40%,…)<br><span>true multi-bounce — physics in the curve</span></code></div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-23-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-23-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-23a,
.ntf-23a *,
.ntf-23a *::before,
.ntf-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-23a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#171b26,#0c0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-23a__wrap {
  display: grid;
  gap: 22px;
  justify-items: center;
}

.ntf-23a__stage {
  position: relative;
  padding: 20px;
}

.ntf-23a__app {
  width: 92px;
  height: 92px;
  display: grid;
  place-items: center;
  border-radius: 26px;
  color: #dfe7f8;
  background: linear-gradient(150deg,oklch(0.55 0.14 265),oklch(0.42 0.14 285));
  border: 1px solid rgba(175,195,240,.25);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.9);
}

.ntf-23a__app svg {
  width: 40px;
  height: 40px;
}

.ntf-23a__badge {
  position: absolute;
  top: 8px;
  inset-inline-end: 8px;
  min-inline-size: 30px;
  block-size: 30px;
  display: grid;
  place-items: center;
  padding-inline: 8px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #fff;
  background: oklch(0.63 0.21 25);
  border: 2.5px solid #171b26;
  transform-origin: bottom center;
  scale: 0;
}

.ntf-23a__badge.is-live {
  scale: 1;
}

.ntf-23a__badge.is-drop {
  animation: ntf-23a-land .7s cubic-bezier(.3,0,.3,1) both;
}

@keyframes ntf-23a-land {
  0% {
    opacity: 0;
    translate: 0 -46px;
    scale: .9 1.15;
  }

  20% {
    opacity: 1;
  }

  45% {
    translate: 0 0;
    scale: 1.22 .78;
  }

  62% {
    translate: 0 -12px;
    scale: .94 1.06;
  }

  78% {
    translate: 0 0;
    scale: 1.06 .96;
  }

  100% {
    translate: 0 0;
    scale: 1 1;
  }
}

.ntf-23a__frames {
  display: grid;
  gap: 5px;
  justify-items: center;
}

.ntf-23a__frames code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  color: rgba(210,222,245,.42);
}

.ntf-23a__btn {
  padding: 12px 26px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #0c0e15;
  background: #e8eefc;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  transition: background .2s,scale .12s;
}

.ntf-23a__btn:hover {
  background: #fff;
}

.ntf-23a__btn:active {
  scale: .96;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-23a__badge.is-drop {
    animation: ntf-23a-rm .2s ease both;
  }

  @keyframes ntf-23a-rm {
    from {
      opacity: 0;
      translate: 0 0;
      scale: 1;
    }

    to {
      opacity: 1;
      translate: 0 0;
      scale: 1;
    }
  }
}

.ntf-23b,
.ntf-23b *,
.ntf-23b *::before,
.ntf-23b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-23b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f2e9,#ece3d0);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-23b__lab {
  width: min(560px,100%);
  text-align: center;
}

.ntf-23b__title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #241f16;
}

.ntf-23b__lanes {
  margin-top: 30px;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 18px;
}

.ntf-23b__lane {
  display: grid;
  justify-items: center;
  gap: 0;
  padding: 26px 18px 20px;
  border-radius: 18px;
  background: #fffdf6;
  border: 1px solid rgba(36,31,22,.11);
  box-shadow: 0 22px 50px -30px rgba(36,31,22,.5);
}

.ntf-23b__chip {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  translate: 0 -70px;
}

.ntf-23b__chip--bez {
  background: oklch(0.6 0.13 260);
  animation: ntf-23b-drop 1.7s cubic-bezier(.34,1.56,.64,1) infinite;
}

.ntf-23b__chip--lin {
  background: oklch(0.63 0.16 40);
  animation: ntf-23b-drop 1.7s linear(0,.47 14%,.84 28%,1 40%,.89 50%,1 60%,.96 70%,1 80%,.99 90%,1) infinite;
}

@keyframes ntf-23b-drop {
  0%,
    12% {
    translate: 0 -70px;
  }

  62%,
    100% {
    translate: 0 0;
  }
}

.ntf-23b__shadow {
  width: 44px;
  height: 9px;
  margin-top: 8px;
  border-radius: 50%;
  background: rgba(36,31,22,.28);
  filter: blur(2px);
}

.ntf-23b__shadow--bez {
  animation: ntf-23b-sh 1.7s cubic-bezier(.34,1.56,.64,1) infinite;
}

.ntf-23b__shadow--lin {
  animation: ntf-23b-sh 1.7s linear(0,.47 14%,.84 28%,1 40%,.89 50%,1 60%,.96 70%,1 80%,.99 90%,1) infinite;
}

@keyframes ntf-23b-sh {
  0%,
    12% {
    scale: .55 1;
    opacity: .35;
  }

  62%,
    100% {
    scale: 1 1;
    opacity: 1;
  }
}

.ntf-23b__lbl {
  margin-top: 14px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  line-height: 1.7;
  color: rgba(36,31,22,.6);
}

.ntf-23b__lbl span {
  color: rgba(36,31,22,.4);
  font-size: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-23b__chip,
    .ntf-23b__shadow {
    animation: none;
    translate: 0 0;
  }
}
```

## JavaScript
```js
(function(){
  var badge=document.getElementById('ntf-23a-badge'); if(!badge) return;
  var n=0;
  badge.addEventListener('animationend',function(){ badge.classList.remove('is-drop'); });
  document.getElementById('ntf-23a-btn').addEventListener('click',function(){
    n++; badge.textContent=n>99?'99+':String(n);
    badge.classList.add('is-live');
    badge.classList.remove('is-drop');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ badge.classList.add('is-drop'); }); });
  });
})();

/* No JavaScript — both chips share ONE keyframe pair (up → down); the left curve overshoots once (the best a bezier can do), the right linear() curve re-crosses 1 three times, so the chip genuinely bounces. The shadows run the same curves. */
```
