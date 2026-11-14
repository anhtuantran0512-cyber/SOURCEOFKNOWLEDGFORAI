---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-status-filter-badge-dropdown-select/"
title: "CSS Status Filter Badge Dropdown Select"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A task-status filter where each option is a colored pill — amber In Progress, green Completed, gray Backlog — with a matching dot, mirrored into the trigger…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Status Filter Badge Dropdown Select
Source: https://codefronts.com/components/css-custom-select/css-status-filter-badge-dropdown-select/

A task-status filter where each option is a colored pill — amber In Progress, green Completed, gray Backlog — with a matching dot, mirrored into the trigger on select.
## HTML
```html
<div class="cs-10">
  <span class="cs-10__label">Task status</span>
  <div class="cs-10__field">
    <button type="button" class="cs-10__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-10__tpill pill" data-s="progress"><span class="dot"></span>In Progress</span>
      <svg class="cs-10__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-10__panel" role="listbox" tabindex="-1">
      <li class="cs-10__opt is-sel" role="option" aria-selected="true" data-s="progress" data-name="In Progress"><span class="pill" data-s="progress"><span class="dot"></span>In Progress</span></li>
      <li class="cs-10__opt" role="option" aria-selected="false" data-s="review" data-name="In Review"><span class="pill" data-s="review"><span class="dot"></span>In Review</span></li>
      <li class="cs-10__opt" role="option" aria-selected="false" data-s="done" data-name="Completed"><span class="pill" data-s="done"><span class="dot"></span>Completed</span></li>
      <li class="cs-10__opt" role="option" aria-selected="false" data-s="blocked" data-name="Blocked"><span class="pill" data-s="blocked"><span class="dot"></span>Blocked</span></li>
      <li class="cs-10__opt" role="option" aria-selected="false" data-s="backlog" data-name="Backlog"><span class="pill" data-s="backlog"><span class="dot"></span>Backlog</span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-10,
.cs-10 *,
.cs-10 *::before,
.cs-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-10 ::selection {
  background: #f59e0b;
  color: #1a1200;
}

.cs-10 {
  --pill-r: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 90% 0%,#141726,#0b0d16);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #e6e8f2;
}

.cs-10__label {
  font-size: 13px;
  font-weight: 600;
  color: #868ca6;
  width: 290px;
}

.cs-10__field {
  position: relative;
  width: 290px;
}

.cs-10__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 11px;
  background: #171a2a;
  border: 1px solid #282d42;
  border-radius: 14px;
  padding: 12px 14px;
  cursor: pointer;
  color: #e6e8f2;
  transition: border-color .2s,box-shadow .2s;
}

.cs-10__trigger:hover {
  border-color: #39405e;
}

.cs-10__trigger:focus-visible {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 4px rgba(99,102,241,.22);
}

.cs-10__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #868ca6;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  margin-left: auto;
  transition: transform .2s;
}

.cs-10__trigger[aria-expanded="true"] .cs-10__chev {
  transform: rotate(180deg);
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border-radius: var(--pill-r);
  padding: 5px 13px;
  font-size: 13px;
  font-weight: 600;
  background: var(--bg,#1e2233);
  color: var(--fg,#c7ccdb);
  border: 1px solid color-mix(in srgb,var(--fg,#c7ccdb) 25%,transparent);
}

.dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--fg,#c7ccdb);
  box-shadow: 0 0 8px -1px var(--fg,#c7ccdb);
}

.pill[data-s="progress"],
[data-s="progress"] {
  --bg: rgba(245,158,11,.14);
  --fg: #fbbf24;
}

.pill[data-s="review"],
[data-s="review"] {
  --bg: rgba(99,102,241,.14);
  --fg: #a5b4fc;
}

.pill[data-s="done"],
[data-s="done"] {
  --bg: rgba(16,185,129,.14);
  --fg: #34d399;
}

.pill[data-s="blocked"],
[data-s="blocked"] {
  --bg: rgba(244,63,94,.14);
  --fg: #fb7185;
}

.pill[data-s="backlog"],
[data-s="backlog"] {
  --bg: rgba(148,163,184,.13);
  --fg: #cbd5e1;
}

.cs-10__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #161927;
  border: 1px solid #282d42;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-10.is-open .cs-10__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-10__opt {
  display: flex;
  align-items: center;
  padding: 9px 10px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .14s;
}

.cs-10__opt:hover,
.cs-10__opt.is-active {
  background: #20263a;
}

.cs-10__opt.is-sel {
  background: #232a40;
}

@media (prefers-reduced-motion: reduce) {
  .cs-10__panel,
    .cs-10__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-10');if(!root)return;
  var trig=root.querySelector('.cs-10__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-10__opt'));
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
(function(){var r=document.querySelector('.cs-10');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;var tp=r.querySelector('.cs-10__tpill');tp.setAttribute('data-s',o.dataset.s);tp.innerHTML='<span class="dot"></span>'+o.dataset.name;});})();
```
