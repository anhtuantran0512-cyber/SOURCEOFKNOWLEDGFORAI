---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-collapsible-breadcrumb-ellipsis-dropdown/"
title: "Tailwind Collapsible Breadcrumb with Ellipsis Dropdown"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A file-explorer header whose breadcrumb collapses to Home › ··· › Documents; the ellipsis opens the hidden ancestors as a dropdown that scales out from the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Collapsible Breadcrumb with Ellipsis Dropdown
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-collapsible-breadcrumb-ellipsis-dropdown/

A file-explorer header whose breadcrumb collapses to Home › ··· › Documents; the ellipsis opens the hidden ancestors as a dropdown that scales out from the button. The port anchors the menu to the ellipsis itself (not a magic top: 88px), adds the click-outside scrim the original's gotchas asked for, and uses real <nav><ol> breadcrumb semantics. Zero JavaScript.
## HTML
```html
<section class="tmn-13 w-full min-h-svh grid place-items-center bg-tmn13-stage px-4 py-6 font-tmn13-sans antialiased" aria-label="Tailwind collapsible breadcrumb demo">
  <div class="group relative flex h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] flex-col overflow-hidden rounded-[2.25rem] bg-tmn13-bg text-tmn13-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.45)]">
    <input type="checkbox" id="tmn-13-crumbs" class="peer sr-only" aria-label="Show full path">
    <label for="tmn-13-crumbs" aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 group-has-checked:pointer-events-auto"></label>

    <header class="relative z-20 flex-none border-b border-tmn13-line bg-white px-4 pt-4 pb-3">
      <div class="mb-2.5 flex items-center gap-2">
        <a href="#" class="grid size-10 place-items-center rounded-xl border border-tmn13-line"><span class="sr-only">Back</span><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg></a>
        <h1 class="flex-1 text-[17px] font-semibold">Documents</h1>
        <button type="button" class="grid size-10 place-items-center rounded-xl border border-tmn13-line"><span class="sr-only">Search</span><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></button>
        <button type="button" class="grid size-10 place-items-center rounded-xl border border-tmn13-line"><span class="sr-only">More</span><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg></button>
      </div>
      <nav aria-label="Breadcrumb">
        <ol class="flex items-center text-[13px] font-medium text-tmn13-mut">
          <li><a href="#" class="rounded-md px-1.5 py-1 text-tmn13-acc hover:bg-tmn13-acc/8">Home</a></li>
          <li class="relative flex items-center before:px-1 before:text-tmn13-line2 before:content-['›']">
            <label for="tmn-13-crumbs" class="grid h-7 min-w-9 cursor-pointer place-items-center rounded-md border border-tmn13-line bg-tmn13-bg text-xs font-bold tracking-[0.1em] transition-colors hover:border-tmn13-acc hover:bg-tmn13-acc hover:text-white group-has-checked:border-tmn13-acc group-has-checked:bg-tmn13-acc group-has-checked:text-white peer-focus-visible:ring-2 peer-focus-visible:ring-tmn13-acc peer-focus-visible:ring-offset-1"><span aria-hidden="true">···</span><span class="sr-only">Show 4 hidden folders</span></label>
            <div class="invisible absolute top-full left-3 z-20 mt-2 min-w-48 origin-top-left -translate-y-2 scale-95 overflow-hidden rounded-xl border border-tmn13-line bg-white py-1 opacity-0 shadow-[0_12px_32px_-8px_oklch(0_0_0/0.18)] transition duration-200 group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100">
              <a href="#" class="flex min-h-11 items-center gap-2.5 px-3.5 text-[13px] text-tmn13-ink hover:bg-tmn13-bg"><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="M17.5 19a4.5 4.5 0 1 0-1.4-8.8A7 7 0 1 0 4 15.3"/><path d="M8 19h9.5"/></svg>My Drive</a>
              <a href="#" class="flex min-h-11 items-center gap-2.5 py-0 pr-3.5 pl-6 text-[13px] text-tmn13-ink hover:bg-tmn13-bg"><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>Work Projects</a>
              <a href="#" class="flex min-h-11 items-center gap-2.5 py-0 pr-3.5 pl-8.5 text-[13px] text-tmn13-ink hover:bg-tmn13-bg"><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>2026</a>
              <a href="#" class="flex min-h-11 items-center gap-2.5 py-0 pr-3.5 pl-11 text-[13px] text-tmn13-ink hover:bg-tmn13-bg"><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>Q3 Reports</a>
            </div>
          </li>
          <li class="flex items-center before:px-1 before:text-tmn13-line2 before:content-['›']"><span aria-current="page" class="px-1 font-semibold text-tmn13-ink">Documents</span></li>
        </ol>
      </nav>
    </header>

    <main class="flex-1 overflow-y-auto">
      <p class="flex items-center justify-between px-4 pt-4 pb-1.5 text-[11px] font-bold tracking-[0.1em] text-tmn13-mut uppercase">Folders <a href="#" class="text-xs font-semibold tracking-normal text-tmn13-acc normal-case">+ New</a></p>
      <a href="#" class="flex min-h-14 items-center gap-3 border-b border-black/4 px-4 hover:bg-black/2"><svg viewBox="0 0 24 24" class="size-6 fill-amber-100 text-amber-500" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="flex-1 text-sm font-medium">Design Assets</span><span class="text-xs text-tmn13-mut">48 items</span><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
      <a href="#" class="flex min-h-14 items-center gap-3 border-b border-black/4 px-4 hover:bg-black/2"><svg viewBox="0 0 24 24" class="size-6 fill-amber-100 text-amber-500" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="flex-1 text-sm font-medium">Client Reports</span><span class="text-xs text-tmn13-mut">12 items</span><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
      <a href="#" class="flex min-h-14 items-center gap-3 border-b border-black/4 px-4 hover:bg-black/2"><svg viewBox="0 0 24 24" class="size-6 fill-amber-100 text-amber-500" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="flex-1 text-sm font-medium">Contracts</span><span class="text-xs text-tmn13-mut">7 items</span><svg viewBox="0 0 24 24" class="size-4 text-tmn13-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
      <p class="px-4 pt-5 pb-1.5 text-[11px] font-bold tracking-[0.1em] text-tmn13-mut uppercase">Recent files</p>
      <a href="#" class="flex min-h-15 items-center gap-3 border-b border-black/4 px-4 hover:bg-black/2"><span class="grid size-9 place-items-center rounded-lg bg-red-50 text-[10px] font-bold text-red-700">PDF</span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium">Q3 Summary Report.pdf</span><span class="block text-xs text-tmn13-mut">2.4 MB · Today, 14:32</span></span></a>
      <a href="#" class="flex min-h-15 items-center gap-3 border-b border-black/4 px-4 hover:bg-black/2"><span class="grid size-9 place-items-center rounded-lg bg-green-50 text-[10px] font-bold text-green-700">XLS</span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium">Analytics Dashboard.xlsx</span><span class="block text-xs text-tmn13-mut">840 KB · Yesterday</span></span></a>
      <a href="#" class="flex min-h-15 items-center gap-3 px-4 hover:bg-black/2"><span class="grid size-9 place-items-center rounded-lg bg-violet-50 text-[10px] font-bold text-violet-700">FIG</span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium">Brand Guidelines.fig</span><span class="block text-xs text-tmn13-mut">18 MB · Sep 3</span></span></a>
    </main>

    <footer class="flex flex-none items-center gap-3 border-t border-tmn13-acc/15 bg-tmn13-acc/5 px-4 py-3">
      <span class="grid size-9 place-items-center rounded-xl bg-tmn13-acc text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M17.5 19a4.5 4.5 0 1 0-1.4-8.8A7 7 0 1 0 4 15.3"/><path d="M8 19h9.5"/></svg></span>
      <div class="flex-1"><p class="text-[13px] font-semibold">24.8 GB of 50 GB used</p><div class="mt-1.5 h-1 overflow-hidden rounded-full bg-tmn13-acc/15"><div class="h-full w-1/2 rounded-full bg-tmn13-acc"></div></div></div>
      <a href="#" class="grid min-h-9 place-items-center rounded-lg border border-tmn13-acc/30 px-3 text-xs font-semibold text-tmn13-acc">Upgrade</a>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn13-stage: #e4e4e7;
  --color-tmn13-stage: oklch(0.92 0.004 286);
  --color-tmn13-bg: #fafafa;
  --color-tmn13-bg: oklch(0.985 0 0);
  --color-tmn13-line: #e4e4e7;
  --color-tmn13-line: oklch(0.92 0.004 286);
  --color-tmn13-line2: #b4b4bb;
  --color-tmn13-line2: oklch(0.77 0.01 286);
  --color-tmn13-ink: #18181b;
  --color-tmn13-ink: oklch(0.21 0.006 285);
  --color-tmn13-mut: #63636b;
  --color-tmn13-mut: oklch(0.5 0.012 286);
  --color-tmn13-acc: #2563eb;
  --color-tmn13-acc: oklch(0.55 0.22 263);
  --font-tmn13-sans: 'Instrument Sans', system-ui, sans-serif;
}
/* Icon base: utilities (fill-*, text-*) still win because this sits in the base layer. */

@layer base {
  .tmn-13 svg {
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

.tmn-13 {
  width: 100%;
  min-height: 100svh;
}
```
