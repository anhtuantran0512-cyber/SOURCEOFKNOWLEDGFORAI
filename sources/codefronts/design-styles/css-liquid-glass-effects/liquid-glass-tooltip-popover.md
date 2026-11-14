---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-tooltip-popover/"
title: "Liquid Glass Tooltip / Popover"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A capsule tooltip that frosts the text behind it instead of blocking it — on hover/focus it fades and slides up into place with a soft glass blur, keeping…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Tooltip / Popover
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-tooltip-popover/

A capsule tooltip that frosts the text behind it instead of blocking it — on hover/focus it fades and slides up into place with a soft glass blur, keeping spatial context. Clean z-indexing and absolute positioning, pure CSS, and reachable by keyboard focus, not just hover.
## HTML
```html
<section class="lg-11" aria-label="Liquid glass tooltip demo">
  <p class="lg-11__para">Your plan renews on the <span class="lg-11__trig" tabindex="0">14th<span class="lg-11__tip" role="tooltip">Auto-renews · cancel anytime up to 24h before</span></span>. You've used <span class="lg-11__trig" tabindex="0">68%<span class="lg-11__tip" role="tooltip">34 GB of your 50 GB quota</span></span> of storage this cycle, and <span class="lg-11__trig" tabindex="0">3 seats<span class="lg-11__tip" role="tooltip">2 active, 1 pending invite</span></span> are assigned.</p>
</section>
```
## CSS
```css
.lg-11,
.lg-11 *,
.lg-11 *::before,
.lg-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  background: url('https://picsum.photos/seed/lgtip/1100/800') center/cover fixed,#141024;
}

.lg-11__para {
  max-width: 44ch;
  font-size: 22px;
  line-height: 1.9;
  color: #fff;
  text-shadow: 0 1px 10px rgba(0,0,0,.5);
  text-align: center;
}

.lg-11__trig {
  position: relative;
  font-weight: 800;
  color: oklch(0.85 0.13 200);
  border-bottom: 2px dotted rgba(255,255,255,.5);
  cursor: help;
  outline: none;
}

.lg-11__trig:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
  border-radius: 4px;
}

.lg-11__tip {
  position: absolute;
  left: 50%;
  bottom: calc(100% + 12px);
  transform: translateX(-50%) translateY(6px);
  width: max-content;
  max-width: 220px;
  font-size: 13px;
  font-weight: 600;
  line-height: 1.4;
  color: #fff;
  text-shadow: none;
  padding: 9px 13px;
  border-radius: 14px;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 16px 34px -18px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  opacity: 0;
  visibility: hidden;
  transition: opacity .25s,transform .25s,visibility 0s .25s;
  z-index: 5;
  pointer-events: none;
}

.lg-11__tip::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-5px) rotate(45deg);
  width: 12px;
  height: 12px;
  background: inherit;
  border-right: 1px solid rgba(255,255,255,.4);
  border-bottom: 1px solid rgba(255,255,255,.4);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

.lg-11__trig:hover .lg-11__tip,
.lg-11__trig:focus-visible .lg-11__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition: opacity .25s,transform .25s;
}

@media (prefers-reduced-motion: reduce) {
  .lg-11__tip {
    transition: opacity .15s,visibility 0s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the tooltip reveals on both :hover and :focus-visible (keyboard-reachable), fades + slides via transform/opacity, and frosts the text behind it with backdrop-filter. */
```
