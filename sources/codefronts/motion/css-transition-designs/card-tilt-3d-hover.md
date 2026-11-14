---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/card-tilt-3d-hover/"
title: "Has Selector Driven Sibling Transitions"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: ":has() lets a state on one element drive a transition on a sibling or an ancestor, which used to require JavaScript for no reason other than selector direction."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Has Selector Driven Sibling Transitions
Source: https://codefronts.com/motion/css-transition-designs/card-tilt-3d-hover/

:has() lets a state on one element drive a transition on a sibling or an ancestor, which used to require JavaScript for no reason other than selector direction. Here a field's validity transitions the styling of the summary row beside it. Includes the specificity surprise: :has() takes the specificity of its most specific argument, so it can quietly outrank the rule you expected to win.
## HTML
```html
<section class="trn-16" aria-labelledby="trn-16-heading">
  <div class="trn-16__stage">
    <div class="trn-16__theme">
      <input class="trn-16__themecb" type="checkbox" id="trn-16-theme">
      <label class="trn-16__themebtn" for="trn-16-theme">
        <span class="trn-16__themeico" aria-hidden="true">
          <svg class="trn-16__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-16__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-16__head">
      <p class="trn-16__kicker">:has()</p>
      <h2 class="trn-16__heading" id="trn-16-heading">A field's state, styling its neighbour</h2>
      <p class="trn-16__sub">Type a short value and Tab out. The summary row above the field reacts — no script, no class.</p>
    </header>

    <fieldset class="trn-16__card">
      <legend class="trn-16__legend">Transfer to Fern Holdings</legend>

      <div class="trn-16__group">
        <div class="trn-16__summary">
          <span class="trn-16__sicon" aria-hidden="true">
            <svg class="trn-16__ok" viewBox="0 0 20 20" width="16" height="16"><path d="m4.8 10.4 3.2 3.2 7.2-7.4" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
            <svg class="trn-16__no" viewBox="0 0 20 20" width="16" height="16"><path d="M10 3.4 18 16.6H2L10 3.4Z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 8v3.6M10 13.4v1" stroke="currentColor" stroke-width="1.7"/></svg>
          </span>
          <span class="trn-16__stext">Reference looks valid</span>
          <span class="trn-16__samount">GBP 4,820.00</span>
        </div>

        <label class="trn-16__label" for="trn-16-ref">Payment reference</label>
        <input class="trn-16__field" id="trn-16-ref" type="text" required minlength="6" placeholder="INV-40921" aria-describedby="trn-16-help">
        <p class="trn-16__help" id="trn-16-help">Six characters or more. Validity is checked after you leave the field.</p>
      </div>

      <code class="trn-16__code">.trn-16__group:has(.trn-16__field:user-invalid) .trn-16__summary { … }</code>
    </fieldset>

    <p class="trn-16__foot">The summary sits <em>before</em> the field in the DOM. No sibling combinator can reach backwards — <code>:has()</code> on their shared parent can.</p>
  </div>
</section>
```
## CSS
```css
.trn-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f6f8f7;
  --page: oklch(0.97 0.005 165);
  --card: #ffffff;
  --ink: #17211d;
  --ink: oklch(0.24 0.014 165);
  --muted: #5c6a64;
  --muted: oklch(0.51 0.014 165);
  --rule: #dde4e0;
  --rule: oklch(0.9 0.008 165);
  --mint: #10a37f;
  --mint: oklch(0.62 0.11 168);
  --flag: #b4483a;
  --flag: oklch(0.52 0.15 30);
  --font-display: "Lucida Grande", "Trebuchet MS", "Segoe UI", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-16 *,
.trn-16 *::before,
.trn-16 *::after {
  box-sizing: border-box;
}

.trn-16__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 60px) 16px;
}

.trn-16__head {
  inline-size: 100%;
  max-inline-size: 46rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.trn-16__kicker {
  margin: 0 0 10px;
  font: 500 12px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  color: var(--mint);
}

.trn-16__heading {
  margin: 0 0 10px;
  font: 600 clamp(24px, 4.4vw, 34px)/1.14 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-16__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-16__card {
  inline-size: 100%;
  max-inline-size: 46rem;
  min-inline-size: 0;
  margin: 0;
  padding: 20px;
  background: var(--card);
  border: 0;
  border-block-start: 2px solid var(--ink);
}

.trn-16__legend {
  padding: 0;
  font: 600 12px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-16__group {
  display: grid;
  gap: 10px;
  margin-block-start: 18px;
}

.trn-16__summary {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
  align-items: center;
  min-inline-size: 0;
  padding: 14px 0;
  border-block: 1px solid var(--rule);
  color: var(--muted);
  transition: color 300ms ease, border-color 300ms ease, padding-inline-start 300ms ease;
}

.trn-16__sicon {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 18px;
  block-size: 18px;
  color: var(--mint);
}

.trn-16__ok,
.trn-16__no {
  grid-area: 1 / 1;
  transition: opacity 260ms ease;
}

.trn-16__no {
  opacity: 0;
}

.trn-16__stext {
  font: 600 13.5px/1.3 var(--font-display);
  color: var(--ink);
}

.trn-16__samount {
  margin-inline-start: auto;
  font: 400 13px/1 ui-monospace, Menlo, monospace;
}

.trn-16__label {
  font: 600 12px/1 var(--font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-16__field {
  min-height: 44px;
  padding: 0 12px;
  background: var(--page);
  border: 1px solid var(--rule);
  border-radius: 4px;
  font: 400 14px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
  transition: border-color 260ms ease, background-color 260ms ease;
}

.trn-16__field:focus-visible {
  outline: 2px solid var(--mint);
  outline-offset: 2px;
  background: var(--card);
}

.trn-16__help {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--muted);
}

@supports selector(:has(*)) {
  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__summary {
    color: var(--flag);
    border-color: var(--flag);
    padding-inline-start: 10px;
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__sicon {
    color: var(--flag);
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__ok {
    opacity: 0;
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__no {
    opacity: 1;
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__stext {
    color: var(--flag);
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__stext::after {
    content: " — six characters minimum";
    font-weight: 400;
  }

  .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__field {
    border-color: var(--flag);
  }
}

.trn-16__code {
  display: block;
  margin-block-start: 18px;
  padding: 10px 12px;
  background: var(--page);
  border-inline-start: 2px solid var(--mint);
  font: 400 11.5px/1.55 ui-monospace, Menlo, monospace;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.trn-16__foot {
  inline-size: 100%;
  max-inline-size: 46rem;
  margin: 18px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.trn-16__foot code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .trn-16__summary {
    transition: color 150ms ease, border-color 150ms ease;
  }

  @supports selector(:has(*)) {
    .trn-16__group:has(.trn-16__field:user-invalid) .trn-16__summary {
      padding-inline-start: 0;
    }
  }
}

@media (prefers-color-scheme: dark) {
  .trn-16 {
    --page: #0f1412;
    --page: oklch(0.19 0.008 165);
    --card: #161d1a;
    --card: oklch(0.23 0.01 165);
    --ink: #e9f0ec;
    --ink: oklch(0.95 0.01 165);
    --muted: #93a29b;
    --muted: oklch(0.71 0.014 165);
    --rule: #26302c;
    --rule: oklch(0.3 0.012 165);
    --mint: #48d3ac;
    --mint: oklch(0.8 0.12 168);
    --flag: #ff8c7a;
    --flag: oklch(0.76 0.14 32);
  }

  .trn-16__card {
    border-block-start-color: var(--mint);
  }
}

[data-theme="dark"] .trn-16 {
  --page: #0f1412;
  --card: #161d1a;
  --ink: #e9f0ec;
  --muted: #93a29b;
  --rule: #26302c;
  --mint: #48d3ac;
  --flag: #ff8c7a;
}

[data-theme="dark"] .trn-16__card {
  border-block-start-color: var(--mint);
}

.trn-16__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-16__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-16__themebtn {
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

.trn-16__themebtn:hover {
  color: var(--ink);
}

.trn-16__themecb:focus-visible + .trn-16__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-16__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-16__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-16__sun {
  opacity: 1;
}

.trn-16__moon {
  opacity: 0.34;
}

.trn-16:has(#trn-16-theme:checked) .trn-16__sun {
  opacity: 0.34;
}

.trn-16:has(#trn-16-theme:checked) .trn-16__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-16:has(#trn-16-theme:checked) {
    --page: #0f1412;
    --page: oklch(0.19 0.008 165);
    --card: #161d1a;
    --card: oklch(0.23 0.01 165);
    --ink: #e9f0ec;
    --ink: oklch(0.95 0.01 165);
    --muted: #93a29b;
    --muted: oklch(0.71 0.014 165);
    --rule: #26302c;
    --rule: oklch(0.3 0.012 165);
    --mint: #48d3ac;
    --mint: oklch(0.8 0.12 168);
    --flag: #ff8c7a;
    --flag: oklch(0.76 0.14 32);
  }

  .trn-16:has(#trn-16-theme:checked) .trn-16__card {
    border-block-start-color: var(--mint);
  }
}

@media (prefers-color-scheme: dark) {
  .trn-16:has(#trn-16-theme:checked) {
    --page: #f6f8f7;
    --page: oklch(0.97 0.005 165);
    --card: #ffffff;
    --ink: #17211d;
    --ink: oklch(0.24 0.014 165);
    --muted: #5c6a64;
    --muted: oklch(0.51 0.014 165);
    --rule: #dde4e0;
    --rule: oklch(0.9 0.008 165);
    --mint: #10a37f;
    --mint: oklch(0.62 0.11 168);
    --flag: #b4483a;
    --flag: oklch(0.52 0.15 30);
    --font-display: "Lucida Grande", "Trebuchet MS", "Segoe UI", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-16:has(#trn-16-theme:checked) .trn-16__card {
    inline-size: 100%;
    max-inline-size: 46rem;
    min-inline-size: 0;
    margin: 0;
    padding: 20px;
    background: var(--card);
    border: 0;
    border-block-start: 2px solid var(--ink);
  }

  .trn-16:has(#trn-16-theme:checked) .trn-16__sun {
    opacity: 1;
  }

  .trn-16:has(#trn-16-theme:checked) .trn-16__moon {
    opacity: 0.34;
  }
}
```
