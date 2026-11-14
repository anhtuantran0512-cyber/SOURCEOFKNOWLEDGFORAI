---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-animated-toggle-switch-button/"
title: "CSS Animated Toggle Switch Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A collection of iOS-style animated toggle switches for dark mode, notifications, and auto-save — styled with pure CSS and driven by accessible checkbox inputs."
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Toggle Switch Button
Source: https://codefronts.com/motion/css-animated-buttons/css-animated-toggle-switch-button/

A collection of iOS-style animated toggle switches for dark mode, notifications, and auto-save — styled with pure CSS and driven by accessible checkbox inputs.
## HTML
```html
<div class="ab-17">
  <p class="ab-17__heading">Preferences</p>
  <div class="ab-17__list">
    <div class="ab-17__row" id="ab-17-row-0">
      <div class="ab-17__info">
        <p class="ab-17__title">Dark Mode</p>
        <p class="ab-17__status" id="ab-17-s0">Off</p>
      </div>
      <div class="ab-17__toggle" style="--on-color:#7c3aed">
        <input class="ab-17__input" type="checkbox" id="ab-17-t0" />
        <label class="ab-17__track" for="ab-17-t0"><span class="ab-17__knob"></span></label>
      </div>
    </div>
    <div class="ab-17__row" id="ab-17-row-1">
      <div class="ab-17__info">
        <p class="ab-17__title">Push Notifications</p>
        <p class="ab-17__status" id="ab-17-s1">Off</p>
      </div>
      <div class="ab-17__toggle" style="--on-color:#0891b2">
        <input class="ab-17__input" type="checkbox" id="ab-17-t1" />
        <label class="ab-17__track" for="ab-17-t1"><span class="ab-17__knob"></span></label>
      </div>
    </div>
    <div class="ab-17__row" id="ab-17-row-2">
      <div class="ab-17__info">
        <p class="ab-17__title">Auto-Save</p>
        <p class="ab-17__status" id="ab-17-s2">Off</p>
      </div>
      <div class="ab-17__toggle" style="--on-color:#059669">
        <input class="ab-17__input" type="checkbox" id="ab-17-t2" checked />
        <label class="ab-17__track" for="ab-17-t2"><span class="ab-17__knob"></span></label>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ab-17,
.ab-17 *,
.ab-17 *::before,
.ab-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-17 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-17 {
  font-family: system-ui,sans-serif;
  background: #f8fafc;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.ab-17__heading {
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #64748b;
  margin-bottom: 1.25rem;
  align-self: flex-start;
  max-width: 380px;
  width: 100%;
}

.ab-17__list {
  width: 100%;
  max-width: 380px;
  display: flex;
  flex-direction: column;
  gap: .5rem;
}

.ab-17__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: #fff;
  border-radius: 12px;
  border: 1.5px solid #e2e8f0;
  transition: border-color .3s,background .3s;
}

.ab-17__row.is-active {
  border-color: rgba(124,58,237,.3);
  background: #faf7ff;
}

.ab-17__title {
  font-size: .93rem;
  font-weight: 600;
  color: #1e293b;
}

.ab-17__status {
  font-size: .78rem;
  color: #94a3b8;
  margin-top: .15rem;
}

.ab-17__toggle {
  position: relative;
}

.ab-17__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.ab-17__track {
  --on-color: #7c3aed;
  display: flex;
  align-items: center;
  width: 50px;
  height: 28px;
  background: #cbd5e1;
  border-radius: 50px;
  cursor: pointer;
  transition: background .3s;
  padding: 3px;
}

.ab-17__input:checked+.ab-17__track {
  background: var(--on-color);
}

.ab-17__knob {
  width: 22px;
  height: 22px;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 1px 4px rgba(0,0,0,.2);
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.ab-17__input:checked+.ab-17__track .ab-17__knob {
  transform: translateX(22px);
}

.ab-17__input:focus-visible+.ab-17__track {
  outline: 2px solid #7c3aed;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .ab-17__knob,
    .ab-17__track,
    .ab-17__row {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var ids=[0,1,2];
  ids.forEach(function(i){
    var inp=document.getElementById('ab-17-t'+i);
    var status=document.getElementById('ab-17-s'+i);
    var row=document.getElementById('ab-17-row-'+i);
    if(!inp||!status||!row)return;
    function update(){
      var on=inp.checked;
      status.textContent=on?'On':'Off';
      row.classList.toggle('is-active',on);
    }
    update();
    inp.addEventListener('change',update);
  });
})();
```
