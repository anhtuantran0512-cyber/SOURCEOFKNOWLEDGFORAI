---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/live-visitor-online-user-count-widget/"
title: "Live Visitor / Online User Count Widget"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The \"32 people are viewing this right now\" widget, built the way a real-time product should build it: a per-digit roll so only the digits that changed move,…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Visitor / Online User Count Widget
Source: https://codefronts.com/motion/css-number-counter-animations/live-visitor-online-user-count-widget/

The "32 people are viewing this right now" widget, built the way a real-time product should build it: a per-digit roll so only the digits that changed move, a breathing live dot, a sparkline of the last 30 seconds, and an aria-live region that speaks at most once every ten seconds no matter how often the socket fires.
## HTML
```html
<section class="cnc-07" aria-label="Live visitor count widget demo">
  <div class="cnc-07__stage">
    <div class="cnc-07__widget">
      <header class="cnc-07__top">
        <span class="cnc-07__live"><span class="cnc-07__dot" aria-hidden="true"></span>Live now</span>
        <span class="cnc-07__src">codefronts.com</span>
      </header>
      <p class="cnc-07__count" aria-hidden="true"><span class="cnc-07__digits"></span></p>
      <p class="cnc-07__label">people viewing this page</p>
      <svg class="cnc-07__spark" viewBox="0 0 200 44" preserveAspectRatio="none" aria-hidden="true">
        <polyline class="cnc-07__sparkline" points=""/>
      </svg>
      <footer class="cnc-07__foot">
        <span class="cnc-07__stat"><b class="cnc-07__peak">48</b> peak today</span>
        <span class="cnc-07__stat"><b class="cnc-07__avg">27</b> 24h average</span>
      </footer>
      <p class="cnc-07__sr" role="status" aria-live="polite"></p>
    </div>
    <p class="cnc-07__chip" aria-hidden="true">per-digit translateY strips · unchanged digits untouched · 10s throttled live region</p>
  </div>
</section>
```
## CSS
```css
.cnc-07,
.cnc-07 *,
.cnc-07 *::before,
.cnc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-07-bg: oklch(0.15 0.018 250);
  --cnc-07-card: oklch(0.21 0.022 250);
  --cnc-07-ink: oklch(0.98 0.004 250);
  --cnc-07-mut: oklch(0.66 0.02 250);
  --cnc-07-acc: oklch(0.8 0.16 145);
  background: var(--cnc-07-bg);
  color: var(--cnc-07-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
}

.cnc-07__widget {
  container-type: inline-size;
  width: min(100%,340px);
  padding: 20px;
  border-radius: 20px;
  background: var(--cnc-07-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.08),0 22px 54px oklch(0 0 0/.45);
}

.cnc-07__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-size: 11.5px;
}

.cnc-07__live {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 10px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cnc-07-acc) 15%,transparent);
  color: var(--cnc-07-acc);
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cnc-07__dot {
  position: relative;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
}

.cnc-07__dot::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: currentColor;
  animation: cnc-07-ping 1.8s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes cnc-07-ping {
  0% {
    opacity: .7;
    scale: 1;
  }

  80%,
    100% {
    opacity: 0;
    scale: 3.4;
  }
}

.cnc-07__src {
  color: var(--cnc-07-mut);
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.cnc-07__count {
  margin-top: 18px;
}

.cnc-07__digits {
  display: flex;
  gap: 2px;
  font-size: clamp(48px,13cqw,62px);
  font-weight: 770;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-07__cell {
  position: relative;
  display: block;
  height: 1em;
  overflow: hidden;
}

.cnc-07__strip {
  display: block;
  transform: translateY(var(--cnc-07-y,0));
  transition: transform .55s cubic-bezier(.16,1,.3,1);
}

.cnc-07__strip i {
  display: block;
  height: 1em;
  font-style: normal;
  text-align: center;
}

.cnc-07__label {
  margin-top: 8px;
  font-size: 13.5px;
  color: var(--cnc-07-mut);
}

.cnc-07__spark {
  display: block;
  width: 100%;
  height: 44px;
  margin-top: 14px;
  overflow: visible;
}

.cnc-07__sparkline {
  fill: none;
  stroke: var(--cnc-07-acc);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  vector-effect: non-scaling-stroke;
  opacity: .9;
}

.cnc-07__foot {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid oklch(1 0 0/.09);
  font-size: 12px;
  color: var(--cnc-07-mut);
}

.cnc-07__stat b {
  color: var(--cnc-07-ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

@container (max-width: 260px) {
  .cnc-07__spark,
    .cnc-07__foot {
    display: none;
  }
}

.cnc-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-07-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,420px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-07__dot::after {
    animation: none;
    opacity: 0;
  }

  .cnc-07__strip {
    transition-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cnc-07__widget').forEach((w) => {
    if (w.dataset.wired) return;
    w.dataset.wired = '1';
    const wrap = w.querySelector('.cnc-07__digits');
    const line = w.querySelector('.cnc-07__sparkline');
    const peakEl = w.querySelector('.cnc-07__peak');
    const say = w.querySelector('.cnc-07__sr');
    let n = 31, peak = 48, history = Array.from({ length: 30 }, () => 24 + Math.round(Math.random() * 12)), spoke = 0;

    const buildCells = (len) => {
      wrap.innerHTML = '';
      for (let i = 0; i < len; i++) {
        const cell = document.createElement('span');
        cell.className = 'cnc-07__cell';
        const strip = document.createElement('span');
        strip.className = 'cnc-07__strip';
        strip.innerHTML = '0123456789'.split('').map((d) => '<i>' + d + '</i>').join('');
        cell.appendChild(strip);
        wrap.appendChild(cell);
      }
    };

    const setCount = (v) => {
      const s = String(v);
      if (wrap.children.length !== s.length) buildCells(s.length);
      [...s].forEach((d, i) => {
        const cell = wrap.children[i];
        if (cell.dataset.d === d) return;                 // unchanged digit stays put
        cell.dataset.d = d;
        cell.firstChild.style.setProperty('--cnc-07-y', -d * 10 + '%');
      });
      if (v > peak) { peak = v; peakEl.textContent = v; }
      history.push(v); history.shift();
      line.setAttribute('points', history.map((h, i) => (i / (history.length - 1)) * 200 + ',' + (42 - (h / Math.max(...history, 1)) * 38)).join(' '));
      if (performance.now() - spoke > 10000) { say.textContent = v + ' people viewing this page'; spoke = performance.now(); }
    };

    setCount(n);
    const id = setInterval(() => {
      if (document.visibilityState !== 'visible') return;
      n = Math.max(6, n + Math.round((Math.random() - 0.46) * 7));
      setCount(n);
    }, 2200);
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
