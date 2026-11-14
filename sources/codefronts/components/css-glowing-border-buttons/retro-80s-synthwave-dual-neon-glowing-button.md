---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/retro-80s-synthwave-dual-neon-glowing-button/"
title: "Retro 80s Synthwave Dual Neon Glowing Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "Miami 1986: magenta and cyan tube-borders offset like misregistered chrome print, italic wide-tracked type with a sunset gradient fill, and a startup flicker…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro 80s Synthwave Dual Neon Glowing Button
Source: https://codefronts.com/components/css-glowing-border-buttons/retro-80s-synthwave-dual-neon-glowing-button/

Miami 1986: magenta and cyan tube-borders offset like misregistered chrome print, italic wide-tracked type with a sunset gradient fill, and a startup flicker that stutters the sign to life on hover — all against a perspective laser-grid floor drawn in two repeating-linear-gradients.
## HTML
```html
<section class="gbb-13" aria-label="Synthwave dual neon glowing button demo">
  <button class="gbb-13__btn" type="button">Play Mixtape</button>
</section>
```
## CSS
```css
.gbb-13,
.gbb-13 *,
.gbb-13 *::before,
.gbb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-13 {
  --mag: oklch(0.65 0.28 340);
  --cyn: oklch(0.82 0.14 200);
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: linear-gradient(180deg,oklch(0.16 0.05 300),oklch(0.12 0.03 280) 55%,oklch(0.1 0.02 260));
}

.gbb-13::before {
  content: "";
  position: absolute;
  left: -25%;
  right: -25%;
  bottom: -12%;
  height: 62%;
  z-index: -1;
  background: repeating-linear-gradient(90deg,color-mix(in oklab,var(--mag) 30%,transparent) 0 1px,transparent 1px 40px),repeating-linear-gradient(0deg,color-mix(in oklab,var(--mag) 22%,transparent) 0 1px,transparent 1px 40px);
  transform: perspective(320px) rotateX(60deg);
  transform-origin: 50% 0;
  mask: linear-gradient(180deg,transparent,#000 30%);
  -webkit-mask: linear-gradient(180deg,transparent,#000 30%);
}

.gbb-13 .gbb-13__btn {
  position: relative;
  cursor: pointer;
  border: 2px solid var(--mag);
  padding: 18px 42px;
  background: oklch(0.13 0.03 300 / .8);
  font: 800 italic 17px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .22em;
  text-transform: uppercase;
  background-clip: border-box;
  box-shadow: 0 0 10px color-mix(in oklab,var(--mag) 55%,transparent),inset 0 0 12px color-mix(in oklab,var(--mag) 18%,transparent);
  transition: box-shadow .25s ease;
}

.gbb-13 .gbb-13__btn {
  color: transparent;
}

.gbb-13 .gbb-13__btn {
  -webkit-background-clip: border-box;
}

.gbb-13 .gbb-13__btn::after {
  content: "PLAY MIXTAPE";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,oklch(0.92 0.06 60) 20%,var(--mag) 60%,oklch(0.85 0.1 340));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 0 7px color-mix(in oklab,var(--mag) 70%,transparent));
  font: inherit;
  letter-spacing: inherit;
}

.gbb-13 .gbb-13__btn::before {
  content: "";
  position: absolute;
  inset: -2px;
  border: 2px solid var(--cyn);
  translate: 5px 5px;
  pointer-events: none;
  box-shadow: 0 0 10px color-mix(in oklab,var(--cyn) 50%,transparent),inset 0 0 8px color-mix(in oklab,var(--cyn) 25%,transparent);
  transition: translate .25s ease;
}

.gbb-13 .gbb-13__btn:hover,
.gbb-13 .gbb-13__btn:focus-visible {
  animation: gbb13-flicker 1s steps(20,jump-none) 1 both;
  box-shadow: 0 0 16px color-mix(in oklab,var(--mag) 75%,transparent),0 0 42px color-mix(in oklab,var(--mag) 40%,transparent),inset 0 0 16px color-mix(in oklab,var(--mag) 25%,transparent);
}

.gbb-13 .gbb-13__btn:hover::before,
.gbb-13 .gbb-13__btn:focus-visible::before {
  translate: 3px 3px;
}

.gbb-13 .gbb-13__btn:focus-visible {
  outline: 2px solid var(--cyn);
  outline-offset: 8px;
}

.gbb-13 .gbb-13__btn:active {
  transform: scale(.98);
}

@keyframes gbb13-flicker {
  0% {
    opacity: 1;
  }

  9% {
    opacity: .4;
  }

  12% {
    opacity: 1;
  }

  21% {
    opacity: .6;
  }

  26% {
    opacity: 1;
  }

  44% {
    opacity: .85;
  }

  48%,
    100% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-13 .gbb-13__btn:hover,
    .gbb-13 .gbb-13__btn:focus-visible {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two offset neon borders (button + translated ::before), background-clip:text chrome type, and an irregular steps() startup flicker. */
```
