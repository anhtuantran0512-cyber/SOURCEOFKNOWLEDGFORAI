---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/floating-action-radial-menu-fab-speed-dial/"
title: "Floating Action Radial Menu (FAB Speed Dial)"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "The classic mobile pattern done the 2027 way: a floating action button that fans four quick actions along a quarter-circle arc, positioned with CSS…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Action Radial Menu (FAB Speed Dial)
Source: https://codefronts.com/navigation/css-circular-menus/floating-action-radial-menu-fab-speed-dial/

The classic mobile pattern done the 2027 way: a floating action button that fans four quick actions along a quarter-circle arc, positioned with CSS trigonometry instead of hand-tuned pixel offsets. Staggered springs, tooltips on hover, full keyboard + screen-reader wiring — drop it in the corner of any app shell.
## HTML
```html
<section class="ccm-01" aria-label="FAB speed dial demo">
  <div class="ccm-01__stage">
    <div class="ccm-01__copy"><h3>Quick actions, one thumb away</h3><p>Tap the button — four tools fan out along a 90° arc.</p></div>
    <nav class="ccm-01__corner">
      <ul class="ccm-01__ring" id="ccm01-menu">
        <li class="ccm-01__item" style="--i:0"><button type="button" class="ccm-01__act" aria-label="New note"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4l11-11-4-4L4 16v4z"/></svg><span class="ccm-01__tip">New note</span></button></li>
        <li class="ccm-01__item" style="--i:1"><button type="button" class="ccm-01__act" aria-label="Upload image"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 17l5-6 4 5 3-3 4 4M4 5h16v14H4z"/></svg><span class="ccm-01__tip">Upload image</span></button></li>
        <li class="ccm-01__item" style="--i:2"><button type="button" class="ccm-01__act" aria-label="Record voice"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v4"/></svg><span class="ccm-01__tip">Record voice</span></button></li>
        <li class="ccm-01__item" style="--i:3"><button type="button" class="ccm-01__act" aria-label="Schedule event"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h14v15H5zM5 9h14M9 3v4M15 3v4"/></svg><span class="ccm-01__tip">Schedule</span></button></li>
      </ul>
      <button type="button" class="ccm-01__fab" aria-expanded="false" aria-controls="ccm01-menu" aria-label="Open quick actions"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button>
    </nav>
  </div>
</section>
```
## CSS
```css
.ccm-01,
.ccm-01 *,
.ccm-01 *::before,
.ccm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-01 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,oklch(0.98 0.005 265),oklch(0.94 0.02 265));
  --brand: oklch(0.62 0.19 265);
  --ink: oklch(0.24 0.02 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.ccm-01__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(160deg,oklch(0.98 0.005 265),oklch(0.94 0.02 265));
  border: 1px solid oklch(0.9 0.01 265);
  padding: 36px;
}

.ccm-01__copy h3 {
  font-size: 22px;
  letter-spacing: -.02em;
}

.ccm-01__copy p {
  margin-top: 6px;
  color: oklch(0.5 0.02 265);
  font-size: 14px;
  max-width: 32ch;
}

.ccm-01__corner {
  position: absolute;
  right: 36px;
  bottom: 36px;
}

.ccm-01__ring {
  position: absolute;
  right: 8px;
  bottom: 8px;
  list-style: none;
  --r: 118px;
}

.ccm-01__item {
  position: absolute;
  right: 0;
  bottom: 0;
  --a: calc(90deg + var(--i) * 30deg);
  translate: 0 0;
  scale: .3;
  opacity: 0;
  visibility: hidden;
  transition: translate .45s cubic-bezier(.34,1.4,.4,1),scale .45s cubic-bezier(.34,1.4,.4,1),opacity .25s,visibility 0s .45s;
  transition-delay: calc(var(--i) * 40ms);
}

.ccm-01__corner.is-open .ccm-01__item {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * -1 * var(--r));
  scale: 1;
  opacity: 1;
  visibility: visible;
  transition: translate .45s cubic-bezier(.34,1.4,.4,1),scale .45s cubic-bezier(.34,1.4,.4,1),opacity .25s,visibility 0s;
  transition-delay: calc(var(--i) * 50ms);
}

.ccm-01__act {
  position: relative;
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  margin: -24px;
  border: none;
  border-radius: 50%;
  background: #fff;
  color: var(--brand);
  cursor: pointer;
  box-shadow: 0 8px 20px -8px oklch(0.4 0.1 265 / .5),0 1px 0 oklch(0.92 0.01 265) inset;
}

.ccm-01__act svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-01__act:hover {
  color: oklch(0.5 0.22 265);
}

.ccm-01__act:focus-visible,
.ccm-01__fab:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-01__tip {
  position: absolute;
  right: calc(100% + 10px);
  top: 50%;
  translate: 4px -50%;
  white-space: nowrap;
  font-size: 12px;
  font-weight: 600;
  background: var(--ink);
  color: #fff;
  padding: 5px 10px;
  border-radius: 7px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s,translate .2s;
}

.ccm-01__act:hover .ccm-01__tip,
.ccm-01__act:focus-visible .ccm-01__tip {
  opacity: 1;
  translate: 0 -50%;
}

.ccm-01__fab {
  position: relative;
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  color: #fff;
  background: linear-gradient(140deg,var(--brand),oklch(0.5 0.22 285));
  box-shadow: 0 14px 30px -10px oklch(0.5 0.22 275 / .6);
  transition: rotate .35s cubic-bezier(.34,1.4,.4,1),box-shadow .3s;
}

.ccm-01__fab svg {
  width: 26px;
  height: 26px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
}

.ccm-01__corner.is-open .ccm-01__fab {
  rotate: 135deg;
  box-shadow: 0 6px 16px -8px oklch(0.5 0.22 275 / .6);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-01 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const corner = document.querySelector('.ccm-01__corner');
  const fab = corner.querySelector('.ccm-01__fab');
  const set = (open) => {
    corner.classList.toggle('is-open', open);
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close quick actions' : 'Open quick actions');
  };
  fab.addEventListener('click', () => set(!corner.classList.contains('is-open')));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && corner.classList.contains('is-open')) { set(false); fab.focus(); }
  });
  document.addEventListener('pointerdown', (e) => {
    if (!corner.contains(e.target)) set(false);
  });
  corner.querySelectorAll('.ccm-01__act').forEach((b) => b.addEventListener('click', () => {
    b.animate([{ scale: '0.85' }, { scale: '1' }], { duration: 250, easing: 'cubic-bezier(.34,1.4,.4,1)' });
  }));
})();
```
