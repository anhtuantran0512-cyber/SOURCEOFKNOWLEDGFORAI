---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/table-rows/"
title: "Data Table Row Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Header row real, body rows pending — the SaaS data-table pattern from Airtable, Notion and Retool."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Table Row Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/table-rows/

Header row real, body rows pending — the SaaS data-table pattern from Airtable, Notion and Retool. It stays a real <table> with a real <thead>, so column widths are already resolved and assistive tech still announces "table, 4 columns" while the data loads.
## HTML
```html
<div class="sk-18">
  <div class="sk-18__stage">
    <section class="sk-18__wrap" aria-labelledby="sk-18-h">
      <header class="sk-18__head">
        <p class="sk-18__eyebrow">table-layout: fixed</p>
        <h2 class="sk-18__h" id="sk-18-h">Header real, columns resolved, rows pending</h2>
        <p class="sk-18__sub">The table is a real <code>&lt;table&gt;</code> with a real <code>&lt;thead&gt;</code> and a <code>&lt;colgroup&gt;</code>, so the grid is final before a single cell of data arrives.</p>
      </header>

      <div class="sk-18__card">
        <div class="sk-18__toolbar">
          <p class="sk-18__title">Workspace members</p>
          <div class="sk-18__tools">
            <p class="sk-18__search">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 20 20" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              Search members
            </p>
            <p class="sk-18__count">5 of 128</p>
          </div>
        </div>

        <div class="sk-18__scroll">
          <table class="sk-18__table">
            <caption class="sk-18__vh" role="status" aria-live="polite">Loading 5 member rows…</caption>
            <colgroup><col class="sk-18__c1"><col class="sk-18__c2"><col class="sk-18__c3"><col class="sk-18__c4"></colgroup>
            <thead>
              <tr><th scope="col">Name</th><th scope="col">Email</th><th scope="col">Role</th><th scope="col">Status</th></tr>
            </thead>
            <tbody aria-busy="true">
              <tr style="--i:0"><td><span class="sk-18__cell"><span class="sk-18__bar sk-18__avatar" aria-hidden="true"></span><span class="sk-18__bar" style="inline-size:7rem" aria-hidden="true"></span></span></td><td><span class="sk-18__bar sk-18__bar--email" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--role" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--status" aria-hidden="true"></span></td></tr>
              <tr style="--i:1"><td><span class="sk-18__cell"><span class="sk-18__bar sk-18__avatar" aria-hidden="true"></span><span class="sk-18__bar" style="inline-size:8.5rem" aria-hidden="true"></span></span></td><td><span class="sk-18__bar sk-18__bar--email" style="inline-size:70%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--role" style="inline-size:44%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--status" aria-hidden="true"></span></td></tr>
              <tr style="--i:2"><td><span class="sk-18__cell"><span class="sk-18__bar sk-18__avatar" aria-hidden="true"></span><span class="sk-18__bar" style="inline-size:6rem" aria-hidden="true"></span></span></td><td><span class="sk-18__bar sk-18__bar--email" style="inline-size:88%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--role" style="inline-size:62%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--status" aria-hidden="true"></span></td></tr>
              <tr style="--i:3"><td><span class="sk-18__cell"><span class="sk-18__bar sk-18__avatar" aria-hidden="true"></span><span class="sk-18__bar" style="inline-size:9rem" aria-hidden="true"></span></span></td><td><span class="sk-18__bar sk-18__bar--email" style="inline-size:76%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--role" style="inline-size:50%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--status" aria-hidden="true"></span></td></tr>
              <tr style="--i:4"><td><span class="sk-18__cell"><span class="sk-18__bar sk-18__avatar" aria-hidden="true"></span><span class="sk-18__bar" style="inline-size:7.5rem" aria-hidden="true"></span></span></td><td><span class="sk-18__bar sk-18__bar--email" style="inline-size:82%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--role" style="inline-size:58%" aria-hidden="true"></span></td><td><span class="sk-18__bar sk-18__bar--status" aria-hidden="true"></span></td></tr>
            </tbody>
          </table>
        </div>

        <div class="sk-18__pager">
          <p class="sk-18__pnote">Rows per page 25</p>
          <p class="sk-18__pnote">Page 1 of 6</p>
        </div>
      </div>

      <aside class="sk-18__spec" aria-label="Recipe">
        <p class="sk-18__srow"><span class="sk-18__skey">grid</span><span class="sk-18__sval">table-layout: fixed + colgroup — columns resolved before data lands</span></p>
        <p class="sk-18__srow"><span class="sk-18__skey">cells</span><span class="sk-18__sval">shape per column: circle + short bar, long email, medium role, status pill</span></p>
        <p class="sk-18__srow"><span class="sk-18__skey">a11y</span><span class="sk-18__sval">aria-busy on tbody · one status caption · aria-hidden on every bar</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-18 {
  --bg: #06070a;
  --bg2: #0d0f14;
  --surface: rgba(255,255,255,.03);
  --raise: rgba(255,255,255,.05);
  --line: rgba(255,255,255,.1);
  --ink: #f4f5f8;
  --muted: rgba(244,245,248,.62);
  --faint: rgba(244,245,248,.42);
  --accent: #a5b4fc;
  --sk: rgba(244,245,248,.1);
  --sheen: rgba(244,245,248,.17);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(56% 40% at 76% -6%, rgba(165,180,252,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-18 *,
.sk-18 *::before,
.sk-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 270)) {
  .sk-18 {
    --ink: oklch(0.97 0.005 275);
    --muted: oklch(0.97 0.005 275 / .62);
    --faint: oklch(0.97 0.005 275 / .42);
    --accent: oklch(0.82 0.09 278);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-18 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-18__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-18__wrap {
  inline-size: min(72rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-18__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
}

.sk-18__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-18__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-18__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-18__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-18__card {
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 30px 70px -46px rgba(0,0,0,.9);
}

.sk-18__toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: clamp(.9rem,1.7vw,1.2rem) clamp(1rem,2vw,1.4rem);
  border-block-end: 1px solid var(--line);
}

.sk-18__title {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.sk-18__tools {
  display: flex;
  align-items: center;
  gap: .8rem;
  flex-wrap: wrap;
}

.sk-18__search {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.2rem;
  padding: .4rem .8rem;
  border-radius: .55rem;
  background: var(--raise);
  border: 1px solid var(--line);
  font-size: .82rem;
  color: var(--muted);
}

.sk-18__search svg {
  inline-size: .95rem;
  block-size: .95rem;
}

.sk-18__count {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-18__scroll {
  overflow-x: auto;
}

.sk-18__table {
  inline-size: 100%;
  min-inline-size: 34rem;
  table-layout: fixed;
  border-collapse: collapse;
}

.sk-18__c1 {
  width: 34%;
}

.sk-18__c2 {
  width: 30%;
}

.sk-18__c3 {
  width: 20%;
}

.sk-18__c4 {
  width: 16%;
}

.sk-18__table th {
  text-align: start;
  padding: .75rem clamp(.7rem,1.4vw,1.1rem);
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  font-weight: 400;
  color: var(--faint);
  border-block-end: 1px solid var(--line);
  background: var(--raise);
}

.sk-18__table td {
  padding: .9rem clamp(.7rem,1.4vw,1.1rem);
  border-block-end: 1px solid var(--line);
  vertical-align: middle;
}

.sk-18__table tbody tr:last-child td {
  border-block-end: 0;
}

.sk-18__cell {
  display: flex;
  align-items: center;
  gap: .75rem;
}

.sk-18__pager {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .85rem clamp(1rem,2vw,1.4rem);
  border-block-start: 1px solid var(--line);
}

.sk-18__pnote {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-18__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-18__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-18-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.16s);
}

@keyframes sk-18-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-18__bar--email {
  inline-size: 82%;
}

.sk-18__bar--role {
  inline-size: 54%;
}

.sk-18__bar--status {
  inline-size: 4.5rem;
  block-size: 1.5rem;
  border-radius: 999px;
}

.sk-18__avatar {
  inline-size: 2rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-18__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-18__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-18__skey {
  min-inline-size: 3.4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-18__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-18[data-theme="light"] {
  --bg: #f7f8fc;
  --bg2: #fff;
  --surface: #ffffff;
  --raise: rgba(8,10,20,.035);
  --line: rgba(8,10,20,.11);
  --ink: #080a14;
  --muted: rgba(8,10,20,.62);
  --faint: rgba(8,10,20,.44);
  --accent: #4338ca;
  background: linear-gradient(178deg,#fff 0%,#eef0f8 100%);
}

@media (prefers-color-scheme: light) {
  .sk-18:not([data-theme="dark"]) {
    --bg: #f7f8fc;
    --bg2: #fff;
    --surface: #ffffff;
    --raise: rgba(8,10,20,.035);
    --line: rgba(8,10,20,.11);
    --ink: #080a14;
    --muted: rgba(8,10,20,.62);
    --faint: rgba(8,10,20,.44);
    --accent: #4338ca;
    background: linear-gradient(178deg,#fff 0%,#eef0f8 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-18__bar::after {
    animation: none;
    background: none;
  }

  .sk-18__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-18__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-18__bar::after {
    animation: none;
    background: none;
  }

  .sk-18__card,
    .sk-18__spec,
    .sk-18__search {
    border-color: CanvasText;
  }
}
```
