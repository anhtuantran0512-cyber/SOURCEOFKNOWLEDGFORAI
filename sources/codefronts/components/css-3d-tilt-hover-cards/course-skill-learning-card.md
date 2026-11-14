---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/course-skill-learning-card/"
title: "Course Skill Learning Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "An EdTech course card where progress is the hero: a 68%-complete pill floats above everything at translateZ(40px), the progress bar's fill glints as the card…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Course Skill Learning Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/course-skill-learning-card/

An EdTech course card where progress is the hero: a 68%-complete pill floats above everything at translateZ(40px), the progress bar's fill glints as the card tilts, and module metadata sits calmly at a lower depth. Built for course catalogs where a dozen of these share a grid — so the motion budget is deliberately mid-range.
## HTML
```html
<section class="thc-14" aria-label="Course learning progress tilt card demo">
  <article class="thc-14__card" tabindex="0" aria-label="Advanced CSS Architecture course, 68 percent complete, 12 modules">
    <span class="thc-14__pill">68% complete</span>
    <div class="thc-14__thumb" aria-hidden="true"><span class="thc-14__glyph">{ }</span></div>
    <h3 class="thc-14__title">Advanced CSS Architecture</h3>
    <p class="thc-14__meta">12 modules &middot; 6.5 hrs &middot; Cert included</p>
    <div class="thc-14__track" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Course progress">
      <div class="thc-14__fill" style="--progress:68%"></div>
    </div>
    <button class="thc-14__cta" type="button">Resume &middot; Module 9</button>
  </article>
</section>
```
## CSS
```css
.thc-14,
.thc-14 *,
.thc-14 *::before,
.thc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-14 {
  --acc: oklch(0.72 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 60px 24px 48px;
  background: linear-gradient(180deg,oklch(0.97 0.008 155),oklch(0.93 0.015 170));
}

.thc-14 .thc-14__card {
  position: relative;
  width: min(300px,100%);
  padding: 24px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid oklch(0.9 0.01 160);
  transform: perspective(1100px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .55s cubic-bezier(.2,.9,.3,1.1),box-shadow .55s ease;
  box-shadow: 0 18px 44px -30px oklch(0.4 0.08 160 / .6);
  cursor: pointer;
}

.thc-14 .thc-14__card.is-live {
  transition: transform .08s linear,box-shadow .4s ease;
  box-shadow: 0 30px 56px -26px oklch(0.4 0.1 160 / .65);
}

.thc-14 .thc-14__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 4px;
}

.thc-14 .thc-14__pill {
  position: absolute;
  top: -14px;
  right: 18px;
  font: 700 11px 'Segoe UI',sans-serif;
  color: #fff;
  background: linear-gradient(120deg,var(--acc),oklch(0.6 0.14 190));
  border-radius: 999px;
  padding: 8px 14px;
  transform: translateZ(40px);
  box-shadow: 0 10px 22px -10px color-mix(in oklab,var(--acc) 80%,transparent);
  animation: thc-14-bob 3.8s ease-in-out infinite;
}

@keyframes thc-14-bob {
  50% {
    margin-top: -5px;
  }
}

.thc-14 .thc-14__thumb {
  width: 100%;
  aspect-ratio: 16/8;
  border-radius: 14px;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 100% at 30% 20%,color-mix(in oklab,var(--acc) 35%,oklch(0.25 0.03 200)),oklch(0.22 0.03 220));
  transform: translateZ(18px);
}

.thc-14 .thc-14__glyph {
  font: 700 34px ui-monospace,monospace;
  color: color-mix(in oklab,var(--acc) 80%,white);
}

.thc-14 .thc-14__title {
  margin-top: 16px;
  font-size: 18px;
  font-weight: 700;
  color: oklch(0.24 0.02 200);
  transform: translateZ(24px);
  text-wrap: pretty;
}

.thc-14 .thc-14__meta {
  margin-top: 6px;
  font-size: 12px;
  color: oklch(0.55 0.02 200);
  transform: translateZ(12px);
}

.thc-14 .thc-14__track {
  margin-top: 16px;
  height: 8px;
  border-radius: 999px;
  background: oklch(0.93 0.01 160);
  overflow: hidden;
  transform: translateZ(20px);
}

.thc-14 .thc-14__fill {
  width: var(--progress,0%);
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg,var(--acc),oklch(0.62 0.14 190)),linear-gradient(115deg,transparent 40%,rgba(255,255,255,.55) 50%,transparent 60%);
  background-size: 100% 100%,300% 100%;
  background-position: 0 0,var(--mx,50%) 0;
  background-blend-mode: overlay;
}

.thc-14 .thc-14__cta {
  margin-top: 18px;
  width: 100%;
  height: 42px;
  border: none;
  border-radius: 11px;
  font: 600 13px 'Segoe UI',sans-serif;
  color: #fff;
  background: oklch(0.35 0.04 200);
  cursor: pointer;
  transform: translateZ(30px);
  transition: background .25s ease;
}

.thc-14 .thc-14__cta:hover {
  background: oklch(0.3 0.05 200);
}

.thc-14 .thc-14__cta:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-14 .thc-14__card {
    transition: none;
  }

  .thc-14__pill {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-14 .thc-14__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 8; // grid-safe motion budget for catalog pages
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--mx', (px * 100).toFixed(1) + '%'); // slides the bar glint
    card.classList.add('is-live');
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
