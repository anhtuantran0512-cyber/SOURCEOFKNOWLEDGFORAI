---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/lightbox-image-gallery/"
title: "Lightbox Image Gallery"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A pure-CSS image viewer that scales a thumbnail to full-screen with prev / next navigation and a dimmed backdrop — the zero-JavaScript lightbox, driven…"
has_js: "false"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Lightbox Image Gallery
Source: https://codefronts.com/components/css-modals/lightbox-image-gallery/

A pure-CSS image viewer that scales a thumbnail to full-screen with prev / next navigation and a dimmed backdrop — the zero-JavaScript lightbox, driven entirely by the :target selector and anchor links.
## HTML
```html
<div class="cm-09" id="cm-09">
  <div class="cm-09__grid">
    <a href="#cm-09-1" class="cm-09__thumb" data-n="01" aria-label="Open image 1"></a>
    <a href="#cm-09-2" class="cm-09__thumb" data-n="02" aria-label="Open image 2"></a>
    <a href="#cm-09-3" class="cm-09__thumb" data-n="03" aria-label="Open image 3"></a>
    <a href="#cm-09-4" class="cm-09__thumb" data-n="04" aria-label="Open image 4"></a>
    <a href="#cm-09-5" class="cm-09__thumb" data-n="05" aria-label="Open image 5"></a>
    <a href="#cm-09-6" class="cm-09__thumb" data-n="06" aria-label="Open image 6"></a>
  </div>

  <div id="cm-09-1" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 1 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-6" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 01"><figcaption>Frame 01 — desert highway</figcaption></figure>
    <a href="#cm-09-2" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
  <div id="cm-09-2" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 2 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-1" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 02"><figcaption>Frame 02 — neon alley</figcaption></figure>
    <a href="#cm-09-3" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
  <div id="cm-09-3" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 3 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-2" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 03"><figcaption>Frame 03 — coastal fog</figcaption></figure>
    <a href="#cm-09-4" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
  <div id="cm-09-4" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 4 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-3" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 04"><figcaption>Frame 04 — pine ridge</figcaption></figure>
    <a href="#cm-09-5" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
  <div id="cm-09-5" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 5 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-4" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 05"><figcaption>Frame 05 — salt flats</figcaption></figure>
    <a href="#cm-09-6" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
  <div id="cm-09-6" class="cm-09__lb" role="dialog" aria-modal="true" aria-label="Image 6 of 6">
    <a href="#cm-09" class="cm-09__scrim" aria-label="Close"></a>
    <a href="#cm-09-5" class="cm-09__nav cm-09__prev" aria-label="Previous image">&#8249;</a>
    <figure class="cm-09__fig" data-label="image 06"><figcaption>Frame 06 — city dusk</figcaption></figure>
    <a href="#cm-09-1" class="cm-09__nav cm-09__next" aria-label="Next image">&#8250;</a>
    <a href="#cm-09" class="cm-09__close" aria-label="Close">&times;</a>
  </div>
</div>
```
## CSS
```css
.cm-09,
.cm-09 *,
.cm-09 *::before,
.cm-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-09 {
  --accent: oklch(0.8 0.14 200);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0b0d12,#060709);
}

.cm-09__grid {
  display: grid;
  grid-template-columns: repeat(3,120px);
  gap: 14px;
}

.cm-09__thumb {
  position: relative;
  aspect-ratio: 1;
  border-radius: 12px;
  overflow: hidden;
  text-decoration: none;
  background: repeating-linear-gradient(135deg,#1a1f2a 0 12px,#151a24 12px 24px);
  border: 1px solid #283040;
  transition: transform .2s,border-color .2s,box-shadow .2s;
}

.cm-09__thumb::after {
  content: attr(data-n);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: 600 15px ui-monospace,monospace;
  color: #5a6478;
}

.cm-09__thumb:hover {
  transform: translateY(-3px);
  border-color: var(--accent);
  box-shadow: 0 12px 30px -14px var(--accent);
}

.cm-09__thumb:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cm-09__lb {
  position: fixed;
  inset: 0;
  z-index: 20;
  display: grid;
  place-items: center;
  padding: 60px 24px;
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s,visibility .3s;
}

.cm-09__lb:target {
  opacity: 1;
  visibility: visible;
}

.cm-09__scrim {
  position: absolute;
  inset: 0;
  background: rgba(4,6,9,.82);
  backdrop-filter: blur(6px);
}

.cm-09__fig {
  position: relative;
  width: min(620px,90vw);
  aspect-ratio: 3/2;
  border-radius: 16px;
  overflow: hidden;
  background: repeating-linear-gradient(135deg,#1c2230 0 18px,#161b27 18px 36px);
  border: 1px solid #303a4c;
  transform: scale(.9);
  transition: transform .3s;
  display: grid;
  place-items: center;
}

.cm-09__lb:target .cm-09__fig {
  transform: scale(1);
}

.cm-09__fig::before {
  content: attr(data-label);
  font: 12px ui-monospace,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #586274;
}

.cm-09__fig figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 14px 18px;
  font-size: 13px;
  color: #cdd5e2;
  background: linear-gradient(transparent,rgba(6,8,12,.85));
}

.cm-09__nav,
.cm-09__close {
  position: absolute;
  z-index: 2;
  display: grid;
  place-items: center;
  text-decoration: none;
  color: #e8edf5;
  background: rgba(20,26,36,.7);
  border: 1px solid #333d50;
  transition: background .2s,transform .1s;
}

.cm-09__nav {
  top: 50%;
  transform: translateY(-50%);
  width: 52px;
  height: 52px;
  border-radius: 50%;
  font-size: 28px;
}

.cm-09__prev {
  left: 18px;
}

.cm-09__next {
  right: 18px;
}

.cm-09__nav:hover {
  background: color-mix(in oklch,var(--accent) 30%,#141a24);
}

.cm-09__close {
  top: 18px;
  right: 18px;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  font-size: 24px;
}

.cm-09__close:hover {
  background: color-mix(in oklch,var(--accent) 30%,#141a24);
}

.cm-09__nav:focus-visible,
.cm-09__close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-09__lb,
    .cm-09__fig {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
/* No JavaScript — :target opens each panel; prev/next/close are plain anchor links. */
```
