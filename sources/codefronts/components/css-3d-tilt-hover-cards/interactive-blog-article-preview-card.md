---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/interactive-blog-article-preview-card/"
title: "Interactive Blog Article Preview Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "An editorial card that respects reading: tilt capped at ±4.5° so the headline never smears, while the cover image lifts on its own Z plane and an author +…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Blog Article Preview Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/interactive-blog-article-preview-card/

An editorial card that respects reading: tilt capped at ±4.5° so the headline never smears, while the cover image lifts on its own Z plane and an author + reading-time metadata row slides up from the card's baseline on hover. The restraint is the lesson — content cards earn trust with millimetres, not theatrics.
## HTML
```html
<section class="thc-08" aria-label="Blog article preview tilt card demo">
  <a class="thc-08__link" href="#">
    <article class="thc-08__card">
      <div class="thc-08__frame" aria-hidden="true"><div class="thc-08__cover"><img src="https://picsum.photos/seed/tokens-grammar/640/360" alt="" loading="lazy"></div></div>
      <div class="thc-08__body">
        <p class="thc-08__kicker">Design Systems</p>
        <h3 class="thc-08__title">Why Your Tokens Need a Grammar, Not a Dictionary</h3>
        <div class="thc-08__revealer"><div class="thc-08__meta">
          <span class="thc-08__dot" aria-hidden="true"></span>
          <span>Priya Sharma</span><span class="thc-08__sep" aria-hidden="true">&middot;</span><span>7 min read</span>
        </div></div>
      </div>
    </article>
  </a>
</section>
```
## CSS
```css
.thc-08,
.thc-08 *,
.thc-08 *::before,
.thc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-08 {
  font-family: Georgia,'Times New Roman',serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.97 0.008 85),oklch(0.94 0.014 75));
}

.thc-08 .thc-08__link {
  text-decoration: none;
  display: block;
  width: min(320px,100%);
}

.thc-08 .thc-08__link:focus-visible {
  outline: 3px solid oklch(0.55 0.12 60);
  outline-offset: 5px;
  border-radius: 18px;
}

.thc-08 .thc-08__card {
  border-radius: 16px;
  background: oklch(0.99 0.004 85);
  border: 1px solid oklch(0.89 0.015 80);
  overflow: hidden;
  transform: perspective(1300px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .55s cubic-bezier(.2,.9,.3,1.05),box-shadow .55s ease;
  box-shadow: 0 16px 40px -28px oklch(0.4 0.05 70 / .6);
}

.thc-08 .thc-08__card.is-live {
  transition: transform .09s linear,box-shadow .4s ease;
  box-shadow: 0 26px 54px -26px oklch(0.4 0.06 70 / .7);
}

.thc-08 .thc-08__frame {
  overflow: hidden;
  aspect-ratio: 16/9;
}

.thc-08 .thc-08__cover {
  width: 100%;
  height: 100%;
  background: radial-gradient(80% 90% at 25% 20%,oklch(0.75 0.11 60),transparent 60%),radial-gradient(70% 80% at 80% 80%,oklch(0.6 0.1 30),transparent 60%),oklch(0.55 0.08 45);
  transform: translateZ(30px) scale(1);
  transition: transform .55s cubic-bezier(.2,.9,.3,1.05);
}

.thc-08 .thc-08__card.is-live .thc-08__cover {
  transform: translateZ(30px) scale(1.04);
}

.thc-08 .thc-08__cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thc-08 .thc-08__body {
  padding: 20px 22px 18px;
}

.thc-08 .thc-08__kicker {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.12 50);
}

.thc-08 .thc-08__title {
  margin-top: 8px;
  font-size: 19px;
  line-height: 1.3;
  color: oklch(0.25 0.02 60);
  text-wrap: pretty;
}

.thc-08 .thc-08__revealer {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .32s ease;
}

.thc-08 .thc-08__card.is-live .thc-08__revealer {
  grid-template-rows: 1fr;
}

.thc-08 .thc-08__meta {
  min-height: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  color: oklch(0.5 0.03 60);
}

.thc-08 .thc-08__meta>span:first-of-type {
  margin-top: 12px;
}

.thc-08 .thc-08__meta span {
  margin-top: 12px;
}

.thc-08 .thc-08__dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(140deg,oklch(0.7 0.1 50),oklch(0.55 0.09 30));
}

.thc-08 .thc-08__sep {
  color: oklch(0.75 0.02 60);
}

@media (hover: none) {
  .thc-08 .thc-08__revealer {
    grid-template-rows: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .thc-08 .thc-08__card,
    .thc-08__cover,
    .thc-08__revealer {
    transition: none;
  }

  .thc-08 .thc-08__revealer {
    grid-template-rows: 1fr;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-08 .thc-08__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 4.5; // legibility cap — headlines shimmer past ~5 degrees
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.classList.add('is-live'); // also opens the 0fr → 1fr metadata row
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
