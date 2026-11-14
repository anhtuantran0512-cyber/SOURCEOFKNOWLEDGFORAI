---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/pinterest-masonry/"
title: "Pinterest Masonry"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The staggered waterfall without a masonry library: a fine-grained row grid (grid-auto-rows: 8px) where each pin spans a per-item number of rows via one…"
has_js: "true"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pinterest Masonry
Source: https://codefronts.com/layouts/css-grid-layouts/pinterest-masonry/

The staggered waterfall without a masonry library: a fine-grained row grid (grid-auto-rows: 8px) where each pin spans a per-item number of rows via one custom property. Items pack across-then-down like real Pinterest — the ordering CSS columns can't give you — and the whole wall is dense-packed against gaps.
## HTML
```html
<section class="cgl-13" aria-label="Pinterest masonry demo">
  <div class="cgl-13__wall">
    <article class="cgl-13__pin" style="--r:22;--h:oklch(0.75 0.11 350)"><div class="cgl-13__ph"></div><p>Rose quartz study</p></article>
    <article class="cgl-13__pin" style="--r:32;--h:oklch(0.72 0.12 230)"><div class="cgl-13__ph"></div><p>Harbor fog, morning</p></article>
    <article class="cgl-13__pin" style="--r:26;--h:oklch(0.78 0.13 130)"><div class="cgl-13__ph"></div><p>Moss macro</p></article>
    <article class="cgl-13__pin" style="--r:36;--h:oklch(0.76 0.13 60)"><div class="cgl-13__ph"></div><p>Ochre canyon, golden hour</p></article>
    <article class="cgl-13__pin" style="--r:20;--h:oklch(0.7 0.13 300)"><div class="cgl-13__ph"></div><p>Violet dusk</p></article>
    <article class="cgl-13__pin" style="--r:28;--h:oklch(0.73 0.12 180)"><div class="cgl-13__ph"></div><p>Glacier melt</p></article>
    <article class="cgl-13__pin" style="--r:24;--h:oklch(0.74 0.14 20)"><div class="cgl-13__ph"></div><p>Terracotta rooftops</p></article>
    <article class="cgl-13__pin" style="--r:30;--h:oklch(0.77 0.1 90)"><div class="cgl-13__ph"></div><p>Wheat field lines</p></article>
  </div>
</section>
```
## CSS
```css
.cgl-13,
.cgl-13 *,
.cgl-13 *::before,
.cgl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-13 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.96 0.008 300);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-13 .cgl-13__wall {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  grid-auto-rows: 8px;
  grid-auto-flow: dense;
  gap: 12px;
}

.cgl-13 .cgl-13__pin {
  grid-row: span var(--r,24);
  background: white;
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 20px -14px oklch(0.4 0.05 300/.7);
}

.cgl-13 .cgl-13__ph {
  flex: 1;
  background: linear-gradient(160deg,var(--h),color-mix(in oklab,var(--h) 55%,oklch(0.3 0.05 300)));
}

.cgl-13 .cgl-13__pin p {
  font-size: .72rem;
  color: oklch(0.4 0.02 300);
  padding: .55rem .7rem;
}
/* Dynamic content sizing (uncomment in production):
const wall=document.querySelector('.cgl-13__wall');
new ResizeObserver(es=>es.forEach(e=>{const p=e.target.closest('.cgl-13__pin');
p.style.setProperty('--r',Math.ceil((e.contentRect.height+34)/ (8+12)*(8+12)/8/ (8+12)*(8+12)/8))})); — or simpler: span = Math.ceil((pin.scrollHeight+gap)/(rowSize+gap)) */
```

## JavaScript
```js
/* No JavaScript required — per-pin --r spans on an 8px row ruler build the waterfall; a 3-line ResizeObserver handles unknown heights in production. */
```
