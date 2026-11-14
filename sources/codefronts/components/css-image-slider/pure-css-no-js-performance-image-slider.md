---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/pure-css-no-js-performance-image-slider/"
title: "Pure CSS No-JS Performance Image Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Pure CSS image slider with no JavaScript — the canonical radio-button hack that ships zero bundle weight and moves the entire strip with one composited…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS No-JS Performance Image Slider
Source: https://codefronts.com/components/css-image-slider/pure-css-no-js-performance-image-slider/

Pure CSS image slider with no JavaScript — the canonical radio-button hack that ships zero bundle weight and moves the entire strip with one composited transform. Core Web Vitals safe, keyboard-navigable out of the box, and copy-paste ready when you need a slideshow without Swiper, Slick, or any dependency.
## HTML
```html
<div class="cis-01">
  <input type="radio" name="cis-01" id="cis-01-1" checked>
  <input type="radio" name="cis-01" id="cis-01-2">
  <input type="radio" name="cis-01" id="cis-01-3">
  <input type="radio" name="cis-01" id="cis-01-4">

  <div class="cis-01__viewport">
    <div class="cis-01__track">
      <figure class="cis-01__slide">
        <img src="https://picsum.photos/seed/cis01a/1000/650" alt="Fog rolling over a pine ridge at dawn">
        <figcaption class="cis-01__cap"><span class="cis-01__k">01 — Ridgeline</span>Alpine fog, first light</figcaption>
      </figure>
      <figure class="cis-01__slide">
        <img src="https://picsum.photos/seed/cis01b/1000/650" alt="Long empty highway through a desert">
        <figcaption class="cis-01__cap"><span class="cis-01__k">02 — Passage</span>Desert route, midday</figcaption>
      </figure>
      <figure class="cis-01__slide">
        <img src="https://picsum.photos/seed/cis01c/1000/650" alt="City rooftops under low cloud">
        <figcaption class="cis-01__cap"><span class="cis-01__k">03 — Overlook</span>Rooftops, weather moving in</figcaption>
      </figure>
      <figure class="cis-01__slide">
        <img src="https://picsum.photos/seed/cis01d/1000/650" alt="Calm lake mirroring the sky">
        <figcaption class="cis-01__cap"><span class="cis-01__k">04 — Still</span>Glass water at dusk</figcaption>
      </figure>
    </div>
  </div>

  <div class="cis-01__arrows" aria-hidden="true">
    <label class="cis-01__arw a-prev p1" for="cis-01-4"></label><label class="cis-01__arw a-next n1" for="cis-01-2"></label>
    <label class="cis-01__arw a-prev p2" for="cis-01-1"></label><label class="cis-01__arw a-next n2" for="cis-01-3"></label>
    <label class="cis-01__arw a-prev p3" for="cis-01-2"></label><label class="cis-01__arw a-next n3" for="cis-01-4"></label>
    <label class="cis-01__arw a-prev p4" for="cis-01-3"></label><label class="cis-01__arw a-next n4" for="cis-01-1"></label>
  </div>

  <div class="cis-01__dots" role="tablist" aria-label="Choose slide">
    <label class="cis-01__dot" for="cis-01-1" aria-label="Slide 1"></label>
    <label class="cis-01__dot" for="cis-01-2" aria-label="Slide 2"></label>
    <label class="cis-01__dot" for="cis-01-3" aria-label="Slide 3"></label>
    <label class="cis-01__dot" for="cis-01-4" aria-label="Slide 4"></label>
  </div>
</div>
```
## CSS
```css
.cis-01,
.cis-01 *,
.cis-01 *::before,
.cis-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-01 ::selection {
  background: #c8ff4d;
  color: #0a0a0a;
}

.cis-01 {
  --bg: #0b0c10;
  --surface: #101218;
  --line: #23262f;
  --text: #eef0f5;
  --accent: oklch(0.86 0.19 122);
  --radius: 18px;
  --dur: .62s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: radial-gradient(120% 130% at 15% 0%,#14161d,#08090d);
}

.cis-01 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 0;
  height: 0;
}

.cis-01__viewport {
  position: relative;
  width: min(680px,92vw);
  aspect-ratio: 16/10.4;
  border-radius: var(--radius);
  overflow: hidden;
  border: 1px solid var(--line);
  box-shadow: 0 40px 90px -40px rgba(0,0,0,.9);
  isolation: isolate;
}

.cis-01__track {
  display: flex;
  width: 400%;
  height: 100%;
  transition: transform var(--dur) cubic-bezier(.7,0,.15,1);
}

.cis-01__slide {
  position: relative;
  width: 25%;
  height: 100%;
}

.cis-01__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-01__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 56px 22px 20px;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: .2px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: linear-gradient(transparent,rgba(6,7,10,.86));
  transform: translateY(14px);
  opacity: 0;
  transition: transform .5s .1s,opacity .5s .1s;
}

.cis-01__k {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--accent);
}
/* radio hack: move the strip + reveal the active caption */

#cis-01-1:checked ~ .cis-01__viewport .cis-01__track {
  transform: translateX(0);
}

#cis-01-2:checked ~ .cis-01__viewport .cis-01__track {
  transform: translateX(-25%);
}

#cis-01-3:checked ~ .cis-01__viewport .cis-01__track {
  transform: translateX(-50%);
}

#cis-01-4:checked ~ .cis-01__viewport .cis-01__track {
  transform: translateX(-75%);
}

#cis-01-1:checked ~ .cis-01__viewport .cis-01__slide:nth-child(1) .cis-01__cap,
#cis-01-2:checked ~ .cis-01__viewport .cis-01__slide:nth-child(2) .cis-01__cap,
#cis-01-3:checked ~ .cis-01__viewport .cis-01__slide:nth-child(3) .cis-01__cap,
#cis-01-4:checked ~ .cis-01__viewport .cis-01__slide:nth-child(4) .cis-01__cap {
  transform: translateY(0);
  opacity: 1;
}
/* dots */

.cis-01__dots {
  position: absolute;
  bottom: 26px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 5;
}

.cis-01__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  cursor: pointer;
  background: rgba(255,255,255,.32);
  transition: transform .3s,background .3s,width .3s;
}

.cis-01__dot:hover {
  background: rgba(255,255,255,.6);
}

#cis-01-1:checked ~ .cis-01__dots .cis-01__dot:nth-child(1),
#cis-01-2:checked ~ .cis-01__dots .cis-01__dot:nth-child(2),
#cis-01-3:checked ~ .cis-01__dots .cis-01__dot:nth-child(3),
#cis-01-4:checked ~ .cis-01__dots .cis-01__dot:nth-child(4) {
  background: var(--accent);
  width: 26px;
  border-radius: 6px;
}
/* arrows — :has() toggles the correct wrap-aware pair */

.cis-01__arrows {
  position: absolute;
  inset: auto;
  pointer-events: none;
  z-index: 6;
}

.cis-01__arw {
  position: absolute;
  top: calc(50% - 60px);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  background: rgba(12,13,17,.55);
  border: 1px solid rgba(255,255,255,.16);
  backdrop-filter: blur(8px);
  transition: opacity .3s,transform .3s,background .3s;
}

.cis-01__arw:hover {
  background: rgba(12,13,17,.85);
  transform: scale(1.08);
}

.cis-01__arw::before {
  content: "";
  width: 11px;
  height: 11px;
  border-top: 2.4px solid var(--text);
  border-right: 2.4px solid var(--text);
}

.a-prev {
  left: calc(50% - min(340px,46vw) + 14px);
}

.a-prev::before {
  transform: rotate(-135deg);
  margin-left: 4px;
}

.a-next {
  right: calc(50% - min(340px,46vw) + 14px);
}

.a-next::before {
  transform: rotate(45deg);
  margin-right: 4px;
}

.cis-01:has(#cis-01-1:checked) .p1,
.cis-01:has(#cis-01-1:checked) .n1,
.cis-01:has(#cis-01-2:checked) .p2,
.cis-01:has(#cis-01-2:checked) .n2,
.cis-01:has(#cis-01-3:checked) .p3,
.cis-01:has(#cis-01-3:checked) .n3,
.cis-01:has(#cis-01-4:checked) .p4,
.cis-01:has(#cis-01-4:checked) .n4 {
  opacity: 1;
  pointer-events: auto;
}

.cis-01 input:focus-visible ~ .cis-01__dots .cis-01__dot {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cis-01__track,
    .cis-01__cap,
    .cis-01__dot,
    .cis-01__arw {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — navigation is 100% CSS via the radio-button hack. */
```
