---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-pill-radio-button-group-with-sliding-indicator-filter-pills-pure-css/"
title: "CSS Pill Radio Button Group with Sliding Indicator (Filter Pills, Pure CSS)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A row of pill-shaped filter buttons — All / Design / Engineering / Growth — with a single highlight that slides between the selected pill."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pill Radio Button Group with Sliding Indicator (Filter Pills, Pure CSS)
Source: https://codefronts.com/components/css-button-groups/css-pill-radio-button-group-with-sliding-indicator-filter-pills-pure-css/

A row of pill-shaped filter buttons — All / Design / Engineering / Growth — with a single highlight that slides between the selected pill. The most-searched 'CSS pill radio button group sliding indicator' for content filters and category tabs, built on real radio inputs so it's keyboard-navigable and announces selection state out of the box.
## HTML
```html
<section class="btn-08" aria-label="Pill radio button group demo">
  <div class="btn-08__wrap">
    <p class="btn-08__label">Browse by team</p>
    <div class="btn-08__pills" role="group" aria-label="Filter by team" style="--x:0px;--w:60px">
      <input type="radio" name="btn-08" id="btn-08-1" class="btn-08__in" checked>
      <label for="btn-08-1" class="btn-08__pill" style="--x:4px;--w:56px">All</label>
      <input type="radio" name="btn-08" id="btn-08-2" class="btn-08__in">
      <label for="btn-08-2" class="btn-08__pill" style="--x:64px;--w:92px">Design</label>
      <input type="radio" name="btn-08" id="btn-08-3" class="btn-08__in">
      <label for="btn-08-3" class="btn-08__pill" style="--x:160px;--w:126px">Engineering</label>
      <input type="radio" name="btn-08" id="btn-08-4" class="btn-08__in">
      <label for="btn-08-4" class="btn-08__pill" style="--x:290px;--w:82px">Growth</label>
      <span class="btn-08__ind" aria-hidden="true"></span>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-08,
.btn-08 *,
.btn-08 *::before,
.btn-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-08 {
  --accent: oklch(0.68 0.2 350);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(130% 130% at 20% 0%,#2a1030,#160820);
  padding: 44px 20px;
}

.btn-08__wrap {
  width: min(560px,100%);
}

.btn-08__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 14px 4px;
}

.btn-08__pills {
  position: relative;
  display: inline-flex;
  flex-wrap: wrap;
  gap: 0;
  padding: 4px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 999px;
  backdrop-filter: blur(6px);
}

.btn-08__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-08__pill {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 42px;
  padding: 0 20px;
  font-size: 14.5px;
  font-weight: 650;
  color: rgba(255,255,255,.7);
  cursor: pointer;
  border-radius: 999px;
  transition: color .25s;
}

.btn-08__ind {
  position: absolute;
  z-index: 0;
  top: 4px;
  left: 0;
  height: calc(100% - 8px);
  width: var(--w);
  translate: var(--x) 0;
  background: var(--accent);
  border-radius: 999px;
  box-shadow: 0 4px 18px -4px var(--accent);
  transition: translate .4s cubic-bezier(.34,1.3,.5,1),width .4s cubic-bezier(.34,1.3,.5,1);
}

.btn-08__pills:has(#btn-08-1:checked) {
  --x: 4px;
  --w: 56px;
}

.btn-08__pills:has(#btn-08-2:checked) {
  --x: 64px;
  --w: 92px;
}

.btn-08__pills:has(#btn-08-3:checked) {
  --x: 160px;
  --w: 126px;
}

.btn-08__pills:has(#btn-08-4:checked) {
  --x: 290px;
  --w: 82px;
}

.btn-08__in:checked + .btn-08__pill {
  color: #fff;
}

.btn-08__in:focus-visible + .btn-08__pill {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-08__ind,
    .btn-08__pill {
    transition: none;
  }
}
```
