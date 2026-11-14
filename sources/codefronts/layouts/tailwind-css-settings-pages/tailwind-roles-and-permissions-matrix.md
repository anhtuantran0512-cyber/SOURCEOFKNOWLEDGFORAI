---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-roles-and-permissions-matrix/"
title: "Tailwind Roles and Permissions Matrix"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A clear RBAC matrix: permissions grouped by area down a sticky first column, roles across the top with live 'n / 12' counts, custom checkbox cells built on…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Roles and Permissions Matrix
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-roles-and-permissions-matrix/

A clear RBAC matrix: permissions grouped by area down a sticky first column, roles across the top with live 'n / 12' counts, custom checkbox cells built on real inputs, a locked Owner column, crosshair row and column highlighting, destructive permissions flagged in red, and change tracking that marks every edited cell and counts unsaved changes in a save bar.
## HTML
```html
<section data-tsp08 class="tsp-08 group/perm w-full min-h-svh bg-tsp08-bg px-4 py-10 font-tsp08-sans text-tsp08-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-08-h">
  <form data-form class="mx-auto grid w-full max-w-6xl gap-6 pb-24">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-08-h" class="text-3xl font-semibold tracking-tight">Roles &amp; permissions</h1><p class="mt-1 text-tsp08-mut">Decide what each role can see and do across the workspace.</p></div>
      <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl border border-tsp08-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp08-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp08-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg>Custom role</button>
    </header>
    <div class="overflow-x-auto rounded-3xl border border-tsp08-line bg-white shadow-[0_1px_2px_rgb(0_0_0/0.04)]">
      <table data-table class="w-full min-w-[44rem] border-collapse text-sm">
        <thead>
          <tr class="border-b border-tsp08-line">
            <th scope="col" class="sticky left-0 z-10 w-[38%] bg-white px-5 py-4 text-left text-xs font-semibold uppercase tracking-wide text-tsp08-mut">Permission</th>
            <th scope="col" class="px-3 py-4 text-center data-hl:bg-tsp08-acc/5"><span class="flex items-center justify-center gap-1 font-semibold"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 text-amber-600"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg>Owner</span><span data-count class="text-xs font-medium tabular-nums text-tsp08-mut"></span></th>
            <th scope="col" class="px-3 py-4 text-center data-hl:bg-tsp08-acc/5"><span class="block font-semibold">Admin</span><span data-count class="text-xs font-medium tabular-nums text-tsp08-mut"></span></th>
            <th scope="col" class="px-3 py-4 text-center data-hl:bg-tsp08-acc/5"><span class="block font-semibold">Editor</span><span data-count class="text-xs font-medium tabular-nums text-tsp08-mut"></span></th>
            <th scope="col" class="px-3 py-4 text-center data-hl:bg-tsp08-acc/5"><span class="block font-semibold">Viewer</span><span data-count class="text-xs font-medium tabular-nums text-tsp08-mut"></span></th>
          </tr>
        </thead>
        <tbody data-body class="[&_tr[data-row]]:transition [&_tr[data-row]:hover]:bg-tsp08-bg/70 [&_tr[data-row]:hover>th]:bg-tsp08-bg">
        </tbody>
      </table>
    </div>
    <p class="text-sm text-tsp08-mut">Owner permissions are fixed. Changes apply to everyone with that role the next time they load a page.</p>
    <div role="status" aria-live="polite" class="fixed inset-x-0 bottom-4 z-20 mx-auto flex w-[min(38rem,calc(100%-2rem))] translate-y-[160%] flex-wrap items-center justify-between gap-3 rounded-2xl bg-tsp08-ink py-2 pl-5 pr-2 text-sm text-white shadow-2xl transition duration-300 group-data-dirty/perm:translate-y-0 motion-reduce:transition-none">
      <span class="flex items-center gap-2"><span class="size-2 rounded-full bg-amber-400"></span><span data-dirty-msg>0 unsaved changes</span></span>
      <span class="flex gap-1.5"><button type="button" data-reset class="min-h-11 rounded-xl px-4 font-semibold text-white/70 transition hover:text-white focus-visible:outline-2 focus-visible:outline-white">Reset</button><button type="submit" class="min-h-11 rounded-xl bg-white px-4 font-semibold text-tsp08-ink transition hover:bg-white/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Save changes</button></span>
    </div>
  </form>
  <template data-tpl-group><tr><th scope="colgroup" colspan="5" class="sticky left-0 bg-tsp08-bg px-5 py-2.5 text-left text-xs font-semibold uppercase tracking-[0.12em] text-tsp08-mut"></th></tr></template>
  <template data-tpl-row><tr data-row class="border-t border-tsp08-line"><th scope="row" class="sticky left-0 z-10 bg-white px-5 py-1.5 text-left font-medium"><span class="flex items-center gap-2"><span data-name></span><span data-danger hidden class="rounded-full bg-rose-50 px-2 py-0.5 text-[11px] font-semibold text-rose-700">Destructive</span></span></th></tr></template>
  <template data-tpl-cell><td class="px-3 text-center data-hl:bg-tsp08-acc/5"><label class="mx-auto grid size-11 cursor-pointer place-items-center has-disabled:cursor-not-allowed"><input type="checkbox" class="peer sr-only"><span class="grid size-5 place-items-center rounded-md border-2 border-tsp08-line bg-white text-white transition [&>svg]:opacity-0 peer-checked:border-tsp08-acc peer-checked:bg-tsp08-acc peer-checked:[&>svg]:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp08-acc peer-disabled:border-amber-300 peer-disabled:bg-amber-100 peer-disabled:text-amber-700 peer-data-changed:ring-4 peer-data-changed:ring-amber-300/60"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></label></td></template>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp08-bg: #f5f5f9;
  --color-tsp08-bg: oklch(0.972 0.005 285);
  --color-tsp08-ink: #191a2c;
  --color-tsp08-ink: oklch(0.225 0.033 280);
  --color-tsp08-mut: #5f6177;
  --color-tsp08-mut: oklch(0.51 0.03 280);
  --color-tsp08-line: #e4e5ee;
  --color-tsp08-line: oklch(0.925 0.011 280);
  --color-tsp08-acc: #4338ca;
  --color-tsp08-acc: oklch(0.457 0.215 277);
  --font-tsp08-sans: 'Instrument Sans', system-ui, sans-serif;
}

.tsp-08 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp08]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const ROLES = ['Owner', 'Admin', 'Editor', 'Viewer'];
  const MATRIX = [
    ['Workspace', [['View workspace', 1111], ['Edit workspace settings', 1100], ['Manage integrations', 1100]]],
    ['Members', [['Invite members', 1110], ['Change member roles', 1100], ['Remove members', 1100, true]]],
    ['Content', [['Create projects', 1110], ['Edit any project', 1110], ['Export data', 1100], ['Delete projects', 1100, true]]],
    ['Billing', [['View invoices', 1100], ['Manage plan &amp; payment', 1000]]],
  ];
  const body = root.querySelector('[data-body]');
  const tpl = (k) => root.querySelector('[data-tpl-' + k + ']').content.firstElementChild;
  MATRIX.forEach(([group, perms]) => {
    const g = tpl('group').cloneNode(true);
    g.querySelector('th').textContent = group;
    body.appendChild(g);
    perms.forEach(([name, bits, danger]) => {
      const tr = tpl('row').cloneNode(true);
      tr.querySelector('[data-name]').innerHTML = name;
      if (danger) tr.querySelector('[data-danger]').hidden = false;
      String(bits).split('').forEach((b, i) => {
        const td = tpl('cell').cloneNode(true);
        const cb = td.querySelector('input');
        cb.checked = b === '1';
        cb.setAttribute('aria-label', ROLES[i] + ': ' + tr.querySelector('[data-name]').textContent);
        if (i === 0) cb.disabled = true;
        cb.dataset.initial = cb.checked;
        tr.appendChild(td);
      });
      body.appendChild(tr);
    });
  });
  const boxes = () => [...body.querySelectorAll('input')];
  const recount = () => {
    const rows = [...body.querySelectorAll('[data-row]')];
    root.querySelectorAll('[data-count]').forEach((el, i) => {
      el.textContent = rows.filter((r) => r.cells[i + 1].querySelector('input').checked).length + ' / ' + rows.length;
    });
    const changed = boxes().filter((b) => String(b.checked) !== b.dataset.initial);
    boxes().forEach((b) => b.toggleAttribute('data-changed', changed.includes(b)));
    root.querySelector('[data-dirty-msg]').textContent = changed.length + ' unsaved change' + (changed.length === 1 ? '' : 's');
    root.toggleAttribute('data-dirty', changed.length > 0);
  };
  body.addEventListener('change', recount);
  root.querySelector('[data-reset]').addEventListener('click', () => { boxes().forEach((b) => { b.checked = b.dataset.initial === 'true'; }); recount(); });
  root.querySelector('[data-form]').addEventListener('submit', (e) => { e.preventDefault(); boxes().forEach((b) => { b.dataset.initial = b.checked; }); recount(); });
  const table = root.querySelector('[data-table]');
  const highlight = (col) => table.querySelectorAll('tr').forEach((tr) => {
    [...tr.cells].forEach((c, i) => c.toggleAttribute('data-hl', col > 0 && i === col && c.colSpan === 1));
  });
  table.addEventListener('pointerover', (e) => { const c = e.target.closest('td, th'); highlight(c && c.colSpan === 1 ? c.cellIndex : -1); });
  table.addEventListener('pointerleave', () => highlight(-1));
  table.addEventListener('focusin', (e) => { const c = e.target.closest('td'); if (c) highlight(c.cellIndex); });
  recount();
})();
```
