---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/multi-step-form-wizard/"
title: "Multi Step Form Wizard"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Step two slides in from the right on Next and from the left on Back, with the step indicator travelling as its own named element."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Step Form Wizard
Source: https://codefronts.com/motion/css-view-transitions/multi-step-form-wizard/

Step two slides in from the right on Next and from the left on Back, with the step indicator travelling as its own named element. The form itself is deliberately plain — two fields per step — because the subject is the step-change mechanism and the direction-aware branch, not the form design.
## HTML
```html
<section class="vtr-15" aria-labelledby="vtr-15-heading">
  <fieldset class="vtr-15__theme">
    <legend class="vtr-15__themelegend">Theme</legend>
    <input class="vtr-15__themeinput" type="radio" name="vtr-15-theme" id="vtr-15-theme-auto" checked>
    <label class="vtr-15__themeopt" for="vtr-15-theme-auto">Auto</label>
    <input class="vtr-15__themeinput" type="radio" name="vtr-15-theme" id="vtr-15-theme-light">
    <label class="vtr-15__themeopt" for="vtr-15-theme-light">Light</label>
    <input class="vtr-15__themeinput" type="radio" name="vtr-15-theme" id="vtr-15-theme-dark">
    <label class="vtr-15__themeopt" for="vtr-15-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-15__stage">
    <header class="vtr-15__head">
      <p class="vtr-15__kicker">Step mechanism</p>
      <h2 class="vtr-15__heading" id="vtr-15-heading">Direction as data</h2>
      <p class="vtr-15__sub">One call site. The type decides which way the step slides.</p>
    </header>

    <div class="vtr-15__wizard">
      <div class="vtr-15__rail" id="vtr-15-rail">
        <span class="vtr-15__dot" data-vtr15-dot="0"><span class="vtr-15__pill" id="vtr-15-pill">1</span></span>
        <span class="vtr-15__dot" data-vtr15-dot="1"></span>
        <span class="vtr-15__dot" data-vtr15-dot="2"></span>
      </div>

      <div class="vtr-15__step" id="vtr-15-step">
        <fieldset class="vtr-15__set">
          <legend class="vtr-15__legend" id="vtr-15-legend">Account</legend>
          <label class="vtr-15__field"><span id="vtr-15-l1">Work email</span><input class="vtr-15__input" type="email" id="vtr-15-f1" autocomplete="email"></label>
          <label class="vtr-15__field"><span id="vtr-15-l2">Team name</span><input class="vtr-15__input" type="text" id="vtr-15-f2"></label>
        </fieldset>
      </div>

      <div class="vtr-15__nav">
        <button class="vtr-15__btn" type="button" id="vtr-15-prev" disabled>Back</button>
        <button class="vtr-15__btn vtr-15__btn--go" type="button" id="vtr-15-next">Next</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-15 {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --line: #e2e6ec;
  --ink: #12161c;
  --muted: #5c6673;
  --accent: #15803d;
  --accent-soft: #e6f4ea;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-15 *,
.vtr-15 *::before,
.vtr-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-15 {
    --bg: oklch(97% 0.004 250);
    --line: oklch(91% 0.008 250);
    --ink: oklch(19% 0.012 250);
    --muted: oklch(50% 0.014 250);
    --accent: oklch(52% 0.13 150);
    --accent-soft: oklch(95% 0.03 150);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-15 {
    --bg: #0e1114;
    --surface: #16191e;
    --line: #262b33;
    --ink: #eef1f5;
    --muted: #98a2af;
    --accent: #4ade80;
    --accent-soft: #16281d;
  }
}

.vtr-15[data-theme="light"] {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --line: #e2e6ec;
  --ink: #12161c;
  --muted: #5c6673;
  --accent: #15803d;
  --accent-soft: #e6f4ea;
}

.vtr-15[data-theme="dark"] {
  --bg: #0e1114;
  --surface: #16191e;
  --line: #262b33;
  --ink: #eef1f5;
  --muted: #98a2af;
  --accent: #4ade80;
  --accent-soft: #16281d;
}

.vtr-15__stage {
  max-width: 34rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 4vw, 2rem);
  display: grid;
  gap: 1.25rem;
}

.vtr-15__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-15__heading {
  margin: 0;
  font-size: clamp(1.3rem, 4.2vw, 1.75rem);
  font-weight: 650;
  letter-spacing: -0.025em;
}

.vtr-15__sub {
  margin: 0.3rem 0 0;
  font-size: 0.86rem;
  color: var(--muted);
}

.vtr-15__wizard {
  border: 1px solid var(--line);
  border-radius: 0.65rem;
  background: var(--surface);
  overflow: hidden;
  min-inline-size: 0;
}

.vtr-15__rail {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 0.9rem;
  border-bottom: 1px solid var(--line);
}

.vtr-15__dot {
  position: relative;
  flex: 1;
  height: 0.35rem;
  border-radius: 999px;
  background: var(--line);
  display: grid;
  place-items: center;
  min-inline-size: 0;
}

.vtr-15__pill {
  position: absolute;
  display: grid;
  place-items: center;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 700;
  view-transition-name: vtr-15-pill;
}

.vtr-15__step {
  padding: 1.1rem 0.9rem 1.25rem;
  view-transition-name: vtr-15-step;
}

.vtr-15__set {
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
  gap: 0.8rem;
}

.vtr-15__legend {
  padding: 0;
  font-size: 0.95rem;
  font-weight: 650;
}

.vtr-15__field {
  display: grid;
  gap: 0.3rem;
  font-size: 0.78rem;
  color: var(--muted);
  min-inline-size: 0;
}

.vtr-15__input {
  min-height: 44px;
  padding: 0 0.7rem;
  border: 1px solid var(--line);
  border-radius: 0.4rem;
  background: var(--bg);
  color: var(--ink);
  font-family: inherit;
  font-size: 0.88rem;
  width: 100%;
}

.vtr-15__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.vtr-15__nav {
  display: flex;
  gap: 0.5rem;
  justify-content: space-between;
  padding: 0.7rem 0.9rem;
  border-top: 1px solid var(--line);
}

.vtr-15__btn {
  min-height: 44px;
  padding: 0 1.15rem;
  border: 1px solid var(--line);
  border-radius: 0.4rem;
  background: transparent;
  color: var(--ink);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}

.vtr-15__btn--go {
  border-color: var(--accent);
  background: var(--accent);
  color: #ffffff;
}

.vtr-15__btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.vtr-15__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@keyframes vtr-15-out-l {
  to {
    transform: translateX(-8%);
    opacity: 0;
  }
}

@keyframes vtr-15-in-r {
  from {
    transform: translateX(8%);
    opacity: 0;
  }
}

@keyframes vtr-15-out-r {
  to {
    transform: translateX(8%);
    opacity: 0;
  }
}

@keyframes vtr-15-in-l {
  from {
    transform: translateX(-8%);
    opacity: 0;
  }
}

:root:active-view-transition-type(vtr-15-next) ::view-transition-old(vtr-15-step) {
  animation: vtr-15-out-l 300ms ease both;
}

:root:active-view-transition-type(vtr-15-next) ::view-transition-new(vtr-15-step) {
  animation: vtr-15-in-r 300ms ease both;
}

:root:active-view-transition-type(vtr-15-prev) ::view-transition-old(vtr-15-step) {
  animation: vtr-15-out-r 300ms ease both;
}

:root:active-view-transition-type(vtr-15-prev) ::view-transition-new(vtr-15-step) {
  animation: vtr-15-in-l 300ms ease both;
}

::view-transition-group(vtr-15-pill) {
  animation-duration: 320ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-15-step),
    ::view-transition-group(vtr-15-pill) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-15 {
  position: relative;
}

.vtr-15__theme {
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

.vtr-15__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-15__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-15__themeopt {
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

.vtr-15__themeopt:hover {
  opacity: 0.85;
}

.vtr-15__themeinput:checked + .vtr-15__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-15__themeinput:focus-visible + .vtr-15__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-15:has(#vtr-15-theme-light:checked) {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --line: #e2e6ec;
  --ink: #12161c;
  --muted: #5c6673;
  --accent: #15803d;
  --accent-soft: #e6f4ea;
}

.vtr-15:has(#vtr-15-theme-dark:checked) {
  --bg: #0e1114;
  --surface: #16191e;
  --line: #262b33;
  --ink: #eef1f5;
  --muted: #98a2af;
  --accent: #4ade80;
  --accent-soft: #16281d;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-15');
  if (!root || root.dataset.vtr15) return;
  root.dataset.vtr15 = 'on';
  const pill = root.querySelector('#vtr-15-pill'), prev = root.querySelector('#vtr-15-prev'), next = root.querySelector('#vtr-15-next');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const slots = ['#vtr-15-legend', '#vtr-15-l1', '#vtr-15-l2'];
  const steps = [['Account', 'Work email', 'Team name'], ['Billing', 'Card number', 'Billing postcode'], ['Review', 'Purchase order (optional)', 'Notes for finance']];
  let i = 0, busy = false;
  const apply = (n) => {
    i = n;
    slots.forEach((sel, k) => { root.querySelector(sel).textContent = steps[n][k]; });
    root.querySelector('[data-vtr15-dot="' + n + '"]').append(pill);
    pill.textContent = String(n + 1);
    prev.disabled = n === 0; next.textContent = n === steps.length - 1 ? 'Finish' : 'Next';
  };
  const go = async (d) => {
    const n = i + d;
    if (n < 0 || n >= steps.length || busy) return;
    if (!document.startViewTransition || reduce.matches) apply(n);
    else {
      busy = true;
      try { await document.startViewTransition({ update: () => apply(n), types: ['vtr-15-' + (d > 0 ? 'next' : 'prev')] }).finished; } finally { busy = false; }
    }
    root.querySelector('#vtr-15-f1').focus();
  };
  next.addEventListener('click', () => go(1));
  prev.addEventListener('click', () => go(-1));
  root.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.matches('.vtr-15__input')) { e.preventDefault(); go(1); } });
})();
```
