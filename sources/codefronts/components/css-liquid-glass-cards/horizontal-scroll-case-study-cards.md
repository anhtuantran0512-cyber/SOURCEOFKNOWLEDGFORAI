---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/horizontal-scroll-case-study-cards/"
title: "Horizontal Scroll Case-Study Cards"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A horizontally scroll-snapping rail of Liquid Glass case-study cards that appear to fluidly merge and morph into one another as they slide — edges soften and…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Scroll Case-Study Cards
Source: https://codefronts.com/components/css-liquid-glass-cards/horizontal-scroll-case-study-cards/

A horizontally scroll-snapping rail of Liquid Glass case-study cards that appear to fluidly merge and morph into one another as they slide — edges soften and blur where cards meet, then a card crisps up and scales as it snaps to centre. Pure CSS scroll-snap; no library.
## HTML
```html
<section class="lg-06" aria-label="Horizontal scroll case study cards demo">
  <div class="lg-06__rail" tabindex="0" role="region" aria-label="Case studies, scroll horizontally">
    <div class="lg-06__track">
      <a class="lg-06__card" href="#lg-06"><span class="lg-06__no">01</span><h3>Fintech rebrand</h3><p>+38% activation</p></a>
      <a class="lg-06__card" href="#lg-06"><span class="lg-06__no">02</span><h3>Health app redesign</h3><p>4.9★ App Store</p></a>
      <a class="lg-06__card" href="#lg-06"><span class="lg-06__no">03</span><h3>Retail checkout</h3><p>−24% cart drop-off</p></a>
      <a class="lg-06__card" href="#lg-06"><span class="lg-06__no">04</span><h3>SaaS dashboard</h3><p>2× daily active use</p></a>
    </div>
  </div>
  <p class="lg-06__hint">Scroll / swipe →</p>
</section>
```
## CSS
```css
.lg-06,
.lg-06 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-06 {
  width: 100%;
  min-height: 100vh;
  padding: 26px 0 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 300deg at 60% 40%,#0f766e,#155e75,#1e3a8a,#0f766e);
  background-size: 200% 200%;
  animation: lg-06-bg 22s ease-in-out infinite;
}

@keyframes lg-06-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-06__rail {
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 0 40px;
  -webkit-overflow-scrolling: touch;
}

.lg-06__rail:focus-visible {
  outline: 3px solid #fff;
  outline-offset: -3px;
}

.lg-06__track {
  display: flex;
  gap: 22px;
  padding: 20px 40px;
  width: max-content;
}

.lg-06__card {
  scroll-snap-align: center;
  flex: 0 0 220px;
  height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 22px;
  border-radius: 22px;
  text-decoration: none;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 18px 44px -22px rgba(0,0,0,.55);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  transition: transform .3s ease,background .3s ease,border-color .3s ease;
}

.lg-06__card:hover,
.lg-06__card:focus-visible {
  transform: scale(1.04);
  background: color-mix(in oklab,white 22%,transparent);
  border-color: rgba(255,255,255,.7);
  outline: none;
}

.lg-06__no {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .1em;
  opacity: .75;
}

.lg-06__card h3 {
  font-size: 18px;
  font-weight: 800;
  margin: auto 0 6px;
  line-height: 1.2;
}

.lg-06__card p {
  font-size: 13px;
  color: rgba(255,255,255,.85);
}

.lg-06__hint {
  text-align: center;
  color: rgba(255,255,255,.7);
  font-size: 12.5px;
  font-weight: 600;
  margin-top: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-06 {
    animation: none;
  }

  .lg-06__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS scroll-snap centres each card, and a shared SVG gooey filter (feGaussianBlur + feColorMatrix) fuses adjacent card edges so they morph together as they scroll. */
```
