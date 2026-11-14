---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/raised-inset-and-flat-soft-ui-states/"
title: "Raised Inset and Flat Soft UI States"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The three-state system that makes soft UI feel like something you can touch: raised for rest, inset for pressed, flat for inactive."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Raised Inset and Flat Soft UI States
Source: https://codefronts.com/design-styles/css-neumorphism/raised-inset-and-flat-soft-ui-states/

The three-state system that makes soft UI feel like something you can touch: raised for rest, inset for pressed, flat for inactive. One control is shown in all three states side by side and again as a live button you can press. Includes the trap nobody warns you about — an outset shadow does not interpolate into an inset one, so the transition jumps at the midpoint — and the two workarounds that fix it.
## HTML
```html
<section class="nm-03" aria-labelledby="nm-03-heading">
      <input type="checkbox" id="nm-03-theme" class="nm-03__themeinput">
      <label for="nm-03-theme" class="nm-03__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-03__stage">
    <header class="nm-03__head">
      <p class="nm-03__kicker">State system</p>
      <h2 class="nm-03__heading" id="nm-03-heading">Raised, inset, flat</h2>
      <p class="nm-03__sub">Rest, pressed, inactive. Three shadow states, each paired with a label so depth is never the only signal.</p>
    </header>

    <div class="nm-03__strip">
      <figure class="nm-03__specimen">
        <div class="nm-03__tile nm-03__tile--raised">
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <figcaption class="nm-03__caption"><b>Raised</b><span>outset pair · resting</span></figcaption>
      </figure>
      <figure class="nm-03__specimen">
        <div class="nm-03__tile nm-03__tile--inset">
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M5 12.5l4.6 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <figcaption class="nm-03__caption"><b>Inset</b><span>same pair, inset keyword · pressed</span></figcaption>
      </figure>
      <figure class="nm-03__specimen">
        <div class="nm-03__tile nm-03__tile--flat">
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6 12h12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <figcaption class="nm-03__caption"><b>Flat</b><span>no shadow, hairline border · inactive</span></figcaption>
      </figure>
    </div>

    <div class="nm-03__lab">
      <article class="nm-03__panel">
        <h3 class="nm-03__ptitle">Cross-faded layers</h3>
        <p class="nm-03__note">Two pseudo-element layers, one raised and one inset, swapped with opacity. The press reads as continuous.</p>
        <button class="nm-03__button nm-03__button--nm-03-good" type="button">
          <span class="nm-03__btnicon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><circle cx="12" cy="12" r="7" fill="none" stroke="currentColor" stroke-width="2"/></svg></span>
          Hold to press
        </button>
      </article>
      <article class="nm-03__panel">
        <h3 class="nm-03__ptitle">Single declaration</h3>
        <p class="nm-03__note">One rule transitioning straight from outset to inset. The shadow holds, then jumps at the midpoint.</p>
        <button class="nm-03__button nm-03__button--nm-03-naive" type="button">
          <span class="nm-03__btnicon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 6v12M6 12h12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          Hold to press
        </button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-03 {
  position: relative;
  --nm-03-surface: #dfe6da;
  --nm-03-dark: rgba(154,171,145,0.66);
  --nm-03-light: rgba(255,255,252,0.94);
  --nm-03-ink: #26312300;
  --nm-03-ink: #263123;
  --nm-03-muted: #5c6b56;
  --nm-03-accent: #3f7a4e;
  --nm-03-distance: clamp(6px, 1.5vw, 10px);
  --nm-03-blur: clamp(12px, 3vw, 20px);
  --nm-03-press-depth: clamp(5px, 1.3vw, 9px);
  --nm-03-speed: 170ms;
  --nm-03-font-display: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", "Quicksand", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-03-surface);
  color: var(--nm-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.02 140)) {
  .nm-03 {
    --nm-03-surface: oklch(0.913 0.021 137);
    --nm-03-ink: oklch(0.30 0.028 145);
    --nm-03-muted: oklch(0.50 0.026 145);
    --nm-03-accent: oklch(0.52 0.098 152);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-03 {
    --nm-03-dark: color-mix(in oklab, var(--nm-03-surface), #000 21%);
    --nm-03-light: color-mix(in oklab, var(--nm-03-surface), #fff 90%);
  }
}

.nm-03 *,
.nm-03 *::before,
.nm-03 *::after {
  box-sizing: border-box;
}

.nm-03__stage {
  max-width: 1000px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(24px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(24px, 4vw, 42px);
}

.nm-03__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-03__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-03-muted);
}

.nm-03__heading {
  margin: 0;
  font-family: var(--nm-03-font-display);
  font-size: clamp(1.6rem, 4.6vw, 2.45rem);
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
  text-wrap: balance;
}

.nm-03__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--nm-03-muted);
  text-wrap: pretty;
}

.nm-03__strip {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 26px);
}

@media (min-width: 560px) {
  .nm-03__strip {
    grid-template-columns: repeat(3, 1fr);
  }
}

.nm-03__specimen {
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  min-inline-size: 0;
}

.nm-03__tile {
  width: 100%;
  max-width: 190px;
  aspect-ratio: 1.35;
  border-radius: 20px;
  display: grid;
  place-items: center;
  background: var(--nm-03-surface);
  color: var(--nm-03-accent);
  border: 1px solid transparent;
}

.nm-03__tile--raised {
  box-shadow: var(--nm-03-distance) var(--nm-03-distance) var(--nm-03-blur) var(--nm-03-dark), calc(var(--nm-03-distance) * -1) calc(var(--nm-03-distance) * -1) var(--nm-03-blur) var(--nm-03-light);
}

.nm-03__tile--inset {
  box-shadow: inset var(--nm-03-press-depth) var(--nm-03-press-depth) calc(var(--nm-03-blur) * 0.85) var(--nm-03-dark), inset calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-blur) * 0.85) var(--nm-03-light);
}

.nm-03__tile--flat {
  box-shadow: none;
  border: 1px dotted var(--nm-03-muted);
  color: var(--nm-03-muted);
}

.nm-03__caption {
  display: flex;
  flex-direction: column;
  gap: 3px;
  text-align: center;
  min-inline-size: 0;
}

.nm-03__caption b {
  font-family: var(--nm-03-font-display);
  font-size: 0.92rem;
  font-weight: 600;
}

.nm-03__caption span {
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--nm-03-muted);
}

.nm-03__lab {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 24px);
}

@media (min-width: 680px) {
  .nm-03__lab {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-03__panel {
  background: var(--nm-03-surface);
  border-radius: 20px;
  padding: clamp(18px, 3vw, 26px);
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  min-inline-size: 0;
  box-shadow: inset 2px 2px 6px var(--nm-03-dark), inset -2px -2px 6px var(--nm-03-light);
}

.nm-03__ptitle {
  margin: 0;
  font-family: var(--nm-03-font-display);
  font-size: 0.95rem;
  font-weight: 600;
}

.nm-03__note {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--nm-03-muted);
  text-wrap: pretty;
}

.nm-03__button {
  position: relative;
  isolation: isolate;
  min-height: 48px;
  min-width: 44px;
  margin-top: 4px;
  padding: 0 22px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  border-radius: 16px;
  border: 1px solid var(--nm-03-muted);
  background: var(--nm-03-surface);
  color: var(--nm-03-ink);
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  font-family: var(--nm-03-font-display);
  cursor: pointer;
}

.nm-03__button::before,
.nm-03__button::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  z-index: -1;
}

.nm-03__button--nm-03-good::before {
  box-shadow: var(--nm-03-distance) var(--nm-03-distance) var(--nm-03-blur) var(--nm-03-dark), calc(var(--nm-03-distance) * -1) calc(var(--nm-03-distance) * -1) var(--nm-03-blur) var(--nm-03-light);
  opacity: 1;
  transition: opacity var(--nm-03-speed) ease;
}

.nm-03__button--nm-03-good::after {
  box-shadow: inset var(--nm-03-press-depth) var(--nm-03-press-depth) calc(var(--nm-03-blur) * 0.8) var(--nm-03-dark), inset calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-blur) * 0.8) var(--nm-03-light);
  opacity: 0;
  transition: opacity var(--nm-03-speed) ease;
}

.nm-03__button--nm-03-good:active::before {
  opacity: 0;
}

.nm-03__button--nm-03-good:active::after {
  opacity: 1;
}

.nm-03__button--nm-03-naive {
  box-shadow: var(--nm-03-distance) var(--nm-03-distance) var(--nm-03-blur) var(--nm-03-dark), calc(var(--nm-03-distance) * -1) calc(var(--nm-03-distance) * -1) var(--nm-03-blur) var(--nm-03-light);
  transition: box-shadow var(--nm-03-speed) ease;
}

.nm-03__button--nm-03-naive:active {
  box-shadow: inset var(--nm-03-press-depth) var(--nm-03-press-depth) calc(var(--nm-03-blur) * 0.8) var(--nm-03-dark), inset calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-press-depth) * -1) calc(var(--nm-03-blur) * 0.8) var(--nm-03-light);
}

.nm-03__button:active {
  color: var(--nm-03-accent);
}

.nm-03__button:focus-visible {
  outline: 2px solid var(--nm-03-accent);
  outline-offset: 3px;
}

.nm-03__btnicon {
  display: inline-flex;
  color: var(--nm-03-accent);
}

@media (prefers-reduced-motion: reduce) {
  .nm-03__button--nm-03-good::before,
    .nm-03__button--nm-03-good::after,
    .nm-03__button--nm-03-naive {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-03 {
    --nm-03-surface: #2b332a;
    --nm-03-dark: rgba(11,14,11,0.7);
    --nm-03-light: rgba(88,101,86,0.46);
    --nm-03-ink: #e2e9de;
    --nm-03-muted: #9aa895;
    --nm-03-accent: #7fc292;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-03 {
      --nm-03-dark: color-mix(in oklab, var(--nm-03-surface), #000 54%);
      --nm-03-light: color-mix(in oklab, var(--nm-03-surface), #fff 14%);
    }
  }
}

.nm-03[data-theme="dark"] {
  --nm-03-surface: #2b332a;
  --nm-03-dark: rgba(11,14,11,0.7);
  --nm-03-light: rgba(88,101,86,0.46);
  --nm-03-ink: #e2e9de;
  --nm-03-muted: #9aa895;
  --nm-03-accent: #7fc292;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-03[data-theme="dark"] {
    --nm-03-dark: color-mix(in oklab, var(--nm-03-surface), #000 54%);
    --nm-03-light: color-mix(in oklab, var(--nm-03-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-03__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-03__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-03-surface);
  color: var(--nm-03-ink);
  border: 1px solid var(--nm-03-line);
  font: 600 11px/1 var(--nm-03-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-03-distance, 6px) var(--nm-03-distance, 6px) var(--nm-03-blur, 14px) var(--nm-03-dark), calc(-1 * var(--nm-03-distance, 6px)) calc(-1 * var(--nm-03-distance, 6px)) var(--nm-03-blur, 14px) var(--nm-03-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-03__themebtn:hover {
  color: var(--nm-03-ink);
}

.nm-03__themeinput:focus-visible + .nm-03__themebtn {
  outline: 2px solid var(--nm-03-ink);
  outline-offset: 3px;
}

.nm-03:has(#nm-03-theme:checked) .nm-03__themebtn {
  box-shadow: inset var(--nm-03-distance, 6px) var(--nm-03-distance, 6px) var(--nm-03-blur, 14px) var(--nm-03-dark), inset calc(-1 * var(--nm-03-distance, 6px)) calc(-1 * var(--nm-03-distance, 6px)) var(--nm-03-blur, 14px) var(--nm-03-light);
}

.nm-03__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-03:has(#nm-03-theme:checked) {
  --nm-03-surface: #2b332a;
  --nm-03-dark: rgba(11,14,11,0.7);
  --nm-03-light: rgba(88,101,86,0.46);
  --nm-03-ink: #e2e9de;
  --nm-03-muted: #9aa895;
  --nm-03-accent: #7fc292;
}

@media (prefers-color-scheme: light) {
  .nm-03:has(#nm-03-theme:checked) {
    --nm-03-surface: #2b332a;
    --nm-03-dark: rgba(11,14,11,0.7);
    --nm-03-light: rgba(88,101,86,0.46);
    --nm-03-ink: #e2e9de;
    --nm-03-muted: #9aa895;
    --nm-03-accent: #7fc292;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-03:has(#nm-03-theme:checked) {
    --nm-03-surface: #dfe6da;
    --nm-03-dark: rgba(154,171,145,0.66);
    --nm-03-light: rgba(255,255,252,0.94);
    --nm-03-ink: #263123;
    --nm-03-muted: #5c6b56;
    --nm-03-accent: #3f7a4e;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-03__themebtn {
    transition: none;
  }
}
```
