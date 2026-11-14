---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-form-layout/"
title: "CSS Flexbox Form Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A structured form layout using flex for single-column fields, inline multi-column field rows, and input groups with prefix/suffix addons — all without tables…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Form Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-form-layout/

A structured form layout using flex for single-column fields, inline multi-column field rows, and input groups with prefix/suffix addons — all without tables or floats.
## HTML
```html
<div class="fl-14">
  <div class="fl-14__card">
    <div class="fl-14__card-header">
      <div class="fl-14__card-eyebrow">Flexbox Form Layout</div>
      <div class="fl-14__card-title">Create Your Account</div>
      <div class="fl-14__card-sub">All field rows and input groups use CSS Flexbox</div>
    </div>

    <div class="fl-14__form">

      <!-- Full-width with prefix -->
      <div class="fl-14__field">
        <label class="fl-14__label">Email address <span class="fl-14__required">*</span></label>
        <div class="fl-14__input-group">
          <div class="fl-14__input-prefix">✉</div>
          <input class="fl-14__input" type="email" placeholder="[email protected]">
        </div>
        <div class="fl-14__hint is-error">Please enter a valid email address</div>
      </div>

      <!-- Two-col row: first + last name -->
      <div class="fl-14__row">
        <div class="fl-14__field">
          <label class="fl-14__label">First name <span class="fl-14__required">*</span></label>
          <input class="fl-14__plain-input" type="text" placeholder="Jane">
        </div>
        <div class="fl-14__field">
          <label class="fl-14__label">Last name</label>
          <input class="fl-14__plain-input" type="text" placeholder="Doe">
        </div>
      </div>

      <!-- Three-col row: country code + phone -->
      <div class="fl-14__field">
        <label class="fl-14__label">Phone number</label>
        <div class="fl-14__row">
          <div class="fl-14__field fl-14__field--narrow">
            <select class="fl-14__select">
              <option>🇺🇸 +1</option>
              <option>🇬🇧 +44</option>
              <option>🇩🇪 +49</option>
            </select>
          </div>
          <div class="fl-14__field fl-14__field--wide">
            <input class="fl-14__plain-input" type="tel" placeholder="(555) 000-0000">
          </div>
        </div>
      </div>

      <!-- Password with suffix -->
      <div class="fl-14__field">
        <label class="fl-14__label">Password <span class="fl-14__required">*</span></label>
        <div class="fl-14__input-group">
          <input class="fl-14__input" type="password" placeholder="Min. 8 characters">
          <div class="fl-14__input-suffix" style="cursor:pointer">👁</div>
        </div>
        <div class="fl-14__hint is-success">✓ Password strength: Strong</div>
      </div>

      <!-- Role select -->
      <div class="fl-14__field">
        <label class="fl-14__label">Role</label>
        <select class="fl-14__select">
          <option>Frontend Developer</option>
          <option>Designer</option>
          <option>Product Manager</option>
          <option>Other</option>
        </select>
      </div>

      <!-- Textarea -->
      <div class="fl-14__field">
        <label class="fl-14__label">Bio</label>
        <textarea class="fl-14__textarea" placeholder="Tell us about yourself..."></textarea>
        <div class="fl-14__hint">0 / 200 characters</div>
      </div>

      <div class="fl-14__divider"></div>

      <!-- Checkboxes: flex column -->
      <div class="fl-14__field">
        <label class="fl-14__label">Preferences</label>
        <div class="fl-14__check-group">
          <div class="fl-14__check-item">
            <div class="fl-14__checkbox is-checked">✓</div>
            <div class="fl-14__check-text">Send me weekly CSS layout tips and pattern updates</div>
          </div>
          <div class="fl-14__check-item">
            <div class="fl-14__checkbox"></div>
            <div class="fl-14__check-text">I agree to the <span style="color:#2563eb;cursor:pointer">Terms of Service</span> and <span style="color:#2563eb;cursor:pointer">Privacy Policy</span></div>
          </div>
        </div>
      </div>

      <!-- Submit row: space-between -->
      <div class="fl-14__submit-row">
        <button class="fl-14__cancel-btn">Cancel</button>
        <div style="display:flex;align-items:center;gap:12px">
          <div class="fl-14__step-indicator">Step <strong>2</strong> of 3</div>
          <button class="fl-14__submit-btn">Continue →</button>
        </div>
      </div>

    </div>
  </div>
</div>
```
## CSS
```css
.fl-14,
.fl-14 *,
.fl-14 *::before,
.fl-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-14 ::selection {
  background: #2563eb;
  color: #fff;
}

.fl-14 {
  --bg: #f8fafc;
  --surface: #fff;
  --ink: #0f172a;
  --muted: #64748b;
  --accent: #2563eb;
  --accent-light: #dbeafe;
  --border: #cbd5e1;
  --border-focus: #2563eb;
  --error: #ef4444;
  --success: #22c55e;
  font-family: 'Lato', sans-serif;
  background: var(--bg);
  padding: 28px;
  border-radius: 16px;
  min-height: 500px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.fl-14__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  width: 100%;
  max-width: 560px;
}

.fl-14__card-header {
  background: linear-gradient(135deg, #1e3a5f, #2563eb);
  padding: 20px 24px;
}

.fl-14__card-eyebrow {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.55);
  margin-bottom: 4px;
}

.fl-14__card-title {
  font-size: 1.1rem;
  font-weight: 900;
  color: #fff;
}

.fl-14__card-sub {
  font-size: 0.75rem;
  color: rgba(255,255,255,0.55);
  margin-top: 4px;
}

.fl-14__form {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
/* ── Row patterns ── */
/* Single full-width field */

.fl-14__field {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
/* Two-col row: flex row with gap */

.fl-14__row {
  display: flex;
  gap: 12px;
}

.fl-14__row .fl-14__field {
  flex: 1;
}

.fl-14__row .fl-14__field--narrow {
  flex: 0 0 100px;
}

.fl-14__row .fl-14__field--wide {
  flex: 2;
}
/* Input group: icon + input side by side */

.fl-14__input-group {
  display: flex;
  align-items: stretch;
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.fl-14__input-group:focus-within {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.12);
}

.fl-14__input-prefix {
  background: #f8fafc;
  border-right: 1px solid var(--border);
  padding: 0 10px;
  display: flex;
  align-items: center;
  font-size: 0.78rem;
  color: var(--muted);
  flex-shrink: 0;
  white-space: nowrap;
}

.fl-14__input-suffix {
  background: #f8fafc;
  border-left: 1px solid var(--border);
  padding: 0 10px;
  display: flex;
  align-items: center;
  font-size: 0.78rem;
  color: var(--muted);
  flex-shrink: 0;
}

.fl-14__input {
  flex: 1;
  border: none;
  outline: none;
  padding: 9px 12px;
  font-size: 0.82rem;
  font-family: 'Lato', sans-serif;
  color: var(--ink);
  background: transparent;
  min-width: 0;
}

.fl-14__input::placeholder {
  color: #94a3b8;
}
/* Plain input (no group) */

.fl-14__plain-input {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 9px 12px;
  font-size: 0.82rem;
  font-family: 'Lato', sans-serif;
  color: var(--ink);
  outline: none;
  width: 100%;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.fl-14__plain-input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.12);
}

.fl-14__plain-input::placeholder {
  color: #94a3b8;
}
/* Select */

.fl-14__select {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 9px 12px;
  font-size: 0.82rem;
  font-family: 'Lato', sans-serif;
  color: var(--ink);
  outline: none;
  width: 100%;
  background: var(--surface);
  cursor: pointer;
  transition: border-color 0.2s;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' fill='none'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2364748b' stroke-width='1.5'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 32px;
}

.fl-14__select:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.12);
}
/* Textarea */

.fl-14__textarea {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 9px 12px;
  font-size: 0.82rem;
  font-family: 'Lato', sans-serif;
  color: var(--ink);
  outline: none;
  width: 100%;
  resize: vertical;
  min-height: 80px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.fl-14__textarea:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.12);
}

.fl-14__label {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 4px;
}

.fl-14__required {
  color: var(--error);
}

.fl-14__hint {
  font-size: 0.68rem;
  color: var(--muted);
}

.fl-14__hint.is-error {
  color: var(--error);
}

.fl-14__hint.is-success {
  color: var(--success);
}
/* Checkbox row */

.fl-14__check-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.fl-14__check-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  cursor: pointer;
}

.fl-14__checkbox {
  width: 16px;
  height: 16px;
  border: 2px solid var(--border);
  border-radius: 4px;
  flex-shrink: 0;
  margin-top: 1px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, border-color 0.15s;
}

.fl-14__checkbox.is-checked {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
  font-size: 0.6rem;
  font-weight: 800;
}

.fl-14__check-text {
  font-size: 0.78rem;
  color: var(--muted);
  line-height: 1.4;
}
/* Divider */

.fl-14__divider {
  height: 1px;
  background: #f1f5f9;
  margin: 4px 0;
}
/* Submit row */

.fl-14__submit-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 4px;
}

.fl-14__submit-btn {
  padding: 10px 24px;
  border-radius: 8px;
  background: var(--accent);
  color: #fff;
  font-size: 0.82rem;
  font-weight: 700;
  font-family: 'Lato', sans-serif;
  border: none;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
  display: flex;
  align-items: center;
  gap: 6px;
}

.fl-14__submit-btn:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
}

.fl-14__cancel-btn {
  padding: 10px 16px;
  border-radius: 8px;
  background: transparent;
  color: var(--muted);
  font-size: 0.82rem;
  font-weight: 600;
  font-family: 'Lato', sans-serif;
  border: 1px solid var(--border);
  cursor: pointer;
  transition: all 0.15s;
}

.fl-14__cancel-btn:hover {
  background: #f8fafc;
  color: var(--ink);
}

.fl-14__step-indicator {
  font-size: 0.7rem;
  color: var(--muted);
}

.fl-14__step-indicator strong {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .fl-14__input-group,
    .fl-14__plain-input,
    .fl-14__select,
    .fl-14__textarea,
    .fl-14__submit-btn,
    .fl-14__cancel-btn {
    transition: none;
  }
}
```
