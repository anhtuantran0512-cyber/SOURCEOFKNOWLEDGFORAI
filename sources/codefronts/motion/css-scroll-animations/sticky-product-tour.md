---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/sticky-product-tour/"
title: "Sticky Pinned Scene Scrubbing"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Pin a scene with position: sticky inside a much taller parent and bind an animation to that parent's scroll: the scene holds still on screen while its…"
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Pinned Scene Scrubbing
Source: https://codefronts.com/motion/css-scroll-animations/sticky-product-tour/

Pin a scene with position: sticky inside a much taller parent and bind an animation to that parent's scroll: the scene holds still on screen while its contents scrub. This is the mechanism behind step-through product tours, and it depends entirely on the sticky element having somewhere to travel.
## HTML
```html
<section class="sa-17" aria-labelledby="sa-17-h">
  <fieldset class="sa-17__theme">
    <legend class="sa-17__themelegend">Theme</legend>
    <input class="sa-17__themeinput" type="radio" name="sa-17-theme" id="sa-17-theme-auto" checked>
    <label class="sa-17__themeopt" for="sa-17-theme-auto">Auto</label>
    <input class="sa-17__themeinput" type="radio" name="sa-17-theme" id="sa-17-theme-light">
    <label class="sa-17__themeopt" for="sa-17-theme-light">Light</label>
    <input class="sa-17__themeinput" type="radio" name="sa-17-theme" id="sa-17-theme-dark">
    <label class="sa-17__themeopt" for="sa-17-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-17__stage">
    <header class="sa-17__head">
      <p class="sa-17__eyebrow">Pinned scene · scrub</p>
      <h2 class="sa-17__h" id="sa-17-h">The scene holds still, the content moves</h2>
      <p class="sa-17__sub">The scene is pinned with <span class="sa-17__mono">position: sticky</span>. Its parent is four times taller, and that extra height is the entire scrub distance.</p>
    </header>

    <div class="sa-17__scroller" tabindex="0" role="region" aria-label="Orbit setup tour, scrollable">
      <div class="sa-17__travel">
        <div class="sa-17__scene">
          <p class="sa-17__scenetag">Orbit · workspace setup</p>
          <div class="sa-17__steps">
            <article class="sa-17__step sa-17__step--1"><p class="sa-17__snum">01</p><p class="sa-17__st">Connect a repository</p><p class="sa-17__sm">Orbit reads the manifest and proposes an environment set. Nothing is written yet.</p></article>
            <article class="sa-17__step sa-17__step--2"><p class="sa-17__snum">02</p><p class="sa-17__st">Invite teammate</p><p class="sa-17__sm">Priya Sharma joins as reviewer. Deploy rights stay with the owner until the first release lands.</p></article>
            <article class="sa-17__step sa-17__step--3"><p class="sa-17__snum">03</p><p class="sa-17__st">Deploy to production</p><p class="sa-17__sm">A canary at 5%, an automatic error-budget check, then the full rollout.</p></article>
          </div>
          <div class="sa-17__track" aria-hidden="true"><span class="sa-17__thumb"></span></div>
        </div>
      </div>
      <p class="sa-17__tail">Past the travel distance the scene unpins and scrolls away normally. That boundary is the parent's bottom edge, nothing more.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-17 {
  --page: #fff5ee;
  --surface: #ffffff;
  --ink: #2a150f;
  --muted: #7c5548;
  --rule: #f0d6c6;
  --accent: #e2542c;
  --accent2: #f0a03c;
  --page: oklch(96.5% 0.02 45);
  --surface: oklch(100% 0 0);
  --ink: oklch(25% 0.06 35);
  --muted: oklch(50% 0.06 38);
  --rule: oklch(89% 0.035 45);
  --accent: oklch(60% 0.19 35);
  --accent2: oklch(76% 0.15 62);
  --font-display: "Avenir Next Condensed", "Roboto Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4.5rem 1.5rem 4rem;
  background: var(--page);
  background-image: linear-gradient(160deg, color-mix(in srgb, var(--accent2) 22%, transparent), transparent 45%);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-17 *,
.sa-17 *::before,
.sa-17 *::after {
  box-sizing: border-box;
}

.sa-17__stage {
  max-inline-size: 56rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.sa-17__head {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-17__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-17__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 5.5vw, 3rem);
  font-weight: 600;
  letter-spacing: 0.01em;
  line-height: 1.05;
}

.sa-17__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 1rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-17__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.sa-17__scroller {
  block-size: 62vh;
  min-block-size: 21rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 1.25rem;
  background: color-mix(in srgb, var(--surface) 55%, transparent);
  scroll-timeline: --sa-17-tour block;
}

.sa-17__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.sa-17__travel {
  min-block-size: 240vh;
  padding: 1.25rem;
}

.sa-17__scene {
  position: sticky;
  inset-block-start: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  padding: 1.75rem;
  border-radius: 1rem;
  background: var(--surface);
  box-shadow: 0 1.5rem 3rem -1rem color-mix(in srgb, var(--accent) 45%, transparent), 0 0 0 1px color-mix(in srgb, var(--accent) 12%, transparent);
}

.sa-17__scenetag {
  margin: 0;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-17__steps {
  position: relative;
  min-block-size: 9.5rem;
}

.sa-17__step {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  opacity: 0;
  transform: translateY(1rem);
  min-inline-size: 0;
}

.sa-17__step--3 {
  opacity: 1;
  transform: none;
}

.sa-17__snum {
  margin: 0;
  font-family: var(--font-display);
  font-size: 2.75rem;
  font-weight: 600;
  line-height: 1;
  color: color-mix(in srgb, var(--accent) 35%, transparent);
}

.sa-17__st {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.sa-17__sm {
  margin: 0;
  max-inline-size: 32rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-17__track {
  position: relative;
  block-size: 0.375rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--ink) 8%, transparent);
}

.sa-17__thumb {
  position: absolute;
  inset-block: 0;
  inline-size: 33%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent2), var(--accent));
  transform: translateX(200%);
}

.sa-17__tail {
  margin: 0;
  padding: 1.5rem 1.75rem 3rem;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-17-in {
  0% {
    opacity: 0;
    transform: translateY(1rem);
  }

  22% {
    opacity: 1;
    transform: none;
  }

  78% {
    opacity: 1;
    transform: none;
  }

  100% {
    opacity: 0;
    transform: translateY(-0.75rem);
  }
}

@keyframes sa-17-last {
  0% {
    opacity: 0;
    transform: translateY(1rem);
  }

  30% {
    opacity: 1;
    transform: none;
  }

  100% {
    opacity: 1;
    transform: none;
  }
}

@keyframes sa-17-thumb {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(200%);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-17__step--1 {
    animation: sa-17-in linear both;
    animation-timeline: --sa-17-tour;
    animation-range: 0% 34%;
  }

  .sa-17__step--2 {
    animation: sa-17-in linear both;
    animation-timeline: --sa-17-tour;
    animation-range: 33% 67%;
  }

  .sa-17__step--3 {
    animation: sa-17-last linear both;
    animation-timeline: --sa-17-tour;
    animation-range: 66% 100%;
  }

  .sa-17__thumb {
    animation: sa-17-thumb linear both;
    animation-timeline: --sa-17-tour;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-17__step {
    animation: none;
  }

  .sa-17__step--1,
    .sa-17__step--2 {
    opacity: 0;
  }

  .sa-17__step--3 {
    opacity: 1;
    transform: none;
  }

  .sa-17__thumb {
    animation: none;
    transform: translateX(200%);
  }
}

.sa-17__theme {
  position: absolute;
  inset-block-start: 1.25rem;
  inset-inline-end: 1.25rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.25rem;
  border: 0;
  border-radius: 999px;
  background: color-mix(in srgb, var(--surface) 75%, transparent);
  box-shadow: 0 0.5rem 1.5rem -0.5rem color-mix(in srgb, var(--accent) 40%, transparent);
}

.sa-17__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-17__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-17__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.75rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-17__themeinput:checked + .sa-17__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-17__themeinput:focus-visible + .sa-17__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .sa-17 {
    padding: 4.5rem 1rem 3rem;
  }

  .sa-17__scene {
    padding: 1.25rem;
  }

  .sa-17__steps {
    min-block-size: 11.5rem;
  }
}

@media (forced-colors: active) {
  .sa-17__thumb {
    background: Highlight;
  }

  .sa-17__scene {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-17:not(:has(#sa-17-theme-light:checked)) {
    --page: #170d09;
    --surface: #21140f;
    --ink: #ffeee5;
    --muted: #bd9686;
    --rule: #3a221a;
    --accent: #ff7043;
    --accent2: #ffb35c;
  }

  .sa-17:not(:has(#sa-17-theme-light:checked)) .sa-17__themeinput:checked + .sa-17__themeopt {
    color: #170d09;
  }
}

@media (prefers-color-scheme: light) {
  .sa-17:has(#sa-17-theme-dark:checked) {
    --page: #170d09;
    --surface: #21140f;
    --ink: #ffeee5;
    --muted: #bd9686;
    --rule: #3a221a;
    --accent: #ff7043;
    --accent2: #ffb35c;
  }

  .sa-17:has(#sa-17-theme-dark:checked) .sa-17__themeinput:checked + .sa-17__themeopt {
    color: #170d09;
  }
}

[data-theme="dark"] .sa-17:not(:has(#sa-17-theme-light:checked)) {
  --page: #170d09;
  --surface: #21140f;
  --ink: #ffeee5;
  --muted: #bd9686;
  --rule: #3a221a;
  --accent: #ff7043;
  --accent2: #ffb35c;
}

.sa-17:has(#sa-17-theme-dark:checked) {
  --page: #170d09;
  --surface: #21140f;
  --ink: #ffeee5;
  --muted: #bd9686;
  --rule: #3a221a;
  --accent: #ff7043;
  --accent2: #ffb35c;
}

.sa-17:has(#sa-17-theme-dark:checked) .sa-17__themeinput:checked + .sa-17__themeopt {
  color: #170d09;
}

.sa-17:has(#sa-17-theme-light:checked) {
  --page: #fff5ee;
  --surface: #ffffff;
  --ink: #2a150f;
  --muted: #7c5548;
  --rule: #f0d6c6;
  --accent: #e2542c;
  --accent2: #f0a03c;
}
```
