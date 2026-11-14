---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-danger-zone-delete-account/"
title: "Tailwind Danger Zone Delete Account"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A responsible danger zone: transfer ownership, archive (reversible) and delete, each with its consequence spelled out."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Danger Zone Delete Account
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-danger-zone-delete-account/

A responsible danger zone: transfer ownership, archive (reversible) and delete, each with its consequence spelled out. Delete opens a native dialog that lists exactly what will be lost, offers an export first, asks for a reason, requires typing the workspace name, and then a press-and-hold button — ending in a 30-day soft delete you can undo.
## HTML
```html
<section data-tsp18 class="tsp-18 group/page w-full min-h-svh bg-tsp18-bg px-4 py-10 font-tsp18-sans text-tsp18-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-18-h">
  <div class="mx-auto grid w-full max-w-4xl gap-6">
    <header><p class="text-sm font-semibold text-tsp18-mut">Settings · Workspace</p><h1 id="tsp-18-h" class="mt-1 text-3xl font-bold tracking-tight">Danger zone</h1><p class="mt-1 text-tsp18-mut">Actions here affect everyone in <strong class="font-semibold text-tsp18-ink">Northwind</strong>. Read each one carefully.</p></header>

    <div class="overflow-hidden rounded-3xl border border-tsp18-acc/30 bg-white shadow-[0_0_0_4px_var(--color-tsp18-glow)]">
      <div class="flex flex-wrap items-center gap-4 border-b border-tsp18-line p-5 sm:p-6">
        <div class="min-w-0 flex-1"><h2 class="font-bold">Transfer ownership</h2><p class="text-sm text-tsp18-mut">The new owner gets billing and can remove you. You'll become an Admin.</p></div>
        <div class="flex flex-wrap gap-2"><select data-owner aria-label="New owner" class="min-h-11 rounded-xl border border-tsp18-line bg-white px-3 text-sm outline-none focus:ring-4 focus:ring-tsp18-acc/15"><option value="">Choose an admin…</option><option>Noah Patel</option><option>Priya Shah</option></select><button type="button" data-transfer disabled class="min-h-11 rounded-xl border border-tsp18-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp18-bg focus-visible:outline-2 focus-visible:outline-tsp18-acc disabled:cursor-not-allowed disabled:opacity-40">Transfer</button></div>
      </div>
      <div class="flex flex-wrap items-center gap-4 border-b border-tsp18-line p-5 sm:p-6">
        <div class="min-w-0 flex-1"><h2 class="flex items-center gap-2 font-bold">Archive workspace <span data-archived-badge hidden class="rounded-full bg-amber-100 px-2 py-0.5 text-[11px] font-bold text-amber-800">Archived</span></h2><p class="text-sm text-tsp18-mut">Read-only for everyone, billing paused. Restore any time within 90 days.</p></div>
        <button type="button" data-archive class="min-h-11 rounded-xl border border-tsp18-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp18-bg focus-visible:outline-2 focus-visible:outline-tsp18-acc data-armed:border-amber-300 data-armed:bg-amber-50 data-armed:text-amber-900">Archive</button>
      </div>
      <div class="flex flex-wrap items-center gap-4 bg-tsp18-glow/50 p-5 sm:p-6">
        <div class="min-w-0 flex-1"><h2 class="flex items-center gap-2 font-bold text-tsp18-acc">Delete workspace <span data-scheduled-badge hidden class="rounded-full bg-tsp18-acc px-2 py-0.5 text-[11px] font-bold text-white">Deletion scheduled</span></h2><p class="text-sm text-tsp18-mut">Permanently remove all projects, files and members after a 30-day grace period.</p></div>
        <button type="button" data-open class="min-h-11 rounded-xl bg-tsp18-acc px-4 text-sm font-semibold text-white shadow-[0_8px_20px_-10px_var(--color-tsp18-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp18-acc">Delete workspace…</button>
      </div>
    </div>
    <p data-status role="status" aria-live="polite" class="text-sm font-medium text-tsp18-mut empty:hidden"></p>
  </div>

  <dialog data-dialog data-step="confirm" aria-labelledby="tsp-18-dh" class="group/dz m-auto w-[min(32rem,calc(100%-2rem))] rounded-3xl bg-white p-0 text-tsp18-ink shadow-2xl transition-[opacity,translate,display,overlay] transition-discrete duration-300 backdrop:bg-tsp18-ink/60 backdrop:backdrop-blur-sm starting:open:translate-y-4 starting:open:opacity-0 motion-reduce:transition-none">
    <form data-form class="grid gap-5 p-6 group-data-[step=done]/dz:hidden sm:p-7" novalidate>
      <div class="flex items-start gap-4"><span class="grid size-11 flex-none place-items-center rounded-full bg-tsp18-glow text-tsp18-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg></span><div><h2 id="tsp-18-dh" class="text-lg font-bold">Delete Northwind?</h2><p class="mt-1 text-sm text-tsp18-mut">After 30 days this can't be undone. Here's what goes:</p></div></div>
      <ul class="grid grid-cols-3 gap-2 text-center">
        <li class="rounded-2xl bg-tsp18-bg p-3"><p class="text-xl font-bold tabular-nums">14</p><p class="text-xs text-tsp18-mut">projects</p></li>
        <li class="rounded-2xl bg-tsp18-bg p-3"><p class="text-xl font-bold tabular-nums">2.5 GB</p><p class="text-xs text-tsp18-mut">of files</p></li>
        <li class="rounded-2xl bg-tsp18-bg p-3"><p class="text-xl font-bold tabular-nums">9</p><p class="text-xs text-tsp18-mut">members lose access</p></li>
      </ul>
      <a href="#tsp-18-h" class="flex min-h-11 items-center justify-between gap-3 rounded-2xl border border-tsp18-line px-4 text-sm font-semibold transition hover:bg-tsp18-bg focus-visible:outline-2 focus-visible:outline-tsp18-acc">Export your data first<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      <label class="grid gap-1.5 text-sm"><span class="font-semibold">Why are you leaving? <span class="font-normal text-tsp18-mut">optional</span></span><select name="reason" class="min-h-11 rounded-xl border border-tsp18-line bg-white px-3 outline-none focus:ring-4 focus:ring-tsp18-acc/15"><option value="">Choose a reason</option><option>Too expensive</option><option>Missing features</option><option>Switching tools</option><option>Project ended</option></select></label>
      <label class="grid gap-1.5 text-sm"><span class="font-semibold">Type <code class="rounded bg-tsp18-bg px-1.5 py-0.5 font-tsp18-mono text-[13px]">northwind</code> to confirm</span><span class="relative"><input data-confirm name="confirm" required pattern="northwind" autocomplete="off" autocapitalize="off" spellcheck="false" class="peer min-h-11 w-full rounded-xl border border-tsp18-line px-3.5 pr-10 font-tsp18-mono text-sm outline-none transition focus:border-tsp18-acc focus:ring-4 focus:ring-tsp18-acc/15 valid:border-emerald-500 valid:ring-4 valid:ring-emerald-500/15"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-3 top-1/2 size-4 -translate-y-1/2 text-emerald-600 opacity-0 transition peer-valid:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
      <div class="grid gap-2">
        <button type="button" data-hold disabled class="group/hold relative min-h-12 overflow-hidden rounded-xl bg-tsp18-ink text-sm font-semibold text-white transition focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp18-acc disabled:cursor-not-allowed disabled:opacity-40 select-none touch-none"><span aria-hidden="true" class="absolute inset-0 origin-left scale-x-0 bg-tsp18-acc transition-transform duration-300 ease-out group-data-holding/hold:scale-x-100 group-data-holding/hold:duration-[1600ms] group-data-holding/hold:ease-linear"></span><span class="relative"><span class="group-data-holding/hold:hidden">Press and hold to delete</span><span class="hidden group-data-holding/hold:inline">Keep holding…</span></span></button>
        <button type="button" data-cancel class="min-h-11 rounded-xl text-sm font-semibold text-tsp18-mut transition hover:text-tsp18-ink focus-visible:outline-2 focus-visible:outline-tsp18-acc">Cancel</button>
      </div>
    </form>
    <div class="hidden justify-items-center gap-4 p-7 text-center group-data-[step=done]/dz:grid">
      <span class="grid size-14 place-items-center rounded-full bg-tsp18-glow text-tsp18-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2M9 2h6"/></svg></span>
      <h2 class="text-lg font-bold">Deletion scheduled for <span data-date>Nov 6, 2026</span></h2>
      <p class="max-w-sm text-pretty text-sm text-tsp18-mut">Members lose access now. We've emailed every admin. Change your mind before then and everything comes back exactly as it was.</p>
      <div class="flex flex-wrap justify-center gap-2"><button type="button" data-undo class="min-h-11 rounded-xl border border-tsp18-line bg-white px-5 text-sm font-semibold shadow-xs transition hover:bg-tsp18-bg focus-visible:outline-2 focus-visible:outline-tsp18-acc">Undo — keep workspace</button><button type="button" data-close class="min-h-11 rounded-xl bg-tsp18-ink px-5 text-sm font-semibold text-white transition hover:bg-tsp18-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp18-acc">Close</button></div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp18-bg: #f7f5f5;
  --color-tsp18-bg: oklch(0.974 0.003 17);
  --color-tsp18-ink: #1c1517;
  --color-tsp18-ink: oklch(0.205 0.012 0);
  --color-tsp18-mut: #6a5f62;
  --color-tsp18-mut: oklch(0.51 0.016 0);
  --color-tsp18-line: #ece5e6;
  --color-tsp18-line: oklch(0.925 0.007 10);
  --color-tsp18-acc: #dc2626;
  --color-tsp18-acc: oklch(0.577 0.215 27);
  --color-tsp18-glow: #fdeaea;
  --color-tsp18-glow: oklch(0.95 0.025 20);
  --font-tsp18-sans: 'Rethink Sans', system-ui, sans-serif;
  --font-tsp18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsp-18 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp18]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const HOLD_MS = 1600;
  const $ = (s) => root.querySelector(s);
  const status = $('[data-status]');
  const owner = $('[data-owner]'), transfer = $('[data-transfer]');
  owner.addEventListener('change', () => { transfer.disabled = !owner.value; });
  transfer.addEventListener('click', () => { status.textContent = 'Transfer request sent to ' + owner.value + '. Ownership moves when they accept.'; transfer.disabled = true; });
  const archive = $('[data-archive]');
  let armT;
  archive.addEventListener('click', () => {
    if (archive.textContent === 'Restore') { archive.textContent = 'Archive'; $('[data-archived-badge]').hidden = true; status.textContent = 'Workspace restored.'; return; }
    if (!archive.hasAttribute('data-armed')) { archive.dataset.armed = ''; archive.textContent = 'Confirm archive'; clearTimeout(armT); armT = setTimeout(() => { delete archive.dataset.armed; if (archive.textContent === 'Confirm archive') archive.textContent = 'Archive'; }, 3500); return; }
    delete archive.dataset.armed; archive.textContent = 'Restore';
    $('[data-archived-badge]').hidden = false;
    status.textContent = 'Workspace archived. It is read-only until restored.';
  });
  const dlg = $('[data-dialog]'), form = $('[data-form]'), confirm = $('[data-confirm]'), hold = $('[data-hold]');
  $('[data-open]').addEventListener('click', () => { form.reset(); hold.disabled = true; dlg.dataset.step = 'confirm'; dlg.showModal(); setTimeout(() => confirm.focus(), 50); });
  $('[data-cancel]').addEventListener('click', () => dlg.close());
  $('[data-close]').addEventListener('click', () => dlg.close());
  confirm.addEventListener('input', () => { hold.disabled = !confirm.validity.valid; });
  let t;
  const start = (e) => {
    if (hold.disabled || hold.hasAttribute('data-holding')) return;
    if (e.type === 'keydown' && e.key !== ' ' && e.key !== 'Enter') return;
    e.preventDefault();
    hold.dataset.holding = '';
    t = setTimeout(finish, matchMedia('(prefers-reduced-motion: reduce)').matches ? 400 : HOLD_MS);
  };
  const stop = (e) => { if (e && e.type === 'keyup' && e.key !== ' ' && e.key !== 'Enter') return; clearTimeout(t); delete hold.dataset.holding; };
  const finish = () => {
    delete hold.dataset.holding;
    const d = new Date(); d.setDate(d.getDate() + 30);
    $('[data-date]').textContent = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    dlg.dataset.step = 'done';
    $('[data-scheduled-badge]').hidden = false;
    status.textContent = 'Workspace scheduled for deletion on ' + $('[data-date]').textContent + '.';
  };
  hold.addEventListener('pointerdown', start);
  hold.addEventListener('keydown', start);
  ['pointerup', 'pointerleave', 'pointercancel', 'keyup', 'blur'].forEach((ev) => hold.addEventListener(ev, stop));
  $('[data-undo]').addEventListener('click', () => { $('[data-scheduled-badge]').hidden = true; status.textContent = 'Deletion cancelled. Northwind is safe.'; dlg.close(); });
})();
```
