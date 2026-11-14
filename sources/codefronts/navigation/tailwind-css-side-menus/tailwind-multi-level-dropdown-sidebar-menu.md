---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-multi-level-dropdown-sidebar-menu/"
title: "Tailwind Multi-Level Dropdown Sidebar Menu (Nested Accordion)"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A three-level documentation tree — section, group, page — built on native <details> disclosures instead of checkbox hacks, so every level is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Level Dropdown Sidebar Menu (Nested Accordion)
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-multi-level-dropdown-sidebar-menu/

A three-level documentation tree — section, group, page — built on native <details> disclosures instead of checkbox hacks, so every level is keyboard-operable and announces expanded/collapsed for free. Panels animate to their true height with ::details-content + interpolate-size, ending the max-height: 300px magic number. Zero JavaScript.
## HTML
```html
<section class="tsm-07 flex w-full min-h-svh bg-tsm07-bg font-tsm07-sans text-tsm07-ink" aria-label="Multi-level dropdown sidebar menu demo">
  <nav aria-label="Documentation" class="w-64 shrink-0 overflow-y-auto border-r border-tsm07-acc/15 bg-tsm07-nav">
    <div class="flex items-center gap-2.5 border-b border-tsm07-acc/15 px-4 py-[18px]">
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-[7px] bg-linear-135 from-tsm07-acc to-tsm07-acc2 text-[13px] font-bold">D</span>
      <p class="text-sm font-bold">DevDocs</p>
    </div>
    <a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 text-[13px] font-medium text-tsm07-mut transition-colors hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:border-tsm07-acc aria-[current=page]:bg-tsm07-acc/10 aria-[current=page]:text-tsm07-ink"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/></svg>Overview</a>
    <details class="group/d border-b border-tsm07-acc/15" open>
      <summary class="flex min-h-11 cursor-pointer list-none items-center gap-2.5 px-4 text-[13px] font-semibold text-tsm07-mut select-none transition-colors hover:bg-tsm07-acc/8 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 [&::-webkit-details-marker]:hidden group-open/d:text-tsm07-acc2"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg>Components<svg class="ml-auto size-4 shrink-0 transition-transform duration-300 group-open/d:rotate-90 group-open/d:text-tsm07-acc2 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></summary>
      <ul class="mb-2 ml-[26px] grid gap-px border-l border-tsm07-acc/20"><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Buttons</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Modals</a></li><li><details class="group/n" open><summary class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full cursor-pointer list-none [&::-webkit-details-marker]:hidden group-open/n:text-tsm07-ink">Forms<svg class="ml-auto size-3.5 shrink-0 transition-transform duration-300 group-open/n:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></summary><ul class="my-1 ml-4 grid gap-px border-l border-tsm07-acc/20"><li><a href="#" aria-current="page" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Text input</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Select</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Date picker</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Validation</a></li></ul></details></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Tables</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Toasts</a></li></ul>
    </details>
    <details class="group/d border-b border-tsm07-acc/15">
      <summary class="flex min-h-11 cursor-pointer list-none items-center gap-2.5 px-4 text-[13px] font-semibold text-tsm07-mut select-none transition-colors hover:bg-tsm07-acc/8 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 [&::-webkit-details-marker]:hidden group-open/d:text-tsm07-acc2"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Foundations<svg class="ml-auto size-4 shrink-0 transition-transform duration-300 group-open/d:rotate-90 group-open/d:text-tsm07-acc2 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></summary>
      <ul class="mb-2 ml-[26px] grid gap-px border-l border-tsm07-acc/20"><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Typography</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Color system</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Spacing scale</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Iconography</a></li></ul>
    </details>
    <details class="group/d border-b border-tsm07-acc/15">
      <summary class="flex min-h-11 cursor-pointer list-none items-center gap-2.5 px-4 text-[13px] font-semibold text-tsm07-mut select-none transition-colors hover:bg-tsm07-acc/8 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 [&::-webkit-details-marker]:hidden group-open/d:text-tsm07-acc2"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>Patterns<svg class="ml-auto size-4 shrink-0 transition-transform duration-300 group-open/d:rotate-90 group-open/d:text-tsm07-acc2 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></summary>
      <ul class="mb-2 ml-[26px] grid gap-px border-l border-tsm07-acc/20"><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Navigation</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Data display</a></li><li><a href="#" class="relative flex min-h-10 items-center rounded-r-lg py-2 pr-3 pl-4 text-[12.5px] font-medium text-tsm07-mut transition-colors before:absolute before:top-1/2 before:-left-px before:h-0 before:w-0.5 before:-translate-y-1/2 before:bg-tsm07-acc2 before:transition-[height] hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:bg-tsm07-acc/12 aria-[current=page]:text-tsm07-acc2 aria-[current=page]:before:h-full">Authentication</a></li></ul>
    </details>
    <a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 text-[13px] font-medium text-tsm07-mut transition-colors hover:bg-tsm07-acc/10 hover:text-tsm07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm07-acc2 aria-[current=page]:border-tsm07-acc aria-[current=page]:bg-tsm07-acc/10 aria-[current=page]:text-tsm07-ink"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg>Settings</a>
  </nav>
  <div class="min-w-0 flex-1 p-6">
    <div class="mx-auto max-w-2xl">
      <nav aria-label="Breadcrumb" class="mb-2 flex items-center gap-1.5 text-xs text-tsm07-mut">Components <svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg> Forms <svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg> <span class="text-tsm07-acc2">Text input</span></nav>
      <h1 class="text-xl font-bold">Text input</h1>
      <p class="mt-2 mb-5 max-w-prose text-[13px] leading-relaxed text-tsm07-mut text-pretty">A three-level tree on native <code class="rounded bg-tsm07-acc/15 px-1 text-tsm07-acc2">&lt;details&gt;</code>: Tab through it, press Enter to expand, and every level animates to its real height.</p>
      <div class="grid gap-3">
        <div class="rounded-xl border border-tsm07-acc/15 bg-tsm07-surface p-[18px]"><h2 class="mb-1 text-sm font-bold">Anatomy</h2><p class="text-[13px] leading-relaxed text-tsm07-mut">Label, field, helper text and error message — all wired with aria-describedby.</p></div>
        <div class="rounded-xl border border-tsm07-acc/15 bg-tsm07-surface p-[18px]"><h2 class="mb-1 text-sm font-bold">States</h2><p class="text-[13px] leading-relaxed text-tsm07-mut">Default, hover, focus, disabled, read-only and invalid, with unified ring styling.</p></div>
        <div class="rounded-xl border border-tsm07-acc/15 bg-tsm07-surface p-[18px]"><h2 class="mb-1 text-sm font-bold">Validation</h2><p class="text-[13px] leading-relaxed text-tsm07-mut">Inline messages appear on blur, never while the user is still typing.</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm07-bg: #0a1628;
  --color-tsm07-bg: oklch(0.2 0.04 258.3);
  --color-tsm07-surface: #102040;
  --color-tsm07-surface: oklch(0.249 0.065 262.6);
  --color-tsm07-nav: #0c1e38;
  --color-tsm07-nav: oklch(0.236 0.056 257.7);
  --color-tsm07-acc: #0891b2;
  --color-tsm07-acc: oklch(0.609 0.111 221.7);
  --color-tsm07-acc2: #22d3ee;
  --color-tsm07-acc2: oklch(0.797 0.134 211.5);
  --color-tsm07-ink: #e2e8f0;
  --color-tsm07-ink: oklch(0.929 0.013 255.5);
  --color-tsm07-mut: #9fb0c6;
  --color-tsm07-mut: oklch(0.751 0.037 254.9);
  --font-tsm07-sans: 'IBM Plex Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-07 {
  width: 100%;
  min-height: 100svh;
}
/* ::details-content has no Tailwind variant, so the height animation stays in CSS. */

.tsm-07 {
  interpolate-size: allow-keywords;
}

.tsm-07 details::details-content {
  block-size: 0;
  overflow: clip;
  transition: block-size 0.35s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.35s allow-discrete;
}

.tsm-07 details[open]::details-content {
  block-size: auto;
}

@media (prefers-reduced-motion: reduce) {
  .tsm-07 details::details-content {
    transition: none;
  }
}
```
