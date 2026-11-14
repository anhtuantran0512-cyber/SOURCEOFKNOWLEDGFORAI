---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/pause-and-resume-rotate-animation/"
title: "Pause and Resume Rotate Animation"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "animation-play-state: paused freezes a rotation at the exact angle it had reached and resumes from there — unlike removing the animation, which snaps the…"
has_js: "true"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pause and Resume Rotate Animation
Source: https://codefronts.com/motion/css-rotate-animation/pause-and-resume-rotate-animation/

animation-play-state: paused freezes a rotation at the exact angle it had reached and resumes from there — unlike removing the animation, which snaps the element back to zero. Three mechanisms are shown together: pause on hover, pause on keyboard focus, and an explicit button. WCAG 2.2.2 requires one of them for any motion running past five seconds.
## HTML
```html
<section class="rot-19" aria-labelledby="rot-19-h">
  <fieldset class="rot-19__theme">
    <legend class="rot-19__themelegend">Theme</legend>
    <input class="rot-19__themeinput" type="radio" name="rot-19-theme" id="rot-19-theme-auto" checked>
    <label class="rot-19__themeopt" for="rot-19-theme-auto">Auto</label>
    <input class="rot-19__themeinput" type="radio" name="rot-19-theme" id="rot-19-theme-light">
    <label class="rot-19__themeopt" for="rot-19-theme-light">Light</label>
    <input class="rot-19__themeinput" type="radio" name="rot-19-theme" id="rot-19-theme-dark">
    <label class="rot-19__themeopt" for="rot-19-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-19__stage" id="rot-19-root" data-state="running">
    <header class="rot-19__head">
      <p class="rot-19__eyebrow">Aperture Console · Motion control</p>
      <h2 class="rot-19__h" id="rot-19-h">Freezing at the angle, not resetting to zero</h2>
      <p class="rot-19__sub">Hover either rotor, tab into it, or use the button. One of them freezes where it is; the other jumps home.</p>
    </header>

    <div class="rot-19__pair">
      <article class="rot-19__panel">
        <p class="rot-19__tag">animation-play-state: paused</p>
        <div class="rot-19__well" tabindex="0" aria-label="Rotor that pauses in place on hover or focus">
          <span class="rot-19__rotor rot-19__rotor--pause" aria-hidden="true"></span>
        </div>
        <p class="rot-19__panelp">The clock stops. The rotor holds its angle and continues from there when it resumes.</p>
      </article>
      <article class="rot-19__panel rot-19__panel--bad">
        <p class="rot-19__tag rot-19__tag--bad">animation: none</p>
        <div class="rot-19__well" tabindex="0" aria-label="Rotor that resets to zero on hover or focus">
          <span class="rot-19__rotor rot-19__rotor--drop" aria-hidden="true"></span>
        </div>
        <p class="rot-19__panelp">The animation is removed, so the rotor reverts to its underlying style — 0 degrees, instantly.</p>
      </article>
    </div>

    <div class="rot-19__controls">
      <button class="rot-19__btn" type="button" id="rot-19-toggle" aria-pressed="false">Pause both rotors</button>
      <output class="rot-19__readout" id="rot-19-readout" aria-live="polite">Running · 4.0s per turn</output>
    </div>

    <p class="rot-19__fine">WCAG 2.2.2: motion that starts automatically and runs longer than five seconds needs a mechanism to pause, stop or hide it. An infinite rotation always qualifies, and the button — not the hover — is what satisfies it.</p>
  </div>
</section>
```
## CSS
```css
.rot-19 {
  --page: #17181c;
  --surface: #1f2127;
  --ink: #eef0f5;
  --muted: #969cab;
  --rule: #2e323b;
  --accent: #5b8cff;
  --warn: #ffab5c;
  --dur: 4s;
  --font-display: "Lucida Sans", "Lucida Grande", "Lucida Sans Unicode", system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-19 {
    --accent: oklch(0.68 0.17 265);
    --warn: oklch(0.79 0.14 65);
  }
}

.rot-19 *,
.rot-19 *::before,
.rot-19 *::after {
  box-sizing: border-box;
}

.rot-19__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3.5vw, 2rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-19__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-19__eyebrow {
  margin: 0 0 0.55rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-19__h {
  margin: 0 0 0.55rem;
  font-size: clamp(1.25rem, 4.4vw, 2rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.18;
}

.rot-19__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-19__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 1rem;
  inline-size: min(100%, 44rem);
}

.rot-19__panel {
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
  justify-items: center;
  padding: 1rem;
  border: 3px solid var(--accent);
  background: var(--surface);
}

.rot-19__panel--bad {
  border-color: var(--warn);
}

.rot-19__tag {
  margin: 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  color: var(--accent);
}

.rot-19__tag--bad {
  color: var(--warn);
}

.rot-19__well {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: clamp(6rem, 22vw, 8.5rem);
  aspect-ratio: 1;
  border: 1px solid var(--rule);
}

.rot-19__well:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.rot-19__rotor {
  position: relative;
  inline-size: 62%;
  aspect-ratio: 1;
  background: var(--accent);
  animation: rot-19-turn var(--dur) linear infinite;
}

.rot-19__rotor::before {
  content: "";
  position: absolute;
  inset-block-start: -0.45rem;
  inset-inline-start: 50%;
  inline-size: 0.5rem;
  block-size: 0.5rem;
  translate: -50% 0;
  border-radius: 50%;
  background: var(--ink);
}

.rot-19__rotor--drop {
  background: var(--warn);
}

@keyframes rot-19-turn {
  to {
    transform: rotate(360deg);
  }
}

.rot-19__panelp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  text-align: center;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-19__controls {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  flex-wrap: wrap;
  justify-content: center;
}

.rot-19__btn {
  min-block-size: 2.75rem;
  padding: 0 1.25rem;
  border: 3px solid var(--accent);
  background: transparent;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
}

.rot-19__btn:hover {
  background: color-mix(in srgb, var(--accent) 22%, transparent);
}

.rot-19__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.rot-19__readout {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.8125rem;
  color: var(--muted);
}

.rot-19__fine {
  inline-size: min(100%, 40rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-19__well:hover .rot-19__rotor--pause,
.rot-19__well:focus-visible .rot-19__rotor--pause {
  animation-play-state: paused;
}

.rot-19__well:hover .rot-19__rotor--drop,
.rot-19__well:focus-visible .rot-19__rotor--drop {
  animation: none;
}

.rot-19__stage[data-state="paused"] .rot-19__rotor--pause {
  animation-play-state: paused;
}

.rot-19__stage[data-state="paused"] .rot-19__rotor--drop {
  animation: none;
}

@media (prefers-reduced-motion: reduce) {
  .rot-19__rotor {
    animation: none;
    transform: rotate(24deg);
  }
}

.rot-19__theme {
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

.rot-19__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-19__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-19__themeopt {
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

.rot-19__themeopt:hover {
  opacity: 0.85;
}

.rot-19__themeinput:checked + .rot-19__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-19__themeinput:focus-visible + .rot-19__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-19__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-19__themeinput:checked + .rot-19__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-19:not(:has(#rot-19-theme-dark:checked)) {
    --page: #f3f4f7;
    --surface: #ffffff;
    --ink: #14161b;
    --muted: #5c6472;
    --rule: #d8dbe2;
    --accent: #2f5fe0;
    --warn: #b3641a;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-19:has(#rot-19-theme-light:checked) {
    --page: #f3f4f7;
    --surface: #ffffff;
    --ink: #14161b;
    --muted: #5c6472;
    --rule: #d8dbe2;
    --accent: #2f5fe0;
    --warn: #b3641a;
  }
}

[data-theme="light"] .rot-19:not(:has(#rot-19-theme-dark:checked)) {
  --page: #f3f4f7;
  --surface: #ffffff;
  --ink: #14161b;
  --muted: #5c6472;
  --rule: #d8dbe2;
  --accent: #2f5fe0;
  --warn: #b3641a;
}

.rot-19:has(#rot-19-theme-light:checked) {
  --page: #f3f4f7;
  --surface: #ffffff;
  --ink: #14161b;
  --muted: #5c6472;
  --rule: #d8dbe2;
  --accent: #2f5fe0;
  --warn: #b3641a;
}

.rot-19:has(#rot-19-theme-dark:checked) {
  --page: #17181c;
  --surface: #1f2127;
  --ink: #eef0f5;
  --muted: #969cab;
  --rule: #2e323b;
  --accent: #5b8cff;
  --warn: #ffab5c;
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-19:not(:has(#rot-19-theme-light:checked)) {
  --page: #17181c;
  --surface: #1f2127;
  --ink: #eef0f5;
  --muted: #969cab;
  --rule: #2e323b;
  --accent: #5b8cff;
  --warn: #ffab5c;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.rot-19__stage');
  if (!root || root.dataset.rot19) return;
  root.dataset.rot19 = '1';
  const btn = root.querySelector('.rot-19__btn');
  const out = root.querySelector('.rot-19__readout');
  const rotor = root.querySelector('.rot-19__rotor--pause');
  const frozenAngle = () => {
    const m = new DOMMatrixReadOnly(getComputedStyle(rotor).transform);
    return Math.round(((Math.atan2(m.b, m.a) * 180 / Math.PI) + 360) % 360);
  };
  btn.addEventListener('click', () => {
    const paused = root.dataset.state !== 'paused';
    root.dataset.state = paused ? 'paused' : 'running';
    btn.setAttribute('aria-pressed', String(paused));
    btn.textContent = paused ? 'Resume both rotors' : 'Pause both rotors';
    out.textContent = paused ? 'Paused · frozen at ' + frozenAngle() + '°' : 'Running · 4.0s per turn';
  });
})();
```
