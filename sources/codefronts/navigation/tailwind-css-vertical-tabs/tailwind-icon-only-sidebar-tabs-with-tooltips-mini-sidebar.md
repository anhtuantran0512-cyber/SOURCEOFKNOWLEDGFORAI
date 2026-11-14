---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-icon-only-sidebar-tabs-with-tooltips-mini-sidebar/"
title: "Tailwind Icon-Only Sidebar Tabs with Tooltips (Mini Sidebar)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A VS&nbsp;Code&ndash;style editor whose activity bar is a rail of icon-only tabs with tooltips &mdash; Explorer, Search, Source control and Extensions each…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon-Only Sidebar Tabs with Tooltips (Mini Sidebar)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-icon-only-sidebar-tabs-with-tooltips-mini-sidebar/

A VS&nbsp;Code&ndash;style editor whose activity bar is a rail of icon-only tabs with tooltips &mdash; Explorer, Search, Source control and Extensions each swap the side panel. Tooltips are pure Tailwind and appear for the pointer and the keyboard (group-hover/tab:opacity-100 plus [:focus-visible+*_&]:opacity-100), while every icon's accessible name lives in a real sr-only span, not in the tooltip.
## HTML
```html
<section class="tvt-04 w-full min-h-svh grid place-items-center bg-tvt04-bg bg-[radial-gradient(60%_50%_at_25%_0%,var(--color-tvt04-glow),transparent_70%),radial-gradient(50%_45%_at_90%_100%,var(--color-tvt04-glow2),transparent_70%)] px-4 py-14 font-tvt04-sans text-tvt04-ink antialiased sm:px-6" aria-label="Tailwind icon-only sidebar tabs with tooltips demo">
  <div class="grid w-full max-w-[62rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="font-tvt04-mono text-[12px] text-tvt04-acc-ink">sr-only names · hover + focus tooltips</p>
      <h2 class="text-[clamp(28px,4.2vw,42px)] leading-[1.05] font-semibold tracking-[-0.03em] text-balance">A mini sidebar with <span class="bg-linear-to-r from-tvt04-hl to-tvt04-hl2 bg-clip-text pe-1 text-transparent">tooltips that keyboards see</span></h2>
      <p class="max-w-[48ch] text-[15px] leading-relaxed text-tvt04-mut text-pretty">Hover an icon, or press Tab to reach the activity bar and use the arrow keys &mdash; each name appears for focus as well as for the pointer.</p>
    </header>

    <div class="@container w-full">
    <div class="group/ide isolate w-full overflow-hidden rounded-[18px] bg-tvt04-side shadow-tvt04-card ring-1 ring-tvt04-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex h-10 items-center gap-2 border-b border-tvt04-line bg-tvt04-chrome px-4">
        <span aria-hidden="true" class="flex gap-1.5"><span class="size-3 rounded-full bg-[oklch(0.7_0.19_25)]"></span><span class="size-3 rounded-full bg-[oklch(0.82_0.15_85)]"></span><span class="size-3 rounded-full bg-[oklch(0.75_0.17_145)]"></span></span>
        <p class="flex-1 truncate text-center font-tvt04-mono text-[12px] text-tvt04-mut">Sidebar.tsx — acme-web</p>
        <span aria-hidden="true" class="w-12"></span>
      </div>

      <div class="grid h-[29rem] grid-cols-[4rem_15.5rem_minmax(0,1fr)] @max-[46rem]:h-[27rem] @max-[46rem]:grid-cols-[4rem_minmax(0,1fr)]">
        <nav aria-label="Activity bar" class="relative z-20 flex flex-col items-center border-e border-tvt04-line bg-tvt04-rail py-3">
          <div role="radiogroup" aria-label="Side panel views" class="flex flex-col items-center gap-2">

          <input type="radio" name="tvt-04-view" id="tvt-04-t1" class="sr-only" checked>
          <label for="tvt-04-t1" class="group/tab relative grid size-11 cursor-pointer place-items-center rounded-xl text-tvt04-mut transition-[background-color,color] duration-200 hover:bg-tvt04-ink/[0.07] hover:text-tvt04-ink [:checked+&]:bg-tvt04-acc/12 [:checked+&]:text-tvt04-acc-ink [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt04-ring before:absolute before:inset-y-2.5 before:-start-[9px] before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-tvt04-acc before:shadow-[0_0_12px] before:shadow-tvt04-acc before:transition-transform before:duration-300 before:ease-[cubic-bezier(.32,.72,.3,1)] [:checked+&]:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false" class="size-[22px] shrink-0 fill-none stroke-current stroke-[1.6]"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4l2 2.5h9A1.5 1.5 0 0 1 21 9v9a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18z" stroke-linejoin="round"/></svg>
            <span class="sr-only">Explorer</span>
            <span aria-hidden="true" class="pointer-events-none absolute start-full top-1/2 z-30 ms-3.5 flex -translate-x-1 -translate-y-1/2 scale-95 items-center gap-2 rounded-lg bg-tvt04-tip px-2.5 py-1.5 text-[12.5px] font-semibold whitespace-nowrap text-tvt04-tip-ink opacity-0 shadow-tvt04-tip ring-1 ring-white/10 transition-[opacity,translate,scale] duration-150 ease-out group-hover/tab:translate-x-0 group-hover/tab:scale-100 group-hover/tab:opacity-100 [:focus-visible+*_&]:translate-x-0 [:focus-visible+*_&]:scale-100 [:focus-visible+*_&]:opacity-100 before:absolute before:-start-1 before:top-1/2 before:size-2 before:-translate-y-1/2 before:rotate-45 before:bg-tvt04-tip motion-reduce:transition-none">Explorer<kbd class="rounded bg-white/10 px-1.5 py-px font-tvt04-mono text-[10.5px] font-medium text-tvt04-tip-mut">⇧⌘E</kbd></span>
          </label>

          <input type="radio" name="tvt-04-view" id="tvt-04-t2" class="sr-only">
          <label for="tvt-04-t2" class="group/tab relative grid size-11 cursor-pointer place-items-center rounded-xl text-tvt04-mut transition-[background-color,color] duration-200 hover:bg-tvt04-ink/[0.07] hover:text-tvt04-ink [:checked+&]:bg-tvt04-acc/12 [:checked+&]:text-tvt04-acc-ink [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt04-ring before:absolute before:inset-y-2.5 before:-start-[9px] before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-tvt04-acc before:shadow-[0_0_12px] before:shadow-tvt04-acc before:transition-transform before:duration-300 before:ease-[cubic-bezier(.32,.72,.3,1)] [:checked+&]:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false" class="size-[22px] shrink-0 fill-none stroke-current stroke-[1.6]"><circle cx="11" cy="11" r="6.2"/><path d="m20 20-4.4-4.4" stroke-linecap="round"/></svg>
            <span class="sr-only">Search</span>
            <span aria-hidden="true" class="pointer-events-none absolute start-full top-1/2 z-30 ms-3.5 flex -translate-x-1 -translate-y-1/2 scale-95 items-center gap-2 rounded-lg bg-tvt04-tip px-2.5 py-1.5 text-[12.5px] font-semibold whitespace-nowrap text-tvt04-tip-ink opacity-0 shadow-tvt04-tip ring-1 ring-white/10 transition-[opacity,translate,scale] duration-150 ease-out group-hover/tab:translate-x-0 group-hover/tab:scale-100 group-hover/tab:opacity-100 [:focus-visible+*_&]:translate-x-0 [:focus-visible+*_&]:scale-100 [:focus-visible+*_&]:opacity-100 before:absolute before:-start-1 before:top-1/2 before:size-2 before:-translate-y-1/2 before:rotate-45 before:bg-tvt04-tip motion-reduce:transition-none">Search<kbd class="rounded bg-white/10 px-1.5 py-px font-tvt04-mono text-[10.5px] font-medium text-tvt04-tip-mut">⇧⌘F</kbd></span>
          </label>

          <input type="radio" name="tvt-04-view" id="tvt-04-t3" class="sr-only">
          <label for="tvt-04-t3" class="group/tab relative grid size-11 cursor-pointer place-items-center rounded-xl text-tvt04-mut transition-[background-color,color] duration-200 hover:bg-tvt04-ink/[0.07] hover:text-tvt04-ink [:checked+&]:bg-tvt04-acc/12 [:checked+&]:text-tvt04-acc-ink [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt04-ring before:absolute before:inset-y-2.5 before:-start-[9px] before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-tvt04-acc before:shadow-[0_0_12px] before:shadow-tvt04-acc before:transition-transform before:duration-300 before:ease-[cubic-bezier(.32,.72,.3,1)] [:checked+&]:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false" class="size-[22px] shrink-0 fill-none stroke-current stroke-[1.6]"><circle cx="7" cy="6.5" r="2.6"/><circle cx="7" cy="18" r="2.6"/><circle cx="17" cy="10" r="2.6"/><path d="M7 9.1v6.3m0-3.2h5.6a2 2 0 0 0 2-2V12" stroke-linecap="round"/></svg><span aria-hidden="true" class="absolute end-1 bottom-1 grid min-w-4 place-items-center rounded-full bg-tvt04-acc px-1 font-tvt04-mono text-[9.5px] leading-4 font-bold text-tvt04-on-acc">3</span>
            <span class="sr-only">Source control</span>
            <span aria-hidden="true" class="pointer-events-none absolute start-full top-1/2 z-30 ms-3.5 flex -translate-x-1 -translate-y-1/2 scale-95 items-center gap-2 rounded-lg bg-tvt04-tip px-2.5 py-1.5 text-[12.5px] font-semibold whitespace-nowrap text-tvt04-tip-ink opacity-0 shadow-tvt04-tip ring-1 ring-white/10 transition-[opacity,translate,scale] duration-150 ease-out group-hover/tab:translate-x-0 group-hover/tab:scale-100 group-hover/tab:opacity-100 [:focus-visible+*_&]:translate-x-0 [:focus-visible+*_&]:scale-100 [:focus-visible+*_&]:opacity-100 before:absolute before:-start-1 before:top-1/2 before:size-2 before:-translate-y-1/2 before:rotate-45 before:bg-tvt04-tip motion-reduce:transition-none">Source control<kbd class="rounded bg-white/10 px-1.5 py-px font-tvt04-mono text-[10.5px] font-medium text-tvt04-tip-mut">⌃⇧G</kbd></span>
          </label>

          <input type="radio" name="tvt-04-view" id="tvt-04-t4" class="sr-only">
          <label for="tvt-04-t4" class="group/tab relative grid size-11 cursor-pointer place-items-center rounded-xl text-tvt04-mut transition-[background-color,color] duration-200 hover:bg-tvt04-ink/[0.07] hover:text-tvt04-ink [:checked+&]:bg-tvt04-acc/12 [:checked+&]:text-tvt04-acc-ink [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt04-ring before:absolute before:inset-y-2.5 before:-start-[9px] before:w-[3px] before:scale-y-0 before:rounded-e-full before:bg-tvt04-acc before:shadow-[0_0_12px] before:shadow-tvt04-acc before:transition-transform before:duration-300 before:ease-[cubic-bezier(.32,.72,.3,1)] [:checked+&]:before:scale-y-100 motion-reduce:transition-none motion-reduce:before:transition-none">
            <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false" class="size-[22px] shrink-0 fill-none stroke-current stroke-[1.6]"><path d="M4 8h5V4.5a1.5 1.5 0 0 1 3 0V8h5v5h3.5a1.5 1.5 0 0 1 0 3H17v4H4z" stroke-linejoin="round"/></svg>
            <span class="sr-only">Extensions</span>
            <span aria-hidden="true" class="pointer-events-none absolute start-full top-1/2 z-30 ms-3.5 flex -translate-x-1 -translate-y-1/2 scale-95 items-center gap-2 rounded-lg bg-tvt04-tip px-2.5 py-1.5 text-[12.5px] font-semibold whitespace-nowrap text-tvt04-tip-ink opacity-0 shadow-tvt04-tip ring-1 ring-white/10 transition-[opacity,translate,scale] duration-150 ease-out group-hover/tab:translate-x-0 group-hover/tab:scale-100 group-hover/tab:opacity-100 [:focus-visible+*_&]:translate-x-0 [:focus-visible+*_&]:scale-100 [:focus-visible+*_&]:opacity-100 before:absolute before:-start-1 before:top-1/2 before:size-2 before:-translate-y-1/2 before:rotate-45 before:bg-tvt04-tip motion-reduce:transition-none">Extensions<kbd class="rounded bg-white/10 px-1.5 py-px font-tvt04-mono text-[10.5px] font-medium text-tvt04-tip-mut">⇧⌘X</kbd></span>
          </label>
          </div>
          <span aria-hidden="true" class="mt-auto grid size-9 place-items-center rounded-full bg-linear-to-br from-tvt04-acc to-tvt04-hl2 text-[11.5px] font-bold text-tvt04-on-acc">DV</span>
        </nav>

        <div class="grid min-w-0 overflow-hidden border-e border-tvt04-line bg-tvt04-side @max-[46rem]:border-e-0">

          <section id="tvt-04-p1" aria-labelledby="tvt-04-h1" class="invisible col-start-1 row-start-1 translate-y-1.5 opacity-0 transition-[opacity,translate,visibility] duration-250 ease-out group-has-[#tvt-04-t1:checked]/ide:visible group-has-[#tvt-04-t1:checked]/ide:translate-y-0 group-has-[#tvt-04-t1:checked]/ide:opacity-100 motion-reduce:transition-none">
            <h3 id="tvt-04-h1" class="px-4 pt-3.5 pb-2 text-[11px] font-semibold tracking-[0.14em] text-tvt04-mut uppercase">Explorer</h3>
            <p class="flex items-center gap-1 px-3 pb-1 text-[12px] font-bold tracking-[0.04em] text-tvt04-ink"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>ACME-WEB</p>
            <ul class="grid">
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span class="truncate">src</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-9 pe-3 text-[13px] text-tvt04-ink/85"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span class="truncate">components</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-[3.25rem] pe-3 text-[13px] bg-tvt04-acc/12 text-tvt04-ink shadow-[inset_2px_0_0] shadow-tvt04-acc"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span><span class="truncate">Sidebar.tsx</span><span class="ms-auto font-tvt04-mono text-[11px] text-tvt04-attr">M</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-[3.25rem] pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span><span class="truncate">Tooltip.tsx</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-[3.25rem] pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span><span class="truncate">CommandBar.tsx</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-9 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-kw">#</span><span class="truncate">app.css</span><span class="ms-auto font-tvt04-mono text-[11px] text-tvt04-str">A</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-attr">{}</span><span class="truncate">package.json</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-mut">i</span><span class="truncate">README.md</span></li>
            </ul>
          </section>

          <section id="tvt-04-p2" aria-labelledby="tvt-04-h2" class="invisible col-start-1 row-start-1 translate-y-1.5 opacity-0 transition-[opacity,translate,visibility] duration-250 ease-out group-has-[#tvt-04-t2:checked]/ide:visible group-has-[#tvt-04-t2:checked]/ide:translate-y-0 group-has-[#tvt-04-t2:checked]/ide:opacity-100 motion-reduce:transition-none">
            <h3 id="tvt-04-h2" class="px-4 pt-3.5 pb-2 text-[11px] font-semibold tracking-[0.14em] text-tvt04-mut uppercase">Search</h3>
            <div class="mx-3 flex min-h-9 items-center gap-2 rounded-lg bg-tvt04-editor px-2.5 font-tvt04-mono text-[12.5px] ring-1 ring-tvt04-acc/60"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false" class="shrink-0 fill-none stroke-current stroke-2 text-tvt04-mut"><circle cx="11" cy="11" r="6.2"/><path d="m20 20-4.4-4.4" stroke-linecap="round"/></svg>sr-only<span class="ms-auto text-[10.5px] text-tvt04-mut">Aa</span></div>
            <p class="px-4 pt-3 pb-1.5 text-[12px] text-tvt04-mut">3 results in 2 files</p>
            <ul class="grid gap-0.5 text-[12.5px]">
              <li class="flex items-center gap-1.5 px-3 font-semibold"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span>Sidebar.tsx<span class="ms-auto rounded-full bg-tvt04-ink/10 px-1.5 font-tvt04-mono text-[10.5px]">2</span></li>
              <li class="truncate ps-11 pe-3 font-tvt04-mono text-[11.5px] text-tvt04-mut">className="<mark class="rounded-sm bg-tvt04-attr/25 px-0.5 text-tvt04-ink">sr-only</mark>"</li>
              <li class="truncate ps-11 pe-3 font-tvt04-mono text-[11.5px] text-tvt04-mut">// <mark class="rounded-sm bg-tvt04-attr/25 px-0.5 text-tvt04-ink">sr-only</mark> gives the name</li>
              <li class="mt-1 flex items-center gap-1.5 px-3 font-semibold"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span>Tooltip.tsx<span class="ms-auto rounded-full bg-tvt04-ink/10 px-1.5 font-tvt04-mono text-[10.5px]">1</span></li>
              <li class="truncate ps-11 pe-3 font-tvt04-mono text-[11.5px] text-tvt04-mut">&lt;span class="<mark class="rounded-sm bg-tvt04-attr/25 px-0.5 text-tvt04-ink">sr-only</mark>"&gt;</li>
            </ul>
          </section>

          <section id="tvt-04-p3" aria-labelledby="tvt-04-h3" class="invisible col-start-1 row-start-1 translate-y-1.5 opacity-0 transition-[opacity,translate,visibility] duration-250 ease-out group-has-[#tvt-04-t3:checked]/ide:visible group-has-[#tvt-04-t3:checked]/ide:translate-y-0 group-has-[#tvt-04-t3:checked]/ide:opacity-100 motion-reduce:transition-none">
            <h3 id="tvt-04-h3" class="px-4 pt-3.5 pb-2 text-[11px] font-semibold tracking-[0.14em] text-tvt04-mut uppercase">Source control</h3>
            <div class="mx-3 min-h-16 rounded-lg bg-tvt04-editor px-2.5 py-2 text-[12.5px] text-tvt04-mut ring-1 ring-tvt04-line">feat(sidebar): show tooltips on keyboard focus</div>
            <p class="mx-3 mt-2 flex min-h-9 items-center justify-center gap-2 rounded-lg bg-linear-to-r from-tvt04-btn to-tvt04-btn2 text-[13px] font-semibold text-white shadow-tvt04-btn">✓ Commit to main</p>
            <p class="flex items-center gap-1 px-3 pt-4 pb-1 text-[12px] font-bold text-tvt04-ink"><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true" focusable="false" class="shrink-0 text-tvt04-mut"><path d="m5 6 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Changes<span class="ms-auto rounded-full bg-tvt04-ink/10 px-1.5 font-tvt04-mono text-[10.5px]">3</span></p>
            <ul class="grid">
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span><span class="truncate">Sidebar.tsx</span><span class="ms-auto font-tvt04-mono text-[11px] font-bold text-tvt04-attr">M</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span><span class="truncate">Tooltip.tsx</span><span class="ms-auto font-tvt04-mono text-[11px] font-bold text-tvt04-attr">M</span></li>
              <li class="flex min-h-7 items-center gap-1.5 ps-6 pe-3 text-[13px] text-tvt04-ink/85"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-kw">#</span><span class="truncate">app.css</span><span class="ms-auto font-tvt04-mono text-[11px] font-bold text-tvt04-str">A</span></li>
            </ul>
          </section>

          <section id="tvt-04-p4" aria-labelledby="tvt-04-h4" class="invisible col-start-1 row-start-1 translate-y-1.5 opacity-0 transition-[opacity,translate,visibility] duration-250 ease-out group-has-[#tvt-04-t4:checked]/ide:visible group-has-[#tvt-04-t4:checked]/ide:translate-y-0 group-has-[#tvt-04-t4:checked]/ide:opacity-100 motion-reduce:transition-none">
            <h3 id="tvt-04-h4" class="px-4 pt-3.5 pb-2 text-[11px] font-semibold tracking-[0.14em] text-tvt04-mut uppercase">Extensions</h3>
            <ul class="grid gap-1 px-2">
              <li class="flex gap-3 rounded-lg p-2 bg-tvt04-acc/[0.08]"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-lg bg-linear-to-br from-[oklch(0.72_0.14_215)] to-[oklch(0.55_0.15_245)] text-white"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M6 10c1-3.3 3-5 6-5 4.5 0 5 3.3 7.5 4-1 3.3-3 5-6 5-4.5 0-5-3.3-7.5-4ZM4.5 17c1-3.3 3-5 6-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span><span class="grid min-w-0 flex-1 leading-tight"><span class="truncate text-[13px] font-semibold">Tailwind CSS IntelliSense</span><span class="truncate text-[11.5px] text-tvt04-mut">Autocomplete for utilities</span><span class="mt-0.5 text-[11px] text-tvt04-acc-ink">Installed · ★ 4.8</span></span></li>
              <li class="flex gap-3 rounded-lg p-2"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-lg bg-linear-to-br from-[oklch(0.75_0.15_330)] to-[oklch(0.55_0.18_300)] font-tvt04-mono text-[13px] font-bold text-white">P</span><span class="grid min-w-0 flex-1 leading-tight"><span class="truncate text-[13px] font-semibold">Prettier</span><span class="truncate text-[11.5px] text-tvt04-mut">Opinionated formatter</span><span class="mt-0.5 text-[11px] text-tvt04-acc-ink">Installed · ★ 4.6</span></span></li>
              <li class="flex gap-3 rounded-lg p-2"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-lg bg-linear-to-br from-[oklch(0.8_0.15_75)] to-[oklch(0.62_0.18_35)] font-tvt04-mono text-[13px] font-bold text-white">!</span><span class="grid min-w-0 flex-1 leading-tight"><span class="truncate text-[13px] font-semibold">Error Lens</span><span class="truncate text-[11.5px] text-tvt04-mut">Inline diagnostics</span><span class="mt-0.5 text-[11px] text-tvt04-mut">Disabled</span></span></li>
            </ul>
          </section>
        </div>

        <div aria-hidden="true" class="flex min-w-0 flex-col bg-tvt04-editor @max-[46rem]:hidden">
          <div class="flex h-9 shrink-0 border-b border-tvt04-line bg-tvt04-side text-[12.5px]">
            <span class="flex items-center gap-1.5 border-e border-tvt04-line bg-tvt04-editor px-3.5 shadow-[inset_0_2px_0] shadow-tvt04-acc"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span>Sidebar.tsx<span class="ms-1 size-2 rounded-full bg-tvt04-ink/40"></span></span>
            <span class="flex items-center gap-1.5 border-e border-tvt04-line px-3.5 text-tvt04-mut"><span aria-hidden="true" class="w-4 shrink-0 text-center font-tvt04-mono text-[10px] font-bold text-tvt04-tag">TS</span>Tooltip.tsx</span>
          </div>
          <p class="px-4 py-1.5 font-tvt04-mono text-[11px] text-tvt04-mut">src › components › Sidebar.tsx › Sidebar</p>
          <pre class="min-h-0 flex-1 overflow-hidden pe-4 font-tvt04-mono text-[12.5px] leading-[1.6]"><code class="grid"><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">1</span><span class="whitespace-pre"><span class="text-tvt04-kw">export function</span> <span class="text-tvt04-attr">Sidebar</span>({ items }) {</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">2</span><span class="whitespace-pre">  <span class="text-tvt04-kw">return</span> (</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">3</span><span class="whitespace-pre">    &lt;<span class="text-tvt04-tag">nav</span> <span class="text-tvt04-attr">aria-label</span>=<span class="text-tvt04-str">"Activity bar"</span> <span class="text-tvt04-attr">className</span>=<span class="text-tvt04-str">"flex flex-col gap-2"</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">4</span><span class="whitespace-pre">      {items.<span class="text-tvt04-attr">map</span>((item) =&gt; (</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">5</span><span class="whitespace-pre">        &lt;<span class="text-tvt04-tag">button</span> <span class="text-tvt04-attr">className</span>=<span class="text-tvt04-str">"group relative size-11"</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">6</span><span class="whitespace-pre">          &lt;<span class="text-tvt04-tag">item.Icon</span> <span class="text-tvt04-attr">aria-hidden</span>=<span class="text-tvt04-str">"true"</span> /&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">7</span><span class="whitespace-pre">          &lt;<span class="text-tvt04-tag">span</span> <span class="text-tvt04-attr">className</span>=<span class="text-tvt04-str">"sr-only"</span>&gt;{item.label}&lt;/<span class="text-tvt04-tag">span</span>&gt;</span></span><span class="flex bg-tvt04-acc/[0.07]"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">8</span><span class="whitespace-pre">          <span class="text-tvt04-com italic">{/* tooltip: hover + keyboard focus */}</span></span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">9</span><span class="whitespace-pre">          &lt;<span class="text-tvt04-tag">span</span> <span class="text-tvt04-attr">aria-hidden</span>=<span class="text-tvt04-str">"true"</span> <span class="text-tvt04-attr">className</span>=<span class="text-tvt04-str">"opacity-0</span></span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">10</span><span class="whitespace-pre">            <span class="text-tvt04-str">group-hover:opacity-100 group-focus-visible:opacity-100"</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">11</span><span class="whitespace-pre">            {item.label}</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">12</span><span class="whitespace-pre">          &lt;/<span class="text-tvt04-tag">span</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">13</span><span class="whitespace-pre">        &lt;/<span class="text-tvt04-tag">button</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">14</span><span class="whitespace-pre">      ))}</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">15</span><span class="whitespace-pre">    &lt;/<span class="text-tvt04-tag">nav</span>&gt;</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">16</span><span class="whitespace-pre">  );</span></span><span class="flex"><span class="w-9 shrink-0 pe-3 text-end text-tvt04-mut/70 select-none">17</span><span class="whitespace-pre">}</span></span></code></pre>
        </div>
      </div>

      <div class="flex h-7 items-center gap-4 bg-linear-to-r from-tvt04-btn to-tvt04-btn2 px-3 font-tvt04-mono text-[11px] text-white">
        <span class="flex items-center gap-1.5"><svg viewBox="0 0 24 24" width="12" height="12" aria-hidden="true" focusable="false" class="fill-none stroke-current stroke-2"><circle cx="7" cy="6.5" r="2.6"/><circle cx="7" cy="18" r="2.6"/><circle cx="17" cy="10" r="2.6"/><path d="M7 9.1v6.3m0-3.2h5.6a2 2 0 0 0 2-2V12" stroke-linecap="round"/></svg>main*</span>
        <span>⊗ 0  ⚠ 0</span>
        <span class="ms-auto @max-[46rem]:hidden">Ln 8, Col 11</span>
        <span>TypeScript JSX</span>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt04-side px-3.5 py-2 text-center font-tvt04-mono text-[11.5px] text-tvt04-mut ring-1 ring-tvt04-line">group-hover/tab · [:focus-visible+*_&amp;]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt04-bg: #e6f2fa;
  --color-tvt04-bg: oklch(0.955 0.016 235);
  --color-tvt04-glow: #92dff2a6;
  --color-tvt04-glow: oklch(0.86 0.08 215 / 0.65);
  --color-tvt04-glow2: #c1d9ff8c;
  --color-tvt04-glow2: oklch(0.88 0.06 260 / 0.55);
  --color-tvt04-chrome: #eaf1f6;
  --color-tvt04-chrome: oklch(0.955 0.01 235);
  --color-tvt04-rail: #e3edf3;
  --color-tvt04-rail: oklch(0.94 0.014 235);
  --color-tvt04-side: #f2f8fb;
  --color-tvt04-side: oklch(0.975 0.008 235);
  --color-tvt04-editor: #fcfeff;
  --color-tvt04-editor: oklch(0.995 0.003 235);
  --color-tvt04-ink: #132331;
  --color-tvt04-ink: oklch(0.25 0.035 245);
  --color-tvt04-mut: #50606e;
  --color-tvt04-mut: oklch(0.48 0.03 245);
  --color-tvt04-line: #d1dde6;
  --color-tvt04-line: oklch(0.89 0.018 240);
  --color-tvt04-acc: #00a9cd;
  --color-tvt04-acc: oklch(0.68 0.14 220);
  --color-tvt04-acc-ink: #006485;
  --color-tvt04-acc-ink: oklch(0.47 0.12 230);
  --color-tvt04-on-acc: #001828;
  --color-tvt04-on-acc: oklch(0.2 0.05 240);
  --color-tvt04-ring: #007ca5;
  --color-tvt04-ring: oklch(0.55 0.15 230);
  --color-tvt04-hl: #007e9a;
  --color-tvt04-hl: oklch(0.55 0.15 220);
  --color-tvt04-hl2: #4761e4;
  --color-tvt04-hl2: oklch(0.55 0.2 270);
  --color-tvt04-tip: #0d1c2a;
  --color-tvt04-tip: oklch(0.22 0.035 250);
  --color-tvt04-tip-ink: #eff7fb;
  --color-tvt04-tip-ink: oklch(0.97 0.01 230);
  --color-tvt04-tip-mut: #abc2ce;
  --color-tvt04-tip-mut: oklch(0.8 0.03 230);
  --color-tvt04-btn: #006c97;
  --color-tvt04-btn: oklch(0.5 0.13 235);
  --color-tvt04-btn2: #355bbd;
  --color-tvt04-btn2: oklch(0.5 0.16 265);
  --color-tvt04-kw: #773ac1;
  --color-tvt04-kw: oklch(0.5 0.2 300);
  --color-tvt04-str: #137738;
  --color-tvt04-str: oklch(0.5 0.13 150);
  --color-tvt04-tag: #006d91;
  --color-tvt04-tag: oklch(0.5 0.12 230);
  --color-tvt04-attr: #a35303;
  --color-tvt04-attr: oklch(0.53 0.13 55);
  --color-tvt04-com: #5b6b79;
  --color-tvt04-com: oklch(0.52 0.03 245);
  --font-tvt04-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tvt04-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tvt04-card: 0 1px 2px oklch(0.2 0.05 250 / 0.1), 0 34px 80px -34px oklch(0.25 0.1 245 / 0.55);
  --shadow-tvt04-tip: 0 12px 28px -10px oklch(0.1 0.04 250 / 0.6);
  --shadow-tvt04-btn: 0 8px 18px -10px oklch(0.45 0.15 250 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.2);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-04 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-04:not([data-theme="light"]) {
    --color-tvt04-bg: #040b18;
    --color-tvt04-bg: oklch(0.15 0.03 255);
    --color-tvt04-glow: #003e5180;
    --color-tvt04-glow: oklch(0.34 0.1 225 / 0.5);
    --color-tvt04-glow2: #21265f73;
    --color-tvt04-glow2: oklch(0.3 0.1 275 / 0.45);
    --color-tvt04-chrome: #06101c;
    --color-tvt04-chrome: oklch(0.17 0.03 255);
    --color-tvt04-rail: #060f1b;
    --color-tvt04-rail: oklch(0.165 0.03 255);
    --color-tvt04-side: #0a1422;
    --color-tvt04-side: oklch(0.19 0.032 255);
    --color-tvt04-editor: #0e1927;
    --color-tvt04-editor: oklch(0.21 0.033 255);
    --color-tvt04-ink: #e7f0f5;
    --color-tvt04-ink: oklch(0.95 0.012 230);
    --color-tvt04-mut: #9aaebc;
    --color-tvt04-mut: oklch(0.74 0.03 240);
    --color-tvt04-line: #202f42;
    --color-tvt04-line: oklch(0.3 0.04 255);
    --color-tvt04-acc: #37d2f2;
    --color-tvt04-acc: oklch(0.8 0.13 215);
    --color-tvt04-acc-ink: #6ae1f5;
    --color-tvt04-acc-ink: oklch(0.85 0.11 210);
    --color-tvt04-on-acc: #001321;
    --color-tvt04-on-acc: oklch(0.18 0.04 240);
    --color-tvt04-ring: #37d2f2;
    --color-tvt04-ring: oklch(0.8 0.13 215);
    --color-tvt04-hl: #59e4f3;
    --color-tvt04-hl: oklch(0.85 0.12 205);
    --color-tvt04-hl2: #86acff;
    --color-tvt04-hl2: oklch(0.75 0.14 265);
    --color-tvt04-tip: #01040d;
    --color-tvt04-tip: oklch(0.11 0.025 255);
    --color-tvt04-tip-ink: #eff7fb;
    --color-tvt04-tip-ink: oklch(0.97 0.01 230);
    --color-tvt04-tip-mut: #a5bbc7;
    --color-tvt04-tip-mut: oklch(0.78 0.03 230);
    --color-tvt04-btn: #006c97;
    --color-tvt04-btn: oklch(0.5 0.13 235);
    --color-tvt04-btn2: #355bbd;
    --color-tvt04-btn2: oklch(0.5 0.16 265);
    --color-tvt04-kw: #cc9fff;
    --color-tvt04-kw: oklch(0.78 0.14 305);
    --color-tvt04-str: #83dc97;
    --color-tvt04-str: oklch(0.82 0.13 150);
    --color-tvt04-tag: #63d6f1;
    --color-tvt04-tag: oklch(0.82 0.11 215);
    --color-tvt04-attr: #f8bf6c;
    --color-tvt04-attr: oklch(0.84 0.12 75);
    --color-tvt04-com: #8395a4;
    --color-tvt04-com: oklch(0.66 0.03 245);
  }
}

.tvt-04[data-theme="dark"] {
  --color-tvt04-bg: #040b18;
  --color-tvt04-bg: oklch(0.15 0.03 255);
  --color-tvt04-glow: #003e5180;
  --color-tvt04-glow: oklch(0.34 0.1 225 / 0.5);
  --color-tvt04-glow2: #21265f73;
  --color-tvt04-glow2: oklch(0.3 0.1 275 / 0.45);
  --color-tvt04-chrome: #06101c;
  --color-tvt04-chrome: oklch(0.17 0.03 255);
  --color-tvt04-rail: #060f1b;
  --color-tvt04-rail: oklch(0.165 0.03 255);
  --color-tvt04-side: #0a1422;
  --color-tvt04-side: oklch(0.19 0.032 255);
  --color-tvt04-editor: #0e1927;
  --color-tvt04-editor: oklch(0.21 0.033 255);
  --color-tvt04-ink: #e7f0f5;
  --color-tvt04-ink: oklch(0.95 0.012 230);
  --color-tvt04-mut: #9aaebc;
  --color-tvt04-mut: oklch(0.74 0.03 240);
  --color-tvt04-line: #202f42;
  --color-tvt04-line: oklch(0.3 0.04 255);
  --color-tvt04-acc: #37d2f2;
  --color-tvt04-acc: oklch(0.8 0.13 215);
  --color-tvt04-acc-ink: #6ae1f5;
  --color-tvt04-acc-ink: oklch(0.85 0.11 210);
  --color-tvt04-on-acc: #001321;
  --color-tvt04-on-acc: oklch(0.18 0.04 240);
  --color-tvt04-ring: #37d2f2;
  --color-tvt04-ring: oklch(0.8 0.13 215);
  --color-tvt04-hl: #59e4f3;
  --color-tvt04-hl: oklch(0.85 0.12 205);
  --color-tvt04-hl2: #86acff;
  --color-tvt04-hl2: oklch(0.75 0.14 265);
  --color-tvt04-tip: #01040d;
  --color-tvt04-tip: oklch(0.11 0.025 255);
  --color-tvt04-tip-ink: #eff7fb;
  --color-tvt04-tip-ink: oklch(0.97 0.01 230);
  --color-tvt04-tip-mut: #a5bbc7;
  --color-tvt04-tip-mut: oklch(0.78 0.03 230);
  --color-tvt04-btn: #006c97;
  --color-tvt04-btn: oklch(0.5 0.13 235);
  --color-tvt04-btn2: #355bbd;
  --color-tvt04-btn2: oklch(0.5 0.16 265);
  --color-tvt04-kw: #cc9fff;
  --color-tvt04-kw: oklch(0.78 0.14 305);
  --color-tvt04-str: #83dc97;
  --color-tvt04-str: oklch(0.82 0.13 150);
  --color-tvt04-tag: #63d6f1;
  --color-tvt04-tag: oklch(0.82 0.11 215);
  --color-tvt04-attr: #f8bf6c;
  --color-tvt04-attr: oklch(0.84 0.12 75);
  --color-tvt04-com: #8395a4;
  --color-tvt04-com: oklch(0.66 0.03 245);
}
```
