---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-command-palette-cmd-k-search/"
title: "Tailwind Command Palette — Cmd+K Search Menu"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A Spotlight-style palette opened by the search bar, ⌘K or Ctrl K: live filtering with highlighted matches, grouped results, shortcut badges, and full…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Command Palette — Cmd+K Search Menu
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-command-palette-cmd-k-search/

A Spotlight-style palette opened by the search bar, ⌘K or Ctrl K: live filtering with highlighted matches, grouped results, shortcut badges, and full keyboard control. The original's footer promised ↑↓ navigation and ↵ to open but never implemented either &mdash; this port does, as an ARIA combobox with aria-activedescendant.
## HTML
```html
<section class="tmn-15 w-full min-h-svh grid place-items-center bg-tmn15-stage px-4 py-6 font-tmn15-sans antialiased" aria-label="Tailwind command palette demo">
  <div data-tmn15 class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn15-bg text-tmn15-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.9)] ring-1 ring-white/8">
    <button type="button" data-trigger aria-haspopup="dialog" class="absolute inset-x-4 top-5 z-[5] flex h-12 items-center gap-2.5 rounded-xl border border-tmn15-line bg-tmn15-surface px-3.5 text-left text-sm text-tmn15-mut transition hover:border-tmn15-acc/45 hover:shadow-[0_0_0_3px] hover:shadow-tmn15-acc/10 focus-visible:ring-2 focus-visible:ring-tmn15-acc focus-visible:outline-none">
      <svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <span class="flex-1">Search or jump to…</span>
      <span class="flex gap-1 font-tmn15-mono text-[11px]"><kbd data-mod class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 py-0.5">⌘</kbd><kbd class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 py-0.5">K</kbd></span>
    </button>

    <main class="absolute inset-x-0 top-[76px] bottom-0 overflow-y-auto px-4 pb-6">
      <p class="mb-3 text-[11px] font-bold tracking-[0.12em] text-tmn15-mut uppercase">Quick actions</p>
      <div class="mb-6 grid grid-cols-2 gap-2.5">
        <a href="#" class="rounded-2xl border border-tmn15-line bg-tmn15-surface p-4 transition-colors hover:border-tmn15-acc/60"><svg viewBox="0 0 24 24" class="mb-2.5 size-5.5 text-tmn15-acc" aria-hidden="true"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 1 1 3 3L7 19l-4 1 1-4z"/></svg><span class="block text-[13px] font-semibold">New document</span><span class="block text-xs text-tmn15-mut">Blank page</span></a>
        <a href="#" class="rounded-2xl border border-tmn15-line bg-tmn15-surface p-4 transition-colors hover:border-tmn15-acc/60"><svg viewBox="0 0 24 24" class="mb-2.5 size-5.5 text-tmn15-acc" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg><span class="block text-[13px] font-semibold">Schedule</span><span class="block text-xs text-tmn15-mut">Add to calendar</span></a>
        <a href="#" class="rounded-2xl border border-tmn15-line bg-tmn15-surface p-4 transition-colors hover:border-tmn15-acc/60"><svg viewBox="0 0 24 24" class="mb-2.5 size-5.5 text-tmn15-acc" aria-hidden="true"><circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M19 8v6M22 11h-6"/></svg><span class="block text-[13px] font-semibold">Invite team</span><span class="block text-xs text-tmn15-mut">Share workspace</span></a>
        <a href="#" class="rounded-2xl border border-tmn15-line bg-tmn15-surface p-4 transition-colors hover:border-tmn15-acc/60"><svg viewBox="0 0 24 24" class="mb-2.5 size-5.5 text-tmn15-acc" aria-hidden="true"><path d="M3 3v18h18M8 16v-5M13 16V8M18 16v-3"/></svg><span class="block text-[13px] font-semibold">Analytics</span><span class="block text-xs text-tmn15-mut">View insights</span></a>
      </div>
      <p class="mb-1 text-[11px] font-bold tracking-[0.12em] text-tmn15-mut uppercase">Recently visited</p>
      <a href="#" class="flex min-h-14 items-center gap-3 border-b border-white/5"><span class="grid size-8 place-items-center rounded-lg bg-tmn15-surface"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9zM14 3v6h6"/></svg></span><span><span class="block text-[13px] font-medium">Product roadmap</span><span class="block text-xs text-tmn15-mut">10 min ago</span></span></a>
      <a href="#" class="flex min-h-14 items-center gap-3 border-b border-white/5"><span class="grid size-8 place-items-center rounded-lg bg-tmn15-surface"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/></svg></span><span><span class="block text-[13px] font-medium">Design review thread</span><span class="block text-xs text-tmn15-mut">1 hour ago</span></span></a>
      <a href="#" class="flex min-h-14 items-center gap-3"><span class="grid size-8 place-items-center rounded-lg bg-tmn15-surface"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><rect x="3" y="3" width="7" height="18" rx="1.5"/><rect x="14" y="3" width="7" height="11" rx="1.5"/></svg></span><span><span class="block text-[13px] font-medium">Sprint planning board</span><span class="block text-xs text-tmn15-mut">Yesterday</span></span></a>
    </main>

    <div data-scrim class="invisible absolute inset-0 z-20 flex flex-col bg-black/60 px-3 pt-16 opacity-0 backdrop-blur-[2px] transition-[opacity,visibility] duration-200 group-data-open:visible group-data-open:opacity-100">
      <div role="dialog" aria-modal="true" aria-label="Command palette" class="-translate-y-2 scale-95 overflow-hidden rounded-2xl border border-tmn15-line bg-tmn15-surface shadow-[0_24px_64px_oklch(0_0_0/0.55)] transition-transform duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] group-data-open:translate-y-0 group-data-open:scale-100">
        <div class="flex items-center gap-2.5 border-b border-tmn15-line px-4">
          <svg viewBox="0 0 24 24" class="size-4.5 text-tmn15-mut" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
          <input data-input role="combobox" aria-expanded="true" aria-controls="tmn-15-list" aria-autocomplete="list" autocomplete="off" spellcheck="false" placeholder="Search commands, pages…" class="h-13 flex-1 bg-transparent text-[15px] placeholder:text-tmn15-mut focus:outline-none">
          <button type="button" data-clear class="hidden size-7 place-items-center rounded-full bg-tmn15-surface2 text-tmn15-mut data-show:grid"><span class="sr-only">Clear search</span><svg viewBox="0 0 24 24" class="size-3.5" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
        </div>
        <ul id="tmn-15-list" data-list role="listbox" aria-label="Results" class="max-h-[360px] overflow-y-auto py-1.5"></ul>
        <div class="flex items-center gap-4 border-t border-tmn15-line px-3.5 py-2 text-[11px] text-tmn15-mut">
          <span class="flex items-center gap-1.5"><kbd class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 font-tmn15-mono">↑↓</kbd>Navigate</span>
          <span class="flex items-center gap-1.5"><kbd class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 font-tmn15-mono">↵</kbd>Open</span>
          <span class="flex items-center gap-1.5"><kbd class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 font-tmn15-mono">esc</kbd>Close</span>
        </div>
      </div>
    </div>

    <p data-toast role="status" aria-live="polite" class="pointer-events-none absolute inset-x-6 bottom-6 z-30 translate-y-3 rounded-xl bg-tmn15-ink px-4 py-3 text-center text-[13px] font-medium text-tmn15-bg opacity-0 transition duration-250 data-show:translate-y-0 data-show:opacity-100"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn15-stage: #08080a;
  --color-tmn15-stage: oklch(0.13 0.003 285);
  --color-tmn15-bg: #111113;
  --color-tmn15-bg: oklch(0.17 0.004 285);
  --color-tmn15-surface: #1c1c1f;
  --color-tmn15-surface: oklch(0.22 0.005 285);
  --color-tmn15-surface2: #27272b;
  --color-tmn15-surface2: oklch(0.27 0.006 285);
  --color-tmn15-line: #303036;
  --color-tmn15-line: oklch(0.31 0.008 285);
  --color-tmn15-ink: #ececf1;
  --color-tmn15-ink: oklch(0.94 0.005 285);
  --color-tmn15-mut: #9a9aa3;
  --color-tmn15-mut: oklch(0.69 0.01 285);
  --color-tmn15-acc: #f97316;
  --color-tmn15-acc: oklch(0.7 0.19 48);
  --font-tmn15-sans: 'Geist', system-ui, sans-serif;
  --font-tmn15-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-15 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const ICONS = {
    home: '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    chart: '<path d="M3 3v18h18M8 16v-5M13 16V8M18 16v-3"/>',
    users: '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/>',
    gear: '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    pen: '<path d="M12 20h9M16.5 3.5a2.1 2.1 0 1 1 3 3L7 19l-4 1 1-4z"/>',
    out: '<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8M16 6l-4-4-4 4M12 2v13"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
    moon: '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
    doc: '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9zM14 3v6h6"/>',
    chat: '<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/>'
  };
  const COMMANDS = [
    { group: 'Pages', icon: 'home', label: 'Dashboard', desc: 'Main workspace' },
    { group: 'Pages', icon: 'chart', label: 'Analytics', desc: 'Traffic & conversions' },
    { group: 'Pages', icon: 'users', label: 'Team members', desc: '12 members' },
    { group: 'Pages', icon: 'gear', label: 'Settings', desc: 'Account & preferences' },
    { group: 'Actions', icon: 'pen', label: 'New document', desc: 'Create a blank page', key: 'N' },
    { group: 'Actions', icon: 'out', label: 'Export as PDF', desc: 'Download current page', key: 'E' },
    { group: 'Actions', icon: 'link', label: 'Copy link', desc: 'Share current page', key: 'L' },
    { group: 'Actions', icon: 'moon', label: 'Change theme', desc: 'Appearance settings' },
    { group: 'Recent', icon: 'doc', label: 'Product roadmap', desc: '10 min ago' },
    { group: 'Recent', icon: 'chat', label: 'Design review', desc: '1 hour ago' }
  ];
  const esc = (s) => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
  const hl = (text, q) => {
    if (!q) return esc(text);
    const at = text.toLowerCase().indexOf(q.toLowerCase());
    if (at < 0) return esc(text);
    return esc(text.slice(0, at)) + '<mark class="bg-transparent text-tmn15-acc">' + esc(text.slice(at, at + q.length)) + '</mark>' + esc(text.slice(at + q.length));
  };
  const isMac = /Mac|iPhone|iPad/.test((navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '');

  document.querySelectorAll('[data-tmn15]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const trigger = root.querySelector('[data-trigger]');
    const scrim = root.querySelector('[data-scrim]');
    const input = root.querySelector('[data-input]');
    const list = root.querySelector('[data-list]');
    const clear = root.querySelector('[data-clear]');
    const toast = root.querySelector('[data-toast]');
    if (!isMac) root.querySelector('[data-mod]').textContent = 'Ctrl';
    let rows = [], active = 0, toastT = 0;

    const select = (k) => {
      if (!rows.length) { input.removeAttribute('aria-activedescendant'); return; }
      active = (k + rows.length) % rows.length;
      rows.forEach((r, j) => r.el.setAttribute('aria-selected', String(j === active)));
      const el = rows[active].el;
      input.setAttribute('aria-activedescendant', el.id);
      const top = el.offsetTop, bottom = top + el.offsetHeight;
      if (top < list.scrollTop) list.scrollTop = top - 6;
      else if (bottom > list.scrollTop + list.clientHeight) list.scrollTop = bottom - list.clientHeight + 6;
    };
    const render = () => {
      const q = input.value.trim();
      const ql = q.toLowerCase();
      const hits = q ? COMMANDS.filter((c) => c.label.toLowerCase().includes(ql) || c.desc.toLowerCase().includes(ql)) : COMMANDS;
      clear.toggleAttribute('data-show', q.length > 0);
      if (!hits.length) {
        list.innerHTML = '<li class="px-4 py-8 text-center text-[13px] text-tmn15-mut">No results for \u201C' + esc(q) + '\u201D</li>';
        rows = []; select(0); return;
      }
      let html = '', last = '';
      hits.forEach((c, j) => {
        if (c.group !== last) {
          html += '<li role="presentation" class="px-4 pt-2.5 pb-1 text-[10px] font-bold tracking-[0.14em] text-tmn15-mut uppercase">' + c.group + '</li>';
          last = c.group;
        }
        html += '<li role="option" id="tmn-15-opt-' + j + '" data-i="' + j + '" aria-selected="false" class="mx-1.5 flex min-h-12 cursor-pointer items-center gap-3 rounded-lg px-2.5 aria-selected:bg-tmn15-acc/12">' +
          '<span class="grid size-8 place-items-center rounded-lg bg-tmn15-surface2 text-tmn15-ink"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true">' + ICONS[c.icon] + '</svg></span>' +
          '<span class="min-w-0 flex-1"><span class="block truncate text-[13px] font-medium">' + hl(c.label, q) + '</span><span class="block truncate text-[11px] text-tmn15-mut">' + hl(c.desc, q) + '</span></span>' +
          (c.key ? '<kbd class="rounded border border-tmn15-line bg-tmn15-surface2 px-1.5 font-tmn15-mono text-[11px] text-tmn15-mut">' + c.key + '</kbd>' : '') + '</li>';
      });
      list.innerHTML = html;
      rows = hits.map((c, j) => ({ cmd: c, el: list.querySelector('#tmn-15-opt-' + j) }));
      list.scrollTop = 0;
      select(0);
    };
    const open = () => { root.setAttribute('data-open', ''); input.value = ''; render(); setTimeout(() => input.focus(), 30); };
    const close = () => { root.removeAttribute('data-open'); trigger.focus({ preventScroll: true }); };
    const run = (r) => {
      if (!r) return;
      close();
      toast.textContent = 'Opened \u201C' + r.cmd.label + '\u201D';
      toast.setAttribute('data-show', '');
      clearTimeout(toastT);
      toastT = setTimeout(() => toast.removeAttribute('data-show'), 1600);
    };

    trigger.addEventListener('click', open);
    scrim.addEventListener('click', (e) => { if (e.target === scrim) close(); });
    input.addEventListener('input', render);
    clear.addEventListener('click', () => { input.value = ''; render(); input.focus(); });
    list.addEventListener('pointermove', (e) => { const li = e.target.closest('[role=option]'); if (li) select(+li.dataset.i); });
    list.addEventListener('click', (e) => { const li = e.target.closest('[role=option]'); if (li) run(rows[+li.dataset.i]); });
    input.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown') { e.preventDefault(); select(active + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); select(active - 1); }
      else if (e.key === 'Enter') { e.preventDefault(); run(rows[active]); }
      else if (e.key === 'Escape') { e.preventDefault(); if (input.value) { input.value = ''; render(); } else close(); }
    });
    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); root.hasAttribute('data-open') ? close() : open(); }
    });
  });
})();
```
