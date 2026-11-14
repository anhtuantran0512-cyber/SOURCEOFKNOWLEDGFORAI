---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-multi-select-tag-dropdown-with-chips/"
title: "CSS Multi-Select Tag Dropdown With Chips"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A multi-select dropdown that injects removable chips into the field as you check options, with a live count, checkbox rows, and an x-to-delete on every chip."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi-Select Tag Dropdown With Chips
Source: https://codefronts.com/components/css-custom-select/css-multi-select-tag-dropdown-with-chips/

A multi-select dropdown that injects removable chips into the field as you check options, with a live count, checkbox rows, and an x-to-delete on every chip.
## HTML
```html
<div class="cs-09">
  <span class="cs-09__label">Filter by skill</span>
  <div class="cs-09__field">
    <button type="button" class="cs-09__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="cs-09__chips"><span class="cs-09__ph">Select skills…</span></span>
      <span class="cs-09__count" hidden>0</span>
      <svg class="cs-09__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-09__panel" role="listbox" aria-multiselectable="true" tabindex="-1">
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="React"><span class="box"></span>React</li>
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="TypeScript"><span class="box"></span>TypeScript</li>
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="CSS"><span class="box"></span>CSS</li>
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="Node.js"><span class="box"></span>Node.js</li>
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="GraphQL"><span class="box"></span>GraphQL</li>
      <li class="cs-09__opt" role="option" aria-selected="false" data-v="Rust"><span class="box"></span>Rust</li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-09,
.cs-09 *,
.cs-09 *::before,
.cs-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-09 ::selection {
  background: #22d3ee;
  color: #04202a;
}

.cs-09 {
  --chip: #22d3ee;
  --chip-r: 8px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(160deg,#071820,#03121a);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #d6f5fb;
}

.cs-09__label {
  font-size: 13px;
  font-weight: 600;
  color: #5b8b97;
  width: 320px;
}

.cs-09__field {
  position: relative;
  width: 320px;
}

.cs-09__trigger {
  width: 100%;
  min-height: 50px;
  display: flex;
  align-items: center;
  gap: 8px;
  background: #08222c;
  border: 1px solid #15414f;
  border-radius: 14px;
  padding: 8px 12px;
  cursor: pointer;
  color: #d6f5fb;
  transition: border-color .2s,box-shadow .2s;
}

.cs-09__trigger:hover {
  border-color: #1d5666;
}

.cs-09__trigger:focus-visible {
  outline: none;
  border-color: var(--chip);
  box-shadow: 0 0 0 4px rgba(34,211,238,.2);
}

.cs-09__chips {
  flex: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
  min-width: 0;
}

.cs-09__ph {
  color: #4b7581;
  font-size: 14.5px;
}

.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(34,211,238,.16);
  color: #a5f3fc;
  border: 1px solid rgba(34,211,238,.3);
  border-radius: var(--chip-r);
  padding: 4px 6px 4px 10px;
  font-size: 12.5px;
  font-weight: 600;
}

.chip button {
  border: none;
  background: none;
  color: #67e8f9;
  cursor: pointer;
  width: 16px;
  height: 16px;
  display: grid;
  place-items: center;
  border-radius: 5px;
  font-size: 13px;
  line-height: 1;
}

.chip button:hover {
  background: rgba(34,211,238,.25);
}

.cs-09__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #5b8b97;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex-shrink: 0;
}

.cs-09__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: #08222c;
  border: 1px solid #15414f;
  border-radius: 14px;
  padding: 6px;
  box-shadow: 0 26px 54px -14px rgba(0,0,0,.7);
  max-height: 250px;
  overflow-y: auto;
  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity .2s,transform .22s cubic-bezier(.16,1,.3,1);
}

.cs-09.is-open .cs-09__panel {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.cs-09__opt {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 10px;
  font-size: 14.5px;
  cursor: pointer;
  transition: background .14s;
}

.cs-09__opt:hover,
.cs-09__opt.is-active {
  background: #0e3140;
}

.box {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  border: 2px solid #2b5f6e;
  position: relative;
  flex-shrink: 0;
  transition: background .14s,border-color .14s;
}

.cs-09__opt.is-on .box {
  background: var(--chip);
  border-color: var(--chip);
}

.cs-09__opt.is-on .box::after {
  content: "";
  position: absolute;
  left: 5px;
  top: 1px;
  width: 6px;
  height: 11px;
  border: solid #04202a;
  border-width: 0 2.5px 2.5px 0;
  transform: rotate(45deg);
}

@media (prefers-reduced-motion: reduce) {
  .cs-09__panel {
    transition: opacity .14s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-09');if(!root)return;
  var trig=root.querySelector('.cs-09__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-09__opt'));
  var chips=root.querySelector('.cs-09__chips');
  var ph=root.querySelector('.cs-09__ph');
  var ai=-1;
  function open(){root.classList.add('is-open');trig.setAttribute('aria-expanded','true');}
  function close(){root.classList.remove('is-open');trig.setAttribute('aria-expanded','false');opts.forEach(function(o){o.classList.remove('is-active')});ai=-1;}
  function render(){
    var on=opts.filter(function(o){return o.classList.contains('is-on')});
    chips.querySelectorAll('.chip').forEach(function(c){c.remove()});
    if(!on.length){ph.style.display='';return;}
    ph.style.display='none';
    on.forEach(function(o){
      var c=document.createElement('span');c.className='chip';
      c.appendChild(document.createTextNode(o.dataset.v));
      var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Remove '+o.dataset.v);b.textContent='×';
      b.addEventListener('click',function(ev){ev.stopPropagation();toggle(o,false);});
      c.appendChild(b);chips.appendChild(c);
    });
  }
  function toggle(o,openAfter){
    var on=!o.classList.contains('is-on');
    o.classList.toggle('is-on',on);o.setAttribute('aria-selected',on?'true':'false');
    render();if(openAfter)open();
  }
  trig.addEventListener('click',function(e){if(e.target.closest('.chip'))return;root.classList.contains('is-open')?close():open();});
  opts.forEach(function(o,k){o.addEventListener('click',function(e){e.stopPropagation();toggle(o,true);});o.addEventListener('mousemove',function(){opts.forEach(function(x){x.classList.remove('is-active')});o.classList.add('is-active');ai=k;});});
  root.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();if(!root.classList.contains('is-open'))return open();ai=(ai+1)%opts.length;opts.forEach(function(x){x.classList.remove('is-active')});opts[ai].classList.add('is-active');opts[ai].scrollIntoView({block:'nearest'});}
    else if(e.key==='ArrowUp'){e.preventDefault();ai=(ai-1+opts.length)%opts.length;opts.forEach(function(x){x.classList.remove('is-active')});opts[ai].classList.add('is-active');opts[ai].scrollIntoView({block:'nearest'});}
    else if((e.key==='Enter'||e.key===' ')&&ai>=0){e.preventDefault();toggle(opts[ai],true);}
    else if(e.key==='Escape'){e.preventDefault();close();trig.focus();}
  });
  trig.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();open();}});
  document.addEventListener('click',function(e){if(!root.contains(e.target))close();});
})();
```
