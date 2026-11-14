---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/glass-morphism-nav-drawer/"
title: "Glass Morphism Nav Drawer"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A sidebar drawer with heavy backdrop-filter glass styling over continuously animated gradient blobs."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Morphism Nav Drawer
Source: https://codefronts.com/navigation/css-mobile-navigation/glass-morphism-nav-drawer/

A sidebar drawer with heavy backdrop-filter glass styling over continuously animated gradient blobs. Features a frosted glass avatar, gradient-tinted nav links, and an upgrade card — all Pure CSS.
## HTML
```html
<div class="mn-10">
  <div class="mn-10__bg">
    <div class="mn-10__blob"></div>
    <div class="mn-10__blob"></div>
    <div class="mn-10__blob"></div>
  </div>
  <input type="checkbox" id="mn-10-toggle">
  <div class="mn-10__topbar">
    <div class="mn-10__logo">Aura<span>UI</span></div>
    <label for="mn-10-toggle" class="mn-10__btn">
      <span></span><span></span><span></span>
    </label>
  </div>
  <label class="mn-10__overlay" for="mn-10-toggle"></label>
  <nav class="mn-10__drawer">
    <div class="mn-10__drawer-top">
      <div class="mn-10__glass-avatar">✨</div>
      <h3>Morgan Lee</h3>
      <p>[email protected]</p>
    </div>
    <div class="mn-10__drawer-nav">
      <div class="mn-10__nav-section">Workspace</div>
      <a class="mn-10__nav-link is-active"><span class="mn-10__nav-link-icon">🏠</span> Dashboard</a>
      <a class="mn-10__nav-link"><span class="mn-10__nav-link-icon">🎨</span> Design <span class="mn-10__nav-link-badge">3</span></a>
      <a class="mn-10__nav-link"><span class="mn-10__nav-link-icon">📊</span> Analytics</a>
      <a class="mn-10__nav-link"><span class="mn-10__nav-link-icon">🔗</span> Integrations</a>
      <div class="mn-10__nav-section">Account</div>
      <a class="mn-10__nav-link"><span class="mn-10__nav-link-icon">👤</span> Profile</a>
      <a class="mn-10__nav-link"><span class="mn-10__nav-link-icon">⚙️</span> Settings</a>
    </div>
    <div class="mn-10__upgrade">
      <h4>Upgrade to Pro ✨</h4>
      <p>Unlock unlimited projects, advanced analytics, and priority support.</p>
      <a href="#" class="mn-10__upgrade-btn">Upgrade Now</a>
    </div>
  </nav>
  <div class="mn-10__page">
    <div class="mn-10__welcome">Good evening ✨</div>
    <div class="mn-10__sub">Here's your workspace overview</div>
    <div class="mn-10__glass-card">
      <div class="mn-10__card-accent-bar" style="background:linear-gradient(90deg,#a78bfa,#38bdf8)"></div>
      <h4>Active Projects</h4>
      <p>8 projects running — 3 due this week</p>
    </div>
    <div class="mn-10__glass-card">
      <div class="mn-10__card-accent-bar" style="background:linear-gradient(90deg,#f472b6,#fb923c)"></div>
      <h4>Recent Designs</h4>
      <p>Landing page refresh updated 20 min ago</p>
    </div>
    <div class="mn-10__glass-card">
      <div class="mn-10__card-accent-bar" style="background:linear-gradient(90deg,#4ade80,#06b6d4)"></div>
      <h4>Team Activity</h4>
      <p>4 collaborators online right now</p>
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
  font-family: 'Segoe UI', sans-serif;
}

.mn-10 {
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
}
/* Background gradient blobs */

.mn-10__bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #1a0533 0%, #0a0a2a 50%, #001a33 100%);
  z-index: 0;
}

.mn-10__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
}

.mn-10__blob:nth-child(1) {
  width: 250px;
  height: 250px;
  top: -80px;
  left: -60px;
  background: radial-gradient(circle, #7c3aed, transparent 70%);
  animation: mn-10-blob1 8s ease-in-out infinite;
}

.mn-10__blob:nth-child(2) {
  width: 200px;
  height: 200px;
  bottom: -40px;
  right: -40px;
  background: radial-gradient(circle, #0ea5e9, transparent 70%);
  animation: mn-10-blob2 10s ease-in-out infinite;
}

.mn-10__blob:nth-child(3) {
  width: 150px;
  height: 150px;
  top: 50%;
  left: 60%;
  background: radial-gradient(circle, #ec4899, transparent 70%);
  animation: mn-10-blob3 12s ease-in-out infinite;
}

@keyframes mn-10-blob1 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(30px,30px);
  }
}

@keyframes mn-10-blob2 {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(-20px,-20px);
  }
}

@keyframes mn-10-blob3 {
  0%,
    100% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(-15px,10px) scale(1.2);
  }
}

.mn-10 #mn-10-toggle {
  display: none;
}
/* Topbar */

.mn-10__topbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 10;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.mn-10__logo {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.3px;
}

.mn-10__logo span {
  background: linear-gradient(90deg, #a78bfa, #38bdf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
/* Hamburger */

.mn-10__btn {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.15);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.mn-10__btn span {
  width: 18px;
  height: 2px;
  background: rgba(255,255,255,0.9);
  border-radius: 2px;
  transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
  transform-origin: center;
}

.mn-10 #mn-10-toggle:checked ~ .mn-10__topbar .mn-10__btn span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.mn-10 #mn-10-toggle:checked ~ .mn-10__topbar .mn-10__btn span:nth-child(2) {
  opacity: 0;
}

.mn-10 #mn-10-toggle:checked ~ .mn-10__topbar .mn-10__btn span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}
/* Overlay */

.mn-10__overlay {
  position: absolute;
  inset: 0;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  background: rgba(0,0,0,0.3);
  z-index: 15;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s;
}

.mn-10 #mn-10-toggle:checked ~ .mn-10__overlay {
  opacity: 1;
  pointer-events: all;
}
/* Glass drawer */

.mn-10__drawer {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 285px;
  background: rgba(255,255,255,0.07);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-right: 1px solid rgba(255,255,255,0.12);
  z-index: 20;
  transform: translateX(-100%);
  transition: transform 0.4s cubic-bezier(0.4,0,0.2,1);
  display: flex;
  flex-direction: column;
}

.mn-10 #mn-10-toggle:checked ~ .mn-10__overlay ~ .mn-10__drawer {
  transform: translateX(0);
}

.mn-10__drawer-top {
  padding: 80px 24px 24px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.mn-10__glass-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(167,139,250,0.5), rgba(56,189,248,0.5));
  border: 2px solid rgba(255,255,255,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-bottom: 14px;
  backdrop-filter: blur(10px);
}

.mn-10__drawer-top h3 {
  color: rgba(255,255,255,0.95);
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 2px;
}

.mn-10__drawer-top p {
  color: rgba(255,255,255,0.45);
  font-size: 13px;
}

.mn-10__drawer-nav {
  flex: 1;
  padding: 12px 0;
  overflow-y: auto;
}

.mn-10__nav-section {
  padding: 12px 24px 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.25);
}

.mn-10__nav-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  color: rgba(255,255,255,0.65);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s;
  border-radius: 0;
}

.mn-10__nav-link:hover,
.mn-10__nav-link.is-active {
  background: rgba(255,255,255,0.07);
  color: rgba(255,255,255,0.95);
}

.mn-10__nav-link.is-active {
  color: #a78bfa;
}

.mn-10__nav-link-icon {
  width: 18px;
  text-align: center;
  font-size: 16px;
}

.mn-10__nav-link-badge {
  margin-left: auto;
  background: rgba(167,139,250,0.2);
  color: #a78bfa;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 10px;
}
/* Glass upgrade card */

.mn-10__upgrade {
  margin: 12px 16px 24px;
  padding: 16px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(124,58,237,0.25), rgba(14,165,233,0.15));
  border: 1px solid rgba(167,139,250,0.3);
}

.mn-10__upgrade h4 {
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 4px;
}

.mn-10__upgrade p {
  color: rgba(255,255,255,0.55);
  font-size: 11px;
  line-height: 1.5;
  margin-bottom: 10px;
}

.mn-10__upgrade-btn {
  display: block;
  width: 100%;
  background: linear-gradient(90deg, #7c3aed, #0ea5e9);
  color: #fff;
  text-align: center;
  font-size: 12px;
  font-weight: 600;
  padding: 8px;
  border-radius: 8px;
  text-decoration: none;
}
/* Page */

.mn-10__page {
  position: absolute;
  top: 64px;
  inset-inline: 0;
  bottom: 0;
  padding: 24px 20px;
  z-index: 5;
  overflow-y: auto;
}

.mn-10__welcome {
  color: rgba(255,255,255,0.95);
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.5px;
  margin-bottom: 8px;
}

.mn-10__sub {
  color: rgba(255,255,255,0.45);
  font-size: 13px;
  margin-bottom: 24px;
}

.mn-10__glass-card {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 12px;
  backdrop-filter: blur(8px);
}

.mn-10__glass-card h4 {
  color: rgba(255,255,255,0.9);
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 6px;
}

.mn-10__glass-card p {
  color: rgba(255,255,255,0.45);
  font-size: 12px;
  line-height: 1.5;
}

.mn-10__card-accent-bar {
  height: 3px;
  border-radius: 2px;
  margin-bottom: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .mn-10__blob {
    animation: none;
  }

  .mn-10__drawer,
    .mn-10__overlay,
    .mn-10__btn span {
    transition: none;
  }
}
```
