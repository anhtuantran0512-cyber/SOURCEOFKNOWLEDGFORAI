---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-tailwind-style-utility-first-select-dropdown/"
title: "CSS Tailwind Style Utility First Select Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A clean utility-first select mimicking Tailwind's aesthetic — subtle ring focus, rounded-lg surfaces, gray-scale palette, and an indigo accent — ready to…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Tailwind Style Utility First Select Dropdown
Source: https://codefronts.com/components/css-custom-select/css-tailwind-style-utility-first-select-dropdown/

A clean utility-first select mimicking Tailwind's aesthetic — subtle ring focus, rounded-lg surfaces, gray-scale palette, and an indigo accent — ready to translate to utility classes.
## HTML
```html
<div class="cs-17">
  <span class="cs-17__label">Team</span>
  <div class="cs-17__field">
    <button type="button" class="cs-17__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-17__tval">Engineering</span>
      <svg class="cs-17__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-17__panel" role="listbox" tabindex="-1">
      <li class="cs-17__opt is-sel" role="option" aria-selected="true" data-name="Engineering">Engineering<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-17__opt" role="option" aria-selected="false" data-name="Design">Design<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-17__opt" role="option" aria-selected="false" data-name="Marketing">Marketing<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-17__opt" role="option" aria-selected="false" data-name="Sales">Sales<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-17__opt" role="option" aria-selected="false" data-name="Support">Support<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-17,
.cs-17 *,
.cs-17 *::before,
.cs-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-17 ::selection {
  background: #6366f1;
  color: #fff;
}

.cs-17 {
  --acc: #6366f1;
  --r: 8px;
  font-family: ui-sans-serif,system-ui,'Segoe UI',sans-serif;
  background: #f9fafb;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 60px 20px;
  color: #111827;
}

.cs-17__label {
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  width: 288px;
}

.cs-17__field {
  position: relative;
  width: 288px;
}

.cs-17__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  background: #fff;
  border: 1px solid #d1d5db;
  border-radius: var(--r);
  padding: 9px 13px;
  cursor: pointer;
  color: #111827;
  font-size: 14px;
  box-shadow: 0 1px 2px rgba(0,0,0,.05);
  transition: box-shadow .15s,border-color .15s;
}

.cs-17__trigger:hover {
  border-color: #9ca3af;
}

.cs-17__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 3px rgba(99,102,241,.4);
}

.cs-17__tval {
  flex: 1;
  text-align: left;
}

.cs-17__chev {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #6b7280;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .18s;
}

.cs-17__trigger[aria-expanded="true"] .cs-17__chev {
  transform: rotate(180deg);
}

.cs-17__panel {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: var(--r);
  padding: 5px;
  box-shadow: 0 10px 25px -5px rgba(0,0,0,.12),0 8px 10px -6px rgba(0,0,0,.08);
  opacity: 0;
  transform: translateY(-6px);
  pointer-events: none;
  transition: opacity .15s,transform .18s ease;
}

.cs-17.is-open .cs-17__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-17__opt {
  display: flex;
  align-items: center;
  padding: 8px 11px;
  border-radius: 6px;
  font-size: 14px;
  color: #374151;
  cursor: pointer;
  transition: background .12s,color .12s;
}

.cs-17__opt:hover,
.cs-17__opt.is-active {
  background: #eef2ff;
  color: #4338ca;
}

.cs-17__opt .ck {
  width: 16px;
  height: 16px;
  margin-left: auto;
  fill: none;
  stroke: var(--acc);
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .12s;
}

.cs-17__opt.is-sel {
  color: #4338ca;
  font-weight: 500;
}

.cs-17__opt.is-sel .ck {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cs-17__panel,
    .cs-17__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-17');if(!root)return;
  var trig=root.querySelector('.cs-17__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-17__opt'));
  var i=opts.findIndex(function(o){return o.classList.contains('is-sel')});if(i<0)i=0;
  function open(){root.classList.add('is-open');trig.setAttribute('aria-expanded','true');mark(i);}
  function close(){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');opts.forEach(function(o){o.classList.remove('is-active')});}
  function mark(n){opts.forEach(function(o,k){o.classList.toggle('is-active',k===n)});if(opts[n])opts[n].scrollIntoView({block:'nearest'});}
  function pick(n){opts.forEach(function(o){o.classList.remove('is-sel');o.setAttribute('aria-selected','false')});var o=opts[n];o.classList.add('is-sel');o.setAttribute('aria-selected','true');root.dispatchEvent(new CustomEvent('cs:pick',{detail:{opt:o,index:n}}));i=n;close();trig.focus();}
  trig.addEventListener('click',function(){root.classList.contains('is-open')?close():open();});
  opts.forEach(function(o,k){o.addEventListener('click',function(){pick(k);});o.addEventListener('mousemove',function(){mark(k);i=k;});});
  trig.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();if(!root.classList.contains('is-open'))open();}});
  root.addEventListener('keydown',function(e){if(!root.classList.contains('is-open'))return;if(e.key==='ArrowDown'){e.preventDefault();i=(i+1)%opts.length;mark(i);}else if(e.key==='ArrowUp'){e.preventDefault();i=(i-1+opts.length)%opts.length;mark(i);}else if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(i);}else if(e.key==='Escape'){e.preventDefault();close();trig.focus();}});
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
(function(){var r=document.querySelector('.cs-17');if(!r)return;r.addEventListener('cs:pick',function(e){r.querySelector('.cs-17__tval').textContent=e.detail.opt.dataset.name;});})();
```
