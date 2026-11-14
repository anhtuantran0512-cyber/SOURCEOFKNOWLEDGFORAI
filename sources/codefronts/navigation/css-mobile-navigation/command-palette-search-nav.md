---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/command-palette-search-nav/"
title: "Command Palette Search Nav"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A Spotlight-style command palette triggered by a search bar click or a keyboard shortcut."
has_js: "true"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Command Palette Search Nav
Source: https://codefronts.com/navigation/css-mobile-navigation/command-palette-search-nav/

A Spotlight-style command palette triggered by a search bar click or a keyboard shortcut. Live-filters a command list by label and description, with group labels, keyboard shortcut badges, and an animated box entrance.
## HTML
```html
<div class="mn-15" id="mn-15-root">
  <div class="mn-15__trigger" id="mn-15-trigger">
    <span class="mn-15__trigger-icon">🔍</span>
    <span class="mn-15__trigger-text">Search or jump to...</span>
    <div class="mn-15__trigger-kbd"><kbd>⌘</kbd><kbd>K</kbd></div>
  </div>

  <div class="mn-15__palette" id="mn-15-palette">
    <div class="mn-15__palette-box">
      <div class="mn-15__input-row">
        <span class="mn-15__input-icon">🔍</span>
        <input class="mn-15__input" id="mn-15-input" placeholder="Search commands, pages, people...">
        <button class="mn-15__input-clear" id="mn-15-clear">✕</button>
      </div>
      <div class="mn-15__results" id="mn-15-results">
        <!-- Populated by JS -->
      </div>
      <div class="mn-15__palette-footer">
        <span><kbd>↑↓</kbd> Navigate</span>
        <span><kbd>↵</kbd> Open</span>
        <span><kbd>Esc</kbd> Close</span>
      </div>
    </div>
  </div>

  <div class="mn-15__page">
    <div class="mn-15__section-title">Quick Actions</div>
    <div class="mn-15__quick-actions">
      <div class="mn-15__action-card">
        <div class="icon">✍️</div>
        <h4>New Document</h4>
        <p>Create blank doc</p>
      </div>
      <div class="mn-15__action-card">
        <div class="icon">📅</div>
        <h4>Schedule</h4>
        <p>Add to calendar</p>
      </div>
      <div class="mn-15__action-card">
        <div class="icon">👥</div>
        <h4>Invite Team</h4>
        <p>Share workspace</p>
      </div>
      <div class="mn-15__action-card">
        <div class="icon">📊</div>
        <h4>Analytics</h4>
        <p>View insights</p>
      </div>
    </div>
    <div class="mn-15__section-title">Recently Visited</div>
    <div class="mn-15__recent-item">
      <div class="mn-15__recent-icon">📄</div>
      <div class="mn-15__recent-text"><h4>Product Roadmap</h4><p>Updated 10 min ago</p></div>
    </div>
    <div class="mn-15__recent-item">
      <div class="mn-15__recent-icon">💬</div>
      <div class="mn-15__recent-text"><h4>Design Review Thread</h4><p>Updated 1 hour ago</p></div>
    </div>
    <div class="mn-15__recent-item">
      <div class="mn-15__recent-icon">📋</div>
      <div class="mn-15__recent-text"><h4>Sprint Planning Board</h4><p>Updated yesterday</p></div>
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

.mn-15 {
  --bg: #111113;
  --surface: #1c1c1f;
  --surface2: #252528;
  --border: #2d2d32;
  --accent: #f97316;
  --text: #ececf1;
  --muted: #737379;
  --highlight: rgba(249,115,22,0.1);
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.8);
}
/* Search trigger button */

.mn-15__trigger {
  position: absolute;
  top: 20px;
  left: 16px;
  right: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px 14px;
  cursor: text;
  z-index: 5;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.mn-15__trigger:hover {
  border-color: rgba(249,115,22,0.4);
  box-shadow: 0 0 0 3px rgba(249,115,22,0.08);
}

.mn-15__trigger-icon {
  font-size: 16px;
  color: var(--muted);
}

.mn-15__trigger-text {
  flex: 1;
  color: var(--muted);
  font-size: 14px;
}

.mn-15__trigger-kbd {
  display: flex;
  gap: 4px;
}

.mn-15__trigger-kbd kbd {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 6px;
  font-size: 11px;
  color: var(--muted);
  font-family: inherit;
}
/* Command palette overlay */

.mn-15__palette {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.6);
  z-index: 20;
  display: flex;
  flex-direction: column;
  padding: 60px 16px 16px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}

.mn-15__palette.is-open {
  opacity: 1;
  pointer-events: all;
}

.mn-15__palette-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 24px 64px rgba(0,0,0,0.5);
  transform: scale(0.95) translateY(-8px);
  transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-15__palette.is-open .mn-15__palette-box {
  transform: scale(1) translateY(0);
}
/* Search input */

.mn-15__input-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--border);
}

.mn-15__input-icon {
  font-size: 18px;
  color: var(--muted);
}

.mn-15__input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 15px;
  color: var(--text);
  font-family: inherit;
}

.mn-15__input::placeholder {
  color: var(--muted);
}

.mn-15__input-clear {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--surface2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 10px;
  color: var(--muted);
  border: none;
  padding: 0;
  display: none;
}

.mn-15__input-clear.is-visible {
  display: flex;
}
/* Results */

.mn-15__results {
  max-height: 380px;
  overflow-y: auto;
}

.mn-15__group-label {
  padding: 8px 16px 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--muted);
}

.mn-15__result-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  cursor: pointer;
  transition: background 0.1s;
}

.mn-15__result-item:hover,
.mn-15__result-item.is-selected {
  background: var(--highlight);
}

.mn-15__result-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
  background: var(--surface2);
}

.mn-15__result-info {
  flex: 1;
}

.mn-15__result-info h4 {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
}

.mn-15__result-info p {
  font-size: 11px;
  color: var(--muted);
}

.mn-15__result-shortcut {
  font-size: 11px;
  color: var(--muted);
}

.mn-15__result-shortcut kbd {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
  font-family: inherit;
}

.mn-15__divider {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}
/* Palette footer */

.mn-15__palette-footer {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 8px 14px;
  border-top: 1px solid var(--border);
}

.mn-15__palette-footer span {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  color: var(--muted);
}

.mn-15__palette-footer kbd {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
  font-size: 10px;
  font-family: inherit;
}
/* Page content */

.mn-15__page {
  position: absolute;
  top: 72px;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 16px;
  overflow-y: auto;
}

.mn-15__section-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 12px;
}

.mn-15__quick-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 20px;
}

.mn-15__action-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px;
  cursor: pointer;
  transition: border-color 0.2s;
}

.mn-15__action-card:hover {
  border-color: var(--accent);
}

.mn-15__action-card .icon {
  font-size: 24px;
  margin-bottom: 8px;
}

.mn-15__action-card h4 {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 2px;
}

.mn-15__action-card p {
  font-size: 11px;
  color: var(--muted);
}

.mn-15__recent-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  cursor: pointer;
}

.mn-15__recent-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--surface);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}

.mn-15__recent-text h4 {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
}

.mn-15__recent-text p {
  font-size: 11px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .mn-15__palette,
    .mn-15__palette-box {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const trigger = document.getElementById('mn-15-trigger');
  const palette = document.getElementById('mn-15-palette');
  const input = document.getElementById('mn-15-input');
  const results = document.getElementById('mn-15-results');
  const clear = document.getElementById('mn-15-clear');
  const root = document.getElementById('mn-15-root');

  const COMMANDS = [
    { group: 'Pages', icon: '🏠', label: 'Dashboard', desc: 'Main workspace' },
    { group: 'Pages', icon: '📊', label: 'Analytics', desc: 'Traffic & conversions' },
    { group: 'Pages', icon: '👥', label: 'Team Members', desc: '12 members' },
    { group: 'Pages', icon: '⚙️', label: 'Settings', desc: 'Account & preferences' },
    { group: 'Actions', icon: '✍️', label: 'New Document', desc: 'Create blank page', shortcut: 'N' },
    { group: 'Actions', icon: '📤', label: 'Export', desc: 'Download as PDF', shortcut: 'E' },
    { group: 'Actions', icon: '🔗', label: 'Copy Link', desc: 'Share current page', shortcut: 'L' },
    { group: 'Actions', icon: '🎨', label: 'Change Theme', desc: 'Appearance settings' },
    { group: 'Recent', icon: '📄', label: 'Product Roadmap', desc: '10 min ago' },
    { group: 'Recent', icon: '💬', label: 'Design Review', desc: '1 hour ago' },
  ];

  function render(q) {
    const filtered = q ? COMMANDS.filter(c => c.label.toLowerCase().includes(q.toLowerCase()) || c.desc.toLowerCase().includes(q.toLowerCase())) : COMMANDS;
    if (!filtered.length) {
      results.innerHTML = `<div style="padding:24px 16px;text-align:center;color:var(--muted);font-size:13px">No results for "${q}"</div>`;
      return;
    }
    let html = '';
    let lastGroup = '';
    filtered.forEach(c => {
      if (c.group !== lastGroup) {
        if (lastGroup) html += '<div class="mn-15__divider"></div>';
        html += `<div class="mn-15__group-label">${c.group}</div>`;
        lastGroup = c.group;
      }
      html += `<div class="mn-15__result-item">
        <div class="mn-15__result-icon">${c.icon}</div>
        <div class="mn-15__result-info"><h4>${c.label}</h4><p>${c.desc}</p></div>
        ${c.shortcut ? `<div class="mn-15__result-shortcut"><kbd>${c.shortcut}</kbd></div>` : ''}
      </div>`;
    });
    results.innerHTML = html;
  }

  function open() { palette.classList.add('is-open'); setTimeout(() => input.focus(), 50); render(''); }
  function close() { palette.classList.remove('is-open'); input.value = ''; clear.classList.remove('is-visible'); }

  trigger.addEventListener('click', open);
  palette.addEventListener('click', e => { if (e.target === palette) close(); });

  input.addEventListener('input', () => {
    render(input.value);
    clear.classList.toggle('is-visible', input.value.length > 0);
  });

  clear.addEventListener('click', () => { input.value = ''; render(''); clear.classList.remove('is-visible'); input.focus(); });

  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); palette.classList.contains('is-open') ? close() : open(); }
    if (e.key === 'Escape') close();
  });

  render('');
})();
```
