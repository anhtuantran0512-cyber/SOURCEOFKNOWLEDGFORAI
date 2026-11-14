---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/biometric-scan/"
title: "Biometric Scan"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A scanline sweeps top-to-bottom, corner brackets glow lilac, and the icon ring lights up when activated."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Biometric Scan
Source: https://codefronts.com/components/css-toggles-switches/biometric-scan/

A scanline sweeps top-to-bottom, corner brackets glow lilac, and the icon ring lights up when activated. Identity-first UI for auth flows — the toggle becomes a scan target instead of a switch.
## HTML
```html
<label class="tgl-31">
  <input class="tgl-31__input" type="checkbox" checked>
  <span class="tgl-31__frame" aria-hidden="true">
    <span class="tgl-31-scanline"></span>
    <span class="tgl-31__corners"></span>
    <span class="tgl-31__icon-wrap">
      <span class="tgl-31__rings"></span>
      <svg class="tgl-31__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 11a2 2 0 0 0-2 2v1a8 8 0 0 1-.6 3"/>
        <path d="M14 13.1c0 .9 0 1.8-.2 2.6a13 13 0 0 1-.6 2.4"/>
        <path d="M16 11.4c.3 1 .4 2 .4 3.1a15 15 0 0 1-.3 2.7"/>
        <path d="M18 11.5c.3 2 .3 4 0 6"/>
        <path d="M8 13.5c0 1.4-.1 2.7-.5 4"/>
        <path d="M6 11c-.2.7-.3 1.4-.3 2.1"/>
        <path d="M3.5 9.5A12 12 0 0 1 12 5a12 12 0 0 1 8.5 4.5"/>
      </svg>
    </span>
    <span class="tgl-31__status">Touch ID · scanning</span>
  </span>
</label>
```
## CSS
```css
.tgl-31 {
  --tgl-31-rim: #14141e;
  --tgl-31-wire: #1e1e2e;
  --tgl-31-ash: #7a7a98;
  --tgl-31-lilac: #c084fc;
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

.tgl-31__input {
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

.tgl-31__frame {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  width: 180px;
  padding: 20px;
  border-radius: 16px;
  background: var(--tgl-31-rim);
  border: 1px solid var(--tgl-31-wire);
  overflow: hidden;
  transition: border-color 0.5s ease, background 0.5s ease;
}

.tgl-31-scanline {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--tgl-31-lilac), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.tgl-31__corners {
  position: absolute;
  inset: 12px;
  pointer-events: none;
}

.tgl-31__corners::before,
.tgl-31__corners::after {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  border-color: var(--tgl-31-wire);
  border-style: solid;
  transition: border-color 0.4s ease;
}

.tgl-31__corners::before {
  top: 0;
  left: 0;
  border-width: 2px 0 0 2px;
  border-radius: 3px 0 0 0;
}

.tgl-31__corners::after {
  bottom: 0;
  right: 0;
  border-width: 0 2px 2px 0;
  border-radius: 0 0 3px 0;
}

.tgl-31__icon-wrap {
  position: relative;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 1.5px solid var(--tgl-31-wire);
  color: var(--tgl-31-ash);
  transition: border-color 0.4s ease, color 0.4s ease;
}

.tgl-31__icon {
  width: 28px;
  height: 28px;
}
/* Two concentric outer rings that light up on scan. The :before adds
   a second ring so we get the layered radar look without extra DOM. */

.tgl-31__rings {
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  border: 1px solid transparent;
  transition: border-color 0.4s ease;
}

.tgl-31__rings::before {
  content: "";
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  border: 1px solid transparent;
  transition: border-color 0.4s ease;
}

.tgl-31__status {
  font-size: 12px;
  letter-spacing: 0.06em;
  color: var(--tgl-31-ash);
  transition: color 0.4s ease;
}

@keyframes tgl-31-scan {
  0% {
    top: 0;
  }

  100% {
    top: 100%;
  }
}

.tgl-31__input:checked ~ .tgl-31__frame {
  border-color: rgba(192,132,252,0.4);
  background: rgba(192,132,252,0.05);
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31-scanline {
  opacity: 1;
  animation: tgl-31-scan 1.8s ease-in-out infinite;
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__icon-wrap {
  border-color: var(--tgl-31-lilac);
  color: var(--tgl-31-lilac);
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__rings {
  border-color: rgba(192,132,252,0.3);
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__rings::before {
  border-color: rgba(192,132,252,0.15);
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__status {
  color: var(--tgl-31-lilac);
}

.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__corners::before,
.tgl-31__input:checked ~ .tgl-31__frame .tgl-31__corners::after {
  border-color: var(--tgl-31-lilac);
}

.tgl-31__input:focus-visible ~ .tgl-31__frame {
  outline: 2px solid var(--tgl-31-lilac);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-31__frame,
    .tgl-31__icon-wrap,
    .tgl-31__rings,
    .tgl-31__status,
    .tgl-31__corners::before,
    .tgl-31__corners::after {
    transition: none;
  }

  .tgl-31__input:checked ~ .tgl-31__frame .tgl-31-scanline {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a looping scanline keyframe, pseudo-element corner brackets and border-only radar rings all light up via :checked ~ rules. */
```
