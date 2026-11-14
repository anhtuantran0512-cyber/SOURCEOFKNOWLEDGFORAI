---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/cyberpunk-cta-button-glow/"
title: "Cyberpunk CTA Button Glow"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A sharp, angular, aggressively-saturated action button for gaming portfolios, web3 drops and cyberpunk landing pages."
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk CTA Button Glow
Source: https://codefronts.com/motion/css-neon-text-effect/cyberpunk-cta-button-glow/

A sharp, angular, aggressively-saturated action button for gaming portfolios, web3 drops and cyberpunk landing pages. Clipped corners, a running edge scan and a hot double-colour glow that hardens on hover.
## HTML
```html
<div class="cnt-03">
  <button class="cnt-03__btn" type="button">
    <span class="cnt-03__txt">ENTER THE GRID</span>
  </button>
</div>
```
## CSS
```css
.cnt-03,
.cnt-03 *,
.cnt-03 *::before,
.cnt-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-03 ::selection {
  background: oklch(0.82 0.18 195);
  color: #03121a;
}

.cnt-03 {
  --c1: oklch(0.82 0.16 200);
  --c2: oklch(0.72 0.24 330);
  --scan: 2.4s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: linear-gradient(0deg,rgba(0,0,0,.6),rgba(0,0,0,.6)), repeating-linear-gradient(90deg,#0a0a0d 0 38px,#0d0d12 38px 39px), #08080b;
}

.cnt-03__btn {
  position: relative;
  isolation: isolate;
  cursor: pointer;
  padding: 22px 52px;
  border: none;
  background: linear-gradient(160deg,#12121a,#0a0a10);
  color: #eafcff;
  font-size: 18px;
  font-weight: 800;
  letter-spacing: .16em;
  clip-path: polygon(14px 0,100% 0,100% calc(100% - 14px),calc(100% - 14px) 100%,0 100%,0 14px);
  box-shadow: inset 0 0 0 1.5px color-mix(in oklch,var(--c1) 80%,var(--c2));
  text-shadow: 0 0 8px var(--c1),0 0 18px color-mix(in oklch,var(--c1) 60%,var(--c2));
  transition: color .25s,text-shadow .25s;
}

.cnt-03__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(transparent 46%,color-mix(in oklch,var(--c1) 50%,transparent) 50%,transparent 54%);
  background-size: 100% 6px;
  mix-blend-mode: screen;
  animation: cnt-03-scan var(--scan) linear infinite;
  opacity: .7;
}

.cnt-03__btn::after {
  content: "";
  position: absolute;
  inset: -2px;
  z-index: -1;
  clip-path: inherit;
  box-shadow: 0 0 18px color-mix(in oklch,var(--c1) 70%,transparent),0 0 46px color-mix(in oklch,var(--c2) 55%,transparent);
  opacity: .6;
  transition: opacity .25s,box-shadow .25s;
}

.cnt-03__btn:hover,
.cnt-03__btn:focus-visible {
  outline: none;
  color: #fff;
  --scan: 1.1s;
  text-shadow: 0 0 8px #fff,0 0 20px var(--c1),0 0 40px var(--c2);
}

.cnt-03__btn:hover::after,
.cnt-03__btn:focus-visible::after {
  opacity: 1;
  box-shadow: 0 0 26px var(--c1),0 0 70px color-mix(in oklch,var(--c2) 70%,transparent);
}

.cnt-03__btn:active {
  transform: translateY(1px);
}

@keyframes cnt-03-scan {
  from {
    background-position: 0 -8px;
  }

  to {
    background-position: 0 44px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-03__btn::before {
    animation: none;
    opacity: .35;
  }
}
```

## JavaScript
```js
/* No JavaScript — clip-path shape, animated scanline and dual-hue glow are all CSS. */
```
