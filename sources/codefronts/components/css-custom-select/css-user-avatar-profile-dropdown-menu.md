---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-user-avatar-profile-dropdown-menu/"
title: "CSS User Avatar Profile Dropdown Menu"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A navbar-anchored profile menu with a gradient monogram avatar, a header card showing name and email, grouped menu items with icons, and a distinct…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS User Avatar Profile Dropdown Menu
Source: https://codefronts.com/components/css-custom-select/css-user-avatar-profile-dropdown-menu/

A navbar-anchored profile menu with a gradient monogram avatar, a header card showing name and email, grouped menu items with icons, and a distinct destructive logout row.
## HTML
```html
<div class="cs-05">
  <div class="cs-05__bar">
    <span class="cs-05__brand">Dashboard</span>
    <div class="cs-05__field">
      <button type="button" class="cs-05__trigger" aria-haspopup="menu" aria-expanded="false">
        <span class="cs-05__av">AM</span>
        <svg class="cs-05__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div class="cs-05__panel" role="menu" tabindex="-1">
        <div class="cs-05__head">
          <span class="cs-05__av lg">AM</span>
          <div class="cs-05__id"><b>Alex Morgan</b><small>[email protected]</small></div>
        </div>
        <div class="cs-05__sep"></div>
        <button class="cs-05__item" role="menuitem"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>My Profile</button>
        <button class="cs-05__item" role="menuitem"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1l2-1.6-2-3.4-2.4 1a7 7 0 0 0-1.7-1L14.5 3h-5l-.3 2.6a7 7 0 0 0-1.7 1l-2.4-1-2 3.4L3 11a7 7 0 0 0 0 2l-2 1.6 2 3.4 2.4-1a7 7 0 0 0 1.7 1l.3 2.6h5l.3-2.6a7 7 0 0 0 1.7-1l2.4 1 2-3.4-2-1.6a7 7 0 0 0 .1-1z"/></svg>Settings</button>
        <button class="cs-05__item" role="menuitem"><svg viewBox="0 0 24 24"><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/><circle cx="12" cy="12" r="4"/></svg>Billing</button>
        <div class="cs-05__sep"></div>
        <button class="cs-05__item is-danger" role="menuitem"><svg viewBox="0 0 24 24"><path d="M16 17l5-5-5-5M21 12H9M13 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h8"/></svg>Sign out</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cs-05,
.cs-05 *,
.cs-05 *::before,
.cs-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-05 ::selection {
  background: #f43f5e;
  color: #fff;
}

.cs-05 {
  --av1: #f43f5e;
  --av2: #8b5cf6;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(180deg,#0b0e16,#12131f);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 0;
  color: #e7e9f3;
}

.cs-05__bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 26px;
  background: rgba(20,22,34,.9);
  border-bottom: 1px solid #232739;
  position: relative;
}

.cs-05__brand {
  font-weight: 800;
  font-size: 17px;
  letter-spacing: .3px;
}

.cs-05__field {
  position: relative;
}

.cs-05__trigger {
  display: flex;
  align-items: center;
  gap: 7px;
  background: #1b1f30;
  border: 1px solid #2c3145;
  border-radius: 40px;
  padding: 5px 10px 5px 5px;
  cursor: pointer;
  transition: border-color .2s,box-shadow .2s;
}

.cs-05__trigger:hover {
  border-color: #3d4460;
}

.cs-05__trigger:focus-visible {
  outline: none;
  border-color: #8b5cf6;
  box-shadow: 0 0 0 4px rgba(139,92,246,.25);
}

.cs-05__av {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg,var(--av1),var(--av2));
  color: #fff;
  font-weight: 800;
  font-size: 13px;
  letter-spacing: .5px;
}

.cs-05__av.lg {
  width: 44px;
  height: 44px;
  font-size: 16px;
}

.cs-05__chev {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #8990ad;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-05__trigger[aria-expanded="true"] .cs-05__chev {
  transform: rotate(180deg);
}

.cs-05__panel {
  position: absolute;
  top: calc(100% + 12px);
  right: 0;
  width: 266px;
  z-index: 30;
  background: #161a29;
  border: 1px solid #2a2f44;
  border-radius: 16px;
  padding: 8px;
  box-shadow: 0 30px 60px -16px rgba(0,0,0,.75);
  opacity: 0;
  transform: scale(.94) translateY(-8px);
  transform-origin: top right;
  pointer-events: none;
  transition: opacity .2s,transform .26s cubic-bezier(.16,1,.3,1);
}

.cs-05.is-open .cs-05__panel {
  opacity: 1;
  transform: scale(1) translateY(0);
  pointer-events: auto;
}

.cs-05__head {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 10px 12px;
}

.cs-05__id {
  display: flex;
  flex-direction: column;
  line-height: 1.35;
  overflow: hidden;
}

.cs-05__id b {
  font-size: 14.5px;
}

.cs-05__id small {
  font-size: 12px;
  color: #8990ad;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cs-05__sep {
  height: 1px;
  background: #262b3e;
  margin: 5px 4px;
}

.cs-05__item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 11px;
  border: none;
  background: none;
  color: #d3d7e6;
  font-size: 14px;
  border-radius: 10px;
  cursor: pointer;
  text-align: left;
  transition: background .14s,color .14s;
}

.cs-05__item svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: .85;
}

.cs-05__item:hover,
.cs-05__item:focus-visible {
  background: #212639;
  outline: none;
}

.cs-05__item.is-danger {
  color: #fb7185;
}

.cs-05__item.is-danger:hover {
  background: rgba(244,63,94,.14);
}

@media (prefers-reduced-motion: reduce) {
  .cs-05__panel,
    .cs-05__chev {
    transition: opacity .15s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-05');if(!root)return;
  var trig=root.querySelector('.cs-05__trigger');
  var items=[].slice.call(root.querySelectorAll('.cs-05__item'));
  function open(){root.classList.add('is-open');trig.setAttribute('aria-expanded','true');if(items[0])items[0].focus();}
  function close(f){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');if(f)trig.focus();}
  trig.addEventListener('click',function(){root.classList.contains('is-open')?close():open();});
  trig.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();open();}});
  root.addEventListener('keydown',function(e){
    if(!root.classList.contains('is-open'))return;
    var idx=items.indexOf(document.activeElement);
    if(e.key==='ArrowDown'){e.preventDefault();(items[(idx+1)%items.length]||items[0]).focus();}
    else if(e.key==='ArrowUp'){e.preventDefault();(items[(idx-1+items.length)%items.length]||items[items.length-1]).focus();}
    else if(e.key==='Escape'){e.preventDefault();close(true);}
  });
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
```
