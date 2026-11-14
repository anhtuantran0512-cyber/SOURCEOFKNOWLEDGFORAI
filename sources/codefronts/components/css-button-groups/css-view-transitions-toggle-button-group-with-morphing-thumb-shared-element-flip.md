---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-view-transitions-toggle-button-group-with-morphing-thumb-shared-element-flip/"
title: "CSS View Transitions Toggle Button Group with Morphing Thumb (Shared-Element FLIP)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A toggle button group where the active highlight doesn't slide — it morphs."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS View Transitions Toggle Button Group with Morphing Thumb (Shared-Element FLIP)
Source: https://codefronts.com/components/css-button-groups/css-view-transitions-toggle-button-group-with-morphing-thumb-shared-element-flip/

A toggle button group where the active highlight doesn't slide — it morphs. Powered by the View Transitions API, the highlight is a shared element that the browser FLIP-animates from the old button to the new one, smoothly stretching across size and position changes. The forward-looking 'CSS View Transitions button group morphing highlight' pattern for 2027 UIs.
## HTML
```html
<section class="btn-03" aria-label="View transitions morphing toggle group demo">
  <div class="btn-03__wrap">
    <p class="btn-03__label">Workspace theme</p>
    <div class="btn-03__group" id="btn-03-group" role="radiogroup" aria-label="Workspace theme">
      <button type="button" class="btn-03__btn" role="radio" aria-checked="true" tabindex="0"><span class="btn-03__hl"></span><span class="btn-03__t">Focus</span></button>
      <button type="button" class="btn-03__btn" role="radio" aria-checked="false" tabindex="-1"><span class="btn-03__hl"></span><span class="btn-03__t">Comfortable</span></button>
      <button type="button" class="btn-03__btn" role="radio" aria-checked="false" tabindex="-1"><span class="btn-03__hl"></span><span class="btn-03__t">Compact</span></button>
      <button type="button" class="btn-03__btn" role="radio" aria-checked="false" tabindex="-1"><span class="btn-03__hl"></span><span class="btn-03__t">Zen</span></button>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-03,
.btn-03 *,
.btn-03 *::before,
.btn-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-03 {
  --accent: oklch(0.5 0.22 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,#f4f5fa,#e7e9f3);
  padding: 44px 20px;
}

.btn-03__wrap {
  width: min(560px,100%);
}

.btn-03__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 14px 4px;
}

.btn-03__group {
  display: inline-flex;
  gap: 6px;
  padding: 6px;
  background: #fff;
  border: 1px solid #e2e4f0;
  border-radius: 16px;
  box-shadow: 0 16px 40px -26px rgba(40,30,120,.5);
}

.btn-03__btn {
  position: relative;
  border: none;
  background: none;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 11px;
  font-size: 15px;
  font-weight: 700;
  color: #5a5f80;
  cursor: pointer;
  overflow: hidden;
  transition: color .2s;
}

.btn-03__hl {
  position: absolute;
  inset: 0;
  border-radius: 11px;
  background: var(--accent);
  opacity: 0;
}

.btn-03__t {
  position: relative;
  z-index: 1;
}

.btn-03__btn[aria-checked=true] {
  color: #fff;
}

.btn-03__btn[aria-checked=true] .btn-03__hl {
  opacity: 1;
  view-transition-name: btn-03-thumb;
  box-shadow: 0 6px 16px -6px var(--accent);
}

.btn-03__btn:not([aria-checked=true]):hover {
  color: #2a2e50;
}

.btn-03__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

::view-transition-group(btn-03-thumb) {
  animation-duration: .45s;
  animation-timing-function: cubic-bezier(.34,1.25,.4,1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(btn-03-thumb) {
    animation-duration: 1ms;
  }
}
```
