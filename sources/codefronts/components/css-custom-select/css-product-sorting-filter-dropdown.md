---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-product-sorting-filter-dropdown/"
title: "CSS Product Sorting Filter Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A retail sort dropdown (Featured, Price low→high, Newest, Rating) with directional arrow icons and an animated active-state underline that slides beneath the…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Product Sorting Filter Dropdown
Source: https://codefronts.com/components/css-custom-select/css-product-sorting-filter-dropdown/

A retail sort dropdown (Featured, Price low→high, Newest, Rating) with directional arrow icons and an animated active-state underline that slides beneath the current option.
## HTML
```html
<div class="cs-12">
  <div class="cs-12__wrap">
    <span class="cs-12__count">248 products</span>
    <div class="cs-12__field">
      <span class="cs-12__pre">Sort:</span>
      <button type="button" class="cs-12__trigger" aria-haspopup="listbox" aria-expanded="false">
        <span class="cs-12__tval">Featured</span>
        <svg class="cs-12__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul class="cs-12__panel" role="listbox" tabindex="-1">
        <span class="cs-12__under" aria-hidden="true"></span>
        <li class="cs-12__opt is-sel" role="option" aria-selected="true" data-name="Featured"><svg viewBox="0 0 24 24" class="i"><path d="M12 3l2.5 6H21l-5 4 2 7-6-4-6 4 2-7-5-4h6.5z"/></svg>Featured</li>
        <li class="cs-12__opt" role="option" aria-selected="false" data-name="Price: Low to High"><svg viewBox="0 0 24 24" class="i"><path d="M12 5v14M6 13l6 6 6-6"/></svg>Price: Low to High</li>
        <li class="cs-12__opt" role="option" aria-selected="false" data-name="Price: High to Low"><svg viewBox="0 0 24 24" class="i"><path d="M12 19V5M6 11l6-6 6 6"/></svg>Price: High to Low</li>
        <li class="cs-12__opt" role="option" aria-selected="false" data-name="Newest Arrivals"><svg viewBox="0 0 24 24" class="i"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>Newest Arrivals</li>
        <li class="cs-12__opt" role="option" aria-selected="false" data-name="Top Rated"><svg viewBox="0 0 24 24" class="i"><path d="M12 3l2.5 6H21l-5 4 2 7-6-4-6 4 2-7-5-4h6.5z"/></svg>Top Rated</li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.cs-12,
.cs-12 *,
.cs-12 *::before,
.cs-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-12 ::selection {
  background: #ec4899;
  color: #fff;
}

.cs-12 {
  --acc: #ec4899;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(180deg,#fdf2f8,#faf5ff);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #1f2937;
}

.cs-12__wrap {
  width: 420px;
  max-width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  border: 1px solid #f3e0ee;
  border-radius: 16px;
  padding: 14px 18px;
  box-shadow: 0 12px 30px -14px rgba(236,72,153,.25);
}

.cs-12__count {
  font-size: 13.5px;
  font-weight: 600;
  color: #9ca3af;
}

.cs-12__field {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cs-12__pre {
  font-size: 13.5px;
  color: #9ca3af;
  font-weight: 600;
}

.cs-12__trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #fdf2f8;
  border: 1px solid #f7d6ea;
  border-radius: 11px;
  padding: 9px 13px;
  cursor: pointer;
  color: #1f2937;
  font-size: 14px;
  font-weight: 600;
  transition: border-color .2s,box-shadow .2s;
}

.cs-12__trigger:hover {
  border-color: #f0abcc;
}

.cs-12__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(236,72,153,.16);
}

.cs-12__chev {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #c77ba0;
  stroke-width: 2.3;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-12__trigger[aria-expanded="true"] .cs-12__chev {
  transform: rotate(180deg);
}

.cs-12__panel {
  position: absolute;
  top: calc(100% + 9px);
  right: 0;
  width: 230px;
  z-index: 20;
  list-style: none;
  background: #fff;
  border: 1px solid #f3e0ee;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 24px 48px -16px rgba(236,72,153,.35);
  opacity: 0;
  transform: translateY(-8px) scale(.98);
  transform-origin: top right;
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-12.is-open .cs-12__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.cs-12__under {
  position: absolute;
  left: 6px;
  right: 6px;
  top: 6px;
  height: 40px;
  border-radius: 10px;
  background: linear-gradient(90deg,rgba(236,72,153,.12),rgba(168,85,247,.1));
  box-shadow: inset 0 0 0 1px rgba(236,72,153,.25);
  transition: transform .28s cubic-bezier(.34,1.4,.64,1),opacity .2s;
  opacity: 0;
  pointer-events: none;
}

.cs-12.is-open .cs-12__under {
  opacity: 1;
}

.cs-12__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  height: 40px;
  padding: 0 11px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 600;
  color: #374151;
  cursor: pointer;
}

.cs-12__opt .i {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: .7;
}

.cs-12__opt.is-sel {
  color: var(--acc);
}

.cs-12__opt.is-sel .i {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cs-12__panel,
    .cs-12__chev,
    .cs-12__under {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-12');if(!root)return;
  var trig=root.querySelector('.cs-12__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-12__opt'));
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
(function(){var r=document.querySelector('.cs-12');if(!r)return;
 var under=r.querySelector('.cs-12__under');var opts=[].slice.call(r.querySelectorAll('.cs-12__opt'));
 function move(n){under.style.transform='translateY('+(n*40)+'px)';}
 function selIdx(){var n=opts.findIndex(function(o){return o.classList.contains('is-sel')});return n<0?0:n;}
 opts.forEach(function(o,k){o.addEventListener('mousemove',function(){move(k);});});
 r.querySelector('.cs-12__panel').addEventListener('mouseleave',function(){move(selIdx());});
 r.querySelector('.cs-12__trigger').addEventListener('click',function(){requestAnimationFrame(function(){move(selIdx());});});
 r.addEventListener('cs:pick',function(e){r.querySelector('.cs-12__tval').textContent=e.detail.opt.dataset.name;move(selIdx());});
})();
```
