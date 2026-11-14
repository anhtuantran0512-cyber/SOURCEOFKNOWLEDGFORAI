---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/stagger-blur-entrance-dropdown/"
title: "Stagger Blur Entrance Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A JS-toggled dropdown where each menu item blurs in from a frosted state, with per-item transition delays applied programmatically for a cinematic cascade."
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stagger Blur Entrance Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/stagger-blur-entrance-dropdown/

A JS-toggled dropdown where each menu item blurs in from a frosted state, with per-item transition delays applied programmatically for a cinematic cascade.
## HTML
```html
<div class="dd-18">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <div class="dd-18__scene">
    <nav class="dd-18__nav">
      <span class="dd-18__brand">Specter</span>
      <div class="dd-18__group" id="dd-18-group">
        <button class="dd-18__trigger" id="dd-18-btn" aria-expanded="false">
          Menu
          <span class="dd-18__dot" id="dd-18-dot"></span>
        </button>
        <div class="dd-18__panel" id="dd-18-panel">
          <a href="#" class="dd-18__item">&#128640; Launch</a>
          <a href="#" class="dd-18__item">&#127775; Discover</a>
          <a href="#" class="dd-18__item">&#128202; Metrics</a>
          <a href="#" class="dd-18__item">&#128172; Community</a>
          <a href="#" class="dd-18__item">&#128274; Security</a>
          <div class="dd-18__sep"></div>
          <a href="#" class="dd-18__item dd-18__item--em">&#9889; Upgrade</a>
        </div>
      </div>
    </nav>
  </div>
</div>
```
## CSS
```css
.dd-18,
.dd-18 *,
.dd-18 *::before,
.dd-18 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-18 ::selection {
  background: #7c3aed;
  color: #ede9fe;
}

.dd-18 {
  --brand: #7c3aed;
  --surface: #fff;
  --text: #18181b;
  --muted: #71717a;
  --border: #e4e4e7;
  --hover: #f5f3ff;
  font-family: 'Space Grotesk', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 36px 20px;
  background: linear-gradient(135deg, #faf5ff 0%, #ede9fe 100%);
}

.dd-18__scene {
  width: 100%;
  max-width: 480px;
  position: relative;
  z-index: 100;
}

.dd-18__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 12px 16px;
  box-shadow: 0 4px 20px rgba(124,58,237,.1);
}

.dd-18__brand {
  font-size: 18px;
  font-weight: 700;
  color: var(--brand);
  letter-spacing: -0.5px;
}

.dd-18__group {
  position: relative;
}

.dd-18__trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  background: var(--brand);
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  transition: opacity 0.15s;
}

.dd-18__trigger:hover {
  opacity: 0.9;
}

.dd-18__trigger[aria-expanded="true"] {
  opacity: 0.85;
}

.dd-18__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #a78bfa;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dd-18__trigger[aria-expanded="true"] .dd-18__dot {
  transform: scale(1.5);
  background: #c4b5fd;
}

.dd-18__panel {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  min-width: 200px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: 0 12px 40px rgba(124,58,237,.18);
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
}

.dd-18__panel.is-open {
  opacity: 1;
  pointer-events: auto;
}

.dd-18__item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 13px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  opacity: 0;
  filter: blur(6px);
  transform: translateY(6px);
  transition: opacity 0.3s ease, filter 0.3s ease, transform 0.3s ease, background 0.12s;
}

.dd-18__panel.is-open .dd-18__item {
  opacity: 1;
  filter: blur(0);
  transform: translateY(0);
}

.dd-18__item:hover {
  background: var(--hover);
}

.dd-18__item--em {
  color: var(--brand);
  font-weight: 700;
}

.dd-18__sep {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

@media (prefers-reduced-motion: reduce) {
  .dd-18__item,
    .dd-18__panel {
    transition: none;
    filter: none;
  }

  .dd-18__panel.is-open .dd-18__item {
    opacity: 1;
    filter: none;
    transform: none;
  }
}
```

## JavaScript
```js
(function() {
  var btn   = document.getElementById('dd-18-btn');
  var panel = document.getElementById('dd-18-panel');
  if (!btn || !panel) return;
  var items = Array.from(panel.querySelectorAll('.dd-18__item'));

  items.forEach(function(el, i) { el.dataset.delay = i * 55; });

  function openPanel() {
    panel.classList.add('is-open');
    btn.setAttribute('aria-expanded', 'true');
    items.forEach(function(el) { el.style.transitionDelay = el.dataset.delay + 'ms'; });
  }

  function closePanel() {
    items.forEach(function(el) { el.style.transitionDelay = '0ms'; });
    panel.classList.remove('is-open');
    btn.setAttribute('aria-expanded', 'false');
  }

  btn.addEventListener('click', function(e) {
    e.stopPropagation();
    panel.classList.contains('is-open') ? closePanel() : openPanel();
  });
  document.addEventListener('click', function(e) {
    if (!panel.contains(e.target) && e.target !== btn) closePanel();
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closePanel();
  });
})();
```
