---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/context-menu-right-click-dropdown/"
title: "Context Menu Right-Click Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A custom right-click context menu that appears at the exact cursor position on contextmenu event, with smooth CSS entrance animation and click-outside…"
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Context Menu Right-Click Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/context-menu-right-click-dropdown/

A custom right-click context menu that appears at the exact cursor position on contextmenu event, with smooth CSS entrance animation and click-outside dismissal.
## HTML
```html
<div class="dd-16">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-16__zone" id="dd-16-zone">
    <div class="dd-16__hint">
      <span class="dd-16__hint-icon">&#128432;</span>
      <p>Right-click anywhere in this area</p>
    </div>
    <div class="dd-16__file" id="dd-16-file">
      <span>&#128196;</span>
      <span>document.pdf</span>
    </div>
  </div>
  <ul class="dd-16__menu" id="dd-16-menu" role="menu">
    <li class="dd-16__item"><span class="dd-16__icon">&#128196;</span> Open</li>
    <li class="dd-16__item"><span class="dd-16__icon">&#128065;</span> Preview</li>
    <li class="dd-16__sep"></li>
    <li class="dd-16__item"><span class="dd-16__icon">&#128461;</span> Copy</li>
    <li class="dd-16__item"><span class="dd-16__icon">&#9999;</span> Rename</li>
    <li class="dd-16__item"><span class="dd-16__icon">&#128279;</span> Copy Link</li>
    <li class="dd-16__sep"></li>
    <li class="dd-16__item dd-16__item--danger"><span class="dd-16__icon">&#128465;</span> Delete</li>
  </ul>
</div>
```
## CSS
```css
.dd-16,
.dd-16 *,
.dd-16 *::before,
.dd-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-16 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.dd-16 {
  --surface: #fff;
  --border: #e5e7eb;
  --text: #111827;
  --muted: #6b7280;
  --danger: #ef4444;
  --accent: #0ea5e9;
  --hover: #f0f9ff;
  font-family: 'Inter', sans-serif;
  min-height: 360px;
  position: relative;
  background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 100%);
  user-select: none;
}

.dd-16__zone {
  width: 100%;
  height: 360px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  cursor: context-menu;
  border: 2px dashed #bae6fd;
  border-radius: 16px;
}

.dd-16__hint {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--muted);
  font-size: 13.5px;
  font-weight: 500;
}

.dd-16__hint-icon {
  font-size: 28px;
}

.dd-16__file {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 18px;
  font-size: 13.5px;
  font-weight: 500;
  color: var(--text);
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,.06);
  transition: box-shadow 0.15s;
}

.dd-16__file:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,.1);
}
/* context menu */

.dd-16__menu {
  position: fixed;
  min-width: 190px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,.16), 0 2px 8px rgba(0,0,0,.08);
  padding: 6px;
  list-style: none;
  z-index: 9999;
  opacity: 0;
  transform: scale(0.92);
  transform-origin: top left;
  pointer-events: none;
  transition: opacity 0.18s ease, transform 0.22s cubic-bezier(0.16,1,0.3,1);
}

.dd-16__menu.is-open {
  opacity: 1;
  transform: scale(1);
  pointer-events: auto;
}

.dd-16__item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  border-radius: 7px;
  font-size: 13.5px;
  font-weight: 500;
  color: var(--text);
  cursor: pointer;
  transition: background 0.12s, color 0.12s;
}

.dd-16__item:hover {
  background: var(--hover);
  color: var(--accent);
}

.dd-16__item--danger {
  color: var(--danger);
}

.dd-16__item--danger:hover {
  background: #fef2f2;
  color: var(--danger);
}

.dd-16__icon {
  font-size: 14px;
  width: 18px;
  text-align: center;
}

.dd-16__sep {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

@media (prefers-reduced-motion: reduce) {
  .dd-16__menu {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const zone = document.getElementById('dd-16-zone');
  const menu = document.getElementById('dd-16-menu');
  if (!zone || !menu) return;

  function openMenu(x, y) {
    menu.classList.add('is-open');
    // position with viewport clamping
    const mw = menu.offsetWidth || 200;
    const mh = menu.offsetHeight || 240;
    const cx = Math.min(x, window.innerWidth - mw - 8);
    const cy = Math.min(y, window.innerHeight - mh - 8);
    menu.style.left = cx + 'px';
    menu.style.top  = cy + 'px';
  }

  function closeMenu() {
    menu.classList.remove('is-open');
  }

  zone.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    closeMenu();
    // small delay so scale origin resets
    requestAnimationFrame(() => openMenu(e.clientX, e.clientY));
  });

  document.addEventListener('click', function(e) {
    if (!menu.contains(e.target)) closeMenu();
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeMenu();
  });

  // item click closes menu
  menu.querySelectorAll('.dd-16__item').forEach(function(item) {
    item.addEventListener('click', closeMenu);
  });
})();
```
