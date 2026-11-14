---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-form-inputs-css/"
title: "Material Design Form Inputs CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Filled and outlined text fields with floating labels, select menus, textarea, checkboxes, radio buttons, toggle switches, and range sliders — interactive,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Form Inputs CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-form-inputs-css/

Filled and outlined text fields with floating labels, select menus, textarea, checkboxes, radio buttons, toggle switches, and range sliders — interactive, fully accessible, no JavaScript.
## HTML
```html
<div class="md-04">
  <div class="md-04__wrap">
    <div class="md-04__page-title">Material Design Form Inputs</div>
    <div class="md-04__page-sub">Filled &amp; outlined text fields, selects, checkboxes, radio buttons, switches and sliders — all CSS</div>

    <!-- Text Fields -->
    <div class="md-04__card">
      <div class="md-04__card-title">Text Fields — Filled Style</div>
      <div class="md-04__grid">
        <div class="md-04__field md-04__field--filled">
          <input class="md-04__input" type="text" id="md04f1" placeholder=" ">
          <label class="md-04__label" for="md04f1">First Name</label>
        </div>
        <div class="md-04__field md-04__field--filled">
          <input class="md-04__input" type="text" id="md04f2" placeholder=" ">
          <label class="md-04__label" for="md04f2">Last Name</label>
        </div>
        <div class="md-04__field md-04__field--filled">
          <input class="md-04__input" type="email" id="md04f3" placeholder=" ">
          <label class="md-04__label" for="md04f3">Email Address</label>
        </div>
        <div class="md-04__field md-04__field--filled">
          <input class="md-04__input" type="tel" id="md04f4" placeholder=" ">
          <label class="md-04__label" for="md04f4">Phone Number</label>
        </div>
      </div>
    </div>

    <!-- Outlined Fields -->
    <div class="md-04__card">
      <div class="md-04__card-title">Text Fields — Outlined Style</div>
      <div class="md-04__grid">
        <div class="md-04__field md-04__field--outlined">
          <input class="md-04__input" type="text" id="md04o1" placeholder=" ">
          <label class="md-04__label" for="md04o1">Company Name</label>
        </div>
        <div class="md-04__field md-04__field--outlined">
          <input class="md-04__input" type="text" id="md04o2" placeholder=" ">
          <label class="md-04__label" for="md04o2">Job Title</label>
        </div>
        <div class="md-04__field md-04__field--outlined md-04__field--error" style="grid-column:1/-1">
          <input class="md-04__input" type="email" id="md04o3" value="invalid-email" placeholder=" ">
          <label class="md-04__label" for="md04o3">Email</label>
          <span class="md-04__helper md-04__helper--error">⚠ Please enter a valid email address</span>
        </div>
      </div>
    </div>

    <!-- Select + Textarea -->
    <div class="md-04__card">
      <div class="md-04__card-title">Select &amp; Textarea</div>
      <div style="display:flex;flex-direction:column;gap:24px">
        <div>
          <label style="font-size:.75rem;color:var(--ink2);display:block;margin-bottom:4px;padding:0 16px">Country / Region</label>
          <select class="md-04__select">
            <option>United States</option>
            <option>United Kingdom</option>
            <option>Germany</option>
            <option>Japan</option>
            <option>India</option>
          </select>
        </div>
        <div>
          <label style="font-size:.75rem;color:var(--ink2);display:block;margin-bottom:4px;padding:0 16px">Message</label>
          <textarea class="md-04__textarea" placeholder="Tell us about your project..."></textarea>
          <div class="md-04__helper">Max 500 characters</div>
        </div>
      </div>
    </div>

    <!-- Checkboxes, Radios, Switches -->
    <div class="md-04__card">
      <div class="md-04__card-title">Checkboxes &amp; Radio Buttons</div>
      <div class="md-04__grid">
        <div style="display:flex;flex-direction:column;gap:8px">
          <div style="font-size:.78rem;color:var(--ink2);font-weight:500;margin-bottom:4px">Preferences</div>
          <label class="md-04__check-wrap"><input class="md-04__check-input" type="checkbox" checked> <span class="md-04__check-label">Email notifications</span></label>
          <label class="md-04__check-wrap"><input class="md-04__check-input" type="checkbox" checked> <span class="md-04__check-label">Weekly digest</span></label>
          <label class="md-04__check-wrap"><input class="md-04__check-input" type="checkbox"> <span class="md-04__check-label">SMS alerts</span></label>
          <label class="md-04__check-wrap"><input class="md-04__check-input" type="checkbox"> <span class="md-04__check-label">Marketing updates</span></label>
        </div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div style="font-size:.78rem;color:var(--ink2);font-weight:500;margin-bottom:4px">Plan</div>
          <label class="md-04__radio-wrap"><input class="md-04__radio-input" type="radio" name="md04plan"> <span class="md-04__radio-label">Free</span></label>
          <label class="md-04__radio-wrap"><input class="md-04__radio-input" type="radio" name="md04plan" checked> <span class="md-04__radio-label">Pro — $12/mo</span></label>
          <label class="md-04__radio-wrap"><input class="md-04__radio-input" type="radio" name="md04plan"> <span class="md-04__radio-label">Enterprise</span></label>
        </div>
      </div>
      <div style="border-top:1px solid var(--divider);margin-top:24px;padding-top:24px;display:flex;flex-direction:column;gap:16px">
        <div style="font-size:.78rem;color:var(--ink2);font-weight:500">Toggles</div>
        <label class="md-04__switch-wrap">
          <input class="md-04__switch-input" id="md04s1" type="checkbox" checked>
          <div class="md-04__switch-track"><div class="md-04__switch-thumb"></div></div>
          <span class="md-04__switch-label">Dark mode</span>
        </label>
        <label class="md-04__switch-wrap">
          <input class="md-04__switch-input" id="md04s2" type="checkbox" checked>
          <div class="md-04__switch-track"><div class="md-04__switch-thumb"></div></div>
          <span class="md-04__switch-label">Auto-save</span>
        </label>
        <label class="md-04__switch-wrap">
          <input class="md-04__switch-input" id="md04s3" type="checkbox">
          <div class="md-04__switch-track"><div class="md-04__switch-thumb"></div></div>
          <span class="md-04__switch-label">Two-factor auth</span>
        </label>
      </div>
    </div>

    <!-- Slider -->
    <div class="md-04__card">
      <div class="md-04__card-title">Continuous Slider</div>
      <div style="padding:0 4px">
        <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--ink2);margin-bottom:4px"><span>Volume</span><span>60%</span></div>
        <input class="md-04__slider" type="range" min="0" max="100" value="60">
        <div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--ink3)"><span>0</span><span>100</span></div>
      </div>
      <div style="padding:0 4px;margin-top:20px">
        <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--ink2);margin-bottom:4px"><span>Budget</span><span>$3,000</span></div>
        <input class="md-04__slider" type="range" min="0" max="10000" value="3000">
        <div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--ink3)"><span>$0</span><span>$10k</span></div>
      </div>
    </div>

    <div class="md-04__form-actions">
      <button class="md-04__btn md-04__btn--outlined">Reset</button>
      <button class="md-04__btn">Save Changes</button>
    </div>
  </div>
</div>
```
## CSS
```css
.md-04,
.md-04 *,
.md-04 *::before,
.md-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-04 ::selection {
  background: #00695c;
  color: #fff;
}

.md-04 {
  --primary: #00695c;
  --primary-l: #4db6ac;
  --error: #b00020;
  --bg: #f1f8f7;
  --surface: #fff;
  --ink: #212121;
  --ink2: #616161;
  --ink3: #9e9e9e;
  --divider: #e0e0e0;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-04__wrap {
  max-width: 700px;
  margin: 0 auto;
}

.md-04__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-04__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 48px;
}

.md-04__card {
  background: var(--surface);
  border-radius: 12px;
  padding: 32px;
  margin-bottom: 28px;
  box-shadow: 0 1px 3px rgba(0,0,0,.1),0 1px 2px rgba(0,0,0,.06);
}

.md-04__card-title {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 8px;
}

.md-04__card-title::before {
  content: '';
  width: 4px;
  height: 1em;
  background: var(--primary);
  border-radius: 2px;
  display: inline-block;
}

.md-04__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

@media (max-width: 540px) {
  .md-04__grid {
    grid-template-columns: 1fr;
  }
}

.md-04__field {
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
}
/* ── FILLED TEXT FIELD ── */

.md-04__field--filled .md-04__label {
  position: absolute;
  left: 16px;
  top: 20px;
  font-size: 1rem;
  color: var(--ink2);
  pointer-events: none;
  transform-origin: left top;
  transition: transform .15s cubic-bezier(.4,0,.2,1),color .15s;
}

.md-04__field--filled .md-04__input {
  height: 56px;
  padding: 20px 16px 6px;
  background: rgba(0,0,0,.06);
  border: none;
  border-bottom: 1px solid var(--ink2);
  border-radius: 4px 4px 0 0;
  font-family: 'Roboto';
  font-size: 1rem;
  color: var(--ink);
  outline: none;
  width: 100%;
  transition: border-color .15s;
}

.md-04__field--filled .md-04__input:focus {
  border-bottom: 2px solid var(--primary);
}

.md-04__field--filled .md-04__input:focus ~ .md-04__label,
.md-04__field--filled .md-04__input:not(:placeholder-shown) ~ .md-04__label {
  transform: translateY(-10px) scale(.75);
  color: var(--primary);
}

.md-04__field--filled .md-04__input::placeholder {
  opacity: 0;
}
/* ── OUTLINED TEXT FIELD ── */

.md-04__field--outlined {
  position: relative;
}

.md-04__field--outlined .md-04__label {
  position: absolute;
  left: 12px;
  top: 16px;
  font-size: 1rem;
  color: var(--ink2);
  pointer-events: none;
  transform-origin: left top;
  transition: transform .15s cubic-bezier(.4,0,.2,1),color .15s,background .15s;
  padding: 0 4px;
}

.md-04__field--outlined .md-04__input {
  height: 56px;
  padding: 0 16px;
  background: var(--surface);
  border: 1px solid var(--ink2);
  border-radius: 4px;
  font-family: 'Roboto';
  font-size: 1rem;
  color: var(--ink);
  outline: none;
  width: 100%;
  transition: border-color .15s;
}

.md-04__field--outlined .md-04__input:focus {
  border: 2px solid var(--primary);
}

.md-04__field--outlined .md-04__input:focus ~ .md-04__label,
.md-04__field--outlined .md-04__input:not(:placeholder-shown) ~ .md-04__label {
  transform: translateY(-24px) scale(.75);
  color: var(--primary);
  background: var(--surface);
}

.md-04__field--outlined .md-04__input::placeholder {
  opacity: 0;
}
/* ── ERROR STATE ── */

.md-04__field--error .md-04__input {
  border-color: var(--error)!important;
}

.md-04__field--error .md-04__label {
  color: var(--error)!important;
}

.md-04__helper {
  font-size: .75rem;
  margin-top: 4px;
  padding: 0 16px;
  color: var(--ink3);
}

.md-04__helper--error {
  color: var(--error);
}
/* ── TEXTAREA ── */

.md-04__textarea {
  padding: 16px;
  resize: vertical;
  min-height: 120px;
  background: rgba(0,0,0,.06);
  border: none;
  border-bottom: 1px solid var(--ink2);
  border-radius: 4px 4px 0 0;
  font-family: 'Roboto';
  font-size: 1rem;
  color: var(--ink);
  outline: none;
  width: 100%;
  transition: border-color .15s;
}

.md-04__textarea:focus {
  border-bottom: 2px solid var(--primary);
}
/* ── SELECT / DROPDOWN ── */

.md-04__select {
  height: 56px;
  padding: 0 16px;
  background: rgba(0,0,0,.06);
  border: none;
  border-bottom: 1px solid var(--ink2);
  border-radius: 4px 4px 0 0;
  font-family: 'Roboto';
  font-size: 1rem;
  color: var(--ink);
  outline: none;
  width: 100%;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23757575' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  cursor: pointer;
}

.md-04__select:focus {
  border-bottom: 2px solid var(--primary);
}
/* ── CHECKBOX ── */

.md-04__check-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 4px 0;
}

.md-04__check-input {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid var(--ink2);
  border-radius: 3px;
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: background .15s,border-color .15s;
}

.md-04__check-input:checked {
  background: var(--primary);
  border-color: var(--primary);
}

.md-04__check-input:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  color: #fff;
  font-size: .8rem;
  font-weight: 700;
  line-height: 1;
}

.md-04__check-label {
  font-size: .9rem;
  color: var(--ink);
}
/* ── RADIO ── */

.md-04__radio-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 4px 0;
}

.md-04__radio-input {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid var(--ink2);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: border-color .15s;
}

.md-04__radio-input:checked {
  border-color: var(--primary);
}

.md-04__radio-input:checked::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--primary);
}

.md-04__radio-label {
  font-size: .9rem;
  color: var(--ink);
}
/* ── SWITCH ── */

.md-04__switch-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.md-04__switch-input {
  display: none;
}

.md-04__switch-track {
  width: 52px;
  height: 32px;
  border-radius: 16px;
  background: #bdbdbd;
  position: relative;
  transition: background .2s;
  flex-shrink: 0;
}

.md-04__switch-thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,.3);
  transition: transform .2s cubic-bezier(.4,0,.2,1);
}

.md-04__switch-input:checked ~ .md-04__switch-track {
  background: var(--primary-l);
}

.md-04__switch-input:checked ~ .md-04__switch-track .md-04__switch-thumb {
  transform: translateX(20px);
}

.md-04__switch-label {
  font-size: .9rem;
  color: var(--ink);
}
/* ── SLIDER ── */

.md-04__slider {
  width: 100%;
  height: 4px;
  border-radius: 2px;
  -webkit-appearance: none;
  background: linear-gradient(to right,var(--primary) 60%,var(--divider) 60%);
  cursor: pointer;
  outline: none;
  margin: 16px 0;
}

.md-04__slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--primary);
  box-shadow: 0 2px 4px rgba(0,0,0,.3);
  cursor: pointer;
  transition: box-shadow .2s;
}

.md-04__slider::-webkit-slider-thumb:hover {
  box-shadow: 0 0 0 8px rgba(0,105,92,.15);
}

.md-04__btn {
  height: 40px;
  padding: 0 24px;
  border: none;
  border-radius: 4px;
  background: var(--primary);
  color: #fff;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  cursor: pointer;
  transition: box-shadow .2s;
  box-shadow: 0 2px 4px rgba(0,0,0,.2);
}

.md-04__btn:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,.25);
}

.md-04__btn--outlined {
  background: transparent;
  color: var(--primary);
  border: 1px solid var(--primary);
  box-shadow: none;
}

.md-04__form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .md-04 * {
    transition: none!important;
  }
}
```
