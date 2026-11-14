---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/usage-limits-quota-meters/"
title: "Usage and Limits Page with Quota Meters"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A usage dashboard that makes plan limits instantly legible: a hero conic-gradient ring for API requests, linear quota bars for seats, storage, bandwidth,…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Usage and Limits Page with Quota Meters
Source: https://codefronts.com/layouts/css-settings-pages/usage-limits-quota-meters/

A usage dashboard that makes plan limits instantly legible: a hero conic-gradient ring for API requests, linear quota bars for seats, storage, bandwidth, build minutes and AI credits, and automatic healthy / warning / over-limit colour states. Meters animate from zero on load with @property, numbers count up with tabular figures, and an upgrade banner appears via :has() the moment any quota goes critical.
## HTML
```html
<section class="csp-03">
  <div class="csp-03__wrap">
    <header class="csp-03__head">
      <div><h1>Usage &amp; limits</h1><p>Pro plan · billing period Oct 1 – Oct 31, 2026 · resets in 24 days</p></div>
      <a class="csp-03__btn" href="#">Upgrade plan</a>
    </header>

    <div class="csp-03__alert" role="alert">
      <strong>You've exceeded a limit.</strong>
      <span>Bandwidth is over quota — overage is billed at $0.08/GB. Upgrade to raise your limits.</span>
    </div>

    <div class="csp-03__grid">
      <article class="csp-03__hero">
        <div class="csp-03__ring" role="meter" aria-label="API requests" data-used="842310" data-limit="1000000" data-unit="" data-meter>
          <div class="csp-03__ringin"><b data-pct>0%</b><small>of monthly quota</small></div>
        </div>
        <div class="csp-03__herotext">
          <span class="csp-03__eyebrow">API requests</span>
          <p class="csp-03__big"><span data-count>0</span> <small>/ 1,000,000</small></p>
          <p class="csp-03__note">Projected to reach ~96% by period end at today's rate.</p>
        </div>
      </article>

      <article class="csp-03__card" role="meter" aria-label="Seats" data-used="8" data-limit="10" data-meter>
        <div class="csp-03__top"><span>Seats</span><span class="csp-03__state"></span></div>
        <p class="csp-03__val"><span data-count>0</span> <small>/ 10</small></p>
        <div class="csp-03__bar"><i></i></div>
      </article>
      <article class="csp-03__card" role="meter" aria-label="Storage" data-used="42.6" data-limit="50" data-unit=" GB" data-meter>
        <div class="csp-03__top"><span>Storage</span><span class="csp-03__state"></span></div>
        <p class="csp-03__val"><span data-count>0</span> <small>/ 50 GB</small></p>
        <div class="csp-03__bar"><i></i></div>
      </article>
      <article class="csp-03__card" role="meter" aria-label="Bandwidth" data-used="1.12" data-limit="1" data-unit=" TB" data-meter>
        <div class="csp-03__top"><span>Bandwidth</span><span class="csp-03__state"></span></div>
        <p class="csp-03__val"><span data-count>0</span> <small>/ 1 TB</small></p>
        <div class="csp-03__bar"><i></i></div>
      </article>
      <article class="csp-03__card" role="meter" aria-label="Build minutes" data-used="2140" data-limit="6000" data-meter>
        <div class="csp-03__top"><span>Build minutes</span><span class="csp-03__state"></span></div>
        <p class="csp-03__val"><span data-count>0</span> <small>/ 6,000</small></p>
        <div class="csp-03__bar"><i></i></div>
      </article>
      <article class="csp-03__card" role="meter" aria-label="AI credits" data-used="310" data-limit="2000" data-meter>
        <div class="csp-03__top"><span>AI credits</span><span class="csp-03__state"></span></div>
        <p class="csp-03__val"><span data-count>0</span> <small>/ 2,000</small></p>
        <div class="csp-03__bar"><i></i></div>
      </article>
    </div>

    <label class="csp-03__opt"><input type="checkbox" checked> Email me when any quota reaches 80%</label>
  </div>
</section>
```
## CSS
```css
@property --csp03-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.csp-03,
.csp-03 *,
.csp-03 *::before,
.csp-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-03 {
  --bg: oklch(0.975 0.004 250);
  --surface: #fff;
  --ink: oklch(0.21 0.02 255);
  --muted: oklch(0.5 0.02 255);
  --line: oklch(0.92 0.006 255);
  --track: oklch(0.94 0.006 255);
  --ok: oklch(0.6 0.15 160);
  --warn: oklch(0.72 0.16 70);
  --crit: oklch(0.6 0.21 27);
  --accent: oklch(0.52 0.19 262);
  color-scheme: light;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 24px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-03__wrap {
  max-width: 980px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.csp-03__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
}

.csp-03__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-03__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-03__btn {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  font: 650 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--ink);
  transition: transform .15s;
}

.csp-03__btn:hover {
  transform: translateY(-1px);
}

.csp-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-03__alert {
  display: none;
  flex-wrap: wrap;
  gap: 4px 10px;
  padding: 14px 18px;
  border-radius: 14px;
  font: 400 14px/1.5 system-ui,sans-serif;
  color: oklch(0.38 0.14 27);
  background: oklch(0.96 0.03 27);
  border: 1px solid oklch(0.88 0.07 27);
}

.csp-03:has([data-level="crit"]) .csp-03__alert {
  display: flex;
}

.csp-03__grid {
  display: grid;
  grid-template-columns: repeat(3,minmax(0,1fr));
  gap: 16px;
}

.csp-03__hero,
.csp-03__card {
  --tone: var(--ok);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 1px 2px oklch(0 0 0/.03);
}

[data-level="warn"] {
  --tone: var(--warn);
}

[data-level="crit"] {
  --tone: var(--crit);
}

.csp-03__hero {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  gap: 32px;
  padding: 28px;
}

.csp-03__ring {
  --tone: var(--ok);
  flex: none;
  display: grid;
  place-items: center;
  width: 180px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(var(--tone) calc(min(var(--csp03-p),100) * 1%),var(--track) 0);
  transition: --csp03-p 1.3s cubic-bezier(.2,.8,.2,1);
}

.csp-03__ringin {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 4px;
  width: calc(100% - 28px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: inset 0 0 0 1px var(--line);
}

.csp-03__ringin b {
  font: 750 34px/1 system-ui,sans-serif;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.csp-03__ringin small {
  font: 500 12px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-03__herotext {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
}

.csp-03__eyebrow {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-03__big {
  font: 750 40px/1 system-ui,sans-serif;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.csp-03__big small,
.csp-03__val small {
  font-size: .45em;
  font-weight: 500;
  letter-spacing: 0;
  color: var(--muted);
}

.csp-03__note {
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-03__card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 20px;
}

.csp-03__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  font: 600 14px/1.2 system-ui,sans-serif;
}

.csp-03__state {
  padding: 4px 9px;
  border-radius: 999px;
  font: 650 11.5px/1 system-ui,sans-serif;
  color: var(--tone);
  background: color-mix(in oklab,var(--tone) 12%,transparent);
  font-variant-numeric: tabular-nums;
}

.csp-03__val {
  font: 700 26px/1 system-ui,sans-serif;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.csp-03__bar {
  height: 8px;
  border-radius: 999px;
  background: var(--track);
  overflow: hidden;
}

.csp-03__bar i {
  display: block;
  height: 100%;
  width: calc(min(var(--csp03-p),100) * 1%);
  border-radius: inherit;
  background: var(--tone);
  transition: --csp03-p 1.3s cubic-bezier(.2,.8,.2,1);
}

[data-level="crit"] .csp-03__bar i {
  background: repeating-linear-gradient(-45deg,var(--crit) 0 8px,oklch(0.66 0.2 27) 8px 16px);
}

.csp-03__opt {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  font: 500 14px/1.3 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
}

.csp-03__opt input {
  width: 18px;
  height: 18px;
}

@container (max-width: 760px) {
  .csp-03__grid {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }
}

@container (max-width: 520px) {
  .csp-03__grid {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-03__hero {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-03__ring,
    .csp-03__bar i {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-03');
  var reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  var fmt = function (n, dec) { return n.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }); };

  root.querySelectorAll('[data-meter]').forEach(function (m) {
    var used = parseFloat(m.dataset.used), limit = parseFloat(m.dataset.limit);
    var dec = (m.dataset.used.split('.')[1] || '').length;
    var pct = used / limit * 100;
    var level = pct >= 100 ? 'crit' : pct >= 80 ? 'warn' : 'ok';
    var host = m.closest('.csp-03__hero') || m;
    host.dataset.level = level;
    m.dataset.level = level;
    m.setAttribute('aria-valuemin', 0);
    m.setAttribute('aria-valuemax', limit);
    m.setAttribute('aria-valuenow', used);
    m.setAttribute('aria-valuetext', fmt(used, dec) + (m.dataset.unit || '') + ' of ' + fmt(limit, 0) + (m.dataset.unit || ''));
    var state = host.querySelector('.csp-03__state');
    if (state) state.textContent = level === 'crit' ? 'Over limit' : Math.round(pct) + '% used';

    requestAnimationFrame(function () { requestAnimationFrame(function () { m.style.setProperty('--csp03-p', pct.toFixed(1)); }); });

    var count = host.querySelector('[data-count]'), pctEl = host.querySelector('[data-pct]');
    var t0 = performance.now(), dur = reduce ? 0 : 1300;
    (function tick(now) {
      var k = dur ? Math.min((now - t0) / dur, 1) : 1;
      var e = 1 - Math.pow(1 - k, 3);
      if (count) count.textContent = fmt(used * e, dec);
      if (pctEl) pctEl.textContent = Math.round(pct * e) + '%';
      if (k < 1) requestAnimationFrame(tick);
    })(t0);
  });
})();
```
