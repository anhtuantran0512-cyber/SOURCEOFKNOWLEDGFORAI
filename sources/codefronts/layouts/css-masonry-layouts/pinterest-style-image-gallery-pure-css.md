---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/pinterest-style-image-gallery-pure-css/"
title: "Pinterest Style Image Gallery Pure CSS"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "The layout that made masonry famous, rebuilt in two declarations and zero scripts: columns: 230px mints as many columns as fit the container, break-inside:…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pinterest Style Image Gallery Pure CSS
Source: https://codefronts.com/layouts/css-masonry-layouts/pinterest-style-image-gallery-pure-css/

The layout that made masonry famous, rebuilt in two declarations and zero scripts: columns: 230px mints as many columns as fit the container, break-inside: avoid keeps every pin whole, and the browser does the packing at compositor speed. Every pin reserves its exact height with aspect-ratio (CLS score: 0 by construction), the Save action surfaces on hover AND keyboard focus, and a container query tightens the gutters wherever the wall is pasted.
## HTML
```html
<section class="msn-01" aria-label="Pinterest style pure CSS masonry gallery demo">
  <div class="msn-01__stage" tabindex="0">
    <header class="msn-01__head">
      <div><h2>Saved ideas</h2><p>184 pins · updated today</p></div>
      <nav class="msn-01__chips" aria-label="Filter pins">
        <a href="#all" aria-current="true">All</a><a href="#interiors">Interiors</a><a href="#travel">Travel</a><a href="#food">Food</a><a href="#style">Style</a>
      </nav>
    </header>
    <div class="msn-01__wall">
      <article class="msn-01__pin"><figure style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=800&auto=format&fit=crop');--a:oklch(0.75 0.09 250);--b:oklch(0.45 0.12 270)"><figcaption>Alpine mornings</figcaption><a class="msn-01__save" href="#save-1">Save</a></figure><h3><a class="msn-01__link" href="#pin-1">Dolomites cabin week</a></h3><p>1.2k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:4/5;--img:url('https://images.unsplash.com/photo-1493809842364-78817add7ffb?q=80&w=800&auto=format&fit=crop');--a:oklch(0.85 0.06 80);--b:oklch(0.6 0.1 60)"><figcaption>Warm minimalism</figcaption><a class="msn-01__save" href="#save-2">Save</a></figure><h3><a class="msn-01__link" href="#pin-2">Living room in oak + linen</a></h3><p>867 saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.13 40);--b:oklch(0.5 0.15 25)"><figcaption>Sunday table</figcaption><a class="msn-01__save" href="#save-3">Save</a></figure><h3><a class="msn-01__link" href="#pin-3">Herbed citrus roast</a></h3><p>2.4k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:16/10;--img:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.85 0.07 220);--b:oklch(0.65 0.1 240)"><figcaption>Shoulder season</figcaption><a class="msn-01__save" href="#save-4">Save</a></figure><h3><a class="msn-01__link" href="#pin-4">Quiet beaches, October</a></h3><p>3.1k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:2/3;--img:url('https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.05 340);--b:oklch(0.55 0.1 320)"><figcaption>Capsule fits</figcaption><a class="msn-01__save" href="#save-5">Save</a></figure><h3><a class="msn-01__link" href="#pin-5">Neutral layering, autumn</a></h3><p>412 saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:4/5;--img:url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=800&auto=format&fit=crop');--a:oklch(0.65 0.08 60);--b:oklch(0.4 0.09 50)"><figcaption>Slow brew</figcaption><a class="msn-01__save" href="#save-6">Save</a></figure><h3><a class="msn-01__link" href="#pin-6">Pour-over ritual at home</a></h3><p>958 saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.11 150);--b:oklch(0.45 0.12 160)"><figcaption>Forest bathing</figcaption><a class="msn-01__save" href="#save-7">Save</a></figure><h3><a class="msn-01__link" href="#pin-7">Old-growth trails, PNW</a></h3><p>1.8k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.04 100);--b:oklch(0.6 0.06 80)"><figcaption>Everyday carry</figcaption><a class="msn-01__save" href="#save-8">Save</a></figure><h3><a class="msn-01__link" href="#pin-8">Field watch, sand strap</a></h3><p>623 saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:2/3;--img:url('https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=800&auto=format&fit=crop');--a:oklch(0.82 0.06 20);--b:oklch(0.6 0.1 0)"><figcaption>Market day</figcaption><a class="msn-01__save" href="#save-9">Save</a></figure><h3><a class="msn-01__link" href="#pin-9">Vintage shopping, Le Marais</a></h3><p>2.9k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:16/10;--img:url('https://images.unsplash.com/photo-1449824913935-59a10b8d2000?q=80&w=800&auto=format&fit=crop');--a:oklch(0.72 0.08 260);--b:oklch(0.5 0.1 280)"><figcaption>Golden hour grid</figcaption><a class="msn-01__save" href="#save-10">Save</a></figure><h3><a class="msn-01__link" href="#pin-10">Downtown from the rooftop</a></h3><p>1.1k saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:1/1;--img:url('https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.1 130);--b:oklch(0.55 0.12 110)"><figcaption>Bowl food</figcaption><a class="msn-01__save" href="#save-11">Save</a></figure><h3><a class="msn-01__link" href="#pin-11">Fifteen-minute grain bowls</a></h3><p>745 saves</p></article>
      <article class="msn-01__pin"><figure style="--ar:3/4;--img:url('https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=800&auto=format&fit=crop');--a:oklch(0.7 0.06 200);--b:oklch(0.45 0.08 220)"><figcaption>Fog lines</figcaption><a class="msn-01__save" href="#save-12">Save</a></figure><h3><a class="msn-01__link" href="#pin-12">Ridge walks before 7am</a></h3><p>534 saves</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-01,
.msn-01 *,
.msn-01 *::before,
.msn-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-01 {
  --gap: 14px;
  --bg: oklch(0.985 0.004 85);
  --ink: oklch(0.22 0.015 60);
  --mut: oklch(0.55 0.02 60);
  --line: oklch(0.91 0.008 85);
  --acc: oklch(0.55 0.21 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-01__stage {
  width: 100%;
  container: msn01/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-01__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px 18px;
  padding: 16px clamp(16px,3cqi,28px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-01__head h2 {
  font-size: clamp(18px,2.6cqi,24px);
  letter-spacing: -.02em;
}

.msn-01__head p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-01__chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.msn-01__chips a {
  display: grid;
  place-items: center;
  min-height: 36px;
  padding: 0 14px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  color: var(--ink);
  border: 1px solid var(--line);
  transition: background .2s,border-color .2s;
}

.msn-01__chips a:hover,
.msn-01__chips a:focus-visible {
  background: oklch(0.94 0.008 85);
  border-color: oklch(0.84 0.01 85);
}

.msn-01__chips a[aria-current] {
  background: var(--ink);
  border-color: var(--ink);
  color: oklch(0.99 0 0);
}

.msn-01__chips a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-01__wall {
  columns: 230px;
  column-gap: var(--gap);
  padding: clamp(16px,3cqi,28px);
}

.msn-01__pin {
  break-inside: avoid;
  margin-bottom: var(--gap);
  position: relative;
}

.msn-01__pin figure {
  position: relative;
  aspect-ratio: var(--ar,3/4);
  border-radius: 16px;
  overflow: clip;
  background: linear-gradient(145deg,var(--a),var(--b));
}

.msn-01__pin figure::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none);
  background-size: cover;
  background-position: center;
  transition: scale .45s cubic-bezier(.2,.7,.2,1);
}

.msn-01__pin figure::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.2 0.02 60/.32),transparent 34%,transparent 66%,oklch(0.2 0.02 60/.42));
  opacity: 0;
  transition: opacity .3s;
}

.msn-01__pin:hover figure::before,
.msn-01__pin:focus-within figure::before {
  scale: 1.045;
}

.msn-01__pin:hover figure::after,
.msn-01__pin:focus-within figure::after {
  opacity: 1;
}

.msn-01__pin figcaption {
  position: absolute;
  left: 12px;
  bottom: 10px;
  z-index: 1;
  font-size: 12px;
  font-weight: 600;
  color: oklch(0.99 0 0);
  text-shadow: 0 1px 8px oklch(0.15 0.02 60/.6);
  opacity: 0;
  translate: 0 6px;
  transition: opacity .3s,translate .3s;
}

.msn-01__pin:hover figcaption,
.msn-01__pin:focus-within figcaption {
  opacity: 1;
  translate: 0 0;
}

.msn-01__save {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--acc);
  opacity: 0;
  translate: 0 -4px;
  transition: opacity .25s,translate .25s,background .2s;
}

.msn-01__pin:hover .msn-01__save,
.msn-01__pin:focus-within .msn-01__save {
  opacity: 1;
  translate: 0 0;
}

.msn-01__save:hover {
  background: oklch(0.48 0.21 25);
}

.msn-01__save:focus-visible {
  outline: 2px solid oklch(0.99 0 0);
  outline-offset: 2px;
}

.msn-01__pin h3 {
  margin-top: 9px;
  font-size: 14px;
  line-height: 1.35;
  letter-spacing: -.01em;
}

.msn-01__link {
  color: inherit;
  text-decoration: none;
}

.msn-01__link::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 16px;
}

.msn-01__link:focus-visible {
  outline: none;
}

.msn-01__link:focus-visible::after {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.msn-01__pin>p {
  margin-top: 3px;
  font-size: 12px;
  color: var(--mut);
}

@media (hover: none) {
  .msn-01__save,
    .msn-01__pin figcaption {
    opacity: 1;
    translate: 0 0;
  }
}

@container msn01 (width < 480px) {
  .msn-01__wall {
    columns: 150px;
    --gap: 10px;
  }

  .msn-01__pin figure {
    border-radius: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-01 *,
    .msn-01 *::before,
    .msn-01 *::after {
    transition-duration: .01ms !important;
  }
}
```
