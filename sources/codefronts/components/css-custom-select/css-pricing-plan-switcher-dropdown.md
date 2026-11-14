---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-pricing-plan-switcher-dropdown/"
title: "CSS Pricing Plan Switcher Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A checkout-ready plan selector where each tier shows a colored gradient orb, plan name, and per-month price, with an animated highlight bar that glides to…"
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pricing Plan Switcher Dropdown
Source: https://codefronts.com/components/css-custom-select/css-pricing-plan-switcher-dropdown/

A checkout-ready plan selector where each tier shows a colored gradient orb, plan name, and per-month price, with an animated highlight bar that glides to the active row.
## HTML
```html
<div class="cs-04">
  <span class="cs-04__label">Choose your plan</span>
  <div class="cs-04__field">
    <button type="button" class="cs-04__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="orb" data-t="pro" aria-hidden="true"></span>
      <span class="cs-04__tval"><b>Pro</b><small>Most popular</small></span>
      <span class="cs-04__price">$29<i>/mo</i></span>
      <svg class="cs-04__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-04__panel" role="listbox" tabindex="-1">
      <span class="cs-04__glow" aria-hidden="true"></span>
      <li class="cs-04__opt" role="option" aria-selected="false" data-t="starter" data-name="Starter" data-sub="For side projects" data-price="$9"><span class="orb" data-t="starter"></span><span class="col"><b>Starter</b><small>For side projects</small></span><span class="p">$9<i>/mo</i></span></li>
      <li class="cs-04__opt is-sel" role="option" aria-selected="true" data-t="pro" data-name="Pro" data-sub="Most popular" data-price="$29"><span class="orb" data-t="pro"></span><span class="col"><b>Pro</b><small>Most popular</small></span><span class="p">$29<i>/mo</i></span></li>
      <li class="cs-04__opt" role="option" aria-selected="false" data-t="enterprise" data-name="Enterprise" data-sub="Advanced controls" data-price="$99"><span class="orb" data-t="enterprise"></span><span class="col"><b>Enterprise</b><small>Advanced controls</small></span><span class="p">$99<i>/mo</i></span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-04,
.cs-04 *,
.cs-04 *::before,
.cs-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-04 ::selection {
  background: #a855f7;
  color: #fff;
}

.cs-04 {
  --o1: radial-gradient(circle at 30% 30%,#38bdf8,#0ea5e9);
  --o2: radial-gradient(circle at 30% 30%,#c084fc,#a855f7);
  --o3: radial-gradient(circle at 30% 30%,#fbbf24,#f59e0b);
  --acc: #a855f7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(130% 100% at 80% 0%,#1e1b3a,#0d0b1f);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #efeaff;
}

.cs-04__label {
  font-size: 13px;
  font-weight: 600;
  color: #9d94c4;
  width: 340px;
}

.cs-04__field {
  position: relative;
  width: 340px;
}

.cs-04__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  background: #1a1636;
  border: 1px solid #322b57;
  border-radius: 16px;
  padding: 14px 16px;
  cursor: pointer;
  color: #efeaff;
  transition: border-color .2s,box-shadow .2s;
}

.cs-04__trigger:hover {
  border-color: #463d75;
}

.cs-04__trigger:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px color-mix(in srgb,var(--acc) 26%,transparent);
}

.orb {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  flex-shrink: 0;
  box-shadow: 0 0 14px -2px rgba(168,85,247,.5);
}

.orb[data-t="starter"] {
  background: var(--o1);
}

.orb[data-t="pro"] {
  background: var(--o2);
}

.orb[data-t="enterprise"] {
  background: var(--o3);
}

.cs-04__tval {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.25;
  flex: 1;
}

.cs-04__tval b {
  font-size: 15px;
}

.cs-04__tval small {
  font-size: 11.5px;
  color: #9d94c4;
}

.cs-04__price {
  font-size: 17px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.cs-04__price i {
  font-size: 11px;
  font-weight: 600;
  font-style: normal;
  color: #9d94c4;
}

.cs-04__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #9d94c4;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-04__trigger[aria-expanded="true"] .cs-04__chev {
  transform: rotate(180deg);
}

.cs-04__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #160f30;
  border: 1px solid #322b57;
  border-radius: 16px;
  padding: 8px;
  box-shadow: 0 28px 58px -14px rgba(0,0,0,.72);
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .22s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-04.is-open .cs-04__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-04__glow {
  position: absolute;
  left: 8px;
  right: 8px;
  height: 60px;
  top: 8px;
  border-radius: 12px;
  background: linear-gradient(90deg,color-mix(in srgb,var(--acc) 22%,transparent),transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb,var(--acc) 40%,transparent);
  transition: transform .3s cubic-bezier(.34,1.4,.64,1);
  pointer-events: none;
}

.cs-04__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 0 12px;
  height: 60px;
  border-radius: 12px;
  cursor: pointer;
}

.cs-04__opt .col {
  display: flex;
  flex-direction: column;
  flex: 1;
  line-height: 1.25;
}

.cs-04__opt .col b {
  font-size: 15px;
}

.cs-04__opt .col small {
  font-size: 11.5px;
  color: #9d94c4;
}

.cs-04__opt .p {
  font-size: 16px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.cs-04__opt .p i {
  font-size: 11px;
  font-weight: 600;
  font-style: normal;
  color: #9d94c4;
}

@media (prefers-reduced-motion: reduce) {
  .cs-04__panel,
    .cs-04__chev,
    .cs-04__glow {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-04');if(!root)return;
  var trig=root.querySelector('.cs-04__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-04__opt'));
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
(function(){var r=document.querySelector('.cs-04');if(!r)return;
 var glow=r.querySelector('.cs-04__glow');var opts=[].slice.call(r.querySelectorAll('.cs-04__opt'));
 var accById={starter:'#0ea5e9',pro:'#a855f7',enterprise:'#f59e0b'};
 function place(){var n=opts.findIndex(function(o){return o.classList.contains('is-sel')});if(n<0)n=0;glow.style.transform='translateY('+(n*60)+'px)';}
 place();
 r.addEventListener('cs:pick',function(e){var o=e.detail.opt;r.style.setProperty('--acc',accById[o.dataset.t]||'#a855f7');r.querySelector('.cs-04__trigger .orb').setAttribute('data-t',o.dataset.t);r.querySelector('.cs-04__tval b').textContent=o.dataset.name;r.querySelector('.cs-04__tval small').textContent=o.dataset.sub;r.querySelector('.cs-04__price').innerHTML=o.dataset.price+'<i>/mo</i>';place();});
 r.querySelector('.cs-04__trigger').addEventListener('click',function(){requestAnimationFrame(place);});
})();
```
