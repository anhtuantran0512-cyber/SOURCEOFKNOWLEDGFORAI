---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/pulse-block/"
title: "Pulse Block Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The cheapest credible loading animation there is: one opacity keyframe, 100% → 40% → 100%."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulse Block Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/pulse-block/

The cheapest credible loading animation there is: one opacity keyframe, 100% → 40% → 100%. No gradient, no extra layer, nothing to repaint — the compositor handles it alone, which is why it is the right default on low-end mobile and inside long virtualised lists.
## HTML
```html
<div class="sk-12">
  <div class="sk-12__stage">
    <section class="sk-12__wrap" aria-labelledby="sk-12-h">
      <header class="sk-12__head">
        <p class="sk-12__eyebrow">opacity · 1800ms</p>
        <h2 class="sk-12__h" id="sk-12-h">The cheapest credible loading animation</h2>
        <p class="sk-12__sub">One keyframe on one compositor-only property. No gradient layer, no repaint — the default when there are more than a dozen placeholders on screen.</p>
      </header>

      <div class="sk-12__cols">
        <article class="sk-12__panel" role="status" aria-live="polite">
          <span class="sk-12__vh">Loading report block…</span>
          <p class="sk-12__label sk-12__label--on">pulse · group animation</p>
          <div class="sk-12__group" aria-hidden="true">
            <span class="sk-12__bar sk-12__bar--hero"></span>
            <span class="sk-12__bar sk-12__bar--title"></span>
            <span class="sk-12__bar"></span>
            <span class="sk-12__bar" style="inline-size:78%"></span>
            <span class="sk-12__bar" style="inline-size:46%"></span>
          </div>
          <p class="sk-12__note">One animation on the container — one composited layer for the whole card, however many bars it holds.</p>
        </article>

        <article class="sk-12__panel" role="status" aria-live="polite">
          <span class="sk-12__vh">Loading list, staggered pulse…</span>
          <p class="sk-12__label">pulse · staggered per row</p>
          <ul class="sk-12__rows" aria-hidden="true">
            <li class="sk-12__row" style="--i:0"><span class="sk-12__bar sk-12__bar--dot"></span><span class="sk-12__bar"></span></li>
            <li class="sk-12__row" style="--i:1"><span class="sk-12__bar sk-12__bar--dot"></span><span class="sk-12__bar" style="inline-size:84%"></span></li>
            <li class="sk-12__row" style="--i:2"><span class="sk-12__bar sk-12__bar--dot"></span><span class="sk-12__bar" style="inline-size:72%"></span></li>
            <li class="sk-12__row" style="--i:3"><span class="sk-12__bar sk-12__bar--dot"></span><span class="sk-12__bar" style="inline-size:90%"></span></li>
            <li class="sk-12__row" style="--i:4"><span class="sk-12__bar sk-12__bar--dot"></span><span class="sk-12__bar" style="inline-size:66%"></span></li>
          </ul>
          <p class="sk-12__note">A 120ms delay ramp reads as a cascade. Costs one layer per row — use it when the rhythm earns the frames.</p>
        </article>
      </div>

      <aside class="sk-12__compare" aria-label="Pulse versus shimmer">
        <p class="sk-12__crow"><span class="sk-12__ckey">pulse</span><span class="sk-12__cval">opacity only · no extra layer · scales to hundreds of bars · says “waiting”</span></p>
        <p class="sk-12__crow"><span class="sk-12__ckey">shimmer</span><span class="sk-12__cval">gradient sweep · one extra layer per bar · best on a single focal block · says “progress”</span></p>
        <p class="sk-12__crow"><span class="sk-12__ckey">verdict</span><span class="sk-12__cval">pulse for lists, tables and mobile; shimmer for one hero surface</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-12 {
  --bg: #05080a;
  --bg2: #0b1114;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #eff6f8;
  --muted: rgba(239,246,248,.62);
  --faint: rgba(239,246,248,.42);
  --accent: #67e8f9;
  --sk: rgba(239,246,248,.13);
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
  background: radial-gradient(60% 42% at 82% -6%, rgba(103,232,249,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-12 *,
.sk-12 *::before,
.sk-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 200)) {
  .sk-12 {
    --ink: oklch(0.97 0.01 205);
    --muted: oklch(0.97 0.01 205 / .62);
    --faint: oklch(0.97 0.01 205 / .42);
    --accent: oklch(0.86 0.11 200);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-12 {
    --sk: color-mix(in oklab, currentColor 13%, transparent);
  }
}

.sk-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-12__wrap {
  inline-size: min(70rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-12__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 45rem;
}

.sk-12__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-12__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-12__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-12__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-12__panel {
  display: grid;
  gap: .8rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
}

.sk-12__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-12__label--on {
  color: var(--accent);
}

.sk-12__note {
  margin: auto 0 0;
  padding-block-start: .8rem;
  border-block-start: 1px solid var(--line);
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-12__bar {
  display: block;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-12__bar--title {
  block-size: 1.35rem;
  inline-size: 68%;
  border-radius: 8px;
}

.sk-12__bar--hero {
  block-size: auto;
  aspect-ratio: 16/6;
  border-radius: 10px;
  margin-block-end: .2rem;
}

.sk-12__bar--dot {
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: 999px;
  flex: none;
}

@keyframes sk-12-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .4;
  }
}

.sk-12__group {
  display: grid;
  gap: .7rem;
  animation: sk-12-pulse 1800ms cubic-bezier(.4,0,.6,1) infinite;
}

.sk-12__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .7rem;
}

.sk-12__row {
  display: flex;
  align-items: center;
  gap: .8rem;
  animation: sk-12-pulse 1800ms cubic-bezier(.4,0,.6,1) infinite;
  animation-delay: calc(var(--i,0) * 120ms);
}

.sk-12__compare {
  padding: clamp(.9rem,1.6vw,1.2rem) clamp(1rem,1.8vw,1.35rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .5rem;
}

.sk-12__crow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.55;
}

.sk-12__ckey {
  min-inline-size: 4.4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-12__cval {
  color: var(--muted);
  word-break: break-word;
}

.sk-12[data-theme="light"] {
  --bg: #f6fafb;
  --bg2: #fff;
  --surface: rgba(4,16,20,.026);
  --line: rgba(4,16,20,.11);
  --ink: #041014;
  --muted: rgba(4,16,20,.62);
  --faint: rgba(4,16,20,.44);
  --accent: #0e7490;
  background: linear-gradient(178deg,#fff 0%,#e9f4f7 100%);
}

@media (prefers-color-scheme: light) {
  .sk-12:not([data-theme="dark"]) {
    --bg: #f6fafb;
    --bg2: #fff;
    --surface: rgba(4,16,20,.026);
    --line: rgba(4,16,20,.11);
    --ink: #041014;
    --muted: rgba(4,16,20,.62);
    --faint: rgba(4,16,20,.44);
    --accent: #0e7490;
    background: linear-gradient(178deg,#fff 0%,#e9f4f7 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-12__group,
    .sk-12__row {
    animation: none;
    opacity: .72;
  }
}

@media (forced-colors: active) {
  .sk-12__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-12__group,
    .sk-12__row {
    animation: none;
    opacity: 1;
  }

  .sk-12__panel,
    .sk-12__compare {
    border-color: CanvasText;
  }
}
```
