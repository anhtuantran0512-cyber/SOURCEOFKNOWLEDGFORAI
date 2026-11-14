---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-crystalline-prism-gradient-text/"
title: "CSS Crystalline Prism Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A pastel multi-stop gradient mimics the delicate refractive colours of crystal or cut glass, with animated background-position movement and complementary…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Crystalline Prism Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-crystalline-prism-gradient-text/

A pastel multi-stop gradient mimics the delicate refractive colours of crystal or cut glass, with animated background-position movement and complementary facet stripe accents.
## HTML
```html
<div class="gt-20">
  <span class="gt-20__label">Crystalline prism gradient</span>
  <div class="gt-20__crystal">CRYSTAL</div>
  <div class="gt-20__facets">
    <div class="gt-20__facet"></div>
    <div class="gt-20__facet"></div>
    <div class="gt-20__facet"></div>
    <div class="gt-20__facet"></div>
    <div class="gt-20__facet"></div>
  </div>
  <p class="gt-20__sub">Refractive light spectrum</p>
  <div class="gt-20__gems">
    <span class="gt-20__gem-word">QUARTZ</span>
    <span class="gt-20__gem-word">AGATE</span>
    <span class="gt-20__gem-word">JASPER</span>
    <span class="gt-20__gem-word">OPAL</span>
  </div>
</div>
```
## CSS
```css
.gt-20,
.gt-20 *,
.gt-20 *::before,
.gt-20 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-20 {
  --bg: #e8f0fa;
  font-family: 'Syncopate', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-20__label {
  font-size: .6rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #c0cce0;
}

.gt-20__crystal {
  font-size: clamp(2.5rem, 10vw, 7rem);
  font-weight: 700;
  line-height: 1;
  letter-spacing: .12em;
  background: linear-gradient(
      120deg,
      #b8d4f0 0%,
      #d0e8ff 8%,
      #f0f8ff 15%,
      #c8e0f8 22%,
      #e8d0f8 30%,
      #f0c8e0 38%,
      #f8e0d0 46%,
      #f0f0c8 54%,
      #d0f0d8 62%,
      #c8f0f0 70%,
      #d0d8f8 78%,
      #e8d0f8 86%,
      #f0e8ff 93%,
      #b8d4f0 100%
    );
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-20-prism 6s ease-in-out infinite;
}

.gt-20__facets {
  display: flex;
  gap: 1px;
  justify-content: center;
}

.gt-20__facet {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg,
      #c8e0f8, #e8d0f8, #f0c8e0, #f8e0d0, #d0f0d8
    );
  background-size: 400% 100%;
  animation: gt-20-fscroll 4s linear infinite;
  opacity: .7;
}

.gt-20__facet:nth-child(odd) {
  animation-direction: reverse;
}

.gt-20__facet:nth-child(2) {
  transform: scaleX(.8);
  opacity: .5;
}

.gt-20__facet:nth-child(4) {
  transform: scaleX(.6);
  opacity: .4;
}

.gt-20__facet:nth-child(5) {
  transform: scaleX(.8);
  opacity: .5;
}

.gt-20__sub {
  font-size: clamp(.6rem, 1.8vw, .9rem);
  font-weight: 700;
  letter-spacing: .3em;
  text-transform: uppercase;
  background: linear-gradient(90deg,
      #8ab4d4 0%, #c090c0 33%, #a0c8a0 66%, #8ab4d4 100%
    );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-20-fscroll 5s linear infinite;
}

.gt-20__gems {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.gt-20__gem-word {
  font-size: clamp(.8rem, 2.5vw, 1.1rem);
  font-weight: 700;
  letter-spacing: .1em;
  text-align: center;
  padding: .6em .8em;
  border-radius: 6px;
  background: linear-gradient(135deg,
      #d0e8ff, #e8d0f8, #d0f0d8, #f8e0d0
    );
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  border: 1px solid #c8d8e8;
  animation: gt-20-prism 4s ease-in-out infinite;
}

.gt-20__gem-word:nth-child(2) {
  animation-delay: -.8s;
}

.gt-20__gem-word:nth-child(3) {
  animation-delay: -1.6s;
}

.gt-20__gem-word:nth-child(4) {
  animation-delay: -2.4s;
}

@keyframes gt-20-prism {
  0%,
    100% {
    background-position: 0% 0%;
  }

  50% {
    background-position: 100% 100%;
  }
}

@keyframes gt-20-fscroll {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-20__crystal,
    .gt-20__facet,
    .gt-20__sub,
    .gt-20__gem-word {
    animation: none;
  }
}
```
