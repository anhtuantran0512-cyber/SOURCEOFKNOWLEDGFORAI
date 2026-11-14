---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-color-palette-css/"
title: "Material Design Color Palette CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Interactive five-theme Material Design 3 colour switcher — purple, teal, red, green, pink — with live colour role grid, tonal surfaces, and a live UI preview…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Color Palette CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-color-palette-css/

Interactive five-theme Material Design 3 colour switcher — purple, teal, red, green, pink — with live colour role grid, tonal surfaces, and a live UI preview panel, all driven by CSS custom properties and radio inputs.
## HTML
```html
<!-- Radio inputs for theme switching — OUTSIDE .md-13 -->
<input class="md-13-radios" type="radio" name="md13-theme" id="md13-t1" checked>
<input class="md-13-radios" type="radio" name="md13-theme" id="md13-t2">
<input class="md-13-radios" type="radio" name="md13-theme" id="md13-t3">
<input class="md-13-radios" type="radio" name="md13-theme" id="md13-t4">
<input class="md-13-radios" type="radio" name="md13-theme" id="md13-t5">

<div class="md-13">

  <!-- Theme picker -->
  <h3>Select Theme</h3>
  <div class="theme-picker">
    <label class="theme-swatch-label" for="md13-t1">
      <div class="theme-dot swatch-purple"></div>
      <span class="theme-label">Purple</span>
    </label>
    <label class="theme-swatch-label" for="md13-t2">
      <div class="theme-dot swatch-teal"></div>
      <span class="theme-label">Teal</span>
    </label>
    <label class="theme-swatch-label" for="md13-t3">
      <div class="theme-dot swatch-red"></div>
      <span class="theme-label">Red</span>
    </label>
    <label class="theme-swatch-label" for="md13-t4">
      <div class="theme-dot swatch-green"></div>
      <span class="theme-label">Green</span>
    </label>
    <label class="theme-swatch-label" for="md13-t5">
      <div class="theme-dot swatch-pink"></div>
      <span class="theme-label">Pink</span>
    </label>
  </div>

  <!-- Color palette display -->
  <h3>Color Roles</h3>
  <div class="palette-grid">
    <div class="palette-chip chip-primary"><span class="chip-label">Primary</span></div>
    <div class="palette-chip chip-primary-dark"><span class="chip-label">On Primary</span></div>
    <div class="palette-chip chip-primary-light"><span class="chip-label">Primary Container</span></div>
    <div class="palette-chip chip-secondary"><span class="chip-label">Secondary</span></div>
    <div class="palette-chip chip-sec-light"><span class="chip-label">Secondary Cont.</span></div>
    <div class="palette-chip chip-tertiary"><span class="chip-label">Tertiary</span></div>
    <div class="palette-chip chip-tert-light"><span class="chip-label">Tertiary Cont.</span></div>
    <div class="palette-chip chip-surface"><span class="chip-label">Surface</span></div>
    <div class="palette-chip chip-surface-var"><span class="chip-label">Surface Variant</span></div>
  </div>

  <!-- Tonal elevation -->
  <h3>Tonal Surfaces</h3>
  <div class="tonal-row">
    <div class="tonal-el tonal-el-1">Primary</div>
    <div class="tonal-el tonal-el-2">Dark</div>
    <div class="tonal-el tonal-el-3">Container</div>
    <div class="tonal-el tonal-el-4">Variant</div>
  </div>

  <!-- Live UI preview -->
  <h3>Live Preview</h3>
  <div class="preview-card">
    <div class="preview-topbar">
      <span class="preview-topbar-title">My App</span>
      <div class="preview-topbar-dots">
        <span></span><span></span><span></span>
      </div>
    </div>
    <div class="preview-body">
      <div class="preview-section-title">Filters</div>
      <div class="preview-chips">
        <span class="preview-chip preview-chip--filled">All</span>
        <span class="preview-chip">Recent</span>
        <span class="preview-chip">Starred</span>
      </div>
      <div class="preview-section-title">Actions</div>
      <div class="preview-btns">
        <button class="preview-btn preview-btn--filled">Confirm</button>
        <button class="preview-btn preview-btn--tonal">Maybe</button>
        <button class="preview-btn preview-btn--outline">Cancel</button>
      </div>
      <div class="preview-fab">+</div>
    </div>
  </div>

</div>

<style>
  .md-13-radios { display: none; }
  @media (prefers-reduced-motion: reduce) {
    .md-13 .palette-chip,
    .md-13 .preview-card,
    .md-13 .preview-topbar,
    .md-13 .preview-btn,
    .md-13 .preview-chip,
    .md-13 .preview-fab,
    .md-13 .tonal-el,
    .md-13 .theme-dot { transition: none !important; }
  }
</style>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
/* ── CSS-only theme switcher via hidden radio inputs ── */

#md13-t1:checked ~ .md-13 {
  --primary: #6750a4;
  --primary-dark: #4f3d7a;
  --primary-light: #eaddff;
  --primary-on: #ffffff;
  --secondary: #625b71;
  --secondary-light: #e8def8;
  --tertiary: #7d5260;
  --tertiary-light: #ffd8e4;
  --surface: #fffbfe;
  --surface-variant: #e7e0ec;
  --on-surface: #1c1b1f;
  --theme-name: "Purple (Default)";
}

#md13-t2:checked ~ .md-13 {
  --primary: #006874;
  --primary-dark: #004f58;
  --primary-light: #a2d0d8;
  --primary-on: #ffffff;
  --secondary: #4a6267;
  --secondary-light: #cce8ed;
  --tertiary: #525e7d;
  --tertiary-light: #dae2ff;
  --surface: #fafdfe;
  --surface-variant: #dbe4e6;
  --on-surface: #191c1d;
  --theme-name: "Teal";
}

#md13-t3:checked ~ .md-13 {
  --primary: #b5271f;
  --primary-dark: #8c1c16;
  --primary-light: #ffdad6;
  --primary-on: #ffffff;
  --secondary: #775651;
  --secondary-light: #ffdad6;
  --tertiary: #715c2e;
  --tertiary-light: #fcdea7;
  --surface: #fffbff;
  --surface-variant: #f5dedd;
  --on-surface: #201a19;
  --theme-name: "Red";
}

#md13-t4:checked ~ .md-13 {
  --primary: #386a20;
  --primary-dark: #255010;
  --primary-light: #b7f397;
  --primary-on: #ffffff;
  --secondary: #55624c;
  --secondary-light: #d8e7cb;
  --tertiary: #386667;
  --tertiary-light: #bcebec;
  --surface: #fdfdf6;
  --surface-variant: #dee5d4;
  --on-surface: #1a1c18;
  --theme-name: "Green";
}

#md13-t5:checked ~ .md-13 {
  --primary: #984061;
  --primary-dark: #72294a;
  --primary-light: #ffd8e4;
  --primary-on: #ffffff;
  --secondary: #74565f;
  --secondary-light: #ffd9e2;
  --tertiary: #7b4e00;
  --tertiary-light: #ffddad;
  --surface: #fffbff;
  --surface-variant: #f2dde2;
  --on-surface: #201a1b;
  --theme-name: "Pink";
}

.md-13-radios {
  display: none;
}

.md-13 {
  --primary: #6750a4;
  --primary-dark: #4f3d7a;
  --primary-light: #eaddff;
  --primary-on: #ffffff;
  --secondary: #625b71;
  --secondary-light: #e8def8;
  --tertiary: #7d5260;
  --tertiary-light: #ffd8e4;
  --surface: #fffbfe;
  --surface-variant: #e7e0ec;
  --on-surface: #1c1b1f;
  --outline: #79747e;
  --outline-variant: #cac4d0;
  all: unset;
  display: block;
  font-family: 'Roboto', sans-serif;
  background: #f3f3f7;
  padding: 32px 24px;
  box-sizing: border-box;
  color: var(--on-surface);
}

.md-13 *,
.md-13 *::before,
.md-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
/* ── Section labels ── */

.md-13 h3 {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--outline);
  margin-bottom: 12px;
  margin-top: 32px;
}

.md-13 h3:first-child {
  margin-top: 0;
}
/* ── Theme picker ── */

.md-13 .theme-picker {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 4px;
}

.md-13 .theme-swatch-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.md-13 .theme-dot {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 3px solid transparent;
  position: relative;
  transition: border-color 200ms, transform 150ms;
  box-shadow: 0 2px 6px rgba(0,0,0,.2);
}

.md-13 .theme-dot::after {
  content: '';
  width: 14px;
  height: 14px;
  background: rgba(255,255,255,.9);
  border-radius: 50%;
  position: absolute;
  bottom: -1px;
  right: -1px;
  opacity: 0;
  transition: opacity 200ms;
}

.md-13 .theme-swatch-label:hover .theme-dot {
  transform: scale(1.1);
}

.md-13 .theme-label {
  font-size: 11px;
  color: var(--outline);
}
/* Swatch colors */

.md-13 .swatch-purple {
  background: #6750a4;
}

.md-13 .swatch-teal {
  background: #006874;
}

.md-13 .swatch-red {
  background: #b5271f;
}

.md-13 .swatch-green {
  background: #386a20;
}

.md-13 .swatch-pink {
  background: #984061;
}
/* Active swatch gets border + checkmark */

#md13-t1:checked ~ .md-13 .swatch-purple,
#md13-t2:checked ~ .md-13 .swatch-teal,
#md13-t3:checked ~ .md-13 .swatch-red,
#md13-t4:checked ~ .md-13 .swatch-green,
#md13-t5:checked ~ .md-13 .swatch-pink {
  border-color: var(--on-surface);
  transform: scale(1.1);
}

#md13-t1:checked ~ .md-13 .swatch-purple::after,
#md13-t2:checked ~ .md-13 .swatch-teal::after,
#md13-t3:checked ~ .md-13 .swatch-red::after,
#md13-t4:checked ~ .md-13 .swatch-green::after,
#md13-t5:checked ~ .md-13 .swatch-pink::after {
  opacity: 1;
}
/* ── Color palette grid ── */

.md-13 .palette-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.md-13 .palette-chip {
  border-radius: 12px;
  padding: 14px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: background 400ms ease, color 400ms ease;
}

.md-13 .palette-chip .chip-label {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: .5px;
}

.md-13 .palette-chip .chip-hex {
  font-size: 10px;
  opacity: .7;
  font-family: monospace;
}

.md-13 .chip-primary {
  background: var(--primary);
  color: var(--primary-on);
}

.md-13 .chip-primary-dark {
  background: var(--primary-dark);
  color: #fff;
}

.md-13 .chip-primary-light {
  background: var(--primary-light);
  color: var(--on-surface);
}

.md-13 .chip-secondary {
  background: var(--secondary);
  color: #fff;
}

.md-13 .chip-sec-light {
  background: var(--secondary-light);
  color: var(--on-surface);
}

.md-13 .chip-tertiary {
  background: var(--tertiary);
  color: #fff;
}

.md-13 .chip-tert-light {
  background: var(--tertiary-light);
  color: var(--on-surface);
}

.md-13 .chip-surface {
  background: var(--surface);
  color: var(--on-surface);
  border: 1px solid var(--outline-variant);
}

.md-13 .chip-surface-var {
  background: var(--surface-variant);
  color: var(--on-surface);
}
/* ── Live UI preview ── */

.md-13 .preview-card {
  background: var(--surface);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,.12);
  transition: background 400ms;
}

.md-13 .preview-topbar {
  background: var(--primary);
  color: var(--primary-on);
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: background 400ms;
}

.md-13 .preview-topbar-title {
  font-size: 16px;
  font-weight: 500;
  flex: 1;
}

.md-13 .preview-topbar-dots {
  display: flex;
  gap: 3px;
}

.md-13 .preview-topbar-dots span {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(255,255,255,.7);
}

.md-13 .preview-body {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.md-13 .preview-section-title {
  font-size: 12px;
  font-weight: 500;
  color: var(--secondary);
  text-transform: uppercase;
  letter-spacing: .8px;
  transition: color 400ms;
}

.md-13 .preview-chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.md-13 .preview-chip {
  padding: 6px 14px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  background: var(--primary-light);
  color: var(--primary);
  transition: background 400ms, color 400ms;
}

.md-13 .preview-chip--filled {
  background: var(--primary);
  color: var(--primary-on);
}

.md-13 .preview-btns {
  display: flex;
  gap: 8px;
}

.md-13 .preview-btn {
  padding: 9px 18px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  letter-spacing: .3px;
  transition: background 400ms, color 400ms;
}

.md-13 .preview-btn--filled {
  background: var(--primary);
  color: var(--primary-on);
}

.md-13 .preview-btn--tonal {
  background: var(--secondary-light);
  color: var(--secondary);
}

.md-13 .preview-btn--outline {
  background: transparent;
  color: var(--primary);
  border: 1px solid var(--primary);
}

.md-13 .preview-fab {
  width: 44px;
  height: 44px;
  border-radius: 14px;
  background: var(--tertiary);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 0 3px 8px rgba(0,0,0,.2);
  align-self: flex-end;
  transition: background 400ms;
}
/* ── Material 3 Tonal Surface row ── */

.md-13 .tonal-row {
  display: flex;
  gap: 8px;
}

.md-13 .tonal-el {
  flex: 1;
  padding: 12px 8px;
  border-radius: 12px;
  text-align: center;
  font-size: 11px;
  font-weight: 500;
  transition: background 400ms, color 400ms;
}

.md-13 .tonal-el-1 {
  background: var(--primary);
  color: var(--primary-on);
}

.md-13 .tonal-el-2 {
  background: var(--primary-dark);
  color: #fff;
}

.md-13 .tonal-el-3 {
  background: var(--primary-light);
  color: var(--on-surface);
}

.md-13 .tonal-el-4 {
  background: var(--surface-variant);
  color: var(--on-surface);
}
```
