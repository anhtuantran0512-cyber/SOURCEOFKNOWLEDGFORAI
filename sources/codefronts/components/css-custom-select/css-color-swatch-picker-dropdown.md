---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-color-swatch-picker-dropdown/"
title: "CSS Color Swatch Picker Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A color picker dropdown where each option leads with a real colored swatch circle, shows the color name and hex, and previews the chosen color as a glowing…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Color Swatch Picker Dropdown
Source: https://codefronts.com/components/css-custom-select/css-color-swatch-picker-dropdown/

A color picker dropdown where each option leads with a real colored swatch circle, shows the color name and hex, and previews the chosen color as a glowing ring on the trigger.
## HTML
```html
<div class="cs-16">
  <span class="cs-16__label">Label color</span>
  <div class="cs-16__field">
    <button type="button" class="cs-16__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="sw cs-16__tsw" style="background:#6366f1" aria-hidden="true"></span>
      <span class="cs-16__tval"><b>Indigo</b><small class="hx">#6366F1</small></span>
      <svg class="cs-16__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-16__panel" role="listbox" tabindex="-1">
      <li class="cs-16__opt is-sel" role="option" aria-selected="true" data-name="Indigo" data-hex="#6366F1"><span class="sw" style="background:#6366f1"></span><span class="nm">Indigo</span><span class="hx">#6366F1</span></li>
      <li class="cs-16__opt" role="option" aria-selected="false" data-name="Rose" data-hex="#F43F5E"><span class="sw" style="background:#f43f5e"></span><span class="nm">Rose</span><span class="hx">#F43F5E</span></li>
      <li class="cs-16__opt" role="option" aria-selected="false" data-name="Emerald" data-hex="#10B981"><span class="sw" style="background:#10b981"></span><span class="nm">Emerald</span><span class="hx">#10B981</span></li>
      <li class="cs-16__opt" role="option" aria-selected="false" data-name="Amber" data-hex="#F59E0B"><span class="sw" style="background:#f59e0b"></span><span class="nm">Amber</span><span class="hx">#F59E0B</span></li>
      <li class="cs-16__opt" role="option" aria-selected="false" data-name="Sky" data-hex="#0EA5E9"><span class="sw" style="background:#0ea5e9"></span><span class="nm">Sky</span><span class="hx">#0EA5E9</span></li>
      <li class="cs-16__opt" role="option" aria-selected="false" data-name="Fuchsia" data-hex="#D946EF"><span class="sw" style="background:#d946ef"></span><span class="nm">Fuchsia</span><span class="hx">#D946EF</span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-16,
.cs-16 *,
.cs-16 *::before,
.cs-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-16 ::selection {
  background: #6366f1;
  color: #fff;
}

.cs-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 80% 0%,#171529,#0a0912);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #e8e7f3;
}

.cs-16__label {
  font-size: 13px;
  font-weight: 600;
  color: #8b89a8;
  width: 300px;
}

.cs-16__field {
  position: relative;
  width: 300px;
}

.cs-16__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #171528;
  border: 1px solid #2a2842;
  border-radius: 14px;
  padding: 12px 15px;
  cursor: pointer;
  color: #e8e7f3;
  transition: border-color .2s,box-shadow .2s;
}

.cs-16__trigger:hover {
  border-color: #3a3860;
}

.cs-16__trigger:focus-visible {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 4px rgba(99,102,241,.22);
}

.sw {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  flex-shrink: 0;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.22);
}

.cs-16__tsw {
  transition: box-shadow .25s;
}

.cs-16__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.3;
  flex: 1;
}

.cs-16__tval b {
  font-size: 14.5px;
}

.cs-16__tval small {
  font-size: 11.5px;
  color: #8b89a8;
  font-family: ui-monospace,Menlo,monospace;
}

.cs-16__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #8b89a8;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-16__trigger[aria-expanded="true"] .cs-16__chev {
  transform: rotate(180deg);
}

.cs-16__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #131126;
  border: 1px solid #2a2842;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.72);
  max-height: 280px;
  overflow-y: auto;
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-16.is-open .cs-16__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-16__opt {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .14s;
}

.cs-16__opt .nm {
  flex: 1;
  font-size: 14px;
}

.cs-16__opt .hx {
  font-size: 11.5px;
  color: #8b89a8;
  font-family: ui-monospace,Menlo,monospace;
}

.cs-16__opt:hover,
.cs-16__opt.is-active {
  background: #1e1b38;
}

.cs-16__opt.is-sel {
  background: #221e40;
}

@media (prefers-reduced-motion: reduce) {
  .cs-16__panel,
    .cs-16__chev,
    .cs-16__tsw {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-16');if(!root)return;
  var trig=root.querySelector('.cs-16__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-16__opt'));
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
(function(){var r=document.querySelector('.cs-16');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;var hex=o.dataset.hex;var sw=r.querySelector('.cs-16__tsw');sw.style.background=hex;sw.style.boxShadow='inset 0 0 0 1px rgba(255,255,255,.22),0 0 14px -1px '+hex;r.querySelector('.cs-16__tval b').textContent=o.dataset.name;r.querySelector('.cs-16__tval .hx').textContent=hex;});})();
```
