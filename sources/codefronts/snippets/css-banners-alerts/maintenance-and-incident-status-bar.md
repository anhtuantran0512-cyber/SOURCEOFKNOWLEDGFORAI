---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/maintenance-and-incident-status-bar/"
title: "Maintenance and Incident Status Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A status bar that a real on-call engineer could ship: four severity levels driven entirely by data-severity, a component-scoped update timeline that expands…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Maintenance and Incident Status Bar
Source: https://codefronts.com/snippets/css-banners-alerts/maintenance-and-incident-status-bar/

A status bar that a real on-call engineer could ship: four severity levels driven entirely by data-severity, a component-scoped update timeline that expands in place, per-service health rows, and an aria-live region that speaks once per state change instead of on every repaint. Change one attribute and the palette, icon, label and pulse all follow.
## HTML
```html
<div class="ba-05">
  <div class="ba-05__bar" data-bar data-severity="major" role="region" aria-labelledby="ba-05-h">
    <div class="ba-05__main">
      <span class="ba-05__dot" aria-hidden="true"></span>
      <div class="ba-05__copy">
        <p class="ba-05__h" id="ba-05-h">
          <span class="ba-05__chip" data-label>Major outage</span>
          <span class="ba-05__msg" data-msg>API writes are failing in eu-west-1. Reads and the dashboard are unaffected.</span>
        </p>
        <p class="ba-05__stamp">
          Updated <time datetime="2026-08-10T09:12:00Z" data-time>09:12 UTC</time>
          <span aria-hidden="true">·</span> Next update by <time datetime="2026-08-10T09:45:00Z">09:45 UTC</time>
        </p>
      </div>
    </div>

    <div class="ba-05__acts">
      <div class="ba-05__switch" role="group" aria-label="Simulate incident severity">
        <button type="button" data-sev="operational">Operational</button>
        <button type="button" data-sev="maintenance">Maintenance</button>
        <button type="button" data-sev="degraded">Degraded</button>
        <button type="button" data-sev="major" aria-pressed="true">Major</button>
      </div>
      <button class="ba-05__sub" type="button" data-sub>Subscribe</button>
    </div>

    <details class="ba-05__log">
      <summary>
        <span>Incident timeline</span>
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m4 6.2 4 4 4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </summary>
      <ol class="ba-05__timeline">
        <li data-phase="monitoring"><p class="ba-05__tHead">Monitoring <time datetime="2026-08-10T09:12:00Z">09:12</time></p><p>Failover to the standby cluster completed. Write latency is back inside SLO; we are watching replication lag.</p></li>
        <li data-phase="identified"><p class="ba-05__tHead">Identified <time datetime="2026-08-10T08:54:00Z">08:54</time></p><p>A schema migration exhausted the connection pool on the primary. Migration rolled back.</p></li>
        <li data-phase="investigating"><p class="ba-05__tHead">Investigating <time datetime="2026-08-10T08:41:00Z">08:41</time></p><p>Elevated 5xx on POST endpoints in eu-west-1. Paging the database on-call.</p></li>
      </ol>
    </details>

    <ul class="ba-05__services">
      <li data-health="up"><span aria-hidden="true"></span>Dashboard<b>Operational</b></li>
      <li data-health="down"><span aria-hidden="true"></span>REST API (writes)<b>Outage</b></li>
      <li data-health="up"><span aria-hidden="true"></span>REST API (reads)<b>Operational</b></li>
      <li data-health="warn"><span aria-hidden="true"></span>Webhooks<b>Delayed</b></li>
      <li data-health="up"><span aria-hidden="true"></span>CDN<b>Operational</b></li>
    </ul>
  </div>

  <main class="ba-05__page">
    <h1>Platform</h1>
    <p>Region eu-west-1 · Plan Scale · 14 projects</p>
    <div class="ba-05__cards" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
  </main>
  <p class="ba-05__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

.ba-05 {
  --bg: #08090c;
  --surface: #101319;
  --ink: #eef1f6;
  --muted: #98a0ad;
  --line: #20252e;
  --green: #22c55e;
  --amber: #f59e0b;
  --red: #f04438;
  --blue: #3b82f6;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  container-type: inline-size;
  interpolate-size: allow-keywords;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto 1fr;
  box-sizing: border-box;
  scroll-padding-block-start: 6rem;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-05 *,
.ba-05 *::before,
.ba-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-05 {
    --bg: oklch(14% .012 265);
    --surface: oklch(20% .018 265);
    --ink: oklch(96% .006 265);
    --muted: oklch(71% .02 265);
    --line: oklch(29% .022 265);
    --green: oklch(72% .17 150);
    --amber: oklch(78% .16 78);
    --red: oklch(64% .21 26);
    --blue: oklch(65% .18 255);
  }
}

@media (prefers-color-scheme: light) {
  .ba-05:not([data-theme="dark"]) {
    --bg: #f7f8fa;
    --surface: #ffffff;
    --ink: #0d1016;
    --muted: #5b6472;
    --line: #e4e7ec;
  }
}

.ba-05[data-theme="light"] {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --ink: #0d1016;
  --muted: #5b6472;
  --line: #e4e7ec;
}

.ba-05__bar {
  --sev: var(--red);
  --sevSoft: color-mix(in oklab,var(--sev) 13%,var(--surface));
  position: sticky;
  top: 0;
  z-index: 5;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: .75rem clamp(1rem,3cqw,2rem);
  padding: clamp(.85rem,2vw,1.15rem) clamp(1rem,4vw,2rem);
  background: var(--sevSoft);
  border-block-end: 1px solid color-mix(in oklab,var(--sev) 30%,var(--line));
  box-shadow: 0 1px 0 0 color-mix(in oklab,var(--sev) 40%,transparent), 0 1.5rem 3rem -2rem rgb(0 0 0 / .6);
  transition: background .5s ease, border-color .5s ease;
}

.ba-05__bar[data-severity="operational"] {
  --sev: var(--green);
}

.ba-05__bar[data-severity="maintenance"] {
  --sev: var(--blue);
}

.ba-05__bar[data-severity="degraded"] {
  --sev: var(--amber);
}

.ba-05__bar[data-severity="major"] {
  --sev: var(--red);
}

.ba-05__main {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .85rem;
  align-items: start;
  min-width: 0;
}

.ba-05__dot {
  position: relative;
  display: block;
  width: .7rem;
  height: .7rem;
  margin: .5rem .25rem;
  border-radius: 999px;
  background: var(--sev);
  box-shadow: 0 0 0 .3rem color-mix(in oklab,var(--sev) 22%,transparent);
  flex: none;
}

.ba-05__dot::before,
.ba-05__dot::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  border: 1.5px solid var(--sev);
  animation: ba-05-ping 2.6s cubic-bezier(.2,.6,.3,1) infinite;
}

.ba-05__dot::after {
  animation-delay: 1.3s;
}

@keyframes ba-05-ping {
  0% {
    scale: 1;
    opacity: .7;
  }

  80%,
    100% {
    scale: 3.4;
    opacity: 0;
  }
}

.ba-05__bar[data-severity="operational"] .ba-05__dot::before,
.ba-05__bar[data-severity="operational"] .ba-05__dot::after {
  animation: none;
  opacity: 0;
}

.ba-05__copy {
  min-width: 0;
  display: grid;
  gap: .3rem;
}

.ba-05__h {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .6rem;
  flex-wrap: wrap;
  min-width: 0;
}

.ba-05__chip {
  flex: none;
  font-family: var(--mono);
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .28rem .5rem;
  border-radius: .4rem;
  color: var(--sev);
  background: color-mix(in oklab,var(--sev) 16%,transparent);
  border: 1px solid color-mix(in oklab,var(--sev) 34%,transparent);
}

.ba-05__msg {
  font-size: clamp(.8125rem,1.7cqw,.9375rem);
  line-height: 1.5;
  letter-spacing: -.012em;
  max-width: 72ch;
  text-wrap: pretty;
}

.ba-05__stamp {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.ba-05__acts {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
  justify-content: end;
}

.ba-05__switch {
  display: flex;
  padding: .2rem;
  gap: .15rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  border: 1px solid var(--line);
}

.ba-05__switch button {
  min-height: 2.25rem;
  padding: .4rem .65rem;
  border: 0;
  border-radius: .6rem;
  cursor: pointer;
  font: inherit;
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--muted);
  background: transparent;
  transition: color .2s ease, background .2s ease;
}

.ba-05__switch button:hover {
  color: var(--ink);
}

.ba-05__switch button[aria-pressed="true"] {
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 1px 0 rgb(255 255 255 / .06) inset;
}

.ba-05__sub {
  min-height: 2.25rem;
  padding: .45rem .9rem;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-size: .75rem;
  font-weight: 700;
  color: var(--sev);
  background: transparent;
  border: 1px solid color-mix(in oklab,var(--sev) 40%,transparent);
  transition: background .2s ease;
}

.ba-05__sub:hover {
  background: color-mix(in oklab,var(--sev) 14%,transparent);
}

.ba-05__sub[data-on]::after {
  content: " ✓";
}

.ba-05__log {
  grid-column: 1 / -1;
  border-block-start: 1px solid var(--line);
  margin-block-start: .25rem;
}

.ba-05__log summary {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: .5rem 0;
  cursor: pointer;
  list-style: none;
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
}

.ba-05__log summary::-webkit-details-marker {
  display: none;
}

.ba-05__log summary:hover {
  color: var(--ink);
}

.ba-05__log summary svg {
  width: .9rem;
  height: .9rem;
  transition: rotate .3s ease;
}

.ba-05__log[open] summary svg {
  rotate: 180deg;
}

.ba-05__log::details-content {
  block-size: 0;
  overflow: clip;
  opacity: 0;
  transition: block-size .4s cubic-bezier(.16,1,.3,1), opacity .3s ease, content-visibility .4s allow-discrete;
}

.ba-05__log[open]::details-content {
  block-size: auto;
  opacity: 1;
}

.ba-05__timeline {
  margin: 0 0 .75rem;
  padding: 0 0 0 1.1rem;
  list-style: none;
  display: grid;
  gap: .85rem;
  max-block-size: 14rem;
  overflow: auto;
  overscroll-behavior: contain;
  border-inline-start: 2px solid color-mix(in oklab,var(--sev) 35%,var(--line));
}

.ba-05__timeline li {
  position: relative;
  padding-inline-start: .35rem;
}

.ba-05__timeline li::before {
  content: "";
  position: absolute;
  inset-inline-start: -1.55rem;
  inset-block-start: .35rem;
  width: .55rem;
  height: .55rem;
  border-radius: 999px;
  background: var(--sev);
  box-shadow: 0 0 0 3px var(--sevSoft);
}

.ba-05__timeline li[data-phase="investigating"]::before {
  background: var(--muted);
}

.ba-05__tHead {
  margin: 0 0 .2rem;
  display: flex;
  gap: .5rem;
  align-items: baseline;
  font-family: var(--mono);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sev);
}

.ba-05__tHead time {
  color: var(--muted);
  letter-spacing: 0;
  font-variant-numeric: tabular-nums;
}

.ba-05__timeline p:last-child {
  margin: 0;
  font-size: .8125rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 70ch;
  text-wrap: pretty;
}

.ba-05__services {
  grid-column: 1 / -1;
  margin: 0;
  padding: .65rem 0 0;
  list-style: none;
  display: grid;
  gap: .35rem .9rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  border-block-start: 1px solid var(--line);
}

.ba-05__services li {
  display: flex;
  align-items: center;
  gap: .45rem;
  font-size: .75rem;
  color: var(--muted);
}

.ba-05__services li b {
  margin-inline-start: auto;
  font-weight: 600;
  font-size: .6875rem;
  color: var(--muted);
}

.ba-05__services span {
  width: .45rem;
  height: .45rem;
  border-radius: 999px;
  flex: none;
  background: var(--green);
}

.ba-05__services li[data-health="warn"] span {
  background: var(--amber);
}

.ba-05__services li[data-health="down"] span {
  background: var(--red);
}

.ba-05__services li[data-health="down"] b {
  color: var(--red);
}

.ba-05__services li[data-health="warn"] b {
  color: var(--amber);
}

.ba-05__page {
  padding: clamp(1.5rem,5vw,3rem) clamp(1rem,4vw,2rem);
  display: grid;
  gap: .6rem;
  align-content: start;
}

.ba-05__page h1 {
  margin: 0;
  font-size: clamp(1.5rem,4cqw,2.25rem);
  font-weight: 600;
  letter-spacing: -.04em;
}

.ba-05__page p {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}

.ba-05__cards {
  display: grid;
  gap: .85rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
  margin-block-start: 1rem;
}

.ba-05__cards span {
  display: block;
  height: clamp(5rem,12vh,8rem);
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: var(--surface);
}

.ba-05 :focus-visible {
  outline: 2px solid var(--sev,var(--blue));
  outline-offset: 2px;
}

.ba-05__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 52rem) {
  .ba-05__bar {
    grid-template-columns: 1fr;
  }

  .ba-05__acts {
    justify-content: start;
  }

  .ba-05__switch {
    flex-wrap: wrap;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-05 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-05__bar {
    border: 1px solid CanvasText;
  }

  .ba-05__dot {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-05');
  if (!root) return;
  const bar = root.querySelector('[data-bar]');
  const live = root.querySelector('.ba-05__live');
  const rtf = new Intl.RelativeTimeFormat('en', { numeric: 'auto' });

  const STATES = {
    operational: { label: 'All systems normal', msg: 'No incidents in the last 7 days. Scheduled maintenance window opens Sunday 02:00 UTC.', health: ['up', 'up', 'up', 'up', 'up'] },
    maintenance: { label: 'Maintenance', msg: 'Planned database upgrade in eu-west-1. Writes pause for up to 4 minutes.', health: ['up', 'warn', 'up', 'warn', 'up'] },
    degraded: { label: 'Degraded', msg: 'Webhook delivery is running 6-9 minutes behind. Retries are queued, nothing is dropped.', health: ['up', 'up', 'up', 'warn', 'up'] },
    major: { label: 'Major outage', msg: 'API writes are failing in eu-west-1. Reads and the dashboard are unaffected.', health: ['up', 'down', 'up', 'warn', 'up'] },
  };

  const apply = (key) => {
    if (bar.dataset.severity === key) return;
    const s = STATES[key];
    bar.dataset.severity = key;
    root.querySelector('[data-label]').textContent = s.label;
    root.querySelector('[data-msg]').textContent = s.msg;
    [...root.querySelectorAll('.ba-05__services li')].forEach((li, i) => {
      li.dataset.health = s.health[i];
      li.querySelector('b').textContent = { up: 'Operational', warn: 'Delayed', down: 'Outage' }[s.health[i]];
    });
    root.querySelectorAll('[data-sev]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.sev === key)));
    live.textContent = 'Status changed to ' + s.label + '. ' + s.msg;
  };

  const stamp = () => {
    const t = root.querySelector('[data-time]');
    const mins = Math.round((Date.now() - new Date(t.dateTime)) / 60000);
    t.textContent = Math.abs(mins) < 60 ? rtf.format(-mins, 'minute') : rtf.format(-Math.round(mins / 60), 'hour');
  };

  root.addEventListener('click', (e) => {
    const sev = e.target.closest('[data-sev]');
    if (sev) apply(sev.dataset.sev);
    const sub = e.target.closest('[data-sub]');
    if (sub) { sub.toggleAttribute('data-on'); sub.textContent = sub.hasAttribute('data-on') ? 'Subscribed' : 'Subscribe'; }
  });
  stamp(); setInterval(stamp, 30000);
})();
```
