---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/caret-companion/"
title: "CSS Caret Slide / Trail Link Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "One indicator, many links: the underline that glides from item to item as you move along a nav, with a caret riding above the hovered link — the pattern…"
has_js: "true"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Caret Slide / Trail Link Hover
Source: https://codefronts.com/motion/css-link-effects/caret-companion/

One indicator, many links: the underline that glides from item to item as you move along a nav, with a caret riding above the hovered link — the pattern behind every polished tab bar. Ships two engines: a 20-line JS version that works everywhere today, and the 2027 flex — the same behavior in pure CSS via anchor positioning, zero JavaScript, progressively enhanced behind @supports.
## HTML
```html
<section class="cle-23" aria-label="Sliding indicator nav demo">
  <div class="cle-23__stage">
    <div class="cle-23__var">
      <nav class="cle-23__nav1" aria-label="Primary">
        <a href="#a1" aria-current="page">Overview</a>
        <a href="#a2">Components</a>
        <a href="#a3">Tokens</a>
        <a href="#a4">Releases</a>
        <span class="cle-23__bar" aria-hidden="true"></span>
        <span class="cle-23__caret" aria-hidden="true"></span>
      </nav>
      <small class="cle-23__cap">A · measured trail + caret (JS)</small>
    </div>
    <div class="cle-23__var">
      <nav class="cle-23__nav2" aria-label="Docs">
        <a href="#b1">Guides</a>
        <a href="#b2">API</a>
        <a href="#b3">Examples</a>
        <a href="#b4">Support</a>
        <span class="cle-23__ind2" aria-hidden="true"></span>
      </nav>
      <small class="cle-23__cap">B · pure CSS anchor positioning</small>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-23,
.cle-23 *,
.cle-23 *::before,
.cle-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-23 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.27 0.02 250);
  --brand: oklch(0.55 0.19 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-23__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 52px;
  border: 1px solid oklch(0.9 0.012 250);
  background: linear-gradient(170deg,oklch(0.98 0.006 250),oklch(0.945 0.014 250));
  padding: 44px 32px;
}

.cle-23__var {
  display: grid;
  gap: 16px;
  justify-items: center;
}

.cle-23__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 250);
}

.cle-23__nav1,
.cle-23__nav2 {
  position: relative;
  display: flex;
  gap: 8px;
  padding: 8px 10px 14px;
  border-radius: 14px;
  background: oklch(1 0 0 / .8);
  border: 1px solid oklch(0.9 0.012 250);
  box-shadow: 0 12px 30px -22px oklch(0.35 0.08 250 / .7);
}

.cle-23 nav a {
  position: relative;
  padding: 10px 16px;
  color: var(--ink);
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 600;
  border-radius: 8px;
  transition: color .25s;
}

.cle-23 nav a:hover,
.cle-23 nav a:focus-visible,
.cle-23 nav a[aria-current="page"] {
  color: var(--brand);
}

.cle-23 nav a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}

.cle-23__bar {
  position: absolute;
  bottom: 8px;
  left: 10px;
  width: 60px;
  height: 3px;
  border-radius: 3px;
  background: var(--brand);
  transition: left .32s cubic-bezier(.3,1.1,.3,1),width .32s cubic-bezier(.3,1.1,.3,1);
}

.cle-23__caret {
  position: absolute;
  bottom: 2px;
  left: 40px;
  width: 12px;
  height: 5px;
  translate: -50% 0;
  background: var(--brand);
  clip-path: polygon(50% 0,0 100%,100% 100%);
  transition: left .32s cubic-bezier(.3,1.1,.3,1);
}

@supports (anchor-name: --a) {
  .cle-23__nav2 a:nth-of-type(1) {
    anchor-name: --clh23-a1;
  }

  .cle-23__nav2 a:nth-of-type(2) {
    anchor-name: --clh23-a2;
  }

  .cle-23__nav2 a:nth-of-type(3) {
    anchor-name: --clh23-a3;
  }

  .cle-23__nav2 a:nth-of-type(4) {
    anchor-name: --clh23-a4;
  }

  .cle-23__ind2 {
    position: absolute;
    position-anchor: --clh23-a1;
    left: anchor(left);
    right: anchor(right);
    bottom: 6px;
    height: 3px;
    border-radius: 3px;
    background: var(--brand);
    transition: left .32s cubic-bezier(.3,1.1,.3,1),right .32s cubic-bezier(.3,1.1,.3,1);
  }

  .cle-23__nav2:has(a:nth-of-type(2):is(:hover,:focus-visible)) .cle-23__ind2 {
    position-anchor: --clh23-a2;
  }

  .cle-23__nav2:has(a:nth-of-type(3):is(:hover,:focus-visible)) .cle-23__ind2 {
    position-anchor: --clh23-a3;
  }

  .cle-23__nav2:has(a:nth-of-type(4):is(:hover,:focus-visible)) .cle-23__ind2 {
    position-anchor: --clh23-a4;
  }
}

@supports not (anchor-name: --a) {
  .cle-23__ind2 {
    display: none;
  }

  .cle-23__nav2 a {
    background: linear-gradient(var(--brand),var(--brand)) no-repeat left calc(100% - 4px) / 0% 3px;
    transition: color .25s,background-size .3s cubic-bezier(.3,.9,.3,1);
  }

  .cle-23__nav2 a:hover,
    .cle-23__nav2 a:focus-visible {
    background-size: calc(100% - 0px) 3px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-23 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const nav = document.querySelector('.cle-23__nav1');
  if (!nav) return;
  const bar = nav.querySelector('.cle-23__bar');
  const caret = nav.querySelector('.cle-23__caret');
  const links = [...nav.querySelectorAll('a')];
  const home = () => links.find((a) => a.hasAttribute('aria-current')) || links[0];
  const move = (a) => {
    bar.style.left = a.offsetLeft + 'px';
    bar.style.width = a.offsetWidth + 'px';
    caret.style.left = (a.offsetLeft + a.offsetWidth / 2) + 'px';
  };
  links.forEach((a) => {
    a.addEventListener('pointerenter', () => move(a));
    a.addEventListener('focus', () => move(a));
  });
  nav.addEventListener('pointerleave', () => move(home()));
  nav.addEventListener('focusout', () => move(home()));
  window.addEventListener('resize', () => move(home()));
  move(home());
})();
```
