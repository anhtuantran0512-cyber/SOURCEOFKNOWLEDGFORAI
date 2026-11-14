---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-animated-slide-fade-dropdown-transition/"
title: "CSS Animated Slide Fade Dropdown Transition"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A dropdown focused purely on the open/close choreography — options cascade in with staggered slide-and-fade, and the panel itself expands with a spring while…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Slide Fade Dropdown Transition
Source: https://codefronts.com/components/css-custom-select/css-animated-slide-fade-dropdown-transition/

A dropdown focused purely on the open/close choreography — options cascade in with staggered slide-and-fade, and the panel itself expands with a spring while a blurred backdrop settles.
## HTML
```html
<div class="cs-18">
  <span class="cs-18__label">Notification sound</span>
  <div class="cs-18__field">
    <button type="button" class="cs-18__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-18__tval">Chime</span>
      <svg class="cs-18__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-18__panel" role="listbox" tabindex="-1">
      <li class="cs-18__opt is-sel" role="option" aria-selected="true" style="--i:0" data-name="Chime">Chime</li>
      <li class="cs-18__opt" role="option" aria-selected="false" style="--i:1" data-name="Pulse">Pulse</li>
      <li class="cs-18__opt" role="option" aria-selected="false" style="--i:2" data-name="Ripple">Ripple</li>
      <li class="cs-18__opt" role="option" aria-selected="false" style="--i:3" data-name="Bloom">Bloom</li>
      <li class="cs-18__opt" role="option" aria-selected="false" style="--i:4" data-name="Silent">Silent</li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-18,
.cs-18 *,
.cs-18 *::before,
.cs-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-18 ::selection {
  background: #22d3ee;
  color: #04202a;
}

.cs-18 {
  --enter-blur: 8px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 100% at 50% 0%,#0c1a2e,#060c18);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #dbeafe;
}

.cs-18__label {
  font-size: 13px;
  font-weight: 600;
  color: #7591b8;
  width: 280px;
}

.cs-18__field {
  position: relative;
  width: 280px;
}

.cs-18__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  background: #0e1f36;
  border: 1px solid #1f3a5c;
  border-radius: 14px;
  padding: 13px 15px;
  cursor: pointer;
  color: #dbeafe;
  font-size: 15px;
  transition: border-color .2s,box-shadow .2s;
}

.cs-18__trigger:hover {
  border-color: #2d5583;
}

.cs-18__trigger:focus-visible {
  outline: none;
  border-color: #22d3ee;
  box-shadow: 0 0 0 4px rgba(34,211,238,.2);
}

.cs-18__tval {
  flex: 1;
  text-align: left;
}

.cs-18__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #7591b8;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}

.cs-18__trigger[aria-expanded="true"] .cs-18__chev {
  transform: rotate(180deg);
}

.cs-18__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #0c1c31;
  border: 1px solid #1f3a5c;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.72);
  opacity: 0;
  transform: translateY(-14px) scale(.92);
  filter: blur(var(--enter-blur));
  transform-origin: top;
  pointer-events: none;
  transition: opacity .28s ease,transform .4s cubic-bezier(.34,1.56,.64,1),filter .28s ease;
}

.cs-18.is-open .cs-18__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  filter: blur(0);
  pointer-events: auto;
}

.cs-18__opt {
  padding: 11px 13px;
  border-radius: 10px;
  font-size: 14.5px;
  cursor: pointer;
  color: #cfe0f5;
  opacity: 0;
  transform: translateY(-10px);
  transition: background .14s,opacity .3s ease,transform .34s cubic-bezier(.34,1.4,.64,1);
}

.cs-18.is-open .cs-18__opt {
  opacity: 1;
  transform: translateY(0);
  transition-delay: calc(var(--i) * .045s + .06s);
}

.cs-18__opt:hover,
.cs-18__opt.is-active {
  background: #15304f;
}

.cs-18__opt.is-sel {
  background: #193758;
  color: #67e8f9;
}

@media (prefers-reduced-motion: reduce) {
  .cs-18__panel {
    transition: opacity .15s;
    filter: none;
    transform: none;
  }

  .cs-18__opt {
    transition: background .12s;
    opacity: 1;
    transform: none;
  }

  .cs-18.is-open .cs-18__opt {
    transition-delay: 0s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-18');if(!root)return;
  var trig=root.querySelector('.cs-18__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-18__opt'));
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
(function(){var r=document.querySelector('.cs-18');if(!r)return;r.addEventListener('cs:pick',function(e){r.querySelector('.cs-18__tval').textContent=e.detail.opt.dataset.name;});})();
```
