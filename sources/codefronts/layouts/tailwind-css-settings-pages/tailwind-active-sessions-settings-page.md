---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-active-sessions-settings-page/"
title: "Tailwind Active Sessions Settings Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A security-first sessions page: the current device pinned at the top with a live animate-ping pulse, every other session listed with device, app, location,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Active Sessions Settings Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-active-sessions-settings-page/

A security-first sessions page: the current device pinned at the top with a live animate-ping pulse, every other session listed with device, app, location, IP and last activity, an unrecognised sign-in flagged in amber with a secure-account shortcut, per-session sign out that collapses the row, a staggered 'sign out everywhere else', and an empty state that appears on its own.
## HTML
```html
<section data-tsp11 class="tsp-11 group/s w-full min-h-svh bg-tsp11-bg px-4 py-10 font-tsp11-sans text-tsp11-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-11-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8 lg:grid-cols-[minmax(0,1fr)_20rem]">
    <div class="grid min-w-0 content-start gap-6">
      <header><h1 id="tsp-11-h" class="text-3xl font-bold tracking-tight">Where you're signed in</h1><p class="mt-1 text-tsp11-mut">Review devices with access to your account. Sign out anything you don't recognise.</p></header>

      <article class="relative overflow-hidden rounded-3xl bg-tsp11-ink p-6 text-white shadow-[0_24px_60px_-30px_rgb(15_23_42/0.6)]" aria-label="This device">
        <div aria-hidden="true" class="pointer-events-none absolute -right-16 -top-20 size-64 rounded-full bg-tsp11-acc/40 blur-3xl"></div>
        <div class="relative flex flex-wrap items-center gap-4">
          <span class="grid size-12 place-items-center rounded-2xl bg-white/10 ring-1 ring-white/15"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/></svg></span>
          <div class="min-w-0 flex-1"><p class="font-semibold">MacBook Pro · Chrome 129</p><p class="text-sm text-white/65">San Francisco, US · 73.15.••.•• · macOS 15</p></div>
          <span class="inline-flex items-center gap-2 rounded-full bg-emerald-400/15 px-3 py-1.5 text-sm font-semibold text-emerald-300 ring-1 ring-emerald-400/25"><span class="relative flex size-2.5"><span class="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75 motion-reduce:hidden"></span><span class="relative inline-flex size-2.5 rounded-full bg-emerald-400"></span></span>This device</span>
        </div>
      </article>

      <div class="flex flex-wrap items-center justify-between gap-3">
        <h2 class="text-lg font-bold">Other sessions <span data-count class="ml-1 rounded-full bg-tsp11-line px-2 py-0.5 text-xs font-bold tabular-nums text-tsp11-mut">5</span></h2>
        <button type="button" data-all class="inline-flex min-h-11 items-center gap-2 rounded-xl border border-rose-200 bg-white px-4 text-sm font-semibold text-rose-700 shadow-xs transition hover:bg-rose-50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-rose-500 group-data-empty/s:hidden">Sign out of all other sessions</button>
      </div>

      <ul data-list class="grid gap-3 group-data-empty/s:hidden">
        <li data-session class="grid grid-rows-[1fr] transition-all duration-300 data-gone:grid-rows-[0fr] data-gone:translate-x-4 data-gone:opacity-0 motion-reduce:transition-none"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-4 rounded-2xl border border-tsp11-line bg-white p-4 sm:p-5">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp11-bg text-tsp11-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></svg></span>
          <div class="min-w-0 flex-1"><p class="font-semibold">iPhone 15 · Safari</p><p class="text-sm text-tsp11-mut">San Francisco, US · 73.15.••.•• · Active 5 min ago</p></div>
          <button type="button" data-out class="min-h-11 rounded-xl px-4 text-sm font-semibold text-tsp11-mut transition hover:bg-rose-50 hover:text-rose-700 focus-visible:outline-2 focus-visible:outline-tsp11-acc">Sign out</button>
        </div></div></li>
        <li data-session class="grid grid-rows-[1fr] transition-all duration-300 data-gone:grid-rows-[0fr] data-gone:translate-x-4 data-gone:opacity-0 motion-reduce:transition-none"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-4 rounded-2xl border-2 border-amber-300 bg-amber-50/60 p-4 sm:p-5">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-amber-100 text-amber-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span>
          <div class="min-w-0 flex-1"><p class="flex flex-wrap items-center gap-2 font-semibold">Windows PC · Edge 128 <span class="rounded-full bg-amber-200 px-2 py-0.5 text-[11px] font-bold text-amber-900">New location</span></p><p class="text-sm text-tsp11-mut">London, UK · 81.2.••.•• · Signed in 3 days ago</p><a href="#tsp-11-h" class="mt-1 inline-flex min-h-8 items-center text-sm font-semibold text-amber-800 underline underline-offset-4 hover:text-amber-950">Not you? Secure your account</a></div>
          <button type="button" data-out class="min-h-11 rounded-xl bg-amber-600 px-4 text-sm font-semibold text-white transition hover:bg-amber-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-amber-600">Sign out</button>
        </div></div></li>
        <li data-session class="grid grid-rows-[1fr] transition-all duration-300 data-gone:grid-rows-[0fr] data-gone:translate-x-4 data-gone:opacity-0 motion-reduce:transition-none"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-4 rounded-2xl border border-tsp11-line bg-white p-4 sm:p-5">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp11-bg text-tsp11-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M11 18h2"/></svg></span>
          <div class="min-w-0 flex-1"><p class="font-semibold">iPad Air · Northwind app</p><p class="text-sm text-tsp11-mut">Oakland, US · 98.42.••.•• · 2 hours ago</p></div>
          <button type="button" data-out class="min-h-11 rounded-xl px-4 text-sm font-semibold text-tsp11-mut transition hover:bg-rose-50 hover:text-rose-700 focus-visible:outline-2 focus-visible:outline-tsp11-acc">Sign out</button>
        </div></div></li>
        <li data-session class="grid grid-rows-[1fr] transition-all duration-300 data-gone:grid-rows-[0fr] data-gone:translate-x-4 data-gone:opacity-0 motion-reduce:transition-none"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-4 rounded-2xl border border-tsp11-line bg-white p-4 sm:p-5">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp11-bg text-tsp11-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/></svg></span>
          <div class="min-w-0 flex-1"><p class="font-semibold">ThinkPad · Firefox 131</p><p class="text-sm text-tsp11-mut">Berlin, DE · 89.0.••.•• · 2 weeks ago</p></div>
          <button type="button" data-out class="min-h-11 rounded-xl px-4 text-sm font-semibold text-tsp11-mut transition hover:bg-rose-50 hover:text-rose-700 focus-visible:outline-2 focus-visible:outline-tsp11-acc">Sign out</button>
        </div></div></li>
        <li data-session class="grid grid-rows-[1fr] transition-all duration-300 data-gone:grid-rows-[0fr] data-gone:translate-x-4 data-gone:opacity-0 motion-reduce:transition-none"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-4 rounded-2xl border border-tsp11-line bg-white p-4 sm:p-5">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp11-bg text-tsp11-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m4 17 6-6-6-6M12 19h8"/></svg></span>
          <div class="min-w-0 flex-1"><p class="font-semibold">Northwind CLI v2.4</p><p class="text-sm text-tsp11-mut">GitHub Actions runner · 140.82.••.•• · 1 month ago</p></div>
          <button type="button" data-out class="min-h-11 rounded-xl px-4 text-sm font-semibold text-tsp11-mut transition hover:bg-rose-50 hover:text-rose-700 focus-visible:outline-2 focus-visible:outline-tsp11-acc">Sign out</button>
        </div></div></li>
      </ul>
      <div class="hidden items-center gap-4 rounded-2xl border border-dashed border-tsp11-line bg-white p-6 group-data-empty/s:flex">
        <span class="grid size-11 flex-none place-items-center rounded-full bg-emerald-100 text-emerald-600"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M20 6 9 17l-5-5"/></svg></span>
        <div><p class="font-semibold">Only this device is signed in</p><p class="text-sm text-tsp11-mut">Everywhere else will need your password and 2FA code to get back in.</p></div>
      </div>
      <p data-status role="status" aria-live="polite" class="text-sm text-tsp11-mut empty:hidden"></p>
    </div>

    <aside class="grid content-start gap-4">
      <div class="grid gap-4 rounded-3xl border border-tsp11-line bg-white p-6">
        <h2 class="font-bold">Session security</h2>
        <label class="grid gap-1.5 text-sm"><span class="font-semibold">Sign out after inactivity</span><select class="min-h-11 rounded-xl border border-tsp11-line bg-white px-3 outline-none focus:ring-4 focus:ring-tsp11-acc/15"><option>Never</option><option>After 1 day</option><option selected>After 30 days</option></select></label>
        <label class="flex min-h-11 cursor-pointer items-center justify-between gap-3 text-sm"><span class="font-semibold">Email me on new sign-ins</span><span class="relative flex-none"><input type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp11-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp11-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
        <label class="flex min-h-11 cursor-pointer items-center justify-between gap-3 text-sm"><span class="font-semibold">Re-confirm for sensitive actions</span><span class="relative flex-none"><input type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp11-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp11-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
      </div>
      <div class="rounded-3xl bg-tsp11-acc/8 p-6 text-sm ring-1 ring-tsp11-acc/15"><p class="font-bold text-tsp11-ink">Spotted something odd?</p><p class="mt-1 text-tsp11-mut">Sign out the session, then change your password. Signing out doesn't revoke API keys — rotate those separately.</p></div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp11-bg: #f4f6f9;
  --color-tsp11-bg: oklch(0.972 0.006 255);
  --color-tsp11-ink: #0f172a;
  --color-tsp11-ink: oklch(0.208 0.04 266);
  --color-tsp11-mut: #5b6576;
  --color-tsp11-mut: oklch(0.51 0.03 260);
  --color-tsp11-line: #e2e7ee;
  --color-tsp11-line: oklch(0.93 0.01 255);
  --color-tsp11-acc: #2563eb;
  --color-tsp11-acc: oklch(0.546 0.215 263);
  --font-tsp11-sans: 'Albert Sans', system-ui, sans-serif;
}

.tsp-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp11]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const STAGGER = 80;
  const status = root.querySelector('[data-status]');
  const count = root.querySelector('[data-count]');
  const live = () => [...root.querySelectorAll('[data-session]:not([data-gone])')];
  const done = () => {
    const n = live().length;
    count.textContent = n;
    if (!root.querySelector('[data-session]')) root.dataset.empty = '';
  };
  const out = (li, delay) => {
    li.style.transitionDelay = (delay || 0) + 'ms';
    li.dataset.gone = '';
    setTimeout(() => { li.remove(); done(); }, 320 + (delay || 0));
  };
  root.querySelectorAll('[data-out]').forEach((b) => b.addEventListener('click', () => {
    const li = b.closest('[data-session]');
    status.textContent = 'Signed out ' + li.querySelector('.font-semibold').firstChild.textContent.trim() + '.';
    out(li); count.textContent = live().length;
  }));
  root.querySelector('[data-all]').addEventListener('click', () => {
    const rows = live();
    rows.forEach((li, i) => out(li, i * STAGGER));
    count.textContent = 0;
    status.textContent = 'Signed out of ' + rows.length + ' other session' + (rows.length === 1 ? '' : 's') + '.';
  });
})();
```
