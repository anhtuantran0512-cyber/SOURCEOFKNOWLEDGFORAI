---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-tab-navigation-with-animated-indicator/"
title: "CSS Tab Navigation with Animated Indicator"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A tab navigation component with a smooth sliding pill indicator that moves between tabs using only CSS."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Tab Navigation with Animated Indicator
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-tab-navigation-with-animated-indicator/

A tab navigation component with a smooth sliding pill indicator that moves between tabs using only CSS. The indicator position and width are driven by CSS custom properties set via sibling selectors from hidden radio inputs — no JavaScript required for the animation.
## HTML
```html
<div class="nav-08">

  <!-- Pill tabs -->
  <div class="nav-08__demo-wrap">
    <p class="nav-08__demo-label">Pill / Capsule Tabs</p>
    <input type="radio" name="nav-08-t1" id="nav-08-t1-1" checked>
    <input type="radio" name="nav-08-t1" id="nav-08-t1-2">
    <input type="radio" name="nav-08-t1" id="nav-08-t1-3">
    <input type="radio" name="nav-08-t1" id="nav-08-t1-4">
    <div class="nav-08__tabs-1">
      <label for="nav-08-t1-1">Overview</label>
      <label for="nav-08-t1-2">Analytics</label>
      <label for="nav-08-t1-3">Reports</label>
      <label for="nav-08-t1-4">Settings</label>
      <div class="nav-08__pill"></div>
    </div>
    <div class="nav-08__panels-1">
      <div class="nav-08__panel"><h3>Overview</h3><p>A summary of all key metrics across your workspace, updated in real time.</p></div>
      <div class="nav-08__panel"><h3>Analytics</h3><p>Deep-dive charts showing traffic, conversions, and user behaviour trends.</p></div>
      <div class="nav-08__panel"><h3>Reports</h3><p>Scheduled reports delivered to your inbox every Monday morning.</p></div>
      <div class="nav-08__panel"><h3>Settings</h3><p>Configure notifications, integrations, and workspace preferences here.</p></div>
    </div>
  </div>

  <!-- Underline tabs -->
  <div class="nav-08__demo-wrap">
    <p class="nav-08__demo-label">Underline Tabs</p>
    <input type="radio" name="nav-08-t2" id="nav-08-t2-1" checked>
    <input type="radio" name="nav-08-t2" id="nav-08-t2-2">
    <input type="radio" name="nav-08-t2" id="nav-08-t2-3">
    <div class="nav-08__tabs-2">
      <label for="nav-08-t2-1">Activity</label>
      <label for="nav-08-t2-2">Integrations</label>
      <label for="nav-08-t2-3">Members</label>
      <div class="nav-08__underline"></div>
    </div>
    <div class="nav-08__panels-2">
      <div class="nav-08__panel"><h3>Activity</h3><p>Latest actions taken by team members in this workspace over the past 7 days.</p></div>
      <div class="nav-08__panel"><h3>Integrations</h3><p>Connect Slack, GitHub, Jira, and 40+ other tools with one click.</p></div>
      <div class="nav-08__panel"><h3>Members</h3><p>Manage roles, permissions, and invitations for every workspace member.</p></div>
    </div>
  </div>

  <!-- Segmented control -->
  <div class="nav-08__demo-wrap">
    <p class="nav-08__demo-label">Segmented Control</p>
    <input type="radio" name="nav-08-s" id="nav-08-s1" checked>
    <input type="radio" name="nav-08-s" id="nav-08-s2">
    <input type="radio" name="nav-08-s" id="nav-08-s3">
    <div class="nav-08__seg">
      <label for="nav-08-s1">Daily</label>
      <label for="nav-08-s2">Weekly</label>
      <label for="nav-08-s3">Monthly</label>
      <div class="nav-08__seg-thumb"></div>
    </div>
  </div>

</div>
```
## CSS
```css
.nav-08,
.nav-08 *,
.nav-08 *::before,
.nav-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-08 ::selection {
  background: #e11d48;
  color: #fff;
}
/* Hide the raw radio inputs. The labels are the visible tab triggers; the
   :checked state on the inputs drives the sliding indicator via sibling
   selectors. position:absolute + opacity:0 + 1px box keeps them keyboard-
   focusable (screen-reader and tab-key users can still activate them) but
   visually invisible. display:none would break keyboard accessibility. */

.nav-08 input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 1px;
  height: 1px;
  margin: 0;
}

.nav-08 {
  --bg: #fff1f2;
  --surface: #fff;
  --border: #fecdd3;
  --text: #1a0a0d;
  --muted: #9f1239;
  --accent: #e11d48;
  --accent2: #fb7185;
  font-family: 'Manrope',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 24px;
}

.nav-08__demo-wrap {
  width: 100%;
  max-width: 720px;
}

.nav-08__demo-wrap + .nav-08__demo-wrap {
  margin-top: 56px;
}

.nav-08__demo-label {
  font-size: .75rem;
  font-weight: 700;
  color: var(--muted);
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-bottom: 14px;
}
/* === Tab style 1: pill/capsule tabs === */

.nav-08__tabs-1 {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 6px;
  /* CSS Grid with 4 equal columns so each tab gets exactly 1/4 of
       the container width regardless of label text length. The pill
       spans one column and shifts by exact multiples — no hardcoded
       pixel widths to drift from rendered label sizes. */
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 2px;
  position: relative;
}

.nav-08__tabs-1 label {
  position: relative;
  z-index: 1;
  padding: 9px 12px;
  border-radius: 11px;
  font-size: .875rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: color .2s;
  white-space: nowrap;
  user-select: none;
  text-align: center;
}

.nav-08__pill {
  position: absolute;
  top: 6px;
  bottom: 6px;
  border-radius: 11px;
  background: var(--accent);
  /* Pill width = one grid column. With 4 columns + 3 gaps of 2px
       inside a container with 6px left+right padding: track width
       = 100% - 12px - 6px = 100% - 18px, single column = that / 4. */
  width: calc((100% - 18px) / 4);
  left: 6px;
  transition: transform .28s cubic-bezier(.34,1.2,.64,1);
  z-index: 0;
}
/* The radio inputs sit OUTSIDE .nav-08__tabs-1 (siblings of the
   tabs container, not of the .nav-08__pill inside it), so the
   old plain-sibling :checked ~ .nav-08__pill selector matched nothing.
   :has() lets us style descendants based on a sibling's state. */

.nav-08__demo-wrap:has(#nav-08-t1-1:checked) .nav-08__pill {
  transform: translateX(0);
}

.nav-08__demo-wrap:has(#nav-08-t1-1:checked) label[for="nav-08-t1-1"] {
  color: #fff;
}

.nav-08__demo-wrap:has(#nav-08-t1-2:checked) .nav-08__pill {
  transform: translateX(calc(100% + 2px));
}

.nav-08__demo-wrap:has(#nav-08-t1-2:checked) label[for="nav-08-t1-2"] {
  color: #fff;
}

.nav-08__demo-wrap:has(#nav-08-t1-3:checked) .nav-08__pill {
  transform: translateX(calc(200% + 4px));
}

.nav-08__demo-wrap:has(#nav-08-t1-3:checked) label[for="nav-08-t1-3"] {
  color: #fff;
}

.nav-08__demo-wrap:has(#nav-08-t1-4:checked) .nav-08__pill {
  transform: translateX(calc(300% + 6px));
}

.nav-08__demo-wrap:has(#nav-08-t1-4:checked) label[for="nav-08-t1-4"] {
  color: #fff;
}
/* panel content */

.nav-08__panels-1 {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  margin-top: 4px;
  overflow: hidden;
}
/* show panel matching checked */

.nav-08__panel {
  display: none;
  padding: 28px;
}

#nav-08-t1-1:checked ~ .nav-08__panels-1 .nav-08__panel:nth-child(1) {
  display: block;
}

#nav-08-t1-2:checked ~ .nav-08__panels-1 .nav-08__panel:nth-child(2) {
  display: block;
}

#nav-08-t1-3:checked ~ .nav-08__panels-1 .nav-08__panel:nth-child(3) {
  display: block;
}

#nav-08-t1-4:checked ~ .nav-08__panels-1 .nav-08__panel:nth-child(4) {
  display: block;
}

.nav-08__panel h3 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 8px;
}

.nav-08__panel p {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.6;
}
/* === Tab style 2: underline tabs === */

.nav-08__tabs-2 {
  /* 3-column grid for 3 equally-sized tabs. Underline width matches
       a single column exactly. */
  display: grid;
  grid-template-columns: repeat(3,1fr);
  border-bottom: 2px solid var(--border);
  position: relative;
}

.nav-08__tabs-2 label {
  padding: 12px 20px;
  font-size: .875rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: color .2s;
  user-select: none;
  text-align: center;
}

.nav-08__tabs-2 label:hover {
  color: var(--text);
}

.nav-08__underline {
  position: absolute;
  bottom: -2px;
  height: 2px;
  background: var(--accent);
  border-radius: 2px;
  width: calc(100% / 3);
  left: 0;
  transition: transform .28s cubic-bezier(.4,0,.2,1);
}
/* Same :has() pattern — radios are outside .nav-08__tabs-2. */

.nav-08__demo-wrap:has(#nav-08-t2-1:checked) .nav-08__underline {
  transform: translateX(0);
}

.nav-08__demo-wrap:has(#nav-08-t2-1:checked) label[for="nav-08-t2-1"] {
  color: var(--text);
}

.nav-08__demo-wrap:has(#nav-08-t2-2:checked) .nav-08__underline {
  transform: translateX(100%);
}

.nav-08__demo-wrap:has(#nav-08-t2-2:checked) label[for="nav-08-t2-2"] {
  color: var(--text);
}

.nav-08__demo-wrap:has(#nav-08-t2-3:checked) .nav-08__underline {
  transform: translateX(200%);
}

.nav-08__demo-wrap:has(#nav-08-t2-3:checked) label[for="nav-08-t2-3"] {
  color: var(--text);
}

.nav-08__panels-2 {
  background: var(--surface);
  border: 1px solid var(--border);
  border-top: none;
  border-radius: 0 0 14px 14px;
}

#nav-08-t2-1:checked ~ .nav-08__panels-2 .nav-08__panel:nth-child(1) {
  display: block;
}

#nav-08-t2-2:checked ~ .nav-08__panels-2 .nav-08__panel:nth-child(2) {
  display: block;
}

#nav-08-t2-3:checked ~ .nav-08__panels-2 .nav-08__panel:nth-child(3) {
  display: block;
}
/* === Segmented control === */

.nav-08__seg {
  /* 3-column grid so each segment label is the same width as the
       thumb that highlights it. */
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 2px;
  background: var(--border);
  border-radius: 10px;
  padding: 3px;
  position: relative;
}

.nav-08__seg label {
  padding: 8px 18px;
  border-radius: 8px;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: color .2s;
  position: relative;
  z-index: 1;
  user-select: none;
  text-align: center;
}

.nav-08__seg-thumb {
  position: absolute;
  top: 3px;
  bottom: 3px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(0,0,0,.1);
  /* width = one column = (track width minus 6px padding and 4px gaps) / 3 */
  width: calc((100% - 10px) / 3);
  left: 3px;
  transition: transform .25s cubic-bezier(.34,1.2,.64,1);
  z-index: 0;
}
/* :has() — same pattern as the other two tab styles. */

.nav-08__demo-wrap:has(#nav-08-s1:checked) .nav-08__seg-thumb {
  transform: translateX(0);
}

.nav-08__demo-wrap:has(#nav-08-s1:checked) label[for="nav-08-s1"] {
  color: var(--text);
}

.nav-08__demo-wrap:has(#nav-08-s2:checked) .nav-08__seg-thumb {
  transform: translateX(calc(100% + 2px));
}

.nav-08__demo-wrap:has(#nav-08-s2:checked) label[for="nav-08-s2"] {
  color: var(--text);
}

.nav-08__demo-wrap:has(#nav-08-s3:checked) .nav-08__seg-thumb {
  transform: translateX(calc(200% + 4px));
}

.nav-08__demo-wrap:has(#nav-08-s3:checked) label[for="nav-08-s3"] {
  color: var(--text);
}

@media (prefers-reduced-motion: reduce) {
  .nav-08__pill,
    .nav-08__underline,
    .nav-08__seg-thumb {
    transition: none;
  }
}
```
