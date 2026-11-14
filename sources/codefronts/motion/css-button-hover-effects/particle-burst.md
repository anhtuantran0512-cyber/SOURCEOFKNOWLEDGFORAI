---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/particle-burst/"
title: "Particle Burst"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A celebratory CTA that scatters little particles outward on hover — confetti-style points fly out and fade, adding delight to sign-ups and likes."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Burst
Source: https://codefronts.com/motion/css-button-hover-effects/particle-burst/

A celebratory CTA that scatters little particles outward on hover — confetti-style points fly out and fade, adding delight to sign-ups and likes.
## HTML
```html
<div class="bhe-24-group">
<section class="bhe-24a" aria-label="Particle burst button">
  <button class="bhe-24a__btn" type="button"><span class="bhe-24a__p bhe-24a__p--1" aria-hidden="true"></span><span class="bhe-24a__p bhe-24a__p--2" aria-hidden="true"></span><span class="bhe-24a__label">Like</span></button>
</section>
<section class="bhe-24b" aria-label="Spark ring button">
  <button class="bhe-24b__btn" type="button"><span class="bhe-24b__ring" aria-hidden="true"></span><span class="bhe-24b__label">Boost</span></button>
</section>
</div>
```
## CSS
```css
.bhe-24-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-24-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-24a,
.bhe-24a *,
.bhe-24a *::before,
.bhe-24a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-24a {
  --accent: oklch(0.62 0.22 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #120a0e;
}

.bhe-24a__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 42px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
  overflow: visible;
}

.bhe-24a__label {
  position: relative;
  z-index: 1;
}

.bhe-24a__p {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #ffd15c;
  opacity: 0;
  pointer-events: none;
}

.bhe-24a__p--1 {
  box-shadow: 34px -18px #ff7ab6,-40px -10px #7ce0ff,54px 12px #b6ff7a,-30px 20px #ffd15c;
}

.bhe-24a__p--2 {
  box-shadow: 20px -30px #7ce0ff,-52px 6px #ffd15c,44px 26px #ff7ab6,-18px -26px #b6ff7a;
}

.bhe-24a__btn:hover .bhe-24a__p,
.bhe-24a__btn:focus-visible .bhe-24a__p {
  animation: bhe-24a-burst .6s ease-out;
}

.bhe-24a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-24a-burst {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(.2);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(1.6);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-24a__btn:hover .bhe-24a__p,
    .bhe-24a__btn:focus-visible .bhe-24a__p {
    animation: none;
  }
}

.bhe-24b,
.bhe-24b *,
.bhe-24b *::before,
.bhe-24b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-24b {
  --accent: oklch(0.7 0.17 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #14100a;
}

.bhe-24b__btn {
  position: relative;
  font-size: 16px;
  font-weight: 800;
  color: #1a1206;
  padding: 16px 42px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
  overflow: visible;
}

.bhe-24b__label {
  position: relative;
  z-index: 1;
}

.bhe-24b__ring {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 8px;
  height: 8px;
  margin: -4px 0 0 -4px;
  border-radius: 50%;
  box-shadow: 0 -34px var(--accent),24px -24px var(--accent),34px 0 var(--accent),24px 24px var(--accent),0 34px var(--accent),-24px 24px var(--accent),-34px 0 var(--accent),-24px -24px var(--accent);
  opacity: 0;
  transform: scale(.3);
  pointer-events: none;
}

.bhe-24b__btn:hover .bhe-24b__ring,
.bhe-24b__btn:focus-visible .bhe-24b__ring {
  animation: bhe-24b-spark .55s ease-out;
}

.bhe-24b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-24b-spark {
  0% {
    opacity: 1;
    transform: scale(.3);
  }

  100% {
    opacity: 0;
    transform: scale(1.5);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-24b__btn:hover .bhe-24b__ring,
    .bhe-24b__btn:focus-visible .bhe-24b__ring {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
