---
source: "codefronts"
url: "https://codefronts.com/snippets/css-custom-cursor/magnifier-zoom-lens/"
title: "Magnifier Zoom Lens Cursor with Native zoom-in / crosshair Keywords and background-position Math"
section: "snippets"
category: "css-custom-cursor"
category_name: "CSS Custom Cursor Styles"
description: "The lightbox / product-gallery classic: a native zoom-in cursor over the image plus a real magnifier lens that follows the pointer and shows a 2.5× close-up…"
has_js: "true"
---

Here's a working CSS Custom Cursor Style from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnifier Zoom Lens Cursor with Native zoom-in / crosshair Keywords and background-position Math
Source: https://codefronts.com/snippets/css-custom-cursor/magnifier-zoom-lens/

The lightbox / product-gallery classic: a native zoom-in cursor over the image plus a real magnifier lens that follows the pointer and shows a 2.5× close-up of exactly what's under it. It layers the simplest technique — CSS's built-in zoom-in / crosshair keywords with a custom SVG magnifier fallback — with a proper background-position lens so users get both the affordance and the payoff.
## HTML
```html
<section class="ccs-06">
  <div class="ccs-06__wrap">
    <div class="ccs-06__figure" data-figure>
      <div class="ccs-06__photo" data-photo></div>
      <div class="ccs-06__lens" data-lens aria-hidden="true"></div>
    </div>
    <p class="ccs-06__cap">Hover the poster — a 2.5× lens follows your pointer. <code>cursor: zoom-in</code> with an SVG loupe fallback.</p>
  </div>
</section>
```
## CSS
```css
.ccs-06,
.ccs-06 *,
.ccs-06 *::before,
.ccs-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccs-06 {
  --photo: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='600' viewBox='0 0 600 600'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%23ff8a3d'/%3E%3Cstop offset='0.5' stop-color='%23e0246c'/%3E%3Cstop offset='1' stop-color='%236b2fe0'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='600' height='600' fill='url(%23g)'/%3E%3Cg fill='none' stroke='%23ffffff' stroke-opacity='0.5' stroke-width='2'%3E%3Ccircle cx='150' cy='150' r='90'/%3E%3Ccircle cx='150' cy='150' r='60'/%3E%3Ccircle cx='150' cy='150' r='30'/%3E%3C/g%3E%3Cg fill='%23ffffff' fill-opacity='0.9'%3E%3Ccircle cx='440' cy='180' r='10'/%3E%3Ccircle cx='480' cy='230' r='6'/%3E%3Ccircle cx='410' cy='240' r='5'/%3E%3C/g%3E%3Cpath d='M60 470 L200 340 L320 430 L460 300 L540 380' fill='none' stroke='%23ffffff' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'/%3E%3Ctext x='50' y='555' font-family='system-ui,sans-serif' font-size='58' font-weight='800' fill='%23ffffff'%3ECODEFRONTS%3C/text%3E%3C/svg%3E");
  --bg: oklch(0.15 0.01 30);
  --text: oklch(0.96 0.005 30);
  --muted: color-mix(in oklab,var(--text) 55%,var(--bg));
  color-scheme: dark;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 28px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
}

.ccs-06__wrap {
  width: min(440px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ccs-06__figure {
  position: relative;
  aspect-ratio: 1;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid oklch(0.34 0.02 30);
}

.ccs-06__photo {
  position: absolute;
  inset: 0;
  background-image: var(--photo);
  background-size: cover;
  background-position: center;
}

.ccs-06__lens {
  position: absolute;
  top: 0;
  left: 0;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  pointer-events: none;
  background-image: var(--photo);
  background-size: 250%;
  box-shadow: 0 0 0 3px oklch(1 0 0/.85),0 12px 30px oklch(0 0 0/.5);
  opacity: 0;
  transition: opacity .2s ease;
}

.ccs-06__figure.is-live .ccs-06__lens {
  opacity: 1;
}

.ccs-06__cap {
  font: 400 13.5px/1.55 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.ccs-06__cap code {
  font: 600 12px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.08);
  color: var(--text);
}

@media (hover: hover) and (pointer: fine) {
  .ccs-06__figure {
    cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'%3E%3Ccircle cx='11' cy='11' r='7.5' fill='none' stroke='%23ffffff' stroke-width='2'/%3E%3Cpath d='M11 8v6M8 11h6' stroke='%23ffffff' stroke-width='2' stroke-linecap='round'/%3E%3Cpath d='M16.5 16.5 25 25' stroke='%23ffffff' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E") 11 11, zoom-in;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccs-06__lens {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var fig = document.querySelector('.ccs-06__figure');
  var lens = fig.querySelector('[data-lens]');
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return; // touch → plain image

  fig.addEventListener('pointerenter', function () { fig.classList.add('is-live'); });
  fig.addEventListener('pointerleave', function () { fig.classList.remove('is-live'); });
  fig.addEventListener('pointermove', function (e) {
    var r = fig.getBoundingClientRect();
    var x = e.clientX - r.left, y = e.clientY - r.top;
    var px = x / r.width * 100, py = y / r.height * 100;   // pointer as % of image
    lens.style.backgroundPosition = px + '% ' + py + '%';  // keep the zoom registered
    lens.style.transform = 'translate(' + x + 'px,' + y + 'px) translate(-50%,-50%)';
  });
})();
```
