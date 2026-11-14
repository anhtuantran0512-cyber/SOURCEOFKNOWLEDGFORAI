---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-flexbox-expanding-panel-gallery/"
title: "CSS Flexbox Expanding Panel Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A full-width split of tall vertical panels that slide open from flex:1 to flex:5 on interaction, revealing a title and blurb over the image — the immersive…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Expanding Panel Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-flexbox-expanding-panel-gallery/

A full-width split of tall vertical panels that slide open from flex:1 to flex:5 on interaction, revealing a title and blurb over the image — the immersive expanding-panels hero landing pages and case-study indexes search for.
## HTML
```html
<section class="gl-09" aria-label="Expanding panel gallery">
  <div class="gl-09__row">
    <a class="gl-09__panel" href="#" style="--img:url('https://images.unsplash.com/photo-1531123897727-8f129e1688ce?q=80&w=900&h=1100&auto=format&fit=crop')"><div class="gl-09__inner"><h3>Structures</h3><p>Concrete, glass and the geometry of modern cities.</p><span class="gl-09__more">View series →</span></div></a>
    <a class="gl-09__panel" href="#" style="--img:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=900&h=1100&auto=format&fit=crop')"><div class="gl-09__inner"><h3>Wilderness</h3><p>Remote landscapes far from the nearest road.</p><span class="gl-09__more">View series →</span></div></a>
    <a class="gl-09__panel" href="#" style="--img:url('https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=900&h=1100&auto=format&fit=crop')"><div class="gl-09__inner"><h3>Portraits</h3><p>Faces and the stories written across them.</p><span class="gl-09__more">View series →</span></div></a>
    <a class="gl-09__panel" href="#" style="--img:url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=900&h=1100&auto=format&fit=crop')"><div class="gl-09__inner"><h3>Water</h3><p>Oceans, rivers and everything in between.</p><span class="gl-09__more">View series →</span></div></a>
    <a class="gl-09__panel" href="#" style="--img:url('https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=900&h=1100&auto=format&fit=crop')"><div class="gl-09__inner"><h3>After Dark</h3><p>Long exposures under a moving sky.</p><span class="gl-09__more">View series →</span></div></a>
  </div>
</section>
```
## CSS
```css
.gl-09,
.gl-09 *,
.gl-09 *::before,
.gl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-09 ::selection {
  background: oklch(0.7 0.15 250);
  color: #fff;
}

.gl-09 {
  --accent: oklch(0.72 0.15 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 0;
  background: #0c0e12;
  display: flex;
  align-items: stretch;
  justify-content: center;
}

.gl-09__row {
  display: flex;
  width: 100%;
  height: 100vh;
}

.gl-09__panel {
  position: relative;
  flex: 1 1 0;
  min-width: 0;
  overflow: hidden;
  text-decoration: none;
  background: var(--img) center/cover no-repeat;
  filter: brightness(.62);
  transition: flex .6s cubic-bezier(.2,.7,.2,1),filter .5s;
}

.gl-09__panel::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(0deg,rgba(8,10,16,.85),transparent 60%);
}

.gl-09__panel:hover,
.gl-09__panel:focus-within {
  flex: 5;
  filter: brightness(1);
}

.gl-09__inner {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
  padding: 32px;
  color: #fff;
  opacity: 0;
  transform: translateY(24px);
  transition: opacity .5s .15s,transform .5s .15s;
  max-width: 520px;
}

.gl-09__panel:hover .gl-09__inner,
.gl-09__panel:focus-within .gl-09__inner {
  opacity: 1;
  transform: translateY(0);
}

.gl-09__inner h3 {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.gl-09__inner p {
  margin-top: 8px;
  font-size: 15px;
  line-height: 1.5;
  color: rgba(255,255,255,.85);
}

.gl-09__more {
  display: inline-block;
  margin-top: 14px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .04em;
  color: var(--accent);
}

.gl-09__panel:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

@media (max-width: 640px) {
  .gl-09__inner h3 {
    font-size: 22px;
  }

  .gl-09__inner p {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-09__panel,
    .gl-09__inner {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex jumps to 5 on :hover/:focus-within and reveals the panel copy. */
```
