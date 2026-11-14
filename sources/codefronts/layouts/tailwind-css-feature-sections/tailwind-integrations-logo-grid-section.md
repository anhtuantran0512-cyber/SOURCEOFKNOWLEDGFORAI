---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-integrations-logo-grid-section/"
title: "Tailwind Integrations Logo Grid Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "An integrations directory in a feature section: twelve app tiles with a category filter (All / Data / Comms / Dev) and three callouts."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Integrations Logo Grid Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-integrations-logo-grid-section/

An integrations directory in a feature section: twelve app tiles with a category filter (All / Data / Comms / Dev) and three callouts. The filter is a radio group; tiles outside the chosen category dim and shrink via group-has-[#id:checked]/int: variants, keeping the grid stable instead of reflowing.
## HTML
```html
<section class="tfs-06 w-full min-h-svh bg-tfs06-bg px-5 py-20 font-tfs06-sans text-tfs06-ink antialiased sm:py-28" aria-labelledby="tfs-06-h">
  <div class="group/int mx-auto grid w-full max-w-6xl gap-12 lg:grid-cols-[1fr_1.25fr] lg:items-center lg:gap-16">
    <div class="grid gap-8">
      <div class="grid gap-4">
        <p class="text-sm font-bold text-tfs06-acc">120+ integrations</p>
        <h2 id="tfs-06-h" class="text-balance text-4xl font-extrabold tracking-tight sm:text-5xl">Plugs into the stack you already run</h2>
        <p class="text-pretty text-lg text-tfs06-mut">Prism connects in minutes, syncs both ways and never asks you to migrate.</p>
      </div>
      <ul class="grid gap-4">
        <li class="flex gap-4"><span class="grid size-10 flex-none place-items-center rounded-xl bg-white text-tfs06-acc shadow-sm ring-1 ring-tfs06-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/></svg></span><div><h3 class="font-bold">One-click OAuth</h3><p class="text-sm text-tfs06-mut">No API keys pasted into Slack.</p></div></li>
        <li class="flex gap-4"><span class="grid size-10 flex-none place-items-center rounded-xl bg-white text-tfs06-acc shadow-sm ring-1 ring-tfs06-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span><div><h3 class="font-bold">Two-way sync</h3><p class="text-sm text-tfs06-mut">Edits flow back within seconds.</p></div></li>
        <li class="flex gap-4"><span class="grid size-10 flex-none place-items-center rounded-xl bg-white text-tfs06-acc shadow-sm ring-1 ring-tfs06-line"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/></svg></span><div><h3 class="font-bold">Open webhooks</h3><p class="text-sm text-tfs06-mut">Build what isn't in the catalogue.</p></div></li>
      </ul>
    </div>
    <div class="grid gap-5 rounded-[2rem] border border-tfs06-line bg-white p-5 shadow-[0_30px_80px_-40px_rgb(30_27_75/0.35)] sm:p-7">
      <fieldset class="flex flex-wrap gap-2">
        <legend class="sr-only">Filter integrations</legend>
        <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tfs06-line px-4 text-sm font-semibold text-tfs06-mut transition hover:border-tfs06-acc/40 has-checked:border-tfs06-ink has-checked:bg-tfs06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs06-acc"><input type="radio" name="tfs-06-f" id="tfs-06-all" class="sr-only" checked>All</label>
        <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tfs06-line px-4 text-sm font-semibold text-tfs06-mut transition hover:border-tfs06-acc/40 has-checked:border-tfs06-ink has-checked:bg-tfs06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs06-acc"><input type="radio" name="tfs-06-f" id="tfs-06-data" class="sr-only">Data</label>
        <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tfs06-line px-4 text-sm font-semibold text-tfs06-mut transition hover:border-tfs06-acc/40 has-checked:border-tfs06-ink has-checked:bg-tfs06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs06-acc"><input type="radio" name="tfs-06-f" id="tfs-06-comms" class="sr-only">Comms</label>
        <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tfs06-line px-4 text-sm font-semibold text-tfs06-mut transition hover:border-tfs06-acc/40 has-checked:border-tfs06-ink has-checked:bg-tfs06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs06-acc"><input type="radio" name="tfs-06-f" id="tfs-06-dev" class="sr-only">Dev</label>
      </fieldset>
      <ul class="grid grid-cols-2 gap-3 sm:grid-cols-3">
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-sky-600 text-sm font-extrabold text-white shadow-sm">P</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Postgres</span><span class="block text-xs text-tfs06-mut">Data</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-cyan-500 text-sm font-extrabold text-white shadow-sm">S</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Snowflake</span><span class="block text-xs text-tfs06-mut">Data</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-blue-600 text-sm font-extrabold text-white shadow-sm">B</span><span class="min-w-0"><span class="block truncate text-sm font-bold">BigQuery</span><span class="block text-xs text-tfs06-mut">Data</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-fuchsia-600 text-sm font-extrabold text-white shadow-sm">S</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Slack</span><span class="block text-xs text-tfs06-mut">Comms</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-indigo-600 text-sm font-extrabold text-white shadow-sm">T</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Teams</span><span class="block text-xs text-tfs06-mut">Comms</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-rose-500 text-sm font-extrabold text-white shadow-sm">G</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Gmail</span><span class="block text-xs text-tfs06-mut">Comms</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-zinc-900 text-sm font-extrabold text-white shadow-sm">G</span><span class="min-w-0"><span class="block truncate text-sm font-bold">GitHub</span><span class="block text-xs text-tfs06-mut">Dev</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-orange-500 text-sm font-extrabold text-white shadow-sm">G</span><span class="min-w-0"><span class="block truncate text-sm font-bold">GitLab</span><span class="block text-xs text-tfs06-mut">Dev</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-violet-600 text-sm font-extrabold text-white shadow-sm">L</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Linear</span><span class="block text-xs text-tfs06-mut">Dev</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-amber-500 text-sm font-extrabold text-white shadow-sm">A</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Airtable</span><span class="block text-xs text-tfs06-mut">Data</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-dev:checked]/int:scale-95 group-has-[#tfs-06-dev:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-blue-500 text-sm font-extrabold text-white shadow-sm">Z</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Zoom</span><span class="block text-xs text-tfs06-mut">Comms</span></span></li>
        <li class="flex items-center gap-3 rounded-2xl border border-tfs06-line bg-tfs06-bg/60 p-3 transition duration-300 hover:-translate-y-1 hover:border-transparent hover:bg-white hover:shadow-lg group-has-[#tfs-06-data:checked]/int:scale-95 group-has-[#tfs-06-data:checked]/int:opacity-25 group-has-[#tfs-06-comms:checked]/int:scale-95 group-has-[#tfs-06-comms:checked]/int:opacity-25"><span class="grid size-10 flex-none place-items-center rounded-xl bg-black text-sm font-extrabold text-white shadow-sm">V</span><span class="min-w-0"><span class="block truncate text-sm font-bold">Vercel</span><span class="block text-xs text-tfs06-mut">Dev</span></span></li>
      </ul>
      <a href="#tfs-06-h" class="group inline-flex min-h-11 items-center justify-center gap-2 rounded-xl bg-tfs06-bg text-sm font-semibold text-tfs06-ink transition hover:bg-tfs06-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs06-acc">Browse all 120 integrations <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-0.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs06-bg: #f5f5fb;
  --color-tfs06-bg: oklch(0.972 0.008 286);
  --color-tfs06-ink: #1e1b4b;
  --color-tfs06-ink: oklch(0.257 0.086 281);
  --color-tfs06-mut: #53517a;
  --color-tfs06-mut: oklch(0.454 0.066 286);
  --color-tfs06-line: #e4e3f1;
  --color-tfs06-line: oklch(0.921 0.019 289);
  --color-tfs06-acc: #6d28d9;
  --color-tfs06-acc: oklch(0.491 0.241 293);
  --font-tfs06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-06 {
  width: 100%;
  min-height: 100svh;
}
```
