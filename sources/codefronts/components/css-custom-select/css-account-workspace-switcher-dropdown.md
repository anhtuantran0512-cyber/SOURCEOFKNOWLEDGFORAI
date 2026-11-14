---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-account-workspace-switcher-dropdown/"
title: "CSS Account Workspace Switcher Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A B2B SaaS workspace switcher with rounded team logos, member counts, plan badges, and a pinned 'Create workspace' action at the bottom of the panel."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Account Workspace Switcher Dropdown
Source: https://codefronts.com/components/css-custom-select/css-account-workspace-switcher-dropdown/

A B2B SaaS workspace switcher with rounded team logos, member counts, plan badges, and a pinned 'Create workspace' action at the bottom of the panel.
## HTML
```html
<div class="cs-07">
  <span class="cs-07__label">Workspace</span>
  <div class="cs-07__field">
    <button type="button" class="cs-07__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="logo" data-hue="265">AC</span>
      <span class="cs-07__tval"><b>Acme Corp</b><small>12 members</small></span>
      <svg class="cs-07__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 9l4-4 4 4M8 15l4 4 4-4"/></svg>
    </button>
    <div class="cs-07__panel" role="listbox" tabindex="-1">
      <div class="cs-07__scroll">
        <div class="cs-07__opt is-sel" role="option" aria-selected="true" data-name="Acme Corp" data-sub="12 members" data-hue="265"><span class="logo" data-hue="265">AC</span><span class="col"><b>Acme Corp</b><small>12 members</small></span><span class="badge">Pro</span></div>
        <div class="cs-07__opt" role="option" aria-selected="false" data-name="Nova Labs" data-sub="4 members" data-hue="190"><span class="logo" data-hue="190">NL</span><span class="col"><b>Nova Labs</b><small>4 members</small></span><span class="badge free">Free</span></div>
        <div class="cs-07__opt" role="option" aria-selected="false" data-name="Orbit Studio" data-sub="27 members" data-hue="150"><span class="logo" data-hue="150">OS</span><span class="col"><b>Orbit Studio</b><small>27 members</small></span><span class="badge">Team</span></div>
        <div class="cs-07__opt" role="option" aria-selected="false" data-name="Pixel Forge" data-sub="8 members" data-hue="25"><span class="logo" data-hue="25">PF</span><span class="col"><b>Pixel Forge</b><small>8 members</small></span><span class="badge">Pro</span></div>
      </div>
      <button class="cs-07__add" type="button"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>Create workspace</button>
    </div>
  </div>
</div>
```
## CSS
```css
.cs-07,
.cs-07 *,
.cs-07 *::before,
.cs-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-07 ::selection {
  background: #7c3aed;
  color: #fff;
}

.cs-07 {
  --ring: #7c3aed;
  --list-max: 230px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 10% 0%,#191233,#0c0a1a);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #eae6ff;
}

.cs-07__label {
  font-size: 13px;
  font-weight: 600;
  color: #9b91c7;
  width: 320px;
}

.cs-07__field {
  position: relative;
  width: 320px;
}

.cs-07__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #181433;
  border: 1px solid #2e2755;
  border-radius: 15px;
  padding: 12px 15px;
  cursor: pointer;
  color: #eae6ff;
  transition: border-color .2s,box-shadow .2s;
}

.cs-07__trigger:hover {
  border-color: #413a70;
}

.cs-07__trigger:focus-visible {
  outline: none;
  border-color: var(--ring);
  box-shadow: 0 0 0 4px rgba(124,58,237,.25);
}

.logo {
  width: 36px;
  height: 36px;
  border-radius: 11px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 13px;
  color: #fff;
  flex-shrink: 0;
  background: linear-gradient(140deg,hsl(var(--h,265) 70% 58%),hsl(calc(var(--h,265) + 30) 70% 46%));
}

.logo[data-hue] {
  --h: attr(data-hue);
}

.cs-07__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.28;
  flex: 1;
}

.cs-07__tval b {
  font-size: 15px;
}

.cs-07__tval small {
  font-size: 11.5px;
  color: #9b91c7;
}

.cs-07__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #9b91c7;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cs-07__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  background: #140f2c;
  border: 1px solid #2e2755;
  border-radius: 15px;
  padding: 6px;
  box-shadow: 0 28px 56px -14px rgba(0,0,0,.72);
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .24s cubic-bezier(.16,1,.3,1);
}

.cs-07.is-open .cs-07__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-07__scroll {
  max-height: var(--list-max);
  overflow-y: auto;
}

.cs-07__opt {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 9px 10px;
  border-radius: 11px;
  cursor: pointer;
  transition: background .14s;
}

.cs-07__opt .col {
  display: flex;
  flex-direction: column;
  flex: 1;
  line-height: 1.28;
}

.cs-07__opt .col b {
  font-size: 14.5px;
}

.cs-07__opt .col small {
  font-size: 11.5px;
  color: #9b91c7;
}

.cs-07__opt:hover,
.cs-07__opt.is-active {
  background: #211a44;
}

.cs-07__opt.is-sel .logo {
  box-shadow: 0 0 0 2px #140f2c,0 0 0 4px var(--ring);
}

.badge {
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(124,58,237,.2);
  color: #c4b5fd;
  letter-spacing: .3px;
}

.badge.free {
  background: rgba(148,163,184,.18);
  color: #cbd5e1;
}

.cs-07__add {
  position: sticky;
  bottom: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 5px;
  padding: 11px;
  border: 1px dashed #3a3268;
  background: #140f2c;
  color: #c4b5fd;
  font-size: 13.5px;
  font-weight: 600;
  border-radius: 11px;
  cursor: pointer;
  transition: background .16s,border-color .16s;
}

.cs-07__add:hover,
.cs-07__add:focus-visible {
  background: #1d1740;
  border-color: var(--ring);
  outline: none;
}

.cs-07__add svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
}

@media (prefers-reduced-motion: reduce) {
  .cs-07__panel {
    transition: opacity .14s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-07');if(!root)return;
  var trig=root.querySelector('.cs-07__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-07__opt'));
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
(function(){var r=document.querySelector('.cs-07');if(!r)return;
 [].forEach.call(r.querySelectorAll('.logo[data-hue]'),function(l){l.style.setProperty('--h',l.getAttribute('data-hue'));});
 r.addEventListener('cs:pick',function(e){var o=e.detail.opt;var t=r.querySelector('.cs-07__trigger .logo');t.textContent=o.querySelector('.logo').textContent;t.style.setProperty('--h',o.dataset.hue);r.querySelector('.cs-07__tval b').textContent=o.dataset.name;r.querySelector('.cs-07__tval small').textContent=o.dataset.sub;});
})();
```
