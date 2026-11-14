---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-button-group-component-segmented-radio-like/"
title: "CSS Button Group Component (Segmented Radio-Like)"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A segmented control built on real radio inputs, so arrow-key navigation, roving focus and form serialisation come from the platform rather than from JavaScript."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Button Group Component (Segmented Radio-Like)
Source: https://codefronts.com/components/css-buttons/css-button-group-component-segmented-radio-like/

A segmented control built on real radio inputs, so arrow-key navigation, roving focus and form serialisation come from the platform rather than from JavaScript. A single sliding thumb tracks the checked segment via :has(), and the active label crosses over the thumb by inverting colour at the same moment.
## HTML
```html
<div class="cb-08">
  <div class="cb-08__stage">
    <div class="cb-08__group" role="group" aria-label="Chart range">
      <span class="cb-08__thumb" aria-hidden="true"></span>
      <label class="cb-08__seg"><input type="radio" name="cb-08-range" value="day"><span>Day</span></label>
      <label class="cb-08__seg"><input type="radio" name="cb-08-range" value="week" checked><span>Week</span></label>
      <label class="cb-08__seg"><input type="radio" name="cb-08-range" value="month"><span>Month</span></label>
      <label class="cb-08__seg"><input type="radio" name="cb-08-range" value="year"><span>Year</span></label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700&display=swap');

.cb-08 {
  --bg: #f1f2f4;
  --track: #e6e7ea;
  --surface: #ffffff;
  --muted: #63636e;
  --ink-on: #0d0d12;
  --thumb: #ffffff;
  --accent: #5b21b6;
  --n: 4;
  --radius: .7rem;
  --spring: linear(0,.42 8%,.79 17%,1.02 24%,1.09 29%,1.06 36%,1 48%,1);
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-08 {
    --bg: oklch(95.8% .004 265);
    --track: oklch(92.5% .005 265);
    --accent: oklch(44% .2 296);
    --muted: oklch(48% .012 280);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-08:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --track: #191922;
    --surface: #0f0f14;
    --thumb: #2c2c3a;
    --ink-on: #f6f6fa;
    --muted: #9494a2;
    --accent: #a78bfa;
  }
}

.cb-08[data-theme="dark"] {
  --bg: #0a0a0d;
  --track: #191922;
  --surface: #0f0f14;
  --thumb: #2c2c3a;
  --ink-on: #f6f6fa;
  --muted: #9494a2;
  --accent: #a78bfa;
}

.cb-08,
.cb-08 *,
.cb-08 *::before,
.cb-08 *::after {
  box-sizing: border-box;
}

.cb-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-08__group {
  position: relative;
  display: flex;
  width: min(100%,25rem);
  padding: .3rem;
  background: var(--track);
  border-radius: calc(var(--radius) + .3rem);
  box-shadow: inset 0 1px 2px color-mix(in oklab,var(--ink-on) 12%,transparent);
}

.cb-08__thumb {
  position: absolute;
  z-index: 0;
  top: .3rem;
  left: .3rem;
  bottom: .3rem;
  width: calc((100% - .6rem) / var(--n));
  background: var(--thumb);
  border-radius: var(--radius);
  box-shadow: 0 1px 2px color-mix(in oklab,var(--ink-on) 18%,transparent), 0 6px 14px -8px color-mix(in oklab,var(--ink-on) 40%,transparent);
  transition: translate .45s cubic-bezier(.16,1,.3,1);
}

@supports (transition-timing-function: linear(0,1)) {
  .cb-08__thumb {
    transition: translate .5s var(--spring);
  }
}

.cb-08__seg {
  position: relative;
  z-index: 1;
  flex: 1 1 0;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  padding: 0 .5rem;
  border-radius: var(--radius);
  font-size: .875rem;
  font-weight: 600;
  letter-spacing: -.005em;
  color: var(--muted);
  transition: color .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-08__seg input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-08__seg:hover {
  color: color-mix(in oklab,var(--ink-on) 70%,var(--muted));
}

.cb-08__seg:has(input:checked) {
  color: var(--ink-on);
}

.cb-08__seg:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cb-08__group:has(.cb-08__seg:nth-of-type(2) input:checked) .cb-08__thumb {
  translate: 100% 0;
}

.cb-08__group:has(.cb-08__seg:nth-of-type(3) input:checked) .cb-08__thumb {
  translate: 200% 0;
}

.cb-08__group:has(.cb-08__seg:nth-of-type(4) input:checked) .cb-08__thumb {
  translate: 300% 0;
}

.cb-08__group:active .cb-08__thumb {
  scale: .97;
}

@supports not selector(:has(*)) {
  .cb-08__thumb {
    display: none;
  }

  .cb-08__seg:has(input:checked),
    .cb-08__seg input:checked ~ span {
    color: var(--ink-on);
  }

  .cb-08__seg input:checked ~ span {
    text-decoration: underline;
    text-underline-offset: .4em;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-08__thumb,
    .cb-08__seg {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-08__group {
    border: 1px solid ButtonText;
  }

  .cb-08__thumb {
    background: Highlight;
  }

  .cb-08__seg:has(input:checked) {
    color: HighlightText;
  }
}
```
