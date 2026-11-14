---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/accessible-transitions-reduced-motion/"
title: "Accessible Transitions Reduced Motion"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Full-viewport transitions are a genuine vestibular trigger, and this API makes them very easy to overuse."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Transitions Reduced Motion
Source: https://codefronts.com/motion/css-view-transitions/accessible-transitions-reduced-motion/

Full-viewport transitions are a genuine vestibular trigger, and this API makes them very easy to overuse. Three tiers side by side: the full transition, a reduced variant that keeps a short cross-fade because motion-sensitive does not always mean motion-free, and complete suppression through skipTransition(). Covers both the CSS route and the JavaScript route.
## HTML
```html
<section class="vtr-16" aria-labelledby="vtr-16-heading">
  <fieldset class="vtr-16__theme">
    <legend class="vtr-16__themelegend">Theme</legend>
    <input class="vtr-16__themeinput" type="radio" name="vtr-16-theme" id="vtr-16-theme-auto" checked>
    <label class="vtr-16__themeopt" for="vtr-16-theme-auto">Auto</label>
    <input class="vtr-16__themeinput" type="radio" name="vtr-16-theme" id="vtr-16-theme-light">
    <label class="vtr-16__themeopt" for="vtr-16-theme-light">Light</label>
    <input class="vtr-16__themeinput" type="radio" name="vtr-16-theme" id="vtr-16-theme-dark">
    <label class="vtr-16__themeopt" for="vtr-16-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-16__stage">
    <header class="vtr-16__head">
      <p class="vtr-16__kicker">SC 2.3.3 · Animation from interactions</p>
      <h2 class="vtr-16__heading" id="vtr-16-heading">Three tiers, one end state</h2>
      <p class="vtr-16__sub">Pick a policy and run the same change. The interface must finish in the same place every time.</p>
    </header>

    <div class="vtr-16__tiers" role="group" aria-label="Motion policy">
      <button class="vtr-16__tier" type="button" data-vtr16-tier="full" aria-pressed="true">
        <span class="vtr-16__tname">Full</span>
        <span class="vtr-16__tnote">Named morph, 480ms. The default experience.</span>
      </button>
      <button class="vtr-16__tier" type="button" data-vtr16-tier="reduced" aria-pressed="false">
        <span class="vtr-16__tname">Reduced</span>
        <span class="vtr-16__tnote">120ms cross-fade only. No travel, still perceptible.</span>
      </button>
      <button class="vtr-16__tier" type="button" data-vtr16-tier="off" aria-pressed="false">
        <span class="vtr-16__tname">Suppressed</span>
        <span class="vtr-16__tnote">skipTransition() immediately. Instant finished state.</span>
      </button>
    </div>

    <div class="vtr-16__demo" id="vtr-16-demo" data-tier="full">
      <div class="vtr-16__card" id="vtr-16-card">
        <p class="vtr-16__ceyebrow" id="vtr-16-eyebrow">Now playing</p>
        <p class="vtr-16__ctitle" id="vtr-16-title">Aperture Sessions, vol. 4</p>
        <p class="vtr-16__cmeta" id="vtr-16-meta">Priya Sharma · 38 min</p>
      </div>
      <button class="vtr-16__run" type="button" id="vtr-16-run">Change the content</button>
    </div>

    <p class="vtr-16__foot">Your system preference is <strong id="vtr-16-pref">unknown</strong>. The wrapper reads it at call time, not on load.</p>
  </div>
</section>
```
## CSS
```css
.vtr-16 {
  --bg: #f3f0fb;
  --surface: #f8f6fe;
  --shadow-a: #ffffff;
  --shadow-b: #dcd6ef;
  --line: #e0d9f4;
  --ink: #201a33;
  --muted: #625a80;
  --accent: #7c5cff;
  --accent-soft: #ebe5ff;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Segoe UI", system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-16 *,
.vtr-16 *::before,
.vtr-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-16 {
    --bg: oklch(95% 0.022 295);
    --surface: oklch(97% 0.015 295);
    --shadow-b: oklch(88% 0.03 295);
    --line: oklch(90% 0.025 295);
    --ink: oklch(23% 0.04 295);
    --muted: oklch(50% 0.04 295);
    --accent: oklch(60% 0.19 292);
    --accent-soft: oklch(93% 0.04 292);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-16 {
    --bg: #14111f;
    --surface: #1a1628;
    --shadow-a: #221d33;
    --shadow-b: #0d0b16;
    --line: #2a2440;
    --ink: #ece8fa;
    --muted: #a29bc4;
    --accent: #a78bfa;
    --accent-soft: #241d3d;
  }
}

.vtr-16[data-theme="light"] {
  --bg: #f3f0fb;
  --surface: #f8f6fe;
  --shadow-a: #ffffff;
  --shadow-b: #dcd6ef;
  --line: #e0d9f4;
  --ink: #201a33;
  --muted: #625a80;
  --accent: #7c5cff;
  --accent-soft: #ebe5ff;
}

.vtr-16[data-theme="dark"] {
  --bg: #14111f;
  --surface: #1a1628;
  --shadow-a: #221d33;
  --shadow-b: #0d0b16;
  --line: #2a2440;
  --ink: #ece8fa;
  --muted: #a29bc4;
  --accent: #a78bfa;
  --accent-soft: #241d3d;
}

.vtr-16__stage {
  max-width: 56rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 4rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 2rem;
}

.vtr-16__kicker {
  margin: 0 0 0.55rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-16__heading {
  margin: 0;
  font-size: clamp(1.5rem, 4.6vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.025em;
}

.vtr-16__sub {
  margin: 0.55rem 0 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 38rem;
}

.vtr-16__tiers {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 50rem) {
  .vtr-16__tiers {
    grid-template-columns: repeat(3, 1fr);
  }
}

.vtr-16__tier {
  display: grid;
  gap: 0.35rem;
  text-align: left;
  min-height: 44px;
  padding: 1.15rem 1.25rem;
  border: 0;
  border-radius: 1.1rem;
  background: var(--surface);
  color: var(--ink);
  cursor: pointer;
  box-shadow: -6px -6px 14px var(--shadow-a), 7px 7px 18px var(--shadow-b);
  min-inline-size: 0;
}

.vtr-16__tier[aria-pressed="true"] {
  box-shadow: inset -4px -4px 10px var(--shadow-a), inset 5px 5px 12px var(--shadow-b);
  color: var(--accent);
}

.vtr-16__tier:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-16__tname {
  font-size: 1rem;
  font-weight: 650;
}

.vtr-16__tnote {
  font-size: 0.8rem;
  line-height: 1.5;
  color: var(--muted);
}

.vtr-16__demo {
  display: grid;
  gap: 1.25rem;
  justify-items: start;
  padding: clamp(1.25rem, 4vw, 2rem);
  border-radius: 1.25rem;
  background: var(--surface);
  box-shadow: inset -5px -5px 12px var(--shadow-a), inset 6px 6px 14px var(--shadow-b);
  min-inline-size: 0;
}

.vtr-16__card {
  width: 100%;
  max-width: 26rem;
  padding: 1.1rem 1.2rem;
  border-radius: 1rem;
  background: var(--bg);
  box-shadow: -5px -5px 12px var(--shadow-a), 6px 6px 14px var(--shadow-b);
  display: grid;
  gap: 0.3rem;
  view-transition-name: vtr-16-card;
}

.vtr-16__ceyebrow {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-16__ctitle {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 650;
  letter-spacing: -0.015em;
}

.vtr-16__cmeta {
  margin: 0;
  font-size: 0.8rem;
  color: var(--muted);
}

.vtr-16__run {
  min-height: 44px;
  padding: 0 1.3rem;
  border: 0;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  font-size: 0.88rem;
  font-weight: 650;
  cursor: pointer;
}

.vtr-16__run:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.vtr-16__foot {
  margin: 0;
  font-size: 0.82rem;
  color: var(--muted);
}

::view-transition-group(vtr-16-card) {
  animation-duration: 480ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

html:has(.vtr-16__demo[data-tier="reduced"]) ::view-transition-group(vtr-16-card) {
  animation-duration: 120ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) {
    animation-duration: 120ms;
  }

  ::view-transition-group(vtr-16-card) {
    animation-duration: 120ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-16 {
  position: relative;
}

.vtr-16__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.vtr-16__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-16__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-16__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.vtr-16__themeopt:hover {
  opacity: 0.85;
}

.vtr-16__themeinput:checked + .vtr-16__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-16__themeinput:focus-visible + .vtr-16__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-16:has(#vtr-16-theme-light:checked) {
  --bg: #f3f0fb;
  --surface: #f8f6fe;
  --shadow-a: #ffffff;
  --shadow-b: #dcd6ef;
  --line: #e0d9f4;
  --ink: #201a33;
  --muted: #625a80;
  --accent: #7c5cff;
  --accent-soft: #ebe5ff;
}

.vtr-16:has(#vtr-16-theme-dark:checked) {
  --bg: #14111f;
  --surface: #1a1628;
  --shadow-a: #221d33;
  --shadow-b: #0d0b16;
  --line: #2a2440;
  --ink: #ece8fa;
  --muted: #a29bc4;
  --accent: #a78bfa;
  --accent-soft: #241d3d;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-16');
  if (!root || root.dataset.vtr16) return;
  root.dataset.vtr16 = 'on';
  const demo = root.querySelector('#vtr-16-demo');
  const tiers = [...root.querySelectorAll('[data-vtr16-tier]')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const sets = [
    ['Now playing', 'Aperture Sessions, vol. 4', 'Priya Sharma · 38 min'],
    ['Up next', 'Field Recordings: Basalt Coast', 'Jordan Lee · 51 min']
  ];
  let i = 0, busy = false;
  const paint = () => {
    i = 1 - i;
    root.querySelector('#vtr-16-eyebrow').textContent = sets[i][0];
    root.querySelector('#vtr-16-title').textContent = sets[i][1];
    root.querySelector('#vtr-16-meta').textContent = sets[i][2];
  };
  root.querySelector('#vtr-16-pref').textContent = reduce.matches ? 'reduce' : 'no-preference';
  tiers.forEach(t => t.addEventListener('click', () => {
    tiers.forEach(x => x.setAttribute('aria-pressed', String(x === t)));
    demo.dataset.tier = t.dataset.vtr16Tier;
  }));
  root.querySelector('#vtr-16-run').addEventListener('click', async () => {
    if (busy) return;
    if (!document.startViewTransition || reduce.matches || demo.dataset.tier === 'off') { paint(); return; }
    busy = true;
    try { await document.startViewTransition(paint).finished; } finally { busy = false; }
  });
})();
```
