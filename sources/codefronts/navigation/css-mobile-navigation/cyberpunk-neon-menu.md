---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/cyberpunk-neon-menu/"
title: "Cyberpunk Neon Menu"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A full-screen cyberpunk navigation overlay with a scanline effect, CSS grid background, clip-path left-to-right reveal, and individually neon-coloured menu…"
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Menu
Source: https://codefronts.com/navigation/css-mobile-navigation/cyberpunk-neon-menu/

A full-screen cyberpunk navigation overlay with a scanline effect, CSS grid background, clip-path left-to-right reveal, and individually neon-coloured menu items that stagger in on activation.
## HTML
```html
<div class="mn-11">
  <div class="mn-11__grid"></div>
  <input type="checkbox" id="mn-11-toggle">
  <div class="mn-11__topbar">
    <div class="mn-11__logo">NEXUS</div>
    <label for="mn-11-toggle" class="mn-11__btn">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="mn-11__menu">
    <div class="mn-11__menu-header">
      <div class="mn-11__menu-sys">SYS · <span>ONLINE</span></div>
      <label for="mn-11-toggle" class="mn-11__close">✕</label>
    </div>
    <ul class="mn-11__nav-list">
      <li><a href="#"><span class="num">01</span><span class="label">Missions</span><span class="arrow">→</span></a></li>
      <li><a href="#"><span class="num">02</span><span class="label">Arsenal</span><span class="arrow">→</span></a></li>
      <li><a href="#"><span class="num">03</span><span class="label">Intel</span><span class="arrow">→</span></a></li>
      <li><a href="#"><span class="num">04</span><span class="label">Network</span><span class="arrow">→</span></a></li>
      <li><a href="#"><span class="num">05</span><span class="label">Profile</span><span class="arrow">→</span></a></li>
    </ul>
    <div class="mn-11__menu-footer">Version 2.4.7 · <span>CLASSIFIED</span></div>
  </div>
  <div class="mn-11__page">
    <div class="mn-11__page-title">// System Status</div>
    <div class="mn-11__page-h1">Nexus Core</div>
    <div class="mn-11__neon-card">
      <h4>Active Missions</h4>
      <p>3 operations in progress — 1 critical priority</p>
    </div>
    <div class="mn-11__neon-card">
      <h4>Network Uplink</h4>
      <p>Encrypted tunnel established · Ping 12ms</p>
    </div>
    <div class="mn-11__neon-card">
      <h4>Agent Status</h4>
      <p>Identity verified · Clearance level ALPHA</p>
    </div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Courier New', monospace;
}

.mn-11 {
  --bg: #05010f;
  --surface: #0d0922;
  --cyan: #00f5ff;
  --magenta: #ff00a0;
  --yellow: #ffe600;
  --green: #00ff88;
  --text: #e0e0ff;
  --muted: #5a5a8a;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 0 60px rgba(0,245,255,0.15), 0 30px 80px rgba(0,0,0,0.9);
}
/* Scanlines */

.mn-11::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px);
  pointer-events: none;
  z-index: 1;
}

.mn-11 #mn-11-toggle {
  display: none;
}
/* Grid lines */

.mn-11__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(0,245,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(0,245,255,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
}
/* Top bar */

.mn-11__topbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 10;
  border-bottom: 1px solid rgba(0,245,255,0.15);
}

.mn-11__logo {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--cyan);
  text-shadow: 0 0 10px var(--cyan), 0 0 20px rgba(0,245,255,0.5);
  animation: mn-11-glow 3s ease-in-out infinite;
}

@keyframes mn-11-glow {
  0%,
    100% {
    text-shadow: 0 0 8px var(--cyan), 0 0 16px rgba(0,245,255,0.4);
  }

  50% {
    text-shadow: 0 0 16px var(--cyan), 0 0 32px rgba(0,245,255,0.7);
  }
}
/* Neon hamburger */

.mn-11__btn {
  width: 40px;
  height: 40px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  border: 1px solid rgba(0,245,255,0.3);
  border-radius: 4px;
  background: rgba(0,245,255,0.04);
  transition: border-color 0.2s, box-shadow 0.2s;
}

.mn-11__btn:hover {
  border-color: var(--cyan);
  box-shadow: 0 0 10px rgba(0,245,255,0.3) inset;
}

.mn-11__btn span {
  width: 20px;
  height: 1px;
  background: var(--cyan);
  box-shadow: 0 0 6px var(--cyan);
  transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
  transform-origin: center;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__topbar .mn-11__btn span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__topbar .mn-11__btn span:nth-child(2) {
  opacity: 0;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__topbar .mn-11__btn span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* Fullscreen neon overlay */

.mn-11__menu {
  position: absolute;
  inset: 0;
  background: rgba(5,1,15,0.97);
  z-index: 20;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px 32px;
  opacity: 0;
  pointer-events: none;
  clip-path: polygon(100% 0, 100% 0, 100% 100%, 100% 100%);
  transition: opacity 0.4s, clip-path 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu {
  opacity: 1;
  pointer-events: all;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}

.mn-11__menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 48px;
}

.mn-11__menu-sys {
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--muted);
  text-transform: uppercase;
}

.mn-11__menu-sys span {
  color: var(--green);
}

.mn-11__close {
  font-size: 20px;
  color: var(--cyan);
  cursor: pointer;
  text-shadow: 0 0 10px var(--cyan);
}

.mn-11__nav-list {
  list-style: none;
}

.mn-11__nav-list li {
  margin-bottom: 4px;
  opacity: 0;
  transform: translateX(-30px);
  transition: opacity 0.4s, transform 0.4s cubic-bezier(0.4,0,0.2,1);
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li {
  opacity: 1;
  transform: translateX(0);
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li:nth-child(1) {
  transition-delay: 0.15s;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li:nth-child(2) {
  transition-delay: 0.22s;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li:nth-child(3) {
  transition-delay: 0.29s;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li:nth-child(4) {
  transition-delay: 0.36s;
}

.mn-11 #mn-11-toggle:checked ~ .mn-11__menu .mn-11__nav-list li:nth-child(5) {
  transition-delay: 0.43s;
}

.mn-11__nav-list a {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 0;
  text-decoration: none;
  border-bottom: 1px solid rgba(0,245,255,0.08);
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}

.mn-11__nav-list a:hover {
  padding-left: 8px;
}

.mn-11__nav-list a .num {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 1px;
  min-width: 28px;
}

.mn-11__nav-list a .label {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  transition: color 0.2s, text-shadow 0.2s;
}

.mn-11__nav-list li:nth-child(1) a .label {
  color: var(--cyan);
  text-shadow: 0 0 12px rgba(0,245,255,0.5);
}

.mn-11__nav-list li:nth-child(2) a .label {
  color: var(--magenta);
  text-shadow: 0 0 12px rgba(255,0,160,0.5);
}

.mn-11__nav-list li:nth-child(3) a .label {
  color: var(--yellow);
  text-shadow: 0 0 12px rgba(255,230,0,0.5);
}

.mn-11__nav-list li:nth-child(4) a .label {
  color: var(--green);
  text-shadow: 0 0 12px rgba(0,255,136,0.5);
}

.mn-11__nav-list li:nth-child(5) a .label {
  color: var(--text);
}

.mn-11__nav-list a .arrow {
  margin-left: auto;
  font-size: 18px;
  color: var(--muted);
}

.mn-11__menu-footer {
  margin-top: 40px;
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--muted);
}

.mn-11__menu-footer span {
  color: var(--magenta);
}
/* Page content */

.mn-11__page {
  position: absolute;
  top: 56px;
  inset-inline: 0;
  bottom: 0;
  padding: 24px 20px;
  z-index: 5;
}

.mn-11__page-title {
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--cyan);
  margin-bottom: 4px;
  text-shadow: 0 0 8px rgba(0,245,255,0.5);
}

.mn-11__page-h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.5px;
  margin-bottom: 24px;
}

.mn-11__neon-card {
  border: 1px solid;
  border-radius: 4px;
  padding: 16px;
  margin-bottom: 12px;
  position: relative;
}

.mn-11__neon-card:nth-child(1) {
  border-color: rgba(0,245,255,0.3);
}

.mn-11__neon-card:nth-child(2) {
  border-color: rgba(255,0,160,0.3);
}

.mn-11__neon-card:nth-child(3) {
  border-color: rgba(0,255,136,0.3);
}

.mn-11__neon-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 16px;
  width: 32px;
  height: 2px;
  border-radius: 0 0 4px 4px;
}

.mn-11__neon-card:nth-child(1)::before {
  background: var(--cyan);
  box-shadow: 0 0 8px var(--cyan);
}

.mn-11__neon-card:nth-child(2)::before {
  background: var(--magenta);
  box-shadow: 0 0 8px var(--magenta);
}

.mn-11__neon-card:nth-child(3)::before {
  background: var(--green);
  box-shadow: 0 0 8px var(--green);
}

.mn-11__neon-card h4 {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--text);
  margin-bottom: 4px;
}

.mn-11__neon-card p {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .mn-11__logo {
    animation: none;
  }

  .mn-11__menu,
    .mn-11__nav-list li,
    .mn-11__btn span {
    transition: none;
  }
}
```
