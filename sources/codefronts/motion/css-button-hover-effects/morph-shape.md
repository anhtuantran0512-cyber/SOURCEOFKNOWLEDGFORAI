---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/morph-shape/"
title: "Morph Shape"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A clean satisfying CTA that morphs its silhouette on hover: sharp corners round off smoothly into a full pill — a simple geometric transformation that feels…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morph Shape
Source: https://codefronts.com/motion/css-button-hover-effects/morph-shape/

A clean satisfying CTA that morphs its silhouette on hover: sharp corners round off smoothly into a full pill — a simple geometric transformation that feels responsive.
## HTML
```html
<div class="bhe-30-group">
<section class="bhe-30a" aria-label="Morph shape button">
  <button class="bhe-30a__btn" type="button">Send message</button>
</section>
<section class="bhe-30b" aria-label="Pill to notched button">
  <button class="bhe-30b__btn" type="button">Reserve seat</button>
</section>
<section class="bhe-30c" aria-label="Circle to bar button">
  <button class="bhe-30c__btn" type="button"><span class="bhe-30c__short" aria-hidden="true">＋</span><span class="bhe-30c__full">Add item</span></button>
</section>
</div>
```
## CSS
```css
.bhe-30-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-30-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-30a,
.bhe-30a *,
.bhe-30a *::before,
.bhe-30a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-30a {
  --accent: oklch(0.58 0.17 210);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f4f6f8;
}

.bhe-30a__btn {
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 38px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: var(--accent);
  box-shadow: 0 10px 22px -12px color-mix(in oklab,var(--accent) 70%,transparent);
  transition: border-radius .5s cubic-bezier(.4,0,.2,1),transform .3s cubic-bezier(.4,0,.2,1),background .3s;
}

.bhe-30a__btn:hover,
.bhe-30a__btn:focus-visible {
  border-radius: 30px;
  transform: translateY(-2px);
  background: color-mix(in oklab,var(--accent) 88%,black);
}

.bhe-30a__btn:active {
  transform: translateY(0) scale(.98);
}

.bhe-30a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-30a__btn {
    transition: border-radius .25s,background .2s;
  }
}

.bhe-30b,
.bhe-30b *,
.bhe-30b *::before,
.bhe-30b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-30b {
  --accent: oklch(0.6 0.16 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #1a1010;
}

.bhe-30b__btn {
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 40px;
  border: none;
  cursor: pointer;
  background: var(--accent);
  border-radius: 30px 30px 30px 30px;
  box-shadow: 0 12px 24px -12px var(--accent);
  transition: border-radius .5s cubic-bezier(.4,0,.2,1),transform .3s cubic-bezier(.4,0,.2,1);
}

.bhe-30b__btn:hover,
.bhe-30b__btn:focus-visible {
  border-radius: 16px 4px 16px 4px;
  transform: translateY(-2px);
}

.bhe-30b__btn:active {
  transform: translateY(0) scale(.98);
}

.bhe-30b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-30b__btn {
    transition: border-radius .25s;
  }
}

.bhe-30c,
.bhe-30c *,
.bhe-30c *::before,
.bhe-30c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-30c {
  --accent: oklch(0.62 0.16 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0c160f;
}

.bhe-30c__btn {
  position: relative;
  display: grid;
  place-items: center;
  height: 56px;
  width: 56px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 28px;
  cursor: pointer;
  background: var(--accent);
  box-shadow: 0 12px 24px -12px var(--accent);
  overflow: hidden;
  transition: width .45s cubic-bezier(.4,0,.2,1),border-radius .45s cubic-bezier(.4,0,.2,1);
}

.bhe-30c__short {
  font-size: 24px;
  line-height: 1;
  transition: opacity .2s ease;
}

.bhe-30c__full {
  position: absolute;
  white-space: nowrap;
  opacity: 0;
  transition: opacity .2s ease;
}

.bhe-30c__btn:hover,
.bhe-30c__btn:focus-visible {
  width: 170px;
  border-radius: 14px;
}

.bhe-30c__btn:hover .bhe-30c__short,
.bhe-30c__btn:focus-visible .bhe-30c__short {
  opacity: 0;
  transition-duration: .15s;
}

.bhe-30c__btn:hover .bhe-30c__full,
.bhe-30c__btn:focus-visible .bhe-30c__full {
  opacity: 1;
  transition-delay: .25s;
}

.bhe-30c__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-30c__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
