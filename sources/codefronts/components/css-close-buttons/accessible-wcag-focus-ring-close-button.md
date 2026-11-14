---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/accessible-wcag-focus-ring-close-button/"
title: "Accessible WCAG Focus Ring Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The accessibility reference implementation: a 44×44px touch target (WCAG 2.5.8 AAA / Apple HIG), a dual-ring :focus-visible indicator that survives any…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible WCAG Focus Ring Close Button
Source: https://codefronts.com/components/css-close-buttons/accessible-wcag-focus-ring-close-button/

The accessibility reference implementation: a 44×44px touch target (WCAG 2.5.8 AAA / Apple HIG), a dual-ring :focus-visible indicator that survives any background, visible keyboard-focus without polluting mouse clicks, and a forced-colors fallback. Ship this pattern and your close button passes an audit unchanged.
## HTML
```html
<section class="ccb-02" aria-label="Accessible focus ring close button demo">
  <div class="ccb-02__panels">
    <div class="ccb-02__panel ccb-02__panel--light">
      <span class="ccb-02__hint">Tab to me</span>
      <button class="ccb-02__close" type="button" aria-label="Close panel"></button>
    </div>
    <div class="ccb-02__panel ccb-02__panel--dark">
      <span class="ccb-02__hint">and me</span>
      <button class="ccb-02__close" type="button" aria-label="Close panel"></button>
    </div>
  </div>
</section>
```
## CSS
```css
.ccb-02,
.ccb-02 *,
.ccb-02 *::before,
.ccb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-02 {
  --ring-ink: oklch(0.45 0.19 265);
  --ring-halo: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.93 0.01 260);
}

.ccb-02 .ccb-02__panels {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: min(440px,100%);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 24px 54px -30px oklch(0.35 0.05 265 / .5);
}

.ccb-02 .ccb-02__panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 38px 20px;
}

.ccb-02 .ccb-02__panel--light {
  background: #fff;
  color: oklch(0.45 0.02 265);
}

.ccb-02 .ccb-02__panel--dark {
  background: oklch(0.22 0.03 265);
  color: oklch(0.8 0.02 265);
}

.ccb-02 .ccb-02__hint {
  font-size: 12px;
  letter-spacing: .04em;
}

.ccb-02 .ccb-02__close {
  position: relative;
  width: 44px;
  height: 44px;
  border: 1.5px solid currentColor;
  border-radius: 12px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background .15s ease;
}

.ccb-02 .ccb-02__close::before,
.ccb-02 .ccb-02__close::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 16px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
}

.ccb-02 .ccb-02__close::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-02 .ccb-02__close::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-02 .ccb-02__close:hover {
  background: color-mix(in oklab,currentColor 10%,transparent);
}

.ccb-02 .ccb-02__close:focus-visible {
  outline: 3px solid var(--ring-ink);
  outline-offset: 2px;
  box-shadow: 0 0 0 6px var(--ring-halo),0 0 0 9px var(--ring-ink);
}

.ccb-02 .ccb-02__close:active {
  transform: scale(.95);
}

@media (forced-colors: active) {
  .ccb-02 .ccb-02__close {
    border-color: ButtonText;
  }

  .ccb-02 .ccb-02__close::before,
    .ccb-02 .ccb-02__close::after {
    background: ButtonText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccb-02 .ccb-02__close {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a dual outline + box-shadow focus ring stays visible on light AND dark surfaces; 44×44px box = the tap target. */
```
