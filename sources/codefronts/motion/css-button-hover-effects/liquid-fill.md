---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/liquid-fill/"
title: "Liquid Fill"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A CTA that fills like a glass of water: on hover a coloured liquid rises from the bottom with an animated wave surface that sways — a bottom-up fill…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Fill
Source: https://codefronts.com/motion/css-button-hover-effects/liquid-fill/

A CTA that fills like a glass of water: on hover a coloured liquid rises from the bottom with an animated wave surface that sways — a bottom-up fill (distinct from topic 13's centre-out blob).
## HTML
```html
<div class="bhe-15-group">
<section class="bhe-15a" aria-label="Liquid wave fill button">
  <button class="bhe-15a__btn" type="button"><span class="bhe-15a__wave" aria-hidden="true"></span><span class="bhe-15a__label">Download</span></button>
</section>
<section class="bhe-15b" aria-label="Tilted flood button">
  <button class="bhe-15b__btn" type="button"><span class="bhe-15b__fill" aria-hidden="true"></span><span class="bhe-15b__label">Install now</span></button>
</section>
</div>
```
## CSS
```css
.bhe-15-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-15-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-15a,
.bhe-15a *,
.bhe-15a *::before,
.bhe-15a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-15a {
  --liquid: oklch(0.6 0.18 235);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0b1020;
}

.bhe-15a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--liquid);
  padding: 18px 44px;
  border: 2px solid var(--liquid);
  border-radius: 12px;
  cursor: pointer;
  background: transparent;
  transition: color .35s .15s;
}

.bhe-15a__label {
  position: relative;
  z-index: 2;
}

.bhe-15a__wave {
  position: absolute;
  left: -50%;
  top: 100%;
  width: 200%;
  height: 100%;
  background: var(--liquid);
  z-index: 1;
  transform: translateY(22px);
  transition: transform .55s cubic-bezier(.4,0,.2,1);
}

.bhe-15a__wave::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 100%;
  width: 100%;
  height: 22px;
  background: radial-gradient(circle at 25% 0,transparent 12px,var(--liquid) 13px) repeat-x;
  background-size: 44px 22px;
}

.bhe-15a__btn:hover .bhe-15a__wave,
.bhe-15a__btn:focus-visible .bhe-15a__wave {
  transform: translateY(-100%);
  animation: bhe-15a-sway 1.6s ease-in-out infinite;
}

.bhe-15a__btn:hover,
.bhe-15a__btn:focus-visible {
  color: #fff;
}

.bhe-15a__btn:focus-visible {
  outline: 3px solid var(--liquid);
  outline-offset: 3px;
}

@keyframes bhe-15a-sway {
  0%,
    100% {
    margin-left: 0;
  }

  50% {
    margin-left: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-15a__wave {
    transition: none;
  }

  .bhe-15a__btn:hover .bhe-15a__wave,
    .bhe-15a__btn:focus-visible .bhe-15a__wave {
    animation: none;
    transform: translateY(-100%);
  }
}

.bhe-15b,
.bhe-15b *,
.bhe-15b *::before,
.bhe-15b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-15b {
  --liquid: oklch(0.7 0.17 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #08160e;
}

.bhe-15b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: var(--liquid);
  padding: 18px 46px;
  border: 2px solid var(--liquid);
  border-radius: 9999px;
  cursor: pointer;
  background: transparent;
  transition: color .3s .12s;
}

.bhe-15b__label {
  position: relative;
  z-index: 1;
}

.bhe-15b__fill {
  position: absolute;
  left: -10%;
  bottom: 0;
  width: 120%;
  height: 180%;
  background: var(--liquid);
  transform: translateY(120%) rotate(6deg);
  transform-origin: center top;
  transition: transform .5s cubic-bezier(.5,0,.2,1);
  z-index: 0;
}

.bhe-15b__btn:hover .bhe-15b__fill,
.bhe-15b__btn:focus-visible .bhe-15b__fill {
  transform: translateY(0) rotate(0deg);
}

.bhe-15b__btn:hover,
.bhe-15b__btn:focus-visible {
  color: #04180d;
}

.bhe-15b__btn:focus-visible {
  outline: 3px solid var(--liquid);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-15b__fill {
    transition: transform .25s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
