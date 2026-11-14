---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/donut-sectors/"
title: "Donut Segment Radial Dropdown"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A segmented ring dropdown: tap the trigger and five donut sectors draw themselves around it, each an SVG arc stroke that thickens on hover like a physical…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Donut Segment Radial Dropdown
Source: https://codefronts.com/navigation/css-circular-menus/donut-sectors/

A segmented ring dropdown: tap the trigger and five donut sectors draw themselves around it, each an SVG arc stroke that thickens on hover like a physical dial detent. The hole in the middle keeps the trigger visible and tappable at all times — the layout advantage donuts have over full pies.
## HTML
```html
<section class="ccm-13" aria-label="Donut segment dropdown demo">
  <div class="ccm-13__stage">
    <div class="ccm-13__hub">
      <svg class="ccm-13__ring" viewBox="0 0 300 300" aria-hidden="true"></svg>
      <ul class="ccm-13__labels" id="ccm13-menu"></ul>
      <button type="button" class="ccm-13__trigger" aria-expanded="false" aria-controls="ccm13-menu">Menu</button>
    </div>
    <p class="ccm-13__note">SVG stroke segments · dashoffset draw-in</p>
  </div>
</section>
```
## CSS
```css
.ccm-13,
.ccm-13 *,
.ccm-13 *::before,
.ccm-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-13 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.25 0.03 250),oklch(0.18 0.025 260));
  --brand: oklch(0.68 0.14 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.92 0.01 230);
}

.ccm-13__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.25 0.03 250),oklch(0.18 0.025 260));
  overflow: hidden;
}

.ccm-13__hub {
  position: relative;
  width: 300px;
  height: 300px;
  display: grid;
  place-items: center;
}

.ccm-13__ring {
  position: absolute;
  inset: 0;
  overflow: visible;
}

.ccm-13__ring path {
  fill: none;
  stroke: var(--seg);
  stroke-width: 34;
  stroke-linecap: butt;
  stroke-dasharray: var(--len);
  stroke-dashoffset: var(--len);
  opacity: 0;
  transition: stroke-dashoffset .55s cubic-bezier(.3,1,.4,1),opacity .2s,stroke-width .25s cubic-bezier(.34,1.4,.4,1);
  transition-delay: var(--d);
}

.ccm-13__hub.is-open .ccm-13__ring path {
  stroke-dashoffset: 0;
  opacity: 1;
}

.ccm-13__ring path.is-hot {
  stroke-width: 44;
}

.ccm-13__labels {
  position: absolute;
  inset: 0;
  list-style: none;
  pointer-events: none;
}

.ccm-13__labels li {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: calc(var(--x) - 50%) calc(var(--y) - 50%);
}

.ccm-13__labels button {
  pointer-events: auto;
  border: none;
  background: none;
  color: #fff;
  font: 600 12.5px/1.2 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .03em;
  cursor: pointer;
  opacity: 0;
  translate: 0 4px;
  transition: opacity .3s,translate .3s;
  transition-delay: calc(var(--d) + .25s);
  padding: 10px 6px;
  text-shadow: 0 1px 3px oklch(0.2 0.03 250);
}

.ccm-13__hub.is-open .ccm-13__labels button {
  opacity: 1;
  translate: 0 0;
}

.ccm-13__hub:not(.is-open) .ccm-13__labels button {
  pointer-events: none;
}

.ccm-13__labels button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
  border-radius: 6px;
}

.ccm-13__trigger {
  position: relative;
  z-index: 2;
  width: 104px;
  height: 104px;
  border: 1px solid oklch(0.6 0.08 230 / .5);
  border-radius: 50%;
  background: radial-gradient(circle at 36% 30%,oklch(0.34 0.04 245),oklch(0.24 0.03 255));
  color: #fff;
  font: 700 15px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .06em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 16px 40px -16px oklch(0 0 0 / .8),inset 0 1px 0 oklch(1 0 0 / .12);
  transition: box-shadow .3s;
}

.ccm-13__hub.is-open .ccm-13__trigger {
  box-shadow: 0 0 0 6px oklch(0.68 0.14 230 / .25),0 16px 40px -16px oklch(0 0 0 / .8);
}

.ccm-13__trigger:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 4px;
}

.ccm-13__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.65 0.06 230 / .55);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-13 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const items = [
    { label: 'Overview', color: 'oklch(0.68 0.14 230)' },
    { label: 'Projects', color: 'oklch(0.72 0.15 195)' },
    { label: 'Team', color: 'oklch(0.75 0.14 160)' },
    { label: 'Billing', color: 'oklch(0.78 0.14 85)' },
    { label: 'Settings', color: 'oklch(0.68 0.17 320)' },
  ];
  const hub = document.querySelector('.ccm-13__hub');
  const svg = hub.querySelector('.ccm-13__ring');
  const labels = hub.querySelector('.ccm-13__labels');
  const trigger = hub.querySelector('.ccm-13__trigger');
  const C = 150, R = 108, GAP = 5; // center, radius, gap in degrees
  const seg = 360 / items.length;
  const pt = (deg) => {
    const a = (deg - 90) * Math.PI / 180;
    return (C + R * Math.cos(a)).toFixed(2) + ' ' + (C + R * Math.sin(a)).toFixed(2);
  };
  items.forEach((it, i) => {
    const a0 = i * seg + GAP / 2, a1 = (i + 1) * seg - GAP / 2;
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'M ' + pt(a0) + ' A ' + R + ' ' + R + ' 0 0 1 ' + pt(a1));
    path.style.setProperty('--seg', it.color);
    path.style.setProperty('--d', (i * 70) + 'ms');
    svg.append(path);
    path.style.setProperty('--len', path.getTotalLength().toFixed(1));
    const mid = ((a0 + a1) / 2 - 90) * Math.PI / 180;
    const li = document.createElement('li');
    li.style.setProperty('--x', (Math.cos(mid) * R) + 'px');
    li.style.setProperty('--y', (Math.sin(mid) * R) + 'px');
    const b = document.createElement('button');
    b.type = 'button'; b.textContent = it.label;
    b.style.setProperty('--d', (i * 70) + 'ms');
    const midDeg = (a0 + a1) / 2; // 0 = 12 o'clock, clockwise
    b.style.rotate = ((midDeg > 90 && midDeg < 270) ? midDeg + 180 : midDeg) + 'deg';
    b.addEventListener('pointerenter', () => path.classList.add('is-hot'));
    b.addEventListener('pointerleave', () => path.classList.remove('is-hot'));
    b.addEventListener('focus', () => path.classList.add('is-hot'));
    b.addEventListener('blur', () => path.classList.remove('is-hot'));
    li.append(b); labels.append(li);
  });
  trigger.addEventListener('click', () => {
    const open = hub.classList.toggle('is-open');
    trigger.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && hub.classList.contains('is-open')) {
      hub.classList.remove('is-open'); trigger.setAttribute('aria-expanded', 'false'); trigger.focus();
    }
  });
})();
```
