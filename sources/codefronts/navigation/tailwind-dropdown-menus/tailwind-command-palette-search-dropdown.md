---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-command-palette-search-dropdown/"
title: "Tailwind Command Palette Search Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A Spotlight-style palette that filters as you type."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Command Palette Search Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-command-palette-search-dropdown/

A Spotlight-style palette that filters as you type. The port keeps every visual state in the markup — backdrop, scale-in, focused row — and leaves the script doing what only a script can: matching text, wrapping the hit in <mark>, and moving a data-active attribute down the list.
## HTML
```html
<section class="tdd-19 group/scene relative w-full min-h-svh grid place-items-center bg-linear-[135deg,var(--color-tdd19-bg1),var(--color-tdd19-bg2)] font-tdd19-sans text-tdd19-ink px-5 py-10" aria-label="Command palette dropdown demo">
  <button type="button" id="tdd19-open" class="flex min-h-11 cursor-pointer items-center gap-2 rounded-[10px] border border-tdd19-edge bg-white px-4.5 py-2.5 font-tdd19-sans text-sm font-medium text-tdd19-mut shadow-[0_2px_8px_oklch(0_0_0/0.06)] transition-[box-shadow,border-color,color] duration-150 hover:border-tdd19-ring hover:text-tdd19-ink hover:shadow-[0_4px_16px_oklch(0.59_0.2_278/0.15)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd19-acc">
    <span aria-hidden="true">&#128269;</span> Search commands
    <kbd class="ml-1 rounded-[5px] border border-tdd19-edge bg-tdd19-kbd px-1.5 py-0.5 font-tdd19-sans text-[11px] text-tdd19-mut">&#8984;K</kbd>
  </button>
  <div id="tdd19-backdrop" class="pointer-events-none fixed inset-0 z-200 bg-black/35 opacity-0 backdrop-blur-[2px] transition-opacity duration-200 group-data-open/scene:pointer-events-auto group-data-open/scene:opacity-100"></div>
  <div id="tdd19-palette" role="dialog" aria-modal="true" aria-label="Command palette" class="pointer-events-none invisible fixed top-1/2 left-1/2 z-201 w-[min(520px,90vw)] -translate-x-1/2 -translate-y-1/2 scale-95 overflow-hidden rounded-2xl border border-tdd19-edge bg-white opacity-0 shadow-[0_24px_80px_oklch(0_0_0/0.25)] transition-[opacity,scale,visibility] duration-240 ease-tdd19 group-data-open/scene:pointer-events-auto group-data-open/scene:visible group-data-open/scene:scale-100 group-data-open/scene:opacity-100 motion-reduce:transition-none">
    <div class="flex items-center gap-2.5 border-b border-tdd19-edge px-4 py-3.5">
      <span class="shrink-0 text-base text-tdd19-mut" aria-hidden="true">&#128269;</span>
      <input id="tdd19-input" type="text" placeholder="Search commands&hellip;" autocomplete="off" class="flex-1 border-0 bg-transparent font-tdd19-sans text-[15px] font-medium text-tdd19-ink outline-none placeholder:font-normal placeholder:text-tdd19-mut">
      <button type="button" id="tdd19-close" class="cursor-pointer rounded-md border border-tdd19-edge bg-tdd19-kbd px-2 py-1 font-tdd19-sans text-[11px] font-semibold text-tdd19-mut transition-colors duration-150 hover:bg-tdd19-edge focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd19-acc">ESC</button>
    </div>
    <ul id="tdd19-list" role="listbox" aria-label="Commands" class="max-h-65 list-none overflow-y-auto p-1.5">
      <li class="px-3 pt-2 pb-1 text-[10.5px] font-bold uppercase tracking-[0.08em] text-tdd19-mut" data-group>Quick Actions</li>
      <li role="option" data-label="New Document" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#128196;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>New Document</span><kbd class="rounded-[5px] border border-tdd19-edge bg-tdd19-kbd px-1.5 py-0.5 text-[11px] text-tdd19-mut">&#8984;N</kbd></li>
      <li role="option" data-label="Open File" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#128193;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Open File</span><kbd class="rounded-[5px] border border-tdd19-edge bg-tdd19-kbd px-1.5 py-0.5 text-[11px] text-tdd19-mut">&#8984;O</kbd></li>
      <li role="option" data-label="Save Project" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#128190;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Save Project</span><kbd class="rounded-[5px] border border-tdd19-edge bg-tdd19-kbd px-1.5 py-0.5 text-[11px] text-tdd19-mut">&#8984;S</kbd></li>
      <li class="px-3 pt-2 pb-1 text-[10.5px] font-bold uppercase tracking-[0.08em] text-tdd19-mut" data-group>Navigation</li>
      <li role="option" data-label="Go to Dashboard" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#127968;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Go to Dashboard</span></li>
      <li role="option" data-label="Go to Settings" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#9881;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Go to Settings</span></li>
      <li role="option" data-label="Go to Analytics" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#128202;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Go to Analytics</span></li>
      <li class="px-3 pt-2 pb-1 text-[10.5px] font-bold uppercase tracking-[0.08em] text-tdd19-mut" data-group>Theme</li>
      <li role="option" data-label="Toggle Dark Mode" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#127769;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Toggle Dark Mode</span></li>
      <li role="option" data-label="Toggle Compact View" class="flex cursor-pointer items-center gap-2.5 rounded-lg px-3 py-2.5 transition-colors duration-100 hover:bg-tdd19-tint data-active:bg-tdd19-tint [&_mark]:rounded-[2px] [&_mark]:bg-tdd19-mark [&_mark]:font-bold [&_mark]:text-tdd19-acc"><span class="w-5 shrink-0 text-center text-[15px]" aria-hidden="true">&#128262;</span><span class="flex-1 text-sm font-medium text-tdd19-ink" data-text>Toggle Compact View</span></li>
    </ul>
    <div class="flex gap-4 border-t border-tdd19-edge bg-tdd19-foot px-4 py-2.5 text-[11px] font-medium text-tdd19-mut">
      <span>&#8593;&#8595; navigate</span><span>&#9166; select</span><span>esc close</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd19-bg1: #eef2ff;
  --color-tdd19-bg1: oklch(0.96 0.02 275);
  --color-tdd19-bg2: #e0e7ff;
  --color-tdd19-bg2: oklch(0.92 0.04 275);
  --color-tdd19-ink: #111827;
  --color-tdd19-ink: oklch(0.21 0.02 265);
  --color-tdd19-mut: #6b7280;
  --color-tdd19-mut: oklch(0.55 0.02 265);
  --color-tdd19-edge: #e5e7eb;
  --color-tdd19-edge: oklch(0.91 0.005 265);
  --color-tdd19-kbd: #f3f4f6;
  --color-tdd19-kbd: oklch(0.96 0.003 265);
  --color-tdd19-foot: #fafafa;
  --color-tdd19-foot: oklch(0.98 0 0);
  --color-tdd19-tint: #f5f3ff;
  --color-tdd19-tint: oklch(0.97 0.02 295);
  --color-tdd19-mark: #c7d2fe;
  --color-tdd19-mark: oklch(0.86 0.06 275);
  --color-tdd19-ring: #c7d2fe;
  --color-tdd19-ring: oklch(0.86 0.06 275);
  --color-tdd19-acc: #6366f1;
  --color-tdd19-acc: oklch(0.59 0.2 278);
  --font-tdd19-sans: 'Inter', system-ui, sans-serif;
  --ease-tdd19: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-19 {
  width: 100%;
  min-height: 100svh;
}

.tdd-19 ::selection {
  background: var(--color-tdd19-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-19').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var openBtn = root.querySelector('#tdd19-open'),
        closeBtn = root.querySelector('#tdd19-close'),
        backdrop = root.querySelector('#tdd19-backdrop'),
        input = root.querySelector('#tdd19-input'),
        list = root.querySelector('#tdd19-list');
    if (!openBtn || !list) return;
    var rows = function () { return Array.from(list.querySelectorAll('[role="option"]')); };
    var visible = function () { return rows().filter(function (r) { return !r.hidden; }); };

    function open() {
      root.toggleAttribute('data-open', true);
      setTimeout(function () { input.focus(); }, 50);
    }
    function close() {
      root.toggleAttribute('data-open', false);
      input.value = '';
      filter('');
      openBtn.focus();
    }
    function filter(q) {
      q = q.toLowerCase().trim();
      rows().forEach(function (row) {
        var label = row.dataset.label || '', text = row.querySelector('[data-text]');
        row.removeAttribute('data-active');
        if (!q) { row.hidden = false; if (text) text.textContent = label; return; }
        var i = label.toLowerCase().indexOf(q);
        row.hidden = i < 0;
        if (i > -1 && text) {
          text.textContent = '';
          text.append(label.slice(0, i));
          var m = document.createElement('mark');
          m.textContent = label.slice(i, i + q.length);
          text.append(m, label.slice(i + q.length));
        }
      });
      list.querySelectorAll('[data-group]').forEach(function (g) {
        var next = g.nextElementSibling, any = false;
        while (next && !next.hasAttribute('data-group')) { if (!next.hidden) any = true; next = next.nextElementSibling; }
        g.hidden = !!q && !any;
      });
      var v = visible();
      if (v.length) v[0].setAttribute('data-active', '');
    }

    openBtn.addEventListener('click', open);
    closeBtn.addEventListener('click', close);
    backdrop.addEventListener('click', close);
    input.addEventListener('input', function () { filter(input.value); });
    rows().forEach(function (r) { r.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) {
      if (!root.hasAttribute('data-open')) return;
      var v = visible(), cur = list.querySelector('[data-active]'), i = cur ? v.indexOf(cur) : -1;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!v.length) return;
        var n = e.key === 'ArrowDown' ? (i + 1) % v.length : (i - 1 + v.length) % v.length;
        v.forEach(function (r) { r.removeAttribute('data-active'); });
        v[n].setAttribute('data-active', '');
      } else if (e.key === 'Enter' && cur) close();
    });
  });
})();
```
