---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/book-open/"
title: "Book Open"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A literary card whose hard cover swings open on a hinge in 3D to reveal the first page and chapter text inside."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Book Open
Source: https://codefronts.com/motion/css-card-hover-effects/book-open/

A literary card whose hard cover swings open on a hinge in 3D to reveal the first page and chapter text inside. Best for publishers, bookstores, courses, and storytelling experiences that benefit from a tactile "open me" gesture.
## HTML
```html
<div class="card-32">
  <article class="card-32__card">
    <div class="card-32__pages">
      <span class="card-32__chapter">Chapter One</span>
      <h2 class="card-32__page-title">The House<br>on Linden Row</h2>
      <p class="card-32__text">"I had not meant to stay the winter. But the house, you understand, had other plans..."</p>
      <span class="card-32__page-no">— 1 —</span>
    </div>
    <div class="card-32__cover">
      <div class="card-32__cover-front">
        <span class="card-32__pub">Harrow &amp; Quill</span>
        <div>
          <h1 class="card-32__cover-title">The House<br>on Linden<br>Row</h1>
          <div class="card-32__rule"></div>
          <span class="card-32__author">by E. Marlowe</span>
        </div>
      </div>
      <div class="card-32__cover-back"></div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Marcellus&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap');

.card-32,
.card-32 *,
.card-32 *::before,
.card-32 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-32 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #2a2018;
  background-image: radial-gradient(circle at 50% 40%, #3a2e22, #1a130d);
  font-family: 'EB Garamond', serif;
  padding: 2rem;
  perspective: 1600px;
}

.card-32__card {
  position: relative;
  width: 300px;
  height: 420px;
  cursor: pointer;
  transform-style: preserve-3d;
}

.card-32__pages {
  position: absolute;
  inset: 0;
  border-radius: 4px 8px 8px 4px;
  background: #f5efe0;
  padding: 2.4rem 2rem 2.4rem 2.6rem;
  box-shadow: inset 18px 0 30px -18px rgba(0,0,0,0.4);
  display: flex;
  flex-direction: column;
  color: #3a2e1f;
}

.card-32__chapter {
  font-family: 'Marcellus', serif;
  font-size: 0.8rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #9a7b4f;
  margin-bottom: 1rem;
}

.card-32__page-title {
  font-family: 'Marcellus', serif;
  font-size: 1.9rem;
  line-height: 1.15;
  margin-bottom: 1rem;
}

.card-32__text {
  font-size: 1rem;
  line-height: 1.65;
  font-style: italic;
  color: #5a4a36;
}

.card-32__page-no {
  margin-top: auto;
  text-align: center;
  font-size: 0.85rem;
  color: #9a7b4f;
}

.card-32__cover {
  position: absolute;
  inset: 0;
  z-index: 2;
  border-radius: 4px 8px 8px 4px;
  transform-origin: left center;
  transform: rotateY(0deg);
  transition: transform 0.9s cubic-bezier(0.65,0,0.35,1), box-shadow 0.9s ease;
  transform-style: preserve-3d;
  box-shadow: 6px 6px 24px rgba(0,0,0,0.5);
}

.card-32__card:hover .card-32__cover {
  transform: rotateY(-145deg);
  box-shadow: -10px 6px 30px rgba(0,0,0,0.4);
}

.card-32__cover-front,
.card-32__cover-back {
  position: absolute;
  inset: 0;
  border-radius: 4px 8px 8px 4px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.card-32__cover-front {
  background: linear-gradient(160deg, #6b2737, #401520);
  padding: 2.6rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e8d8b8;
  border-left: 6px solid #2e0f17;
}

.card-32__cover-back {
  background: #5a1f2c;
  transform: rotateY(180deg);
  box-shadow: inset 0 0 40px rgba(0,0,0,0.4);
}

.card-32__pub {
  font-family: 'Marcellus', serif;
  font-size: 0.72rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #c9a86b;
}

.card-32__cover-title {
  font-family: 'Marcellus', serif;
  font-size: 2.6rem;
  line-height: 1.05;
}

.card-32__rule {
  width: 50px;
  height: 2px;
  background: #c9a86b;
  margin: 0.8rem 0;
}

.card-32__author {
  font-style: italic;
  font-size: 1.05rem;
  color: #d8c3a0;
}

@media (prefers-reduced-motion: reduce) {
  .card-32__cover {
    transition: none !important;
  }
}
```
