---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-arcade-game-ui-kit/"
title: "Retro Arcade Game Interface"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "An arcade attract screen: illuminated marquee, high-score table with initials, and the insert-coin prompt cycling on the cabinet's own cadence."
has_js: "true"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Arcade Game Interface
Source: https://codefronts.com/design-styles/css-retro-designs/retro-arcade-game-ui-kit/

An arcade attract screen: illuminated marquee, high-score table with initials, and the insert-coin prompt cycling on the cabinet's own cadence. The blink is the interesting part &mdash; it is exactly the pattern the pause-and-stop success criterion exists for, so it runs on a period-correct rhythm, stays under three flashes a second, and stops dead under reduced motion.
## HTML
```html
<section class="rt-15" aria-labelledby="rt-15-title" data-rt15-attract="scores">
  <h2 class="rt-15__sr" id="rt-15-title">Arcade cabinet attract screen</h2>

  <div class="rt-15__theme">
    <input class="rt-15__theme-input" type="checkbox" id="rt-15-theme">
    <label class="rt-15__theme-label" for="rt-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-15__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-15__stage">
    <div class="rt-15__cab">
      <div class="rt-15__marquee">
        <span class="rt-15__marquee-t">VECTOR PATROL</span>
        <span class="rt-15__marquee-s">1 or 2 players</span>
      </div>

      <div class="rt-15__screen">
        <div class="rt-15__hud">
          <span>1UP <b>0032100</b></span>
          <span>HI <b>0198750</b></span>
          <span>2UP <b>0000000</b></span>
        </div>

        <div class="rt-15__panels">
          <section class="rt-15__panel" data-rt-15-panel="scores" aria-labelledby="rt-15-p1">
            <h3 class="rt-15__panel-h" id="rt-15-p1">HIGH SCORES</h3>
            <ol class="rt-15__scores">
              <li><span class="rt-15__rk">1ST</span><span class="rt-15__in">AJC</span><span class="rt-15__sc">0198750</span></li>
              <li><span class="rt-15__rk">2ND</span><span class="rt-15__in">PSA</span><span class="rt-15__sc">0176420</span></li>
              <li><span class="rt-15__rk">3RD</span><span class="rt-15__in">JLE</span><span class="rt-15__sc">0154900</span></li>
              <li><span class="rt-15__rk">4TH</span><span class="rt-15__in">SRV</span><span class="rt-15__sc">0132080</span></li>
              <li><span class="rt-15__rk">5TH</span><span class="rt-15__in">ZZZ</span><span class="rt-15__sc">0100000</span></li>
            </ol>
          </section>

          <section class="rt-15__panel" data-rt-15-panel="title" aria-labelledby="rt-15-p2">
            <h3 class="rt-15__panel-h" id="rt-15-p2">VECTOR PATROL</h3>
            <p class="rt-15__tag">DEFEND SECTOR SEVEN</p>
            <ul class="rt-15__legend">
              <li><span class="rt-15__pip rt-15__pip--a" aria-hidden="true"></span>SCOUT &mdash; 100 PTS</li>
              <li><span class="rt-15__pip rt-15__pip--b" aria-hidden="true"></span>RUNNER &mdash; 250 PTS</li>
              <li><span class="rt-15__pip rt-15__pip--c" aria-hidden="true"></span>CARRIER &mdash; 1000 PTS</li>
            </ul>
          </section>

          <section class="rt-15__panel" data-rt-15-panel="credits" aria-labelledby="rt-15-p3">
            <h3 class="rt-15__panel-h" id="rt-15-p3">CREDITS 00</h3>
            <p class="rt-15__coin">INSERT COIN</p>
            <p class="rt-15__small">1 COIN 1 PLAY &nbsp;&middot;&nbsp; 2 COINS 3 PLAYS</p>
          </section>
        </div>

        <p class="rt-15__footer">&copy; 1983 NORTHGATE ELECTRONICS &middot; ALL RIGHTS RESERVED</p>
      </div>

      <div class="rt-15__controls">
        <span class="rt-15__stick" aria-hidden="true"></span>
        <div class="rt-15__buttons">
          <button class="rt-15__ab" type="button">FIRE</button>
          <button class="rt-15__ab rt-15__ab--b" type="button">THRUST</button>
          <button class="rt-15__ab rt-15__ab--c" type="button">1P START</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-15 {
  --rt-15-shell: #1d1f24;
  --rt-15-shell-2: #101216;
  --rt-15-edge: #34383f;
  --rt-15-green: #4dff9a;
  --rt-15-amber: #ffc247;
  --rt-15-red: #ff5a4d;
  --rt-15-cyan: #52e5ff;
  --rt-15-mono: ui-monospace, SFMono-Regular, "Cascadia Mono", Consolas, "DejaVu Sans Mono", monospace;
  --rt-15-bg: #0c0d10;
  --rt-15-bg: oklch(15% 0.006 280);
  --rt-15-ink-2: #a2a7b0;
  --rt-15-ink-2: oklch(73% 0.01 280);
  --rt-15-acc: #52e5ff;
  --rt-15-acc: oklch(84% 0.11 218);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-15-bg);
  color: #eef1f5;
  font-family: var(--rt-15-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-15 *,
.rt-15 *::before,
.rt-15 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .rt-15 {
    --rt-15-bg: #cfd2d8;
    --rt-15-bg: oklch(85% 0.007 280);
    --rt-15-ink-2: #4b505a;
    --rt-15-ink-2: oklch(43% 0.012 280);
    --rt-15-acc: #0d5f7a;
    --rt-15-acc: oklch(45% 0.1 218);
  }
}

.rt-15[data-theme="dark"] {
  --rt-15-bg: #0c0d10;
  --rt-15-bg: oklch(15% 0.006 280);
  --rt-15-ink-2: #a2a7b0;
  --rt-15-acc: #52e5ff;
}

@media (prefers-color-scheme: light) {
  .rt-15:has(.rt-15__theme-input:checked) {
    --rt-15-bg: #0c0d10;
    --rt-15-bg: oklch(15% 0.006 280);
    --rt-15-ink-2: #a2a7b0;
    --rt-15-acc: #52e5ff;
  }
}

@media (prefers-color-scheme: dark) {
  .rt-15:has(.rt-15__theme-input:checked) {
    --rt-15-bg: #cfd2d8;
    --rt-15-bg: oklch(85% 0.007 280);
    --rt-15-ink-2: #4b505a;
    --rt-15-acc: #0d5f7a;
  }
}

.rt-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-15__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 8;
}

.rt-15__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  border-radius: 4px;
  background: var(--rt-15-shell);
  color: var(--rt-15-acc);
  border: 1px solid var(--rt-15-edge);
}

.rt-15__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-15__theme-input:focus-visible + .rt-15__theme-label {
  outline: 2px solid var(--rt-15-acc);
  outline-offset: 3px;
}

.rt-15__stage {
  max-inline-size: 54rem;
  margin-inline: auto;
  padding: clamp(3.75rem, 3rem + 3vw, 5rem) clamp(0.75rem, 0.5rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
}

.rt-15__cab {
  min-inline-size: 0;
  border-radius: 14px 14px 6px 6px;
  overflow: hidden;
  background: linear-gradient(180deg, var(--rt-15-shell) 0%, var(--rt-15-shell-2) 100%);
  border: 1px solid var(--rt-15-edge);
  box-shadow: 0 26px 52px -26px rgba(0,0,0,0.85);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
}

.rt-15__marquee {
  position: relative;
  min-inline-size: 0;
  padding: clamp(0.9rem, 0.6rem + 1.4vw, 1.4rem) 1rem;
  text-align: center;
  display: grid;
  gap: 0.3rem;
  background: radial-gradient(120% 180% at 50% 50%, rgba(255,255,255,0.28) 0%, rgba(255,255,255,0.05) 55%, rgba(0,0,0,0.4) 100%), linear-gradient(180deg, #2b1a5e 0%, #7a1f6a 60%, #b3324a 100%);
  border-block-end: 3px solid #05060a;
  box-shadow: 0 14px 30px -10px rgba(179, 50, 74, 0.55);
}

.rt-15__marquee-t {
  font-size: clamp(1.2rem, 0.7rem + 3.4vw, 2.4rem);
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #fff6d8;
  text-shadow: 0 0 12px rgba(255, 214, 120, 0.75), 0 2px 0 #47102f;
  min-inline-size: 0;
}

.rt-15__marquee-s {
  font-size: 0.68rem;
  letter-spacing: 0.3em;
  color: #f2d9e6;
  text-transform: uppercase;
}

.rt-15__screen {
  min-inline-size: 0;
  margin: clamp(0.6rem, 0.4rem + 1vw, 1.1rem);
  border-radius: 10px;
  background: #04060a;
  padding: clamp(0.85rem, 0.6rem + 1.4vw, 1.5rem);
  box-shadow: inset 0 0 0 2px #000, inset 0 0 34px 10px rgba(0,0,0,0.9);
  display: grid;
  gap: 0.9rem;
  align-content: start;
}

.rt-15__hud {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.5rem 1rem;
  font-size: clamp(0.6rem, 0.5rem + 0.55vw, 0.78rem);
  color: var(--rt-15-cyan);
  letter-spacing: 0.1em;
  min-inline-size: 0;
}

.rt-15__hud b {
  color: #ffffff;
  font-variant-numeric: tabular-nums;
}

.rt-15__panels {
  display: grid;
  min-block-size: clamp(210px, 30vw, 280px);
  min-inline-size: 0;
}

.rt-15__panel {
  grid-area: 1 / 1;
  min-inline-size: 0;
  display: none;
  align-content: center;
  justify-items: center;
  gap: 0.75rem;
  text-align: center;
}

.rt-15[data-rt15-attract="scores"] [data-rt-15-panel="scores"],
.rt-15[data-rt15-attract="title"] [data-rt-15-panel="title"],
.rt-15[data-rt15-attract="credits"] [data-rt-15-panel="credits"] {
  display: grid;
}

.rt-15__panel-h {
  margin: 0;
  font-size: clamp(0.85rem, 0.6rem + 1.4vw, 1.3rem);
  letter-spacing: 0.24em;
  color: var(--rt-15-amber);
  font-weight: 700;
  min-inline-size: 0;
}

.rt-15__scores {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.35rem;
  min-inline-size: 0;
  inline-size: min(100%, 26rem);
}

.rt-15__scores li {
  display: grid;
  grid-template-columns: 3.5rem minmax(0, 1fr) auto;
  gap: 0.75rem;
  align-items: baseline;
  font-size: clamp(0.7rem, 0.55rem + 0.8vw, 0.95rem);
  color: var(--rt-15-green);
}

.rt-15__rk {
  color: var(--rt-15-cyan);
  letter-spacing: 0.1em;
}

.rt-15__in {
  text-align: start;
  letter-spacing: 0.3em;
  color: #ffffff;
  min-inline-size: 0;
}

.rt-15__sc {
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.08em;
}

.rt-15__tag {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.22em;
  color: var(--rt-15-cyan);
}

.rt-15__legend {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
  font-size: 0.75rem;
  color: var(--rt-15-green);
}

.rt-15__legend li {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-inline-size: 0;
}

.rt-15__pip {
  inline-size: 14px;
  block-size: 14px;
  flex: none;
}

.rt-15__pip--a {
  background: var(--rt-15-cyan);
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}

.rt-15__pip--b {
  background: var(--rt-15-amber);
  clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
}

.rt-15__pip--c {
  background: var(--rt-15-red);
}

.rt-15__coin {
  margin: 0;
  font-size: clamp(1.1rem, 0.7rem + 2.6vw, 2rem);
  letter-spacing: 0.2em;
  font-weight: 800;
  color: var(--rt-15-red);
  min-inline-size: 0;
  animation: rt-15-blink 1.4s steps(1, end) infinite;
}

@keyframes rt-15-blink {
  0%,
    59% {
    opacity: 1;
  }

  60%,
    100% {
    opacity: 0.12;
  }
}

.rt-15__small {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  color: var(--rt-15-cyan);
}

.rt-15__footer {
  margin: 0;
  font-size: 0.6rem;
  letter-spacing: 0.12em;
  color: #6f7c86;
  text-align: center;
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-15__controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  padding: clamp(0.85rem, 0.6rem + 1.2vw, 1.4rem);
  background: linear-gradient(180deg, #22252b, #15171b);
  border-block-start: 1px solid var(--rt-15-edge);
  min-inline-size: 0;
}

.rt-15__stick {
  inline-size: 46px;
  block-size: 46px;
  flex: none;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 30%, #ff8a7a, #b32d1f 62%, #6d1a10 100%);
  box-shadow: 0 4px 0 #0c0d10, 0 8px 14px rgba(0,0,0,0.6);
}

.rt-15__buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  flex: 1 1 auto;
  min-inline-size: 0;
}

.rt-15__ab {
  min-block-size: 46px;
  min-inline-size: 46px;
  padding: 0.6rem 1.1rem;
  border: 0;
  cursor: pointer;
  border-radius: 999px;
  font: inherit;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #12060a;
  background: linear-gradient(180deg, #ffd36b, #e09a1f);
  box-shadow: 0 4px 0 #6d4a08, 0 7px 12px rgba(0,0,0,0.5);
}

.rt-15__ab--b {
  background: linear-gradient(180deg, #7ef0b6, #24b071);
  box-shadow: 0 4px 0 #0f5636, 0 7px 12px rgba(0,0,0,0.5);
}

.rt-15__ab--c {
  background: linear-gradient(180deg, #8fd2ff, #2f86d8);
  color: #061423;
  box-shadow: 0 4px 0 #14456f, 0 7px 12px rgba(0,0,0,0.5);
}

.rt-15__ab:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 rgba(0,0,0,0.6);
}

.rt-15__ab:focus-visible {
  outline: 2px solid #ffffff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .rt-15__coin {
    animation: none;
    opacity: 1;
  }

  .rt-15__ab {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.currentScript.closest('.rt-15') || document.querySelector('.rt-15');
const order = ['scores', 'title', 'credits'];
const calm = window.matchMedia('(prefers-reduced-motion: reduce)');
let i = 0;
let timer = null;
const step = () => {
  i = (i + 1) % order.length;
  root.dataset.rt15Attract = order[i];
};
const start = () => {
  if (timer !== null || calm.matches) return;
  timer = setInterval(step, 4200);
};
const stop = () => { clearInterval(timer); timer = null; };
const onPref = () => {
  if (calm.matches) { stop(); i = 0; root.dataset.rt15Attract = 'scores'; } else { start(); }
};
calm.addEventListener('change', onPref);
onPref();
root.__rtCleanup = () => { stop(); calm.removeEventListener('change', onPref); };
```
