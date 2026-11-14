---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sticky-sidebar-navigation-scrolling-content/"
title: "Tailwind Sticky Sidebar Navigation with Scrolling Content"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A full-height sidebar pinned with sticky top-0 h-svh while a long article list scrolls past it, topped by a scroll-driven progress bar that needs no…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Sidebar Navigation with Scrolling Content
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sticky-sidebar-navigation-scrolling-content/

A full-height sidebar pinned with sticky top-0 h-svh while a long article list scrolls past it, topped by a scroll-driven progress bar that needs no JavaScript ([animation-timeline:scroll()]). Below 45rem of container width the sidebar folds into an icon rail whose labels stay available to screen readers via @max-[45rem]:sr-only.
## HTML
```html
<section class="tsm-06 @container relative w-full min-h-svh bg-tsm06-bg font-tsm06-sans text-tsm06-ink" aria-label="Sticky sidebar navigation with scrolling content demo">
  <div aria-hidden="true" class="fixed inset-x-0 top-0 z-30 hidden h-[3px] origin-left scale-x-0 bg-linear-to-r from-tsm06-acc to-tsm06-acc2 animate-tsm06-progress [animation-timeline:scroll()] supports-[animation-timeline:scroll()]:block"></div>
  <div class="flex">
    <nav aria-label="Main" class="sticky top-0 flex h-svh w-60 shrink-0 flex-col self-start overflow-y-auto border-r border-tsm06-acc/15 bg-tsm06-nav py-5 after:pointer-events-none after:absolute after:bottom-0 after:left-1/2 after:size-32 after:-translate-x-1/2 after:bg-[radial-gradient(circle,oklch(0.59_0.22_0/0.18),transparent_70%)] @max-[45rem]:w-16">
      <div class="mx-4 mb-4 flex items-center gap-2.5 border-b border-tsm06-acc/15 pb-4 @max-[45rem]:mx-2 @max-[45rem]:justify-center">
        <span aria-hidden="true" class="grid size-[34px] shrink-0 place-items-center rounded-lg bg-linear-135 from-tsm06-acc to-tsm06-acc2 text-sm font-extrabold">N</span>
        <p class="text-[15px] font-extrabold @max-[45rem]:sr-only">Nova <span class="ml-1 rounded-full bg-tsm06-acc/15 px-1.5 py-px text-[10px] font-bold text-tsm06-acc2">Pro</span></p>
      </div>
      <p class="mt-1 mb-1.5 px-3 text-[10px] font-bold tracking-[0.14em] text-tsm06-mut uppercase @max-[45rem]:sr-only">Content</p>
      <ul class="grid gap-0.5 px-3 @max-[45rem]:px-2">
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0" aria-current="page"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/></svg><span class="@max-[45rem]:sr-only">Articles</span><span class="ml-auto rounded-full bg-tsm06-acc/20 px-1.5 py-0.5 text-[10px] font-bold text-tsm06-acc2 @max-[45rem]:hidden">24</span></a></li>
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg><span class="@max-[45rem]:sr-only">Drafts</span><span class="ml-auto rounded-full bg-tsm06-acc/20 px-1.5 py-0.5 text-[10px] font-bold text-tsm06-acc2 @max-[45rem]:hidden">3</span></a></li>
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/></svg><span class="@max-[45rem]:sr-only">Media</span></a></li>
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span class="@max-[45rem]:sr-only">Comments</span></a></li>
      </ul>
      <p class="mt-1 mb-1.5 px-3 text-[10px] font-bold tracking-[0.14em] text-tsm06-mut uppercase @max-[45rem]:sr-only mt-3 border-t border-tsm06-acc/15 pt-3">Manage</p>
      <ul class="grid flex-1 content-start gap-0.5 px-3 @max-[45rem]:px-2">
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg><span class="@max-[45rem]:sr-only">Users</span></a></li>
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg><span class="@max-[45rem]:sr-only">Settings</span></a></li>
        <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm06-mut transition-colors hover:bg-tsm06-acc/10 hover:text-tsm06-ink focus-visible:outline-2 focus-visible:outline-tsm06-acc2 aria-[current=page]:bg-tsm06-acc/15 aria-[current=page]:text-tsm06-ink @max-[45rem]:justify-center @max-[45rem]:px-0"><svg class="size-[18px] shrink-0 group-aria-[current=page]/l:text-tsm06-acc2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 8 4.5v9L12 21l-8-4.5v-9z"/><path d="m4 7.5 8 4.5 8-4.5"/><path d="M12 12v9"/></svg><span class="@max-[45rem]:sr-only">Plugins</span></a></li>
      </ul>
      <div class="relative z-10 mx-3 mt-4 rounded-xl border border-tsm06-acc/25 bg-linear-135 from-tsm06-acc/15 to-tsm06-acc2/5 p-3.5 @max-[45rem]:hidden">
        <p class="text-[13px] font-bold">Upgrade to Team</p>
        <p class="mt-1 text-[11px] leading-normal text-tsm06-mut">Collaborate with up to 20 members and unlock analytics.</p>
        <a href="#" class="mt-2.5 inline-flex min-h-9 items-center rounded-lg bg-tsm06-acc px-3.5 text-xs font-bold text-white transition-colors hover:bg-tsm06-acc2 hover:text-tsm06-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm06-acc2">View plans →</a>
      </div>
    </nav>
    <div class="min-w-0 flex-1 px-6 py-8 @max-[45rem]:px-4">
      <div class="mx-auto max-w-2xl">
        <h1 class="text-xl font-extrabold">Articles</h1>
        <p class="mt-1 mb-6 text-[13px] leading-relaxed text-tsm06-mut text-pretty">Scroll the page: the sidebar stays pinned and the bar at the top tracks your progress.</p>
        <ul class="grid gap-3">
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Getting Started with CSS Grid Layout</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">A practical guide to template areas, named lines and implicit grids for professional web layouts.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Published · 4 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Mastering the Cascade and Specificity</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">How browsers resolve style conflicts, and why cascade layers beat specificity hacks.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Draft · 7 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Container Queries: Component-Level Responsive UI</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">Let components respond to the space they are given instead of the viewport width.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Published · 5 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Advanced Custom Properties Techniques</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">Custom properties as data channels, calculation bridges and runtime animation drivers.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Published · 6 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Scroll-Driven Animations Without JavaScript</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">Bind progress bars, reveals and parallax to scroll position with animation-timeline.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Published · 8 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">The :has() Selector in Production</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">Parent selection, quantity queries and form state — patterns that replace small scripts.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Draft · 5 min read</p></li>
          <li class="rounded-xl border border-tsm06-acc/15 bg-tsm06-surface p-4"><h2 class="mb-1.5 text-sm font-bold text-balance">Designing Accessible Focus States</h2><p class="text-[13px] leading-relaxed text-tsm06-mut">Visible, high-contrast focus rings that survive dark mode and custom components.</p><p class="mt-2 text-[11px] font-semibold text-tsm06-acc2">Published · 4 min read</p></li>
        </ul>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm06-bg: #0c0c14;
  --color-tsm06-bg: oklch(0.159 0.017 284.3);
  --color-tsm06-surface: #15151f;
  --color-tsm06-surface: oklch(0.201 0.02 284.5);
  --color-tsm06-nav: #0e0e19;
  --color-tsm06-nav: oklch(0.17 0.023 283.7);
  --color-tsm06-acc: #db2777;
  --color-tsm06-acc: oklch(0.592 0.218 0.6);
  --color-tsm06-acc2: #f472b6;
  --color-tsm06-acc2: oklch(0.725 0.175 349.8);
  --color-tsm06-ink: #f8fafc;
  --color-tsm06-ink: oklch(0.984 0.003 247.9);
  --color-tsm06-mut: #a3a3b4;
  --color-tsm06-mut: oklch(0.721 0.024 285.8);
  --font-tsm06-sans: 'Manrope', system-ui, sans-serif;
  --animate-tsm06-progress: tsm06-progress linear both;

  @keyframes tsm06-progress {
    from {
      scale: 0 1;
    }

    to {
      scale: 1 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-06 {
  width: 100%;
  min-height: 100svh;
}
```
