---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-masonry-gallery-zoom-hover/"
title: "CSS Masonry Gallery Zoom Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Pinterest-style column masonry gallery where individual items zoom in on hover without disrupting the column flow via isolated overflow contexts."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Gallery Zoom Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-masonry-gallery-zoom-hover/

Pinterest-style column masonry gallery where individual items zoom in on hover without disrupting the column flow via isolated overflow contexts.
## HTML
```html
<div class="ih-18">
  <div class="ih-18__masonry">
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--tall ih-18__img--a"></div>
      <span class="ih-18__emoji">🌌</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Cosmos</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--sq ih-18__img--b"></div>
      <span class="ih-18__emoji">🌿</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Flora</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--wide ih-18__img--c"></div>
      <span class="ih-18__emoji">🏜️</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Desert</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--sq ih-18__img--d"></div>
      <span class="ih-18__emoji">🌊</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Ocean</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--tall ih-18__img--e"></div>
      <span class="ih-18__emoji">🌺</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Bloom</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--wide ih-18__img--f"></div>
      <span class="ih-18__emoji">🧊</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Ice</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--wide ih-18__img--g"></div>
      <span class="ih-18__emoji">🔮</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Mystic</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--tall ih-18__img--h"></div>
      <span class="ih-18__emoji">🌲</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Forest</span></div>
    </div>
    <div class="ih-18__item">
      <div class="ih-18__img ih-18__img--sq ih-18__img--a"></div>
      <span class="ih-18__emoji">⭐</span>
      <div class="ih-18__overlay"><span class="ih-18__tag">Stars</span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-18,
.ih-18 *,
.ih-18 *::before,
.ih-18 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-18 ::selection {
  background: #f43f5e;
  color: #fff;
}

.ih-18 {
  --accent: #f43f5e;
  --bg: #08080c;
  --text: #f1f5f9;
  --muted: #64748b;
  --duration: 0.4s;
  --ease: cubic-bezier(0.25,0.46,0.45,0.94);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 32px 24px;
  min-height: 100vh;
}
/* CSS Masonry via columns — no JS layout required */

.ih-18__masonry {
  columns: 3;
  column-gap: 12px;
  max-width: 780px;
  margin: 0 auto;
}

.ih-18__item {
  break-inside: avoid;
  margin-bottom: 12px;
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  /* Isolate so zoom doesn't clip to the column boundary */
  display: block;
}

.ih-18__img {
  display: block;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease);
}

.ih-18__item:hover .ih-18__img {
  transform: scale(1.08);
}
/* Heights via padding-top for aspect ratios */

.ih-18__img--tall {
  padding-top: 140%;
}

.ih-18__img--sq {
  padding-top: 100%;
}

.ih-18__img--wide {
  padding-top: 65%;
}

.ih-18__img--a {
  background-image: url('https://picsum.photos/seed/masonry-a/600/600'), linear-gradient(150deg,#1a0533,#4c1d95,#7c3aed);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--b {
  background-image: url('https://picsum.photos/seed/masonry-b/600/600'), linear-gradient(150deg,#042f2e,#065f46,#10b981);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--c {
  background-image: url('https://picsum.photos/seed/masonry-c/600/600'), linear-gradient(150deg,#1c1003,#92400e,#f59e0b);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--d {
  background-image: url('https://picsum.photos/seed/masonry-d/600/600'), linear-gradient(150deg,#0c1445,#1e3a8a,#3b82f6);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--e {
  background-image: url('https://picsum.photos/seed/masonry-e/600/600'), linear-gradient(150deg,#1a0010,#9d174d,#f43f5e);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--f {
  background-image: url('https://picsum.photos/seed/masonry-f/600/600'), linear-gradient(150deg,#082032,#1e3a5f,#0891b2);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--g {
  background-image: url('https://picsum.photos/seed/masonry-g/600/600'), linear-gradient(150deg,#0f0c29,#312e81,#4f46e5);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-18__img--h {
  background-image: url('https://picsum.photos/seed/masonry-h/600/600'), linear-gradient(150deg,#052e16,#14532d,#4ade80);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
/* Hover overlay */

.ih-18__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,rgba(0,0,0,0.7) 0%,transparent 60%);
  opacity: 0;
  transition: opacity var(--duration) var(--ease);
  display: flex;
  align-items: flex-end;
  padding: 10px;
}

.ih-18__item:hover .ih-18__overlay {
  opacity: 1;
}

.ih-18__tag {
  font-size: 10px;
  font-weight: 700;
  color: #fff;
  background: rgba(244,63,94,0.7);
  border-radius: 4px;
  padding: 2px 6px;
}

.ih-18__emoji {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  font-size: 36px;
  opacity: 0.3;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .ih-18__img,
    .ih-18__overlay {
    transition: none;
  }

  .ih-18__overlay {
    opacity: 1;
  }
}
```
