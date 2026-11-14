---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/meet-the-team-slider/"
title: "Meet the Team Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A gently gliding rail of circular staff portraits with names and roles — the 'meet the team' / 'our people' section on about pages."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Meet the Team Slider
Source: https://codefronts.com/snippets/css-image-carousel/meet-the-team-slider/

A gently gliding rail of circular staff portraits with names and roles — the 'meet the team' / 'our people' section on about pages. Scroll-snap keeps each face centred, and the active card scales up for focus.
## HTML
```html
<section class="car-07" aria-label="Meet the team">
  <ul class="car-07__rail" tabindex="0" role="group" aria-label="Team members, scrollable">
    <li class="car-07__card"><img class="car-07__ph" src="https://picsum.photos/seed/team-1/300/300" width="300" height="300" alt="Portrait of Dana Osei"><h4 class="car-07__name">Dana Osei</h4><p class="car-07__role">Head of Design</p></li>
    <li class="car-07__card"><img class="car-07__ph" src="https://picsum.photos/seed/team-2/300/300" width="300" height="300" alt="Portrait of Ravi Menon"><h4 class="car-07__name">Ravi Menon</h4><p class="car-07__role">Principal Engineer</p></li>
    <li class="car-07__card"><img class="car-07__ph" src="https://picsum.photos/seed/team-3/300/300" width="300" height="300" alt="Portrait of Elin Broer"><h4 class="car-07__name">Elin Broer</h4><p class="car-07__role">Product Manager</p></li>
    <li class="car-07__card"><img class="car-07__ph" src="https://picsum.photos/seed/team-4/300/300" width="300" height="300" alt="Portrait of Tomas Vega"><h4 class="car-07__name">Tomas Vega</h4><p class="car-07__role">UX Researcher</p></li>
    <li class="car-07__card"><img class="car-07__ph" src="https://picsum.photos/seed/team-5/300/300" width="300" height="300" alt="Portrait of Yuki Sato"><h4 class="car-07__name">Yuki Sato</h4><p class="car-07__role">Design Engineer</p></li>
  </ul>
</section>
```
## CSS
```css
.car-07,
.car-07 *,
.car-07 *::before,
.car-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-07 ::selection {
  background: oklch(0.6 0.13 200);
  color: #fff;
}

.car-07 {
  --accent: oklch(0.6 0.13 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 12px;
  background: #eef4f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-07__rail {
  list-style: none;
  display: flex;
  gap: 20px;
  width: min(720px,100%);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 16px;
  padding: 16px 16px 24px;
  scrollbar-width: thin;
  scrollbar-color: #c4dada transparent;
}

.car-07__rail:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 16px;
}

.car-07__card {
  flex: 0 0 150px;
  scroll-snap-align: center;
  text-align: center;
  transition: transform .3s cubic-bezier(.2,.8,.2,1);
}

.car-07__card:hover,
.car-07__card:focus-within {
  transform: scale(1.06);
}

.car-07__ph {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #fff;
  box-shadow: 0 14px 30px -18px rgba(20,60,60,.7);
  transition: box-shadow .3s;
  background: #d7e6e6;
}

.car-07__card:hover .car-07__ph {
  box-shadow: 0 18px 34px -14px rgba(20,60,60,.6),0 0 0 4px var(--accent);
}

.car-07__name {
  margin: 16px 0 2px;
  font-size: 15px;
  font-weight: 700;
  color: #1c3535;
}

.car-07__role {
  font-size: 12.5px;
  color: #5c7676;
}

@media (prefers-reduced-motion: reduce) {
  .car-07__card,
    .car-07__ph {
    transition: none;
  }

  .car-07__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — a centred scroll-snap rail; active portraits scale via transform only. */
```
