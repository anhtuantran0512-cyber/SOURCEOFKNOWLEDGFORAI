---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/native-scroll-marker-scroll-button-slider/"
title: "Native ::scroll-marker & ::scroll-button Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Native ::scroll-marker and ::scroll-button CSS Carousel slider — cutting-edge zero-JS carousel built on the emerging CSS Carousel spec where the browser…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Native ::scroll-marker & ::scroll-button Slider
Source: https://codefronts.com/components/css-image-slider/native-scroll-marker-scroll-button-slider/

Native ::scroll-marker and ::scroll-button CSS Carousel slider — cutting-edge zero-JS carousel built on the emerging CSS Carousel spec where the browser generates pagination dots via ::scroll-marker and prev/next arrows via ::scroll-button(). Real focusable controls straight from the stylesheet, native screen-reader announcements, and a natural @supports fallback to scroll-snap. The pattern that replaces Swiper (145KB), Slick (85KB), and Splide (60KB) once support hits ~80%.
## HTML
```html
<div class="cis-19">
  <div class="cis-19__rail" tabindex="0" aria-label="Native CSS carousel">
    <figure class="cis-19__slide"><img src="https://picsum.photos/seed/cis19a/900/600" alt="Slide one"></figure>
    <figure class="cis-19__slide"><img src="https://picsum.photos/seed/cis19b/900/600" alt="Slide two"></figure>
    <figure class="cis-19__slide"><img src="https://picsum.photos/seed/cis19c/900/600" alt="Slide three"></figure>
    <figure class="cis-19__slide"><img src="https://picsum.photos/seed/cis19d/900/600" alt="Slide four"></figure>
    <figure class="cis-19__slide"><img src="https://picsum.photos/seed/cis19e/900/600" alt="Slide five"></figure>
  </div>
  <p class="cis-19__note">Dots &amp; arrows are generated natively by CSS — no markup, no JS.</p>
</div>
```
## CSS
```css
.cis-19,
.cis-19 *,
.cis-19 *::before,
.cis-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-19 ::selection {
  background: oklch(0.85 0.16 140);
  color: #04140a;
}

.cis-19 {
  --accent: oklch(0.82 0.15 145);
  --surface: #101611;
  --line: #213026;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eaf2ec;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 44px 20px;
  background: radial-gradient(120% 110% at 50% 0%,#0f1712,#080b09);
}

.cis-19__rail {
  position: relative;
  display: flex;
  gap: 16px;
  width: min(720px,94vw);
  padding: 6px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
}

.cis-19__rail::-webkit-scrollbar {
  display: none;
}

.cis-19__rail:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 5px;
  border-radius: 20px;
}

.cis-19__slide {
  flex: 0 0 100%;
  scroll-snap-align: center;
  aspect-ratio: 3/2;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--line);
}

.cis-19__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-19__note {
  font-size: 12px;
  color: #6a7d70;
  text-align: center;
  max-width: 40ch;
}

@supports (scroll-marker-group: after) {
  .cis-19__rail {
    scroll-marker-group: after;
    padding-bottom: 26px;
  }

  .cis-19__rail::scroll-marker-group {
    display: flex;
    gap: 9px;
    justify-content: center;
    margin-top: 16px;
  }

  .cis-19__slide::scroll-marker {
    content: "";
    width: 9px;
    height: 9px;
    border-radius: 50%;
    border: 0;
    background: rgba(255,255,255,.28);
    cursor: pointer;
    transition: background .25s,width .25s;
  }

  .cis-19__slide::scroll-marker:hover {
    background: rgba(255,255,255,.55);
  }

  .cis-19__slide::scroll-marker:target-current {
    background: var(--accent);
    width: 24px;
    border-radius: 5px;
  }
}

@supports (overflow: auto) and (selector(::scroll-button(*))) {
  .cis-19__rail::scroll-button(inline-start),
    .cis-19__rail::scroll-button(inline-end) {
    position: absolute;
    top: calc(50% - 22px);
    z-index: 4;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.16);
    background: rgba(10,14,11,.7);
    color: #fff;
    font-size: 18px;
    cursor: pointer;
    backdrop-filter: blur(8px);
    transition: background .25s,opacity .25s;
  }

  .cis-19__rail::scroll-button(inline-start) {
    content: "‹";
    left: 12px;
  }

  .cis-19__rail::scroll-button(inline-end) {
    content: "›";
    right: 12px;
  }

  .cis-19__rail::scroll-button(*):hover {
    background: rgba(10,14,11,.95);
  }

  .cis-19__rail::scroll-button(*):disabled {
    opacity: .3;
    cursor: default;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-19__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — ::scroll-marker generates dots and ::scroll-button() generates arrows. */
```
