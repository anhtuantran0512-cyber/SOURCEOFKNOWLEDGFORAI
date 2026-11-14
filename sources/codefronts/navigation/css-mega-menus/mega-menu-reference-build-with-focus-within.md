---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/mega-menu-reference-build-with-focus-within/"
title: "Mega Menu Reference Build with Focus Within"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The reference build the rest of this collection borrows from: a <nav> with an accessible name, top-level items as real <button> elements carrying…"
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Reference Build with Focus Within
Source: https://codefronts.com/navigation/css-mega-menus/mega-menu-reference-build-with-focus-within/

The reference build the rest of this collection borrows from: a <nav> with an accessible name, top-level items as real <button> elements carrying aria-expanded and aria-controls, and a panel that opens on :hover and :focus-within so a keyboard user gets the same affordance a mouse user does. Drop-in product header, panel and page surface, with no script anywhere.
## HTML
```html
<section class="mm-01" aria-labelledby="mm-01-title">
  <h2 class="mm-01__sr" id="mm-01-title">Meridian</h2>

  <div class="mm-01__theme">
    <input class="mm-01__theme-input" type="checkbox" id="mm-01-theme">
    <label class="mm-01__theme-label" for="mm-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-01__header">
    <div class="mm-01__bar">
      <a class="mm-01__brand" href="#mm-01-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 17 12 4l8 13" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M4 20h16" fill="none" stroke="currentColor" stroke-width="2"/></svg>
        Meridian
      </a>

      <nav class="mm-01__nav" aria-label="Primary">
        <ul class="mm-01__list">
          <li class="mm-01__item">
            <button class="mm-01__trigger" type="button" aria-expanded="false" aria-controls="mm-01-panel-platform">Platform
              <svg class="mm-01__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>

            <div class="mm-01__panel" id="mm-01-panel-platform" aria-label="Platform">
              <div class="mm-01__panel-inner">
                <section class="mm-01__col" aria-labelledby="mm-01-h-build">
                  <h3 class="mm-01__col-head" id="mm-01-h-build">Build</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>Edge runtime</b><span>Deploy to 34 regions</span></a></li>
                    <li><a href="#mm-01-title"><b>Managed Postgres</b><span>Branching and PITR</span></a></li>
                    <li><a href="#mm-01-title"><b>Object storage</b><span>S3-compatible</span></a></li>
                    <li><a href="#mm-01-title"><b>Queues and jobs</b><span>Durable execution</span></a></li>
                  </ul>
                </section>
                <section class="mm-01__col" aria-labelledby="mm-01-h-operate">
                  <h3 class="mm-01__col-head" id="mm-01-h-operate">Operate</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>Observability</b><span>Traces and metrics</span></a></li>
                    <li><a href="#mm-01-title"><b>Incident timeline</b><span>Shared context</span></a></li>
                    <li><a href="#mm-01-title"><b>Access control</b><span>SSO and SCIM</span></a></li>
                    <li><a href="#mm-01-title" aria-current="page"><b>Status page</b><span>All systems normal</span></a></li>
                  </ul>
                </section>
                <section class="mm-01__col" aria-labelledby="mm-01-h-learn">
                  <h3 class="mm-01__col-head" id="mm-01-h-learn">Developers</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>API reference</b><span>REST and gRPC</span></a></li>
                    <li><a href="#mm-01-title"><b>Migration guide</b><span>v3 to v4</span></a></li>
                    <li><a href="#mm-01-title"><b>Architecture notes</b><span>Design decisions</span></a></li>
                    <li><a href="#mm-01-title"><b>Changelog</b><span>Weekly</span></a></li>
                  </ul>
                </section>

                <aside class="mm-01__promo" aria-label="Platform release">
                  <p class="mm-01__promo-tag">v4.2</p>
                  <p class="mm-01__promo-head">Regional read replicas</p>
                  <p class="mm-01__promo-body">Cut p95 read latency to 18ms in eu-west-2 without changing a query.</p>
                  <a class="mm-01__promo-cta" href="#mm-01-title">Read the release note</a>
                </aside>
              </div>
            </div>
          </li>

          <li class="mm-01__item">
            <button class="mm-01__trigger" type="button" aria-expanded="false" aria-controls="mm-01-panel-solutions">Solutions
              <svg class="mm-01__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="mm-01__panel" id="mm-01-panel-solutions" aria-label="Solutions">
              <div class="mm-01__panel-inner">
                <section class="mm-01__col" aria-labelledby="mm-01-h-team">
                  <h3 class="mm-01__col-head" id="mm-01-h-team">By team</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>Platform engineering</b><span>Golden paths</span></a></li>
                    <li><a href="#mm-01-title"><b>Data teams</b><span>Pipelines and warehouses</span></a></li>
                    <li><a href="#mm-01-title"><b>Security</b><span>Audit and residency</span></a></li>
                  </ul>
                </section>
                <section class="mm-01__col" aria-labelledby="mm-01-h-scale">
                  <h3 class="mm-01__col-head" id="mm-01-h-scale">By scale</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>Startups</b><span>Free for 12 months</span></a></li>
                    <li><a href="#mm-01-title"><b>Scale-ups</b><span>Usage-based</span></a></li>
                    <li><a href="#mm-01-title"><b>Enterprise</b><span>Committed spend</span></a></li>
                  </ul>
                </section>
                <section class="mm-01__col" aria-labelledby="mm-01-h-story">
                  <h3 class="mm-01__col-head" id="mm-01-h-story">Customers</h3>
                  <ul class="mm-01__links">
                    <li><a href="#mm-01-title"><b>Vale Logistics</b><span>212 depots</span></a></li>
                    <li><a href="#mm-01-title"><b>Basalt Health</b><span>HIPAA</span></a></li>
                    <li><a href="#mm-01-title"><b>Orbit Retail</b><span>Peak traffic</span></a></li>
                  </ul>
                </section>
                <aside class="mm-01__promo" aria-label="Customer story">
                  <p class="mm-01__promo-tag">Case study</p>
                  <p class="mm-01__promo-head">Vale cut deploy time by 71%</p>
                  <p class="mm-01__promo-body">One pipeline across 212 depots, rolled out in a quarter.</p>
                  <a class="mm-01__promo-cta" href="#mm-01-title">Read the story</a>
                </aside>
              </div>
            </div>
          </li>

          <li class="mm-01__item"><a class="mm-01__plain" href="#mm-01-title">Docs</a></li>
          <li class="mm-01__item"><a class="mm-01__plain" href="#mm-01-title">Pricing</a></li>
        </ul>
      </nav>

      <div class="mm-01__utils">
        <a class="mm-01__signin" href="#mm-01-title">Sign in</a>
        <a class="mm-01__cta" href="#mm-01-title">Start free</a>
      </div>
    </div>
  </header>

  <main class="mm-01__page">
    <div class="mm-01__hero">
      <p class="mm-01__eyebrow">Meridian Platform</p>
      <h1 class="mm-01__title">Ship to the edge without leaving Postgres behind.</h1>
      <p class="mm-01__sub">One runtime, one database, one bill. Deploy in 34 regions with a single command and keep your data where your users are.</p>
      <div class="mm-01__actions">
        <a class="mm-01__cta mm-01__cta--lg" href="#mm-01-title">Start free</a>
        <a class="mm-01__ghost" href="#mm-01-title">Book a walkthrough</a>
      </div>
      <dl class="mm-01__stats">
        <div><dt>Regions</dt><dd>34</dd></div>
        <div><dt>p95 read</dt><dd>18ms</dd></div>
        <div><dt>Uptime</dt><dd>99.99%</dd></div>
      </dl>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-01 {
  --mm-01-bg: #f4f6fb;
  --mm-01-grid: #e4e9f4;
  --mm-01-surf: #ffffff;
  --mm-01-line: #d6dded;
  --mm-01-ink: #0c1322;
  --mm-01-mut: #5c6a80;
  --mm-01-acc: #2f5bff;
  --mm-01-acc: oklch(55% 0.22 265);
  --mm-01-on-acc: #ffffff;
  --mm-01-panel-w: 74rem;
  --mm-01-lift: 10px;
  --mm-01-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-01-bg);
  background-image: linear-gradient(var(--mm-01-grid) 1px, transparent 1px), linear-gradient(90deg, var(--mm-01-grid) 1px, transparent 1px);
  background-size: 26px 26px, 26px 26px;
  color: var(--mm-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.mm-01 *,
.mm-01 *::before,
.mm-01 *::after {
  box-sizing: border-box;
}

.mm-01 :focus-visible {
  outline: 2px solid var(--mm-01-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.mm-01__sr {
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

.mm-01:has(.mm-01__theme-input:checked) {
  --mm-01-bg: #070b13;
  --mm-01-grid: #0e1522;
  --mm-01-surf: #111a28;
  --mm-01-line: #24314a;
  --mm-01-ink: #e9eff7;
  --mm-01-mut: #94a3ba;
  --mm-01-acc: #82a0ff;
  --mm-01-acc: oklch(75% 0.15 265);
  --mm-01-on-acc: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-01 {
    --mm-01-bg: #070b13;
    --mm-01-grid: #0e1522;
    --mm-01-surf: #111a28;
    --mm-01-line: #24314a;
    --mm-01-ink: #e9eff7;
    --mm-01-mut: #94a3ba;
    --mm-01-acc: #82a0ff;
    --mm-01-acc: oklch(75% 0.15 265);
    --mm-01-on-acc: #12100e;
  }

  .mm-01:has(.mm-01__theme-input:checked) {
    --mm-01-bg: #f4f6fb;
    --mm-01-grid: #e4e9f4;
    --mm-01-surf: #ffffff;
    --mm-01-line: #d6dded;
    --mm-01-ink: #0c1322;
    --mm-01-mut: #5c6a80;
    --mm-01-acc: #2f5bff;
    --mm-01-acc: oklch(55% 0.22 265);
    --mm-01-on-acc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-01:has(.mm-01__theme-input:checked) {
    --mm-01-bg: #070b13;
    --mm-01-grid: #0e1522;
    --mm-01-surf: #111a28;
    --mm-01-line: #24314a;
    --mm-01-ink: #e9eff7;
    --mm-01-mut: #94a3ba;
    --mm-01-acc: #82a0ff;
    --mm-01-acc: oklch(75% 0.15 265);
    --mm-01-on-acc: #12100e;
  }
}

.mm-01__theme {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-01__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-01-line);
  border-radius: 12px;
  background: var(--mm-01-surf);
  color: var(--mm-01-ink);
  cursor: pointer;
}

.mm-01__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-01__theme-input:focus-visible + .mm-01__theme-label {
  outline: 2px solid var(--mm-01-acc);
  outline-offset: 3px;
}

.mm-01__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-01-surf);
  border-block-end: 1px solid var(--mm-01-line);
}

.mm-01__bar {
  inline-size: min(var(--mm-01-panel-w), calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.75rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline-end: 60px;
}

.mm-01__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--mm-01-ink);
  text-decoration: none;
  font: 700 1rem/1 var(--mm-01-font-display);
  letter-spacing: -0.02em;
}

.mm-01__brand svg {
  inline-size: 19px;
  block-size: 19px;
  color: var(--mm-01-acc);
}

.mm-01__nav {
  min-inline-size: 0;
}

.mm-01__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-01__item {
  position: static;
}

.mm-01__trigger,
.mm-01__plain {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-block-size: 44px;
  padding-inline: 0.8rem;
  border: 0;
  border-radius: 9px;
  background: transparent;
  color: var(--mm-01-ink);
  font: 600 0.92rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-01__trigger:hover,
.mm-01__plain:hover {
  color: var(--mm-01-acc);
}

.mm-01__chev {
  inline-size: 15px;
  block-size: 15px;
  transition: transform 180ms ease;
}

.mm-01__item--open > .mm-01__trigger .mm-01__chev,
.mm-01__item:hover > .mm-01__trigger .mm-01__chev,
.mm-01__item:focus-within > .mm-01__trigger .mm-01__chev {
  transform: rotate(180deg);
}

.mm-01__item--open > .mm-01__trigger,
.mm-01__item:hover > .mm-01__trigger,
.mm-01__item:focus-within > .mm-01__trigger {
  background: color-mix(in oklab, var(--mm-01-acc) 11%, transparent);
  color: color-mix(in oklab, var(--mm-01-acc) 74%, var(--mm-01-ink));
}

.mm-01__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.mm-01__signin {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.7rem;
  color: var(--mm-01-mut);
  text-decoration: none;
  font: 600 0.88rem/1 system-ui, sans-serif;
}

.mm-01__signin:hover {
  color: var(--mm-01-ink);
}

.mm-01__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1rem;
  border-radius: 9px;
  background: var(--mm-01-acc);
  color: var(--mm-01-on-acc);
  text-decoration: none;
  font: 600 0.88rem/1 system-ui, sans-serif;
}

.mm-01__cta:hover {
  filter: brightness(1.08);
}

.mm-01__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-01-surf);
  border-block-end: 1px solid var(--mm-01-line);
  box-shadow: 0 26px 60px -34px rgba(12, 19, 34, 0.5);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(calc(var(--mm-01-lift) * -1));
  transition: opacity 170ms ease, transform 170ms ease, visibility 0s linear 170ms;
}

.mm-01__item--open > .mm-01__panel,
.mm-01__item:focus-within > .mm-01__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-01__item:hover > .mm-01__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: translateY(0);
    transition-delay: 0s;
  }
}

.mm-01__panel-inner {
  inline-size: min(var(--mm-01-panel-w), calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: clamp(0.9rem, 2.6vw, 2rem);
  padding-block: clamp(1.1rem, 3vw, 1.9rem);
}

@media (min-width: 68rem) {
  .mm-01__panel-inner {
    grid-template-columns: repeat(3, minmax(0, 1fr)) 16rem;
  }
}

.mm-01__col {
  min-inline-size: 0;
}

.mm-01__col-head {
  margin: 0 0 0.4rem;
  font: 700 0.68rem/1 var(--mm-01-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mm-01-mut);
}

.mm-01__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-01__links a {
  display: grid;
  align-content: center;
  gap: 1px;
  min-block-size: 48px;
  padding: 0.3rem 0.5rem;
  margin-inline: -0.5rem;
  border-radius: 8px;
  color: var(--mm-01-ink);
  text-decoration: none;
  min-inline-size: 0;
}

.mm-01__links b {
  font: 600 0.9rem/1.25 system-ui, sans-serif;
}

.mm-01__links span {
  font: 400 0.75rem/1.3 system-ui, sans-serif;
  color: var(--mm-01-mut);
}

.mm-01__links a:hover {
  background: color-mix(in oklab, var(--mm-01-acc) 9%, transparent);
}

.mm-01__links a:hover b {
  color: var(--mm-01-acc);
}

.mm-01__links a[aria-current="page"] {
  box-shadow: inset 2px 0 0 var(--mm-01-acc);
}

.mm-01__links a[aria-current="page"] b {
  color: var(--mm-01-acc);
}

.mm-01__promo {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.3rem;
  padding: clamp(0.85rem, 2.2vw, 1.1rem);
  border-radius: 12px;
  background: color-mix(in oklab, var(--mm-01-acc) 10%, transparent);
}

.mm-01__promo-tag {
  margin: 0;
  font: 700 0.64rem/1 var(--mm-01-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-01-acc);
}

.mm-01__promo-head {
  margin: 0;
  font: 600 1rem/1.2 system-ui, sans-serif;
  text-wrap: balance;
}

.mm-01__promo-body {
  margin: 0;
  font-size: 0.82rem;
  color: var(--mm-01-mut);
  text-wrap: pretty;
}

.mm-01__promo-cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-01-acc);
  font: 600 0.83rem/1 system-ui, sans-serif;
  text-decoration: none;
}

.mm-01__promo-cta:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.mm-01__page {
  inline-size: min(var(--mm-01-panel-w), calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 10vw, 6rem);
}

.mm-01__hero {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.9rem;
}

.mm-01__eyebrow {
  margin: 0;
  font: 700 0.7rem/1 var(--mm-01-font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-01-acc);
}

.mm-01__title {
  margin: 0;
  font: 700 clamp(2rem, 6vw, 3.6rem)/1.05 system-ui, sans-serif;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.mm-01__sub {
  margin: 0;
  max-inline-size: 36rem;
  color: var(--mm-01-mut);
  font-size: clamp(0.95rem, 2.4vw, 1.1rem);
  text-wrap: pretty;
}

.mm-01__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-block-start: 0.3rem;
}

.mm-01__cta--lg {
  min-block-size: 48px;
  padding-inline: 1.4rem;
  font-size: 0.95rem;
}

.mm-01__ghost {
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  padding-inline: 1.2rem;
  border: 1px solid var(--mm-01-line);
  border-radius: 9px;
  background: var(--mm-01-surf);
  color: var(--mm-01-ink);
  text-decoration: none;
  font: 600 0.95rem/1 system-ui, sans-serif;
}

.mm-01__ghost:hover {
  border-color: var(--mm-01-acc);
  color: var(--mm-01-acc);
}

.mm-01__stats {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(1.25rem, 5vw, 3rem);
  margin: clamp(1rem, 4vw, 2rem) 0 0;
  padding-block-start: clamp(1rem, 3vw, 1.5rem);
  border-block-start: 1px solid var(--mm-01-line);
}

.mm-01__stats dt {
  font: 700 0.66rem/1 var(--mm-01-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-01-mut);
}

.mm-01__stats dd {
  margin: 0.3rem 0 0;
  font: 700 clamp(1.3rem, 3.6vw, 1.7rem)/1 system-ui, sans-serif;
  letter-spacing: -0.02em;
}

@media (max-width: 52rem) {
  .mm-01__bar {
    align-items: stretch;
    flex-direction: column;
    padding-block: 0.6rem;
  }

  .mm-01__list {
    flex-direction: column;
  }

  .mm-01__utils {
    margin-inline-start: 0;
  }

  .mm-01__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: none;
    box-shadow: none;
    display: none;
  }

  .mm-01__item--open > .mm-01__panel,
    .mm-01__item:focus-within > .mm-01__panel {
    display: block;
  }

  .mm-01__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-01__panel,
    .mm-01__chev {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-01__trigger {
    position: relative;
  }

  .mm-01__item:hover > .mm-01__trigger::after,
    .mm-01__item:focus-within > .mm-01__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — columns cascade up in sequence; links stay still */

.mm-01__panel-inner > * {
  opacity: 0;
  translate: 0 16px;
  transition: opacity 240ms ease, translate 400ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-01__item:hover > .mm-01__panel .mm-01__panel-inner > *,
.mm-01__item:focus-within > .mm-01__panel .mm-01__panel-inner > *,
.mm-01__item--open > .mm-01__panel .mm-01__panel-inner > * {
  opacity: 1;
  translate: 0 0;
}

.mm-01__panel-inner > *:nth-child(1) {
  transition-delay: 40ms;
}

.mm-01__panel-inner > *:nth-child(2) {
  transition-delay: 110ms;
}

.mm-01__panel-inner > *:nth-child(3) {
  transition-delay: 180ms;
}

.mm-01__panel-inner > *:nth-child(4) {
  transition-delay: 250ms;
}

.mm-01__panel-inner > *:nth-child(5) {
  transition-delay: 320ms;
}

.mm-01__panel-inner > *:nth-child(n+6) {
  transition-delay: 320ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-01__panel-inner > * {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-01__panel-inner > * {
    opacity: 1;
    translate: none;
  }
}
```
