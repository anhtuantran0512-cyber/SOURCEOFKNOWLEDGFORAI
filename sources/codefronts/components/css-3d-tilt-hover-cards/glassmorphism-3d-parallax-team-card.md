---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/glassmorphism-3d-parallax-team-card/"
title: "Glassmorphism 3D Parallax Team Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A frosted-glass profile card for agency About pages: the avatar ring, name block and social pills each hover at a different translateZ depth behind real…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism 3D Parallax Team Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/glassmorphism-3d-parallax-team-card/

A frosted-glass profile card for agency About pages: the avatar ring, name block and social pills each hover at a different translateZ depth behind real backdrop-filter blur, over an oklch aurora that glows through the glass as the card tilts. The gradient hairline border is drawn with the background-clip trick — no extra wrapper.
## HTML
```html
<section class="thc-02" aria-label="Glassmorphism team profile tilt card demo">
  <article class="thc-02__card" tabindex="0" aria-label="Maya Chen, Design Director">
    <div class="thc-02__ring" aria-hidden="true"><div class="thc-02__avatar"><img src="https://i.pravatar.cc/180?img=47" alt="" loading="lazy"></div></div>
    <h3 class="thc-02__name">Maya Chen</h3>
    <p class="thc-02__role">Design Director</p>
    <p class="thc-02__bio">Leads brand systems and motion for product teams across three time zones.</p>
    <div class="thc-02__socials" aria-label="Social links">
      <a class="thc-02__pill" href="#">Portfolio</a>
      <a class="thc-02__pill" href="#">LinkedIn</a>
    </div>
    <div class="thc-02__glare" aria-hidden="true"></div>
  </article>
</section>
```
## CSS
```css
.thc-02,
.thc-02 *,
.thc-02 *::before,
.thc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-02 {
  --a: oklch(0.7 0.16 200);
  --b: oklch(0.65 0.19 310);
  --spin: 7s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(70% 90% at 20% 15%,oklch(0.4 0.13 310 / .8),transparent 55%),radial-gradient(80% 90% at 85% 90%,oklch(0.45 0.12 210 / .8),transparent 55%),oklch(0.16 0.02 280);
}

.thc-02 .thc-02__card {
  position: relative;
  width: min(310px,100%);
  padding: 34px 28px 30px;
  text-align: center;
  border: 1px solid transparent;
  border-radius: 24px;
  background: linear-gradient(rgba(255,255,255,.07),rgba(255,255,255,.04)) padding-box,linear-gradient(150deg,rgba(255,255,255,.45),rgba(255,255,255,.06) 40%,rgba(255,255,255,.28)) border-box;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  transform: perspective(1100px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.2,.9,.3,1.1);
  box-shadow: 0 30px 70px -30px rgba(0,0,0,.7);
}

.thc-02 .thc-02__card.is-live {
  transition: transform .08s linear;
}

.thc-02 .thc-02__card:focus-visible {
  outline: 3px solid var(--a);
  outline-offset: 4px;
}

.thc-02 .thc-02__ring {
  width: 92px;
  height: 92px;
  margin: 0 auto;
  padding: 3px;
  border-radius: 50%;
  background: conic-gradient(from var(--ang,0deg),var(--a),var(--b),var(--a));
  animation: thc-02-spin var(--spin) linear infinite;
  transform: translateZ(45px);
  display: grid;
  place-items: center;
}

@property --ang {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@keyframes thc-02-spin {
  100% {
    --ang: 360deg;
  }
}

.thc-02 .thc-02__avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  display: grid;
  place-items: center;
  font: 700 26px 'Segoe UI',sans-serif;
  color: #fff;
  background: linear-gradient(160deg,oklch(0.45 0.1 290),oklch(0.3 0.06 260));
  border: 3px solid oklch(0.18 0.02 280);
}

.thc-02 .thc-02__avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.thc-02 .thc-02__name {
  margin-top: 18px;
  font-size: 21px;
  font-weight: 700;
  color: #fff;
  transform: translateZ(28px);
}

.thc-02 .thc-02__role {
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--a) 75%,white);
  margin-top: 4px;
  transform: translateZ(28px);
}

.thc-02 .thc-02__bio {
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(255,255,255,.65);
  margin-top: 14px;
  transform: translateZ(18px);
}

.thc-02 .thc-02__socials {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
  transform: translateZ(55px);
}

.thc-02 .thc-02__pill {
  font: 600 12px 'Segoe UI',sans-serif;
  color: #fff;
  text-decoration: none;
  padding: 9px 16px;
  border-radius: 999px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
  transition: background .25s ease;
}

.thc-02 .thc-02__pill:hover {
  background: rgba(255,255,255,.22);
}

.thc-02 .thc-02__pill:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.thc-02 .thc-02__glare {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: radial-gradient(300px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.16),transparent 60%);
  opacity: 0;
  transition: opacity .4s ease;
}

.thc-02 .thc-02__card.is-live .thc-02__glare {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .thc-02 .thc-02__card {
    transition: none;
  }

  .thc-02__ring {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-02 .thc-02__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 10; // glass reads best under 12 degrees
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    card.classList.add('is-live');
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
