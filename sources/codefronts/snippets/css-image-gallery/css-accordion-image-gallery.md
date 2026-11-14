---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-accordion-image-gallery/"
title: "CSS Accordion Image Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "A compact row of vertical image strips that smoothly expand on hover or keyboard focus while their neighbours shrink to make room — the space-saving…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Accordion Image Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-accordion-image-gallery/

A compact row of vertical image strips that smoothly expand on hover or keyboard focus while their neighbours shrink to make room — the space-saving accordion gallery portfolios and hero sections search for.
## HTML
```html
<section class="gl-08" aria-label="Accordion image gallery">
  <div class="gl-08__acc">
    <button class="gl-08__panel" type="button" style="--img:url('https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=700&h=900&auto=format&fit=crop')"><span class="gl-08__lbl">Peaks</span></button>
    <button class="gl-08__panel" type="button" style="--img:url('https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=700&h=900&auto=format&fit=crop')"><span class="gl-08__lbl">Forests</span></button>
    <button class="gl-08__panel" type="button" style="--img:url('https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=700&h=900&auto=format&fit=crop')"><span class="gl-08__lbl">Coast</span></button>
    <button class="gl-08__panel" type="button" style="--img:url('https://images.unsplash.com/photo-1463453091185-61582044d556?q=80&w=700&h=900&auto=format&fit=crop')"><span class="gl-08__lbl">Desert</span></button>
    <button class="gl-08__panel" type="button" style="--img:url('https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?q=80&w=700&h=900&auto=format&fit=crop')"><span class="gl-08__lbl">Cities</span></button>
  </div>
</section>
```
## CSS
```css
.gl-08,
.gl-08 *,
.gl-08 *::before,
.gl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-08 ::selection {
  background: oklch(0.62 0.16 20);
  color: #fff;
}

.gl-08 {
  --accent: oklch(0.62 0.16 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #14110f;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-08__acc {
  display: flex;
  gap: 8px;
  width: min(880px,100%);
  height: min(440px,60vh);
}

.gl-08__panel {
  position: relative;
  flex: 1 1 0;
  min-width: 0;
  border: none;
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  padding: 0;
  background: var(--img) center/cover no-repeat;
  filter: brightness(.72) saturate(.95);
  transition: flex-grow .5s cubic-bezier(.2,.7,.2,1),filter .4s;
}

.gl-08__panel:hover,
.gl-08__panel:focus {
  flex-grow: 4;
  filter: brightness(1) saturate(1.05);
}

.gl-08__panel::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(0deg,rgba(10,6,4,.7),transparent 55%);
}

.gl-08__lbl {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 16px;
  z-index: 2;
  text-align: center;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  left: auto;
  right: 12px;
  bottom: auto;
  top: 16px;
  text-shadow: 0 1px 4px rgba(0,0,0,.7);
  transition: opacity .4s;
}

.gl-08__panel:hover .gl-08__lbl,
.gl-08__panel:focus .gl-08__lbl {
  writing-mode: horizontal-tb;
  transform: none;
  top: auto;
  bottom: 16px;
  left: 0;
  right: 0;
  font-size: 18px;
}

.gl-08__panel:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .gl-08__panel {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex-grow rises on :hover/:focus so the focused strip expands. */
```
