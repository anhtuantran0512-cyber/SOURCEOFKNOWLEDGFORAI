---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-date-range-time-period-picker-dropdown/"
title: "CSS Date Range Time Period Picker Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "An analytics date-range dropdown with quick presets (Last 7 Days, Month to Date, Custom Range), each showing its resolved date span as muted subtext and a…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Date Range Time Period Picker Dropdown
Source: https://codefronts.com/components/css-custom-select/css-date-range-time-period-picker-dropdown/

An analytics date-range dropdown with quick presets (Last 7 Days, Month to Date, Custom Range), each showing its resolved date span as muted subtext and a calendar-icon trigger.
## HTML
```html
<div class="cs-11">
  <span class="cs-11__label">Date range</span>
  <div class="cs-11__field">
    <button type="button" class="cs-11__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-11__cal" aria-hidden="true"></span>
      <span class="cs-11__tval"><b>Last 7 Days</b><small class="cs-11__span"></small></span>
      <svg class="cs-11__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-11__panel" role="listbox" tabindex="-1">
      <li class="cs-11__opt is-sel" role="option" aria-selected="true" data-k="7d" data-name="Last 7 Days"><span class="col"><b>Last 7 Days</b><small class="sp"></small></span></li>
      <li class="cs-11__opt" role="option" aria-selected="false" data-k="30d" data-name="Last 30 Days"><span class="col"><b>Last 30 Days</b><small class="sp"></small></span></li>
      <li class="cs-11__opt" role="option" aria-selected="false" data-k="mtd" data-name="Month to Date"><span class="col"><b>Month to Date</b><small class="sp"></small></span></li>
      <li class="cs-11__opt" role="option" aria-selected="false" data-k="ytd" data-name="Year to Date"><span class="col"><b>Year to Date</b><small class="sp"></small></span></li>
      <li class="cs-11__opt cs-11__custom" role="option" aria-selected="false" data-k="custom" data-name="Custom Range"><span class="col"><b>Custom Range</b><small>Pick specific dates</small></span><svg viewBox="0 0 24 24" class="arw"><path d="M9 6l6 6-6 6"/></svg></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-11,
.cs-11 *,
.cs-11 *::before,
.cs-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-11 ::selection {
  background: #f472b6;
  color: #2a0619;
}

.cs-11 {
  --acc: #f472b6;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(150deg,#1a0f1a,#12091a 60%,#180d1e);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #f3e6f0;
}

.cs-11__label {
  font-size: 13px;
  font-weight: 600;
  color: #b088a3;
  width: 300px;
}

.cs-11__field {
  position: relative;
  width: 300px;
}

.cs-11__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #1e1222;
  border: 1px solid #3a2440;
  border-radius: 14px;
  padding: 12px 15px;
  cursor: pointer;
  color: #f3e6f0;
  transition: border-color .2s,box-shadow .2s;
}

.cs-11__trigger:hover {
  border-color: #54324e;
}

.cs-11__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(244,114,182,.2);
}

.cs-11__cal {
  width: 20px;
  height: 20px;
  border: 2px solid #c586b3;
  border-radius: 5px;
  position: relative;
  flex-shrink: 0;
  margin-top: 2px;
}

.cs-11__cal::before {
  content: "";
  position: absolute;
  left: -2px;
  right: -2px;
  top: -2px;
  height: 6px;
  background: #c586b3;
  border-radius: 5px 5px 0 0;
}

.cs-11__cal::after {
  content: "";
  position: absolute;
  left: 3px;
  right: 3px;
  top: 8px;
  height: 2px;
  background: #c586b3;
  box-shadow: 0 4px 0 #c586b3;
}

.cs-11__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.3;
  flex: 1;
}

.cs-11__tval b {
  font-size: 14.5px;
}

.cs-11__tval small {
  font-size: 11.5px;
  color: #b088a3;
}

.cs-11__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #b088a3;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-11__trigger[aria-expanded="true"] .cs-11__chev {
  transform: rotate(180deg);
}

.cs-11__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #1a0f1e;
  border: 1px solid #3a2440;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.72);
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-11.is-open .cs-11__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-11__opt {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .14s;
}

.cs-11__opt .col {
  display: flex;
  flex-direction: column;
  flex: 1;
  line-height: 1.3;
}

.cs-11__opt .col b {
  font-size: 14px;
}

.cs-11__opt .col small {
  font-size: 11.5px;
  color: #b088a3;
}

.cs-11__opt:hover,
.cs-11__opt.is-active {
  background: #2a1730;
}

.cs-11__opt.is-sel .col b {
  color: var(--acc);
}

.cs-11__custom {
  margin-top: 4px;
  border-top: 1px solid #33203a;
  padding-top: 12px;
  border-radius: 0 0 10px 10px;
}

.cs-11__custom .arw {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #b088a3;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

@media (prefers-reduced-motion: reduce) {
  .cs-11__panel,
    .cs-11__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-11');if(!root)return;
  var trig=root.querySelector('.cs-11__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-11__opt'));
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
(function(){var r=document.querySelector('.cs-11');if(!r)return;
 var fmt=function(d){return d.toLocaleDateString('en-US',{month:'short',day:'numeric'});};
 var now=new Date();
 function span(k){
   var end=new Date(now),start=new Date(now);
   if(k==='7d'){start.setDate(end.getDate()-6);}
   else if(k==='30d'){start.setDate(end.getDate()-29);}
   else if(k==='mtd'){start=new Date(now.getFullYear(),now.getMonth(),1);}
   else if(k==='ytd'){start=new Date(now.getFullYear(),0,1);}
   else return '';
   return fmt(start)+' – '+fmt(end);
 }
 [].forEach.call(r.querySelectorAll('.cs-11__opt'),function(o){var sp=o.querySelector('.sp');if(sp)sp.textContent=span(o.dataset.k);});
 r.querySelector('.cs-11__span').textContent=span('7d');
 r.addEventListener('cs:pick',function(e){var o=e.detail.opt;r.querySelector('.cs-11__tval b').textContent=o.dataset.name;r.querySelector('.cs-11__span').textContent=o.dataset.k==='custom'?'Pick specific dates':span(o.dataset.k);});
})();
```
