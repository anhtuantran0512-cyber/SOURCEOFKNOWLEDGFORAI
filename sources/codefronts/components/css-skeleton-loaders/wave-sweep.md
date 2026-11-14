---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/wave-sweep/"
title: "Wave Sweep Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A shimmer with a shaped leading edge."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wave Sweep Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/wave-sweep/

A shimmer with a shaped leading edge. Instead of a straight-edged gradient, an inline SVG wave becomes the sweep's mask-image, so the highlight arrives as a soft crest rather than a bar wiping past — the softer, more expensive-feeling loading state used on premium product surfaces.
## HTML
```html
<div class="sk-15">
  <div class="sk-15__stage">
    <section class="sk-15__wrap" aria-labelledby="sk-15-h">
      <header class="sk-15__head">
        <p class="sk-15__eyebrow">mask-image · SVG crest</p>
        <h2 class="sk-15__h" id="sk-15-h">Give the highlight a shape, not an edge</h2>
        <p class="sk-15__sub">The sweep is a plain gradient. The wave lives in its mask — one inline SVG path, zero requests, and a softer arrival than any straight-edged shimmer.</p>
      </header>

      <div class="sk-15__cols">
        <article class="sk-15__panel" role="status" aria-live="polite">
          <span class="sk-15__vh">Loading, long wave…</span>
          <p class="sk-15__label sk-15__label--on">mask-size: 120% — one lazy crest</p>
          <div class="sk-15__bars" aria-hidden="true">
            <span class="sk-15__bar sk-15__bar--soft sk-15__bar--hero"></span>
            <span class="sk-15__bar sk-15__bar--soft sk-15__bar--title"></span>
            <span class="sk-15__bar sk-15__bar--soft"></span>
            <span class="sk-15__bar sk-15__bar--soft" style="inline-size:78%"></span>
            <span class="sk-15__bar sk-15__bar--soft" style="inline-size:48%"></span>
          </div>
          <p class="sk-15__note">A single crest crossing the bar. Calm, premium, and the version to reach for on a hero surface.</p>
        </article>

        <article class="sk-15__panel" role="status" aria-live="polite">
          <span class="sk-15__vh">Loading, tight ripples…</span>
          <p class="sk-15__label">mask-size: 35% — several ripples</p>
          <div class="sk-15__bars" aria-hidden="true">
            <span class="sk-15__bar sk-15__bar--tight sk-15__bar--hero"></span>
            <span class="sk-15__bar sk-15__bar--tight sk-15__bar--title"></span>
            <span class="sk-15__bar sk-15__bar--tight"></span>
            <span class="sk-15__bar sk-15__bar--tight" style="inline-size:78%"></span>
            <span class="sk-15__bar sk-15__bar--tight" style="inline-size:48%"></span>
          </div>
          <p class="sk-15__note">More energy per pass. Reads well on small bars, busier than you want behind long-form text.</p>
        </article>
      </div>

      <aside class="sk-15__spec" aria-label="Recipe">
        <p class="sk-15__srow"><span class="sk-15__skey">mask</span><span class="sk-15__sval">mask-image: url("data:image/svg+xml,…%23fff…") — encode # as %23</span></p>
        <p class="sk-15__srow"><span class="sk-15__skey">tile</span><span class="sk-15__sval">mask-size: 60% 100% + mask-repeat: repeat-x — seamless at any width</span></p>
        <p class="sk-15__srow"><span class="sk-15__skey">gate</span><span class="sk-15__sval">@supports (mask-image: url("")) → plain linear sweep as the fallback</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-15 {
  --bg: #050710;
  --bg2: #0b0f1e;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f1f4fd;
  --muted: rgba(241,244,253,.62);
  --faint: rgba(241,244,253,.42);
  --accent: #93c5fd;
  --sk: rgba(241,244,253,.09);
  --sheen: rgba(241,244,253,.24);
  --wave: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 40' preserveAspectRatio='none'%3E%3Cpath d='M0 24C15 8 30 8 45 24S75 40 90 24s15-16 30 0V40H0Z' fill='%23fff'/%3E%3C/svg%3E");
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
  background: radial-gradient(60% 45% at 30% -8%, rgba(147,197,253,.14) 0%, transparent 62%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-15 *,
.sk-15 *::before,
.sk-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 250)) {
  .sk-15 {
    --ink: oklch(0.97 0.008 255);
    --muted: oklch(0.97 0.008 255 / .62);
    --faint: oklch(0.97 0.008 255 / .42);
    --accent: oklch(0.83 0.1 250);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-15 {
    --sk: color-mix(in oklab, currentColor 9%, transparent);
    --sheen: color-mix(in oklab, currentColor 24%, transparent);
  }
}

.sk-15__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-15__wrap {
  inline-size: min(70rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-15__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 45rem;
}

.sk-15__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-15__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-15__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-15__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-15__panel {
  display: grid;
  gap: .8rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
}

.sk-15__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-15__label--on {
  color: var(--accent);
}

.sk-15__bars {
  display: grid;
  gap: .7rem;
  margin-block: .2rem;
}

.sk-15__note {
  margin: auto 0 0;
  padding-block-start: .8rem;
  border-block-start: 1px solid var(--line);
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-15__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .85rem;
  inline-size: 100%;
  border-radius: 7px;
  background: var(--sk);
}

.sk-15__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 5%, var(--sheen) 50%, transparent 95%);
  translate: -100% 0;
  animation: sk-15-wave 1.6s linear infinite;
}

@keyframes sk-15-wave {
  to {
    translate: 100% 0;
  }
}

@supports ((mask-image: url("")) or (-webkit-mask-image: url(""))) {
  .sk-15__bar::after {
    -webkit-mask-image: var(--wave);
    mask-image: var(--wave);
    -webkit-mask-repeat: repeat-x;
    mask-repeat: repeat-x;
    -webkit-mask-size: 60% 100%;
    mask-size: 60% 100%;
  }

  .sk-15__bar--soft::after {
    -webkit-mask-size: 120% 100%;
    mask-size: 120% 100%;
  }

  .sk-15__bar--tight::after {
    -webkit-mask-size: 35% 100%;
    mask-size: 35% 100%;
  }
}

.sk-15__bar--title {
  block-size: 1.35rem;
  inline-size: 68%;
  border-radius: 9px;
}

.sk-15__bar--hero {
  block-size: auto;
  aspect-ratio: 16/6;
  border-radius: 12px;
  margin-block-end: .2rem;
}

.sk-15__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-15__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-15__skey {
  min-inline-size: 3.4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-15__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-15[data-theme="light"] {
  --bg: #f7f9fe;
  --bg2: #fff;
  --surface: rgba(8,12,28,.026);
  --line: rgba(8,12,28,.11);
  --ink: #080c1c;
  --muted: rgba(8,12,28,.62);
  --faint: rgba(8,12,28,.44);
  --accent: #1d4ed8;
  background: linear-gradient(178deg,#fff 0%,#ecf0fb 100%);
}

@media (prefers-color-scheme: light) {
  .sk-15:not([data-theme="dark"]) {
    --bg: #f7f9fe;
    --bg2: #fff;
    --surface: rgba(8,12,28,.026);
    --line: rgba(8,12,28,.11);
    --ink: #080c1c;
    --muted: rgba(8,12,28,.62);
    --faint: rgba(8,12,28,.44);
    --accent: #1d4ed8;
    background: linear-gradient(178deg,#fff 0%,#ecf0fb 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-15__bar::after {
    animation: none;
    background: none;
  }

  .sk-15__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-15__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-15__bar::after {
    animation: none;
    background: none;
  }

  .sk-15__panel,
    .sk-15__spec {
    border-color: CanvasText;
  }
}
```
