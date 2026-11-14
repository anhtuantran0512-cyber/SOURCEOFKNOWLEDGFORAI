---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/border-morph/"
title: "Border Morph"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A wellness/meditation card that morphs from an organic blob shape into a clean rounded rectangle on hover, with icons and buttons reshaping in sync."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Border Morph
Source: https://codefronts.com/motion/css-card-hover-effects/border-morph/

A wellness/meditation card that morphs from an organic blob shape into a clean rounded rectangle on hover, with icons and buttons reshaping in sync. Best for calm, friendly, lifestyle, or health brands where softness is on-brand.
## HTML
```html
<div class="card-22">
  <article class="card-22__card">
    <div class="card-22__inner">
      <div class="card-22__icon">🫧</div>
      <div>
        <h2 class="card-22__title">Bubble<br>Wellness</h2>
        <p class="card-22__desc">A meditation app that breathes with you. Shapes soften and settle as you exhale.</p>
      </div>
      <span class="card-22__btn">Try a session</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=DM+Sans:opsz,[email protected],400;9..40,500&display=swap');

.card-22,
.card-22 *,
.card-22 *::before,
.card-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-22 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #fef0e6;
  background-image: radial-gradient(circle at 80% 10%, #ffe0cc, transparent 50%);
  font-family: 'DM Sans', sans-serif;
  padding: 2rem;
}

.card-22__card {
  position: relative;
  width: 320px;
  height: 420px;
  cursor: pointer;
  background: linear-gradient(155deg, #ff7e54, #ff4d8d);
  color: #fff;
  border-radius: 38% 62% 63% 37% / 41% 44% 56% 59%;
  transition: border-radius 0.7s cubic-bezier(0.34,1.4,0.5,1), transform 0.5s ease, box-shadow 0.5s ease;
  box-shadow: 0 20px 45px rgba(255,77,141,0.35);
  overflow: hidden;
}

.card-22__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.35), transparent 55%);
}

.card-22__card:hover {
  border-radius: 28px;
  transform: translateY(-6px);
  box-shadow: 0 30px 60px rgba(255,77,141,0.45);
}

.card-22__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.6rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-22__icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  display: grid;
  place-items: center;
  font-size: 1.6rem;
  transition: border-radius 0.7s cubic-bezier(0.34,1.4,0.5,1);
}

.card-22__card:hover .card-22__icon {
  border-radius: 16px;
}

.card-22__title {
  font-family: 'Fredoka', sans-serif;
  font-weight: 700;
  font-size: 2.5rem;
  line-height: 1;
}

.card-22__desc {
  font-size: 0.9rem;
  line-height: 1.6;
  color: rgba(255,255,255,0.9);
}

.card-22__btn {
  align-self: flex-start;
  background: #fff;
  color: #ff4d8d;
  font-family: 'Fredoka', sans-serif;
  font-weight: 600;
  padding: 0.7rem 1.6rem;
  border-radius: 999px;
  font-size: 0.9rem;
  transition: border-radius 0.7s cubic-bezier(0.34,1.4,0.5,1);
}

.card-22__card:hover .card-22__btn {
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .card-22__card,
    .card-22__icon,
    .card-22__btn {
    transition: none !important;
  }
}
```
