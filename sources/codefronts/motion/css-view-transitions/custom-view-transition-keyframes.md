---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/custom-view-transition-keyframes/"
title: "Custom View Transition Keyframes"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The default transition is a cross-fade."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom View Transition Keyframes
Source: https://codefronts.com/motion/css-view-transitions/custom-view-transition-keyframes/

The default transition is a cross-fade. This replaces it: your own @keyframes attached to ::view-transition-old() and ::view-transition-new() to get a slide-under, a scale-through or a directional wipe. Includes a diagram of the pseudo tree so you know which of the four layers to target for which kind of effect.
## HTML
```html
<section class="vtr-04" aria-labelledby="vtr-04-heading">
  <fieldset class="vtr-04__theme">
    <legend class="vtr-04__themelegend">Theme</legend>
    <input class="vtr-04__themeinput" type="radio" name="vtr-04-theme" id="vtr-04-theme-auto" checked>
    <label class="vtr-04__themeopt" for="vtr-04-theme-auto">Auto</label>
    <input class="vtr-04__themeinput" type="radio" name="vtr-04-theme" id="vtr-04-theme-light">
    <label class="vtr-04__themeopt" for="vtr-04-theme-light">Light</label>
    <input class="vtr-04__themeinput" type="radio" name="vtr-04-theme" id="vtr-04-theme-dark">
    <label class="vtr-04__themeopt" for="vtr-04-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-04__stage">
    <header class="vtr-04__head">
      <p class="vtr-04__kicker">Pseudo-element tree</p>
      <h2 class="vtr-04__heading" id="vtr-04-heading">Replacing the default cross-fade</h2>
      <p class="vtr-04__sub">Four layers, two of them worth animating. Pick an effect and the same DOM swap runs with different keyframes.</p>
    </header>

    <div class="vtr-04__grid">
      <figure class="vtr-04__tree">
        <figcaption class="vtr-04__treelabel">::view-transition</figcaption>
        <div class="vtr-04__node vtr-04__node--group">
          <span class="vtr-04__nodename">::view-transition-group(name)</span>
          <span class="vtr-04__nodejob">Position and size interpolation</span>
          <div class="vtr-04__node vtr-04__node--pair">
            <span class="vtr-04__nodename">::view-transition-image-pair(name)</span>
            <span class="vtr-04__nodejob">Clipping and blending</span>
            <div class="vtr-04__leaves">
              <div class="vtr-04__node vtr-04__node--leaf">
                <span class="vtr-04__nodename">-old(name)</span>
                <span class="vtr-04__nodejob">Outgoing snapshot</span>
              </div>
              <div class="vtr-04__node vtr-04__node--leaf">
                <span class="vtr-04__nodename">-new(name)</span>
                <span class="vtr-04__nodejob">Incoming snapshot</span>
              </div>
            </div>
          </div>
        </div>
      </figure>

      <div class="vtr-04__demo">
        <div class="vtr-04__controls" role="group" aria-label="Transition effect">
          <button class="vtr-04__ctl" type="button" data-vtr04-fx="slide" aria-pressed="true">Slide under</button>
          <button class="vtr-04__ctl" type="button" data-vtr04-fx="scale" aria-pressed="false">Scale through</button>
          <button class="vtr-04__ctl" type="button" data-vtr04-fx="wipe" aria-pressed="false">Directional wipe</button>
        </div>
        <div class="vtr-04__frame" id="vtr-04-frame" data-fx="slide">
          <article class="vtr-04__essay" id="vtr-04-essay">
            <p class="vtr-04__meta">Quill Review · Essay</p>
            <h3 class="vtr-04__title">The case against the default fade</h3>
            <p class="vtr-04__body">A cross-fade tells the reader nothing about direction. Replace it and the same DOM change starts carrying meaning: forward, backward, deeper, out.</p>
          </article>
        </div>
        <p class="vtr-04__hint">Each button re-runs the same swap with a different pair of <code>@keyframes</code>.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-04 {
  --bg: #f6f4ee;
  --surface: #fffdf8;
  --line: #ddd7c9;
  --ink: #14120f;
  --muted: #5f5a50;
  --accent: #b91c1c;
  --accent-soft: #fbe9e7;
  --dur: 520ms;
  --font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-04 *,
.vtr-04 *::before,
.vtr-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-04 {
    --bg: oklch(96% 0.011 95);
    --surface: oklch(99% 0.008 95);
    --line: oklch(87.5% 0.018 92);
    --ink: oklch(17% 0.008 80);
    --muted: oklch(48% 0.012 80);
    --accent: oklch(50% 0.19 26);
    --accent-soft: oklch(94% 0.03 30);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-04 {
    --bg: #131211;
    --surface: #1c1a17;
    --line: #302c26;
    --ink: #f4f1e8;
    --muted: #a49d90;
    --accent: #f87171;
    --accent-soft: #33201f;
  }
}

.vtr-04[data-theme="light"] {
  --bg: #f6f4ee;
  --surface: #fffdf8;
  --line: #ddd7c9;
  --ink: #14120f;
  --muted: #5f5a50;
  --accent: #b91c1c;
  --accent-soft: #fbe9e7;
}

.vtr-04[data-theme="dark"] {
  --bg: #131211;
  --surface: #1c1a17;
  --line: #302c26;
  --ink: #f4f1e8;
  --muted: #a49d90;
  --accent: #f87171;
  --accent-soft: #33201f;
}

.vtr-04__stage {
  max-width: 64rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 2rem;
}

.vtr-04__kicker {
  margin: 0 0 0.5rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-04__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.6rem, 5vw, 2.4rem);
  font-weight: 400;
  letter-spacing: -0.015em;
}

.vtr-04__sub {
  margin: 0.5rem 0 0;
  color: var(--muted);
  font-size: 0.95rem;
  max-width: 38rem;
  line-height: 1.6;
}

.vtr-04__grid {
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr;
}

@media (min-width: 58rem) {
  .vtr-04__grid {
    grid-template-columns: 20rem 1fr;
    align-items: start;
  }
}

.vtr-04__tree {
  margin: 0;
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.vtr-04__treelabel {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  color: var(--muted);
  padding-bottom: 0.35rem;
  border-bottom: 1px solid var(--line);
}

.vtr-04__node {
  display: grid;
  gap: 0.1rem;
  padding: 0.55rem 0.65rem;
}

.vtr-04__node--group {
  border-left: 2px solid var(--accent);
}

.vtr-04__node--pair {
  border-left: 1px solid var(--line);
  margin-top: 0.4rem;
}

.vtr-04__leaves {
  display: grid;
  gap: 0.4rem;
  grid-template-columns: 1fr 1fr;
  margin-top: 0.4rem;
}

.vtr-04__node--leaf {
  border: 1px solid var(--line);
  background: var(--surface);
  border-radius: 0.25rem;
  min-inline-size: 0;
}

.vtr-04__nodename {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  word-break: break-word;
}

.vtr-04__nodejob {
  font-size: 0.68rem;
  color: var(--muted);
}

.vtr-04__demo {
  display: grid;
  gap: 0.75rem;
  min-inline-size: 0;
}

.vtr-04__controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.vtr-04__ctl {
  min-height: 44px;
  padding: 0 0.95rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--surface);
  color: var(--muted);
  font-size: 0.8rem;
  cursor: pointer;
}

.vtr-04__ctl[aria-pressed="true"] {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-soft);
}

.vtr-04__ctl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-04__frame {
  border-top: 1px solid var(--ink);
  border-bottom: 1px solid var(--ink);
  padding: 1.5rem 0;
  min-inline-size: 0;
}

.vtr-04__essay {
  view-transition-name: vtr-04-essay;
  display: grid;
  gap: 0.6rem;
}

.vtr-04__meta {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-04__title {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 4vw, 1.75rem);
  font-weight: 400;
  line-height: 1.2;
  text-wrap: balance;
}

.vtr-04__body {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 32rem;
}

.vtr-04__hint {
  margin: 0;
  font-size: 0.75rem;
  color: var(--muted);
}

.vtr-04__hint code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
}

@keyframes vtr-04-out-left {
  to {
    transform: translateX(-24%);
    opacity: 0;
  }
}

@keyframes vtr-04-in-right {
  from {
    transform: translateX(24%);
    opacity: 0;
  }
}

@keyframes vtr-04-out-shrink {
  to {
    transform: scale(0.92);
    opacity: 0;
  }
}

@keyframes vtr-04-in-grow {
  from {
    transform: scale(1.06);
    opacity: 0;
  }
}

@keyframes vtr-04-out-wipe {
  to {
    clip-path: inset(0 0 0 100%);
  }
}

@keyframes vtr-04-in-wipe {
  from {
    clip-path: inset(0 100% 0 0);
  }
}

::view-transition-image-pair(vtr-04-essay) {
  isolation: auto;
}

::view-transition-old(vtr-04-essay),
::view-transition-new(vtr-04-essay) {
  mix-blend-mode: normal;
  animation-duration: 520ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

.vtr-04__frame[data-fx="slide"] .vtr-04__essay {
  view-transition-name: vtr-04-essay;
}

html:has(.vtr-04__frame[data-fx="slide"]) ::view-transition-old(vtr-04-essay) {
  animation-name: vtr-04-out-left;
}

html:has(.vtr-04__frame[data-fx="slide"]) ::view-transition-new(vtr-04-essay) {
  animation-name: vtr-04-in-right;
}

html:has(.vtr-04__frame[data-fx="scale"]) ::view-transition-old(vtr-04-essay) {
  animation-name: vtr-04-out-shrink;
}

html:has(.vtr-04__frame[data-fx="scale"]) ::view-transition-new(vtr-04-essay) {
  animation-name: vtr-04-in-grow;
}

html:has(.vtr-04__frame[data-fx="wipe"]) ::view-transition-old(vtr-04-essay) {
  animation-name: vtr-04-out-wipe;
}

html:has(.vtr-04__frame[data-fx="wipe"]) ::view-transition-new(vtr-04-essay) {
  animation-name: vtr-04-in-wipe;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(vtr-04-essay),
    ::view-transition-new(vtr-04-essay) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-04 {
  position: relative;
}

.vtr-04__theme {
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

.vtr-04__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-04__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-04__themeopt {
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

.vtr-04__themeopt:hover {
  opacity: 0.85;
}

.vtr-04__themeinput:checked + .vtr-04__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-04__themeinput:focus-visible + .vtr-04__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-04:has(#vtr-04-theme-light:checked) {
  --bg: #f6f4ee;
  --surface: #fffdf8;
  --line: #ddd7c9;
  --ink: #14120f;
  --muted: #5f5a50;
  --accent: #b91c1c;
  --accent-soft: #fbe9e7;
}

.vtr-04:has(#vtr-04-theme-dark:checked) {
  --bg: #131211;
  --surface: #1c1a17;
  --line: #302c26;
  --ink: #f4f1e8;
  --muted: #a49d90;
  --accent: #f87171;
  --accent-soft: #33201f;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-04');
  if (!root || root.dataset.vtr04) return;
  root.dataset.vtr04 = 'on';
  const frame = root.querySelector('#vtr-04-frame');
  const essay = root.querySelector('#vtr-04-essay');
  const ctls = [...root.querySelectorAll('[data-vtr04-fx]')];
  const copy = [
    ['Quill Review · Essay', 'The case against the default fade', 'A cross-fade tells the reader nothing about direction. Replace it and the same DOM change starts carrying meaning: forward, backward, deeper, out.'],
    ['Quill Review · Notebook', 'Which layer should this animation live on', 'Animate the group to change how the box travels. Animate the old and new images to change how the content enters and leaves. Mixing the two reads as drift.']
  ];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let i = 0, busy = false;
  const swap = () => {
    i = 1 - i;
    essay.querySelector('.vtr-04__meta').textContent = copy[i][0];
    essay.querySelector('.vtr-04__title').textContent = copy[i][1];
    essay.querySelector('.vtr-04__body').textContent = copy[i][2];
  };
  ctls.forEach(btn => btn.addEventListener('click', async () => {
    if (busy) return;
    ctls.forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    frame.dataset.fx = btn.dataset.vtr04Fx;
    if (!document.startViewTransition || reduce.matches) { swap(); return; }
    busy = true;
    try { await document.startViewTransition(swap).finished; } finally { busy = false; }
  }));
})();
```
