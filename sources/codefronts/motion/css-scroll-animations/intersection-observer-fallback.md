---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/intersection-observer-fallback/"
title: "Intersection Observer Fallback Contract"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Safari has not shipped scroll-driven animations, so anything scroll-bound needs a plan for it — and the honest plan is IntersectionObserver, which triggers…"
has_js: "true"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Intersection Observer Fallback Contract
Source: https://codefronts.com/motion/css-scroll-animations/intersection-observer-fallback/

Safari has not shipped scroll-driven animations, so anything scroll-bound needs a plan for it — and the honest plan is IntersectionObserver, which triggers rather than scrubs. This demo runs both paths side by side and states the contract plainly: the fallback is a different behaviour, so design it as an intentional one.
## HTML
```html
<section class="sa-01" aria-labelledby="sa-01-h">
  <fieldset class="sa-01__theme">
    <legend class="sa-01__themelegend">Theme</legend>
    <input class="sa-01__themeinput" type="radio" name="sa-01-theme" id="sa-01-theme-auto" checked>
    <label class="sa-01__themeopt" for="sa-01-theme-auto">Auto</label>
    <input class="sa-01__themeinput" type="radio" name="sa-01-theme" id="sa-01-theme-light">
    <label class="sa-01__themeopt" for="sa-01-theme-light">Light</label>
    <input class="sa-01__themeinput" type="radio" name="sa-01-theme" id="sa-01-theme-dark">
    <label class="sa-01__themeopt" for="sa-01-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-01__stage">
    <header class="sa-01__head">
      <p class="sa-01__eyebrow">fallback contract</p>
      <h2 class="sa-01__h" id="sa-01-h">Scrub on the left, trigger on the right</h2>
      <p class="sa-01__sub">One scroller, two mechanisms. Scroll down, then back up: the bound column reverses, the observed column does not. That asymmetry is the contract.</p>
      <p class="sa-01__status" id="sa-01-status" role="status">Detecting support…</p>
    </header>

    <div class="sa-01__scroller" tabindex="0" role="region" aria-label="Scrub versus trigger comparison, scrollable">
      <div class="sa-01__cols">
        <div class="sa-01__col">
          <p class="sa-01__ctag sa-01__ctag--css">Bound to scroll() — scrubs</p>
          <div class="sa-01__list">
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">api-gateway</p><p class="sa-01__cm">reverses on scroll up</p></article>
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">worker-pool</p><p class="sa-01__cm">progress is position</p></article>
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">edge-cache</p><p class="sa-01__cm">no listener, off main thread</p></article>
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">audit-log</p><p class="sa-01__cm">Chrome 115+, Firefox 136+</p></article>
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">billing-worker</p><p class="sa-01__cm">progress survives a fling</p></article>
            <article class="sa-01__card sa-01__card--css"><p class="sa-01__ct">search-index</p><p class="sa-01__cm">no state to reset</p></article>
          </div>
        </div>
        <div class="sa-01__col">
          <p class="sa-01__ctag sa-01__ctag--js">IntersectionObserver — triggers once</p>
          <div class="sa-01__list">
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">api-gateway</p><p class="sa-01__cm">fires at 20% visible</p></article>
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">worker-pool</p><p class="sa-01__cm">runs on its own clock</p></article>
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">edge-cache</p><p class="sa-01__cm">does not reverse</p></article>
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">audit-log</p><p class="sa-01__cm">works in every engine</p></article>
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">billing-worker</p><p class="sa-01__cm">unobserved after firing</p></article>
            <article class="sa-01__card sa-01__card--js"><p class="sa-01__ct">search-index</p><p class="sa-01__cm">one shot, then done</p></article>
          </div>
        </div>
      </div>
      <p class="sa-01__tail">Design the fallback as a deliberate one-shot entrance. Never let it inherit the scrub's start state.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-01 {
  --page: #04070500;
  --page: #040705;
  --surface: #0a0f0b;
  --ink: #d9f7e2;
  --muted: #6f9a7d;
  --rule: #16241a;
  --accent: #3ff08a;
  --page: oklch(10% 0.012 155);
  --surface: oklch(14% 0.016 155);
  --ink: oklch(93% 0.05 155);
  --muted: oklch(65% 0.06 155);
  --rule: oklch(23% 0.03 155);
  --accent: oklch(85% 0.19 152);
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4rem 1rem 3rem;
  background: var(--page);
  background-image: linear-gradient(var(--rule) 1px, transparent 1px), linear-gradient(90deg, var(--rule) 1px, transparent 1px);
  background-size: 1.5rem 1.5rem;
  color: var(--ink);
  font-family: var(--font-display);
}

.sa-01 *,
.sa-01 *::before,
.sa-01 *::after {
  box-sizing: border-box;
}

.sa-01__stage {
  max-inline-size: 58rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-01__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-01__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-01__h {
  margin: 0;
  font-size: clamp(1.25rem, 3.8vw, 1.875rem);
  font-weight: 500;
  letter-spacing: -0.03em;
  line-height: 1.15;
}

.sa-01__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-family: system-ui, sans-serif;
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-01__status {
  margin: 0;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--rule);
  background: var(--surface);
  font-size: 0.75rem;
  color: var(--accent);
}

.sa-01__scroller {
  block-size: 58vh;
  min-block-size: 19rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 1px solid var(--rule);
  background: color-mix(in srgb, var(--surface) 88%, transparent);
  scroll-timeline: --sa-01-track block;
}

.sa-01__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-01__cols {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.75rem;
  padding: 0.75rem;
}

.sa-01__col {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  min-inline-size: 0;
}

.sa-01__ctag {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  margin: 0;
  padding: 0.5rem;
  background: var(--page);
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.sa-01__ctag--css {
  color: var(--accent);
  border-block-end: 1px solid var(--accent);
}

.sa-01__ctag--js {
  color: var(--ink);
  border-block-end: 1px dashed var(--muted);
}

.sa-01__list {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  min-block-size: 30rem;
  padding-block: 1.5rem 3rem;
}

.sa-01__card {
  padding: 0.875rem;
  border: 1px solid var(--rule);
  background: var(--surface);
  opacity: 1;
  transform: none;
  min-inline-size: 0;
}

.sa-01__card--css {
  border-inline-start: 3px solid var(--accent);
}

.sa-01__card--js {
  border-inline-start: 3px dashed var(--muted);
  transition: opacity 420ms ease-out, transform 420ms ease-out;
}

.sa-01__ct {
  margin: 0 0 0.25rem;
  font-size: 0.9375rem;
  font-weight: 500;
}

.sa-01__cm {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  color: var(--muted);
}

.sa-01__tail {
  margin: 0;
  padding: 0.875rem;
  border-block-start: 1px solid var(--rule);
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-01--js .sa-01__card--js {
  opacity: 0.15;
  transform: translateY(1.25rem);
}

.sa-01--js .sa-01__card--js.is-sa-01-in {
  opacity: 1;
  transform: none;
}

@keyframes sa-01-scrub {
  from {
    opacity: 0.2;
    transform: translateY(1.25rem);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@supports (animation-timeline: view()) {
  .sa-01__card--css {
    animation: sa-01-scrub linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 45%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-01__card--css {
    animation: none;
    opacity: 1;
    transform: none;
  }

  .sa-01--js .sa-01__card--js {
    opacity: 1;
    transform: none;
    transition: none;
  }
}

.sa-01__theme {
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

.sa-01__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-01__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-01__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-01__themeinput:checked + .sa-01__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-01__themeinput:focus-visible + .sa-01__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 40rem) {
  .sa-01__cols {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-01 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-01__card {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: light) {
  .sa-01:not(:has(#sa-01-theme-dark:checked)) {
    --page: #f4f8f5;
    --surface: #ffffff;
    --ink: #0b1a10;
    --muted: #4d6b57;
    --rule: #d3e2d8;
    --accent: #0f7a44;
  }

  .sa-01:not(:has(#sa-01-theme-dark:checked)) .sa-01__themeinput:checked + .sa-01__themeopt {
    color: #ffffff;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-01:has(#sa-01-theme-light:checked) {
    --page: #f4f8f5;
    --surface: #ffffff;
    --ink: #0b1a10;
    --muted: #4d6b57;
    --rule: #d3e2d8;
    --accent: #0f7a44;
  }

  .sa-01:has(#sa-01-theme-light:checked) .sa-01__themeinput:checked + .sa-01__themeopt {
    color: #ffffff;
  }
}

[data-theme="light"] .sa-01:not(:has(#sa-01-theme-dark:checked)) {
  --page: #f4f8f5;
  --surface: #ffffff;
  --ink: #0b1a10;
  --muted: #4d6b57;
  --rule: #d3e2d8;
  --accent: #0f7a44;
}

.sa-01:has(#sa-01-theme-light:checked) {
  --page: #f4f8f5;
  --surface: #ffffff;
  --ink: #0b1a10;
  --muted: #4d6b57;
  --rule: #d3e2d8;
  --accent: #0f7a44;
}

.sa-01:has(#sa-01-theme-light:checked) .sa-01__themeinput:checked + .sa-01__themeopt {
  color: #ffffff;
}

.sa-01:has(#sa-01-theme-dark:checked) {
  --page: #040705;
  --surface: #0a0f0b;
  --ink: #d9f7e2;
  --muted: #6f9a7d;
  --rule: #16241a;
  --accent: #3ff08a;
}
```

## JavaScript
```js
const root = document.querySelector('.sa-01');
const status = document.getElementById('sa-01-status');
const bound = CSS.supports('animation-timeline: scroll()');
status.textContent = bound
  ? 'animation-timeline supported — CSS column scrubs, observer column stays a trigger.'
  : 'animation-timeline unsupported — both columns fall back; the observer column triggers once.';
root.classList.add('sa-01--js');
const cards = [...root.querySelectorAll('.sa-01__card--js')];
const io = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (!entry.isIntersecting) continue;
    entry.target.classList.add('is-sa-01-in');
    io.unobserve(entry.target);
  }
}, { root: root.querySelector('.sa-01__scroller'), threshold: 0.2 });
cards.forEach((card) => io.observe(card));
root.saCleanup = () => {
  io.disconnect();
  root.classList.remove('sa-01--js');
};
```
