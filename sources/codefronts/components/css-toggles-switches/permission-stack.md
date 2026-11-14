---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/permission-stack/"
title: "Permission Stack"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Grouped consent UI with mini pill toggles inside stacked bordered rows."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Permission Stack
Source: https://codefronts.com/components/css-toggles-switches/permission-stack/

Grouped consent UI with mini pill toggles inside stacked bordered rows. Each row independently grants or revokes a permission — the icon and label brighten and the pill switches to brand-green when granted. The dominant trust-first UI pattern replacing modal popups.
## HTML
```html
<div class="tgl-33">
  <label class="tgl-33__item">
    <input class="tgl-33__input" type="checkbox" checked>
    <svg class="tgl-33__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
      <circle cx="12" cy="10" r="3"/>
    </svg>
    <span class="tgl-33__info">
      <span class="tgl-33__name">Location</span>
      <span class="tgl-33__desc">While using the app</span>
    </span>
    <span class="tgl-33__pill" aria-hidden="true">
      <span class="tgl-33__thumb"></span>
    </span>
  </label>
  <label class="tgl-33__item">
    <input class="tgl-33__input" type="checkbox">
    <svg class="tgl-33__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M23 7l-7 5 7 5V7z"/>
      <rect x="1" y="5" width="15" height="14" rx="2"/>
    </svg>
    <span class="tgl-33__info">
      <span class="tgl-33__name">Camera</span>
      <span class="tgl-33__desc">Photos and video</span>
    </span>
    <span class="tgl-33__pill" aria-hidden="true">
      <span class="tgl-33__thumb"></span>
    </span>
  </label>
  <label class="tgl-33__item">
    <input class="tgl-33__input" type="checkbox" checked>
    <svg class="tgl-33__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <rect x="9" y="2" width="6" height="12" rx="3"/>
      <path d="M19 10a7 7 0 0 1-14 0"/>
      <path d="M12 18v3"/>
    </svg>
    <span class="tgl-33__info">
      <span class="tgl-33__name">Microphone</span>
      <span class="tgl-33__desc">Voice input</span>
    </span>
    <span class="tgl-33__pill" aria-hidden="true">
      <span class="tgl-33__thumb"></span>
    </span>
  </label>
  <label class="tgl-33__item">
    <input class="tgl-33__input" type="checkbox">
    <svg class="tgl-33__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
      <circle cx="9" cy="7" r="4"/>
      <path d="M22 21v-2a4 4 0 0 0-3-3.87"/>
      <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
    </svg>
    <span class="tgl-33__info">
      <span class="tgl-33__name">Contacts</span>
      <span class="tgl-33__desc">Read access only</span>
    </span>
    <span class="tgl-33__pill" aria-hidden="true">
      <span class="tgl-33__thumb"></span>
    </span>
  </label>
</div>
```
## CSS
```css
.tgl-33 {
  --tgl-33-bg: #08080f;
  --tgl-33-rim: #14141e;
  --tgl-33-wire: #1e1e2e;
  --tgl-33-fog: #3a3a52;
  --tgl-33-ash: #7a7a98;
  --tgl-33-snow: #f0f0fa;
  --tgl-33-volt: #e0ff00;
  --tgl-33-void: #04040a;
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #14141e;
  box-sizing: border-box;
}

.tgl-33__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border: 1px solid var(--tgl-33-wire);
  margin-top: -1px;
  background: var(--tgl-33-bg);
  cursor: pointer;
  transition: background 0.2s ease;
}

.tgl-33__item:first-child {
  border-radius: 12px 12px 0 0;
}

.tgl-33__item:last-child {
  border-radius: 0 0 12px 12px;
}

.tgl-33__item:hover {
  background: var(--tgl-33-rim);
}

.tgl-33__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.tgl-33__icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  color: var(--tgl-33-ash);
  opacity: 0.4;
  transition: opacity 0.3s ease, color 0.3s ease;
}

.tgl-33__info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.tgl-33__name {
  font-size: 13px;
  letter-spacing: 0.02em;
  color: var(--tgl-33-snow);
  opacity: 0.5;
  transition: opacity 0.3s ease;
}

.tgl-33__desc {
  font-size: 11px;
  color: var(--tgl-33-ash);
}
/* Mini pill toggle on the right of each row. */

.tgl-33__pill {
  position: relative;
  width: 38px;
  height: 20px;
  flex-shrink: 0;
  border-radius: 10px;
  background: var(--tgl-33-wire);
  border: 1px solid var(--tgl-33-fog);
  transition: background 0.3s ease, border-color 0.3s ease;
}

.tgl-33__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--tgl-33-fog);
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1), background 0.3s ease;
}

.tgl-33__input:checked ~ .tgl-33__icon {
  opacity: 1;
  color: var(--tgl-33-volt);
}

.tgl-33__input:checked ~ .tgl-33__info .tgl-33__name {
  opacity: 1;
}

.tgl-33__input:checked ~ .tgl-33__pill {
  background: var(--tgl-33-volt);
  border-color: var(--tgl-33-volt);
}

.tgl-33__input:checked ~ .tgl-33__pill .tgl-33__thumb {
  transform: translateX(18px);
  background: var(--tgl-33-void);
}

.tgl-33__input:focus-visible ~ .tgl-33__pill {
  outline: 2px solid var(--tgl-33-volt);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-33__item,
    .tgl-33__icon,
    .tgl-33__name,
    .tgl-33__pill,
    .tgl-33__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — independent per-row checkboxes; :checked ~ chains brighten icon, label and mini pill with an overshoot-bezier thumb. */
```
