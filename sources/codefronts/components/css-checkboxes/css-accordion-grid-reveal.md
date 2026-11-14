---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/css-accordion-grid-reveal/"
title: "CSS Accordion Grid Reveal"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A pure-CSS FAQ / disclosure list where each checkbox expands its panel with a genuinely smooth height transition — no max-height guesswork, no JavaScript."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Accordion Grid Reveal
Source: https://codefronts.com/components/css-checkboxes/css-accordion-grid-reveal/

A pure-CSS FAQ / disclosure list where each checkbox expands its panel with a genuinely smooth height transition — no max-height guesswork, no JavaScript. Built on the modern grid-rows 0fr→1fr technique.
## HTML
```html
<section class="cb-04" aria-label="Frequently asked questions">
  <div class="cb-04__list">
    <div class="cb-04__item">
      <input type="checkbox" class="cb-04__input" id="cb-04-1" checked>
      <label class="cb-04__head" for="cb-04-1">What browsers are supported?<span class="cb-04__chev" aria-hidden="true"></span></label>
      <div class="cb-04__panel"><div class="cb-04__inner">Every evergreen browser — Chrome, Edge, Safari and Firefox. The grid-row reveal degrades to an instant open in legacy engines.</div></div>
    </div>
    <div class="cb-04__item">
      <input type="checkbox" class="cb-04__input" id="cb-04-2">
      <label class="cb-04__head" for="cb-04-2">Is there any JavaScript?<span class="cb-04__chev" aria-hidden="true"></span></label>
      <div class="cb-04__panel"><div class="cb-04__inner">None. The open/close state is the checkbox itself, and the height animation is pure CSS via grid-template-rows.</div></div>
    </div>
    <div class="cb-04__item">
      <input type="checkbox" class="cb-04__input" id="cb-04-3">
      <label class="cb-04__head" for="cb-04-3">Can multiple panels stay open?<span class="cb-04__chev" aria-hidden="true"></span></label>
      <div class="cb-04__panel"><div class="cb-04__inner">Yes — these are independent checkboxes. Swap them for radios with a shared name to force a single-open accordion.</div></div>
    </div>
  </div>
</section>
```
## CSS
```css
.cb-04,
.cb-04 *,
.cb-04 *::before,
.cb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-04 ::selection {
  background: oklch(0.62 0.16 250);
  color: #fff;
}

.cb-04 {
  --accent: oklch(0.62 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-04__list {
  width: min(560px,100%);
  background: #fff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 18px 40px -30px rgba(16,24,40,.5);
}

.cb-04__item {
  border-bottom: 1px solid #eef0f3;
}

.cb-04__item:last-child {
  border-bottom: 0;
}

.cb-04__input {
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

.cb-04__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  cursor: pointer;
  padding: 18px 22px;
  font-size: 15px;
  font-weight: 600;
  color: #1f2430;
}

.cb-04__chev {
  width: 11px;
  height: 11px;
  flex: none;
  border-right: 2.5px solid #9aa0ac;
  border-bottom: 2.5px solid #9aa0ac;
  transform: rotate(45deg);
  transition: transform .3s ease;
}

.cb-04__input:checked ~ .cb-04__head .cb-04__chev {
  transform: rotate(-135deg);
}

.cb-04__input:focus-visible ~ .cb-04__head {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

.cb-04__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s ease;
}

.cb-04__input:checked ~ .cb-04__panel {
  grid-template-rows: 1fr;
}

.cb-04__inner {
  overflow: hidden;
  font-size: 13.5px;
  line-height: 1.6;
  color: #6b7280;
  padding: 0 22px;
}

.cb-04__input:checked ~ .cb-04__panel .cb-04__inner {
  padding-bottom: 20px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-04__panel,
    .cb-04__chev {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — input:checked ~ .panel animates grid-template-rows 0fr→1fr. */
```
