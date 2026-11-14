---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/solar-flare/"
title: "CSS Date-Range Preset Button Group with Cursor-Following Glow (Spotlight Hover)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A date-range preset group — Today / 7d / 30d / Quarter / Year — lit by a solar-flare spotlight that tracks your cursor across the whole group, with the…"
has_js: "true"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Date-Range Preset Button Group with Cursor-Following Glow (Spotlight Hover)
Source: https://codefronts.com/components/css-button-groups/solar-flare/

A date-range preset group — Today / 7d / 30d / Quarter / Year — lit by a solar-flare spotlight that tracks your cursor across the whole group, with the hovered preset flaring brightest and one preset selected. The polished 'CSS cursor-following glow button group' spotlight effect for analytics dashboards and reporting filters.
## HTML
```html
<section class="btn-25" aria-label="Cursor-following glow date range presets demo">
  <div class="btn-25__wrap">
    <p class="btn-25__label">Date range</p>
    <div class="btn-25__group" id="btn-25-group" role="radiogroup" aria-label="Date range preset" style="--mx:50%;--my:50%">
      <input type="radio" name="btn-25" id="btn-25-1" class="btn-25__in">
      <label for="btn-25-1" class="btn-25__btn">Today</label>
      <input type="radio" name="btn-25" id="btn-25-2" class="btn-25__in" checked>
      <label for="btn-25-2" class="btn-25__btn">Last 7 days</label>
      <input type="radio" name="btn-25" id="btn-25-3" class="btn-25__in">
      <label for="btn-25-3" class="btn-25__btn">Last 30 days</label>
      <input type="radio" name="btn-25" id="btn-25-4" class="btn-25__in">
      <label for="btn-25-4" class="btn-25__btn">Quarter</label>
      <input type="radio" name="btn-25" id="btn-25-5" class="btn-25__in">
      <label for="btn-25-5" class="btn-25__btn">Year</label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-25,
.btn-25 *,
.btn-25 *::before,
.btn-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-25 {
  --accent: oklch(0.78 0.16 65);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(130% 120% at 50% 0%,#1e130a,#0b0705);
  padding: 44px 20px;
}

.btn-25__wrap {
  width: min(620px,100%);
}

.btn-25__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 16px 2px;
}

.btn-25__group {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.btn-25__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-25__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 50px;
  padding: 0 22px;
  font-size: 15px;
  font-weight: 700;
  color: #c8b49a;
  background: #1b120b;
  border: 1.5px solid #362619;
  border-radius: 13px;
  cursor: pointer;
  transition: color .2s,border-color .2s;
}

.btn-25__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: radial-gradient(220px circle at var(--mx) var(--my),color-mix(in oklab,var(--accent) 55%,transparent),transparent 60%);
  opacity: 0;
  transition: opacity .3s;
}

.btn-25__group:hover .btn-25__btn::before {
  opacity: 1;
}

.btn-25__btn:hover {
  color: #fff2e2;
  border-color: var(--accent);
}

.btn-25__in:checked + .btn-25__btn {
  color: #1a0f06;
  background: var(--accent);
  border-color: var(--accent);
  box-shadow: 0 8px 24px -10px var(--accent);
}

.btn-25__in:focus-visible + .btn-25__btn {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-25__btn,
    .btn-25__btn::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* One small enhancement: track the pointer and write --mx/--my so a single solar-flare spotlight glides across the whole group. Selection stays pure-CSS via radios, so it works without JS (falling back to a centered hover glow). */
(function(){
  var g = document.getElementById('btn-25-group');
  if(!g) return;
  function move(e){
    var r = g.getBoundingClientRect();
    var btns = g.querySelectorAll('.btn-25__btn');
    btns.forEach(function(b){
      var br = b.getBoundingClientRect();
      b.style.setProperty('--mx', (e.clientX - br.left) + 'px');
      b.style.setProperty('--my', (e.clientY - br.top) + 'px');
    });
  }
  g.addEventListener('pointermove', move, {passive:true});
})();
```
