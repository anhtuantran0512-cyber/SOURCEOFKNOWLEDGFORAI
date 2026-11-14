---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-slider-range-input/"
title: "Liquid Glass Slider / Range Input"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A premium range control where the track is translucent glass and the thumb is a heavy glass lens that magnifies and refracts the value scale beneath it as…"
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Slider / Range Input
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-slider-range-input/

A premium range control where the track is translucent glass and the thumb is a heavy glass lens that magnifies and refracts the value scale beneath it as you drag. Replaces the default browser slider with something that feels like sliding a real lens across a ruler.
## HTML
```html
<section class="lg-13" id="lg-13-root" aria-label="Liquid glass range slider">
  <div class="lg-13__wrap" style="--v:40">
    <div class="lg-13__scale" aria-hidden="true"><span>0</span><span>25</span><span>50</span><span>75</span><span>100</span></div>
    <div class="lg-13__track" aria-hidden="true"><div class="lg-13__fill"></div></div>
    <div class="lg-13__lens" aria-hidden="true"><span class="lg-13__mag" id="lg-13-mag">40</span></div>
    <input class="lg-13__input" id="lg-13-input" type="range" min="0" max="100" value="40" aria-label="Quality">
  </div>
</section>
```
## CSS
```css
.lg-13,
.lg-13 *,
.lg-13 *::before,
.lg-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-13 {
  --accent: oklch(0.7 0.17 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  background: radial-gradient(circle at 30% 30%,#1c3050,#0d1424);
}

.lg-13__wrap {
  position: relative;
  width: min(440px,90vw);
  height: 120px;
}

.lg-13__scale {
  position: absolute;
  top: 34px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  font-size: 26px;
  font-weight: 800;
  color: rgba(255,255,255,.14);
  pointer-events: none;
}

.lg-13__track {
  position: absolute;
  top: 54px;
  left: 0;
  right: 0;
  height: 10px;
  border-radius: 999px;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.5);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  overflow: hidden;
}

.lg-13__fill {
  position: absolute;
  inset: 0;
  width: calc(var(--v)*1%);
  background: linear-gradient(90deg,color-mix(in oklab,var(--accent) 60%,transparent),var(--accent));
  box-shadow: 0 0 16px color-mix(in oklab,var(--accent) 70%,transparent);
}

.lg-13__lens {
  position: absolute;
  top: 59px;
  left: calc(var(--v)*1%);
  transform: translate(-50%,-50%);
  width: 56px;
  height: 56px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.6);
  box-shadow: inset 0 2px 6px rgba(255,255,255,.5),inset 0 -6px 12px rgba(0,0,0,.35),0 10px 24px -8px rgba(0,0,0,.6);
  backdrop-filter: blur(3px) saturate(160%) brightness(1.1);
  -webkit-backdrop-filter: blur(3px) saturate(160%) brightness(1.1);
  pointer-events: none;
  transition: box-shadow .2s;
}

.lg-13__mag {
  font-size: 24px;
  font-weight: 900;
  color: #fff;
  text-shadow: 0 1px 4px rgba(0,0,0,.5);
  transform: scale(1.15);
}

.lg-13__input {
  position: absolute;
  top: 44px;
  left: -8px;
  width: calc(100% + 16px);
  height: 40px;
  margin: 0;
  background: transparent;
  -webkit-appearance: none;
  appearance: none;
  cursor: grab;
  opacity: 0;
}

.lg-13__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 56px;
  height: 56px;
}

.lg-13__input::-moz-range-thumb {
  width: 56px;
  height: 56px;
  border: none;
  background: transparent;
}

.lg-13__input:active {
  cursor: grabbing;
}

.lg-13__input:focus-visible+.lg-13__lens,
.lg-13__root:has(.lg-13__input:focus-visible) .lg-13__lens {
  box-shadow: 0 0 0 3px #fff,inset 0 2px 6px rgba(255,255,255,.5);
}

@media (prefers-reduced-motion: reduce) {
  .lg-13__lens {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-13-root');
  const input = root.querySelector('#lg-13-input');
  const wrap = root.querySelector('.lg-13__wrap');
  const mag = root.querySelector('#lg-13-mag');
  function sync(){ wrap.style.setProperty('--v', input.value); mag.textContent = input.value; }
  input.addEventListener('input', sync);
  input.addEventListener('focus', () => root.querySelector('.lg-13__lens').style.boxShadow = '0 0 0 3px #fff, inset 0 2px 6px rgba(255,255,255,.5)');
  input.addEventListener('blur', () => root.querySelector('.lg-13__lens').style.boxShadow = '');
  sync();
})();
```
