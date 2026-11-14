---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/stat-tiles/"
title: "Stat Tiles Dashboard Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The dashboard hero row: four KPI tiles where the labels are real (\"Users\", \"Revenue\", \"Sessions\", \"Conversion Rate\") and only the numbers are pending."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stat Tiles Dashboard Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/stat-tiles/

The dashboard hero row: four KPI tiles where the labels are real ("Users", "Revenue", "Sessions", "Conversion Rate") and only the numbers are pending. Keeping the labels means the user can read the dashboard's shape immediately — and the tile never resizes, because a tabular-figures number occupies a predictable box.
## HTML
```html
<div class="sk-19">
  <div class="sk-19__stage">
    <section class="sk-19__wrap" aria-labelledby="sk-19-h">
      <header class="sk-19__head">
        <p class="sk-19__eyebrow">dashboard hero row</p>
        <h2 class="sk-19__h" id="sk-19-h">Skeleton the value. Keep the label.</h2>
        <p class="sk-19__sub">Labels come from your config, not the API — they should paint instantly. Only the figure, the delta and the sparkline are unknown.</p>
      </header>

      <div class="sk-19__grid" role="status" aria-live="polite">
        <span class="sk-19__vh">Loading four dashboard metrics…</span>
        <article class="sk-19__tile" style="--i:0">
          <p class="sk-19__label">Users</p>
          <span class="sk-19__bar sk-19__bar--num" aria-hidden="true"></span>
          <div class="sk-19__trend" aria-hidden="true"><span class="sk-19__bar sk-19__bar--chip"></span><span class="sk-19__bar sk-19__bar--since"></span></div>
          <span class="sk-19__bar sk-19__bar--spark" aria-hidden="true"></span>
        </article>
        <article class="sk-19__tile" style="--i:1">
          <p class="sk-19__label">Revenue</p>
          <span class="sk-19__bar sk-19__bar--num" aria-hidden="true"></span>
          <div class="sk-19__trend" aria-hidden="true"><span class="sk-19__bar sk-19__bar--chip"></span><span class="sk-19__bar sk-19__bar--since"></span></div>
          <span class="sk-19__bar sk-19__bar--spark" aria-hidden="true"></span>
        </article>
        <article class="sk-19__tile" style="--i:2">
          <p class="sk-19__label">Sessions</p>
          <span class="sk-19__bar sk-19__bar--num" aria-hidden="true"></span>
          <div class="sk-19__trend" aria-hidden="true"><span class="sk-19__bar sk-19__bar--chip"></span><span class="sk-19__bar sk-19__bar--since"></span></div>
          <span class="sk-19__bar sk-19__bar--spark" aria-hidden="true"></span>
        </article>
        <article class="sk-19__tile" style="--i:3">
          <p class="sk-19__label">Conversion Rate</p>
          <span class="sk-19__bar sk-19__bar--num" aria-hidden="true"></span>
          <div class="sk-19__trend" aria-hidden="true"><span class="sk-19__bar sk-19__bar--chip"></span><span class="sk-19__bar sk-19__bar--since"></span></div>
          <span class="sk-19__bar sk-19__bar--spark" aria-hidden="true"></span>
        </article>
      </div>

      <article class="sk-19__tile sk-19__tile--real">
        <p class="sk-19__label">Revenue <span class="sk-19__resolved">resolved, same box</span></p>
        <p class="sk-19__value">$248,910</p>
        <div class="sk-19__trend">
          <p class="sk-19__delta">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19V6m0 0-5.2 5.2M12 6l5.2 5.2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            12.4%
          </p>
          <p class="sk-19__since">vs. previous 30 days</p>
        </div>
      </article>

      <aside class="sk-19__spec" aria-label="Recipe">
        <p class="sk-19__srow"><span class="sk-19__skey">grid</span><span class="sk-19__sval">repeat(auto-fit, minmax(13rem, 1fr)) — 4-up to 1-up, no breakpoints</span></p>
        <p class="sk-19__srow"><span class="sk-19__skey">number</span><span class="sk-19__sval">block-size 2.1rem · inline-size min(8ch, 70%) — sized from the real figure</span></p>
        <p class="sk-19__srow"><span class="sk-19__skey">chart</span><span class="sk-19__sval">aspect-ratio on the sparkline — the top dashboard CLS fix</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-19 {
  --bg: #060708;
  --bg2: #0d0f11;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f5f6f7;
  --muted: rgba(245,246,247,.62);
  --faint: rgba(245,246,247,.42);
  --accent: #34d399;
  --sk: rgba(245,246,247,.1);
  --sheen: rgba(245,246,247,.17);
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
  background: radial-gradient(56% 40% at 24% -6%, rgba(52,211,153,.11) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-19 *,
.sk-19 *::before,
.sk-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 160)) {
  .sk-19 {
    --ink: oklch(0.97 0.003 200);
    --muted: oklch(0.97 0.003 200 / .62);
    --faint: oklch(0.97 0.003 200 / .42);
    --accent: oklch(0.8 0.13 162);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-19 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-19__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-19__wrap {
  inline-size: min(76rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-19__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
}

.sk-19__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-19__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-19__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-19__grid {
  display: grid;
  gap: clamp(.8rem,1.6vw,1.1rem);
  grid-template-columns: repeat(auto-fit,minmax(13rem,1fr));
}

.sk-19__tile {
  display: grid;
  gap: .85rem;
  align-content: start;
  padding: clamp(1rem,1.9vw,1.35rem);
  border: 1px solid var(--line);
  border-radius: 1.05rem;
  background: var(--surface);
  min-block-size: 12rem;
}

.sk-19__tile--real {
  max-inline-size: 20rem;
  border-color: rgba(52,211,153,.32);
}

.sk-19__label {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-19__resolved {
  padding: .14rem .4rem;
  border-radius: .35rem;
  background: rgba(52,211,153,.16);
  color: var(--accent);
  letter-spacing: .06em;
}

.sk-19__value {
  margin: 0;
  font-size: clamp(1.9rem,3.6vw,2.3rem);
  font-weight: 600;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.sk-19__trend {
  display: flex;
  align-items: center;
  gap: .65rem;
  flex-wrap: wrap;
}

.sk-19__delta {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .25rem;
  padding: .22rem .5rem;
  border-radius: .4rem;
  background: rgba(52,211,153,.14);
  color: var(--accent);
  font-family: var(--mono);
  font-size: .75rem;
  font-variant-numeric: tabular-nums;
}

.sk-19__delta svg {
  inline-size: .85rem;
  block-size: .85rem;
}

.sk-19__since {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--faint);
}

.sk-19__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-19__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-19-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.2s);
}

@keyframes sk-19-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-19__bar--num {
  block-size: 2.1rem;
  inline-size: min(8ch,70%);
  border-radius: 8px;
}

.sk-19__bar--chip {
  inline-size: 3.6rem;
  block-size: 1.35rem;
  border-radius: .4rem;
}

.sk-19__bar--since {
  inline-size: 7rem;
  block-size: .65rem;
}

.sk-19__bar--spark {
  margin-block-start: auto;
  block-size: auto;
  aspect-ratio: 16/5;
  border-radius: 8px;
}

.sk-19__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-19__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-19__skey {
  min-inline-size: 4.2rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-19__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-19[data-theme="light"] {
  --bg: #f7f9f8;
  --bg2: #fff;
  --surface: #ffffff;
  --line: rgba(8,12,10,.11);
  --ink: #080c0a;
  --muted: rgba(8,12,10,.62);
  --faint: rgba(8,12,10,.44);
  --accent: #047857;
  background: linear-gradient(178deg,#fff 0%,#edf3f0 100%);
}

@media (prefers-color-scheme: light) {
  .sk-19:not([data-theme="dark"]) {
    --bg: #f7f9f8;
    --bg2: #fff;
    --surface: #ffffff;
    --line: rgba(8,12,10,.11);
    --ink: #080c0a;
    --muted: rgba(8,12,10,.62);
    --faint: rgba(8,12,10,.44);
    --accent: #047857;
    background: linear-gradient(178deg,#fff 0%,#edf3f0 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-19__bar::after {
    animation: none;
    background: none;
  }

  .sk-19__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-19__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-19__bar::after {
    animation: none;
    background: none;
  }

  .sk-19__tile,
    .sk-19__spec {
    border-color: CanvasText;
  }
}
```
