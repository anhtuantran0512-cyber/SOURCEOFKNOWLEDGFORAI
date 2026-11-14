---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/magnetic-cross/"
title: "Magnetic Cross Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The award-site micro-interaction: as the cursor approaches, the × leans toward it — pulled by an invisible magnetic field — then snaps elastically home when…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Cross Close Button
Source: https://codefronts.com/components/css-close-buttons/magnetic-cross/

The award-site micro-interaction: as the cursor approaches, the × leans toward it — pulled by an invisible magnetic field — then snaps elastically home when the cursor leaves. Ten lines of pointer math feed two CSS custom properties; CSS does all the actual motion, so the effect stays 60fps and fully degradable.
## HTML
```html
<section class="ccb-14" aria-label="Magnetic close button demo">
  <div class="ccb-14__zone" id="ccb-14-zone">
    <button class="ccb-14__close" type="button" aria-label="Close">
      <span class="ccb-14__x" aria-hidden="true"></span>
    </button>
  </div>
</section>
```
## CSS
```css
.ccb-14,
.ccb-14 *,
.ccb-14 *::before,
.ccb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-14 {
  --accent: oklch(0.72 0.17 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 120% at 50% 0%,oklch(0.24 0.04 160 / .9),transparent 60%),oklch(0.16 0.02 170);
}

.ccb-14 .ccb-14__zone {
  --mx: 0px;
  --my: 0px;
  --gx: 0px;
  --gy: 0px;
  display: grid;
  place-items: center;
  width: 170px;
  height: 170px;
  border-radius: 50%;
}

.ccb-14 .ccb-14__close {
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border: 1.5px solid oklch(0.72 0.17 150 / .4);
  border-radius: 50%;
  background: oklch(0.2 0.03 165);
  cursor: pointer;
  transform: translate3d(var(--mx),var(--my),0);
  transition: transform .08s linear,border-color .2s ease;
  box-shadow: 0 16px 36px -18px rgba(0,0,0,.8);
}

.ccb-14 .ccb-14__x {
  position: relative;
  width: 20px;
  height: 20px;
  transform: translate3d(var(--gx),var(--gy),0);
  transition: transform .08s linear;
}

.ccb-14 .ccb-14__x::before,
.ccb-14 .ccb-14__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 2px;
  border-radius: 2px;
  background: var(--accent);
}

.ccb-14 .ccb-14__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-14 .ccb-14__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-14 .ccb-14__zone.is-releasing .ccb-14__close,
.ccb-14 .ccb-14__zone.is-releasing .ccb-14__x {
  transition: transform .5s cubic-bezier(.34,1.8,.44,1);
}

.ccb-14 .ccb-14__close:hover {
  border-color: var(--accent);
}

.ccb-14 .ccb-14__close:active {
  transform: translate3d(var(--mx),var(--my),0) scale(.92);
}

.ccb-14 .ccb-14__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
```

## JavaScript
```js
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const zone = document.getElementById('ccb-14-zone'); if (!zone) return;
  const MAX = 14;
  const clamp = (v) => Math.max(-MAX, Math.min(MAX, v));
  zone.addEventListener('pointermove', (e) => {
    zone.classList.remove('is-releasing');
    const r = zone.getBoundingClientRect();
    const dx = e.clientX - (r.left + r.width / 2);
    const dy = e.clientY - (r.top + r.height / 2);
    zone.style.setProperty('--mx', clamp(dx * 0.3) + 'px');
    zone.style.setProperty('--my', clamp(dy * 0.3) + 'px');
    zone.style.setProperty('--gx', clamp(dx * 0.45) + 'px');  // glyph leads the chase
    zone.style.setProperty('--gy', clamp(dy * 0.45) + 'px');
  });
  zone.addEventListener('pointerleave', () => {
    zone.classList.add('is-releasing');                        // swap to elastic bezier
    ['--mx','--my','--gx','--gy'].forEach(p => zone.style.setProperty(p, '0px'));
  });
})();
```
