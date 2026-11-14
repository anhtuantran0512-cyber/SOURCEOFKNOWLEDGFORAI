---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/magnetic-border/"
title: "Magnetic Border"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A subtle high-craft CTA where the outlined frame drifts toward the cursor as it approaches, lagging behind with an elastic settle — restrained and premium."
has_js: "true"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Border
Source: https://codefronts.com/motion/css-button-hover-effects/magnetic-border/

A subtle high-craft CTA where the outlined frame drifts toward the cursor as it approaches, lagging behind with an elastic settle — restrained and premium.
## HTML
```html
<div class="bhe-16-group">
<section class="bhe-16a" aria-label="Magnetic border button">
  <div class="bhe-16a__wrap" id="bhe-16a-wrap"><button class="bhe-16a__btn" type="button"><span class="bhe-16a__label">Let's talk</span></button></div>
</section>
<section class="bhe-16b" aria-label="Magnetic filled button">
  <div class="bhe-16b__wrap" id="bhe-16b-wrap"><button class="bhe-16b__btn" type="button"><span class="bhe-16b__label">Hire us</span></button></div>
</section>
</div>
```
## CSS
```css
.bhe-16-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-16-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-16a,
.bhe-16a *,
.bhe-16a *::before,
.bhe-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-16a {
  --edge: oklch(0.7 0.14 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #141210;
}

.bhe-16a__wrap {
  padding: 34px;
  display: grid;
  place-items: center;
}

.bhe-16a__btn {
  position: relative;
  font-size: 16px;
  font-weight: 700;
  color: var(--edge);
  padding: 18px 42px;
  border: 2px solid var(--edge);
  border-radius: 9999px;
  cursor: pointer;
  background: transparent;
  transform: translate(calc(var(--dx,0)*14px),calc(var(--dy,0)*14px));
  transition: transform .5s cubic-bezier(.34,1.56,.64,1),background .3s,color .3s;
}

.bhe-16a__label {
  display: inline-block;
  transform: translate(calc(var(--dx,0)*6px),calc(var(--dy,0)*6px));
  transition: transform .5s cubic-bezier(.34,1.56,.64,1);
}

.bhe-16a__btn:hover {
  background: var(--edge);
  color: #141210;
}

.bhe-16a__btn:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-16a__btn,
    .bhe-16a__label {
    transition: background .2s,color .2s;
  }
}

.bhe-16b,
.bhe-16b *,
.bhe-16b *::before,
.bhe-16b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-16b {
  --accent: oklch(0.6 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0c0a18;
}

.bhe-16b__wrap {
  padding: 40px;
  display: grid;
  place-items: center;
}

.bhe-16b__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 18px 44px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--accent);
  box-shadow: 0 14px 30px -14px var(--accent);
  transform: translate(calc(var(--dx,0)*18px),calc(var(--dy,0)*18px));
  transition: transform .45s cubic-bezier(.34,1.56,.64,1),box-shadow .3s;
}

.bhe-16b__label {
  display: inline-block;
  transform: translate(calc(var(--dx,0)*8px),calc(var(--dy,0)*8px));
  transition: transform .45s cubic-bezier(.34,1.56,.64,1);
}

.bhe-16b__btn:hover {
  box-shadow: 0 22px 44px -16px var(--accent);
}

.bhe-16b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-16b__btn,
    .bhe-16b__label {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
(() => {
  const wrap = document.querySelector('#bhe-16a-wrap'); if (!wrap) return;
  const btn = wrap.querySelector('.bhe-16a__btn');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  wrap.addEventListener('pointermove', e => { const r=wrap.getBoundingClientRect(); btn.style.setProperty('--dx',((e.clientX-r.left)/r.width-.5).toFixed(3)); btn.style.setProperty('--dy',((e.clientY-r.top)/r.height-.5).toFixed(3)); });
  wrap.addEventListener('pointerleave', () => { btn.style.setProperty('--dx','0'); btn.style.setProperty('--dy','0'); });
})();
(() => {
  const wrap = document.querySelector('#bhe-16b-wrap'); if (!wrap) return;
  const btn = wrap.querySelector('.bhe-16b__btn');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  wrap.addEventListener('pointermove', e => { const r=wrap.getBoundingClientRect(); btn.style.setProperty('--dx',((e.clientX-r.left)/r.width-.5).toFixed(3)); btn.style.setProperty('--dy',((e.clientY-r.top)/r.height-.5).toFixed(3)); });
  wrap.addEventListener('pointerleave', () => { btn.style.setProperty('--dx','0'); btn.style.setProperty('--dy','0'); });
})();
```
