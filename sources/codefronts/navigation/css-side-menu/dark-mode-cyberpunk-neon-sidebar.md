---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/dark-mode-cyberpunk-neon-sidebar/"
title: "Dark Mode Cyberpunk Neon Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A futuristic dark-themed navigation sidebar with pulsing neon text-shadow glows, CSS scanline overlays, sharp geometric accents, and a subtle logo flicker…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Cyberpunk Neon Sidebar
Source: https://codefronts.com/navigation/css-side-menu/dark-mode-cyberpunk-neon-sidebar/

A futuristic dark-themed navigation sidebar with pulsing neon text-shadow glows, CSS scanline overlays, sharp geometric accents, and a subtle logo flicker animation.
## HTML
```html
<div class="sm-11">
  <nav class="sm-11__nav">
    <div class="sm-11__brand">
      <div class="sm-11__brand-label">// SYSTEM ACTIVE</div>
      <div class="sm-11__brand-name">CYBERX</div>
    </div>
    <div class="sm-11__links">
      <a class="sm-11__link sm-11__link--active" href="#"><span class="sm-11__link-bullet"></span> Matrix</a>
      <a class="sm-11__link" href="#"><span class="sm-11__link-bullet"></span> Network</a>
      <a class="sm-11__link" href="#"><span class="sm-11__link-bullet"></span> Console</a>
      <a class="sm-11__link" href="#"><span class="sm-11__link-bullet"></span> Threats</a>
      <a class="sm-11__link" href="#"><span class="sm-11__link-bullet"></span> Logs</a>
      <a class="sm-11__link" href="#"><span class="sm-11__link-bullet"></span> Config</a>
    </div>
    <div class="sm-11__status-bar">
      <div class="sm-11__status-row"><span>CPU</span><span>73%</span></div>
      <div class="sm-11__status-row"><span>MEM</span><span>4.1 GB</span></div>
      <div class="sm-11__progress"><div class="sm-11__progress-fill"></div></div>
    </div>
  </nav>
  <div class="sm-11__main">
    <div class="sm-11__heading">// THREAT MATRIX</div>
    <div class="sm-11__sub">Dark cyberpunk sidebar with neon text-shadow glows, scanline overlays, and a CSS flicker animation — all without a single image or external asset.</div>
    <div class="sm-11__cards">
      <div class="sm-11__card"><div class="sm-11__card-val">0</div><div class="sm-11__card-lbl">Critical</div></div>
      <div class="sm-11__card"><div class="sm-11__card-val">3</div><div class="sm-11__card-lbl">Warnings</div></div>
      <div class="sm-11__card"><div class="sm-11__card-val">99.9%</div><div class="sm-11__card-lbl">Uptime</div></div>
      <div class="sm-11__card"><div class="sm-11__card-val">14ms</div><div class="sm-11__card-lbl">Latency</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-11,
.sm-11 *,
.sm-11 *::before,
.sm-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-11 ::selection {
  background: #ff2d78;
  color: #000;
}

.sm-11 {
  --bg: #020409;
  --surface: #07080f;
  --nav-bg: #040610;
  --neon-pink: #ff2d78;
  --neon-cyan: #00e5ff;
  --neon-purple: #a855f7;
  --text: #e2e8f0;
  --muted: #374151;
  --font-head: 'Orbitron', monospace;
  --font-body: 'Rajdhani', system-ui, sans-serif;
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 12px;
  overflow: hidden;
}

.sm-11__nav {
  width: 220px;
  background: var(--nav-bg);
  border-right: 1px solid var(--neon-pink);
  box-shadow: 2px 0 20px rgba(255,45,120,0.1);
  display: flex;
  flex-direction: column;
  padding: 0;
  flex-shrink: 0;
  position: relative;
  overflow: hidden;
}
/* Scanlines overlay */

.sm-11__nav::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,229,255,0.015) 2px, rgba(0,229,255,0.015) 4px);
  pointer-events: none;
  z-index: 0;
}
/* Neon corner accent */

.sm-11__nav::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 1px;
  height: 60px;
  background: linear-gradient(180deg, var(--neon-cyan), transparent);
  box-shadow: 0 0 8px var(--neon-cyan);
}

.sm-11__brand {
  position: relative;
  z-index: 1;
  padding: 20px 16px;
  border-bottom: 1px solid rgba(255,45,120,0.3);
}

.sm-11__brand-label {
  font-family: var(--font-head);
  font-size: 10px;
  font-weight: 400;
  letter-spacing: 0.2em;
  color: var(--neon-cyan);
  margin-bottom: 4px;
  text-shadow: 0 0 8px var(--neon-cyan);
}

.sm-11__brand-name {
  font-family: var(--font-head);
  font-size: 18px;
  font-weight: 900;
  color: #fff;
  text-shadow: 0 0 12px var(--neon-pink), 0 0 30px rgba(255,45,120,0.4);
  letter-spacing: 0.05em;
}

.sm-11__links {
  flex: 1;
  padding: 12px 0;
  position: relative;
  z-index: 1;
}

.sm-11__link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 16px;
  color: #4b5563;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.08em;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  border-left: 2px solid transparent;
  position: relative;
  text-transform: uppercase;
}

.sm-11__link:hover {
  color: var(--neon-cyan);
  border-left-color: var(--neon-cyan);
  text-shadow: 0 0 8px var(--neon-cyan);
  background: rgba(0,229,255,0.04);
}

.sm-11__link--active {
  color: var(--neon-pink);
  border-left-color: var(--neon-pink);
  text-shadow: 0 0 10px var(--neon-pink);
  background: rgba(255,45,120,0.06);
}
/* Glowing bullet */

.sm-11__link-bullet {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
  box-shadow: 0 0 8px currentColor;
  flex-shrink: 0;
}

.sm-11__status-bar {
  position: relative;
  z-index: 1;
  padding: 12px 16px;
  border-top: 1px solid rgba(255,45,120,0.2);
  font-family: var(--font-head);
  font-size: 9px;
  letter-spacing: 0.1em;
}

.sm-11__status-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
  color: #374151;
}

.sm-11__status-row span:last-child {
  color: var(--neon-cyan);
}

.sm-11__progress {
  height: 2px;
  background: rgba(0,229,255,0.15);
  border-radius: 2px;
  margin-top: 6px;
  overflow: hidden;
}

.sm-11__progress-fill {
  height: 100%;
  width: 73%;
  background: var(--neon-cyan);
  box-shadow: 0 0 6px var(--neon-cyan);
  border-radius: 2px;
}
/* Main */

.sm-11__main {
  flex: 1;
  padding: 22px;
  position: relative;
  overflow: hidden;
}

.sm-11__main::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,229,255,0.008) 3px, rgba(0,229,255,0.008) 6px);
  pointer-events: none;
}

.sm-11__heading {
  font-family: var(--font-head);
  font-size: 16px;
  font-weight: 900;
  color: var(--neon-pink);
  text-shadow: 0 0 12px var(--neon-pink);
  letter-spacing: 0.1em;
  margin-bottom: 6px;
}

.sm-11__sub {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.7;
  margin-bottom: 22px;
  font-weight: 600;
}

.sm-11__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-11__card {
  background: var(--surface);
  border: 1px solid rgba(0,229,255,0.15);
  border-radius: 6px;
  padding: 14px;
  position: relative;
  overflow: hidden;
}
/* Corner glow */

.sm-11__card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 40px;
  height: 1px;
  background: var(--neon-cyan);
  box-shadow: 0 0 8px var(--neon-cyan);
}

.sm-11__card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 1px;
  height: 30px;
  background: var(--neon-cyan);
  box-shadow: 0 0 8px var(--neon-cyan);
}

.sm-11__card-val {
  font-family: var(--font-head);
  font-size: 20px;
  font-weight: 700;
  color: var(--neon-cyan);
  text-shadow: 0 0 10px var(--neon-cyan);
}

.sm-11__card-lbl {
  font-size: 10px;
  color: #374151;
  margin-top: 4px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

@keyframes sm-11-flicker {
  0%,
    95%,
    100% {
    opacity: 1;
  }

  96% {
    opacity: 0.7;
  }

  98% {
    opacity: 0.9;
  }
}

.sm-11__brand-name {
  animation: sm-11-flicker 6s step-end infinite;
}

@media (prefers-reduced-motion: reduce) {
  .sm-11__brand-name {
    animation: none;
  }

  .sm-11__link {
    transition: none;
  }
}
```
