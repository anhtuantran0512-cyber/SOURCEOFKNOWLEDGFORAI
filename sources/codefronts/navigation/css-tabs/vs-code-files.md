---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/vs-code-files/"
title: "VS Code Files"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "IDE-inspired file tabs with language-colored dots and editor chrome."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: VS Code Files
Source: https://codefronts.com/navigation/css-tabs/vs-code-files/

IDE-inspired file tabs with language-colored dots and editor chrome. The active tab lifts with a top accent stripe and matches the editor surface, just like VS Code. Pure CSS.
## HTML
```html
<div class="tt25">
  <nav class="tt25n">
    <input type="radio" name="tt25" id="tt25-r1" checked />
    <label class="tt25b" for="tt25-r1"
      ><span class="tt25dot" style="--c: #3178c6"></span>app.tsx</label
    >
    <input type="radio" name="tt25" id="tt25-r2" />
    <label class="tt25b" for="tt25-r2"
      ><span class="tt25dot" style="--c: #f0db4f"></span>config.js</label
    >
    <input type="radio" name="tt25" id="tt25-r3" />
    <label class="tt25b" for="tt25-r3"
      ><span class="tt25dot" style="--c: #264de4"></span>styles.css</label
    >
  </nav>
  <div class="tt25body">
    <div class="tt25p">// app.tsx<br />export default App;</div>
    <div class="tt25p">// config.js<br />module.exports = {};</div>
    <div class="tt25p">/* styles.css */<br />:root { color: white; }</div>
  </div>
</div>
```
## CSS
```css
.tt25 {
  background: #1e1e1e;
  padding: 0;
  font-family: ui-monospace, monospace;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt25n {
  display: flex;
  background: #2d2d2d;
  border-bottom: 1px solid #1e1e1e;
  min-width: 0;
}

.tt25n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt25b {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  font: 12px/1 ui-monospace, monospace;
  color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  border-right: 1px solid #1e1e1e;
  position: relative;
  white-space: nowrap;
  transition: background 0.18s, color 0.18s;
}

.tt25b:hover {
  color: rgba(255, 255, 255, 0.85);
  background: rgba(255, 255, 255, 0.04);
}

.tt25dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--c);
  flex-shrink: 0;
}

.tt25n input:checked + .tt25b {
  background: #1e1e1e;
  color: #fff;
  border-bottom: 1px solid #1e1e1e;
  margin-bottom: -1px;
}

.tt25n input:checked + .tt25b::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #4fc1ff;
}

.tt25n input:focus-visible + .tt25b {
  outline: 1px dashed #4fc1ff;
  outline-offset: -3px;
}

.tt25body {
  padding: 18px 20px;
}

.tt25p {
  display: none;
  font: 12px/1.6 ui-monospace, monospace;
  color: #d4d4d4;
}

.tt25p:nth-of-type(1) {
  color: #569cd6;
}

.tt25:has(#tt25-r1:checked) .tt25p:nth-of-type(1),
.tt25:has(#tt25-r2:checked) .tt25p:nth-of-type(2),
.tt25:has(#tt25-r3:checked) .tt25p:nth-of-type(3) {
  display: block;
}
```
