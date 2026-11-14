---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/root-margin-threshold-semantics/"
title: "Root Margin and Threshold Semantics"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "The two IntersectionObserver options that most people set by trial and error."
has_js: "true"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Root Margin and Threshold Semantics
Source: https://codefronts.com/motion/css-scroll-animations/root-margin-threshold-semantics/

The two IntersectionObserver options that most people set by trial and error. rootMargin grows or shrinks the detection box in CSS-length syntax, negatives included; threshold decides how much of the subject must be visible to fire, and an array fires at several points. A live dial reports the current ratio and which threshold last fired.
## HTML
```html
<section class="sa-02" aria-labelledby="sa-02-h">
  <fieldset class="sa-02__theme">
    <legend class="sa-02__themelegend">Theme</legend>
    <input class="sa-02__themeinput" type="radio" name="sa-02-theme" id="sa-02-theme-auto" checked>
    <label class="sa-02__themeopt" for="sa-02-theme-auto">Auto</label>
    <input class="sa-02__themeinput" type="radio" name="sa-02-theme" id="sa-02-theme-light">
    <label class="sa-02__themeopt" for="sa-02-theme-light">Light</label>
    <input class="sa-02__themeinput" type="radio" name="sa-02-theme" id="sa-02-theme-dark">
    <label class="sa-02__themeopt" for="sa-02-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-02__stage">
    <header class="sa-02__head">
      <p class="sa-02__eyebrow">rootMargin · threshold</p>
      <h2 class="sa-02__h" id="sa-02-h">What actually fired, and at what ratio</h2>
      <p class="sa-02__sub">The detection box is the panel shrunk by 25% at the bottom. Scroll and watch the dial: every crossing of 0, 0.25, 0.5, 0.75 and 1 reports itself.</p>
    </header>

    <div class="sa-02__layout">
      <div class="sa-02__dial">
        <p class="sa-02__dlabel">intersectionRatio</p>
        <p class="sa-02__dvalue" id="sa-02-ratio" role="status">0.00</p>
        <div class="sa-02__gauge"><span class="sa-02__gfill" id="sa-02-fill"></span></div>
        <p class="sa-02__dfired">last threshold fired · <span class="sa-02__dfnum" id="sa-02-threshold">—</span></p>
        <ul class="sa-02__opts">
          <li class="sa-02__opt"><code class="sa-02__code">root</code> the panel, not the viewport</li>
          <li class="sa-02__opt"><code class="sa-02__code">rootMargin</code> 0px 0px -25% 0px</li>
          <li class="sa-02__opt"><code class="sa-02__code">threshold</code> [0, .25, .5, .75, 1]</li>
        </ul>
      </div>

      <div class="sa-02__scroller" id="sa-02-scroller" tabindex="0" role="region" aria-label="Observed rows, scrollable">
        <div class="sa-02__pad">
          <p class="sa-02__hint">Scroll · the tracked row is outlined</p>
          <div class="sa-02__row">Aperture · 1,204 sessions</div>
          <div class="sa-02__row">Basalt · 986 sessions</div>
          <div class="sa-02__row sa-02__row--target" id="sa-02-target">Meridian · tracked subject</div>
          <div class="sa-02__row">Nova · 742 sessions</div>
          <div class="sa-02__row">Orbit · 655 sessions</div>
          <div class="sa-02__row">Prism · 418 sessions</div>
          <div class="sa-02__row">Vale · 209 sessions</div>
          <div class="sa-02__row">Quill · 186 sessions</div>
          <div class="sa-02__row">Ranger · 174 sessions</div>
          <div class="sa-02__row">Sable · 168 sessions</div>
          <div class="sa-02__row">Talon · 141 sessions</div>
          <div class="sa-02__row">Fern · 133 sessions</div>
          <div class="sa-02__row">Meridian · 97 sessions</div>
          <div class="sa-02__row">Orbit · 84 sessions</div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-02 {
  --page: #f2effa;
  --surface: #f7f5fd;
  --ink: #1d1533;
  --muted: #5f5484;
  --rule: #ded7f2;
  --accent: #d726a4;
  --accent2: #6d40e0;
  --page: oklch(95% 0.018 300);
  --surface: oklch(97% 0.012 300);
  --ink: oklch(23% 0.05 300);
  --muted: oklch(48% 0.06 300);
  --rule: oklch(88% 0.025 300);
  --accent: oklch(58% 0.24 340);
  --accent2: oklch(52% 0.2 295);
  --font-display: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
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

.sa-02 *,
.sa-02 *::before,
.sa-02 *::after {
  box-sizing: border-box;
}

.sa-02__stage {
  max-inline-size: 58rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.sa-02__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-02__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-02__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

.sa-02__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-02__layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.35fr);
  gap: 1.25rem;
  align-items: start;
}

.sa-02__dial {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  padding: 1.25rem;
  border-radius: 1.25rem;
  background: var(--surface);
  box-shadow: 0.5rem 0.5rem 1rem color-mix(in srgb, var(--accent2) 22%, transparent), -0.375rem -0.375rem 0.875rem color-mix(in srgb, #ffffff 85%, transparent);
  min-inline-size: 0;
}

.sa-02__dlabel {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-02__dvalue {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(2.25rem, 8vw, 3.25rem);
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.05em;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.sa-02__gauge {
  block-size: 0.75rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--ink) 8%, transparent);
  box-shadow: inset 0.125rem 0.125rem 0.375rem color-mix(in srgb, var(--accent2) 25%, transparent);
  overflow: hidden;
}

.sa-02__gfill {
  display: block;
  block-size: 100%;
  inline-size: 0%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent2), var(--accent));
  transition: inline-size 120ms linear;
}

.sa-02__dfired {
  margin: 0;
  font-size: 0.75rem;
  color: var(--muted);
}

.sa-02__dfnum {
  font-family: ui-monospace, Menlo, monospace;
  font-weight: 700;
  color: var(--ink);
}

.sa-02__opts {
  margin: 0.25rem 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

.sa-02__opt {
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
}

.sa-02__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
  color: var(--accent2);
  font-weight: 600;
}

.sa-02__scroller {
  block-size: 56vh;
  min-block-size: 19rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 1.25rem;
  background: var(--surface);
  box-shadow: inset 0.25rem 0.25rem 0.75rem color-mix(in srgb, var(--accent2) 18%, transparent);
}

.sa-02__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-02__pad {
  min-block-size: calc(100% + 6rem);
  padding: 1rem 1.125rem 4rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sa-02__hint {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-02__row {
  padding: 1rem 1.125rem;
  border-radius: 0.875rem;
  background: color-mix(in srgb, var(--ink) 4%, transparent);
  font-size: 0.875rem;
  min-inline-size: 0;
}

.sa-02__row--target {
  min-block-size: 7rem;
  display: flex;
  align-items: center;
  border: 2px solid var(--accent);
  background: color-mix(in srgb, var(--accent) 10%, transparent);
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .sa-02__gfill {
    transition: none;
  }
}

.sa-02__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.25rem;
  border: 0;
  border-radius: 999px;
  background: var(--surface);
  box-shadow: 0.25rem 0.25rem 0.625rem color-mix(in srgb, var(--accent2) 20%, transparent);
}

.sa-02__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-02__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-02__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.75rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-02__themeinput:checked + .sa-02__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-02__themeinput:focus-visible + .sa-02__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-02__layout {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-02 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-02__row--target {
    border: 2px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-02:not(:has(#sa-02-theme-light:checked)) {
    --page: #100b1c;
    --surface: #181128;
    --ink: #ece6fb;
    --muted: #a294c9;
    --rule: #2a1f45;
    --accent: #ff5cc8;
    --accent2: #9d7bff;
  }

  .sa-02:not(:has(#sa-02-theme-light:checked)) .sa-02__dial,
    .sa-02:not(:has(#sa-02-theme-light:checked)) .sa-02__theme {
    box-shadow: 0.375rem 0.375rem 0.875rem #0a0713, -0.25rem -0.25rem 0.75rem color-mix(in srgb, var(--accent2) 18%, transparent);
  }

  .sa-02:not(:has(#sa-02-theme-light:checked)) .sa-02__themeinput:checked + .sa-02__themeopt {
    color: #100b1c;
  }
}

@media (prefers-color-scheme: light) {
  .sa-02:has(#sa-02-theme-dark:checked) {
    --page: #100b1c;
    --surface: #181128;
    --ink: #ece6fb;
    --muted: #a294c9;
    --rule: #2a1f45;
    --accent: #ff5cc8;
    --accent2: #9d7bff;
  }

  .sa-02:has(#sa-02-theme-dark:checked) .sa-02__dial {
    box-shadow: 0.375rem 0.375rem 0.875rem #0a0713, -0.25rem -0.25rem 0.75rem color-mix(in srgb, var(--accent2) 18%, transparent);
  }

  .sa-02:has(#sa-02-theme-dark:checked) .sa-02__themeinput:checked + .sa-02__themeopt {
    color: #100b1c;
  }
}

[data-theme="dark"] .sa-02:not(:has(#sa-02-theme-light:checked)) {
  --page: #100b1c;
  --surface: #181128;
  --ink: #ece6fb;
  --muted: #a294c9;
  --rule: #2a1f45;
  --accent: #ff5cc8;
  --accent2: #9d7bff;
}

.sa-02:has(#sa-02-theme-dark:checked) {
  --page: #100b1c;
  --surface: #181128;
  --ink: #ece6fb;
  --muted: #a294c9;
  --rule: #2a1f45;
  --accent: #ff5cc8;
  --accent2: #9d7bff;
}

.sa-02:has(#sa-02-theme-dark:checked) .sa-02__dial {
  box-shadow: 0.375rem 0.375rem 0.875rem #0a0713, -0.25rem -0.25rem 0.75rem color-mix(in srgb, var(--accent2) 18%, transparent);
}

.sa-02:has(#sa-02-theme-dark:checked) .sa-02__themeinput:checked + .sa-02__themeopt {
  color: #100b1c;
}

.sa-02:has(#sa-02-theme-light:checked) {
  --page: #f2effa;
  --surface: #f7f5fd;
  --ink: #1d1533;
  --muted: #5f5484;
  --rule: #ded7f2;
  --accent: #d726a4;
  --accent2: #6d40e0;
}
```

## JavaScript
```js
const root = document.querySelector('.sa-02');
const scroller = document.getElementById('sa-02-scroller');
const target = document.getElementById('sa-02-target');
const ratioOut = document.getElementById('sa-02-ratio');
const firedOut = document.getElementById('sa-02-threshold');
const fill = document.getElementById('sa-02-fill');
const steps = [0, 0.25, 0.5, 0.75, 1];
const io = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    const ratio = Math.max(0, Math.min(1, entry.intersectionRatio));
    ratioOut.textContent = ratio.toFixed(2);
    fill.style.inlineSize = (ratio * 100).toFixed(1) + '%';
    const nearest = steps.reduce((a, b) => Math.abs(b - ratio) < Math.abs(a - ratio) ? b : a);
    firedOut.textContent = nearest.toFixed(2) + (entry.isIntersecting ? ' · intersecting' : ' · out');
  }
}, { root: scroller, rootMargin: '0px 0px -25% 0px', threshold: steps });
io.observe(target);
root.saCleanup = () => io.disconnect();
```
