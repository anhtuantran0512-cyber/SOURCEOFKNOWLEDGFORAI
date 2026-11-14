---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-ghost-outline-button/"
title: "CSS Ghost / Outline Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A ghost button that keeps its 1px silhouette at rest and fills from the bottom edge on hover, with the label colour inverting in the same beat."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ghost / Outline Button
Source: https://codefronts.com/components/css-buttons/css-ghost-outline-button/

A ghost button that keeps its 1px silhouette at rest and fills from the bottom edge on hover, with the label colour inverting in the same beat. The fill is one background-size transition on a gradient — no pseudo-element, no overflow clipping, and the border is drawn in currentColor so a single colour change re-skins everything.
## HTML
```html
<div class="cb-03">
  <div class="cb-03__stage">
    <button class="cb-03__btn" type="button">
      <span>Read the case study</span>
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"/><path d="M8.5 7H17v8.5"/></svg>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

.cb-03 {
  --bg: #faf9f6;
  --accent: #111827;
  --on-accent: #f9fafb;
  --border-w: 1px;
  --radius: 999px;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-03 {
    --bg: oklch(97.8% .006 95);
    --accent: oklch(22% .02 265);
    --on-accent: oklch(98% .003 265);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-03:not([data-theme="light"]) {
    --bg: #0b0b0c;
    --accent: #f4f4f0;
    --on-accent: #101012;
  }
}

.cb-03[data-theme="dark"] {
  --bg: #0b0b0c;
  --accent: #f4f4f0;
  --on-accent: #101012;
}

.cb-03,
.cb-03 *,
.cb-03 *::before,
.cb-03 *::after {
  box-sizing: border-box;
}

.cb-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-03__btn {
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .65rem;
  min-height: 3.25rem;
  padding: 0 1.75rem;
  border: var(--border-w) solid currentColor;
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 500;
  letter-spacing: .01em;
  color: var(--accent);
  background-color: transparent;
  background-image: linear-gradient(var(--accent),var(--accent));
  background-repeat: no-repeat;
  background-position: 50% 100%;
  background-size: 100% 0%;
  transition: background-size .42s cubic-bezier(.16,1,.3,1), color .3s ease .06s, letter-spacing .42s cubic-bezier(.16,1,.3,1);
}

.cb-03__btn svg {
  width: 1.05rem;
  height: 1.05rem;
  transition: rotate .42s cubic-bezier(.16,1,.3,1);
}

.cb-03__btn:is(:hover,:focus-visible) {
  background-size: 100% 100%;
  color: var(--on-accent);
  letter-spacing: .03em;
}

.cb-03__btn:is(:hover,:focus-visible) svg {
  rotate: 45deg;
}

.cb-03__btn:active {
  scale: .985;
}

.cb-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.cb-03__btn:disabled {
  cursor: not-allowed;
  opacity: .4;
  background-size: 100% 0%;
}

@media (prefers-reduced-motion: reduce) {
  .cb-03__btn,
    .cb-03__btn svg {
    transition: color .1s linear, background-size .1s linear;
  }
}

@media (forced-colors: active) {
  .cb-03__btn {
    background: none;
    border-color: ButtonText;
    color: ButtonText;
  }

  .cb-03__btn:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```
