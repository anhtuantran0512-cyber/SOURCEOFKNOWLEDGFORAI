---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-floating-action-button-fab/"
title: "Liquid Glass Floating Action Button (FAB)"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A tactile glass FAB anchored bottom-right that expands into a radial fan of frosted sub-action buttons on tap — each one floating in with a staggered spring."
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Floating Action Button (FAB)
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-floating-action-button-fab/

A tactile glass FAB anchored bottom-right that expands into a radial fan of frosted sub-action buttons on tap — each one floating in with a staggered spring. Mobile-first, out of the way, and pure CSS via a hidden checkbox so it's keyboard-operable.
## HTML
```html
<section class="lg-18" aria-label="Liquid glass floating action button">
  <img class="lg-18__bg" src="https://picsum.photos/seed/lgfab/1000/750" width="1000" height="750" alt="App backdrop">
  <div class="lg-18__dock">
    <input class="lg-18__sr" type="checkbox" id="lg-18-open">
    <a class="lg-18__sub" style="--d:1" href="#lg-18" aria-label="Share">↗</a>
    <a class="lg-18__sub" style="--d:2" href="#lg-18" aria-label="Add photo">◨</a>
    <a class="lg-18__sub" style="--d:3" href="#lg-18" aria-label="New note">✎</a>
    <label class="lg-18__fab" for="lg-18-open" aria-label="Open actions"><span class="lg-18__plus"></span></label>
  </div>
</section>
```
## CSS
```css
.lg-18,
.lg-18 *,
.lg-18 *::before,
.lg-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-18 {
  --accent: oklch(0.64 0.2 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: #100c1e;
}

.lg-18__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lg-18__dock {
  position: absolute;
  right: 32px;
  bottom: 32px;
  width: 62px;
  height: 62px;
}

.lg-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.lg-18__fab {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: grid;
  place-items: center;
  border-radius: 50%;
  cursor: pointer;
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 82%,white),var(--accent));
  border: 1px solid color-mix(in oklab,var(--accent) 40%,white);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 16px 30px -12px rgba(0,0,0,.7);
  transition: transform .3s;
}

.lg-18__plus {
  position: relative;
  width: 22px;
  height: 22px;
}

.lg-18__plus::before,
.lg-18__plus::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 2.5px;
  border-radius: 2px;
  background: #fff;
  transform: translate(-50%,-50%);
  transition: transform .3s;
}

.lg-18__plus::after {
  transform: translate(-50%,-50%) rotate(90deg);
}

.lg-18__sub {
  position: absolute;
  right: 11px;
  bottom: 11px;
  z-index: 2;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  text-decoration: none;
  font-size: 17px;
  color: #fff;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 10px 22px -10px rgba(0,0,0,.6);
  backdrop-filter: blur(14px) saturate(170%);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
  transform: scale(0);
  opacity: 0;
  transition: transform .4s cubic-bezier(.3,1.3,.5,1),opacity .3s;
  transition-delay: calc(var(--d) * 40ms);
}

.lg-18__sub:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-18__sr:checked~.lg-18__fab {
  transform: rotate(135deg);
}

.lg-18__sr:checked~.lg-18__sub {
  opacity: 1;
}

.lg-18__sr:checked~.lg-18__sub[style*="--d:1"] {
  transform: translateY(-74px);
}

.lg-18__sr:checked~.lg-18__sub[style*="--d:2"] {
  transform: translate(-52px,-52px);
}

.lg-18__sr:checked~.lg-18__sub[style*="--d:3"] {
  transform: translateX(-74px);
}

.lg-18__sr:focus-visible~.lg-18__fab {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-18__sub {
    transition: opacity .2s;
  }

  .lg-18__fab {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden, focusable checkbox toggles the open state; on :checked the sub-actions transform from scale(0) at the FAB centre out into a radial fan with staggered transition-delay. */
```
