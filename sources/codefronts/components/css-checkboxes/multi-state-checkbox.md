---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/multi-state-checkbox/"
title: "Multi-State Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "One control that cycles through three discrete states on each activation — unset → yes → not-applicable — the pattern for review checklists, moderation…"
has_js: "true"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-State Checkbox
Source: https://codefronts.com/components/css-checkboxes/multi-state-checkbox/

One control that cycles through three discrete states on each activation — unset → yes → not-applicable — the pattern for review checklists, moderation queues and audit forms where a plain on/off isn't enough. Uses the accessible tri-state button role, not a fragile hack.
## HTML
```html
<section class="cb-25" id="cb-25" aria-label="Multi-state review checklist">
  <div class="cb-25__panel">
    <div class="cb-25__row"><button type="button" class="cb-25__btn" role="checkbox" aria-checked="true" data-cycle><span class="cb-25__box" aria-hidden="true"></span></button><span class="cb-25__label">Accessibility audit</span><span class="cb-25__state" aria-hidden="true"></span></div>
    <div class="cb-25__row"><button type="button" class="cb-25__btn" role="checkbox" aria-checked="mixed" data-cycle><span class="cb-25__box" aria-hidden="true"></span></button><span class="cb-25__label">Performance budget</span><span class="cb-25__state" aria-hidden="true"></span></div>
    <div class="cb-25__row"><button type="button" class="cb-25__btn" role="checkbox" aria-checked="false" data-cycle><span class="cb-25__box" aria-hidden="true"></span></button><span class="cb-25__label">Legal review</span><span class="cb-25__state" aria-hidden="true"></span></div>
  </div>
</section>
```
## CSS
```css
.cb-25,
.cb-25 *,
.cb-25 *::before,
.cb-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-25 ::selection {
  background: oklch(0.62 0.16 250);
  color: #fff;
}

.cb-25 {
  --yes: oklch(0.56 0.14 155);
  --na: oklch(0.68 0.13 70);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-25__panel {
  width: min(430px,100%);
  background: #fff;
  border: 1px solid #e6e8ec;
  border-radius: 14px;
  padding: 8px 14px;
}

.cb-25__row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 8px;
  border-bottom: 1px solid #f0f1f4;
}

.cb-25__row:last-child {
  border-bottom: 0;
}

.cb-25__btn {
  flex: none;
  padding: 0;
  border: 0;
  background: none;
  cursor: pointer;
  line-height: 0;
  border-radius: 8px;
}

.cb-25__box {
  position: relative;
  display: block;
  width: 24px;
  height: 24px;
  border-radius: 7px;
  border: 2px solid #c3c8d1;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-25__box::before,
.cb-25__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transition: opacity .18s;
}

.cb-25__box::before {
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-25__box::after {
  -webkit-mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E");
  mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E");
}

.cb-25__btn[aria-checked="true"] .cb-25__box {
  background: var(--yes);
  border-color: var(--yes);
}

.cb-25__btn[aria-checked="true"] .cb-25__box::before {
  opacity: 1;
}

.cb-25__btn[aria-checked="mixed"] .cb-25__box {
  background: var(--na);
  border-color: var(--na);
}

.cb-25__btn[aria-checked="mixed"] .cb-25__box::after {
  opacity: 1;
}

.cb-25__btn:focus-visible {
  outline: 3px solid oklch(0.62 0.16 250);
  outline-offset: 3px;
}

.cb-25__label {
  flex: 1;
  font-size: 14.5px;
  color: #2a2f3a;
}

.cb-25__state {
  font: 600 11px ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #9aa0aa;
}

.cb-25__btn[aria-checked="false"] ~ .cb-25__state::after {
  content: "unset";
}

.cb-25__btn[aria-checked="true"] ~ .cb-25__state::after {
  content: "done";
  color: var(--yes);
}

.cb-25__btn[aria-checked="mixed"] ~ .cb-25__state::after {
  content: "n/a";
  color: var(--na);
}

@media (prefers-reduced-motion: reduce) {
  .cb-25__box,
    .cb-25__box::before,
    .cb-25__box::after {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('cb-25');
  if(!root) return;
  var CYCLE = ['false','true','mixed'];
  root.querySelectorAll('[data-cycle]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var cur = btn.getAttribute('aria-checked') || 'false';
      var next = CYCLE[(CYCLE.indexOf(cur) + 1) % CYCLE.length];
      btn.setAttribute('aria-checked', next);
    });
  });
})();
```
