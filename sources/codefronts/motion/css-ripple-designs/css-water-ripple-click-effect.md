---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-water-ripple-click-effect/"
title: "Water Surface Click Ripple"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Three concentric rings leave the same point a beat apart, each one wider, slower and fainter than the last."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Water Surface Click Ripple
Source: https://codefronts.com/motion/css-ripple-designs/css-water-ripple-click-effect/

Three concentric rings leave the same point a beat apart, each one wider, slower and fainter than the last. That stagger is what separates a water ripple from a single expanding circle: the surface is still responding after the first ring has gone. Coordinates come from the container box, easing comes from the tuned displacement curve.
## HTML
```html
<section class="rpl-09" id="rpl-09-surface" aria-labelledby="rpl-09-title">
  <input class="rpl-09__theme-input" type="checkbox" id="rpl-09-theme">
  <label class="rpl-09__theme" for="rpl-09-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-09__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-09__depth" aria-hidden="true"></div>
  <div class="rpl-09__content">
    <p class="rpl-09__eyebrow">Session 04 &middot; Stillwater</p>
    <h1 class="rpl-09__h1" id="rpl-09-title">Breathe with the surface</h1>
    <p class="rpl-09__lede">Touch the water anywhere. Twelve minutes, no narration.</p>
    <div class="rpl-09__cta">
      <button class="rpl-09__play" type="button">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
        Begin session
      </button>
      <span class="rpl-09__len">12:00</span>
    </div>
  </div>
  <div class="rpl-09__foot" aria-hidden="true">
    <span>Ambient</span><span>Loop</span><span>Offline ready</span>
  </div>
</section>
```
## CSS
```css
.rpl-09 {
  --rpl-09-deep: #04262e;
  --rpl-09-deep: oklch(0.26 0.048 210);
  --rpl-09-shallow: #0b4a52;
  --rpl-09-shallow: oklch(0.40 0.062 200);
  --rpl-09-fg: #eefaf9;
  --rpl-09-fg: oklch(0.975 0.012 190);
  --rpl-09-muted: #9dc4c4;
  --rpl-09-muted: oklch(0.80 0.035 195);
  --rpl-09-ring: rgba(224, 255, 252, 0.55);
  --rpl-09-ring: oklch(0.98 0.02 190 / 0.55);
  --rpl-09-dur: 2600ms;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(22px, 5vw, 64px);
  background: radial-gradient(120% 90% at 50% 10%, oklch(0.46 0.065 195 / 0.9), transparent 70%), linear-gradient(180deg, var(--rpl-09-shallow), var(--rpl-09-deep));
  color: var(--rpl-09-fg);
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  overflow: hidden;
  isolation: isolate;
  cursor: crosshair;
  box-sizing: border-box;
  -webkit-tap-highlight-color: transparent;
}

.rpl-09 *,
.rpl-09 *::before,
.rpl-09 *::after {
  box-sizing: border-box;
}

.rpl-09__depth {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background: repeating-linear-gradient(102deg, oklch(1 0 0 / 0.035) 0 2px, transparent 2px 26px), repeating-linear-gradient(-8deg, oklch(0 0 0 / 0.05) 0 3px, transparent 3px 40px);
  mix-blend-mode: soft-light;
}

.rpl-09__content {
  position: relative;
  z-index: 3;
  max-inline-size: min(94%, 640px);
  margin-block: auto;
  pointer-events: none;
}

.rpl-09__eyebrow {
  margin: 0 0 14px;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--rpl-09-muted);
}

.rpl-09__h1 {
  margin: 0 0 14px;
  max-inline-size: 13ch;
  font-size: clamp(34px, 6.2vw, 68px);
  font-weight: 400;
  line-height: 1.02;
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.rpl-09__lede {
  margin: 0 0 26px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: clamp(14px, 1.8vw, 16px);
  line-height: 1.6;
  color: var(--rpl-09-muted);
  max-inline-size: 34ch;
}

.rpl-09__cta {
  display: flex;
  align-items: center;
  gap: 16px;
  pointer-events: auto;
}

.rpl-09__play {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-block-size: 52px;
  padding: 0 24px;
  border: 0;
  border-radius: 999px;
  background: var(--rpl-09-fg);
  color: var(--rpl-09-deep);
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.rpl-09__play svg {
  inline-size: 18px;
  block-size: 18px;
}

.rpl-09__play:focus-visible {
  outline: 2px solid var(--rpl-09-fg);
  outline-offset: 4px;
}

.rpl-09__len {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 13px;
  color: var(--rpl-09-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-09__foot {
  position: relative;
  z-index: 3;
  display: flex;
  gap: 22px;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 10.5px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--rpl-09-muted);
  pointer-events: none;
}

.rpl-09__ring {
  position: absolute;
  left: var(--rpl-09-x, 50%);
  top: var(--rpl-09-y, 50%);
  inline-size: 22px;
  aspect-ratio: 1;
  border: 1.5px solid var(--rpl-09-ring);
  border-radius: 50%;
  z-index: 1;
  pointer-events: none;
  mix-blend-mode: screen;
  animation: rpl-09-spread var(--rpl-09-dur) cubic-bezier(0.06, 0.72, 0.24, 1) forwards, rpl-09-fade var(--rpl-09-dur) cubic-bezier(0.3, 0.05, 0.6, 1) forwards;
  animation-delay: var(--rpl-09-delay, 0ms);
}

@keyframes rpl-09-spread {
  from {
    transform: translate(-50%, -50%) scale(0.2);
  }

  to {
    transform: translate(-50%, -50%) scale(var(--rpl-09-max, 16));
  }
}

@keyframes rpl-09-fade {
  from {
    opacity: 0.85;
  }

  to {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-09__ring {
    animation: none;
    opacity: 0;
  }

  .rpl-09 {
    cursor: default;
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-09:has(#rpl-09-theme:checked) {
  --rpl-09-deep: oklch(0.743 0.048 210);
  --rpl-09-shallow: oklch(0.613 0.062 200);
  --rpl-09-fg: oklch(0.140 0.012 190);
  --rpl-09-muted: oklch(0.241 0.035 195);
  --rpl-09-ring: oklch(0.140 0.02 190 / 0.55);
  background: radial-gradient(120% 90% at 50% 10%, oklch(0.557 0.065 195 / 0.9), transparent 70%), linear-gradient(180deg, var(--rpl-09-shallow), var(--rpl-09-deep));
  color: var(--rpl-09-fg);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__depth {
  background: repeating-linear-gradient(102deg, oklch(0.140 0 0 / 0.035) 0 2px, transparent 2px 26px), repeating-linear-gradient(-8deg, oklch(0.985 0 0 / 0.05) 0 3px, transparent 3px 40px);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__eyebrow {
  color: var(--rpl-09-muted);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__lede {
  color: var(--rpl-09-muted);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__play {
  background: var(--rpl-09-fg);
  color: var(--rpl-09-deep);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__play:focus-visible {
  outline: 2px solid var(--rpl-09-fg);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__len {
  color: var(--rpl-09-muted);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__foot {
  color: var(--rpl-09-muted);
}

.rpl-09:has(#rpl-09-theme:checked) .rpl-09__ring {
  border: 1.5px solid var(--rpl-09-ring);
  mix-blend-mode: multiply;
}

.rpl-09 {
  position: relative;
}

.rpl-09__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-09__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-09__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-09__theme:active {
  transform: scale(0.94);
}

.rpl-09__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-09__theme-input:checked + .rpl-09__theme svg {
  transform: rotate(180deg);
}

.rpl-09__theme-input:focus-visible + .rpl-09__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-09__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-09__theme,
    .rpl-09__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('#rpl-09-surface');
const timers = new Set();

const drop = (event) => {
  if (event.target.closest('.rpl-09__play')) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = root.getBoundingClientRect();
  const x = event.clientX - box.left;
  const y = event.clientY - box.top;
  const live = root.querySelectorAll('.rpl-09__ring');
  if (live.length >= 12) live[0].remove();
  for (let i = 0; i < 3; i++) {
    const ring = document.createElement('span');
    ring.className = 'rpl-09__ring';
    ring.setAttribute('aria-hidden', 'true');
    ring.style.setProperty('--rpl-09-x', x + 'px');
    ring.style.setProperty('--rpl-09-y', y + 'px');
    ring.style.setProperty('--rpl-09-max', String(16 - i * 4));
    ring.style.setProperty('--rpl-09-delay', i * 220 + 'ms');
    ring.addEventListener('animationend', () => ring.remove(), { once: true });
    const t = setTimeout(() => { timers.delete(t); ring.remove(); }, 3600);
    timers.add(t);
    root.append(ring);
  }
};

root.addEventListener('pointerdown', drop);
root.__rplCleanup = () => { root.removeEventListener('pointerdown', drop); timers.forEach(clearTimeout); timers.clear(); };
```
