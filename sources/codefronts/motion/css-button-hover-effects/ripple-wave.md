---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/ripple-wave/"
title: "Ripple Wave"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A Material-style ripple CTA: on hover a circular wave expands from the centre and fades as it grows, like a drop hitting water — a familiar tactile feedback."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Wave
Source: https://codefronts.com/motion/css-button-hover-effects/ripple-wave/

A Material-style ripple CTA: on hover a circular wave expands from the centre and fades as it grows, like a drop hitting water — a familiar tactile feedback.
## HTML
```html
<div class="bhe-28-group">
<section class="bhe-28a" aria-label="Ripple wave button">
  <button class="bhe-28a__btn" type="button"><span class="bhe-28a__label">Continue</span></button>
</section>
<section class="bhe-28b" aria-label="Echo ripple button">
  <button class="bhe-28b__btn" type="button"><span class="bhe-28b__label">Ping</span></button>
</section>
</div>
```
## CSS
```css
.bhe-28-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-28-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-28a,
.bhe-28a *,
.bhe-28a *::before,
.bhe-28a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-28a {
  --accent: oklch(0.58 0.16 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #081418;
}

.bhe-28a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 17px 44px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-28a__label {
  position: relative;
  z-index: 1;
}

.bhe-28a__btn::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 120px;
  height: 120px;
  margin: -60px 0 0 -60px;
  border-radius: 50%;
  background: rgba(255,255,255,.4);
  transform: scale(0);
  opacity: 1;
  transition: transform .6s ease-out,opacity .6s ease-out;
  z-index: 0;
}

.bhe-28a__btn:hover::before,
.bhe-28a__btn:focus-visible::before {
  transform: scale(4);
  opacity: 0;
}

.bhe-28a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-28a__btn::before {
    transition: opacity .2s;
  }

  .bhe-28a__btn:hover::before,
    .bhe-28a__btn:focus-visible::before {
    transform: scale(0);
    opacity: .3;
  }
}

.bhe-28b,
.bhe-28b *,
.bhe-28b *::before,
.bhe-28b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-28b {
  --accent: oklch(0.6 0.17 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a0c1a;
}

.bhe-28b__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 17px 44px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-28b__label {
  position: relative;
  z-index: 1;
}

.bhe-28b__btn::before,
.bhe-28b__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  border: 2px solid var(--accent);
  opacity: 0;
  pointer-events: none;
}

.bhe-28b__btn:hover::before,
.bhe-28b__btn:focus-visible::before {
  animation: bhe-28b-echo 1.4s ease-out infinite;
}

.bhe-28b__btn:hover::after,
.bhe-28b__btn:focus-visible::after {
  animation: bhe-28b-echo 1.4s ease-out .7s infinite;
}

.bhe-28b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-28b-echo {
  0% {
    opacity: .7;
    transform: scale(1);
  }

  100% {
    opacity: 0;
    transform: scale(1.5);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-28b__btn::before,
    .bhe-28b__btn::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
