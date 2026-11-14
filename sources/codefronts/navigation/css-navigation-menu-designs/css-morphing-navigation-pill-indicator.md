---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-morphing-navigation-pill-indicator/"
title: "CSS Morphing Navigation Pill Indicator"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "An advanced navigation component featuring a morphing pill indicator that smoothly slides and stretches between tab positions using only CSS."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Navigation Pill Indicator
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-morphing-navigation-pill-indicator/

An advanced navigation component featuring a morphing pill indicator that smoothly slides and stretches between tab positions using only CSS. The pill uses a squash-and-stretch scale animation during transition, creating a fluid, organic movement that feels alive.
## HTML
```html
<div class="nav-15">
  <input type="radio" name="nav-15" id="nav-15-1" checked>
  <input type="radio" name="nav-15" id="nav-15-2">
  <input type="radio" name="nav-15" id="nav-15-3">
  <input type="radio" name="nav-15" id="nav-15-4">
  <input type="radio" name="nav-15" id="nav-15-5">
  <div class="nav-15__wrap">
    <div class="nav-15__nav-shell">
      <div class="nav-15__pill"></div>
      <label for="nav-15-1">
        <svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
        <span>Overview</span>
      </label>
      <label for="nav-15-2">
        <svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
        <span>Analytics</span>
      </label>
      <label for="nav-15-3">
        <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        <span>Customers</span>
      </label>
      <label for="nav-15-4">
        <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/></svg>
        <span>Orders</span>
      </label>
      <label for="nav-15-5">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M5.34 18.66l-1.41 1.41M20 12h2M2 12H0M19.07 19.07l-1.41-1.41M5.34 5.34L3.93 3.93M12 20v2M12 2v2"/></svg>
        <span>Settings</span>
      </label>
    </div>
    <div class="nav-15__content">
      <!-- Panel 1: Overview -->
      <div class="nav-15__panel">
        <div class="nav-15__panel-hero">
          <div class="nav-15__panel-icon" style="background:#6366f1"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></div>
          <div class="nav-15__panel-hero-text"><h2>Overview Dashboard</h2><p>The pill morphs between positions with a spring easing, changing background colour to match each tab. Powered by CSS <code>:checked</code> + custom property offsets.</p></div>
        </div>
        <div class="nav-15__panel-body">
          <div class="nav-15__metric-row">
            <div class="nav-15__metric"><div class="nav-15__metric-val">$128k</div><div class="nav-15__metric-label">Total revenue</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">8,412</div><div class="nav-15__metric-label">Active users</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">94.2%</div><div class="nav-15__metric-label">Uptime</div></div>
          </div>
        </div>
      </div>
      <!-- Panel 2: Analytics -->
      <div class="nav-15__panel">
        <div class="nav-15__panel-hero">
          <div class="nav-15__panel-icon" style="background:#8b5cf6"><svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
          <div class="nav-15__panel-hero-text"><h2>Analytics</h2><p>Traffic and conversion metrics. Notice how the pill moves and recolours smoothly as you switch — the <code>background</code> property transitions alongside the position.</p></div>
        </div>
        <div class="nav-15__panel-body">
          <div class="nav-15__progress-row">
            <div class="nav-15__prog-item"><div class="nav-15__prog-label"><span>Organic Search</span><span>48%</span></div><div class="nav-15__prog-track"><div class="nav-15__prog-fill" style="width:48%;background:#8b5cf6"></div></div></div>
            <div class="nav-15__prog-item"><div class="nav-15__prog-label"><span>Direct</span><span>31%</span></div><div class="nav-15__prog-track"><div class="nav-15__prog-fill" style="width:31%;background:#a78bfa"></div></div></div>
            <div class="nav-15__prog-item"><div class="nav-15__prog-label"><span>Social</span><span>14%</span></div><div class="nav-15__prog-track"><div class="nav-15__prog-fill" style="width:14%;background:#c4b5fd"></div></div></div>
          </div>
        </div>
      </div>
      <!-- Panel 3: Customers -->
      <div class="nav-15__panel">
        <div class="nav-15__panel-hero">
          <div class="nav-15__panel-icon" style="background:#ec4899"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
          <div class="nav-15__panel-hero-text"><h2>Customers</h2><p>Manage your customer base. Each panel fades in with a subtle <code>translateY</code> + <code>opacity</code> keyframe animation for a snappy feel.</p></div>
        </div>
        <div class="nav-15__panel-body">
          <div class="nav-15__metric-row">
            <div class="nav-15__metric"><div class="nav-15__metric-val">3,241</div><div class="nav-15__metric-label">Total customers</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">128</div><div class="nav-15__metric-label">New this week</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">4.8★</div><div class="nav-15__metric-label">Avg rating</div></div>
          </div>
        </div>
      </div>
      <!-- Panel 4: Orders -->
      <div class="nav-15__panel">
        <div class="nav-15__panel-hero">
          <div class="nav-15__panel-icon" style="background:#f59e0b"><svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/></svg></div>
          <div class="nav-15__panel-hero-text"><h2>Orders</h2><p>Order management. The pill indicator changes its amber glow matching this tab's accent color — all driven by a <code>box-shadow</code> CSS property value.</p></div>
        </div>
        <div class="nav-15__panel-body">
          <div class="nav-15__metric-row">
            <div class="nav-15__metric"><div class="nav-15__metric-val">1,093</div><div class="nav-15__metric-label">Total orders</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">47</div><div class="nav-15__metric-label">Pending</div></div>
            <div class="nav-15__metric"><div class="nav-15__metric-val">$68</div><div class="nav-15__metric-label">Avg order value</div></div>
          </div>
        </div>
      </div>
      <!-- Panel 5: Settings -->
      <div class="nav-15__panel">
        <div class="nav-15__panel-hero">
          <div class="nav-15__panel-icon" style="background:#10b981"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M5.34 18.66l-1.41 1.41M20 12h2M2 12H0"/></svg></div>
          <div class="nav-15__panel-hero-text"><h2>Settings</h2><p>Configure your workspace. Zero JavaScript — the morphing indicator is driven entirely by the <code>:checked</code> pseudo-class and precise <code>left</code> + <code>width</code> calculations in CSS.</p></div>
        </div>
        <div class="nav-15__panel-body">
          <div class="nav-15__progress-row">
            <div class="nav-15__prog-item"><div class="nav-15__prog-label"><span>Storage used</span><span>62%</span></div><div class="nav-15__prog-track"><div class="nav-15__prog-fill" style="width:62%;background:#10b981"></div></div></div>
            <div class="nav-15__prog-item"><div class="nav-15__prog-label"><span>API quota</span><span>28%</span></div><div class="nav-15__prog-track"><div class="nav-15__prog-fill" style="width:28%;background:#34d399"></div></div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.nav-15,
.nav-15 *,
.nav-15 *::before,
.nav-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-15 ::selection {
  background: #6366f1;
  color: #fff;
}

.nav-15 {
  --bg: #030712;
  --surface: #0d1117;
  --surface2: #161b26;
  --border: rgba(255,255,255,.07);
  --text: #f9fafb;
  --muted: #6b7280;
  --p1: #6366f1;
  --p2: #8b5cf6;
  --p3: #ec4899;
  --p4: #f59e0b;
  --p5: #10b981;
  font-family: 'Inter',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
}
/* radio state */

.nav-15 input[type=radio] {
  display: none;
}
/* top centered floating pill nav */

.nav-15__wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 24px;
}

.nav-15__nav-shell {
  background: rgba(255,255,255,.04);
  border: 1px solid var(--border);
  border-radius: 100px;
  padding: 5px;
  /* 5-column grid so each tab gets 1/5 of the shell width regardless
       of label-text length. The pill spans one column exactly. */
  display: grid;
  grid-template-columns: repeat(5,1fr);
  position: relative;
  gap: 2px;
}
/* sliding pill — width = one column, offset = N columns + gap */

.nav-15__pill {
  position: absolute;
  top: 5px;
  bottom: 5px;
  border-radius: 100px;
  transform-origin: center;
  /* Width = one column = (shell minus 10px padding minus 8px of gaps) / 5 */
  width: calc((100% - 18px) / 5);
  left: 5px;
  transition: transform .45s cubic-bezier(.34,1.4,.64,1),background .3s ease;
  z-index: 0;
}
/* Squash-stretch morph — separated from the translateX motion so they
   compose cleanly. Earlier attempt had the morph keyframe override
   the pill's static translateX, causing the pill to "teleport back
   to position 1" for the duration of the animation before snapping
   to the correct tab.

   The clean fix: keep transform on the OUTER pill for translateX
   (driven by transition for smooth slide), and run the scale morph
   on an INNER ::before pseudo-element that fills the pill. The two
   transforms compose without conflict.

   Each :checked rule assigns a unique animation name (1..5) to force
   the keyframe to re-trigger on every tab change. */

.nav-15__pill::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: inherit;
  /* Inherit the pill's background so the morph looks like the pill
       itself is squashing/stretching. The outer pill keeps box-shadow
       so the glow doesn't squish along with the morph. */
}

@keyframes nav-15-morph-1 {
  0%,
    100% {
    transform: scaleY(1) scaleX(1);
  }

  50% {
    transform: scaleY(.7) scaleX(1.1);
  }
}

@keyframes nav-15-morph-2 {
  0%,
    100% {
    transform: scaleY(1) scaleX(1);
  }

  50% {
    transform: scaleY(.7) scaleX(1.1);
  }
}

@keyframes nav-15-morph-3 {
  0%,
    100% {
    transform: scaleY(1) scaleX(1);
  }

  50% {
    transform: scaleY(.7) scaleX(1.1);
  }
}

@keyframes nav-15-morph-4 {
  0%,
    100% {
    transform: scaleY(1) scaleX(1);
  }

  50% {
    transform: scaleY(.7) scaleX(1.1);
  }
}

@keyframes nav-15-morph-5 {
  0%,
    100% {
    transform: scaleY(1) scaleX(1);
  }

  50% {
    transform: scaleY(.7) scaleX(1.1);
  }
}
/* Pill positioning — translateX on the OUTER pill (smooth slide
   via transition). Morph animation runs on the ::before pseudo
   inside the pill (composes without fighting the slide). */

#nav-15-1:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill {
  transform: translateX(0);
  background: var(--p1);
  box-shadow: 0 0 20px rgba(99,102,241,.4);
}

#nav-15-1:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill::before {
  animation: nav-15-morph-1 .45s ease-out;
}

#nav-15-2:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill {
  transform: translateX(calc(100% + 2px));
  background: var(--p2);
  box-shadow: 0 0 20px rgba(139,92,246,.4);
}

#nav-15-2:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill::before {
  animation: nav-15-morph-2 .45s ease-out;
}

#nav-15-3:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill {
  transform: translateX(calc(200% + 4px));
  background: var(--p3);
  box-shadow: 0 0 20px rgba(236,72,153,.4);
}

#nav-15-3:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill::before {
  animation: nav-15-morph-3 .45s ease-out;
}

#nav-15-4:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill {
  transform: translateX(calc(300% + 6px));
  background: var(--p4);
  box-shadow: 0 0 20px rgba(245,158,11,.35);
}

#nav-15-4:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill::before {
  animation: nav-15-morph-4 .45s ease-out;
}

#nav-15-5:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill {
  transform: translateX(calc(400% + 8px));
  background: var(--p5);
  box-shadow: 0 0 20px rgba(16,185,129,.35);
}

#nav-15-5:checked ~ .nav-15__wrap .nav-15__nav-shell .nav-15__pill::before {
  animation: nav-15-morph-5 .45s ease-out;
}
/* labels */

.nav-15__nav-shell label {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 9px 16px;
  border-radius: 100px;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
  transition: color .25s;
  white-space: nowrap;
}

.nav-15__nav-shell label svg {
  width: 14px;
  height: 14px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  flex-shrink: 0;
}

#nav-15-1:checked ~ .nav-15__wrap .nav-15__nav-shell label[for=nav-15-1] {
  color: #fff;
}

#nav-15-2:checked ~ .nav-15__wrap .nav-15__nav-shell label[for=nav-15-2] {
  color: #fff;
}

#nav-15-3:checked ~ .nav-15__wrap .nav-15__nav-shell label[for=nav-15-3] {
  color: #fff;
}

#nav-15-4:checked ~ .nav-15__wrap .nav-15__nav-shell label[for=nav-15-4] {
  color: #fff;
}

#nav-15-5:checked ~ .nav-15__wrap .nav-15__nav-shell label[for=nav-15-5] {
  color: #fff;
}
/* content area */

.nav-15__content {
  width: 100%;
  max-width: 780px;
  margin-top: 40px;
}

.nav-15__panel {
  display: none;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  animation: nav-15-fade .25s ease forwards;
}

@keyframes nav-15-fade {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

#nav-15-1:checked ~ .nav-15__wrap .nav-15__content .nav-15__panel:nth-child(1) {
  display: block;
}

#nav-15-2:checked ~ .nav-15__wrap .nav-15__content .nav-15__panel:nth-child(2) {
  display: block;
}

#nav-15-3:checked ~ .nav-15__wrap .nav-15__content .nav-15__panel:nth-child(3) {
  display: block;
}

#nav-15-4:checked ~ .nav-15__wrap .nav-15__content .nav-15__panel:nth-child(4) {
  display: block;
}

#nav-15-5:checked ~ .nav-15__wrap .nav-15__content .nav-15__panel:nth-child(5) {
  display: block;
}

.nav-15__panel-hero {
  padding: 36px 36px 0;
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.nav-15__panel-icon {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  flex-shrink: 0;
  display: grid;
  place-items: center;
}

.nav-15__panel-icon svg {
  width: 24px;
  height: 24px;
  stroke: #fff;
  fill: none;
  stroke-width: 1.75;
}

.nav-15__panel-hero-text h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.02em;
  margin-bottom: 6px;
}

.nav-15__panel-hero-text p {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.65;
}

.nav-15__panel-body {
  padding: 28px 36px 36px;
}

.nav-15__metric-row {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
  margin-bottom: 20px;
}

.nav-15__metric {
  background: var(--surface2);
  border-radius: 12px;
  padding: 16px 18px;
}

.nav-15__metric-val {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.03em;
}

.nav-15__metric-label {
  font-size: .75rem;
  color: var(--muted);
  margin-top: 3px;
}

.nav-15__progress-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nav-15__prog-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.nav-15__prog-label {
  display: flex;
  justify-content: space-between;
  font-size: .8rem;
  color: var(--muted);
  font-weight: 500;
}

.nav-15__prog-track {
  height: 6px;
  background: rgba(255,255,255,.06);
  border-radius: 3px;
  overflow: hidden;
}

.nav-15__prog-fill {
  height: 100%;
  border-radius: 3px;
}

@media (max-width: 600px) {
  .nav-15__metric-row {
    grid-template-columns: 1fr 1fr;
  }

  .nav-15__nav-shell label span {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-15__pill {
    transition: none;
  }

  .nav-15__panel {
    animation: none;
  }
}
```
