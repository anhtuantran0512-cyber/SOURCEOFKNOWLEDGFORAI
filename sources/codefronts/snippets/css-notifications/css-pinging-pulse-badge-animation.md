---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-pinging-pulse-badge-animation/"
title: "CSS Pinging Pulse Badge Animation"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The ping, engineered and then enjoyed: a message icon whose unread dot emits staggered double rings (the exact anatomy of Tailwind's animate-ping, annotated…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pinging Pulse Badge Animation
Source: https://codefronts.com/snippets/css-notifications/css-pinging-pulse-badge-animation/

The ping, engineered and then enjoyed: a message icon whose unread dot emits staggered double rings (the exact anatomy of Tailwind's animate-ping, annotated and improved with dead-time and a reduced-motion halo), and a full radar sweep stage — conic-gradient beam, ranging rings, blipping contacts — that shows the same ping keyframes scaling from 8px badge to 280px instrument.
## HTML
```html
<div class="ntf-14-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-14a" aria-label="Message icon with pinging unread badge">
  <div class="ntf-14a__wrap">
    <button class="ntf-14a__btn" type="button" aria-label="Messages, new unread">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      <span class="ntf-14a__ping" aria-hidden="true"></span>
    </button>
    <div class="ntf-14a__notes">
      <code class="ntf-14a__line"><i>::before + ::after</i> — two rings, 1.1s apart</code>
      <code class="ntf-14a__line"><i>55%,100%</i> — dead-time between waves</code>
      <code class="ntf-14a__line"><i>background:inherit</i> — rings follow the dot's color</code>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<section class="ntf-14b" aria-label="Radar sweep with pinging contact blips">
  <div class="ntf-14b__rig">
    <div class="ntf-14b__scope" role="img" aria-label="Radar scope: three contacts pinging as the beam passes">
      <i class="ntf-14b__sweep" aria-hidden="true"></i>
      <i class="ntf-14b__blip" style="--x:66%;--y:30%;--d:.9s" aria-hidden="true"></i>
      <i class="ntf-14b__blip" style="--x:32%;--y:58%;--d:2.5s" aria-hidden="true"></i>
      <i class="ntf-14b__blip ntf-14b__blip--hot" style="--x:58%;--y:70%;--d:1.7s" aria-hidden="true"></i>
    </div>
    <p class="ntf-14b__read">CONTACTS: 3 &nbsp;·&nbsp; SWEEP 4.0s &nbsp;·&nbsp; blip delay = bearing / 360 × 4s</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-14-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-14-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-14a,
.ntf-14a *,
.ntf-14a *::before,
.ntf-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-14a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#161a24,#0b0e14);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-14a__wrap {
  display: grid;
  gap: 30px;
  justify-items: center;
}

.ntf-14a__btn {
  position: relative;
  width: 74px;
  height: 74px;
  display: grid;
  place-items: center;
  border: 1px solid rgba(165,190,230,.2);
  border-radius: 22px;
  color: #dbe4f6;
  background: rgba(255,255,255,.055);
  cursor: pointer;
  transition: background .2s,translate .2s;
}

.ntf-14a__btn:hover {
  background: rgba(255,255,255,.1);
  translate: 0 -2px;
}

.ntf-14a__btn svg {
  width: 32px;
  height: 32px;
}

.ntf-14a__ping {
  position: absolute;
  top: 14px;
  inset-inline-end: 14px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: oklch(0.68 0.21 25);
  translate: 50% -50%;
}

.ntf-14a__ping::before,
.ntf-14a__ping::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ntf-14a-ping 2.2s cubic-bezier(0,0,.2,1) infinite;
}

.ntf-14a__ping::after {
  animation-delay: 1.1s;
}

@keyframes ntf-14a-ping {
  55%,
    100% {
    scale: 3;
    opacity: 0;
  }
}

.ntf-14a__notes {
  display: grid;
  gap: 8px;
}

.ntf-14a__line {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11.5px;
  color: rgba(205,220,248,.5);
}

.ntf-14a__line i {
  font-style: normal;
  color: oklch(0.75 0.15 25);
  background: oklch(0.68 0.21 25 / .1);
  border: 1px solid oklch(0.68 0.21 25 / .3);
  padding: 2px 7px;
  border-radius: 6px;
  margin-inline-end: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-14a__ping::before,
    .ntf-14a__ping::after {
    animation: none;
    scale: 1.9;
    opacity: .22;
  }

  .ntf-14a__ping::after {
    scale: 2.6;
    opacity: .12;
  }
}

.ntf-14b,
.ntf-14b *,
.ntf-14b *::before,
.ntf-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-14b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #07100b;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
}

.ntf-14b__rig {
  display: grid;
  gap: 22px;
  justify-items: center;
}

.ntf-14b__scope {
  position: relative;
  width: min(280px,72vw);
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  background: radial-gradient(circle,#0b1810 30%,#081209 70%),repeating-radial-gradient(circle at 50% 50%,transparent 0 34px,oklch(0.75 0.16 150 / .14) 34px 35px);
  background-blend-mode: screen;
  border: 1.5px solid oklch(0.75 0.16 150 / .4);
  box-shadow: 0 0 60px -10px oklch(0.75 0.16 150 / .3),inset 0 0 40px rgba(0,0,0,.6);
}

.ntf-14b__scope::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(oklch(0.75 0.16 150 / .12) 1px,transparent 1px) 50% 50%/100% 50.5%,linear-gradient(90deg,oklch(0.75 0.16 150 / .12) 1px,transparent 1px) 50% 50%/50.5% 100%;
  background-repeat: no-repeat;
}

.ntf-14b__sweep {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 0deg,oklch(0.8 0.18 150 / .45),transparent 70deg);
  animation: ntf-14b-sweep 4s linear infinite;
}

@keyframes ntf-14b-sweep {
  to {
    rotate: 360deg;
  }
}

.ntf-14b__blip {
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(0.85 0.17 150);
  translate: -50% -50%;
}

.ntf-14b__blip::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ntf-14b-ping 4s cubic-bezier(0,0,.2,1) var(--d) infinite;
}

.ntf-14b__blip--hot {
  background: oklch(0.75 0.19 25);
}

@keyframes ntf-14b-ping {
  0% {
    scale: 1;
    opacity: .9;
  }

  30%,
    100% {
    scale: 4;
    opacity: 0;
  }
}

.ntf-14b__read {
  font-size: 10.5px;
  letter-spacing: .14em;
  color: oklch(0.8 0.14 150 / .65);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-14b__sweep {
    animation: none;
    opacity: .25;
  }

  .ntf-14b__blip::after {
    animation: none;
    scale: 2.2;
    opacity: .25;
  }
}
```

## JavaScript
```js
/* No JavaScript — two pseudo-element rings share one keyframe, offset by half a period; the 55% jump parks each ring invisible between waves so the ping breathes instead of strobing. */

/* No JavaScript — the beam is a rotating conic-gradient, range rings are a repeating-radial-gradient, and every blip reuses the same ping keyframes with a delay matching its bearing so it flares as the beam passes. */
```
