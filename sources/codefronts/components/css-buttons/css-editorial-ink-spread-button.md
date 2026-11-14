---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-editorial-ink-spread-button/"
title: "CSS Editorial Ink Spread Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Letterpress restraint: a serif label on cream stock, a hairline rule that grows into a full underline, and an ink blot that floods from the baseline on hover…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Editorial Ink Spread Button
Source: https://codefronts.com/components/css-buttons/css-editorial-ink-spread-button/

Letterpress restraint: a serif label on cream stock, a hairline rule that grows into a full underline, and an ink blot that floods from the baseline on hover with a soft irregular edge — a masked radial gradient scaling up, so it feels absorbed rather than filled.
## HTML
```html
<div class="cb-19">
  <div class="cb-19__stage">
    <button class="cb-19__btn" type="button">
      <span class="cb-19__ink" aria-hidden="true"></span>
      <span class="cb-19__label">Read the essay</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap');

.cb-19 {
  --paper: #f4efe4;
  --ink: #1a1614;
  --accent: #8c2f1f;
  --radius: .25rem;
  --serif: "Instrument Serif",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(60rem 40rem at 50% 0%, color-mix(in oklab,white 55%,transparent), transparent 60%), var(--paper);
  font-family: var(--serif);
}

@supports (color: oklch(50% 0 0)) {
  .cb-19 {
    --paper: oklch(95% .018 85);
    --ink: oklch(20% .012 40);
    --accent: oklch(43% .13 32);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-19:not([data-theme="light"]) {
    --paper: #14110f;
    --ink: #f2ebdd;
    --accent: #e08b6d;
  }
}

.cb-19[data-theme="dark"] {
  --paper: #14110f;
  --ink: #f2ebdd;
  --accent: #e08b6d;
}

.cb-19,
.cb-19 *,
.cb-19 *::before,
.cb-19 *::after {
  box-sizing: border-box;
}

.cb-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-19__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 3.5rem;
  padding: .35rem 1.9rem .5rem;
  border: 1px solid color-mix(in oklab,var(--ink) 30%,transparent);
  border-radius: var(--radius);
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1.375rem;
  letter-spacing: .005em;
  font-variant-ligatures: common-ligatures;
  transition: border-color .4s ease, color .34s ease .1s;
}

.cb-19__label {
  position: relative;
  z-index: 2;
}

.cb-19__label::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -.28rem;
  height: 1px;
  background: currentColor;
  scale: 0 1;
  transform-origin: left;
  transition: scale .5s cubic-bezier(.16,1,.3,1);
}

.cb-19__ink {
  position: absolute;
  inset: -20% -10%;
  z-index: 1;
  background: var(--ink);
  -webkit-mask: radial-gradient(58% 120% at 50% 112%, #000 38%, rgba(0,0,0,.5) 64%, transparent 80%);
  mask: radial-gradient(58% 120% at 50% 112%, #000 38%, rgba(0,0,0,.5) 64%, transparent 80%);
  scale: .25;
  opacity: 0;
  transform-origin: 50% 100%;
  transition: scale .62s cubic-bezier(.16,1,.3,1), opacity .34s ease;
}

.cb-19__btn:is(:hover,:focus-visible) {
  color: var(--paper);
  border-color: var(--ink);
}

.cb-19__btn:is(:hover,:focus-visible) .cb-19__ink {
  scale: 1.45;
  opacity: 1;
}

.cb-19__btn:is(:hover,:focus-visible) .cb-19__label::after {
  scale: 1 1;
}

.cb-19__btn:focus-visible {
  outline: 1px solid var(--accent);
  outline-offset: 5px;
}

.cb-19__btn:active {
  scale: .99;
}

.cb-19__btn:active .cb-19__ink {
  background: var(--accent);
}

.cb-19__btn:disabled {
  cursor: not-allowed;
  color: color-mix(in oklab,var(--ink) 45%,var(--paper));
  border-color: color-mix(in oklab,var(--ink) 15%,transparent);
}

.cb-19__btn:disabled .cb-19__ink {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cb-19__btn,
    .cb-19__ink,
    .cb-19__label::after {
    transition: color .12s linear, background-color .12s linear;
  }

  .cb-19__ink {
    scale: 1.45;
    opacity: 0;
  }

  .cb-19__btn:is(:hover,:focus-visible) .cb-19__ink {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .cb-19__btn {
    color: ButtonText;
    border-color: ButtonText;
    background: ButtonFace;
  }

  .cb-19__ink {
    display: none;
  }

  .cb-19__btn:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```
