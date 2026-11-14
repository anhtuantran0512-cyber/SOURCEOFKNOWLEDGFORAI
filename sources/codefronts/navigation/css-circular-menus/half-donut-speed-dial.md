---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/half-donut-speed-dial/"
title: "Semi-Circle Speed Dial Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A bottom-docked half-circle dial made for thumbs: five actions arc across 180° above a center trigger, exactly spanning the natural sweep of a thumb on a phone."
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Semi-Circle Speed Dial Menu
Source: https://codefronts.com/navigation/css-circular-menus/half-donut-speed-dial/

A bottom-docked half-circle dial made for thumbs: five actions arc across 180° above a center trigger, exactly spanning the natural sweep of a thumb on a phone. The half-disc backdrop rises like a tiny bottom sheet. This is the radial pattern that actually belongs on mobile.
## HTML
```html
<section class="ccm-14" aria-label="Semi-circle speed dial demo">
  <div class="ccm-14__stage">
    <div class="ccm-14__phone">
      <div class="ccm-14__screen" aria-hidden="true"><span></span><span style="width:64%"></span><span style="width:78%"></span></div>
      <div class="ccm-14__dock" style="--n:5">
        <span class="ccm-14__sheet" aria-hidden="true"></span>
        <ul class="ccm-14__arc" id="ccm14-menu">
          <li style="--i:0"><button type="button" aria-label="Camera"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.2"/></svg></button></li>
          <li style="--i:1"><button type="button" aria-label="Gallery"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5" width="16" height="14" rx="2"/><path d="M4 15l4-4 4 4 3-3 5 5"/><circle cx="9" cy="9" r="1.2"/></svg></button></li>
          <li style="--i:2"><button type="button" aria-label="New post"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v12M6 12h12"/></svg></button></li>
          <li style="--i:3"><button type="button" aria-label="Voice note"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v4"/></svg></button></li>
          <li style="--i:4"><button type="button" aria-label="Live"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M6.3 6.3a8 8 0 0 0 0 11.4M17.7 6.3a8 8 0 0 1 0 11.4" transform="rotate(90 12 12)"/></svg></button></li>
        </ul>
        <button type="button" class="ccm-14__go" aria-expanded="false" aria-controls="ccm14-menu" aria-label="Open create menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-14,
.ccm-14 *,
.ccm-14 *::before,
.ccm-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-14 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(170deg,oklch(0.93 0.02 300),oklch(0.88 0.035 290));
  --brand: oklch(0.65 0.21 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-14__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(170deg,oklch(0.93 0.02 300),oklch(0.88 0.035 290));
  border: 1px solid oklch(0.87 0.02 295);
  padding: 30px;
}

.ccm-14__phone {
  position: relative;
  width: 300px;
  height: 460px;
  border-radius: 36px;
  background: oklch(0.99 0.002 300);
  border: 1px solid oklch(0.88 0.015 300);
  box-shadow: 0 30px 60px -30px oklch(0.4 0.1 295 / .6);
  overflow: hidden;
}

.ccm-14__screen {
  display: grid;
  gap: 12px;
  padding: 28px 24px;
}

.ccm-14__screen span {
  display: block;
  height: 12px;
  border-radius: 6px;
  background: oklch(0.93 0.01 300);
}

.ccm-14__screen span:first-child {
  height: 22px;
  width: 48%;
  background: oklch(0.89 0.02 300);
}

.ccm-14__dock {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 210px;
  pointer-events: none;
}

.ccm-14__dock > * {
  pointer-events: auto;
}

.ccm-14__sheet {
  position: absolute;
  left: 50%;
  bottom: -150px;
  width: 420px;
  height: 420px;
  margin-left: -210px;
  border-radius: 50%;
  background: linear-gradient(180deg,color-mix(in oklab,var(--brand) 96%,black),color-mix(in oklab,var(--brand) 75%,black));
  box-shadow: 0 -14px 44px -14px oklch(0.5 0.2 300 / .55);
  translate: 0 105%;
  transition: translate .5s cubic-bezier(.32,1.15,.35,1);
  pointer-events: none;
}

.ccm-14__dock.is-open .ccm-14__sheet {
  translate: 0 0;
}

.ccm-14__arc {
  position: absolute;
  left: 50%;
  bottom: 44px;
  list-style: none;
}

.ccm-14__arc li {
  position: absolute;
  left: 0;
  bottom: 0;
  --a: calc(180deg + (180deg / (var(--n) - 1)) * var(--i));
}

.ccm-14__arc button {
  position: absolute;
  left: -24px;
  bottom: -24px;
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  border: none;
  border-radius: 50%;
  background: oklch(1 0 0 / .14);
  color: #fff;
  cursor: pointer;
  translate: 0 0;
  opacity: 0;
  scale: .4;
  visibility: hidden;
  transition: translate .5s cubic-bezier(.34,1.35,.4,1),opacity .25s,scale .5s cubic-bezier(.34,1.35,.4,1),visibility 0s .5s,background .2s;
  transition-delay: calc(var(--i) * 35ms);
}

.ccm-14__dock.is-open .ccm-14__arc button {
  translate: calc(cos(var(--a)) * 108px) calc(sin(var(--a)) * 108px);
  opacity: 1;
  scale: 1;
  visibility: visible;
  transition: translate .5s cubic-bezier(.34,1.35,.4,1),opacity .3s,scale .5s cubic-bezier(.34,1.35,.4,1),visibility 0s,background .2s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-14__arc button:hover,
.ccm-14__arc button:focus-visible {
  background: oklch(1 0 0 / .3);
}

.ccm-14__arc button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.ccm-14__arc svg {
  width: 21px;
  height: 21px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-14__go {
  position: absolute;
  left: 50%;
  bottom: 22px;
  translate: -50% 0;
  display: grid;
  place-items: center;
  width: 58px;
  height: 58px;
  border: none;
  border-radius: 50%;
  background: var(--brand);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 12px 30px -10px oklch(0.55 0.21 300 / .7);
  transition: rotate .4s cubic-bezier(.34,1.35,.4,1),background .3s;
  z-index: 2;
}

.ccm-14__go svg {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
}

.ccm-14__go:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-14__dock.is-open .ccm-14__go {
  rotate: 135deg;
  background: oklch(1 0 0 / .18);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-14 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.querySelector('.ccm-14__dock');
  const go = dock.querySelector('.ccm-14__go');
  const set = (open) => {
    dock.classList.toggle('is-open', open);
    go.setAttribute('aria-expanded', String(open));
  };
  go.addEventListener('click', () => set(!dock.classList.contains('is-open')));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dock.classList.contains('is-open')) { set(false); go.focus(); }
  });
})();
```
