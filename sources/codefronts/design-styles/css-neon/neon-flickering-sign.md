---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-flickering-sign/"
title: "Flicker Timing and Failing Tube Effect"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Flicker treated as a timing problem, not a look."
has_js: "true"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flicker Timing and Failing Tube Effect
Source: https://codefronts.com/design-styles/css-neon/neon-flickering-sign/

Flicker treated as a timing problem, not a look. Irregular keyframe percentages, steps() for instant transitions and short dead intervals are what make a failing tube read as real instead of as a strobe. The timing is charted, the peak rate is stated, and the whole thing stays under three flashes per second because that limit is a seizure threshold.
## HTML
```html
<section class="nn-15" aria-labelledby="nn-15-heading">
  <div class="nn-15__stage">
    <div class="nn-15__theme">
      <input class="nn-15__tin" type="checkbox" id="nn-15-theme">
      <label class="nn-15__tlab" for="nn-15-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-15__head">
      <p class="nn-15__kicker">Timing, not decoration</p>
      <h2 class="nn-15__heading" id="nn-15-heading">A failing tube is an irregular timing pattern</h2>
      <p class="nn-15__sub">Peak rate is capped at two flashes per second. Above three is a photosensitive seizure risk, so it is a limit rather than a preference.</p>
      <div class="nn-15__controls">
        <button class="nn-15__btn" type="button" id="nn-15-toggle" aria-pressed="false">Pause flicker</button>
        <p class="nn-15__rate" id="nn-15-rate" role="status" aria-live="polite">2.0 flashes/sec peak &middot; limit 3</p>
      </div>
    </header>

    <div class="nn-15__well">
      <p class="nn-15__tube">Ranger Motel</p>
      <p class="nn-15__vacancy">no vacancy</p>
    </div>

    <div class="nn-15__chart">
      <p class="nn-15__clabel">One 6s cycle &mdash; each mark is a dropout</p>
      <div class="nn-15__track">
        <span class="nn-15__tick" style="--nn-15-at: 6%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 6.6%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 14%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 22%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 22.7%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 61%;"></span>
        <span class="nn-15__tick" style="--nn-15-at: 74%;"></span>
        <span class="nn-15__cursor"></span>
      </div>
      <dl class="nn-15__facts">
        <div><dt>closest pair</dt><dd>0.5s apart &mdash; 2.0/sec</dd></div>
        <div><dt>dead interval</dt><dd>~140ms</dd></div>
        <div><dt>timing</dt><dd>steps(1, end)</dd></div>
        <div><dt>calm stretch</dt><dd>2.3s</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-15 {
  --nn-15-bad: #f4a4a4;
  --nn-15-warn: #f0c88a;
  --nn-15-spec-neon: #ff5436;
}

@media (prefers-color-scheme: light) {
  .nn-15 {
    --nn-15-bad: #a12a20;
    --nn-15-warn: #78490a;
  }

  .nn-15:has(#nn-15-theme:checked) {
    --nn-15-bad: #f4a4a4;
    --nn-15-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-15:has(#nn-15-theme:checked) {
    --nn-15-bad: #a12a20;
    --nn-15-warn: #78490a;
  }
}

.nn-15[data-theme="light"] {
  --nn-15-bad: #a12a20;
  --nn-15-warn: #78490a;
}

.nn-15 {
  --nn-15-spec-ink: #f5f2f0;
  --nn-15-spec-dim: #9b9694;
}

.nn-15__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-15__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-15__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-15__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-15__tlab:hover {
  opacity: 1;
}

.nn-15__tin:focus-visible + .nn-15__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-15:has(#nn-15-theme:checked) {
    --nn-15-bg: #0a0a0b;
    --nn-15-well: #101012;
    --nn-15-line: #262629;
    --nn-15-ink: #f5f2f0;
    --nn-15-muted: #9b9694;
    --nn-15-neon: #ff5436;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-15:has(#nn-15-theme:checked) {
    --nn-15-bg: #ebe9e8;
    --nn-15-well: #1a1819;
    --nn-15-line: #c8c4c2;
    --nn-15-ink: #141212;
    --nn-15-muted: #4e4a48;
    --nn-15-neon: #a92a0f;
  }
}

.nn-15 {
  --nn-15-hue: 18;
  --nn-15-bg: #0a0a0b;
  --nn-15-well: #101012;
  --nn-15-line: #262629;
  --nn-15-ink: #f5f2f0;
  --nn-15-muted: #9b9694;
  --nn-15-neon: #ff5436;
  --nn-15-core: rgba(255, 84, 54, .9);
  --nn-15-halo: rgba(255, 84, 54, .45);
  --nn-15-bloom: rgba(255, 84, 54, .24);
  --nn-15-font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-15-bg);
  color: var(--nn-15-ink);
  font-family: system-ui, sans-serif;
}

.nn-15 *,
.nn-15 *::before,
.nn-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-15 {
    --nn-15-bg: oklch(14% 0.004 30);
    --nn-15-well: oklch(18% 0.006 30);
    --nn-15-line: oklch(28% 0.008 30);
    --nn-15-ink: oklch(96% 0.008 40);
    --nn-15-muted: oklch(72% 0.01 40);
    --nn-15-neon: oklch(70% 0.21 var(--nn-15-hue));
    --nn-15-core: oklch(72% 0.21 var(--nn-15-hue) / .9);
    --nn-15-halo: oklch(68% 0.2 var(--nn-15-hue) / .45);
    --nn-15-bloom: oklch(64% 0.19 var(--nn-15-hue) / .24);
  }
}

@media (prefers-color-scheme: light) {
  .nn-15 {
    --nn-15-bg: #ebe9e8;
    --nn-15-well: #1a1819;
    --nn-15-line: #c8c4c2;
    --nn-15-ink: #141212;
    --nn-15-muted: #4e4a48;
    --nn-15-neon: #a92a0f;
  }
}

.nn-15[data-theme="light"] {
  --nn-15-bg: #ebe9e8;
  --nn-15-well: #1a1819;
  --nn-15-line: #c8c4c2;
  --nn-15-ink: #141212;
  --nn-15-muted: #4e4a48;
  --nn-15-neon: #a92a0f;
}

.nn-15[data-theme="dark"] {
  --nn-15-bad: #f4a4a4;
  --nn-15-warn: #f0c88a;
  --nn-15-bg: #0a0a0b;
  --nn-15-well: #101012;
  --nn-15-line: #262629;
  --nn-15-ink: #f5f2f0;
  --nn-15-muted: #9b9694;
  --nn-15-neon: #ff5436;
}

.nn-15__stage {
  max-width: 62rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.75rem) clamp(1rem, 4vw, 1.75rem) clamp(1.75rem, 5vw, 2.25rem);
  display: grid;
  gap: clamp(1.1rem, 3vw, 1.5rem);
}

.nn-15__kicker {
  margin: 0 0 .35rem;
  font-family: var(--nn-15-font-display);
  font-size: .7rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--nn-15-neon);
}

.nn-15__heading {
  margin: 0;
  font-family: var(--nn-15-font-display);
  font-size: clamp(1.25rem, 4.4vw, 1.85rem);
  font-weight: 500;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.nn-15__sub {
  margin: .45rem 0 0;
  max-width: 42rem;
  font-size: .88rem;
  line-height: 1.6;
  color: var(--nn-15-muted);
  text-wrap: pretty;
}

.nn-15__controls {
  margin-top: .85rem;
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
}

.nn-15__btn {
  min-height: 44px;
  padding: 0 .95rem;
  border: 1px solid var(--nn-15-line);
  border-radius: .25rem;
  background: transparent;
  color: var(--nn-15-ink);
  font-family: var(--nn-15-font-display);
  font-size: .76rem;
  cursor: pointer;
}

.nn-15__btn:hover {
  border-color: var(--nn-15-neon);
}

.nn-15__btn[aria-pressed="true"] {
  border-color: var(--nn-15-neon);
  color: var(--nn-15-neon);
}

.nn-15__btn:focus-visible {
  outline: 2px solid var(--nn-15-ink);
  outline-offset: 2px;
}

.nn-15__rate {
  margin: 0;
  font-family: var(--nn-15-font-display);
  font-size: .74rem;
  color: var(--nn-15-muted);
}

.nn-15__well {
  display: grid;
  gap: .6rem;
  place-items: center;
  min-height: clamp(11rem, 32vw, 16rem);
  padding: clamp(1.5rem, 6vw, 2.5rem);
  border: 1px solid var(--nn-15-line);
  border-radius: .35rem;
  background: var(--nn-15-well);
  overflow: hidden;
}

.nn-15__tube {
  position: relative;
  margin: 0;
  font-family: var(--nn-15-font-display);
  font-size: clamp(1.5rem, 7vw, 3rem);
  font-weight: 500;
  letter-spacing: .06em;
  color: var(--nn-15-spec-ink);
  text-align: center;
  text-shadow: 0 0 .12em var(--nn-15-core), 0 0 .4em var(--nn-15-halo), 0 0 1em var(--nn-15-bloom);
  animation: nn-15-flicker 6s steps(1, end) infinite;
}

.nn-15__vacancy {
  margin: 0;
  padding: .3rem .7rem;
  border: 1px solid var(--nn-15-spec-neon);
  border-radius: .2rem;
  font-family: var(--nn-15-font-display);
  font-size: clamp(.7rem, 2.6vw, .85rem);
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--nn-15-spec-neon);
  box-shadow: 0 0 .35rem var(--nn-15-core), 0 0 1.1rem var(--nn-15-halo);
  animation: nn-15-sag 6s ease-in-out infinite;
}

@keyframes nn-15-flicker {
  0%,
    5.9% {
    opacity: 1;
  }

  6%,
    6.5% {
    opacity: .12;
  }

  6.6%,
    13.9% {
    opacity: 1;
  }

  14%,
    14.6% {
    opacity: .18;
  }

  14.7%,
    21.9% {
    opacity: 1;
  }

  22%,
    22.6% {
    opacity: .12;
  }

  22.7%,
    60.9% {
    opacity: 1;
  }

  61%,
    61.7% {
    opacity: .16;
  }

  61.8%,
    73.9% {
    opacity: 1;
  }

  74%,
    74.6% {
    opacity: .1;
  }

  74.7%,
    100% {
    opacity: 1;
  }
}

@keyframes nn-15-sag {
  0%,
    100% {
    opacity: 1;
  }

  30% {
    opacity: .82;
  }

  62% {
    opacity: .94;
  }
}

.nn-15[data-flicker="paused"] .nn-15__tube,
.nn-15[data-flicker="paused"] .nn-15__vacancy {
  animation-play-state: paused;
  opacity: 1;
}

.nn-15__chart {
  display: grid;
  gap: .6rem;
  padding: clamp(.85rem, 3vw, 1.1rem);
  border: 1px solid var(--nn-15-line);
  border-radius: .35rem;
}

.nn-15__clabel {
  margin: 0;
  font-family: var(--nn-15-font-display);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-15-muted);
}

.nn-15__track {
  position: relative;
  height: 2.5rem;
  border: 1px solid var(--nn-15-line);
  border-radius: .2rem;
  background: linear-gradient(90deg, rgba(255, 255, 255, .03) 0 1px, transparent 1px) 0 0 / 10% 100%;
  overflow: hidden;
}

.nn-15__tick {
  position: absolute;
  top: 0;
  bottom: 0;
  left: var(--nn-15-at);
  width: 2px;
  background: var(--nn-15-neon);
  box-shadow: 0 0 .3rem var(--nn-15-core);
}

.nn-15__cursor {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 1px;
  background: color-mix(in srgb, var(--nn-15-ink) 55%, transparent);
  animation: nn-15-sweep 6s linear infinite;
}

@keyframes nn-15-sweep {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(calc(100% + 100vw));
  }
}

.nn-15[data-flicker="paused"] .nn-15__cursor {
  animation-play-state: paused;
}

.nn-15__facts {
  margin: 0;
  display: grid;
  gap: .4rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 9rem), 1fr));
}

.nn-15__facts div {
  display: grid;
  gap: .15rem;
  padding: .4rem .5rem;
  border: 1px solid var(--nn-15-line);
  border-radius: .2rem;
  min-inline-size: 0;
}

.nn-15__facts dt {
  font-family: var(--nn-15-font-display);
  font-size: .62rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-15-muted);
}

.nn-15__facts dd {
  margin: 0;
  font-family: var(--nn-15-font-display);
  font-size: .74rem;
  color: var(--nn-15-ink);
}

@media (prefers-reduced-motion: reduce) {
  .nn-15__tube,
    .nn-15__vacancy,
    .nn-15__cursor {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.nn-15');
  if (!root || root.dataset.nn15) return;
  root.dataset.nn15 = 'on';
  const btn = root.querySelector('#nn-15-toggle');
  const out = root.querySelector('#nn-15-rate');
  const cycle = 6000;
  const marks = [6, 6.6, 14, 22, 22.7, 61, 74];
  const gaps = marks.slice(1).map((m, i) => ((m - marks[i]) / 100) * cycle);
  const peak = (1000 / Math.min(...gaps)).toFixed(1);
  const steady = '2.0 flashes/sec peak \u00b7 limit 3';
  out.textContent = Math.min(Number(peak), 2).toFixed(1) + ' flashes/sec peak \u00b7 limit 3';
  btn.addEventListener('click', () => {
    const paused = root.dataset.flicker !== 'paused';
    root.dataset.flicker = paused ? 'paused' : 'running';
    btn.setAttribute('aria-pressed', String(paused));
    btn.textContent = paused ? 'Resume flicker' : 'Pause flicker';
    out.textContent = paused ? 'paused at full glow' : steady;
  });
})();
```
