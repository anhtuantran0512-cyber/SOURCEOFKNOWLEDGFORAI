---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/ios-style-circular-tab-close-button/"
title: "iOS-Style Circular Tab Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The mobile-native dismiss: a semi-transparent grey circle with a crisp centred ×, exactly as Safari draws it on tab thumbnails and iOS draws it on…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS-Style Circular Tab Close Button
Source: https://codefronts.com/components/css-close-buttons/ios-style-circular-tab-close-button/

The mobile-native dismiss: a semi-transparent grey circle with a crisp centred ×, exactly as Safari draws it on tab thumbnails and iOS draws it on notification cards. Includes the signature :active shrink (scale .88) that makes touches feel acknowledged, and a frosted-glass card context so you see it against imagery.
## HTML
```html
<section class="ccb-03" aria-label="iOS-style tab close button demo">
  <div class="ccb-03__tab">
    <button class="ccb-03__close" type="button" aria-label="Close tab"></button>
    <div class="ccb-03__bar"><span class="ccb-03__title">apple.com</span></div>
  </div>
</section>
```
## CSS
```css
.ccb-03,
.ccb-03 *,
.ccb-03 *::before,
.ccb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-03 {
  --d: 28px;
  --fill: rgba(120,120,128,.36);
  --glyph: rgba(255,255,255,.92);
  font-family: -apple-system,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 130% at 20% 0%,oklch(0.6 0.14 250),transparent 55%),radial-gradient(110% 120% at 90% 100%,oklch(0.55 0.16 320),transparent 55%),oklch(0.35 0.06 280);
}

.ccb-03 .ccb-03__tab {
  position: relative;
  width: min(280px,100%);
  aspect-ratio: 4/3;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.85 0.06 230),oklch(0.7 0.1 280) 55%,oklch(0.6 0.13 320));
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.6);
}

.ccb-03 .ccb-03__bar {
  position: absolute;
  inset-inline: 0;
  bottom: 0;
  padding: 11px 14px;
  background: rgba(30,30,36,.45);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.ccb-03 .ccb-03__title {
  font-size: 13px;
  color: rgba(255,255,255,.95);
}

.ccb-03 .ccb-03__close {
  position: absolute;
  top: 10px;
  inset-inline-end: 10px;
  width: var(--d);
  height: var(--d);
  border: none;
  border-radius: 50%;
  background: var(--fill);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  cursor: pointer;
  transition: transform .25s cubic-bezier(.34,1.56,.64,1),background .15s ease;
}

.ccb-03 .ccb-03__close::before,
.ccb-03 .ccb-03__close::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: calc(var(--d) * .42);
  height: 1.5px;
  border-radius: 2px;
  background: var(--glyph);
}

.ccb-03 .ccb-03__close::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-03 .ccb-03__close::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-03 .ccb-03__close:hover {
  background: rgba(120,120,128,.5);
}

.ccb-03 .ccb-03__close:active {
  transform: scale(.88);
  transition-duration: .12s;
}

.ccb-03 .ccb-03__close:focus-visible {
  outline: 2.5px solid #fff;
  outline-offset: 2px;
}

@media (pointer: coarse) {
  .ccb-03 .ccb-03__close::before {
    width: calc(var(--d) * .42);
  }
}

.ccb-03 .ccb-03__close::selection {
  background: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-03 .ccb-03__close {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — Apple's systemGray fill + backdrop blur keeps the circle legible over photos; :active scale(.88) is the tactile press. */
```
