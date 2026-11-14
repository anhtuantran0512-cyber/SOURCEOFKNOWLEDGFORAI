---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-country-selector-dropdown-with-flags/"
title: "CSS Country Selector Dropdown With Flags"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "An accessible country picker with pure-CSS SVG-style flag chips, keyboard arrow navigation, and a smooth discrete-property open animation for shipping and…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Country Selector Dropdown With Flags
Source: https://codefronts.com/components/css-custom-select/css-country-selector-dropdown-with-flags/

An accessible country picker with pure-CSS SVG-style flag chips, keyboard arrow navigation, and a smooth discrete-property open animation for shipping and checkout forms.
## HTML
```html
<div class="cs-01">
  <label class="cs-01__label" id="cs-01-lbl">Shipping country</label>
  <div class="cs-01__field">
    <button type="button" class="cs-01__trigger" id="cs-01-trigger" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="cs-01-lbl cs-01-trigger">
      <span class="flag" data-c="us" aria-hidden="true"></span>
      <span class="cs-01__val">United States</span>
      <svg class="cs-01__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-01__panel" id="cs-01-panel" role="listbox" aria-labelledby="cs-01-lbl" tabindex="-1">
      <li class="cs-01__opt is-sel" role="option" aria-selected="true" data-v="United States"><span class="flag" data-c="us" aria-hidden="true"></span>United States<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-01__opt" role="option" aria-selected="false" data-v="United Kingdom"><span class="flag" data-c="uk" aria-hidden="true"></span>United Kingdom<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-01__opt" role="option" aria-selected="false" data-v="Canada"><span class="flag" data-c="ca" aria-hidden="true"></span>Canada<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-01__opt" role="option" aria-selected="false" data-v="Australia"><span class="flag" data-c="au" aria-hidden="true"></span>Australia<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-01__opt" role="option" aria-selected="false" data-v="Germany"><span class="flag" data-c="de" aria-hidden="true"></span>Germany<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-01__opt" role="option" aria-selected="false" data-v="Japan"><span class="flag" data-c="jp" aria-hidden="true"></span>Japan<svg class="cs-01__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-01,
.cs-01 *,
.cs-01 *::before,
.cs-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-01 ::selection {
  background: #6366f1;
  color: #fff;
}

.cs-01 {
  --cs-bg: #0e1120;
  --cs-surface: #171b2e;
  --cs-line: #2a2f4a;
  --cs-text: #e6e8f2;
  --cs-mut: #8b90ad;
  --cs-accent: #6366f1;
  --cs-ring: #818cf8;
  --cs-radius: 14px;
  --cs-dur: .22s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 20% 0%,#151933,#0b0e1a);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 60px 20px;
  color: var(--cs-text);
}

.cs-01__label {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .3px;
  color: var(--cs-mut);
  width: 280px;
}

.cs-01__field {
  position: relative;
  width: 280px;
}

.cs-01__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 11px;
  background: var(--cs-surface);
  border: 1px solid var(--cs-line);
  color: var(--cs-text);
  border-radius: var(--cs-radius);
  padding: 13px 15px;
  font-size: 15px;
  cursor: pointer;
  transition: border-color var(--cs-dur),box-shadow var(--cs-dur);
}

.cs-01__trigger:hover {
  border-color: #3a4066;
}

.cs-01__trigger:focus-visible {
  outline: none;
  border-color: var(--cs-ring);
  box-shadow: 0 0 0 4px rgba(129,140,248,.22);
}

.cs-01__val {
  flex: 1;
  text-align: left;
}

.cs-01__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: var(--cs-mut);
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform var(--cs-dur);
}

.cs-01__trigger[aria-expanded="true"] .cs-01__chev {
  transform: rotate(180deg);
}

.flag {
  width: 24px;
  height: 16px;
  border-radius: 3px;
  flex-shrink: 0;
  box-shadow: 0 0 0 1px rgba(255,255,255,.1);
  background-size: cover;
}

.flag[data-c="us"] {
  background: repeating-linear-gradient(#b22234 0 2px,#fff 2px 4px);
  position: relative;
}

.flag[data-c="us"]::before {
  content: "";
  position: absolute;
  inset: 0 60% 46% 0;
  background: #3c3b6e;
  border-radius: 3px 0 0 0;
}

.flag[data-c="uk"] {
  background: linear-gradient(#012169,#012169);
  position: relative;
  overflow: hidden;
}

.flag[data-c="uk"]::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent 42%,#fff 42% 58%,transparent 58%),linear-gradient(0deg,transparent 38%,#fff 38% 62%,transparent 62%);
}

.flag[data-c="uk"]::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent 45%,#c8102e 45% 55%,transparent 55%),linear-gradient(0deg,transparent 42%,#c8102e 42% 58%,transparent 58%);
}

.flag[data-c="ca"] {
  background: linear-gradient(90deg,#d80621 22%,#fff 22% 78%,#d80621 78%);
  position: relative;
}

.flag[data-c="ca"]::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 5px;
  height: 5px;
  background: #d80621;
  transform: translate(-50%,-50%) rotate(45deg);
}

.flag[data-c="au"] {
  background: #012169;
  position: relative;
}

.flag[data-c="au"]::before {
  content: "";
  position: absolute;
  right: 3px;
  top: 50%;
  width: 3px;
  height: 3px;
  background: #fff;
  border-radius: 50%;
  box-shadow: -4px -3px 0 -1px #fff,4px 2px 0 -1px #fff;
}

.flag[data-c="de"] {
  background: linear-gradient(#000 0 33%,#dd0000 33% 66%,#ffce00 66%);
}

.flag[data-c="jp"] {
  background: #fff;
  position: relative;
}

.flag[data-c="jp"]::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 8px;
  height: 8px;
  background: #bc002d;
  border-radius: 50%;
  transform: translate(-50%,-50%);
}

.cs-01__panel {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: var(--cs-surface);
  border: 1px solid var(--cs-line);
  border-radius: var(--cs-radius);
  padding: 6px;
  box-shadow: 0 24px 50px -12px rgba(0,0,0,.6);
  max-height: 260px;
  overflow-y: auto;
  opacity: 0;
  transform: translateY(-8px) scale(.98);
  pointer-events: none;
  transform-origin: top;
  transition: opacity var(--cs-dur) ease,transform var(--cs-dur) cubic-bezier(.16,1,.3,1);
}

.cs-01.is-open .cs-01__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.cs-01__opt {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 12px;
  border-radius: 9px;
  font-size: 15px;
  cursor: pointer;
  color: var(--cs-text);
  transition: background .14s;
}

.cs-01__opt:hover,
.cs-01__opt.is-active {
  background: #232842;
}

.cs-01__tick {
  width: 17px;
  height: 17px;
  margin-left: auto;
  fill: none;
  stroke: var(--cs-accent);
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .14s;
}

.cs-01__opt.is-sel .cs-01__tick {
  opacity: 1;
}

.cs-01__opt.is-sel {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .cs-01__panel,
    .cs-01__chev,
    .cs-01__trigger {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-01');if(!root)return;
  var trig=root.querySelector('.cs-01__trigger');
  var panel=root.querySelector('.cs-01__panel');
  var opts=[].slice.call(root.querySelectorAll('.cs-01__opt'));
  var val=root.querySelector('.cs-01__val');
  var flag=trig.querySelector('.flag');
  var i=opts.findIndex(function(o){return o.classList.contains('is-sel')});
  if(i<0)i=0;
  function open(){root.classList.add('is-open');trig.setAttribute('aria-expanded','true');mark(i);}
  function close(){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');opts.forEach(function(o){o.classList.remove('is-active')});}
  function mark(n){opts.forEach(function(o,k){o.classList.toggle('is-active',k===n)});if(opts[n])opts[n].scrollIntoView({block:'nearest'});}
  function pick(n){
    opts.forEach(function(o){o.classList.remove('is-sel');o.setAttribute('aria-selected','false')});
    var o=opts[n];o.classList.add('is-sel');o.setAttribute('aria-selected','true');
    val.textContent=o.dataset.v;flag.setAttribute('data-c',o.querySelector('.flag').getAttribute('data-c'));
    i=n;close();trig.focus();
  }
  trig.addEventListener('click',function(){root.classList.contains('is-open')?close():open();});
  opts.forEach(function(o,k){o.addEventListener('click',function(){pick(k);});o.addEventListener('mousemove',function(){mark(k);i=k;});});
  trig.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();if(!root.classList.contains('is-open'))open();}
  });
  root.addEventListener('keydown',function(e){
    if(!root.classList.contains('is-open'))return;
    if(e.key==='ArrowDown'){e.preventDefault();i=(i+1)%opts.length;mark(i);}
    else if(e.key==='ArrowUp'){e.preventDefault();i=(i-1+opts.length)%opts.length;mark(i);}
    else if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(i);}
    else if(e.key==='Escape'){e.preventDefault();close();trig.focus();}
  });
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
```
