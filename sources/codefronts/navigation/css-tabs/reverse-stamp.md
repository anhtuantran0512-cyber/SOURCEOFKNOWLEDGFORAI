---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/reverse-stamp/"
title: "Reverse Stamp"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "The whole bar is cream-on-crimson."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reverse Stamp
Source: https://codefronts.com/navigation/css-tabs/reverse-stamp/

The whole bar is cream-on-crimson. The active tab inverts — crimson ink stamped on cream. A single-frame impact shadow flashes on activation, like a rubber stamp pressing in.
## HTML
```html
<div class="tt11">
  <nav class="tt11n">
    <input type="radio" name="tt11" id="tt11-r1" checked />
    <label class="tt11b" for="tt11-r1">Recto</label>
    <input type="radio" name="tt11" id="tt11-r2" />
    <label class="tt11b" for="tt11-r2">Verso</label>
    <input type="radio" name="tt11" id="tt11-r3" />
    <label class="tt11b" for="tt11-r3">Folio</label>
  </nav>
  <div class="tt11p">The right-hand page, traditionally odd-numbered.</div>
  <div class="tt11p">The left-hand page, traditionally even.</div>
  <div class="tt11p">The full leaf — both sides counted as one.</div>
</div>
```
## CSS
```css
.tt11 {
  background: #dc1e3a;
  padding: 0;
  font-family: ui-monospace, monospace;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  width: 100%;
}

.tt11n {
  display: flex;
  gap: 0;
  flex-shrink: 0;
}

.tt11n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt11b {
  flex: 1;
  padding: 18px 12px;
  border: 0;
  background: #dc1e3a;
  color: #f5ead0;
  font: 800 12px/1 ui-monospace, monospace;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  cursor: pointer;
  border-right: 1px solid rgba(245, 234, 208, 0.25);
  transition: background 0.05s steps(1, end), color 0.05s steps(1, end), box-shadow 0.4s;
}

.tt11b:last-child {
  border-right: 0;
}

.tt11b:hover {
  background: rgba(245, 234, 208, 0.1);
}

.tt11n input:checked + .tt11b {
  background: #f5ead0;
  color: #dc1e3a;
  box-shadow: inset 0 0 0 0 rgba(0, 0, 0, 0.4);
  animation: tt11-impact 0.35s cubic-bezier(0.65, 0, 0.35, 1);
}

@keyframes tt11-impact {
  0% {
    box-shadow: inset 0 0 0 0 rgba(0, 0, 0, 0.4);
  }

  20% {
    box-shadow: inset 0 4px 14px rgba(0, 0, 0, 0.5);
  }

  100% {
    box-shadow: inset 0 0 0 0 rgba(0, 0, 0, 0);
  }
}

.tt11p {
  display: none;
  padding: 14px 18px;
  background: #f5ead0;
  font: italic 11px/1.6 ui-serif, Georgia, serif;
  color: #3a3a42;
  flex: 1;
}

.tt11:has(#tt11-r1:checked) .tt11p:nth-of-type(1),
.tt11:has(#tt11-r2:checked) .tt11p:nth-of-type(2),
.tt11:has(#tt11-r3:checked) .tt11p:nth-of-type(3),
.tt11:has(#tt11-r4:checked) .tt11p:nth-of-type(4),
.tt11:has(#tt11-r5:checked) .tt11p:nth-of-type(5),
.tt11:has(#tt11-r6:checked) .tt11p:nth-of-type(6) {
  display: flex;
  align-items: center;
}

@media (prefers-reduced-motion: reduce) {
  .tt11n input:checked + .tt11b {
    animation: none;
  }
}
```
