---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-skeleton-loading-avatar/"
title: "CSS Skeleton Loading Avatar"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "A shimmer placeholder in the avatar's exact shape that crossfades into the real photo the moment it decodes — no layout shift, because the frame owns the…"
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Skeleton Loading Avatar
Source: https://codefronts.com/components/css-avatars/css-skeleton-loading-avatar/

A shimmer placeholder in the avatar's exact shape that crossfades into the real photo the moment it decodes — no layout shift, because the frame owns the geometry and the image only changes opacity. The shimmer animates background-position on a fixed gradient (one property, no repaint of the layout), the loading state is announced with aria-busy, and reduced-motion gets a calm static placeholder instead of a moving one.
## HTML
```html
<div class="av-20">
  <button class="av-20__theme" type="button" aria-pressed="false">
    <svg class="av-20__i av-20__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-20__i av-20__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-20__vh">Toggle dark theme</span>
  </button>

  <div class="av-20__stage">
    <section class="av-20__wrap" aria-labelledby="av-20-h">
      <header class="av-20__head">
        <p class="av-20__eyebrow">Loading · Placeholder</p>
        <h2 class="av-20__h" id="av-20-h">Shimmer to photo</h2>
        <p class="av-20__sub">Both layers are mounted from the start, so the crossfade shifts nothing. Replay it below.</p>
      </header>

      <ul class="av-20__list" id="av-20-list">
        <li class="av-20__row">
          <span class="av-20__fig" aria-busy="true">
            <span class="av-20__skel" aria-hidden="true"></span>
            <img class="av-20__img" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ava Lindqvist" width="200" height="200" decoding="async">
          </span>
          <span class="av-20__text">
            <span class="av-20__line av-20__line--name">Ava Lindqvist</span>
            <span class="av-20__line av-20__line--meta">Product analytics · Stockholm</span>
          </span>
        </li>
        <li class="av-20__row">
          <span class="av-20__fig" aria-busy="true">
            <span class="av-20__skel" aria-hidden="true"></span>
            <img class="av-20__img" src="https://images.unsplash.com/photo-1552058544-f2b08422138a?w=200&auto=format&fit=facearea&facepad=2.5" alt="Leo Mbeki" width="200" height="200" decoding="async">
          </span>
          <span class="av-20__text">
            <span class="av-20__line av-20__line--name">Leo Mbeki</span>
            <span class="av-20__line av-20__line--meta">Infrastructure · Cape Town</span>
          </span>
        </li>
        <li class="av-20__row">
          <span class="av-20__fig" aria-busy="true">
            <span class="av-20__skel" aria-hidden="true"></span>
            <img class="av-20__img" src="https://images.unsplash.com/photo-1618641986557-1ecd230959aa?w=200&auto=format&fit=facearea&facepad=2.5" alt="Tara Whitfield" width="200" height="200" decoding="async">
          </span>
          <span class="av-20__text">
            <span class="av-20__line av-20__line--name">Tara Whitfield</span>
            <span class="av-20__line av-20__line--meta">Customer research · Leeds</span>
          </span>
        </li>
      </ul>

      <div class="av-20__bar">
        <button class="av-20__btn" type="button" id="av-20-replay">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 12a8 8 0 1 1-2.6-5.9M20 4v4h-4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Replay the load
        </button>
        <p class="av-20__live" id="av-20-live" aria-live="polite">Loaded.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-20 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --sk1: oklch(94% .008 265);
    --sk2: oklch(98% .004 265);
  }
}

.av-20 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --sk1: #e9ecf2;
  --sk2: #f8fafc;
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --size: clamp(3rem,8vw,3.75rem);
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

.av-20 *,
.av-20 *::before,
.av-20 *::after {
  box-sizing: border-box;
}

.av-20__vh {
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

.av-20__theme {
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

.av-20__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-20__theme:hover {
  translate: 0 -1px;
}

.av-20__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-20__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-20__i--sun {
  display: none;
}

.av-20[data-theme="dark"] .av-20__i--moon {
  display: none;
}

.av-20[data-theme="dark"] .av-20__i--sun {
  display: block;
}

.av-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-20__wrap {
  inline-size: min(50rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-20__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-20__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-20__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-20__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-20__list {
  list-style: none;
  margin: 0;
  padding: .6rem;
  display: flex;
  flex-direction: column;
  gap: .2rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-20__row {
  display: flex;
  align-items: center;
  gap: .95rem;
  padding: .75rem .85rem;
  border-radius: 12px;
}

.av-20__fig {
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  flex: none;
}

.av-20__skel {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(100deg, var(--sk1) 22%, var(--sk2) 42%, var(--sk1) 62%);
  background-size: 300% 100%;
  animation: av-20-shimmer 1.4s linear infinite;
}

@keyframes av-20-shimmer {
  from {
    background-position: 150% 0;
  }

  to {
    background-position: -50% 0;
  }
}

.av-20__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  border-radius: inherit;
  object-fit: cover;
  object-position: center top;
  opacity: 0;
  transition: opacity .45s ease;
}

.av-20__fig[data-loaded="true"] .av-20__img {
  opacity: 1;
}

.av-20__fig[data-loaded="true"] .av-20__skel {
  opacity: 0;
  transition: opacity .45s ease;
}

.av-20__text {
  display: flex;
  flex-direction: column;
  gap: .3rem;
  min-inline-size: 0;
  flex: 1;
}

.av-20__line {
  position: relative;
  display: block;
  color: transparent;
  border-radius: 6px;
  background: linear-gradient(100deg, var(--sk1) 22%, var(--sk2) 42%, var(--sk1) 62%);
  background-size: 300% 100%;
  animation: av-20-shimmer 1.4s linear infinite;
  transition: color .3s ease .1s, background .3s ease;
}

.av-20__line--name {
  max-inline-size: 11rem;
  font-size: .95rem;
  font-weight: 650;
  letter-spacing: -.015em;
}

.av-20__line--meta {
  max-inline-size: 15rem;
  font-size: .8rem;
}

.av-20__row:has([data-loaded="true"]) .av-20__line {
  background: none;
  animation: none;
  color: var(--ink);
}

.av-20__row:has([data-loaded="true"]) .av-20__line--meta {
  color: var(--muted);
}

.av-20__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .85rem 1.25rem;
  padding: .9rem 1.1rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-20__btn {
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

.av-20__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.av-20__btn:hover {
  translate: 0 -1px;
  opacity: .92;
}

.av-20__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-20__live {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.av-20[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --sk1: #1e222b;
  --sk2: #2b313d;
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

@media (prefers-color-scheme: dark) {
  .av-20:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --sk1: #1e222b;
    --sk2: #2b313d;
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-20:not([data-theme="light"]) .av-20__i--moon {
    display: none;
  }

  .av-20:not([data-theme="light"]) .av-20__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-20 *,
    .av-20 *::before,
    .av-20 *::after {
    transition: none !important;
    animation: none !important;
  }

  .av-20__skel,
    .av-20__line {
    background: var(--sk1);
  }
}

@media (forced-colors: active) {
  .av-20__skel,
    .av-20__line {
    background: GrayText;
    animation: none;
  }

  .av-20__list,
    .av-20__bar,
    .av-20__btn,
    .av-20__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av20 = document.querySelector('.av-20');
const av20live = av20.querySelector('#av-20-live');
const av20figs = [...av20.querySelectorAll('.av-20__fig')];

const av20reveal = async (fig) => {
  const img = fig.querySelector('.av-20__img');
  try { await img.decode(); } catch (e) { /* fall through to load */ }
  fig.dataset.loaded = 'true';
  fig.removeAttribute('aria-busy');
  if (av20figs.every((f) => f.dataset.loaded === 'true')) av20live.textContent = 'Loaded.';
};

av20figs.forEach((fig) => {
  const img = fig.querySelector('.av-20__img');
  img.addEventListener('load', () => av20reveal(fig));
  if (img.complete && img.naturalWidth > 0) av20reveal(fig);
});

av20.querySelector('#av-20-replay').addEventListener('click', () => {
  av20live.textContent = 'Loading three avatars…';
  av20figs.forEach((fig) => {
    const img = fig.querySelector('.av-20__img');
    const base = img.src.split('&cb=')[0];
    delete fig.dataset.loaded;
    fig.setAttribute('aria-busy', 'true');
    img.src = base + '&cb=' + Date.now();
  });
});

av20.querySelector('.av-20__theme').addEventListener('click', (e) => {
  const on = av20.dataset.theme !== 'dark';
  av20.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
```
