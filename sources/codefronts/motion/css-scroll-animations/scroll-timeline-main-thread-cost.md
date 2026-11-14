---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/scroll-timeline-main-thread-cost/"
title: "Scroll Timeline Performance and Main Thread Cost"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "The practical argument for CSS scroll timelines over a scroll listener: the CSS path runs off the main thread, so it stays smooth while JavaScript is busy."
has_js: "true"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Timeline Performance and Main Thread Cost
Source: https://codefronts.com/motion/css-scroll-animations/scroll-timeline-main-thread-cost/

The practical argument for CSS scroll timelines over a scroll listener: the CSS path runs off the main thread, so it stays smooth while JavaScript is busy. Two indicators, one bound in CSS and one driven by a scroll event, with a button that blocks the main thread on purpose — so the difference is visible rather than asserted.
## HTML
```html
<section class="sa-06" aria-labelledby="sa-06-h">
  <fieldset class="sa-06__theme">
    <legend class="sa-06__themelegend">Theme</legend>
    <input class="sa-06__themeinput" type="radio" name="sa-06-theme" id="sa-06-theme-auto" checked>
    <label class="sa-06__themeopt" for="sa-06-theme-auto">Auto</label>
    <input class="sa-06__themeinput" type="radio" name="sa-06-theme" id="sa-06-theme-light">
    <label class="sa-06__themeopt" for="sa-06-theme-light">Light</label>
    <input class="sa-06__themeinput" type="radio" name="sa-06-theme" id="sa-06-theme-dark">
    <label class="sa-06__themeopt" for="sa-06-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-06__stage">
    <header class="sa-06__head">
      <p class="sa-06__eyebrow">compositor vs main thread</p>
      <h2 class="sa-06__h" id="sa-06-h">Same scroll, two indicators, one busy thread</h2>
      <p class="sa-06__sub">Start scrolling the panel, then press Block main thread while you scroll. One indicator keeps up. The other cannot.</p>
      <div class="sa-06__controls">
        <button class="sa-06__btn" type="button" id="sa-06-block">Block main thread · 600ms</button>
        <p class="sa-06__state" id="sa-06-state" role="status">Idle</p>
      </div>
    </header>

    <div class="sa-06__gauges">
      <div class="sa-06__gauge">
        <p class="sa-06__gtag sa-06__gtag--css">Bound to scroll() — compositor</p>
        <div class="sa-06__track"><span class="sa-06__fill sa-06__fill--css"></span></div>
      </div>
      <div class="sa-06__gauge">
        <p class="sa-06__gtag sa-06__gtag--js">scroll listener — main thread</p>
        <div class="sa-06__track"><span class="sa-06__fill sa-06__fill--js" id="sa-06-jsfill"></span></div>
      </div>
    </div>

    <div class="sa-06__scroller" id="sa-06-scroller" tabindex="0" role="region" aria-label="Load test content, scrollable">
      <ul class="sa-06__rows">
        <li class="sa-06__row">Meridian · 4.2.0 · deploy queued</li>
        <li class="sa-06__row">Basalt · migration check passed</li>
        <li class="sa-06__row">Fern · 41 branches archived</li>
        <li class="sa-06__row">Nova · retention cohort recomputed</li>
        <li class="sa-06__row">Orbit · on-call rotation updated</li>
        <li class="sa-06__row">Prism · changelog published</li>
        <li class="sa-06__row">Quill · error budget 68% remaining</li>
        <li class="sa-06__row">Ranger · webhook queue drained</li>
        <li class="sa-06__row">Sable · canary at 5%</li>
        <li class="sa-06__row">Talon · 412 peak queue depth</li>
        <li class="sa-06__row">Vale · invoice run approved</li>
        <li class="sa-06__row">Aperture · seat allocation synced</li>
        <li class="sa-06__row">Fern · search index rebuilt</li>
        <li class="sa-06__row">Orbit · access tokens expired</li>
        <li class="sa-06__row">Vale · region key rotated</li>
        <li class="sa-06__row">Basalt · status page updated</li>
        <li class="sa-06__row">Nova · runbook handed to on-call</li>
        <li class="sa-06__row">Prism · change ticket closed</li>
        <li class="sa-06__row">Quill · provisioning branch archived</li>
        <li class="sa-06__row">Sable · canary promoted to 100%</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-06 {
  --page: #f4f5f7;
  --surface: #ffffff;
  --ink: #16181d;
  --muted: #5c6270;
  --rule: #22252c;
  --accent: #2f6df6;
  --bad: #d33b2f;
  --page: oklch(96.5% 0.003 260);
  --surface: oklch(100% 0 0);
  --ink: oklch(20% 0.008 265);
  --muted: oklch(48% 0.015 265);
  --rule: oklch(26% 0.01 265);
  --accent: oklch(55% 0.2 262);
  --bad: oklch(52% 0.2 28);
  --font-display: ui-monospace, "IBM Plex Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4rem 1.25rem 3.5rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-06 *,
.sa-06 *::before,
.sa-06 *::after {
  box-sizing: border-box;
}

.sa-06__stage {
  max-inline-size: 58rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-06__head {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-06__eyebrow {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-06__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.8vw, 1.875rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.14;
}

.sa-06__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-06__controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem;
}

.sa-06__btn {
  min-block-size: 2.75rem;
  min-inline-size: 11rem;
  padding: 0 1rem;
  border: 2px solid var(--rule);
  border-radius: 0;
  background: var(--ink);
  color: var(--surface);
  box-shadow: 0.25rem 0.25rem 0 var(--accent);
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  cursor: pointer;
}

.sa-06__btn:hover {
  box-shadow: 0.125rem 0.125rem 0 var(--accent);
}

.sa-06__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-06__state {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.75rem;
  color: var(--muted);
}

.sa-06__gauges {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.75rem;
}

.sa-06__gauge {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  padding: 0.75rem;
  border: 2px solid var(--rule);
  background: var(--surface);
  min-inline-size: 0;
}

.sa-06__gtag {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.sa-06__gtag--css {
  color: var(--accent);
}

.sa-06__gtag--js {
  color: var(--bad);
}

.sa-06__track {
  block-size: 0.75rem;
  background: color-mix(in srgb, var(--ink) 10%, transparent);
  overflow: hidden;
}

.sa-06__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-06__fill--css {
  background: var(--accent);
}

.sa-06__fill--js {
  background: var(--bad);
  transform: scaleX(0);
}

.sa-06__scroller {
  block-size: 48vh;
  min-block-size: 16rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 2px solid var(--rule);
  background: var(--surface);
  scroll-timeline: --sa-06-track block;
}

.sa-06__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-06__rows {
  margin: 0;
  min-block-size: calc(100% + 6rem);
  padding: 0.75rem;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-06__row {
  padding: 0.875rem;
  border-inline-start: 3px solid color-mix(in srgb, var(--ink) 15%, transparent);
  background: color-mix(in srgb, var(--ink) 4%, transparent);
  font-size: 0.8125rem;
  min-inline-size: 0;
}

@keyframes sa-06-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-06__fill--css {
    animation: sa-06-fill linear both;
    animation-timeline: --sa-06-track;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-06__fill--css {
    animation: none;
    transform: scaleX(1);
  }
}

.sa-06__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0;
  margin: 0;
  padding: 0;
  border: 2px solid var(--rule);
  background: var(--surface);
}

.sa-06__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-06__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-06__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-06__themeinput:checked + .sa-06__themeopt {
  color: var(--surface);
  background: var(--ink);
}

.sa-06__themeinput:focus-visible + .sa-06__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 40rem) {
  .sa-06__gauges {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-06 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-06__fill--css {
    background: Highlight;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-06:not(:has(#sa-06-theme-light:checked)) {
    --page: #0d0f12;
    --surface: #15181d;
    --ink: #e9ecf2;
    --muted: #98a1b2;
    --rule: #2b313a;
    --accent: #6f9bff;
    --bad: #ff7a6a;
  }

  .sa-06:not(:has(#sa-06-theme-light:checked)) .sa-06__btn {
    background: var(--surface);
    color: var(--ink);
  }

  .sa-06:not(:has(#sa-06-theme-light:checked)) .sa-06__themeinput:checked + .sa-06__themeopt {
    color: #0d0f12;
    background: var(--ink);
  }
}

@media (prefers-color-scheme: light) {
  .sa-06:has(#sa-06-theme-dark:checked) {
    --page: #0d0f12;
    --surface: #15181d;
    --ink: #e9ecf2;
    --muted: #98a1b2;
    --rule: #2b313a;
    --accent: #6f9bff;
    --bad: #ff7a6a;
  }

  .sa-06:has(#sa-06-theme-dark:checked) .sa-06__btn {
    background: var(--surface);
    color: var(--ink);
  }

  .sa-06:has(#sa-06-theme-dark:checked) .sa-06__themeinput:checked + .sa-06__themeopt {
    color: #0d0f12;
    background: var(--ink);
  }
}

[data-theme="dark"] .sa-06:not(:has(#sa-06-theme-light:checked)) {
  --page: #0d0f12;
  --surface: #15181d;
  --ink: #e9ecf2;
  --muted: #98a1b2;
  --rule: #2b313a;
  --accent: #6f9bff;
  --bad: #ff7a6a;
}

.sa-06:has(#sa-06-theme-dark:checked) {
  --page: #0d0f12;
  --surface: #15181d;
  --ink: #e9ecf2;
  --muted: #98a1b2;
  --rule: #2b313a;
  --accent: #6f9bff;
  --bad: #ff7a6a;
}

.sa-06:has(#sa-06-theme-dark:checked) .sa-06__btn {
  background: var(--surface);
  color: var(--ink);
}

.sa-06:has(#sa-06-theme-dark:checked) .sa-06__themeinput:checked + .sa-06__themeopt {
  color: #0d0f12;
  background: var(--ink);
}

.sa-06:has(#sa-06-theme-light:checked) {
  --page: #f4f5f7;
  --surface: #ffffff;
  --ink: #16181d;
  --muted: #5c6270;
  --rule: #22252c;
  --accent: #2f6df6;
  --bad: #d33b2f;
}
```

## JavaScript
```js
const root = document.querySelector('.sa-06');
const scroller = document.getElementById('sa-06-scroller');
const jsFill = document.getElementById('sa-06-jsfill');
const state = document.getElementById('sa-06-state');
const btn = document.getElementById('sa-06-block');
const onScroll = () => {
  const max = scroller.scrollHeight - scroller.clientHeight;
  jsFill.style.transform = 'scaleX(' + (max > 0 ? scroller.scrollTop / max : 0).toFixed(3) + ')';
};
scroller.addEventListener('scroll', onScroll, { passive: true });
onScroll();
const block = () => {
  state.textContent = 'Main thread blocked — keep scrolling';
  const end = performance.now() + 600;
  while (performance.now() < end) { /* deliberate synchronous work */ }
  state.textContent = 'Released — the listener bar had to catch up';
};
btn.addEventListener('click', block);
btn.addEventListener('keydown', (e) => { if (e.key === 'Enter') block(); });
root.saCleanup = () => scroller.removeEventListener('scroll', onScroll);
```
