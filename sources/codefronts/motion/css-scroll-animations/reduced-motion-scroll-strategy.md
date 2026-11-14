---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/reduced-motion-scroll-strategy/"
title: "Reduced Motion Strategy for Scroll Motion"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Scroll-bound motion is among the strongest vestibular triggers, because it tracks a movement the user did not ask for."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reduced Motion Strategy for Scroll Motion
Source: https://codefronts.com/motion/css-scroll-animations/reduced-motion-scroll-strategy/

Scroll-bound motion is among the strongest vestibular triggers, because it tracks a movement the user did not ask for. The usual blanket animation: none is wrong here for a specific reason: it can strand elements at their range-start state, invisible or misplaced. The correct order is end state first, binding second.
## HTML
```html
<section class="sa-05" aria-labelledby="sa-05-h">
  <fieldset class="sa-05__theme">
    <legend class="sa-05__themelegend">Theme</legend>
    <input class="sa-05__themeinput" type="radio" name="sa-05-theme" id="sa-05-theme-auto" checked>
    <label class="sa-05__themeopt" for="sa-05-theme-auto">Auto</label>
    <input class="sa-05__themeinput" type="radio" name="sa-05-theme" id="sa-05-theme-light">
    <label class="sa-05__themeopt" for="sa-05-theme-light">Light</label>
    <input class="sa-05__themeinput" type="radio" name="sa-05-theme" id="sa-05-theme-dark">
    <label class="sa-05__themeopt" for="sa-05-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-05__stage">
    <header class="sa-05__head">
      <p class="sa-05__eyebrow">prefers-reduced-motion</p>
      <h2 class="sa-05__h" id="sa-05-h">End state first, binding second</h2>
      <p class="sa-05__sub">Three treatments of one card list. Change your system motion setting and scroll again — only one of the three behaves correctly in both modes.</p>
    </header>

    <div class="sa-05__scroller" tabindex="0" role="region" aria-label="Three reduced motion treatments, scrollable">
      <div class="sa-05__cols">
        <div class="sa-05__col">
          <p class="sa-05__ctag sa-05__ctag--bad">Wrong · blanket animation: none</p>
          <p class="sa-05__cnote">Base style is the start state, so a reduced-motion reader is left with cards stranded at 0 opacity.</p>
          <div class="sa-05__set">
            <article class="sa-05__card sa-05__card--bad">Rotate signing key</article>
            <article class="sa-05__card sa-05__card--bad">Approve invoice run</article>
            <article class="sa-05__card sa-05__card--bad">Archive stale branches</article>
            <article class="sa-05__card sa-05__card--bad">Retry parked webhooks</article>
            <article class="sa-05__card sa-05__card--bad">Close change ticket</article>
            <article class="sa-05__card sa-05__card--bad">Promote the canary</article>
            <article class="sa-05__card sa-05__card--bad">Publish the changelog</article>
          </div>
        </div>

        <div class="sa-05__col">
          <p class="sa-05__ctag sa-05__ctag--ok">Better · non-moving cue</p>
          <p class="sa-05__cnote">Bound opacity, no travel. There is feedback, but nothing crosses the reader's field of view.</p>
          <div class="sa-05__set">
            <article class="sa-05__card sa-05__card--dim">Rotate signing key</article>
            <article class="sa-05__card sa-05__card--dim">Approve invoice run</article>
            <article class="sa-05__card sa-05__card--dim">Archive stale branches</article>
            <article class="sa-05__card sa-05__card--dim">Retry parked webhooks</article>
            <article class="sa-05__card sa-05__card--dim">Close change ticket</article>
            <article class="sa-05__card sa-05__card--dim">Promote the canary</article>
            <article class="sa-05__card sa-05__card--dim">Publish the changelog</article>
          </div>
        </div>

        <div class="sa-05__col">
          <p class="sa-05__ctag sa-05__ctag--best">Right · end state is the default</p>
          <p class="sa-05__cnote">Finished layout in the base layer, motion added only inside a no-preference query. Correct in both modes.</p>
          <div class="sa-05__set">
            <article class="sa-05__card sa-05__card--good">Rotate signing key</article>
            <article class="sa-05__card sa-05__card--good">Approve invoice run</article>
            <article class="sa-05__card sa-05__card--good">Archive stale branches</article>
            <article class="sa-05__card sa-05__card--good">Retry parked webhooks</article>
            <article class="sa-05__card sa-05__card--good">Close change ticket</article>
            <article class="sa-05__card sa-05__card--good">Promote the canary</article>
            <article class="sa-05__card sa-05__card--good">Publish the changelog</article>
          </div>
        </div>
      </div>
      <p class="sa-05__tail">Ordering, not suppression. The accessible state is the default state, and motion is the enhancement.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-05 {
  --page: #f6f3ee;
  --surface: #fffdf9;
  --ink: #232019;
  --muted: #635d51;
  --rule: #ddd6c9;
  --accent: #3a3730;
  --bad: #9c3b2e;
  --page: oklch(96% 0.008 85);
  --surface: oklch(99% 0.005 85);
  --ink: oklch(24% 0.014 75);
  --muted: oklch(49% 0.018 75);
  --rule: oklch(87% 0.014 80);
  --accent: oklch(33% 0.012 75);
  --bad: oklch(48% 0.15 30);
  --font-display: "Segoe UI", Frutiger, "Gill Sans", Calibri, system-ui, sans-serif;
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

.sa-05 *,
.sa-05 *::before,
.sa-05 *::after {
  box-sizing: border-box;
}

.sa-05__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-05__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-05__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-05__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.12;
}

.sa-05__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-05__scroller {
  block-size: 60vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-block: 1px solid var(--rule);
  background: var(--surface);
  scroll-timeline: --sa-05-track block;
}

.sa-05__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-05__cols {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.25rem;
  padding: 1.25rem;
}

.sa-05__col {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-inline-size: 0;
}

.sa-05__ctag {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  margin: 0;
  padding: 0.5rem 0;
  background: var(--surface);
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-block-end: 1px solid var(--rule);
}

.sa-05__ctag--bad {
  color: var(--bad);
}

.sa-05__ctag--ok {
  color: var(--muted);
}

.sa-05__ctag--best {
  color: var(--accent);
}

.sa-05__cnote {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-05__set {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  min-block-size: 28rem;
  padding-block: 1.25rem 3rem;
}

.sa-05__card {
  padding: 1rem 0.875rem;
  border-block-start: 2px solid var(--accent);
  background: color-mix(in srgb, var(--ink) 4%, transparent);
  font-size: 0.875rem;
  font-weight: 600;
  min-inline-size: 0;
}

.sa-05__card--bad {
  opacity: 0;
  transform: translateY(1.5rem);
}

.sa-05__card--dim {
  opacity: 0.55;
  border-block-start-color: var(--muted);
}

.sa-05__card--good {
  opacity: 1;
  transform: none;
}

.sa-05__tail {
  margin: 0;
  padding: 1rem 1.25rem 2rem;
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-05-rise {
  from {
    opacity: 0;
    transform: translateY(1.5rem);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes sa-05-fade {
  from {
    opacity: 0.55;
  }

  to {
    opacity: 1;
  }
}

@supports (animation-timeline: view()) {
  .sa-05__card--bad {
    animation: sa-05-rise linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 40%;
  }

  .sa-05__card--dim {
    animation: sa-05-fade linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 40%;
  }

  @media (prefers-reduced-motion: no-preference) {
    .sa-05__card--good {
      animation: sa-05-rise linear both;
      animation-timeline: view(block);
      animation-range: entry 0% cover 40%;
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-05__card--bad {
    animation: none;
  }

  .sa-05__scroller {
    scroll-behavior: auto;
  }
}

.sa-05__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  background: var(--surface);
}

.sa-05__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-05__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-05__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-05__themeinput:checked + .sa-05__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-05__themeinput:focus-visible + .sa-05__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 52rem) {
  .sa-05__cols {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-05__set {
    gap: 1.5rem;
    padding-block-end: 2rem;
  }

  .sa-05 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-05__card {
    border-block-start: 2px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-05:not(:has(#sa-05-theme-light:checked)) {
    --page: #17150f;
    --surface: #1e1c15;
    --ink: #f2eee4;
    --muted: #a09a8b;
    --rule: #322e25;
    --accent: #e8e2d4;
    --bad: #ff8878;
  }

  .sa-05:not(:has(#sa-05-theme-light:checked)) .sa-05__themeinput:checked + .sa-05__themeopt {
    color: #17150f;
  }
}

@media (prefers-color-scheme: light) {
  .sa-05:has(#sa-05-theme-dark:checked) {
    --page: #17150f;
    --surface: #1e1c15;
    --ink: #f2eee4;
    --muted: #a09a8b;
    --rule: #322e25;
    --accent: #e8e2d4;
    --bad: #ff8878;
  }

  .sa-05:has(#sa-05-theme-dark:checked) .sa-05__themeinput:checked + .sa-05__themeopt {
    color: #17150f;
  }
}

[data-theme="dark"] .sa-05:not(:has(#sa-05-theme-light:checked)) {
  --page: #17150f;
  --surface: #1e1c15;
  --ink: #f2eee4;
  --muted: #a09a8b;
  --rule: #322e25;
  --accent: #e8e2d4;
  --bad: #ff8878;
}

.sa-05:has(#sa-05-theme-dark:checked) {
  --page: #17150f;
  --surface: #1e1c15;
  --ink: #f2eee4;
  --muted: #a09a8b;
  --rule: #322e25;
  --accent: #e8e2d4;
  --bad: #ff8878;
}

.sa-05:has(#sa-05-theme-dark:checked) .sa-05__themeinput:checked + .sa-05__themeopt {
  color: #17150f;
}

.sa-05:has(#sa-05-theme-light:checked) {
  --page: #f6f3ee;
  --surface: #fffdf9;
  --ink: #232019;
  --muted: #635d51;
  --rule: #ddd6c9;
  --accent: #3a3730;
  --bad: #9c3b2e;
}
```
