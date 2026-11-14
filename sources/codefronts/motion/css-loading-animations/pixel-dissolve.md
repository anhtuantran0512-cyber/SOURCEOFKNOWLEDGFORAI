---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/pixel-dissolve/"
title: "Pixel Dissolve Reveal Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "A media-grade reveal: a 36-tile mosaic dissolves in a pseudo-random order to expose the artwork underneath, then re-forms and repeats."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pixel Dissolve Reveal Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/pixel-dissolve/

A media-grade reveal: a 36-tile mosaic dissolves in a pseudo-random order to expose the artwork underneath, then re-forms and repeats. The scatter comes from a CSS mod() hash on each tile's index — no JavaScript randomness, no 36 hand-written delays — with a linear fallback for engines that lack mod().
## HTML
```html
<div class="la-19" data-state="loading">
  <div class="la-19__chrome">
    <button class="la-19__btn la-19__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-19__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-19__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-19__btn la-19__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-19__card" role="status" aria-live="polite" aria-label="Loading gallery image, 3 of 12">
    <div class="la-19__frame">
      <span class="la-19__art" aria-hidden="true"></span>
      <div class="la-19__mosaic" aria-hidden="true">
        <i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i><i style="--i:3"></i><i style="--i:4"></i><i style="--i:5"></i>
        <i style="--i:6"></i><i style="--i:7"></i><i style="--i:8"></i><i style="--i:9"></i><i style="--i:10"></i><i style="--i:11"></i>
        <i style="--i:12"></i><i style="--i:13"></i><i style="--i:14"></i><i style="--i:15"></i><i style="--i:16"></i><i style="--i:17"></i>
        <i style="--i:18"></i><i style="--i:19"></i><i style="--i:20"></i><i style="--i:21"></i><i style="--i:22"></i><i style="--i:23"></i>
        <i style="--i:24"></i><i style="--i:25"></i><i style="--i:26"></i><i style="--i:27"></i><i style="--i:28"></i><i style="--i:29"></i>
        <i style="--i:30"></i><i style="--i:31"></i><i style="--i:32"></i><i style="--i:33"></i><i style="--i:34"></i><i style="--i:35"></i>
      </div>
    </div>

    <div class="la-19__copy">
      <p class="la-19__label">
        <span class="la-19__load">Decoding image</span>
        <span class="la-19__ready">Golden Gate at dusk</span>
      </p>
      <p class="la-19__meta">gg-dusk-4096.avif <span aria-hidden="true">·</span> 3 of 12 <span aria-hidden="true">·</span> Sam Rivera</p>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.la-19 {
  --bg: #0a0b11;
  --surface: #13151d;
  --ink: #f2f4fa;
  --muted: #98a0b4;
  --line: #232833;
  --tile: #13151d;
  --acc: #ffd166;
  --ok: #3ad68f;
  --ring: #ffd166;
  --dur: 3.6s;
  --n: 6;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(80% 60% at 50% 0%, #191d28, var(--bg));
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-19,
.la-19 *,
.la-19 *::before,
.la-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-19 {
    --acc: oklch(86% .14 85);
    --ok: oklch(78% .16 160);
  }
}

.la-19__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: .8rem .8rem 1.1rem;
  display: grid;
  gap: .9rem;
  border-radius: 1.4rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px #000, 0 0 0 1px rgba(255,255,255,.03) inset;
}

.la-19__frame {
  position: relative;
  aspect-ratio: 4/3;
  border-radius: 1rem;
  overflow: hidden;
  isolation: isolate;
}

.la-19__art {
  position: absolute;
  inset: 0;
  background: radial-gradient(50% 40% at 72% 26%, #ffd8a0, transparent 62%), linear-gradient(180deg, #2c3f6b 0 38%, #7c4a6b 38% 58%, #221b33 58%), linear-gradient(90deg, #1a2440, #3a2a4a);
}

.la-19__art::after {
  content: "";
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  block-size: 34%;
  background: linear-gradient(180deg, transparent, rgba(6,8,16,.7)), repeating-linear-gradient(90deg, rgba(255,209,102,.16) 0 3px, transparent 3px 12px);
}

.la-19__mosaic {
  position: absolute;
  inset: -1px;
  /* 1px bleed kills sub-pixel seams at the edges */
  display: grid;
  grid-template-columns: repeat(var(--n),1fr);
  grid-auto-rows: 1fr;
}

.la-19__mosaic i {
  background: var(--tile);
  box-shadow: 0 0 0 1px var(--tile);
  /* and hairlines between tiles */
  animation: la-19-cycle var(--dur) steps(2, jump-none) infinite;
  animation-delay: calc(var(--i) * .06s);
}

@supports (width: mod(3, 2)) {
  .la-19__mosaic i {
    animation-delay: calc(mod(var(--i) * 17, 36) * .098s);
  }
}

@keyframes la-19-cycle {
  0%,
    20% {
    opacity: 1;
  }

  36%,
    62% {
    opacity: 0;
  }

  80%,
    100% {
    opacity: 1;
  }
}

.la-19__copy {
  display: grid;
  gap: .22rem;
  padding-inline: .35rem;
}

.la-19__label {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-19__ready {
  display: none;
}

.la-19__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-19.is-ready .la-19__mosaic i {
  animation: none;
  opacity: 0;
}

.la-19.is-ready .la-19__frame {
  box-shadow: 0 0 0 1px color-mix(in oklab,var(--ok) 35%,transparent) inset;
}

.la-19.is-ready .la-19__load {
  display: none;
}

.la-19.is-ready .la-19__ready {
  display: inline;
}

.la-19__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-19__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 22%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 78%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-19__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-19__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-19__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-19__sun {
  display: none;
}

.la-19__theme[aria-pressed="true"] .la-19__sun {
  display: block;
}

.la-19__theme[aria-pressed="true"] .la-19__moon {
  display: none;
}

.la-19__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #04231a;
}

@media (prefers-color-scheme: light) {
  .la-19:not([data-theme="dark"]) {
    --bg: #eff1f6;
    --surface: #ffffff;
    --ink: #0c101a;
    --muted: #5f6a7d;
    --line: #e2e6ee;
    --tile: #ffffff;
    --acc: #b8860b;
    --ok: #0f9d63;
    --ring: #b8860b;
  }

  .la-19:not([data-theme="dark"]) .la-19__card {
    box-shadow: 0 1px 0 #fff inset, 0 34px 60px -42px rgba(12,16,26,.24);
  }

  .la-19:not([data-theme="dark"]) .la-19__done[aria-pressed="true"] {
    color: #fff;
  }
}

.la-19[data-theme="light"] {
  --bg: #eff1f6;
  --surface: #ffffff;
  --ink: #0c101a;
  --muted: #5f6a7d;
  --line: #e2e6ee;
  --tile: #ffffff;
  --acc: #b8860b;
  --ok: #0f9d63;
  --ring: #b8860b;
}

.la-19[data-theme="light"] .la-19__card {
  box-shadow: 0 1px 0 #fff inset, 0 34px 60px -42px rgba(12,16,26,.24);
}

.la-19[data-theme="light"] .la-19__done[aria-pressed="true"] {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .la-19 * {
    animation: none !important;
    transition: none !important;
  }

  .la-19__mosaic i:nth-child(3n) {
    opacity: 0;
  }

  .la-19__mosaic i:nth-child(4n+1) {
    opacity: 0;
  }
}

@media (forced-colors: active) {
  .la-19__card {
    border: 1px solid CanvasText;
  }

  .la-19__mosaic i {
    background: Canvas;
  }

  .la-19__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-19');
  if (!root) return;
  const theme = root.querySelector('.la-19__theme');
  const done = root.querySelector('.la-19__done');
  const region = root.querySelector('[role="status"]');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');        // img.decode().then(...)
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    region.setAttribute('aria-label', ready ? 'Golden Gate at dusk, image 3 of 12' : 'Loading gallery image, 3 of 12');
  });
  sync();
})();
```
