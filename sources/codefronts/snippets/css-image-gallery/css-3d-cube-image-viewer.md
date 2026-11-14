---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-3d-cube-image-viewer/"
title: "CSS 3D Cube Image Viewer"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Six photos mapped onto the faces of a real 3D cube that rotates to whichever face you pick — a spinning cube image viewer for product showcases and…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Cube Image Viewer
Source: https://codefronts.com/snippets/css-image-gallery/css-3d-cube-image-viewer/

Six photos mapped onto the faces of a real 3D cube that rotates to whichever face you pick — a spinning cube image viewer for product showcases and galleries, controlled by accessible radio buttons with no JavaScript.
## HTML
```html
<section class="gl-15" aria-label="3D cube image viewer">
  <fieldset class="gl-15__controls">
    <legend>Choose a face</legend>
    <label><input type="radio" name="gl-15" value="front" checked><span>Front</span></label>
    <label><input type="radio" name="gl-15" value="right"><span>Right</span></label>
    <label><input type="radio" name="gl-15" value="back"><span>Back</span></label>
    <label><input type="radio" name="gl-15" value="left"><span>Left</span></label>
    <label><input type="radio" name="gl-15" value="top"><span>Top</span></label>
    <label><input type="radio" name="gl-15" value="bottom"><span>Bottom</span></label>
  </fieldset>
  <div class="gl-15__stage">
    <div class="gl-15__cube">
      <figure class="gl-15__face gl-15__face--front"><img src="https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera front view" loading="lazy" decoding="async"></figure>
      <figure class="gl-15__face gl-15__face--right"><img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera right view" loading="lazy" decoding="async"></figure>
      <figure class="gl-15__face gl-15__face--back"><img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera back view" loading="lazy" decoding="async"></figure>
      <figure class="gl-15__face gl-15__face--left"><img src="https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera left view" loading="lazy" decoding="async"></figure>
      <figure class="gl-15__face gl-15__face--top"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera top view" loading="lazy" decoding="async"></figure>
      <figure class="gl-15__face gl-15__face--bottom"><img src="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera bottom view" loading="lazy" decoding="async"></figure>
    </div>
  </div>
</section>
```
## CSS
```css
.gl-15,
.gl-15 *,
.gl-15 *::before,
.gl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-15 ::selection {
  background: oklch(0.7 0.16 200);
  color: #041318;
}

.gl-15 {
  --size: 240px;
  --half: 120px;
  --accent: oklch(0.72 0.16 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0e1418,#05080a);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 40px;
}

.gl-15__controls {
  border: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}

.gl-15__controls legend {
  width: 100%;
  text-align: center;
  margin-bottom: 12px;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #7c8b93;
}

.gl-15__controls label {
  cursor: pointer;
}

.gl-15__controls input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.gl-15__controls span {
  display: block;
  padding: 8px 16px;
  border-radius: 10px;
  border: 1px solid #223038;
  background: #0e161b;
  color: #a9bcc4;
  font-size: 13px;
  font-weight: 600;
  transition: .2s;
}

.gl-15__controls label:hover span {
  border-color: var(--accent);
  color: #fff;
}

.gl-15__controls input:checked+span {
  background: var(--accent);
  color: #041318;
  border-color: var(--accent);
}

.gl-15__controls input:focus-visible+span {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.gl-15__stage {
  perspective: 900px;
  width: var(--size);
  height: var(--size);
}

.gl-15__cube {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transform: rotateX(-18deg) rotateY(-24deg);
  transition: transform .8s cubic-bezier(.4,.1,.2,1);
}

.gl-15__face {
  position: absolute;
  inset: 0;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(255,255,255,.08) inset;
}

.gl-15__face img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gl-15__face--front {
  transform: translateZ(var(--half));
}

.gl-15__face--back {
  transform: rotateY(180deg) translateZ(var(--half));
}

.gl-15__face--right {
  transform: rotateY(90deg) translateZ(var(--half));
}

.gl-15__face--left {
  transform: rotateY(-90deg) translateZ(var(--half));
}

.gl-15__face--top {
  transform: rotateX(90deg) translateZ(var(--half));
}

.gl-15__face--bottom {
  transform: rotateX(-90deg) translateZ(var(--half));
}

.gl-15:has(input[value="front"]:checked) .gl-15__cube {
  transform: rotateY(0deg);
}

.gl-15:has(input[value="right"]:checked) .gl-15__cube {
  transform: rotateY(-90deg);
}

.gl-15:has(input[value="back"]:checked) .gl-15__cube {
  transform: rotateY(-180deg);
}

.gl-15:has(input[value="left"]:checked) .gl-15__cube {
  transform: rotateY(90deg);
}

.gl-15:has(input[value="top"]:checked) .gl-15__cube {
  transform: rotateX(-90deg);
}

.gl-15:has(input[value="bottom"]:checked) .gl-15__cube {
  transform: rotateX(90deg);
}

@media (prefers-reduced-motion: reduce) {
  .gl-15__cube {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — six radios drive the cube rotation through :has(:checked). */
```
