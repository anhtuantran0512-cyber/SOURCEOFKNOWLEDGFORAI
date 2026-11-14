---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-notification-preferences-page/"
title: "Tailwind Notification Preferences Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A notification matrix that respects attention: event types grouped down the side, Email, Push, In-app and Slack across the top, mini-switch cells on real…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Notification Preferences Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-notification-preferences-page/

A notification matrix that respects attention: event types grouped down the side, Email, Push, In-app and Slack across the top, mini-switch cells on real checkboxes, column master toggles with true indeterminate state, a locked security row, a Pause-all switch that dims and disables the matrix, digest frequency, quiet hours that reveal their time pickers, and quiet autosave.
## HTML
```html
<section data-tsp12 class="tsp-12 group/np w-full min-h-svh bg-tsp12-bg px-4 py-10 font-tsp12-sans text-tsp12-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-12-h">
  <form data-form class="mx-auto grid w-full max-w-5xl gap-6">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-12-h" class="text-3xl font-extrabold tracking-tight">Notifications</h1><p class="mt-1 text-tsp12-mut">Choose what reaches you, and where.</p></div>
      <p data-saved role="status" aria-live="polite" class="flex min-h-8 items-center gap-1.5 text-sm font-semibold text-emerald-700 opacity-0 transition-opacity data-show:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg><span>Saved</span></p>
    </header>

    <div class="flex flex-wrap items-center gap-4 rounded-3xl border border-tsp12-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)]">
      <span class="grid size-11 flex-none place-items-center rounded-2xl bg-tsp12-acc/10 text-tsp12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0M3 3l18 18"/></svg></span>
      <div class="min-w-0 flex-1"><p class="font-bold">Pause all notifications</p><p class="text-sm text-tsp12-mut">Security alerts still come through.</p></div>
      <select name="pauseFor" aria-label="Pause duration" class="min-h-11 rounded-xl border border-tsp12-line bg-white px-3 text-sm outline-none focus:ring-4 focus:ring-tsp12-acc/15"><option>For 1 hour</option><option selected>Until tomorrow</option><option>For a week</option></select>
      <label class="relative flex-none cursor-pointer"><span class="sr-only">Pause all notifications</span><input id="tsp-12-pause" name="pause" type="checkbox" role="switch" class="peer sr-only"><span class="block h-7 w-12 rounded-full bg-zinc-300 transition peer-checked:bg-tsp12-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp12-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-6 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></label>
    </div>

    <p class="hidden items-center gap-2 rounded-2xl bg-tsp12-ink px-4 py-3 text-sm font-medium text-white group-has-[#tsp-12-pause:checked]/np:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor" class="size-4"><path d="M7 5h3v14H7zM14 5h3v14h-3z"/></svg>Notifications are paused. You'll catch up on everything when they resume.</p>

    <div data-matrix class="overflow-x-auto rounded-3xl border border-tsp12-line bg-white shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition group-has-[#tsp-12-pause:checked]/np:pointer-events-none group-has-[#tsp-12-pause:checked]/np:opacity-40 group-has-[#tsp-12-pause:checked]/np:grayscale">
      <table data-table class="w-full min-w-[40rem] border-collapse text-sm">
        <thead><tr class="border-b border-tsp12-line">
          <th scope="col" class="w-[44%] px-5 py-4 text-left text-xs font-bold uppercase tracking-wide text-tsp12-mut">Event</th>
          <th scope="col" class="px-2 py-4"><label class="grid cursor-pointer justify-items-center gap-1.5 font-bold"><span class="flex items-center gap-1.5"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tsp12-mut"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>Email</span><input type="checkbox" data-master class="size-4 accent-tsp12-acc" aria-label="Toggle all email notifications"></label></th>
          <th scope="col" class="px-2 py-4"><label class="grid cursor-pointer justify-items-center gap-1.5 font-bold"><span class="flex items-center gap-1.5"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tsp12-mut"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></svg>Push</span><input type="checkbox" data-master class="size-4 accent-tsp12-acc" aria-label="Toggle all push notifications"></label></th>
          <th scope="col" class="px-2 py-4"><label class="grid cursor-pointer justify-items-center gap-1.5 font-bold"><span class="flex items-center gap-1.5"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tsp12-mut"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>In-app</span><input type="checkbox" data-master class="size-4 accent-tsp12-acc" aria-label="Toggle all in-app notifications"></label></th>
          <th scope="col" class="px-2 py-4"><label class="grid cursor-pointer justify-items-center gap-1.5 font-bold"><span class="flex items-center gap-1.5"><span class="grid size-4 place-items-center rounded bg-[#4a154b] text-[9px] font-extrabold text-white">#</span>Slack</span><input type="checkbox" data-master class="size-4 accent-tsp12-acc" aria-label="Toggle all Slack notifications"></label></th>
        </tr></thead>
        <tbody data-body class="[&_tr[data-row]]:border-t [&_tr[data-row]]:border-tsp12-line [&_tr[data-row]:hover]:bg-tsp12-bg/60"></tbody>
      </table>
    </div>

    <div class="grid gap-6 md:grid-cols-2">
      <fieldset class="grid content-start gap-2 rounded-3xl border border-tsp12-line bg-white p-6">
        <legend class="sr-only">Email delivery</legend>
        <p class="mb-2 font-bold">Email delivery</p>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 transition has-checked:bg-tsp12-acc/8 has-checked:font-semibold"><input type="radio" name="digest" value="instant" class="size-4 accent-tsp12-acc" checked>Instantly</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 transition has-checked:bg-tsp12-acc/8 has-checked:font-semibold"><input type="radio" name="digest" value="hourly" class="size-4 accent-tsp12-acc">Hourly digest</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 transition has-checked:bg-tsp12-acc/8 has-checked:font-semibold"><input type="radio" name="digest" value="daily" class="size-4 accent-tsp12-acc">Daily digest at 9:00 AM</label>
      </fieldset>
      <div class="grid content-start gap-4 rounded-3xl border border-tsp12-line bg-white p-6">
        <label class="flex min-h-11 cursor-pointer items-center justify-between gap-3"><span><span class="block font-bold">Quiet hours</span><span class="block text-sm text-tsp12-mut">Hold push notifications overnight.</span></span><span class="relative flex-none"><input id="tsp-12-quiet" name="quiet" type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp12-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp12-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
        <div class="hidden grid-cols-2 gap-3 group-has-[#tsp-12-quiet:checked]/np:grid">
          <label class="grid gap-1.5 text-sm"><span class="font-semibold">From</span><input type="time" name="from" value="22:00" class="min-h-11 rounded-xl border border-tsp12-line px-3 outline-none focus:ring-4 focus:ring-tsp12-acc/15"></label>
          <label class="grid gap-1.5 text-sm"><span class="font-semibold">Until</span><input type="time" name="until" value="07:00" class="min-h-11 rounded-xl border border-tsp12-line px-3 outline-none focus:ring-4 focus:ring-tsp12-acc/15"></label>
        </div>
      </div>
    </div>
  </form>
  <template data-tpl-group><tr><th scope="colgroup" colspan="5" class="bg-tsp12-bg px-5 py-2.5 text-left text-xs font-bold uppercase tracking-[0.12em] text-tsp12-mut"></th></tr></template>
  <template data-tpl-row><tr data-row><th scope="row" class="px-5 py-2 text-left font-normal"><span data-name class="block font-semibold"></span><span data-hint class="block text-xs text-tsp12-mut"></span></th></tr></template>
  <template data-tpl-cell><td class="px-2 text-center"><label class="mx-auto grid h-11 w-14 cursor-pointer place-items-center has-disabled:cursor-not-allowed"><span class="relative"><input type="checkbox" class="peer sr-only"><span class="block h-5 w-9 rounded-full bg-zinc-200 transition peer-checked:bg-tsp12-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp12-acc peer-disabled:opacity-60"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-4 rounded-full bg-white shadow-sm transition peer-checked:translate-x-4"></span></span></label></td></template>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp12-bg: #faf6f7;
  --color-tsp12-bg: oklch(0.976 0.005 10);
  --color-tsp12-ink: #22161a;
  --color-tsp12-ink: oklch(0.22 0.02 5);
  --color-tsp12-mut: #6e5f64;
  --color-tsp12-mut: oklch(0.52 0.022 0);
  --color-tsp12-line: #eee4e7;
  --color-tsp12-line: oklch(0.928 0.01 0);
  --color-tsp12-acc: #e11d48;
  --color-tsp12-acc: oklch(0.586 0.222 17);
  --font-tsp12-sans: 'Hanken Grotesk', system-ui, sans-serif;
}

.tsp-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp12]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const ROWS = [
    ['Activity', [['Mentions', 'Someone @mentions you', '1111'], ['Replies', 'Replies to your comments', '1110'], ['Assigned to me', 'Tasks assigned to you', '1111']]],
    ['Projects', [['Status changes', 'A project you follow moves stage', '0010'], ['Due soon', 'Reminders 24 hours before a due date', '1110']]],
    ['Billing', [['Invoices', 'A new invoice is ready', '1000'], ['Failed payments', 'A charge was declined', '1110']]],
    ['Security', [['New sign-in', 'Always on — we can\'t let you miss these', '1100', true]]],
  ];
  const CH = ['email', 'push', 'in-app', 'Slack'];
  const body = root.querySelector('[data-body]');
  const tpl = (k) => root.querySelector('[data-tpl-' + k + ']').content.firstElementChild;
  ROWS.forEach(([g, rows]) => {
    const gr = tpl('group').cloneNode(true); gr.querySelector('th').textContent = g; body.appendChild(gr);
    rows.forEach(([name, hint, bits, locked]) => {
      const tr = tpl('row').cloneNode(true);
      tr.querySelector('[data-name]').textContent = name;
      tr.querySelector('[data-hint]').textContent = hint;
      bits.split('').forEach((b, i) => {
        const td = tpl('cell').cloneNode(true);
        const cb = td.querySelector('input');
        cb.checked = b === '1';
        cb.setAttribute('aria-label', name + ' by ' + CH[i]);
        if (locked && b === '1') cb.disabled = true;
        tr.appendChild(td);
      });
      body.appendChild(tr);
    });
  });
  const masters = [...root.querySelectorAll('[data-master]')];
  const col = (i) => [...body.querySelectorAll('[data-row]')].map((r) => r.cells[i + 1].querySelector('input'));
  const sync = () => masters.forEach((m, i) => {
    const cells = col(i), on = cells.filter((c) => c.checked).length;
    m.checked = on === cells.length;
    m.indeterminate = on > 0 && on < cells.length;
  });
  masters.forEach((m, i) => m.addEventListener('change', () => { col(i).forEach((c) => { if (!c.disabled) c.checked = m.checked; }); sync(); }));
  const saved = root.querySelector('[data-saved]');
  let t;
  root.querySelector('[data-form]').addEventListener('change', (e) => {
    if (e.target.closest('[data-body]')) sync();
    if (e.target.id === 'tsp-12-pause') root.querySelector('[data-matrix]').inert = e.target.checked;
    saved.dataset.show = '';
    clearTimeout(t);
    t = setTimeout(() => delete saved.dataset.show, 1600);
  });
  sync();
})();
```
