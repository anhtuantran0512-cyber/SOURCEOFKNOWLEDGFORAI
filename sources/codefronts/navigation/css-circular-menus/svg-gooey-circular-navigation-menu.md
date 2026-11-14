---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/svg-gooey-circular-navigation-menu/"
title: "SVG Gooey Circular Navigation Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "The liquid 'metaball' effect: buttons that ooze out of the trigger like drops of mercury, merging and separating as they travel."
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Gooey Circular Navigation Menu
Source: https://codefronts.com/navigation/css-circular-menus/svg-gooey-circular-navigation-menu/

The liquid 'metaball' effect: buttons that ooze out of the trigger like drops of mercury, merging and separating as they travel. One reusable SVG filter — blur, then a contrast-crushing color matrix — turns any group of round shapes into goo. A favorite for playful brands and creative portfolios.
## HTML
```html
<section class="ccm-04" aria-label="Gooey circular menu demo">
  <svg class="ccm-04__defs" aria-hidden="true"><defs><filter id="ccm04-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="9" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -10"/></filter></defs></svg>
  <div class="ccm-04__stage">
    <div class="ccm-04__hub">
      <div class="ccm-04__goo" aria-hidden="true">
        <span class="ccm-04__blob ccm-04__blob--core"></span>
        <span class="ccm-04__blob" style="--i:0"></span>
        <span class="ccm-04__blob" style="--i:1"></span>
        <span class="ccm-04__blob" style="--i:2"></span>
        <span class="ccm-04__blob" style="--i:3"></span>
      </div>
      <ul class="ccm-04__icons" id="ccm04-menu">
        <li style="--i:0"><a href="#dribbble" aria-label="Dribbble"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M5 8.5c5 2 9.5 2 13.5-1M4.5 14c5-1 10 .5 13 5M9 3.5c3 3.5 5 8 6 16"/></svg></a></li>
        <li style="--i:1"><a href="#instagram" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.5"/><circle cx="17" cy="7" r="1" fill="currentColor" stroke="none"/></svg></a></li>
        <li style="--i:2"><a href="#youtube" aria-label="YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="4"/><path d="M10.5 9.5l4.5 2.5-4.5 2.5z" fill="currentColor" stroke="none"/></svg></a></li>
        <li style="--i:3"><a href="#mail" aria-label="Email"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg></a></li>
      </ul>
      <button type="button" class="ccm-04__fab" aria-expanded="false" aria-controls="ccm04-menu" aria-label="Open social menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button>
    </div>
    <p class="ccm-04__note">SVG filter goo · blobs + icons ride the same arc</p>
  </div>
</section>
```
## CSS
```css
.ccm-04,
.ccm-04 *,
.ccm-04 *::before,
.ccm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-04 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 30% 20%,oklch(0.3 0.08 320),oklch(0.17 0.05 300) 70%);
  --goo: oklch(0.65 0.24 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-04__defs {
  position: absolute;
  width: 0;
  height: 0;
}

.ccm-04__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 30% 20%,oklch(0.3 0.08 320),oklch(0.17 0.05 300) 70%);
  overflow: hidden;
}

.ccm-04__hub {
  position: relative;
  width: 72px;
  height: 72px;
}

.ccm-04__goo {
  position: absolute;
  inset: -120px;
  filter: url(#ccm04-goo);
}

.ccm-04__blob {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 58px;
  height: 58px;
  margin: -29px;
  border-radius: 50%;
  background: var(--goo);
  --a: calc(-155deg + var(--i) * 43deg);
  translate: 0 0;
  transition: translate .6s cubic-bezier(.45,1.5,.4,1);
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-04__blob--core {
  width: 72px;
  height: 72px;
  margin: -36px;
}

.ccm-04__hub.is-open .ccm-04__blob:not(.ccm-04__blob--core) {
  translate: calc(cos(var(--a)) * 116px) calc(sin(var(--a)) * 116px);
}

.ccm-04__icons {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-04__icons li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  --a: calc(-155deg + var(--i) * 43deg);
  translate: 0 0;
  opacity: 0;
  visibility: hidden;
  transition: translate .6s cubic-bezier(.45,1.5,.4,1),opacity .3s .1s,visibility 0s .6s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-04__hub.is-open .ccm-04__icons li {
  translate: calc(cos(var(--a)) * 116px) calc(sin(var(--a)) * 116px);
  opacity: 1;
  visibility: visible;
  transition: translate .6s cubic-bezier(.45,1.5,.4,1),opacity .3s .15s,visibility 0s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-04__icons a {
  display: grid;
  place-items: center;
  width: 58px;
  height: 58px;
  border-radius: 50%;
  color: #fff;
}

.ccm-04__icons a:focus-visible {
  outline: 3px solid #fff;
  outline-offset: -4px;
  border-radius: 50%;
}

.ccm-04__icons svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-04__fab {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 50%;
  background: transparent;
  color: #fff;
  cursor: pointer;
  transition: rotate .45s cubic-bezier(.45,1.5,.4,1);
}

.ccm-04__fab svg {
  width: 28px;
  height: 28px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
}

.ccm-04__fab:focus-visible {
  outline: 3px solid var(--goo);
  outline-offset: 6px;
}

.ccm-04__hub.is-open .ccm-04__fab {
  rotate: 225deg;
}

.ccm-04__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.75 0.08 330 / .55);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-04 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const hub = document.querySelector('.ccm-04__hub');
  const fab = hub.querySelector('.ccm-04__fab');
  fab.addEventListener('click', () => {
    const open = hub.classList.toggle('is-open');
    fab.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && hub.classList.contains('is-open')) {
      hub.classList.remove('is-open'); fab.setAttribute('aria-expanded', 'false'); fab.focus();
    }
  });
})();
```
