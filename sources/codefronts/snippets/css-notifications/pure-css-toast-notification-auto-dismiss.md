---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/pure-css-toast-notification-auto-dismiss/"
title: "Pure CSS Toast Notification Auto Dismiss"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Auto-dismiss without a single setTimeout: a checkbox-armed toast whose enter → hold → exit lifecycle is one keyframe timeline with the hold time written as…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Toast Notification Auto Dismiss
Source: https://codefronts.com/snippets/css-notifications/pure-css-toast-notification-auto-dismiss/

Auto-dismiss without a single setTimeout: a checkbox-armed toast whose enter → hold → exit lifecycle is one keyframe timeline with the hold time written as percentages, and a three-toast demo reel where staggered animation-delays choreograph an endless notification sequence that pauses when you hover it.
## HTML
```html
<div class="ntf-02-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-02a" aria-label="Auto-dismissing toast on a single keyframe timeline">
  <input class="ntf-02a__fire" type="checkbox" id="ntf-02a-fire">
  <div class="ntf-02a__card">
    <p class="ntf-02a__kbd">0% in &nbsp;·&nbsp; 8–88% hold &nbsp;·&nbsp; 100% gone</p>
    <h2 class="ntf-02a__title">Draft autosave</h2>
    <p class="ntf-02a__sub">One animation owns the whole lifecycle. Uncheck &amp; recheck the button to replay it.</p>
    <label class="ntf-02a__btn" for="ntf-02a-fire">Save draft</label>
  </div>
  <aside class="ntf-02a__toast" role="status">
    <span class="ntf-02a__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><path d="M17 21v-8H7v8M7 3v5h8"/></svg></span>
    <span class="ntf-02a__body"><b>Draft saved</b><small>Dismisses itself in 4 seconds</small></span>
  </aside>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..700&display=swap" rel="stylesheet">
<section class="ntf-02b" aria-label="Three auto-dismissing toasts on staggered infinite loops">
  <div class="ntf-02b__copy">
    <h2 class="ntf-02b__title">The notification reel</h2>
    <p class="ntf-02b__sub">Three identical timelines, offset by 3s each — an endless feed with no JavaScript. <b>Hover the stack to pause it.</b></p>
  </div>
  <div class="ntf-02b__stack" aria-hidden="true">
    <div class="ntf-02b__toast ntf-02b__toast--1"><span class="ntf-02b__ico" style="background:oklch(0.8 0.14 155)">&#10003;</span><span><b>Payment received</b><small>Invoice #2041 · $1,250.00</small></span></div>
    <div class="ntf-02b__toast ntf-02b__toast--2"><span class="ntf-02b__ico" style="background:oklch(0.8 0.11 250)">@</span><span><b>Maya mentioned you</b><small>"ask @you about the rollout"</small></span></div>
    <div class="ntf-02b__toast ntf-02b__toast--3"><span class="ntf-02b__ico" style="background:oklch(0.82 0.13 85)">&#8593;</span><span><b>v3.2 update ready</b><small>Restart to apply</small></span></div>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-02-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-02-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-02a,
.ntf-02a *,
.ntf-02a *::before,
.ntf-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-02a {
  --acc: #3ec98e;
  --acc: oklch(0.78 0.15 160);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 100% at 50% 100%,#10231e,#0a1211);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-02a__fire {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-02a__card {
  width: min(430px,100%);
  text-align: center;
}

.ntf-02a__kbd {
  display: inline-block;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  font-weight: 600;
  color: var(--acc);
  background: oklch(0.78 0.15 160 / .09);
  border: 1px solid oklch(0.78 0.15 160 / .25);
  padding: 5px 11px;
  border-radius: 999px;
}

.ntf-02a__title {
  margin-top: 16px;
  font-size: 26px;
  font-weight: 600;
  color: #ecf6f1;
  letter-spacing: -.01em;
}

.ntf-02a__sub {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(214,235,226,.55);
}

.ntf-02a__btn {
  display: inline-block;
  margin-top: 22px;
  padding: 13px 28px;
  font-size: 14px;
  font-weight: 600;
  color: #0a1211;
  background: var(--acc);
  border-radius: 12px;
  cursor: pointer;
  user-select: none;
  transition: filter .15s,scale .12s;
}

.ntf-02a__btn:hover {
  filter: brightness(1.08);
}

.ntf-02a__btn:active {
  scale: .96;
}

.ntf-02a__toast {
  position: absolute;
  bottom: 30px;
  left: 50%;
  margin-left: min(-170px,calc(-50% + 24px));
  width: min(340px,calc(100% - 48px));
  display: none;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 15px;
  background: rgba(16,32,27,.92);
  border: 1px solid oklch(0.78 0.15 160 / .3);
  box-shadow: 0 24px 50px -20px rgba(0,0,0,.8);
}

.ntf-02a__fire:checked ~ .ntf-02a__toast {
  display: flex;
  animation: ntf-02a-life 4.2s cubic-bezier(.4,0,.2,1) forwards;
}

.ntf-02a__icon {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #0a1211;
  background: var(--acc);
}

.ntf-02a__icon svg {
  width: 18px;
  height: 18px;
}

.ntf-02a__body {
  display: grid;
  gap: 2px;
}

.ntf-02a__body b {
  font-size: 13.5px;
  font-weight: 600;
  color: #ecf6f1;
}

.ntf-02a__body small {
  font-size: 11.5px;
  color: rgba(214,235,226,.55);
}

@keyframes ntf-02a-life {
  0% {
    opacity: 0;
    translate: 0 16px;
    scale: .97;
  }

  8%,
    88% {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  100% {
    opacity: 0;
    translate: 0 -10px;
    scale: .98;
    visibility: hidden;
  }
}

@media (prefers-reduced-motion: reduce) {
  @keyframes ntf-02a-life {
    0% {
      opacity: 0;
    }

    8%,
        88% {
      opacity: 1;
    }

    100% {
      opacity: 0;
      visibility: hidden;
    }
  }
}

.ntf-02b,
.ntf-02b *,
.ntf-02b *::before,
.ntf-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-02b {
  --ink: #241f18;
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 34px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#fbf6ec,#f3e9d6);
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.ntf-02b__copy {
  width: min(460px,100%);
  text-align: center;
}

.ntf-02b__title {
  font-size: clamp(28px,4vw,36px);
  font-weight: 700;
  letter-spacing: -.02em;
  color: var(--ink);
}

.ntf-02b__sub {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(36,31,24,.55);
}

.ntf-02b__sub b {
  color: var(--ink);
}

.ntf-02b__stack {
  position: relative;
  width: min(340px,100%);
  height: 76px;
}

.ntf-02b__toast {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 18px;
  border-radius: 16px;
  background: #fff;
  border: 1px solid rgba(36,31,24,.1);
  box-shadow: 0 20px 44px -22px rgba(36,31,24,.45);
  opacity: 0;
  animation: ntf-02b-life 9s cubic-bezier(.4,0,.2,1) infinite;
}

.ntf-02b__toast--2 {
  animation-delay: 3s;
}

.ntf-02b__toast--3 {
  animation-delay: 6s;
}

.ntf-02b__stack:hover .ntf-02b__toast {
  animation-play-state: paused;
}

.ntf-02b__ico {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  font-size: 15px;
  font-weight: 700;
  color: #241f18;
}

.ntf-02b__toast span:last-child {
  display: grid;
  gap: 2px;
}

.ntf-02b__toast b {
  font-size: 14px;
  font-weight: 700;
  color: var(--ink);
}

.ntf-02b__toast small {
  font-size: 12px;
  color: rgba(36,31,24,.5);
}

@keyframes ntf-02b-life {
  0% {
    opacity: 0;
    translate: 0 22px;
    scale: .96;
  }

  4%,
    29% {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  33%,
    100% {
    opacity: 0;
    translate: 0 -14px;
    scale: .97;
  }
}

@media (prefers-reduced-motion: reduce) {
  @keyframes ntf-02b-life {
    0% {
      opacity: 0;
      translate: 0 0;
      scale: 1;
    }

    4%,
        29% {
      opacity: 1;
    }

    33%,
        100% {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — the checkbox arms the animation, the keyframe timeline is the timer (0–8% enter, 8–88% hold, 88–100% exit), forwards holds the end state and visibility:hidden retires the hit-area. */

/* No JavaScript — each toast runs the same 9s lifecycle keyframes; animation-delay of 0/3/6s turns three loops into a sequence, and :hover pauses every animation in the stack at once. */
```
