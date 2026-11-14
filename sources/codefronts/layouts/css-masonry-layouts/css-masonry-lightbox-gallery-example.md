---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-lightbox-gallery-example/"
title: "CSS Masonry Lightbox Gallery Example"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "A photographer's masonry wall where every tile opens a true modal — built on the native <dialog> element, so the focus trap, Esc-to-close, focus restore and…"
has_js: "true"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Lightbox Gallery Example
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-lightbox-gallery-example/

A photographer's masonry wall where every tile opens a true modal — built on the native <dialog> element, so the focus trap, Esc-to-close, focus restore and top-layer stacking are free browser features, not 400 lines of library code. Eighteen lines of JavaScript only ferry the clicked image into the dialog; the entrance animation is pure CSS via @starting-style, and the blurred, dimmed backdrop is one ::backdrop rule.
## HTML
```html
<section class="msn-02" aria-label="CSS masonry lightbox gallery demo">
  <div class="msn-02__stage" tabindex="0">
    <header class="msn-02__head">
      <div><h2>Field Notes</h2><p>Structures &amp; light — click any frame</p></div>
      <span class="msn-02__hint">Esc closes · Tab stays inside</span>
    </header>
    <div class="msn-02__wall">
      <button class="msn-02__tile" type="button" data-cap="Museum atrium, noon — Oslo" style="--ar:4/5;--img:url('https://images.unsplash.com/photo-1487958449943-2429e8be8625?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.82 0.05 240);--b:oklch(0.55 0.08 260)"><figure></figure><span>Atrium, noon</span></button>
      <button class="msn-02__tile" type="button" data-cap="Stairwell helix — Copenhagen" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1511818966892-d7d671e672a2?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.75 0.06 60);--b:oklch(0.5 0.08 40)"><figure></figure><span>Stairwell helix</span></button>
      <button class="msn-02__tile" type="button" data-cap="Curtain wall grid at dusk" style="--ar:16/10;--img:url('https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.6 0.07 250);--b:oklch(0.35 0.08 270)"><figure></figure><span>Curtain wall</span></button>
      <button class="msn-02__tile" type="button" data-cap="Poured concrete, morning fog" style="--ar:2/3;--img:url('https://images.unsplash.com/photo-1486718448742-163732cd1544?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.78 0.02 80);--b:oklch(0.55 0.03 60)"><figure></figure><span>Poured concrete</span></button>
      <button class="msn-02__tile" type="button" data-cap="The 50mm that started it" style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.7 0.05 30);--b:oklch(0.45 0.06 20)"><figure></figure><span>The 50mm</span></button>
      <button class="msn-02__tile" type="button" data-cap="Studio bench, end of day" style="--ar:4/3;--img:url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.5 0.04 280);--b:oklch(0.3 0.05 300)"><figure></figure><span>Studio bench</span></button>
      <button class="msn-02__tile" type="button" data-cap="Scouting the ridge line" style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1493863641943-9b68992a8d07?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.72 0.06 220);--b:oklch(0.48 0.07 240)"><figure></figure><span>Scouting</span></button>
      <button class="msn-02__tile" type="button" data-cap="Contact sheet, roll 14" style="--ar:16/9;--img:url('https://images.unsplash.com/photo-1502920917128-1aa500764cbd?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.65 0.05 200);--b:oklch(0.4 0.06 220)"><figure></figure><span>Roll 14</span></button>
      <button class="msn-02__tile" type="button" data-cap="North face, last light" style="--ar:2/3;--img:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1000&auto=format&fit=crop');--a:oklch(0.68 0.08 260);--b:oklch(0.42 0.1 280)"><figure></figure><span>North face</span></button>
    </div>
    <dialog class="msn-02__lb" aria-label="Photo viewer">
      <figure></figure>
      <div class="msn-02__lbBar"><p class="msn-02__lbCap"></p><button class="msn-02__lbClose" type="button">Close</button></div>
    </dialog>
  </div>
</section>
```
## CSS
```css
.msn-02,
.msn-02 *,
.msn-02 *::before,
.msn-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-02 {
  --bg: oklch(0.21 0.012 260);
  --ink: oklch(0.95 0.005 260);
  --mut: oklch(0.68 0.01 260);
  --line: oklch(0.32 0.012 260);
  --acc: oklch(0.8 0.12 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-02__stage {
  width: 100%;
  container: msn02/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-02__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 14px;
  padding: 18px clamp(16px,3cqi,30px);
  background: color-mix(in oklch,var(--bg) 82%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-02__head h2 {
  font-size: clamp(18px,2.6cqi,24px);
  letter-spacing: -.02em;
}

.msn-02__head p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-02__hint {
  font-size: 11.5px;
  color: var(--mut);
  border: 1px solid var(--line);
  border-radius: 99px;
  padding: 6px 12px;
  white-space: nowrap;
}

.msn-02__wall {
  columns: 240px;
  column-gap: 12px;
  padding: clamp(16px,3cqi,30px);
}

.msn-02__tile {
  display: block;
  width: 100%;
  break-inside: avoid;
  margin-bottom: 12px;
  position: relative;
  border: 0;
  padding: 0;
  background: none;
  cursor: zoom-in;
  border-radius: 10px;
  color: inherit;
  font: inherit;
}

.msn-02__tile figure {
  aspect-ratio: var(--ar,3/4);
  border-radius: 10px;
  overflow: clip;
  background: linear-gradient(150deg,var(--a),var(--b));
  position: relative;
}

.msn-02__tile figure::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none);
  background-size: cover;
  background-position: center;
  transition: scale .4s cubic-bezier(.2,.7,.2,1),opacity .3s;
}

.msn-02__tile:hover figure::before,
.msn-02__tile:focus-visible figure::before {
  scale: 1.04;
  opacity: .92;
}

.msn-02__tile>span {
  position: absolute;
  left: 10px;
  bottom: 10px;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .02em;
  color: oklch(0.98 0 0);
  background: oklch(0.15 0.01 260/.62);
  backdrop-filter: blur(4px);
  padding: 5px 10px;
  border-radius: 99px;
  opacity: 0;
  translate: 0 5px;
  transition: opacity .25s,translate .25s;
}

.msn-02__tile:hover>span,
.msn-02__tile:focus-visible>span {
  opacity: 1;
  translate: 0 0;
}

.msn-02__tile:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.msn-02__lb {
  margin: auto;
  border: 0;
  padding: 10px;
  border-radius: 16px;
  background: oklch(0.24 0.012 260);
  color: var(--ink);
  width: min(880px,94vw);
  opacity: 1;
  scale: 1;
  transition: opacity .32s cubic-bezier(.2,.7,.2,1),scale .32s cubic-bezier(.2,.7,.2,1);
}

.msn-02__lb[open] {
  opacity: 1;
  scale: 1;
}

@starting-style {
  .msn-02__lb[open] {
    opacity: 0;
    scale: .94;
  }
}

.msn-02__lb::backdrop {
  background: oklch(0.13 0.01 260/.78);
  backdrop-filter: blur(8px);
}

.msn-02__lb figure {
  aspect-ratio: var(--ar,3/2);
  max-height: 72vh;
  margin: auto;
  border-radius: 10px;
  background-image: var(--img,none),linear-gradient(150deg,var(--a,oklch(0.4 0.02 260)),var(--b,oklch(0.25 0.02 260)));
  background-size: cover;
  background-position: center;
}

.msn-02__lbBar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 12px 6px 4px;
}

.msn-02__lbCap {
  font-size: 13.5px;
  color: var(--mut);
}

.msn-02__lbClose {
  min-height: 40px;
  padding: 0 18px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: none;
  color: var(--ink);
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.msn-02__lbClose:hover,
.msn-02__lbClose:focus-visible {
  background: oklch(0.3 0.014 260);
  border-color: oklch(0.45 0.015 260);
}

.msn-02__lbClose:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@container msn02 (width < 480px) {
  .msn-02__wall {
    columns: 2;
    column-gap: 8px;
  }

  .msn-02__tile {
    margin-bottom: 8px;
  }

  .msn-02__hint {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-02 *,
    .msn-02 *::before {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.msn-02').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var lb = root.querySelector('.msn-02__lb');
    var fig = lb.querySelector('figure');
    var cap = lb.querySelector('.msn-02__lbCap');
    root.querySelectorAll('.msn-02__tile').forEach(function (tile) {
      tile.addEventListener('click', function () {
        ['--img', '--a', '--b', '--ar'].forEach(function (p) {
          fig.style.setProperty(p, getComputedStyle(tile).getPropertyValue(p));
        });
        cap.textContent = tile.dataset.cap || '';
        lb.showModal();
      });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
    lb.querySelector('.msn-02__lbClose').addEventListener('click', function () { lb.close(); });
  });
})();
```
