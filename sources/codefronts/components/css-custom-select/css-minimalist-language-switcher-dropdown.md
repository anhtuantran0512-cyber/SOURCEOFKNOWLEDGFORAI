---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-minimalist-language-switcher-dropdown/"
title: "CSS Minimalist Language Switcher Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A tiny globe-icon language switcher for clean headers, expanding to a compact list of languages with native names and a subtle check on the active locale."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Minimalist Language Switcher Dropdown
Source: https://codefronts.com/components/css-custom-select/css-minimalist-language-switcher-dropdown/

A tiny globe-icon language switcher for clean headers, expanding to a compact list of languages with native names and a subtle check on the active locale.
## HTML
```html
<div class="cs-06">
  <div class="cs-06__bar">
    <span class="cs-06__logo">codefronts</span>
    <div class="cs-06__field">
      <button type="button" class="cs-06__trigger" aria-haspopup="listbox" aria-expanded="false" aria-label="Change language">
        <span class="cs-06__globe" aria-hidden="true"></span>
        <span class="cs-06__code">EN</span>
      </button>
      <ul class="cs-06__panel" role="listbox" tabindex="-1">
        <li class="cs-06__opt is-sel" role="option" aria-selected="true" data-code="EN"><span class="l"><b>English</b><small>English</small></span><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-06__opt" role="option" aria-selected="false" data-code="FR"><span class="l"><b>French</b><small>Français</small></span><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-06__opt" role="option" aria-selected="false" data-code="DE"><span class="l"><b>German</b><small>Deutsch</small></span><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-06__opt" role="option" aria-selected="false" data-code="ES"><span class="l"><b>Spanish</b><small>Español</small></span><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-06__opt" role="option" aria-selected="false" data-code="JA"><span class="l"><b>Japanese</b><small>日本語</small></span><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.cs-06,
.cs-06 *,
.cs-06 *::before,
.cs-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-06 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.cs-06 {
  --ink: #334155;
  --acc: #0ea5e9;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(180deg,#f8fafc,#eef2f7);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  color: #0f172a;
}

.cs-06__bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 28px;
  background: #fff;
  border-bottom: 1px solid #e6eaf0;
}

.cs-06__logo {
  font-weight: 800;
  font-size: 17px;
  letter-spacing: -.3px;
  color: #0f172a;
}

.cs-06__field {
  position: relative;
}

.cs-06__trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  border-radius: 40px;
  padding: 7px 13px 7px 11px;
  cursor: pointer;
  color: var(--ink);
  transition: background .18s,border-color .18s,box-shadow .18s;
}

.cs-06__trigger:hover {
  background: #e8eef5;
}

.cs-06__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(14,165,233,.18);
}

.cs-06__globe {
  width: 17px;
  height: 17px;
  border-radius: 50%;
  border: 1.7px solid currentColor;
  position: relative;
  flex-shrink: 0;
}

.cs-06__globe::before {
  content: "";
  position: absolute;
  inset: -1.7px 4px;
  border: 1.7px solid currentColor;
  border-radius: 50%;
}

.cs-06__globe::after {
  content: "";
  position: absolute;
  left: 50%;
  top: -1.7px;
  bottom: -1.7px;
  width: 0;
  border-left: 1.7px solid currentColor;
  transform: translateX(-50%);
}

.cs-06__code {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .5px;
}

.cs-06__panel {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  width: 210px;
  z-index: 20;
  list-style: none;
  background: #fff;
  border: 1px solid #e6eaf0;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 22px 44px -16px rgba(15,23,42,.24);
  opacity: 0;
  transform: scale(.95) translateY(-6px);
  transform-origin: top right;
  pointer-events: none;
  transition: opacity .18s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-06.is-open .cs-06__panel {
  opacity: 1;
  transform: scale(1) translateY(0);
  pointer-events: auto;
}

.cs-06__opt {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 11px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .14s;
}

.cs-06__opt .l {
  display: flex;
  flex-direction: column;
  line-height: 1.3;
  flex: 1;
}

.cs-06__opt .l b {
  font-size: 14px;
  color: #0f172a;
}

.cs-06__opt .l small {
  font-size: 12px;
  color: #94a3b8;
}

.cs-06__opt svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: var(--acc);
  stroke-width: 2.6;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .14s;
}

.cs-06__opt.is-sel svg {
  opacity: 1;
}

.cs-06__opt:hover,
.cs-06__opt.is-active {
  background: #f1f5f9;
}

@media (prefers-reduced-motion: reduce) {
  .cs-06__panel {
    transition: opacity .14s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-06');if(!root)return;
  var trig=root.querySelector('.cs-06__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-06__opt'));
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
(function(){var r=document.querySelector('.cs-06');if(!r)return;r.addEventListener('cs:pick',function(e){r.querySelector('.cs-06__code').textContent=e.detail.opt.dataset.code;});})();
```
