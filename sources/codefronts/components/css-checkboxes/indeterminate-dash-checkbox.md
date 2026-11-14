---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/indeterminate-dash-checkbox/"
title: "Indeterminate Dash Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "The parent/child select-all pattern from every data table and file tree: the master box shows a dash when only some children are ticked, a check when all…"
has_js: "true"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Indeterminate Dash Checkbox
Source: https://codefronts.com/components/css-checkboxes/indeterminate-dash-checkbox/

The parent/child select-all pattern from every data table and file tree: the master box shows a dash when only some children are ticked, a check when all are, and empties when none are. The dash state can only be set via the DOM property — the one place a checkbox genuinely needs a line of JS.
## HTML
```html
<section class="cb-05" id="cb-05" aria-label="Select all with indeterminate state">
  <div class="cb-05__card">
    <label class="cb-05__row cb-05__row--master">
      <input type="checkbox" class="cb-05__input" data-master aria-checked="mixed">
      <span class="cb-05__box" aria-hidden="true"></span>
      <span class="cb-05__label">Select all recipients</span>
    </label>
    <div class="cb-05__children">
      <label class="cb-05__row"><input type="checkbox" class="cb-05__input" data-child checked><span class="cb-05__box" aria-hidden="true"></span><span class="cb-05__label">[email protected]</span></label>
      <label class="cb-05__row"><input type="checkbox" class="cb-05__input" data-child><span class="cb-05__box" aria-hidden="true"></span><span class="cb-05__label">[email protected]</span></label>
      <label class="cb-05__row"><input type="checkbox" class="cb-05__input" data-child checked><span class="cb-05__box" aria-hidden="true"></span><span class="cb-05__label">[email protected]</span></label>
      <label class="cb-05__row"><input type="checkbox" class="cb-05__input" data-child><span class="cb-05__box" aria-hidden="true"></span><span class="cb-05__label">[email protected]</span></label>
    </div>
  </div>
</section>
```
## CSS
```css
.cb-05,
.cb-05 *,
.cb-05 *::before,
.cb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-05 ::selection {
  background: oklch(0.62 0.16 250);
  color: #fff;
}

.cb-05 {
  --accent: oklch(0.62 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-05__card {
  width: min(420px,100%);
  background: #fff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
  padding: 10px 8px;
  box-shadow: 0 18px 40px -30px rgba(16,24,40,.5);
}

.cb-05__row {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 11px 14px;
  border-radius: 9px;
}

.cb-05__row:hover {
  background: #f6f7f9;
}

.cb-05__row--master {
  border-bottom: 1px solid #eef0f3;
  border-radius: 9px 9px 0 0;
  font-weight: 600;
}

.cb-05__children {
  padding-left: 20px;
}

.cb-05__input {
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

.cb-05__box {
  position: relative;
  flex: none;
  width: 22px;
  height: 22px;
  border-radius: 6px;
  border: 2px solid #c3c8d1;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-05__box::before,
.cb-05__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transition: opacity .18s;
}

.cb-05__box::before {
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-05__box::after {
  -webkit-mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E");
  mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E");
}

.cb-05__input:checked ~ .cb-05__box,
.cb-05__input:indeterminate ~ .cb-05__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-05__input:checked ~ .cb-05__box::before {
  opacity: 1;
}

.cb-05__input:indeterminate ~ .cb-05__box::after {
  opacity: 1;
}

.cb-05__input:focus-visible ~ .cb-05__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-05__label {
  font-size: 14px;
  color: #2a2f3a;
}

@media (prefers-reduced-motion: reduce) {
  .cb-05__box,
    .cb-05__box::before,
    .cb-05__box::after {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('cb-05');
  if(!root) return;
  var master = root.querySelector('[data-master]');
  var kids = [].slice.call(root.querySelectorAll('[data-child]'));
  function syncMaster(){
    var on = kids.filter(function(k){return k.checked;}).length;
    master.checked = on === kids.length;
    master.indeterminate = on > 0 && on < kids.length;
    master.setAttribute('aria-checked', master.indeterminate ? 'mixed' : String(master.checked));
  }
  master.addEventListener('change', function(){
    kids.forEach(function(k){ k.checked = master.checked; });
    master.indeterminate = false;
    master.setAttribute('aria-checked', String(master.checked));
  });
  kids.forEach(function(k){ k.addEventListener('change', syncMaster); });
  syncMaster();
})();
```
