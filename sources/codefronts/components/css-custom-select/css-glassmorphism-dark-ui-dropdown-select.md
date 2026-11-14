---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-glassmorphism-dark-ui-dropdown-select/"
title: "CSS Glassmorphism Dark UI Dropdown Select"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A design-forward glassmorphism dropdown over an animated aurora backdrop, using backdrop-filter blur, layered translucency, and a subtle border sheen for a…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Dark UI Dropdown Select
Source: https://codefronts.com/components/css-custom-select/css-glassmorphism-dark-ui-dropdown-select/

A design-forward glassmorphism dropdown over an animated aurora backdrop, using backdrop-filter blur, layered translucency, and a subtle border sheen for a premium SaaS feel.
## HTML
```html
<div class="cs-20">
  <span class="cs-20__aurora" aria-hidden="true"></span>
  <div class="cs-20__inner">
    <span class="cs-20__label">Region</span>
    <div class="cs-20__field">
      <button type="button" class="cs-20__trigger" aria-haspopup="listbox" aria-expanded="false">
        <span class="cs-20__dot" aria-hidden="true"></span>
        <span class="cs-20__tval">US East (N. Virginia)</span>
        <svg class="cs-20__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul class="cs-20__panel" role="listbox" tabindex="-1">
        <li class="cs-20__opt is-sel" role="option" aria-selected="true" data-name="US East (N. Virginia)"><span class="d"></span>US East (N. Virginia)<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-20__opt" role="option" aria-selected="false" data-name="US West (Oregon)"><span class="d"></span>US West (Oregon)<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-20__opt" role="option" aria-selected="false" data-name="EU (Frankfurt)"><span class="d"></span>EU (Frankfurt)<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-20__opt" role="option" aria-selected="false" data-name="Asia Pacific (Tokyo)"><span class="d"></span>Asia Pacific (Tokyo)<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="cs-20__opt" role="option" aria-selected="false" data-name="South America (São Paulo)"><span class="d"></span>South America (São Paulo)<svg class="ck" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.cs-20,
.cs-20 *,
.cs-20 *::before,
.cs-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-20 ::selection {
  background: #c084fc;
  color: #1a0b2e;
}

.cs-20 {
  --blur: 18px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  overflow: hidden;
  background: #0a0714;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #f2ecfb;
}

.cs-20__aurora {
  position: absolute;
  inset: -20%;
  z-index: 0;
  filter: blur(20px);
  background: radial-gradient(40% 40% at 25% 30%,rgba(168,85,247,.55),transparent 70%), radial-gradient(45% 45% at 75% 65%,rgba(56,189,248,.5),transparent 70%), radial-gradient(35% 35% at 60% 20%,rgba(236,72,153,.4),transparent 70%);
  animation: cs-20-drift 16s ease-in-out infinite alternate;
}

@keyframes cs-20-drift {
  0% {
    transform: translate(-4%,-3%) scale(1);
  }

  50% {
    transform: translate(5%,4%) scale(1.12);
  }

  100% {
    transform: translate(-3%,5%) scale(1.05);
  }
}

.cs-20__inner {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 320px;
  max-width: 100%;
}

.cs-20__label {
  font-size: 13px;
  font-weight: 600;
  color: rgba(242,236,251,.7);
}

.cs-20__field {
  position: relative;
}

.cs-20__trigger {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  gap: 11px;
  background: rgba(20,14,36,.45);
  backdrop-filter: blur(var(--blur));
  -webkit-backdrop-filter: blur(var(--blur));
  border: none;
  border-radius: 15px;
  padding: 14px 16px;
  cursor: pointer;
  color: #f2ecfb;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.14),0 10px 30px -12px rgba(0,0,0,.6);
  transition: box-shadow .2s;
}

.cs-20__trigger::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 15px;
  padding: 1px;
  background: linear-gradient(140deg,rgba(255,255,255,.5),rgba(255,255,255,.05) 40%,transparent);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.cs-20__trigger:focus-visible {
  outline: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2),0 0 0 4px rgba(192,132,252,.3);
}

.cs-20__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #4ade80;
  box-shadow: 0 0 10px -1px #4ade80;
  flex-shrink: 0;
}

.cs-20__tval {
  flex: 1;
  text-align: left;
  font-size: 15px;
}

.cs-20__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: rgba(242,236,251,.65);
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-20__trigger[aria-expanded="true"] .cs-20__chev {
  transform: rotate(180deg);
}

.cs-20__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: rgba(18,12,32,.62);
  backdrop-filter: blur(var(--blur));
  -webkit-backdrop-filter: blur(var(--blur));
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 15px;
  padding: 6px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.1),0 28px 56px -16px rgba(0,0,0,.7);
  opacity: 0;
  transform: translateY(-10px) scale(.98);
  transform-origin: top;
  pointer-events: none;
  transition: opacity .22s,transform .28s cubic-bezier(.16,1,.3,1);
}

.cs-20.is-open .cs-20__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.cs-20__opt {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 12px;
  border-radius: 10px;
  font-size: 14.5px;
  color: #e9e1f7;
  cursor: pointer;
  transition: background .14s;
}

.cs-20__opt .d {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgba(242,236,251,.35);
  flex-shrink: 0;
}

.cs-20__opt:hover,
.cs-20__opt.is-active {
  background: rgba(255,255,255,.08);
}

.cs-20__opt.is-sel .d {
  background: #4ade80;
  box-shadow: 0 0 8px -1px #4ade80;
}

.cs-20__opt .ck {
  width: 17px;
  height: 17px;
  margin-left: auto;
  fill: none;
  stroke: #c084fc;
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .14s;
}

.cs-20__opt.is-sel .ck {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cs-20__aurora {
    animation: none;
  }

  .cs-20__panel,
    .cs-20__chev {
    transition: opacity .15s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-20');if(!root)return;
  var trig=root.querySelector('.cs-20__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-20__opt'));
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
(function(){var r=document.querySelector('.cs-20');if(!r)return;r.addEventListener('cs:pick',function(e){r.querySelector('.cs-20__tval').textContent=e.detail.opt.dataset.name;});})();
```
