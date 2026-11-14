---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-toggle-button-group-with-radio-inputs-single-select-alignment-group/"
title: "CSS Toggle Button Group with Radio Inputs (Single-Select Alignment Group)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The classic single-select toggle group — text-align Left / Center / Right / Justify — where exactly one option stays pressed at a time."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toggle Button Group with Radio Inputs (Single-Select Alignment Group)
Source: https://codefronts.com/components/css-button-groups/css-toggle-button-group-with-radio-inputs-single-select-alignment-group/

The classic single-select toggle group — text-align Left / Center / Right / Justify — where exactly one option stays pressed at a time. The canonical 'CSS toggle button group radio inputs' pattern for editor controls and settings, using genuine radios so only one is ever active, keyboard arrows move between them, and the pressed state is announced natively.
## HTML
```html
<section class="btn-09" aria-label="Toggle button group demo">
  <div class="btn-09__wrap">
    <p class="btn-09__label">Text alignment</p>
    <div class="btn-09__group" role="radiogroup" aria-label="Text alignment">
      <input type="radio" name="btn-09" id="btn-09-1" class="btn-09__in" checked>
      <label for="btn-09-1" class="btn-09__btn" aria-label="Align left"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 6h16M4 11h10M4 16h14M4 21h8"/></svg></label>
      <input type="radio" name="btn-09" id="btn-09-2" class="btn-09__in">
      <label for="btn-09-2" class="btn-09__btn" aria-label="Align center"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 6h16M7 11h10M5 16h14M8 21h8"/></svg></label>
      <input type="radio" name="btn-09" id="btn-09-3" class="btn-09__in">
      <label for="btn-09-3" class="btn-09__btn" aria-label="Align right"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 6h16M10 11h10M6 16h14M12 21h8"/></svg></label>
      <input type="radio" name="btn-09" id="btn-09-4" class="btn-09__in">
      <label for="btn-09-4" class="btn-09__btn" aria-label="Justify"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 6h16M4 11h16M4 16h16M4 21h16"/></svg></label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-09,
.btn-09 *,
.btn-09 *::before,
.btn-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-09 {
  --accent: oklch(0.5 0.13 155);
  --gold: oklch(0.78 0.13 85);
  --ink: #20301f;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,#f7f5ec,#eef1e4);
  padding: 44px 20px;
}

.btn-09__wrap {
  width: min(420px,100%);
}

.btn-09__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 14px 4px;
}

.btn-09__group {
  display: inline-flex;
  padding: 5px;
  gap: 4px;
  background: #fff;
  border: 1px solid #e3e6d6;
  border-radius: 15px;
  box-shadow: 0 14px 34px -22px rgba(40,60,30,.5);
}

.btn-09__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-09__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 46px;
  height: 46px;
  color: #5c6b52;
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s,color .15s,box-shadow .15s;
}

.btn-09__btn:hover {
  background: #f0f2e6;
  color: var(--ink);
}

.btn-09__in:checked + .btn-09__btn {
  background: var(--accent);
  color: #fff;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.3);
}

.btn-09__in:checked + .btn-09__btn::after {
  content: "";
  position: absolute;
  bottom: 6px;
  width: 14px;
  height: 2px;
  border-radius: 2px;
  background: var(--gold);
}

.btn-09__btn {
  position: relative;
}

.btn-09__in:focus-visible + .btn-09__btn {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-09__btn {
    transition: none;
  }
}
```
