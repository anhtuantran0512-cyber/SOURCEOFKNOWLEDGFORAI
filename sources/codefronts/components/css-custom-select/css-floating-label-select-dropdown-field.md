---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-floating-label-select-dropdown-field/"
title: "CSS Floating Label Select Dropdown Field"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A full-width form select where the label floats up into the border once a value is chosen or the field is focused, matching Material-style text-field behavior."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Label Select Dropdown Field
Source: https://codefronts.com/components/css-custom-select/css-floating-label-select-dropdown-field/

A full-width form select where the label floats up into the border once a value is chosen or the field is focused, matching Material-style text-field behavior.
## HTML
```html
<div class="cs-19">
  <div class="cs-19__field">
    <span class="cs-19__lab" id="cs-19-lab">Country of residence</span>
    <button type="button" class="cs-19__trigger" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="cs-19-lab">
      <span class="cs-19__tval"></span>
      <svg class="cs-19__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-19__panel" role="listbox" aria-labelledby="cs-19-lab" tabindex="-1">
      <li class="cs-19__opt" role="option" aria-selected="false" data-name="United States">United States</li>
      <li class="cs-19__opt" role="option" aria-selected="false" data-name="United Kingdom">United Kingdom</li>
      <li class="cs-19__opt" role="option" aria-selected="false" data-name="Canada">Canada</li>
      <li class="cs-19__opt" role="option" aria-selected="false" data-name="Australia">Australia</li>
      <li class="cs-19__opt" role="option" aria-selected="false" data-name="Netherlands">Netherlands</li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-19,
.cs-19 *,
.cs-19 *::before,
.cs-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-19 ::selection {
  background: #2dd4bf;
  color: #032b26;
}

.cs-19 {
  --acc: #2dd4bf;
  --surf: #101826;
  --line: #2a3446;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(180deg,#0a0f18,#0d1420);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  color: #e6ecf5;
}

.cs-19__field {
  position: relative;
  width: 360px;
  max-width: 100%;
}

.cs-19__lab {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #8090a6;
  font-size: 15px;
  pointer-events: none;
  background: transparent;
  padding: 0 5px;
  transition: transform .2s cubic-bezier(.16,1,.3,1),color .2s,background .2s;
  transform-origin: left center;
}

.cs-19__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  background: var(--surf);
  border: 1.5px solid var(--line);
  border-radius: 12px;
  padding: 16px 15px;
  cursor: pointer;
  color: #e6ecf5;
  font-size: 15px;
  transition: border-color .2s,box-shadow .2s;
}

.cs-19__trigger:hover {
  border-color: #3a4761;
}

.cs-19__field.is-focus .cs-19__trigger,
.cs-19__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(45,212,191,.16);
}

.cs-19__field.has-value .cs-19__lab,
.cs-19__field.is-focus .cs-19__lab {
  transform: translateY(-30px) scale(.82);
  background: var(--surf);
  color: var(--acc);
}

.cs-19__tval {
  flex: 1;
  text-align: left;
}

.cs-19__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #8090a6;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-19__trigger[aria-expanded="true"] .cs-19__chev {
  transform: rotate(180deg);
}

.cs-19__panel {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  opacity: 0;
  transform: translateY(-8px);
  pointer-events: none;
  transition: opacity .18s,transform .2s cubic-bezier(.16,1,.3,1);
}

.cs-19.is-open .cs-19__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-19__opt {
  padding: 12px 13px;
  border-radius: 9px;
  font-size: 14.5px;
  color: #cdd6e5;
  cursor: pointer;
  transition: background .14s,color .14s;
}

.cs-19__opt:hover,
.cs-19__opt.is-active {
  background: #182234;
}

.cs-19__opt.is-sel {
  background: #193530;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cs-19__panel,
    .cs-19__chev,
    .cs-19__lab {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-19');if(!root)return;
  var field=root.querySelector('.cs-19__field');
  var trig=root.querySelector('.cs-19__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-19__opt'));
  var val=root.querySelector('.cs-19__tval');
  var i=-1;
  function open(){root.classList.add('is-open');field.classList.add('is-focus');trig.setAttribute('aria-expanded','true');mark(i<0?0:i);}
  function close(){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');if(!field.classList.contains('has-value'))field.classList.remove('is-focus');else field.classList.remove('is-focus');opts.forEach(function(o){o.classList.remove('is-active')});}
  function mark(n){opts.forEach(function(o,k){o.classList.toggle('is-active',k===n)});if(opts[n])opts[n].scrollIntoView({block:'nearest'});i=n;}
  function pick(n){opts.forEach(function(o){o.classList.remove('is-sel');o.setAttribute('aria-selected','false')});var o=opts[n];o.classList.add('is-sel');o.setAttribute('aria-selected','true');val.textContent=o.dataset.name;field.classList.add('has-value');i=n;close();trig.focus();}
  trig.addEventListener('click',function(){root.classList.contains('is-open')?close():open();});
  trig.addEventListener('focus',function(){field.classList.add('is-focus');});
  trig.addEventListener('blur',function(){if(!root.classList.contains('is-open')&&!field.classList.contains('has-value'))field.classList.remove('is-focus');});
  opts.forEach(function(o,k){o.addEventListener('click',function(){pick(k);});o.addEventListener('mousemove',function(){mark(k);});});
  trig.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();open();}});
  root.addEventListener('keydown',function(e){if(!root.classList.contains('is-open'))return;if(e.key==='ArrowDown'){e.preventDefault();mark((i+1)%opts.length);}else if(e.key==='ArrowUp'){e.preventDefault();mark((i-1+opts.length)%opts.length);}else if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(i<0?0:i);}else if(e.key==='Escape'){e.preventDefault();close();trig.focus();}});
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
```
