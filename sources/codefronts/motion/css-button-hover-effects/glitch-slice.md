---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/glitch-slice/"
title: "Glitch Slice"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A digital-distortion CTA: on hover the button splits into horizontal slices that jump out of alignment before snapping back — a sharp data-corruption glitch."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Slice
Source: https://codefronts.com/motion/css-button-hover-effects/glitch-slice/

A digital-distortion CTA: on hover the button splits into horizontal slices that jump out of alignment before snapping back — a sharp data-corruption glitch.
## HTML
```html
<div class="bhe-17-group">
<section class="bhe-17a" aria-label="Glitch slice button">
  <button class="bhe-17a__btn" type="button" data-text="Play now"><span>Play now</span></button>
</section>
<section class="bhe-17b" aria-label="Skew glitch button">
  <button class="bhe-17b__btn" type="button" data-text="Deploy"><span>Deploy</span></button>
</section>
</div>
```
## CSS
```css
.bhe-17-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-17-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-17a,
.bhe-17a *,
.bhe-17a *::before,
.bhe-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-17a {
  font-family: ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a0a12;
}

.bhe-17a__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #eafcff;
  padding: 16px 40px;
  border: 1px solid #2af;
  border-radius: 6px;
  cursor: pointer;
  background: #0f1226;
}

.bhe-17a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-17a__btn::before,
.bhe-17a__btn::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: inherit;
  letter-spacing: .14em;
  background: #0f1226;
  pointer-events: none;
}

.bhe-17a__btn::before {
  color: #22e3ff;
  clip-path: inset(0 0 55% 0);
}

.bhe-17a__btn::after {
  color: #ff2bd6;
  clip-path: inset(55% 0 0 0);
}

.bhe-17a__btn:hover::before {
  animation: bhe-17a-a .4s steps(3) infinite;
}

.bhe-17a__btn:hover::after {
  animation: bhe-17a-b .4s steps(3) infinite;
}

.bhe-17a__btn:focus-visible {
  outline: 3px solid #22e3ff;
  outline-offset: 4px;
}

@keyframes bhe-17a-a {
  0% {
    transform: translateX(0);
  }

  33% {
    transform: translateX(-5px);
  }

  66% {
    transform: translateX(4px);
  }

  100% {
    transform: translateX(0);
  }
}

@keyframes bhe-17a-b {
  0% {
    transform: translateX(0);
  }

  33% {
    transform: translateX(5px);
  }

  66% {
    transform: translateX(-4px);
  }

  100% {
    transform: translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-17a__btn:hover::before,
    .bhe-17a__btn:hover::after {
    animation: none;
  }
}

.bhe-17b,
.bhe-17b *,
.bhe-17b *::before,
.bhe-17b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-17b {
  font-family: ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #100810;
}

.bhe-17b__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #fff;
  padding: 16px 42px;
  border: 1px solid #ff4dd2;
  border-radius: 6px;
  cursor: pointer;
  background: #1a0e1a;
}

.bhe-17b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-17b__btn::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: inherit;
  letter-spacing: .16em;
  color: #4dd2ff;
  background: #1a0e1a;
  opacity: 0;
  pointer-events: none;
}

.bhe-17b__btn:hover::before {
  opacity: .85;
  animation: bhe-17b-tear .35s steps(2) infinite;
}

.bhe-17b__btn:focus-visible {
  outline: 3px solid #ff4dd2;
  outline-offset: 4px;
}

@keyframes bhe-17b-tear {
  0% {
    transform: skewX(0) translateX(0);
    clip-path: inset(0 0 70% 0);
  }

  50% {
    transform: skewX(-14deg) translateX(-4px);
    clip-path: inset(40% 0 20% 0);
  }

  100% {
    transform: skewX(0) translateX(0);
    clip-path: inset(0 0 70% 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-17b__btn:hover::before {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
