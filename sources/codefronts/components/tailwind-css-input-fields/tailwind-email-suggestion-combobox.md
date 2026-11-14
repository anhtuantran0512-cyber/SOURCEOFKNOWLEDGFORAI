---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-email-suggestion-combobox/"
title: "Tailwind Email Suggestion Combobox"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Type @ and the common domains appear in a keyboard-navigable listbox."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Email Suggestion Combobox
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-email-suggestion-combobox/

Type @ and the common domains appear in a keyboard-navigable listbox. A full ARIA combobox — aria-expanded, aria-controls, aria-activedescendant, role="option" — with the selected row styled by aria-selected: rather than a class.
## HTML
```html
<div class="tif-21 grid min-h-svh w-full place-items-center bg-tif21-bg px-6 pt-14 pb-40 font-tif21-sans" aria-label="Email suggestion combobox demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif21-mono text-[10px] tracking-[0.12em] text-tif21-mut uppercase">Work email</span>
    <span class="relative block">
      <input id="tif21-input" type="email" name="tif21-email" autocomplete="email" placeholder="[email protected]"
        role="combobox" aria-controls="tif21-list" aria-expanded="false" aria-autocomplete="list"
        class="w-full rounded-[10px] border border-white/12 bg-tif21-field px-3.5 py-3 text-sm font-medium text-tif21-ink outline-none transition-[border-color,border-radius] duration-150 placeholder:text-tif21-mut focus:border-tif21-acc aria-expanded:rounded-b-none aria-expanded:border-b-transparent">
      <ul id="tif21-list" role="listbox" aria-label="Email domain suggestions" hidden
        class="absolute inset-x-0 top-full z-10 m-0 max-h-45 list-none overflow-y-auto rounded-b-[10px] border border-t-0 border-tif21-acc bg-tif21-field p-1"></ul>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif21-bg: #12121a;
  --color-tif21-bg: oklch(0.19 0.015 285);
  --color-tif21-field: #1a1a22;
  --color-tif21-field: oklch(0.23 0.015 285);
  --color-tif21-ink: #f0eeff;
  --color-tif21-ink: oklch(0.95 0.02 290);
  --color-tif21-mut: #b8b6d4;
  --color-tif21-mut: oklch(0.77 0.03 290);
  --color-tif21-acc: #2eb88a;
  --color-tif21-acc: oklch(0.7 0.13 165);
  --font-tif21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif21-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-21 {
  width: 100%;
}

.tif-21 ::selection {
  background: var(--color-tif21-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  var DOMAINS = ['gmail.com', 'outlook.com', 'icloud.com', 'proton.me', 'fastmail.com'];
  var OPTION = 'cursor-pointer rounded-md px-2.5 py-1.5 text-[13px] font-medium text-tif21-ink/80 ' +
    'hover:bg-tif21-acc/15 hover:text-white aria-selected:bg-tif21-acc/15 aria-selected:text-white';

  document.querySelectorAll('.tif-21').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var input = root.querySelector('#tif21-input');
    var list = root.querySelector('#tif21-list');
    if (!input || !list) return;
    var idx = -1;

    function close() {
      list.hidden = true;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      idx = -1;
    }
    function open(local) {
      list.textContent = '';
      DOMAINS.forEach(function (d, n) {
        if ((input.value || '').toLowerCase().indexOf('@' + d) > -1) return;
        var li = document.createElement('li');
        li.id = 'tif21-opt-' + n;
        li.setAttribute('role', 'option');
        li.className = OPTION;
        li.dataset.value = local + d;
        li.append(document.createTextNode(local));
        var b = document.createElement('b');
        b.className = 'font-semibold text-tif21-acc';
        b.textContent = d;
        li.appendChild(b);
        list.appendChild(li);
      });
      if (!list.children.length) return close();
      list.hidden = false;
      input.setAttribute('aria-expanded', 'true');
    }
    function select(n) {
      var items = list.querySelectorAll('li');
      if (!items.length) return;
      items.forEach(function (li) { li.removeAttribute('aria-selected'); });
      idx = (n + items.length) % items.length;
      items[idx].setAttribute('aria-selected', 'true');
      input.setAttribute('aria-activedescendant', items[idx].id);
    }
    function commit(li) {
      input.value = li.dataset.value;
      close();
      input.focus();
    }

    input.addEventListener('input', function () {
      var at = input.value.indexOf('@');
      if (at >= 0) open(input.value.slice(0, at + 1)); else close();
    });
    input.addEventListener('blur', function () { setTimeout(close, 0); });
    input.addEventListener('keydown', function (e) {
      if (list.hidden) return;
      var items = list.querySelectorAll('li');
      if (e.key === 'ArrowDown') { e.preventDefault(); select(idx + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); select(idx - 1); }
      else if (e.key === 'Escape') { close(); }
      else if (e.key === 'Enter' && idx >= 0) { e.preventDefault(); commit(items[idx]); }
    });
    list.addEventListener('mousedown', function (e) {
      var li = e.target.closest('li[role="option"]');
      if (li) { e.preventDefault(); commit(li); }
    });
  });
})();
```
