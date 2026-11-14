---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-currency-picker-dropdown-with-symbols/"
title: "CSS Currency Picker Dropdown With Symbols"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A compact currency selector showing bold symbol badges, ISO codes, and full names in a monospace-aligned layout, with a glowing gradient trigger suited to…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Currency Picker Dropdown With Symbols
Source: https://codefronts.com/components/css-custom-select/css-currency-picker-dropdown-with-symbols/

A compact currency selector showing bold symbol badges, ISO codes, and full names in a monospace-aligned layout, with a glowing gradient trigger suited to fintech checkout UIs.
## HTML
```html
<div class="cs-02">
  <span class="cs-02__label">Pay in currency</span>
  <div class="cs-02__field">
    <button type="button" class="cs-02__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-02__badge sym">$</span>
      <span class="cs-02__tval"><b>USD</b><small>US Dollar</small></span>
      <svg class="cs-02__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-02__panel" role="listbox" tabindex="-1">
      <li class="cs-02__opt is-sel" role="option" aria-selected="true" data-sym="$" data-code="USD" data-name="US Dollar"><span class="sym">$</span><span class="code">USD</span><span class="nm">US Dollar</span></li>
      <li class="cs-02__opt" role="option" aria-selected="false" data-sym="€" data-code="EUR" data-name="Euro"><span class="sym">€</span><span class="code">EUR</span><span class="nm">Euro</span></li>
      <li class="cs-02__opt" role="option" aria-selected="false" data-sym="£" data-code="GBP" data-name="British Pound"><span class="sym">£</span><span class="code">GBP</span><span class="nm">British Pound</span></li>
      <li class="cs-02__opt" role="option" aria-selected="false" data-sym="¥" data-code="JPY" data-name="Japanese Yen"><span class="sym">¥</span><span class="code">JPY</span><span class="nm">Japanese Yen</span></li>
      <li class="cs-02__opt" role="option" aria-selected="false" data-sym="C$" data-code="CAD" data-name="Canadian Dollar"><span class="sym">C$</span><span class="code">CAD</span><span class="nm">Canadian Dollar</span></li>
      <li class="cs-02__opt" role="option" aria-selected="false" data-sym="A$" data-code="AUD" data-name="Australian Dollar"><span class="sym">A$</span><span class="code">AUD</span><span class="nm">Australian Dollar</span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-02,
.cs-02 *,
.cs-02 *::before,
.cs-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-02 ::selection {
  background: #10b981;
  color: #04120c;
}

.cs-02 {
  --sym-size: 34px;
  --glow: #10b981;
  --cs-cols: auto 52px 1fr;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(160deg,#04120c,#071a12 60%,#04140d);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #d7f5e8;
}

.cs-02__label {
  font-size: 13px;
  font-weight: 600;
  color: #5e8b78;
  width: 300px;
  letter-spacing: .3px;
}

.cs-02__field {
  position: relative;
  width: 300px;
}

.cs-02__trigger {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  background: #0a1f16;
  border: none;
  border-radius: 16px;
  padding: 14px 16px;
  cursor: pointer;
  color: #eafff5;
  overflow: hidden;
}

.cs-02__trigger::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 16px;
  padding: 1.5px;
  background: conic-gradient(from 210deg,#10b981,#0891b2,#10b981,#065f46,#10b981);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: .8;
  transition: opacity .25s;
}

.cs-02__trigger:hover::before {
  opacity: 1;
}

.cs-02__trigger:focus-visible {
  outline: none;
}

.cs-02__trigger:focus-visible::before {
  opacity: 1;
  box-shadow: 0 0 22px -4px var(--glow);
}

.cs-02__badge {
  width: var(--sym-size);
  height: var(--sym-size);
  display: grid;
  place-items: center;
  border-radius: 10px;
  background: linear-gradient(140deg,#10b981,#0891b2);
  color: #04120c;
  font-weight: 800;
  font-size: 17px;
  flex-shrink: 0;
}

.cs-02__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.25;
  flex: 1;
}

.cs-02__tval b {
  font-size: 15px;
  letter-spacing: .5px;
}

.cs-02__tval small {
  font-size: 11.5px;
  color: #5e8b78;
}

.cs-02__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #5e8b78;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .25s;
}

.cs-02__trigger[aria-expanded="true"] .cs-02__chev {
  transform: rotate(180deg);
}

.cs-02__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #0a1f16;
  border: 1px solid #163a2a;
  border-radius: 16px;
  padding: 7px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  clip-path: inset(0 0 100% 0);
  opacity: 0;
  pointer-events: none;
  transition: clip-path .28s cubic-bezier(.16,1,.3,1),opacity .2s;
}

.cs-02.is-open .cs-02__panel {
  clip-path: inset(0 0 0 0);
  opacity: 1;
  pointer-events: auto;
}

.cs-02__opt {
  display: grid;
  grid-template-columns: var(--cs-cols);
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 11px;
  cursor: pointer;
  transition: background .14s;
}

.cs-02__opt .sym {
  width: var(--sym-size);
  height: var(--sym-size);
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: #0f2c20;
  color: #4ade80;
  font-weight: 800;
  font-size: 16px;
}

.cs-02__opt .code {
  font-family: ui-monospace,'SF Mono',Menlo,monospace;
  font-size: 13.5px;
  font-weight: 700;
  color: #eafff5;
  letter-spacing: .5px;
}

.cs-02__opt .nm {
  font-size: 13px;
  color: #7fae9b;
}

.cs-02__opt:hover,
.cs-02__opt.is-active {
  background: #123227;
}

.cs-02__opt.is-sel .sym {
  background: linear-gradient(140deg,#10b981,#0891b2);
  color: #04120c;
}

@media (prefers-reduced-motion: reduce) {
  .cs-02__panel,
    .cs-02__chev {
    transition: opacity .15s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-02');if(!root)return;
  var trig=root.querySelector('.cs-02__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-02__opt'));
  var i=opts.findIndex(function(o){return o.classList.contains('is-sel')});if(i<0)i=0;
  function open(){root.classList.add('is-open');trig.setAttribute('aria-expanded','true');mark(i);}
  function close(){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');opts.forEach(function(o){o.classList.remove('is-active')});}
  function mark(n){opts.forEach(function(o,k){o.classList.toggle('is-active',k===n)});if(opts[n])opts[n].scrollIntoView({block:'nearest'});}
  function pick(n){opts.forEach(function(o){o.classList.remove('is-sel');o.setAttribute('aria-selected','false')});var o=opts[n];o.classList.add('is-sel');o.setAttribute('aria-selected','true');root.dispatchEvent(new CustomEvent('cs:pick',{detail:{opt:o}}));i=n;close();trig.focus();}
  trig.addEventListener('click',function(){root.classList.contains('is-open')?close():open();});
  opts.forEach(function(o,k){o.addEventListener('click',function(){pick(k);});o.addEventListener('mousemove',function(){mark(k);i=k;});});
  trig.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();if(!root.classList.contains('is-open'))open();}});
  root.addEventListener('keydown',function(e){if(!root.classList.contains('is-open'))return;if(e.key==='ArrowDown'){e.preventDefault();i=(i+1)%opts.length;mark(i);}else if(e.key==='ArrowUp'){e.preventDefault();i=(i-1+opts.length)%opts.length;mark(i);}else if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(i);}else if(e.key==='Escape'){e.preventDefault();close();trig.focus();}});
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
(function(){var r=document.querySelector('.cs-02');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;r.querySelector('.cs-02__badge').textContent=o.dataset.sym;r.querySelector('.cs-02__tval b').textContent=o.dataset.code;r.querySelector('.cs-02__tval small').textContent=o.dataset.name;});})();
```
