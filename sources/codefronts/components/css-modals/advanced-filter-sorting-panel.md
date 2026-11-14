---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/advanced-filter-sorting-panel/"
title: "Advanced Filter & Sorting Panel"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A data-dense filter and sort panel that docks to the side on desktop and becomes a bottom sheet on mobile — sort radios, category checkboxes, a price range…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Advanced Filter & Sorting Panel
Source: https://codefronts.com/components/css-modals/advanced-filter-sorting-panel/

A data-dense filter and sort panel that docks to the side on desktop and becomes a bottom sheet on mobile — sort radios, category checkboxes, a price range and colour swatches, with a live result count, Apply and Clear.
## HTML
```html
<div class="cm-15">
  <button class="cm-15__open" type="button"><span aria-hidden="true">⚙</span> Filter &amp; sort</button>

  <dialog class="cm-15__dlg" aria-labelledby="cm-15-title">
    <form class="cm-15__card" method="dialog">
      <header class="cm-15__head">
        <h2 id="cm-15-title">Filter &amp; sort</h2>
        <button class="cm-15__x" type="button" aria-label="Close panel">&times;</button>
      </header>

      <div class="cm-15__scroll">
        <fieldset class="cm-15__group"><legend>Sort by</legend>
          <label class="cm-15__radio"><input type="radio" name="cm-15-sort" checked> Featured</label>
          <label class="cm-15__radio"><input type="radio" name="cm-15-sort"> Price: low to high</label>
          <label class="cm-15__radio"><input type="radio" name="cm-15-sort"> Price: high to low</label>
          <label class="cm-15__radio"><input type="radio" name="cm-15-sort"> Newest</label>
        </fieldset>

        <fieldset class="cm-15__group"><legend>Category</legend>
          <label class="cm-15__check"><input type="checkbox" class="cm-15__f" checked> Outerwear <span>(128)</span></label>
          <label class="cm-15__check"><input type="checkbox" class="cm-15__f"> Knitwear <span>(64)</span></label>
          <label class="cm-15__check"><input type="checkbox" class="cm-15__f" checked> Accessories <span>(42)</span></label>
          <label class="cm-15__check"><input type="checkbox" class="cm-15__f"> Footwear <span>(31)</span></label>
        </fieldset>

        <fieldset class="cm-15__group"><legend>Max price — <output id="cm-15-out">$220</output></legend>
          <input type="range" id="cm-15-price" class="cm-15__range" min="20" max="400" step="10" value="220" aria-label="Maximum price">
        </fieldset>

        <fieldset class="cm-15__group"><legend>Colour</legend>
          <div class="cm-15__swatches">
            <label class="cm-15__sw" style="--sw:#3a4a3f"><input type="checkbox" aria-label="Forest"></label>
            <label class="cm-15__sw" style="--sw:#5a3f2f"><input type="checkbox" aria-label="Rust"></label>
            <label class="cm-15__sw" style="--sw:#2c3440"><input type="checkbox" aria-label="Slate"></label>
            <label class="cm-15__sw" style="--sw:#c9b58a"><input type="checkbox" aria-label="Sand"></label>
            <label class="cm-15__sw" style="--sw:#7a2f3a"><input type="checkbox" aria-label="Wine"></label>
          </div>
        </fieldset>
      </div>

      <footer class="cm-15__foot">
        <button type="button" class="cm-15__clear">Clear all</button>
        <button type="button" class="cm-15__apply">Show <span id="cm-15-n">170</span> results</button>
      </footer>
    </form>
  </dialog>
</div>
```
## CSS
```css
.cm-15,
.cm-15 *,
.cm-15 *::before,
.cm-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-15 {
  --accent: oklch(0.72 0.13 200);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0c1113,#07090a);
}

.cm-15__open {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  padding: 13px 24px;
  border-radius: 11px;
  color: #e6f1f3;
  font: 600 14px system-ui;
  border: 1px solid #23323a;
  background: #111a1d;
  transition: border-color .2s,background .2s;
}

.cm-15__open:hover {
  border-color: var(--accent);
  background: #152226;
}

.cm-15__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-15__dlg {
  margin: 0 0 0 auto;
  height: 100%;
  max-height: 100dvh;
  width: min(380px,100vw);
  padding: 0;
  border: none;
  color: #e7eef0;
  background: linear-gradient(180deg,#131a1d,#0e1416);
  box-shadow: -30px 0 80px -20px #000;
  transform: translateX(100%);
  transition: transform .34s cubic-bezier(.4,0,.2,1),overlay .34s allow-discrete,display .34s allow-discrete;
}

.cm-15__dlg[open] {
  transform: none;
}

@starting-style {
  .cm-15__dlg[open] {
    transform: translateX(100%);
  }
}

.cm-15__dlg::backdrop {
  background: rgba(4,7,8,0);
  transition: background .34s,overlay .34s allow-discrete,display .34s allow-discrete;
}

.cm-15__dlg[open]::backdrop {
  background: rgba(4,7,8,.55);
}

@starting-style {
  .cm-15__dlg[open]::backdrop {
    background: rgba(4,7,8,0);
  }
}

.cm-15__card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.cm-15__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 22px;
  border-bottom: 1px solid #202b30;
}

.cm-15__head h2 {
  font-size: 17px;
  font-weight: 700;
  color: #f0f6f7;
}

.cm-15__x {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #88969a;
  font-size: 22px;
  cursor: pointer;
}

.cm-15__x:hover {
  background: #1a2529;
  color: #fff;
}

.cm-15__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-15__scroll {
  flex: 1;
  overflow: auto;
  padding: 8px 22px;
}

.cm-15__group {
  border: none;
  padding: 16px 0;
  border-bottom: 1px solid #1c262a;
}

.cm-15__group legend {
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #8b999d;
  margin-bottom: 12px;
}

.cm-15__group output {
  color: var(--accent);
  font-weight: 700;
  letter-spacing: 0;
  text-transform: none;
}

.cm-15__radio,
.cm-15__check {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 8px 0;
  font-size: 14px;
  color: #c7d0d3;
  cursor: pointer;
}

.cm-15__check span {
  margin-left: auto;
  font-size: 12px;
  color: #788589;
}

.cm-15__radio input,
.cm-15__check input {
  width: 18px;
  height: 18px;
  accent-color: var(--accent);
  cursor: pointer;
}

.cm-15__radio input:focus-visible,
.cm-15__check input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-15__range {
  width: 100%;
  accent-color: var(--accent);
  cursor: pointer;
}

.cm-15__range:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
  border-radius: 4px;
}

.cm-15__swatches {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.cm-15__sw {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  background: var(--sw);
  cursor: pointer;
  position: relative;
  box-shadow: inset 0 0 0 2px #0e1416,0 0 0 1px #2c3a3e;
}

.cm-15__sw input {
  position: absolute;
  opacity: 0;
  inset: 0;
  cursor: pointer;
}

.cm-15__sw:has(:checked) {
  box-shadow: inset 0 0 0 2px #0e1416,0 0 0 2px var(--accent);
}

.cm-15__sw:has(:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cm-15__foot {
  display: flex;
  gap: 12px;
  padding: 16px 22px;
  border-top: 1px solid #202b30;
  background: #0f1618;
}

.cm-15__clear {
  padding: 13px 18px;
  border-radius: 11px;
  border: 1px solid #2a373b;
  background: #131c1f;
  color: #d0dadc;
  font: 600 14px system-ui;
  cursor: pointer;
  transition: all .18s;
}

.cm-15__clear:hover {
  border-color: #3a4a4e;
  background: #182225;
}

.cm-15__apply {
  flex: 1;
  padding: 13px;
  border: none;
  border-radius: 11px;
  background: var(--accent);
  color: #04161a;
  font: 700 14.5px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-15__apply:hover {
  filter: brightness(1.08);
}

.cm-15__apply:active {
  transform: translateY(1px);
}

.cm-15__clear:focus-visible,
.cm-15__apply:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (max-width: 520px) {
  .cm-15__dlg {
    margin: auto 0 0;
    width: 100vw;
    height: auto;
    max-height: 86dvh;
    border-radius: 20px 20px 0 0;
    transform: translateY(100%);
  }

  .cm-15__dlg[open] {
    transform: none;
  }

  @starting-style {
    .cm-15__dlg[open] {
      transform: translateY(100%);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .cm-15__dlg,
    .cm-15__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-15');
  var dlg = root.querySelector('.cm-15__dlg');
  var out = root.querySelector('#cm-15-out');
  var price = root.querySelector('#cm-15-price');
  var n = root.querySelector('#cm-15-n');
  root.querySelector('.cm-15__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-15__x').addEventListener('click', function(){ dlg.close(); });
  price.addEventListener('input', function(){ out.textContent = '$' + price.value; recount(); });
  function recount(){
    // toy live count so the demo feels real
    var cats = root.querySelectorAll('.cm-15__f:checked').length;
    var base = cats * 42 + Math.round((price.value - 20) / 380 * 40);
    n.textContent = Math.max(0, base);
  }
  root.querySelectorAll('.cm-15__f').forEach(function(c){ c.addEventListener('change', recount); });
  root.querySelector('.cm-15__apply').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-15__clear').addEventListener('click', function(){
    root.querySelectorAll('.cm-15__card input[type=checkbox]').forEach(function(c){ c.checked = false; });
    root.querySelector('.cm-15__radio input').checked = true;
    price.value = 220; out.textContent = '$220'; recount();
  });
  recount();
})();
```
