---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/clip-path-reveals/"
title: "View Timeline Subject and Scroller"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "scroll() tracks the scroller's total offset; view() tracks one element's own passage through that scroller."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: View Timeline Subject and Scroller
Source: https://codefronts.com/motion/css-scroll-animations/clip-path-reveals/

scroll() tracks the scroller's total offset; view() tracks one element's own passage through that scroller. The difference is the source of most "why does it animate at the wrong time" confusion, so this demo runs both bindings side by side with the subject and the scroller labelled on each.
## HTML
```html
<section class="sa-11" aria-labelledby="sa-11-h">
  <fieldset class="sa-11__theme">
    <legend class="sa-11__themelegend">Theme</legend>
    <input class="sa-11__themeinput" type="radio" name="sa-11-theme" id="sa-11-theme-auto" checked>
    <label class="sa-11__themeopt" for="sa-11-theme-auto">Auto</label>
    <input class="sa-11__themeinput" type="radio" name="sa-11-theme" id="sa-11-theme-light">
    <label class="sa-11__themeopt" for="sa-11-theme-light">Light</label>
    <input class="sa-11__themeinput" type="radio" name="sa-11-theme" id="sa-11-theme-dark">
    <label class="sa-11__themeopt" for="sa-11-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-11__stage">
    <header class="sa-11__head">
      <p class="sa-11__eyebrow">Subject vs scroller</p>
      <h2 class="sa-11__h" id="sa-11-h">Which element is being tracked?</h2>
      <p class="sa-11__sub">Same scroller, same keyframes, two bindings. Scroll either column: the left reads each card's own passage, the right reads the container's offset.</p>
    </header>

    <div class="sa-11__diagram">
      <div class="sa-11__dcell"><span class="sa-11__dkey sa-11__dkey--subject">Subject</span><p class="sa-11__dtext">the element being tracked. With <span class="sa-11__mono">view()</span> that is the element the declaration sits on.</p></div>
      <div class="sa-11__dcell"><span class="sa-11__dkey sa-11__dkey--scroller">Scroller</span><p class="sa-11__dtext">the scroll container it travels through. Resolved as <span class="sa-11__mono">nearest</span> unless you say otherwise.</p></div>
    </div>

    <div class="sa-11__pair">
      <article class="sa-11__col">
        <p class="sa-11__label"><span class="sa-11__badge sa-11__badge--a">view()</span> tracks each card's passage</p>
        <div class="sa-11__scroller" tabindex="0" role="region" aria-label="Cards bound with view timeline, scrollable">
          <div class="sa-11__inner">
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Aperture · Q3 usage</p><p class="sa-11__cm">Subject 1 of 5</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Fern · seat allocation</p><p class="sa-11__cm">Subject 2 of 5</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Nova · retention cohort</p><p class="sa-11__cm">Subject 3 of 5</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Talon · error budget</p><p class="sa-11__cm">Subject 4 of 5</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Vale · invoice run</p><p class="sa-11__cm">Subject 5 of 8</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Basalt · queue latency</p><p class="sa-11__cm">Subject 6 of 8</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Prism · trial conversions</p><p class="sa-11__cm">Subject 7 of 8</p></div>
            <div class="sa-11__card sa-11__card--view"><p class="sa-11__ct">Ranger · support backlog</p><p class="sa-11__cm">Subject 8 of 8</p></div>
          </div>
        </div>
        <p class="sa-11__verdict">Each card animates around its own arrival. Add a sixth and it behaves identically.</p>
      </article>

      <article class="sa-11__col">
        <p class="sa-11__label"><span class="sa-11__badge sa-11__badge--b">scroll()</span> tracks the container's offset</p>
        <div class="sa-11__scroller" tabindex="0" role="region" aria-label="Cards bound with scroll timeline, scrollable">
          <div class="sa-11__inner">
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Aperture · Q3 usage</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Fern · seat allocation</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Nova · retention cohort</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Talon · error budget</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Vale · invoice run</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Basalt · queue latency</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Prism · trial conversions</p><p class="sa-11__cm">Not the subject</p></div>
            <div class="sa-11__card sa-11__card--scroll"><p class="sa-11__ct">Ranger · support backlog</p><p class="sa-11__cm">Not the subject</p></div>
          </div>
        </div>
        <p class="sa-11__verdict">All five move together, already part-finished on arrival. Right for page chrome, wrong for cards.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-11 {
  --page: #f1f3f5;
  --surface: #ffffff;
  --ink: #16191d;
  --muted: #5c646e;
  --rule: #d6dbe1;
  --accent: #0d7f8c;
  --accent2: #8a6cff;
  --page: oklch(96% 0.004 240);
  --surface: oklch(100% 0 0);
  --ink: oklch(20% 0.008 250);
  --muted: oklch(50% 0.014 250);
  --rule: oklch(88% 0.008 250);
  --accent: oklch(56% 0.1 195);
  --accent2: oklch(62% 0.17 288);
  --font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
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

.sa-11 *,
.sa-11 *::before,
.sa-11 *::after {
  box-sizing: border-box;
}

.sa-11__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-11__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-11__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-11__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.4vw, 2.375rem);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.015em;
}

.sa-11__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-11__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
}

.sa-11__diagram {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 0.75rem;
}

.sa-11__dcell {
  display: flex;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.625rem;
  box-shadow: 0 1px 2px color-mix(in srgb, var(--ink) 8%, transparent);
  min-inline-size: 0;
}

.sa-11__dkey {
  flex: 0 0 auto;
  align-self: start;
  padding: 0.1875rem 0.5rem;
  border-radius: 0.3125rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #fff;
}

.sa-11__dkey--subject {
  background: var(--accent);
}

.sa-11__dkey--scroller {
  background: var(--accent2);
}

.sa-11__dtext {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.8125rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-11__pair {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.sa-11__col {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  min-inline-size: 0;
}

.sa-11__label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
}

.sa-11__badge {
  padding: 0.1875rem 0.4375rem;
  border-radius: 0.25rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  color: #fff;
}

.sa-11__badge--a {
  background: var(--accent);
}

.sa-11__badge--b {
  background: var(--accent2);
}

.sa-11__scroller {
  block-size: 52vh;
  min-block-size: 17rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: var(--surface);
  box-shadow: 0 1px 3px color-mix(in srgb, var(--ink) 10%, transparent);
  scroll-timeline: --sa-11-track block;
}

.sa-11__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-11__inner {
  min-block-size: calc(100% + 6rem);
  padding: 1rem 1rem 3rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-11__card {
  padding: 1.125rem 1rem;
  border-radius: 0.625rem;
  border: 1px solid var(--rule);
  background: color-mix(in srgb, var(--ink) 3%, transparent);
  opacity: 1;
  transform: none;
  min-inline-size: 0;
}

.sa-11__card--view {
  border-inline-start: 3px solid var(--accent);
}

.sa-11__card--scroll {
  border-inline-start: 3px solid var(--accent2);
}

.sa-11__ct {
  margin: 0 0 0.1875rem;
  font-family: var(--font-display);
  font-size: 1rem;
}

.sa-11__cm {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-11__verdict {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-11-sweep {
  from {
    opacity: 0.25;
    transform: translateY(1.25rem) scale(0.96);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@supports (animation-timeline: view()) {
  .sa-11__card--view {
    animation: sa-11-sweep linear both;
    animation-timeline: view(block);
    animation-range: entry 5% cover 45%;
  }

  .sa-11__card--scroll {
    animation: sa-11-sweep linear both;
    animation-timeline: --sa-11-track;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-11__card--view,
    .sa-11__card--scroll {
    animation: none;
    opacity: 1;
    transform: none;
  }
}

.sa-11__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  border-radius: 999px;
  background: var(--surface);
}

.sa-11__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-11__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-11__themeopt {
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
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-11__themeinput:checked + .sa-11__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-11__themeinput:focus-visible + .sa-11__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 46rem) {
  .sa-11__pair {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-11__scroller {
    block-size: 42vh;
  }
}

@media (forced-colors: active) {
  .sa-11__badge {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-11:not(:has(#sa-11-theme-light:checked)) {
    --page: #0f1214;
    --surface: #171b1f;
    --ink: #eaeef2;
    --muted: #9aa5b1;
    --rule: #2a3037;
    --accent: #3fc7d4;
    --accent2: #a48cff;
  }

  .sa-11:not(:has(#sa-11-theme-light:checked)) .sa-11__dkey,
    .sa-11:not(:has(#sa-11-theme-light:checked)) .sa-11__badge {
    color: #0f1214;
  }
}

@media (prefers-color-scheme: light) {
  .sa-11:has(#sa-11-theme-dark:checked) {
    --page: #0f1214;
    --surface: #171b1f;
    --ink: #eaeef2;
    --muted: #9aa5b1;
    --rule: #2a3037;
    --accent: #3fc7d4;
    --accent2: #a48cff;
  }

  .sa-11:has(#sa-11-theme-dark:checked) .sa-11__dkey,
    .sa-11:has(#sa-11-theme-dark:checked) .sa-11__badge {
    color: #0f1214;
  }
}

[data-theme="dark"] .sa-11:not(:has(#sa-11-theme-light:checked)) {
  --page: #0f1214;
  --surface: #171b1f;
  --ink: #eaeef2;
  --muted: #9aa5b1;
  --rule: #2a3037;
  --accent: #3fc7d4;
  --accent2: #a48cff;
}

.sa-11:has(#sa-11-theme-dark:checked) {
  --page: #0f1214;
  --surface: #171b1f;
  --ink: #eaeef2;
  --muted: #9aa5b1;
  --rule: #2a3037;
  --accent: #3fc7d4;
  --accent2: #a48cff;
}

.sa-11:has(#sa-11-theme-dark:checked) .sa-11__dkey,
.sa-11:has(#sa-11-theme-dark:checked) .sa-11__badge {
  color: #0f1214;
}

.sa-11:has(#sa-11-theme-light:checked) {
  --page: #f1f3f5;
  --surface: #ffffff;
  --ink: #16191d;
  --muted: #5c646e;
  --rule: #d6dbe1;
  --accent: #0d7f8c;
  --accent2: #8a6cff;
}

.sa-11:has(#sa-11-theme-light:checked) .sa-11__dkey,
.sa-11:has(#sa-11-theme-light:checked) .sa-11__badge {
  color: #ffffff;
}
```
