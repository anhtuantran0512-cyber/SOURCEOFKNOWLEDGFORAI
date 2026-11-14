---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/glassmorphism-hover-transition/"
title: "Backdrop Filter Transitions and Their Cost"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "Transitioning backdrop-filter: blur() forces everything behind the element to be re-composited on every frame, which makes it one of the most expensive…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backdrop Filter Transitions and Their Cost
Source: https://codefronts.com/motion/css-transition-designs/glassmorphism-hover-transition/

Transitioning backdrop-filter: blur() forces everything behind the element to be re-composited on every frame, which makes it one of the most expensive transitions available. Both approaches are shown and labelled: the correct blur transition, and the cheaper alternative that cross-fades a pre-blurred layer instead. Ships -webkit-backdrop-filter alongside, and shows the transformed-ancestor trap.
## HTML
```html
<section class="trn-17" aria-labelledby="trn-17-heading">
  <div class="trn-17__stage">
    <div class="trn-17__theme">
      <input class="trn-17__themecb" type="checkbox" id="trn-17-theme">
      <label class="trn-17__themebtn" for="trn-17-theme">
        <span class="trn-17__themeico" aria-hidden="true">
          <svg class="trn-17__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-17__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <div class="trn-17__scenery" aria-hidden="true">
      <span class="trn-17__blob trn-17__blob--a"></span>
      <span class="trn-17__blob trn-17__blob--b"></span>
      <span class="trn-17__type">Nova &middot; observability &middot; 2,481 series &middot; p99 184ms &middot; Nova &middot; observability</span>
    </div>

    <header class="trn-17__head">
      <p class="trn-17__kicker">backdrop-filter</p>
      <h2 class="trn-17__heading" id="trn-17-heading">The most expensive frame you can ask for</h2>
      <p class="trn-17__sub">Hover each panel. Both look like glass. Only one recomputes the backdrop sixty times a second.</p>
    </header>

    <div class="trn-17__row">
      <article class="trn-17__panel trn-17__panel--blur">
        <p class="trn-17__label trn-17__label--cost">Transitions blur() — re-composites the backdrop each frame</p>
        <p class="trn-17__pbody">Every frame snapshots what is behind the panel, blurs it, and composites the result. Correct, and the priciest option on the list.</p>
        <code class="trn-17__code">transition: backdrop-filter 420ms ease;</code>
      </article>

      <article class="trn-17__panel trn-17__panel--fade">
        <span class="trn-17__pre" aria-hidden="true"></span>
        <p class="trn-17__label trn-17__label--cheap">Fades a pre-blurred layer — one composite, cached blur</p>
        <p class="trn-17__pbody">The blur is computed once and never changes. Only opacity moves, which is the cheapest work the compositor does.</p>
        <code class="trn-17__code">transition: opacity 420ms ease;</code>
      </article>

      <article class="trn-17__panel trn-17__panel--trap">
        <p class="trn-17__label trn-17__label--trap">Transformed ancestor — the effect vanishes</p>
        <p class="trn-17__pbody">This panel's wrapper carries <code>transform: rotate(.001deg)</code>. The declaration is identical to the first panel and the blur never appears.</p>
        <code class="trn-17__code">backdrop-filter: blur(14px); /* no backdrop to read */</code>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  --page: #071b2c;
  --page: oklch(0.22 0.05 240);
  --ink: #eaf6ff;
  --ink: oklch(0.96 0.014 230);
  --muted: #9fc0d8;
  --muted: oklch(0.78 0.035 230);
  --glass: rgba(255, 255, 255, 0.1);
  --edge: rgba(255, 255, 255, 0.22);
  --cyan: #45e0f0;
  --cyan: oklch(0.86 0.12 200);
  --cheap: #8ce6b0;
  --cheap: oklch(0.86 0.12 155);
  --trap: #ff9b8a;
  --trap: oklch(0.78 0.13 35);
  --blur: 14px;
  --font-display: "Varela Round", ui-rounded, "SF Pro Rounded", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  overflow: hidden;
}

.trn-17 *,
.trn-17 *::before,
.trn-17 *::after {
  box-sizing: border-box;
}

.trn-17__stage {
  position: relative;
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 6vw, 64px) 16px;
}

.trn-17__scenery {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.trn-17__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
}

.trn-17__blob--a {
  inline-size: 46vmin;
  block-size: 46vmin;
  inset-block-start: -8vmin;
  inset-inline-start: -6vmin;
  background: radial-gradient(circle, #2bd6e8 0%, rgba(43, 214, 232, 0) 70%);
}

.trn-17__blob--b {
  inline-size: 52vmin;
  block-size: 52vmin;
  inset-block-end: -14vmin;
  inset-inline-end: -10vmin;
  background: radial-gradient(circle, #7a5cff 0%, rgba(122, 92, 255, 0) 70%);
}

.trn-17__type {
  position: absolute;
  inset-block-start: 42%;
  inset-inline: -10%;
  font: 700 clamp(28px, 7vw, 62px)/1 var(--font-display);
  letter-spacing: -0.02em;
  color: rgba(255, 255, 255, 0.08);
  white-space: nowrap;
}

.trn-17__head {
  position: relative;
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 26px;
}

.trn-17__kicker {
  margin: 0 0 12px;
  font: 600 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  color: var(--cyan);
}

.trn-17__heading {
  margin: 0 0 10px;
  font: 700 clamp(25px, 4.8vw, 38px)/1.1 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-17__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-17__row {
  position: relative;
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 16px;
}

.trn-17__panel {
  position: relative;
  min-inline-size: 0;
  padding: 18px;
  border: 1px solid var(--edge);
  border-radius: 18px;
  background: var(--glass);
  overflow: hidden;
}

.trn-17__label {
  position: relative;
  margin: 0 0 12px;
  font: 700 12px/1.45 var(--font-display);
}

.trn-17__label--cost {
  color: var(--cyan);
}

.trn-17__label--cheap {
  color: var(--cheap);
}

.trn-17__label--trap {
  color: var(--trap);
}

.trn-17__pbody {
  position: relative;
  margin: 0 0 14px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-17__pbody code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.trn-17__code {
  position: relative;
  display: block;
  padding: 8px 10px;
  background: rgba(0, 0, 0, 0.24);
  border-radius: 8px;
  font: 400 11px/1.5 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .trn-17__panel--blur {
    -webkit-backdrop-filter: blur(0px) saturate(1);
    backdrop-filter: blur(0px) saturate(1);
    transition: -webkit-backdrop-filter 420ms ease, backdrop-filter 420ms ease, border-color 420ms ease;
  }

  .trn-17__panel--blur:hover {
    -webkit-backdrop-filter: blur(var(--blur)) saturate(1.4);
    backdrop-filter: blur(var(--blur)) saturate(1.4);
    border-color: var(--cyan);
  }

  .trn-17__pre {
    position: absolute;
    inset: 0;
    opacity: 0;
    -webkit-backdrop-filter: blur(var(--blur)) saturate(1.4);
    backdrop-filter: blur(var(--blur)) saturate(1.4);
    transition: opacity 420ms ease;
  }

  .trn-17__panel--fade:hover .trn-17__pre {
    opacity: 1;
  }

  .trn-17__panel--fade {
    transition: border-color 420ms ease;
  }

  .trn-17__panel--fade:hover {
    border-color: var(--cheap);
  }

  .trn-17__panel--trap {
    transform: rotate(0.001deg);
    -webkit-backdrop-filter: blur(var(--blur));
    backdrop-filter: blur(var(--blur));
    transition: border-color 420ms ease;
  }

  .trn-17__panel--trap:hover {
    border-color: var(--trap);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .trn-17__panel {
    background: rgba(7, 27, 44, 0.82);
    transition: background-color 420ms ease, border-color 420ms ease;
  }

  .trn-17__panel:hover {
    background: rgba(7, 27, 44, 0.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .trn-17__panel--blur {
    transition: border-color 160ms ease;
  }

  .trn-17__pre {
    transition: opacity 160ms ease;
  }
}

@media (prefers-color-scheme: light) {
  .trn-17 {
    --page: #eef6fb;
    --ink: #08243a;
    --muted: #3f6580;
    --glass: rgba(255, 255, 255, 0.5);
    --edge: rgba(8, 36, 58, 0.12);
    --cyan: #067b8c;
    --cheap: #1c7a4e;
    --trap: #ba4a30;
  }

  .trn-17__type {
    color: rgba(8, 36, 58, 0.07);
  }

  .trn-17__code {
    background: rgba(8, 36, 58, 0.06);
  }

  @supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    .trn-17__panel {
      background: rgba(255, 255, 255, 0.88);
    }

    .trn-17__panel:hover {
      background: #ffffff;
    }
  }
}

[data-theme="dark"] .trn-17 {
  --page: #071b2c;
  --ink: #eaf6ff;
  --muted: #9fc0d8;
  --glass: rgba(255, 255, 255, 0.1);
  --edge: rgba(255, 255, 255, 0.22);
  --cyan: #45e0f0;
  --cheap: #8ce6b0;
  --trap: #ff9b8a;
}

[data-theme="dark"] .trn-17__type {
  color: rgba(255, 255, 255, 0.08);
}

[data-theme="dark"] .trn-17__code {
  background: rgba(0, 0, 0, 0.24);
}

.trn-17__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-17__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-17__themebtn {
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

.trn-17__themebtn:hover {
  color: var(--ink);
}

.trn-17__themecb:focus-visible + .trn-17__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-17__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-17__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-17__sun {
  opacity: 0.34;
}

.trn-17__moon {
  opacity: 1;
}

.trn-17:has(#trn-17-theme:checked) .trn-17__sun {
  opacity: 1;
}

.trn-17:has(#trn-17-theme:checked) .trn-17__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-17:has(#trn-17-theme:checked) {
    --page: #eef6fb;
    --ink: #08243a;
    --muted: #3f6580;
    --glass: rgba(255, 255, 255, 0.5);
    --edge: rgba(8, 36, 58, 0.12);
    --cyan: #067b8c;
    --cheap: #1c7a4e;
    --trap: #ba4a30;
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__type {
    color: rgba(8, 36, 58, 0.07);
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__code {
    background: rgba(8, 36, 58, 0.06);
  }
}

@media (prefers-color-scheme: light) {
  .trn-17:has(#trn-17-theme:checked) {
    --page: #071b2c;
    --page: oklch(0.22 0.05 240);
    --ink: #eaf6ff;
    --ink: oklch(0.96 0.014 230);
    --muted: #9fc0d8;
    --muted: oklch(0.78 0.035 230);
    --glass: rgba(255, 255, 255, 0.1);
    --edge: rgba(255, 255, 255, 0.22);
    --cyan: #45e0f0;
    --cyan: oklch(0.86 0.12 200);
    --cheap: #8ce6b0;
    --cheap: oklch(0.86 0.12 155);
    --trap: #ff9b8a;
    --trap: oklch(0.78 0.13 35);
    --blur: 14px;
    --font-display: "Varela Round", ui-rounded, "SF Pro Rounded", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__type {
    position: absolute;
    inset-block-start: 42%;
    inset-inline: -10%;
    font: 700 clamp(28px, 7vw, 62px)/1 var(--font-display);
    letter-spacing: -0.02em;
    color: rgba(255, 255, 255, 0.08);
    white-space: nowrap;
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__code {
    position: relative;
    display: block;
    padding: 8px 10px;
    background: rgba(0, 0, 0, 0.24);
    border-radius: 8px;
    font: 400 11px/1.5 ui-monospace, Menlo, monospace;
    color: var(--ink);
    overflow-wrap: anywhere;
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__sun {
    opacity: 0.34;
  }

  .trn-17:has(#trn-17-theme:checked) .trn-17__moon {
    opacity: 1;
  }
}
```
