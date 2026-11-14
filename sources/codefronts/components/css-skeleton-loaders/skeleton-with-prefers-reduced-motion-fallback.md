---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/skeleton-with-prefers-reduced-motion-fallback/"
title: "Skeleton with prefers-reduced-motion Fallback"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "Shimmer is a repeating motion in a user's peripheral vision — for a vestibular-sensitive reader that is a symptom trigger, not a delight."
has_js: "true"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton with prefers-reduced-motion Fallback
Source: https://codefronts.com/components/css-skeleton-loaders/skeleton-with-prefers-reduced-motion-fallback/

Shimmer is a repeating motion in a user's peripheral vision — for a vestibular-sensitive reader that is a symptom trigger, not a delight. This demo shows the animated skeleton and its prefers-reduced-motion fallback side by side, with an in-demo toggle so you can preview the reduced state without touching your OS settings.
## HTML
```html
<div class="sk-03">
  <div class="sk-03__stage">
    <section class="sk-03__wrap" aria-labelledby="sk-03-h">
      <header class="sk-03__head">
        <p class="sk-03__eyebrow">WCAG 2.2 · SC 2.3.3</p>
        <h2 class="sk-03__h" id="sk-03-h">The fill says loading. The motion is optional.</h2>
        <p class="sk-03__sub">Left runs the 1.4s sheen. Right is the same skeleton under <code>prefers-reduced-motion: reduce</code> — zero moving pixels, still unmistakably a placeholder.</p>
        <button class="sk-03__toggle" id="sk-03-btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 5.5v13M18 5.5v13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span id="sk-03-label">Preview reduced motion for both panels</span>
        </button>
      </header>

      <div class="sk-03__cols" id="sk-03-panels">
        <article class="sk-03__panel" role="status" aria-live="polite">
          <span class="sk-03__vh">Loading report, animated placeholder…</span>
          <header class="sk-03__phead">
            <p class="sk-03__label">default</p>
            <p class="sk-03__ptitle">Animated sheen</p>
            <p class="sk-03__pnote">1.4s linear infinite · translate on a ::after layer</p>
          </header>
          <div class="sk-03__body" aria-hidden="true">
            <div class="sk-03__row">
              <span class="sk-03__bar sk-03__avatar"></span>
              <div class="sk-03__ident"><span class="sk-03__bar" style="inline-size:8.5rem"></span><span class="sk-03__bar sk-03__bar--sm" style="inline-size:5.5rem"></span></div>
            </div>
            <span class="sk-03__bar sk-03__bar--media"></span>
            <span class="sk-03__bar sk-03__bar--sm"></span>
            <span class="sk-03__bar sk-03__bar--sm"></span>
            <span class="sk-03__bar sk-03__bar--sm" style="inline-size:58%"></span>
          </div>
        </article>

        <article class="sk-03__panel sk-03__panel--still" role="status" aria-live="polite">
          <span class="sk-03__vh">Loading report, static placeholder…</span>
          <header class="sk-03__phead">
            <p class="sk-03__label sk-03__label--on">reduce</p>
            <p class="sk-03__ptitle">Static gradient</p>
            <p class="sk-03__pnote">animation: none · linear-gradient(105deg) holds the signal</p>
          </header>
          <div class="sk-03__body" aria-hidden="true">
            <div class="sk-03__row">
              <span class="sk-03__bar sk-03__avatar"></span>
              <div class="sk-03__ident"><span class="sk-03__bar" style="inline-size:8.5rem"></span><span class="sk-03__bar sk-03__bar--sm" style="inline-size:5.5rem"></span></div>
            </div>
            <span class="sk-03__bar sk-03__bar--media"></span>
            <span class="sk-03__bar sk-03__bar--sm"></span>
            <span class="sk-03__bar sk-03__bar--sm"></span>
            <span class="sk-03__bar sk-03__bar--sm" style="inline-size:58%"></span>
          </div>
        </article>
      </div>

      <aside class="sk-03__spec" aria-label="Recipe">
        <p class="sk-03__srow"><span class="sk-03__skey">guard</span><span class="sk-03__sval">@media (prefers-reduced-motion: reduce) — required on every animated skeleton</span></p>
        <p class="sk-03__srow"><span class="sk-03__skey">keep</span><span class="sk-03__sval">a static fill above 3:1 contrast, never a blank box</span></p>
        <p class="sk-03__srow"><span class="sk-03__skey">js</span><span class="sk-03__sval">matchMedia('(prefers-reduced-motion: reduce)') + change listener</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-03 {
  --bg: #0a0806;
  --bg2: #13100c;
  --surface: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.09);
  --ink: #f8f6f3;
  --muted: rgba(248,246,243,.62);
  --faint: rgba(248,246,243,.42);
  --accent: #f0b429;
  --sk: rgba(248,246,243,.1);
  --sheen: rgba(248,246,243,.19);
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
  background: radial-gradient(65% 45% at 15% -5%, rgba(240,180,41,.1) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-03 *,
.sk-03 *::before,
.sk-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 80)) {
  .sk-03 {
    --ink: oklch(0.975 0.006 80);
    --muted: oklch(0.975 0.006 80 / .62);
    --faint: oklch(0.975 0.006 80 / .42);
    --accent: oklch(0.82 0.14 82);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-03 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 19%, transparent);
  }
}

.sk-03__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-03__wrap {
  inline-size: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-03__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
  justify-items: start;
}

.sk-03__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-03__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-03__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-03__sub code {
  font-family: var(--mono);
  font-size: .88em;
  color: var(--ink);
}

.sk-03__toggle {
  margin-block-start: .3rem;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .6rem 1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line);
  transition: background .18s ease, border-color .18s ease;
}

.sk-03__toggle svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--accent);
}

.sk-03__toggle:hover {
  background: rgba(255,255,255,.07);
}

.sk-03__toggle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sk-03__toggle[aria-pressed="true"] {
  background: var(--accent);
  border-color: var(--accent);
  color: #1a1206;
}

.sk-03__toggle[aria-pressed="true"] svg {
  color: #1a1206;
}

.sk-03__cols {
  display: grid;
  gap: clamp(.9rem,1.8vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.sk-03__panel {
  display: grid;
  gap: 1.1rem;
  align-content: start;
  padding: clamp(1.05rem,2vw,1.5rem);
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--surface);
  min-block-size: 24rem;
}

.sk-03__panel--still {
  border-color: rgba(240,180,41,.3);
}

.sk-03__phead {
  display: grid;
  gap: .35rem;
}

.sk-03__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-03__label--on {
  color: var(--accent);
}

.sk-03__ptitle {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.sk-03__pnote {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-03__body {
  display: grid;
  gap: .7rem;
}

.sk-03__row {
  display: flex;
  align-items: center;
  gap: .85rem;
  margin-block-end: .2rem;
}

.sk-03__ident {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.sk-03__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .85rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-03__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-03-sheen 1.4s linear infinite;
}

@keyframes sk-03-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-03__bar--sm {
  block-size: .7rem;
}

.sk-03__bar--media {
  block-size: auto;
  aspect-ratio: 16/9;
  border-radius: 10px;
  margin-block: .25rem;
}

.sk-03__avatar {
  inline-size: 2.6rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}
/* the fallback: authored once, applied by the media query AND by the preview class */

.sk-03__panel--still .sk-03__bar::after,
.sk-03--still .sk-03__bar::after {
  animation: none;
  background: none;
}

.sk-03__panel--still .sk-03__bar,
.sk-03--still .sk-03__bar {
  background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
}

.sk-03__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-03__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-03__skey {
  min-inline-size: 3.5rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-03__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-03[data-theme="light"] {
  --bg: #fbf9f6;
  --bg2: #fff;
  --surface: rgba(18,12,6,.028);
  --line: rgba(18,12,6,.11);
  --ink: #120c06;
  --muted: rgba(18,12,6,.62);
  --faint: rgba(18,12,6,.44);
  --accent: #9a6100;
  background: linear-gradient(178deg,#fff 0%,#f5f1ea 100%);
}

@media (prefers-color-scheme: light) {
  .sk-03:not([data-theme="dark"]) {
    --bg: #fbf9f6;
    --bg2: #fff;
    --surface: rgba(18,12,6,.028);
    --line: rgba(18,12,6,.11);
    --ink: #120c06;
    --muted: rgba(18,12,6,.62);
    --faint: rgba(18,12,6,.44);
    --accent: #9a6100;
    background: linear-gradient(178deg,#fff 0%,#f5f1ea 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-03__bar::after {
    animation: none;
    background: none;
  }

  .sk-03__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }

  .sk-03__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .sk-03__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-03__bar::after {
    animation: none;
    background: none;
  }

  .sk-03__panel,
    .sk-03__spec,
    .sk-03__toggle {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sk-03');
const btn = document.getElementById('sk-03-btn');

btn.addEventListener('click', () => {
  const on = root.classList.toggle('sk-03--still');
  btn.setAttribute('aria-pressed', String(on));
});

// keep the preview honest: if the OS already asks for reduced motion, say so
const mq = matchMedia('(prefers-reduced-motion: reduce)');
const label = document.getElementById('sk-03-label');
const sync = () => {
  btn.disabled = mq.matches;
  label.textContent = mq.matches
    ? 'Reduced motion is already on at OS level'
    : 'Preview reduced motion for both panels';
};
mq.addEventListener('change', sync);
sync();
```
