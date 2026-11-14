---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/swipe-gesture-sidebar/"
title: "Swipe Gesture Sidebar"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A sidebar navigation that responds to edge-swipe touch gestures with real drag tracking, velocity-based dismiss, and a page push parallax effect — built with…"
has_js: "true"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Swipe Gesture Sidebar
Source: https://codefronts.com/navigation/css-mobile-navigation/swipe-gesture-sidebar/

A sidebar navigation that responds to edge-swipe touch gestures with real drag tracking, velocity-based dismiss, and a page push parallax effect — built with a small vanilla JS touch handler and CSS transitions.
## HTML
```html
<div class="mn-06" id="mn-06-root">
  <div class="mn-06__hint"></div>
  <div class="mn-06__overlay" id="mn-06-overlay"></div>

  <nav class="mn-06__sidebar" id="mn-06-sidebar">
    <div class="mn-06__sidebar-header">
      <div class="mn-06__user-pill">
        <div class="mn-06__avatar">🎨</div>
        <div class="mn-06__user-info">
          <h4>Casey Rivera</h4>
          <p>Pro Designer</p>
        </div>
      </div>
    </div>
    <div class="mn-06__sidebar-nav">
      <div class="mn-06__nav-label">Workspace</div>
      <a class="mn-06__nav-item is-active">🎨 Canvas</a>
      <a class="mn-06__nav-item">📐 Wireframes</a>
      <a class="mn-06__nav-item">🎬 Prototypes</a>
      <a class="mn-06__nav-item">📦 Assets</a>
      <div class="mn-06__nav-label">Team</div>
      <a class="mn-06__nav-item">👥 Members</a>
      <a class="mn-06__nav-item">💬 Comments</a>
      <div class="mn-06__nav-label">Account</div>
      <a class="mn-06__nav-item">⚙️ Settings</a>
    </div>
  </nav>

  <div class="mn-06__page">
    <div class="mn-06__topbar">
      <div class="mn-06__menu-btn" id="mn-06-menu-btn">
        <span></span><span></span><span></span>
      </div>
      <span class="mn-06__page-title">Canvas</span>
      <div style="width:40px"></div>
    </div>
    <div class="mn-06__swipe-hint-text">
      <strong>← Swipe right</strong> from the left edge<br>or tap the menu button<br>to open the sidebar
    </div>
    <div class="mn-06__card">
      <div class="mn-06__card-accent" style="background: linear-gradient(90deg, var(--accent), var(--accent2))"></div>
      <h4>Brand Identity Project</h4>
      <p>Updated 2 hours ago · 14 layers</p>
    </div>
    <div class="mn-06__card">
      <div class="mn-06__card-accent" style="background: #14b8a6"></div>
      <h4>App Redesign</h4>
      <p>Updated yesterday · 38 layers</p>
    </div>
  </div>

  <div class="mn-06__edge-zone" id="mn-06-edge"></div>
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

.mn-06 {
  --bg: #18181b;
  --surface: #27272a;
  --border: #3f3f46;
  --accent: #a78bfa;
  --accent2: #f472b6;
  --text: #fafafa;
  --muted: #71717a;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
  touch-action: pan-y;
  user-select: none;
}
/* Overlay */

.mn-06__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0);
  z-index: 10;
  pointer-events: none;
  transition: background 0.3s;
}

.mn-06.is-open .mn-06__overlay {
  background: rgba(0,0,0,0.55);
  pointer-events: all;
}
/* Sidebar */

.mn-06__sidebar {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  background: var(--surface);
  transform: translateX(-100%);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 20;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  will-change: transform;
}

.mn-06.is-open .mn-06__sidebar {
  transform: translateX(0);
}

.mn-06__sidebar.is-dragging {
  transition: none;
}
/* Edge hit zone */

.mn-06__edge-zone {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 20px;
  z-index: 25;
  cursor: ew-resize;
}

.mn-06__sidebar-header {
  padding: 40px 20px 20px;
  background: linear-gradient(135deg, rgba(167,139,250,0.15), rgba(244,114,182,0.08));
  border-bottom: 1px solid var(--border);
}

.mn-06__user-pill {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mn-06__avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.mn-06__user-info h4 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
}

.mn-06__user-info p {
  font-size: 12px;
  color: var(--muted);
}

.mn-06__sidebar-nav {
  flex: 1;
  padding: 12px 0;
}

.mn-06__nav-label {
  padding: 12px 20px 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(113,113,122,0.6);
}

.mn-06__nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.15s;
  border-radius: 0;
  cursor: pointer;
}

.mn-06__nav-item:hover,
.mn-06__nav-item.is-active {
  color: var(--text);
  background: rgba(167,139,250,0.1);
}

.mn-06__nav-item.is-active {
  color: var(--accent);
}
/* Swipe hint */

.mn-06__hint {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 48px;
  background: linear-gradient(to bottom, var(--accent), var(--accent2));
  border-radius: 0 4px 4px 0;
  opacity: 0.5;
  animation: mn-06-pulse 2s ease-in-out infinite;
}

.mn-06.is-open .mn-06__hint {
  opacity: 0;
}

@keyframes mn-06-pulse {
  0%,
    100% {
    opacity: 0.2;
    transform: translateY(-50%) scaleY(0.8);
  }

  50% {
    opacity: 0.6;
    transform: translateY(-50%) scaleY(1);
  }
}
/* Page content */

.mn-06__page {
  position: absolute;
  inset: 0;
  padding: 20px;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

.mn-06.is-open .mn-06__page {
  transform: translateX(60px);
}

.mn-06__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.mn-06__menu-btn {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--surface);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  cursor: pointer;
  border: 1px solid var(--border);
}

.mn-06__menu-btn span {
  width: 18px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
}

.mn-06__page-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
}

.mn-06__swipe-hint-text {
  text-align: center;
  margin-top: 40px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.8;
}

.mn-06__swipe-hint-text strong {
  color: var(--accent);
}

.mn-06__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 12px;
}

.mn-06__card h4 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 6px;
}

.mn-06__card p {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.5;
}

.mn-06__card-accent {
  width: 32px;
  height: 3px;
  border-radius: 2px;
  margin-bottom: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .mn-06__sidebar,
    .mn-06__page,
    .mn-06__overlay,
    .mn-06__hint {
    transition: none;
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const root = document.getElementById('mn-06-root');
  const sidebar = document.getElementById('mn-06-sidebar');
  const overlay = document.getElementById('mn-06-overlay');
  const menuBtn = document.getElementById('mn-06-menu-btn');
  const edge = document.getElementById('mn-06-edge');
  const SIDEBAR_W = 280;

  let startX = 0, startY = 0, currentX = 0, isDragging = false, isOpen = false;

  function open() { isOpen = true; root.classList.add('is-open'); }
  function close() { isOpen = false; root.classList.remove('is-open'); sidebar.style.transform = ''; sidebar.classList.remove('is-dragging'); }

  menuBtn.addEventListener('click', () => isOpen ? close() : open());
  overlay.addEventListener('click', close);

  function onTouchStart(e) {
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
    isDragging = false;
  }

  function onTouchMove(e) {
    const dx = e.touches[0].clientX - startX;
    const dy = e.touches[0].clientY - startY;
    if (!isDragging && Math.abs(dy) > Math.abs(dx)) return;
    if (!isDragging && Math.abs(dx) < 8) return;
    isDragging = true;

    const rect = root.getBoundingClientRect();
    currentX = e.touches[0].clientX - rect.left;

    if (!isOpen && currentX > SIDEBAR_W + 20) return;
    if (isOpen) {
      const offset = Math.min(0, currentX - startX);
      if (offset < 0) {
        sidebar.classList.add('is-dragging');
        sidebar.style.transform = `translateX(${offset}px)`;
      }
    } else {
      const offset = Math.min(SIDEBAR_W, Math.max(0, currentX));
      sidebar.classList.add('is-dragging');
      sidebar.style.transform = `translateX(${offset - SIDEBAR_W}px)`;
    }
  }

  function onTouchEnd(e) {
    if (!isDragging) return;
    sidebar.classList.remove('is-dragging');
    sidebar.style.transform = '';
    const dx = e.changedTouches[0].clientX - startX;
    if (!isOpen && dx > 60) open();
    else if (isOpen && dx < -60) close();
    isDragging = false;
  }

  root.addEventListener('touchstart', onTouchStart, { passive: true });
  root.addEventListener('touchmove', onTouchMove, { passive: true });
  root.addEventListener('touchend', onTouchEnd);
})();
```
