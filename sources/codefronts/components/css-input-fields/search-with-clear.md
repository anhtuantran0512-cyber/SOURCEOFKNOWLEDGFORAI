---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/search-with-clear/"
title: "Search with Clear"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Search input with a leading magnifier icon and a trailing clear button."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search with Clear
Source: https://codefronts.com/components/css-input-fields/search-with-clear/

Search input with a leading magnifier icon and a trailing clear button. The clear control appears only when the field has content — handled with `:placeholder-shown`.
## HTML
```html
<form class="if-08" role="search">
  <span class="if-08-icon" aria-hidden="true">
    <svg viewBox="0 0 16 16" width="14" height="14">
      <path
        fill="none"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
        d="M11 11l3 3M7 12a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"
      />
    </svg>
  </span>
  <input type="search" name="q" placeholder="Search projects, people, files…" aria-label="Search" />
  <button type="reset" class="if-08-clear" aria-label="Clear search">
    <svg viewBox="0 0 12 12" width="10" height="10" aria-hidden="true">
      <path
        fill="none"
        stroke="currentColor"
        stroke-width="1.6"
        stroke-linecap="round"
        d="M2 2l8 8M10 2l-8 8"
      />
    </svg>
  </button>
</form>
```
## CSS
```css
.if-08 {
  position: relative;
  width: 100%;
  max-width: 280px;
  display: flex;
  align-items: center;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 999px;
  padding: 0 8px 0 36px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.if-08:focus-within {
  border-color: #60a5fa;
  box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.18);
}

.if-08-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #b8b6d4;
  display: grid;
  place-items: center;
}

.if-08:focus-within .if-08-icon {
  color: #60a5fa;
}

.if-08 input {
  flex: 1;
  min-width: 0;
  background: transparent;
  border: 0;
  outline: none;
  color: #f0eeff;
  font-size: 14px;
  padding: 11px 0;
}

.if-08 input::placeholder {
  color: #b8b6d4;
}

.if-08 input::-webkit-search-cancel-button {
  display: none;
}

.if-08-clear {
  display: grid;
  place-items: center;
  width: 22px;
  height: 22px;
  background: rgba(255, 255, 255, 0.06);
  border: 0;
  border-radius: 50%;
  color: #b8b6d4;
  cursor: pointer;
  transition: opacity 0.15s, background 0.15s, color 0.15s;
}

.if-08:has(input:placeholder-shown) .if-08-clear,
.if-08:has(input[value=""]) .if-08-clear {
  opacity: 0;
  pointer-events: none;
}

.if-08-clear:hover {
  background: rgba(255, 255, 255, 0.12);
  color: #f0eeff;
}
```
