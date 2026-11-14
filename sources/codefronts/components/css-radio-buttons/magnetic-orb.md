---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/magnetic-orb/"
title: "Interactive 3D Sphere Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Radio options rendered as glossy 3D orbs — layered radial gradients build the sphere illusion, a specular highlight tracks your cursor across each orb (tiny…"
has_js: "true"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive 3D Sphere Radio
Source: https://codefronts.com/components/css-radio-buttons/magnetic-orb/

Radio options rendered as glossy 3D orbs — layered radial gradients build the sphere illusion, a specular highlight tracks your cursor across each orb (tiny JS writing two custom properties), and the checked orb earns a slowly orbiting ring. A show-piece selector for themes, planets or difficulty levels.
## HTML
```html
<div class="crb-09-group">
<section class="crb-09a" aria-label="Interactive 3D sphere radio buttons">
  <fieldset class="crb-09a__group" id="crb-09a-group">
    <legend class="crb-09a__legend">Pick your world</legend>
    <div class="crb-09a__row">
      <label class="crb-09a__opt" style="--c:oklch(0.62 0.19 25)">
        <input class="crb-09a__input" type="radio" name="crb-09a" value="ember" checked>
        <span class="crb-09a__orb" aria-hidden="true"></span>
        <span class="crb-09a__name">Ember</span>
      </label>
      <label class="crb-09a__opt" style="--c:oklch(0.62 0.15 230)">
        <input class="crb-09a__input" type="radio" name="crb-09a" value="tide">
        <span class="crb-09a__orb" aria-hidden="true"></span>
        <span class="crb-09a__name">Tide</span>
      </label>
      <label class="crb-09a__opt" style="--c:oklch(0.68 0.16 145)">
        <input class="crb-09a__input" type="radio" name="crb-09a" value="moss">
        <span class="crb-09a__orb" aria-hidden="true"></span>
        <span class="crb-09a__name">Moss</span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-09-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-09-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-09a,
.crb-09a *,
.crb-09a *::before,
.crb-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-09a {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(130% 110% at 50% -10%,#171c2e,#0a0c14);
}

.crb-09a__group {
  border: none;
}

.crb-09a__legend {
  font-size: 24px;
  font-weight: 750;
  color: #eef1fa;
  letter-spacing: -.02em;
  text-align: center;
}

.crb-09a__row {
  display: flex;
  flex-wrap: wrap;
  gap: 36px;
  justify-content: center;
  margin-top: 30px;
}

.crb-09a__opt {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 14px;
  cursor: pointer;
}

.crb-09a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-09a__orb {
  position: relative;
  width: 96px;
  height: 96px;
  border-radius: 50%;
  background: radial-gradient(circle at 32% 28%,color-mix(in oklab,var(--c) 55%,white),var(--c) 46%,color-mix(in oklab,var(--c) 45%,black) 88%);
  box-shadow: inset -14px -16px 28px rgba(0,0,0,.45),inset 6px 8px 16px rgba(255,255,255,.18),0 18px 34px -14px color-mix(in oklab,var(--c) 55%,transparent);
  transition: transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .35s;
}

.crb-09a__orb::before {
  content: "";
  position: absolute;
  top: 14%;
  left: 18%;
  width: 30%;
  height: 22%;
  border-radius: 50%;
  background: radial-gradient(closest-side,rgba(255,255,255,.85),transparent);
  filter: blur(1px);
  transform: translate(var(--hx,0px),var(--hy,0px));
  transition: transform .15s linear;
}

.crb-09a__orb::after {
  content: "";
  position: absolute;
  inset: -14px;
  border-radius: 50%;
  border: 2px solid color-mix(in oklab,var(--c) 75%,white);
  border-top-color: transparent;
  border-bottom-color: transparent;
  opacity: 0;
  transform: rotate(20deg);
  transition: opacity .3s;
}

.crb-09a__name {
  font-size: 14px;
  font-weight: 650;
  color: #aab2cc;
  transition: color .25s;
}

.crb-09a__opt:hover .crb-09a__orb {
  transform: translateY(-5px);
}

.crb-09a__opt:has(.crb-09a__input:checked) .crb-09a__orb {
  transform: scale(1.07);
  box-shadow: inset -14px -16px 28px rgba(0,0,0,.45),inset 6px 8px 16px rgba(255,255,255,.18),0 24px 44px -14px color-mix(in oklab,var(--c) 75%,transparent);
}

.crb-09a__opt:has(.crb-09a__input:checked) .crb-09a__orb::after {
  opacity: 1;
  animation: crb-09a-orbit 4s linear infinite;
}

.crb-09a__opt:has(.crb-09a__input:checked) .crb-09a__name {
  color: #fff;
}

.crb-09a__opt:has(.crb-09a__input:focus-visible) .crb-09a__orb {
  outline: 3px solid #fff;
  outline-offset: 5px;
}

@keyframes crb-09a-orbit {
  to {
    transform: rotate(380deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-09a__orb,
    .crb-09a__orb::before {
    transition: none;
  }

  .crb-09a__opt:has(.crb-09a__input:checked) .crb-09a__orb::after {
    animation: none;
    opacity: 1;
  }

  .crb-09a__opt:hover .crb-09a__orb {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const init = () => {
    const group = document.querySelector('#crb-09a-group'); if (!group) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const PULL = 10;
    group.querySelectorAll('.crb-09a__orb').forEach((orb) => {
      const opt = orb.closest('.crb-09a__opt');
      opt.addEventListener('pointermove', (e) => {
        const r = orb.getBoundingClientRect();
        orb.style.setProperty('--hx', (((e.clientX - r.left) / r.width - .5) * PULL).toFixed(1) + 'px');
        orb.style.setProperty('--hy', (((e.clientY - r.top) / r.height - .5) * PULL).toFixed(1) + 'px');
      }, { passive: true });
      opt.addEventListener('pointerleave', () => { orb.style.setProperty('--hx', '0px'); orb.style.setProperty('--hy', '0px'); });
    });
  };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
```
