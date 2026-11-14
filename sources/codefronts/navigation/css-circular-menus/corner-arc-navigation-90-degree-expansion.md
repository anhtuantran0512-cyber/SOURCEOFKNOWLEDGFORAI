---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/corner-arc-navigation-90-degree-expansion/"
title: "Corner Arc Navigation (90-Degree Expansion)"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A docked corner widget — the pattern behind help launchers and share docks — where a quarter-circle sheet sweeps open from the corner and five actions ride…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Arc Navigation (90-Degree Expansion)
Source: https://codefronts.com/navigation/css-circular-menus/corner-arc-navigation-90-degree-expansion/

A docked corner widget — the pattern behind help launchers and share docks — where a quarter-circle sheet sweeps open from the corner and five actions ride the arc's edge, each with a label that slides in after the sweep. The sheet itself is a single element scaled from the corner, so the reveal is one buttery transform.
## HTML
```html
<section class="ccm-05" aria-label="Corner arc navigation demo">
  <div class="ccm-05__stage">
    <article class="ccm-05__fakepage" aria-hidden="true"><span></span><span style="width:72%"></span><span style="width:84%"></span><span style="width:56%"></span></article>
    <div class="ccm-05__dock">
      <span class="ccm-05__sheet" aria-hidden="true"></span>
      <ul class="ccm-05__arc" id="ccm05-menu">
        <li style="--i:0"><button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v12m0 0l-4-4m4 4l4-4M5 20h14"/></svg><span>Download</span></button></li>
        <li style="--i:1"><button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.2 10.8l7.6-3.6M8.2 13.2l7.6 3.6"/></svg><span>Share</span></button></li>
        <li style="--i:2"><button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.6-9.5-9A5.4 5.4 0 0 1 12 6.5 5.4 5.4 0 0 1 21.5 12C19 16.4 12 21 12 21z"/></svg><span>Save</span></button></li>
        <li style="--i:3"><button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 8h10M7 12h6M4 4h16v13H9l-5 4z"/></svg><span>Comment</span></button></li>
        <li style="--i:4"><button type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.5v.01"/></svg><span>Help</span></button></li>
      </ul>
      <button type="button" class="ccm-05__trigger" aria-expanded="false" aria-controls="ccm05-menu" aria-label="Open page actions"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1.6" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/><circle cx="19" cy="12" r="1.6" fill="currentColor" stroke="none"/></svg></button>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-05,
.ccm-05 *,
.ccm-05 *::before,
.ccm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-05 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: oklch(0.975 0.005 250);
  --brand: oklch(0.55 0.16 250);
  --sheet: 520px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-05__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  background: oklch(0.975 0.005 250);
  border: 1px solid oklch(0.9 0.01 250);
  padding: 32px;
}

.ccm-05__fakepage {
  display: grid;
  gap: 14px;
  max-width: 520px;
}

.ccm-05__fakepage span {
  display: block;
  height: 13px;
  border-radius: 7px;
  background: oklch(0.91 0.01 250);
}

.ccm-05__fakepage span:first-child {
  height: 26px;
  width: 44%;
  background: oklch(0.86 0.02 250);
}

.ccm-05__dock {
  position: absolute;
  right: 0;
  bottom: 0;
}

.ccm-05__sheet {
  position: absolute;
  right: calc(var(--sheet) / -2);
  bottom: calc(var(--sheet) / -2);
  width: var(--sheet);
  height: var(--sheet);
  border-radius: 50%;
  background: color-mix(in oklab,var(--brand) 92%,black);
  box-shadow: 0 -10px 50px -12px oklch(0.4 0.12 250 / .55);
  scale: 0;
  transform-origin: 50% 50%;
  transition: scale .5s cubic-bezier(.32,1.2,.35,1);
}

.ccm-05__dock.is-open .ccm-05__sheet {
  scale: 1;
}

.ccm-05__arc {
  position: absolute;
  right: 28px;
  bottom: 28px;
  list-style: none;
}

.ccm-05__arc li {
  position: absolute;
  right: 0;
  bottom: 0;
  --a: calc(188deg + var(--i) * 18.5deg);
}

.ccm-05__arc button {
  position: absolute;
  right: -22px;
  bottom: -22px;
  display: grid;
  place-items: center;
  border: none;
  background: none;
  color: #fff;
  cursor: pointer;
  font: 600 12px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .02em;
  translate: 0 0;
  opacity: 0;
  visibility: hidden;
  transition: translate .5s cubic-bezier(.32,1.2,.35,1),opacity .25s,visibility 0s .5s;
  transition-delay: calc(var(--i) * 35ms);
}

.ccm-05__dock.is-open .ccm-05__arc button {
  translate: calc(cos(var(--a)) * 172px) calc(sin(var(--a)) * 172px);
  opacity: 1;
  visibility: visible;
  transition: translate .5s cubic-bezier(.32,1.2,.35,1),opacity .3s .1s,visibility 0s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-05__arc svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
  padding: 0;
}

.ccm-05__arc button svg {
  width: 44px;
  height: 44px;
  padding: 11px;
  border-radius: 50%;
  background: oklch(1 0 0 / .12);
  transition: background .2s;
}

.ccm-05__arc button:hover svg,
.ccm-05__arc button:focus-visible svg {
  background: oklch(1 0 0 / .28);
}

.ccm-05__arc button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 4px;
  border-radius: 26px;
}

.ccm-05__arc button span {
  position: absolute;
  right: calc(100% + 8px);
  top: 50%;
  translate: 6px -50%;
  white-space: nowrap;
  padding: 5px 10px;
  border-radius: 7px;
  background: oklch(0.22 0.05 250);
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s,translate .2s;
}

.ccm-05__arc button:hover span,
.ccm-05__arc button:focus-visible span {
  opacity: 1;
  translate: 0 -50%;
}

.ccm-05__trigger {
  position: absolute;
  right: 24px;
  bottom: 24px;
  z-index: 2;
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 50%;
  background: var(--brand);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 12px 28px -10px oklch(0.5 0.16 250 / .7);
  transition: background .3s,rotate .4s;
}

.ccm-05__trigger svg {
  width: 24px;
  height: 24px;
}

.ccm-05__trigger:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-05__dock.is-open .ccm-05__trigger {
  background: oklch(1 0 0 / .16);
  rotate: 90deg;
}

@media (prefers-reduced-motion: reduce) {
  .ccm-05 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.querySelector('.ccm-05__dock');
  const trigger = dock.querySelector('.ccm-05__trigger');
  const set = (open) => {
    dock.classList.toggle('is-open', open);
    trigger.setAttribute('aria-expanded', String(open));
  };
  trigger.addEventListener('click', () => set(!dock.classList.contains('is-open')));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dock.classList.contains('is-open')) { set(false); trigger.focus(); }
  });
  document.addEventListener('pointerdown', (e) => { if (!dock.contains(e.target)) set(false); });
})();
```
