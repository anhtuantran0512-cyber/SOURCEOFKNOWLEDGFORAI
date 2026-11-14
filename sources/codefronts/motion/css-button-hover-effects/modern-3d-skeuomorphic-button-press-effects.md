---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/modern-3d-skeuomorphic-button-press-effects/"
title: "Modern 3D Skeuomorphic Button Press Effects"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A soft tactile neumorphic CTA that appears extruded from the surface using paired light/dark shadows."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern 3D Skeuomorphic Button Press Effects
Source: https://codefronts.com/motion/css-button-hover-effects/modern-3d-skeuomorphic-button-press-effects/

A soft tactile neumorphic CTA that appears extruded from the surface using paired light/dark shadows. On press it depresses inward as the shadows invert to a subtle inset.
## HTML
```html
<div class="bhe-10-group">
<section class="bhe-10a" aria-label="Skeuomorphic press button">
  <button class="bhe-10a__btn" type="button">Save changes</button>
</section>
<section class="bhe-10b" aria-label="Glossy plastic button">
  <button class="bhe-10b__btn" type="button">Confirm order</button>
</section>
</div>
```
## CSS
```css
.bhe-10-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-10-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-10a,
.bhe-10a *,
.bhe-10a *::before,
.bhe-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-10a {
  --surf: #e6e9ef;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: var(--surf);
}

.bhe-10a__btn {
  font-size: 16px;
  font-weight: 800;
  color: oklch(0.5 0.02 265);
  padding: 18px 40px;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  background: var(--surf);
  box-shadow: -6px -6px 14px color-mix(in oklab,var(--surf) 60%,white),7px 7px 16px color-mix(in oklab,var(--surf) 62%,black);
  transition: transform .18s,box-shadow .18s,color .18s;
}

.bhe-10a__btn:hover {
  color: oklch(0.55 0.16 265);
  box-shadow: -8px -8px 18px color-mix(in oklab,var(--surf) 55%,white),9px 9px 20px color-mix(in oklab,var(--surf) 58%,black);
}

.bhe-10a__btn:active {
  transform: translateY(2px);
  box-shadow: inset -4px -4px 10px color-mix(in oklab,var(--surf) 60%,white),inset 5px 5px 12px color-mix(in oklab,var(--surf) 62%,black);
}

.bhe-10a__btn:focus-visible {
  outline: 3px solid oklch(0.55 0.16 265);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-10a__btn {
    transition: box-shadow .12s,color .12s;
  }
}

.bhe-10b,
.bhe-10b *,
.bhe-10b *::before,
.bhe-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-10b {
  --accent: oklch(0.6 0.18 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #e8ecf3;
}

.bhe-10b__btn {
  position: relative;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 18px 42px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 78%,white),var(--accent));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7),inset 0 -6px 12px -6px rgba(0,0,0,.4),0 10px 20px -8px color-mix(in oklab,var(--accent) 60%,transparent);
  text-shadow: 0 1px 1px rgba(0,0,0,.25);
  transition: transform .14s,box-shadow .14s;
}

.bhe-10b__btn::before {
  content: "";
  position: absolute;
  top: 2px;
  left: 8px;
  right: 8px;
  height: 42%;
  border-radius: 12px 12px 40% 40%/12px 12px 60% 60%;
  background: linear-gradient(180deg,rgba(255,255,255,.55),transparent);
  pointer-events: none;
}

.bhe-10b__btn:hover {
  transform: translateY(-1px);
}

.bhe-10b__btn:active {
  transform: translateY(2px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),inset 0 4px 10px -4px rgba(0,0,0,.5),0 4px 10px -6px color-mix(in oklab,var(--accent) 60%,transparent);
}

.bhe-10b__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-10b__btn {
    transition: box-shadow .1s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
