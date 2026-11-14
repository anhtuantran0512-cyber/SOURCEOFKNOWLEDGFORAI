---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-brass-periscope-lens-button/"
title: "CSS Brass Periscope Lens Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A brass periscope objective: a knurled bezel, an engraved focus scale, and a six-blade iris that irises open on hover to reveal the glass — each blade a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Brass Periscope Lens Button
Source: https://codefronts.com/components/css-buttons/css-brass-periscope-lens-button/

A brass periscope objective: a knurled bezel, an engraved focus scale, and a six-blade iris that irises open on hover to reveal the glass — each blade a clipped triangle rotating about the optical centre, with a reflection sweep across the coated lens.
## HTML
```html
<div class="cb-51">
  <div class="cb-51__stage">
    <button class="cb-51__btn" type="button" aria-label="Open the viewfinder">
      <span class="cb-51__bezel" aria-hidden="true">
        <span class="cb-51__knurl"></span>
        <span class="cb-51__scale"></span>
        <span class="cb-51__barrel">
          <span class="cb-51__glass"></span>
          <span class="cb-51__iris">
            <span class="cb-51__blade" style="--i:0"></span>
            <span class="cb-51__blade" style="--i:1"></span>
            <span class="cb-51__blade" style="--i:2"></span>
            <span class="cb-51__blade" style="--i:3"></span>
            <span class="cb-51__blade" style="--i:4"></span>
            <span class="cb-51__blade" style="--i:5"></span>
          </span>
          <span class="cb-51__flare"></span>
        </span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&display=swap');

.cb-51 {
  --bg: #141613;
  --brass: #b28c4c;
  --brass-hi: #e8cc90;
  --brass-lo: #6f5426;
  --blade: #2a2b28;
  --blade-hi: #4a4b46;
  --glass: #1a3b46;
  --coat: #4fd6c9;
  --size: 9.5rem;
  --sans: "Oswald",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 44%, color-mix(in oklab,var(--brass) 14%,transparent), transparent 74%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-51 {
    --brass: oklch(66% .08 84);
    --brass-hi: oklch(86% .08 88);
    --brass-lo: oklch(45% .07 82);
    --coat: oklch(82% .12 182);
  }
}

@media (prefers-color-scheme: light) {
  .cb-51:not([data-theme="dark"]) {
    --bg: #1e211d;
  }
}

.cb-51[data-theme="light"] {
  --bg: #1e211d;
}

.cb-51,
.cb-51 *,
.cb-51 *::before,
.cb-51 *::after {
  box-sizing: border-box;
}

.cb-51__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-51__btn {
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0;
  font: inherit;
  -webkit-tap-highlight-color: transparent;
}

.cb-51__bezel {
  position: relative;
  display: grid;
  place-items: center;
  width: var(--size);
  height: var(--size);
  border-radius: 50%;
  background: radial-gradient(circle at 34% 26%, var(--brass-hi), transparent 56%), linear-gradient(150deg, var(--brass), var(--brass-lo));
  box-shadow: inset 0 2px 3px rgba(255,255,255,.45), inset 0 -3px 7px rgba(0,0,0,.55), 0 18px 28px -12px rgba(0,0,0,.85);
  transition: rotate .55s cubic-bezier(.16,1,.3,1), filter .3s ease;
}

.cb-51__knurl {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, rgba(255,255,255,.22) 0 1.4deg, rgba(0,0,0,.28) 1.4deg 3deg);
  -webkit-mask: radial-gradient(farthest-side, transparent 86%, #000 88%);
  mask: radial-gradient(farthest-side, transparent 86%, #000 88%);
}

.cb-51__scale {
  position: absolute;
  inset: 9%;
  border-radius: 50%;
  background: repeating-conic-gradient(from -90deg, var(--brass-lo) 0 1deg, transparent 1deg 15deg);
  -webkit-mask: radial-gradient(farthest-side, transparent 82%, #000 84%);
  mask: radial-gradient(farthest-side, transparent 82%, #000 84%);
  opacity: .75;
}

.cb-51__barrel {
  position: relative;
  display: grid;
  place-items: center;
  width: 66%;
  height: 66%;
  border-radius: 50%;
  overflow: hidden;
  background: radial-gradient(circle at 50% 50%, #101210, #050605);
  box-shadow: inset 0 0 0 3px color-mix(in oklab,var(--brass-lo) 80%,black), inset 0 4px 10px rgba(0,0,0,.9);
}

.cb-51__glass {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  z-index: 1;
  background: radial-gradient(circle at 62% 70%, color-mix(in oklab,var(--coat) 55%,transparent), transparent 58%), radial-gradient(circle at 34% 26%, rgba(255,255,255,.5), transparent 42%), radial-gradient(circle at 50% 50%, var(--glass), #08181d 78%);
}

.cb-51__iris {
  position: absolute;
  inset: 0;
  z-index: 2;
  border-radius: 50%;
}

.cb-51__blade {
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, var(--blade-hi), var(--blade));
  clip-path: polygon(50% 50%, 100% 6%, 100% 94%);
  rotate: calc(var(--i) * 60deg);
  transform-origin: 50% 50%;
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.5);
  transition: rotate .55s cubic-bezier(.16,1,.3,1), scale .55s cubic-bezier(.16,1,.3,1), opacity .4s ease;
}

.cb-51__flare {
  position: absolute;
  inset: -30%;
  z-index: 3;
  pointer-events: none;
  background: linear-gradient(104deg, transparent 42%, rgba(255,255,255,.42) 50%, transparent 58%);
  translate: -70% 0;
  transition: translate .9s cubic-bezier(.16,1,.3,1);
}

.cb-51__btn:is(:hover,:focus-visible) .cb-51__blade {
  rotate: calc(var(--i) * 60deg + 44deg);
  scale: .5;
}

.cb-51__btn:is(:hover,:focus-visible) .cb-51__flare {
  translate: 70% 0;
}

.cb-51__btn:hover .cb-51__bezel {
  filter: brightness(1.06);
}

.cb-51__btn:focus-visible {
  outline: none;
}

.cb-51__btn:focus-visible .cb-51__bezel {
  outline: 2px solid var(--brass-hi);
  outline-offset: 5px;
}

.cb-51__btn:active .cb-51__bezel {
  rotate: 6deg;
}

.cb-51__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.7) brightness(.85);
}

@media (prefers-reduced-motion: reduce) {
  .cb-51__bezel,
    .cb-51__blade,
    .cb-51__flare {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-51__bezel {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-51__knurl,
    .cb-51__scale,
    .cb-51__flare {
    display: none;
  }

  .cb-51__barrel {
    background: Canvas;
    box-shadow: inset 0 0 0 2px CanvasText;
  }

  .cb-51__blade {
    background: ButtonText;
  }
}
```
