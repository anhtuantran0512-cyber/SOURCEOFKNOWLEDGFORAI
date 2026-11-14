---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/custom-animated-select-dropdown/"
title: "Custom Animated Select Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A fully custom replacement for the native HTML select element, with animated option reveal, keyboard support, and a value display that updates on selection."
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Animated Select Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/custom-animated-select-dropdown/

A fully custom replacement for the native HTML select element, with animated option reveal, keyboard support, and a value display that updates on selection.
## HTML
```html
<div class="dd-22">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <div class="dd-22__card">
    <p class="dd-22__title">Choose your plan</p>
    <p class="dd-22__sub">Select the option that fits your needs</p>

    <!-- native select (hidden, for form) -->
    <select id="dd-22-native" aria-hidden="true" tabindex="-1" style="position:absolute;opacity:0;pointer-events:none;width:0;height:0">
      <option value="">Select a plan…</option>
      <option value="free">Free — $0/month</option>
      <option value="pro">Pro — $12/month</option>
      <option value="team">Team — $39/month</option>
      <option value="enterprise">Enterprise — Custom</option>
    </select>

    <!-- custom select -->
    <div class="dd-22__select" id="dd-22-select">
      <button
        class="dd-22__btn"
        id="dd-22-btn"
        aria-haspopup="listbox"
        aria-expanded="false"
        aria-labelledby="dd-22-val"
      >
        <span class="dd-22__val" id="dd-22-val">Select a plan…</span>
        <span class="dd-22__chevron" id="dd-22-chevron">▾</span>
      </button>
      <ul
        class="dd-22__list"
        id="dd-22-list"
        role="listbox"
        aria-label="Plan options"
      >
        <li class="dd-22__opt" role="option" aria-selected="false" data-value="free">
          <span class="dd-22__opt-name">&#127381; Free</span>
          <span class="dd-22__opt-price">$0/month</span>
        </li>
        <li class="dd-22__opt" role="option" aria-selected="false" data-value="pro">
          <span class="dd-22__opt-name">&#128640; Pro</span>
          <span class="dd-22__opt-price">$12/month</span>
        </li>
        <li class="dd-22__opt" role="option" aria-selected="false" data-value="team">
          <span class="dd-22__opt-name">&#128101; Team</span>
          <span class="dd-22__opt-price">$39/month</span>
        </li>
        <li class="dd-22__opt dd-22__opt--featured" role="option" aria-selected="false" data-value="enterprise">
          <span class="dd-22__opt-name">&#127959; Enterprise</span>
          <span class="dd-22__opt-price">Custom</span>
        </li>
      </ul>
    </div>

    <button class="dd-22__submit" id="dd-22-submit">Continue &#8594;</button>
    <p class="dd-22__status" id="dd-22-status">No plan selected</p>
  </div>
</div>
```
## CSS
```css
.dd-22,
.dd-22 *,
.dd-22 *::before,
.dd-22 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-22 ::selection {
  background: #f59e0b;
  color: #fff;
}

.dd-22 {
  --brand: #f59e0b;
  --brand-dark: #d97706;
  --surface: #fff;
  --text: #1c1917;
  --muted: #78716c;
  --border: #e7e5e4;
  --hover: #fffbeb;
  --selected: #fef3c7;
  font-family: 'Inter', sans-serif;
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 60%, #fde68a 100%);
  padding: 40px 20px;
}

.dd-22__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 24px;
  width: 100%;
  max-width: 360px;
  box-shadow: 0 8px 40px rgba(245,158,11,.15);
  display: flex;
  flex-direction: column;
  gap: 12px;
  position: relative;
}

.dd-22__title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.3px;
}

.dd-22__sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: -8px;
}
/* custom select wrapper */

.dd-22__select {
  position: relative;
  z-index: 100;
}

.dd-22__btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 12px 16px;
  background: var(--surface);
  border: 2px solid var(--border);
  border-radius: 12px;
  cursor: pointer;
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 500;
  color: var(--muted);
  text-align: left;
  transition: border-color 0.18s, box-shadow 0.18s;
}

.dd-22__btn:hover {
  border-color: var(--brand);
}

.dd-22__btn[aria-expanded="true"] {
  border-color: var(--brand);
  box-shadow: 0 0 0 4px rgba(245,158,11,.14);
  color: var(--text);
}

.dd-22__btn.has-value {
  color: var(--text);
  font-weight: 600;
}

.dd-22__chevron {
  font-size: 14px;
  color: var(--muted);
  display: inline-block;
  transition: transform 0.28s cubic-bezier(0.34, 1.56, 0.64, 1);
  flex-shrink: 0;
}

.dd-22__btn[aria-expanded="true"] .dd-22__chevron {
  transform: rotate(180deg);
}
/* option list */

.dd-22__list {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: 0 12px 40px rgba(245,158,11,.18), 0 2px 8px rgba(0,0,0,.06);
  list-style: none;
  padding: 6px;
  transform: scaleY(0);
  transform-origin: top center;
  opacity: 0;
  pointer-events: none;
  transition: transform 0.38s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.2s ease;
}

.dd-22__list.is-open {
  transform: scaleY(1);
  opacity: 1;
  pointer-events: auto;
}
/* stagger options */

.dd-22__opt {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 11px 14px;
  border-radius: 9px;
  cursor: pointer;
  opacity: 0;
  transform: translateY(4px);
  transition: opacity 0.28s ease, transform 0.28s ease, background 0.12s;
}

.dd-22__list.is-open .dd-22__opt {
  opacity: 1;
  transform: translateY(0);
}

.dd-22__list.is-open .dd-22__opt:nth-child(1) {
  transition-delay: 0.04s;
}

.dd-22__list.is-open .dd-22__opt:nth-child(2) {
  transition-delay: 0.09s;
}

.dd-22__list.is-open .dd-22__opt:nth-child(3) {
  transition-delay: 0.14s;
}

.dd-22__list.is-open .dd-22__opt:nth-child(4) {
  transition-delay: 0.19s;
}

.dd-22__opt:hover {
  background: var(--hover);
}

.dd-22__opt.is-selected {
  background: var(--selected);
}

.dd-22__opt.is-highlighted {
  background: var(--hover);
  outline: 2px solid var(--brand);
  outline-offset: -2px;
}

.dd-22__opt--featured {
  border: 1px dashed var(--brand);
  margin-top: 4px;
}

.dd-22__opt--featured:hover {
  background: var(--selected);
}

.dd-22__opt-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 8px;
}

.dd-22__opt-price {
  font-size: 12.5px;
  font-weight: 500;
  color: var(--muted);
}
/* selected tick */

.dd-22__opt.is-selected .dd-22__opt-name::after {
  content: '✓';
  color: var(--brand);
  font-size: 13px;
  font-weight: 700;
}
/* submit button */

.dd-22__submit {
  width: 100%;
  padding: 12px;
  background: var(--brand);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, transform 0.15s;
  margin-top: 4px;
}

.dd-22__submit:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.dd-22__submit:active {
  transform: translateY(0);
}

.dd-22__status {
  text-align: center;
  font-size: 12.5px;
  color: var(--muted);
  font-style: italic;
  min-height: 18px;
}

@media (prefers-reduced-motion: reduce) {
  .dd-22__list,
    .dd-22__opt,
    .dd-22__chevron,
    .dd-22__submit {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const btn      = document.getElementById('dd-22-btn');
  const list     = document.getElementById('dd-22-list');
  const valSpan  = document.getElementById('dd-22-val');
  const native   = document.getElementById('dd-22-native');
  const submitBtn = document.getElementById('dd-22-submit');
  const status   = document.getElementById('dd-22-status');
  if (!btn || !list || !native) return;

  const opts = Array.from(list.querySelectorAll('.dd-22__opt'));
  let activeIdx = -1;

  /* ── open / close ── */
  function openList() {
    list.classList.add('is-open');
    btn.setAttribute('aria-expanded', 'true');
    // highlight currently selected
    const selIdx = opts.findIndex(function(o) { return o.classList.contains('is-selected'); });
    setHighlight(selIdx > -1 ? selIdx : 0);
  }

  function closeList() {
    list.classList.remove('is-open');
    btn.setAttribute('aria-expanded', 'false');
    activeIdx = -1;
    opts.forEach(function(o) { o.classList.remove('is-highlighted'); });
  }

  function isOpen() { return list.classList.contains('is-open'); }

  /* ── highlight (keyboard focus) ── */
  function setHighlight(idx) {
    opts.forEach(function(o) { o.classList.remove('is-highlighted'); });
    if (idx < 0 || idx >= opts.length) return;
    opts[idx].classList.add('is-highlighted');
    opts[idx].scrollIntoView({ block: 'nearest' });
    activeIdx = idx;
  }

  /* ── select option ── */
  function selectOpt(opt) {
    opts.forEach(function(o) {
      o.classList.remove('is-selected');
      o.setAttribute('aria-selected', 'false');
    });
    opt.classList.add('is-selected');
    opt.setAttribute('aria-selected', 'true');

    const value = opt.dataset.value;
    const name  = opt.querySelector('.dd-22__opt-name').textContent.trim();
    const price = opt.querySelector('.dd-22__opt-price').textContent.trim();

    valSpan.textContent = name + ' — ' + price;
    btn.classList.add('has-value');
    native.value = value;
    native.dispatchEvent(new Event('change', { bubbles: true }));
    status.textContent = 'Selected: ' + name + ' (' + price + ')';
    closeList();
    btn.focus();
  }

  /* ── events ── */
  btn.addEventListener('click', function(e) {
    e.stopPropagation();
    isOpen() ? closeList() : openList();
  });

  opts.forEach(function(opt, i) {
    opt.addEventListener('click', function() { selectOpt(opt); });
    opt.addEventListener('mousemove', function() { setHighlight(i); });
  });

  btn.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      if (!isOpen()) openList();
    }
  });

  list.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setHighlight((activeIdx + 1) % opts.length);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setHighlight((activeIdx - 1 + opts.length) % opts.length);
    } else if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      if (activeIdx > -1) selectOpt(opts[activeIdx]);
    } else if (e.key === 'Escape' || e.key === 'Tab') {
      closeList();
      btn.focus();
    }
  });

  // make list focusable for keyboard relay
  list.setAttribute('tabindex', '-1');
  btn.addEventListener('keydown', function(e) {
    if (isOpen() && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
      e.preventDefault();
      list.focus();
      setHighlight(e.key === 'ArrowDown' ? 0 : opts.length - 1);
    }
  });

  document.addEventListener('click', function(e) {
    if (!btn.contains(e.target) && !list.contains(e.target)) closeList();
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && isOpen()) { closeList(); btn.focus(); }
  });

  submitBtn && submitBtn.addEventListener('click', function() {
    if (!native.value) {
      status.textContent = '⚠ Please select a plan first.';
      btn.style.borderColor = '#ef4444';
      setTimeout(function() { btn.style.borderColor = ''; }, 1500);
    } else {
      status.textContent = '✓ Proceeding with ' + valSpan.textContent;
    }
  });
})();
```
