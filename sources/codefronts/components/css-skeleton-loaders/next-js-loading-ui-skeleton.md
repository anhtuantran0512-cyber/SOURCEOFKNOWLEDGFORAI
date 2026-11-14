---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/next-js-loading-ui-skeleton/"
title: "Next.js Loading UI Skeleton"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Next.js App Router turns a whole route into a loading state: drop loading.tsx next to page.tsx and the framework wraps the segment in a Suspense boundary for…"
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Next.js Loading UI Skeleton
Source: https://codefronts.com/components/css-skeleton-loaders/next-js-loading-ui-skeleton/

Next.js App Router turns a whole route into a loading state: drop loading.tsx next to page.tsx and the framework wraps the segment in a Suspense boundary for you. This demo renders that route-level shell inside mock browser chrome — header, sidebar and main grid all skeletonised — with the file tree annotated so the placement is unambiguous.
## HTML
```html
<div class="sk-02">
  <div class="sk-02__stage">
    <section class="sk-02__wrap" aria-labelledby="sk-02-h">
      <header class="sk-02__head">
        <p class="sk-02__eyebrow">Next.js 15 · App Router</p>
        <h2 class="sk-02__h" id="sk-02-h">One file turns a whole route into a loading state</h2>
        <p class="sk-02__sub">Drop <code>loading.tsx</code> beside <code>page.tsx</code> and the segment gets a Suspense boundary for free. Skeleton the page, never the layout.</p>
      </header>

      <div class="sk-02__split">
        <aside class="sk-02__files" aria-label="File tree">
          <p class="sk-02__fline">app/</p>
          <p class="sk-02__fline sk-02__fline--i1">dashboard/</p>
          <p class="sk-02__fline sk-02__fline--i2">layout.tsx <span class="sk-02__fnote">stays mounted</span></p>
          <p class="sk-02__fline sk-02__fline--i2">page.tsx <span class="sk-02__fnote">async · streaming</span></p>
          <p class="sk-02__fline sk-02__fline--i2 sk-02__fline--on">loading.tsx <span class="sk-02__fnote">this shell</span></p>
          <p class="sk-02__fline sk-02__fline--i1">settings/</p>
        </aside>

        <figure class="sk-02__browser">
          <div class="sk-02__chrome">
            <span class="sk-02__dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <p class="sk-02__url">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Zm0 0c2.6 2 3.9 5 3.9 9S14.6 19 12 21m0-18C9.4 5 8.1 8 8.1 12S9.4 19 12 21M3.4 9.5h17.2M3.4 14.5h17.2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
              acme.app/dashboard
            </p>
            <span class="sk-02__spin" aria-hidden="true"></span>
          </div>

          <div class="sk-02__shell" role="status" aria-live="polite">
            <span class="sk-02__vh">Loading dashboard…</span>
            <nav class="sk-02__topnav" aria-label="Product navigation">
              <p class="sk-02__brand">Acme<span>/</span>Analytics</p>
              <span class="sk-02__bar sk-02__bar--pill" style="--i:0; inline-size:6rem" aria-hidden="true"></span>
              <span class="sk-02__bar sk-02__avatar" style="--i:1" aria-hidden="true"></span>
            </nav>

            <aside class="sk-02__side" aria-label="Section navigation">
              <p class="sk-02__slabel">Overview</p>
              <p class="sk-02__slabel">Funnels</p>
              <p class="sk-02__slabel">Retention</p>
              <p class="sk-02__slabel">Sources</p>
              <p class="sk-02__hint">from layout.tsx — already painted</p>
            </aside>

            <main class="sk-02__main">
              <div class="sk-02__tiles" aria-hidden="true">
                <div class="sk-02__tile" style="--i:0"><span class="sk-02__bar sk-02__bar--xs"></span><span class="sk-02__bar sk-02__bar--big"></span></div>
                <div class="sk-02__tile" style="--i:1"><span class="sk-02__bar sk-02__bar--xs"></span><span class="sk-02__bar sk-02__bar--big"></span></div>
                <div class="sk-02__tile" style="--i:2"><span class="sk-02__bar sk-02__bar--xs"></span><span class="sk-02__bar sk-02__bar--big"></span></div>
              </div>
              <div class="sk-02__chart" style="--i:3" aria-hidden="true"><span class="sk-02__bar sk-02__bar--block"></span></div>
              <ul class="sk-02__rows" aria-hidden="true">
                <li class="sk-02__row" style="--i:0"><span class="sk-02__bar sk-02__bar--dot"></span><span class="sk-02__bar" style="inline-size:38%"></span><span class="sk-02__bar" style="inline-size:5rem"></span></li>
                <li class="sk-02__row" style="--i:1"><span class="sk-02__bar sk-02__bar--dot"></span><span class="sk-02__bar" style="inline-size:52%"></span><span class="sk-02__bar" style="inline-size:5rem"></span></li>
                <li class="sk-02__row" style="--i:2"><span class="sk-02__bar sk-02__bar--dot"></span><span class="sk-02__bar" style="inline-size:44%"></span><span class="sk-02__bar" style="inline-size:5rem"></span></li>
              </ul>
            </main>
          </div>
        </figure>
      </div>

      <aside class="sk-02__spec" aria-label="Recipe">
        <p class="sk-02__srow"><span class="sk-02__skey">file</span><span class="sk-02__sval">app/dashboard/loading.tsx — default export, server component</span></p>
        <p class="sk-02__srow"><span class="sk-02__skey">scope</span><span class="sk-02__sval">the segment and its children, never layout.tsx chrome</span></p>
        <p class="sk-02__srow"><span class="sk-02__skey">stagger</span><span class="sk-02__sval">animation-delay: calc(var(--i) * -.18s)</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-02 {
  --bg: #07080a;
  --bg2: #101216;
  --surface: rgba(255,255,255,.03);
  --raise: rgba(255,255,255,.05);
  --line: rgba(255,255,255,.09);
  --ink: #f6f7f9;
  --muted: rgba(246,247,249,.6);
  --faint: rgba(246,247,249,.4);
  --accent: #ffffff;
  --sk: rgba(246,247,249,.1);
  --sheen: rgba(246,247,249,.16);
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
  background: radial-gradient(80% 45% at 50% -10%, rgba(255,255,255,.07) 0%, transparent 60%), linear-gradient(180deg,#0c0e12 0%,var(--bg) 65%);
}

.sk-02 *,
.sk-02 *::before,
.sk-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 200)) {
  .sk-02 {
    --bg: oklch(0.15 0.006 260);
    --ink: oklch(0.975 0.002 260);
    --muted: oklch(0.975 0.002 260 / .6);
    --faint: oklch(0.975 0.002 260 / .4);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-02 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 16%, transparent);
  }
}

.sk-02__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-02__wrap {
  inline-size: min(80rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-02__head {
  display: grid;
  gap: .55rem;
  max-inline-size: 46rem;
}

.sk-02__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.sk-02__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-02__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-02__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
  background: var(--raise);
  padding: .1em .35em;
  border-radius: .3rem;
}

.sk-02__split {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: minmax(0,1fr);
}

@media (min-width: 62rem) {
  .sk-02__split {
    grid-template-columns: 15rem minmax(0,1fr);
  }
}

.sk-02__files {
  padding: clamp(.9rem,1.6vw,1.15rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  align-content: start;
  display: grid;
  gap: .1rem;
}

.sk-02__fline {
  margin: 0;
  font-family: var(--mono);
  font-size: .76rem;
  line-height: 1.95;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-02__fline--i1 {
  padding-inline-start: .9rem;
}

.sk-02__fline--i2 {
  padding-inline-start: 1.8rem;
}

.sk-02__fline--on {
  color: var(--ink);
  font-weight: 500;
}

.sk-02__fnote {
  font-size: .66rem;
  color: var(--faint);
  margin-inline-start: .35rem;
}

.sk-02__fline--on .sk-02__fnote {
  color: var(--ink);
  opacity: .7;
}

.sk-02__browser {
  margin: 0;
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  overflow: hidden;
  background: var(--bg2);
  box-shadow: 0 32px 80px -44px rgba(0,0,0,.9);
}

.sk-02__chrome {
  display: flex;
  align-items: center;
  gap: .8rem;
  padding: .7rem .9rem;
  border-block-end: 1px solid var(--line);
  background: var(--surface);
}

.sk-02__dots {
  display: flex;
  gap: .35rem;
  flex: none;
}

.sk-02__dots i {
  inline-size: .6rem;
  block-size: .6rem;
  border-radius: 999px;
  background: var(--sk);
}

.sk-02__url {
  margin: 0;
  flex: 1;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  gap: .45rem;
  padding: .35rem .7rem;
  border-radius: .5rem;
  background: var(--raise);
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-02__url svg {
  inline-size: .9rem;
  block-size: .9rem;
  flex: none;
  color: var(--faint);
}

.sk-02__spin {
  inline-size: .95rem;
  block-size: .95rem;
  flex: none;
  border-radius: 999px;
  border: 2px solid var(--sk);
  border-block-start-color: var(--ink);
  animation: sk-02-spin .9s linear infinite;
}

@keyframes sk-02-spin {
  to {
    rotate: 360deg;
  }
}

.sk-02__shell {
  display: grid;
  gap: 1px;
  background: var(--line);
  grid-template-areas: 'nav' 'side' 'main';
  padding: 0;
}

@media (min-width: 48rem) {
  .sk-02__shell {
    grid-template-columns: 12.5rem minmax(0,1fr);
    grid-template-areas: 'nav nav' 'side main';
  }
}

.sk-02__topnav {
  grid-area: nav;
  display: flex;
  align-items: center;
  gap: .8rem;
  padding: .85rem 1.1rem;
  background: var(--bg2);
}

.sk-02__brand {
  margin: 0;
  flex: 1;
  font-size: .9rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.sk-02__brand span {
  color: var(--faint);
  margin-inline: .3rem;
}

.sk-02__side {
  grid-area: side;
  display: grid;
  gap: .15rem;
  align-content: start;
  padding: 1.1rem;
  background: var(--bg2);
}

.sk-02__slabel {
  margin: 0;
  padding: .42rem .55rem;
  border-radius: .45rem;
  font-size: .82rem;
  color: var(--muted);
}

.sk-02__slabel:first-child {
  background: var(--raise);
  color: var(--ink);
}

.sk-02__hint {
  margin: .7rem 0 0;
  font-family: var(--mono);
  font-size: .63rem;
  line-height: 1.5;
  color: var(--faint);
  text-wrap: pretty;
}

.sk-02__main {
  grid-area: main;
  display: grid;
  gap: clamp(.75rem,1.4vw,1.05rem);
  padding: clamp(1rem,2vw,1.4rem);
  background: var(--bg2);
  min-block-size: 22rem;
  align-content: start;
}

.sk-02__tiles {
  display: grid;
  gap: clamp(.7rem,1.3vw,1rem);
  grid-template-columns: repeat(auto-fit,minmax(8.5rem,1fr));
}

.sk-02__tile {
  display: grid;
  gap: .7rem;
  padding: .95rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
  background: var(--surface);
}

.sk-02__chart {
  padding: .95rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
  background: var(--surface);
}

.sk-02__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .55rem;
}

.sk-02__row {
  display: flex;
  align-items: center;
  gap: .8rem;
}

.sk-02__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  border-radius: 6px;
  background: var(--sk);
}

.sk-02__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-02-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.18s);
}

@keyframes sk-02-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-02__bar--xs {
  block-size: .6rem;
  inline-size: 4.2rem;
}

.sk-02__bar--big {
  block-size: 1.7rem;
  inline-size: 70%;
  border-radius: 8px;
}

.sk-02__bar--block {
  block-size: clamp(5rem,11vw,7.5rem);
  inline-size: 100%;
  border-radius: 8px;
}

.sk-02__bar--pill {
  block-size: 1.65rem;
  border-radius: 999px;
}

.sk-02__bar--dot {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  border-radius: 999px;
  flex: none;
}

.sk-02__avatar {
  inline-size: 1.75rem;
  block-size: 1.75rem;
  border-radius: 999px;
  flex: none;
}

.sk-02__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-02__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-02__skey {
  min-inline-size: 4rem;
  color: var(--ink);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-02__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-02[data-theme="light"] {
  --bg: #f7f8fa;
  --bg2: #ffffff;
  --surface: rgba(8,10,16,.022);
  --raise: rgba(8,10,16,.05);
  --line: rgba(8,10,16,.1);
  --ink: #0a0c12;
  --muted: rgba(10,12,18,.62);
  --faint: rgba(10,12,18,.42);
  background: linear-gradient(180deg,#fff 0%,#eef0f5 100%);
}

@media (prefers-color-scheme: light) {
  .sk-02:not([data-theme="dark"]) {
    --bg: #f7f8fa;
    --bg2: #ffffff;
    --surface: rgba(8,10,16,.022);
    --raise: rgba(8,10,16,.05);
    --line: rgba(8,10,16,.1);
    --ink: #0a0c12;
    --muted: rgba(10,12,18,.62);
    --faint: rgba(10,12,18,.42);
    background: linear-gradient(180deg,#fff 0%,#eef0f5 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-02__bar::after {
    animation: none;
    background: none;
  }

  .sk-02__bar {
    background: var(--sheen);
  }

  .sk-02__spin {
    animation: none;
    border-block-start-color: var(--sk);
  }
}

@media (forced-colors: active) {
  .sk-02__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-02__bar::after {
    animation: none;
    background: none;
  }

  .sk-02__browser,
    .sk-02__files,
    .sk-02__spec,
    .sk-02__tile,
    .sk-02__chart {
    border-color: CanvasText;
  }
}
```
