---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-zoom-thumbnail-carousel/"
title: "CSS Aspect Ratio Zoom Thumbnail Carousel"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A detail-page gallery where zoom never moves the layout: each carousel frame is a locked 1:1 box, the photo scales to 2.2× inside it on hover, and 12 lines…"
has_js: "true"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Zoom Thumbnail Carousel
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-zoom-thumbnail-carousel/

A detail-page gallery where zoom never moves the layout: each carousel frame is a locked 1:1 box, the photo scales to 2.2× inside it on hover, and 12 lines of JS steer transform-origin under the cursor for a true magnifier feel. The thumbnails are plain anchor links — scroll-snap plus scroll-behavior: smooth turns the browser's own anchor navigation into the carousel engine, so frame switching costs zero JavaScript. Watch-store aesthetics, keyboard path included.
## HTML
```html
<section class="car-07" aria-label="Zoom thumbnail carousel demo">
  <div class="car-07__stage" id="car07-top">
    <header class="car-07__bar">
      <a class="car-07__brand" href="#car07-top">MERAUX</a>
      <nav class="car-07__nav" aria-label="Primary"><a href="#car07-top">Chronographs</a><a href="#car07-top">Divers</a><a href="#car07-top">Straps</a></nav>
      <span class="car-07__chip">frames &amp; thumbs: <code>aspect-ratio: 1</code></span>
    </header>
    <main class="car-07__main">
      <div class="car-07__viewer">
        <div class="car-07__frames" aria-label="Product photos — hover or focus to zoom" tabindex="-1">
          <figure class="car-07__frame" id="car07-f1" tabindex="0" aria-label="Dial close-up, zoomable"><img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=1000&h=1000&auto=format&fit=crop" width="1000" height="1000" alt="Meraux C-01 chronograph, dial close-up"></figure>
          <figure class="car-07__frame" id="car07-f2" tabindex="0" aria-label="Case profile, zoomable"><img src="https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=1000&h=1000&auto=format&fit=crop" width="1000" height="1000" loading="lazy" alt="Case profile with crown detail"></figure>
          <figure class="car-07__frame" id="car07-f3" tabindex="0" aria-label="Movement detail, zoomable"><img src="https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?q=80&w=1000&h=1000&auto=format&fit=crop" width="1000" height="1000" loading="lazy" alt="Exhibition caseback movement"></figure>
          <figure class="car-07__frame" id="car07-f4" tabindex="0" aria-label="On-wrist shot, zoomable"><img src="https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?q=80&w=1000&h=1000&auto=format&fit=crop" width="1000" height="1000" loading="lazy" alt="Watch worn on wrist"></figure>
        </div>
        <nav class="car-07__thumbs" aria-label="Choose photo">
          <a href="#car07-f1"><img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Photo 1: dial"></a>
          <a href="#car07-f2"><img src="https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Photo 2: case"></a>
          <a href="#car07-f3"><img src="https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Photo 3: movement"></a>
          <a href="#car07-f4"><img src="https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Photo 4: on wrist"></a>
        </nav>
      </div>
      <div class="car-07__info">
        <p class="car-07__kicker">C-01 · Automatic chronograph</p>
        <h1>Meraux Calibre One</h1>
        <p class="car-07__price">$1,890</p>
        <p class="car-07__blurb">Hover the photo — the image scales to 2.2× <em>inside</em> its 1:1 frame while the page doesn't move a pixel. The thumbnails drive the carousel with nothing but anchor links and scroll-snap.</p>
        <ul class="car-07__specs">
          <li><b>Case</b><span>39mm brushed 904L steel</span></li>
          <li><b>Movement</b><span>La Joux-Perret G100, 68h reserve</span></li>
          <li><b>Crystal</b><span>Double-domed sapphire</span></li>
          <li><b>Water resistance</b><span>10 ATM</span></li>
        </ul>
        <a class="car-07__cta" href="#car07-top">Reserve yours</a>
        <p class="car-07__note">Ships October · 5-year movement warranty</p>
      </div>
    </main>
    <footer class="car-07__foot">Zoom is <code>scale</code> + <code>transform-origin: var(--zx) var(--zy)</code> inside an <code>overflow:hidden</code> ratio box — layout never reflows. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
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

.car-07 {
  --bg: oklch(0.17 0.012 260);
  --panel: oklch(0.22 0.015 260);
  --ink: oklch(0.95 0.006 250);
  --mut: oklch(0.66 0.015 255);
  --line: oklch(0.33 0.02 260);
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

.car-07__stage {
  width: 100%;
  container: car07/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-07__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
  flex-wrap: wrap;
}

.car-07__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .34em;
  color: inherit;
  text-decoration: none;
}

.car-07__nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.car-07__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.car-07__nav a:hover,
.car-07__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.28 0.02 260/.7);
}

.car-07__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-07__chip {
  font-size: 11.5px;
  color: var(--mut);
}

.car-07__chip code,
.car-07__blurb code,
.car-07__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .92em;
  background: oklch(0.27 0.02 260);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-07__main {
  display: grid;
  grid-template-columns: minmax(0,6fr) minmax(300px,5fr);
  gap: clamp(22px,4cqi,56px);
  align-items: start;
  max-width: 1180px;
  margin-inline: auto;
  padding: clamp(20px,4cqi,44px) clamp(16px,4cqi,44px);
}

.car-07__viewer {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 0;
}

.car-07__frames {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  border-radius: 18px;
  scrollbar-width: none;
  background: var(--panel);
}

.car-07__frames::-webkit-scrollbar {
  display: none;
}

.car-07__frame {
  position: relative;
  flex: none;
  width: 100%;
  aspect-ratio: 1;
  overflow: hidden;
  scroll-snap-align: start;
  background: linear-gradient(150deg,oklch(0.3 0.03 260),oklch(0.22 0.02 290));
  cursor: zoom-in;
}

.car-07__frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transform-origin: var(--zx,50%) var(--zy,50%);
  transition: scale .35s cubic-bezier(.2,.7,.2,1);
}

@media (hover: hover) {
  .car-07__frame:hover img {
    scale: 2.2;
  }
}

.car-07__frame:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
}

.car-07__frame:focus-visible img {
  scale: 2.2;
}

.car-07__thumbs {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
}

.car-07__thumbs a {
  aspect-ratio: 1;
  border-radius: 12px;
  overflow: hidden;
  border: 2px solid var(--line);
  transition: border-color .2s,translate .2s;
}

.car-07__thumbs a:hover,
.car-07__thumbs a:focus-visible {
  border-color: var(--acc);
  translate: 0 -2px;
}

.car-07__thumbs a:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-07__thumbs img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-07__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-07__info h1 {
  font-size: clamp(24px,3.4cqi,36px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-top: 8px;
}

.car-07__price {
  margin-top: 8px;
  font-size: 20px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.car-07__blurb {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
}

.car-07__specs {
  list-style: none;
  margin-top: 18px;
  border-top: 1px solid var(--line);
}

.car-07__specs li {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  padding: 11px 0;
  border-bottom: 1px solid var(--line);
  font-size: 13px;
}

.car-07__specs b {
  color: var(--mut);
  font-weight: 600;
}

.car-07__specs span {
  text-align: right;
}

.car-07__cta {
  display: grid;
  place-items: center;
  min-height: 52px;
  margin-top: 20px;
  border-radius: 13px;
  background: var(--acc);
  color: oklch(0.22 0.04 85);
  font-size: 15px;
  font-weight: 800;
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.car-07__cta:hover,
.car-07__cta:focus-visible {
  background: color-mix(in oklch,var(--acc) 88%,white);
  translate: 0 -2px;
}

.car-07__cta:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-07__note {
  margin-top: 10px;
  font-size: 12px;
  color: var(--mut);
  text-align: center;
}

.car-07__foot {
  max-width: 1180px;
  margin-inline: auto;
  padding: 18px clamp(16px,4cqi,44px) 34px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

@container car07 (width < 720px) {
  .car-07__main {
    grid-template-columns: 1fr;
  }

  .car-07__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-07__frames {
    scroll-behavior: auto;
  }

  .car-07 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.car-07__frame').forEach((f) => {
    if (f.dataset.zoom) return;
    f.dataset.zoom = '1';
    f.addEventListener('pointermove', (e) => {
      const r = f.getBoundingClientRect();
      f.style.setProperty('--zx', (((e.clientX - r.left) / r.width) * 100).toFixed(2) + '%');
      f.style.setProperty('--zy', (((e.clientY - r.top) / r.height) * 100).toFixed(2) + '%');
    });
    f.addEventListener('pointerleave', () => { f.style.removeProperty('--zx'); f.style.removeProperty('--zy'); });
  });
})();
```
