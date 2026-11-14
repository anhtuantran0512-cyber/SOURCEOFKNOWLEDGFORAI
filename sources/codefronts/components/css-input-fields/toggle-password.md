---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/toggle-password/"
title: "Toggle Password"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Password field with an eye toggle that swaps `type=\"password\"` ↔ `type=\"text\"`."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Toggle Password
Source: https://codefronts.com/components/css-input-fields/toggle-password/

Password field with an eye toggle that swaps `type="password"` ↔ `type="text"`. `aria-pressed` reflects state for screen readers; `autocomplete="new-password"` for sign-up flows.
## HTML
```html
<label class="if-27">
  <span class="if-27-label">Password</span>
  <span class="if-27-wrap">
    <input
      type="password"
      name="pw"
      autocomplete="new-password"
      placeholder="At least 8 characters"
      minlength="8"
      data-if-27
    />
    <button
      type="button"
      class="if-27-toggle"
      aria-label="Show password"
      aria-pressed="false"
      data-if-27-toggle
    >
      <svg class="if-27-eye" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7Z" />
        <circle cx="12" cy="12" r="3" />
      </svg>
      <svg class="if-27-eye-off" viewBox="0 0 24 24" aria-hidden="true">
        <path
          d="M3 3l18 18M9.9 5.1A10 10 0 0 1 22 12a16 16 0 0 1-2.7 3.7M6.7 6.7A16 16 0 0 0 2 12s4 7 10 7a10 10 0 0 0 4.1-.9"
        />
      </svg>
    </button>
  </span>
</label>
```
## CSS
```css
.if-27 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-27-label {
  font-weight: 600;
}

.if-27 input {
  width: 100%;
  box-sizing: border-box;
  padding: 11px 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #f0eeff;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.if-27 input:focus {
  border-color: #c084fc;
}

.if-27-meter {
  position: relative;
  height: 4px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.08);
  overflow: hidden;
}

.if-27-fill {
  position: absolute;
  inset: 0;
  width: 0;
  background: linear-gradient(90deg, #ef4444, #f59e0b, #22c55e);
  border-radius: inherit;
  transition: width 0.3s ease;
}

.if-27:has(input:placeholder-shown) .if-27-fill {
  width: 0;
}

.if-27:has(input:not(:placeholder-shown):invalid) .if-27-fill {
  width: 30%;
}

.if-27:has(input:not(:placeholder-shown):valid) .if-27-fill {
  width: 65%;
}

.if-27:has(input:focus:valid) .if-27-fill {
  width: 100%;
}

.if-27-hint {
  font-size: 10.5px;
  color: #b8b6d4;
}

.if-27 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-27-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-27-wrap {
  display: inline-flex;
  align-items: center;
  padding: 0 6px 0 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: border-color 0.2s;
}

.if-27-wrap:focus-within {
  border-color: #7c6cff;
}

.if-27 input {
  flex: 1;
  min-width: 0;
  padding: 12px 0;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 500 14px/1 system-ui, sans-serif;
  letter-spacing: 0.08em;
}

.if-27 input::placeholder {
  color: #b8b6d4;
}

.if-27-toggle {
  width: 32px;
  height: 32px;
  border: 0;
  cursor: pointer;
  background: transparent;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s;
}

.if-27-toggle:hover {
  background: rgba(255, 255, 255, 0.05);
}

.if-27-toggle svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #b8b6d4;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.if-27-eye-off {
  display: none;
}

.if-27-toggle[aria-pressed="true"] .if-27-eye {
  display: none;
}

.if-27-toggle[aria-pressed="true"] .if-27-eye-off {
  display: block;
}

.if-27-toggle[aria-pressed="true"] svg {
  stroke: #7c6cff;
}
```

## JavaScript
```js
// Toggle Password — swap input type + reflect state via aria-pressed
document.querySelectorAll("[data-if-27-toggle]").forEach(function (btn) {
  var input = btn.closest(".if-27-wrap").querySelector("input");
  btn.addEventListener("click", function () {
    var on = btn.getAttribute("aria-pressed") === "true";
    btn.setAttribute("aria-pressed", on ? "false" : "true");
    btn.setAttribute("aria-label", on ? "Show password" : "Hide password");
    input.type = on ? "password" : "text";
  });
});
```
