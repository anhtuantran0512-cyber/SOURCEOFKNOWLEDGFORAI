---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/split-screen-vertical-carousel/"
title: "Split-Screen Vertical Carousel"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Split-screen vertical carousel — agency-style hero where the text half slides up while the image half slides down in the opposite direction as you switch…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Screen Vertical Carousel
Source: https://codefronts.com/components/css-image-slider/split-screen-vertical-carousel/

Split-screen vertical carousel — agency-style hero where the text half slides up while the image half slides down in the opposite direction as you switch slides. Two synced vertical tracks driven entirely by the radio-button hack. Pattern used on Vercel, Linear, and Superhuman product marketing pages; ships without Framer Motion or GSAP scroll listeners.
## HTML
```html
<div class="cis-08">
  <input type="radio" name="cis-08" id="cis-08-1" checked>
  <input type="radio" name="cis-08" id="cis-08-2">
  <input type="radio" name="cis-08" id="cis-08-3">
  <div class="cis-08__grid">
    <div class="cis-08__col">
      <div class="cis-08__ttrack">
        <div class="cis-08__tp"><span class="cis-08__k">Nº 01</span><h2>Build in the open.</h2><p>Ship weekly, learn faster, keep nothing precious.</p></div>
        <div class="cis-08__tp"><span class="cis-08__k">Nº 02</span><h2>Design with rhythm.</h2><p>Type, space and motion tuned to a single scale.</p></div>
        <div class="cis-08__tp"><span class="cis-08__k">Nº 03</span><h2>Measure what matters.</h2><p>Signal over vanity. Fewer numbers, better ones.</p></div>
      </div>
    </div>
    <div class="cis-08__col cis-08__col--img">
      <div class="cis-08__itrack">
        <div class="cis-08__ip"><img src="https://picsum.photos/seed/cis08c/900/1200" alt="Slide 3 visual"></div>
        <div class="cis-08__ip"><img src="https://picsum.photos/seed/cis08b/900/1200" alt="Slide 2 visual"></div>
        <div class="cis-08__ip"><img src="https://picsum.photos/seed/cis08a/900/1200" alt="Slide 1 visual"></div>
      </div>
    </div>
  </div>
  <div class="cis-08__nav">
    <label for="cis-08-1"><span>01</span></label>
    <label for="cis-08-2"><span>02</span></label>
    <label for="cis-08-3"><span>03</span></label>
  </div>
</div>
```
## CSS
```css
.cis-08,
.cis-08 *,
.cis-08 *::before,
.cis-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-08 ::selection {
  background: oklch(0.85 0.16 320);
  color: #160418;
}

.cis-08 {
  --accent: oklch(0.8 0.15 330);
  --dur: .75s;
  --text: #f3eef6;
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(150deg,#140a18,#0c0710);
}

.cis-08 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-08__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 100vh;
}

.cis-08__col {
  overflow: hidden;
  position: relative;
}

.cis-08__ttrack,
.cis-08__itrack {
  height: 300%;
  transition: transform var(--dur) cubic-bezier(.7,0,.15,1);
}

.cis-08__tp {
  height: calc(100vh);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
  padding: clamp(28px,6vw,90px);
}

.cis-08__k {
  font: 700 12px ui-monospace,Menlo,monospace;
  letter-spacing: .3em;
  color: var(--accent);
}

.cis-08__tp h2 {
  font-size: clamp(30px,4.6vw,56px);
  line-height: 1;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cis-08__tp p {
  font-size: 16px;
  line-height: 1.5;
  color: #c9bcd2;
  max-width: 34ch;
}

.cis-08__ip {
  height: 100vh;
}

.cis-08__ip img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(.82);
}
/* counter-motion: text up, image down */

#cis-08-1:checked ~ .cis-08__grid .cis-08__ttrack {
  transform: translateY(0);
}

#cis-08-2:checked ~ .cis-08__grid .cis-08__ttrack {
  transform: translateY(-33.333%);
}

#cis-08-3:checked ~ .cis-08__grid .cis-08__ttrack {
  transform: translateY(-66.666%);
}

#cis-08-1:checked ~ .cis-08__grid .cis-08__itrack {
  transform: translateY(-66.666%);
}

#cis-08-2:checked ~ .cis-08__grid .cis-08__itrack {
  transform: translateY(-33.333%);
}

#cis-08-3:checked ~ .cis-08__grid .cis-08__itrack {
  transform: translateY(0);
}

.cis-08__nav {
  position: absolute;
  left: 50%;
  bottom: 30px;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 5;
}

.cis-08__nav label {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  cursor: pointer;
  font: 700 12px ui-monospace,Menlo,monospace;
  color: #c9bcd2;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.14);
  transition: all .3s;
}

.cis-08__nav label:hover {
  background: rgba(255,255,255,.14);
}

#cis-08-1:checked ~ .cis-08__nav label[for="cis-08-1"],
#cis-08-2:checked ~ .cis-08__nav label[for="cis-08-2"],
#cis-08-3:checked ~ .cis-08__nav label[for="cis-08-3"] {
  background: var(--accent);
  color: #160418;
  border-color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .cis-08__ttrack,
    .cis-08__itrack {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two counter-moving vertical tracks driven by the radio hack. */
```
