---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/video-buffering-progress-with-buffered-range-overlay/"
title: "Video Buffering Progress with Buffered Range Overlay"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The player bar with two truths in one track: a light buffered range from video.buffered and a bright played fill from currentTime, with a scrubber handle…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Buffering Progress with Buffered Range Overlay
Source: https://codefronts.com/components/css-progress-bars/video-buffering-progress-with-buffered-range-overlay/

The player bar with two truths in one track: a light buffered range from video.buffered and a bright played fill from currentTime, with a scrubber handle riding the playhead. Buffered runs ahead of playback, exactly as a real network does.
## HTML
```html
<div class="pb-10">
  <button class="pb-10__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-10__stage">
    <div class="pb-10__player" id="pb-10-player" data-playing="true">
      <div class="pb-10__frame">
        <span class="pb-10__frameGlow" aria-hidden="true"></span>
        <span class="pb-10__frameGrid" aria-hidden="true"></span>
        <p class="pb-10__frameMeta"><span class="pb-10__live pb-10__mono"><span class="pb-10__liveDot" aria-hidden="true"></span>1080p</span><span class="pb-10__mono">Chapter 3 &middot; View transitions</span></p>
        <p class="pb-10__frameTitle">Building the router bar</p>
        <button class="pb-10__bigPlay" type="button" id="pb-10-big" aria-label="Play or pause">
          <svg class="pb-10__bigPlayIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 5.5l10 6.5-10 6.5z" fill="currentColor"/></svg>
          <svg class="pb-10__bigPauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6v12M15 6v12" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
      </div>

      <div class="pb-10__controls">
        <div class="pb-10__scrubWrap">
          <div class="pb-10__track" id="pb-10-track" tabindex="0" role="slider" aria-label="Seek" aria-valuemin="0" aria-valuemax="225" aria-valuenow="84" aria-valuetext="1:24 of 3:45" style="--value:37; --buffered:72">
            <span class="pb-10__buffered"></span>
            <span class="pb-10__played"></span>
            <span class="pb-10__handle"></span>
          </div>
        </div>

        <div class="pb-10__bottom">
          <button class="pb-10__btn" type="button" id="pb-10-toggle" aria-pressed="true" aria-label="Pause">
            <svg class="pb-10__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 5.5l10 6.5-10 6.5z" fill="currentColor"/></svg>
            <svg class="pb-10__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6v12M15 6v12" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
          </button>
          <p class="pb-10__time pb-10__mono"><span id="pb-10-now">1:24</span><span class="pb-10__sep">/</span><span class="pb-10__dur">3:45</span></p>
          <p class="pb-10__legend">
            <span class="pb-10__key"><i class="pb-10__swatch pb-10__swatch--played"></i>played <span class="pb-10__mono" id="pb-10-pPct">37%</span></span>
            <span class="pb-10__key"><i class="pb-10__swatch pb-10__swatch--buffered"></i>buffered <span class="pb-10__mono" id="pb-10-bPct">72%</span></span>
          </p>
        </div>
      </div>
    </div>
    <p class="pb-10__caption">Arrow keys seek 5 seconds, Home and End jump to the ends &mdash; the track is a <code>role="slider"</code>, because a seek bar is settable.</p>
  </div>
</div>
```
## CSS
```css
.pb-10 {
  --bg: #050507;
  --card: #0b0b0f;
  --ink: #f2f3f7;
  --muted: rgba(242,243,247,.6);
  --line: rgba(242,243,247,.12);
  --track: rgba(242,243,247,.16);
  --buffered-color: rgba(242,243,247,.42);
  --accent: #f43f5e;
  --accent-2: #fb7185;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(66% .22 15)) {
  .pb-10 {
    --accent: oklch(66% .22 15);
    --accent-2: oklch(72% .18 15);
  }
}

.pb-10 *,
.pb-10 *::before,
.pb-10 *::after {
  box-sizing: border-box;
}

.pb-10__stage {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 1rem;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(90% 60% at 50% 0%,color-mix(in srgb,var(--accent) 14%,transparent),transparent 60%);
}

.pb-10__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.07);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-10__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.13);
}

.pb-10__theme:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-10__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-10__sun {
  display: none;
}

.pb-10__moon {
  display: block;
}

.pb-10[data-theme="light"] .pb-10__sun {
  display: block;
}

.pb-10[data-theme="light"] .pb-10__moon {
  display: none;
}

.pb-10__player {
  inline-size: min(48rem,100%);
  border-radius: 1.3rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--card);
  box-shadow: 0 40px 90px -50px rgba(0,0,0,.95);
}

.pb-10__frame {
  position: relative;
  aspect-ratio: 16 / 9;
  display: grid;
  align-content: space-between;
  gap: .5rem;
  padding: clamp(.9rem,2.4vw,1.4rem);
  overflow: hidden;
  background: linear-gradient(145deg,#1b1030 0%,#0b1020 45%,#161022 100%);
}

.pb-10__frameGlow {
  position: absolute;
  inset: -30% -10% auto -10%;
  block-size: 80%;
  pointer-events: none;
  background: radial-gradient(60% 60% at 30% 40%,color-mix(in srgb,var(--accent) 45%,transparent),transparent 70%), radial-gradient(50% 50% at 80% 60%,rgba(96,165,250,.45),transparent 70%);
  filter: blur(6px);
}

.pb-10__frameGrid {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .3;
  background-image: linear-gradient(rgba(255,255,255,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.09) 1px,transparent 1px);
  background-size: 2.6rem 2.6rem;
  mask-image: linear-gradient(180deg,transparent,black 40%,black 70%,transparent);
}

.pb-10__frameMeta {
  position: relative;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
  color: rgba(255,255,255,.82);
}

.pb-10__mono {
  font-family: var(--mono);
  font-size: .74rem;
  font-variant-numeric: tabular-nums;
}

.pb-10__live {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .24rem .5rem;
  border-radius: .4rem;
  background: rgba(0,0,0,.4);
  border: 1px solid rgba(255,255,255,.18);
}

.pb-10__liveDot {
  inline-size: .42rem;
  block-size: .42rem;
  border-radius: 99px;
  background: var(--accent);
}

.pb-10__frameTitle {
  position: relative;
  margin: 0;
  font-size: clamp(1.2rem,3.4vw,1.9rem);
  font-weight: 650;
  letter-spacing: -.024em;
  color: #fff;
  text-shadow: 0 2px 20px rgba(0,0,0,.5);
}

.pb-10__bigPlay {
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: 4.2rem;
  block-size: 4.2rem;
  display: grid;
  place-items: center;
  border-radius: 99px;
  border: 1px solid rgba(255,255,255,.28);
  color: #fff;
  cursor: pointer;
  background: rgba(0,0,0,.35);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: transform .2s,background .2s,opacity .2s;
}

.pb-10__bigPlay:hover {
  transform: scale(1.06);
  background: rgba(0,0,0,.5);
}

.pb-10__bigPlay:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.pb-10__bigPlay svg {
  inline-size: 1.7rem;
  block-size: 1.7rem;
  grid-area: 1/1;
  display: none;
}

.pb-10__player[data-playing="true"] .pb-10__bigPlay {
  opacity: 0;
  pointer-events: none;
}

.pb-10__player[data-playing="true"] .pb-10__bigPauseIcon {
  display: block;
}

.pb-10__player[data-playing="false"] .pb-10__bigPlayIcon {
  display: block;
}

.pb-10__controls {
  display: grid;
  gap: .7rem;
  padding: clamp(.9rem,2.2vw,1.2rem) clamp(.9rem,2.4vw,1.4rem) clamp(1rem,2.4vw,1.3rem);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.pb-10__scrubWrap {
  padding-block: .5rem;
}

.pb-10__track {
  position: relative;
  inline-size: 100%;
  block-size: .35rem;
  border-radius: 99px;
  background: var(--track);
  cursor: pointer;
  transition: block-size .16s ease;
}

.pb-10__track:hover,
.pb-10__track:focus-visible {
  block-size: .55rem;
}

.pb-10__track:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 6px;
  border-radius: 99px;
}

.pb-10__buffered,
.pb-10__played {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  border-radius: 99px;
}

.pb-10__buffered {
  inline-size: calc(var(--buffered,0) * 1%);
  background: var(--buffered-color);
  transition: inline-size .4s linear;
}

.pb-10__played {
  inline-size: calc(var(--value,0) * 1%);
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
}

.pb-10__handle {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: calc(var(--value,0) * 1%);
  inline-size: .85rem;
  block-size: .85rem;
  border-radius: 99px;
  background: #fff;
  transform: translate(-50%,-50%);
  box-shadow: 0 0 0 4px color-mix(in srgb,var(--accent) 45%,transparent);
  transition: transform .16s ease;
}

.pb-10__track:hover .pb-10__handle,
.pb-10__track:focus-visible .pb-10__handle {
  transform: translate(-50%,-50%) scale(1.2);
}

.pb-10__bottom {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
  align-items: center;
}

.pb-10__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 8%,transparent);
  color: var(--ink);
  cursor: pointer;
  transition: background .18s,transform .18s;
}

.pb-10__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 15%,transparent);
}

.pb-10__btn:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-10__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  grid-area: 1/1;
  display: none;
}

.pb-10__player[data-playing="true"] .pb-10__pauseIcon {
  display: block;
}

.pb-10__player[data-playing="false"] .pb-10__playIcon {
  display: block;
}

.pb-10__time {
  margin: 0;
  display: flex;
  gap: .4rem;
  font-size: .85rem;
  color: var(--ink);
}

.pb-10__sep,
.pb-10__dur {
  color: var(--muted);
}

.pb-10__legend {
  margin: 0 0 0 auto;
  display: flex;
  flex-wrap: wrap;
  gap: .9rem;
  font-size: .76rem;
  color: var(--muted);
}

.pb-10__key {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
}

.pb-10__swatch {
  inline-size: .7rem;
  block-size: .35rem;
  border-radius: 99px;
}

.pb-10__swatch--played {
  background: var(--accent);
}

.pb-10__swatch--buffered {
  background: var(--buffered-color);
}

.pb-10__caption {
  margin: 0;
  inline-size: min(48rem,100%);
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-10__caption code {
  font-family: var(--mono);
  font-size: .85em;
  color: var(--accent-2);
}

.pb-10[data-theme="light"] {
  --bg: #f4f4f7;
  --card: #ffffff;
  --ink: #101018;
  --muted: rgba(16,16,24,.62);
  --line: rgba(16,16,24,.1);
  --track: rgba(16,16,24,.12);
  --buffered-color: rgba(16,16,24,.3);
  --accent: #e11d48;
  --accent-2: #be123c;
}

.pb-10[data-theme="light"] .pb-10__theme {
  background: rgba(16,16,24,.05);
}

@media (prefers-color-scheme: light) {
  .pb-10:not([data-theme="dark"]) {
    --bg: #f4f4f7;
    --card: #ffffff;
    --ink: #101018;
    --muted: rgba(16,16,24,.62);
    --line: rgba(16,16,24,.1);
    --track: rgba(16,16,24,.12);
    --buffered-color: rgba(16,16,24,.3);
    --accent: #e11d48;
    --accent-2: #be123c;
  }

  .pb-10:not([data-theme="dark"]) .pb-10__theme {
    background: rgba(16,16,24,.05);
  }

  .pb-10:not([data-theme="dark"]) .pb-10__sun {
    display: block;
  }

  .pb-10:not([data-theme="dark"]) .pb-10__moon {
    display: none;
  }

  .pb-10[data-theme="dark"] .pb-10__sun {
    display: none;
  }

  .pb-10[data-theme="dark"] .pb-10__moon {
    display: block;
  }
}

@media (max-width: 32rem) {
  .pb-10__legend {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-10 *,
    .pb-10 *::before,
    .pb-10 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-10__player,
    .pb-10__btn,
    .pb-10__theme,
    .pb-10__track {
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .pb-10__played {
    background: Highlight;
  }

  .pb-10__buffered {
    background: GrayText;
  }
}
```

## JavaScript
```js
const pb10 = document.querySelector('.pb-10');
if (pb10) {
  const q = (s) => pb10.querySelector(s);
  const [player, track, now] = ['#pb-10-player','#pb-10-track','#pb-10-now'].map(q);
  const DUR = 225;
  let t = 84, buf = 162, timer;
  const clock = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  const paint = () => {
    const p = t / DUR * 100, b = Math.min(100, buf / DUR * 100);
    track.style.setProperty('--value', p.toFixed(2));
    track.style.setProperty('--buffered', b.toFixed(2));
    track.setAttribute('aria-valuenow', Math.round(t));
    track.setAttribute('aria-valuetext', clock(t) + ' of ' + clock(DUR));
    now.textContent = clock(t);
    q('#pb-10-pPct').textContent = Math.round(p) + '%';
    q('#pb-10-bPct').textContent = Math.round(b) + '%';
  };
  const tick = () => { t = Math.min(DUR, t + 0.4); buf = Math.min(DUR, Math.max(buf + 0.9, t + 6)); paint(); if (t >= DUR) toggle(false); };
  const toggle = (on) => {
    player.dataset.playing = String(on);
    q('#pb-10-toggle').setAttribute('aria-pressed', String(on));
    q('#pb-10-toggle').setAttribute('aria-label', on ? 'Pause' : 'Play');
    clearInterval(timer); if (on) timer = setInterval(tick, 100);
  };
  [q('#pb-10-toggle'), q('#pb-10-big')].forEach((b) => b.addEventListener('click', () => toggle(player.dataset.playing !== 'true')));
  const seek = (d) => { t = Math.max(0, Math.min(DUR, t + d)); buf = Math.max(buf, t + 6); paint(); };
  track.addEventListener('keydown', (e) => {
    const d = { ArrowRight: 5, ArrowUp: 5, ArrowLeft: -5, ArrowDown: -5 }[e.key];
    if (d) { e.preventDefault(); seek(d); }
    else if (e.key === 'Home') { e.preventDefault(); t = 0; paint(); }
    else if (e.key === 'End') { e.preventDefault(); t = DUR; paint(); }
  });
  track.addEventListener('pointerdown', (e) => {
    const r = track.getBoundingClientRect();
    t = Math.max(0, Math.min(DUR, (e.clientX - r.left) / r.width * DUR)); buf = Math.max(buf, t + 6); paint();
  });
  q('.pb-10__theme').addEventListener('click', (e) => {
    const light = pb10.dataset.theme !== 'light';
    pb10.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  toggle(true); paint();
}
```
