---
source: "codefronts"
url: "https://codefronts.com/components/css-custom-select/css-credit-card-type-selector-dropdown/"
title: "CSS Credit Card Type Selector Dropdown"
section: "components"
category: "css-custom-select"
category_name: "CSS Custom Select Dropdowns"
description: "A payment-method dropdown rendering pure-CSS card brand marks (Visa, Mastercard, Amex) beside masked card numbers, styled as a dark glass fintech control."
has_js: "true"
---

Here's a working CSS Custom Select Dropdown from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Credit Card Type Selector Dropdown
Source: https://codefronts.com/components/css-custom-select/css-credit-card-type-selector-dropdown/

A payment-method dropdown rendering pure-CSS card brand marks (Visa, Mastercard, Amex) beside masked card numbers, styled as a dark glass fintech control.
## HTML
```html
<div class="cs-03">
  <span class="cs-03__label">Payment method</span>
  <div class="cs-03__field">
    <button type="button" class="cs-03__trigger" aria-haspopup="listbox" aria-expanded="false">
      <span class="mark" data-brand="visa" aria-hidden="true"></span>
      <span class="cs-03__tval">Visa <span class="pan">•••• 4242</span></span>
      <svg class="cs-03__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <ul class="cs-03__panel" role="listbox" tabindex="-1">
      <li class="cs-03__opt is-sel" role="option" aria-selected="true" data-brand="visa" data-name="Visa" data-pan="•••• 4242"><span class="mark" data-brand="visa"></span><span class="txt">Visa</span><span class="pan">•••• 4242</span></li>
      <li class="cs-03__opt" role="option" aria-selected="false" data-brand="mc" data-name="Mastercard" data-pan="•••• 8210"><span class="mark" data-brand="mc"></span><span class="txt">Mastercard</span><span class="pan">•••• 8210</span></li>
      <li class="cs-03__opt" role="option" aria-selected="false" data-brand="amex" data-name="Amex" data-pan="•••• 3005"><span class="mark" data-brand="amex"></span><span class="txt">American Express</span><span class="pan">•••• 3005</span></li>
      <li class="cs-03__opt" role="option" aria-selected="false" data-brand="disc" data-name="Discover" data-pan="•••• 6011"><span class="mark" data-brand="disc"></span><span class="txt">Discover</span><span class="pan">•••• 6011</span></li>
    </ul>
  </div>
</div>
```
## CSS
```css
.cs-03,
.cs-03 *,
.cs-03 *::before,
.cs-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cs-03 ::selection {
  background: #fbbf24;
  color: #1a1400;
}

.cs-03 {
  --rail: #fbbf24;
  --blur: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(135deg,#1a1730,#0f1226 55%,#161033);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 60px 20px;
  color: #ece9ff;
}

.cs-03__label {
  font-size: 13px;
  font-weight: 600;
  color: #9a93c9;
  width: 320px;
}

.cs-03__field {
  position: relative;
  width: 320px;
}

.cs-03__trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  background: rgba(38,32,66,.7);
  border: 1px solid #3a3363;
  border-radius: 15px;
  padding: 14px 16px;
  cursor: pointer;
  color: #ece9ff;
  transition: border-color .2s,box-shadow .2s;
}

.cs-03__trigger:hover {
  border-color: #544c85;
}

.cs-03__trigger:focus-visible {
  outline: none;
  border-color: var(--rail);
  box-shadow: 0 0 0 4px rgba(251,191,36,.2);
}

.cs-03__tval {
  flex: 1;
  text-align: left;
  font-size: 15px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.cs-03__chev {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: #9a93c9;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform .2s;
}

.cs-03__trigger[aria-expanded="true"] .cs-03__chev {
  transform: rotate(180deg);
}

.pan {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  letter-spacing: 1px;
  color: #9a93c9;
}

.mark {
  width: 40px;
  height: 26px;
  border-radius: 5px;
  flex-shrink: 0;
  position: relative;
  background: #fff;
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.08);
}

.mark[data-brand="visa"] {
  background: linear-gradient(135deg,#1a1f71,#2434b0);
}

.mark[data-brand="visa"]::before {
  content: "VISA";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 800;
  font-style: italic;
  font-size: 11px;
  letter-spacing: .5px;
}

.mark[data-brand="mc"] {
  background: #20143b;
}

.mark[data-brand="mc"]::before {
  content: "";
  position: absolute;
  left: 9px;
  top: 50%;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #eb001b;
  transform: translateY(-50%);
}

.mark[data-brand="mc"]::after {
  content: "";
  position: absolute;
  right: 9px;
  top: 50%;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #f79e1b;
  transform: translateY(-50%);
  mix-blend-mode: screen;
}

.mark[data-brand="amex"] {
  background: linear-gradient(135deg,#2e77bb,#1e5a9c);
}

.mark[data-brand="amex"]::before {
  content: "AMEX";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 800;
  font-size: 9px;
  letter-spacing: .5px;
}

.mark[data-brand="disc"] {
  background: #1a1730;
  overflow: hidden;
}

.mark[data-brand="disc"]::before {
  content: "";
  position: absolute;
  right: -3px;
  top: 50%;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: radial-gradient(circle,#ff6b00,#f79e1b);
  transform: translateY(-50%);
}

.mark[data-brand="disc"]::after {
  content: "DISC";
  position: absolute;
  left: 5px;
  top: 50%;
  transform: translateY(-50%);
  color: #fff;
  font-weight: 800;
  font-size: 8px;
}

.cs-03__panel {
  position: absolute;
  top: calc(100% + 9px);
  left: 0;
  right: 0;
  z-index: 20;
  list-style: none;
  background: rgba(30,25,54,.82);
  backdrop-filter: blur(var(--blur));
  -webkit-backdrop-filter: blur(var(--blur));
  border: 1px solid #3a3363;
  border-radius: 15px;
  padding: 7px;
  box-shadow: 0 28px 56px -14px rgba(0,0,0,.7);
  opacity: 0;
  transform: translateY(-10px) scale(.98);
  pointer-events: none;
  transform-origin: top;
  transition: opacity .24s,transform .34s cubic-bezier(.34,1.56,.64,1);
}

.cs-03.is-open .cs-03__panel {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.cs-03__opt {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 11px;
  cursor: pointer;
  border-left: 3px solid transparent;
  transition: background .14s,border-color .14s;
}

.cs-03__opt .txt {
  flex: 1;
  font-size: 14.5px;
}

.cs-03__opt:hover,
.cs-03__opt.is-active {
  background: rgba(58,51,99,.55);
}

.cs-03__opt.is-sel {
  border-left-color: var(--rail);
  background: rgba(58,51,99,.4);
}

@media (prefers-reduced-motion: reduce) {
  .cs-03__panel,
    .cs-03__chev {
    transition: opacity .15s;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cs-03');if(!root)return;
  var trig=root.querySelector('.cs-03__trigger');
  var opts=[].slice.call(root.querySelectorAll('.cs-03__opt'));
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
(function(){var r=document.querySelector('.cs-03');if(!r)return;r.addEventListener('cs:pick',function(e){var o=e.detail.opt;r.querySelector('.cs-03__trigger .mark').setAttribute('data-brand',o.dataset.brand);r.querySelector('.cs-03__tval').innerHTML=o.dataset.name+' <span class="pan">'+o.dataset.pan+'</span>';});})();
```
