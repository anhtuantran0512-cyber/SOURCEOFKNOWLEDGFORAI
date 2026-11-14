---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-file-manager-table/"
title: "Tailwind Dark Mode File Manager Table"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A file browser in the dark: folder shelf, sortable column headers, alternating row tints derived with the opacity modifier rather than two hard-coded greys,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode File Manager Table
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-file-manager-table/

A file browser in the dark: folder shelf, sortable column headers, alternating row tints derived with the opacity modifier rather than two hard-coded greys, and a selected row marked by an accent edge plus a checked box — never colour alone. A live "N selected" count is computed by CSS counters, so selection feedback works with zero script.
## HTML
```html
<div class="tdm-18 scheme-light-dark has-[#tdm-18-toggle:checked]:scheme-dark dark:has-[#tdm-18-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-tdm18-bg px-3 py-10 font-tdm18-sans text-tdm18-ink antialiased transition-colors duration-300 sm:px-6">
  <div class="grid w-full max-w-6xl overflow-hidden rounded-[24px] border border-tdm18-line bg-tdm18-surface shadow-tdm18-win md:grid-cols-[15rem_minmax(0,1fr)]">
    <aside aria-label="Folders" class="grid content-start gap-1 border-b border-tdm18-line bg-tdm18-tree p-3 md:border-r md:border-b-0">
      <p class="px-2.5 pt-1 pb-2 font-tdm18-mono text-[11px] uppercase tracking-[0.14em] text-tdm18-mut">Shelves</p>
      <button type="button" aria-current="true" class="flex min-h-11 items-center gap-2.5 rounded-xl px-2.5 text-left text-sm text-tdm18-mut transition hover:bg-tdm18-ink/5 hover:text-tdm18-ink focus-visible:outline-2 focus-visible:outline-tdm18-focus aria-[current=true]:bg-tdm18-acc/12 aria-[current=true]:font-medium aria-[current=true]:text-tdm18-ink"><svg class="size-[18px] text-tdm18-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h4l2 2.5h7A2.5 2.5 0 0 1 21 10v7.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5Z"/></svg><span class="flex-1">Design system</span><span class="font-tdm18-mono text-[11px] tabular-nums">128</span></button>
      <button type="button" class="flex min-h-11 items-center gap-2.5 rounded-xl px-2.5 text-left text-sm text-tdm18-mut transition hover:bg-tdm18-ink/5 hover:text-tdm18-ink focus-visible:outline-2 focus-visible:outline-tdm18-focus aria-[current=true]:bg-tdm18-acc/12 aria-[current=true]:font-medium aria-[current=true]:text-tdm18-ink"><svg class="size-[18px] text-tdm18-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h4l2 2.5h7A2.5 2.5 0 0 1 21 10v7.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5Z"/></svg><span class="flex-1">Brand</span><span class="font-tdm18-mono text-[11px] tabular-nums">46</span></button>
      <button type="button" class="flex min-h-11 items-center gap-2.5 rounded-xl px-2.5 text-left text-sm text-tdm18-mut transition hover:bg-tdm18-ink/5 hover:text-tdm18-ink focus-visible:outline-2 focus-visible:outline-tdm18-focus aria-[current=true]:bg-tdm18-acc/12 aria-[current=true]:font-medium aria-[current=true]:text-tdm18-ink"><svg class="size-[18px] text-tdm18-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h4l2 2.5h7A2.5 2.5 0 0 1 21 10v7.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5Z"/></svg><span class="flex-1">Research</span><span class="font-tdm18-mono text-[11px] tabular-nums">17</span></button>
      <button type="button" class="flex min-h-11 items-center gap-2.5 rounded-xl px-2.5 text-left text-sm text-tdm18-mut transition hover:bg-tdm18-ink/5 hover:text-tdm18-ink focus-visible:outline-2 focus-visible:outline-tdm18-focus aria-[current=true]:bg-tdm18-acc/12 aria-[current=true]:font-medium aria-[current=true]:text-tdm18-ink"><svg class="size-[18px] text-tdm18-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h4l2 2.5h7A2.5 2.5 0 0 1 21 10v7.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5Z"/></svg><span class="flex-1">Archive</span><span class="font-tdm18-mono text-[11px] tabular-nums">904</span></button>
    </aside>
    <section aria-label="Files" class="@container min-w-0">
      <header class="flex flex-wrap items-center justify-between gap-3 border-b border-tdm18-line bg-tdm18-toolbar px-4 py-3">
        <p class="flex items-center gap-2 text-sm text-tdm18-mut">Design system <span aria-hidden="true">/</span> <strong class="font-semibold text-tdm18-ink">tokens</strong></p>
        <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm18-line bg-tdm18-surface transition duration-200 hover:-translate-y-px hover:border-tdm18-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm18-focus motion-reduce:transition-none ">
        <input id="tdm-18-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm18-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm18-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
      </header>
      <div role="table" aria-label="Files in tokens" class="[counter-reset:tdm18] text-sm">
        <div role="row" class="grid grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line font-tdm18-mono text-[11px] uppercase tracking-wide text-tdm18-mut @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="columnheader" class="px-4 py-2.5"><span class="sr-only">Select</span></span>
          <button type="button" role="columnheader" aria-sort="ascending" class="flex min-h-10 items-center gap-1 px-2 text-left uppercase transition hover:text-tdm18-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm18-focus aria-[sort]:text-tdm18-ink ">Name<svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 7l10 10M17 9v8H9"/></svg></button>
          <button type="button" role="columnheader" class="flex min-h-10 items-center gap-1 px-2 text-left uppercase transition hover:text-tdm18-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm18-focus aria-[sort]:text-tdm18-ink ">Size</button>
          <button type="button" role="columnheader" class="flex min-h-10 items-center gap-1 px-2 text-left uppercase transition hover:text-tdm18-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm18-focus aria-[sort]:text-tdm18-ink @max-[42rem]:hidden">Modified</button>
          <button type="button" role="columnheader" class="flex min-h-10 items-center gap-1 px-2 text-left uppercase transition hover:text-tdm18-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdm18-focus aria-[sort]:text-tdm18-ink @max-[42rem]:hidden">Owner</button>
        </div>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only" checked><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">theme.css</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">18.4 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">14 Aug 09:12</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">AC</span>Alex Chen</span>
        </label>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only" checked><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">tokens.dark.json</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">6.1 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">13 Aug 17:48</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">PS</span>Priya Sharma</span>
        </label>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only"><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">App.tsx</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">24.9 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">13 Aug 11:02</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">JL</span>Jordan Lee</span>
        </label>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only"><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">next.config.mjs</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">1.8 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">12 Aug 20:31</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">SR</span>Sam Rivera</span>
        </label>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only"><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">package.json</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">3.4 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">12 Aug 08:55</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">AC</span>Alex Chen</span>
        </label>
        <label role="row" class="group/row relative grid min-h-13 cursor-pointer grid-cols-[3rem_minmax(0,1fr)_5.5rem_8.5rem_8.5rem] items-center border-b border-tdm18-line/60 transition even:bg-tdm18-ink/[.025] hover:bg-tdm18-hover has-checked:bg-tdm18-sel has-checked:[counter-increment:tdm18] has-checked:before:absolute has-checked:before:inset-y-0 has-checked:before:left-0 has-checked:before:w-0.5 has-checked:before:bg-tdm18-acc has-checked:before:content-[''] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdm18-focus @max-[42rem]:grid-cols-[3rem_minmax(0,1fr)_5.5rem]">
          <span role="cell" class="grid place-items-center"><input type="checkbox" class="sr-only"><span class="grid size-[18px] place-items-center rounded-md border border-tdm18-mut/50 transition group-has-checked/row:border-tdm18-acc group-has-checked/row:bg-tdm18-acc" aria-hidden="true"><svg class="size-3 text-tdm18-acc-ink opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span></span>
          <span role="cell" class="flex min-w-0 items-center gap-2.5 px-2 font-medium"><svg class="size-4 flex-none text-tdm18-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5"/></svg><span class="truncate">contrast-audit.mjs</span></span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut tabular-nums">9.2 KB</span>
          <span role="cell" class="px-2 font-tdm18-mono text-xs text-tdm18-mut @max-[42rem]:hidden">11 Aug 15:20</span>
          <span role="cell" class="flex items-center gap-2 px-2 text-[13px] text-tdm18-mut @max-[42rem]:hidden"><span class="grid size-6 place-items-center rounded-full bg-tdm18-acc/15 text-[10px] font-semibold text-tdm18-acc" aria-hidden="true">PS</span>Priya Sharma</span>
        </label>
        <div class="flex flex-wrap items-center justify-between gap-3 bg-tdm18-toolbar px-4 py-3">
          <p class="text-[13px] text-tdm18-mut" aria-hidden="true"><span class="font-tdm18-mono font-semibold text-tdm18-ink before:content-[counter(tdm18)]"></span> of 6 selected</p>
          <div class="flex gap-2">
            <button type="button" class="min-h-10 rounded-lg border border-tdm18-line px-3.5 text-[13px] font-medium transition hover:bg-tdm18-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm18-focus">Move</button>
            <button type="button" class="min-h-10 rounded-lg bg-tdm18-acc px-3.5 text-[13px] font-semibold text-tdm18-acc-ink transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm18-focus">Download</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm18-bg: light-dark(#eceef1, #060709);
  --color-tdm18-surface: light-dark(#ffffff, #0f1115);
  --color-tdm18-toolbar: light-dark(#f8f9fa, #0c0e12);
  --color-tdm18-tree: light-dark(#f8f9fa, #0b0d10);
  --color-tdm18-ink: light-dark(#0e1116, #eceef2);
  --color-tdm18-mut: light-dark(#5a6270, #9198a6);
  --color-tdm18-line: light-dark(#e3e6ea, #1f232b);
  --color-tdm18-hover: light-dark(#f3f5f7, #161a20);
  --color-tdm18-sel: light-dark(rgb(13 148 136 / .08), rgb(94 234 212 / .07));
  --color-tdm18-acc: light-dark(#0f766e, #5eead4);
  --color-tdm18-acc-ink: light-dark(#ffffff, #03211c);
  --color-tdm18-focus: light-dark(#0f766e, #99f6e4);
  --color-tdm18-sun: light-dark(#b45309, transparent);
  --color-tdm18-moon: light-dark(transparent, #99f6e4);
  --shadow-tdm18-win: 0 50px 100px -60px light-dark(rgb(14 17 22 / .35), rgb(0 0 0 / .9));
  --font-tdm18-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm18-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
