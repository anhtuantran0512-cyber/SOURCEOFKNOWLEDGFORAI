---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/staggered-portfolio-list/"
title: "Non Root Scroll Containers and Overflow"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "A scroll timeline needs a scroll container, and an element only becomes one through overflow: scroll or auto."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Non Root Scroll Containers and Overflow
Source: https://codefronts.com/motion/css-scroll-animations/staggered-portfolio-list/

A scroll timeline needs a scroll container, and an element only becomes one through overflow: scroll or auto. Bind to a panel that never scrolls and there is no error, no warning, and no motion. Two panels here differ by exactly one declaration — one works, one is dead — and both are labelled.
## HTML
```html
<section class="sa-16" aria-labelledby="sa-16-h">
  <fieldset class="sa-16__theme">
    <legend class="sa-16__themelegend">Theme</legend>
    <input class="sa-16__themeinput" type="radio" name="sa-16-theme" id="sa-16-theme-auto" checked>
    <label class="sa-16__themeopt" for="sa-16-theme-auto">Auto</label>
    <input class="sa-16__themeinput" type="radio" name="sa-16-theme" id="sa-16-theme-light">
    <label class="sa-16__themeopt" for="sa-16-theme-light">Light</label>
    <input class="sa-16__themeinput" type="radio" name="sa-16-theme" id="sa-16-theme-dark">
    <label class="sa-16__themeopt" for="sa-16-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-16__stage">
    <header class="sa-16__head">
      <p class="sa-16__eyebrow">One declaration apart</p>
      <h2 class="sa-16__h" id="sa-16-h">Only a scroll container has a timeline</h2>
      <p class="sa-16__sub">Identical markup, identical keyframes, identical binding. The panel on the right is missing <span class="sa-16__mono">overflow-y: auto</span>, so its timeline has nothing to read.</p>
    </header>

    <div class="sa-16__pair">
      <article class="sa-16__panel sa-16__panel--good">
        <div class="sa-16__phead">
          <span class="sa-16__state sa-16__state--good">
            <svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false"><path d="M2.5 8.5 6 12l7.5-8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
            Scroll container — indicator advances
          </span>
          <code class="sa-16__code">overflow-y: auto</code>
        </div>
        <div class="sa-16__meter"><span class="sa-16__fill sa-16__fill--good"></span></div>
        <div class="sa-16__box sa-16__box--scrolls" tabindex="0" role="region" aria-label="Working scroll container, scrollable">
          <ul class="sa-16__rows">
            <li class="sa-16__row">Deploy to production · Meridian</li>
            <li class="sa-16__row">Sync 4 repositories · Fern</li>
            <li class="sa-16__row">Rotate signing key · Basalt</li>
            <li class="sa-16__row">Invite teammate · Nova</li>
            <li class="sa-16__row">Archive stale branches · Quill</li>
            <li class="sa-16__row">Publish changelog · Prism</li>
            <li class="sa-16__row">Review error budget · Talon</li>
            <li class="sa-16__row">Approve invoice run · Vale</li>
            <li class="sa-16__row">Rebuild search index · Aperture</li>
            <li class="sa-16__row">Expire access tokens · Ranger</li>
            <li class="sa-16__row">Promote replica · Sable</li>
            <li class="sa-16__row">Retry parked webhooks · Talon</li>
            <li class="sa-16__row">Close change ticket · Orbit</li>
            <li class="sa-16__row">Rotate region key · Vale</li>
          </ul>
        </div>
      </article>

      <article class="sa-16__panel sa-16__panel--bad">
        <div class="sa-16__phead">
          <span class="sa-16__state sa-16__state--bad">
            <svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false"><path d="M4 4l8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"></path></svg>
            Not a scroll container — indicator is dead
          </span>
          <code class="sa-16__code">overflow: visible</code>
        </div>
        <div class="sa-16__meter"><span class="sa-16__fill sa-16__fill--bad"></span></div>
        <div class="sa-16__box sa-16__box--clipped">
          <ul class="sa-16__rows">
            <li class="sa-16__row">Deploy to production · Meridian</li>
            <li class="sa-16__row">Sync 4 repositories · Fern</li>
            <li class="sa-16__row">Rotate signing key · Basalt</li>
            <li class="sa-16__row">Invite teammate · Nova</li>
          </ul>
          <p class="sa-16__why">No overflow declaration, so no scroll container. <span class="sa-16__mono">scroll(nearest)</span> walks past this element and binds to whatever scrolls above it.</p>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-16 {
  --page: #f5f8fd;
  --surface: #ffffff;
  --ink: #0d1b2e;
  --muted: #536b8a;
  --rule: #d3e0ef;
  --accent: #1667d6;
  --bad: #c9342b;
  --page: oklch(97.5% 0.012 250);
  --surface: oklch(100% 0 0);
  --ink: oklch(22% 0.04 255);
  --muted: oklch(52% 0.05 250);
  --rule: oklch(89% 0.025 250);
  --accent: oklch(53% 0.18 258);
  --bad: oklch(53% 0.19 27);
  --font-display: system-ui, "Segoe UI", "Helvetica Neue", sans-serif;
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

.sa-16 *,
.sa-16 *::before,
.sa-16 *::after {
  box-sizing: border-box;
}

.sa-16__stage {
  max-inline-size: 64rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-16__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-16__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-16__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.025em;
  line-height: 1.12;
}

.sa-16__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-16__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
}

.sa-16__pair {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  align-items: start;
}

.sa-16__panel {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1rem;
  border-radius: 0.875rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  box-shadow: 0 0.375rem 0 color-mix(in srgb, var(--accent) 22%, transparent);
  min-inline-size: 0;
}

.sa-16__panel--bad {
  box-shadow: 0 0.375rem 0 color-mix(in srgb, var(--bad) 25%, transparent);
}

.sa-16__phead {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  justify-content: space-between;
}

.sa-16__state {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  min-inline-size: 0;
  font-size: 0.75rem;
  font-weight: 700;
}

.sa-16__state--good {
  color: var(--accent);
}

.sa-16__state--bad {
  color: var(--bad);
}

.sa-16__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  padding: 0.1875rem 0.375rem;
  border-radius: 0.25rem;
  background: color-mix(in srgb, var(--ink) 7%, transparent);
}

.sa-16__meter {
  block-size: 0.5rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--ink) 8%, transparent);
  overflow: hidden;
}

.sa-16__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  border-radius: 999px;
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-16__fill--good {
  background: var(--accent);
}

.sa-16__fill--bad {
  background: var(--bad);
  transform: scaleX(0.06);
}

.sa-16__box {
  block-size: 44vh;
  min-block-size: 15rem;
  border-radius: 0.625rem;
  border: 1px solid var(--rule);
  background: color-mix(in srgb, var(--ink) 3%, transparent);
}

.sa-16__box--scrolls {
  overflow-y: auto;
  overscroll-behavior: contain;
  scroll-timeline: --sa-16-good block;
}

.sa-16__box--scrolls:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-16__box--clipped {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.sa-16__rows {
  margin: 0;
  min-block-size: calc(100% + 6rem);
  padding: 0.75rem;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-16__row {
  padding: 0.75rem 0.875rem;
  border-radius: 0.5rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  font-size: 0.8125rem;
  min-inline-size: 0;
}

.sa-16__why {
  margin: auto 0 0;
  padding: 0.875rem;
  border-block-start: 1px dashed var(--bad);
  font-size: 0.75rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-16-fill {
  from {
    transform: scaleX(0.06);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-16__fill--good {
    animation: sa-16-fill linear both;
    animation-timeline: --sa-16-good;
  }

  .sa-16__fill--bad {
    animation: sa-16-fill linear both;
    animation-timeline: --sa-16-missing;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-16__fill--good {
    animation: none;
    transform: scaleX(1);
  }
}

.sa-16__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
}

.sa-16__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-16__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-16__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 0.375rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-16__themeinput:checked + .sa-16__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-16__themeinput:focus-visible + .sa-16__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-16__pair {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-16__box {
    block-size: 34vh;
  }

  .sa-16 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-16__fill--good {
    background: Highlight;
  }

  .sa-16__panel {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-16:not(:has(#sa-16-theme-light:checked)) {
    --page: #080e18;
    --surface: #101a29;
    --ink: #e6eefb;
    --muted: #93a6c2;
    --rule: #223148;
    --accent: #5b9dff;
    --bad: #ff7b70;
  }

  .sa-16:not(:has(#sa-16-theme-light:checked)) .sa-16__themeinput:checked + .sa-16__themeopt {
    color: #080e18;
  }
}

@media (prefers-color-scheme: light) {
  .sa-16:has(#sa-16-theme-dark:checked) {
    --page: #080e18;
    --surface: #101a29;
    --ink: #e6eefb;
    --muted: #93a6c2;
    --rule: #223148;
    --accent: #5b9dff;
    --bad: #ff7b70;
  }

  .sa-16:has(#sa-16-theme-dark:checked) .sa-16__themeinput:checked + .sa-16__themeopt {
    color: #080e18;
  }
}

[data-theme="dark"] .sa-16:not(:has(#sa-16-theme-light:checked)) {
  --page: #080e18;
  --surface: #101a29;
  --ink: #e6eefb;
  --muted: #93a6c2;
  --rule: #223148;
  --accent: #5b9dff;
  --bad: #ff7b70;
}

.sa-16:has(#sa-16-theme-dark:checked) {
  --page: #080e18;
  --surface: #101a29;
  --ink: #e6eefb;
  --muted: #93a6c2;
  --rule: #223148;
  --accent: #5b9dff;
  --bad: #ff7b70;
}

.sa-16:has(#sa-16-theme-dark:checked) .sa-16__themeinput:checked + .sa-16__themeopt {
  color: #080e18;
}

.sa-16:has(#sa-16-theme-light:checked) {
  --page: #f5f8fd;
  --surface: #ffffff;
  --ink: #0d1b2e;
  --muted: #536b8a;
  --rule: #d3e0ef;
  --accent: #1667d6;
  --bad: #c9342b;
}
```
