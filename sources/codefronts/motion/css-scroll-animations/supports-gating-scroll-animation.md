---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/supports-gating-scroll-animation/"
title: "Progressive Enhancement with Supports Gating"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "How to ship a scroll animation while a major engine has not implemented it: make the static layout complete and correct on its own, then layer motion on top…"
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Progressive Enhancement with Supports Gating
Source: https://codefronts.com/motion/css-scroll-animations/supports-gating-scroll-animation/

How to ship a scroll animation while a major engine has not implemented it: make the static layout complete and correct on its own, then layer motion on top inside @supports (animation-timeline: scroll()). The ordering rule is the whole lesson — the base must be the finished state, never the start state.
## HTML
```html
<section class="sa-07" aria-labelledby="sa-07-h">
  <fieldset class="sa-07__theme">
    <legend class="sa-07__themelegend">Theme</legend>
    <input class="sa-07__themeinput" type="radio" name="sa-07-theme" id="sa-07-theme-auto" checked>
    <label class="sa-07__themeopt" for="sa-07-theme-auto">Auto</label>
    <input class="sa-07__themeinput" type="radio" name="sa-07-theme" id="sa-07-theme-light">
    <label class="sa-07__themeopt" for="sa-07-theme-light">Light</label>
    <input class="sa-07__themeinput" type="radio" name="sa-07-theme" id="sa-07-theme-dark">
    <label class="sa-07__themeopt" for="sa-07-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-07__stage">
    <header class="sa-07__head">
      <p class="sa-07__eyebrow">@supports gating</p>
      <h2 class="sa-07__h" id="sa-07-h">Which layer holds the start state</h2>
      <p class="sa-07__sub">Both columns animate identically where scroll timelines exist. Only one of them is still a usable page where they do not.</p>
    </header>

    <div class="sa-07__pair">
      <article class="sa-07__col">
        <p class="sa-07__ctag sa-07__ctag--good">Correct gate — base is the finished state</p>
        <pre class="sa-07__code">.card { opacity: 1; transform: none }

@supports (animation-timeline: scroll()) {
  .card { opacity: 0; animation: rise linear both;
          animation-timeline: view() }
}</pre>
        <div class="sa-07__scroller" tabindex="0" role="region" aria-label="Correctly gated column, scrollable">
          <div class="sa-07__set">
            <div class="sa-07__card sa-07__card--good">Provision the edge cache</div>
            <div class="sa-07__card sa-07__card--good">Attach the replica</div>
            <div class="sa-07__card sa-07__card--good">Run the smoke suite</div>
            <div class="sa-07__card sa-07__card--good">Deploy to production</div>
            <div class="sa-07__card sa-07__card--good">Watch the error budget</div>
            <div class="sa-07__card sa-07__card--good">Promote the canary</div>
            <div class="sa-07__card sa-07__card--good">Close the change ticket</div>
            <div class="sa-07__card sa-07__card--good">Update the status page</div>
            <div class="sa-07__card sa-07__card--good">Hand over the runbook</div>
            <div class="sa-07__card sa-07__card--good">Archive the branch</div>
          </div>
        </div>
        <p class="sa-07__verdict sa-07__verdict--good">No support: a complete, readable checklist. With support: the same checklist, scrubbed in.</p>
      </article>

      <article class="sa-07__col">
        <p class="sa-07__ctag sa-07__ctag--bad">Broken gate — base is the start state</p>
        <pre class="sa-07__code">.card { opacity: 0 }

@supports (animation-timeline: scroll()) {
  .card { animation: rise linear both;
          animation-timeline: view() }
}</pre>
        <div class="sa-07__scroller" tabindex="0" role="region" aria-label="Broken gate column, scrollable">
          <div class="sa-07__set">
            <div class="sa-07__card sa-07__card--bad">Provision the edge cache</div>
            <div class="sa-07__card sa-07__card--bad">Attach the replica</div>
            <div class="sa-07__card sa-07__card--bad">Run the smoke suite</div>
            <div class="sa-07__card sa-07__card--bad">Deploy to production</div>
            <div class="sa-07__card sa-07__card--bad">Watch the error budget</div>
            <div class="sa-07__card sa-07__card--bad">Promote the canary</div>
            <div class="sa-07__card sa-07__card--bad">Close the change ticket</div>
            <div class="sa-07__card sa-07__card--bad">Update the status page</div>
            <div class="sa-07__card sa-07__card--bad">Hand over the runbook</div>
            <div class="sa-07__card sa-07__card--bad">Archive the branch</div>
          </div>
        </div>
        <p class="sa-07__verdict sa-07__verdict--bad">No support: four invisible rows and no error. With support: indistinguishable from the left.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-07 {
  --page: #0b1220;
  --surface: #121b2c;
  --ink: #e8eefa;
  --muted: #94a3bd;
  --rule: #22304a;
  --accent: #34d399;
  --bad: #f97362;
  --page: oklch(17% 0.03 258);
  --surface: oklch(22% 0.035 258);
  --ink: oklch(94% 0.012 250);
  --muted: oklch(70% 0.03 250);
  --rule: oklch(30% 0.035 255);
  --accent: oklch(78% 0.16 163);
  --bad: oklch(70% 0.16 30);
  --font-display: "Helvetica Neue", Helvetica, "Segoe UI", system-ui, sans-serif;
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

.sa-07 *,
.sa-07 *::before,
.sa-07 *::after {
  box-sizing: border-box;
}

.sa-07__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-07__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-07__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-07__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.1;
  text-transform: uppercase;
}

.sa-07__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-07__pair {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  align-items: start;
}

.sa-07__col {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: var(--surface);
  box-shadow: 0 0.5rem 1.5rem -0.75rem #00000080;
  min-inline-size: 0;
}

.sa-07__ctag {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.sa-07__ctag--good {
  color: var(--accent);
}

.sa-07__ctag--bad {
  color: var(--bad);
}

.sa-07__code {
  margin: 0;
  padding: 0.75rem;
  overflow-x: auto;
  border-radius: 0.5rem;
  background: color-mix(in srgb, var(--ink) 6%, transparent);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  line-height: 1.55;
  color: var(--ink);
}

.sa-07__scroller {
  block-size: 40vh;
  min-block-size: 14rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 0.5rem;
  background: color-mix(in srgb, var(--ink) 4%, transparent);
  scroll-timeline: --sa-07-track block;
}

.sa-07__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-07__set {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  min-block-size: calc(100% + 6rem);
  padding: 1rem 0.875rem 3rem;
}

.sa-07__card {
  padding: 0.9375rem 1rem;
  border-radius: 0.5rem;
  border-inline-start: 3px solid var(--accent);
  background: color-mix(in srgb, var(--ink) 7%, transparent);
  font-size: 0.875rem;
  font-weight: 600;
  min-inline-size: 0;
}

.sa-07__card--good {
  opacity: 1;
  transform: none;
}

.sa-07__card--bad {
  opacity: 0;
  border-inline-start-color: var(--bad);
}

.sa-07__verdict {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.55;
  text-wrap: pretty;
}

.sa-07__verdict--good {
  color: var(--accent);
}

.sa-07__verdict--bad {
  color: var(--bad);
}

@keyframes sa-07-rise {
  from {
    opacity: 0;
    transform: translateY(1.25rem);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@supports (animation-timeline: view()) {
  .sa-07__card--good {
    opacity: 0;
    animation: sa-07-rise linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 45%;
  }

  .sa-07__card--bad {
    animation: sa-07-rise linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 45%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-07__card--good {
    animation: none;
    opacity: 1;
    transform: none;
  }
}

.sa-07__theme {
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

.sa-07__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-07__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-07__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 0.375rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-07__themeinput:checked + .sa-07__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-07__themeinput:focus-visible + .sa-07__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-07__pair {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-07 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-07__card {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: light) {
  .sa-07:not(:has(#sa-07-theme-dark:checked)) {
    --page: #eef2f8;
    --surface: #ffffff;
    --ink: #101827;
    --muted: #576375;
    --rule: #d5dde9;
    --accent: #0f8a5f;
    --bad: #c4402f;
  }

  .sa-07:not(:has(#sa-07-theme-dark:checked)) .sa-07__themeinput:checked + .sa-07__themeopt {
    color: #ffffff;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-07:has(#sa-07-theme-light:checked) {
    --page: #eef2f8;
    --surface: #ffffff;
    --ink: #101827;
    --muted: #576375;
    --rule: #d5dde9;
    --accent: #0f8a5f;
    --bad: #c4402f;
  }

  .sa-07:has(#sa-07-theme-light:checked) .sa-07__themeinput:checked + .sa-07__themeopt {
    color: #ffffff;
  }
}

[data-theme="light"] .sa-07:not(:has(#sa-07-theme-dark:checked)) {
  --page: #eef2f8;
  --surface: #ffffff;
  --ink: #101827;
  --muted: #576375;
  --rule: #d5dde9;
  --accent: #0f8a5f;
  --bad: #c4402f;
}

.sa-07:has(#sa-07-theme-light:checked) {
  --page: #eef2f8;
  --surface: #ffffff;
  --ink: #101827;
  --muted: #576375;
  --rule: #d5dde9;
  --accent: #0f8a5f;
  --bad: #c4402f;
}

.sa-07:has(#sa-07-theme-light:checked) .sa-07__themeinput:checked + .sa-07__themeopt {
  color: #ffffff;
}

.sa-07:has(#sa-07-theme-dark:checked) {
  --page: #0b1220;
  --surface: #121b2c;
  --ink: #e8eefa;
  --muted: #94a3bd;
  --rule: #22304a;
  --accent: #34d399;
  --bad: #f97362;
}
```
