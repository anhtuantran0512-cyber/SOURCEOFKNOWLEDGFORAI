---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/password-strength/"
title: "Password Strength"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Sign-up password input with a live strength bar that grades red → amber → green. Driven by `:has(input:valid/:invalid)` — zero scoring JavaScript."
has_js: "false"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Password Strength
Source: https://codefronts.com/components/css-input-fields/password-strength/

Sign-up password input with a live strength bar that grades red → amber → green. Driven by `:has(input:valid/:invalid)` — zero scoring JavaScript.
## HTML
```html
<label class="if-09">
  <span class="if-09-label">Password</span>
  <input
    type="password"
    name="password"
    autocomplete="new-password"
    placeholder="At least 12 characters"
    minlength="6"
    required
  />
  <span class="if-09-meter" aria-hidden="true"><span class="if-09-fill"></span></span>
  <span class="if-09-hint">Use 12+ characters with letters, numbers, and a symbol.</span>
</label>
```
## CSS
```css
.if-09 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
  font-size: 11px;
  color: #b8b6d4;
}

.if-09-label {
  font-weight: 600;
}

.if-09 input {
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

.if-09 input:focus {
  border-color: #c084fc;
}

.if-09-meter {
  position: relative;
  height: 4px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.08);
  overflow: hidden;
}

.if-09-fill {
  position: absolute;
  inset: 0;
  width: 0;
  background: linear-gradient(90deg, #ef4444, #f59e0b, #22c55e);
  border-radius: inherit;
  transition: width 0.3s ease;
}

.if-09:has(input:placeholder-shown) .if-09-fill {
  width: 0;
}

.if-09:has(input:not(:placeholder-shown):invalid) .if-09-fill {
  width: 30%;
}

.if-09:has(input:not(:placeholder-shown):valid) .if-09-fill {
  width: 65%;
}

.if-09:has(input:focus:valid) .if-09-fill {
  width: 100%;
}

.if-09-hint {
  font-size: 10.5px;
  color: #b8b6d4;
}

.if-09 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 280px;
}

.if-09-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-09-wrap {
  display: inline-flex;
  align-items: center;
  padding: 0 6px 0 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: border-color 0.2s;
}

.if-09-wrap:focus-within {
  border-color: #7c6cff;
}

.if-09 input {
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

.if-09 input::placeholder {
  color: #b8b6d4;
}

.if-09-toggle {
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

.if-09-toggle:hover {
  background: rgba(255, 255, 255, 0.05);
}

.if-09-toggle svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: #b8b6d4;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.if-09-eye-off {
  display: none;
}

.if-09-toggle[aria-pressed="true"] .if-09-eye {
  display: none;
}

.if-09-toggle[aria-pressed="true"] .if-09-eye-off {
  display: block;
}

.if-09-toggle[aria-pressed="true"] svg {
  stroke: #7c6cff;
}
```
