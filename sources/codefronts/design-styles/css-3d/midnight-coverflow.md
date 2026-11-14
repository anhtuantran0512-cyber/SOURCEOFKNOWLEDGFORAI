---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/midnight-coverflow/"
title: "Ring Layout with Rotate and TranslateZ"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Items distributed evenly around a circle with one chained transform per item: rotateY(i &times; 360/n) then translateZ(radius)."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ring Layout with Rotate and TranslateZ
Source: https://codefronts.com/design-styles/css-3d/midnight-coverflow/

Items distributed evenly around a circle with one chained transform per item: rotateY(i &times; 360/n) then translateZ(radius). The radius is derived from item count and item width, so the panels never overlap and the ring resizes with the scene. Geometry, not a carousel &mdash; there is no active slide and nothing advances.
## HTML
```html
<section class="d3-12" aria-labelledby="d3-12-title">
  <h2 class="d3-12__sr" id="d3-12-title">Ring layout of album covers</h2>

  <div class="d3-12__theme">
    <input class="d3-12__theme-input" type="checkbox" id="d3-12-theme">
    <label class="d3-12__theme-label" for="d3-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-12__stage">
    <div class="d3-12__viewport">
      <header class="d3-12__head">
        <div>
          <span class="d3-12__kicker">Nightshift Radio</span>
          <strong>Rotation 08 &mdash; harbour sessions</strong>
        </div>
        <span class="d3-12__meta">8 panels &middot; radius = w / 2 &divide; tan(22.5&deg;)</span>
      </header>

      <div class="d3-12__scene">
        <div class="d3-12__ring">
          <article class="d3-12__panel" style="--d3-12-i: 0">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1024/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">01</span>
            <span class="d3-12__text"><b>Midnight Ferry</b><em>Ivo Halden</em></span>
            <span class="d3-12__time">4:12</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 1">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1035/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">02</span>
            <span class="d3-12__text"><b>Salt Air</b><em>Nadia Reyes</em></span>
            <span class="d3-12__time">3:38</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 2">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1043/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">03</span>
            <span class="d3-12__text"><b>Low Tide</b><em>The Kestrels</em></span>
            <span class="d3-12__time">5:04</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 3">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1050/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">04</span>
            <span class="d3-12__text"><b>Copper Wire</b><em>Junia</em></span>
            <span class="d3-12__time">3:21</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 4">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1062/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">05</span>
            <span class="d3-12__text"><b>Northbound</b><em>Ash Verrier</em></span>
            <span class="d3-12__time">4:47</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 5">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1074/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">06</span>
            <span class="d3-12__text"><b>Blue Hour</b><em>Marta Sol</em></span>
            <span class="d3-12__time">3:55</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 6">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1080/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">07</span>
            <span class="d3-12__text"><b>Static Bloom</b><em>Okra</em></span>
            <span class="d3-12__time">4:29</span>
          </article>
          <article class="d3-12__panel" style="--d3-12-i: 7">
            <img class="d3-12__art" src="https://picsum.photos/seed/d312-1084/400/400" alt="" loading="lazy" decoding="async" width="400" height="400">
            <span class="d3-12__scrim" aria-hidden="true"></span>
            <span class="d3-12__no">08</span>
            <span class="d3-12__text"><b>Harbour Lights</b><em>Pell</em></span>
            <span class="d3-12__time">5:16</span>
          </article>
        </div>
      </div>

      <footer class="d3-12__bar">
        <span class="d3-12__play" aria-hidden="true"></span>
        <span class="d3-12__now"><b>Midnight Ferry</b><em>Ivo Halden &middot; now playing</em></span>
        <span class="d3-12__wave" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-12 {
  --d3-12-bg: #f5f1e8;
  --d3-12-surf: #ffffff;
  --d3-12-line: #ded6c6;
  --d3-12-ink: #14171a;
  --d3-12-mut: #6a6a63;
  --d3-12-acc: #0f8f86;
  --d3-12-acc: oklch(56% 0.11 184);
  --d3-12-acc2: #e2604a;
  --d3-12-acc2: oklch(65% 0.16 32);
  --d3-12-count: 8;
  --d3-12-w: clamp(7rem, 20vw, 10rem);
  --d3-12-radius: calc(var(--d3-12-w) * 1.2071);
  --d3-12-spin: 34s;
  --d3-12-font-display: "Helvetica Neue", "Inter", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(52rem 26rem at 86% -10%, color-mix(in oklab, var(--d3-12-acc) 22%, transparent), transparent 62%), radial-gradient(40rem 22rem at -4% 104%, color-mix(in oklab, var(--d3-12-acc2) 18%, transparent), transparent 60%), var(--d3-12-bg);
  color: var(--d3-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-12 *,
.d3-12 *::before,
.d3-12 *::after {
  box-sizing: border-box;
}

.d3-12__sr {
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

.d3-12:has(.d3-12__theme-input:checked) {
  --d3-12-bg: #0e1113;
  --d3-12-surf: #171b1e;
  --d3-12-line: #2b3134;
  --d3-12-ink: #f2f0ea;
  --d3-12-mut: #9ba19f;
  --d3-12-acc: #4fd8cb;
  --d3-12-acc: oklch(82% 0.11 184);
  --d3-12-acc2: #ff8f74;
  --d3-12-acc2: oklch(78% 0.14 32);
}

@media (prefers-color-scheme: dark) {
  .d3-12 {
    --d3-12-bg: #0e1113;
    --d3-12-surf: #171b1e;
    --d3-12-line: #2b3134;
    --d3-12-ink: #f2f0ea;
    --d3-12-mut: #9ba19f;
    --d3-12-acc: #4fd8cb;
    --d3-12-acc: oklch(82% 0.11 184);
    --d3-12-acc2: #ff8f74;
    --d3-12-acc2: oklch(78% 0.14 32);
  }

  .d3-12:has(.d3-12__theme-input:checked) {
    --d3-12-bg: #f5f1e8;
    --d3-12-surf: #ffffff;
    --d3-12-line: #ded6c6;
    --d3-12-ink: #14171a;
    --d3-12-mut: #6a6a63;
    --d3-12-acc: #0f8f86;
    --d3-12-acc: oklch(56% 0.11 184);
    --d3-12-acc2: #e2604a;
    --d3-12-acc2: oklch(65% 0.16 32);
  }
}

@media (prefers-color-scheme: light) {
  .d3-12:has(.d3-12__theme-input:checked) {
    --d3-12-bg: #0e1113;
    --d3-12-surf: #171b1e;
    --d3-12-line: #2b3134;
    --d3-12-ink: #f2f0ea;
    --d3-12-mut: #9ba19f;
    --d3-12-acc: #4fd8cb;
    --d3-12-acc: oklch(82% 0.11 184);
    --d3-12-acc2: #ff8f74;
    --d3-12-acc2: oklch(78% 0.14 32);
  }
}

.d3-12__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-12__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-12-line);
  border-radius: 999px;
  background: var(--d3-12-surf);
  color: var(--d3-12-ink);
  cursor: pointer;
}

.d3-12__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-12__theme-input:focus-visible + .d3-12__theme-label {
  outline: 2px solid var(--d3-12-acc);
  outline-offset: 3px;
}

.d3-12__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-12__viewport {
  inline-size: 100%;
  max-inline-size: 62rem;
  overflow: hidden;
  display: grid;
  gap: clamp(0.9rem, 3vw, 1.5rem);
}

.d3-12__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.75rem;
}

.d3-12__kicker {
  display: block;
  font: 700 0.64rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--d3-12-acc);
}

.d3-12__head strong {
  font: 700 clamp(1.2rem, 4.2vw, 2.05rem)/1.05 var(--d3-12-font-display);
  letter-spacing: -0.025em;
}

.d3-12__meta {
  font: 500 0.7rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-12-mut);
}

.d3-12__scene {
  perspective: clamp(900px, 110vw, 1600px);
  perspective-origin: 50% 44%;
  block-size: clamp(15rem, 42vw, 20rem);
  display: grid;
  place-items: center;
}

.d3-12__ring {
  position: relative;
  inline-size: var(--d3-12-w);
  block-size: calc(var(--d3-12-w) * 1.28);
  transform-style: preserve-3d;
  animation: d3-12-turn var(--d3-12-spin) linear infinite;
}

@keyframes d3-12-turn {
  from {
    transform: rotateX(-8deg) rotateY(0deg);
  }

  to {
    transform: rotateX(-8deg) rotateY(-360deg);
  }
}

.d3-12__panel {
  position: absolute;
  inset: 0;
  overflow: hidden;
  border-radius: 14px;
  background: var(--d3-12-surf);
  border: 1px solid color-mix(in oklab, var(--d3-12-ink) 12%, transparent);
  box-shadow: 0 24px 44px -26px rgba(0, 0, 0, 0.7);
  transform: rotateY(calc(var(--d3-12-i) * (360deg / var(--d3-12-count)))) translateZ(var(--d3-12-radius));
  backface-visibility: hidden;
  display: grid;
  align-content: end;
  gap: 0.1rem;
  padding: 0.7rem;
  color: #fff;
}

.d3-12__art {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.d3-12__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(6, 10, 12, 0.1) 20%, rgba(6, 10, 12, 0.88) 100%);
}

.d3-12__no {
  position: absolute;
  inset-block-start: 0.55rem;
  inset-inline-start: 0.6rem;
  padding: 0.15rem 0.4rem;
  border-radius: 999px;
  background: color-mix(in oklab, var(--d3-12-acc) 85%, transparent);
  font: 700 0.6rem/1.4 ui-monospace, Menlo, monospace;
  color: #04211f;
}

.d3-12__text {
  position: relative;
  display: grid;
  gap: 0.05rem;
}

.d3-12__text b {
  font: 700 clamp(0.78rem, 2.2vw, 0.92rem)/1.15 var(--d3-12-font-display);
  letter-spacing: -0.01em;
}

.d3-12__text em {
  font: 500 0.64rem/1.2 ui-monospace, Menlo, monospace;
  font-style: normal;
  color: rgba(255, 255, 255, 0.72);
}

.d3-12__time {
  position: absolute;
  inset-block-end: 0.7rem;
  inset-inline-end: 0.7rem;
  font: 600 0.62rem/1 ui-monospace, Menlo, monospace;
  color: var(--d3-12-acc);
}

.d3-12__bar {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.7rem 0.9rem;
  border: 1px solid var(--d3-12-line);
  border-radius: 999px;
  background: color-mix(in oklab, var(--d3-12-surf) 80%, transparent);
}

.d3-12__play {
  inline-size: 34px;
  block-size: 34px;
  flex: none;
  border-radius: 999px;
  background: var(--d3-12-acc2);
  position: relative;
}

.d3-12__play::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 54%;
  inline-size: 0;
  block-size: 0;
  margin: -6px 0 0 -4px;
  border-block: 6px solid transparent;
  border-inline-start: 10px solid #fff;
}

.d3-12__now {
  display: grid;
  gap: 0.05rem;
}

.d3-12__now b {
  font: 700 0.85rem/1.1 var(--d3-12-font-display);
}

.d3-12__now em {
  font: 500 0.66rem/1.2 ui-monospace, Menlo, monospace;
  font-style: normal;
  color: var(--d3-12-mut);
}

.d3-12__wave {
  margin-inline-start: auto;
  display: flex;
  align-items: flex-end;
  gap: 3px;
  block-size: 1.4rem;
}

.d3-12__wave i {
  inline-size: 3px;
  border-radius: 2px;
  background: var(--d3-12-acc);
  animation: d3-12-wave 1.1s ease-in-out infinite;
}

.d3-12__wave i:nth-child(1) {
  block-size: 40%;
  animation-delay: -0.9s;
}

.d3-12__wave i:nth-child(2) {
  block-size: 75%;
  animation-delay: -0.6s;
}

.d3-12__wave i:nth-child(3) {
  block-size: 100%;
  animation-delay: -0.3s;
}

.d3-12__wave i:nth-child(4) {
  block-size: 62%;
  animation-delay: -0.15s;
}

.d3-12__wave i:nth-child(5) {
  block-size: 34%;
}

@keyframes d3-12-wave {
  0%,
    100% {
    transform: scaleY(0.5);
  }

  50% {
    transform: scaleY(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-12__ring {
    animation: none;
    transform: rotateX(-8deg) rotateY(-18deg);
  }

  .d3-12__wave i {
    animation: none;
  }
}
```
