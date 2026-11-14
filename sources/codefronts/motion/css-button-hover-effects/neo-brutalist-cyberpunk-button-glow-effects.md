---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/neo-brutalist-cyberpunk-button-glow-effects/"
title: "Neo-Brutalist & Cyberpunk Button Glow Effects"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A loud neo-brutalist CTA: flat fill, thick solid border and a hard blur-free offset shadow."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist & Cyberpunk Button Glow Effects
Source: https://codefronts.com/motion/css-button-hover-effects/neo-brutalist-cyberpunk-button-glow-effects/

A loud neo-brutalist CTA: flat fill, thick solid border and a hard blur-free offset shadow. On hover it snaps onto its shadow and the shadow flips to saturated neon — a hard, instant snap (not a soft glow).
## HTML
```html
<div class="bhe-11-group">
<section class="bhe-11a" aria-label="Neo-brutalist neon button">
  <button class="bhe-11a__btn" type="button">Subscribe</button>
</section>
<section class="bhe-11b" aria-label="Brutalist sticker button">
  <button class="bhe-11b__btn" type="button">Get access</button>
</section>
</div>
```
## CSS
```css
.bhe-11-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-11-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-11a,
.bhe-11a *,
.bhe-11a *::before,
.bhe-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-11a {
  font-family: 'Space Grotesk',ui-monospace,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #f5e94a;
}

.bhe-11a__btn {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: .02em;
  text-transform: uppercase;
  color: #111;
  padding: 17px 38px;
  border: 3px solid #111;
  border-radius: 0;
  cursor: pointer;
  background: #fff;
  box-shadow: 7px 7px 0 #111;
  transition: transform .12s ease,box-shadow .12s ease;
}

.bhe-11a__btn:hover {
  transform: translate(7px,7px);
  box-shadow: 0 0 0 #111,0 0 22px 2px #ff2bd6,0 0 34px 6px rgba(34,227,255,.7);
}

.bhe-11a__btn:active {
  transform: translate(7px,7px) scale(.98);
}

.bhe-11a__btn:focus-visible {
  outline: 3px solid #111;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-11a__btn {
    transition: box-shadow .12s;
  }

  .bhe-11a__btn:hover {
    transform: none;
  }
}

.bhe-11b,
.bhe-11b *,
.bhe-11b *::before,
.bhe-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-11b {
  font-family: 'Space Grotesk',ui-monospace,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #111;
}

.bhe-11b__btn {
  font-size: 17px;
  font-weight: 800;
  text-transform: uppercase;
  color: #111;
  padding: 17px 40px;
  border: 3px solid #111;
  border-radius: 10px;
  cursor: pointer;
  background: #4df08a;
  box-shadow: -6px 6px 0 #111;
  transition: transform .12s,box-shadow .12s,background .12s;
}

.bhe-11b__btn:hover {
  transform: translate(-6px,6px);
  box-shadow: 0 0 0 #111;
  background: #ffe14d;
}

.bhe-11b__btn:active {
  transform: translate(-6px,6px) scale(.98);
}

.bhe-11b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-11b__btn {
    transition: background .12s;
  }

  .bhe-11b__btn:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
