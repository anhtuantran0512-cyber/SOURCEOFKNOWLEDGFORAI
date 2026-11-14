---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-command-palette-modal-cmd-k-roving-selection/"
title: "Tailwind Command Palette Modal with ⌘K and Roving Selection"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The ⌘K launcher: type to filter, arrow to move, Enter to run."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Command Palette Modal with ⌘K and Roving Selection
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-command-palette-modal-cmd-k-roving-selection/

The ⌘K launcher: type to filter, arrow to move, Enter to run. The port's neat trick is that the active row needs no class at all — aria-[selected=true]:bg-tm18-acctint styles the attribute the screen reader is already reading, so the highlight and the announcement cannot disagree.
## HTML
```html
<section class="tm-18 w-full min-h-svh grid place-items-center bg-tm18-bg font-tm18-sans px-6 py-10">
  <button type="button" data-tm18-open class="inline-flex items-center justify-between gap-3 min-w-[220px] min-h-11 pl-5 pr-3 rounded-xl text-sm text-tm18-mut bg-tm18-btn border border-tm18-edge cursor-pointer transition-colors duration-200 hover:bg-tm18-btnhover hover:border-tm18-acc focus-visible:outline-2 focus-visible:outline-tm18-acc focus-visible:outline-offset-2">Search <kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px] font-semibold text-tm18-ink">⌘K</kbd></button>

  <dialog id="tm-18-dlg" aria-label="Command palette" class="mx-auto mt-[12vh] mb-0 w-[min(560px,94vw)] p-0 border-0 rounded-2xl text-tm18-ink bg-tm18-card shadow-[0_50px_100px_-28px_#000,0_0_0_1px_var(--color-tm18-edge)] opacity-0 -translate-y-4 scale-[0.98] transition-[opacity,translate,scale,overlay,display] duration-[240ms] transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:-translate-y-4 open:starting:scale-[0.98] open:backdrop:bg-tm18-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div data-tm18-card>
      <div class="flex items-center gap-3 px-4 py-3.5 border-b border-tm18-edge">
        <span aria-hidden="true" class="text-[19px] text-tm18-faint">⌕</span>
        <input data-tm18-input type="text" role="combobox" aria-expanded="true" aria-controls="tm-18-list" aria-autocomplete="list" autocomplete="off" placeholder="Type a command or search…" class="flex-1 min-h-11 bg-transparent border-0 outline-none text-base text-tm18-hi placeholder:text-tm18-faint">
        <kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[10px] font-semibold text-tm18-mut">esc</kbd>
      </div>

      <ul data-tm18-list id="tm-18-list" role="listbox" aria-label="Commands" class="list-none max-h-[320px] overflow-auto m-0 p-2"></ul>
      <div data-tm18-empty hidden class="px-5 py-8 text-center text-sm text-tm18-mut">No commands match “<span data-tm18-q class="text-tm18-hi"></span>”.</div>
      <p data-tm18-count aria-live="polite" class="sr-only"></p>

      <footer class="flex flex-wrap gap-4 px-4 py-3 border-t border-tm18-edge text-xs text-tm18-mut">
        <span class="inline-flex items-center gap-1.5"><kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px]">↑</kbd><kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px]">↓</kbd> navigate</span>
        <span class="inline-flex items-center gap-1.5"><kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px]">↵</kbd> select</span>
        <span class="inline-flex items-center gap-1.5"><kbd class="px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px]">esc</kbd> close</span>
      </footer>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm18-bg: #08080d;
  --color-tm18-bg: oklch(0.14 0.012 265);
  --color-tm18-card: #161824;
  --color-tm18-card: oklch(0.22 0.018 265);
  --color-tm18-btn: #12141e;
  --color-tm18-btn: oklch(0.19 0.015 265);
  --color-tm18-btnhover: #171a26;
  --color-tm18-btnhover: oklch(0.22 0.02 265);
  --color-tm18-kbd: #232838;
  --color-tm18-kbd: oklch(0.27 0.02 265);
  --color-tm18-kbdedge: #333a4e;
  --color-tm18-kbdedge: oklch(0.34 0.025 265);
  --color-tm18-edge: #282d40;
  --color-tm18-edge: oklch(0.3 0.022 265);
  --color-tm18-icon: #212636;
  --color-tm18-icon: oklch(0.26 0.02 265);
  --color-tm18-hi: #f1f3fa;
  --color-tm18-hi: oklch(0.96 0.006 265);
  --color-tm18-ink: #d3d8e6;
  --color-tm18-ink: oklch(0.88 0.012 265);
  --color-tm18-mut: #9ba3ba;
  --color-tm18-mut: oklch(0.72 0.02 265);
  --color-tm18-faint: #7d8599;
  --color-tm18-faint: oklch(0.62 0.02 265);
  --color-tm18-acc: #8fa6ff;
  --color-tm18-acc: oklch(0.76 0.13 265);
  --color-tm18-acctint: #2c3555;
  --color-tm18-acctint: oklch(0.34 0.08 265);
  --color-tm18-accicon: #3f4c7a;
  --color-tm18-accicon: oklch(0.42 0.1 265);
  --color-tm18-scrim: #05060a99;
  --color-tm18-scrim: oklch(0.12 0.01 265 / 0.6);
  --font-tm18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-18 {
  width: 100%;
}

#tm-18-dlg::backdrop {
  background: oklch(0.12 0.01 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .28s, backdrop-filter .28s, overlay .28s allow-discrete, display .28s allow-discrete;
}

@starting-style {
  #tm-18-dlg[open]::backdrop {
    background: oklch(0.12 0.01 265 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-18');
  var dlg = root.querySelector('#tm-18-dlg');
  var card = root.querySelector('[data-tm18-card]');
  var input = root.querySelector('[data-tm18-input]');
  var list = root.querySelector('[data-tm18-list]');
  var empty = root.querySelector('[data-tm18-empty]');
  var count = root.querySelector('[data-tm18-count]');

  // Class lists are whole strings so the compiler can see them.
  var ROW = 'flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-[9px] cursor-pointer text-[14.5px] text-tm18-ink scroll-mt-2 aria-[selected=true]:bg-tm18-acctint aria-[selected=true]:text-white';
  var ICON = 'grid place-items-center size-7 shrink-0 rounded-[7px] text-sm bg-tm18-icon text-tm18-mut group-aria-[selected=true]:bg-tm18-accicon';
  var GRP = 'px-3 pt-3 pb-1.5 text-[11px] uppercase tracking-[0.14em] text-tm18-faint';
  var KBD = 'px-1.5 py-0.5 rounded border border-tm18-kbdedge bg-tm18-kbd font-tm18-mono text-[11px] text-tm18-mut';

  var COMMANDS = [
    { group: 'Actions', i: '✎', label: 'New document', keys: 'create file', sc: ['⌘', 'N'] },
    { group: 'Actions', i: '⬆', label: 'Upload files', keys: 'import media', sc: ['⌘', 'U'] },
    { group: 'Actions', i: '🖇', label: 'Invite teammate', keys: 'add member share', sc: ['⌘', 'I'] },
    { group: 'Navigate', i: '⌂', label: 'Go to Dashboard', keys: 'home overview', sc: ['G', 'H'] },
    { group: 'Navigate', i: '▤', label: 'Go to Projects', keys: 'boards work', sc: ['G', 'P'] },
    { group: 'Navigate', i: '⚙', label: 'Open Settings', keys: 'preferences account', sc: ['⌘', ','] },
    { group: 'Help', i: '?', label: 'Keyboard shortcuts', keys: 'keys help', sc: ['⌘', '/'] },
    { group: 'Help', i: '✉', label: 'Contact support', keys: 'email ticket', sc: [] }
  ];
  var active = 0, visible = [];

  function render(q) {
    q = (q || '').trim().toLowerCase();
    list.innerHTML = ''; visible = [];
    var lastGroup = null;
    COMMANDS.forEach(function (c) {
      if (q && (c.label + ' ' + c.keys).toLowerCase().indexOf(q) === -1) return;
      if (c.group !== lastGroup) {
        var h = document.createElement('li');
        h.className = GRP; h.textContent = c.group; h.setAttribute('role', 'presentation');
        list.appendChild(h); lastGroup = c.group;
      }
      var li = document.createElement('li');
      li.className = 'group ' + ROW;
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', 'false');
      li.innerHTML = '<span class="' + ICON + '">' + c.i + '</span>' + c.label +
        '<span class="ml-auto flex gap-1">' + c.sc.map(function (k) { return '<kbd class="' + KBD + '">' + k + '</kbd>'; }).join('') + '</span>';
      li.addEventListener('mousemove', function () { setActive(visible.indexOf(li)); });
      li.addEventListener('click', function () { run(li); });
      list.appendChild(li); visible.push(li);
    });
    empty.hidden = visible.length > 0;
    if (!empty.hidden) root.querySelector('[data-tm18-q]').textContent = q;
    active = 0; paint();
    count.textContent = visible.length + ' commands';
  }

  function paint() {
    visible.forEach(function (li, n) { li.setAttribute('aria-selected', n === active ? 'true' : 'false'); });
    if (visible[active]) visible[active].scrollIntoView({ block: 'nearest' });
  }
  function setActive(n) { if (n < 0 || n >= visible.length) return; active = n; paint(); }
  function run(li) { input.value = li.textContent.replace(/[⌘↵]/g, '').trim(); dlg.close(); }

  input.addEventListener('input', function () { render(input.value); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(active + 1, visible.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
    else if (e.key === 'Enter') { e.preventDefault(); if (visible[active]) run(visible[active]); }
  });

  function open() { input.value = ''; render(''); dlg.showModal(); setTimeout(function () { input.focus(); }, 20); }
  root.querySelector('[data-tm18-open]').addEventListener('click', open);
  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); if (!dlg.open) open(); }
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
