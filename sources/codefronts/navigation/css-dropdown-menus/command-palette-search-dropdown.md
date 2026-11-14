---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/command-palette-search-dropdown/"
title: "Command Palette Search Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A Spotlight/Linear-style command palette that filters a list of commands in real time as you type, with keyboard navigation and highlighted match text."
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Command Palette Search Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/command-palette-search-dropdown/

A Spotlight/Linear-style command palette that filters a list of commands in real time as you type, with keyboard navigation and highlighted match text.
## HTML
```html
<div class="dd-19">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-19__scene">
    <button class="dd-19__open-btn" id="dd-19-open">
      <span>&#128269;</span> Search commands
      <kbd class="dd-19__kbd">&#8984;K</kbd>
    </button>
    <div class="dd-19__backdrop" id="dd-19-backdrop"></div>
    <div class="dd-19__palette" id="dd-19-palette" role="dialog" aria-modal="true" aria-label="Command palette">
      <div class="dd-19__search-row">
        <span class="dd-19__search-icon">&#128269;</span>
        <input class="dd-19__input" id="dd-19-input" type="text" placeholder="Search commands…" autocomplete="off">
        <button class="dd-19__esc-btn" id="dd-19-close">ESC</button>
      </div>
      <ul class="dd-19__list" id="dd-19-list" role="listbox">
        <li class="dd-19__group-label">Quick Actions</li>
        <li class="dd-19__cmd" data-label="New Document" role="option"><span class="dd-19__ci">&#128196;</span><span class="dd-19__ct">New Document</span><kbd class="dd-19__kbd">&#8984;N</kbd></li>
        <li class="dd-19__cmd" data-label="Open File" role="option"><span class="dd-19__ci">&#128193;</span><span class="dd-19__ct">Open File</span><kbd class="dd-19__kbd">&#8984;O</kbd></li>
        <li class="dd-19__cmd" data-label="Save Project" role="option"><span class="dd-19__ci">&#128190;</span><span class="dd-19__ct">Save Project</span><kbd class="dd-19__kbd">&#8984;S</kbd></li>
        <li class="dd-19__group-label">Navigation</li>
        <li class="dd-19__cmd" data-label="Go to Dashboard" role="option"><span class="dd-19__ci">&#127968;</span><span class="dd-19__ct">Go to Dashboard</span></li>
        <li class="dd-19__cmd" data-label="Go to Settings" role="option"><span class="dd-19__ci">&#9881;</span><span class="dd-19__ct">Go to Settings</span></li>
        <li class="dd-19__cmd" data-label="Go to Analytics" role="option"><span class="dd-19__ci">&#128202;</span><span class="dd-19__ct">Go to Analytics</span></li>
        <li class="dd-19__group-label">Theme</li>
        <li class="dd-19__cmd" data-label="Toggle Dark Mode" role="option"><span class="dd-19__ci">&#127769;</span><span class="dd-19__ct">Toggle Dark Mode</span></li>
        <li class="dd-19__cmd" data-label="Toggle Compact View" role="option"><span class="dd-19__ci">&#128262;</span><span class="dd-19__ct">Toggle Compact View</span></li>
      </ul>
      <div class="dd-19__footer">
        <span>&#8593;&#8595; navigate</span>
        <span>&#9166; select</span>
        <span>esc close</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dd-19,
.dd-19 *,
.dd-19 *::before,
.dd-19 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-19 ::selection {
  background: #6366f1;
  color: #fff;
}

.dd-19 {
  --brand: #6366f1;
  --surface: #fff;
  --text: #111827;
  --muted: #6b7280;
  --border: #e5e7eb;
  --hover: #f5f3ff;
  font-family: 'Inter', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%);
  padding: 40px 20px;
  position: relative;
}

.dd-19__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
  max-width: 520px;
  position: relative;
}

.dd-19__open-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  color: var(--muted);
  box-shadow: 0 2px 8px rgba(0,0,0,.06);
  transition: box-shadow 0.15s, border-color 0.15s;
}

.dd-19__open-btn:hover {
  box-shadow: 0 4px 16px rgba(99,102,241,.15);
  border-color: #c7d2fe;
  color: var(--text);
}

.dd-19__kbd {
  background: #f3f4f6;
  border: 1px solid var(--border);
  border-radius: 5px;
  padding: 2px 6px;
  font-size: 11px;
  font-family: inherit;
  color: var(--muted);
  margin-left: 4px;
}

.dd-19__backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.35);
  backdrop-filter: blur(2px);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
}

.dd-19__backdrop.is-open {
  opacity: 1;
  pointer-events: auto;
}

.dd-19__palette {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.95);
  width: min(520px, 90vw);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  box-shadow: 0 24px 80px rgba(0,0,0,.25);
  z-index: 201;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.24s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}

.dd-19__palette.is-open {
  opacity: 1;
  pointer-events: auto;
  transform: translate(-50%, -50%) scale(1);
}

.dd-19__search-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--border);
}

.dd-19__search-icon {
  font-size: 16px;
  color: var(--muted);
  flex-shrink: 0;
}

.dd-19__input {
  flex: 1;
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
  background: transparent;
}

.dd-19__input::placeholder {
  color: var(--muted);
  font-weight: 400;
}

.dd-19__esc-btn {
  background: #f3f4f6;
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 3px 8px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  color: var(--muted);
  font-family: inherit;
  transition: background 0.12s;
}

.dd-19__esc-btn:hover {
  background: #e5e7eb;
}

.dd-19__list {
  list-style: none;
  max-height: 260px;
  overflow-y: auto;
  padding: 6px;
}

.dd-19__group-label {
  padding: 8px 12px 4px;
  font-size: 10.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}

.dd-19__cmd {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.1s;
}

.dd-19__cmd:hover,
.dd-19__cmd.is-focused {
  background: var(--hover);
}

.dd-19__ci {
  font-size: 15px;
  width: 20px;
  text-align: center;
  flex-shrink: 0;
}

.dd-19__ct {
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  flex: 1;
}

.dd-19__ct mark {
  background: #c7d2fe;
  color: var(--brand);
  border-radius: 2px;
  font-weight: 700;
}

.dd-19__footer {
  display: flex;
  gap: 16px;
  padding: 10px 16px;
  border-top: 1px solid var(--border);
  background: #fafafa;
  font-size: 11px;
  color: var(--muted);
  font-weight: 500;
}

@media (prefers-reduced-motion: reduce) {
  .dd-19__palette,
    .dd-19__backdrop {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  var openBtn  = document.getElementById('dd-19-open');
  var closeBtn = document.getElementById('dd-19-close');
  var palette  = document.getElementById('dd-19-palette');
  var backdrop = document.getElementById('dd-19-backdrop');
  var input    = document.getElementById('dd-19-input');
  var list     = document.getElementById('dd-19-list');
  if (!openBtn || !palette) return;

  function getCmds() {
    return Array.from(list.querySelectorAll('.dd-19__cmd')).filter(function(el) {
      return el.style.display !== 'none';
    });
  }

  function openPalette() {
    palette.classList.add('is-open');
    backdrop.classList.add('is-open');
    setTimeout(function() { input.focus(); }, 50);
  }

  function closePalette() {
    palette.classList.remove('is-open');
    backdrop.classList.remove('is-open');
    input.value = '';
    filterCmds('');
  }

  function filterCmds(query) {
    var q = query.toLowerCase().trim();
    list.querySelectorAll('.dd-19__cmd').forEach(function(cmd) {
      var label = cmd.dataset.label || '';
      var ct = cmd.querySelector('.dd-19__ct');
      cmd.classList.remove('is-focused');
      if (!q) { cmd.style.display = ''; if (ct) ct.textContent = label; return; }
      if (label.toLowerCase().includes(q)) {
        cmd.style.display = '';
        if (ct) {
          var idx = label.toLowerCase().indexOf(q);
          ct.innerHTML = label.slice(0, idx) + '<mark>' + label.slice(idx, idx + q.length) + '</mark>' + label.slice(idx + q.length);
        }
      } else { cmd.style.display = 'none'; }
    });
    var visible = getCmds();
    if (visible.length) visible[0].classList.add('is-focused');
  }

  openBtn.addEventListener('click', openPalette);
  closeBtn.addEventListener('click', closePalette);
  backdrop.addEventListener('click', closePalette);
  input.addEventListener('input', function() { filterCmds(input.value); });

  document.addEventListener('keydown', function(e) {
    if (!palette.classList.contains('is-open')) return;
    var cmds = getCmds();
    var focused = list.querySelector('.dd-19__cmd.is-focused');
    var idx = focused ? cmds.indexOf(focused) : -1;
    if (e.key === 'Escape') { closePalette(); }
    else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (cmds.length) { cmds.forEach(function(c) { c.classList.remove('is-focused'); }); cmds[(idx + 1) % cmds.length].classList.add('is-focused'); }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (cmds.length) { cmds.forEach(function(c) { c.classList.remove('is-focused'); }); cmds[(idx - 1 + cmds.length) % cmds.length].classList.add('is-focused'); }
    } else if (e.key === 'Enter' && focused) { closePalette(); }
  });
})();
```
