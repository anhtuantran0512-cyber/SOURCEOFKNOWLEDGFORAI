---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/cross-browser-fallback-and-polyfill/"
title: "Cross Browser Fallback and Polyfill"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Popover and anchor positioning ship on different timelines, so one feature test is not enough."
has_js: "true"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cross Browser Fallback and Polyfill
Source: https://codefronts.com/snippets/css-popovers/cross-browser-fallback-and-polyfill/

Popover and anchor positioning ship on different timelines, so one feature test is not enough. This demo detects each separately, reports both live, and layers the experience: an absolutely positioned panel that works with no API at all, popover behaviour as the first enhancement, and anchor positioning as the second.
## HTML
```html
<div class="pop-16" data-popover="unknown" data-anchor="unknown">
  <div class="pop-16__stage">
    <div class="pop-16__card">
      <p class="pop-16__kicker">Support probe</p>
      <h2 class="pop-16__h">Two features, two tests</h2>
      <dl class="pop-16__probe">
        <div class="pop-16__prow">
          <dt class="pop-16__dt">popover attribute</dt>
          <dd class="pop-16__dd" id="pop-16-r1">checking…</dd>
        </div>
        <div class="pop-16__prow">
          <dt class="pop-16__dt">anchor-name</dt>
          <dd class="pop-16__dd" id="pop-16-r2">checking…</dd>
        </div>
      </dl>
      <button class="pop-16__btn" type="button" popovertarget="pop-16-panel" id="pop-16-trigger" aria-expanded="false">Open the layered panel</button>
      <p class="pop-16__foot" id="pop-16-note">The panel below is a plain positioned element first, a popover second, and anchored third.</p>
    </div>
  </div>

  <div class="pop-16__panel" popover="auto" id="pop-16-panel" role="group" aria-label="Layered panel">
    <p class="pop-16__ptitle">Layer report</p>
    <ul class="pop-16__list">
      <li class="pop-16__li">Baseline · absolutely positioned, no top layer</li>
      <li class="pop-16__li">Enhanced · popover attribute owns dismissal</li>
      <li class="pop-16__li">Enhanced · anchor positioning owns placement</li>
    </ul>
    <p class="pop-16__pfoot">Polyfill for the attribute: popover-polyfill from Open UI. No equivalent exists for anchoring.</p>
  </div>
</div>
```
## CSS
```css
.pop-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  --bg: #eef0f3;
  --s1: #ffffff;
  --s2: #f7f8fa;
  --ink: #1a1e25;
  --muted: #667080;
  --rule: #d6dae1;
  --ok: #17624a;
  --no: #8c3520;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 38px 16px;
}

.pop-16__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 76px);
}

.pop-16__card {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 20px 18px 18px;
}

.pop-16__kicker {
  margin: 0 0 8px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-16__h {
  margin: 0 0 16px;
  font: 600 clamp(19px, 4.4vw, 24px)/1.2 var(--font-ui);
  letter-spacing: -0.02em;
}

.pop-16__probe {
  margin: 0 0 16px;
  display: grid;
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
}

.pop-16__prow {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: space-between;
  padding: 9px 11px;
  background: var(--s2);
  min-inline-size: 0;
}

.pop-16__dt {
  margin: 0;
  font: 600 12px/1.3 var(--font-mono);
  min-inline-size: 0;
}

.pop-16__dd {
  margin: 0;
  font: 700 11px/1.3 var(--font-ui);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-16[data-popover="yes"] #pop-16-r1,
.pop-16[data-anchor="yes"] #pop-16-r2 {
  color: var(--ok);
}

.pop-16[data-popover="no"] #pop-16-r1,
.pop-16[data-anchor="no"] #pop-16-r2 {
  color: var(--no);
}

.pop-16__btn {
  inline-size: 100%;
  min-height: 44px;
  padding: 0 14px;
  font: 650 13px/1 var(--font-ui);
  color: var(--s1);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 3px;
  cursor: pointer;
  anchor-name: --pop-16-anchor;
}

.pop-16__btn:focus-visible {
  outline: 3px solid var(--ok);
  outline-offset: 2px;
}

.pop-16__foot {
  margin: 12px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-16__panel {
  position: absolute;
  inset-block-start: auto;
  inset-inline: 16px;
  inset-block-end: 16px;
  margin: 0;
  inline-size: auto;
  max-inline-size: calc(100% - 32px);
  padding: 14px;
  color: var(--ink);
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 4px;
  box-shadow: 0 18px 36px -22px rgba(26, 30, 37, 0.5);
}

@supports (anchor-name: --a) {
  .pop-16__panel {
    position: fixed;
    position-anchor: --pop-16-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    inline-size: min(21rem, calc(100vw - 32px));
    max-inline-size: calc(100vw - 32px);
    margin-block-start: 8px;
    position-try-fallbacks: flip-block;
  }
}

.pop-16__ptitle {
  margin: 0 0 10px;
  font: 700 10.5px/1 var(--font-ui);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-16__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 7px;
}

.pop-16__li {
  font-size: 12.5px;
  line-height: 1.5;
  padding-inline-start: 14px;
  position: relative;
  min-inline-size: 0;
}

.pop-16__li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 7px;
  inline-size: 5px;
  block-size: 5px;
  background: var(--muted);
  border-radius: 1px;
}

.pop-16__pfoot {
  margin: 12px 0 0;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .pop-16 {
    --bg: #0f1216;
    --s1: #191d23;
    --s2: #14181d;
    --ink: #e9ecf1;
    --muted: #8b95a3;
    --rule: #29303a;
    --ok: #6fd6ac;
    --no: #f09277;
  }

  .pop-16__btn {
    color: #0f1216;
    background: var(--ink);
    border-color: var(--ink);
  }
}

[data-theme="dark"] .pop-16 {
  --bg: #0f1216;
  --s1: #191d23;
  --s2: #14181d;
  --ink: #e9ecf1;
  --muted: #8b95a3;
  --rule: #29303a;
  --ok: #6fd6ac;
  --no: #f09277;
}

[data-theme="dark"] .pop-16 .pop-16__btn {
  color: #0f1216;
  background: var(--ink);
  border-color: var(--ink);
}
```

## JavaScript
```js
const root = document.querySelector('.pop-16');
const hasPopover = HTMLElement.prototype.hasOwnProperty('popover');
const hasAnchor = window.CSS && CSS.supports('anchor-name: --a');
root.dataset.popover = hasPopover ? 'yes' : 'no';
root.dataset.anchor = hasAnchor ? 'yes' : 'no';
document.getElementById('pop-16-r1').textContent = hasPopover ? 'supported' : 'missing · polyfill';
document.getElementById('pop-16-r2').textContent = hasAnchor ? 'supported' : 'missing · fallback';
const panel = document.getElementById('pop-16-panel');
const trigger = document.getElementById('pop-16-trigger');
if (hasPopover) {
  panel.addEventListener('toggle', (e) => {
    trigger.setAttribute('aria-expanded', String(e.newState === 'open'));
  });
} else {
  panel.hidden = true;
  trigger.addEventListener('click', () => {
    panel.hidden = !panel.hidden;
    trigger.setAttribute('aria-expanded', String(!panel.hidden));
  });
}
```
