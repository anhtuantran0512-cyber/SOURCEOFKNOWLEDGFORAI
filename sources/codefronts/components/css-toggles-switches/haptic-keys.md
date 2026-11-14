---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/haptic-keys/"
title: "Haptic Keys"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Chunky square key with a 3D press-depth shadow and a glowing accent ring on activate."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Haptic Keys
Source: https://codefronts.com/components/css-toggles-switches/haptic-keys/

Chunky square key with a 3D press-depth shadow and a glowing accent ring on activate. Pressing literally sinks the button 3px while the hard bottom shadow collapses — pure tactile button metaphor for tactile UI trends.
## HTML
```html
<label class="tgl-28">
  <input class="tgl-28__input" type="checkbox" checked>
  <span class="tgl-28__btn" aria-hidden="true">
    <span class="tgl-28__ring"></span>
    <svg class="tgl-28__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/>
      <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>
    </svg>
  </span>
  <span class="tgl-28__label">Notify</span>
</label>
```
## CSS
```css
.tgl-28 {
  --tgl-28-rim: #14141e;
  --tgl-28-wire: #1e1e2e;
  --tgl-28-edge: #020205;
  --tgl-28-accent: #39d353;
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
  color: #1a1a2e;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #f2f2f7;
  box-sizing: border-box;
}

.tgl-28__input {
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

.tgl-28__btn {
  position: relative;
  display: inline-flex;
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: var(--tgl-28-rim);
  border: 1px solid var(--tgl-28-wire);
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 0 var(--tgl-28-edge), 0 8px 16px rgba(0,0,0,0.5);
  transition: box-shadow 0.1s ease, transform 0.1s ease, background 0.3s ease, border-color 0.3s ease;
}

.tgl-28__icon {
  width: 22px;
  height: 22px;
  color: #3a3a52;
  filter: grayscale(1) brightness(0.6);
  position: relative;
  z-index: 1;
  transition: color 0.3s ease, transform 0.3s ease, filter 0.3s ease;
}

.tgl-28__ring {
  position: absolute;
  inset: -4px;
  border-radius: 20px;
  border: 2px solid transparent;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}
/* Press effect — clicking the label sinks the button.
   Using the label's :active so the whole hit-area drives the press. */

.tgl-28:active .tgl-28__btn {
  box-shadow: 0 2px 0 var(--tgl-28-edge), 0 3px 8px rgba(0,0,0,0.5);
  transform: translateY(3px);
}

.tgl-28__input:checked ~ .tgl-28__btn {
  background: #0f1a0f;
  border-color: rgba(57,211,83,0.3);
  box-shadow: 0 6px 0 var(--tgl-28-edge), 0 8px 16px rgba(0,0,0,0.5), 0 0 20px rgba(57,211,83,0.15);
}

.tgl-28__input:checked ~ .tgl-28__btn .tgl-28__icon {
  color: var(--tgl-28-accent);
  filter: none;
  transform: scale(1.15);
}

.tgl-28__input:checked ~ .tgl-28__btn .tgl-28__ring {
  border-color: var(--tgl-28-accent);
  box-shadow: 0 0 12px rgba(57,211,83,0.3);
}

.tgl-28__input:focus-visible ~ .tgl-28__btn {
  outline: 2px solid var(--tgl-28-accent);
  outline-offset: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-28__btn,
    .tgl-28__icon,
    .tgl-28__ring {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hard bottom box-shadow stem gives key depth, :active sinks the cap 3px, and :checked backlights icon + accent ring. */
```
