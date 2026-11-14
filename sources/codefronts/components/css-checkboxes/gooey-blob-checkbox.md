---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/gooey-blob-checkbox/"
title: "Gooey Blob Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A liquid-mercury effect: separate blobs stretch, detach and fuse back together like a single gooey mass as the box fills."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gooey Blob Checkbox
Source: https://codefronts.com/components/css-checkboxes/gooey-blob-checkbox/

A liquid-mercury effect: separate blobs stretch, detach and fuse back together like a single gooey mass as the box fills. Achieved with the classic blur + contrast filter trick — no SVG filters, no JS.
## HTML
```html
<section class="cb-21" aria-label="Gooey blob checkboxes">
  <div class="cb-21__panel">
    <label class="cb-21__row"><input type="checkbox" class="cb-21__input" checked><span class="cb-21__box" aria-hidden="true"><span class="cb-21__goo"><span class="cb-21__b1"></span><span class="cb-21__b2"></span></span><span class="cb-21__tick"></span></span><span class="cb-21__label">Blend layers</span></label>
    <label class="cb-21__row"><input type="checkbox" class="cb-21__input"><span class="cb-21__box" aria-hidden="true"><span class="cb-21__goo"><span class="cb-21__b1"></span><span class="cb-21__b2"></span></span><span class="cb-21__tick"></span></span><span class="cb-21__label">Merge branches</span></label>
    <label class="cb-21__row"><input type="checkbox" class="cb-21__input"><span class="cb-21__box" aria-hidden="true"><span class="cb-21__goo"><span class="cb-21__b1"></span><span class="cb-21__b2"></span></span><span class="cb-21__tick"></span></span><span class="cb-21__label">Fuse particles</span></label>
  </div>
</section>
```
## CSS
```css
.cb-21,
.cb-21 *,
.cb-21 *::before,
.cb-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-21 ::selection {
  background: oklch(0.62 0.18 20);
  color: #fff;
}

.cb-21 {
  --accent: oklch(0.6 0.19 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #fbf3f1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-21__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #f0ded9;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-21__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-21__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-21__box {
  position: relative;
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 9px;
  border: 2px solid #e6bcb2;
  background: #fff;
  overflow: hidden;
  transition: border-color .25s;
}

.cb-21__goo {
  position: absolute;
  inset: 0;
  filter: blur(4px) contrast(14);
}

.cb-21__b1,
.cb-21__b2 {
  position: absolute;
  border-radius: 50%;
  background: var(--accent);
}

.cb-21__b1 {
  width: 16px;
  height: 16px;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%) scale(0);
  transition: transform .4s cubic-bezier(.3,1.2,.4,1);
}

.cb-21__b2 {
  width: 9px;
  height: 9px;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%) scale(0);
}

.cb-21__tick {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .25s .12s,transform .25s .12s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-21__input:checked ~ .cb-21__box {
  border-color: var(--accent);
}

.cb-21__input:checked ~ .cb-21__box .cb-21__b1 {
  transform: translate(-50%,-50%) scale(2.6);
}

.cb-21__input:checked ~ .cb-21__box .cb-21__b2 {
  animation: cb-21-orbit .55s ease;
}

.cb-21__input:checked ~ .cb-21__box .cb-21__tick {
  opacity: 1;
  transform: scale(1);
}

.cb-21__input:focus-visible ~ .cb-21__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-21__label {
  font-size: 14.5px;
  color: #3a2723;
}

@keyframes cb-21-orbit {
  0% {
    transform: translate(-50%,-50%) scale(0);
  }

  45% {
    transform: translate(30%,-160%) scale(1);
  }

  100% {
    transform: translate(-50%,-50%) scale(2);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-21__b1,
    .cb-21__tick {
    transition: none;
  }

  .cb-21__input:checked ~ .cb-21__box .cb-21__b2 {
    animation: none;
    transform: translate(-50%,-50%) scale(2);
  }
}
```

## JavaScript
```js
/* No JavaScript — blur()+contrast() fuses the blobs; transforms drive the merge. */
```
