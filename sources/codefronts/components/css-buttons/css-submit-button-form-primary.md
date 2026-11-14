---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-submit-button-form-primary/"
title: "CSS Submit Button (Form Primary)"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "The button every form ends with, engineered properly: a two-layer elevation shadow that reads as physical depth, a masked sheen that sweeps once on hover, a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Submit Button (Form Primary)
Source: https://codefronts.com/components/css-buttons/css-submit-button-form-primary/

The button every form ends with, engineered properly: a two-layer elevation shadow that reads as physical depth, a masked sheen that sweeps once on hover, a real 1px press travel, and a focus ring built from outline plus a soft halo so it survives on any background. Zero JavaScript, four states, one token block.
## HTML
```html
<div class="cb-01">
  <div class="cb-01__stage">
    <button class="cb-01__btn" type="submit">
      <span>Create account</span>
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h14"/><path d="M12.5 5.5 19 12l-6.5 6.5"/></svg>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&display=swap');

.cb-01 {
  --bg: #f2f1ee;
  --accent: #16a34a;
  --on-accent: #ffffff;
  --shadow: #0b3d20;
  --radius: .9rem;
  --travel: 2px;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-01 {
    --bg: oklch(96.5% .006 95);
    --accent: oklch(58% .15 152);
    --shadow: oklch(32% .09 155);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-01:not([data-theme="light"]) {
    --bg: #0e1211;
    --accent: #22c55e;
    --on-accent: #04140a;
    --shadow: #000000;
  }
}

.cb-01[data-theme="dark"] {
  --bg: #0e1211;
  --accent: #22c55e;
  --on-accent: #04140a;
  --shadow: #000000;
}

.cb-01,
.cb-01 *,
.cb-01 *::before,
.cb-01 *::after {
  box-sizing: border-box;
}

.cb-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-01__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .6rem;
  min-height: 3.25rem;
  padding: 0 1.6rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--on-accent);
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 88%,white),var(--accent));
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 38%,transparent), 0 1px 2px color-mix(in oklab,var(--shadow) 38%,transparent), 0 10px 24px -8px color-mix(in oklab,var(--shadow) 55%,transparent);
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .22s cubic-bezier(.16,1,.3,1), filter .22s ease;
}

.cb-01__btn svg {
  width: 1.15rem;
  height: 1.15rem;
  transition: translate .3s cubic-bezier(.16,1,.3,1);
}

.cb-01__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background: linear-gradient(105deg,transparent 35%,color-mix(in oklab,white 42%,transparent) 50%,transparent 65%);
  translate: -125% 0;
  transition: translate .8s cubic-bezier(.16,1,.3,1);
}

.cb-01__btn:hover {
  translate: 0 calc(var(--travel) * -1);
  filter: saturate(1.06);
}

.cb-01__btn:hover svg {
  translate: .2rem 0;
}

.cb-01__btn:hover::before,
.cb-01__btn:focus-visible::before {
  translate: 125% 0;
}

.cb-01__btn:active {
  translate: 0 1px;
  box-shadow: inset 0 2px 6px color-mix(in oklab,var(--shadow) 45%,transparent);
}

.cb-01__btn:focus-visible {
  outline: 2px solid color-mix(in oklab,var(--accent) 70%,black);
  outline-offset: 3px;
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 38%,transparent), 0 0 0 6px color-mix(in oklab,var(--accent) 22%,transparent);
}

.cb-01__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(1);
  opacity: .5;
  box-shadow: none;
  translate: 0;
}

@media (prefers-reduced-motion: reduce) {
  .cb-01__btn,
    .cb-01__btn::before,
    .cb-01__btn svg {
    transition: none;
  }

  .cb-01__btn::before {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-01__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-01__btn::before {
    display: none;
  }
}
```
