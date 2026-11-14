---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/buffer-bar/"
title: "Media Buffer Bar with Loaded and Playhead Positions"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The podcast scrubber: three stacked layers — muted track, loaded range, playhead fill — with a dot at the playhead and elapsed/remaining labels flanking the…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media Buffer Bar with Loaded and Playhead Positions
Source: https://codefronts.com/components/css-progress-bars/buffer-bar/

The podcast scrubber: three stacked layers — muted track, loaded range, playhead fill — with a dot at the playhead and elapsed/remaining labels flanking the bar. Slim by default, thicker on hover and focus, and keyboard-seekable.
## HTML
```html
<div class="pb-22">
  <button class="pb-22__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-22__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-22__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-22__stage">
    <div class="pb-22__player" id="pb-22-player" data-playing="true">
      <div class="pb-22__top">
        <span class="pb-22__art" aria-hidden="true">
          <span class="pb-22__artGlow"></span>
          <svg viewBox="0 0 24 24" fill="none"><path d="M8.5 16.5V7.2l9-1.6v9.3" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><ellipse cx="6.6" cy="16.8" rx="2.1" ry="1.9" stroke="currentColor" stroke-width="1.7"/><ellipse cx="15.6" cy="14.9" rx="2.1" ry="1.9" stroke="currentColor" stroke-width="1.7"/></svg>
        </span>
        <span class="pb-22__meta">
          <span class="pb-22__show pb-22__mono">Episode 47 &middot; The Frontend Hours</span>
          <span class="pb-22__title">Everything is a progress bar</span>
          <span class="pb-22__guest">with Maya Okonkwo</span>
        </span>
      </div>

      <div class="pb-22__scrub">
        <span class="pb-22__time pb-22__mono" id="pb-22-elapsed">14:42</span>
        <div class="pb-22__trackPad" id="pb-22-pad">
          <div class="pb-22__track" id="pb-22-track" tabindex="0" role="slider" aria-label="Seek within episode" aria-valuemin="0" aria-valuemax="2820" aria-valuenow="882" aria-valuetext="14:42 elapsed, 32:18 remaining" style="--value:31.3; --loaded:74">
            <span class="pb-22__loaded"></span>
            <span class="pb-22__played"></span>
            <span class="pb-22__dot"></span>
          </div>
        </div>
        <span class="pb-22__time pb-22__mono" id="pb-22-remain">-32:18</span>
      </div>

      <div class="pb-22__controls">
        <button class="pb-22__ctl" type="button" id="pb-22-back" aria-label="Back 15 seconds">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.9a7.4 7.4 0 1 1-7.35 8.66" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M14.6 2.5 12 4.9l2.6 2.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="pb-22__ctlNum pb-22__mono">15</span>
        </button>
        <button class="pb-22__ctl pb-22__ctl--play" type="button" id="pb-22-toggle" aria-pressed="true" aria-label="Pause">
          <svg class="pb-22__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 5.5l10 6.5-10 6.5z" fill="currentColor"/></svg>
          <svg class="pb-22__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6v12M15 6v12" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
        <button class="pb-22__ctl" type="button" id="pb-22-fwd" aria-label="Forward 30 seconds">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.9a7.4 7.4 0 1 0 7.35 8.66" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M9.4 2.5 12 4.9l-2.6 2.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="pb-22__ctlNum pb-22__mono">30</span>
        </button>
        <button class="pb-22__speed pb-22__mono" type="button" id="pb-22-speed">1.0&times;</button>
      </div>
      <p class="pb-22__hint pb-22__mono" id="pb-22-hint">loaded 74% &middot; playhead 31% &middot; arrows seek 10s</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-22 {
  --bg: #050506;
  --card: #0c0c10;
  --card2: #131318;
  --ink: #f0f0f4;
  --muted: rgba(240,240,244,.58);
  --line: rgba(240,240,244,.12);
  --track: rgba(240,240,244,.13);
  --loadedC: rgba(240,240,244,.34);
  --accent: #4ade80;
  --accent-2: #22d3ee;
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

@supports (color: oklch(82% .18 145)) {
  .pb-22 {
    --accent: oklch(82% .18 148);
    --accent-2: oklch(82% .13 199);
  }
}

.pb-22 *,
.pb-22 *::before,
.pb-22 *::after {
  box-sizing: border-box;
}

.pb-22__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(70% 50% at 20% 0%,color-mix(in srgb,var(--accent) 14%,transparent),transparent 58%), radial-gradient(60% 50% at 95% 100%,color-mix(in srgb,var(--accent-2) 12%,transparent),transparent 60%);
}

.pb-22__theme {
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
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-22__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-22__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-22__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-22__sun {
  display: none;
}

.pb-22__moon {
  display: block;
}

.pb-22[data-theme="light"] .pb-22__sun {
  display: block;
}

.pb-22[data-theme="light"] .pb-22__moon {
  display: none;
}

.pb-22__player {
  inline-size: min(34rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vw,1.2rem);
  padding: clamp(1.3rem,3.4vw,2rem);
  border-radius: 1.6rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 36px 84px -46px rgba(0,0,0,.95);
}

.pb-22__top {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 1rem;
  align-items: center;
}

.pb-22__art {
  position: relative;
  inline-size: 4.5rem;
  block-size: 4.5rem;
  display: grid;
  place-items: center;
  border-radius: 1rem;
  overflow: hidden;
  color: #04140a;
  background: linear-gradient(140deg,var(--accent),var(--accent-2));
  box-shadow: 0 18px 40px -22px color-mix(in srgb,var(--accent) 70%,transparent);
}

.pb-22__artGlow {
  position: absolute;
  inset: -40% -20% auto -20%;
  block-size: 90%;
  background: radial-gradient(50% 60% at 40% 40%,rgba(255,255,255,.55),transparent 70%);
}

.pb-22__art svg {
  position: relative;
  inline-size: 2rem;
  block-size: 2rem;
}

.pb-22__meta {
  display: grid;
  gap: .15rem;
  min-inline-size: 0;
}

.pb-22__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-22__show {
  letter-spacing: .02em;
}

.pb-22__title {
  font-size: clamp(1.05rem,2.6vw,1.3rem);
  font-weight: 650;
  letter-spacing: -.02em;
}

.pb-22__guest {
  font-size: .82rem;
  color: var(--muted);
}

.pb-22__scrub {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .7rem;
  align-items: center;
}

.pb-22__time {
  font-size: .74rem;
  color: var(--muted);
  min-inline-size: 2.9rem;
}

.pb-22__time:last-child {
  text-align: end;
}

.pb-22__trackPad {
  padding-block: 1.05rem;
  cursor: pointer;
}

.pb-22__track {
  position: relative;
  inline-size: 100%;
  block-size: .25rem;
  border-radius: 99px;
  background: var(--track);
  transition: block-size .16s ease;
}

.pb-22__trackPad:hover .pb-22__track,
.pb-22__trackPad:focus-within .pb-22__track {
  block-size: .4rem;
}

.pb-22__track:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 99px;
}

.pb-22__loaded,
.pb-22__played {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  border-radius: 99px;
}

.pb-22__loaded {
  inline-size: calc(var(--loaded,0) * 1%);
  background: var(--loadedC);
  transition: inline-size .5s linear;
}

.pb-22__played {
  inline-size: calc(var(--value,0) * 1%);
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
}

.pb-22__dot {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: calc(var(--value,0) * 1%);
  inline-size: .7rem;
  block-size: .7rem;
  border-radius: 99px;
  background: var(--ink);
  transform: translate(-50%,-50%);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 40%,transparent);
  transition: transform .16s ease;
}

.pb-22__trackPad:hover .pb-22__dot,
.pb-22__trackPad:focus-within .pb-22__dot {
  transform: translate(-50%,-50%) scale(1.25);
}

.pb-22__controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(.6rem,3vw,1.4rem);
}

.pb-22__ctl {
  position: relative;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  border-radius: 99px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: background .18s,transform .18s;
}

.pb-22__ctl:hover {
  background: color-mix(in srgb,var(--ink) 10%,transparent);
  transform: translateY(-1px);
}

.pb-22__ctl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.pb-22__ctl svg {
  inline-size: 1.95rem;
  block-size: 1.95rem;
  grid-area: 1/1;
}

.pb-22__ctlNum {
  position: absolute;
  inset-block-start: 55%;
  inset-inline-start: 50%;
  transform: translate(-50%,-50%);
  font-size: .46rem;
  line-height: 1;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--ink);
  pointer-events: none;
}

.pb-22__ctl--play {
  inline-size: 3.4rem;
  block-size: 3.4rem;
  background: var(--ink);
  color: var(--card);
  box-shadow: 0 14px 30px -16px rgba(0,0,0,.8);
}

.pb-22__ctl--play:hover {
  background: color-mix(in srgb,var(--ink) 90%,var(--accent));
}

.pb-22__ctl--play svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
  display: none;
}

.pb-22__player[data-playing="true"] .pb-22__pauseIcon {
  display: block;
}

.pb-22__player[data-playing="false"] .pb-22__playIcon {
  display: block;
}

.pb-22__speed {
  min-block-size: 2.4rem;
  padding: .45rem .75rem;
  border-radius: .65rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .78rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s,transform .18s;
}

.pb-22__speed:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-22__speed:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.pb-22__hint {
  margin: 0;
  text-align: center;
  opacity: .75;
}

.pb-22[data-theme="light"] {
  --bg: #f6f6f8;
  --card: #ffffff;
  --card2: #fafafc;
  --ink: #0a0a0d;
  --muted: rgba(10,10,13,.6);
  --line: rgba(10,10,13,.1);
  --track: rgba(10,10,13,.12);
  --loadedC: rgba(10,10,13,.28);
  --accent: #16a34a;
  --accent-2: #0891b2;
}

.pb-22[data-theme="light"] .pb-22__theme {
  background: rgba(10,10,13,.05);
}

.pb-22[data-theme="light"] .pb-22__art {
  color: #f8fffb;
}

@media (prefers-color-scheme: light) {
  .pb-22:not([data-theme="dark"]) {
    --bg: #f6f6f8;
    --card: #ffffff;
    --card2: #fafafc;
    --ink: #0a0a0d;
    --muted: rgba(10,10,13,.6);
    --line: rgba(10,10,13,.1);
    --track: rgba(10,10,13,.12);
    --loadedC: rgba(10,10,13,.28);
    --accent: #16a34a;
    --accent-2: #0891b2;
  }

  .pb-22:not([data-theme="dark"]) .pb-22__theme {
    background: rgba(10,10,13,.05);
  }

  .pb-22:not([data-theme="dark"]) .pb-22__art {
    color: #f8fffb;
  }

  .pb-22:not([data-theme="dark"]) .pb-22__sun {
    display: block;
  }

  .pb-22:not([data-theme="dark"]) .pb-22__moon {
    display: none;
  }

  .pb-22[data-theme="dark"] .pb-22__sun {
    display: none;
  }

  .pb-22[data-theme="dark"] .pb-22__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-22 *,
    .pb-22 *::before,
    .pb-22 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-22__player,
    .pb-22__speed,
    .pb-22__theme,
    .pb-22__track {
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .pb-22__played {
    background: Highlight;
  }

  .pb-22__loaded {
    background: GrayText;
  }

  .pb-22__art {
    background: Canvas;
    color: CanvasText;
  }
}
```

## JavaScript
```js
const pb22 = document.querySelector('.pb-22');
if (pb22) {
  const q = (s) => pb22.querySelector(s);
  const DUR = 2820, SPEEDS = [1, 1.25, 1.5, 2];
  const [player, track, elapsed, remain, hint] = ['#pb-22-player','#pb-22-track','#pb-22-elapsed','#pb-22-remain','#pb-22-hint'].map(q);
  let t = 882, loaded = 2087, si = 0, timer;
  const clock = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  const paint = () => {
    const p = t / DUR * 100, l = Math.min(100, loaded / DUR * 100);
    track.style.setProperty('--value', p.toFixed(2));
    track.style.setProperty('--loaded', l.toFixed(2));
    track.setAttribute('aria-valuenow', Math.round(t));
    track.setAttribute('aria-valuetext', clock(t) + ' elapsed, ' + clock(DUR - t) + ' remaining');
    elapsed.textContent = clock(t); remain.textContent = '-' + clock(DUR - t);
    hint.textContent = 'loaded ' + Math.round(l) + '% \u00b7 playhead ' + Math.round(p) + '% \u00b7 arrows seek 10s';
  };
  const seek = (d) => { t = Math.max(0, Math.min(DUR, t + d)); loaded = Math.max(loaded, t + 40); paint(); };
  const toggle = (on) => {
    player.dataset.playing = String(on);
    q('#pb-22-toggle').setAttribute('aria-pressed', String(on));
    q('#pb-22-toggle').setAttribute('aria-label', on ? 'Pause' : 'Play');
    clearInterval(timer);
    if (on) timer = setInterval(() => { t = Math.min(DUR, t + SPEEDS[si] / 2); loaded = Math.min(DUR, Math.max(loaded + 1.4, t + 40)); paint(); if (t >= DUR) toggle(false); }, 500);
  };
  q('#pb-22-toggle').addEventListener('click', () => toggle(player.dataset.playing !== 'true'));
  q('#pb-22-back').addEventListener('click', () => seek(-15));
  q('#pb-22-fwd').addEventListener('click', () => seek(30));
  q('#pb-22-speed').addEventListener('click', (e) => { si = (si + 1) % SPEEDS.length; e.currentTarget.textContent = SPEEDS[si].toFixed(2).replace(/0$/, '') + '\u00d7'; if (player.dataset.playing === 'true') toggle(true); });
  track.addEventListener('keydown', (e) => {
    const d = { ArrowRight: 10, ArrowUp: 10, ArrowLeft: -10, ArrowDown: -10 }[e.key];
    if (d) { e.preventDefault(); seek(d); }
    else if (e.key === 'Home') { e.preventDefault(); t = 0; paint(); }
    else if (e.key === 'End') { e.preventDefault(); t = DUR; paint(); }
  });
  q('#pb-22-pad').addEventListener('pointerdown', (e) => {
    const r = track.getBoundingClientRect();
    t = Math.max(0, Math.min(DUR, (e.clientX - r.left) / r.width * DUR)); loaded = Math.max(loaded, t + 40); paint();
  });
  q('.pb-22__theme').addEventListener('click', (e) => {
    const light = pb22.dataset.theme !== 'light';
    pb22.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  toggle(true); paint();
}
```
