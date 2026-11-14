---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/bootstrap-5-faq-accordion-customization/"
title: "Bootstrap 5 FAQ Accordion Customization"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "How to make a Bootstrap 5 accordion stop looking like Bootstrap: the stock .accordion markup restyled entirely through the --bs-accordion-* CSS custom…"
has_js: "true"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 FAQ Accordion Customization
Source: https://codefronts.com/snippets/css-faq-accordion/bootstrap-5-faq-accordion-customization/

How to make a Bootstrap 5 accordion stop looking like Bootstrap: the stock .accordion markup restyled entirely through the --bs-accordion-* CSS custom properties Bootstrap 5.2+ exposes — no Sass rebuild, no !important wars, no source diving. The demo shows a stock-look item and the customized theme side by side from identical markup, with a annotated variable map of the 10 properties that matter. Ships with a 12-line collapse shim so the preview runs without bootstrap.js; in a real Bootstrap project you delete it.
## HTML
```html
<section class="cfa-23" aria-label="Bootstrap 5 accordion customization">
  <div class="cfa-23__wrap">
    <header class="cfa-23__head">
      <h1>De-Bootstrapping the accordion</h1>
      <p>Identical <code>.accordion</code> markup — the theme below is nothing but <code>--bs-accordion-*</code> variable overrides.</p>
    </header>
    <div class="accordion faq-custom" id="cfa23-acc">
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#cfa23-c1" aria-expanded="true" aria-controls="cfa23-c1">Why theme with CSS variables instead of Sass?</button>
        </h2>
        <div id="cfa23-c1" class="accordion-collapse collapse show" data-bs-parent="#cfa23-acc">
          <div class="accordion-body">No build step, no fork of Bootstrap's source, and the overrides survive Bootstrap patch updates untouched. Sass remains the right tool for structural changes — spacing scales, breakpoints — but paint belongs to the variables.</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#cfa23-c2" aria-expanded="false" aria-controls="cfa23-c2">Which variables actually matter?</button>
        </h2>
        <div id="cfa23-c2" class="accordion-collapse collapse" data-bs-parent="#cfa23-acc">
          <div class="accordion-body">Ten of the ~20 do the visible work: bg, color, border-color, border-radius, btn-color, btn-bg, active-bg, active-color, btn-focus-box-shadow, and the two btn-icon data-URIs. The rest are paddings you rarely touch.</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#cfa23-c3" aria-expanded="false" aria-controls="cfa23-c3">How do I recolor the chevron icon?</button>
        </h2>
        <div id="cfa23-c3" class="accordion-collapse collapse" data-bs-parent="#cfa23-acc">
          <div class="accordion-body">Supply your own SVG data-URIs for --bs-accordion-btn-icon and --bs-accordion-btn-active-icon with the stroke color baked in — background images can't inherit currentColor. Remember to encode # as %23 or the icon silently vanishes.</div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#cfa23-c4" aria-expanded="false" aria-controls="cfa23-c4">Does this survive Bootstrap upgrades?</button>
        </h2>
        <div id="cfa23-c4" class="accordion-collapse collapse" data-bs-parent="#cfa23-acc">
          <div class="accordion-body">Yes — that is the entire pitch. The variables are Bootstrap's public theming API from 5.2 onward; minor and patch releases keep them stable, unlike selector-override hacks that break on any internal refactor.</div>
        </div>
      </div>
    </div>
    <p class="cfa-23__foot">Preview runs on a 12-line collapse shim — delete it when real <code>bootstrap.bundle.js</code> is loaded. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
/* ── Part 1: minimal Bootstrap 5.3 accordion structure, so the preview runs without the CDN.
      In a real Bootstrap project, delete Part 1 — bootstrap.css provides it. ── */

.cfa-23,
.cfa-23 *,
.cfa-23 *::before,
.cfa-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: oklch(0.14 0.012 240);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: oklch(0.94 0.008 230);
}

.cfa-23__wrap {
  width: min(100%,640px);
}

.cfa-23__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-23__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: oklch(0.66 0.015 235);
}

.cfa-23__head code,
.cfa-23__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .87em;
  background: oklch(0.24 0.02 200);
  padding: 2px 6px;
  border-radius: 5px;
  color: oklch(0.8 0.13 165);
}

.cfa-23 .accordion {
  margin-top: 24px;
}

.cfa-23 .accordion-item {
  color: var(--bs-accordion-color);
  background: var(--bs-accordion-bg);
  border: 1px solid var(--bs-accordion-border-color);
}

.cfa-23 .accordion-item:first-of-type {
  border-top-left-radius: var(--bs-accordion-border-radius);
  border-top-right-radius: var(--bs-accordion-border-radius);
}

.cfa-23 .accordion-item:last-of-type {
  border-bottom-left-radius: var(--bs-accordion-border-radius);
  border-bottom-right-radius: var(--bs-accordion-border-radius);
}

.cfa-23 .accordion-item:not(:first-of-type) {
  border-top: 0;
}

.cfa-23 .accordion-header {
  font-size: inherit;
}

.cfa-23 .accordion-button {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 48px;
  padding: 16px 18px;
  font: inherit;
  font-size: 15px;
  font-weight: 650;
  text-align: left;
  color: var(--bs-accordion-btn-color);
  background: var(--bs-accordion-btn-bg);
  border: 0;
  border-radius: 0;
  cursor: pointer;
  transition: background .25s,color .25s,border-radius .15s;
}

.cfa-23 .accordion-item:first-of-type .accordion-button {
  border-top-left-radius: var(--bs-accordion-inner-border-radius);
  border-top-right-radius: var(--bs-accordion-inner-border-radius);
}

.cfa-23 .accordion-button:not(.collapsed) {
  color: var(--bs-accordion-active-color);
  background: var(--bs-accordion-active-bg);
}

.cfa-23 .accordion-button:focus-visible {
  outline: 0;
  box-shadow: var(--bs-accordion-btn-focus-box-shadow);
  position: relative;
  z-index: 2;
}

.cfa-23 .accordion-button::after {
  content: "";
  flex-shrink: 0;
  width: 18px;
  height: 18px;
  margin-left: auto;
  background-image: var(--bs-accordion-btn-icon);
  background-size: 18px;
  background-repeat: no-repeat;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.cfa-23 .accordion-button:not(.collapsed)::after {
  background-image: var(--bs-accordion-btn-active-icon);
  transform: rotate(-180deg);
}

.cfa-23 .accordion-collapse {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s cubic-bezier(.4,0,.2,1);
}

.cfa-23 .accordion-collapse.show {
  grid-template-rows: 1fr;
}

.cfa-23 .accordion-body {
  overflow: hidden;
  min-height: 0;
  padding: 0 18px;
  font-size: 13.5px;
  line-height: 1.7;
  color: oklch(0.66 0.015 235);
}

.cfa-23 .accordion-collapse.show .accordion-body {
  padding-bottom: 17px;
}
/* ── Part 2: THE ACTUAL DEMO — your theme, pure --bs-accordion-* overrides ── */

.cfa-23 .faq-custom {
  --bs-accordion-bg: #101418;
  --bs-accordion-color: #e8edf2;
  --bs-accordion-border-color: #232b33;
  --bs-accordion-border-radius: 14px;
  --bs-accordion-inner-border-radius: 13px;
  --bs-accordion-btn-color: #e8edf2;
  --bs-accordion-btn-bg: transparent;
  --bs-accordion-active-bg: #16202a;
  --bs-accordion-active-color: #7fd4a8;
  --bs-accordion-btn-focus-box-shadow: 0 0 0 3px rgba(127,212,168,.35);
  --bs-accordion-btn-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3 6l5 5 5-5' fill='none' stroke='%238a97a3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  --bs-accordion-btn-active-icon: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3 6l5 5 5-5' fill='none' stroke='%237fd4a8' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}

.cfa-23 .faq-custom .accordion-button:hover {
  color: #7fd4a8;
}

.cfa-23__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: oklch(0.66 0.015 235);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-23 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  /* Collapse shim for standalone preview ONLY — real bootstrap.bundle.js replaces this. */
  var root=document.querySelector('.cfa-23');if(!root||root.dataset.cfa23)return;root.dataset.cfa23='1';
  if(window.bootstrap&&window.bootstrap.Collapse)return;
  [].slice.call(root.querySelectorAll('[data-bs-toggle="collapse"]')).forEach(function(btn){
    btn.addEventListener('click',function(){
      var target=root.querySelector(btn.getAttribute('data-bs-target')),opening=!target.classList.contains('show');
      [].slice.call(root.querySelectorAll('.accordion-collapse.show')).forEach(function(c){
        if(c!==target){c.classList.remove('show');var b=root.querySelector('[data-bs-target="#'+c.id+'"]');b.classList.add('collapsed');b.setAttribute('aria-expanded','false');}
      });
      target.classList.toggle('show',opening);
      btn.classList.toggle('collapsed',!opening);
      btn.setAttribute('aria-expanded',String(opening));
    });
  });
})();
```
