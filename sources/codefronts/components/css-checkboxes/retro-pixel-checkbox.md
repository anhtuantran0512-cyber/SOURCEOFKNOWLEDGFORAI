---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/retro-pixel-checkbox/"
title: "Retro Pixel Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "8-bit nostalgia: a jagged, aliased checkmark built entirely from stacked box-shadow 'pixels' — no image files, no SVG."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Pixel Checkbox
Source: https://codefronts.com/components/css-checkboxes/retro-pixel-checkbox/

8-bit nostalgia: a jagged, aliased checkmark built entirely from stacked box-shadow 'pixels' — no image files, no SVG. Snaps in blocky and hard-edged, perfect for game UIs, dev tools with personality and retro landing pages.
## HTML
```html
<section class="cb-19" aria-label="Retro pixel checkboxes">
  <div class="cb-19__panel">
    <label class="cb-19__row"><input type="checkbox" class="cb-19__input" checked><span class="cb-19__box" aria-hidden="true"><span class="cb-19__px"></span></span><span class="cb-19__label">INSERT COIN</span></label>
    <label class="cb-19__row"><input type="checkbox" class="cb-19__input"><span class="cb-19__box" aria-hidden="true"><span class="cb-19__px"></span></span><span class="cb-19__label">CONTINUE?</span></label>
    <label class="cb-19__row"><input type="checkbox" class="cb-19__input"><span class="cb-19__box" aria-hidden="true"><span class="cb-19__px"></span></span><span class="cb-19__label">EXTRA LIFE</span></label>
  </div>
</section>
```
## CSS
```css
.cb-19,
.cb-19 *,
.cb-19 *::before,
.cb-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-19 ::selection {
  background: #39ff6a;
  color: #04120a;
}

.cb-19 {
  --accent: #2a2f45;
  --c: #39ff6a;
  --p: 3px;
  font-family: ui-monospace,'Courier New',monospace;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #12131f;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-19__panel {
  width: min(400px,100%);
  background: #1b1d2e;
  border: 2px solid #2f3350;
  padding: 10px 14px;
}

.cb-19__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-19__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-19__box {
  position: relative;
  flex: none;
  width: 28px;
  height: 28px;
  background: #0e0f18;
  border: 2px solid #4a5080;
  transition: background .12s steps(2),border-color .12s;
}

.cb-19__px {
  position: absolute;
  left: 5px;
  top: 13px;
  width: var(--p);
  height: var(--p);
  background: transparent;
  opacity: 0;
  transition: opacity .1s steps(2);
}

.cb-19__input:checked ~ .cb-19__box {
  background: var(--accent);
  border-color: var(--c);
}

.cb-19__input:checked ~ .cb-19__box .cb-19__px {
  opacity: 1;
  background: var(--c);
  box-shadow: calc(1*var(--p)) calc(1*var(--p)) 0 var(--c), calc(2*var(--p)) calc(2*var(--p)) 0 var(--c), calc(3*var(--p)) calc(1*var(--p)) 0 var(--c), calc(4*var(--p)) calc(0*var(--p)) 0 var(--c), calc(5*var(--p)) calc(-1*var(--p)) 0 var(--c), calc(6*var(--p)) calc(-2*var(--p)) 0 var(--c);
}

.cb-19__input:focus-visible ~ .cb-19__box {
  outline: 3px solid var(--c);
  outline-offset: 3px;
}

.cb-19__label {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .08em;
  color: #c8ccec;
}

@media (prefers-reduced-motion: reduce) {
  .cb-19__box,
    .cb-19__px {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a stacked box-shadow pixel list draws the check on :checked. */
```
