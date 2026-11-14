---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-buttons-css/"
title: "Material Design Buttons CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Filled, outlined, text, elevated, tonal, and FAB buttons plus toggle groups and filter chips — all Material Design 3, zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Buttons CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-buttons-css/

Filled, outlined, text, elevated, tonal, and FAB buttons plus toggle groups and filter chips — all Material Design 3, zero JavaScript.
## HTML
```html
<div class="md-01">
  <div class="md-01__page-title">Material Design 3 Buttons</div>
  <div class="md-01__page-sub">Production-ready CSS button components — filled, outlined, text, FAB, icon &amp; chip variants</div>

  <div class="md-01__section">
    <div class="md-01__section-label">Contained / Filled Buttons</div>
    <div class="md-01__row">
      <button class="md-01__btn md-01__btn--filled"><span class="md-01__btn-icon">🚀</span>Launch</button>
      <button class="md-01__btn md-01__btn--filled-teal"><span class="md-01__btn-icon">✓</span>Confirm</button>
      <button class="md-01__btn md-01__btn--filled-err"><span class="md-01__btn-icon">✕</span>Delete</button>
      <button class="md-01__btn md-01__btn--filled-warn"><span class="md-01__btn-icon">⚠</span>Warning</button>
      <button class="md-01__btn md-01__btn--filled-ok"><span class="md-01__btn-icon">↓</span>Download</button>
      <button class="md-01__btn md-01__btn--disabled">Disabled</button>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Outlined Buttons</div>
    <div class="md-01__row">
      <button class="md-01__btn md-01__btn--outlined"><span class="md-01__btn-icon">♡</span>Save</button>
      <button class="md-01__btn md-01__btn--outlined-teal"><span class="md-01__btn-icon">↗</span>Share</button>
      <button class="md-01__btn md-01__btn--outlined-err"><span class="md-01__btn-icon">🗑</span>Remove</button>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Text Buttons</div>
    <div class="md-01__row">
      <button class="md-01__btn md-01__btn--text">Learn more</button>
      <button class="md-01__btn md-01__btn--text">View details</button>
      <button class="md-01__btn md-01__btn--text-teal">Cancel</button>
      <button class="md-01__btn md-01__btn--text-teal">Skip for now</button>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Floating Action Buttons</div>
    <div class="md-01__row">
      <button class="md-01__fab">+</button>
      <button class="md-01__fab md-01__fab--teal">✏</button>
      <button class="md-01__fab md-01__fab--mini">♥</button>
      <button class="md-01__fab md-01__fab--extended"><span>✏</span>Compose</button>
      <button class="md-01__fab md-01__fab--extended md-01__fab--teal"><span>+</span>New item</button>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Icon Buttons</div>
    <div class="md-01__row">
      <button class="md-01__iconbtn">♡</button>
      <button class="md-01__iconbtn">🔖</button>
      <button class="md-01__iconbtn md-01__iconbtn--filled">★</button>
      <button class="md-01__iconbtn md-01__iconbtn--outlined">↗</button>
      <button class="md-01__iconbtn md-01__iconbtn--tonal">✏</button>
      <button class="md-01__iconbtn md-01__iconbtn--tonal">⚙</button>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Toggle Button Group</div>
    <div class="md-01__row">
      <div class="md-01__toggle-group">
        <input type="radio" name="md01-view" id="md01-t1" checked>
        <label for="md01-t1">📋 List</label>
        <input type="radio" name="md01-view" id="md01-t2">
        <label for="md01-t2">⊞ Grid</label>
        <input type="radio" name="md01-view" id="md01-t3">
        <label for="md01-t3">📊 Chart</label>
      </div>
    </div>
  </div>

  <div class="md-01__section">
    <div class="md-01__section-label">Filter Chip Buttons</div>
    <div class="md-01__row">
      <button class="md-01__chip md-01__chip--selected"><span class="md-01__chip-icon">✓</span>All</button>
      <button class="md-01__chip"><span class="md-01__chip-icon">🎨</span>Design</button>
      <button class="md-01__chip"><span class="md-01__chip-icon">⚡</span>Development</button>
      <button class="md-01__chip"><span class="md-01__chip-icon">📱</span>Mobile</button>
      <button class="md-01__chip"><span class="md-01__chip-icon">☁</span>Cloud</button>
      <button class="md-01__chip"><span class="md-01__chip-icon">🔒</span>Security</button>
    </div>
  </div>
</div>
```
## CSS
```css
.md-01,
.md-01 *,
.md-01 *::before,
.md-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-01 ::selection {
  background: #6200ea;
  color: #fff;
}

.md-01 {
  --md-primary: #6200ea;
  --md-secondary: #03dac6;
  --md-error: #b00020;
  --md-warning: #ff6d00;
  --md-success: #00c853;
  --md-surface: #fff;
  --md-bg: #f5f5f5;
  --md-on-primary: #fff;
  --md-ink: #212121;
  --md-ink2: #757575;
  --md-elev1: 0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);
  --md-elev2: 0 3px 6px rgba(0,0,0,.15),0 2px 4px rgba(0,0,0,.12);
  --md-elev4: 0 10px 20px rgba(0,0,0,.15),0 3px 6px rgba(0,0,0,.1);
  --md-elev6: 0 15px 25px rgba(0,0,0,.15),0 5px 10px rgba(0,0,0,.05);
  font-family: 'Roboto',sans-serif;
  background: var(--md-bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--md-ink);
}

.md-01__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 4px;
  color: var(--md-ink);
}

.md-01__page-sub {
  font-size: .9rem;
  color: var(--md-ink2);
  margin-bottom: 48px;
}

.md-01__section {
  margin-bottom: 48px;
}

.md-01__section-label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--md-ink2);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.md-01__section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #e0e0e0;
}

.md-01__row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
}
/* ── Contained (Filled) ── */

.md-01__btn {
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  padding: 0 16px;
  height: 36px;
  transition: box-shadow .2s cubic-bezier(.4,0,.2,1);
  white-space: nowrap;
}

.md-01__btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  transform: translate(-50%,-50%);
  transition: width .4s ease,height .4s ease,opacity .4s ease;
  opacity: 0;
}

.md-01__btn:hover::after {
  width: 200px;
  height: 200px;
  opacity: .1;
}

.md-01__btn:active::after {
  width: 220px;
  height: 220px;
  opacity: .2;
  transition: width .1s,height .1s,opacity .1s;
}
/* contained variants */

.md-01__btn--filled {
  background: var(--md-primary);
  color: #fff;
  box-shadow: var(--md-elev1);
}

.md-01__btn--filled:hover {
  box-shadow: var(--md-elev2);
}

.md-01__btn--filled::after {
  background: #fff;
}

.md-01__btn--filled-teal {
  background: var(--md-secondary);
  color: #000;
}

.md-01__btn--filled-teal:hover {
  box-shadow: var(--md-elev2);
}

.md-01__btn--filled-teal::after {
  background: #000;
}

.md-01__btn--filled-err {
  background: var(--md-error);
  color: #fff;
  box-shadow: var(--md-elev1);
}

.md-01__btn--filled-err:hover {
  box-shadow: var(--md-elev2);
}

.md-01__btn--filled-err::after {
  background: #fff;
}

.md-01__btn--filled-warn {
  background: var(--md-warning);
  color: #fff;
  box-shadow: var(--md-elev1);
}

.md-01__btn--filled-warn:hover {
  box-shadow: var(--md-elev2);
}

.md-01__btn--filled-warn::after {
  background: #fff;
}

.md-01__btn--filled-ok {
  background: var(--md-success);
  color: #fff;
  box-shadow: var(--md-elev1);
}

.md-01__btn--filled-ok:hover {
  box-shadow: var(--md-elev2);
}

.md-01__btn--filled-ok::after {
  background: #fff;
}
/* outlined */

.md-01__btn--outlined {
  background: transparent;
  color: var(--md-primary);
  border: 1px solid rgba(98,0,234,.5);
}

.md-01__btn--outlined:hover {
  background: rgba(98,0,234,.04);
  border-color: var(--md-primary);
}

.md-01__btn--outlined::after {
  background: var(--md-primary);
}

.md-01__btn--outlined-teal {
  background: transparent;
  color: #018786;
  border: 1px solid rgba(1,135,134,.5);
}

.md-01__btn--outlined-teal:hover {
  background: rgba(1,135,134,.04);
}

.md-01__btn--outlined-teal::after {
  background: #018786;
}

.md-01__btn--outlined-err {
  background: transparent;
  color: var(--md-error);
  border: 1px solid rgba(176,0,32,.5);
}

.md-01__btn--outlined-err:hover {
  background: rgba(176,0,32,.04);
}

.md-01__btn--outlined-err::after {
  background: var(--md-error);
}
/* text */

.md-01__btn--text {
  background: transparent;
  color: var(--md-primary);
  padding: 0 8px;
}

.md-01__btn--text:hover {
  background: rgba(98,0,234,.04);
}

.md-01__btn--text::after {
  background: var(--md-primary);
}

.md-01__btn--text-teal {
  background: transparent;
  color: #018786;
  padding: 0 8px;
}

.md-01__btn--text-teal:hover {
  background: rgba(1,135,134,.04);
}

.md-01__btn--text-teal::after {
  background: #018786;
}
/* icon + label */

.md-01__btn-icon {
  font-size: 1.1rem;
  line-height: 1;
}
/* disabled */

.md-01__btn--disabled {
  background: rgba(0,0,0,.12);
  color: rgba(0,0,0,.37);
  cursor: not-allowed;
  pointer-events: none;
  box-shadow: none;
}
/* FAB */

.md-01__fab {
  position: relative;
  overflow: hidden;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  border: none;
  cursor: pointer;
  background: var(--md-primary);
  color: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  box-shadow: var(--md-elev4);
  transition: box-shadow .2s,transform .2s;
}

.md-01__fab:hover {
  box-shadow: var(--md-elev6);
  transform: translateY(-2px);
}

.md-01__fab::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: #fff;
  transform: translate(-50%,-50%);
  transition: width .4s ease,height .4s ease,opacity .4s ease;
  opacity: 0;
}

.md-01__fab:hover::after {
  width: 80px;
  height: 80px;
  opacity: .15;
}

.md-01__fab--mini {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  font-size: 1.1rem;
  background: var(--md-secondary);
  color: #000;
  box-shadow: var(--md-elev2);
}

.md-01__fab--extended {
  width: auto;
  padding: 0 20px;
  gap: 10px;
  border-radius: 16px;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
}

.md-01__fab--teal {
  background: var(--md-secondary);
  color: #000;
}

.md-01__fab--teal::after {
  background: #000;
}
/* Icon buttons */

.md-01__iconbtn {
  position: relative;
  overflow: hidden;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  background: transparent;
  color: var(--md-primary);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  transition: background .2s;
}

.md-01__iconbtn:hover {
  background: rgba(98,0,234,.08);
}

.md-01__iconbtn--filled {
  background: var(--md-primary);
  color: #fff;
}

.md-01__iconbtn--filled:hover {
  box-shadow: var(--md-elev1);
}

.md-01__iconbtn--outlined {
  border: 1px solid rgba(98,0,234,.4);
}

.md-01__iconbtn--tonal {
  background: rgba(98,0,234,.12);
  color: var(--md-primary);
}
/* toggle group */

.md-01__toggle-group {
  display: inline-flex;
  border: 1px solid #c4c4c4;
  border-radius: 4px;
  overflow: hidden;
}

.md-01__toggle-group input[type=radio] {
  display: none;
}

.md-01__toggle-group label {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 0 16px;
  height: 36px;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  color: var(--md-primary);
  background: #fff;
  border-right: 1px solid #c4c4c4;
  transition: background .15s;
  user-select: none;
}

.md-01__toggle-group label:last-of-type {
  border-right: none;
}

.md-01__toggle-group input:checked + label {
  background: rgba(98,0,234,.12);
}
/* chip buttons */

.md-01__chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 32px;
  padding: 0 12px;
  border-radius: 8px;
  border: 1px solid #c4c4c4;
  background: #fff;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 400;
  color: var(--md-ink);
  cursor: pointer;
  transition: background .15s,box-shadow .15s;
}

.md-01__chip:hover {
  box-shadow: var(--md-elev1);
  background: #f9f9f9;
}

.md-01__chip--selected {
  background: rgba(98,0,234,.12);
  border-color: var(--md-primary);
  color: var(--md-primary);
}

.md-01__chip-icon {
  font-size: .9rem;
}

@media (prefers-reduced-motion: reduce) {
  .md-01 * {
    transition: none!important;
    animation: none!important;
  }
}
```
