---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/fan-reveal/"
title: "Collapsible Fan-Out Radial Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "Cards that fan open like a hand of playing cards: five labeled options pivot from a shared hinge point, each rotated a few degrees further than the last."
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Collapsible Fan-Out Radial Menu
Source: https://codefronts.com/navigation/css-circular-menus/fan-reveal/

Cards that fan open like a hand of playing cards: five labeled options pivot from a shared hinge point, each rotated a few degrees further than the last. Unlike ring menus, a fan preserves reading order — the eye scans it top-to-bottom — so it suits labeled navigation, not just icons.
## HTML
```html
<section class="ccm-09" aria-label="Fan-out radial menu demo">
  <div class="ccm-09__stage">
    <div class="ccm-09__hand">
      <ul class="ccm-09__fan" id="ccm09-menu">
        <li class="ccm-09__card" style="--i:4"><a href="#exports"><b>⇩</b>Exports<span>⌘E</span></a></li>
        <li class="ccm-09__card" style="--i:3"><a href="#reports"><b>▤</b>Reports<span>⌘R</span></a></li>
        <li class="ccm-09__card" style="--i:2"><a href="#boards"><b>▦</b>Boards<span>⌘B</span></a></li>
        <li class="ccm-09__card" style="--i:1"><a href="#docs"><b>≡</b>Docs<span>⌘D</span></a></li>
        <li class="ccm-09__card" style="--i:0"><a href="#inbox"><b>▣</b>Inbox<span>⌘I</span></a></li>
      </ul>
      <button type="button" class="ccm-09__deal" aria-expanded="false" aria-controls="ccm09-menu">Workspace<i aria-hidden="true">❯</i></button>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-09,
.ccm-09 *,
.ccm-09 *::before,
.ccm-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-09 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(165deg,oklch(0.95 0.015 305),oklch(0.9 0.03 290));
  --brand: oklch(0.6 0.2 300);
  --paper: oklch(0.99 0.003 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-09__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(165deg,oklch(0.95 0.015 305),oklch(0.9 0.03 290));
  border: 1px solid oklch(0.88 0.02 300);
  overflow: hidden;
}

.ccm-09__hand {
  position: relative;
  translate: -40px 30px;
}

.ccm-09__fan {
  position: absolute;
  left: 0;
  bottom: 56px;
  list-style: none;
}

.ccm-09__card {
  position: absolute;
  left: 0;
  bottom: 0;
  transform-origin: 24px calc(100% + 46px);
  rotate: calc(var(--i) * -2deg);
  translate: 0 calc(var(--i) * 2px);
  transition: rotate .5s cubic-bezier(.34,1.3,.4,1),translate .5s cubic-bezier(.34,1.3,.4,1),scale .25s,opacity .3s;
  transition-delay: calc((4 - var(--i)) * 40ms);
}

.ccm-09__hand.is-open .ccm-09__card {
  rotate: calc(var(--i) * -15deg);
  translate: 0 0;
  transition-delay: calc(var(--i) * 55ms);
}

.ccm-09__hand.is-open .ccm-09__card:hover,
.ccm-09__hand.is-open .ccm-09__card:focus-within {
  z-index: 10;
  scale: 1.06;
  transition-delay: 0s;
}

.ccm-09__card a {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 196px;
  padding: 13px 16px;
  border-radius: 14px;
  background: var(--paper);
  border: 1px solid oklch(0.88 0.02 300);
  box-shadow: 0 10px 24px -12px oklch(0.4 0.1 300 / .45);
  color: oklch(0.3 0.04 300);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  transition: border-color .2s,box-shadow .2s,translate .2s;
}

.ccm-09__card a:hover,
.ccm-09__card a:focus-visible {
  border-color: var(--brand);
  box-shadow: 0 16px 34px -10px oklch(0.5 0.18 300 / .6);
  outline: none;
}

.ccm-09__card a:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.ccm-09__card b {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: color-mix(in oklab,var(--brand) 12%,white);
  color: var(--brand);
  font-weight: 500;
  font-size: 15px;
}

.ccm-09__card span {
  margin-left: auto;
  font-size: 11px;
  font-weight: 500;
  color: oklch(0.6 0.03 300);
  border: 1px solid oklch(0.88 0.02 300);
  border-radius: 6px;
  padding: 2px 6px;
}

.ccm-09__deal {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 22px;
  border: none;
  border-radius: 14px;
  background: oklch(0.28 0.06 300);
  color: #fff;
  font: 600 14px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .02em;
  cursor: pointer;
  box-shadow: 0 12px 26px -12px oklch(0.28 0.06 300 / .8);
}

.ccm-09__deal i {
  font-style: normal;
  font-size: 11px;
  rotate: -90deg;
  transition: rotate .4s cubic-bezier(.34,1.3,.4,1);
}

.ccm-09__hand.is-open .ccm-09__deal i {
  rotate: 90deg;
}

.ccm-09__deal:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-09__hand:not(.is-open) .ccm-09__card a {
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .ccm-09 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const hand = document.querySelector('.ccm-09__hand');
  const deal = hand.querySelector('.ccm-09__deal');
  deal.addEventListener('click', () => {
    const open = hand.classList.toggle('is-open');
    deal.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && hand.classList.contains('is-open')) {
      hand.classList.remove('is-open'); deal.setAttribute('aria-expanded', 'false'); deal.focus();
    }
  });
})();
```
