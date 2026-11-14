---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-timeline-layout/"
title: "CSS Flexbox Timeline Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A vertical event timeline where each entry is a flex row — a narrow connector column with a dot and line, and an expanding content card — creating a clean…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Timeline Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-timeline-layout/

A vertical event timeline where each entry is a flex row — a narrow connector column with a dot and line, and an expanding content card — creating a clean left-rail chronology.
## HTML
```html
<div class="fl-11">
  <div class="fl-11__header">
    <div class="fl-11__eyebrow">Flexbox Pattern</div>
    <h2 class="fl-11__title">CSS Flexbox Timeline Layout</h2>
    <p class="fl-11__sub">Each row is a flex container: connector column + content area</p>
  </div>

  <div class="fl-11__timeline">

    <div class="fl-11__event">
      <div class="fl-11__connector">
        <div class="fl-11__dot" style="background:#0284c7">🚀</div>
        <div class="fl-11__line"></div>
      </div>
      <div class="fl-11__content">
        <div class="fl-11__event-meta">
          <div class="fl-11__date">Jan 2024</div>
          <div class="fl-11__event-tag" style="background:#dbeafe;color:#1d4ed8">Launch</div>
        </div>
        <div class="fl-11__event-title">Project Kickoff</div>
        <div class="fl-11__event-desc">Initial CSS Flexbox design system established. Team aligned on layout patterns and naming conventions for all 15 demo types.</div>
        <div class="fl-11__event-card">
          <div class="fl-11__card-row">
            <div class="fl-11__card-icon" style="background:#dbeafe">👥</div>
            <div>
              <div class="fl-11__card-text">Team onboarded</div>
              <div class="fl-11__card-sub">8 contributors</div>
            </div>
            <div class="fl-11__card-value">8 devs</div>
          </div>
        </div>
      </div>
    </div>

    <div class="fl-11__event">
      <div class="fl-11__connector">
        <div class="fl-11__dot" style="background:#d97706">⚡</div>
        <div class="fl-11__line"></div>
      </div>
      <div class="fl-11__content">
        <div class="fl-11__event-meta">
          <div class="fl-11__date">Mar 2024</div>
          <div class="fl-11__event-tag" style="background:#fef3c7;color:#b45309">Milestone</div>
        </div>
        <div class="fl-11__event-title">v1.0 Layout System Released</div>
        <div class="fl-11__event-desc">First stable release of the flexbox layout library. Included holy grail, sidebar dashboard, and card grid patterns.</div>
        <div class="fl-11__event-card">
          <div class="fl-11__card-row">
            <div class="fl-11__card-icon" style="background:#fef3c7">📦</div>
            <div>
              <div class="fl-11__card-text">Components shipped</div>
              <div class="fl-11__card-sub">npm install flexlayout</div>
            </div>
            <div class="fl-11__card-value" style="color:#d97706">24 patterns</div>
          </div>
        </div>
      </div>
    </div>

    <div class="fl-11__today">
      <div class="fl-11__today-line"></div>
      <div class="fl-11__today-label">Today</div>
      <div class="fl-11__today-line"></div>
    </div>

    <div class="fl-11__event">
      <div class="fl-11__connector">
        <div class="fl-11__dot" style="background:#059669">✓</div>
        <div class="fl-11__line"></div>
      </div>
      <div class="fl-11__content">
        <div class="fl-11__event-meta">
          <div class="fl-11__date">Jun 2025</div>
          <div class="fl-11__event-tag" style="background:#d1fae5;color:#065f46">Current</div>
        </div>
        <div class="fl-11__event-title">Flexbox Gallery Collection</div>
        <div class="fl-11__event-desc">15 production-grade CSS Flexbox demos published. Covers every major layout pattern from holy grail to kanban board.</div>
        <div class="fl-11__event-card">
          <div class="fl-11__card-row">
            <div class="fl-11__card-icon" style="background:#d1fae5">🎨</div>
            <div>
              <div class="fl-11__card-text">Demos live</div>
              <div class="fl-11__card-sub">All SEO-targeted</div>
            </div>
            <div class="fl-11__card-value">15 demos</div>
          </div>
        </div>
      </div>
    </div>

    <div class="fl-11__event">
      <div class="fl-11__connector">
        <div class="fl-11__dot" style="background:#7c3aed;opacity:0.5">→</div>
        <div class="fl-11__line"></div>
      </div>
      <div class="fl-11__content">
        <div class="fl-11__event-meta">
          <div class="fl-11__date">Q3 2025</div>
          <div class="fl-11__event-tag" style="background:#ede9fe;color:#5b21b6">Planned</div>
        </div>
        <div class="fl-11__event-title">Grid + Subgrid Expansion</div>
        <div class="fl-11__event-desc" style="opacity:0.6">Next phase: 15 CSS Grid layout demos with subgrid, named areas, and masonry support.</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-11,
.fl-11 *,
.fl-11 *::before,
.fl-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-11 ::selection {
  background: #059669;
  color: #fff;
}

.fl-11 {
  --bg: #fafdf9;
  --surface: #fff;
  --ink: #0a1f13;
  --muted: #6b7c74;
  --accent: #059669;
  --accent-light: #d1fae5;
  --accent2: #0284c7;
  --accent3: #d97706;
  --accent4: #7c3aed;
  --timeline-line: #d1fae5;
  --border: #e2f0ea;
  font-family: 'IBM Plex Sans', sans-serif;
  background: var(--bg);
  padding: 28px;
  border-radius: 16px;
  min-height: 500px;
}

.fl-11__header {
  margin-bottom: 28px;
}

.fl-11__eyebrow {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 4px;
}

.fl-11__title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--ink);
}

.fl-11__sub {
  font-size: 0.78rem;
  color: var(--muted);
  margin-top: 4px;
}
/*
  TIMELINE TECHNIQUE:
  Each event = flex row with:
    - connector column (dot + line): flex-shrink: 0
    - content card: flex: 1
  The vertical line is a ::before pseudo on the connector
  that grows to fill the item height.
*/

.fl-11__timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.fl-11__event {
  display: flex;
  gap: 16px;
  position: relative;
}
/* Connector column */

.fl-11__connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
  width: 32px;
}

.fl-11__dot {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  flex-shrink: 0;
  z-index: 1;
  border: 3px solid var(--bg);
  transition: transform 0.2s;
}

.fl-11__event:hover .fl-11__dot {
  transform: scale(1.15);
}

.fl-11__line {
  flex: 1;
  width: 2px;
  background: var(--timeline-line);
  margin-top: 4px;
  margin-bottom: 0;
  min-height: 16px;
}

.fl-11__event:last-child .fl-11__line {
  display: none;
}
/* Content */

.fl-11__content {
  flex: 1;
  padding-bottom: 24px;
}

.fl-11__event-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.fl-11__date {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

.fl-11__event-tag {
  font-size: 0.62rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.fl-11__event-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 4px;
}

.fl-11__event-desc {
  font-size: 0.78rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 8px;
}

.fl-11__event-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 12px 14px;
}

.fl-11__card-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.78rem;
}

.fl-11__card-icon {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.fl-11__card-text {
  color: var(--ink);
  font-weight: 500;
  flex: 1;
}

.fl-11__card-sub {
  font-size: 0.7rem;
  color: var(--muted);
  margin-top: 2px;
}

.fl-11__card-value {
  font-weight: 700;
  color: var(--accent);
  font-size: 0.82rem;
}
/* Today marker */

.fl-11__today {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 4px 0 0 0;
}

.fl-11__today-line {
  flex: 1;
  height: 1px;
  background: repeating-linear-gradient(90deg, var(--accent) 0, var(--accent) 5px, transparent 5px, transparent 10px);
}

.fl-11__today-label {
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-light);
  padding: 3px 8px;
  border-radius: 4px;
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .fl-11__dot {
    transition: none;
  }
}
```
