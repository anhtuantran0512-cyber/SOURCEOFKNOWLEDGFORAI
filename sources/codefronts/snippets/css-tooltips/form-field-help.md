---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/form-field-help/"
title: "Form Field Help"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Compact help circles sit next to form labels and reveal a one-line hint on hover — username rules, email visibility, time-zone purpose."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Form Field Help
Source: https://codefronts.com/snippets/css-tooltips/form-field-help/

Compact help circles sit next to form labels and reveal a one-line hint on hover — username rules, email visibility, time-zone purpose. The tooltip pops to the right with a side-arrow tail so the form line stays uninterrupted. For settings panels, sign-up forms, and profile editors.
## HTML
```html
<div class="tp-21">
  <div class="tp-21__form">
    <div class="tp-21__field">
      <div class="tp-21__label">
        Username
        <span class="tp-21__t">
          <span class="tp-21__icon">?</span>
          <span class="tp-21__tip">Letters, numbers, and underscores only. 3–20 characters.</span>
        </span>
      </div>
      <input class="tp-21__input" type="text" value="kalani_a" readonly>
    </div>
    <div class="tp-21__field">
      <div class="tp-21__label">
        Email address
        <span class="tp-21__t">
          <span class="tp-21__icon">?</span>
          <span class="tp-21__tip">Used for login and account recovery. Never shown publicly.</span>
        </span>
      </div>
      <input class="tp-21__input" type="email" value="[email protected]" readonly>
    </div>
    <div class="tp-21__field">
      <div class="tp-21__label">
        Website
        <span class="tp-21__t">
          <span class="tp-21__icon">?</span>
          <span class="tp-21__tip">Include https:// — displayed on your public profile page.</span>
        </span>
      </div>
      <input class="tp-21__input" type="text" value="https://kalani.dev" readonly>
    </div>
    <div class="tp-21__field">
      <div class="tp-21__label">
        Bio
        <span class="tp-21__t">
          <span class="tp-21__icon">?</span>
          <span class="tp-21__tip">Shown below your name on your profile. Max 160 characters.</span>
        </span>
      </div>
      <input class="tp-21__input" type="text" value="Building things on the web. Based in Honolulu." readonly>
    </div>
    <div class="tp-21__field tp-21__field-last">
      <div class="tp-21__label">
        Time zone
        <span class="tp-21__t">
          <span class="tp-21__icon">?</span>
          <span class="tp-21__tip">Used to display timestamps and schedule notifications correctly.</span>
        </span>
      </div>
      <input class="tp-21__input" type="text" value="Pacific/Honolulu (UTC −10:00)" readonly>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-21 {
  width: 100%;
  min-height: 100vh;
  background: #fff;
  /* Right room — help tooltips pop to the RIGHT of each ? icon,
       ~280px wide single-line pills. Padding the right side gives them
       room to extend without getting clipped by the gallery card. */
  padding: 40px 320px 40px 28px;
  font-family: system-ui, -apple-system, sans-serif;
}

.tp-21__form {
  max-width: 400px;
  margin: 0 auto;
}

.tp-21__field {
  margin-bottom: 18px;
}

.tp-21__field-last {
  margin-bottom: 0;
}

.tp-21__label {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 12.5px;
  font-weight: 500;
  color: #111;
  margin-bottom: 6px;
}

.tp-21__t {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.tp-21__icon {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #e5e7eb;
  color: #9ca3af;
  font-size: 9px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: help;
  transition: background .12s, color .12s;
  flex-shrink: 0;
  line-height: 1;
}

.tp-21__t:hover .tp-21__icon {
  background: #d1d5db;
  color: #374151;
}

.tp-21__tip {
  position: absolute;
  top: 50%;
  left: calc(100% + 8px);
  transform: translateY(-50%) translateX(4px);
  background: #18181b;
  color: #fff;
  font-size: 11.5px;
  padding: 7px 11px;
  border-radius: 5px;
  width: 240px;
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transition: opacity .14s, transform .14s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .14s;
  z-index: 100;
  line-height: 1.4;
  display: block;
}

.tp-21__t:hover .tp-21__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-21__tip::after {
  content: '';
  position: absolute;
  top: 50%;
  right: 100%;
  transform: translateY(-50%);
  border: 4px solid transparent;
  border-right-color: #18181b;
}

.tp-21__input {
  width: 100%;
  padding: 8px 11px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-size: 12.5px;
  color: #374151;
  background: #fafafa;
  outline: none;
  font-family: inherit;
}

.tp-21__input:focus {
  border-color: #6366f1;
  background: #fff;
}
```
