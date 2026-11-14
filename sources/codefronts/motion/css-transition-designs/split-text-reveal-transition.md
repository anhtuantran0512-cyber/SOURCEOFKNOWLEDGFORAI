---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/split-text-reveal-transition/"
title: "Discrete Property Transition Behaviour"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "Not every property interpolates."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Discrete Property Transition Behaviour
Source: https://codefronts.com/motion/css-transition-designs/split-text-reveal-transition/

Not every property interpolates. Discrete properties — display, visibility, content-visibility, overlay, flex-direction and others — have no midpoint, so by default they flip at 50% of the duration. This demo marks that midpoint on a timeline, shows the same property flipping at the end under transition-behavior: allow-discrete, and lists which properties behave this way.
## HTML
```html
<section class="trn-21" aria-labelledby="trn-21-heading">
  <div class="trn-21__stage">
    <div class="trn-21__theme">
      <input class="trn-21__themecb" type="checkbox" id="trn-21-theme">
      <label class="trn-21__themebtn" for="trn-21-theme">
        <span class="trn-21__themeico" aria-hidden="true">
          <svg class="trn-21__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-21__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-21__head">
      <p class="trn-21__kicker">discrete properties</p>
      <h2 class="trn-21__heading" id="trn-21-heading">Where the flip happens</h2>
      <p class="trn-21__sub">Same property, same duration, two flip points. Toggle and watch the marked timelines.</p>
    </header>

    <input class="trn-21__input" type="checkbox" id="trn-21-run" checked>
    <label class="trn-21__toggle" for="trn-21-run">Toggle both panels</label>

    <div class="trn-21__pair">
      <article class="trn-21__col">
        <h3 class="trn-21__label">transition-behavior: normal &mdash; flips at 50%</h3>
        <div class="trn-21__box"><span class="trn-21__thing trn-21__thing--mid">visible</span></div>
        <div class="trn-21__timeline"><span class="trn-21__flip trn-21__flip--mid">flip</span></div>
        <div class="trn-21__ticks"><span>0%</span><span>50%</span><span>100%</span></div>
        <p class="trn-21__note">The element is hidden from the midpoint on, so the second half of the fade is never seen.</p>
      </article>

      <article class="trn-21__col">
        <h3 class="trn-21__label">allow-discrete &mdash; flips at 100%</h3>
        <div class="trn-21__box"><span class="trn-21__thing trn-21__thing--end">visible</span></div>
        <div class="trn-21__timeline"><span class="trn-21__flip trn-21__flip--end">flip</span></div>
        <div class="trn-21__ticks"><span>0%</span><span>50%</span><span>100%</span></div>
        <p class="trn-21__note">The fade completes, then the property changes. Exit reads correctly; entry flips first instead.</p>
      </article>
    </div>

    <div class="trn-21__tablewrap">
    <table class="trn-21__table">
      <caption>Properties you will actually meet</caption>
      <thead><tr><th scope="col">Property</th><th scope="col">Interpolates</th><th scope="col">Default flip</th><th scope="col">With allow-discrete</th></tr></thead>
      <tbody>
        <tr><th scope="row">display</th><td>no</td><td>50%</td><td>end (out) / start (in)</td></tr>
        <tr><th scope="row">visibility</th><td>no</td><td>50%</td><td>end (out) / start (in)</td></tr>
        <tr><th scope="row">content-visibility</th><td>no</td><td>50%</td><td>end (out) / start (in)</td></tr>
        <tr><th scope="row">overlay</th><td>no</td><td>50%</td><td>end (out) / start (in)</td></tr>
        <tr><th scope="row">background-image</th><td>no</td><td>50%</td><td>unchanged &mdash; register the inputs instead</td></tr>
        <tr><th scope="row">opacity, transform</th><td>yes</td><td>&mdash;</td><td>not applicable</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-21 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #191a1c;
  --page: oklch(0.22 0.004 250);
  --card: #202225;
  --card: oklch(0.26 0.004 250);
  --ink: #ececee;
  --ink: oklch(0.94 0.002 250);
  --muted: #9b9da2;
  --muted: oklch(0.7 0.006 250);
  --rule: #2f3135;
  --rule: oklch(0.32 0.005 250);
  --line: #6f7379;
  --dur: 900ms;
  --font-display: ui-monospace, "IBM Plex Mono", "JetBrains Mono", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-21 *,
.trn-21 *::before,
.trn-21 *::after {
  box-sizing: border-box;
}

.trn-21__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  justify-items: center;
  align-items: start;
  max-inline-size: 100%;
  padding: clamp(20px, 4.5vw, 48px) 14px;
}

.trn-21__head {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  margin: 0 0 18px;
}

.trn-21__kicker {
  margin: 0 0 8px;
  font: 400 10.5px/1 var(--font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-21__heading {
  margin: 0 0 6px;
  font: 500 clamp(22px, 4.2vw, 31px)/1.1 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.trn-21__sub {
  margin: 0;
  max-inline-size: 54ch;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-21__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-21__toggle {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 14px;
  margin-block-end: 16px;
  border: 1px solid var(--rule);
  border-radius: 2px;
  cursor: pointer;
  font: 400 12px/1 var(--font-display);
  color: var(--ink);
  transition: border-color 160ms ease, background-color 160ms ease;
}

.trn-21__toggle:hover {
  border-color: var(--line);
  background: var(--card);
}

.trn-21__input:focus-visible + .trn-21__toggle {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-21__input:checked + .trn-21__toggle::after {
  content: " · on";
  color: var(--muted);
}

.trn-21__pair {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 12px;
}

.trn-21__col {
  min-inline-size: 0;
  padding: 12px;
  background: var(--card);
  border-block-start: 1px solid var(--line);
}

.trn-21__label {
  margin: 0 0 12px;
  font: 400 11px/1.4 var(--font-display);
  color: var(--ink);
}

.trn-21__box {
  display: grid;
  place-items: center;
  block-size: 74px;
  border: 1px dashed var(--rule);
}

.trn-21__thing {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  background: var(--page);
  border: 1px solid var(--line);
  font: 400 11.5px/1 var(--font-display);
  color: var(--ink);
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--dur) linear, visibility var(--dur) linear;
}

.trn-21:has(#trn-21-run:checked) .trn-21__thing {
  opacity: 1;
  visibility: visible;
}

.trn-21__thing--end {
  transition: opacity var(--dur) linear, visibility 0s linear var(--dur);
}

.trn-21:has(#trn-21-run:checked) .trn-21__thing--end {
  transition: opacity var(--dur) linear, visibility 0s linear 0s;
}

@supports (transition-behavior: allow-discrete) {
  .trn-21__thing--end {
    visibility: visible;
    display: none;
    transition: opacity var(--dur) linear, display var(--dur) allow-discrete;
  }

  .trn-21:has(#trn-21-run:checked) .trn-21__thing--end {
    display: inline-flex;
  }
}

.trn-21__timeline {
  position: relative;
  block-size: 22px;
  margin-block-start: 12px;
  border-block-end: 1px solid var(--rule);
}

.trn-21__flip {
  position: absolute;
  inset-block-end: -1px;
  padding-block-end: 3px;
  font: 400 10px/1 var(--font-display);
  color: var(--ink);
  border-inline-start: 1px solid var(--ink);
  padding-inline-start: 4px;
}

.trn-21__flip--mid {
  inset-inline-start: 50%;
}

.trn-21__flip--end {
  inset-inline-start: calc(100% - 26px);
}

.trn-21__ticks {
  display: flex;
  justify-content: space-between;
  margin-block-start: 5px;
  font: 400 9.5px/1 var(--font-display);
  color: var(--muted);
}

.trn-21__note {
  margin: 10px 0 0;
  font-size: 12px;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-21__tablewrap {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  margin: 18px 0 0;
  overflow-x: auto;
}

.trn-21__table {
  inline-size: 100%;
  min-inline-size: 20rem;
  border-collapse: collapse;
  font-size: 11.5px;
}

.trn-21__table caption {
  margin-block-end: 8px;
  text-align: start;
  font: 400 10px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-21__table th,
.trn-21__table td {
  padding: 7px 8px;
  text-align: start;
  border-block-end: 1px solid var(--rule);
  font-weight: 400;
  color: var(--muted);
}

.trn-21__table thead th {
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.trn-21__table tbody th {
  color: var(--ink);
  font-family: var(--font-display);
}

@media (prefers-reduced-motion: reduce) {
  .trn-21 {
    --dur: 260ms;
  }
}

@media (prefers-color-scheme: light) {
  .trn-21 {
    --page: #fbfbfc;
    --card: #ffffff;
    --ink: #1a1b1e;
    --muted: #61646b;
    --rule: #dfe1e5;
    --line: #9a9ea6;
  }
}

[data-theme="dark"] .trn-21 {
  --page: #191a1c;
  --card: #202225;
  --ink: #ececee;
  --muted: #9b9da2;
  --rule: #2f3135;
  --line: #6f7379;
}

.trn-21__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-21__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-21__themebtn {
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

.trn-21__themebtn:hover {
  color: var(--ink);
}

.trn-21__themecb:focus-visible + .trn-21__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-21__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-21__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-21__sun {
  opacity: 0.34;
}

.trn-21__moon {
  opacity: 1;
}

.trn-21:has(#trn-21-theme:checked) .trn-21__sun {
  opacity: 1;
}

.trn-21:has(#trn-21-theme:checked) .trn-21__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-21:has(#trn-21-theme:checked) {
    --page: #fbfbfc;
    --card: #ffffff;
    --ink: #1a1b1e;
    --muted: #61646b;
    --rule: #dfe1e5;
    --line: #9a9ea6;
  }
}

@media (prefers-color-scheme: light) {
  .trn-21:has(#trn-21-theme:checked) {
    --page: #191a1c;
    --page: oklch(0.22 0.004 250);
    --card: #202225;
    --card: oklch(0.26 0.004 250);
    --ink: #ececee;
    --ink: oklch(0.94 0.002 250);
    --muted: #9b9da2;
    --muted: oklch(0.7 0.006 250);
    --rule: #2f3135;
    --rule: oklch(0.32 0.005 250);
    --line: #6f7379;
    --dur: 900ms;
    --font-display: ui-monospace, "IBM Plex Mono", "JetBrains Mono", Menlo, monospace;
    background: var(--page);
  }

  .trn-21:has(#trn-21-theme:checked) .trn-21__sun {
    opacity: 0.34;
  }

  .trn-21:has(#trn-21-theme:checked) .trn-21__moon {
    opacity: 1;
  }
}
```
