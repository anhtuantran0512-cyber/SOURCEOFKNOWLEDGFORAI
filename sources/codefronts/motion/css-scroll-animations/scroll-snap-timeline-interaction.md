---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/scroll-snap-timeline-interaction/"
title: "Scroll Snap and Timeline Interaction"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Scroll snapping and scroll timelines work together, but snapping changes the shape of the progress signal: instead of sweeping, it lands."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Snap and Timeline Interaction
Source: https://codefronts.com/motion/css-scroll-animations/scroll-snap-timeline-interaction/

Scroll snapping and scroll timelines work together, but snapping changes the shape of the progress signal: instead of sweeping, it lands. An animation tuned for smooth scrolling reads as a stutter once snapped. Two identical scrollers — one snapping, one free — plus the adjustment that makes the snapped one read correctly.
## HTML
```html
<section class="sa-03" aria-labelledby="sa-03-h">
  <fieldset class="sa-03__theme">
    <legend class="sa-03__themelegend">Theme</legend>
    <input class="sa-03__themeinput" type="radio" name="sa-03-theme" id="sa-03-theme-auto" checked>
    <label class="sa-03__themeopt" for="sa-03-theme-auto">Auto</label>
    <input class="sa-03__themeinput" type="radio" name="sa-03-theme" id="sa-03-theme-light">
    <label class="sa-03__themeopt" for="sa-03-theme-light">Light</label>
    <input class="sa-03__themeinput" type="radio" name="sa-03-theme" id="sa-03-theme-dark">
    <label class="sa-03__themeopt" for="sa-03-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-03__stage">
    <header class="sa-03__head">
      <p class="sa-03__eyebrow">snap · timeline</p>
      <h2 class="sa-03__h" id="sa-03-h">Progress that lands instead of sweeping</h2>
      <p class="sa-03__sub">Same content, same timeline, same range. The left panel snaps and uses stepped keyframes to suit it. The right panel scrolls freely with a continuous sweep.</p>
    </header>

    <div class="sa-03__pair">
      <article class="sa-03__side sa-03__side--snap">
        <p class="sa-03__label">Snapped — <span class="sa-03__mono">scroll-snap-type: block mandatory</span>, stepped keyframes</p>
        <div class="sa-03__meter"><span class="sa-03__fill sa-03__fill--snap"></span></div>
        <div class="sa-03__scroller sa-03__scroller--snap" tabindex="0" role="region" aria-label="Snapping panel, scrollable">
          <div class="sa-03__item">Ranger · onboarding</div>
          <div class="sa-03__item">Ranger · billing</div>
          <div class="sa-03__item">Ranger · webhooks</div>
          <div class="sa-03__item">Ranger · audit log</div>
          <div class="sa-03__item">Ranger · handoff</div>
        </div>
      </article>

      <article class="sa-03__side sa-03__side--free">
        <p class="sa-03__label">Free — no snapping, continuous sweep</p>
        <div class="sa-03__meter"><span class="sa-03__fill sa-03__fill--free"></span></div>
        <div class="sa-03__scroller sa-03__scroller--free" tabindex="0" role="region" aria-label="Free scrolling panel, scrollable">
          <div class="sa-03__item">Ranger · onboarding</div>
          <div class="sa-03__item">Ranger · billing</div>
          <div class="sa-03__item">Ranger · webhooks</div>
          <div class="sa-03__item">Ranger · audit log</div>
          <div class="sa-03__item">Ranger · handoff</div>
        </div>
      </article>
    </div>

    <p class="sa-03__note">The adjustment is not a longer duration — duration is ignored here. It is keyframes shaped like the signal: plateaus where the scroller rests, change where it travels.</p>
  </div>
</section>
```
## CSS
```css
.sa-03 {
  --page: #fef6e4;
  --surface: #ffffff;
  --ink: #001858;
  --muted: #5a6a9a;
  --rule: #001858;
  --accent: #0fa3b1;
  --accent2: #f582ae;
  --page: oklch(96.5% 0.04 90);
  --surface: oklch(100% 0 0);
  --ink: oklch(28% 0.13 265);
  --muted: oklch(52% 0.07 265);
  --accent: oklch(66% 0.11 205);
  --accent2: oklch(78% 0.13 5);
  --font-display: ui-rounded, "SF Pro Rounded", "Segoe UI Variable Display", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4.5rem 1.5rem 4rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-03 *,
.sa-03 *::before,
.sa-03 *::after {
  box-sizing: border-box;
}

.sa-03__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

.sa-03__head {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-03__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-03__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.625rem, 4.6vw, 2.5rem);
  font-weight: 700;
  letter-spacing: -0.025em;
  line-height: 1.08;
}

.sa-03__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-03__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
}

.sa-03__pair {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
}

.sa-03__side {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1.25rem;
  border: 2px solid var(--ink);
  border-radius: 1rem;
  background: var(--surface);
  box-shadow: 0.5rem 0.5rem 0 var(--accent);
  min-inline-size: 0;
}

.sa-03__side--free {
  box-shadow: 0.5rem 0.5rem 0 var(--accent2);
}

.sa-03__label {
  margin: 0;
  font-size: 0.75rem;
  font-weight: 700;
  line-height: 1.45;
  text-wrap: pretty;
}

.sa-03__meter {
  block-size: 0.625rem;
  border: 2px solid var(--ink);
  border-radius: 999px;
  overflow: hidden;
}

.sa-03__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-03__fill--snap {
  background: var(--accent);
}

.sa-03__fill--free {
  background: var(--accent2);
}

.sa-03__scroller {
  block-size: 46vh;
  min-block-size: 15rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 0.75rem;
  background: color-mix(in srgb, var(--ink) 5%, transparent);
}

.sa-03__scroller--snap {
  scroll-snap-type: block mandatory;
  scroll-timeline: --sa-03-snap block;
}

.sa-03__scroller--free {
  scroll-timeline: --sa-03-free block;
}

.sa-03__scroller:focus-visible {
  outline: 3px solid var(--accent2);
  outline-offset: 2px;
}

.sa-03__item {
  display: flex;
  align-items: center;
  justify-content: center;
  min-block-size: 11rem;
  margin: 0.5rem;
  border-radius: 0.75rem;
  background: var(--surface);
  border: 2px solid var(--ink);
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  scroll-snap-align: start;
  scroll-snap-stop: always;
  min-inline-size: 0;
}

.sa-03__note {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-03-step {
  0% {
    transform: scaleX(0.05);
  }

  18% {
    transform: scaleX(0.05);
  }

  25% {
    transform: scaleX(0.3);
  }

  43% {
    transform: scaleX(0.3);
  }

  50% {
    transform: scaleX(0.55);
  }

  68% {
    transform: scaleX(0.55);
  }

  75% {
    transform: scaleX(0.8);
  }

  93% {
    transform: scaleX(0.8);
  }

  100% {
    transform: scaleX(1);
  }
}

@keyframes sa-03-sweep {
  from {
    transform: scaleX(0.05);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-03__fill--snap {
    animation: sa-03-step linear both;
    animation-timeline: --sa-03-snap;
  }

  .sa-03__fill--free {
    animation: sa-03-sweep linear both;
    animation-timeline: --sa-03-free;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-03__fill {
    animation: none;
    transform: scaleX(1);
  }

  .sa-03__scroller {
    scroll-behavior: auto;
  }
}

.sa-03__theme {
  position: absolute;
  inset-block-start: 1.25rem;
  inset-inline-end: 1.25rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 2px solid var(--ink);
  border-radius: 999px;
  background: var(--surface);
}

.sa-03__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-03__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-03__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-03__themeinput:checked + .sa-03__themeopt {
  color: var(--surface);
  background: var(--ink);
}

.sa-03__themeinput:focus-visible + .sa-03__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-03__pair {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-03 {
    padding: 4.5rem 1rem 3rem;
  }

  .sa-03__item {
    min-block-size: 8.5rem;
  }
}

@media (forced-colors: active) {
  .sa-03__fill {
    background: Highlight;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-03:not(:has(#sa-03-theme-light:checked)) {
    --page: #0b1020;
    --surface: #141b31;
    --ink: #e8ecff;
    --muted: #9aa6d4;
    --accent: #35c9d6;
    --accent2: #ff9dc2;
  }

  .sa-03:not(:has(#sa-03-theme-light:checked)) .sa-03__themeinput:checked + .sa-03__themeopt {
    color: #0b1020;
  }
}

@media (prefers-color-scheme: light) {
  .sa-03:has(#sa-03-theme-dark:checked) {
    --page: #0b1020;
    --surface: #141b31;
    --ink: #e8ecff;
    --muted: #9aa6d4;
    --accent: #35c9d6;
    --accent2: #ff9dc2;
  }

  .sa-03:has(#sa-03-theme-dark:checked) .sa-03__themeinput:checked + .sa-03__themeopt {
    color: #0b1020;
  }
}

[data-theme="dark"] .sa-03:not(:has(#sa-03-theme-light:checked)) {
  --page: #0b1020;
  --surface: #141b31;
  --ink: #e8ecff;
  --muted: #9aa6d4;
  --accent: #35c9d6;
  --accent2: #ff9dc2;
}

.sa-03:has(#sa-03-theme-dark:checked) {
  --page: #0b1020;
  --surface: #141b31;
  --ink: #e8ecff;
  --muted: #9aa6d4;
  --accent: #35c9d6;
  --accent2: #ff9dc2;
}

.sa-03:has(#sa-03-theme-dark:checked) .sa-03__themeinput:checked + .sa-03__themeopt {
  color: #0b1020;
}

.sa-03:has(#sa-03-theme-light:checked) {
  --page: #fef6e4;
  --surface: #ffffff;
  --ink: #001858;
  --muted: #5a6a9a;
  --accent: #0fa3b1;
  --accent2: #f582ae;
}
```
