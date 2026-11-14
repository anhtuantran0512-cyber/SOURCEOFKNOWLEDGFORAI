---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/react-suspense-fallback-skeleton/"
title: "React Suspense Fallback Skeleton"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The pattern React devs actually ship: a <Suspense> boundary whose fallback is a skeleton with the same geometry as the component it stands in for."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: React Suspense Fallback Skeleton
Source: https://codefronts.com/components/css-skeleton-loaders/react-suspense-fallback-skeleton/

The pattern React devs actually ship: a <Suspense> boundary whose fallback is a skeleton with the same geometry as the component it stands in for. The demo puts the pending state and the resolved state side by side against a labelled component tree, so you can see that a good fallback is a tracing of the real layout — same avatar size, same line count, same card padding.
## HTML
```html
<div class="sk-01">
  <div class="sk-01__stage">
    <section class="sk-01__wrap" aria-labelledby="sk-01-h">
      <header class="sk-01__head">
        <p class="sk-01__eyebrow">React 19 · Suspense</p>
        <h2 class="sk-01__h" id="sk-01-h">A fallback is a tracing of the resolved component</h2>
        <p class="sk-01__sub">Same avatar box, same line count, same padding. When the promise settles, nothing on the page moves.</p>
        <p class="sk-01__code"><span class="sk-01__tok">&lt;Suspense</span> fallback<span class="sk-01__tok">={</span>&lt;CardSkeleton /&gt;<span class="sk-01__tok">}&gt;</span></p>
      </header>

      <div class="sk-01__tree" aria-label="Component tree">
        <p class="sk-01__tline"><span class="sk-01__glyph">└─</span> &lt;DashboardPage&gt;</p>
        <p class="sk-01__tline sk-01__tline--i1"><span class="sk-01__glyph">└─</span> &lt;Suspense fallback&gt; <span class="sk-01__note">boundary</span></p>
        <p class="sk-01__tline sk-01__tline--i2"><span class="sk-01__glyph">└─</span> &lt;ProjectCard&gt; <span class="sk-01__note">lazy · pending</span></p>
      </div>

      <div class="sk-01__cols">
        <article class="sk-01__panel sk-01__panel--resolved" aria-label="Resolved state, shown for comparison">
          <p class="sk-01__label">resolved · promise settled</p>
          <div class="sk-01__row">
            <img class="sk-01__pic" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Priya Sharma" loading="lazy" decoding="async">
            <div class="sk-01__ident">
              <p class="sk-01__name">Priya Sharma</p>
              <p class="sk-01__role">Design Systems · edited 4m ago</p>
            </div>
          </div>
          <p class="sk-01__copy">Migrating the loading states off spinners. Every boundary now renders a skeleton that matches its resolved geometry, so the dashboard stopped jumping on slow networks.</p>
          <dl class="sk-01__meta">
            <div><dt>Sessions</dt><dd>18,402</dd></div>
            <div><dt>CLS</dt><dd>0.00</dd></div>
            <div><dt>p75 TTFB</dt><dd>210ms</dd></div>
          </dl>
        </article>

        <article class="sk-01__panel sk-01__panel--fallback" role="status" aria-live="polite">
          <span class="sk-01__vh">Loading project card…</span>
          <p class="sk-01__label sk-01__label--on">fallback · promise pending</p>
          <div class="sk-01__row">
            <span class="sk-01__bar sk-01__avatar" aria-hidden="true"></span>
            <div class="sk-01__ident">
              <span class="sk-01__bar" style="inline-size:9rem" aria-hidden="true"></span>
              <span class="sk-01__bar sk-01__bar--sm" style="inline-size:13rem" aria-hidden="true"></span>
            </div>
          </div>
          <div class="sk-01__lines" aria-hidden="true">
            <span class="sk-01__bar sk-01__bar--sm"></span>
            <span class="sk-01__bar sk-01__bar--sm"></span>
            <span class="sk-01__bar sk-01__bar--sm" style="inline-size:62%"></span>
          </div>
          <div class="sk-01__metaskel" aria-hidden="true">
            <div><span class="sk-01__bar sk-01__bar--xs"></span><span class="sk-01__bar sk-01__bar--md"></span></div>
            <div><span class="sk-01__bar sk-01__bar--xs"></span><span class="sk-01__bar sk-01__bar--md"></span></div>
            <div><span class="sk-01__bar sk-01__bar--xs"></span><span class="sk-01__bar sk-01__bar--md"></span></div>
          </div>
        </article>
      </div>

      <aside class="sk-01__spec" aria-label="Recipe">
        <p class="sk-01__srow"><span class="sk-01__skey">fill</span><span class="sk-01__sval">color-mix(in oklab, currentColor 10%, transparent)</span></p>
        <p class="sk-01__srow"><span class="sk-01__skey">sheen</span><span class="sk-01__sval">translate -100% → 100% · 1.4s linear infinite</span></p>
        <p class="sk-01__srow"><span class="sk-01__skey">a11y</span><span class="sk-01__sval">role="status" + visually hidden "Loading…"</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-01 {
  --bg: #08090c;
  --bg2: #0d1016;
  --surface: rgba(255,255,255,.028);
  --line: rgba(255,255,255,.09);
  --ink: #f4f6fa;
  --muted: rgba(244,246,250,.6);
  --faint: rgba(244,246,250,.42);
  --accent: #61dafb;
  --sk: rgba(244,246,250,.1);
  --sheen: rgba(244,246,250,.14);
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
  -webkit-text-size-adjust: 100%;
  background: radial-gradient(70% 50% at 78% -6%, rgba(97,218,251,.1) 0%, transparent 62%), linear-gradient(178deg, var(--bg2) 0%, var(--bg) 60%);
}

.sk-01 *,
.sk-01 *::before,
.sk-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 200)) {
  .sk-01 {
    --bg: oklch(0.16 0.012 265);
    --bg2: oklch(0.21 0.02 260);
    --ink: oklch(0.97 0.004 260);
    --muted: oklch(0.97 0.004 260 / .6);
    --faint: oklch(0.97 0.004 260 / .42);
    --accent: oklch(0.85 0.11 210);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-01 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 14%, transparent);
  }
}

.sk-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-01__wrap {
  inline-size: min(76rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-01__head {
  display: grid;
  gap: .55rem;
  max-inline-size: 44rem;
}

.sk-01__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-01__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-01__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-01__code {
  margin: .35rem 0 0;
  justify-self: start;
  padding: .42rem .7rem;
  border-radius: .55rem;
  border: 1px solid var(--line);
  background: var(--surface);
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--ink);
}

.sk-01__tok {
  color: var(--accent);
}

.sk-01__tree {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
}

.sk-01__tline {
  margin: 0;
  font-family: var(--mono);
  font-size: .79rem;
  line-height: 1.9;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-01__tline--i1 {
  padding-inline-start: 1.4rem;
}

.sk-01__tline--i2 {
  padding-inline-start: 2.8rem;
  color: var(--ink);
}

.sk-01__glyph {
  color: var(--faint);
  margin-inline-end: .4rem;
}

.sk-01__note {
  color: var(--accent);
  font-size: .72rem;
}

.sk-01__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-01__panel {
  display: grid;
  gap: .95rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  min-block-size: 19rem;
}

.sk-01__panel--resolved {
  opacity: .4;
}

.sk-01__panel--fallback {
  border-color: rgba(97,218,251,.28);
  box-shadow: 0 24px 60px -34px rgba(0,0,0,.8);
}

.sk-01__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-01__label--on {
  color: var(--accent);
}

.sk-01__row {
  display: flex;
  align-items: center;
  gap: .85rem;
}

.sk-01__pic {
  inline-size: 2.75rem;
  aspect-ratio: 1;
  border-radius: 999px;
  object-fit: cover;
  background: var(--sk);
}

.sk-01__ident {
  display: grid;
  gap: .4rem;
  min-inline-size: 0;
}

.sk-01__name {
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.sk-01__role {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.sk-01__copy {
  margin: 0;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-01__meta,
.sk-01__metaskel {
  margin: auto 0 0;
  padding-block-start: .9rem;
  border-block-start: 1px solid var(--line);
  display: flex;
  gap: clamp(1rem,2.4vw,2rem);
  flex-wrap: wrap;
}

.sk-01__meta div,
.sk-01__metaskel div {
  display: grid;
  gap: .35rem;
}

.sk-01__meta dt {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-01__meta dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .9rem;
  font-variant-numeric: tabular-nums;
}
/* the skeleton recipe */

.sk-01__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .85rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-01__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-01-sheen 1.4s linear infinite;
}

@keyframes sk-01-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-01__bar--xs {
  block-size: .55rem;
  inline-size: 3.4rem;
}

.sk-01__bar--sm {
  block-size: .7rem;
}

.sk-01__bar--md {
  block-size: .95rem;
  inline-size: 4.2rem;
}

.sk-01__avatar {
  inline-size: 2.75rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-01__lines {
  display: grid;
  gap: .6rem;
}

.sk-01__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-01__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-01__skey {
  min-inline-size: 3.5rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-01__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-01[data-theme="light"] {
  --bg: #fbfbfd;
  --bg2: #f2f4f8;
  --surface: rgba(9,11,20,.025);
  --line: rgba(9,11,20,.1);
  --ink: #0b0d14;
  --muted: rgba(11,13,20,.62);
  --faint: rgba(11,13,20,.44);
  --accent: #0873a8;
  background: radial-gradient(70% 50% at 78% -6%, rgba(8,115,168,.08) 0%, transparent 62%), linear-gradient(178deg,#fff 0%,#f2f4f8 70%);
}

@media (prefers-color-scheme: light) {
  .sk-01:not([data-theme="dark"]) {
    --bg: #fbfbfd;
    --bg2: #f2f4f8;
    --surface: rgba(9,11,20,.025);
    --line: rgba(9,11,20,.1);
    --ink: #0b0d14;
    --muted: rgba(11,13,20,.62);
    --faint: rgba(11,13,20,.44);
    --accent: #0873a8;
    background: radial-gradient(70% 50% at 78% -6%, rgba(8,115,168,.08) 0%, transparent 62%), linear-gradient(178deg,#fff 0%,#f2f4f8 70%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-01__bar::after {
    animation: none;
    background: none;
  }

  .sk-01__bar {
    background: var(--sheen);
  }
}

@media (forced-colors: active) {
  .sk-01__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-01__bar::after {
    animation: none;
    background: none;
  }

  .sk-01__panel,
    .sk-01__tree,
    .sk-01__spec,
    .sk-01__code {
    border-color: CanvasText;
  }
}
```
