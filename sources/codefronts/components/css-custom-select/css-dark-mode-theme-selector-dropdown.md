---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-dark-mode-theme-selector-dropdown/"
title: "CSS Dark Mode Theme Selector Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A Light / Dark / System theme picker with inline sun, moon, and monitor SVG icons and a live preview swatch, wired so the demo container actually re-themes…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dark Mode Theme Selector Dropdown
Source: https://codefronts.com/components/css-custom-select/css-dark-mode-theme-selector-dropdown/

A Light / Dark / System theme picker with inline sun, moon, and monitor SVG icons and a live preview swatch, wired so the demo container actually re-themes on selection.
## HTML
```html
<div class="cs-08" data-theme="dark">
  <span class="cs-08__label">Appearance</span>
  <div class="cs-08__field">
    <button type="button" class="cs-08__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-08__ic" data-i="moon" aria-hidden="true"></span>
      <span class="cs-08__tval">Dark</span>
      <span class="cs-08__prev" aria-hidden="true"></span>
      <svg class="cs-08__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-08__panel" role="listbox" tabindex="-1">
      <li class="cs-08__opt" role="option" aria-selected="false" data-theme="light" data-name="Light"><span class="cs-08__ic" data-i="sun"></span>Light<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-08__opt is-sel" role="option" aria-selected="true" data-theme="dark" data-name="Dark"><span class="cs-08__ic" data-i="moon"></span>Dark<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      <li class="cs-08__opt" role="option" aria-selected="false" data-theme="system" data-name="System"><span class="cs-08__ic" data-i="sys"></span>System<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-08,
.cs-08 *,
.cs-08 *::before,
.cs-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-08[data-theme="dark"] {
  --bg: #0f1117;
  --surf: #1a1d27;
  --line: #2a2f3d;
  --txt: #e8eaf0;
  --mut: #8a90a2;
  --acc: #38bdf8;
  --prev: #0f1117;
}

.cs-08[data-theme="light"] {
  --bg: #eef1f6;
  --surf: #ffffff;
  --line: #e2e7ef;
  --txt: #1a1d27;
  --mut: #6b7280;
  --acc: #0284c7;
  --prev: #ffffff;
}

.cs-08[data-theme="system"] {
  --bg: #12141c;
  --surf: #1a1d27;
  --line: #2a2f3d;
  --txt: #e8eaf0;
  --mut: #8a90a2;
  --acc: #818cf8;
  --prev: linear-gradient(120deg,#0f1117 50%,#eef1f6 50%);
}

.cs-08 ::selection {
  background: var(--acc);
  color: #fff;
}

.cs-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  color: var(--txt);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  transition: background .3s,color .3s;
}

.cs-08__label {
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  width: 280px;
}

.cs-08__field {
  position: relative;
  width: 280px;
}

.cs-08__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 11px;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 13px 15px;
  cursor: pointer;
  color: var(--txt);
  transition: border-color .2s,box-shadow .2s,background .3s;
}

.cs-08__trigger:hover {
  border-color: var(--acc);
}

.cs-08__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px color-mix(in srgb,var(--acc) 22%,transparent);
}

.cs-08__tval {
  flex: 1;
  text-align: left;
  font-size: 15px;
}

.cs-08__prev {
  width: 22px;
  height: 22px;
  border-radius: 6px;
  background: var(--prev);
  box-shadow: inset 0 0 0 1px var(--line);
}

.cs-08__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-08__trigger[aria-expanded="true"] .cs-08__chev {
  transform: rotate(180deg);
}

.cs-08__ic {
  width: 19px;
  height: 19px;
  flex-shrink: 0;
  color: var(--acc);
  position: relative;
  display: inline-block;
}

.cs-08__ic[data-i="sun"] {
  border-radius: 50%;
  box-shadow: inset 0 0 0 2px currentColor;
}

.cs-08__ic[data-i="sun"]::before {
  content: "";
  position: absolute;
  inset: -4px;
  background: conic-gradient(currentColor 0 8%,transparent 8% 25%,currentColor 25% 33%,transparent 33% 50%,currentColor 50% 58%,transparent 58% 75%,currentColor 75% 83%,transparent 83%);
  -webkit-mask: radial-gradient(circle,transparent 55%,#000 56% 70%,transparent 71%);
  mask: radial-gradient(circle,transparent 55%,#000 56% 70%,transparent 71%);
}

.cs-08__ic[data-i="moon"] {
  border-radius: 50%;
  box-shadow: inset -5px 0 0 0 currentColor;
}

.cs-08__ic[data-i="sys"] {
  border: 2px solid currentColor;
  border-radius: 4px;
  height: 15px;
  margin-top: 2px;
}

.cs-08__ic[data-i="sys"]::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -6px;
  width: 9px;
  height: 2px;
  background: currentColor;
  transform: translateX(-50%);
}

.cs-08__panel {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 24px 50px -14px rgba(0,0,0,.5);
  opacity: 0;
  transform: translateY(-8px) scale(.98);
  transform-origin: top;
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-08.is-open .cs-08__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.cs-08__opt {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 10px;
  font-size: 15px;
  cursor: pointer;
  color: var(--txt);
  transition: background .14s;
}

.cs-08__opt:hover,
.cs-08__opt.is-active {
  background: color-mix(in srgb,var(--acc) 12%,transparent);
}

.cs-08__opt .ck {
  width: 17px;
  height: 17px;
  margin-left: auto;
  fill: none;
  stroke: var(--acc);
  stroke-width: 2.5;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .14s;
}

.cs-08__opt.is-sel .ck {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cs-08,
    .cs-08__panel,
    .cs-08__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-08');if(!root)return;
  var trig=root.querySelector('.cs-08__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-08__opt'));
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
(function(){var r=document.querySelector('.cs-08');if(!r)return;
 var mq=window.matchMedia('(prefers-color-scheme: dark)');var cur='dark';
 function apply(t){cur=t;if(t==='system'){r.setAttribute('data-theme','system');}else{r.setAttribute('data-theme',t);}}
 r.addEventListener('cs:pick',function(e){var o=e.detail.opt;apply(o.dataset.theme);var ti=r.querySelector('.cs-08__trigger .cs-08__ic');ti.setAttribute('data-i',o.querySelector('.cs-08__ic').getAttribute('data-i'));r.querySelector('.cs-08__tval').textContent=o.dataset.name;});
 mq.addEventListener&&mq.addEventListener('change',function(){if(cur==='system')apply('system');});
})();
```
