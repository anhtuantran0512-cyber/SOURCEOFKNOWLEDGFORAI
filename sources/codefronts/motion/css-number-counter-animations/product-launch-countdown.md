---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/product-launch-countdown/"
title: "Product Launch Countdown Timer"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A launch countdown that survives contact with reality: it computes from a real target timestamp (not a decrementing variable, which drifts and breaks on tab…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Launch Countdown Timer
Source: https://codefronts.com/motion/css-number-counter-animations/product-launch-countdown/

A launch countdown that survives contact with reality: it computes from a real target timestamp (not a decrementing variable, which drifts and breaks on tab sleep), renders days/hours/minutes/seconds with progress rings, announces at meaningful thresholds only, and degrades to a live 'We're live' state when it reaches zero.
## HTML
```html
<section class="cnc-13" aria-label="Product launch countdown timer demo">
  <div class="cnc-13__stage">
    <div class="cnc-13__panel" data-state="live">
      <p class="cnc-13__eyebrow">Public beta opens</p>
      <h2 class="cnc-13__head">Halo Studio 3.0</h2>
      <div class="cnc-13__units" role="timer" aria-label="Time remaining until launch">
        <div class="cnc-13__unit" data-max="30" style="--cnc-13-p:0"><span class="cnc-13__ring"><b class="cnc-13__n">00</b></span><span class="cnc-13__u">days</span></div>
        <div class="cnc-13__unit" data-max="24" style="--cnc-13-p:0"><span class="cnc-13__ring"><b class="cnc-13__n">00</b></span><span class="cnc-13__u">hours</span></div>
        <div class="cnc-13__unit" data-max="60" style="--cnc-13-p:0"><span class="cnc-13__ring"><b class="cnc-13__n">00</b></span><span class="cnc-13__u">minutes</span></div>
        <div class="cnc-13__unit" data-max="60" style="--cnc-13-p:0"><span class="cnc-13__ring"><b class="cnc-13__n">00</b></span><span class="cnc-13__u">seconds</span></div>
      </div>
      <p class="cnc-13__when"></p>
      <button class="cnc-13__cta" type="button">Notify me at launch</button>
      <p class="cnc-13__sr" role="status" aria-live="polite"></p>
    </div>
    <p class="cnc-13__chip" aria-hidden="true">recompute from timestamp · conic ring per unit · threshold-only announcements</p>
  </div>
</section>
```
## CSS
```css
.cnc-13,
.cnc-13 *,
.cnc-13 *::before,
.cnc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-13-bg: oklch(0.17 0.05 285);
  --cnc-13-ink: oklch(0.98 0.005 280);
  --cnc-13-mut: oklch(0.72 0.03 285);
  --cnc-13-acc: oklch(0.78 0.18 195);
  --cnc-13-acc2: oklch(0.66 0.22 305);
  background: var(--cnc-13-bg);
  color: var(--cnc-13-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(70% 60% at 20% 0%,color-mix(in oklch,var(--cnc-13-acc2) 30%,transparent),transparent 65%),radial-gradient(60% 55% at 85% 100%,color-mix(in oklch,var(--cnc-13-acc) 25%,transparent),transparent 65%);
}

.cnc-13__panel {
  width: min(100%,600px);
  padding: clamp(24px,4.5vw,38px);
  border-radius: 26px;
  text-align: center;
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.13);
  -webkit-backdrop-filter: blur(18px);
  backdrop-filter: blur(18px);
  box-shadow: 0 30px 70px oklch(0 0 0/.4);
}

.cnc-13__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--cnc-13-acc);
}

.cnc-13__head {
  margin-top: 8px;
  font-size: clamp(26px,4.6vw,38px);
  font-weight: 700;
  letter-spacing: -.035em;
}

.cnc-13__units {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: clamp(8px,2vw,16px);
  margin-top: 26px;
}

.cnc-13__unit {
  display: grid;
  justify-items: center;
  gap: 9px;
}

.cnc-13__ring {
  position: relative;
  display: grid;
  place-items: center;
  width: 100%;
  max-width: 104px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(var(--cnc-13-acc) calc(var(--cnc-13-p,0) * 360deg),oklch(1 0 0/.09) 0);
  transition: background .35s linear;
}

.cnc-13__ring::before {
  content: "";
  position: absolute;
  inset: 7px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--cnc-13-bg) 88%,black);
}

.cnc-13__n {
  position: relative;
  font-size: clamp(22px,4.6vw,32px);
  font-weight: 750;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-13__unit.is-tick .cnc-13__n {
  animation: cnc-13-tick .4s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-13-tick {
  0% {
    opacity: .25;
    translate: 0 6px;
  }

  100% {
    opacity: 1;
    translate: 0 0;
  }
}

.cnc-13__u {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-13-mut);
}

.cnc-13__when {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--cnc-13-mut);
}

.cnc-13__cta {
  min-height: 48px;
  margin-top: 18px;
  padding: 0 26px;
  border: 0;
  border-radius: 99px;
  background: linear-gradient(100deg,var(--cnc-13-acc),var(--cnc-13-acc2));
  color: oklch(0.16 0.04 280);
  font: inherit;
  font-size: 14.5px;
  font-weight: 700;
  cursor: pointer;
  transition: transform .2s,filter .2s;
}

.cnc-13__cta:hover {
  transform: translateY(-2px);
  filter: brightness(1.08);
}

.cnc-13__cta:focus-visible {
  outline: 3px solid var(--cnc-13-ink);
  outline-offset: 3px;
}

.cnc-13__panel[data-state="done"] .cnc-13__units {
  opacity: .35;
}

.cnc-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-13-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,540px);
}

@media (max-width: 420px) {
  .cnc-13__units {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-13 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cnc-13__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const units = [...panel.querySelectorAll('.cnc-13__unit')];
    const whenEl = panel.querySelector('.cnc-13__when');
    const say = panel.querySelector('.cnc-13__sr');
    // Fixed launch date; rolled forward if it has already passed so the demo never sits at zero.
    let target = Date.parse('2026-11-18T15:00:00Z');
    while (target < Date.now()) target += 27 * 864e5;
    whenEl.textContent = new Intl.DateTimeFormat(undefined, { dateStyle: 'full', timeStyle: 'short' }).format(target);

    const thresholds = [86400, 3600, 600, 60, 0];
    let spoken = new Set();
    const set = (unit, val, frac) => {
      const b = unit.querySelector('.cnc-13__n');
      const txt = String(val).padStart(2, '0');
      unit.style.setProperty('--cnc-13-p', frac.toFixed(4));
      if (b.textContent === txt) return;
      b.textContent = txt;
      unit.classList.remove('is-tick'); void unit.offsetWidth; unit.classList.add('is-tick');
    };
    const tick = () => {
      const ms = Math.max(0, target - Date.now());          // always recomputed, never decremented
      const total = Math.floor(ms / 1000);
      const d = Math.floor(total / 86400), h = Math.floor(total / 3600) % 24, m = Math.floor(total / 60) % 60, s = total % 60;
      set(units[0], d, Math.min(1, d / 30));
      set(units[1], h, h / 24);
      set(units[2], m, m / 60);
      set(units[3], s, s / 60);
      panel.dataset.state = total === 0 ? 'done' : 'live';
      const hit = thresholds.find((t) => total <= t && !spoken.has(t));
      if (hit !== undefined) {
        spoken.add(hit);
        say.textContent = total === 0 ? 'We are live' : d + ' days ' + h + ' hours ' + m + ' minutes remaining until launch';
      }
    };
    tick();
    const id = setInterval(tick, 1000);
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') tick(); });
    panel.querySelector('.cnc-13__cta').addEventListener('click', (e) => {
      e.currentTarget.textContent = 'You are on the list ✓';
      say.textContent = 'You will be notified at launch';
    });
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
