---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/video-streaming-buffering-loader/"
title: "Video Streaming Buffering Loader"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "A player-grade buffering overlay: a segmented ring where the buffered arc sweeps ahead of twelve chunk ticks, a glassy scrim over the video frame, a live…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Streaming Buffering Loader
Source: https://codefronts.com/motion/css-loading-animations/video-streaming-buffering-loader/

A player-grade buffering overlay: a segmented ring where the buffered arc sweeps ahead of twelve chunk ticks, a glassy scrim over the video frame, a live timecode, and a quality chip that only surfaces once the buffer is healthy — the same information hierarchy Netflix and YouTube use to tell you "we're still fetching, but we're fine". Built with one conic-gradient, a mask ring and zero images.
## HTML
```html
<div class="la-02" data-state="loading">
  <div class="la-02__chrome">
    <button class="la-02__btn la-02__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-02__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-02__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-02__btn la-02__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <div class="la-02__player">
    <div class="la-02__frame" aria-hidden="true"></div>
    <div class="la-02__scrim" role="status" aria-live="polite" aria-label="Buffering high definition stream">
      <div class="la-02__ring">
        <span class="la-02__arc" aria-hidden="true"></span>
        <span class="la-02__ticks" aria-hidden="true">
          <i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i><i style="--i:3"></i>
          <i style="--i:4"></i><i style="--i:5"></i><i style="--i:6"></i><i style="--i:7"></i>
          <i style="--i:8"></i><i style="--i:9"></i><i style="--i:10"></i><i style="--i:11"></i>
        </span>
        <svg class="la-02__glyph" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
          <path class="la-02__play" d="M9 6.5 18 12l-9 5.5z"/>
          <path class="la-02__pause" d="M9.5 7v10M14.5 7v10"/>
        </svg>
      </div>
      <p class="la-02__label">
        <span class="la-02__load">Buffering HD stream</span>
        <span class="la-02__ready">Ready to play</span>
      </p>
      <p class="la-02__chip"><span class="la-02__q">1080p</span> <span aria-hidden="true">·</span> Dolby Atmos</p>
    </div>
    <div class="la-02__bar" aria-hidden="true"><span class="la-02__buf"></span><span class="la-02__head"></span></div>
    <p class="la-02__time" aria-hidden="true">00:42 / 21:36</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-02-deg {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.la-02 {
  --bg: #0a0b10;
  --surface: #14161d;
  --ink: #f4f6fa;
  --muted: #9aa3b2;
  --line: #262b36;
  --acc: #ff3b30;
  --acc-2: #ffb020;
  --ring: #ff5d54;
  --scrim: .55;
  --dur: 4.8s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(90% 70% at 50% 0%, #1a1d27, var(--bg));
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-02,
.la-02 *,
.la-02 *::before,
.la-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-02 {
    --acc: oklch(62% .23 26);
    --acc-2: oklch(80% .16 78);
  }
}

.la-02__player {
  position: relative;
  inline-size: min(30rem,100%);
  aspect-ratio: 16/10;
  border-radius: 1.25rem;
  overflow: hidden;
  isolation: isolate;
  border: 1px solid var(--line);
  box-shadow: 0 50px 90px -50px rgba(0,0,0,.9), 0 0 0 1px rgba(255,255,255,.03) inset;
}

.la-02__frame {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 80% at 22% 18%, color-mix(in oklab,var(--acc) 55%,transparent), transparent 60%), radial-gradient(50% 70% at 82% 74%, color-mix(in oklab,#4b6bff 60%,transparent), transparent 62%), linear-gradient(150deg,#1d2130,#0c0e15 70%);
  filter: saturate(1.05);
}

.la-02__frame::after {
  content: "";
  position: absolute;
  inset: 0;
  opacity: .5;
  mix-blend-mode: overlay;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.05) 0 1px, transparent 1px 3px);
}

.la-02__scrim {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: .85rem;
  background: color-mix(in srgb, #05060a calc(var(--scrim) * 100%), transparent);
  -webkit-backdrop-filter: blur(6px) saturate(1.1);
  backdrop-filter: blur(6px) saturate(1.1);
  text-align: center;
  padding: 1rem;
}

.la-02__ring {
  position: relative;
  inline-size: 5.5rem;
  block-size: 5.5rem;
  display: grid;
  place-items: center;
}

.la-02__ring::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(rgba(255,255,255,.16) 0 360deg);
  mask: radial-gradient(closest-side, transparent 71%, #000 72%);
  -webkit-mask: radial-gradient(closest-side, transparent 71%, #000 72%);
}

.la-02__arc {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: conic-gradient(from -90deg, var(--acc) var(--la-02-deg, 200deg), transparent 0);
  mask: radial-gradient(closest-side, transparent 71%, #000 72%);
  -webkit-mask: radial-gradient(closest-side, transparent 71%, #000 72%);
  animation: la-02-buffer var(--dur) steps(12, jump-none) infinite;
  filter: drop-shadow(0 0 8px color-mix(in oklab,var(--acc) 55%,transparent));
}

@keyframes la-02-buffer {
  from {
    --la-02-deg: 0deg;
  }

  to {
    --la-02-deg: 360deg;
  }
}

.la-02__ticks {
  position: absolute;
  inset: 0;
}

.la-02__ticks i {
  position: absolute;
  inset: 0;
  display: grid;
  justify-items: center;
  rotate: calc(var(--i) * 30deg);
}

.la-02__ticks i::before {
  content: "";
  inline-size: 2px;
  block-size: .34rem;
  border-radius: 2px;
  margin-block-start: .16rem;
  background: rgba(255,255,255,.45);
  animation: la-02-tick var(--dur) linear infinite;
  animation-delay: calc(var(--i) * (var(--dur) / 12));
}

@keyframes la-02-tick {
  0%,
    6% {
    background: var(--acc-2);
    block-size: .5rem;
  }

  14%,
    100% {
    background: rgba(255,255,255,.35);
    block-size: .34rem;
  }
}

.la-02__glyph {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  fill: none;
  stroke: var(--ink);
  stroke-width: 1.8;
  stroke-linejoin: round;
  stroke-linecap: round;
}

.la-02__play {
  fill: var(--ink);
  stroke: none;
  opacity: 0;
}

.la-02__pause {
  opacity: .85;
  animation: la-02-pulse 1.6s ease-in-out infinite;
}

@keyframes la-02-pulse {
  50% {
    opacity: .35;
  }
}

.la-02__label {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.la-02__ready {
  display: none;
}

.la-02__chip {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .3rem .6rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .04em;
  color: var(--muted);
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.1);
  opacity: 0;
  animation: la-02-chip var(--dur) linear infinite;
}

.la-02__q {
  color: var(--acc-2);
}

@keyframes la-02-chip {
  0%,
    72% {
    opacity: 0;
    translate: 0 4px;
  }

  84%,
    100% {
    opacity: 1;
    translate: 0 0;
  }
}

.la-02__bar {
  position: absolute;
  inset-inline: 1rem;
  inset-block-end: 1.5rem;
  block-size: 3px;
  border-radius: 999px;
  background: rgba(255,255,255,.16);
}

.la-02__buf {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  border-radius: 999px;
  background: rgba(255,255,255,.4);
  inline-size: 22%;
  animation: la-02-buf var(--dur) steps(12, jump-none) infinite;
}

.la-02__head {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 18%;
  border-radius: 999px;
  background: var(--acc);
}

@keyframes la-02-buf {
  from {
    inline-size: 18%;
  }

  to {
    inline-size: 100%;
  }
}

.la-02__time {
  position: absolute;
  inset-inline-start: 1rem;
  inset-block-end: .4rem;
  margin: 0;
  font-family: var(--mono);
  font-size: .65rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-02.is-ready .la-02__scrim {
  background: transparent;
  -webkit-backdrop-filter: none;
  backdrop-filter: none;
}

.la-02.is-ready .la-02__arc,
.la-02.is-ready .la-02__ticks i::before,
.la-02.is-ready .la-02__buf {
  animation: none;
}

.la-02.is-ready .la-02__arc {
  --la-02-deg: 360deg;
}

.la-02.is-ready .la-02__buf {
  inline-size: 100%;
}

.la-02.is-ready .la-02__pause {
  opacity: 0;
  animation: none;
}

.la-02.is-ready .la-02__play {
  opacity: 1;
}

.la-02.is-ready .la-02__load {
  display: none;
}

.la-02.is-ready .la-02__ready {
  display: inline;
}

.la-02.is-ready .la-02__chip {
  animation: none;
  opacity: 1;
  translate: 0 0;
}

.la-02__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-02__btn {
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

.la-02__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-02__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-02__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-02__sun {
  display: none;
}

.la-02__theme[aria-pressed="true"] .la-02__sun {
  display: block;
}

.la-02__theme[aria-pressed="true"] .la-02__moon {
  display: none;
}

.la-02__done[aria-pressed="true"] {
  background: var(--acc);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .la-02:not([data-theme="dark"]) {
    --bg: #eceef3;
    --surface: #ffffff;
    --ink: #0b0e14;
    --muted: #5d6675;
    --line: #dfe3ea;
    --scrim: .42;
  }

  .la-02:not([data-theme="dark"]) .la-02__scrim {
    color: #fff;
  }

  .la-02:not([data-theme="dark"]) .la-02__player {
    box-shadow: 0 40px 70px -45px rgba(11,14,20,.5);
  }
}

.la-02[data-theme="light"] {
  --bg: #eceef3;
  --surface: #ffffff;
  --ink: #0b0e14;
  --muted: #5d6675;
  --line: #dfe3ea;
  --scrim: .42;
}

.la-02[data-theme="light"] .la-02__scrim {
  color: #fff;
}

.la-02[data-theme="light"] .la-02__glyph {
  stroke: #fff;
}

.la-02[data-theme="light"] .la-02__play {
  fill: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .la-02 * {
    animation: none !important;
    transition: none !important;
  }

  .la-02__arc {
    --la-02-deg: 250deg;
  }

  .la-02__buf {
    inline-size: 70%;
  }

  .la-02__chip {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .la-02__player {
    border: 1px solid CanvasText;
  }

  .la-02__arc {
    background: Highlight;
  }

  .la-02__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-02');
  if (!root) return;
  const theme = root.querySelector('.la-02__theme');
  const done = root.querySelector('.la-02__done');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');        // fires on video 'canplaythrough'
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    root.querySelector('.la-02__scrim').setAttribute('aria-label', ready ? 'Stream ready to play' : 'Buffering high definition stream');
  });
  sync();
})();
```
