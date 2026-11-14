---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-magazine-layout-gallery/"
title: "CSS Magazine Layout Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A premium editorial spread: a bold full-bleed hero image with a headline set directly over it in a blend mode, flanked by an asymmetric grid of supporting…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magazine Layout Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-magazine-layout-gallery/

A premium editorial spread: a bold full-bleed hero image with a headline set directly over it in a blend mode, flanked by an asymmetric grid of supporting shots. The magazine-style image layout design-led sites search for.
## HTML
```html
<section class="gl-03" aria-label="Magazine layout gallery">
  <div class="gl-03__grid">
    <figure class="gl-03__hero">
      <img src="https://images.unsplash.com/photo-1481277542470-605612bd2d61?q=80&w=900&h=700&auto=format&fit=crop" alt="Winding coastal road at sunset" loading="lazy" decoding="async">
      <figcaption class="gl-03__over">
        <span class="gl-03__kicker">Issue 24 · Travel</span>
        <h3 class="gl-03__title">The Long Way North</h3>
      </figcaption>
    </figure>
    <figure class="gl-03__cell"><img src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?q=80&w=500&h=500&auto=format&fit=crop" alt="Fishing harbour at first light" loading="lazy" decoding="async"><figcaption>Harbour mornings</figcaption></figure>
    <figure class="gl-03__cell"><img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=500&h=500&auto=format&fit=crop" alt="Timber cabin among pines" loading="lazy" decoding="async"><figcaption>Off the map</figcaption></figure>
    <figure class="gl-03__cell gl-03__cell--wide"><img src="https://images.unsplash.com/photo-1611432579699-484f7990b127?q=80&w=900&h=450&auto=format&fit=crop" alt="Empty mountain highway" loading="lazy" decoding="async"><figcaption>Nothing but road ahead</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.gl-03,
.gl-03 *,
.gl-03 *::before,
.gl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-03 ::selection {
  background: #111;
  color: #fff;
}

.gl-03 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 44px 20px;
  background: #f7f5f0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-03__grid {
  width: min(940px,100%);
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(2,1fr);
  grid-auto-rows: auto;
}

.gl-03__hero {
  position: relative;
  grid-column: 1 / 2;
  grid-row: 1 / 3;
  border-radius: 6px;
  overflow: hidden;
}

.gl-03__hero img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  aspect-ratio: 9/11;
}

.gl-03__over {
  position: absolute;
  inset: auto 0 0 0;
  padding: 24px;
  mix-blend-mode: difference;
  color: #fff;
}

.gl-03__kicker {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  opacity: .9;
}

.gl-03__title {
  margin-top: 8px;
  font-family: Georgia,'Times New Roman',serif;
  font-size: 40px;
  line-height: 1.02;
  font-weight: 700;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.gl-03__cell {
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  background: #e7e3da;
}

.gl-03__cell img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  aspect-ratio: 1/1;
  transition: transform .5s cubic-bezier(.2,.7,.2,1);
}

.gl-03__cell--wide {
  grid-column: 1 / 3;
}

.gl-03__cell--wide img {
  aspect-ratio: 2/1;
}

.gl-03__cell figcaption {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 10px 14px;
  color: #fff;
  font-family: Georgia,serif;
  font-style: italic;
  font-size: 15px;
  background: linear-gradient(0deg,rgba(0,0,0,.6),transparent);
  width: 100%;
}

.gl-03__cell:hover img {
  transform: scale(1.05);
}

@media (max-width: 640px) {
  .gl-03__grid {
    grid-template-columns: 1fr;
  }

  .gl-03__hero {
    grid-column: 1;
    grid-row: auto;
  }

  .gl-03__cell--wide {
    grid-column: 1;
  }

  .gl-03__title {
    font-size: 32px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-03__cell img {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS Grid + mix-blend-mode set editorial type over the hero image. */
```
