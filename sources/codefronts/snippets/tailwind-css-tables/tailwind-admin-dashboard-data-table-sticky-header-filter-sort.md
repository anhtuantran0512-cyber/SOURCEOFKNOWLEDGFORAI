---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-admin-dashboard-data-table-sticky-header-filter-sort/"
title: "Tailwind Admin Dashboard Data Table with Sticky Header, Filter & Sort"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A GitHub-dark user-management grid that finally does what it draws: status filter pills that actually filter, a live search box, and sortable User and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Admin Dashboard Data Table with Sticky Header, Filter & Sort
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-admin-dashboard-data-table-sticky-header-filter-sort/

A GitHub-dark user-management grid that finally does what it draws: status filter pills that actually filter, a live search box, and sortable User and Revenue columns with real aria-sort. The header stays pinned with sticky top-0, and every visual state — pressed pill, sorted column, arrow direction — is an aria-* variant, so the script only ever sets attributes.
## HTML
```html
<section class="ttb-03 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb03-bg px-5 py-14 font-ttb03-sans text-ttb03-ink" aria-label="Admin dashboard data table demo">
  <div id="ttb03-grid" class="w-full max-w-5xl">
    <header class="mb-5 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-baseline gap-3">
        <h2 class="text-lg font-semibold">User management</h2>
        <span data-count role="status" class="rounded-full bg-ttb03-surface2 px-2.5 py-0.5 text-xs text-ttb03-mut ring-1 ring-ttb03-line">6 users</span>
      </div>
      <div class="flex flex-wrap items-center gap-2">
        <label class="relative">
          <span class="sr-only">Search users</span>
          <svg class="pointer-events-none absolute top-1/2 left-3 size-4 -translate-y-1/2 text-ttb03-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <input type="search" placeholder="Search name or email" class="min-h-11 w-56 rounded-lg bg-ttb03-surface pr-3 pl-9 text-sm text-ttb03-ink ring-1 ring-ttb03-line transition placeholder:text-ttb03-mut focus:ring-2 focus:ring-ttb03-blue focus:outline-none">
        </label>
        <div class="flex gap-1 rounded-lg bg-ttb03-surface p-1 ring-1 ring-ttb03-line" role="group" aria-label="Filter by status">
          <button type="button" data-filter="all" aria-pressed="true" class="min-h-9 rounded-md px-3 text-xs font-semibold text-ttb03-mut transition hover:text-ttb03-ink aria-pressed:bg-ttb03-blue/12 aria-pressed:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">All</button>
          <button type="button" data-filter="active" aria-pressed="false" class="min-h-9 rounded-md px-3 text-xs font-semibold text-ttb03-mut transition hover:text-ttb03-ink aria-pressed:bg-ttb03-blue/12 aria-pressed:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">Active</button>
          <button type="button" data-filter="pending" aria-pressed="false" class="min-h-9 rounded-md px-3 text-xs font-semibold text-ttb03-mut transition hover:text-ttb03-ink aria-pressed:bg-ttb03-blue/12 aria-pressed:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">Pending</button>
          <button type="button" data-filter="trial" aria-pressed="false" class="min-h-9 rounded-md px-3 text-xs font-semibold text-ttb03-mut transition hover:text-ttb03-ink aria-pressed:bg-ttb03-blue/12 aria-pressed:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">Trial</button>
          <button type="button" data-filter="banned" aria-pressed="false" class="min-h-9 rounded-md px-3 text-xs font-semibold text-ttb03-mut transition hover:text-ttb03-ink aria-pressed:bg-ttb03-blue/12 aria-pressed:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">Banned</button>
        </div>
      </div>
    </header>
    <div tabindex="0" role="region" aria-label="Users table, scrollable" class="relative max-h-[22rem] overflow-auto rounded-xl bg-ttb03-surface ring-1 ring-ttb03-line [scrollbar-color:var(--color-ttb03-line)_transparent] [scrollbar-width:thin] focus-visible:outline-2 focus-visible:outline-ttb03-blue">
      <table class="w-full min-w-[760px] border-collapse text-left text-[13px]">
        <caption class="sr-only">Users with plan, status, last activity and revenue</caption>
        <thead class="[&_th]:sticky [&_th]:top-0 [&_th]:z-10 [&_th]:bg-ttb03-surface2 [&_th]:px-4 [&_th]:py-3 [&_th]:text-[11px] [&_th]:font-semibold [&_th]:tracking-[0.08em] [&_th]:text-ttb03-mut [&_th]:uppercase [&_th]:shadow-[inset_0_-1px_0_var(--color-ttb03-line)]">
          <tr>
            <th scope="col" aria-sort="none" class="group/th">
              <button type="button" data-sort="name" class="-mx-2 inline-flex min-h-8 items-center gap-1.5 rounded px-2 uppercase transition hover:text-ttb03-ink group-aria-[sort=ascending]/th:text-ttb03-blue group-aria-[sort=descending]/th:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">User
                <svg class="size-3.5 opacity-50 transition group-aria-[sort=ascending]/th:opacity-100 group-aria-[sort=descending]/th:rotate-180 group-aria-[sort=descending]/th:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
              </button>
            </th>
            <th scope="col">Email</th>
            <th scope="col">Plan</th>
            <th scope="col">Status</th>
            <th scope="col">Last active</th>
            <th scope="col" aria-sort="none" class="group/th text-right">
              <button type="button" data-sort="revenue" class="-mx-2 inline-flex min-h-8 items-center gap-1.5 rounded px-2 uppercase transition hover:text-ttb03-ink group-aria-[sort=ascending]/th:text-ttb03-blue group-aria-[sort=descending]/th:text-ttb03-blue focus-visible:outline-2 focus-visible:outline-ttb03-blue">Revenue
                <svg class="size-3.5 opacity-50 transition group-aria-[sort=ascending]/th:opacity-100 group-aria-[sort=descending]/th:rotate-180 group-aria-[sort=descending]/th:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
              </button>
            </th>
            <th scope="col"><span class="sr-only">Actions</span></th>
          </tr>
        </thead>
        <tbody class="divide-y divide-ttb03-line [&_td]:px-4 [&_td]:py-3 [&_tr]:transition-colors [&_tr:hover]:bg-ttb03-blue/5">
          <tr data-status="active" data-name="arya kapoor" data-revenue="4280">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-indigo-500 to-cyan-400 text-xs font-semibold text-white">AK</span><div><div class="font-semibold">Arya Kapoor</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_8841</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-purple/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-purple">Enterprise</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-green/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-green ring-1 ring-ttb03-green/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Active</span></td>
            <td class="text-ttb03-mut">2 min ago</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-green tabular-nums">$4,280</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit Arya Kapoor" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for Arya Kapoor" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-status="pending" data-name="marcus reid" data-revenue="290">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-amber-400 to-red-500 text-xs font-semibold text-white">MR</span><div><div class="font-semibold">Marcus Reid</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_7722</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-blue/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-blue">Pro</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-yellow/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-yellow ring-1 ring-ttb03-yellow/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Pending</span></td>
            <td class="text-ttb03-mut">1 hr ago</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-ink tabular-nums">$290</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit Marcus Reid" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for Marcus Reid" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-status="active" data-name="selin novak" data-revenue="580">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-emerald-500 to-cyan-500 text-xs font-semibold text-white">SN</span><div><div class="font-semibold">Selin Novak</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_6610</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-blue/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-blue">Pro</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-green/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-green ring-1 ring-ttb03-green/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Active</span></td>
            <td class="text-ttb03-mut">4 hrs ago</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-green tabular-nums">$580</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit Selin Novak" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for Selin Novak" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-status="trial" data-name="theo walsh" data-revenue="0">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-violet-500 to-pink-500 text-xs font-semibold text-white">TW</span><div><div class="font-semibold">Theo Walsh</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_5503</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-surface2 px-2 py-0.5 text-[11px] font-semibold text-ttb03-mut">Free</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-purple/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-purple ring-1 ring-ttb03-purple/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Trial</span></td>
            <td class="text-ttb03-mut">2 days ago</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-mut tabular-nums">$0</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit Theo Walsh" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for Theo Walsh" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-status="banned" data-name="lena kim" data-revenue="-120">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-rose-500 to-rose-300 text-xs font-semibold text-white">LK</span><div><div class="font-semibold">Lena Kim</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_4491</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-surface2 px-2 py-0.5 text-[11px] font-semibold text-ttb03-mut">Free</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-red/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-red ring-1 ring-ttb03-red/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Banned</span></td>
            <td class="text-ttb03-mut">14 days ago</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-red tabular-nums">−$120</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit Lena Kim" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for Lena Kim" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-status="active" data-name="james park" data-revenue="12400">
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-sky-500 to-sky-300 text-xs font-semibold text-white">JP</span><div><div class="font-semibold">James Park</div><div class="font-ttb03-mono text-[11px] text-ttb03-mut">#usr_3380</div></div></div></td>
            <td class="text-ttb03-mut">[email protected]</td>
            <td><span class="rounded-md bg-ttb03-purple/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-purple">Enterprise</span></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-ttb03-green/12 px-2 py-0.5 text-[11px] font-semibold text-ttb03-green ring-1 ring-ttb03-green/30"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Active</span></td>
            <td class="text-ttb03-mut">Just now</td>
            <td class="text-right font-ttb03-mono font-medium text-ttb03-green tabular-nums">$12,400</td>
            <td><div class="flex justify-end gap-1"><button type="button" aria-label="Edit James Park" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg></button><button type="button" aria-label="More actions for James Park" class="relative grid size-8 place-items-center rounded-md text-ttb03-mut ring-1 ring-ttb03-line transition after:absolute after:-inset-1.5 hover:text-ttb03-blue hover:ring-ttb03-blue/60 focus-visible:outline-2 focus-visible:outline-ttb03-blue"><svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg></button></div></td>
          </tr>
          <tr data-empty hidden><td colspan="7" class="py-12! text-center text-ttb03-mut">No users match this filter.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb03-bg: #0d1117;
  --color-ttb03-bg: oklch(0.18 0.012 260);
  --color-ttb03-surface: #161b22;
  --color-ttb03-surface: oklch(0.21 0.013 260);
  --color-ttb03-surface2: #21262d;
  --color-ttb03-surface2: oklch(0.26 0.012 260);
  --color-ttb03-line: #30363d;
  --color-ttb03-line: oklch(0.34 0.012 260);
  --color-ttb03-ink: #e6edf3;
  --color-ttb03-ink: oklch(0.94 0.01 240);
  --color-ttb03-mut: #9198a1;
  --color-ttb03-mut: oklch(0.68 0.015 250);
  --color-ttb03-blue: #58a6ff;
  --color-ttb03-blue: oklch(0.72 0.15 255);
  --color-ttb03-green: #3fb950;
  --color-ttb03-green: oklch(0.7 0.17 145);
  --color-ttb03-yellow: #d29922;
  --color-ttb03-yellow: oklch(0.71 0.14 80);
  --color-ttb03-red: #f85149;
  --color-ttb03-red: oklch(0.66 0.2 25);
  --color-ttb03-purple: #bc8cff;
  --color-ttb03-purple: oklch(0.73 0.15 300);
  --font-ttb03-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-ttb03-mono: 'IBM Plex Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('ttb03-grid');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const body = root.querySelector('tbody');
  const rows = Array.from(body.querySelectorAll('tr[data-status]'));
  const empty = body.querySelector('[data-empty]');
  const count = root.querySelector('[data-count]');
  const search = root.querySelector('input[type="search"]');
  let filter = 'all';
  const apply = () => {
    const q = search.value.trim().toLowerCase();
    let n = 0;
    rows.forEach((r) => {
      const ok = (filter === 'all' || r.dataset.status === filter) && r.textContent.toLowerCase().includes(q);
      r.hidden = !ok;
      if (ok) n++;
    });
    empty.hidden = n !== 0;
    count.textContent = n + (n === 1 ? ' user' : ' users');
  };
  root.querySelectorAll('[data-filter]').forEach((btn) => btn.addEventListener('click', () => {
    root.querySelectorAll('[data-filter]').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
    filter = btn.dataset.filter;
    apply();
  }));
  search.addEventListener('input', apply);
  root.querySelectorAll('[data-sort]').forEach((btn) => btn.addEventListener('click', () => {
    const th = btn.closest('th');
    const dir = th.getAttribute('aria-sort') === 'ascending' ? 'descending' : 'ascending';
    root.querySelectorAll('th[aria-sort]').forEach((t) => t.setAttribute('aria-sort', 'none'));
    th.setAttribute('aria-sort', dir);
    const key = btn.dataset.sort;
    const val = (r) => key === 'revenue' ? Number(r.dataset.revenue) : r.dataset.name;
    rows.sort((a, b) => {
      const x = val(a), y = val(b);
      const c = x > y ? 1 : x < y ? -1 : 0;
      return dir === 'ascending' ? c : -c;
    });
    rows.forEach((r) => body.insertBefore(r, empty));
  }));
  apply();
})();
```
