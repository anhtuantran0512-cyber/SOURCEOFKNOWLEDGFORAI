---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/slide-up-content/"
title: "Slide Up Content"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A travel/blog card showing a hero image with a minimal label that slides away as a frosted detail panel rises from the bottom."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide Up Content
Source: https://codefronts.com/motion/css-card-hover-effects/slide-up-content/

A travel/blog card showing a hero image with a minimal label that slides away as a frosted detail panel rises from the bottom. A clean, dependable pattern for article grids, portfolios, and product listings that need progressive disclosure.
## HTML
```html
<div class="card-18">
  <article class="card-18__card">
    <div class="card-18__media"></div>
    <div class="card-18__peek">
      <span class="card-18__peek-cat">Travel · 12 min</span>
      <h2 class="card-18__peek-title">Sunset Over<br>Cartagena</h2>
    </div>
    <div class="card-18__panel">
      <span class="card-18__panel-cat">Travel · 12 min read</span>
      <h3 class="card-18__panel-title">Sunset Over Cartagena</h3>
      <p class="card-18__panel-desc">Walled-city rooftops, fruit carts at dusk, and where to find the best ceviche after dark.</p>
      <a class="card-18__panel-link">READ STORY →</a>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=JetBrains+Mono:wght@400;500&display=swap');

.card-18,
.card-18 *,
.card-18 *::before,
.card-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-18 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #e8e4dd;
  font-family: 'Sora', sans-serif;
  padding: 2rem;
}

.card-18__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 20px;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 18px 40px rgba(0,0,0,0.2);
}

.card-18__media {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg, #ff6b4a, #c91f5f 60%, #5b1e6b);
}

.card-18__media::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 25%, rgba(255,255,255,0.3), transparent 50%);
}

.card-18__peek {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 1.8rem;
  z-index: 3;
  color: #fff;
  transition: transform 0.5s cubic-bezier(0.16,1,0.3,1), opacity 0.4s ease;
}

.card-18__peek-cat {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  opacity: 0.85;
}

.card-18__peek-title {
  font-weight: 800;
  font-size: 1.9rem;
  line-height: 1.05;
  margin-top: 0.3rem;
}

.card-18__card:hover .card-18__peek {
  transform: translateY(-130px);
  opacity: 0;
}

.card-18__panel {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(12,8,16,0.92);
  backdrop-filter: blur(8px);
  color: #f0ece6;
  padding: 1.8rem;
  z-index: 4;
  transform: translateY(100%);
  transition: transform 0.5s cubic-bezier(0.16,1,0.3,1);
}

.card-18__card:hover .card-18__panel {
  transform: translateY(0);
}

.card-18__panel-cat {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #ff8a6b;
}

.card-18__panel-title {
  font-weight: 800;
  font-size: 1.7rem;
  line-height: 1.05;
  margin: 0.4rem 0 0.7rem;
}

.card-18__panel-desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #c4bdb4;
}

.card-18__panel-link {
  display: inline-block;
  margin-top: 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  color: #ff8a6b;
  letter-spacing: 0.08em;
}

@media (prefers-reduced-motion: reduce) {
  .card-18__peek,
    .card-18__panel {
    transition: none !important;
  }
}
```
