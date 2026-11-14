---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/overlay-slide/"
title: "Overlay Slide"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A magazine card where a bold color panel slides up from the bottom to overtake the cover, swapping the teaser for full article details."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Overlay Slide
Source: https://codefronts.com/motion/css-card-hover-effects/overlay-slide/

A magazine card where a bold color panel slides up from the bottom to overtake the cover, swapping the teaser for full article details. A strong choice for editorial grids, issue archives, and publication or portfolio listings.
## HTML
```html
<div class="card-25">
  <article class="card-25__card">
    <div class="card-25__base">
      <span class="card-25__base-cat">Editorial</span>
      <h2 class="card-25__base-title">Issue<br>No. 27</h2>
    </div>
    <div class="card-25__panel">
      <span class="card-25__panel-num">№ 27 — Spring</span>
      <h3 class="card-25__panel-title">The Red<br>Issue</h3>
      <p class="card-25__panel-desc">Forty pages on color, courage, and the people painting cities awake.</p>
      <span class="card-25__panel-link">Read the issue →</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,[email protected],500;6..96,900&family=Work+Sans:wght@400;500&display=swap');

.card-25,
.card-25 *,
.card-25 *::before,
.card-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-25 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #f2f0eb;
  font-family: 'Work Sans', sans-serif;
  padding: 2rem;
}

.card-25__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 2px;
  cursor: pointer;
  overflow: hidden;
  background: #1a1a1a;
  box-shadow: 0 18px 40px rgba(0,0,0,0.2);
}

.card-25__base {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.45)), linear-gradient(135deg, #6b7c8c, #2f3a44);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 2.2rem;
  color: #fff;
}

.card-25__base-cat {
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  opacity: 0.85;
}

.card-25__base-title {
  font-family: 'Bodoni Moda', serif;
  font-weight: 900;
  font-size: 2.4rem;
  line-height: 1;
  margin-top: 0.4rem;
}

.card-25__panel {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #e23744;
  transform: translateY(101%);
  transition: transform 0.55s cubic-bezier(0.76,0,0.24,1);
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #fff;
}

.card-25__card:hover .card-25__panel {
  transform: translateY(0);
}

.card-25__panel-num {
  font-family: 'Bodoni Moda', serif;
  font-style: italic;
  font-size: 1rem;
}

.card-25__panel-title {
  font-family: 'Bodoni Moda', serif;
  font-weight: 900;
  font-size: 2.6rem;
  line-height: 0.95;
}

.card-25__panel-desc {
  font-size: 0.88rem;
  line-height: 1.6;
  color: rgba(255,255,255,0.92);
}

.card-25__panel-link {
  font-size: 0.78rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  border-top: 1px solid rgba(255,255,255,0.4);
  padding-top: 1rem;
}

@media (prefers-reduced-motion: reduce) {
  .card-25__panel {
    transition: none !important;
  }
}
```
