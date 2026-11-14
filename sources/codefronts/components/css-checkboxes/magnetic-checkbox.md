---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/magnetic-checkbox/"
title: "Magnetic Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A physical, attractive feel: as the cursor approaches, the box leans toward it like a magnet, then snaps back when the pointer leaves."
has_js: "true"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Checkbox
Source: https://codefronts.com/components/css-checkboxes/magnetic-checkbox/

A physical, attractive feel: as the cursor approaches, the box leans toward it like a magnet, then snaps back when the pointer leaves. A tiny bit of pointer math drives a purely transform-based lean — smooth, GPU-friendly and fully optional.
## HTML
```html
<section class="cb-26" id="cb-26" aria-label="Magnetic checkboxes">
  <div class="cb-26__panel">
    <label class="cb-26__row" data-magnet><input type="checkbox" class="cb-26__input" checked><span class="cb-26__box" aria-hidden="true"></span><span class="cb-26__label">Snap to grid</span></label>
    <label class="cb-26__row" data-magnet><input type="checkbox" class="cb-26__input"><span class="cb-26__box" aria-hidden="true"></span><span class="cb-26__label">Magnetic guides</span></label>
    <label class="cb-26__row" data-magnet><input type="checkbox" class="cb-26__input"><span class="cb-26__box" aria-hidden="true"></span><span class="cb-26__label">Auto-align nodes</span></label>
  </div>
</section>
```
## CSS
```css
.cb-26,
.cb-26 *,
.cb-26 *::before,
.cb-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-26 ::selection {
  background: oklch(0.62 0.16 275);
  color: #fff;
}

.cb-26 {
  --accent: oklch(0.56 0.17 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f3f3fa;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-26__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e6e5f2;
  border-radius: 14px;
  padding: 8px 14px;
}

.cb-26__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 16px 10px;
}

.cb-26__input {
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

.cb-26__box {
  --dx: 0px;
  --dy: 0px;
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  border: 2px solid #c2c0d8;
  background: #fff;
  transform: translate(var(--dx),var(--dy));
  transition: transform .3s cubic-bezier(.3,1.2,.4,1),background .2s,border-color .2s;
}

.cb-26__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .2s,transform .2s cubic-bezier(.2,.9,.3,1.2);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-26__input:checked ~ .cb-26__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-26__input:checked ~ .cb-26__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-26__input:focus-visible ~ .cb-26__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-26__label {
  font-size: 14.5px;
  color: #2d2a3d;
}

@media (prefers-reduced-motion: reduce) {
  .cb-26__box {
    transition: background .2s,border-color .2s;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('cb-26');
  if(!root) return;
  if(matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  var MAX = 6; // px of lean
  root.querySelectorAll('[data-magnet]').forEach(function(row){
    var box = row.querySelector('.cb-26__box');
    row.addEventListener('pointermove', function(e){
      var r = box.getBoundingClientRect();
      var cx = r.left + r.width/2, cy = r.top + r.height/2;
      var dx = Math.max(-MAX, Math.min(MAX, (e.clientX - cx) / 3));
      var dy = Math.max(-MAX, Math.min(MAX, (e.clientY - cy) / 3));
      box.style.setProperty('--dx', dx.toFixed(1) + 'px');
      box.style.setProperty('--dy', dy.toFixed(1) + 'px');
    });
    row.addEventListener('pointerleave', function(){
      box.style.setProperty('--dx','0px');
      box.style.setProperty('--dy','0px');
    });
  });
})();
```
