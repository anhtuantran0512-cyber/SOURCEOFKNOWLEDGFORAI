---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/background-color-transition/"
title: "Color and Gradient Transitions with Registered Properties"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "background-image is a discrete property, so a gradient cannot be interpolated — swapping one for another flips at the midpoint no matter what duration you…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color and Gradient Transitions with Registered Properties
Source: https://codefronts.com/motion/css-transition-designs/background-color-transition/

background-image is a discrete property, so a gradient cannot be interpolated — swapping one for another flips at the midpoint no matter what duration you write. The fix is to register the gradient's angle and its stop colours as typed @property custom properties and transition those instead. The naive attempt and the registered version sit side by side, both labelled.
## HTML
```html
<section class="trn-06" aria-labelledby="trn-06-heading">
  <div class="trn-06__stage">
    <div class="trn-06__theme">
      <input class="trn-06__themecb" type="checkbox" id="trn-06-theme">
      <label class="trn-06__themebtn" for="trn-06-theme">
        <span class="trn-06__themeico" aria-hidden="true">
          <svg class="trn-06__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-06__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-06__head">
      <p class="trn-06__kicker">@property &middot; gradient interpolation</p>
      <h2 class="trn-06__heading" id="trn-06-heading">A gradient cannot transition. Its inputs can.</h2>
      <p class="trn-06__sub">Hover or focus both cards. Same duration, same gradient — only one of them interpolates.</p>
    </header>

    <div class="trn-06__pair">
      <article class="trn-06__card trn-06__card--naive">
        <p class="trn-06__tag trn-06__tag--bad">Transitions background-image — flips at the midpoint</p>
        <div class="trn-06__swatch trn-06__swatch--naive" aria-hidden="true"></div>
        <code class="trn-06__code">transition: background-image 700ms ease;</code>
        <p class="trn-06__note">background-image is discrete. There is no defined blend between two gradients, so the engine swaps them at 50% of the duration.</p>
      </article>

      <article class="trn-06__card trn-06__card--typed">
        <p class="trn-06__tag trn-06__tag--good">Transitions registered --angle and --stop colours — true sweep</p>
        <div class="trn-06__swatch trn-06__swatch--typed" aria-hidden="true"></div>
        <code class="trn-06__code">transition: --trn-06-angle 700ms ease, --trn-06-c1 700ms ease, --trn-06-c2 700ms ease;</code>
        <p class="trn-06__note">The gradient is written once in terms of typed custom properties. Each frame re-resolves it from interpolated inputs.</p>
      </article>
    </div>

    <dl class="trn-06__spec">
      <dt>syntax</dt><dd>'&lt;angle&gt;' &nbsp;/&nbsp; '&lt;color&gt;'</dd>
      <dt>inherits</dt><dd>false — descendants should not recompute each frame</dd>
      <dt>initial-value</dt><dd>required, or the whole registration is dropped</dd>
    </dl>
  </div>
</section>
```
## CSS
```css
@property --trn-06-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 120deg;
}

@property --trn-06-c1 {
  syntax: '<color>';
  inherits: false;
  initial-value: #7b2dff;
}

@property --trn-06-c2 {
  syntax: '<color>';
  inherits: false;
  initial-value: #17d4e6;
}

.trn-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #0a0714;
  --page: oklch(0.16 0.05 300);
  --card: #130d24;
  --card: oklch(0.21 0.06 300);
  --ink: #f3ecff;
  --ink: oklch(0.96 0.02 300);
  --muted: #a394c6;
  --muted: oklch(0.72 0.05 300);
  --rule: #291d47;
  --rule: oklch(0.3 0.07 300);
  --violet: #8b3dff;
  --violet: oklch(0.6 0.25 300);
  --cyan: #17d4e6;
  --cyan: oklch(0.82 0.13 205);
  --bad: #ff5d8f;
  --bad: oklch(0.7 0.19 5);
  --font-display: "Nunito", "Quicksand", ui-rounded, "SF Pro Rounded", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-06 *,
.trn-06 *::before,
.trn-06 *::after {
  box-sizing: border-box;
}

.trn-06__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 6vw, 62px) 16px;
}

.trn-06__head {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 28px;
}

.trn-06__kicker {
  margin: 0 0 12px;
  font: 600 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.12em;
  color: var(--cyan);
}

.trn-06__heading {
  margin: 0 0 12px;
  font: 800 clamp(25px, 4.8vw, 38px)/1.12 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-06__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-06__pair {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 18px;
}

.trn-06__card {
  min-inline-size: 0;
  padding: 18px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 18px;
  transition: box-shadow 700ms ease, border-color 700ms ease;
}

.trn-06__card--naive:hover {
  border-color: var(--bad);
  box-shadow: 0 18px 44px -22px rgba(255, 93, 143, 0.6);
}

.trn-06__card--typed:hover {
  border-color: var(--cyan);
  box-shadow: 0 18px 50px -20px rgba(23, 212, 230, 0.55);
}

.trn-06__tag {
  margin: 0 0 14px;
  font: 700 12px/1.45 var(--font-display);
}

.trn-06__tag--bad {
  color: var(--bad);
}

.trn-06__tag--good {
  color: var(--cyan);
}

.trn-06__swatch {
  block-size: 148px;
  border-radius: 12px;
}

.trn-06__swatch--naive {
  background-image: linear-gradient(120deg, #7b2dff 0%, #17d4e6 100%);
  transition: background-image 700ms ease;
}

.trn-06__card--naive:hover .trn-06__swatch--naive {
  background-image: linear-gradient(300deg, #ff8a3d 0%, #ff2d70 100%);
}

.trn-06__swatch--typed {
  background-image: linear-gradient(var(--trn-06-angle), var(--trn-06-c1) 0%, var(--trn-06-c2) 100%);
  transition: --trn-06-angle 700ms ease, --trn-06-c1 700ms ease, --trn-06-c2 700ms ease;
}

.trn-06__card--typed:hover .trn-06__swatch--typed {
  --trn-06-angle: 300deg;
  --trn-06-c1: #ff8a3d;
  --trn-06-c2: #ff2d70;
}

.trn-06__code {
  display: block;
  margin-block-start: 14px;
  padding: 9px 10px;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 8px;
  font: 400 11px/1.55 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.trn-06__note {
  margin: 10px 0 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-06__spec {
  inline-size: 100%;
  max-inline-size: 58rem;
  margin: 26px 0 0;
  display: grid;
  grid-template-columns: minmax(0, 8rem) minmax(0, 1fr);
  gap: 0;
}

.trn-06__spec dt {
  padding: 10px 12px 10px 0;
  border-block-start: 1px solid var(--rule);
  font: 600 12px/1.4 ui-monospace, Menlo, monospace;
  color: var(--cyan);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.trn-06__spec dd {
  margin: 0;
  padding: 10px 0;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  line-height: 1.45;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .trn-06__swatch--typed {
    transition: --trn-06-c1 200ms ease, --trn-06-c2 200ms ease;
  }

  .trn-06__card--typed:hover .trn-06__swatch--typed {
    --trn-06-angle: 120deg;
  }

  .trn-06__card {
    transition: border-color 200ms ease;
    box-shadow: none;
  }

  .trn-06__card--naive:hover,
    .trn-06__card--typed:hover {
    box-shadow: none;
  }
}

@media (prefers-color-scheme: light) {
  .trn-06 {
    --page: #f7f4ff;
    --card: #ffffff;
    --ink: #180d2e;
    --muted: #5c4d80;
    --rule: #e2daf5;
    --violet: #6a1fe0;
    --cyan: #0e8fa0;
    --bad: #d01f52;
  }

  .trn-06__code {
    background: rgba(24, 13, 46, 0.05);
  }
}

[data-theme="dark"] .trn-06 {
  --page: #0a0714;
  --card: #130d24;
  --ink: #f3ecff;
  --muted: #a394c6;
  --rule: #291d47;
  --violet: #8b3dff;
  --cyan: #17d4e6;
  --bad: #ff5d8f;
}

[data-theme="dark"] .trn-06__code {
  background: rgba(255, 255, 255, 0.04);
}

.trn-06__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-06__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-06__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-06__themebtn:hover {
  color: var(--ink);
}

.trn-06__themecb:focus-visible + .trn-06__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-06__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-06__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-06__sun {
  opacity: 0.34;
}

.trn-06__moon {
  opacity: 1;
}

.trn-06:has(#trn-06-theme:checked) .trn-06__sun {
  opacity: 1;
}

.trn-06:has(#trn-06-theme:checked) .trn-06__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-06:has(#trn-06-theme:checked) {
    --page: #f7f4ff;
    --card: #ffffff;
    --ink: #180d2e;
    --muted: #5c4d80;
    --rule: #e2daf5;
    --violet: #6a1fe0;
    --cyan: #0e8fa0;
    --bad: #d01f52;
  }

  .trn-06:has(#trn-06-theme:checked) .trn-06__code {
    background: rgba(24, 13, 46, 0.05);
  }
}

@media (prefers-color-scheme: light) {
  .trn-06:has(#trn-06-theme:checked) {
    --page: #0a0714;
    --page: oklch(0.16 0.05 300);
    --card: #130d24;
    --card: oklch(0.21 0.06 300);
    --ink: #f3ecff;
    --ink: oklch(0.96 0.02 300);
    --muted: #a394c6;
    --muted: oklch(0.72 0.05 300);
    --rule: #291d47;
    --rule: oklch(0.3 0.07 300);
    --violet: #8b3dff;
    --violet: oklch(0.6 0.25 300);
    --cyan: #17d4e6;
    --cyan: oklch(0.82 0.13 205);
    --bad: #ff5d8f;
    --bad: oklch(0.7 0.19 5);
    --font-display: "Nunito", "Quicksand", ui-rounded, "SF Pro Rounded", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-06:has(#trn-06-theme:checked) .trn-06__code {
    display: block;
    margin-block-start: 14px;
    padding: 9px 10px;
    background: rgba(255, 255, 255, 0.04);
    border-radius: 8px;
    font: 400 11px/1.55 ui-monospace, Menlo, monospace;
    color: var(--ink);
    overflow-wrap: anywhere;
  }

  .trn-06:has(#trn-06-theme:checked) .trn-06__sun {
    opacity: 0.34;
  }

  .trn-06:has(#trn-06-theme:checked) .trn-06__moon {
    opacity: 1;
  }
}
```
