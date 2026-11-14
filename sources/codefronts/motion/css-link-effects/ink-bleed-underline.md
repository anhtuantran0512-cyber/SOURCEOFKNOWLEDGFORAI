---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/ink-bleed-underline/"
title: "CSS Ink Spread / Bleed Link Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Ink physics for links: a drop that blooms from the center until it floods the pill, a ripple that spreads from the exact point your cursor entered (six lines…"
has_js: "true"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ink Spread / Bleed Link Hover Effect
Source: https://codefronts.com/motion/css-link-effects/ink-bleed-underline/

Ink physics for links: a drop that blooms from the center until it floods the pill, a ripple that spreads from the exact point your cursor entered (six lines of JS feed the coordinates to CSS), and the bleed — accent ink soaking through the glyphs themselves via an animated radial-gradient radius, the @property trick most developers haven't met yet.
## HTML
```html
<section class="cle-21" aria-label="Ink spread hover demo">
  <div class="cle-21__stage">
    <div class="cle-21__var"><a href="#a" class="cle-21__bloom">Request access</a><small class="cle-21__cap">A · center bloom</small></div>
    <div class="cle-21__var"><a href="#b" class="cle-21__cursor">Enter anywhere</a><small class="cle-21__cap">B · spreads from cursor (JS)</small></div>
    <div class="cle-21__var"><a href="#c" class="cle-21__bleed">Inkworks</a><small class="cle-21__cap">C · bleeds through glyphs</small></div>
  </div>
</section>
```
## CSS
```css
.cle-21,
.cle-21 *,
.cle-21 *::before,
.cle-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --clh21-r {
  syntax: '<length>';
  inherits: false;
  initial-value: 2px;
}

.cle-21 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.27 0.03 290);
  --brand: oklch(0.55 0.22 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-21__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 46px 58px;
  border: 1px solid oklch(0.9 0.015 290);
  background: linear-gradient(170deg,oklch(0.98 0.007 290),oklch(0.945 0.02 290));
  padding: 44px 36px;
}

.cle-21__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-21__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 290);
}

.cle-21__bloom,
.cle-21__cursor {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-block;
  padding: 16px 30px;
  border-radius: 999px;
  border: 1.5px solid oklch(0.6 0.12 290 / .5);
  background: oklch(1 0 0 / .85);
  color: var(--ink);
  text-decoration: none;
  font-size: 15.5px;
  font-weight: 700;
  transition: color .35s,border-color .35s;
}

.cle-21__bloom:hover,
.cle-21__bloom:focus-visible,
.cle-21__cursor:hover,
.cle-21__cursor:focus-visible {
  color: oklch(0.99 0.005 290);
  border-color: transparent;
}

.cle-21__bloom:focus-visible,
.cle-21__cursor:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.cle-21__bloom::before,
.cle-21__cursor::before {
  content: "";
  position: absolute;
  z-index: -1;
  aspect-ratio: 1/1;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.62 0.22 290),var(--brand) 70%);
  translate: -50% -50%;
  scale: 0;
  transition: scale .5s cubic-bezier(.3,.7,.2,1);
}

.cle-21__bloom::before {
  width: 135%;
  left: 50%;
  top: 50%;
}

.cle-21__cursor::before {
  width: 260%;
  left: var(--x,50%);
  top: var(--y,50%);
}

.cle-21__bloom:hover::before,
.cle-21__bloom:focus-visible::before,
.cle-21__cursor:hover::before,
.cle-21__cursor:focus-visible::before {
  scale: 1;
}

.cle-21__bleed {
  font-size: clamp(34px,5vw,48px);
  font-weight: 800;
  letter-spacing: -.02em;
  text-decoration: none;
  background-image: radial-gradient(circle var(--clh21-r,2px) at 42% 55%,var(--brand) 99.6%,var(--ink) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  transition: --clh21-r .6s cubic-bezier(.4,0,.3,1);
}

.cle-21__bleed:hover,
.cle-21__bleed:focus-visible {
  --clh21-r: 8em;
}

.cle-21__bleed:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-21__bleed::selection {
  background: oklch(0.85 0.08 290 / .5);
  color: var(--ink);
  -webkit-text-fill-color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .cle-21 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cle-21__cursor').forEach((a) => {
    a.addEventListener('pointerenter', (e) => {
      const r = a.getBoundingClientRect();
      a.style.setProperty('--x', (e.clientX - r.left).toFixed(0) + 'px');
      a.style.setProperty('--y', (e.clientY - r.top).toFixed(0) + 'px');
    });
  });
})();
```
