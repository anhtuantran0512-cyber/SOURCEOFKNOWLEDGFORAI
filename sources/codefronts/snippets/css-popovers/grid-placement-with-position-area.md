---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/grid-placement-with-position-area/"
title: "Grid Placement with Position Area"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "position-area treats the area around an anchor as a three by three grid and lets you name a cell instead of computing coordinates."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grid Placement with Position Area
Source: https://codefronts.com/snippets/css-popovers/grid-placement-with-position-area/

position-area treats the area around an anchor as a three by three grid and lets you name a cell instead of computing coordinates. This board makes that literal: nine buttons around a fixed anchor card, each opening the same kind of panel in a different cell, so the physical and logical keyword sets stop being an abstraction you have to hold in your head.
## HTML
```html
<div class="pop-06">
  <div class="pop-06__stage">
    <div class="pop-06__wrap">
      <p class="pop-06__kicker">position-area · nine cells</p>
      <div class="pop-06__grid">
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p1">block-start<br>inline-start</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p2">block-start<br>center</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p3">block-start<br>inline-end</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p4">center<br>inline-start</button>
        <div class="pop-06__anchor">ANCHOR</div>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p6">center<br>inline-end</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p7">block-end<br>inline-start</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p8">block-end<br>center</button>
        <button class="pop-06__cell" type="button" popovertarget="pop-06-p9">block-end<br>inline-end</button>
      </div>
      <p class="pop-06__foot">Nine buttons, nine panels, one anchor. Every panel differs by a single declaration.</p>
    </div>
  </div>

  <div class="pop-06__p pop-06__p--1" popover="auto" id="pop-06-p1" role="group" aria-label="block-start inline-start">block-start inline-start</div>
  <div class="pop-06__p pop-06__p--2" popover="auto" id="pop-06-p2" role="group" aria-label="block-start center">block-start center</div>
  <div class="pop-06__p pop-06__p--3" popover="auto" id="pop-06-p3" role="group" aria-label="block-start inline-end">block-start inline-end</div>
  <div class="pop-06__p pop-06__p--4" popover="auto" id="pop-06-p4" role="group" aria-label="center inline-start">center inline-start</div>
  <div class="pop-06__p pop-06__p--6" popover="auto" id="pop-06-p6" role="group" aria-label="center inline-end">center inline-end</div>
  <div class="pop-06__p pop-06__p--7" popover="auto" id="pop-06-p7" role="group" aria-label="block-end inline-start">block-end inline-start</div>
  <div class="pop-06__p pop-06__p--8" popover="auto" id="pop-06-p8" role="group" aria-label="block-end center">block-end center</div>
  <div class="pop-06__p pop-06__p--9" popover="auto" id="pop-06-p9" role="group" aria-label="block-end inline-end">block-end inline-end</div>
</div>
```
## CSS
```css
.pop-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f1f2f4;
  --surface: #ffffff;
  --ink: #191c21;
  --muted: #6a707a;
  --rule: #d5d8de;
  --accent: #2f3b52;
  --gap: 8px;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 34px 16px;
}

.pop-06__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 68px);
}

.pop-06__wrap {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
}

.pop-06__kicker {
  margin: 0 0 12px;
  font: 650 11px/1 var(--font-mono);
  letter-spacing: 0.1em;
  color: var(--muted);
  text-transform: uppercase;
}

.pop-06__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 2px;
  background: var(--rule);
  border: 1px solid var(--rule);
}

.pop-06__cell {
  min-height: 56px;
  padding: 6px 4px;
  font: 600 9.5px/1.35 var(--font-mono);
  letter-spacing: 0.01em;
  color: var(--muted);
  background: var(--surface);
  border: 0;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-06__cell:hover {
  color: var(--ink);
  background: color-mix(in oklab, var(--surface) 92%, var(--accent));
}

.pop-06__cell:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

.pop-06__anchor {
  display: grid;
  place-items: center;
  min-height: 56px;
  font: 700 10px/1 var(--font-mono);
  letter-spacing: 0.18em;
  color: var(--surface);
  background: var(--accent);
  anchor-name: --pop-06-anchor;
}

.pop-06__foot {
  margin: 14px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-06__p {
  position: fixed;
  margin: 0;
  inline-size: max-content;
  max-inline-size: min(13rem, calc(100vw - 24px));
  padding: 9px 11px;
  font: 650 11px/1.3 var(--font-mono);
  color: var(--surface);
  background: var(--ink);
  border: 0;
  border-radius: 0;
  box-shadow: 0 10px 24px -14px rgba(25, 28, 33, 0.7);
}

@supports (anchor-name: --a) {
  .pop-06__p {
    position-anchor: --pop-06-anchor;
    inset: auto;
  }

  .pop-06__p--1 {
    position-area: block-start inline-start;
    margin: 0 var(--gap) var(--gap) 0;
  }

  .pop-06__p--2 {
    position-area: block-start center;
    margin-block-end: var(--gap);
  }

  .pop-06__p--3 {
    position-area: block-start inline-end;
    margin: 0 0 var(--gap) var(--gap);
  }

  .pop-06__p--4 {
    position-area: center inline-start;
    margin-inline-end: var(--gap);
  }

  .pop-06__p--6 {
    position-area: center inline-end;
    margin-inline-start: var(--gap);
  }

  .pop-06__p--7 {
    position-area: block-end inline-start;
    margin: var(--gap) var(--gap) 0 0;
  }

  .pop-06__p--8 {
    position-area: block-end center;
    margin-block-start: var(--gap);
  }

  .pop-06__p--9 {
    position-area: block-end inline-end;
    margin: var(--gap) 0 0 var(--gap);
  }
}

@media (prefers-color-scheme: dark) {
  .pop-06 {
    --bg: #101317;
    --surface: #1a1e24;
    --ink: #eef1f5;
    --muted: #939aa5;
    --rule: #2a2f37;
    --accent: #7f9cc9;
  }

  .pop-06__anchor {
    color: #101317;
  }

  .pop-06__p {
    color: #101317;
    background: #eef1f5;
  }
}

[data-theme="dark"] .pop-06 {
  --bg: #101317;
  --surface: #1a1e24;
  --ink: #eef1f5;
  --muted: #939aa5;
  --rule: #2a2f37;
  --accent: #7f9cc9;
}

[data-theme="dark"] .pop-06 .pop-06__anchor {
  color: #101317;
}

[data-theme="dark"] .pop-06 .pop-06__p {
  color: #101317;
  background: #eef1f5;
}
```
