---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/magnetic-ripple-attraction/"
title: "Magnetic Ripple Attraction"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A premium CTA that feels physically alive: as the cursor enters, a soft ripple grows from the pointer position and the label nudges toward the cursor like…"
has_js: "true"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Ripple Attraction
Source: https://codefronts.com/motion/css-button-hover-effects/magnetic-ripple-attraction/

A premium CTA that feels physically alive: as the cursor enters, a soft ripple grows from the pointer position and the label nudges toward the cursor like it's magnetically attracted — mapped with elastic easing so it overshoots before settling.
## HTML
```html
<div class="bhe-01-group">
<section class="bhe-01a" aria-label="Magnetic ripple button">
  <button class="bhe-01a__btn" id="bhe-01a-btn" type="button"><span class="bhe-01a__ripple" aria-hidden="true"></span><span class="bhe-01a__label">Get started</span></button>
</section>
<section class="bhe-01b" aria-label="Magnetic colour-fill ripple button">
  <button class="bhe-01b__btn" id="bhe-01b-btn" type="button"><span class="bhe-01b__fill" aria-hidden="true"></span><span class="bhe-01b__label">Add to cart</span></button>
</section>
<section class="bhe-01c" aria-label="Magnetic glow button">
  <button class="bhe-01c__btn" type="button"><span class="bhe-01c__label">Subscribe</span></button>
</section>
</div>
```
## CSS
```css
.bhe-01-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-01-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-01a,
.bhe-01a *,
.bhe-01a *::before,
.bhe-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-01a {
  --accent: oklch(0.62 0.21 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: radial-gradient(120% 120% at 50% 0%,#241a3d,#0f0a1e);
}

.bhe-01a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 17px;
  font-weight: 700;
  color: #fff;
  padding: 18px 42px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 86%,white),var(--accent));
  box-shadow: 0 16px 34px -14px color-mix(in oklab,var(--accent) 70%,transparent);
  transform: translate(var(--tx,0),var(--ty,0));
  transition: transform .5s cubic-bezier(.34,1.56,.64,1),box-shadow .3s;
}

.bhe-01a__ripple {
  position: absolute;
  left: var(--mx,50%);
  top: var(--my,50%);
  width: 16px;
  height: 16px;
  margin: -8px 0 0 -8px;
  border-radius: 50%;
  background: rgba(255,255,255,.55);
  transform: scale(0);
  opacity: 0;
  transition: transform .55s cubic-bezier(.22,1,.36,1),opacity .6s;
  pointer-events: none;
  z-index: -1;
}

.bhe-01a__label {
  position: relative;
  z-index: 1;
}

.bhe-01a__btn:hover .bhe-01a__ripple,
.bhe-01a__btn:focus-visible .bhe-01a__ripple {
  transform: scale(2.5);
  opacity: 1;
}

.bhe-01a__btn:active {
  transform: translate(var(--tx,0),var(--ty,0)) scale(.96);
}

.bhe-01a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-01a__btn {
    transition: box-shadow .2s;
  }

  .bhe-01a__ripple {
    transition: opacity .2s;
  }
}

.bhe-01b,
.bhe-01b *,
.bhe-01b *::before,
.bhe-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-01b {
  --edge: oklch(0.6 0.19 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #071417;
}

.bhe-01b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 17px;
  font-weight: 800;
  color: var(--edge);
  padding: 18px 44px;
  border: 2px solid var(--edge);
  border-radius: 12px;
  cursor: pointer;
  background: transparent;
  transition: color .3s;
}

.bhe-01b__label {
  position: relative;
  z-index: 1;
}

.bhe-01b__fill {
  position: absolute;
  left: var(--mx,50%);
  top: var(--my,50%);
  width: 20px;
  height: 20px;
  margin: -10px 0 0 -10px;
  border-radius: 50%;
  background: var(--edge);
  transform: scale(0);
  transition: transform .5s cubic-bezier(.22,1,.36,1);
  pointer-events: none;
  z-index: 0;
}

.bhe-01b__btn:hover,
.bhe-01b__btn:focus-visible {
  color: #04191d;
}

.bhe-01b__btn:hover .bhe-01b__fill,
.bhe-01b__btn:focus-visible .bhe-01b__fill {
  transform: scale(30);
}

.bhe-01b__btn:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-01b__fill {
    transition: transform .25s;
  }
}

.bhe-01c,
.bhe-01c *,
.bhe-01c *::before,
.bhe-01c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-01c {
  --accent: oklch(0.65 0.2 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #150913;
}

.bhe-01c__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  padding: 18px 44px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: color-mix(in oklab,var(--accent) 28%,#150913);
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--accent) 50%,transparent);
  transition: transform .3s,box-shadow .3s;
}

.bhe-01c__label {
  position: relative;
  z-index: 1;
}

.bhe-01c__btn::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 300%;
  aspect-ratio: 1;
  transform: translate(-50%,-50%);
  background: conic-gradient(from 0deg,transparent,var(--accent),transparent 40%);
  opacity: 0;
  transition: opacity .35s;
  animation: bhe-01c-spin 3s linear infinite;
  z-index: 0;
}

.bhe-01c__btn:hover,
.bhe-01c__btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--accent) 70%,transparent),0 10px 30px -10px var(--accent);
}

.bhe-01c__btn:hover::before,
.bhe-01c__btn:focus-visible::before {
  opacity: .9;
}

.bhe-01c__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@keyframes bhe-01c-spin {
  to {
    transform: translate(-50%,-50%) rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-01c__btn::before {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('#bhe-01a-btn'); if (!btn) return;
  const PULL = 6; const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  btn.addEventListener('pointermove', e => {
    const r = btn.getBoundingClientRect();
    btn.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    btn.style.setProperty('--my', (e.clientY - r.top) + 'px');
    if (!reduce){ btn.style.setProperty('--tx', (((e.clientX-r.left)/r.width-.5)*PULL).toFixed(1)+'px'); btn.style.setProperty('--ty', (((e.clientY-r.top)/r.height-.5)*PULL).toFixed(1)+'px'); }
  });
  btn.addEventListener('pointerleave', () => { btn.style.setProperty('--tx','0px'); btn.style.setProperty('--ty','0px'); });
})();
(() => {
  const btn = document.querySelector('#bhe-01b-btn'); if (!btn) return;
  btn.addEventListener('pointerenter', e => { const r=btn.getBoundingClientRect(); btn.style.setProperty('--mx',(e.clientX-r.left)+'px'); btn.style.setProperty('--my',(e.clientY-r.top)+'px'); });
  btn.addEventListener('focus', () => { btn.style.setProperty('--mx','50%'); btn.style.setProperty('--my','50%'); });
})();
/* No JavaScript — a masked conic-gradient sweep behind the fill fakes a magnetic light trail on :hover; pure CSS. */
```
