---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-voice-message-chat-bubble/"
title: "CSS Voice Message Chat Bubble"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A voice-note bubble with a real scrubbable waveform — 44 bars, no canvas, no library."
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Voice Message Chat Bubble
Source: https://codefronts.com/snippets/css-chat-bubbles/css-voice-message-chat-bubble/

A voice-note bubble with a real scrubbable waveform — 44 bars, no canvas, no library. The played portion is revealed by a second bar layer clipped to the progress width, so the fill animates on the compositor. Click or drag anywhere on the wave to seek, use the arrow keys on the slider, switch playback speed, and open the transcript in a <details> that animates with ::details-content.
## HTML
```html
<div class="cb-13">
  <button class="cb-13__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <div class="cb-13__stage">
    <div class="cb-13__turn">
      <img class="cb-13__avatar" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="44" height="44" alt="Idris Bello" loading="lazy" decoding="async">
      <div class="cb-13__bubble">
        <div class="cb-13__row">
          <button class="cb-13__play" id="cb-13-play" type="button" aria-label="Play voice message, 42 seconds">
            <svg class="cb-13__ico-play" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8.5 5.5 18 12l-9.5 6.5z" fill="currentColor"/></svg>
            <svg class="cb-13__ico-pause" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="7.5" y="5.5" width="3.4" height="13" rx="1.2" fill="currentColor"/><rect x="13.1" y="5.5" width="3.4" height="13" rx="1.2" fill="currentColor"/></svg>
          </button>

          <div class="cb-13__wave" id="cb-13-wave">
            <div class="cb-13__bars" id="cb-13-bars" aria-hidden="true"></div>
            <div class="cb-13__fill" id="cb-13-fill" aria-hidden="true"><div class="cb-13__bars" id="cb-13-bars-2"></div></div>
            <input class="cb-13__seek" id="cb-13-seek" type="range" min="0" max="42" step="0.1" value="0" aria-label="Seek voice message">
          </div>

          <button class="cb-13__speed" id="cb-13-speed" type="button" aria-label="Playback speed: 1 times">1×</button>
        </div>

        <div class="cb-13__foot">
          <time class="cb-13__time" id="cb-13-time" datetime="PT42S">0:42</time>
          <span class="cb-13__dot" aria-hidden="true"></span>
          <span class="cb-13__sent"><time datetime="2027-08-03T14:08">14:08</time></span>
        </div>

        <details class="cb-13__tx">
          <summary>Transcript</summary>
          <p>Quick one — the studio's free on Saturday after eleven, so if you can get the drums loaded by then we'll have the whole afternoon. Bring the ribbon mic if it's still with you.</p>
        </details>
      </div>
    </div>
    <p class="cb-13__sr" id="cb-13-status" role="status" aria-live="polite"></p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&display=swap');

.cb-13 {
  --bg: #0f1014;
  --surface: #191b22;
  --ink: #f1f2f7;
  --muted: #949bab;
  --line: #262a34;
  --in: #20242e;
  --in-ink: #f1f2f7;
  --acc: #38e07b;
  --acc-ink: #08130c;
  --dim: #3d4352;
  --ring: #38e07b;
  --shadow: rgba(0,0,0,.6);
  --bar-w: 3px;
  --bar-gap: 2px;
  --sans: "Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(85% 55% at 50% 100%, color-mix(in oklab,var(--acc) 15%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-13,
.cb-13 *,
.cb-13 *::before,
.cb-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-13 {
    --bg: oklch(16% .012 270);
    --surface: oklch(22% .015 270);
    --ink: oklch(96% .005 270);
    --muted: oklch(71% .02 270);
    --line: oklch(29% .018 270);
    --in: oklch(25% .018 270);
    --acc: oklch(82% .19 150);
    --acc-ink: oklch(20% .06 150);
    --dim: oklch(42% .02 270);
  }
}

.cb-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-13 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.cb-13__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-13__theme:hover {
  transform: translateY(-2px);
}

.cb-13__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-13__moon {
  display: none;
}

.cb-13__sun {
  display: block;
}

.cb-13__stage {
  inline-size: min(100%,30rem);
}

.cb-13__turn {
  display: flex;
  align-items: flex-end;
  gap: .6rem;
}

.cb-13__avatar {
  flex: 0 0 auto;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}

.cb-13__bubble {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  padding: .7rem .85rem .6rem;
  border-radius: 1.4rem 1.4rem 1.4rem .4rem;
  background: var(--in);
  color: var(--in-ink);
  box-shadow: 0 20px 50px -35px var(--shadow);
}

.cb-13__bubble::after {
  content: '';
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: -8px;
  border-block: 9px solid transparent;
  border-inline-end: 10px solid var(--in);
}

.cb-13__row {
  display: flex;
  align-items: center;
  gap: .7rem;
}

.cb-13__play {
  flex: 0 0 auto;
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: var(--acc);
  color: var(--acc-ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-13__play:hover {
  transform: scale(1.07);
}

.cb-13__play svg {
  inline-size: 22px;
  block-size: 22px;
}

.cb-13__ico-pause {
  display: none;
}

.cb-13[data-playing] .cb-13__ico-play {
  display: none;
}

.cb-13[data-playing] .cb-13__ico-pause {
  display: block;
}
/* ── waveform ── */

.cb-13__wave {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  block-size: 2.4rem;
  --p: 0%;
}

.cb-13__bars {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  gap: min(var(--bar-gap), .6%);
  inline-size: 100%;
}

.cb-13__bar {
  flex: 1 1 0;
  min-inline-size: 0;
  border-radius: 999px;
  background: var(--dim);
  block-size: calc(8% + var(--h) * 92%);
  transition: background .25s;
}

.cb-13__fill {
  position: absolute;
  inset: 0;
  overflow: hidden;
  inline-size: var(--p);
  pointer-events: none;
}

.cb-13__fill .cb-13__bars {
  inline-size: var(--wave-w,100%);
}

.cb-13__fill .cb-13__bar {
  background: var(--acc);
}

.cb-13__seek {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  appearance: none;
  -webkit-appearance: none;
  background: transparent;
  cursor: pointer;
}

.cb-13__seek::-webkit-slider-thumb {
  -webkit-appearance: none;
  inline-size: 16px;
  block-size: 100%;
}

.cb-13__seek::-moz-range-thumb {
  inline-size: 16px;
  block-size: 100%;
  border: 0;
}
/* the playhead is drawn by the wave itself, so it lines up with the fill edge exactly */

.cb-13__wave::after {
  content: '';
  position: absolute;
  inset-block: -2px;
  inset-inline-start: var(--p);
  inline-size: 2px;
  border-radius: 2px;
  background: var(--acc);
  opacity: 0;
  transition: opacity .2s;
  pointer-events: none;
}

.cb-13[data-playing] .cb-13__wave::after,
.cb-13__wave:hover::after,
.cb-13__wave:focus-within::after {
  opacity: 1;
}

.cb-13__speed {
  flex: 0 0 auto;
  min-inline-size: 44px;
  min-block-size: 32px;
  padding: .2rem .5rem;
  cursor: pointer;
  border: 1px solid var(--line);
  border-radius: .6rem;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .76rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  transition: color .2s, border-color .2s;
}

.cb-13__speed:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--acc) 50%,var(--line));
}

.cb-13__foot {
  display: flex;
  align-items: center;
  gap: .45rem;
  padding: .5rem .2rem .1rem;
}

.cb-13__time {
  font-size: .72rem;
  font-weight: 600;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-13__dot {
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 50%;
  background: var(--acc);
}

.cb-13[data-played] .cb-13__dot {
  background: var(--dim);
}

.cb-13__sent {
  margin-inline-start: auto;
  font-size: .68rem;
  font-weight: 500;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}
/* ── transcript ── */

.cb-13__tx {
  margin-block-start: .35rem;
  border-block-start: 1px solid var(--line);
}

.cb-13__tx summary {
  display: flex;
  align-items: center;
  gap: .35rem;
  min-block-size: 40px;
  cursor: pointer;
  font-size: .76rem;
  font-weight: 600;
  color: var(--muted);
  list-style: none;
}

.cb-13__tx summary::-webkit-details-marker {
  display: none;
}

.cb-13__tx summary::after {
  content: '';
  inline-size: .42rem;
  block-size: .42rem;
  border: solid currentColor;
  border-width: 0 1.6px 1.6px 0;
  rotate: 45deg;
  translate: 0 -1px;
  transition: rotate .3s cubic-bezier(.16,1,.3,1);
}

.cb-13__tx[open] summary::after {
  rotate: 225deg;
  translate: 0 1px;
}

.cb-13__tx summary:hover {
  color: var(--ink);
}

.cb-13__tx p {
  margin: 0 0 .5rem;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@supports (interpolate-size: allow-keywords) {
  .cb-13 {
    interpolate-size: allow-keywords;
  }

  .cb-13__tx::details-content {
    block-size: 0;
    overflow: clip;
    opacity: 0;
    transition: block-size .35s cubic-bezier(.16,1,.3,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .cb-13__tx[open]::details-content {
    block-size: auto;
    opacity: 1;
  }
}
/* light */

.cb-13[data-theme="light"] {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --ink: #0e1016;
  --muted: #5d6675;
  --line: #e3e6ee;
  --in: #ffffff;
  --in-ink: #0e1016;
  --acc: #0f9d58;
  --acc-ink: #ffffff;
  --dim: #c9cedb;
  --shadow: rgba(14,16,22,.2);
}

.cb-13[data-theme="light"] .cb-13__moon {
  display: block;
}

.cb-13[data-theme="light"] .cb-13__sun {
  display: none;
}

@media (prefers-color-scheme: light) {
  .cb-13:not([data-theme="dark"]) {
    --bg: #f2f3f7;
    --surface: #ffffff;
    --ink: #0e1016;
    --muted: #5d6675;
    --line: #e3e6ee;
    --in: #ffffff;
    --in-ink: #0e1016;
    --acc: #0f9d58;
    --acc-ink: #ffffff;
    --dim: #c9cedb;
    --shadow: rgba(14,16,22,.2);
  }

  .cb-13:not([data-theme="dark"]) .cb-13__moon {
    display: block;
  }

  .cb-13:not([data-theme="dark"]) .cb-13__sun {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-13 *,
    .cb-13 *::before,
    .cb-13 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-13__bubble {
    border: 1px solid CanvasText;
  }

  .cb-13__bar {
    background: CanvasText;
    forced-color-adjust: none;
  }

  .cb-13__fill .cb-13__bar {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-13');
  if (!root) return;
  const play = root.querySelector('#cb-13-play');
  const wave = root.querySelector('#cb-13-wave');
  const seek = root.querySelector('#cb-13-seek');
  const fill = root.querySelector('#cb-13-fill');
  const timeEl = root.querySelector('#cb-13-time');
  const speedBtn = root.querySelector('#cb-13-speed');
  const status = root.querySelector('#cb-13-status');
  const DUR = 42, SPEEDS = [1, 1.5, 2];

  /* peaks: in production, compute these once from the decoded audio and cache them */
  const PEAKS = [.18,.32,.5,.66,.44,.28,.52,.74,.86,.62,.4,.55,.7,.92,.78,.5,.36,.6,.82,.68,
                 .44,.3,.48,.72,.9,.76,.54,.38,.5,.66,.84,.7,.46,.32,.44,.62,.8,.58,.4,.28,.36,.5,.34,.2];
  const barsHTML = PEAKS.map((h) => '<i class="cb-13__bar" style="--h:' + h + '"></i>').join('');
  root.querySelector('#cb-13-bars').innerHTML = barsHTML;
  root.querySelector('#cb-13-bars-2').innerHTML = barsHTML;

  /* the clipped layer must be as wide as the wave, not as wide as the clip */
  const syncWidth = () => wave.style.setProperty('--wave-w', wave.clientWidth + 'px');
  syncWidth();
  new ResizeObserver(syncWidth).observe(wave);

  const mmss = (s) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  let t = 0, rate = 1, playing = false, raf = null, last = 0;

  const paint = () => {
    wave.style.setProperty('--p', (t / DUR) * 100 + '%');
    seek.value = t.toFixed(1);
    timeEl.textContent = mmss(playing || t > 0 ? t : DUR);
    timeEl.dateTime = 'PT' + Math.round(t) + 'S';
  };

  const stop = (done) => {
    playing = false; cancelAnimationFrame(raf); raf = null;
    delete root.dataset.playing;
    play.setAttribute('aria-label', 'Play voice message, 42 seconds');
    if (done) { root.dataset.played = ''; status.textContent = 'Voice message finished'; }
  };

  const frame = (now) => {
    if (!playing) return;
    const dt = (now - last) / 1000; last = now;
    t = Math.min(DUR, t + dt * rate);
    paint();
    if (t >= DUR) { stop(true); return; }
    raf = requestAnimationFrame(frame);
  };

  const start = () => {
    if (t >= DUR) t = 0;
    playing = true; root.dataset.playing = '';
    play.setAttribute('aria-label', 'Pause voice message');
    status.textContent = 'Playing voice message';
    last = performance.now();
    raf = requestAnimationFrame(frame);
  };

  play.addEventListener('click', () => (playing ? stop(false) : start()));
  seek.addEventListener('input', () => { t = Number(seek.value); paint(); });
  speedBtn.addEventListener('click', () => {
    rate = SPEEDS[(SPEEDS.indexOf(rate) + 1) % SPEEDS.length];
    speedBtn.textContent = rate + '×';
    speedBtn.setAttribute('aria-label', 'Playback speed: ' + rate + ' times');
    status.textContent = 'Speed ' + rate + '×';
  });
  paint();
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-13');
  const btn = root && root.querySelector('.cb-13__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: light)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
