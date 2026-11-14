---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/permission-stack-with-live-status/"
title: "Permission Stack with Live Status"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A settings-panel pattern: a stack of permission rows, each with its own mini switch — and a status badge in the header that flips between 'Full access' and…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Permission Stack with Live Status
Source: https://codefronts.com/components/css-toggles-switches/permission-stack-with-live-status/

A settings-panel pattern: a stack of permission rows, each with its own mini switch — and a status badge in the header that flips between 'Full access' and 'Partial' by *watching the group* with :has(). The container reads its own children's state, no script.
## HTML
```html
<section class="tgl-13" aria-label="Permission toggles with live status">
  <div class="tgl-13__card">
    <header class="tgl-13__head">
      <b>App permissions</b>
      <span class="tgl-13__badge" aria-hidden="true"><i class="tgl-13__b tgl-13__b--full">Full access</i><i class="tgl-13__b tgl-13__b--part">Partial</i><i class="tgl-13__b tgl-13__b--none">No access</i></span>
    </header>
    <label class="tgl-13__row"><span class="tgl-13__txt"><b>Camera</b><small>Photos &amp; video capture</small></span><input type="checkbox" class="tgl-13__sw" role="switch" checked></label>
    <label class="tgl-13__row"><span class="tgl-13__txt"><b>Microphone</b><small>Voice notes &amp; calls</small></span><input type="checkbox" class="tgl-13__sw" role="switch" checked></label>
    <label class="tgl-13__row"><span class="tgl-13__txt"><b>Location</b><small>While using the app</small></span><input type="checkbox" class="tgl-13__sw" role="switch"></label>
  </div>
</section>
```
## CSS
```css
.tgl-13,
.tgl-13 *,
.tgl-13 *::before,
.tgl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-13 {
  --on: oklch(0.68 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #eef0f4;
}

.tgl-13__card {
  width: min(360px,100%);
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 16px 40px -26px rgba(30,40,70,.5);
  overflow: hidden;
}

.tgl-13__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px;
  border-bottom: 1px solid #eef0f4;
}

.tgl-13__head > b {
  font-size: 16px;
  color: #22283a;
}

.tgl-13__badge {
  position: relative;
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .04em;
}

.tgl-13__b {
  display: none;
  padding: 4px 10px;
  border-radius: 999px;
}

.tgl-13__b--full {
  display: inline-block;
  background: oklch(0.93 0.06 155);
  color: oklch(0.4 0.1 155);
}

.tgl-13__card:has(.tgl-13__sw:not(:checked)) .tgl-13__b--full {
  display: none;
}

.tgl-13__card:has(.tgl-13__sw:not(:checked)) .tgl-13__b--part {
  display: inline-block;
  background: oklch(0.93 0.08 80);
  color: oklch(0.45 0.11 60);
}

.tgl-13__card:not(:has(.tgl-13__sw:checked)) .tgl-13__b--part {
  display: none;
}

.tgl-13__card:not(:has(.tgl-13__sw:checked)) .tgl-13__b--none {
  display: inline-block;
  background: #eceef2;
  color: #697086;
}

.tgl-13__row {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 14px 20px;
  cursor: pointer;
  transition: background-color .2s;
}

.tgl-13__row + .tgl-13__row {
  border-top: 1px solid #f2f4f7;
}

.tgl-13__row:hover {
  background: #f8f9fc;
}

.tgl-13__txt {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tgl-13__txt b {
  font-size: 14.5px;
  color: #7d8494;
  font-weight: 600;
  transition: color .2s;
}

.tgl-13__row:has(.tgl-13__sw:checked) .tgl-13__txt b {
  color: #22283a;
}

.tgl-13__txt small {
  font-size: 12px;
  color: #98a0b0;
}

.tgl-13__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 44px;
  height: 26px;
  border-radius: 14px;
  background: #e3e6ec;
  position: relative;
  cursor: pointer;
  transition: background-color .25s;
}

.tgl-13__sw::before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 5px rgba(20,30,60,.3);
  transition: transform .25s cubic-bezier(.25,.9,.3,1.1);
}

.tgl-13__sw:checked {
  background: var(--on);
}

.tgl-13__sw:checked::before {
  transform: translateX(18px);
}

.tgl-13__sw:focus-visible {
  outline: 3px solid oklch(0.6 0.17 250);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-13__sw,
    .tgl-13__sw::before,
    .tgl-13__row,
    .tgl-13__txt b {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the card watches its own switches with :has(): any unchecked shows 'Partial', none checked shows 'No access', all checked shows 'Full access'. */
```
