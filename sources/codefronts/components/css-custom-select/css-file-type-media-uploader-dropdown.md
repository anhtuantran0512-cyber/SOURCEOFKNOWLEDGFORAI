---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-file-type-media-uploader-dropdown/"
title: "CSS File Type Media Uploader Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "An upload-field dropdown listing accepted formats (PDF, CSV, PNG, MP4) each with a colored file-type badge, size limit subtext, and a dashed drop-zone trigger."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS File Type Media Uploader Dropdown
Source: https://codefronts.com/components/css-custom-select/css-file-type-media-uploader-dropdown/

An upload-field dropdown listing accepted formats (PDF, CSV, PNG, MP4) each with a colored file-type badge, size limit subtext, and a dashed drop-zone trigger.
## HTML
```html
<div class="cs-15">
  <span class="cs-15__label">Accepted file type</span>
  <div class="cs-15__field">
    <button type="button" class="cs-15__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-15__up" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg></span>
      <span class="cs-15__tval"><b>PDF documents</b><small>up to 25 MB</small></span>
      <span class="ext" data-x="pdf">PDF</span>
    </button>
    <ul class="cs-15__panel" role="listbox" tabindex="-1">
      <li class="cs-15__opt is-sel" role="option" aria-selected="true" data-x="pdf" data-name="PDF documents" data-sz="up to 25 MB"><span class="ext" data-x="pdf">PDF</span><span class="col"><b>PDF documents</b><small>up to 25 MB</small></span></li>
      <li class="cs-15__opt" role="option" aria-selected="false" data-x="csv" data-name="CSV spreadsheets" data-sz="up to 10 MB"><span class="ext" data-x="csv">CSV</span><span class="col"><b>CSV spreadsheets</b><small>up to 10 MB</small></span></li>
      <li class="cs-15__opt" role="option" aria-selected="false" data-x="png" data-name="PNG images" data-sz="up to 8 MB"><span class="ext" data-x="png">PNG</span><span class="col"><b>PNG images</b><small>up to 8 MB</small></span></li>
      <li class="cs-15__opt" role="option" aria-selected="false" data-x="mp4" data-name="MP4 video" data-sz="up to 200 MB"><span class="ext" data-x="mp4">MP4</span><span class="col"><b>MP4 video</b><small>up to 200 MB</small></span></li>
      <li class="cs-15__opt" role="option" aria-selected="false" data-x="zip" data-name="ZIP archives" data-sz="up to 100 MB"><span class="ext" data-x="zip">ZIP</span><span class="col"><b>ZIP archives</b><small>up to 100 MB</small></span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-15,
.cs-15 *,
.cs-15 *::before,
.cs-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-15 ::selection {
  background: #14b8a6;
  color: #03201c;
}

.cs-15 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(160deg,#0a1a1a,#04120f 60%,#08181a);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #dcf5f0;
}

.cs-15__label {
  font-size: 13px;
  font-weight: 600;
  color: #5f8f88;
  width: 330px;
}

.cs-15__field {
  position: relative;
  width: 330px;
}

.cs-15__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  background: #0b201d;
  border: 2px dashed #1d453e;
  border-radius: 15px;
  padding: 14px 16px;
  cursor: pointer;
  color: #dcf5f0;
  transition: border-color .2s,box-shadow .2s,background .2s;
}

.cs-15__trigger:hover {
  border-color: #2b6157;
  background: #0d2622;
}

.cs-15__trigger:focus-visible {
  outline: none;
  border-color: #14b8a6;
  box-shadow: 0 0 0 4px rgba(20,184,166,.2);
}

.cs-15__up {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(20,184,166,.14);
  display: grid;
  place-items: center;
  flex-shrink: 0;
}

.cs-15__up svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: #2dd4bf;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cs-15__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.3;
  flex: 1;
}

.cs-15__tval b {
  font-size: 14.5px;
}

.cs-15__tval small {
  font-size: 11.5px;
  color: #5f8f88;
}

.ext {
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .5px;
  padding: 5px 9px;
  border-radius: 8px;
  flex-shrink: 0;
}

.ext[data-x="pdf"] {
  background: rgba(239,68,68,.16);
  color: #fca5a5;
}

.ext[data-x="csv"] {
  background: rgba(34,197,94,.16);
  color: #86efac;
}

.ext[data-x="png"] {
  background: rgba(59,130,246,.16);
  color: #93c5fd;
}

.ext[data-x="mp4"] {
  background: rgba(168,85,247,.16);
  color: #d8b4fe;
}

.ext[data-x="zip"] {
  background: rgba(245,158,11,.16);
  color: #fcd34d;
}

.cs-15__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #0a1c1a;
  border: 1px solid #1d453e;
  border-radius: 15px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-15.is-open .cs-15__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-15__opt {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 10px 11px;
  border-radius: 11px;
  cursor: pointer;
  transition: background .14s;
}

.cs-15__opt .col {
  display: flex;
  flex-direction: column;
  line-height: 1.3;
}

.cs-15__opt .col b {
  font-size: 14px;
}

.cs-15__opt .col small {
  font-size: 11.5px;
  color: #5f8f88;
}

.cs-15__opt:hover,
.cs-15__opt.is-active {
  background: #10312c;
}

.cs-15__opt.is-sel {
  background: #123933;
}

@media (prefers-reduced-motion: reduce) {
  .cs-15__panel {
    transition: opacity .14s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-15');if(!root)return;
  var trig=root.querySelector('.cs-15__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-15__opt'));
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
(function(){var r=document.querySelector('.cs-15');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;var ex=r.querySelector('.cs-15__trigger .ext');ex.setAttribute('data-x',o.dataset.x);ex.textContent=o.dataset.x.toUpperCase();r.querySelector('.cs-15__tval b').textContent=o.dataset.name;r.querySelector('.cs-15__tval small').textContent=o.dataset.sz;});})();
```
