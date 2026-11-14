---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-dashboard-overlay/"
title: "CSS Frosted Glass Dashboard Overlay"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A dashboard with three app widgets (music player, weather, calendar events) beneath a frosted glass notification overlay panel — the pattern iOS 26, macOS…"
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Frosted Glass Dashboard Overlay
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-dashboard-overlay/

A dashboard with three app widgets (music player, weather, calendar events) beneath a frosted glass notification overlay panel — the pattern iOS 26, macOS 26, and modern desktop OSes use for system chrome. Each widget shows real content: current song with progress bar, weather forecast, upcoming meetings. The floating notification panel demonstrates glassmorphism as UI chrome rather than pure decoration.
## HTML
```html
<div class="fg-02">
  <div class="fg-02__stage">

    <header class="fg-02__topbar">
      <div class="fg-02__topbar-left">
        <span class="fg-02__brand">Studio OS</span>
        <span class="fg-02__crumbs">Dashboard · Home</span>
      </div>
      <div class="fg-02__topbar-right">
        <span class="fg-02__time">2:47 PM</span>
        <span class="fg-02__badge" aria-label="3 unread">3</span>
      </div>
    </header>

    <div class="fg-02__grid">

      <!-- Music player widget -->
      <article class="fg-02__widget fg-02__widget--music">
        <span class="fg-02__widget-kicker">Now Playing</span>
        <div class="fg-02__music-cover" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.6">
            <circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2" fill="currentColor"/>
          </svg>
        </div>
        <h3 class="fg-02__music-title">Midnight Drive</h3>
        <p class="fg-02__music-artist">Aurora · Nightlands</p>
        <div class="fg-02__progress" role="progressbar" aria-valuenow="42">
          <span class="fg-02__progress-fill"></span>
        </div>
        <div class="fg-02__music-time">
          <span>1:47</span>
          <span>4:12</span>
        </div>
      </article>

      <!-- Weather widget -->
      <article class="fg-02__widget fg-02__widget--weather">
        <div class="fg-02__weather-head">
          <span class="fg-02__widget-kicker">San Francisco</span>
          <span class="fg-02__weather-cond">Partly cloudy</span>
        </div>
        <div class="fg-02__weather-hero">
          <span class="fg-02__weather-temp">64°</span>
          <span class="fg-02__weather-icon" aria-hidden="true">☁</span>
        </div>
        <ul class="fg-02__weather-hours">
          <li><span>3 PM</span><b>64°</b></li>
          <li><span>4 PM</span><b>62°</b></li>
          <li><span>5 PM</span><b>60°</b></li>
          <li><span>6 PM</span><b>58°</b></li>
        </ul>
      </article>

      <!-- Calendar widget -->
      <article class="fg-02__widget fg-02__widget--calendar">
        <span class="fg-02__widget-kicker">Today · 3 events</span>
        <ul class="fg-02__events">
          <li>
            <span class="fg-02__event-time">3:00</span>
            <div>
              <b>Design review</b>
              <span>with Maya, Liam</span>
            </div>
          </li>
          <li>
            <span class="fg-02__event-time">4:30</span>
            <div>
              <b>1:1 with Aria</b>
              <span>Weekly sync</span>
            </div>
          </li>
          <li>
            <span class="fg-02__event-time">6:00</span>
            <div>
              <b>Ship glassmorphism</b>
              <span>Codefronts release</span>
            </div>
          </li>
        </ul>
      </article>

    </div>

    <!-- Floating frosted notification panel -->
    <div class="fg-02__panel" role="alert">
      <div class="fg-02__panel-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"/>
        </svg>
      </div>
      <div class="fg-02__panel-body">
        <div class="fg-02__panel-head">
          <span class="fg-02__panel-title">Maya Chen</span>
          <span class="fg-02__panel-time">now</span>
        </div>
        <p class="fg-02__panel-msg">Design review is starting in 12 minutes. Room 4B or join remotely from your calendar.</p>
        <div class="fg-02__panel-actions">
          <button type="button" class="fg-02__panel-btn fg-02__panel-btn--primary">Join</button>
          <button type="button" class="fg-02__panel-btn">Snooze</button>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fg-02,
.fg-02 *,
.fg-02 *::before,
.fg-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-02 ::selection {
  background: rgba(255,255,255,.28);
  color: #fff;
}

.fg-02 {
  --accent: #7c6cff;
  --paper: #0b0d15;
  --card: #181c2b;
  --ink: #f1f5f9;
  --muted: #94a3b8;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,sans-serif;
  color: var(--ink);
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fg-02__stage {
  position: relative;
  width: 100%;
  min-height: calc(100vh - 48px);
  border-radius: 22px;
  overflow: hidden;
  background: radial-gradient(circle at 20% 20%, rgba(124,108,255,0.28) 0%, transparent 42%), radial-gradient(circle at 85% 80%, rgba(236,72,153,0.22) 0%, transparent 40%), linear-gradient(135deg,#0b0d15 0%,#1a1d2d 100%);
  padding: clamp(20px,2.6vw,32px);
  display: flex;
  flex-direction: column;
  gap: clamp(16px,2vw,24px);
}
/* Topbar */

.fg-02__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 6px;
}

.fg-02__topbar-left {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.fg-02__brand {
  font-size: .94rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
}

.fg-02__crumbs {
  font-size: .78rem;
  color: var(--muted);
  font-weight: 500;
}

.fg-02__topbar-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.fg-02__time {
  font-size: .82rem;
  color: var(--muted);
  font-weight: 600;
  font-feature-settings: "tnum";
}

.fg-02__badge {
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-size: .7rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
/* Widget grid */

.fg-02__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: clamp(14px,1.8vw,20px);
  flex: 1;
  align-content: start;
}

.fg-02__widget {
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  padding: clamp(16px,2vw,22px);
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: clamp(200px,22vw,260px);
}

.fg-02__widget-kicker {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}
/* Music widget */

.fg-02__music-cover {
  width: clamp(52px,6vw,64px);
  height: clamp(52px,6vw,64px);
  border-radius: 14px;
  background: linear-gradient(135deg,#7c6cff,#ec4899);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: auto;
}

.fg-02__music-title {
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-top: 6px;
}

.fg-02__music-artist {
  font-size: .82rem;
  color: var(--muted);
}

.fg-02__progress {
  height: 4px;
  border-radius: 2px;
  background: rgba(255,255,255,0.08);
  overflow: hidden;
  margin-top: auto;
}

.fg-02__progress-fill {
  display: block;
  height: 100%;
  width: 42%;
  background: var(--accent);
  border-radius: 2px;
}

.fg-02__music-time {
  display: flex;
  justify-content: space-between;
  font-size: .72rem;
  color: var(--muted);
  font-feature-settings: "tnum";
}
/* Weather widget */

.fg-02__weather-head {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.fg-02__weather-cond {
  font-size: .86rem;
  font-weight: 600;
  color: var(--ink);
}

.fg-02__weather-hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 8px 0;
}

.fg-02__weather-temp {
  font-size: clamp(2.4rem,4.4vw,3.2rem);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1;
  font-feature-settings: "tnum";
}

.fg-02__weather-icon {
  font-size: 2.6rem;
  line-height: 1;
  color: var(--muted);
}

.fg-02__weather-hours {
  list-style: none;
  display: flex;
  justify-content: space-between;
  margin-top: auto;
  padding-top: 10px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.fg-02__weather-hours li {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  font-size: .72rem;
}

.fg-02__weather-hours li span {
  color: var(--muted);
}

.fg-02__weather-hours li b {
  font-size: .86rem;
  font-weight: 700;
  color: var(--ink);
}
/* Calendar widget */

.fg-02__events {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fg-02__events li {
  display: flex;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.fg-02__events li:last-child {
  border-bottom: 0;
}

.fg-02__event-time {
  font-size: .82rem;
  font-weight: 700;
  color: var(--accent);
  font-feature-settings: "tnum";
  min-width: 36px;
}

.fg-02__events li > div {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.fg-02__events li b {
  font-size: .88rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.25;
}

.fg-02__events li span {
  font-size: .76rem;
  color: var(--muted);
}
/* Floating frosted notification panel */

.fg-02__panel {
  position: absolute;
  top: 22%;
  right: clamp(20px,4vw,60px);
  width: min(360px,calc(100% - 40px));
  padding: clamp(16px,2vw,20px);
  border-radius: 16px;
  background: rgba(255,255,255,0.14);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.22);
  box-shadow: 0 24px 48px -20px rgba(0,0,0,0.42), inset 0 1px 0 rgba(255,255,255,0.32);
  display: flex;
  gap: 12px;
  z-index: 2;
  color: #fff;
}

@supports not (backdrop-filter: blur(1px)) {
  .fg-02__panel {
    background: rgba(24,28,43,0.94);
  }
}

.fg-02__panel-icon {
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: rgba(124,108,255,0.32);
  color: #c4b5fd;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fg-02__panel-body {
  flex: 1;
  min-width: 0;
}

.fg-02__panel-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
}

.fg-02__panel-title {
  font-size: .94rem;
  font-weight: 700;
  color: #fff;
}

.fg-02__panel-time {
  font-size: .74rem;
  color: rgba(255,255,255,0.6);
  font-weight: 600;
}

.fg-02__panel-msg {
  font-size: .86rem;
  line-height: 1.45;
  color: rgba(255,255,255,0.86);
  margin: 4px 0 12px;
}

.fg-02__panel-actions {
  display: flex;
  gap: 8px;
}

.fg-02__panel-btn {
  padding: 6px 14px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.22);
  background: rgba(255,255,255,0.08);
  color: #fff;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.fg-02__panel-btn:hover {
  background: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,0.35);
}

.fg-02__panel-btn--primary {
  background: var(--accent);
  border-color: var(--accent);
}

.fg-02__panel-btn--primary:hover {
  background: #6d5cf0;
  border-color: #6d5cf0;
}

@media (max-width: 900px) {
  .fg-02__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .fg-02__widget--calendar {
    grid-column: 1 / -1;
  }

  .fg-02__panel {
    top: auto;
    bottom: 24px;
    left: 20px;
    right: 20px;
    width: auto;
  }
}

@media (max-width: 560px) {
  .fg-02__grid {
    grid-template-columns: 1fr;
  }

  .fg-02__widget--calendar {
    grid-column: auto;
  }

  .fg-02__weather-icon {
    font-size: 2rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-02__panel-btn,
    .fg-02__progress-fill {
    transition: none;
  }
}
```
