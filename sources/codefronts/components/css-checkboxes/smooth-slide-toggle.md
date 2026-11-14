---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/smooth-slide-toggle/"
title: "Smooth Slide Toggle"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A toggle whose indicator glides continuously across the track on a single compositor-only property."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smooth Slide Toggle
Source: https://codefronts.com/components/css-checkboxes/smooth-slide-toggle/

A toggle whose indicator glides continuously across the track on a single compositor-only property. Purpose-built for buttery 60fps motion — the thumb rides entirely on the GPU via translate3d, with inline ON/OFF copy for extra clarity.
## HTML
```html
<section class="cb-07" aria-label="Smooth slide toggles">
  <div class="cb-07__stack">
    <label class="cb-07__row"><span class="cb-07__name">Auto-save drafts</span>
      <input type="checkbox" class="cb-07__input" checked>
      <span class="cb-07__track" data-on="ON" data-off="OFF"><span class="cb-07__thumb"></span></span>
    </label>
    <label class="cb-07__row"><span class="cb-07__name">Compact density</span>
      <input type="checkbox" class="cb-07__input">
      <span class="cb-07__track" data-on="ON" data-off="OFF"><span class="cb-07__thumb"></span></span>
    </label>
    <label class="cb-07__row"><span class="cb-07__name">Beta features</span>
      <input type="checkbox" class="cb-07__input">
      <span class="cb-07__track" data-on="ON" data-off="OFF"><span class="cb-07__thumb"></span></span>
    </label>
  </div>
</section>
```
## CSS
```css
.cb-07,
.cb-07 *,
.cb-07 *::before,
.cb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-07 ::selection {
  background: oklch(0.6 0.15 200);
  color: #fff;
}

.cb-07 {
  --on: oklch(0.58 0.13 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef2f3;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-07__stack {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.cb-07__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dde3e5;
  border-radius: 12px;
  padding: 14px 18px;
}

.cb-07__name {
  font-size: 14.5px;
  font-weight: 600;
  color: #28323a;
}

.cb-07__input {
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

.cb-07__track {
  --w: 66px;
  --h: 30px;
  position: relative;
  flex: none;
  width: var(--w);
  height: var(--h);
  border-radius: 999px;
  background: #c3ccd0;
  transition: background .3s ease;
  overflow: hidden;
}

.cb-07__track::before,
.cb-07__track::after {
  position: absolute;
  top: 0;
  height: var(--h);
  display: flex;
  align-items: center;
  font: 700 10px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
  transition: opacity .25s;
}

.cb-07__track::before {
  content: attr(data-on);
  left: 11px;
  color: #fff;
  opacity: 0;
}

.cb-07__track::after {
  content: attr(data-off);
  right: 11px;
  color: #5b6a70;
  opacity: 1;
}

.cb-07__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: calc(var(--h) - 6px);
  height: calc(var(--h) - 6px);
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(20,30,40,.4);
  will-change: transform;
  transform: translate3d(0,0,0);
  transition: transform .32s cubic-bezier(.4,.9,.3,1);
}

.cb-07__input:checked ~ .cb-07__track {
  background: var(--on);
}

.cb-07__input:checked ~ .cb-07__track::before {
  opacity: 1;
}

.cb-07__input:checked ~ .cb-07__track::after {
  opacity: 0;
}

.cb-07__input:checked ~ .cb-07__track .cb-07__thumb {
  transform: translate3d(calc(var(--w) - var(--h)),0,0);
}

.cb-07__input:focus-visible ~ .cb-07__track {
  outline: 3px solid var(--on);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-07__track,
    .cb-07__thumb,
    .cb-07__track::before,
    .cb-07__track::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the thumb glides via GPU-composited translate3d on :checked. */
```
