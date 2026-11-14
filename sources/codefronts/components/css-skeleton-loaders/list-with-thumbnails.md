---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/list-with-thumbnails/"
title: "Media List Skeleton with Thumbnails"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The queue pattern from YouTube, Spotify and every podcast app: five rows, each a 64px square thumbnail plus a title line and a metadata line, with a duration…"
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media List Skeleton with Thumbnails
Source: https://codefronts.com/components/css-skeleton-loaders/list-with-thumbnails/

The queue pattern from YouTube, Spotify and every podcast app: five rows, each a 64px square thumbnail plus a title line and a metadata line, with a duration pill on the right. Rows are a real <ul>, the thumbnail is a fixed square, and the staggered sheen fills the list from the top.
## HTML
```html
<div class="sk-21">
  <div class="sk-21__stage">
    <section class="sk-21__wrap" aria-labelledby="sk-21-h">
      <header class="sk-21__head">
        <p class="sk-21__eyebrow">--thumb: 4rem · 5 rows</p>
        <h2 class="sk-21__h" id="sk-21-h">Fixed thumbnail, fluid title, fixed duration</h2>
        <p class="sk-21__sub">Three columns and only one of them flexes. The middle column carries <code>min-inline-size: 0</code> so a long title can never push the duration pill off the row.</p>
      </header>

      <div class="sk-21__panel">
        <div class="sk-21__phead">
          <p class="sk-21__ptitle">Up next</p>
          <p class="sk-21__pmeta">5 episodes · loading</p>
        </div>

        <ul class="sk-21__list" role="status" aria-live="polite">
          <span class="sk-21__vh">Loading 5 episodes…</span>
          <li class="sk-21__row" style="--i:0" aria-hidden="true">
            <span class="sk-21__bar sk-21__thumb"></span>
            <div class="sk-21__mid"><span class="sk-21__bar sk-21__bar--t"></span><span class="sk-21__bar sk-21__bar--m"></span></div>
            <span class="sk-21__bar sk-21__dur"></span>
          </li>
          <li class="sk-21__row" style="--i:1" aria-hidden="true">
            <span class="sk-21__bar sk-21__thumb"></span>
            <div class="sk-21__mid"><span class="sk-21__bar sk-21__bar--t" style="inline-size:68%"></span><span class="sk-21__bar sk-21__bar--m" style="inline-size:46%"></span></div>
            <span class="sk-21__bar sk-21__dur"></span>
          </li>
          <li class="sk-21__row" style="--i:2" aria-hidden="true">
            <span class="sk-21__bar sk-21__thumb"></span>
            <div class="sk-21__mid"><span class="sk-21__bar sk-21__bar--t" style="inline-size:90%"></span><span class="sk-21__bar sk-21__bar--m" style="inline-size:62%"></span></div>
            <span class="sk-21__bar sk-21__dur"></span>
          </li>
          <li class="sk-21__row" style="--i:3" aria-hidden="true">
            <span class="sk-21__bar sk-21__thumb"></span>
            <div class="sk-21__mid"><span class="sk-21__bar sk-21__bar--t" style="inline-size:74%"></span><span class="sk-21__bar sk-21__bar--m" style="inline-size:52%"></span></div>
            <span class="sk-21__bar sk-21__dur"></span>
          </li>
          <li class="sk-21__row" style="--i:4" aria-hidden="true">
            <span class="sk-21__bar sk-21__thumb"></span>
            <div class="sk-21__mid"><span class="sk-21__bar sk-21__bar--t" style="inline-size:84%"></span><span class="sk-21__bar sk-21__bar--m" style="inline-size:40%"></span></div>
            <span class="sk-21__bar sk-21__dur"></span>
          </li>
        </ul>

        <hr class="sk-21__rule">

        <ul class="sk-21__list">
          <li class="sk-21__row">
            <img class="sk-21__pic" src="https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?auto=format&amp;fit=crop&amp;w=128&amp;h=128&amp;q=70" width="128" height="128" alt="Autumn leaves" loading="lazy" decoding="async">
            <div class="sk-21__mid">
              <p class="sk-21__rt">Loading states that don't lie</p>
              <p class="sk-21__rm">Interface Notes · Priya Sharma</p>
            </div>
            <p class="sk-21__rd">42:18</p>
          </li>
        </ul>
      </div>

      <aside class="sk-21__spec" aria-label="Recipe">
        <p class="sk-21__srow"><span class="sk-21__skey">row</span><span class="sk-21__sval">flex · thumb flex:none · mid flex:1 min-inline-size:0 · duration flex:none</span></p>
        <p class="sk-21__srow"><span class="sk-21__skey">thumb</span><span class="sk-21__sval">inline-size: var(--thumb); aspect-ratio: 1 — one token for both states</span></p>
        <p class="sk-21__srow"><span class="sk-21__skey">stagger</span><span class="sk-21__sval">animation-delay: calc(var(--i) * -.18s) — fills downward, nothing waits</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-21 {
  --thumb: 4rem;
  --bg: #08070a;
  --bg2: #0f0e13;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f5f4f7;
  --muted: rgba(245,244,247,.62);
  --faint: rgba(245,244,247,.42);
  --accent: #f472b6;
  --sk: rgba(245,244,247,.1);
  --sheen: rgba(245,244,247,.17);
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
  background: radial-gradient(56% 40% at 84% -6%, rgba(244,114,182,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-21 *,
.sk-21 *::before,
.sk-21 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 350)) {
  .sk-21 {
    --ink: oklch(0.97 0.004 320);
    --muted: oklch(0.97 0.004 320 / .62);
    --faint: oklch(0.97 0.004 320 / .42);
    --accent: oklch(0.76 0.15 350);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-21 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-21__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-21__wrap {
  inline-size: min(56rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-21__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
}

.sk-21__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-21__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.4rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.07;
  text-wrap: balance;
}

.sk-21__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-21__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-21__panel {
  display: grid;
  gap: 1rem;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  box-shadow: 0 28px 66px -46px rgba(0,0,0,.9);
}

.sk-21__phead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.sk-21__ptitle {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.sk-21__pmeta {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-21__rule {
  margin: .2rem 0;
  border: 0;
  border-block-start: 1px solid var(--line);
}

.sk-21__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .9rem;
}

.sk-21__row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.sk-21__mid {
  flex: 1;
  min-inline-size: 0;
  display: grid;
  gap: .5rem;
}

.sk-21__pic {
  inline-size: var(--thumb);
  aspect-ratio: 1;
  border-radius: .65rem;
  object-fit: cover;
  background: var(--sk);
  flex: none;
}

.sk-21__rt {
  margin: 0;
  font-size: .98rem;
  font-weight: 500;
  letter-spacing: -.012em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-21__rm {
  margin: 0;
  font-size: .83rem;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-21__rd {
  margin: 0;
  flex: none;
  font-family: var(--mono);
  font-size: .78rem;
  font-variant-numeric: tabular-nums;
  color: var(--faint);
}

.sk-21__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-21__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-21-sheen 1.4s linear infinite;
  animation-delay: calc(var(--i,0) * -.18s);
}

@keyframes sk-21-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-21__bar--t {
  block-size: .85rem;
  inline-size: 82%;
}

.sk-21__bar--m {
  block-size: .68rem;
  inline-size: 54%;
}

.sk-21__thumb {
  inline-size: var(--thumb);
  block-size: auto;
  aspect-ratio: 1;
  border-radius: .65rem;
  flex: none;
}

.sk-21__dur {
  inline-size: 2.8rem;
  block-size: .7rem;
  flex: none;
}

.sk-21__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-21__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-21__skey {
  min-inline-size: 4.2rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-21__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-21[data-theme="light"] {
  --bg: #fbf8fa;
  --bg2: #fff;
  --surface: #ffffff;
  --line: rgba(14,10,12,.11);
  --ink: #0e0a0c;
  --muted: rgba(14,10,12,.62);
  --faint: rgba(14,10,12,.44);
  --accent: #be185d;
  background: linear-gradient(178deg,#fff 0%,#f6eef2 100%);
}

@media (prefers-color-scheme: light) {
  .sk-21:not([data-theme="dark"]) {
    --bg: #fbf8fa;
    --bg2: #fff;
    --surface: #ffffff;
    --line: rgba(14,10,12,.11);
    --ink: #0e0a0c;
    --muted: rgba(14,10,12,.62);
    --faint: rgba(14,10,12,.44);
    --accent: #be185d;
    background: linear-gradient(178deg,#fff 0%,#f6eef2 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-21__bar::after {
    animation: none;
    background: none;
  }

  .sk-21__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-21__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-21__bar::after {
    animation: none;
    background: none;
  }

  .sk-21__panel,
    .sk-21__spec {
    border-color: CanvasText;
  }
}
```
