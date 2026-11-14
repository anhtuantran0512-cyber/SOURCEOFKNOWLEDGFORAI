---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/reading-time-indicator/"
title: "Reading Time Indicator"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Three states — not started, in progress, done."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reading Time Indicator
Source: https://codefronts.com/snippets/css-badges/reading-time-indicator/

Three states — not started, in progress, done. A 2px bar at the bottom fills to 100% on hover so the user can see what completion looks like. Clean type, no decoration.
## HTML
```html
<div class="bdg-20-stage">
  <div class="bdg-20-stack">
    <div class="bdg-20-badge" style="--bdg-20-progress: 0%">
      <span class="bdg-20-icon">⌛</span>
      <div class="bdg-20-main">
        <div class="bdg-20-duration">2 min</div>
        <div class="bdg-20-label">reading time</div>
      </div>
      <div class="bdg-20-divider"></div>
      <div class="bdg-20-status bdg-20-status-unread"><span class="bdg-20-dot"></span>Not started</div>
    </div>

    <div class="bdg-20-badge" style="--bdg-20-progress: 55%">
      <span class="bdg-20-icon">⌛</span>
      <div class="bdg-20-main">
        <div class="bdg-20-duration">7 min</div>
        <div class="bdg-20-label">reading time</div>
      </div>
      <div class="bdg-20-divider"></div>
      <div class="bdg-20-status bdg-20-status-progress"><span class="bdg-20-dot"></span>In progress</div>
    </div>

    <div class="bdg-20-badge" style="--bdg-20-progress: 100%">
      <span class="bdg-20-icon">⌛</span>
      <div class="bdg-20-main">
        <div class="bdg-20-duration">14 min</div>
        <div class="bdg-20-label">reading time</div>
      </div>
      <div class="bdg-20-divider"></div>
      <div class="bdg-20-status bdg-20-status-done"><span class="bdg-20-dot"></span>Finished</div>
    </div>

    <div class="bdg-20-hint">↑ hover any badge to complete it</div>
  </div>
</div>
```
## CSS
```css
.bdg-20-stage {
  background: #fafaf7;
  padding: 60px 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-20-stack {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: flex-start;
}

.bdg-20-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px 10px 12px;
  border: 1.5px solid #1a1612;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  position: relative;
  overflow: hidden;
  cursor: default;
}

.bdg-20-badge::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  background: #1a1612;
  width: var(--bdg-20-progress, 0%);
  transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.bdg-20-badge:hover::after {
  width: 100% !important;
}

@media (prefers-reduced-motion: reduce) {
  .bdg-20-badge::after {
    transition: none;
  }
}

.bdg-20-icon {
  font-size: 16px;
  line-height: 1;
  flex-shrink: 0;
}

.bdg-20-main {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.bdg-20-duration {
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: #1a1612;
  line-height: 1;
}

.bdg-20-label {
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #4a4239;
  line-height: 1;
}

.bdg-20-divider {
  width: 1px;
  height: 28px;
  background: #cfc6b1;
  flex-shrink: 0;
}

.bdg-20-status {
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  white-space: nowrap;
  line-height: 1.2;
}

.bdg-20-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  vertical-align: middle;
  margin-right: 4px;
  margin-bottom: 1px;
}

.bdg-20-status-done {
  color: #1d8f4a;
}

.bdg-20-status-progress {
  color: #b8442d;
}

.bdg-20-status-unread {
  color: #aaa;
}

.bdg-20-hint {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #bbb;
  text-align: center;
  margin-top: 8px;
}
```
