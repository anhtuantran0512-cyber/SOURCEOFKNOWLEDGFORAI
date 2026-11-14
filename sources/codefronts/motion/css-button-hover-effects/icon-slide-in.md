---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/icon-slide-in/"
title: "Icon Slide In"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A directional CTA where the label nudges left and an arrow slides in from outside the right edge on hover — a purposeful 'forward' cue for Next / Continue…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Slide In
Source: https://codefronts.com/motion/css-button-hover-effects/icon-slide-in/

A directional CTA where the label nudges left and an arrow slides in from outside the right edge on hover — a purposeful 'forward' cue for Next / Continue actions.
## HTML
```html
<div class="bhe-31-group">
<section class="bhe-31a" aria-label="Icon slide in button">
  <button class="bhe-31a__btn" type="button"><span class="bhe-31a__label">Continue</span><span class="bhe-31a__icon" aria-hidden="true">→</span></button>
</section>
<section class="bhe-31b" aria-label="Icon swap button">
  <button class="bhe-31b__btn" type="button"><span class="bhe-31b__icon" aria-hidden="true">↓</span><span class="bhe-31b__label">Save file</span></button>
</section>
</div>
```
## CSS
```css
.bhe-31-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-31-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-31a,
.bhe-31a *,
.bhe-31a *::before,
.bhe-31a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-31a {
  --accent: oklch(0.55 0.17 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #eef0f6;
}

.bhe-31a__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 34px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-31a__label {
  transition: transform .3s cubic-bezier(.2,.9,.2,1);
}

.bhe-31a__icon {
  width: 0;
  opacity: 0;
  transform: translateX(-6px);
  transition: opacity .3s,transform .3s cubic-bezier(.2,.9,.2,1),width .3s,margin-left .3s;
  font-size: 18px;
  overflow: hidden;
}

.bhe-31a__btn:hover .bhe-31a__label,
.bhe-31a__btn:focus-visible .bhe-31a__label {
  transform: translateX(-4px);
}

.bhe-31a__btn:hover .bhe-31a__icon,
.bhe-31a__btn:focus-visible .bhe-31a__icon {
  opacity: 1;
  transform: translateX(0);
  width: 18px;
  margin-left: 8px;
}

.bhe-31a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-31a__label,
    .bhe-31a__icon {
    transition: opacity .2s;
  }
}

.bhe-31b,
.bhe-31b *,
.bhe-31b *::before,
.bhe-31b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-31b {
  --accent: oklch(0.58 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a1618;
}

.bhe-31b__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 34px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-31b__icon {
  width: 0;
  opacity: 0;
  transform: translateX(6px);
  transition: opacity .3s,transform .3s cubic-bezier(.2,.9,.2,1),width .3s,margin-right .3s;
  font-size: 18px;
  overflow: hidden;
}

.bhe-31b__label {
  transition: transform .3s cubic-bezier(.2,.9,.2,1);
}

.bhe-31b__btn:hover .bhe-31b__icon,
.bhe-31b__btn:focus-visible .bhe-31b__icon {
  opacity: 1;
  transform: translateX(0);
  width: 18px;
  margin-right: 8px;
}

.bhe-31b__btn:hover .bhe-31b__label,
.bhe-31b__btn:focus-visible .bhe-31b__label {
  transform: translateX(4px);
}

.bhe-31b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-31b__icon,
    .bhe-31b__label {
    transition: opacity .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
