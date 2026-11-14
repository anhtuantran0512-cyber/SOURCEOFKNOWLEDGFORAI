---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/empty-dashboard-no-analytics-data/"
title: "Empty Dashboard / No Analytics Data"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A dashboard with no data yet, treated as a wiring problem rather than a void: the chart grid is drawn but desaturated behind a focused connect panel, and…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Empty Dashboard / No Analytics Data
Source: https://codefronts.com/snippets/css-empty-states/empty-dashboard-no-analytics-data/

A dashboard with no data yet, treated as a wiring problem rather than a void: the chart grid is drawn but desaturated behind a focused connect panel, and picking a source brings the whole grid to life &mdash; bars rise, the donut fills, the cohort cells warm up, the sidebar status flips to syncing. No invented numbers anywhere, just axis scaffolding until something real arrives.
## HTML
```html
<div class="est-07">
  <div class="est-07__shell">
    <aside class="est-07__side">
      <span class="est-07__logo">Cadence</span>
      <nav class="est-07__nav">
        <a class="est-07__nl est-07__nl--on" href="#est-07" aria-current="page">Overview</a>
        <a class="est-07__nl" href="#est-07">Funnels</a>
        <a class="est-07__nl" href="#est-07">Retention</a>
        <a class="est-07__nl" href="#est-07">Sources</a>
        <a class="est-07__nl" href="#est-07">Settings</a>
      </nav>
      <div class="est-07__sfoot">
        <span class="est-07__stat" id="est-07-status">No source connected</span>
      </div>
    </aside>

    <main class="est-07__main">
      <header class="est-07__top">
        <h1 class="est-07__h1">Overview</h1>
        <div class="est-07__range" role="group" aria-label="Date range">
          <button class="est-07__rb" type="button">24h</button>
          <button class="est-07__rb est-07__rb--on" type="button">7d</button>
          <button class="est-07__rb" type="button">30d</button>
          <button class="est-07__rb" type="button">Quarter</button>
        </div>
      </header>

      <section class="est-07__grid" id="est-07-grid">
        <article class="est-07__card est-07__card--wide">
          <p class="est-07__ct">Sessions</p>
          <div class="est-07__plot" aria-hidden="true">
            <span class="est-07__axis"></span>
            <span class="est-07__base"></span>
            <span class="est-07__ticks"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
          </div>
        </article>
        <article class="est-07__card">
          <p class="est-07__ct">Conversion</p>
          <div class="est-07__donut" aria-hidden="true"></div>
        </article>
        <article class="est-07__card">
          <p class="est-07__ct">Top channels</p>
          <div class="est-07__bars" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
        </article>
        <article class="est-07__card est-07__card--wide">
          <p class="est-07__ct">Retention cohorts</p>
          <div class="est-07__cells" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
        </article>
      </section>

      <div class="est-07__overlay" id="est-07-overlay">
        <div class="est-07__panel" id="est-07-panel">
          <span class="est-07__pulse" aria-hidden="true"></span>
          <h2 class="est-07__ph" id="est-07-ph">Nothing to chart yet</h2>
          <p class="est-07__pp" id="est-07-pp">Connect a source and the first events land in about a minute. Charts fill in as they arrive.</p>
          <div class="est-07__pacts" id="est-07-pacts">
            <button class="est-07__pri" type="button" id="est-07-connect">Connect a source</button>
            <button class="est-07__ghost" type="button">Paste a tracking snippet</button>
          </div>
          <ul class="est-07__sources" id="est-07-sources" hidden>
            <li><button class="est-07__src" type="button" data-src="Postgres">Postgres</button></li>
            <li><button class="est-07__src" type="button" data-src="Stripe">Stripe</button></li>
            <li><button class="est-07__src" type="button" data-src="Segment">Segment</button></li>
            <li><button class="est-07__src" type="button" data-src="Webhook">Webhook</button></li>
          </ul>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-07 {
  --bg: #0a0d0c;
  --panel: #111614;
  --panel-2: #16201c;
  --line: #1e2a25;
  --line-2: #2a3a33;
  --text: #eaf2ee;
  --muted: #93a49c;
  --faint: #66776f;
  --accent: #8ee6a8;
  --amber: #e8c37a;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--text);
  color-scheme: dark;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-07 *,
.est-07 *::before,
.est-07 *::after {
  box-sizing: border-box;
}

.est-07 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-07 {
    --bg: oklch(0.155 0.009 165);
    --panel: oklch(0.195 0.012 165);
    --panel-2: oklch(0.235 0.016 165);
    --line: oklch(0.275 0.016 165);
    --line-2: oklch(0.335 0.019 165);
    --text: oklch(0.96 0.01 165);
    --muted: oklch(0.73 0.021 165);
    --faint: oklch(0.575 0.021 165);
    --accent: oklch(0.86 0.115 155);
    --amber: oklch(0.84 0.09 85);
  }
}

.est-07__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(14rem,22vw) minmax(0,1fr);
}

.est-07__side {
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  gap: 1.25rem;
  padding: 1.15rem .9rem;
  border-inline-end: 1px solid var(--line);
  background: linear-gradient(180deg,var(--panel),var(--bg));
}

.est-07__logo {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.02em;
  padding-inline: .35rem;
}

.est-07__nav {
  display: grid;
  gap: .1rem;
  align-content: start;
}

.est-07__nl {
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: color .16s, background .16s;
}

.est-07__nl:hover {
  color: var(--text);
  background: var(--panel-2);
}

.est-07__nl--on {
  color: var(--text);
  background: var(--panel-2);
  box-shadow: inset 0 0 0 1px var(--line-2);
}

.est-07__sfoot {
  padding: .65rem .7rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--panel);
}

.est-07__stat {
  display: flex;
  align-items: center;
  gap: .45rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  letter-spacing: .02em;
  color: var(--faint);
}

.est-07__stat::before {
  content: '';
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 50%;
  background: var(--faint);
}

.est-07__stat[data-live] {
  color: var(--accent);
}

.est-07__stat[data-live]::before {
  background: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--accent) 20%, transparent);
  animation: est-07-blink 2s ease-in-out infinite;
}

@keyframes est-07-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.est-07__main {
  position: relative;
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  align-content: start;
}

.est-07__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding: 1.05rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
}

.est-07__h1 {
  margin: 0;
  font-size: clamp(1.15rem,2.6vw,1.5rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.est-07__range {
  display: flex;
  gap: .15rem;
  padding: .2rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px;
}

.est-07__rb {
  padding: .38rem .7rem;
  font: inherit;
  font-size: .78rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--muted);
  background: transparent;
  border: 0;
  border-radius: 7px;
  transition: color .16s, background .16s;
}

.est-07__rb:hover {
  color: var(--text);
}

.est-07__rb--on {
  color: var(--bg);
  background: var(--accent);
}

.est-07__grid {
  padding: clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1rem;
  align-content: start;
  grid-template-columns: repeat(auto-fit,minmax(min(15rem,100%),1fr));
  filter: saturate(.6);
  opacity: .5;
  transition: opacity .6s ease, filter .6s ease;
}

.est-07__grid[data-live] {
  opacity: 1;
  filter: none;
}

.est-07__card {
  display: grid;
  gap: .9rem;
  align-content: start;
  padding: 1rem 1.1rem 1.15rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  min-block-size: 11rem;
}

.est-07__card--wide {
  grid-column: span 2;
}

.est-07__ct {
  margin: 0;
  font-size: .82rem;
  font-weight: 500;
  color: var(--muted);
}

.est-07__plot {
  position: relative;
  block-size: 7rem;
}

.est-07__axis {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 1px;
  background: var(--line-2);
}

.est-07__base {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  block-size: 1px;
  background: var(--line-2);
}

.est-07__plot::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(180deg, var(--line) 0 1px, transparent 1px 25%);
  opacity: .7;
}

.est-07__ticks {
  position: absolute;
  inset-block-end: 0;
  inset-inline: .5rem 0;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  block-size: 100%;
}

.est-07__ticks i {
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 50%;
  background: var(--line-2);
}

.est-07__grid[data-live] .est-07__ticks i {
  block-size: .4rem;
  background: var(--accent);
  animation: est-07-rise 1.4s cubic-bezier(.2,.7,.3,1) both;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(2) {
  align-self: flex-end;
  block-size: 2.2rem;
  inline-size: .4rem;
  border-radius: 3px;
  animation-delay: .05s;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(3) {
  block-size: 3.4rem;
  border-radius: 3px;
  animation-delay: .1s;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(4) {
  block-size: 2.8rem;
  border-radius: 3px;
  animation-delay: .15s;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(5) {
  block-size: 4.6rem;
  border-radius: 3px;
  animation-delay: .2s;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(6) {
  block-size: 3.9rem;
  border-radius: 3px;
  animation-delay: .25s;
}

.est-07__grid[data-live] .est-07__ticks i:nth-child(7) {
  block-size: 5.4rem;
  border-radius: 3px;
  animation-delay: .3s;
}

@keyframes est-07-rise {
  from {
    scale: 1 .05;
    opacity: .2;
  }

  to {
    scale: 1 1;
    opacity: 1;
  }
}

.est-07__donut {
  justify-self: center;
  inline-size: 6.5rem;
  block-size: 6.5rem;
  border-radius: 50%;
  background: conic-gradient(var(--line-2) 0 100%);
  position: relative;
  transition: background .8s ease;
}

.est-07__grid[data-live] .est-07__donut {
  background: conic-gradient(var(--accent) 0 34%, var(--amber) 34% 52%, var(--line-2) 52% 100%);
}

.est-07__donut::after {
  content: '';
  position: absolute;
  inset: 1.15rem;
  border-radius: 50%;
  background: var(--panel);
}

.est-07__bars {
  display: grid;
  gap: .55rem;
  align-content: end;
  block-size: 7rem;
}

.est-07__bars i {
  block-size: .55rem;
  border-radius: 3px;
  background: var(--line-2);
  inline-size: 35%;
  transition: inline-size .9s cubic-bezier(.2,.7,.3,1), background .5s;
}

.est-07__grid[data-live] .est-07__bars i {
  background: color-mix(in oklab, var(--accent) 70%, var(--panel));
}

.est-07__grid[data-live] .est-07__bars i:nth-child(1) {
  inline-size: 88%;
}

.est-07__grid[data-live] .est-07__bars i:nth-child(2) {
  inline-size: 64%;
}

.est-07__grid[data-live] .est-07__bars i:nth-child(3) {
  inline-size: 41%;
}

.est-07__grid[data-live] .est-07__bars i:nth-child(4) {
  inline-size: 22%;
}

.est-07__cells {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: .4rem;
}

.est-07__cells i {
  aspect-ratio: 1;
  border-radius: 4px;
  background: var(--line);
  transition: background .6s;
}

.est-07__grid[data-live] .est-07__cells i:nth-child(3n) {
  background: color-mix(in oklab, var(--accent) 45%, var(--panel));
}

.est-07__grid[data-live] .est-07__cells i:nth-child(4n) {
  background: color-mix(in oklab, var(--accent) 22%, var(--panel));
}

.est-07__overlay {
  position: absolute;
  inset-block-start: 4.5rem;
  inset-inline: 0;
  inset-block-end: 0;
  display: grid;
  place-items: center;
  padding: 1.5rem;
  background: radial-gradient(60% 50% at 50% 45%, color-mix(in oklab, var(--bg) 70%, transparent), color-mix(in oklab, var(--bg) 92%, transparent));
  backdrop-filter: blur(1.5px);
  transition: opacity .45s ease;
}

.est-07__overlay[data-gone] {
  opacity: 0;
  pointer-events: none;
}

.est-07__panel {
  inline-size: min(30rem,100%);
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .55rem;
  padding: clamp(1.5rem,3.5vw,2.25rem);
  background: color-mix(in oklab, var(--panel) 92%, transparent);
  border: 1px solid var(--line-2);
  border-radius: 20px;
  box-shadow: 0 40px 80px -60px #000, inset 0 1px 0 color-mix(in oklab, #fff 5%, transparent);
  animation: est-07-in .5s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-07-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-07__pulse {
  position: relative;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 50%;
  margin-block-end: .35rem;
  background: radial-gradient(circle at 50% 50%, color-mix(in oklab, var(--accent) 85%, transparent) 0 26%, transparent 27%);
}

.est-07__pulse::before,
.est-07__pulse::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid color-mix(in oklab, var(--accent) 45%, transparent);
  animation: est-07-ring 3.4s ease-out infinite;
}

.est-07__pulse::after {
  animation-delay: 1.7s;
}

@keyframes est-07-ring {
  0% {
    scale: .5;
    opacity: .9;
  }

  100% {
    scale: 1.6;
    opacity: 0;
  }
}

.est-07__ph {
  margin: 0;
  font-size: clamp(1.15rem,2.6vw,1.45rem);
  font-weight: 600;
  letter-spacing: -.028em;
  text-wrap: balance;
}

.est-07__pp {
  margin: 0;
  max-inline-size: 38ch;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-07__pacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .85rem;
}

.est-07__pri {
  min-block-size: 2.75rem;
  padding: .65rem 1.05rem;
  font: inherit;
  font-size: .87rem;
  font-weight: 500;
  cursor: pointer;
  color: #08130d;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 11px;
  transition: translate .16s, background .16s;
}

.est-07__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 85%, #fff);
}

.est-07__ghost {
  min-block-size: 2.75rem;
  padding: .65rem 1rem;
  font: inherit;
  font-size: .87rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--text);
  background: var(--panel-2);
  border: 1px solid var(--line-2);
  border-radius: 11px;
  transition: background .16s;
}

.est-07__ghost:hover {
  background: var(--line);
}

.est-07__sources {
  margin: .85rem 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(7rem,1fr));
  gap: .4rem;
  inline-size: 100%;
}

.est-07__src {
  inline-size: 100%;
  min-block-size: 2.6rem;
  padding: .55rem .7rem;
  cursor: pointer;
  font: inherit;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .76rem;
  color: var(--text);
  background: var(--panel-2);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: border-color .16s, background .16s;
}

.est-07__src:hover {
  border-color: var(--accent);
  background: var(--line);
}

.est-07__pri:focus-visible,
.est-07__ghost:focus-visible,
.est-07__src:focus-visible,
.est-07__rb:focus-visible,
.est-07__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 900px) {
  .est-07__shell {
    grid-template-columns: 1fr;
  }

  .est-07__side {
    grid-template-rows: auto;
    grid-template-columns: auto minmax(0,1fr) auto;
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-07__nav {
    display: none;
  }

  .est-07__card--wide {
    grid-column: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-07 *,
    .est-07 *::before,
    .est-07 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-07__panel,
    .est-07__card,
    .est-07__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-07'); if(!root) return;
  var connect = root.querySelector('#est-07-connect'), sources = root.querySelector('#est-07-sources'),
      overlay = root.querySelector('#est-07-overlay'), grid = root.querySelector('#est-07-grid'),
      ph = root.querySelector('#est-07-ph'), pp = root.querySelector('#est-07-pp'),
      pacts = root.querySelector('#est-07-pacts'), status = root.querySelector('#est-07-status');
  connect.addEventListener('click', function(){
    sources.hidden = false;
    ph.textContent = 'Pick a source';
    pp.textContent = 'Read-only credentials are enough. You can add more later.';
    pacts.hidden = true;
  });
  sources.addEventListener('click', function(e){
    var b = e.target.closest('[data-src]'); if(!b) return;
    status.textContent = b.dataset.src + ' syncing';
    status.setAttribute('data-live','');
    ph.textContent = 'First events arriving';
    pp.textContent = b.dataset.src + ' is connected. Charts fill in as the backfill lands.';
    sources.hidden = true;
    setTimeout(function(){
      grid.setAttribute('data-live','');
      overlay.setAttribute('data-gone','');
    }, 700);
  });
})();
```
