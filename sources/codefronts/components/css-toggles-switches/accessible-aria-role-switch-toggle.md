---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/accessible-aria-role-switch-toggle/"
title: "Accessible ARIA role=switch Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The reference implementation to ship in a design system: a button[role=switch] toggle with correct aria-checked handling, visible state text, a spec-grade…"
has_js: "true"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA role=switch Toggle
Source: https://codefronts.com/components/css-toggles-switches/accessible-aria-role-switch-toggle/

The reference implementation to ship in a design system: a button[role=switch] toggle with correct aria-checked handling, visible state text, a spec-grade focus ring — and it stays fully functional and visible in Windows High Contrast / forced-colors mode, where most CSS toggles silently vanish.
## HTML
```html
<section class="tgl-27" aria-label="Accessible ARIA switch">
  <div class="tgl-27__card">
    <div class="tgl-27__head"><b>Live captions</b><span>Immediate effect · not a form value</span></div>
    <button type="button" class="tgl-27__btn" id="tgl-27-btn" role="switch" aria-checked="false">
      <span class="tgl-27__track" aria-hidden="true"><span class="tgl-27__thumb"></span></span>
      <span class="tgl-27__state" aria-hidden="true"><i class="tgl-27__off">Off</i><i class="tgl-27__on">On</i></span>
    </button>
    <p class="tgl-27__live" id="tgl-27-live" aria-live="polite"></p>
    <p class="tgl-27__note">Space or Enter toggles · survives Windows High Contrast</p>
  </div>
</section>
```
## CSS
```css
.tgl-27,
.tgl-27 *,
.tgl-27 *::before,
.tgl-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-27 {
  --on: oklch(0.6 0.15 250);
  --track: #d6d9e0;
  --ring: oklch(0.6 0.15 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #f5f6f9;
}

.tgl-27__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  background: #fff;
  border: 1px solid #e6e8ee;
  border-radius: 18px;
  padding: 28px 34px;
  width: min(340px,100%);
}

.tgl-27__head {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.tgl-27__head b {
  font-size: 17px;
  color: #242938;
}

.tgl-27__head span {
  font-size: 12.5px;
  color: #8a90a2;
}

.tgl-27__btn {
  display: flex;
  align-items: center;
  gap: 14px;
  border: none;
  background: none;
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 12px;
  font: inherit;
}

.tgl-27__track {
  position: relative;
  display: block;
  width: 60px;
  height: 34px;
  border-radius: 18px;
  background: var(--track);
  transition: background-color .25s;
}

.tgl-27__btn[aria-checked="true"] .tgl-27__track {
  background: var(--on);
}

.tgl-27__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(25,30,60,.35);
  transition: transform .25s cubic-bezier(.3,1,.35,1.05);
}

.tgl-27__btn[aria-checked="true"] .tgl-27__thumb {
  transform: translateX(26px);
}

.tgl-27__state {
  position: relative;
  width: 32px;
  height: 1.3em;
  font-size: 15px;
  font-weight: 700;
  color: #3c4358;
  text-align: left;
}

.tgl-27__state i {
  position: absolute;
  inset: 0;
  font-style: normal;
  transition: opacity .2s;
}

.tgl-27__on {
  opacity: 0;
}

.tgl-27__btn[aria-checked="true"] .tgl-27__off {
  opacity: 0;
}

.tgl-27__btn[aria-checked="true"] .tgl-27__on {
  opacity: 1;
  color: var(--on);
}

.tgl-27__btn:focus-visible {
  outline: 3px solid var(--ring);
  outline-offset: 2px;
}

.tgl-27__live {
  font-size: 12.5px;
  color: #8a90a2;
  min-height: 1.2em;
}

.tgl-27__note {
  font-size: 11.5px;
  color: #a7acbc;
  text-align: center;
}

@media (forced-colors: active) {
  .tgl-27__track {
    background: Canvas;
    border: 2px solid ButtonText;
  }

  .tgl-27__btn[aria-checked="true"] .tgl-27__track {
    background: Highlight;
    border-color: Highlight;
  }

  .tgl-27__thumb {
    background: ButtonText;
    border: 2px solid ButtonText;
    box-shadow: none;
  }

  .tgl-27__btn[aria-checked="true"] .tgl-27__thumb {
    background: Canvas;
    border-color: Canvas;
  }

  .tgl-27__btn:focus-visible {
    outline: 3px solid Highlight;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tgl-27__track,
    .tgl-27__thumb,
    .tgl-27__state i {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('#tgl-27-btn');
  const live = document.querySelector('#tgl-27-live');
  btn.addEventListener('click', () => {
    const next = btn.getAttribute('aria-checked') !== 'true';
    btn.setAttribute('aria-checked', String(next));
    live.textContent = next ? 'Live captions on' : 'Live captions off';
  });
})();
```
