---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/center-underline-draw/"
title: "Center Underline Draw"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A minimal text-link CTA where a crisp underline grows outward from the centre to full width on hover — the cleanest affordance for nav links and inline CTAs."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Center Underline Draw
Source: https://codefronts.com/motion/css-button-hover-effects/center-underline-draw/

A minimal text-link CTA where a crisp underline grows outward from the centre to full width on hover — the cleanest affordance for nav links and inline CTAs.
## HTML
```html
<div class="bhe-22-group">
<section class="bhe-22a" aria-label="Center underline button">
  <button class="bhe-22a__btn" type="button">Learn more</button>
</section>
<section class="bhe-22b" aria-label="Ink swipe underline button">
  <button class="bhe-22b__btn" type="button">Read essay</button>
</section>
<section class="bhe-22c" aria-label="Double rule underline button">
  <button class="bhe-22c__btn" type="button">See pricing</button>
</section>
</div>
```
## CSS
```css
.bhe-22-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-22-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-22a,
.bhe-22a *,
.bhe-22a *::before,
.bhe-22a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-22a {
  --line: oklch(0.55 0.18 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #fafafa;
}

.bhe-22a__btn {
  position: relative;
  font-size: 18px;
  font-weight: 700;
  color: #1a1a1a;
  padding: 6px 4px 10px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-22a__btn::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 0;
  height: 2px;
  background: var(--line);
  transform: translateX(-50%);
  transition: width .3s ease;
}

.bhe-22a__btn:hover::after,
.bhe-22a__btn:focus-visible::after {
  width: 100%;
}

.bhe-22a__btn:hover,
.bhe-22a__btn:focus-visible {
  color: var(--line);
}

.bhe-22a__btn:focus-visible {
  outline: none;
}

.bhe-22a__btn:focus-visible::after {
  width: 100%;
  height: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-22a__btn::after {
    transition: none;
  }
}

.bhe-22b,
.bhe-22b *,
.bhe-22b *::before,
.bhe-22b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-22b {
  --line: oklch(0.5 0.15 25);
  font-family: Georgia,'Times New Roman',serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #fbf8f3;
}

.bhe-22b__btn {
  position: relative;
  font-size: 20px;
  font-style: italic;
  color: #241c17;
  padding: 4px 2px 10px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-22b__btn::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 2px;
  width: 100%;
  height: 3px;
  background: var(--line);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .35s cubic-bezier(.6,0,.2,1);
}

.bhe-22b__btn:hover::after,
.bhe-22b__btn:focus-visible::after {
  transform: scaleX(1);
  transform-origin: left;
}

.bhe-22b__btn:focus-visible {
  outline: none;
  color: var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .bhe-22b__btn::after {
    transition: none;
  }
}

.bhe-22c,
.bhe-22c *,
.bhe-22c *::before,
.bhe-22c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-22c {
  --line: oklch(0.55 0.14 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f4f8f8;
}

.bhe-22c__btn {
  position: relative;
  font-size: 18px;
  font-weight: 700;
  color: #0e2a2c;
  padding: 6px 4px 14px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.bhe-22c__btn::before,
.bhe-22c__btn::after {
  content: "";
  position: absolute;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--line);
  transform: scaleX(0);
  transition: transform .3s ease;
}

.bhe-22c__btn::before {
  bottom: 6px;
  transform-origin: left;
}

.bhe-22c__btn::after {
  bottom: 0;
  transform-origin: right;
  transition-delay: .08s;
}

.bhe-22c__btn:hover::before,
.bhe-22c__btn:focus-visible::before,
.bhe-22c__btn:hover::after,
.bhe-22c__btn:focus-visible::after {
  transform: scaleX(1);
}

.bhe-22c__btn:focus-visible {
  outline: none;
  color: var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .bhe-22c__btn::before,
    .bhe-22c__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
