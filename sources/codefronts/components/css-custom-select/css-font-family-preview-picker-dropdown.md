---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-font-family-preview-picker-dropdown/"
title: "CSS Font Family Preview Picker Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "An editor-style font picker where each option renders its own label in that font family, with a live preview sentence and a monospace/serif/sans category tag."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Font Family Preview Picker Dropdown
Source: https://codefronts.com/components/css-custom-select/css-font-family-preview-picker-dropdown/

An editor-style font picker where each option renders its own label in that font family, with a live preview sentence and a monospace/serif/sans category tag.
## HTML
```html
<div class="cs-14">
  <span class="cs-14__label">Editor font</span>
  <div class="cs-14__field">
    <button type="button" class="cs-14__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-14__tval">Inter</span>
      <svg class="cs-14__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-14__panel" role="listbox" tabindex="-1">
      <li class="cs-14__opt is-sel" role="option" aria-selected="true" data-ff="system-ui,'Segoe UI',sans-serif" data-name="Inter" style="font-family:system-ui,'Segoe UI',sans-serif"><span class="nm">Inter</span><span class="tag" data-cat="sans">Sans</span></li>
      <li class="cs-14__opt" role="option" aria-selected="false" data-ff="Georgia,'Times New Roman',serif" data-name="Georgia" style="font-family:Georgia,'Times New Roman',serif"><span class="nm">Georgia</span><span class="tag" data-cat="serif">Serif</span></li>
      <li class="cs-14__opt" role="option" aria-selected="false" data-ff="'Courier New',ui-monospace,monospace" data-name="Courier" style="font-family:'Courier New',ui-monospace,monospace"><span class="nm">Courier New</span><span class="tag" data-cat="mono">Mono</span></li>
      <li class="cs-14__opt" role="option" aria-selected="false" data-ff="'Trebuchet MS',sans-serif" data-name="Trebuchet" style="font-family:'Trebuchet MS',sans-serif"><span class="nm">Trebuchet MS</span><span class="tag" data-cat="sans">Sans</span></li>
      <li class="cs-14__opt" role="option" aria-selected="false" data-ff="'Palatino Linotype','Book Antiqua',serif" data-name="Palatino" style="font-family:'Palatino Linotype','Book Antiqua',serif"><span class="nm">Palatino</span><span class="tag" data-cat="serif">Serif</span></li>
      <li class="cs-14__opt" role="option" aria-selected="false" data-ff="'Lucida Console',monospace" data-name="Lucida Console" style="font-family:'Lucida Console',monospace"><span class="nm">Lucida Console</span><span class="tag" data-cat="mono">Mono</span></li>
    </ul>
    <p class="cs-14__sample" style="font-family:system-ui,'Segoe UI',sans-serif">The quick brown fox jumps over the lazy dog.</p>
  </div>
</div>
```
## CSS
```css
.cs-14,
.cs-14 *,
.cs-14 *::before,
.cs-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-14 ::selection {
  background: #2563eb;
  color: #fff;
}

.cs-14 {
  font-family: system-ui,'Segoe UI',sans-serif;
  background: linear-gradient(180deg,#0f172a,#111827);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #e5e9f3;
}

.cs-14__label {
  font-size: 13px;
  font-weight: 600;
  color: #8592ad;
  width: 340px;
}

.cs-14__field {
  position: relative;
  width: 340px;
}

.cs-14__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 11px;
  background: #1a2236;
  border: 1px solid #2b3650;
  border-radius: 14px;
  padding: 13px 15px;
  cursor: pointer;
  color: #e5e9f3;
  transition: border-color .2s,box-shadow .2s;
}

.cs-14__trigger:hover {
  border-color: #3a4869;
}

.cs-14__trigger:focus-visible {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 4px rgba(59,130,246,.22);
}

.cs-14__tval {
  flex: 1;
  text-align: left;
  font-size: 16px;
  font-family: var(--ff,system-ui);
}

.cs-14__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #8592ad;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-14__trigger[aria-expanded="true"] .cs-14__chev {
  transform: rotate(180deg);
}

.cs-14__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #161d30;
  border: 1px solid #2b3650;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  max-height: 280px;
  overflow-y: auto;
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-14.is-open .cs-14__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-14__opt {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 13px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .14s;
}

.cs-14__opt .nm {
  font-size: 16px;
}

.cs-14__opt:hover,
.cs-14__opt.is-active {
  background: #212b44;
}

.cs-14__opt.is-sel {
  background: #25314e;
}

.tag {
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 20px;
  letter-spacing: .3px;
  font-family: system-ui,sans-serif;
}

.tag[data-cat="sans"] {
  background: rgba(59,130,246,.18);
  color: #93c5fd;
}

.tag[data-cat="serif"] {
  background: rgba(168,85,247,.18);
  color: #d8b4fe;
}

.tag[data-cat="mono"] {
  background: rgba(16,185,129,.18);
  color: #6ee7b7;
}

.cs-14__sample {
  margin-top: 14px;
  font-size: 17px;
  line-height: 1.5;
  color: #cbd5e1;
  background: #131a2b;
  border: 1px solid #263048;
  border-radius: 12px;
  padding: 14px 16px;
}

@media (prefers-reduced-motion: reduce) {
  .cs-14__panel,
    .cs-14__chev {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-14');if(!root)return;
  var trig=root.querySelector('.cs-14__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-14__opt'));
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
(function(){var r=document.querySelector('.cs-14');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;r.style.setProperty('--ff',o.dataset.ff);r.querySelector('.cs-14__tval').textContent=o.dataset.name;r.querySelector('.cs-14__sample').style.fontFamily=o.dataset.ff;});})();
```
