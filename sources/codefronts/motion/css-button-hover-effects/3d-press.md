---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/3d-press/"
title: "3D Press"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A deeply tactile CTA on a thick 3D base like a plunger key."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Press
Source: https://codefronts.com/motion/css-button-hover-effects/3d-press/

A deeply tactile CTA on a thick 3D base like a plunger key. On press it drives straight down while the base shadow compresses — a straight vertical plunge (distinct from topic 06's isometric tilt).
## HTML
```html
<div class="bhe-35-group">
<section class="bhe-35a" aria-label="3D plunger press button">
  <button class="bhe-35a__btn" type="button">Confirm</button>
</section>
<section class="bhe-35b" aria-label="Chunky keycap button">
  <button class="bhe-35b__btn" type="button">Enter ⏎</button>
</section>
</div>
```
## CSS
```css
.bhe-35-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-35-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-35a,
.bhe-35a *,
.bhe-35a *::before,
.bhe-35a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-35a {
  --cap: oklch(0.62 0.2 25);
  --base: oklch(0.4 0.15 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 60px 24px;
  background: #160a08;
}

.bhe-35a__btn {
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  padding: 16px 42px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--cap);
  transform: translateY(-8px);
  box-shadow: 0 8px 0 var(--base),0 14px 18px -6px rgba(0,0,0,.5);
  transition: transform .12s ease,box-shadow .12s ease;
}

.bhe-35a__btn:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 0 var(--base),0 18px 22px -6px rgba(0,0,0,.5);
}

.bhe-35a__btn:active {
  transform: translateY(-2px);
  box-shadow: 0 2px 0 var(--base),0 6px 10px -4px rgba(0,0,0,.5);
}

.bhe-35a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-35a__btn {
    transition: box-shadow .1s;
  }
}

.bhe-35b,
.bhe-35b *,
.bhe-35b *::before,
.bhe-35b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-35b {
  --cap: oklch(0.9 0.02 260);
  --base: oklch(0.62 0.03 260);
  font-family: ui-monospace,'Segoe UI',monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 60px 24px;
  background: #1c2030;
}

.bhe-35b__btn {
  font-size: 16px;
  font-weight: 800;
  color: #2a2f42;
  padding: 18px 40px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: linear-gradient(180deg,#fff,var(--cap));
  transform: translateY(-10px);
  box-shadow: 0 10px 0 var(--base),inset 0 2px 0 #fff,0 16px 20px -6px rgba(0,0,0,.5);
  transition: transform .1s ease,box-shadow .1s ease;
}

.bhe-35b__btn:active {
  transform: translateY(-2px);
  box-shadow: 0 2px 0 var(--base),inset 0 2px 0 #fff,0 6px 10px -4px rgba(0,0,0,.5);
}

.bhe-35b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-35b__btn {
    transition: box-shadow .1s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
