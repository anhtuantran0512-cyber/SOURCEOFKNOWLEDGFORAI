---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-fallback-for-broken-images/"
title: "CSS Avatar Fallback for Broken Images"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "What happens when the photo 404s — and this demo actually breaks one so you can see the fallback fire."
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Fallback for Broken Images
Source: https://codefronts.com/components/css-avatars/css-avatar-fallback-for-broken-images/

What happens when the photo 404s — and this demo actually breaks one so you can see the fallback fire. The initials layer sits beneath the image from the start, so there is no flash and no layout shift; the image simply stops covering it. Includes the detail almost every tutorial misses: images that already failed before your script ran, caught with a complete && naturalWidth === 0 check.
## HTML
```html
<div class="av-15">
  <button class="av-15__theme" type="button" aria-pressed="false">
    <svg class="av-15__i av-15__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-15__i av-15__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-15__vh">Toggle dark theme</span>
  </button>

  <div class="av-15__stage">
    <section class="av-15__wrap" aria-labelledby="av-15-h">
      <header class="av-15__head">
        <p class="av-15__eyebrow">Resilience · Fallback</p>
        <h2 class="av-15__h" id="av-15-h">When the photo 404s</h2>
        <p class="av-15__sub">The third avatar points at a dead URL. Its initials were always there, underneath.</p>
      </header>

      <ul class="av-15__row">
        <li class="av-15__cell">
          <span class="av-15__fig" data-state="ok">
            <span class="av-15__init" style="--h:264" aria-hidden="true">PS</span>
            <img class="av-15__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" decoding="async">
          </span>
          <span class="av-15__who"><span class="av-15__name">Priya Sharma</span><span class="av-15__meta av-15__meta--ok">Loaded</span></span>
        </li>
        <li class="av-15__cell">
          <span class="av-15__fig" data-state="ok">
            <span class="av-15__init" style="--h:152" aria-hidden="true">JL</span>
            <img class="av-15__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" decoding="async">
          </span>
          <span class="av-15__who"><span class="av-15__name">Jordan Lee</span><span class="av-15__meta av-15__meta--ok">Loaded</span></span>
        </li>
        <li class="av-15__cell">
          <span class="av-15__fig" data-state="ok">
            <span class="av-15__init" style="--h:22" aria-hidden="true">NK</span>
            <img class="av-15__img" id="av-15-broken" src="https://images.unsplash.com/photo-0000000000000-deleted-avatar?w=200&auto=format" alt="Nina Kaur" width="200" height="200" decoding="async">
          </span>
          <span class="av-15__who"><span class="av-15__name">Nina Kaur</span><span class="av-15__meta av-15__meta--bad">Photo unavailable</span></span>
        </li>
        <li class="av-15__cell">
          <span class="av-15__fig" data-state="ok">
            <span class="av-15__init" style="--h:318" aria-hidden="true">TB</span>
            <img class="av-15__img" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Tom Bergström" width="200" height="200" decoding="async">
          </span>
          <span class="av-15__who"><span class="av-15__name">Tom Bergström</span><span class="av-15__meta av-15__meta--ok">Loaded</span></span>
        </li>
      </ul>

      <div class="av-15__bar">
        <button class="av-15__btn" type="button" id="av-15-retry">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 12a8 8 0 1 1-2.6-5.9M20 4v4h-4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Retry the broken photo
        </button>
        <p class="av-15__live" id="av-15-live" aria-live="polite">1 of 4 photos failed. Initials shown instead.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-15 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --ok: oklch(58% .15 155);
    --bad: oklch(58% .19 30);
  }

  .av-15__init {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }
}

.av-15 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --ok: #15803d;
  --bad: #c2410c;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --size: clamp(4rem,11vw,5.5rem);
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-15 *,
.av-15 *::before,
.av-15 *::after {
  box-sizing: border-box;
}

.av-15__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-15 [hidden] {
  display: none !important;
}

.av-15__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-15__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-15__theme:hover {
  translate: 0 -1px;
}

.av-15__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-15__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-15__i--sun {
  display: none;
}

.av-15[data-theme="dark"] .av-15__i--moon {
  display: none;
}

.av-15[data-theme="dark"] .av-15__i--sun {
  display: block;
}

.av-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-15__wrap {
  inline-size: min(56rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-15__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-15__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-15__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-15__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-15__row {
  list-style: none;
  margin: 0;
  padding: clamp(1.5rem,4vw,2.25rem) clamp(1rem,3vw,1.75rem);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-15__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .7rem;
  text-align: center;
}

.av-15__fig {
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.06);
}

.av-15__init {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
  font-size: calc(var(--size) * .32);
  font-weight: 700;
  letter-spacing: .02em;
}

.av-15__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  transition: opacity .3s ease;
}

.av-15__fig[data-state="broken"] .av-15__img {
  opacity: 0;
}

.av-15__fig[data-state="broken"] {
  box-shadow: 0 0 0 1px var(--line), 0 0 0 3px var(--panel);
}

.av-15__fig:has(img[data-broken]) .av-15__img {
  opacity: 0;
}

.av-15__who {
  display: flex;
  flex-direction: column;
  gap: .1rem;
}

.av-15__name {
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.av-15__meta {
  font-size: .75rem;
  font-weight: 600;
}

.av-15__meta--ok {
  color: var(--ok);
}

.av-15__meta--bad {
  color: var(--bad);
}

.av-15__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .85rem 1.25rem;
  padding: .9rem 1.1rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-15__btn {
  appearance: none;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.75rem;
  padding: 0 1rem;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .86rem;
  font-weight: 600;
  cursor: pointer;
  transition: translate .16s ease, opacity .16s ease;
}

.av-15__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.av-15__btn:hover {
  translate: 0 -1px;
  opacity: .92;
}

.av-15__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-15__live {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.av-15[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --ok: #4ade80;
  --bad: #fb923c;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-15[data-theme="dark"] .av-15__init {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

@supports (color: oklch(50% .1 250)) {
  .av-15[data-theme="dark"] .av-15__init {
    background: oklch(30% .07 var(--h));
    color: oklch(88% .12 var(--h));
  }
}

@media (prefers-color-scheme: dark) {
  .av-15:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --ok: #4ade80;
    --bad: #fb923c;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-15:not([data-theme="light"]) .av-15__i--moon {
    display: none;
  }

  .av-15:not([data-theme="light"]) .av-15__i--sun {
    display: block;
  }

  .av-15:not([data-theme="light"]) .av-15__init {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }

  @supports (color: oklch(50% .1 250)) {
    .av-15:not([data-theme="light"]) .av-15__init {
      background: oklch(30% .07 var(--h));
      color: oklch(88% .12 var(--h));
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-15 *,
    .av-15 *::before,
    .av-15 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-15__init {
    background: Canvas;
    color: CanvasText;
    box-shadow: inset 0 0 0 1px CanvasText;
  }

  .av-15__row,
    .av-15__bar,
    .av-15__btn,
    .av-15__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av15 = document.querySelector('.av-15');
const av15live = av15.querySelector('#av-15-live');

const av15watch = (img) => {
  const fig = img.closest('.av-15__fig');
  const fail = () => { fig.dataset.state = 'broken'; img.dataset.broken = 'true'; };
  img.addEventListener('error', fail);
  img.addEventListener('load', () => { fig.dataset.state = 'ok'; delete img.dataset.broken; });
  if (img.complete && img.naturalWidth === 0) fail();
};

av15.querySelectorAll('.av-15__img').forEach(av15watch);

av15.querySelector('#av-15-retry').addEventListener('click', () => {
  const img = av15.querySelector('#av-15-broken');
  const base = img.src.split('&cb=')[0];
  av15live.textContent = 'Retrying Nina Kaur photo…';
  img.src = base + '&cb=' + Date.now();
  setTimeout(() => {
    av15live.textContent = img.dataset.broken
      ? 'Still unavailable. Initials shown instead.'
      : 'Photo loaded.';
  }, 1200);
});

av15.querySelector('.av-15__theme').addEventListener('click', (e) => {
  const on = av15.dataset.theme !== 'dark';
  av15.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
```
