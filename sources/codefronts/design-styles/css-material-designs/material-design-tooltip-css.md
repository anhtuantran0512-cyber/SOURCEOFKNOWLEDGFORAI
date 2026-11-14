---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-tooltip-css/"
title: "Material Design Tooltip CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Plain and rich tooltips in four directions, linear progress (determinate and indeterminate), circular progress, notification badges, and page dot navigation…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Tooltip CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-tooltip-css/

Plain and rich tooltips in four directions, linear progress (determinate and indeterminate), circular progress, notification badges, and page dot navigation — all pure CSS.
## HTML
```html
<div class="md-10">
  <div class="md-10__wrap">
    <div class="md-10__page-title">Material Design Tooltips &amp; Indicators</div>
    <div class="md-10__page-sub">Tooltips (all 4 positions + rich), progress bars, circular indicators and badge components — pure CSS</div>

    <!-- Tooltips -->
    <div class="md-10__section">
      <div class="md-10__section-title">Tooltips — Hover to See</div>
      <div style="display:flex;flex-wrap:wrap;gap:24px;align-items:center;justify-content:center;padding:24px 0">
        <div class="md-10__tooltip-wrap">
          <button class="md-10__icon-btn">✏</button>
          <div class="md-10__tooltip md-10__tooltip--top">Edit item</div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__icon-btn" style="background:#c62828">🗑</button>
          <div class="md-10__tooltip md-10__tooltip--bottom">Delete permanently</div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__icon-btn" style="background:#7b1fa2">↗</button>
          <div class="md-10__tooltip md-10__tooltip--right">Share with team</div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__icon-btn" style="background:#1565c0">⚙</button>
          <div class="md-10__tooltip md-10__tooltip--left">Open settings</div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__text-btn">Format options</button>
          <div class="md-10__tooltip md-10__tooltip--top">Bold, italic, underline, strikethrough</div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__badge-btn">Keyboard shortcuts</button>
          <div class="md-10__tooltip md-10__tooltip--top" style="max-width:220px;white-space:normal">Press ⌘K to open the command palette, ⌘S to save, ⌘Z to undo.</div>
        </div>
      </div>
    </div>

    <!-- Rich Tooltip -->
    <div class="md-10__section">
      <div class="md-10__section-title">Rich Tooltip (Hover)</div>
      <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:center;justify-content:center;padding:24px 0">
        <div class="md-10__tooltip-wrap">
          <button class="md-10__icon-btn" style="background:#ff8f00">★</button>
          <div class="md-10__tooltip md-10__tooltip--top md-10__tooltip--rich" style="bottom:calc(100% + 12px);min-width:240px">
            <div class="md-10__tt-title">Add to favourites</div>
            <div class="md-10__tt-body">Save this item to your favourites list to access it quickly from the sidebar.</div>
            <div class="md-10__tt-actions">
              <button class="md-10__tt-btn">Learn more</button>
              <button class="md-10__tt-btn" style="margin-left:auto">Got it</button>
            </div>
          </div>
        </div>
        <div class="md-10__tooltip-wrap">
          <button class="md-10__text-btn">Privacy settings ℹ</button>
          <div class="md-10__tooltip md-10__tooltip--right md-10__tooltip--rich" style="left:calc(100% + 12px)">
            <div class="md-10__tt-title">Privacy controls</div>
            <div class="md-10__tt-body">Control who can see your profile and how your data is shared. Settings apply immediately.</div>
            <div class="md-10__tt-actions">
              <button class="md-10__tt-btn">Open settings</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Linear Progress -->
    <div class="md-10__section">
      <div class="md-10__section-title">Linear Progress Indicators</div>
      <div class="md-10__progress-row">
        <div>
          <div class="md-10__progress-label"><span>Storage used</span><span>72%</span></div>
          <div class="md-10__progress-track"><div class="md-10__progress-fill" style="width:72%"></div></div>
        </div>
        <div>
          <div class="md-10__progress-label"><span>Upload complete</span><span>45%</span></div>
          <div class="md-10__progress-track" style="height:8px;border-radius:4px"><div class="md-10__progress-fill" style="width:45%;background:#1565c0"></div></div>
        </div>
        <div>
          <div class="md-10__progress-label"><span>Confidence score</span><span>94%</span></div>
          <div class="md-10__progress-track" style="height:6px;background:#c8e6c9"><div class="md-10__progress-fill" style="width:94%;background:#2e7d32"></div></div>
        </div>
        <div>
          <div class="md-10__progress-label"><span>Loading data…</span><span>Indeterminate</span></div>
          <div class="md-10__progress-track" style="overflow:hidden;position:relative"><div class="md-10__progress-fill md-10__progress-fill--indeterminate" style="position:absolute"></div></div>
        </div>
      </div>
    </div>

    <!-- Circular Progress -->
    <div class="md-10__section">
      <div class="md-10__section-title">Circular Progress Indicators</div>
      <div class="md-10__circular-row">
        <div style="text-align:center">
          <div class="md-10__circular">
            <svg viewBox="0 0 64 64"><circle class="md-10__circular-track" cx="32" cy="32" r="28"/><circle class="md-10__circular-fill" cx="32" cy="32" r="28" stroke-dasharray="131" stroke-dashoffset="33" style="stroke:var(--primary)"/></svg>
            <div class="md-10__circular-val">75%</div>
          </div>
          <div style="font-size:.75rem;color:var(--ink2);margin-top:6px">Progress</div>
        </div>
        <div style="text-align:center">
          <div class="md-10__circular">
            <svg viewBox="0 0 64 64"><circle class="md-10__circular-track" cx="32" cy="32" r="28"/><circle class="md-10__circular-fill" cx="32" cy="32" r="28" stroke-dasharray="131" stroke-dashoffset="72" style="stroke:#2e7d32"/></svg>
            <div class="md-10__circular-val" style="color:#2e7d32">45%</div>
          </div>
          <div style="font-size:.75rem;color:var(--ink2);margin-top:6px">Budget</div>
        </div>
        <div style="text-align:center">
          <div class="md-10__circular">
            <svg viewBox="0 0 64 64"><circle class="md-10__circular-track" cx="32" cy="32" r="28"/><circle class="md-10__circular-fill" cx="32" cy="32" r="28" stroke-dasharray="131" stroke-dashoffset="13" style="stroke:#e65100"/></svg>
            <div class="md-10__circular-val" style="color:#e65100">90%</div>
          </div>
          <div style="font-size:.75rem;color:var(--ink2);margin-top:6px">Capacity</div>
        </div>
        <div style="text-align:center">
          <div class="md-10__circular md-10__circular--spin">
            <svg viewBox="0 0 64 64"><circle class="md-10__circular-track" cx="32" cy="32" r="28"/><circle class="md-10__circular-fill" cx="32" cy="32" r="28" style="stroke:var(--primary)"/></svg>
          </div>
          <div style="font-size:.75rem;color:var(--ink2);margin-top:6px">Loading…</div>
        </div>
        <div style="text-align:center">
          <div class="md-10__circular md-10__circular--spin">
            <svg viewBox="0 0 64 64"><circle class="md-10__circular-track" cx="32" cy="32" r="28" style="stroke:#fce4ec"/><circle class="md-10__circular-fill" cx="32" cy="32" r="28" style="stroke:#e91e63"/></svg>
          </div>
          <div style="font-size:.75rem;color:var(--ink2);margin-top:6px">Syncing</div>
        </div>
      </div>
    </div>

    <!-- Badges -->
    <div class="md-10__section">
      <div class="md-10__section-title">Badges</div>
      <div class="md-10__badge-demo-row">
        <div class="md-10__badge-wrap">
          <button class="md-10__icon-btn" style="background:#455a64">🔔</button>
          <div class="md-10__badge">3</div>
        </div>
        <div class="md-10__badge-wrap">
          <button class="md-10__icon-btn" style="background:#455a64">📧</button>
          <div class="md-10__badge">99+</div>
        </div>
        <div class="md-10__badge-wrap">
          <button class="md-10__icon-btn" style="background:#455a64">⚙</button>
          <div class="md-10__badge md-10__badge--dot"></div>
        </div>
        <div class="md-10__badge-wrap">
          <button class="md-10__text-btn">Inbox</button>
          <div class="md-10__badge md-10__badge--large" style="top:-8px;right:-8px">New</div>
        </div>
        <div class="md-10__badge-wrap">
          <button class="md-10__text-btn">Messages</button>
          <div class="md-10__badge" style="top:-6px;right:-6px;background:#2e7d32">12</div>
        </div>
      </div>

      <!-- Page indicator dots -->
      <div style="margin-top:28px">
        <div style="font-size:.78rem;color:var(--ink2);margin-bottom:12px">Page Indicator Dots</div>
        <div class="md-10__dots-row">
          <div class="md-10__dot"></div>
          <div class="md-10__dot md-10__dot--active"></div>
          <div class="md-10__dot"></div>
          <div class="md-10__dot"></div>
          <div class="md-10__dot"></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-10,
.md-10 *,
.md-10 *::before,
.md-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-10 ::selection {
  background: #00695c;
  color: #fff;
}

.md-10 {
  --primary: #00695c;
  --primary-l: #4db6ac;
  --secondary: #f57c00;
  --surface: #fff;
  --bg: #e0f2f1;
  --ink: #212121;
  --ink2: #546e7a;
  --ink3: #90a4ae;
  --divider: #b2dfdb;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-10__wrap {
  max-width: 900px;
  margin: 0 auto;
}

.md-10__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-10__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}

.md-10__section {
  background: var(--surface);
  border-radius: 12px;
  padding: 32px;
  margin-bottom: 24px;
  box-shadow: 0 1px 4px rgba(0,0,0,.1);
}

.md-10__section-title {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink2);
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.md-10__section-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--divider);
}
/* ── TOOLTIP ── */

.md-10__tooltip-wrap {
  position: relative;
  display: inline-flex;
}

.md-10__tooltip {
  position: absolute;
  z-index: 10;
  background: #212121;
  color: #fff;
  font-size: .75rem;
  font-weight: 400;
  line-height: 1.4;
  padding: 6px 10px;
  border-radius: 4px;
  white-space: nowrap;
  max-width: 240px;
  white-space: normal;
  pointer-events: none;
  opacity: 0;
  transition: opacity .15s .1s,transform .15s .1s;
}
/* Arrow */

.md-10__tooltip::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
}
/* Top tooltip */

.md-10__tooltip--top {
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
}

.md-10__tooltip--top::before {
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: #212121;
}

.md-10__tooltip-wrap:hover .md-10__tooltip--top {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
/* Bottom tooltip */

.md-10__tooltip--bottom {
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(-4px);
}

.md-10__tooltip--bottom::before {
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-bottom-color: #212121;
}

.md-10__tooltip-wrap:hover .md-10__tooltip--bottom {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
/* Left tooltip */

.md-10__tooltip--left {
  right: calc(100% + 8px);
  top: 50%;
  transform: translateY(-50%) translateX(4px);
}

.md-10__tooltip--left::before {
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  border: 5px solid transparent;
  border-left-color: #212121;
}

.md-10__tooltip-wrap:hover .md-10__tooltip--left {
  opacity: 1;
  transform: translateY(-50%) translateX(0);
}
/* Right tooltip */

.md-10__tooltip--right {
  left: calc(100% + 8px);
  top: 50%;
  transform: translateY(-50%) translateX(-4px);
}

.md-10__tooltip--right::before {
  right: 100%;
  top: 50%;
  transform: translateY(-50%);
  border: 5px solid transparent;
  border-right-color: #212121;
}

.md-10__tooltip-wrap:hover .md-10__tooltip--right {
  opacity: 1;
  transform: translateY(-50%) translateX(0);
}
/* Rich tooltip */

.md-10__tooltip--rich {
  background: var(--surface);
  color: var(--ink);
  max-width: 280px;
  padding: 12px 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,.2);
  border-radius: 8px;
  white-space: normal;
}

.md-10__tooltip--rich::before {
  display: none;
}

.md-10__tooltip--rich .md-10__tt-title {
  font-size: .875rem;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--ink);
}

.md-10__tooltip--rich .md-10__tt-body {
  font-size: .8rem;
  line-height: 1.5;
  color: var(--ink2);
}

.md-10__tooltip--rich .md-10__tt-actions {
  display: flex;
  gap: 8px;
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid var(--divider);
}

.md-10__tooltip--rich .md-10__tt-btn {
  background: none;
  border: none;
  color: var(--primary);
  font-family: 'Roboto';
  font-size: .78rem;
  font-weight: 500;
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: .05em;
  padding: 0;
}
/* ── TRIGGER BUTTONS ── */

.md-10__icon-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  background: var(--primary);
  color: #fff;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(0,0,0,.2);
  transition: box-shadow .2s;
}

.md-10__icon-btn:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,.25);
}

.md-10__text-btn {
  height: 36px;
  padding: 0 16px;
  border: 1px solid var(--divider);
  border-radius: 4px;
  background: var(--surface);
  font-family: 'Roboto';
  font-size: .875rem;
  cursor: pointer;
  color: var(--ink);
}

.md-10__badge-btn {
  background: var(--primary);
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px 16px;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  cursor: pointer;
}
/* ── PROGRESS INDICATORS ── */

.md-10__progress-row {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.md-10__progress-label {
  font-size: .8rem;
  color: var(--ink2);
  margin-bottom: 6px;
  display: flex;
  justify-content: space-between;
}

.md-10__progress-track {
  height: 4px;
  background: #b2dfdb;
  border-radius: 2px;
  overflow: hidden;
  position: relative;
}

.md-10__progress-fill {
  height: 100%;
  background: var(--primary);
  border-radius: 2px;
  position: relative;
}
/* Indeterminate bar */

.md-10__progress-fill--indeterminate {
  width: 30%;
  animation: md10-indeterminate 2s linear infinite;
}

@keyframes md10-indeterminate {
  0% {
    left: -30%;
    width: 30%;
  }

  60% {
    left: 60%;
    width: 50%;
  }

  100% {
    left: 110%;
    width: 30%;
  }
}
/* Circular progress */

.md-10__circular-row {
  display: flex;
  gap: 28px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.md-10__circular {
  position: relative;
  width: 64px;
  height: 64px;
  flex-shrink: 0;
}

.md-10__circular svg {
  transform: rotate(-90deg);
  width: 64px;
  height: 64px;
}

.md-10__circular-track {
  fill: none;
  stroke: #b2dfdb;
  stroke-width: 4;
}

.md-10__circular-fill {
  fill: none;
  stroke: var(--primary);
  stroke-width: 4;
  stroke-linecap: round;
  transition: stroke-dashoffset .5s ease;
}

.md-10__circular-val {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .8rem;
  font-weight: 700;
  color: var(--primary);
}
/* Indeterminate circle */

.md-10__circular--spin .md-10__circular-fill {
  stroke-dasharray: 160 200;
  animation: md10-cspin 1.4s linear infinite;
}

@keyframes md10-cspin {
  0% {
    stroke-dashoffset: 0;
    transform: none;
  }

  100% {
    stroke-dashoffset: -320;
    transform: none;
  }
}

.md-10__circular--spin svg {
  animation: md10-svg-spin 1.4s linear infinite;
}

@keyframes md10-svg-spin {
  0% {
    transform: rotate(-90deg);
  }

  100% {
    transform: rotate(270deg);
  }
}
/* ── BADGE ── */

.md-10__badge-wrap {
  position: relative;
  display: inline-flex;
}

.md-10__badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: var(--secondary);
  color: #fff;
  font-size: .65rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 10px;
  border: 2px solid var(--surface);
  line-height: 1.4;
  white-space: nowrap;
  min-width: 20px;
  text-align: center;
}

.md-10__badge--dot {
  width: 10px;
  height: 10px;
  min-width: 0;
  padding: 0;
  top: -2px;
  right: -2px;
}

.md-10__badge--large {
  font-size: .75rem;
  padding: 3px 8px;
  border-radius: 12px;
}

.md-10__badge-demo-row {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  align-items: center;
}
/* ── PROGRESS OVERFLOW DOTS ── */

.md-10__dots-row {
  display: flex;
  gap: 4px;
  align-items: center;
  justify-content: center;
  padding: 8px 0;
}

.md-10__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--divider);
  transition: all .2s;
}

.md-10__dot--active {
  background: var(--primary);
  width: 24px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .md-10 * {
    animation: none!important;
    transition: none!important;
  }
}
```
