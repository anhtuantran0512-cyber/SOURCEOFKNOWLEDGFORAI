---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/magazine-split-slider/"
title: "Magazine Split Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A featured-article slider split down the middle: a large photo on one side, a headline and excerpt on the other."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magazine Split Slider
Source: https://codefronts.com/snippets/css-image-carousel/magazine-split-slider/

A featured-article slider split down the middle: a large photo on one side, a headline and excerpt on the other. Radio controls cross-fade between stories, and the layout stacks to a single column on mobile — the editorial hero for content sites.
## HTML
```html
<section class="car-10" aria-label="Featured articles">
  <div class="car-10__wrap">
    <input type="radio" name="car-10" id="car-10-1" class="car-10__radio" checked>
    <input type="radio" name="car-10" id="car-10-2" class="car-10__radio">
    <input type="radio" name="car-10" id="car-10-3" class="car-10__radio">
    <div class="car-10__stage">
      <article class="car-10__slide"><div class="car-10__pic"><img src="https://picsum.photos/seed/mag-1/900/700" width="900" height="700" alt="Aerial view of a coastal city"></div><div class="car-10__text"><span class="car-10__cat">City Guide</span><h3 class="car-10__title">48 hours in Lisbon, off the tourist trail</h3><p class="car-10__ex">Where locals actually eat, drink and swim — a slower map of the city's seven hills.</p><a class="car-10__more" href="#">Read story →</a></div></article>
      <article class="car-10__slide"><div class="car-10__pic"><img src="https://picsum.photos/seed/mag-2/900/700" width="900" height="700" alt="Studio workspace with plants"></div><div class="car-10__text"><span class="car-10__cat">Workspaces</span><h3 class="car-10__title">The quiet rise of the two-hour workday</h3><p class="car-10__ex">Deep-work rituals from designers who ship more by doing less, on purpose.</p><a class="car-10__more" href="#">Read story →</a></div></article>
      <article class="car-10__slide"><div class="car-10__pic"><img src="https://picsum.photos/seed/mag-3/900/700" width="900" height="700" alt="Close-up of ceramic bowls"></div><div class="car-10__text"><span class="car-10__cat">Craft</span><h3 class="car-10__title">Why handmade ceramics are having a moment</h3><p class="car-10__ex">A generation trading screens for clay, and the studios teaching them how.</p><a class="car-10__more" href="#">Read story →</a></div></article>
    </div>
    <div class="car-10__dots">
      <label class="car-10__dot" for="car-10-1" aria-label="Story 1"></label>
      <label class="car-10__dot" for="car-10-2" aria-label="Story 2"></label>
      <label class="car-10__dot" for="car-10-3" aria-label="Story 3"></label>
    </div>
  </div>
</section>
```
## CSS
```css
.car-10,
.car-10 *,
.car-10 *::before,
.car-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-10 ::selection {
  background: #c0392b;
  color: #fff;
}

.car-10 {
  --accent: #c0392b;
  font-family: Georgia,'Times New Roman',serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f7f3ec;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-10__wrap {
  width: min(880px,100%);
}

.car-10__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.car-10__stage {
  position: relative;
  background: #fff;
  border: 1px solid #e6ddce;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 24px 50px -34px rgba(80,50,20,.6);
  min-height: 340px;
}

.car-10__slide {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  opacity: 0;
  transition: opacity .5s ease;
  pointer-events: none;
}

.car-10__pic {
  overflow: hidden;
  background: #e9e0d0;
}

.car-10__pic img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-10__text {
  padding: clamp(22px,4vw,44px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.car-10__cat {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 12px;
}

.car-10__title {
  font-size: clamp(22px,3.4vw,30px);
  line-height: 1.16;
  color: #241d15;
  margin-bottom: 14px;
  text-wrap: balance;
}

.car-10__ex {
  font-size: 15px;
  line-height: 1.6;
  color: #665a4a;
  margin-bottom: 20px;
}

.car-10__more {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: #241d15;
  text-decoration: none;
  border-bottom: 2px solid var(--accent);
  align-self: flex-start;
  padding-bottom: 2px;
}

.car-10__radio:nth-of-type(1):checked ~ .car-10__stage .car-10__slide:nth-child(1),
.car-10__radio:nth-of-type(2):checked ~ .car-10__stage .car-10__slide:nth-child(2),
.car-10__radio:nth-of-type(3):checked ~ .car-10__stage .car-10__slide:nth-child(3) {
  opacity: 1;
  pointer-events: auto;
}

.car-10__dots {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 18px;
}

.car-10__dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #d8ccb8;
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.car-10__dot:hover {
  background: #b7a68b;
}

.car-10__radio:nth-of-type(1):checked ~ .car-10__dots .car-10__dot:nth-child(1),
.car-10__radio:nth-of-type(2):checked ~ .car-10__dots .car-10__dot:nth-child(2),
.car-10__radio:nth-of-type(3):checked ~ .car-10__dots .car-10__dot:nth-child(3) {
  background: var(--accent);
  transform: scale(1.3);
}

.car-10__radio:nth-of-type(1):focus-visible ~ .car-10__dots .car-10__dot:nth-child(1),
.car-10__radio:nth-of-type(2):focus-visible ~ .car-10__dots .car-10__dot:nth-child(2),
.car-10__radio:nth-of-type(3):focus-visible ~ .car-10__dots .car-10__dot:nth-child(3) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 560px) {
  .car-10__stage {
    min-height: 0;
  }

  .car-10__slide {
    position: relative;
    grid-template-columns: 1fr;
    display: none;
  }

  .car-10__slide {
    inset: auto;
  }

  .car-10__radio:nth-of-type(1):checked ~ .car-10__stage .car-10__slide:nth-child(1),
    .car-10__radio:nth-of-type(2):checked ~ .car-10__stage .car-10__slide:nth-child(2),
    .car-10__radio:nth-of-type(3):checked ~ .car-10__stage .car-10__slide:nth-child(3) {
    display: grid;
  }

  .car-10__pic {
    aspect-ratio: 16/10;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-10__slide,
    .car-10__dot {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radio group cross-fades split-layout slides and paints the active dot. */
```
