---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-chip-css/"
title: "Material Design Chip CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Suggestion, filter (checkbox-interactive), choice (radio-interactive), input with avatar, tonal, filled, outlined, status, elevated, and segmented chip…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Chip CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-chip-css/

Suggestion, filter (checkbox-interactive), choice (radio-interactive), input with avatar, tonal, filled, outlined, status, elevated, and segmented chip variants — all Material Design 3.
## HTML
```html
<div class="md-08">
  <div class="md-08__wrap">
    <div class="md-08__page-title">Material Design Chips CSS</div>
    <div class="md-08__page-sub">Filter, choice, input, suggestion and status chips — all CSS, checkbox-hack interactive filtering</div>

    <!-- Assist / Suggestion Chips -->
    <div class="md-08__section">
      <div class="md-08__section-title">Suggestion &amp; Assist Chips</div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--suggestion"><span class="md-08__chip-icon">✨</span>Add to calendar</div>
        <div class="md-08__chip md-08__chip--suggestion"><span class="md-08__chip-icon">📍</span>Add location</div>
        <div class="md-08__chip md-08__chip--suggestion"><span class="md-08__chip-icon">👥</span>Invite people</div>
        <div class="md-08__chip md-08__chip--suggestion"><span class="md-08__chip-icon">🔗</span>Copy link</div>
        <div class="md-08__chip md-08__chip--suggestion"><span class="md-08__chip-icon">📧</span>Send email</div>
      </div>
    </div>

    <!-- Filter Chips -->
    <div class="md-08__section">
      <div class="md-08__section-title">Filter Chips (Interactive — click to toggle)</div>
      <div class="md-08__chip-row">
        <input class="md-08__filter-in" type="checkbox" id="md08f1" checked>
        <label class="md-08__filter-lbl" for="md08f1"><span class="md-08__chip-icon">🎨</span>Design</label>
        <input class="md-08__filter-in" type="checkbox" id="md08f2">
        <label class="md-08__filter-lbl" for="md08f2"><span class="md-08__chip-icon">⚡</span>Development</label>
        <input class="md-08__filter-in" type="checkbox" id="md08f3" checked>
        <label class="md-08__filter-lbl" for="md08f3"><span class="md-08__chip-icon">📱</span>Mobile</label>
        <input class="md-08__filter-in" type="checkbox" id="md08f4">
        <label class="md-08__filter-lbl" for="md08f4"><span class="md-08__chip-icon">☁</span>Cloud</label>
        <input class="md-08__filter-in" type="checkbox" id="md08f5">
        <label class="md-08__filter-lbl" for="md08f5"><span class="md-08__chip-icon">🔒</span>Security</label>
        <input class="md-08__filter-in" type="checkbox" id="md08f6">
        <label class="md-08__filter-lbl" for="md08f6"><span class="md-08__chip-icon">📊</span>Analytics</label>
      </div>
    </div>

    <!-- Choice Chips -->
    <div class="md-08__section">
      <div class="md-08__section-title">Choice Chips (Single Select)</div>
      <div class="md-08__chip-row">
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c1">
        <label class="md-08__choice-lbl" for="md08c1">XS</label>
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c2">
        <label class="md-08__choice-lbl" for="md08c2">S</label>
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c3" checked>
        <label class="md-08__choice-lbl" for="md08c3">M</label>
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c4">
        <label class="md-08__choice-lbl" for="md08c4">L</label>
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c5">
        <label class="md-08__choice-lbl" for="md08c5">XL</label>
        <input class="md-08__choice-in" type="radio" name="md08size" id="md08c6">
        <label class="md-08__choice-lbl" for="md08c6">2XL</label>
      </div>
      <div class="md-08__chip-row">
        <input class="md-08__choice-in" type="radio" name="md08sort" id="md08s1" checked>
        <label class="md-08__choice-lbl" for="md08s1">⬆ Price: Low to High</label>
        <input class="md-08__choice-in" type="radio" name="md08sort" id="md08s2">
        <label class="md-08__choice-lbl" for="md08s2">⬇ Price: High to Low</label>
        <input class="md-08__choice-in" type="radio" name="md08sort" id="md08s3">
        <label class="md-08__choice-lbl" for="md08s3">★ Top Rated</label>
        <input class="md-08__choice-in" type="radio" name="md08sort" id="md08s4">
        <label class="md-08__choice-lbl" for="md08s4">🆕 Newest</label>
      </div>
    </div>

    <!-- Input Chips (avatar) -->
    <div class="md-08__section">
      <div class="md-08__section-title">Input Chips with Avatars</div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--input"><div class="md-08__chip-avatar" style="background:#ad1457">A</div>Alex T.<button class="md-08__chip-close">✕</button></div>
        <div class="md-08__chip md-08__chip--input"><div class="md-08__chip-avatar" style="background:#1565c0">M</div>Maria C.<button class="md-08__chip-close">✕</button></div>
        <div class="md-08__chip md-08__chip--input"><div class="md-08__chip-avatar" style="background:#00897b">J</div>Jordan K.<button class="md-08__chip-close">✕</button></div>
        <div class="md-08__chip md-08__chip--input"><div class="md-08__chip-avatar" style="background:#7b1fa2">S</div>Sam R.<button class="md-08__chip-close">✕</button></div>
      </div>
      <div class="md-08__tag-input">
        <div class="md-08__chip md-08__chip--input" style="height:28px;font-size:.8rem"><span class="md-08__chip-icon">🏷</span>Material Design<button class="md-08__chip-close">✕</button></div>
        <div class="md-08__chip md-08__chip--input" style="height:28px;font-size:.8rem"><span class="md-08__chip-icon">🏷</span>CSS<button class="md-08__chip-close">✕</button></div>
        <div class="md-08__chip md-08__chip--input" style="height:28px;font-size:.8rem"><span class="md-08__chip-icon">🏷</span>UI Components<button class="md-08__chip-close">✕</button></div>
        <input class="md-08__tag-field" type="text" placeholder="Add tag...">
      </div>
    </div>

    <!-- Outlined / Tonal / Filled -->
    <div class="md-08__section">
      <div class="md-08__section-title">Tonal &amp; Filled Chips</div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--filled-primary"><span class="md-08__chip-icon">★</span>Featured</div>
        <div class="md-08__chip md-08__chip--filled-teal"><span class="md-08__chip-icon">✓</span>Verified</div>
        <div class="md-08__chip md-08__chip--filled-amber"><span class="md-08__chip-icon">⚡</span>New</div>
        <div class="md-08__chip md-08__chip--filled-blue"><span class="md-08__chip-icon">💎</span>Premium</div>
      </div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--outlined-red"><span class="md-08__chip-icon">⚠</span>Deprecated</div>
        <div class="md-08__chip md-08__chip--outlined-green"><span class="md-08__chip-icon">✓</span>Stable</div>
        <div class="md-08__chip md-08__chip--outlined-orange"><span class="md-08__chip-icon">🔔</span>Beta</div>
        <div class="md-08__chip md-08__chip--outlined-purple"><span class="md-08__chip-icon">🔬</span>Experimental</div>
      </div>
    </div>

    <!-- Status Chips -->
    <div class="md-08__section">
      <div class="md-08__section-title">Status Chips</div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--status-ok">● Active</div>
        <div class="md-08__chip md-08__chip--status-warn">◔ Pending</div>
        <div class="md-08__chip md-08__chip--status-err">✕ Failed</div>
        <div class="md-08__chip md-08__chip--status-info">◑ In Progress</div>
        <div class="md-08__chip md-08__chip--status-neutral">○ Archived</div>
        <div class="md-08__chip md-08__chip--disabled md-08__chip--filled-primary">Disabled</div>
      </div>
    </div>

    <!-- Elevated -->
    <div class="md-08__section">
      <div class="md-08__section-title">Elevated Chips</div>
      <div class="md-08__chip-row">
        <div class="md-08__chip md-08__chip--elevated"><span class="md-08__chip-icon">📊</span>Dashboard</div>
        <div class="md-08__chip md-08__chip--elevated"><span class="md-08__chip-icon">📁</span>Projects</div>
        <div class="md-08__chip md-08__chip--elevated"><span class="md-08__chip-icon">🔔</span>Notifications</div>
        <div class="md-08__chip md-08__chip--elevated"><span class="md-08__chip-icon">⚙</span>Settings</div>
        <div class="md-08__chip md-08__chip--elevated"><span class="md-08__chip-icon">👤</span>Profile</div>
      </div>
    </div>

    <!-- Segmented Chip Group -->
    <div class="md-08__section">
      <div class="md-08__section-title">Segmented Choice Chip Group</div>
      <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center">
        <div class="md-08__choice-group">
          <input class="md-08__choice-in" type="radio" name="md08view" id="md08vl" checked>
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08vl">📋 List</label>
          <input class="md-08__choice-in" type="radio" name="md08view" id="md08vg">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08vg">⊞ Grid</label>
          <input class="md-08__choice-in" type="radio" name="md08view" id="md08vc">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08vc">📊 Chart</label>
        </div>
        <div class="md-08__choice-group">
          <input class="md-08__choice-in" type="radio" name="md08time" id="md08t1d" checked>
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08t1d">1D</label>
          <input class="md-08__choice-in" type="radio" name="md08time" id="md08t7d">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08t7d">7D</label>
          <input class="md-08__choice-in" type="radio" name="md08time" id="md08t1m">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08t1m">1M</label>
          <input class="md-08__choice-in" type="radio" name="md08time" id="md08t1y">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08t1y">1Y</label>
          <input class="md-08__choice-in" type="radio" name="md08time" id="md08tall">
          <label class="md-08__choice-lbl md-08__choice-lbl--seg" for="md08tall">All</label>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-08,
.md-08 *,
.md-08 *::before,
.md-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-08 ::selection {
  background: #ad1457;
  color: #fff;
}

.md-08 {
  --primary: #ad1457;
  --primary-l: #f06292;
  --secondary: #1565c0;
  --surface: #fff;
  --bg: #fce4ec;
  --ink: #212121;
  --ink2: #616161;
  --ink3: #bdbdbd;
  --divider: #f8bbd0;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-08__wrap {
  max-width: 900px;
  margin: 0 auto;
}

.md-08__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-08__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}

.md-08__section {
  background: var(--surface);
  border-radius: 12px;
  padding: 28px;
  margin-bottom: 24px;
  box-shadow: 0 1px 4px rgba(0,0,0,.08);
}

.md-08__section-title {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink2);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.md-08__section-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--divider);
}

.md-08__chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}
/* ── BASE CHIP ── */

.md-08__chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 32px;
  padding: 0 12px;
  border-radius: 8px;
  border: 1px solid #f8bbd0;
  background: var(--surface);
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 400;
  color: var(--ink);
  cursor: pointer;
  transition: background .15s,box-shadow .15s,border-color .15s;
  user-select: none;
  position: relative;
  overflow: hidden;
}

.md-08__chip:hover {
  box-shadow: 0 1px 3px rgba(0,0,0,.12);
  background: #fdf4f8;
}
/* Chip ripple */

.md-08__chip::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(173,20,87,.15);
  transform: translate(-50%,-50%);
  transition: width .3s,height .3s,opacity .3s;
  opacity: 0;
}

.md-08__chip:hover::after {
  width: 120px;
  height: 120px;
  opacity: 1;
}

.md-08__chip-icon {
  font-size: 1rem;
}

.md-08__chip-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .7rem;
  font-weight: 700;
  color: #fff;
  margin-left: -4px;
}

.md-08__chip-close {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: none;
  background: rgba(0,0,0,.1);
  font-size: .65rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: -4px;
  color: var(--ink2);
  transition: background .15s;
  padding: 0;
}

.md-08__chip-close:hover {
  background: rgba(0,0,0,.2);
}
/* ── FILTER CHIP (checkbox-hack) ── */

.md-08__filter-in {
  display: none;
}

.md-08__filter-lbl {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 32px;
  padding: 0 12px;
  border-radius: 8px;
  border: 1px solid #f8bbd0;
  background: var(--surface);
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 400;
  color: var(--ink);
  cursor: pointer;
  transition: background .15s,border-color .15s;
  user-select: none;
}

.md-08__filter-lbl::before {
  content: '';
  width: 16px;
  height: 16px;
  border: 1px solid var(--ink3);
  border-radius: 3px;
  flex-shrink: 0;
  transition: background .15s,border-color .15s;
}

.md-08__filter-in:checked + .md-08__filter-lbl {
  background: rgba(173,20,87,.1);
  border-color: var(--primary);
  color: var(--primary);
  font-weight: 500;
}

.md-08__filter-in:checked + .md-08__filter-lbl::before {
  background: var(--primary);
  border-color: var(--primary);
  content: '✓';
  color: #fff;
  font-size: .6rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* ── CHOICE CHIP (radio) ── */

.md-08__choice-in {
  display: none;
}

.md-08__choice-lbl {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 32px;
  padding: 0 16px;
  border-radius: 8px;
  border: 1px solid #f8bbd0;
  background: var(--surface);
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 400;
  color: var(--ink);
  cursor: pointer;
  transition: background .15s,border-color .15s,color .15s;
  user-select: none;
}

.md-08__choice-in:checked + .md-08__choice-lbl {
  background: rgba(173,20,87,.12);
  border-color: var(--primary);
  color: var(--primary);
  font-weight: 500;
}
/* ── INPUT CHIP ── */

.md-08__chip--input {
  background: rgba(173,20,87,.1);
  border-color: var(--primary);
  color: var(--primary);
}
/* ── SUGGESTION CHIP ── */

.md-08__chip--suggestion {
  border-style: dashed;
  color: var(--secondary);
  border-color: var(--secondary);
  background: rgba(21,101,192,.06);
}

.md-08__chip--suggestion:hover {
  background: rgba(21,101,192,.1);
}
/* ── OUTLINED CHIPS ── */

.md-08__chip--outlined-red {
  border-color: #c62828;
  color: #c62828;
}

.md-08__chip--outlined-green {
  border-color: #2e7d32;
  color: #2e7d32;
}

.md-08__chip--outlined-orange {
  border-color: #e65100;
  color: #e65100;
}

.md-08__chip--outlined-purple {
  border-color: #6a1b9a;
  color: #6a1b9a;
}
/* ── FILLED CHIPS ── */

.md-08__chip--filled-primary {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

.md-08__chip--filled-primary:hover {
  background: #880e4f;
}

.md-08__chip--filled-teal {
  background: #00897b;
  color: #fff;
  border-color: #00897b;
}

.md-08__chip--filled-amber {
  background: #ff8f00;
  color: #fff;
  border-color: #ff8f00;
}

.md-08__chip--filled-blue {
  background: #1565c0;
  color: #fff;
  border-color: #1565c0;
}
/* ── CHIP ELEVATED ── */

.md-08__chip--elevated {
  box-shadow: 0 1px 3px rgba(0,0,0,.2),0 1px 2px rgba(0,0,0,.14);
  border: none;
}

.md-08__chip--elevated:hover {
  box-shadow: 0 3px 8px rgba(0,0,0,.2);
}
/* ── DISABLED ── */

.md-08__chip--disabled {
  opacity: .38;
  cursor: not-allowed;
  pointer-events: none;
}
/* Status chips */

.md-08__chip--status-ok {
  background: #e8f5e9;
  color: #2e7d32;
  border-color: #a5d6a7;
}

.md-08__chip--status-warn {
  background: #fff8e1;
  color: #f57f17;
  border-color: #ffe082;
}

.md-08__chip--status-err {
  background: #fce4ec;
  color: #c62828;
  border-color: #f48fb1;
}

.md-08__chip--status-info {
  background: #e3f2fd;
  color: #1565c0;
  border-color: #90caf9;
}

.md-08__chip--status-neutral {
  background: #f5f5f5;
  color: #616161;
  border-color: #e0e0e0;
}
/* ── TAG INPUT DEMO ── */

.md-08__tag-input {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  padding: 8px 12px;
  border: 1px solid var(--divider);
  border-radius: 8px;
  background: #fff;
  min-height: 48px;
  cursor: text;
}

.md-08__tag-input:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 2px rgba(173,20,87,.12);
}

.md-08__tag-field {
  border: none;
  outline: none;
  font-family: 'Roboto';
  font-size: .875rem;
  color: var(--ink);
  background: transparent;
  min-width: 80px;
}
/* ── CHIP GROUP BAR ── */

.md-08__choice-group {
  display: flex;
  gap: 0;
  border: 1px solid var(--divider);
  border-radius: 8px;
  overflow: hidden;
  display: inline-flex;
}

.md-08__choice-lbl--seg {
  border-radius: 0;
  border: none;
  border-right: 1px solid var(--divider);
  height: 36px;
}

.md-08__choice-lbl--seg:last-of-type {
  border-right: none;
}

.md-08__choice-in:checked + .md-08__choice-lbl--seg {
  background: rgba(173,20,87,.12);
  color: var(--primary);
}

@media (prefers-reduced-motion: reduce) {
  .md-08 * {
    transition: none!important;
    animation: none!important;
  }
}
```
