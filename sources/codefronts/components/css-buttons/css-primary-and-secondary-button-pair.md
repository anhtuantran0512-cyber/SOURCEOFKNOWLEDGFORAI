---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-primary-and-secondary-button-pair/"
title: "CSS Primary and Secondary Button Pair"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "One shared button recipe, two visual weights, and a container that stacks them on a phone without a media query — hierarchy done the way a design system does…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Primary and Secondary Button Pair
Source: https://codefronts.com/components/css-buttons/css-primary-and-secondary-button-pair/

One shared button recipe, two visual weights, and a container that stacks them on a phone without a media query — hierarchy done the way a design system does it: the variant classes override only three tokens each, so every state, size and focus behaviour is written once.
## HTML
```html
<div class="cb-02">
  <div class="cb-02__stage">
    <div class="cb-02__pair">
      <button class="cb-02__btn cb-02__btn--primary" type="button">Start free trial</button>
      <button class="cb-02__btn cb-02__btn--secondary" type="button">Book a demo</button>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

.cb-02 {
  --bg: #f6f6f4;
  --surface: #ffffff;
  --text: #141416;
  --muted: #5f5f68;
  --line: #dcdcd6;
  --accent: #4f39f6;
  --on-accent: #ffffff;
  --radius: .75rem;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-02 {
    --bg: oklch(97% .003 90);
    --accent: oklch(51% .23 279);
    --text: oklch(16% .01 285);
    --line: oklch(89% .008 90);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-02:not([data-theme="light"]) {
    --bg: #0c0c0f;
    --surface: #17171c;
    --text: #f4f4f7;
    --muted: #a1a1ad;
    --line: #2c2c35;
    --accent: #8b7cff;
    --on-accent: #0b0a1a;
  }
}

.cb-02[data-theme="dark"] {
  --bg: #0c0c0f;
  --surface: #17171c;
  --text: #f4f4f7;
  --muted: #a1a1ad;
  --line: #2c2c35;
  --accent: #8b7cff;
  --on-accent: #0b0a1a;
}

.cb-02,
.cb-02 *,
.cb-02 *::before,
.cb-02 *::after {
  box-sizing: border-box;
}

.cb-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-02__pair {
  container-type: inline-size;
  width: min(100%,26rem);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: .75rem;
}

.cb-02__btn {
  --ring: transparent;
  --ring-w: 0px;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 3rem;
  padding: 0 1.5rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  background: var(--fill);
  color: var(--ink);
  box-shadow: inset 0 0 0 var(--ring-w) var(--ring);
  transition: translate .2s cubic-bezier(.16,1,.3,1), background-color .2s ease, box-shadow .2s ease;
}

.cb-02__btn--primary {
  --fill: var(--accent);
  --ink: var(--on-accent);
  box-shadow: 0 8px 20px -10px color-mix(in oklab,var(--accent) 80%,transparent);
}

.cb-02__btn--secondary {
  --fill: var(--surface);
  --ink: var(--text);
  --ring: var(--line);
  --ring-w: 1px;
}

.cb-02__btn:hover {
  translate: 0 -1px;
}

.cb-02__btn--primary:hover {
  --fill: color-mix(in oklab,var(--accent) 88%,black);
}

.cb-02__btn--secondary:hover {
  --fill: color-mix(in oklab,var(--text) 5%,var(--surface));
  --ring: color-mix(in oklab,var(--text) 22%,var(--line));
}

.cb-02__btn:active {
  translate: 0 1px;
}

.cb-02__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cb-02__btn:disabled {
  cursor: not-allowed;
  opacity: .45;
  translate: 0;
}

@container (max-width: 22rem) {
  .cb-02__btn {
    flex: 1 1 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-02__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-02__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-02__btn--primary {
    background: Highlight;
    color: HighlightText;
  }
}
```
