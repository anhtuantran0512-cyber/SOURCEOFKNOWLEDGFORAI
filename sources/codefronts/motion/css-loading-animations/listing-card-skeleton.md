---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/listing-card-skeleton/"
title: "Property Listing Card Skeleton Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Skeleton screens beat spinners for content-heavy lists because they preserve layout and reduce perceived wait."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Property Listing Card Skeleton Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/listing-card-skeleton/

Skeleton screens beat spinners for content-heavy lists because they preserve layout and reduce perceived wait. This one is a complete property-listing card — media, price, address, spec chips, agent row — that shimmers while loading and crossfades into the real listing on .is-ready, with aria-busy handled correctly so screen readers do not read placeholder boxes.
## HTML
```html
<div class="la-15" data-state="loading">
  <div class="la-15__chrome">
    <button class="la-15__btn la-15__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-15__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-15__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-15__btn la-15__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <article class="la-15__card" role="status" aria-live="polite" aria-busy="true" aria-label="Loading property listing">
    <div class="la-15__stack">
      <div class="la-15__skeleton" aria-hidden="true">
        <span class="la-15__sk la-15__sk--media"></span>
        <span class="la-15__sk la-15__sk--price"></span>
        <span class="la-15__sk la-15__sk--addr"></span>
        <span class="la-15__chips">
          <i class="la-15__sk"></i><i class="la-15__sk"></i><i class="la-15__sk"></i>
        </span>
        <span class="la-15__agent">
          <i class="la-15__sk la-15__sk--av"></i>
          <i class="la-15__sk la-15__sk--name"></i>
        </span>
      </div>

      <div class="la-15__real" hidden>
        <span class="la-15__media">
          <span class="la-15__tag">New</span>
          <span class="la-15__shot"></span>
        </span>
        <p class="la-15__price">$1,285,000</p>
        <p class="la-15__addr">1042 Precita Ave <span aria-hidden="true">·</span> Bernal Heights, SF</p>
        <ul class="la-15__specs">
          <li>3 bd</li><li>2 ba</li><li>1,640 sqft</li>
        </ul>
        <p class="la-15__by"><span class="la-15__av" aria-hidden="true">AC</span> Listed by Alex Chen <span aria-hidden="true">·</span> 2h ago</p>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.la-15 {
  --bg: #f2f4f8;
  --surface: #ffffff;
  --ink: #0d121c;
  --muted: #657084;
  --line: #e2e7f0;
  --sk: #e7ebf2;
  --sk-hi: #f4f7fb;
  --acc: #3b5bdb;
  --ok: #0f9d63;
  --ring: #3b5bdb;
  --shadow: rgba(13,18,28,.16);
  --shimmer-dur: 1.5s;
  --serif: "Instrument Serif",ui-serif,Georgia,serif;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 60% at 50% -10%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-15,
.la-15 *,
.la-15 *::before,
.la-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-15 {
    --acc: oklch(52% .2 267);
    --ok: oklch(62% .15 158);
  }
}

.la-15__card {
  inline-size: min(21rem,100%);
  padding: .85rem .85rem 1rem;
  border-radius: 1.4rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 34px 60px -40px var(--shadow);
}

.la-15__stack {
  display: grid;
}

.la-15__stack > * {
  grid-area: 1/1;
}

.la-15__skeleton,
.la-15__real {
  display: grid;
  gap: .7rem;
}

.la-15__real[hidden] {
  display: none;
}

.la-15__sk {
  display: block;
  border-radius: .5rem;
  background: linear-gradient(90deg, var(--sk) 25%, var(--sk-hi) 37%, var(--sk) 50%) 0 0/220% 100%;
  animation: la-15-shimmer var(--shimmer-dur) linear infinite;
}

@keyframes la-15-shimmer {
  to {
    background-position: -220% 0;
  }
}

.la-15__sk--media {
  aspect-ratio: 16/10;
  border-radius: 1rem;
}

.la-15__sk--price {
  block-size: 1.4rem;
  inline-size: 52%;
}

.la-15__sk--addr {
  block-size: .85rem;
  inline-size: 80%;
}

.la-15__chips {
  display: flex;
  gap: .4rem;
}

.la-15__chips i {
  block-size: 1.5rem;
  inline-size: 3.6rem;
  border-radius: 999px;
}

.la-15__agent {
  display: flex;
  align-items: center;
  gap: .55rem;
  padding-block-start: .2rem;
}

.la-15__sk--av {
  inline-size: 1.9rem;
  block-size: 1.9rem;
  border-radius: 999px;
  flex: none;
}

.la-15__sk--name {
  block-size: .8rem;
  inline-size: 9rem;
}

.la-15__media {
  position: relative;
  display: block;
  aspect-ratio: 16/10;
  border-radius: 1rem;
  overflow: hidden;
}

.la-15__shot {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, color-mix(in oklab,var(--acc) 30%,transparent), transparent 45%), radial-gradient(60% 50% at 78% 22%, #ffd89b, transparent 60%), linear-gradient(160deg, #6f8fd8 0 42%, #2f4470 42% 58%, #24304d 58%), var(--sk);
}

.la-15__shot::after {
  content: "";
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  block-size: 38%;
  background: linear-gradient(180deg, transparent, rgba(6,10,18,.45)), repeating-linear-gradient(90deg, rgba(255,255,255,.06) 0 6px, transparent 6px 14px);
}

.la-15__tag {
  position: absolute;
  z-index: 2;
  inset-block-start: .55rem;
  inset-inline-start: .55rem;
  padding: .2rem .55rem;
  border-radius: 999px;
  background: var(--surface);
  color: var(--acc);
  font-family: var(--mono);
  font-size: .58rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.la-15__price {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.9rem;
  line-height: 1;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.la-15__addr {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
  text-wrap: pretty;
}

.la-15__specs {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.la-15__specs li {
  padding: .3rem .65rem;
  border-radius: 999px;
  font-size: .75rem;
  font-variant-numeric: tabular-nums;
  background: color-mix(in oklab,var(--acc) 8%,transparent);
  border: 1px solid color-mix(in oklab,var(--acc) 16%,transparent);
}

.la-15__by {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .75rem;
  color: var(--muted);
}

.la-15__av {
  inline-size: 1.9rem;
  block-size: 1.9rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  flex: none;
  background: linear-gradient(140deg, color-mix(in oklab,var(--acc) 80%,white), var(--acc));
  color: #fff;
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .04em;
}

.la-15.is-ready .la-15__skeleton {
  display: none;
}

.la-15.is-ready .la-15__real {
  display: grid;
}

.la-15:has(.la-15__real:not([hidden])) .la-15__card {
  border-color: color-mix(in oklab,var(--ok) 30%,var(--line));
}

@supports (transition-behavior: allow-discrete) {
  .la-15__real {
    transition: opacity .32s ease, display .32s allow-discrete;
  }

  @starting-style {
    .la-15.is-ready .la-15__real {
      opacity: 0;
    }
  }
}

.la-15__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-15__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 72%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-15__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-15__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-15__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-15__sun {
  display: none;
}

.la-15__theme[aria-pressed="true"] .la-15__sun {
  display: block;
}

.la-15__theme[aria-pressed="true"] .la-15__moon {
  display: none;
}

.la-15__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-15:not([data-theme="light"]) {
    --bg: #080a11;
    --surface: #111621;
    --ink: #eef1f8;
    --muted: #909cb0;
    --line: #212a38;
    --sk: #1a212d;
    --sk-hi: #252f3e;
    --acc: #7f9cff;
    --ok: #31d68f;
    --ring: #7f9cff;
    --shadow: rgba(0,0,0,.7);
  }

  .la-15:not([data-theme="light"]) .la-15__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-15:not([data-theme="light"]) .la-15__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-15[data-theme="dark"] {
  --bg: #080a11;
  --surface: #111621;
  --ink: #eef1f8;
  --muted: #909cb0;
  --line: #212a38;
  --sk: #1a212d;
  --sk-hi: #252f3e;
  --acc: #7f9cff;
  --ok: #31d68f;
  --ring: #7f9cff;
  --shadow: rgba(0,0,0,.7);
}

.la-15[data-theme="dark"] .la-15__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-15[data-theme="dark"] .la-15__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-15 * {
    animation: none !important;
    transition: none !important;
  }

  .la-15__sk {
    background: var(--sk);
  }
}

@media (forced-colors: active) {
  .la-15__card {
    border: 1px solid CanvasText;
  }

  .la-15__sk {
    background: Canvas;
    border: 1px solid CanvasText;
  }

  .la-15__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-15');
  if (!root) return;
  const theme = root.querySelector('.la-15__theme');
  const done = root.querySelector('.la-15__done');
  const card = root.querySelector('.la-15__card');
  const real = root.querySelector('.la-15__real');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    real.hidden = !ready;                                   // hidden attribute AND the CSS rule
    card.setAttribute('aria-busy', String(!ready));          // never leave aria-busy on
    card.setAttribute('aria-label', ready ? '1042 Precita Ave, Bernal Heights, 1,285,000 dollars' : 'Loading property listing');
  });
  sync();
})();
```
