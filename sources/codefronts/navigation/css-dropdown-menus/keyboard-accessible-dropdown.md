---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/keyboard-accessible-dropdown/"
title: "Keyboard Accessible Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A fully ARIA-compliant dropdown with keyboard navigation: arrow keys move focus between items, Escape closes the menu, and Enter activates links."
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Accessible Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/keyboard-accessible-dropdown/

A fully ARIA-compliant dropdown with keyboard navigation: arrow keys move focus between items, Escape closes the menu, and Enter activates links.
## HTML
```html
<div class="dd-17">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-17__scene">
    <div class="dd-17__hint-row">
      <span class="dd-17__badge">&#9654; Keyboard</span>
      <span class="dd-17__tip">Try: Enter, &#8593;&#8595;, Escape</span>
    </div>
    <div class="dd-17__wrap">
      <button
        class="dd-17__trigger"
        id="dd-17-btn"
        aria-haspopup="true"
        aria-expanded="false"
        aria-controls="dd-17-menu"
      >
        <span>My Account</span>
        <span class="dd-17__avatar">JD</span>
      </button>
      <ul
        class="dd-17__menu"
        id="dd-17-menu"
        role="menu"
        aria-labelledby="dd-17-btn"
        aria-hidden="true"
      >
        <li role="none"><a href="#" class="dd-17__item" role="menuitem" tabindex="-1">&#128100; Profile</a></li>
        <li role="none"><a href="#" class="dd-17__item" role="menuitem" tabindex="-1">&#9881; Settings</a></li>
        <li role="none"><a href="#" class="dd-17__item" role="menuitem" tabindex="-1">&#128178; Billing</a></li>
        <li role="none"><a href="#" class="dd-17__item" role="menuitem" tabindex="-1">&#127381; Upgrade</a></li>
        <li class="dd-17__sep" role="separator"></li>
        <li role="none"><a href="#" class="dd-17__item dd-17__item--danger" role="menuitem" tabindex="-1">&#128275; Sign Out</a></li>
      </ul>
    </div>
    <p class="dd-17__a11y-note">Fully ARIA-compliant — works with screen readers</p>
  </div>
</div>
```
## CSS
```css
.dd-17,
.dd-17 *,
.dd-17 *::before,
.dd-17 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-17 ::selection {
  background: #059669;
  color: #ecfdf5;
}

.dd-17 {
  --brand: #059669;
  --surface: #fff;
  --text: #111827;
  --muted: #6b7280;
  --border: #e5e7eb;
  --hover: #f0fdf4;
  --danger: #ef4444;
  font-family: 'Inter', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
  padding: 40px 20px;
}

.dd-17__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  position: relative;
  z-index: 100;
}

.dd-17__hint-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dd-17__badge {
  background: #d1fae5;
  color: var(--brand);
  font-size: 11px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 100px;
  letter-spacing: 0.04em;
}

.dd-17__tip {
  font-size: 12.5px;
  color: var(--muted);
}

.dd-17__wrap {
  position: relative;
}

.dd-17__trigger {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px 10px 18px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  box-shadow: 0 1px 4px rgba(0,0,0,.05);
  transition: box-shadow 0.15s, border-color 0.15s;
}

.dd-17__trigger:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,.10);
  border-color: #6ee7b7;
}

.dd-17__trigger:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}

.dd-17__trigger[aria-expanded="true"] {
  border-color: var(--brand);
  box-shadow: 0 0 0 3px rgba(5,150,105,.12);
}

.dd-17__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--brand);
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  letter-spacing: 0.04em;
}

.dd-17__menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  min-width: 200px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 12px 40px rgba(0,0,0,.12);
  padding: 6px;
  list-style: none;
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
  transform-origin: top right;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.24s cubic-bezier(0.16,1,0.3,1);
}

.dd-17__menu[aria-hidden="false"] {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.dd-17__item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  transition: background 0.12s, color 0.12s;
}

.dd-17__item:hover,
.dd-17__item:focus-visible {
  background: var(--hover);
  color: var(--brand);
  outline: none;
}

.dd-17__item--danger {
  color: var(--danger);
}

.dd-17__item--danger:hover,
.dd-17__item--danger:focus-visible {
  background: #fef2f2;
  color: var(--danger);
}

.dd-17__sep {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

.dd-17__a11y-note {
  font-size: 12px;
  color: var(--muted);
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .dd-17__menu {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const btn  = document.getElementById('dd-17-btn');
  const menu = document.getElementById('dd-17-menu');
  if (!btn || !menu) return;

  const getItems = () =>
    Array.from(menu.querySelectorAll('[role="menuitem"]'));

  function openMenu() {
    btn.setAttribute('aria-expanded', 'true');
    menu.setAttribute('aria-hidden', 'false');
    const items = getItems();
    if (items.length) items[0].focus();
  }

  function closeMenu(returnFocus) {
    btn.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-hidden', 'true');
    if (returnFocus) btn.focus();
  }

  function isOpen() {
    return btn.getAttribute('aria-expanded') === 'true';
  }

  btn.addEventListener('click', function() {
    isOpen() ? closeMenu(false) : openMenu();
  });

  menu.addEventListener('keydown', function(e) {
    const items = getItems();
    const idx   = items.indexOf(document.activeElement);

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      items[(idx + 1) % items.length].focus();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      items[(idx - 1 + items.length) % items.length].focus();
    } else if (e.key === 'Home') {
      e.preventDefault();
      items[0].focus();
    } else if (e.key === 'End') {
      e.preventDefault();
      items[items.length - 1].focus();
    } else if (e.key === 'Escape') {
      closeMenu(true);
    } else if (e.key === 'Tab') {
      closeMenu(false);
    }
  });

  btn.addEventListener('keydown', function(e) {
    if ((e.key === 'Enter' || e.key === ' ') && !isOpen()) {
      e.preventDefault();
      openMenu();
    } else if (e.key === 'Escape' && isOpen()) {
      closeMenu(false);
    }
  });

  document.addEventListener('mousedown', function(e) {
    if (!btn.contains(e.target) && !menu.contains(e.target)) {
      closeMenu(false);
    }
  });
})();
```
