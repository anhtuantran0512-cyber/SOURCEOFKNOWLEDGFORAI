---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-off-canvas-push-sidebar-menu/"
title: "Tailwind Off-Canvas Push Sidebar Menu"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "The true off-canvas pattern: instead of overlapping, the whole app shell is pushed right by exactly the drawer's width — and in this port it also scales back…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Off-Canvas Push Sidebar Menu
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-off-canvas-push-sidebar-menu/

The true off-canvas pattern: instead of overlapping, the whole app shell is pushed right by exactly the drawer's width — and in this port it also scales back to 96% with a rounded edge, so the menu reads as a layer underneath the page. The nav slides in on a parallax offset (one-third of its width) for the depth of a native mobile app. Pure Tailwind.
## HTML
```html
<section class="tsm-03 group relative isolate w-full min-h-svh overflow-hidden bg-tsm03-nav font-tsm03-sans text-tsm03-ink [--tsm03-w:16.25rem]" aria-label="Off-canvas push sidebar demo">
  <input type="checkbox" id="tsm-03-toggle" class="peer sr-only">
  <nav aria-label="Main" class="invisible absolute inset-y-0 left-0 z-0 flex w-(--tsm03-w) -translate-x-1/3 flex-col py-6 opacity-60 transition-[translate,opacity,visibility] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:visible group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none">
    <div class="mx-5 mb-4 flex items-center gap-2.5 border-b border-tsm03-acc/15 pb-5">
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-tsm03-acc text-sm font-bold text-black">G</span>
      <p class="font-bold">Grove</p>
    </div>
    <ul class="grid gap-1 px-2.5">
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-lg px-3.5 text-sm font-medium text-tsm03-mut transition-colors hover:bg-tsm03-acc/10 hover:text-tsm03-ink focus-visible:outline-2 focus-visible:outline-tsm03-acc2 aria-[current=page]:bg-tsm03-acc/12 aria-[current=page]:font-semibold aria-[current=page]:text-tsm03-acc2" aria-current="page"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/></svg>Home</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-lg px-3.5 text-sm font-medium text-tsm03-mut transition-colors hover:bg-tsm03-acc/10 hover:text-tsm03-ink focus-visible:outline-2 focus-visible:outline-tsm03-acc2 aria-[current=page]:bg-tsm03-acc/12 aria-[current=page]:font-semibold aria-[current=page]:text-tsm03-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg>Analytics</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-lg px-3.5 text-sm font-medium text-tsm03-mut transition-colors hover:bg-tsm03-acc/10 hover:text-tsm03-ink focus-visible:outline-2 focus-visible:outline-tsm03-acc2 aria-[current=page]:bg-tsm03-acc/12 aria-[current=page]:font-semibold aria-[current=page]:text-tsm03-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/></svg>Reports</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-lg px-3.5 text-sm font-medium text-tsm03-mut transition-colors hover:bg-tsm03-acc/10 hover:text-tsm03-ink focus-visible:outline-2 focus-visible:outline-tsm03-acc2 aria-[current=page]:bg-tsm03-acc/12 aria-[current=page]:font-semibold aria-[current=page]:text-tsm03-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg>Team</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-lg px-3.5 text-sm font-medium text-tsm03-mut transition-colors hover:bg-tsm03-acc/10 hover:text-tsm03-ink focus-visible:outline-2 focus-visible:outline-tsm03-acc2 aria-[current=page]:bg-tsm03-acc/12 aria-[current=page]:font-semibold aria-[current=page]:text-tsm03-acc2"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg>Settings</a></li>
    </ul>
  </nav>
  <div class="relative z-10 min-h-svh origin-left bg-tsm03-bg transition-[translate,scale,border-radius,box-shadow] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:translate-x-(--tsm03-w) group-has-checked:scale-[0.96] group-has-checked:overflow-hidden group-has-checked:rounded-2xl group-has-checked:shadow-[-24px_0_60px_oklch(0_0_0/0.5)] motion-reduce:transition-none">
    <label for="tsm-03-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-20 group-has-checked:pointer-events-auto group-has-checked:cursor-pointer"></label>
    <div class="flex items-center gap-3.5 border-b border-tsm03-acc/15 px-5 py-4">
      <label for="tsm-03-toggle" data-tsm03-burger class="relative z-30 grid size-11 cursor-pointer place-content-center gap-[5px] rounded-lg border border-tsm03-acc/15 bg-tsm03-surface transition-colors hover:bg-tsm03-acc/20 group-has-[input:focus-visible]:outline-2 group-has-[input:focus-visible]:outline-offset-2 group-has-[input:focus-visible]:outline-tsm03-acc2">
        <span class="sr-only">Toggle navigation menu</span>
        <span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm03-acc2 transition-transform duration-450 group-has-checked:translate-y-[7px] group-has-checked:rotate-45"></span>
        <span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm03-acc2 transition-opacity duration-450 group-has-checked:opacity-0"></span>
        <span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm03-acc2 transition-transform duration-450 group-has-checked:-translate-y-[7px] group-has-checked:-rotate-45"></span>
      </label>
      <h1 class="text-[17px] font-bold">Dashboard</h1>
    </div>
    <div class="mx-auto max-w-3xl p-5">
      <p class="mb-5 max-w-prose text-sm leading-relaxed text-tsm03-mut text-pretty">The whole page slides right and recedes when the menu opens — a genuine push, not an overlay. Tap the pushed page to close it.</p>
      <div class="grid grid-cols-2 gap-2.5 md:grid-cols-4">
          <div class="rounded-xl border border-tsm03-acc/15 bg-tsm03-surface p-4"><p class="text-[22px] font-bold tabular-nums text-tsm03-acc2">7,291</p><p class="mt-1 text-[11px] text-tsm03-mut">Visitors</p></div>
          <div class="rounded-xl border border-tsm03-acc/15 bg-tsm03-surface p-4"><p class="text-[22px] font-bold tabular-nums text-tsm03-acc2">89%</p><p class="mt-1 text-[11px] text-tsm03-mut">Retention</p></div>
          <div class="rounded-xl border border-tsm03-acc/15 bg-tsm03-surface p-4"><p class="text-[22px] font-bold tabular-nums text-tsm03-acc2">$9.1k</p><p class="mt-1 text-[11px] text-tsm03-mut">Revenue</p></div>
          <div class="rounded-xl border border-tsm03-acc/15 bg-tsm03-surface p-4"><p class="text-[22px] font-bold tabular-nums text-tsm03-acc2">312</p><p class="mt-1 text-[11px] text-tsm03-mut">Sign-ups</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm03-bg: #0a0f0d;
  --color-tsm03-bg: oklch(0.162 0.009 168.9);
  --color-tsm03-surface: #131a16;
  --color-tsm03-surface: oklch(0.209 0.013 160);
  --color-tsm03-nav: #0d1a13;
  --color-tsm03-nav: oklch(0.203 0.023 159.9);
  --color-tsm03-acc: #10b981;
  --color-tsm03-acc: oklch(0.696 0.149 162.5);
  --color-tsm03-acc2: #34d399;
  --color-tsm03-acc2: oklch(0.773 0.153 163.2);
  --color-tsm03-ink: #ecfdf5;
  --color-tsm03-ink: oklch(0.979 0.021 166.1);
  --color-tsm03-mut: #a1aaa6;
  --color-tsm03-mut: oklch(0.73 0.012 167.7);
  --font-tsm03-sans: 'DM Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-03 {
  width: 100%;
  min-height: 100svh;
}
```
