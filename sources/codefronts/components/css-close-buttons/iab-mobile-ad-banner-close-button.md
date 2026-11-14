---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/iab-mobile-ad-banner-close-button/"
title: "IAB Mobile Ad Banner Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The ad-tech compliance pattern: a visually small × on a mobile banner ad whose real tap target is inflated to 48×48px with pure padding — WCAG 2.5.8 and…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: IAB Mobile Ad Banner Close Button
Source: https://codefronts.com/components/css-close-buttons/iab-mobile-ad-banner-close-button/

The ad-tech compliance pattern: a visually small × on a mobile banner ad whose real tap target is inflated to 48×48px with pure padding — WCAG 2.5.8 and Google Better Ads guidance satisfied without visually crowding a 50px-tall creative. The demo overlays a translucent debug outline you can toggle in CSS to SEE the invisible target.
## HTML
```html
<section class="ccb-06" aria-label="Mobile ad banner close button demo">
  <div class="ccb-06__slot">
    <div class="ccb-06__ad">
      <div class="ccb-06__creative">
        <span class="ccb-06__brand">SUMMER SALE</span>
        <span class="ccb-06__copy">Up to 60% off — today only</span>
      </div>
      <button class="ccb-06__close" type="button" aria-label="Close ad"><span class="ccb-06__dot" aria-hidden="true"></span></button>
    </div>
    <p class="ccb-06__note">Dashed ring = the real 48×48 tap target (set <code>--debug:0</code> to hide)</p>
  </div>
</section>
```
## CSS
```css
.ccb-06,
.ccb-06 *,
.ccb-06 *::before,
.ccb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-06 {
  --d: 20px;
  --debug: 1;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.94 0.01 80);
}

.ccb-06 .ccb-06__slot {
  width: min(360px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
}

.ccb-06 .ccb-06__ad {
  position: relative;
  width: 100%;
  height: 64px;
  border-radius: 10px;
  background: linear-gradient(100deg,oklch(0.62 0.19 40),oklch(0.55 0.21 20));
  box-shadow: 0 14px 30px -16px oklch(0.45 0.15 30 / .6);
}

.ccb-06 .ccb-06__creative {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 3px;
  padding: 0 16px;
  color: #fff;
}

.ccb-06 .ccb-06__brand {
  font: 800 15px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .06em;
}

.ccb-06 .ccb-06__copy {
  font-size: 11.5px;
  opacity: .9;
}

.ccb-06 .ccb-06__close {
  position: absolute;
  top: 0;
  inset-inline-end: 0;
  margin: -14px -14px 0 0;
  padding: 14px;
  border: none;
  background: transparent;
  cursor: pointer;
  outline: calc(var(--debug) * 1.5px) dashed oklch(0.55 0.15 30 / .65);
  outline-offset: -2px;
  border-radius: 14px;
}

.ccb-06 .ccb-06__dot {
  position: relative;
  display: block;
  width: var(--d);
  height: var(--d);
  border-radius: 50%;
  background: rgba(20,16,14,.72);
  transition: transform .15s ease;
}

.ccb-06 .ccb-06__dot::before,
.ccb-06 .ccb-06__dot::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: calc(var(--d) * .5);
  height: 1.5px;
  border-radius: 2px;
  background: #fff;
}

.ccb-06 .ccb-06__dot::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-06 .ccb-06__dot::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-06 .ccb-06__close:hover .ccb-06__dot {
  transform: scale(1.1);
}

.ccb-06 .ccb-06__close:active .ccb-06__dot {
  transform: scale(.9);
}

.ccb-06 .ccb-06__close:focus-visible {
  outline: 3px solid oklch(0.5 0.18 30);
  outline-offset: 0;
}

.ccb-06 .ccb-06__note {
  font-size: 11.5px;
  color: oklch(0.5 0.03 60);
  text-align: center;
}

.ccb-06 .ccb-06__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-06 .ccb-06__dot {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — padding inflates a 20px visual to a 48×48 tap target; the dashed outline visualises it (--debug:0 hides). */
```
