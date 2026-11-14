---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-metro-tile-grid-gallery/"
title: "CSS Metro Tile Grid Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A Windows-8 / Windows-Phone 'Metro' layout mixing large 2×2 hero tiles, wide 2×1 banners and small 1×1 squares into one dense, deliberately asymmetric grid."
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Metro Tile Grid Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-metro-tile-grid-gallery/

A Windows-8 / Windows-Phone 'Metro' layout mixing large 2×2 hero tiles, wide 2×1 banners and small 1×1 squares into one dense, deliberately asymmetric grid. The tile-mosaic look devs search for by name.
## HTML
```html
<section class="gl-02" aria-label="Metro tile image gallery">
  <div class="gl-02__grid">
    <a class="gl-02__tile gl-02__tile--big" href="#"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=800&h=800&auto=format&fit=crop" alt="Modern city architecture" loading="lazy" decoding="async"><span class="gl-02__cap">Architecture</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=400&h=400&auto=format&fit=crop" alt="Busy city street" loading="lazy" decoding="async"><span class="gl-02__cap">Street</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=400&h=400&auto=format&fit=crop" alt="Coffee on a cafe table" loading="lazy" decoding="async"><span class="gl-02__cap">Cafe</span></a>
    <a class="gl-02__tile gl-02__tile--wide" href="#"><img src="https://images.unsplash.com/photo-1573496799652-408c2ac9fe98?q=80&w=800&h=400&auto=format&fit=crop" alt="Suspension bridge at dusk" loading="lazy" decoding="async"><span class="gl-02__cap">Bridge</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=400&h=400&auto=format&fit=crop" alt="Open air market stalls" loading="lazy" decoding="async"><span class="gl-02__cap">Market</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1523362628745-0c100150b504?q=80&w=400&h=400&auto=format&fit=crop" alt="Underground subway platform" loading="lazy" decoding="async"><span class="gl-02__cap">Transit</span></a>
    <a class="gl-02__tile gl-02__tile--tall" href="#"><img src="https://images.unsplash.com/photo-1418985991508-e47386d96a71?q=80&w=400&h=800&auto=format&fit=crop" alt="Glass tower rising overhead" loading="lazy" decoding="async"><span class="gl-02__cap">Skyline</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1507473885765-e6ed057f782c?q=80&w=400&h=400&auto=format&fit=crop" alt="City park in spring" loading="lazy" decoding="async"><span class="gl-02__cap">Park</span></a>
    <a class="gl-02__tile" href="#"><img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=400&h=400&auto=format&fit=crop" alt="Neon signs at night" loading="lazy" decoding="async"><span class="gl-02__cap">Nightlife</span></a>
  </div>
</section>
```
## CSS
```css
.gl-02,
.gl-02 *,
.gl-02 *::before,
.gl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-02 ::selection {
  background: oklch(0.6 0.17 200);
  color: #fff;
}

.gl-02 {
  --accent: oklch(0.6 0.17 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #101418;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-02__grid {
  width: min(760px,100%);
  display: grid;
  gap: 8px;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: 1fr;
  grid-auto-flow: dense;
}

.gl-02__grid::before {
  content: "";
  grid-column: 1;
  grid-row: 1;
  aspect-ratio: 1/1;
  grid-area: 1/1;
}

.gl-02__tile {
  position: relative;
  overflow: hidden;
  text-decoration: none;
  aspect-ratio: 1/1;
  background: #1a2027;
  border-radius: 4px;
}

.gl-02__tile--big {
  grid-column: span 2;
  grid-row: span 2;
  aspect-ratio: auto;
}

.gl-02__tile--wide {
  grid-column: span 2;
  aspect-ratio: auto;
}

.gl-02__tile--tall {
  grid-row: span 2;
  aspect-ratio: auto;
}

.gl-02__tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1);
  transition: transform .5s cubic-bezier(.2,.7,.2,1);
  filter: saturate(1.02);
}

.gl-02__tile:hover img,
.gl-02__tile:focus-visible img {
  transform: scale(1.08);
}

.gl-02__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 26px 14px 12px;
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .02em;
  background: linear-gradient(0deg,rgba(6,10,14,.82),transparent);
  transform: translateY(8px);
  opacity: 0;
  transition: transform .3s,opacity .3s;
}

.gl-02__tile:hover .gl-02__cap,
.gl-02__tile:focus-visible .gl-02__cap {
  transform: translateY(0);
  opacity: 1;
}

.gl-02__tile:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 640px) {
  .gl-02__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .gl-02__tile--big,
    .gl-02__tile--wide {
    grid-column: span 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-02__tile img,
    .gl-02__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS Grid span + grid-auto-flow:dense build the Metro mosaic. */
```
