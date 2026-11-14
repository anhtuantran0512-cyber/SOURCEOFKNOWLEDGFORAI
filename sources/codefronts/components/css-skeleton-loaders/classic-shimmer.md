---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/classic-shimmer/"
title: "Classic Shimmer Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The reference shimmer, written the canonical way: a three-stop linear-gradient at 200% width, moved with background-position."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Shimmer Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/classic-shimmer/

The reference shimmer, written the canonical way: a three-stop linear-gradient at 200% width, moved with background-position. This is the version every tutorial teaches — so the demo also shows the compositor-friendly variant beside it and names the exact trade-off between them.
## HTML
```html
<div class="sk-11">
  <div class="sk-11__stage">
    <section class="sk-11__wrap" aria-labelledby="sk-11-h">
      <header class="sk-11__head">
        <p class="sk-11__eyebrow">the reference shimmer</p>
        <h2 class="sk-11__h" id="sk-11-h">One oversized gradient, one moving offset</h2>
        <p class="sk-11__sub">Both panels look identical at 1400ms. The left one repaints each frame; the right one runs on the compositor. Pick by bar count.</p>
      </header>

      <div class="sk-11__cols">
        <article class="sk-11__panel" role="status" aria-live="polite">
          <span class="sk-11__vh">Loading, canonical shimmer…</span>
          <p class="sk-11__label sk-11__label--on">background-position</p>
          <div class="sk-11__bars" aria-hidden="true">
            <span class="sk-11__bar sk-11__bar--hero"></span>
            <span class="sk-11__bar sk-11__bar--title"></span>
            <span class="sk-11__bar"></span>
            <span class="sk-11__bar" style="inline-size:82%"></span>
            <span class="sk-11__bar" style="inline-size:54%"></span>
          </div>
          <p class="sk-11__note">Canonical and short. Each frame repaints the element — invisible at this scale, measurable across a 40-row table.</p>
        </article>

        <article class="sk-11__panel" role="status" aria-live="polite">
          <span class="sk-11__vh">Loading, compositor shimmer…</span>
          <p class="sk-11__label">translate on ::after</p>
          <div class="sk-11__bars" aria-hidden="true">
            <span class="sk-11__bar sk-11__bar--gpu sk-11__bar--hero"></span>
            <span class="sk-11__bar sk-11__bar--gpu sk-11__bar--title"></span>
            <span class="sk-11__bar sk-11__bar--gpu"></span>
            <span class="sk-11__bar sk-11__bar--gpu" style="inline-size:82%"></span>
            <span class="sk-11__bar sk-11__bar--gpu" style="inline-size:54%"></span>
          </div>
          <p class="sk-11__note">Same 1400ms sweep, zero repaint. The one to reach for in feeds, tables and anything virtualised.</p>
        </article>
      </div>

      <aside class="sk-11__spec" aria-label="Recipe">
        <p class="sk-11__srow"><span class="sk-11__skey">gradient</span><span class="sk-11__sval">linear-gradient(100deg, --sk 20%, --sheen 42%, --sheen 58%, --sk 80%)</span></p>
        <p class="sk-11__srow"><span class="sk-11__skey">size</span><span class="sk-11__sval">background-size: 200% 100% — room to travel off both edges, no seam</span></p>
        <p class="sk-11__srow"><span class="sk-11__skey">loop</span><span class="sk-11__sval">@keyframes: background-position 200% 0 → -100% 0 · 1.4s linear infinite</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-11 {
  --bg: #07080b;
  --bg2: #0e1017;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f4f6fb;
  --muted: rgba(244,246,251,.62);
  --faint: rgba(244,246,251,.42);
  --accent: #c4b5fd;
  --sk: rgba(244,246,251,.09);
  --sheen: rgba(244,246,251,.2);
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
  background: radial-gradient(58% 42% at 50% -8%, rgba(196,181,253,.13) 0%, transparent 62%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-11 *,
.sk-11 *::before,
.sk-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 290)) {
  .sk-11 {
    --ink: oklch(0.97 0.006 285);
    --muted: oklch(0.97 0.006 285 / .62);
    --faint: oklch(0.97 0.006 285 / .42);
    --accent: oklch(0.84 0.09 295);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-11 {
    --sk: color-mix(in oklab, currentColor 9%, transparent);
    --sheen: color-mix(in oklab, currentColor 20%, transparent);
  }
}

.sk-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-11__wrap {
  inline-size: min(70rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-11__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 45rem;
}

.sk-11__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-11__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-11__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-11__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-11__panel {
  display: grid;
  gap: .8rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
}

.sk-11__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-11__label--on {
  color: var(--accent);
}

.sk-11__bars {
  display: grid;
  gap: .7rem;
  margin-block: .2rem;
}

.sk-11__note {
  margin: auto 0 0;
  padding-block-start: .8rem;
  border-block-start: 1px solid var(--line);
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-11__bar {
  display: block;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  overflow: hidden;
  background-color: var(--sk);
  background-image: linear-gradient(100deg, var(--sk) 20%, var(--sheen) 42%, var(--sheen) 58%, var(--sk) 80%);
  background-size: 200% 100%;
  background-position: 200% 0;
  background-repeat: no-repeat;
  animation: sk-11-shimmer 1.4s linear infinite;
}

@keyframes sk-11-shimmer {
  to {
    background-position: -100% 0;
  }
}

.sk-11__bar--title {
  block-size: 1.35rem;
  inline-size: 70%;
  border-radius: 8px;
}

.sk-11__bar--hero {
  block-size: auto;
  aspect-ratio: 16/6;
  border-radius: 10px;
  margin-block-end: .2rem;
}

.sk-11__bar--gpu {
  position: relative;
  background-image: none;
  animation: none;
}

.sk-11__bar--gpu::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-11-sweep 1.4s linear infinite;
}

@keyframes sk-11-sweep {
  to {
    translate: 100% 0;
  }
}

.sk-11__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-11__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-11__skey {
  min-inline-size: 4.6rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-11__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-11[data-theme="light"] {
  --bg: #f8f8fc;
  --bg2: #fff;
  --surface: rgba(10,10,24,.026);
  --line: rgba(10,10,24,.11);
  --ink: #0a0a18;
  --muted: rgba(10,10,24,.62);
  --faint: rgba(10,10,24,.44);
  --accent: #6d28d9;
  background: linear-gradient(178deg,#fff 0%,#eeedf8 100%);
}

@media (prefers-color-scheme: light) {
  .sk-11:not([data-theme="dark"]) {
    --bg: #f8f8fc;
    --bg2: #fff;
    --surface: rgba(10,10,24,.026);
    --line: rgba(10,10,24,.11);
    --ink: #0a0a18;
    --muted: rgba(10,10,24,.62);
    --faint: rgba(10,10,24,.44);
    --accent: #6d28d9;
    background: linear-gradient(178deg,#fff 0%,#eeedf8 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-11__bar {
    animation: none;
    background-position: 50% 0;
  }

  .sk-11__bar--gpu::after {
    animation: none;
    background: none;
  }

  .sk-11__bar--gpu {
    background-image: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-11__bar {
    background: GrayText;
    background-image: none;
    animation: none;
    forced-color-adjust: none;
  }

  .sk-11__bar--gpu::after {
    animation: none;
    background: none;
  }

  .sk-11__panel,
    .sk-11__spec {
    border-color: CanvasText;
  }
}
```
