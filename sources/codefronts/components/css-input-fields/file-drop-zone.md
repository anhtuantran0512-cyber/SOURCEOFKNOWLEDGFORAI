---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/file-drop-zone/"
title: "File Drop Zone"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Drag-and-drop file input with a custom dashed boundary."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Drop Zone
Source: https://codefronts.com/components/css-input-fields/file-drop-zone/

Drag-and-drop file input with a custom dashed boundary. Native <input type="file"> underneath, the visible filename appearing via `:has()` — accessible, keyboard-friendly, and minimal.
## HTML
```html
<label class="if-15">
  <input type="file" name="upload" accept="image/*,.pdf" />
  <span class="if-15-icon" aria-hidden="true">
    <svg
      viewBox="0 0 24 24"
      width="22"
      height="22"
      fill="none"
      stroke="currentColor"
      stroke-width="1.6"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="17 8 12 3 7 8" />
      <line x1="12" y1="3" x2="12" y2="15" />
    </svg>
  </span>
  <span class="if-15-text">
    <strong>Click to upload</strong> or drag &amp; drop
    <span class="if-15-types">PNG, JPG, or PDF · max 10 MB</span>
  </span>
</label>
```
## CSS
```css
.if-15 {
  position: relative;
  display: block;
  width: 100%;
  max-width: 320px;
  cursor: pointer;
  border: 1.5px dashed rgba(99, 102, 241, 0.5);
  border-radius: 12px;
  padding: 22px 18px;
  background: rgba(99, 102, 241, 0.05);
  text-align: center;
  transition: border-color 0.2s, background 0.2s, transform 0.15s;
}

.if-15:hover {
  border-color: #818cf8;
  background: rgba(99, 102, 241, 0.1);
}

.if-15:focus-within {
  border-color: #818cf8;
  background: rgba(99, 102, 241, 0.12);
  box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.18);
}

.if-15 input[type="file"] {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.if-15-icon {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  margin: 0 auto 8px;
  border-radius: 10px;
  background: rgba(99, 102, 241, 0.18);
  color: #a5b4fc;
}

.if-15-text {
  display: block;
  font-size: 13px;
  color: #c8c0ff;
}

.if-15-text strong {
  color: #a5b4fc;
  font-weight: 600;
}

.if-15-types {
  display: block;
  font-size: 11px;
  color: #b8b6d4;
  margin-top: 4px;
}
```
