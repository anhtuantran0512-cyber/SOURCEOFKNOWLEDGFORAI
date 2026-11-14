---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/glass-dome/"
title: "Glassmorphism Circular Popover Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A frosted-glass disc that floats over a vivid photo-style backdrop using the native Popover API — real top-layer rendering, light-dismiss and Escape handling…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Circular Popover Menu
Source: https://codefronts.com/navigation/css-circular-menus/glass-dome/

A frosted-glass disc that floats over a vivid photo-style backdrop using the native Popover API — real top-layer rendering, light-dismiss and Escape handling from the browser, zero positioning libraries. Six glass chips sit on the ring, each catching the background through two layers of backdrop blur.
## HTML
```html
<section class="ccm-15" aria-label="Glassmorphism popover menu demo">
  <div class="ccm-15__stage">
    <div class="ccm-15__scenery" aria-hidden="true"><i></i><i></i><i></i></div>
    <button type="button" class="ccm-15__orb" popovertarget="ccm15-pop"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="5.5" r="1.7" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.7" fill="currentColor" stroke="none"/><circle cx="12" cy="18.5" r="1.7" fill="currentColor" stroke="none"/></svg><span class="ccm-15__sr">Open glass menu</span></button>
    <nav id="ccm15-pop" class="ccm-15__pop" popover style="--n:6" aria-label="Glass menu">
      <ul class="ccm-15__ring">
        <li style="--i:0"><a href="#profile"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.6"/><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5"/></svg><span>Profile</span></a></li>
        <li style="--i:1"><a href="#inbox"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="14" rx="3"/><path d="M3.5 13h5l1.5 2.5h4L15.5 13h5"/></svg><span>Inbox</span></a></li>
        <li style="--i:2"><a href="#tasks"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg><span>Tasks</span></a></li>
        <li style="--i:3"><a href="#stats"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19V11M12 19V5M19 19v-6"/></svg><span>Stats</span></a></li>
        <li style="--i:4"><a href="#files"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7a2 2 0 0 1 2-2h4l2 2.5h6A2 2 0 0 1 20 9.5V17a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/></svg><span>Files</span></a></li>
        <li style="--i:5"><a href="#more"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 8.5v7M8.5 12h7"/></svg><span>More</span></a></li>
      </ul>
      <span class="ccm-15__core" aria-hidden="true"></span>
    </nav>
  </div>
</section>
```
## CSS
```css
.ccm-15,
.ccm-15 *,
.ccm-15 *::before,
.ccm-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-15 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(140deg,oklch(0.55 0.19 300),oklch(0.6 0.17 250) 45%,oklch(0.68 0.16 180));
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-15__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.55 0.19 300),oklch(0.6 0.17 250) 45%,oklch(0.68 0.16 180));
}

.ccm-15__scenery i {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
}

.ccm-15__scenery i:nth-child(1) {
  width: 260px;
  height: 260px;
  left: -60px;
  top: -70px;
  background: oklch(0.75 0.16 340 / .55);
}

.ccm-15__scenery i:nth-child(2) {
  width: 200px;
  height: 200px;
  right: -40px;
  top: 30%;
  background: oklch(0.8 0.14 120 / .45);
}

.ccm-15__scenery i:nth-child(3) {
  width: 300px;
  height: 300px;
  left: 22%;
  bottom: -130px;
  background: oklch(0.72 0.17 60 / .5);
}

.ccm-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-15__orb {
  display: grid;
  place-items: center;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  border: 1px solid oklch(1 0 0 / .4);
  background: oklch(1 0 0 / .14);
  backdrop-filter: blur(14px) saturate(1.5);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 16px 40px -14px oklch(0.3 0.1 280 / .7),inset 0 1px 0 oklch(1 0 0 / .35);
  transition: scale .25s;
}

.ccm-15__orb:hover {
  scale: 1.07;
}

.ccm-15__orb:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

.ccm-15__orb svg {
  width: 24px;
  height: 24px;
}

.ccm-15__pop {
  position: fixed;
  inset: 0;
  margin: auto;
  width: 330px;
  height: 330px;
  border: none;
  overflow: visible;
  border-radius: 50%;
  background: oklch(1 0 0 / .09);
  backdrop-filter: blur(22px) saturate(1.6);
  box-shadow: 0 30px 90px -30px oklch(0.2 0.08 280 / .85),inset 0 1px 0 oklch(1 0 0 / .25),inset 0 0 0 1px oklch(1 0 0 / .15);
}

.ccm-15__pop {
  opacity: 1;
  scale: 1;
  transition: opacity .3s,scale .35s cubic-bezier(.32,1.25,.4,1),display .35s allow-discrete,overlay .35s allow-discrete;
}

.ccm-15__pop:not(:popover-open) {
  opacity: 0;
  scale: .8;
}

@starting-style {
  .ccm-15__pop:popover-open {
    opacity: 0;
    scale: .7;
  }
}

.ccm-15__ring {
  position: absolute;
  inset: 0;
  list-style: none;
  --r: 112px;
}

.ccm-15__ring li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}

.ccm-15__ring a {
  pointer-events: auto;
  display: grid;
  justify-items: center;
  gap: 5px;
  width: 76px;
  padding: 12px 4px 10px;
  border-radius: 18px;
  background: oklch(1 0 0 / .12);
  border: 1px solid oklch(1 0 0 / .28);
  backdrop-filter: blur(8px);
  color: #fff;
  text-decoration: none;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .02em;
  text-shadow: 0 1px 2px oklch(0.3 0.08 280 / .5);
  transition: background .25s,translate .25s;
}

.ccm-15__ring a:hover,
.ccm-15__ring a:focus-visible {
  background: oklch(1 0 0 / .28);
  translate: 0 -3px;
  outline: none;
}

.ccm-15__ring a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.ccm-15__ring svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-15__core {
  position: absolute;
  inset: 50%;
  translate: -50% -50%;
  width: 86px;
  height: 86px;
  border-radius: 50%;
  background: oklch(1 0 0 / .1);
  border: 1px solid oklch(1 0 0 / .3);
  box-shadow: inset 0 1px 0 oklch(1 0 0 / .3);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-15 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  // The Popover API handles open/close/light-dismiss natively.
  // This tiny enhancement just re-centers the popover over its trigger's stage
  // when embedded in a scrolling collection page.
  const stage = document.querySelector('.ccm-15__stage');
  const pop = document.getElementById('ccm15-pop');
  const place = () => {
    const r = stage.getBoundingClientRect();
    pop.style.inset = 'auto';
    pop.style.left = (r.left + r.width / 2 - 165) + 'px';
    pop.style.top = (r.top + r.height / 2 - 165) + 'px';
  };
  pop.addEventListener('beforetoggle', (e) => { if (e.newState === 'open') place(); });
  // choosing an item dismisses the menu, like any menu pick
  pop.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => pop.hidePopover()));
  addEventListener('resize', () => { if (pop.matches(':popover-open')) place(); });
  addEventListener('scroll', () => { if (pop.matches(':popover-open')) place(); }, true);
})();
```
