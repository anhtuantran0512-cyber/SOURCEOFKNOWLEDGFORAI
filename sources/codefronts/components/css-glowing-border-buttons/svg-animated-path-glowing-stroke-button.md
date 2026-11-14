---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/svg-animated-path-glowing-stroke-button/"
title: "SVG Animated Path Glowing Stroke Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The agency-showcase flex: on hover, a glowing stroke draws itself around the button's rounded outline from a single origin point, meets itself, and holds —…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Animated Path Glowing Stroke Button
Source: https://codefronts.com/components/css-glowing-border-buttons/svg-animated-path-glowing-stroke-button/

The agency-showcase flex: on hover, a glowing stroke draws itself around the button's rounded outline from a single origin point, meets itself, and holds — powered by stroke-dasharray on an SVG rect with pathLength="100", so the dash math is percentage-simple regardless of the button's real size.
## HTML
```html
<section class="gbb-12" aria-label="SVG stroke trace glowing button demo">
  <a class="gbb-12__btn" href="#">
    See Our Work
    <svg class="gbb-12__trace" aria-hidden="true">
      <defs>
        <linearGradient id="gbb-12-grad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="oklch(0.86 0.16 195)"/>
          <stop offset="100%" stop-color="oklch(0.78 0.19 235)"/>
        </linearGradient>
      </defs>
      <rect class="gbb-12__under" x="1.5" y="1.5" rx="14" pathLength="100"></rect>
      <rect class="gbb-12__line" x="1.5" y="1.5" rx="14" pathLength="100"></rect>
    </svg>
  </a>
</section>
```
## CSS
```css
.gbb-12,
.gbb-12 *,
.gbb-12 *::before,
.gbb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-12 {
  --ink: oklch(0.86 0.16 195);
  --ink-2: oklch(0.78 0.19 235);
  --ease: cubic-bezier(0.22,1,0.36,1);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(55% 60% at 25% 20%,oklch(0.24 0.06 200 / .35),transparent 60%),radial-gradient(50% 55% at 82% 88%,oklch(0.22 0.07 245 / .35),transparent 60%),linear-gradient(165deg,oklch(0.14 0.018 220),oklch(0.11 0.012 245));
}

.gbb-12 .gbb-12__btn {
  position: relative;
  display: inline-block;
  padding: 18px 38px;
  border-radius: 14px;
  font: 600 15px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .02em;
  color: #eefbff;
  text-decoration: none;
  background: linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  border: 1px solid rgba(255,255,255,.10);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08),inset 0 -1px 0 rgba(0,0,0,.15),0 1px 0 rgba(0,0,0,.3);
  transition: background .35s var(--ease),border-color .35s var(--ease),box-shadow .35s var(--ease),transform .35s var(--ease);
}

.gbb-12 .gbb-12__trace {
  position: absolute;
  inset: -1.5px;
  width: calc(100% + 3px);
  height: calc(100% + 3px);
  pointer-events: none;
  overflow: visible;
}

.gbb-12 .gbb-12__trace rect {
  width: calc(100% - 3px);
  height: calc(100% - 3px);
  fill: none;
  stroke-width: 2;
  stroke-linecap: butt;
  stroke-dasharray: 0.001 100;
  stroke-dashoffset: 0;
  transition: stroke-dasharray .9s var(--ease),opacity .3s ease;
}

.gbb-12 .gbb-12__line {
  stroke: var(--ink);
  filter: drop-shadow(0 0 6px var(--ink)) drop-shadow(0 0 14px color-mix(in oklab,var(--ink) 55%,transparent));
}

.gbb-12 .gbb-12__under {
  stroke: url(#gbb-12-grad);
  opacity: .35;
  stroke-width: 6;
  filter: blur(5px);
}

.gbb-12 .gbb-12__btn:hover,
.gbb-12 .gbb-12__btn:focus-visible {
  background: linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.03));
  border-color: color-mix(in oklab,var(--ink) 35%,transparent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12),inset 0 -1px 0 rgba(0,0,0,.2),0 1px 0 rgba(0,0,0,.4),0 0 24px -6px color-mix(in oklab,var(--ink) 35%,transparent);
  transform: translateY(-1px);
}

.gbb-12 .gbb-12__btn:hover rect,
.gbb-12 .gbb-12__btn:focus-visible rect {
  stroke-dasharray: 100 0;
}

.gbb-12 .gbb-12__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 5px;
}

.gbb-12 .gbb-12__btn:active {
  transform: translateY(0);
  transition-duration: .1s;
}

@media (prefers-reduced-motion: reduce) {
  .gbb-12 .gbb-12__trace rect {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pathLength="100" normalizes the perimeter so stroke-dashoffset 100→0 draws one full lap at any size; un-hover retracts it for free. */
```
