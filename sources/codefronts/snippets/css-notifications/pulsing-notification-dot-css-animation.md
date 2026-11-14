---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/pulsing-notification-dot-css-animation/"
title: "Pulsing Notification Dot CSS Animation"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "A status-dot system with three motion grammars (LIVE pings outward, online breathes softly, away sits still — stillness is information too), and a…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulsing Notification Dot CSS Animation
Source: https://codefronts.com/snippets/css-notifications/pulsing-notification-dot-css-animation/

A status-dot system with three motion grammars (LIVE pings outward, online breathes softly, away sits still — stillness is information too), and a performance clinic that runs the same pulse two ways — animated box-shadow versus a scaled pseudo-element ring — with DevTools-verifiable labels explaining why one stays on the compositor.
## HTML
```html
<div class="ntf-10-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="ntf-10a" aria-label="Live online and away status dots">
  <div class="ntf-10a__panel">
    <h2 class="ntf-10a__title">Presence</h2>
    <div class="ntf-10a__rowset">
      <div class="ntf-10a__row"><span class="ntf-10a__dot ntf-10a__dot--live" aria-hidden="true"></span><span class="ntf-10a__tx"><b>Design crit — streaming</b><small>184 watching</small></span><code class="ntf-10a__tag ntf-10a__tag--live">LIVE</code></div>
      <div class="ntf-10a__row"><span class="ntf-10a__dot ntf-10a__dot--on" aria-hidden="true"></span><span class="ntf-10a__tx"><b>Amara Okafor</b><small>online · in #frontend</small></span><code class="ntf-10a__tag">ONLINE</code></div>
      <div class="ntf-10a__row"><span class="ntf-10a__dot ntf-10a__dot--away" aria-hidden="true"></span><span class="ntf-10a__tx"><b>Jonas Weber</b><small>away · back at 14:00</small></span><code class="ntf-10a__tag">AWAY</code></div>
    </div>
    <p class="ntf-10a__cap">Ping = happening now · breathe = available · still = away. Motion is a vocabulary — don't pulse everything.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<section class="ntf-10b" aria-label="Box-shadow pulse versus transform pulse performance comparison">
  <div class="ntf-10b__lab">
    <p class="ntf-10b__head">// same pulse, two render paths</p>
    <div class="ntf-10b__split">
      <div class="ntf-10b__cell ntf-10b__cell--bad">
        <span class="ntf-10b__dot ntf-10b__dot--shadow" aria-hidden="true"></span>
        <code class="ntf-10b__code">@keyframes bad {
  to { box-shadow:
    0 0 0 14px transparent }
}</code>
        <p class="ntf-10b__verdict ntf-10b__verdict--bad">✗ paints every frame</p>
      </div>
      <div class="ntf-10b__cell">
        <span class="ntf-10b__dot ntf-10b__dot--ring" aria-hidden="true"></span>
        <code class="ntf-10b__code">@keyframes good {
  75%, 100% { scale: 2.4;
    opacity: 0 }
}</code>
        <p class="ntf-10b__verdict">✓ compositor only</p>
      </div>
    </div>
    <p class="ntf-10b__cap">Open DevTools → Rendering → “Paint flashing”: the left dot flashes green on every frame, the right one never does. One dot is harmless — a presence list of 50 is not.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-10-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-10-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-10a,
.ntf-10a *,
.ntf-10a *::before,
.ntf-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-10a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151a24,#0b0e14);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-10a__panel {
  width: min(410px,100%);
  padding: 24px;
  border-radius: 20px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(165,190,230,.15);
  box-shadow: 0 30px 70px -40px rgba(0,0,0,.9);
}

.ntf-10a__title {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #edf2fc;
}

.ntf-10a__rowset {
  margin-top: 14px;
  display: grid;
}

.ntf-10a__row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 13px 10px;
  border-radius: 12px;
  transition: background .15s;
}

.ntf-10a__row:hover {
  background: rgba(255,255,255,.045);
}

.ntf-10a__row+.ntf-10a__row {
  border-top: 1px solid rgba(165,190,230,.09);
}

.ntf-10a__dot {
  flex: none;
  position: relative;
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.ntf-10a__dot--live {
  background: oklch(0.66 0.21 25);
}

.ntf-10a__dot--live::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ntf-10a-ping 1.6s cubic-bezier(0,0,.2,1) infinite;
}

.ntf-10a__dot--on {
  background: oklch(0.78 0.16 155);
}

.ntf-10a__dot--on::after {
  content: "";
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  border: 1.5px solid oklch(0.78 0.16 155 / .5);
  animation: ntf-10a-breathe 2.6s ease-in-out infinite;
}

.ntf-10a__dot--away {
  background: oklch(0.8 0.13 85);
  opacity: .8;
}

@keyframes ntf-10a-ping {
  75%,
    100% {
    scale: 2.6;
    opacity: 0;
  }
}

@keyframes ntf-10a-breathe {
  0%,
    100% {
    scale: .85;
    opacity: .4;
  }

  50% {
    scale: 1.15;
    opacity: 1;
  }
}

.ntf-10a__tx {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-10a__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #edf2fc;
}

.ntf-10a__tx small {
  font-size: 11.5px;
  color: rgba(212,224,246,.5);
}

.ntf-10a__tag {
  margin-left: auto;
  flex: none;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 9.5px;
  letter-spacing: .12em;
  color: rgba(212,224,246,.55);
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(165,190,230,.16);
  padding: 4px 8px;
  border-radius: 6px;
}

.ntf-10a__tag--live {
  color: oklch(0.75 0.18 25);
  background: oklch(0.66 0.21 25 / .12);
  border-color: oklch(0.66 0.21 25 / .35);
}

.ntf-10a__cap {
  margin-top: 16px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(212,224,246,.42);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-10a__dot--live::after {
    animation: none;
    scale: 1.8;
    opacity: .25;
  }

  .ntf-10a__dot--on::after {
    animation: none;
    opacity: .7;
  }
}

.ntf-10b,
.ntf-10b *,
.ntf-10b *::before,
.ntf-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-10b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0d0f12;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
}

.ntf-10b__lab {
  width: min(560px,100%);
}

.ntf-10b__head {
  font-size: 12px;
  color: rgba(190,210,180,.5);
  letter-spacing: .04em;
}

.ntf-10b__split {
  margin-top: 16px;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 14px;
}

.ntf-10b__cell {
  display: grid;
  justify-items: center;
  gap: 16px;
  padding: 28px 20px 20px;
  border-radius: 14px;
  background: #12151a;
  border: 1px solid rgba(120,220,160,.25);
}

.ntf-10b__cell--bad {
  border-color: rgba(240,110,110,.3);
}

.ntf-10b__dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  position: relative;
}

.ntf-10b__dot--shadow {
  background: oklch(0.68 0.19 25);
  animation: ntf-10b-bad 1.6s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes ntf-10b-bad {
  0% {
    box-shadow: 0 0 0 0 oklch(0.68 0.19 25 / .55);
  }

  75%,
    100% {
    box-shadow: 0 0 0 16px oklch(0.68 0.19 25 / 0);
  }
}

.ntf-10b__dot--ring {
  background: oklch(0.78 0.16 155);
}

.ntf-10b__dot--ring::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ntf-10b-good 1.6s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes ntf-10b-good {
  75%,
    100% {
    scale: 2.4;
    opacity: 0;
  }
}

.ntf-10b__code {
  white-space: pre;
  font-size: 11px;
  line-height: 1.7;
  color: #c7d4e8;
  background: #0a0c0f;
  border: 1px solid rgba(140,160,200,.14);
  padding: 12px 14px;
  border-radius: 10px;
  width: 100%;
}

.ntf-10b__verdict {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .05em;
  color: oklch(0.8 0.15 155);
}

.ntf-10b__verdict--bad {
  color: oklch(0.72 0.17 25);
}

.ntf-10b__cap {
  margin-top: 18px;
  font-size: 11px;
  line-height: 1.75;
  color: rgba(199,212,232,.45);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-10b__dot--shadow {
    animation: none;
    box-shadow: 0 0 0 6px oklch(0.68 0.19 25 / .25);
  }

  .ntf-10b__dot--ring::after {
    animation: none;
    scale: 1.8;
    opacity: .3;
  }
}
```

## JavaScript
```js
/* No JavaScript — each status is a different motion grammar on the same two-layer dot; reduced-motion swaps the ping for a static halo so LIVE still reads as louder than ONLINE. */

/* No JavaScript — the two animations are the demo. Verify with DevTools → More tools → Rendering → Paint flashing: box-shadow repaints per frame, the scaled ::after ring never leaves the compositor. */
```
