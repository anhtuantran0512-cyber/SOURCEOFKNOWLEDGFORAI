---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/failed-to-load-connection-error-state/"
title: "Failed to Load / Connection Error State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "Not a whole-page error &mdash; one panel on a working dashboard that failed to load, which is what actually happens in production."
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Failed to Load / Connection Error State
Source: https://codefronts.com/snippets/css-empty-states/failed-to-load-connection-error-state/

Not a whole-page error &mdash; one panel on a working dashboard that failed to load, which is what actually happens in production. The failed card keeps its header, carries a compact diagnostic row (endpoint, code, attempt) and a retry that walks through loading and into a real chart, while the two panels beside it stay live and untouched so the user can see the blast radius is small.
## HTML
```html
<div class="est-11">
  <div class="est-11__page">
    <header class="est-11__head">
      <div>
        <span class="est-11__eyebrow">Warehouse operations</span>
        <h1 class="est-11__h1">Fulfilment health</h1>
      </div>
      <div class="est-11__hacts">
        <button class="est-11__ghost" type="button">Last 7 days</button>
        <button class="est-11__ghost" type="button">Share</button>
      </div>
    </header>

    <div class="est-11__grid">
      <section class="est-11__panel est-11__panel--tall" id="est-11-panel" data-state="error">
        <header class="est-11__phead">
          <span class="est-11__ptitle">Pick rate by station</span>
          <span class="est-11__ptag" id="est-11-tag">Failed</span>
        </header>

        <div class="est-11__pbody">
          <div class="est-11__error" id="est-11-error">
            <span class="est-11__mark" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4.8 20.5 19H3.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M12 10v4M12 16.4h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            </span>
            <p class="est-11__eh">This panel could not load</p>
            <p class="est-11__ep">The metrics service answered with a gateway error. The rest of the page is live and unaffected.</p>
            <div class="est-11__eacts">
              <button class="est-11__pri" type="button" id="est-11-retry">Try again</button>
              <button class="est-11__ghost est-11__ghost--sm" type="button">Report the outage</button>
            </div>
            <dl class="est-11__diag">
              <div><dt>Endpoint</dt><dd>metrics.pick_rate</dd></div>
              <div><dt>Code</dt><dd>502</dd></div>
              <div><dt>Attempt</dt><dd id="est-11-attempt">1</dd></div>
            </dl>
          </div>

          <div class="est-11__load" id="est-11-load" hidden>
            <span class="est-11__bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></span>
            <p class="est-11__lp">Refetching pick rate</p>
          </div>

          <div class="est-11__ok" id="est-11-ok" hidden>
            <div class="est-11__chart" aria-hidden="true">
              <span style="--h:42%"></span><span style="--h:66%"></span><span style="--h:51%"></span>
              <span style="--h:78%"></span><span style="--h:63%"></span><span style="--h:88%"></span><span style="--h:72%"></span>
            </div>
            <ul class="est-11__legend">
              <li><i data-c="1"></i>Station A &mdash; Aisle 1 to 4</li>
              <li><i data-c="2"></i>Station B &mdash; Aisle 5 to 9</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="est-11__panel">
        <header class="est-11__phead"><span class="est-11__ptitle">Open exceptions</span><span class="est-11__ptag est-11__ptag--ok">Live</span></header>
        <ul class="est-11__list">
          <li><span>Damaged on arrival</span><span class="est-11__lv">Aisle 6</span></li>
          <li><span>Barcode unreadable</span><span class="est-11__lv">Aisle 2</span></li>
          <li><span>Short pick</span><span class="est-11__lv">Aisle 9</span></li>
        </ul>
      </section>

      <section class="est-11__panel">
        <header class="est-11__phead"><span class="est-11__ptitle">Shift notes</span><span class="est-11__ptag est-11__ptag--ok">Live</span></header>
        <p class="est-11__note">Night shift reported a jam on the sorter at 02:40. Cleared by 03:05, no packages lost.</p>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-11 {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --sunk: #f0f2f5;
  --line: #e3e6eb;
  --line-2: #d0d5dd;
  --ink: #131720;
  --muted: #576070;
  --faint: #88919f;
  --accent: #2b4a8b;
  --bad: #b5442f;
  --ok: #2f6b4f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-11 *,
.est-11 *::before,
.est-11 *::after {
  box-sizing: border-box;
}

.est-11 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-11 {
    --bg: oklch(0.978 0.004 255);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.958 0.005 255);
    --line: oklch(0.915 0.007 255);
    --line-2: oklch(0.858 0.009 255);
    --ink: oklch(0.19 0.014 265);
    --muted: oklch(0.475 0.018 265);
    --faint: oklch(0.635 0.017 265);
    --accent: oklch(0.42 0.11 262);
    --bad: oklch(0.52 0.15 32);
    --ok: oklch(0.48 0.09 155);
  }
}

.est-11__page {
  inline-size: min(78rem,100%);
  justify-self: center;
  padding: clamp(1.25rem,4vw,3rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1.25rem;
  align-content: start;
}

.est-11__head {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
  justify-content: space-between;
}

.est-11__eyebrow {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-11__h1 {
  margin: .35rem 0 0;
  font-size: clamp(1.45rem,3.2vw,2rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1;
}

.est-11__hacts {
  display: flex;
  gap: .5rem;
}

.est-11__ghost {
  min-block-size: 2.6rem;
  padding: .6rem .95rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s;
}

.est-11__ghost:hover {
  background: var(--sunk);
}

.est-11__ghost--sm {
  min-block-size: 2.4rem;
  padding: .5rem .85rem;
  font-size: .82rem;
}

.est-11__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(17rem,100%),1fr));
  align-items: start;
}

.est-11__panel {
  display: grid;
  gap: 0;
  align-content: start;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(19,23,32,.04);
}

.est-11__panel--tall {
  grid-column: span 2;
  min-block-size: 22rem;
}

.est-11__panel[data-state="error"] {
  border-color: color-mix(in oklab, var(--bad) 28%, var(--line));
}

.est-11__phead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .8rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--sunk);
}

.est-11__ptitle {
  font-size: .87rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-11__ptag {
  padding: .18rem .45rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .66rem;
  letter-spacing: .03em;
  color: var(--bad);
  background: color-mix(in oklab, var(--bad) 9%, var(--surface));
  border: 1px solid color-mix(in oklab, var(--bad) 26%, transparent);
  border-radius: 5px;
}

.est-11__ptag--ok {
  color: var(--ok);
  background: color-mix(in oklab, var(--ok) 9%, var(--surface));
  border-color: color-mix(in oklab, var(--ok) 26%, transparent);
}

.est-11__pbody {
  display: grid;
  min-block-size: 0;
}

.est-11__error {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .45rem;
  padding: clamp(1.75rem,5vh,3rem) 1.25rem;
  animation: est-11-in .45s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-11-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-11__mark {
  position: relative;
  inline-size: 3.35rem;
  block-size: 3.35rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
  color: var(--bad);
  background: color-mix(in oklab, var(--bad) 8%, var(--surface));
  border-radius: 14px;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--bad) 20%, transparent);
}

.est-11__mark svg {
  inline-size: 1.45rem;
  block-size: 1.45rem;
}

.est-11__mark::after {
  content: '';
  position: absolute;
  inset: -.4rem;
  border-radius: 18px;
  border: 1px solid color-mix(in oklab, var(--bad) 16%, transparent);
  animation: est-11-breathe 4.5s ease-in-out infinite;
}

@keyframes est-11-breathe {
  0%,
    100% {
    opacity: .9;
  }

  50% {
    opacity: .3;
  }
}

.est-11__eh {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.022em;
}

.est-11__ep {
  margin: 0;
  max-inline-size: 44ch;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-11__eacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .85rem;
}

.est-11__pri {
  min-block-size: 2.6rem;
  padding: .6rem 1.05rem;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 9px;
  box-shadow: 0 8px 18px -14px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-11__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-11__pri:disabled {
  opacity: .6;
  cursor: progress;
  translate: none;
}

.est-11__diag {
  margin: 1.35rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  justify-content: center;
  padding-block-start: 1rem;
  border-block-start: 1px dashed var(--line-2);
  inline-size: min(30rem,100%);
}

.est-11__diag div {
  display: grid;
  gap: .2rem;
}

.est-11__diag dt {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-11__diag dd {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .78rem;
  color: var(--muted);
}

.est-11__load {
  display: grid;
  justify-items: center;
  gap: 1rem;
  padding: clamp(2rem,6vh,3.5rem) 1.25rem;
}

.est-11__bars {
  display: flex;
  align-items: flex-end;
  gap: .35rem;
  block-size: 4.5rem;
}

.est-11__bars i {
  inline-size: .6rem;
  border-radius: 3px;
  background: color-mix(in oklab, var(--accent) 22%, var(--sunk));
  animation: est-11-pulse 1.15s ease-in-out infinite;
}

.est-11__bars i:nth-child(1) {
  block-size: 35%;
  animation-delay: 0s;
}

.est-11__bars i:nth-child(2) {
  block-size: 62%;
  animation-delay: .08s;
}

.est-11__bars i:nth-child(3) {
  block-size: 48%;
  animation-delay: .16s;
}

.est-11__bars i:nth-child(4) {
  block-size: 78%;
  animation-delay: .24s;
}

.est-11__bars i:nth-child(5) {
  block-size: 58%;
  animation-delay: .32s;
}

.est-11__bars i:nth-child(6) {
  block-size: 88%;
  animation-delay: .4s;
}

@keyframes est-11-pulse {
  0%,
    100% {
    opacity: .35;
    scale: 1 .85;
  }

  50% {
    opacity: 1;
    scale: 1 1;
  }
}

.est-11__lp {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .76rem;
  letter-spacing: .04em;
  color: var(--faint);
}

.est-11__ok {
  display: grid;
  gap: 1rem;
  padding: 1.25rem 1.15rem 1.35rem;
  animation: est-11-in .5s cubic-bezier(.2,.7,.3,1) both;
}

.est-11__chart {
  display: flex;
  align-items: flex-end;
  gap: .5rem;
  block-size: 11rem;
  padding-block-end: .5rem;
  border-block-end: 1px solid var(--line);
}

.est-11__chart span {
  flex: 1 1 0;
  block-size: var(--h);
  border-radius: 5px 5px 2px 2px;
  background: linear-gradient(180deg, color-mix(in oklab, var(--accent) 80%, transparent), color-mix(in oklab, var(--accent) 35%, transparent));
  animation: est-11-grow .7s cubic-bezier(.2,.7,.3,1) both;
}

.est-11__chart span:nth-child(2) {
  animation-delay: .05s;
}

.est-11__chart span:nth-child(3) {
  animation-delay: .1s;
}

.est-11__chart span:nth-child(4) {
  animation-delay: .15s;
}

.est-11__chart span:nth-child(5) {
  animation-delay: .2s;
}

.est-11__chart span:nth-child(6) {
  animation-delay: .25s;
}

.est-11__chart span:nth-child(7) {
  animation-delay: .3s;
}

@keyframes est-11-grow {
  from {
    scale: 1 .04;
  }

  to {
    scale: 1 1;
  }
}

.est-11__legend {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1.15rem;
  font-size: .78rem;
  color: var(--muted);
}

.est-11__legend li {
  display: flex;
  align-items: center;
  gap: .4rem;
}

.est-11__legend i {
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: 2px;
  background: var(--accent);
}

.est-11__legend i[data-c="2"] {
  background: color-mix(in oklab, var(--accent) 45%, var(--surface));
}

.est-11__list {
  margin: 0;
  padding: .5rem .6rem .75rem;
  list-style: none;
  display: grid;
  gap: .1rem;
}

.est-11__list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .55rem .5rem;
  border-radius: 8px;
  font-size: .85rem;
}

.est-11__list li:hover {
  background: var(--sunk);
}

.est-11__lv {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .74rem;
  color: var(--faint);
}

.est-11__note {
  margin: 0;
  padding: 1rem 1.1rem 1.2rem;
  font-size: .85rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-11__pri:focus-visible,
.est-11__ghost:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 820px) {
  .est-11__panel--tall {
    grid-column: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-11 *,
    .est-11 *::before,
    .est-11 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-11__panel,
    .est-11__mark,
    .est-11__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-11'); if(!root) return;
  var panel = root.querySelector('#est-11-panel'), err = root.querySelector('#est-11-error'),
      load = root.querySelector('#est-11-load'), ok = root.querySelector('#est-11-ok'),
      retry = root.querySelector('#est-11-retry'), tag = root.querySelector('#est-11-tag'),
      attempt = root.querySelector('#est-11-attempt');
  var tries = 1;
  retry.addEventListener('click', function(){
    err.hidden = true; load.hidden = false;
    panel.setAttribute('data-state','loading');
    tag.textContent = 'Retrying'; tag.className = 'est-11__ptag';
    retry.disabled = true;
    setTimeout(function(){
      load.hidden = true; ok.hidden = false;
      panel.setAttribute('data-state','ok');
      tag.textContent = 'Live'; tag.className = 'est-11__ptag est-11__ptag--ok';
      tries++; attempt.textContent = tries; retry.disabled = false;
    }, 1500);
  });
})();
```
