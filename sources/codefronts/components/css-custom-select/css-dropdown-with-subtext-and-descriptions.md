---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-dropdown-with-subtext-and-descriptions/"
title: "CSS Dropdown With Subtext And Descriptions"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A rich two-line option dropdown pairing a bold title with a descriptive second line and a leading gradient icon tile, ideal for plan or role pickers that…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dropdown With Subtext And Descriptions
Source: https://codefronts.com/components/css-custom-select/css-dropdown-with-subtext-and-descriptions/

A rich two-line option dropdown pairing a bold title with a descriptive second line and a leading gradient icon tile, ideal for plan or role pickers that need context.
## HTML
```html
<div class="cs-13">
  <span class="cs-13__label">Access role</span>
  <div class="cs-13__field">
    <button type="button" class="cs-13__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="tile" data-g="a" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2l7 4v6c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/></svg></span>
      <span class="cs-13__tval"><b>Administrator</b><small>Full access to all settings</small></span>
      <svg class="cs-13__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-13__panel" role="listbox" tabindex="-1">
      <li class="cs-13__opt is-sel" role="option" aria-selected="true" data-name="Administrator" data-g="a"><span class="tile" data-g="a"><svg viewBox="0 0 24 24"><path d="M12 2l7 4v6c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/></svg></span><span class="col"><b>Administrator</b><small>Full access to all settings and billing</small></span><svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-13__opt" role="option" aria-selected="false" data-name="Editor" data-g="b"><span class="tile" data-g="b"><svg viewBox="0 0 24 24"><path d="M4 20l4-1 10-10-3-3L5 16z"/></svg></span><span class="col"><b>Editor</b><small>Create and edit content, no billing</small></span><svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-13__opt" role="option" aria-selected="false" data-name="Viewer" data-g="c"><span class="tile" data-g="c"><svg viewBox="0 0 24 24"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg></span><span class="col"><b>Viewer</b><small>Read-only access to shared items</small></span><svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-13__opt" role="option" aria-selected="false" data-name="Guest" data-g="d"><span class="tile" data-g="d"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg></span><span class="col"><b>Guest</b><small>Limited, time-boxed access</small></span><svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-13,
.cs-13 *,
.cs-13 *::before,
.cs-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-13 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.cs-13 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 20% 0%,#1c1636,#0d0a1c);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #ece8fb;
}

.cs-13__label {
  font-size: 13px;
  font-weight: 600;
  color: #9990c1;
  width: 340px;
}

.cs-13__field {
  position: relative;
  width: 340px;
}

.cs-13__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  background: #191333;
  border: 1px solid #2f2757;
  border-radius: 15px;
  padding: 12px 15px;
  cursor: pointer;
  color: #ece8fb;
  transition: border-color .2s,box-shadow .2s;
}

.cs-13__trigger:hover {
  border-color: #443b73;
}

.cs-13__trigger:focus-visible {
  outline: none;
  border-color: #8b5cf6;
  box-shadow: 0 0 0 4px rgba(139,92,246,.24);
}

.tile {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  flex-shrink: 0;
}

.tile svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: #fff;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.tile[data-g="a"] {
  background: linear-gradient(140deg,#8b5cf6,#6366f1);
}

.tile[data-g="b"] {
  background: linear-gradient(140deg,#06b6d4,#3b82f6);
}

.tile[data-g="c"] {
  background: linear-gradient(140deg,#10b981,#059669);
}

.tile[data-g="d"] {
  background: linear-gradient(140deg,#f59e0b,#ef4444);
}

.cs-13__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.3;
  flex: 1;
}

.cs-13__tval b {
  font-size: 14.5px;
}

.cs-13__tval small {
  font-size: 11.5px;
  color: #9990c1;
}

.cs-13__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #9990c1;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-13__trigger[aria-expanded="true"] .cs-13__chev {
  transform: rotate(180deg);
}

.cs-13__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #15102e;
  border: 1px solid #2f2757;
  border-radius: 15px;
  padding: 6px;
  box-shadow: 0 28px 56px -14px rgba(0,0,0,.72);
  max-height: 300px;
  overflow-y: auto;
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-13.is-open .cs-13__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-13__opt {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 10px 11px;
  border-radius: 12px;
  cursor: pointer;
  transition: background .14s,box-shadow .14s;
}

.cs-13__opt .col {
  display: flex;
  flex-direction: column;
  flex: 1;
  line-height: 1.3;
}

.cs-13__opt .col b {
  font-size: 14px;
}

.cs-13__opt .col small {
  font-size: 11.5px;
  color: #9990c1;
}

.cs-13__opt:hover,
.cs-13__opt.is-active {
  background: #221a45;
  box-shadow: inset 0 0 0 1px #352b60;
}

.cs-13__opt .ck {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #a78bfa;
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .14s;
}

.cs-13__opt.is-sel .ck {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cs-13__panel,
    .cs-13__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-13');if(!root)return;
  var trig=root.querySelector('.cs-13__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-13__opt'));
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
(function(){var r=document.querySelector('.cs-13');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;var t=r.querySelector('.cs-13__trigger .tile');t.setAttribute('data-g',o.dataset.g);t.innerHTML=o.querySelector('.tile').innerHTML;r.querySelector('.cs-13__tval b').textContent=o.dataset.name;r.querySelector('.cs-13__tval small').textContent=o.querySelector('.col small').textContent;});})();
```
