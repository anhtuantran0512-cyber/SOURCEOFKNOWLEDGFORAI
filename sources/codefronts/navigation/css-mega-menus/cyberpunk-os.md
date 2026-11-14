---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/cyberpunk-os/"
title: "Dashboard Mega Menu with Live Status Panel"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Product navigation carrying an operational column: service health rows, the current incident line, and deploy state, sitting beside the ordinary link columns."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard Mega Menu with Live Status Panel
Source: https://codefronts.com/navigation/css-mega-menus/cyberpunk-os/

Product navigation carrying an operational column: service health rows, the current incident line, and deploy state, sitting beside the ordinary link columns. The trap this demo is built around is that live-updating content inside an open panel must not shift layout under the pointer &mdash; every row is fixed-height, every number is tabular, and the longest possible value reserves its own space.
## HTML
```html
<section class="mm-16" aria-labelledby="mm-16-title">
  <h2 class="mm-16__sr" id="mm-16-title">Basalt Console</h2>

  <div class="mm-16__theme">
    <input class="mm-16__theme-input" type="checkbox" id="mm-16-theme">
    <label class="mm-16__theme-label" for="mm-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-16__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-16__header">
    <div class="mm-16__bar">
      <a class="mm-16__brand" href="#mm-16-title">basalt<span>/console</span></a>

      <nav class="mm-16__nav" aria-label="Primary">
        <ul class="mm-16__list">
          <li class="mm-16__item">
            <button class="mm-16__trigger" type="button" id="mm-16-trigger-services" aria-expanded="false" aria-controls="mm-16-panel-services">Services</button>
            <div class="mm-16__panel" id="mm-16-panel-services" aria-labelledby="mm-16-trigger-services">
              <div class="mm-16__panel-inner">
                <section class="mm-16__col" aria-labelledby="mm-16-h-compute">
                  <h3 class="mm-16__col-head" id="mm-16-h-compute">Compute</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">Edge functions</a></li><li><a href="#mm-16-title">Container fleet</a></li><li><a href="#mm-16-title">Cron and queues</a></li><li><a href="#mm-16-title">Build pipeline</a></li></ul>
                </section>
                <section class="mm-16__col" aria-labelledby="mm-16-h-data">
                  <h3 class="mm-16__col-head" id="mm-16-h-data">Data</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">Postgres clusters</a></li><li><a href="#mm-16-title">Object storage</a></li><li><a href="#mm-16-title">Replication</a></li></ul>
                </section>
                <section class="mm-16__col" aria-labelledby="mm-16-h-observe">
                  <h3 class="mm-16__col-head" id="mm-16-h-observe">Observe</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">Traces</a></li><li><a href="#mm-16-title">Log search</a></li><li><a href="#mm-16-title">Alert rules</a></li></ul>
                </section>

                <section class="mm-16__rail" aria-labelledby="mm-16-h-status">
                  <h3 class="mm-16__col-head mm-16__col-head--rail" id="mm-16-h-status">Live status</h3>
                  <ul class="mm-16__health">
                    <li class="mm-16__health-row" data-mm-16-state="ok">
                      <span class="mm-16__dot" aria-hidden="true"></span>
                      <span class="mm-16__svc">api.eu-west-2</span>
                      <span class="mm-16__num">142ms</span>
                      <span class="mm-16__state">operational</span>
                    </li>
                    <li class="mm-16__health-row" data-mm-16-state="warn">
                      <span class="mm-16__dot" aria-hidden="true"></span>
                      <span class="mm-16__svc">queue.workers</span>
                      <span class="mm-16__num">1204ms</span>
                      <span class="mm-16__state">degraded</span>
                    </li>
                    <li class="mm-16__health-row" data-mm-16-state="ok">
                      <span class="mm-16__dot" aria-hidden="true"></span>
                      <span class="mm-16__svc">pg.primary</span>
                      <span class="mm-16__num">18ms</span>
                      <span class="mm-16__state">operational</span>
                    </li>
                  </ul>
                  <p class="mm-16__incident"><b>INC-4471</b> Elevated queue latency in eu-west-2. Mitigation applied 09:41 UTC.</p>
                  <dl class="mm-16__deploy">
                    <div><dt>deploy</dt><dd>v4.2.0 &middot; canary 25%</dd></div>
                    <div><dt>owner</dt><dd>Alex Chen</dd></div>
                  </dl>
                  <a class="mm-16__rail-cta" href="#mm-16-title">Open status page</a>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-16__item">
            <button class="mm-16__trigger" type="button" id="mm-16-trigger-projects" aria-expanded="false" aria-controls="mm-16-panel-projects">Projects</button>
            <div class="mm-16__panel" id="mm-16-panel-projects" aria-labelledby="mm-16-trigger-projects">
              <div class="mm-16__panel-inner">
                <section class="mm-16__col" aria-labelledby="mm-16-h-active">
                  <h3 class="mm-16__col-head" id="mm-16-h-active">Active</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">northwind-api</a></li><li><a href="#mm-16-title">orbit-web</a></li><li><a href="#mm-16-title">fern-cms</a></li></ul>
                </section>
                <section class="mm-16__col" aria-labelledby="mm-16-h-env">
                  <h3 class="mm-16__col-head" id="mm-16-h-env">Environments</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">production</a></li><li><a href="#mm-16-title">staging</a></li><li><a href="#mm-16-title">preview</a></li></ul>
                </section>
                <section class="mm-16__col" aria-labelledby="mm-16-h-team">
                  <h3 class="mm-16__col-head" id="mm-16-h-team">Team</h3>
                  <ul class="mm-16__links"><li><a href="#mm-16-title">Members</a></li><li><a href="#mm-16-title">API tokens</a></li></ul>
                </section>
                <section class="mm-16__rail" aria-labelledby="mm-16-h-builds">
                  <h3 class="mm-16__col-head mm-16__col-head--rail" id="mm-16-h-builds">Recent builds</h3>
                  <ul class="mm-16__health">
                    <li class="mm-16__health-row" data-mm-16-state="ok"><span class="mm-16__dot" aria-hidden="true"></span><span class="mm-16__svc">northwind-api</span><span class="mm-16__num">1m42s</span><span class="mm-16__state">passed</span></li>
                    <li class="mm-16__health-row" data-mm-16-state="down"><span class="mm-16__dot" aria-hidden="true"></span><span class="mm-16__svc">fern-cms</span><span class="mm-16__num">0m38s</span><span class="mm-16__state">failed</span></li>
                    <li class="mm-16__health-row" data-mm-16-state="ok"><span class="mm-16__dot" aria-hidden="true"></span><span class="mm-16__svc">orbit-web</span><span class="mm-16__num">2m11s</span><span class="mm-16__state">passed</span></li>
                  </ul>
                  <p class="mm-16__incident"><b>fern-cms</b> Build failed at test step 4 of 9. Retry queued.</p>
                  <a class="mm-16__rail-cta" href="#mm-16-title">Open build log</a>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-16__item"><a class="mm-16__plain" href="#mm-16-title">Docs</a></li>
        </ul>
      </nav>

      <div class="mm-16__utils">
        <span class="mm-16__env" aria-hidden="true">prod</span>
        <span class="mm-16__avatar" aria-hidden="true">AC</span>
      </div>
    </div>
  </header>

  <main class="mm-16__page">
    <div class="mm-16__metrics">
      <div class="mm-16__metric"><dt>requests / min</dt><dd>84,210</dd></div>
      <div class="mm-16__metric"><dt>error rate</dt><dd>0.04%</dd></div>
      <div class="mm-16__metric"><dt>p95 latency</dt><dd>142ms</dd></div>
      <div class="mm-16__metric"><dt>spend today</dt><dd>$318.40</dd></div>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-16 {
  --mm-16-bg: #04070a;
  --mm-16-surf: #080d12;
  --mm-16-panel: #0a1117;
  --mm-16-line: #17242e;
  --mm-16-ink: #d6f4e3;
  --mm-16-mut: #6b8a7c;
  --mm-16-acc: #22c55e;
  --mm-16-acc: oklch(74% 0.19 145);
  --mm-16-warn: #f59e0b;
  --mm-16-warn: oklch(78% 0.16 78);
  --mm-16-down: #ef4444;
  --mm-16-down: oklch(64% 0.22 27);
  --mm-16-row: 34px;
  --mm-16-font-display: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-16-bg);
  background-image: linear-gradient(rgba(34, 197, 94, 0.05) 1px, transparent 1px);
  background-size: 100% 3px;
  color: var(--mm-16-ink);
  font-family: var(--mm-16-font-display);
  line-height: 1.5;
}

.mm-16 *,
.mm-16 *::before,
.mm-16 *::after {
  box-sizing: border-box;
}

.mm-16 :focus-visible {
  outline: 2px solid var(--mm-16-acc);
  outline-offset: 2px;
}

.mm-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-16:has(.mm-16__theme-input:checked) {
  --mm-16-bg: #f2f6f3;
  --mm-16-surf: #ffffff;
  --mm-16-panel: #ffffff;
  --mm-16-line: #cfdcd4;
  --mm-16-ink: #0b1a12;
  --mm-16-mut: #5d7267;
  --mm-16-acc: #15803d;
  --mm-16-acc: oklch(50% 0.15 145);
}

@media (prefers-color-scheme: light) {
  .mm-16 {
    --mm-16-bg: #f2f6f3;
    --mm-16-surf: #ffffff;
    --mm-16-panel: #ffffff;
    --mm-16-line: #cfdcd4;
    --mm-16-ink: #0b1a12;
    --mm-16-mut: #5d7267;
    --mm-16-acc: #15803d;
    --mm-16-acc: oklch(50% 0.15 145);
  }

  .mm-16:has(.mm-16__theme-input:checked) {
    --mm-16-bg: #04070a;
    --mm-16-surf: #080d12;
    --mm-16-panel: #0a1117;
    --mm-16-line: #17242e;
    --mm-16-ink: #d6f4e3;
    --mm-16-mut: #6b8a7c;
    --mm-16-acc: #22c55e;
    --mm-16-acc: oklch(74% 0.19 145);
  }
}

@media (prefers-color-scheme: dark) {
  .mm-16:has(.mm-16__theme-input:checked) {
    --mm-16-bg: #f2f6f3;
    --mm-16-surf: #ffffff;
    --mm-16-panel: #ffffff;
    --mm-16-line: #cfdcd4;
    --mm-16-ink: #0b1a12;
    --mm-16-mut: #5d7267;
    --mm-16-acc: #15803d;
    --mm-16-acc: oklch(50% 0.15 145);
  }
}

.mm-16__theme {
  position: absolute;
  inset-block-start: 8px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-16__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-16-line);
  background: var(--mm-16-surf);
  color: var(--mm-16-acc);
  cursor: pointer;
}

.mm-16__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-16__theme-input:focus-visible + .mm-16__theme-label {
  outline: 2px solid var(--mm-16-acc);
  outline-offset: 3px;
}

.mm-16__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-16-surf);
  border-block: 1px solid var(--mm-16-line);
}

.mm-16__bar {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.5rem);
  flex-wrap: wrap;
  min-block-size: 58px;
  padding-inline-end: 60px;
}

.mm-16__brand {
  color: var(--mm-16-acc);
  text-decoration: none;
  font: 700 0.9rem/1 var(--mm-16-font-display);
  letter-spacing: -0.02em;
}

.mm-16__brand span {
  color: var(--mm-16-mut);
}

.mm-16__nav {
  min-inline-size: 0;
}

.mm-16__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-16__item {
  position: static;
}

.mm-16__trigger,
.mm-16__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.85rem;
  border: 0;
  background: transparent;
  color: var(--mm-16-ink);
  font: 500 0.85rem/1 var(--mm-16-font-display);
  letter-spacing: 0.02em;
  text-decoration: none;
  cursor: pointer;
}

.mm-16__trigger::before,
.mm-16__plain::before {
  content: "> ";
  color: var(--mm-16-mut);
}

.mm-16__item--open > .mm-16__trigger,
.mm-16__item:hover > .mm-16__trigger,
.mm-16__item:focus-within > .mm-16__trigger {
  color: var(--mm-16-acc);
  background: color-mix(in oklab, var(--mm-16-acc) 12%, transparent);
}

.mm-16__plain:hover,
.mm-16__trigger:hover {
  color: var(--mm-16-acc);
}

.mm-16__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.mm-16__env {
  display: inline-flex;
  align-items: center;
  block-size: 22px;
  padding-inline: 0.5rem;
  border: 1px solid var(--mm-16-acc);
  color: var(--mm-16-acc);
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mm-16__avatar {
  display: grid;
  place-items: center;
  inline-size: 28px;
  block-size: 28px;
  background: color-mix(in oklab, var(--mm-16-acc) 22%, transparent);
  color: var(--mm-16-acc);
  font: 700 0.68rem/1 var(--mm-16-font-display);
}

.mm-16__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-16-panel);
  border-block-end: 1px solid var(--mm-16-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 140ms linear, visibility 0s linear 140ms;
}

.mm-16__item--open > .mm-16__panel,
.mm-16__item:focus-within > .mm-16__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-16__item:hover > .mm-16__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-16__panel-inner {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.9rem, 2.6vw, 2rem);
  padding-block: clamp(1rem, 3vw, 1.75rem);
}

.mm-16__rail {
  grid-column: 1 / -1;
}

@media (min-width: 66rem) {
  .mm-16__panel-inner {
    grid-template-columns: repeat(3, minmax(0, 1fr)) 24rem;
  }

  .mm-16__rail {
    grid-column: auto;
  }
}

.mm-16__col {
  min-inline-size: 0;
}

.mm-16__col-head {
  margin: 0 0 0.5rem;
  font: 700 0.68rem/1 var(--mm-16-font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-16-mut);
}

.mm-16__col-head--rail {
  color: var(--mm-16-acc);
}

.mm-16__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-16__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.5rem;
  margin-inline: -0.5rem;
  color: var(--mm-16-ink);
  text-decoration: none;
  font-size: 0.85rem;
  min-inline-size: 0;
}

.mm-16__links a:hover {
  background: color-mix(in oklab, var(--mm-16-acc) 14%, transparent);
  color: var(--mm-16-acc);
}

.mm-16__rail {
  min-inline-size: 0;
  container-type: inline-size;
  display: grid;
  align-content: start;
  gap: 0.6rem;
  padding: 0.85rem 1rem;
  border: 1px solid var(--mm-16-line);
  background: color-mix(in oklab, var(--mm-16-acc) 5%, transparent);
}

.mm-16__health {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  font-variant-numeric: tabular-nums;
}

.mm-16__health-row {
  display: grid;
  grid-template-columns: 10px minmax(0, 1fr) 7ch 10ch;
  align-items: center;
  gap: 0.6rem;
  min-block-size: var(--mm-16-row);
  font-size: 0.78rem;
}

.mm-16__dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 999px;
  background: var(--mm-16-acc);
  position: relative;
}

.mm-16__dot::after {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  opacity: 0.35;
  animation: mm-16-pulse 2.4s ease-in-out infinite;
}

[data-mm-16-state="ok"] .mm-16__dot {
  background: var(--mm-16-acc);
  color: var(--mm-16-acc);
}

[data-mm-16-state="warn"] .mm-16__dot {
  background: var(--mm-16-warn);
  color: var(--mm-16-warn);
}

[data-mm-16-state="down"] .mm-16__dot {
  background: var(--mm-16-down);
  color: var(--mm-16-down);
}

@keyframes mm-16-pulse {
  0%,
    100% {
    opacity: 0.12;
  }

  50% {
    opacity: 0.5;
  }
}

.mm-16__svc {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mm-16__num {
  min-inline-size: 7ch;
  text-align: end;
  color: var(--mm-16-mut);
}

.mm-16__state {
  min-inline-size: 10ch;
  text-align: end;
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mm-16-mut);
}

@container (max-width: 20rem) {
  .mm-16__health-row {
    grid-template-columns: 10px minmax(4ch, 1fr) 7ch;
  }

  .mm-16__state {
    display: none;
  }
}

@container (max-width: 13rem) {
  .mm-16__health-row {
    grid-template-columns: 10px minmax(4ch, 1fr);
  }

  .mm-16__num {
    display: none;
  }
}

[data-mm-16-state="warn"] .mm-16__state {
  color: var(--mm-16-warn);
}

[data-mm-16-state="down"] .mm-16__state {
  color: var(--mm-16-down);
}

.mm-16__incident {
  margin: 0;
  min-block-size: 3.4rem;
  padding: 0.5rem 0.65rem;
  border-inline-start: 2px solid var(--mm-16-warn);
  background: color-mix(in oklab, var(--mm-16-warn) 10%, transparent);
  font-size: 0.75rem;
  color: var(--mm-16-ink);
  text-wrap: pretty;
}

.mm-16__incident b {
  color: var(--mm-16-warn);
}

.mm-16__deploy {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.5rem;
  margin: 0;
  font-size: 0.75rem;
}

.mm-16__deploy dt {
  color: var(--mm-16-mut);
  font-size: 0.64rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.mm-16__deploy dd {
  margin: 0.15rem 0 0;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mm-16__rail-cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-16-acc);
  font-size: 0.78rem;
  text-decoration: none;
}

.mm-16__rail-cta::before {
  content: "-> ";
}

.mm-16__page {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(1.5rem, 5vw, 3rem);
}
/* Dividers are per-cell borders, not a 1px gap revealing the grid
   background: auto-fit leaves empty tracks at some widths and the bleed
   trick paints those as solid grey blocks. A transparent grid makes any
   item count safe. */

.mm-16__metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: 0;
  background: transparent;
  border: 1px solid var(--mm-16-line);
  border-block-end: 0;
  border-inline-end: 0;
}

.mm-16__metric {
  border-inline-end: 1px solid var(--mm-16-line);
  border-block-end: 1px solid var(--mm-16-line);
  display: grid;
  gap: 2px;
  padding: 0.9rem 1rem;
  background: var(--mm-16-surf);
  min-inline-size: 0;
}

.mm-16__metric dt {
  font-size: 0.64rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-16-mut);
}

.mm-16__metric dd {
  margin: 0;
  font: 700 clamp(1.3rem, 3.6vw, 1.7rem)/1 var(--mm-16-font-display);
  font-variant-numeric: tabular-nums;
  color: var(--mm-16-acc);
}

@media (max-width: 52rem) {
  .mm-16__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.5rem;
  }

  .mm-16__list {
    flex-direction: column;
  }

  .mm-16__utils {
    margin-inline-start: 0;
  }

  .mm-16__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-16__item--open > .mm-16__panel,
    .mm-16__item:focus-within > .mm-16__panel {
    display: block;
  }

  .mm-16__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-16__panel {
    transition-duration: 1ms;
  }

  .mm-16__dot::after {
    animation: none;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-16__trigger {
    position: relative;
  }

  .mm-16__item:hover > .mm-16__trigger::after,
    .mm-16__item:focus-within > .mm-16__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — a scanline runs down the panel while rows switch on in discrete flickers */

@keyframes mm-16-scan {
  0% {
    translate: 0 -100%;
    opacity: 0;
  }

  12% {
    opacity: 0.85;
  }

  100% {
    translate: 0 320%;
    opacity: 0;
  }
}

.mm-16__panel {
  overflow: clip;
}

.mm-16__panel::before {
  content: "";
  position: absolute;
  inset-inline: 0;
  inset-block-start: 0;
  block-size: 32%;
  pointer-events: none;
  opacity: 0;
  background: linear-gradient(180deg, transparent, color-mix(in oklab, var(--mm-16-acc) 24%, transparent));
}

.mm-16__item:hover > .mm-16__panel::before,
.mm-16__item:focus-within > .mm-16__panel::before,
.mm-16__item--open > .mm-16__panel::before {
  animation: mm-16-scan 720ms linear 1;
}

.mm-16__links li {
  opacity: 0;
  transition: opacity 1ms steps(1, end);
}

.mm-16__item:hover > .mm-16__panel .mm-16__links li,
.mm-16__item:focus-within > .mm-16__panel .mm-16__links li,
.mm-16__item--open > .mm-16__panel .mm-16__links li {
  opacity: 1;
}

.mm-16__links li:nth-child(1) {
  transition-delay: 25ms;
}

.mm-16__links li:nth-child(2) {
  transition-delay: 60ms;
}

.mm-16__links li:nth-child(3) {
  transition-delay: 95ms;
}

.mm-16__links li:nth-child(4) {
  transition-delay: 130ms;
}

.mm-16__links li:nth-child(5) {
  transition-delay: 165ms;
}

.mm-16__links li:nth-child(6) {
  transition-delay: 200ms;
}

.mm-16__links li:nth-child(7) {
  transition-delay: 235ms;
}

.mm-16__links li:nth-child(n+8) {
  transition-delay: 235ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-16__panel::before,
    .mm-16__links li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-16__links li {
    opacity: 1;
  }
}
```
