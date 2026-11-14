---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/auto-grow-textarea/"
title: "Auto-Grow Textarea"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "A multi-line <textarea> that grows with its content using `field-sizing: content` — no JS observer needed."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto-Grow Textarea
Source: https://codefronts.com/components/css-input-fields/auto-grow-textarea/

A multi-line <textarea> that grows with its content using `field-sizing: content` — no JS observer needed. Falls back to a min-height on browsers without support.
## HTML
```html
<label class="if-22">
  <span class="if-22-label">Notes</span>
  <textarea name="notes" rows="2" placeholder="Type as much as you need..."></textarea>
  <span class="if-22-hint">Field grows as you type</span>
</label>
```
## CSS
```css
.if-22 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 320px;
}

.if-22-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-22 textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 12px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  color: #f0eeff;
  font: 500 14px/1.55 system-ui, sans-serif;
  outline: none;
  resize: none;
  min-height: 64px;
  field-sizing: content;
  transition: border-color 0.2s, background 0.2s;
}

.if-22 textarea:focus {
  border-color: #a78bfa;
  background: #1f1f2a;
}

.if-22 textarea::placeholder {
  color: #b8b6d4;
}

.if-22-hint {
  font-size: 11px;
  color: #b8b6d4;
}
```
