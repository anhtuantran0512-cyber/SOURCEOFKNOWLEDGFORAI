---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/glassmorphism-button-with-subtle-glow-border/"
title: "Glassmorphism Button with Subtle Glow Border"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "Fintech-dashboard glass: a backdrop-blurred button whose hairline border is a real gradient (bright top-left, fading bottom-right — how light actually hits…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Button with Subtle Glow Border
Source: https://codefronts.com/components/css-glowing-border-buttons/glassmorphism-button-with-subtle-glow-border/

Fintech-dashboard glass: a backdrop-blurred button whose hairline border is a real gradient (bright top-left, fading bottom-right — how light actually hits glass), with a soft interior sheen that drifts toward the cursor side on hover. Quiet at rest, unmistakably premium in motion.
## HTML
```html
<section class="gbb-07" aria-label="Glassmorphism glowing border button demo">
  <button class="gbb-07__btn" type="button">View Portfolio &middot; $128,410</button>
</section>
```
## CSS
```css
.gbb-07,
.gbb-07 *,
.gbb-07 *::before,
.gbb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-07 {
  --tint: oklch(0.8 0.1 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(50% 60% at 25% 20%,oklch(0.5 0.17 300 / .55),transparent 60%),radial-gradient(45% 55% at 80% 75%,oklch(0.55 0.15 220 / .5),transparent 60%),oklch(0.15 0.02 270);
}

.gbb-07 .gbb-07__btn {
  position: relative;
  isolation: isolate;
  cursor: pointer;
  padding: 17px 32px;
  border-radius: 16px;
  border: 1px solid transparent;
  background: linear-gradient(rgba(255,255,255,.06),rgba(255,255,255,.06)) padding-box,linear-gradient(135deg,rgba(255,255,255,.55),color-mix(in oklab,var(--tint) 35%,transparent) 40%,rgba(255,255,255,.06) 80%) border-box;
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  backdrop-filter: blur(16px) saturate(1.4);
  font: 600 15px/1 'Segoe UI',system-ui,sans-serif;
  color: rgba(255,255,255,.95);
  box-shadow: 0 8px 32px rgba(0,0,0,.25);
  transition: box-shadow .35s ease,transform .25s ease,background .35s ease;
}

.gbb-07 .gbb-07__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background: radial-gradient(120% 90% at 18% 0%,rgba(255,255,255,.14),transparent 55%);
  opacity: .8;
  transition: opacity .35s ease;
}

.gbb-07 .gbb-07__btn:hover,
.gbb-07 .gbb-07__btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(0,0,0,.25),0 0 0 1px color-mix(in oklab,var(--tint) 35%,transparent),0 0 32px color-mix(in oklab,var(--tint) 30%,transparent);
}

.gbb-07 .gbb-07__btn:hover::before {
  opacity: 1;
}

.gbb-07 .gbb-07__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 4px;
}

.gbb-07 .gbb-07__btn:active {
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .gbb-07 .gbb-07__btn,
    .gbb-07 .gbb-07__btn::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter frost + a padding-box/border-box gradient hairline; the hover glow is a color-mix()ed box-shadow bloom. */
```
