---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/svg-placeholder-blur-up-image-skeleton/"
title: "SVG Placeholder Blur-Up Image Skeleton"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The Medium / WordPress blur-up pattern, hand-rolled: a two-shape inline SVG blurred to blur(20px) sits inside an aspect-ratio box and cross-fades out when…"
has_js: "true"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Placeholder Blur-Up Image Skeleton
Source: https://codefronts.com/components/css-skeleton-loaders/svg-placeholder-blur-up-image-skeleton/

The Medium / WordPress blur-up pattern, hand-rolled: a two-shape inline SVG blurred to blur(20px) sits inside an aspect-ratio box and cross-fades out when the real photograph decodes. Press Simulate slow load to replay the 1.2s reveal as many times as you need to get the easing right.
## HTML
```html
<div class="sk-05">
  <div class="sk-05__stage">
    <section class="sk-05__wrap" aria-labelledby="sk-05-h">
      <header class="sk-05__head">
        <p class="sk-05__eyebrow">LQIP · blur-up</p>
        <h2 class="sk-05__h" id="sk-05-h">Ship a blurred guess in the first frame</h2>
        <p class="sk-05__sub">An inline SVG placeholder costs a few hundred bytes and paints instantly. The photograph cross-fades over it when <code>decode()</code> resolves — and the box never changes size.</p>
        <div class="sk-05__controls">
          <button class="sk-05__btn" id="sk-05-go" type="button">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12a8 8 0 1 1 2.6 5.9" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M4 6.5V12h5.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Simulate slow load
          </button>
          <p class="sk-05__status" id="sk-05-msg" role="status" aria-live="polite">Placeholder shown · waiting for decode</p>
        </div>
      </header>

      <figure class="sk-05__figure">
        <div class="sk-05__frame" id="sk-05-frame">
          <svg class="sk-05__lqip" viewBox="0 0 32 20" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
            <rect width="32" height="20" fill="#1d3557"/>
            <ellipse cx="9" cy="7" rx="11" ry="7" fill="#e07a5f"/>
            <ellipse cx="25" cy="15" rx="12" ry="8" fill="#3d5a80"/>
            <ellipse cx="20" cy="4" rx="7" ry="4" fill="#f2cc8f"/>
          </svg>
          <img class="sk-05__img" id="sk-05-img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&amp;fit=crop&amp;w=1280&amp;h=800&amp;q=72" width="1280" height="800" alt="Fog moving through a dark pine forest at dawn" decoding="async" fetchpriority="low">
        </div>
        <figcaption class="sk-05__cap">
          <span class="sk-05__captitle">Foggy pines, 1280×800</span>
          <span class="sk-05__capmeta">aspect-ratio: 16 / 10 · CLS 0.00 · placeholder 412 B</span>
        </figcaption>
      </figure>

      <aside class="sk-05__spec" aria-label="Recipe">
        <p class="sk-05__srow"><span class="sk-05__skey">box</span><span class="sk-05__sval">aspect-ratio: 16/10 + overflow: hidden — reserves space before any byte lands</span></p>
        <p class="sk-05__srow"><span class="sk-05__skey">lqip</span><span class="sk-05__sval">filter: blur(20px); scale: 1.08 — blur then overscale to hide edge bleed</span></p>
        <p class="sk-05__srow"><span class="sk-05__skey">reveal</span><span class="sk-05__sval">await img.decode() → opacity 0→1 over 1.2s cubic-bezier(.2,.7,.3,1)</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-05 {
  --bg: #06080a;
  --bg2: #0d1418;
  --surface: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.1);
  --ink: #f2f7f7;
  --muted: rgba(242,247,247,.62);
  --faint: rgba(242,247,247,.42);
  --accent: #5eead4;
  --sk: rgba(242,247,247,.09);
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
  background: radial-gradient(60% 45% at 10% -5%, rgba(94,234,212,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-05 *,
.sk-05 *::before,
.sk-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 180)) {
  .sk-05 {
    --ink: oklch(0.97 0.008 190);
    --muted: oklch(0.97 0.008 190 / .62);
    --faint: oklch(0.97 0.008 190 / .42);
    --accent: oklch(0.85 0.12 178);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-05 {
    --sk: color-mix(in oklab, currentColor 9%, transparent);
  }
}

.sk-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-05__wrap {
  inline-size: min(64rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-05__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
}

.sk-05__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-05__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-05__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-05__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-05__controls {
  display: flex;
  align-items: center;
  gap: .9rem;
  flex-wrap: wrap;
  margin-block-start: .35rem;
}

.sk-05__btn {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .6rem 1.05rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  color: #04211d;
  background: var(--accent);
  border: 1px solid transparent;
  transition: translate .18s ease, opacity .18s ease;
}

.sk-05__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.sk-05__btn:hover {
  translate: 0 -1px;
}

.sk-05__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.sk-05__btn[disabled] {
  opacity: .5;
  cursor: progress;
  translate: none;
}

.sk-05__status {
  margin: 0;
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
}

.sk-05__figure {
  margin: 0;
  display: grid;
  gap: .8rem;
}

.sk-05__frame {
  position: relative;
  overflow: hidden;
  aspect-ratio: 16/10;
  border-radius: 16px;
  border: 1px solid var(--line);
  background: var(--sk);
  box-shadow: 0 34px 80px -46px rgba(0,0,0,.95);
}

.sk-05__lqip,
.sk-05__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  display: block;
}

.sk-05__lqip {
  filter: blur(20px);
  scale: 1.08;
  transition: opacity 1.2s cubic-bezier(.2,.7,.3,1);
}

.sk-05__img {
  object-fit: cover;
  opacity: 0;
  filter: blur(6px);
  scale: 1.02;
  transition: opacity 1.2s cubic-bezier(.2,.7,.3,1), filter 1.2s cubic-bezier(.2,.7,.3,1), scale 1.2s cubic-bezier(.2,.7,.3,1);
}

.sk-05__frame.is-loaded .sk-05__img {
  opacity: 1;
  filter: blur(0);
  scale: 1;
}

.sk-05__frame.is-loaded .sk-05__lqip {
  opacity: 0;
}

.sk-05__frame::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(100deg, transparent 20%, rgba(255,255,255,.1) 50%, transparent 80%);
  translate: -100% 0;
  animation: sk-05-sheen 1.6s linear infinite;
}

.sk-05__frame.is-loaded::after {
  animation: none;
  opacity: 0;
}

@keyframes sk-05-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-05__cap {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.sk-05__captitle {
  font-size: .9rem;
  color: var(--ink);
}

.sk-05__capmeta {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--faint);
}

.sk-05__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-05__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-05__skey {
  min-inline-size: 3.5rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-05__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-05[data-theme="light"] {
  --bg: #f6faf9;
  --bg2: #fff;
  --surface: rgba(4,20,18,.028);
  --line: rgba(4,20,18,.11);
  --ink: #04120f;
  --muted: rgba(4,18,15,.62);
  --faint: rgba(4,18,15,.44);
  --accent: #0f766e;
  background: linear-gradient(178deg,#fff 0%,#e9f4f1 100%);
}

@media (prefers-color-scheme: light) {
  .sk-05:not([data-theme="dark"]) {
    --bg: #f6faf9;
    --bg2: #fff;
    --surface: rgba(4,20,18,.028);
    --line: rgba(4,20,18,.11);
    --ink: #04120f;
    --muted: rgba(4,18,15,.62);
    --faint: rgba(4,18,15,.44);
    --accent: #0f766e;
    background: linear-gradient(178deg,#fff 0%,#e9f4f1 100%);
  }

  .sk-05__btn {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-05__frame::after {
    animation: none;
    background: none;
  }

  .sk-05__lqip,
    .sk-05__img {
    transition-duration: .01ms;
  }

  .sk-05__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-05__frame,
    .sk-05__spec,
    .sk-05__btn {
    border-color: CanvasText;
  }

  .sk-05__frame::after {
    animation: none;
    background: none;
  }
}
```

## JavaScript
```js
const frame = document.getElementById('sk-05-frame');
const img = document.getElementById('sk-05-img');
const msg = document.getElementById('sk-05-msg');
const go = document.getElementById('sk-05-go');
const src = img.currentSrc || img.src;

const reveal = async () => {
  try { await img.decode(); } catch { /* older engines: load event already fired */ }
  frame.classList.add('is-loaded');
  msg.textContent = 'Image decoded · cross-faded over 1.2s';
  go.disabled = false;
};

go.addEventListener('click', () => {
  go.disabled = true;
  frame.classList.remove('is-loaded');
  msg.textContent = 'Placeholder shown · fetching full image…';
  img.src = '';
  // cache-bust so the decode is observable on every replay
  setTimeout(() => { img.src = src + '&sim=' + Date.now(); reveal(); }, 700);
});

reveal();
```
