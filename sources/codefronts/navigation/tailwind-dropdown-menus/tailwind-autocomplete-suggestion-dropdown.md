---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-autocomplete-suggestion-dropdown/"
title: "Tailwind Autocomplete Suggestion Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "Type three letters, get matching destinations."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Autocomplete Suggestion Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-autocomplete-suggestion-dropdown/

Type three letters, get matching destinations. The port's two lessons are focus-within: — the input ring belongs to the field wrapper, and Tailwind has a variant for exactly that — and the discipline of rendering suggestion rows from one class string the script holds, so a row's appearance is still declared in one place.
## HTML
```html
<section class="tdd-20 w-full min-h-svh grid place-items-center bg-linear-[160deg,var(--color-tdd20-bg1),var(--color-tdd20-bg2)] font-tdd20-sans text-tdd20-ink px-5 py-10" aria-label="Autocomplete suggestion dropdown demo">
  <div class="relative w-[min(380px,100%)] rounded-[20px] border border-tdd20-edge bg-white px-6 py-7 shadow-[0_8px_40px_oklch(0.68_0.15_233/0.15)]">
    <p class="mb-1 text-xl font-bold text-tdd20-ink">&#127758; Where to?</p>
    <p class="mb-4.5 text-[13px] text-tdd20-mut">Search for a destination</p>
    <div id="tdd20-field" class="flex items-center gap-2 rounded-xl border-2 border-tdd20-edge px-3.5 py-2.5 transition-[border-color,box-shadow] duration-200 focus-within:border-tdd20-acc focus-within:shadow-[0_0_0_4px_oklch(0.68_0.15_233/0.12)]">
      <span class="shrink-0 text-base text-tdd20-mut" aria-hidden="true">&#128269;</span>
      <input id="tdd20-input" type="text" role="combobox" aria-expanded="false" aria-controls="tdd20-list" aria-autocomplete="list" placeholder="Type a city or country&hellip;" autocomplete="off" class="min-h-6 flex-1 border-0 bg-transparent font-tdd20-sans text-[15px] font-medium text-tdd20-ink outline-none placeholder:font-normal placeholder:text-tdd20-place">
      <button type="button" id="tdd20-clear" aria-label="Clear" class="cursor-pointer border-0 bg-transparent text-lg leading-none text-tdd20-mut opacity-0 transition-opacity duration-150 hover:text-tdd20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd20-acc data-visible:opacity-100">&#215;</button>
    </div>
    <ul id="tdd20-list" role="listbox" aria-label="Suggestions" class="mt-1.5 max-h-0 list-none overflow-hidden rounded-xl border border-tdd20-edge bg-white opacity-0 shadow-[0_8px_24px_oklch(0_0_0/0.1)] transition-[max-height,opacity] duration-300 data-open:max-h-70 data-open:overflow-y-auto data-open:opacity-100 [&_strong]:font-bold [&_strong]:text-tdd20-acc motion-reduce:transition-none"></ul>
    <p id="tdd20-hint" class="mt-3 text-center text-xs text-tdd20-mut">Try: &ldquo;Tok&rdquo;, &ldquo;Par&rdquo;, &ldquo;Bar&rdquo;</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd20-bg1: #f0f9ff;
  --color-tdd20-bg1: oklch(0.98 0.02 230);
  --color-tdd20-bg2: #bae6fd;
  --color-tdd20-bg2: oklch(0.88 0.07 230);
  --color-tdd20-ink: #0f172a;
  --color-tdd20-ink: oklch(0.21 0.04 265);
  --color-tdd20-mut: #64748b;
  --color-tdd20-mut: oklch(0.55 0.03 255);
  --color-tdd20-place: #94a3b8;
  --color-tdd20-place: oklch(0.7 0.03 255);
  --color-tdd20-edge: #e2e8f0;
  --color-tdd20-edge: oklch(0.92 0.01 255);
  --color-tdd20-tint: #f0f9ff;
  --color-tdd20-tint: oklch(0.98 0.02 230);
  --color-tdd20-acc: #0ea5e9;
  --color-tdd20-acc: oklch(0.68 0.15 233);
  --font-tdd20-sans: 'DM Sans', system-ui, sans-serif;
}

.tdd-20 {
  width: 100%;
  min-height: 100svh;
}

.tdd-20 ::selection {
  background: var(--color-tdd20-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  var CITIES = [
    ['Tokyo', '🇯🇵'], ['Paris', '🇫🇷'], ['Barcelona', '🇪🇸'],
    ['Kyoto', '🇯🇵'], ['Nairobi', '🇰🇪'], ['Madrid', '🇪🇸'],
    ['New York', '🇺🇸'], ['Rio de Janeiro', '🇧🇷'], ['Sydney', '🇦🇺'],
    ['Rome', '🇮🇹'], ['Oslo', '🇳🇴'], ['Cairo', '🇪🇬'],
    ['Toronto', '🇨🇦'], ['Mexico City', '🇲🇽'], ['Lisbon', '🇵🇹'],
    ['Amsterdam', '🇳🇱'], ['Doha', '🇶🇦'], ['Shanghai', '🇨🇳'],
    ['Dublin', '🇮🇪'], ['Porto', '🇵🇹'], ['Singapore', '🇸🇬'],
    ['Berlin', '🇩🇪']
  ];
  // One class string = one place that describes a suggestion row.
  var ROW = 'flex min-h-11 cursor-pointer items-center gap-2.5 px-4 py-2.5 text-sm font-medium text-tdd20-ink transition-colors duration-150 hover:bg-tdd20-tint hover:text-tdd20-acc data-active:bg-tdd20-tint data-active:text-tdd20-acc';

  document.querySelectorAll('.tdd-20').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var input = root.querySelector('#tdd20-input'),
        list = root.querySelector('#tdd20-list'),
        clear = root.querySelector('#tdd20-clear'),
        hint = root.querySelector('#tdd20-hint'),
        field = root.querySelector('#tdd20-field');
    if (!input || !list) return;
    var active = -1;
    var items = function () { return Array.from(list.querySelectorAll('li[data-city]')); };

    function setOpen(open) {
      list.toggleAttribute('data-open', open);
      input.setAttribute('aria-expanded', String(open));
    }

    function choose(city) {
      input.value = city;
      setOpen(false);
      clear.toggleAttribute('data-visible', true);
      if (hint) hint.hidden = true;
    }

    function render(q) {
      q = q.trim().toLowerCase();
      list.textContent = '';
      active = -1;
      clear.toggleAttribute('data-visible', !!q);
      if (hint) hint.hidden = !!q;
      if (!q) { setOpen(false); return; }
      var hits = CITIES.filter(function (c) { return c[0].toLowerCase().indexOf(q) > -1; }).slice(0, 8);
      if (!hits.length) {
        var empty = document.createElement('li');
        empty.className = 'px-4 py-2.5 text-sm text-tdd20-place';
        empty.textContent = 'No destinations found';
        list.appendChild(empty);
      } else {
        hits.forEach(function (c) {
          var li = document.createElement('li');
          li.className = ROW;
          li.setAttribute('role', 'option');
          li.dataset.city = c[0];
          var flag = document.createElement('span');
          flag.textContent = c[1];
          var label = document.createElement('span');
          var i = c[0].toLowerCase().indexOf(q);
          label.append(c[0].slice(0, i));
          var s = document.createElement('strong');
          s.textContent = c[0].slice(i, i + q.length);
          label.append(s, c[0].slice(i + q.length));
          li.append(flag, label);
          li.addEventListener('mousedown', function () { choose(c[0]); });
          list.appendChild(li);
        });
      }
      setOpen(true);
    }

    input.addEventListener('input', function () { render(input.value); });
    input.addEventListener('keydown', function (e) {
      var list_ = items();
      if (!list_.length) return;
      if (e.key === 'ArrowDown') { e.preventDefault(); active = (active + 1) % list_.length; }
      else if (e.key === 'ArrowUp') { e.preventDefault(); active = (active - 1 + list_.length) % list_.length; }
      else if (e.key === 'Enter' && active > -1) { e.preventDefault(); choose(list_[active].dataset.city); return; }
      else if (e.key === 'Escape') { setOpen(false); return; }
      list_.forEach(function (li, i) { li.toggleAttribute('data-active', i === active); });
    });
    clear.addEventListener('click', function () { input.value = ''; render(''); input.focus(); });
    document.addEventListener('click', function (e) {
      if (!field.contains(e.target) && !list.contains(e.target)) setOpen(false);
    });
  });
})();
```
