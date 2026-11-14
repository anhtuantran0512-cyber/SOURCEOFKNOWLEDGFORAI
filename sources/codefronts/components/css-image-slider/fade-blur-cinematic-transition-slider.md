---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/fade-blur-cinematic-transition-slider/"
title: "Fade & Blur Cinematic Transition Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Fade and blur cinematic transition slider — a slider that ditches the harsh horizontal slide for an elegant cross-fade where outgoing images blur out while…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fade & Blur Cinematic Transition Slider
Source: https://codefronts.com/components/css-image-slider/fade-blur-cinematic-transition-slider/

Fade and blur cinematic transition slider — a slider that ditches the harsh horizontal slide for an elegant cross-fade where outgoing images blur out while the incoming one sharpens into focus. Stacked absolute slides toggled by radios in pure CSS, no JavaScript. Ideal for photography portfolios, wedding galleries, and film-industry landing pages that want rack-focus transitions.
## HTML
```html
<div class="cis-15">
  <input type="radio" name="cis-15" id="cis-15-1" checked>
  <input type="radio" name="cis-15" id="cis-15-2">
  <input type="radio" name="cis-15" id="cis-15-3">
  <input type="radio" name="cis-15" id="cis-15-4">
  <div class="cis-15__stage">
    <figure class="cis-15__slide"><img src="https://picsum.photos/seed/cis15a/1100/700" alt="Scene one"><figcaption>Nightfall over the strait</figcaption></figure>
    <figure class="cis-15__slide"><img src="https://picsum.photos/seed/cis15b/1100/700" alt="Scene two"><figcaption>Rain on the avenue</figcaption></figure>
    <figure class="cis-15__slide"><img src="https://picsum.photos/seed/cis15c/1100/700" alt="Scene three"><figcaption>Last light, high desert</figcaption></figure>
    <figure class="cis-15__slide"><img src="https://picsum.photos/seed/cis15d/1100/700" alt="Scene four"><figcaption>Fog in the harbour</figcaption></figure>
  </div>
  <div class="cis-15__dots">
    <label for="cis-15-1" aria-label="Slide 1"></label>
    <label for="cis-15-2" aria-label="Slide 2"></label>
    <label for="cis-15-3" aria-label="Slide 3"></label>
    <label for="cis-15-4" aria-label="Slide 4"></label>
  </div>
</div>
```
## CSS
```css
.cis-15,
.cis-15 *,
.cis-15 *::before,
.cis-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-15 ::selection {
  background: oklch(0.85 0.13 80);
  color: #181200;
}

.cis-15 {
  --dur: 1s;
  --accent: oklch(0.85 0.12 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f4f1e9;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 18px;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 0%,#12100a,#070604);
}

.cis-15 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-15__stage {
  position: relative;
  width: min(720px,94vw);
  aspect-ratio: 11/7;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid #221e14;
  box-shadow: 0 40px 90px -46px #000;
}

.cis-15__slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: scale(1.06);
  filter: blur(16px) brightness(.8);
  transition: opacity var(--dur) ease,filter var(--dur) ease,transform var(--dur) ease;
}

.cis-15__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-15__slide figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 56px 22px 20px;
  font-size: 19px;
  font-weight: 600;
  background: linear-gradient(transparent,rgba(7,6,4,.85));
}

#cis-15-1:checked ~ .cis-15__stage .cis-15__slide:nth-child(1),
#cis-15-2:checked ~ .cis-15__stage .cis-15__slide:nth-child(2),
#cis-15-3:checked ~ .cis-15__stage .cis-15__slide:nth-child(3),
#cis-15-4:checked ~ .cis-15__stage .cis-15__slide:nth-child(4) {
  opacity: 1;
  filter: blur(0) brightness(1);
  transform: scale(1);
  animation: cis-15-kb 9s ease-out forwards;
}

@keyframes cis-15-kb {
  from {
    transform: scale(1);
  }

  to {
    transform: scale(1.06);
  }
}

.cis-15__dots {
  display: flex;
  gap: 10px;
}

.cis-15__dots label {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  cursor: pointer;
  background: rgba(255,255,255,.28);
  transition: background .3s,width .3s;
}

.cis-15__dots label:hover {
  background: rgba(255,255,255,.55);
}

#cis-15-1:checked ~ .cis-15__dots label[for="cis-15-1"],
#cis-15-2:checked ~ .cis-15__dots label[for="cis-15-2"],
#cis-15-3:checked ~ .cis-15__dots label[for="cis-15-3"],
#cis-15-4:checked ~ .cis-15__dots label[for="cis-15-4"] {
  background: var(--accent);
  width: 26px;
  border-radius: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .cis-15__slide {
    filter: brightness(.8);
    transition: opacity .4s;
  }

  #cis-15-1:checked ~ .cis-15__stage .cis-15__slide:nth-child(1),
    #cis-15-2:checked ~ .cis-15__stage .cis-15__slide:nth-child(2),
    #cis-15-3:checked ~ .cis-15__stage .cis-15__slide:nth-child(3),
    #cis-15-4:checked ~ .cis-15__stage .cis-15__slide:nth-child(4) {
    filter: brightness(1);
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — opacity + blur cross-fade between stacked slides. */
```
