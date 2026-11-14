---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/bento-grid/"
title: "Bento Grid"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Three-column bento grid where the tabs themselves are the cards."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid
Source: https://codefronts.com/navigation/css-tabs/bento-grid/

Three-column bento grid where the tabs themselves are the cards. The active card lifts, gains a colored top stripe, and the panel becomes the fourth bento cell underneath. Pure CSS.
## HTML
```html
<div class="tt27">
  <div class="tt27grid">
    <input type="radio" name="tt27" id="tt27-r1" checked />
    <label class="tt27card" for="tt27-r1">
      <span class="tt27ttl">Stats</span>
      <span class="tt27sub">Real-time data</span>
    </label>
    <input type="radio" name="tt27" id="tt27-r2" />
    <label class="tt27card" for="tt27-r2">
      <span class="tt27ttl">Inbox</span>
      <span class="tt27sub">12 new</span>
    </label>
    <input type="radio" name="tt27" id="tt27-r3" />
    <label class="tt27card" for="tt27-r3">
      <span class="tt27ttl">Tasks</span>
      <span class="tt27sub">3 pending</span>
    </label>
  </div>
  <div class="tt27p">Stats — daily and weekly metrics summary.</div>
  <div class="tt27p">Inbox — unread messages from your team.</div>
  <div class="tt27p">Tasks — items due in the next 7 days.</div>
</div>
```
## CSS
```css
.tt27 {
  background: #0a0a0e;
  padding: 18px 16px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt27grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  min-width: 0;
}

.tt27grid input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt27card {
  position: relative;
  padding: 18px 14px 14px;
  background: #18181f;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: transform 0.25s, background 0.25s, border-color 0.25s, box-shadow 0.3s;
  min-width: 0;
}

.tt27card:hover {
  background: #1f1f28;
  border-color: rgba(255, 255, 255, 0.14);
}

.tt27ttl {
  font: 700 13px/1 ui-sans-serif, system-ui;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tt27sub {
  font: 11px/1 ui-sans-serif, system-ui;
  color: rgba(255, 255, 255, 0.55);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tt27grid input:checked + .tt27card {
  background: #1c1c26;
  border-color: #7c6cff;
  transform: translateY(-2px);
  box-shadow: 0 8px 18px rgba(124, 108, 255, 0.25);
}

.tt27grid input:focus-visible + .tt27card {
  outline: 2px dashed #7c6cff;
  outline-offset: 3px;
}

.tt27p {
  display: none;
  margin-top: 12px;
  padding: 14px 16px;
  background: #18181f;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 10px;
  font: 12px/1.55 ui-sans-serif, system-ui;
  color: rgba(255, 255, 255, 0.7);
}

.tt27:has(#tt27-r1:checked) .tt27p:nth-of-type(1),
.tt27:has(#tt27-r2:checked) .tt27p:nth-of-type(2),
.tt27:has(#tt27-r3:checked) .tt27p:nth-of-type(3) {
  display: block;
}
```
