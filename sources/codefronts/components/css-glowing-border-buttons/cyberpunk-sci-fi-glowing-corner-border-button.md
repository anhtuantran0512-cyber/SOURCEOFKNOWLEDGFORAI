---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/cyberpunk-sci-fi-glowing-corner-border-button/"
title: "Cyberpunk Sci-Fi Glowing Corner Border Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "Angular Web3/HUD energy: a clip-path button with sliced corners, amber corner brackets, and a glow that follows the clipped shape exactly — because it uses…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Sci-Fi Glowing Corner Border Button
Source: https://codefronts.com/components/css-glowing-border-buttons/cyberpunk-sci-fi-glowing-corner-border-button/

Angular Web3/HUD energy: a clip-path button with sliced corners, amber corner brackets, and a glow that follows the clipped shape exactly — because it uses drop-shadow(), not box-shadow. On hover the brackets snap outward and a scanline flickers across the face.
## HTML
```html
<section class="gbb-04" aria-label="Cyberpunk clipped corner glowing button demo">
  <span class="gbb-04__wrap"><button class="gbb-04__btn" type="button">Connect Wallet</button></span>
</section>
```
## CSS
```css
.gbb-04,
.gbb-04 *,
.gbb-04 *::before,
.gbb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-04 {
  --cyb: oklch(0.8 0.16 75);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: repeating-linear-gradient(0deg,transparent 0 3px,rgba(255,255,255,.012) 3px 4px),radial-gradient(70% 90% at 50% 110%,oklch(0.2 0.04 75 / .5),transparent 60%),oklch(0.11 0.01 260);
}

.gbb-04 .gbb-04__wrap {
  position: relative;
  display: inline-block;
  filter: drop-shadow(0 0 6px color-mix(in oklab,var(--cyb) 45%,transparent)) drop-shadow(0 0 18px color-mix(in oklab,var(--cyb) 22%,transparent));
  transition: filter .25s ease;
}

.gbb-04 .gbb-04__wrap:hover,
.gbb-04 .gbb-04__wrap:focus-within {
  filter: drop-shadow(0 0 8px color-mix(in oklab,var(--cyb) 70%,transparent)) drop-shadow(0 0 26px color-mix(in oklab,var(--cyb) 40%,transparent));
}

.gbb-04 .gbb-04__wrap:focus-within {
  outline: 2px solid var(--cyb);
  outline-offset: 6px;
}

.gbb-04 .gbb-04__btn {
  position: relative;
  cursor: pointer;
  border: 1px solid color-mix(in oklab,var(--cyb) 65%,transparent);
  padding: 16px 38px;
  font: 700 14px/1 ui-monospace,'Cascadia Code',Menlo,monospace;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--cyb);
  background: linear-gradient(180deg,color-mix(in oklab,var(--cyb) 14%,transparent),color-mix(in oklab,var(--cyb) 5%,transparent)),oklch(0.13 0.012 260);
  clip-path: polygon(14px 0,100% 0,100% calc(100% - 14px),calc(100% - 14px) 100%,0 100%,0 14px);
  outline: none;
  transition: color .2s ease,background .2s ease;
}

.gbb-04 .gbb-04__wrap::before,
.gbb-04 .gbb-04__wrap::after {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  border: 0 solid var(--cyb);
  transition: translate .2s ease;
  pointer-events: none;
  z-index: 2;
}

.gbb-04 .gbb-04__wrap::before {
  top: 0;
  left: 0;
  border-width: 2px 0 0 2px;
}

.gbb-04 .gbb-04__wrap::after {
  bottom: 0;
  right: 0;
  border-width: 0 2px 2px 0;
}

.gbb-04 .gbb-04__wrap:hover .gbb-04__btn {
  color: oklch(0.95 0.05 85);
  animation: gbb04-flicker .5s steps(2,jump-none) 1;
}

.gbb-04 .gbb-04__wrap:hover::before {
  translate: -2px -2px;
}

.gbb-04 .gbb-04__wrap:hover::after {
  translate: 2px 2px;
}

.gbb-04 .gbb-04__btn:active {
  transform: translateY(1px);
}

@keyframes gbb04-flicker {
  0% {
    opacity: 1;
  }

  25% {
    opacity: .55;
  }

  50% {
    opacity: 1;
  }

  75% {
    opacity: .75;
  }

  100% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-04 .gbb-04__wrap:hover .gbb-04__btn {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — clip-path cuts the corners; drop-shadow() on a wrapper draws the glow along the clipped silhouette (box-shadow can't). */
```
