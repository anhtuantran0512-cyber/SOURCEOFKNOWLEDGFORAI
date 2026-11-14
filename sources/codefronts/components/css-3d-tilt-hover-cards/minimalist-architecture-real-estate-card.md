---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/minimalist-architecture-real-estate-card/"
title: "Minimalist Architecture Real Estate Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A luxury listing card built on absence: acres of white, one hairline rule, serif numerals — and a property photo that lives in grayscale until hover drains…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Architecture Real Estate Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/minimalist-architecture-real-estate-card/

A luxury listing card built on absence: acres of white, one hairline rule, serif numerals — and a property photo that lives in grayscale until hover drains the filter away as the card tilts a fluid ±7°. The grayscale-to-color transition is doing the persuasion; the 3D just makes it feel hand-held.
## HTML
```html
<section class="thc-11" aria-label="Minimalist real estate tilt card demo">
  <a class="thc-11__link" href="#">
    <article class="thc-11__card">
      <div class="thc-11__frame" aria-hidden="true"><div class="thc-11__photo"><img src="https://picsum.photos/seed/cliffside-142/620/465" alt="" loading="lazy"></div></div>
      <div class="thc-11__body">
        <div class="thc-11__row">
          <h3 class="thc-11__price">$2,450,000</h3>
          <span class="thc-11__status">FOR SALE</span>
        </div>
        <p class="thc-11__addr">142 Cliffside Terrace, Byron Bay</p>
        <hr class="thc-11__rule">
        <div class="thc-11__meta">
          <span>4 BD</span><span>3 BA</span><span>380 M&sup2;</span><span>OCEAN</span>
        </div>
      </div>
    </article>
  </a>
</section>
```
## CSS
```css
.thc-11,
.thc-11 *,
.thc-11 *::before,
.thc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.965 0.004 90);
}

.thc-11 .thc-11__link {
  text-decoration: none;
  display: block;
  width: min(310px,100%);
}

.thc-11 .thc-11__link:focus-visible {
  outline: 2px solid oklch(0.3 0.02 60);
  outline-offset: 6px;
}

.thc-11 .thc-11__card {
  background: #fff;
  border: 1px solid oklch(0.91 0.006 90);
  overflow: hidden;
  transform: perspective(1200px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .75s cubic-bezier(.2,.8,.2,1),box-shadow .75s ease;
  box-shadow: 0 20px 50px -34px oklch(0.3 0.02 60 / .5);
}

.thc-11 .thc-11__card.is-live {
  transition: transform .1s linear,box-shadow .5s ease;
  box-shadow: 0 34px 64px -30px oklch(0.3 0.02 60 / .5);
}

.thc-11 .thc-11__frame {
  overflow: hidden;
  aspect-ratio: 4/3;
}

.thc-11 .thc-11__photo {
  width: 100%;
  height: 100%;
  transform: translateZ(25px);
  background: radial-gradient(90% 70% at 50% 100%,oklch(0.62 0.07 220),transparent 55%),linear-gradient(180deg,oklch(0.85 0.04 230) 0 45%,oklch(0.75 0.05 90) 45% 60%,oklch(0.55 0.05 70) 60%);
  filter: grayscale(1) contrast(1.05);
  transition: filter .7s ease;
}

.thc-11 .thc-11__card.is-live .thc-11__photo {
  filter: grayscale(0) contrast(1);
}

.thc-11 .thc-11__photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thc-11 .thc-11__body {
  padding: 22px 24px 24px;
  transform: translateZ(15px);
}

.thc-11 .thc-11__row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
}

.thc-11 .thc-11__price {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 26px;
  font-weight: 500;
  letter-spacing: -.01em;
  color: oklch(0.22 0.01 60);
  font-variant-numeric: lining-nums;
}

.thc-11 .thc-11__status {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: .2em;
  color: oklch(0.45 0.02 60);
}

.thc-11 .thc-11__addr {
  margin-top: 6px;
  font-size: 12.5px;
  color: oklch(0.5 0.015 60);
}

.thc-11 .thc-11__rule {
  border: none;
  border-top: 1px solid oklch(0.9 0.006 90);
  margin: 18px 0 14px;
}

.thc-11 .thc-11__meta {
  display: flex;
  gap: 18px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .14em;
  color: oklch(0.4 0.015 60);
}

@media (prefers-reduced-motion: reduce) {
  .thc-11 .thc-11__card,
    .thc-11__photo {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-11 .thc-11__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 7; // fluid but unhurried — match the brand's pace
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.classList.add('is-live'); // develops the photo from grayscale to colour
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
