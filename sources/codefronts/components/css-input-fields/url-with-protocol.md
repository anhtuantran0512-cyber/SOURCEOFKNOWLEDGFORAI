---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/url-with-protocol/"
title: "URL with Protocol"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "URL input with a non-editable `https://` prefix that visually integrates with the field. Submit value is the full URL; users only type the host portion."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: URL with Protocol
Source: https://codefronts.com/components/css-input-fields/url-with-protocol/

URL input with a non-editable `https://` prefix that visually integrates with the field. Submit value is the full URL; users only type the host portion.
## HTML
```html
<label class="if-25">
  <span class="if-25-label">Website</span>
  <span class="if-25-wrap">
    <span class="if-25-prefix">https://</span>
    <input
      type="text"
      name="url-host"
      inputmode="url"
      placeholder="codefronts.com"
      pattern="[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}.*"
    />
  </span>
</label>
```
## CSS
```css
.if-25 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 320px;
}

.if-25-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-25-wrap {
  display: inline-flex;
  align-items: stretch;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.if-25-wrap:focus-within {
  border-color: #06b6d4;
}

.if-25-prefix {
  display: inline-flex;
  align-items: center;
  padding: 0 12px;
  background: rgba(6, 182, 212, 0.08);
  color: #06b6d4;
  font: 600 12px/1 "JetBrains Mono", monospace;
  border-right: 1px solid rgba(255, 255, 255, 0.08);
}

.if-25 input {
  flex: 1;
  min-width: 0;
  padding: 12px 14px;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
}

.if-25 input::placeholder {
  color: #b8b6d4;
}
```
