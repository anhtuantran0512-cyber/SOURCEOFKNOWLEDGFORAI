---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/parallax-layered-depth-slider/"
title: "Parallax Layered Depth Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Parallax layered depth image slider in pure CSS — the background photo cross-fades with a Ken-Burns settle while the foreground headline slides horizontally…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Layered Depth Slider
Source: https://codefronts.com/components/css-image-slider/parallax-layered-depth-slider/

Parallax layered depth image slider in pure CSS — the background photo cross-fades with a Ken-Burns settle while the foreground headline slides horizontally at slide speed, producing real depth without ever exposing the edge of a neighboring image. No JavaScript, no rellax.js or Locomotive Scroll dependency, no scroll-listener overhead. Perfect for cinematic editorial heroes and storytelling landing pages.
## HTML
```html
<div class="cis-14">
  <input type="radio" name="cis-14" id="cis-14-1" checked>
  <input type="radio" name="cis-14" id="cis-14-2">
  <input type="radio" name="cis-14" id="cis-14-3">
  <div class="cis-14__stage">
    <div class="cis-14__bg">
      <img class="cis-14__img" data-i="1" src="https://picsum.photos/seed/cis14a/1600/1000" alt="Northern Reach — moody courtyard">
      <img class="cis-14__img" data-i="2" src="https://picsum.photos/seed/cis14b/1600/1000" alt="The Long Valley — Icelandic horses">
      <img class="cis-14__img" data-i="3" src="https://picsum.photos/seed/cis14c/1600/1000" alt="Above the Snowline — boardwalk">
    </div>
    <div class="cis-14__fg">
      <div class="cis-14__cap" data-i="1"><span>Chapter I</span><h2>Northern Reach</h2></div>
      <div class="cis-14__cap" data-i="2"><span>Chapter II</span><h2>The Long Valley</h2></div>
      <div class="cis-14__cap" data-i="3"><span>Chapter III</span><h2>Above the Snowline</h2></div>
    </div>
    <div class="cis-14__nav">
      <label for="cis-14-1" aria-label="Slide 1"></label>
      <label for="cis-14-2" aria-label="Slide 2"></label>
      <label for="cis-14-3" aria-label="Slide 3"></label>
    </div>
  </div>
</div>
```
## CSS
```css
.cis-14,
.cis-14 *,
.cis-14 *::before,
.cis-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-14 ::selection {
  background: oklch(0.86 0.13 200);
  color: #04141a;
}

.cis-14 {
  --accent: oklch(0.85 0.12 200);
  --dur: .9s;
  --ease: cubic-bezier(.7,0,.15,1);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f2f6f8;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: #05080a;
}

.cis-14 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-14__stage {
  position: relative;
  width: min(760px,96vw);
  aspect-ratio: 16/10;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid #1a2226;
  box-shadow: 0 40px 90px -46px #000;
}
/* Stacked bg images cross-fade — never a horizontal strip, so neighbor
   images can NEVER bleed into the active slide edge. */

.cis-14__bg {
  position: absolute;
  inset: 0;
}

.cis-14__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(.7);
  opacity: 0;
  transform: scale(1.14) translateX(4%);
  transition: opacity var(--dur) var(--ease),transform calc(var(--dur) * 1.4) var(--ease);
}
/* Foreground caption strip still slides horizontally so headline feels the parallax:
   fg travels FASTER than the bg fade (which is stationary within the frame). */

.cis-14__fg {
  position: absolute;
  inset: 0;
  display: flex;
  width: 300%;
  z-index: 2;
  transition: transform var(--dur) var(--ease);
  will-change: transform;
}

.cis-14__cap {
  width: 33.333%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 8px;
  padding: clamp(24px,5vw,60px);
}

.cis-14__cap span {
  font: 700 12px ui-monospace,Menlo,monospace;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--accent);
}

.cis-14__cap h2 {
  font-size: clamp(30px,5vw,58px);
  line-height: 1;
  font-weight: 800;
  letter-spacing: -.02em;
}
/* Active bg: fade in and settle to zero translate — the "camera pushing back"
   parallax read comes from the settling transform, not from strip translation. */

#cis-14-1:checked ~ .cis-14__stage .cis-14__img[data-i="1"],
#cis-14-2:checked ~ .cis-14__stage .cis-14__img[data-i="2"],
#cis-14-3:checked ~ .cis-14__stage .cis-14__img[data-i="3"] {
  opacity: 1;
  transform: scale(1.14) translateX(0);
}

#cis-14-1:checked ~ .cis-14__stage .cis-14__fg {
  transform: translateX(0);
}

#cis-14-2:checked ~ .cis-14__stage .cis-14__fg {
  transform: translateX(-33.333%);
}

#cis-14-3:checked ~ .cis-14__stage .cis-14__fg {
  transform: translateX(-66.666%);
}

.cis-14__nav {
  position: absolute;
  left: 50%;
  bottom: 20px;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 3;
}

.cis-14__nav label {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  cursor: pointer;
  background: rgba(255,255,255,.3);
  transition: background .3s,width .3s;
}

.cis-14__nav label:hover {
  background: rgba(255,255,255,.6);
}

#cis-14-1:checked ~ .cis-14__stage .cis-14__nav label[for="cis-14-1"],
#cis-14-2:checked ~ .cis-14__stage .cis-14__nav label[for="cis-14-2"],
#cis-14-3:checked ~ .cis-14__stage .cis-14__nav label[for="cis-14-3"] {
  background: var(--accent);
  width: 26px;
  border-radius: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .cis-14__img,
    .cis-14__fg {
    transition: none;
  }

  .cis-14__img {
    transform: none;
  }

  #cis-14-1:checked ~ .cis-14__stage .cis-14__img[data-i="1"],
    #cis-14-2:checked ~ .cis-14__stage .cis-14__img[data-i="2"],
    #cis-14-3:checked ~ .cis-14__stage .cis-14__img[data-i="3"] {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — layers translate by different amounts from one :checked state. */
```
