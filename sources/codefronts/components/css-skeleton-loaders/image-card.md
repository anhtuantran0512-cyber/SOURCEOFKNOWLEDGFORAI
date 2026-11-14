---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/image-card/"
title: "Image Placeholder Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A 16:9 media placeholder that reserves its box exactly, with a centred inline SVG so it reads as \"image loading\" rather than \"something is broken\"."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Placeholder Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/image-card/

A 16:9 media placeholder that reserves its box exactly, with a centred inline SVG so it reads as "image loading" rather than "something is broken". Distinct from the blur-up demo: no LQIP here, just the correct geometry, an icon, and a caption row that also reserves its two lines.
## HTML
```html
<div class="sk-14">
  <div class="sk-14__stage">
    <section class="sk-14__wrap" aria-labelledby="sk-14-h">
      <header class="sk-14__head">
        <p class="sk-14__eyebrow">aspect-ratio: 16 / 9</p>
        <h2 class="sk-14__h" id="sk-14-h">Reserve the crop, then say what's coming</h2>
        <p class="sk-14__sub">The box is exact before any byte arrives. A quiet glyph tells the user it is media rather than an error — and the caption reserves its lines too.</p>
      </header>

      <div class="sk-14__cards">
        <article class="sk-14__card" role="status" aria-live="polite">
          <span class="sk-14__vh">Loading hero image…</span>
          <div class="sk-14__media">
            <span class="sk-14__ratio" aria-hidden="true">16:9</span>
            <span class="sk-14__glyph" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3" y="4.5" width="18" height="15" rx="2.5" stroke="currentColor" stroke-width="1.6"/><circle cx="8.6" cy="10" r="1.7" stroke="currentColor" stroke-width="1.6"/><path d="M3.4 17.2l4.5-4.1a2 2 0 0 1 2.7 0l3 2.8m0 0 2-1.8a2 2 0 0 1 2.7 0l2.3 2.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            </span>
          </div>
          <div class="sk-14__cap" aria-hidden="true">
            <span class="sk-14__bar sk-14__bar--title"></span>
            <span class="sk-14__bar sk-14__bar--sm" style="inline-size:56%"></span>
          </div>
        </article>

        <article class="sk-14__card sk-14__card--real">
          <div class="sk-14__media sk-14__media--real">
            <img class="sk-14__img" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&amp;fit=crop&amp;w=960&amp;h=540&amp;q=72" width="960" height="540" alt="A still lake at dusk with mountains behind" loading="lazy" decoding="async">
          </div>
          <div class="sk-14__cap">
            <h3 class="sk-14__title">Resolved, in the same box</h3>
            <p class="sk-14__by">Priya Sharma · 4 min read</p>
          </div>
        </article>
      </div>

      <aside class="sk-14__spec" aria-label="Recipe">
        <p class="sk-14__srow"><span class="sk-14__skey">box</span><span class="sk-14__sval">inline-size: 100%; aspect-ratio: var(--ratio) — never declare a height</span></p>
        <p class="sk-14__srow"><span class="sk-14__skey">glyph</span><span class="sk-14__sval">inline SVG at currentColor, ~2rem, 35% opacity, aria-hidden</span></p>
        <p class="sk-14__srow"><span class="sk-14__skey">caption</span><span class="sk-14__sval">two bars matched to the resolved title and byline metrics</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-14 {
  --ratio: 16 / 9;
  --bg: #060809;
  --bg2: #0d1113;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f2f6f7;
  --muted: rgba(242,246,247,.62);
  --faint: rgba(242,246,247,.42);
  --accent: #a3e635;
  --sk: rgba(242,246,247,.1);
  --sheen: rgba(242,246,247,.17);
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
  background: radial-gradient(58% 40% at 88% -6%, rgba(163,230,53,.1) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-14 *,
.sk-14 *::before,
.sk-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 130)) {
  .sk-14 {
    --ink: oklch(0.97 0.006 195);
    --muted: oklch(0.97 0.006 195 / .62);
    --faint: oklch(0.97 0.006 195 / .42);
    --accent: oklch(0.85 0.16 125);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-14 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-14__wrap {
  inline-size: min(66rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-14__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 45rem;
}

.sk-14__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-14__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-14__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-14__cards {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.3rem);
  grid-template-columns: repeat(auto-fit,minmax(18rem,1fr));
}

.sk-14__card {
  display: grid;
  gap: .9rem;
  align-content: start;
  padding: clamp(.95rem,1.8vw,1.25rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
}

.sk-14__card--real {
  opacity: .92;
}

.sk-14__media {
  position: relative;
  inline-size: 100%;
  aspect-ratio: var(--ratio);
  border-radius: 14px;
  overflow: hidden;
  display: grid;
  place-items: center;
  background: var(--sk);
}

.sk-14__media::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-14-sheen 1.4s linear infinite;
}

.sk-14__media--real::after {
  content: none;
}

@keyframes sk-14-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-14__ratio {
  position: absolute;
  inset-block-start: .6rem;
  inset-inline-start: .6rem;
  z-index: 2;
  padding: .22rem .5rem;
  border-radius: .4rem;
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--ink);
  background: rgba(0,0,0,.35);
  border: 1px solid var(--line);
}

.sk-14__glyph {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  color: currentColor;
  opacity: .35;
}

.sk-14__glyph svg {
  inline-size: 2rem;
  block-size: 2rem;
}

.sk-14__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.sk-14__cap {
  display: grid;
  gap: .55rem;
  padding-inline: .2rem;
}

.sk-14__title {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.sk-14__by {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.sk-14__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-14__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-14-sheen 1.4s linear infinite;
}

.sk-14__bar--sm {
  block-size: .7rem;
}

.sk-14__bar--title {
  block-size: 1.2rem;
  inline-size: 76%;
  border-radius: 7px;
}

.sk-14__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-14__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-14__skey {
  min-inline-size: 4.2rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-14__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-14[data-theme="light"] {
  --bg: #f8faf6;
  --bg2: #fff;
  --surface: rgba(10,16,8,.026);
  --line: rgba(10,16,8,.11);
  --ink: #0a1008;
  --muted: rgba(10,16,8,.62);
  --faint: rgba(10,16,8,.44);
  --accent: #4d7c0f;
  background: linear-gradient(178deg,#fff 0%,#eff4e8 100%);
}

.sk-14[data-theme="light"] .sk-14__ratio {
  background: rgba(255,255,255,.8);
}

@media (prefers-color-scheme: light) {
  .sk-14:not([data-theme="dark"]) {
    --bg: #f8faf6;
    --bg2: #fff;
    --surface: rgba(10,16,8,.026);
    --line: rgba(10,16,8,.11);
    --ink: #0a1008;
    --muted: rgba(10,16,8,.62);
    --faint: rgba(10,16,8,.44);
    --accent: #4d7c0f;
    background: linear-gradient(178deg,#fff 0%,#eff4e8 100%);
  }

  .sk-14:not([data-theme="dark"]) .sk-14__ratio {
    background: rgba(255,255,255,.8);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-14__media::after,
    .sk-14__bar::after {
    animation: none;
    background: none;
  }

  .sk-14__media,
    .sk-14__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-14__bar,
    .sk-14__media {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-14__media::after,
    .sk-14__bar::after {
    animation: none;
    background: none;
  }

  .sk-14__card,
    .sk-14__spec,
    .sk-14__ratio {
    border-color: CanvasText;
  }
}
```
