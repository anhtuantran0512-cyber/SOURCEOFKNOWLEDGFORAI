---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-accordion-feature-cards-section/"
title: "Tailwind Accordion Feature Cards Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "An expandable feature list paired with a preview pane: five native <details name> cards form an exclusive accordion, and the preview on the right swaps to…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion Feature Cards Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-accordion-feature-cards-section/

An expandable feature list paired with a preview pane: five native <details name> cards form an exclusive accordion, and the preview on the right swaps to match whichever card is open — read straight from the DOM with group-has-[#id[open]]/acc:. Height animates with ::details-content + interpolate-size.
## HTML
```html
<section class="tfs-07 w-full min-h-svh bg-tfs07-bg px-5 py-20 font-tfs07-sans text-tfs07-ink antialiased sm:py-28" aria-labelledby="tfs-07-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12">
    <header class="grid max-w-2xl gap-4">
      <p class="text-sm font-semibold text-tfs07-acc">Platform</p>
      <h2 id="tfs-07-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Everything Quill does, one card at a time</h2>
    </header>
    <div class="group/acc grid gap-8 lg:grid-cols-[1fr_1.1fr] lg:items-start">
      <div class="grid gap-3">
        <details name="tfs-07" id="tfs-07-d1" open class="group rounded-2xl border border-tfs07-line bg-white/50 transition open:border-transparent open:bg-white open:shadow-[0_20px_50px_-24px_rgb(12_74_110/0.35)]">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs07-acc"><span class="grid size-10 flex-none place-items-center rounded-xl bg-tfs07-soft text-tfs07-acc transition group-open:bg-tfs07-acc group-open:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg></span><span class="flex-1 text-lg font-semibold">AI drafting</span><span class="grid size-8 place-items-center rounded-full border border-tfs07-line text-tfs07-mut transition group-open:rotate-45 group-open:border-tfs07-acc group-open:text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg></span></summary>
          <p class="px-5 pb-5 pl-[4.75rem] text-pretty text-tfs07-mut">Turn bullet points into a first draft in your house style, with citations to your own docs.</p>
        </details>
        <details name="tfs-07" id="tfs-07-d2" class="group rounded-2xl border border-tfs07-line bg-white/50 transition open:border-transparent open:bg-white open:shadow-[0_20px_50px_-24px_rgb(12_74_110/0.35)]">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs07-acc"><span class="grid size-10 flex-none place-items-center rounded-xl bg-tfs07-soft text-tfs07-acc transition group-open:bg-tfs07-acc group-open:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span><span class="flex-1 text-lg font-semibold">Live co-editing</span><span class="grid size-8 place-items-center rounded-full border border-tfs07-line text-tfs07-mut transition group-open:rotate-45 group-open:border-tfs07-acc group-open:text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg></span></summary>
          <p class="px-5 pb-5 pl-[4.75rem] text-pretty text-tfs07-mut">Cursors, comments and suggestions in real time, with offline edits merged on reconnect.</p>
        </details>
        <details name="tfs-07" id="tfs-07-d3" class="group rounded-2xl border border-tfs07-line bg-white/50 transition open:border-transparent open:bg-white open:shadow-[0_20px_50px_-24px_rgb(12_74_110/0.35)]">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs07-acc"><span class="grid size-10 flex-none place-items-center rounded-xl bg-tfs07-soft text-tfs07-acc transition group-open:bg-tfs07-acc group-open:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span><span class="flex-1 text-lg font-semibold">Version history</span><span class="grid size-8 place-items-center rounded-full border border-tfs07-line text-tfs07-mut transition group-open:rotate-45 group-open:border-tfs07-acc group-open:text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg></span></summary>
          <p class="px-5 pb-5 pl-[4.75rem] text-pretty text-tfs07-mut">Every keystroke is recoverable. Compare any two versions side by side.</p>
        </details>
        <details name="tfs-07" id="tfs-07-d4" class="group rounded-2xl border border-tfs07-line bg-white/50 transition open:border-transparent open:bg-white open:shadow-[0_20px_50px_-24px_rgb(12_74_110/0.35)]">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs07-acc"><span class="grid size-10 flex-none place-items-center rounded-xl bg-tfs07-soft text-tfs07-acc transition group-open:bg-tfs07-acc group-open:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg></span><span class="flex-1 text-lg font-semibold">Granular sharing</span><span class="grid size-8 place-items-center rounded-full border border-tfs07-line text-tfs07-mut transition group-open:rotate-45 group-open:border-tfs07-acc group-open:text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg></span></summary>
          <p class="px-5 pb-5 pl-[4.75rem] text-pretty text-tfs07-mut">Share a single section, set expiry dates and watermark exported PDFs.</p>
        </details>
        <details name="tfs-07" id="tfs-07-d5" class="group rounded-2xl border border-tfs07-line bg-white/50 transition open:border-transparent open:bg-white open:shadow-[0_20px_50px_-24px_rgb(12_74_110/0.35)]">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs07-acc"><span class="grid size-10 flex-none place-items-center rounded-xl bg-tfs07-soft text-tfs07-acc transition group-open:bg-tfs07-acc group-open:text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span><span class="flex-1 text-lg font-semibold">Publish anywhere</span><span class="grid size-8 place-items-center rounded-full border border-tfs07-line text-tfs07-mut transition group-open:rotate-45 group-open:border-tfs07-acc group-open:text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg></span></summary>
          <p class="px-5 pb-5 pl-[4.75rem] text-pretty text-tfs07-mut">One click to your help centre, blog or Notion-style public page.</p>
        </details>
      </div>
      <div class="relative grid overflow-hidden rounded-[2rem] bg-tfs07-ink p-6 shadow-2xl sm:p-10 lg:sticky lg:top-8 lg:min-h-[28rem]">
        <div aria-hidden="true" class="absolute -right-20 -top-20 size-72 rounded-full bg-tfs07-acc/40 blur-3xl"></div>
        <div aria-hidden="true" class="relative grid place-items-center opacity-0 transition duration-500 [grid-area:1/1] group-has-[#tfs-07-d1[open]]/acc:opacity-100"><div class="w-full max-w-sm rounded-2xl bg-white p-5 shadow-xl"><p class="flex items-center gap-2 text-xs font-semibold text-tfs07-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg>Drafting…</p><div class="mt-3 grid gap-2"><i class="h-2.5 w-full rounded bg-slate-200"></i><i class="h-2.5 w-[92%] rounded bg-slate-200"></i><i class="h-2.5 w-[70%] rounded bg-tfs07-acc/40"></i></div><p class="mt-4 inline-flex rounded-md bg-tfs07-soft px-2 py-1 text-[11px] font-medium text-tfs07-acc">3 sources cited</p></div></div>
        <div aria-hidden="true" class="relative grid place-items-center opacity-0 transition duration-500 [grid-area:1/1] group-has-[#tfs-07-d2[open]]/acc:opacity-100"><div class="relative w-full max-w-sm rounded-2xl bg-white p-5 shadow-xl"><div class="grid gap-2"><i class="h-2.5 w-full rounded bg-slate-200"></i><i class="h-2.5 w-[80%] rounded bg-amber-200"></i><i class="h-2.5 w-[88%] rounded bg-slate-200"></i></div><span class="absolute left-[60%] top-[38%] rounded-md rounded-tl-none bg-amber-500 px-2 py-0.5 text-[10px] font-bold text-white">Priya</span><span class="absolute left-[24%] top-[72%] rounded-md rounded-tl-none bg-tfs07-acc px-2 py-0.5 text-[10px] font-bold text-white">Alex</span></div></div>
        <div aria-hidden="true" class="relative grid place-items-center opacity-0 transition duration-500 [grid-area:1/1] group-has-[#tfs-07-d3[open]]/acc:opacity-100"><ol class="grid w-full max-w-sm gap-2"><li class="flex items-center gap-3 rounded-xl bg-white text-tfs07-ink px-4 py-3 text-sm font-medium"><span class="size-2 rounded-full bg-tfs07-acc"></span>Today 14:02 · Alex</li><li class="flex items-center gap-3 rounded-xl bg-white/10 text-white px-4 py-3 text-sm font-medium"><span class="size-2 rounded-full bg-white/40"></span>Today 11:40 · Priya</li><li class="flex items-center gap-3 rounded-xl bg-white/10 text-white px-4 py-3 text-sm font-medium"><span class="size-2 rounded-full bg-white/40"></span>Yesterday · Jordan</li></ol></div>
        <div aria-hidden="true" class="relative grid place-items-center opacity-0 transition duration-500 [grid-area:1/1] group-has-[#tfs-07-d4[open]]/acc:opacity-100"><div class="w-full max-w-sm rounded-2xl bg-white p-5 shadow-xl"><p class="text-sm font-semibold">Share “Q4 plan”</p><div class="mt-3 flex items-center justify-between rounded-lg bg-slate-100 px-3 py-2 text-xs"><span>Section 2 only</span><span class="font-semibold text-tfs07-acc">Can comment</span></div><div class="mt-2 flex items-center justify-between rounded-lg bg-slate-100 px-3 py-2 text-xs"><span>Expires</span><span class="font-semibold">in 7 days</span></div></div></div>
        <div aria-hidden="true" class="relative grid place-items-center opacity-0 transition duration-500 [grid-area:1/1] group-has-[#tfs-07-d5[open]]/acc:opacity-100"><div class="grid w-full max-w-sm grid-cols-3 gap-3"><div class="grid aspect-square place-items-center rounded-2xl bg-white/10 p-2 text-center text-xs font-semibold text-white ring-1 ring-white/15">Help centre</div><div class="grid aspect-square place-items-center rounded-2xl bg-white/10 p-2 text-center text-xs font-semibold text-white ring-1 ring-white/15">Blog</div><div class="grid aspect-square place-items-center rounded-2xl bg-white/10 p-2 text-center text-xs font-semibold text-white ring-1 ring-white/15">Public page</div></div></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs07-bg: #f2f7fa;
  --color-tfs07-bg: oklch(0.973 0.007 234);
  --color-tfs07-soft: #e0f0f8;
  --color-tfs07-soft: oklch(0.946 0.02 229);
  --color-tfs07-ink: #082f49;
  --color-tfs07-ink: oklch(0.293 0.063 243);
  --color-tfs07-mut: #475e6c;
  --color-tfs07-mut: oklch(0.469 0.036 235);
  --color-tfs07-line: #d6e3ea;
  --color-tfs07-line: oklch(0.908 0.017 231);
  --color-tfs07-acc: #0284c7;
  --color-tfs07-acc: oklch(0.588 0.139 242);
  --font-tfs07-sans: 'Outfit', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-07 {
  width: 100%;
  min-height: 100svh;
}
/* No Tailwind variant exists for ::details-content yet — the one rule that stays CSS. */

.tfs-07 {
  interpolate-size: allow-keywords;
}

.tfs-07 details::details-content {
  block-size: 0;
  overflow: clip;
  transition: block-size 0.35s ease, content-visibility 0.35s allow-discrete;
}

.tfs-07 details[open]::details-content {
  block-size: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tfs-07 details::details-content {
    transition: none;
  }
}
```
