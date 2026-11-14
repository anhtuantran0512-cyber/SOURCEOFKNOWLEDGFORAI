---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-list-css/"
title: "Material Design List CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Single-line, two-line with avatars, three-line with thumbnails, icon lists with subheaders and dividers, checkbox lists, and action-button rows — complete…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design List CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-list-css/

Single-line, two-line with avatars, three-line with thumbnails, icon lists with subheaders and dividers, checkbox lists, and action-button rows — complete Material Design 3 list system.
## HTML
```html
<div class="md-12">

  <!-- Single-line list -->
  <h3>Single-Line</h3>
  <div class="list-card">
    <div class="list-item">
      <div class="item-text"><div class="item-primary">Inbox</div></div>
      <div class="item-trailing"><div class="item-badge">12</div></div>
    </div>
    <div class="list-item">
      <div class="item-text"><div class="item-primary">Starred</div></div>
      <div class="item-trailing item-chevron">›</div>
    </div>
    <div class="list-item">
      <div class="item-text"><div class="item-primary">Sent</div></div>
    </div>
    <div class="list-item">
      <div class="item-text"><div class="item-primary">Drafts</div></div>
      <div class="item-trailing"><div class="item-badge">3</div></div>
    </div>
    <div class="list-item">
      <div class="item-text"><div class="item-primary">Trash</div></div>
    </div>
  </div>

  <!-- Two-line with avatars -->
  <h3>Two-Line with Avatars</h3>
  <div class="list-card">
    <div class="list-item list-item--two">
      <div class="item-avatar">J</div>
      <div class="item-text">
        <div class="item-primary">Jamie Lee</div>
        <div class="item-secondary">Hey! Are you free this weekend?</div>
      </div>
      <div class="item-trailing item-meta">2m</div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="teal">A</div>
      <div class="item-text">
        <div class="item-primary">Alex Kim</div>
        <div class="item-secondary">The designs look great, nice work!</div>
      </div>
      <div class="item-trailing item-meta">1h</div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="orange">M</div>
      <div class="item-text">
        <div class="item-primary">Morgan Blake</div>
        <div class="item-secondary">Can we reschedule the meeting?</div>
      </div>
      <div class="item-trailing item-meta">3h</div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="purple">S</div>
      <div class="item-text">
        <div class="item-primary">Sam Rivera</div>
        <div class="item-secondary">Just sent over the report</div>
      </div>
      <div class="item-trailing item-meta">9h</div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="red">T</div>
      <div class="item-text">
        <div class="item-primary">Taylor Brooks</div>
        <div class="item-secondary">Thanks for the introduction!</div>
      </div>
      <div class="item-trailing item-meta">1d</div>
    </div>
  </div>

  <!-- Three-line with image thumbnails -->
  <h3>Three-Line with Thumbnails</h3>
  <div class="list-card">
    <div class="list-item list-item--three">
      <div class="item-image">
        <svg viewBox="0 0 24 24"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>
      </div>
      <div class="item-text">
        <div class="item-primary">Summer Retreat 2024</div>
        <div class="item-secondary">Album · 48 photos</div>
        <div class="item-tertiary">Mountain views, campfire nights, and hiking trails across the national park.</div>
      </div>
    </div>
    <div class="list-item list-item--three">
      <div class="item-image">
        <svg viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
      </div>
      <div class="item-text">
        <div class="item-primary">Late Night Mix</div>
        <div class="item-secondary">Playlist · 22 tracks</div>
        <div class="item-tertiary">Chill ambient and lo-fi beats for focused late-night work sessions.</div>
      </div>
    </div>
    <div class="list-item list-item--three">
      <div class="item-image">
        <svg viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg>
      </div>
      <div class="item-text">
        <div class="item-primary">Deep Work</div>
        <div class="item-secondary">Book · Cal Newport</div>
        <div class="item-tertiary">Rules for focused success in a distracted world — a must-read for knowledge workers.</div>
      </div>
    </div>
  </div>

  <!-- With icons + subheaders + dividers -->
  <h3>With Icons &amp; Subheaders</h3>
  <div class="list-card">
    <div class="list-subheader">General</div>
    <div class="list-item">
      <div class="item-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></div>
      <div class="item-text"><div class="item-primary">Account</div></div>
      <div class="item-trailing item-chevron">›</div>
    </div>
    <div class="list-item">
      <div class="item-icon"><svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg></div>
      <div class="item-text"><div class="item-primary">Notifications</div></div>
      <div class="item-trailing"><div class="item-switch item-switch--on"></div></div>
    </div>
    <div class="list-divider"></div>
    <div class="list-subheader">Display</div>
    <div class="list-item">
      <div class="item-icon"><svg viewBox="0 0 24 24"><path d="M20 8.69V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12 20 8.69zM12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6zm0-10c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4z"/></svg></div>
      <div class="item-text">
        <div class="item-primary">Dark Theme</div>
        <div class="item-secondary">Currently off</div>
      </div>
      <div class="item-trailing"><div class="item-switch"></div></div>
    </div>
    <div class="list-item">
      <div class="item-icon"><svg viewBox="0 0 24 24"><path d="M12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm8.94 3c-.46-4.17-3.77-7.48-7.94-7.94V1h-2v2.06C6.83 3.52 3.52 6.83 3.06 11H1v2h2.06c.46 4.17 3.77 7.48 7.94 7.94V23h2v-2.06c4.17-.46 7.48-3.77 7.94-7.94H23v-2h-2.06z"/></svg></div>
      <div class="item-text"><div class="item-primary">Language &amp; Region</div></div>
      <div class="item-trailing item-chevron">›</div>
    </div>
  </div>

  <!-- Checkbox list -->
  <h3>Checkbox List</h3>
  <div class="list-card">
    <div class="list-item list-item--two">
      <div class="item-text">
        <div class="item-primary">Design system components</div>
        <div class="item-secondary">Buttons, chips, dialogs</div>
      </div>
      <div class="item-trailing"><div class="item-check item-check--on"></div></div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-text">
        <div class="item-primary">Accessibility audit</div>
        <div class="item-secondary">WCAG 2.1 AA compliance</div>
      </div>
      <div class="item-trailing"><div class="item-check item-check--on"></div></div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-text">
        <div class="item-primary">Dark mode theming</div>
        <div class="item-secondary">Token mapping &amp; overrides</div>
      </div>
      <div class="item-trailing"><div class="item-check"></div></div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-text">
        <div class="item-primary">Documentation</div>
        <div class="item-secondary">Component usage &amp; API</div>
      </div>
      <div class="item-trailing"><div class="item-check"></div></div>
    </div>
  </div>

  <!-- Action buttons trailing -->
  <h3>With Action Buttons</h3>
  <div class="list-card">
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="green">K</div>
      <div class="item-text">
        <div class="item-primary">Kai Nakamura</div>
        <div class="item-secondary">Frontend Engineer</div>
      </div>
      <div class="item-trailing item-actions">
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></button>
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></button>
      </div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="pink">P</div>
      <div class="item-text">
        <div class="item-primary">Priya Sharma</div>
        <div class="item-secondary">Product Designer</div>
      </div>
      <div class="item-trailing item-actions">
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></button>
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></button>
      </div>
    </div>
    <div class="list-item list-item--two">
      <div class="item-avatar" data-color="red">C</div>
      <div class="item-text">
        <div class="item-primary">Carlos Vega</div>
        <div class="item-secondary">Engineering Manager</div>
      </div>
      <div class="item-trailing item-actions">
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></button>
        <button class="item-action-btn"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></button>
      </div>
    </div>
  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

.md-12 {
  --primary: #1976d2;
  --primary-light: #e3f2fd;
  --on-surface: #1c1b1f;
  --surface: #fffbfe;
  --surface-variant: #f3f3f3;
  --outline: #79747e;
  --outline-variant: #e0e0e0;
  all: unset;
  display: block;
  font-family: 'Roboto', sans-serif;
  background: #f5f5f5;
  padding: 32px 24px;
  box-sizing: border-box;
  color: var(--on-surface);
}

.md-12 *,
.md-12 *::before,
.md-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-12 h3 {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--outline);
  margin-bottom: 4px;
  margin-top: 32px;
}

.md-12 h3:first-child {
  margin-top: 0;
}
/* ── List card container ── */

.md-12 .list-card {
  background: var(--surface);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,.1);
  margin-top: 8px;
}
/* ── Subheader ── */

.md-12 .list-subheader {
  padding: 8px 16px 4px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--primary);
  background: var(--primary-light);
}
/* ── List item base ── */

.md-12 .list-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 16px;
  min-height: 48px;
  cursor: pointer;
  position: relative;
  transition: background 150ms ease;
  border-bottom: 1px solid var(--outline-variant);
}

.md-12 .list-item:last-child {
  border-bottom: none;
}

.md-12 .list-item:hover {
  background: rgba(25,118,210,.05);
}

.md-12 .list-item:active {
  background: rgba(25,118,210,.1);
}
/* Ripple */

.md-12 .list-item::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--primary);
  opacity: 0;
  border-radius: inherit;
  transition: opacity 400ms ease;
}

.md-12 .list-item:active::after {
  opacity: .06;
  transition: none;
}
/* ── Two-line item ── */

.md-12 .list-item--two {
  min-height: 64px;
}

.md-12 .list-item--three {
  min-height: 80px;
  align-items: flex-start;
  padding-top: 12px;
  padding-bottom: 12px;
}
/* ── Text block ── */

.md-12 .item-text {
  flex: 1;
  min-width: 0;
}

.md-12 .item-primary {
  font-size: 15px;
  font-weight: 400;
  color: var(--on-surface);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.md-12 .item-secondary {
  font-size: 13px;
  color: var(--outline);
  margin-top: 1px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.md-12 .item-tertiary {
  font-size: 12px;
  color: #aaa;
  margin-top: 1px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  white-space: normal;
}
/* ── Leading avatar ── */

.md-12 .item-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--primary);
  color: #fff;
  font-size: 15px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.md-12 .item-avatar--img {
  background-size: cover;
  background-position: center;
  font-size: 0;
}
/* Avatar color variants */

.md-12 .item-avatar[data-color="teal"] {
  background: #00897b;
}

.md-12 .item-avatar[data-color="orange"] {
  background: #f57c00;
}

.md-12 .item-avatar[data-color="purple"] {
  background: #7b1fa2;
}

.md-12 .item-avatar[data-color="red"] {
  background: #c62828;
}

.md-12 .item-avatar[data-color="green"] {
  background: #388e3c;
}

.md-12 .item-avatar[data-color="pink"] {
  background: #d81b60;
}
/* ── Leading icon ── */

.md-12 .item-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
  fill: var(--outline);
  display: flex;
  align-items: center;
  justify-content: center;
}

.md-12 .item-icon svg {
  width: 24px;
  height: 24px;
}
/* ── Leading image ── */

.md-12 .item-image {
  width: 56px;
  height: 56px;
  border-radius: 4px;
  background: var(--outline-variant);
  flex-shrink: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.md-12 .item-image svg {
  width: 28px;
  height: 28px;
  fill: #bbb;
}
/* ── Trailing elements ── */

.md-12 .item-trailing {
  flex-shrink: 0;
}

.md-12 .item-meta {
  font-size: 12px;
  color: var(--outline);
}

.md-12 .item-badge {
  min-width: 20px;
  height: 20px;
  background: var(--primary);
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
}

.md-12 .item-chevron {
  color: #bbb;
  font-size: 18px;
}
/* ── Checkbox / radio trailing ── */

.md-12 .item-check {
  width: 18px;
  height: 18px;
  border: 2px solid var(--outline);
  border-radius: 3px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 150ms, border-color 150ms;
}

.md-12 .item-check--on {
  background: var(--primary);
  border-color: var(--primary);
}

.md-12 .item-check--on::after {
  content: '';
  width: 10px;
  height: 6px;
  border-left: 2px solid #fff;
  border-bottom: 2px solid #fff;
  transform: rotate(-45deg) translate(1px,-1px);
  display: block;
}

.md-12 .item-radio {
  width: 18px;
  height: 18px;
  border: 2px solid var(--outline);
  border-radius: 50%;
  flex-shrink: 0;
  position: relative;
  transition: border-color 150ms;
}

.md-12 .item-radio--on {
  border-color: var(--primary);
}

.md-12 .item-radio--on::after {
  content: '';
  width: 10px;
  height: 10px;
  background: var(--primary);
  border-radius: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
}
/* ── Switch trailing ── */

.md-12 .item-switch {
  width: 36px;
  height: 20px;
  background: #bdbdbd;
  border-radius: 10px;
  position: relative;
  transition: background 200ms;
  flex-shrink: 0;
}

.md-12 .item-switch::after {
  content: '';
  width: 16px;
  height: 16px;
  background: #fff;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  transition: left 200ms, background 200ms;
  box-shadow: 0 1px 3px rgba(0,0,0,.3);
}

.md-12 .item-switch--on {
  background: var(--primary);
}

.md-12 .item-switch--on::after {
  left: 18px;
}
/* ── Divider ── */

.md-12 .list-divider {
  height: 1px;
  background: var(--outline-variant);
  margin: 0;
}

.md-12 .list-divider--inset {
  margin-left: 72px;
}
/* ── Dense list ── */

.md-12 .list-item--dense {
  min-height: 36px;
}

.md-12 .list-item--dense .item-primary {
  font-size: 13px;
}
/* ── Action list (icon-button trailing) ── */

.md-12 .item-actions {
  display: flex;
  gap: 4px;
}

.md-12 .item-action-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 150ms;
  fill: var(--outline);
}

.md-12 .item-action-btn svg {
  width: 18px;
  height: 18px;
}

.md-12 .item-action-btn:hover {
  background: rgba(0,0,0,.07);
}

@media (prefers-reduced-motion: reduce) {
  .md-12 .list-item,
    .md-12 .list-item::after,
    .md-12 .item-switch,
    .md-12 .item-switch::after,
    .md-12 .item-check,
    .md-12 .item-action-btn {
    transition: none !important;
  }
}
```
