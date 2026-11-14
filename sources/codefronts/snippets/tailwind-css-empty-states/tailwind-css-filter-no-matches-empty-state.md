---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-filter-no-matches-empty-state/"
title: "Tailwind CSS Filter No Matches Empty State (Pure CSS)"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A recruiting pipeline filtered down to nothing — with zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Filter No Matches Empty State (Pure CSS)
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-filter-no-matches-empty-state/

A recruiting pipeline filtered down to nothing — with zero JavaScript. Checkboxes in the sidebar hide non-matching rows through has-[#id:checked]:[&_[data-x=no]]:hidden on the wrapper, active-filter chips appear beside the title, and a CSS counter reports "Showing N of 5" because counters skip display:none rows.
## HTML
```html
<div class="tes-06 w-full min-h-svh bg-tes06-bg font-tes06-sans text-tes06-ink antialiased [counter-reset:tes06] has-[#tes06-senior:checked]:[&_[data-senior=no]]:hidden has-[#tes06-design:checked]:[&_[data-design=no]]:hidden has-[#tes06-remote:checked]:[&_[data-remote=no]]:hidden">
  <div class="mx-auto grid w-full max-w-6xl gap-6 px-[clamp(1rem,4vw,3rem)] py-[clamp(1.5rem,5vw,3.5rem)] md:grid-cols-[14rem_minmax(0,1fr)]">
    <aside aria-labelledby="tes06-fl" class="grid content-start gap-5 md:sticky md:top-6">
      <p id="tes06-fl" class="text-xs font-semibold tracking-[0.12em] text-tes06-mut uppercase">Pipeline filters</p>
      <fieldset class="grid gap-1 border-t border-tes06-line pt-4">
        <legend class="float-left mb-1 text-[13px] font-medium">Seniority</legend>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-2 text-sm hover:bg-tes06-sunk"><input type="checkbox" id="tes06-senior" checked class="peer sr-only"><span aria-hidden="true" class="grid size-5 place-items-center rounded-md border border-tes06-line2 bg-tes06-card text-white transition peer-checked:border-tes06-acc peer-checked:bg-tes06-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes06-acc [&>svg]:opacity-0 peer-checked:[&>svg]:opacity-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>Senior only</label>
      </fieldset>
      <fieldset class="grid gap-1 border-t border-tes06-line pt-4">
        <legend class="float-left mb-1 text-[13px] font-medium">Discipline</legend>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-2 text-sm hover:bg-tes06-sunk"><input type="checkbox" id="tes06-design" checked class="peer sr-only"><span aria-hidden="true" class="grid size-5 place-items-center rounded-md border border-tes06-line2 bg-tes06-card text-white transition peer-checked:border-tes06-acc peer-checked:bg-tes06-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes06-acc [&>svg]:opacity-0 peer-checked:[&>svg]:opacity-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>Design</label>
      </fieldset>
      <fieldset class="grid gap-1 border-t border-tes06-line pt-4">
        <legend class="float-left mb-1 text-[13px] font-medium">Location</legend>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-2 text-sm hover:bg-tes06-sunk"><input type="checkbox" id="tes06-remote" class="peer sr-only"><span aria-hidden="true" class="grid size-5 place-items-center rounded-md border border-tes06-line2 bg-tes06-card text-white transition peer-checked:border-tes06-acc peer-checked:bg-tes06-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes06-acc [&>svg]:opacity-0 peer-checked:[&>svg]:opacity-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>Remote</label>
      </fieldset>
    </aside>
    <section aria-labelledby="tes06-h" class="grid content-start gap-4">
      <header class="grid gap-3">
        <h1 id="tes06-h" class="text-[clamp(1.35rem,2.6vw,1.75rem)] font-semibold tracking-tight text-balance">Product engineering — open pipeline</h1>
        <div class="flex min-h-9 flex-wrap gap-2">
          <label for="tes06-senior" class="hidden h-9 cursor-pointer items-center gap-1.5 rounded-full bg-tes06-acc/10 pr-2 pl-3 text-xs font-medium text-tes06-acc transition hover:bg-tes06-acc/20 [.tes-06:has(#tes06-senior:checked)_&]:inline-flex">Senior only<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></label>
          <label for="tes06-design" class="hidden h-9 cursor-pointer items-center gap-1.5 rounded-full bg-tes06-acc/10 pr-2 pl-3 text-xs font-medium text-tes06-acc transition hover:bg-tes06-acc/20 [.tes-06:has(#tes06-design:checked)_&]:inline-flex">Design<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></label>
          <label for="tes06-remote" class="hidden h-9 cursor-pointer items-center gap-1.5 rounded-full bg-tes06-acc/10 pr-2 pl-3 text-xs font-medium text-tes06-acc transition hover:bg-tes06-acc/20 [.tes-06:has(#tes06-remote:checked)_&]:inline-flex">Remote<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></label>
        </div>
      </header>
      <ul class="divide-y divide-tes06-line overflow-hidden rounded-2xl border border-tes06-line bg-tes06-card [.tes-06:has(#tes06-senior:checked):has(#tes06-design:checked)_&]:hidden">
        <li data-design="no" class="flex items-center gap-3.5 px-4 py-3.5 [counter-increment:tes06]"><span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-[#dbe7ff] text-xs font-semibold text-[#2b4fb0]">AK</span><span class="grid min-w-0 flex-1"><span class="text-sm font-medium">Ana Kowalski</span><span class="truncate text-xs text-tes06-mut">Staff engineer · Remote, Lisbon</span></span><span class="hidden rounded-full bg-tes06-sunk px-2.5 py-1 text-xs text-tes06-mut sm:block">Onsite loop</span></li>
        <li data-senior="no" data-design="no" data-remote="no" class="flex items-center gap-3.5 px-4 py-3.5 [counter-increment:tes06]"><span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-[#ffe2cc] text-xs font-semibold text-[#9a4a12]">BT</span><span class="grid min-w-0 flex-1"><span class="text-sm font-medium">Ben Tran</span><span class="truncate text-xs text-tes06-mut">Backend engineer · Berlin office</span></span><span class="hidden rounded-full bg-tes06-sunk px-2.5 py-1 text-xs text-tes06-mut sm:block">Tech screen</span></li>
        <li data-design="no" data-remote="no" class="flex items-center gap-3.5 px-4 py-3.5 [counter-increment:tes06]"><span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-[#d6f3e6] text-xs font-semibold text-[#17734f]">CN</span><span class="grid min-w-0 flex-1"><span class="text-sm font-medium">Chi Nakamura</span><span class="truncate text-xs text-tes06-mut">Senior platform engineer · Berlin office</span></span><span class="hidden rounded-full bg-tes06-acc/10 px-2.5 py-1 text-xs font-medium text-tes06-acc sm:block">Offer drafted</span></li>
        <li data-senior="no" class="flex items-center gap-3.5 px-4 py-3.5 [counter-increment:tes06]"><span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-[#f1dcff] text-xs font-semibold text-[#7330a8]">DO</span><span class="grid min-w-0 flex-1"><span class="text-sm font-medium">Dee Osei</span><span class="truncate text-xs text-tes06-mut">Product designer · Remote, Accra</span></span><span class="hidden rounded-full bg-tes06-sunk px-2.5 py-1 text-xs text-tes06-mut sm:block">Portfolio review</span></li>
        <li data-senior="no" data-remote="no" class="flex items-center gap-3.5 px-4 py-3.5 [counter-increment:tes06]"><span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-[#fff1bf] text-xs font-semibold text-[#86640a]">EL</span><span class="grid min-w-0 flex-1"><span class="text-sm font-medium">Eli Lindqvist</span><span class="truncate text-xs text-tes06-mut">Junior designer · Stockholm office</span></span><span class="hidden rounded-full bg-tes06-sunk px-2.5 py-1 text-xs text-tes06-mut sm:block">Intro call</span></li>
      </ul>
      <div class="hidden justify-items-center rounded-2xl border border-dashed border-tes06-line2 bg-[radial-gradient(var(--color-tes06-line)_1px,transparent_1.5px)] bg-size-[16px_16px] px-6 py-14 text-center [.tes-06:has(#tes06-senior:checked):has(#tes06-design:checked)_&]:grid">
        <span aria-hidden="true" class="grid size-16 place-items-center rounded-2xl bg-tes06-card text-tes06-acc shadow-[0_10px_30px_-10px_color-mix(in_oklab,var(--color-tes06-acc)_45%,transparent)] ring-1 ring-tes06-line"><svg class="size-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5h16l-6 7.5V18l-4 2v-7.5z"/><path d="m16 15 4 4M20 15l-4 4"/></svg></span>
        <p class="mt-5 text-lg font-semibold text-balance">No senior designers in this pipeline</p>
        <p class="mt-1.5 max-w-[42ch] text-sm/6 text-tes06-mut text-pretty">Senior design roles are handled by the brand team. Drop one filter to see the rest.</p>
        <div class="mt-5 flex flex-wrap justify-center gap-2.5">
          <label for="tes06-design" class="inline-flex min-h-11 cursor-pointer items-center rounded-xl bg-tes06-ink px-4 text-sm font-medium text-white transition hover:bg-tes06-acc active:scale-[.98]">Drop the design filter</label>
          <label for="tes06-senior" class="inline-flex min-h-11 cursor-pointer items-center rounded-xl border border-tes06-line2 bg-tes06-card px-4 text-sm transition hover:border-tes06-ink">Drop senior only</label>
        </div>
      </div>
      <p aria-hidden="true" class="text-xs text-tes06-mut before:content-['Showing_'] before:font-medium after:content-[counter(tes06)_'_of_5_candidates']"></p>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes06-bg: #f6f7f9;
  --color-tes06-bg: oklch(0.974 0.004 255);
  --color-tes06-card: #ffffff;
  --color-tes06-card: oklch(1 0 0);
  --color-tes06-sunk: #eef0f4;
  --color-tes06-sunk: oklch(0.952 0.006 255);
  --color-tes06-line: #e0e3ea;
  --color-tes06-line: oklch(0.909 0.009 255);
  --color-tes06-line2: #c3c8d3;
  --color-tes06-line2: oklch(0.82 0.015 255);
  --color-tes06-ink: #161b26;
  --color-tes06-ink: oklch(0.21 0.02 260);
  --color-tes06-mut: #596173;
  --color-tes06-mut: oklch(0.47 0.025 260);
  --color-tes06-acc: #c2410c;
  --color-tes06-acc: oklch(0.55 0.18 40);
  --font-tes06-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-06 {
  width: 100%;
  min-height: 100svh;
}

.tes-06 [hidden] {
  display: none !important;
}
```
