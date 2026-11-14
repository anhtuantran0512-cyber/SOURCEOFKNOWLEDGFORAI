---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/autocomplete-suggestion-dropdown/"
title: "Autocomplete Suggestion Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A live autocomplete input that filters a dataset and shows a suggestion dropdown as you type, with keyboard selection and highlighted match prefix."
has_js: "true"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Autocomplete Suggestion Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/autocomplete-suggestion-dropdown/

A live autocomplete input that filters a dataset and shows a suggestion dropdown as you type, with keyboard selection and highlighted match prefix.
## HTML
```html
<div class="dd-20">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-20__card">
    <p class="dd-20__title">&#127758; Where to?</p>
    <p class="dd-20__sub">Search for a destination</p>
    <div class="dd-20__field" id="dd-20-field">
      <span class="dd-20__field-icon">&#128269;</span>
      <input class="dd-20__input" id="dd-20-input" type="text" placeholder="Type a city or country…" autocomplete="off">
      <button class="dd-20__clear" id="dd-20-clear" aria-label="Clear">&#215;</button>
    </div>
    <ul class="dd-20__list" id="dd-20-list" role="listbox"></ul>
    <p class="dd-20__hint" id="dd-20-hint">Try: "Tok", "Par", "Bar"</p>
  </div>
</div>
```
## CSS
```css
.dd-20,
.dd-20 *,
.dd-20 *::before,
.dd-20 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-20 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.dd-20 {
  --brand: #0ea5e9;
  --surface: #fff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --hover: #f0f9ff;
  font-family: 'DM Sans', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg, #f0f9ff 0%, #bae6fd 100%);
  padding: 40px 20px;
}

.dd-20__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 24px;
  width: 100%;
  max-width: 380px;
  box-shadow: 0 8px 40px rgba(14,165,233,.15);
  position: relative;
}

.dd-20__title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.dd-20__sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 18px;
}

.dd-20__field {
  display: flex;
  align-items: center;
  gap: 8px;
  border: 2px solid var(--border);
  border-radius: 12px;
  padding: 10px 14px;
  transition: border-color 0.18s, box-shadow 0.18s;
}

.dd-20__field:focus-within {
  border-color: var(--brand);
  box-shadow: 0 0 0 4px rgba(14,165,233,.12);
}

.dd-20__field-icon {
  font-size: 16px;
  color: var(--muted);
  flex-shrink: 0;
}

.dd-20__input {
  flex: 1;
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
  background: transparent;
}

.dd-20__input::placeholder {
  color: #94a3b8;
  font-weight: 400;
}

.dd-20__clear {
  background: none;
  border: none;
  font-size: 18px;
  color: var(--muted);
  cursor: pointer;
  line-height: 1;
  opacity: 0;
  transition: opacity 0.15s;
}

.dd-20__clear.is-visible {
  opacity: 1;
}

.dd-20__clear:hover {
  color: var(--text);
}

.dd-20__list {
  list-style: none;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  max-height: 0;
  opacity: 0;
  margin-top: 6px;
  box-shadow: 0 8px 24px rgba(0,0,0,.10);
  transition: max-height 0.3s ease, opacity 0.2s ease;
}

.dd-20__list.is-open {
  max-height: 280px;
  opacity: 1;
  overflow-y: auto;
}

.dd-20__list li {
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: background 0.12s;
}

.dd-20__list li:hover,
.dd-20__list li.is-active {
  background: var(--hover);
  color: var(--brand);
}

.dd-20__list li strong {
  color: var(--brand);
  font-weight: 700;
}

.dd-20__hint {
  margin-top: 12px;
  font-size: 12px;
  color: var(--muted);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .dd-20__list,
    .dd-20__field {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  var data = [
    'Tokyo','Paris','Barcelona','Kyoto','Nairobi','Madrid',
    'New York','Rio de Janeiro','Sydney','Rome','Oslo','Cairo',
    'Toronto','Mexico City','Lisbon','Amsterdam','Doha','Shanghai',
    'Dublin','Bergen','Porto','Nicosia','Singapore','Berlin'
  ];
  var flags = ['&#127470;&#127481;','&#127467;&#127479;','&#127463;&#127462;','&#127472;&#127486;','&#127472;&#127466;','&#127466;&#127480;',
    '&#127482;&#127480;','&#127463;&#127479;','&#127462;&#127482;','&#127470;&#127481;','&#127475;&#127476;','&#127466;&#127468;',
    '&#127464;&#127462;','&#127474;&#127485;','&#127477;&#127481;','&#127475;&#127473;','&#127478;&#127462;','&#127464;&#127475;',
    '&#127470;&#127466;','&#127475;&#127476;','&#127477;&#127481;','&#127464;&#127486;','&#127480;&#127468;','&#127465;&#127466;'];

  var input    = document.getElementById('dd-20-input');
  var list     = document.getElementById('dd-20-list');
  var clearBtn = document.getElementById('dd-20-clear');
  var hint     = document.getElementById('dd-20-hint');
  if (!input || !list) return;
  var activeIdx = -1;

  function getItems() { return Array.from(list.querySelectorAll('li[data-idx]')); }

  function render(query) {
    var q = query.trim().toLowerCase();
    list.innerHTML = '';
    activeIdx = -1;
    if (!q) {
      list.classList.remove('is-open');
      hint && (hint.style.display = '');
      clearBtn.classList.remove('is-visible');
      return;
    }
    clearBtn.classList.add('is-visible');
    if (hint) hint.style.display = 'none';
    var matched = data.filter(function(d) { return d.toLowerCase().includes(q); });
    if (!matched.length) {
      var li = document.createElement('li');
      li.style.color = '#94a3b8'; li.style.cursor = 'default';
      li.textContent = 'No destinations found';
      list.appendChild(li);
    } else {
      matched.slice(0, 8).forEach(function(city) {
        var li = document.createElement('li');
        var origIdx = data.indexOf(city);
        var flag = flags[origIdx] || '&#127758;';
        var lc = city.toLowerCase();
        var start = lc.indexOf(q);
        var highlighted = start > -1
          ? city.slice(0, start) + '<strong>' + city.slice(start, start + q.length) + '</strong>' + city.slice(start + q.length)
          : city;
        li.innerHTML = '<span>' + flag + '</span><span>' + highlighted + '</span>';
        li.dataset.idx = origIdx;
        li.addEventListener('mousedown', function() {
          input.value = city;
          list.classList.remove('is-open');
          clearBtn.classList.add('is-visible');
          if (hint) hint.style.display = 'none';
        });
        list.appendChild(li);
      });
    }
    list.classList.add('is-open');
  }

  input.addEventListener('input', function() { render(input.value); });
  input.addEventListener('keydown', function(e) {
    var items = getItems();
    if (e.key === 'ArrowDown') { e.preventDefault(); activeIdx = (activeIdx + 1) % items.length; }
    else if (e.key === 'ArrowUp') { e.preventDefault(); activeIdx = (activeIdx - 1 + items.length) % items.length; }
    else if (e.key === 'Enter' && activeIdx > -1) { items[activeIdx].dispatchEvent(new Event('mousedown')); return; }
    else if (e.key === 'Escape') { list.classList.remove('is-open'); return; }
    items.forEach(function(li, i) { li.classList.toggle('is-active', i === activeIdx); });
  });
  clearBtn.addEventListener('click', function() { input.value = ''; render(''); input.focus(); });
  document.addEventListener('click', function(e) {
    if (!e.target.closest('#dd-20-field') && !list.contains(e.target)) list.classList.remove('is-open');
  });
})();
```
