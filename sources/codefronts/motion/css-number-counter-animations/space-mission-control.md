---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/space-mission-control/"
title: "Mission Telemetry & Countdown Control Panel"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A launch console: a tenth-of-a-second T-minus clock, live velocity, altitude and downrange readouts, a conic-gradient throttle dial and a flight-event…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mission Telemetry & Countdown Control Panel
Source: https://codefronts.com/motion/css-number-counter-animations/space-mission-control/

A launch console: a tenth-of-a-second T-minus clock, live velocity, altitude and downrange readouts, a conic-gradient throttle dial and a flight-event sequencer — every number derived from one authoritative clock. It is the reference implementation for any long-running counter, because the naive version (add 100 ms every 100 ms) drifts by seconds over a flight and looks broken next to a real timer.
## HTML
```html
<section class="cnc-25" aria-label="Mission telemetry and countdown control panel demo">
  <div class="cnc-25__stage">
    <div class="cnc-25__panel" data-phase="hold">
      <header class="cnc-25__head">
        <p class="cnc-25__mission">Vector-9 · demo flight <span>sample telemetry</span></p>
        <span class="cnc-25__state"><i aria-hidden="true"></i><b class="cnc-25__statet">Terminal count</b></span>
      </header>
      <div class="cnc-25__clock">
        <span class="cnc-25__sign" aria-hidden="true">T−</span>
        <time class="cnc-25__t" datetime="PT10S" aria-hidden="true">00:00:10.0</time>
      </div>
      <p class="cnc-25__clocklab">Mission elapsed time</p>
      <div class="cnc-25__cols">
        <dl class="cnc-25__tel">
          <div><dt>Velocity</dt><dd><span class="cnc-25__vel">0</span><small>m/s</small></dd></div>
          <div><dt>Altitude</dt><dd><span class="cnc-25__alt">0.0</span><small>km</small></dd></div>
          <div><dt>Downrange</dt><dd><span class="cnc-25__dr">0.0</span><small>km</small></dd></div>
          <div><dt>Dynamic pressure</dt><dd><span class="cnc-25__q">0</span><small>kPa</small></dd></div>
        </dl>
        <div class="cnc-25__gaugewrap">
          <div class="cnc-25__gauge" role="meter" aria-label="Main engine throttle" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
            <span class="cnc-25__gaugev"><b class="cnc-25__thr">0</b><small>%</small></span>
          </div>
          <p class="cnc-25__gaugelab">Throttle</p>
        </div>
      </div>
      <div class="cnc-25__fuel">
        <p class="cnc-25__fuellab">LOX <b class="cnc-25__lox">100</b>%</p>
        <div class="cnc-25__bar"><span class="cnc-25__loxb"></span></div>
        <p class="cnc-25__fuellab">RP-1 <b class="cnc-25__rp">100</b>%</p>
        <div class="cnc-25__bar"><span class="cnc-25__rpb"></span></div>
      </div>
      <ol class="cnc-25__seq">
        <li data-at="-6">Ignition</li><li data-at="0">Liftoff</li><li data-at="52">Max-Q</li>
        <li data-at="96">MECO</li><li data-at="104">Stage sep</li>
      </ol>
      <div class="cnc-25__ctrl">
        <button class="cnc-25__btn" type="button" data-hold aria-pressed="false">Hold count</button>
        <button class="cnc-25__btn cnc-25__btn--ghost" type="button" data-recycle>Recycle to T−10</button>
      </div>
      <p class="cnc-25__sr" role="status" aria-live="polite"></p>
    </div>
    <p class="cnc-25__chip" aria-hidden="true">timestamp-derived clock (no drift) · 10 Hz telemetry writes · @property &lt;angle&gt; conic dial</p>
  </div>
</section>
```
## CSS
```css
.cnc-25,
.cnc-25 *,
.cnc-25 *::before,
.cnc-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cnc-25-ang {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cnc-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-25-bg: oklch(0.14 0.02 250);
  --cnc-25-card: oklch(0.19 0.025 250);
  --cnc-25-ink: oklch(0.97 0.008 220);
  --cnc-25-mut: oklch(0.67 0.02 230);
  --cnc-25-acc: oklch(0.84 0.16 190);
  --cnc-25-warn: oklch(0.80 0.16 75);
  --cnc-25-mono: ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  background: var(--cnc-25-bg);
  color: var(--cnc-25-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-25__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(14px,3.5vw,40px);
  background: linear-gradient(oklch(1 0 0/.028) 1px,transparent 1px) 0 0/100% 34px,radial-gradient(80% 60% at 50% 0%,color-mix(in oklch,var(--cnc-25-acc) 12%,transparent),transparent 65%);
}

.cnc-25__panel {
  width: min(100%,720px);
  padding: clamp(18px,3.4vw,26px);
  border-radius: 20px;
  background: var(--cnc-25-card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.09),0 30px 70px oklch(0 0 0/.55);
}

.cnc-25__head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cnc-25__mission {
  font-family: var(--cnc-25-mono);
  font-size: 11.5px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--cnc-25-mut);
}

.cnc-25__mission span {
  padding-left: 8px;
  color: color-mix(in oklch,var(--cnc-25-mut) 70%,transparent);
}

.cnc-25__state {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 11px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cnc-25-warn);
  background: color-mix(in oklch,var(--cnc-25-warn) 14%,transparent);
}

.cnc-25__panel[data-phase="flight"] .cnc-25__state {
  color: var(--cnc-25-acc);
  background: color-mix(in oklch,var(--cnc-25-acc) 14%,transparent);
}

.cnc-25__state i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
  animation: cnc-25-blink 1.6s steps(1,end) infinite;
}

@keyframes cnc-25-blink {
  0%,
    60% {
    opacity: 1;
  }

  61%,
    100% {
    opacity: .25;
  }
}

.cnc-25__clock {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-top: 18px;
  font-family: var(--cnc-25-mono);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-25__sign {
  font-size: clamp(22px,4.4vw,30px);
  font-weight: 700;
  color: var(--cnc-25-mut);
}

.cnc-25__t {
  font-size: clamp(34px,8.4vw,58px);
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1;
  text-shadow: 0 0 26px color-mix(in oklch,var(--cnc-25-acc) 40%,transparent);
}

.cnc-25__clocklab {
  margin-top: 7px;
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-25-mut);
}

.cnc-25__cols {
  display: grid;
  grid-template-columns: 1fr;
  gap: 18px;
  margin-top: 20px;
  padding-top: 18px;
  border-top: 1px solid oklch(1 0 0/.09);
}

@media (min-width: 560px) {
  .cnc-25__cols {
    grid-template-columns: 1fr auto;
  }
}

.cnc-25__tel {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px 18px;
  align-content: start;
}

.cnc-25__tel dt {
  font-size: 10.5px;
  font-weight: 660;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cnc-25-mut);
}

.cnc-25__tel dd {
  margin-top: 4px;
  font-family: var(--cnc-25-mono);
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-25__tel dd small {
  font-size: .52em;
  font-weight: 600;
  color: var(--cnc-25-mut);
  margin-left: 4px;
}

.cnc-25__gaugewrap {
  display: grid;
  justify-items: center;
  gap: 8px;
}

.cnc-25__gauge {
  --cnc-25-ang: 0deg;
  position: relative;
  display: grid;
  place-items: center;
  width: 126px;
  height: 126px;
  border-radius: 50%;
  background: conic-gradient(from 225deg,var(--cnc-25-acc) var(--cnc-25-ang),oklch(1 0 0/.09) 0 270deg,transparent 0);
  -webkit-mask: radial-gradient(farthest-side,transparent 62%,#000 64%);
  mask: radial-gradient(farthest-side,transparent 62%,#000 64%);
  transition: --cnc-25-ang .6s cubic-bezier(.16,1,.3,1);
}

.cnc-25__gaugev {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  justify-items: center;
  -webkit-mask: none;
  mask: none;
  font-family: var(--cnc-25-mono);
  font-variant-numeric: tabular-nums;
}

.cnc-25__gaugev b {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -.03em;
}

.cnc-25__gaugev small {
  font-size: 11px;
  color: var(--cnc-25-mut);
}

.cnc-25__gaugelab {
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-25-mut);
}

.cnc-25__fuel {
  display: grid;
  grid-template-columns: auto 1fr auto 1fr;
  align-items: center;
  gap: 8px 12px;
  margin-top: 20px;
}

.cnc-25__fuellab {
  font-family: var(--cnc-25-mono);
  font-size: 11px;
  letter-spacing: .06em;
  color: var(--cnc-25-mut);
  white-space: nowrap;
}

.cnc-25__fuellab b {
  color: var(--cnc-25-ink);
  font-variant-numeric: tabular-nums;
}

.cnc-25__bar {
  height: 7px;
  border-radius: 99px;
  background: oklch(1 0 0/.1);
  overflow: hidden;
}

.cnc-25__bar span {
  display: block;
  height: 100%;
  width: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--cnc-25-acc),color-mix(in oklch,var(--cnc-25-acc) 55%,var(--cnc-25-warn)));
  transform-origin: left;
  transition: width .4s linear;
}

.cnc-25__seq {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 20px;
}

.cnc-25__seq li {
  padding: 6px 11px;
  border-radius: 6px;
  font-family: var(--cnc-25-mono);
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--cnc-25-mut);
  background: oklch(1 0 0/.05);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.06);
  transition: color .3s,background .3s,box-shadow .3s;
}

.cnc-25__seq li[data-state="done"] {
  color: color-mix(in oklch,var(--cnc-25-acc) 70%,var(--cnc-25-mut));
}

.cnc-25__seq li[data-state="active"] {
  color: oklch(0.16 0.02 250);
  background: var(--cnc-25-acc);
  box-shadow: 0 0 22px color-mix(in oklch,var(--cnc-25-acc) 45%,transparent);
}

.cnc-25__ctrl {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 22px;
}

.cnc-25__btn {
  flex: 1 1 auto;
  min-height: 46px;
  padding: 12px 18px;
  border: 0;
  border-radius: 12px;
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .04em;
  color: oklch(0.15 0.02 250);
  background: var(--cnc-25-acc);
  cursor: pointer;
  transition: filter .18s,transform .16s;
}

.cnc-25__btn:hover {
  filter: brightness(1.08);
}

.cnc-25__btn:active {
  transform: scale(.97);
}

.cnc-25__btn:focus-visible {
  outline: 3px solid var(--cnc-25-ink);
  outline-offset: 3px;
}

.cnc-25__btn[aria-pressed="true"] {
  background: var(--cnc-25-warn);
}

.cnc-25__btn--ghost {
  flex: 0 1 auto;
  background: transparent;
  color: var(--cnc-25-mut);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.16);
}

.cnc-25__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-25__chip {
  font-family: var(--cnc-25-mono);
  font-size: 11.5px;
  color: var(--cnc-25-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,620px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-25 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const EVENTS = [[-6, 'Ignition'], [0, 'Liftoff'], [52, 'Max-Q'], [96, 'MECO'], [104, 'Stage sep']];
  const ACCEL = 26;                       // m/s² average, demo profile
  const pad = (n, w) => String(Math.floor(n)).padStart(w, '0');

  document.querySelectorAll('.cnc-25__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const q = (s) => panel.querySelector(s);
    const el = { t: q('.cnc-25__t'), sign: q('.cnc-25__sign'), vel: q('.cnc-25__vel'), alt: q('.cnc-25__alt'),
      dr: q('.cnc-25__dr'), qq: q('.cnc-25__q'), thr: q('.cnc-25__thr'), gauge: q('.cnc-25__gauge'),
      lox: q('.cnc-25__lox'), loxb: q('.cnc-25__loxb'), rp: q('.cnc-25__rp'), rpb: q('.cnc-25__rpb'),
      state: q('.cnc-25__statet'), sr: q('.cnc-25__sr'), hold: q('[data-hold]') };
    const seq = [...panel.querySelectorAll('.cnc-25__seq li')];

    let t0 = performance.now() + 10000;   // T-0 is ten seconds from now
    let heldMs = 0, holdAt = 0, raf = 0, lastSlow = 0, announced = -Infinity;

    const throttleAt = (t) => t < -6 ? 0 : t < 0 ? 62 : t < 44 ? 100 : t < 62 ? 68 : t < 96 ? 100 : 0;

    const paint = (now) => {
      const t = (now - t0 - heldMs) / 1000;                 // seconds relative to T-0 — never accumulated
      const a = Math.abs(t);
      el.sign.textContent = t < 0 ? 'T−' : 'T+';
      el.t.textContent = pad(a / 3600, 2) + ':' + pad((a / 60) % 60, 2) + ':' + pad(a % 60, 2) + '.' + Math.floor((a % 1) * 10);
      el.t.dateTime = 'PT' + a.toFixed(1) + 'S';

      if (now - lastSlow > 100) {                            // telemetry at 10 Hz, clock at 60
        lastSlow = now;
        const ft = Math.max(0, t);
        const v = ACCEL * ft, alt = 0.5 * ACCEL * ft * ft / 1000, thr = throttleAt(t);
        el.vel.textContent = Math.round(v).toLocaleString('en-US');
        el.alt.textContent = alt.toFixed(1);
        el.dr.textContent = (alt * 0.72 * Math.min(1, ft / 40)).toFixed(1);
        el.qq.textContent = Math.round(Math.max(0, 34 * Math.exp(-Math.pow((ft - 52) / 26, 2))));
        el.thr.textContent = thr;
        el.gauge.style.setProperty('--cnc-25-ang', (thr / 100 * 270) + 'deg');
        el.gauge.setAttribute('aria-valuenow', thr);
        const fuel = Math.max(0, 100 - ft * 0.9);
        el.lox.textContent = Math.round(fuel); el.loxb.style.width = fuel + '%';
        el.rp.textContent = Math.round(Math.max(0, fuel - 3)); el.rpb.style.width = Math.max(0, fuel - 3) + '%';
        panel.dataset.phase = t < 0 ? 'hold' : 'flight';
        el.state.textContent = t < -6 ? 'Terminal count' : t < 0 ? 'Ignition sequence' : thr === 0 && t > 90 ? 'Coasting' : 'Powered flight';

        let active = -1;
        EVENTS.forEach((e, i) => { if (t >= e[0]) active = i; });
        seq.forEach((li, i) => { li.dataset.state = i < active ? 'done' : i === active ? 'active' : 'pending'; });
        if (active > -1 && active !== announced) { announced = active; el.sr.textContent = EVENTS[active][1] + ' at T plus ' + Math.round(Math.max(0, t)) + ' seconds.'; }
      }
      raf = requestAnimationFrame(paint);
    };

    el.hold.addEventListener('click', () => {
      const on = el.hold.getAttribute('aria-pressed') !== 'true';
      el.hold.setAttribute('aria-pressed', String(on));
      el.hold.textContent = on ? 'Resume count' : 'Hold count';
      if (on) { holdAt = performance.now(); cancelAnimationFrame(raf); raf = 0; el.state.textContent = 'Count held'; el.sr.textContent = 'Count held.'; }
      else { heldMs += performance.now() - holdAt; raf = requestAnimationFrame(paint); }
    });
    panel.querySelector('[data-recycle]').addEventListener('click', () => {
      t0 = performance.now() + 10000; heldMs = 0; announced = -Infinity;
      if (el.hold.getAttribute('aria-pressed') === 'true') { el.hold.setAttribute('aria-pressed', 'false'); el.hold.textContent = 'Hold count'; }
      if (!raf) raf = requestAnimationFrame(paint);
      el.sr.textContent = 'Recycled to T minus 10 seconds.';
    });
    raf = requestAnimationFrame(paint);
    addEventListener('pagehide', () => cancelAnimationFrame(raf), { once: true });
  });
})();
```
