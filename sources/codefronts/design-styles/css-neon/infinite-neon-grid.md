---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/infinite-neon-grid/"
title: "Infinite Neon Grid and Perspective Floor"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "A perspective floor treated as geometry plus falloff: a repeating grid on a rotated plane, translated by exactly one cell per loop so the motion is seamless,…"
has_js: "true"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Neon Grid and Perspective Floor
Source: https://codefronts.com/design-styles/css-neon/infinite-neon-grid/

A perspective floor treated as geometry plus falloff: a repeating grid on a rotated plane, translated by exactly one cell per loop so the motion is seamless, with glow fading toward the horizon via a mask rather than by dimming the lines. Speed and density are adjustable, and the whole thing animates one transform.
## HTML
```html
<section class="nn-19" aria-labelledby="nn-19-heading">
  <div class="nn-19__stage">
    <div class="nn-19__theme">
      <input class="nn-19__tin" type="checkbox" id="nn-19-theme">
      <label class="nn-19__tlab" for="nn-19-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-19__head">
      <p class="nn-19__kicker">Geometry and falloff</p>
      <h2 class="nn-19__heading" id="nn-19-heading">A floor that loops on exactly one cell</h2>
      <p class="nn-19__sub">One transform animation, one gradient, one mask. The seam disappears because the loop distance is the grid pitch.</p>
      <div class="nn-19__controls">
        <button class="nn-19__btn" type="button" data-nn19-speed="slow">Slow</button>
        <button class="nn-19__btn" type="button" data-nn19-speed="normal" aria-pressed="true">Normal</button>
        <button class="nn-19__btn" type="button" data-nn19-speed="fast">Fast</button>
        <button class="nn-19__btn nn-19__btn--alt" type="button" id="nn-19-density">Density: 3rem</button>
      </div>
    </header>

    <div class="nn-19__frame">
      <div class="nn-19__sky"></div>
      <span class="nn-19__horizon"></span>
      <div class="nn-19__floor"><div class="nn-19__plane"></div></div>
      <div class="nn-19__vignette"></div>
    </div>

    <dl class="nn-19__facts">
      <div><dt>loop</dt><dd>translate3d(0, one cell, 0)</dd></div>
      <div><dt>plane</dt><dd>rotateX(74deg), perspective 12rem</dd></div>
      <div><dt>falloff</dt><dd>mask-image fade toward the horizon</dd></div>
      <div><dt>animated</dt><dd>transform only</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.nn-19 {
  --nn-19-neons: #ff5ec4;
  --nn-19-bad: #f4a4a4;
  --nn-19-warn: #f0c88a;
  --nn-19-spec-neon: #ff5ec4;
}

@media (prefers-color-scheme: light) {
  .nn-19 {
    --nn-19-bad: #a12a20;
    --nn-19-warn: #78490a;
  }

  .nn-19:has(#nn-19-theme:checked) {
    --nn-19-bad: #f4a4a4;
    --nn-19-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-19:has(#nn-19-theme:checked) {
    --nn-19-bad: #a12a20;
    --nn-19-warn: #78490a;
  }
}

.nn-19[data-theme="light"] {
  --nn-19-bad: #a12a20;
  --nn-19-warn: #78490a;
}

.nn-19 {
  --nn-19-spec-ink: #f4eefb;
  --nn-19-spec-dim: #a294c4;
}

.nn-19__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-19__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-19__tlab {
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

.nn-19__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-19__tlab:hover {
  opacity: 1;
}

.nn-19__tin:focus-visible + .nn-19__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-19:has(#nn-19-theme:checked) {
    --nn-19-bg: #080617;
    --nn-19-line: #221a44;
    --nn-19-ink: #f4eefb;
    --nn-19-muted: #a294c4;
    --nn-19-neon: #ff5ec4;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-19:has(#nn-19-theme:checked) {
    --nn-19-bg: #eceaf4;
    --nn-19-line: #c9c2dc;
    --nn-19-ink: #120c22;
    --nn-19-muted: #4f4570;
    --nn-19-neon: #a3126f;
  }
}

.nn-19 {
  --nn-19-hue: 330;
  --nn-19-cell: 3rem;
  --nn-19-dur: 2.4s;
  --nn-19-bg: #080617;
  --nn-19-line: #221a44;
  --nn-19-ink: #f4eefb;
  --nn-19-muted: #a294c4;
  --nn-19-neon: #ff5ec4;
  --nn-19-core: rgba(255, 94, 196, .9);
  --nn-19-halo: rgba(255, 94, 196, .4);
  --nn-19-font-display: "Avenir Next Condensed", "Roboto Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-19-bg);
  color: var(--nn-19-ink);
  font-family: system-ui, sans-serif;
}

.nn-19 *,
.nn-19 *::before,
.nn-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-19 {
    --nn-19-bg: oklch(13% 0.04 290);
    --nn-19-line: oklch(28% 0.06 290);
    --nn-19-ink: oklch(96% 0.016 320);
    --nn-19-muted: oklch(73% 0.04 300);
    --nn-19-neon: oklch(76% 0.21 var(--nn-19-hue));
    --nn-19-core: oklch(78% 0.21 var(--nn-19-hue) / .9);
    --nn-19-halo: oklch(74% 0.2 var(--nn-19-hue) / .4);
  }
}

@media (prefers-color-scheme: light) {
  .nn-19 {
    --nn-19-bg: #eceaf4;
    --nn-19-line: #c9c2dc;
    --nn-19-ink: #120c22;
    --nn-19-muted: #4f4570;
    --nn-19-neon: #a3126f;
  }
}

.nn-19[data-theme="light"] {
  --nn-19-bg: #eceaf4;
  --nn-19-line: #c9c2dc;
  --nn-19-ink: #120c22;
  --nn-19-muted: #4f4570;
  --nn-19-neon: #a3126f;
}

.nn-19[data-theme="dark"] {
  --nn-19-bad: #f4a4a4;
  --nn-19-warn: #f0c88a;
  --nn-19-bg: #080617;
  --nn-19-line: #221a44;
  --nn-19-ink: #f4eefb;
  --nn-19-muted: #a294c4;
  --nn-19-neon: #ff5ec4;
}

.nn-19[data-speed="slow"] {
  --nn-19-dur: 4.5s;
}

.nn-19[data-speed="fast"] {
  --nn-19-dur: 1.2s;
}

.nn-19[data-density="tight"] {
  --nn-19-cell: 1.75rem;
}

.nn-19[data-density="wide"] {
  --nn-19-cell: 4.5rem;
}

.nn-19__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 2.5rem) clamp(1.25rem, 5vw, 2.25rem) clamp(2.25rem, 6vw, 3rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-19__kicker {
  margin: 0 0 .45rem;
  font-family: var(--nn-19-font-display);
  font-size: .82rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--nn-19-neon);
}

.nn-19__heading {
  margin: 0;
  font-family: var(--nn-19-font-display);
  font-size: clamp(1.5rem, 5.5vw, 2.4rem);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .02em;
  text-wrap: balance;
}

.nn-19__sub {
  margin: .55rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-19-muted);
  text-wrap: pretty;
}

.nn-19__controls {
  margin-top: .9rem;
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.nn-19__btn {
  min-height: 44px;
  padding: 0 .9rem;
  border: 1px solid var(--nn-19-line);
  border-radius: .2rem;
  background: transparent;
  color: var(--nn-19-muted);
  font-family: var(--nn-19-font-display);
  font-size: .8rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  cursor: pointer;
}

.nn-19__btn:hover {
  color: var(--nn-19-ink);
  border-color: var(--nn-19-neon);
}

.nn-19__btn[aria-pressed="true"] {
  color: var(--nn-19-ink);
  border-color: var(--nn-19-neon);
  box-shadow: 0 0 .35rem var(--nn-19-halo);
}

.nn-19__btn:focus-visible {
  outline: 2px solid var(--nn-19-ink);
  outline-offset: 2px;
}

.nn-19__frame {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-height: clamp(16rem, 48vw, 26rem);
  border: 1px solid var(--nn-19-line);
  background: linear-gradient(180deg, #0b0824 0%, #080617 48%, #050411 100%);
}

.nn-19__sky {
  position: absolute;
  inset: 0 0 52% 0;
  background: radial-gradient(70% 120% at 50% 100%, color-mix(in srgb, var(--nn-19-neons) 22%, transparent), transparent 70%);
}

.nn-19__horizon {
  position: absolute;
  left: 0;
  right: 0;
  top: 48%;
  height: 1px;
  background: var(--nn-19-neons);
  box-shadow: 0 0 .35rem var(--nn-19-core), 0 0 clamp(1.5rem, 7vw, 3rem) var(--nn-19-halo);
}

.nn-19__floor {
  position: absolute;
  inset: 48% 0 0 0;
  perspective: 12rem;
  perspective-origin: 50% 0%;
  overflow: hidden;
}

.nn-19__plane {
  position: absolute;
  left: -50%;
  right: -50%;
  top: 0;
  height: 300%;
  transform-origin: 50% 0%;
  transform: rotateX(74deg);
  background-image: repeating-linear-gradient(90deg, var(--nn-19-neons) 0 1px, transparent 1px var(--nn-19-cell)), repeating-linear-gradient(180deg, var(--nn-19-neons) 0 1px, transparent 1px var(--nn-19-cell));
  -webkit-mask-image: linear-gradient(180deg, transparent 0%, #000 22%, #000 100%);
  mask-image: linear-gradient(180deg, transparent 0%, #000 22%, #000 100%);
  animation: nn-19-scroll var(--nn-19-dur) linear infinite;
}

@keyframes nn-19-scroll {
  from {
    transform: rotateX(74deg) translate3d(0, 0, 0);
  }

  to {
    transform: rotateX(74deg) translate3d(0, var(--nn-19-cell), 0);
  }
}

.nn-19__vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(110% 80% at 50% 48%, transparent 45%, rgba(3, 2, 10, .8) 100%);
}

.nn-19__facts {
  margin: 0;
  display: grid;
  gap: .4rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
}

.nn-19__facts div {
  display: grid;
  gap: .15rem;
  padding: .5rem .6rem;
  border: 1px solid var(--nn-19-line);
  min-inline-size: 0;
}

.nn-19__facts dt {
  font-family: var(--nn-19-font-display);
  font-size: .68rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--nn-19-muted);
}

.nn-19__facts dd {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  color: var(--nn-19-ink);
}

@media (prefers-reduced-motion: reduce) {
  .nn-19__plane {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.nn-19');
  if (!root || root.dataset.nn19) return;
  root.dataset.nn19 = 'on';
  const dens = root.querySelector('#nn-19-density');
  const steps = [['normal', '3rem'], ['tight', '1.75rem'], ['wide', '4.5rem']];
  let d = 0;
  root.addEventListener('click', (e) => {
    const speed = e.target.closest('[data-nn19-speed]');
    if (speed) {
      root.dataset.speed = speed.dataset.nn19Speed;
      root.querySelectorAll('[data-nn19-speed]').forEach((b) => b.setAttribute('aria-pressed', String(b === speed)));
      return;
    }
    if (e.target.closest('#nn-19-density')) {
      d = (d + 1) % steps.length;
      root.dataset.density = steps[d][0];
      dens.textContent = 'Density: ' + steps[d][1];
    }
  });
})();
```
