---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/responsive-tailwind-sidebar-mobile-hamburger-toggle/"
title: "Responsive Tailwind Sidebar with Mobile Hamburger Toggle"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "One markup, two layouts: a permanent sidebar column on wide containers that becomes an off-canvas drawer with a hamburger toggle on narrow ones."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Sidebar with Mobile Hamburger Toggle
Source: https://codefronts.com/navigation/tailwind-css-side-menus/responsive-tailwind-sidebar-mobile-hamburger-toggle/

One markup, two layouts: a permanent sidebar column on wide containers that becomes an off-canvas drawer with a hamburger toggle on narrow ones. The port switches on a container query (@max-[40rem]:) rather than the viewport, so the component responds to the space it is given — a sidebar inside a split pane collapses correctly even on a 27-inch monitor.
## HTML
```html
<section class="tsm-05 @container w-full min-h-svh bg-tsm05-bg font-tsm05-sans text-tsm05-ink" aria-label="Responsive sidebar with mobile hamburger toggle demo">
  <div class="group relative flex min-h-svh overflow-hidden">
    <input type="checkbox" id="tsm-05-toggle" class="peer sr-only">
    <label for="tsm-05-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 hidden bg-tsm05-ink/0 transition-colors @max-[40rem]:block @max-[40rem]:group-has-checked:pointer-events-auto @max-[40rem]:group-has-checked:bg-tsm05-ink/35"></label>
    <nav aria-label="Main" class="flex w-60 shrink-0 flex-col border-r border-tsm05-line bg-tsm05-surface py-5 transition-[translate,visibility] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] @max-[40rem]:invisible @max-[40rem]:absolute @max-[40rem]:inset-y-0 @max-[40rem]:left-0 @max-[40rem]:z-20 @max-[40rem]:-translate-x-full @max-[40rem]:shadow-[8px_0_32px_oklch(0.2_0.03_265/0.18)] @max-[40rem]:group-has-checked:visible @max-[40rem]:group-has-checked:translate-x-0 motion-reduce:transition-none">
      <div class="mx-5 mb-3 flex items-center gap-2.5 border-b border-tsm05-line pb-4">
        <span aria-hidden="true" class="grid size-[34px] place-items-center rounded-lg bg-linear-135 from-tsm05-acc to-tsm05-acc2 text-[15px] font-extrabold text-white">P</span>
        <p class="text-[15px] font-extrabold">Prism UI</p>
      </div>
      <p class="px-5 pt-2 pb-1 text-[10px] font-bold tracking-[0.12em] text-tsm05-mut uppercase">Main menu</p>
      <ul class="grid gap-0.5 px-2.5">
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc" aria-current="page"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/></svg>Home</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/></svg>Reports<span class="ml-auto rounded-full bg-tsm05-acc px-2 py-0.5 text-[10px] font-bold text-white">4</span></a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10v4h4l8 5V5l-8 5z"/><path d="M19 9a4 4 0 0 1 0 6"/></svg>Campaigns</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg>Audience</a></li>
      </ul>
      <p class="px-5 pt-2 pb-1 text-[10px] font-bold tracking-[0.12em] text-tsm05-mut uppercase mt-3 border-t border-tsm05-line pt-4">Account</p>
      <ul class="grid flex-1 content-start gap-0.5 px-2.5">
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Profile</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-2.5 rounded-[10px] px-3.5 text-sm font-semibold text-tsm05-mut transition-colors hover:bg-tsm05-acc/8 hover:text-tsm05-acc focus-visible:outline-2 focus-visible:outline-tsm05-acc aria-[current=page]:bg-tsm05-acc/10 aria-[current=page]:text-tsm05-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg>Settings</a></li>
      </ul>
      <div class="mx-4 flex items-center gap-2.5 border-t border-tsm05-line pt-4">
        <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-indigo-500 to-purple-500 text-xs font-bold text-white">SR</span>
        <div><p class="text-[13px] font-bold">Sam R.</p><p class="text-[11px] text-tsm05-mut">Editor</p></div>
      </div>
    </nav>
    <div class="min-w-0 flex-1">
      <div class="flex items-center gap-3.5 border-b border-tsm05-line bg-tsm05-surface px-5 py-3.5">
        <label for="tsm-05-toggle" class="hidden size-11 cursor-pointer place-content-center gap-1 rounded-lg border border-tsm05-line bg-tsm05-bg transition-colors hover:bg-tsm05-acc/10 group-has-[input:focus-visible]:outline-2 group-has-[input:focus-visible]:outline-offset-2 group-has-[input:focus-visible]:outline-tsm05-acc @max-[40rem]:grid">
          <span class="sr-only">Toggle navigation menu</span>
          <span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm05-mut"></span><span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm05-mut"></span><span aria-hidden="true" class="block h-0.5 w-4 rounded-full bg-tsm05-mut"></span>
        </label>
        <h1 class="text-base font-extrabold">Home</h1>
        <nav aria-label="Breadcrumb" class="ml-auto text-xs text-tsm05-mut @max-[28rem]:hidden">Prism <span aria-hidden="true">/</span> Home</nav>
      </div>
      <div class="mx-auto max-w-3xl px-5 py-6">
        <p class="text-[19px] font-extrabold">Good morning, Sam</p>
        <p class="mt-1.5 mb-5 max-w-prose text-[13px] leading-relaxed text-tsm05-mut text-pretty">The sidebar is a column while this component is wider than 640px. Narrow it (or switch the preview to mobile) and it becomes a drawer behind the menu button.</p>
        <div class="grid grid-cols-2 gap-2.5 @3xl:grid-cols-4">
          <div class="rounded-xl border border-tsm05-line bg-tsm05-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.03_265/0.06)]"><p class="text-[22px] font-extrabold tabular-nums text-tsm05-acc">5,382</p><p class="mt-1 text-xs text-tsm05-mut">Sessions</p></div>
          <div class="rounded-xl border border-tsm05-line bg-tsm05-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.03_265/0.06)]"><p class="text-[22px] font-extrabold tabular-nums text-tsm05-acc">63%</p><p class="mt-1 text-xs text-tsm05-mut">Conversion</p></div>
          <div class="rounded-xl border border-tsm05-line bg-tsm05-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.03_265/0.06)]"><p class="text-[22px] font-extrabold tabular-nums text-tsm05-acc">228</p><p class="mt-1 text-xs text-tsm05-mut">Subscribers</p></div>
          <div class="rounded-xl border border-tsm05-line bg-tsm05-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.03_265/0.06)]"><p class="text-[22px] font-extrabold tabular-nums text-tsm05-acc">$4.8k</p><p class="mt-1 text-xs text-tsm05-mut">Revenue</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm05-bg: #f8fafc;
  --color-tsm05-bg: oklch(0.984 0.003 247.9);
  --color-tsm05-surface: #ffffff;
  --color-tsm05-surface: oklch(1 0 0);
  --color-tsm05-line: #e2e8f0;
  --color-tsm05-line: oklch(0.929 0.013 255.5);
  --color-tsm05-acc: #6366f1;
  --color-tsm05-acc: oklch(0.585 0.204 277.1);
  --color-tsm05-acc2: #818cf8;
  --color-tsm05-acc2: oklch(0.68 0.158 276.9);
  --color-tsm05-ink: #1e293b;
  --color-tsm05-ink: oklch(0.279 0.037 260);
  --color-tsm05-mut: #5b6b80;
  --color-tsm05-mut: oklch(0.522 0.039 255.3);
  --font-tsm05-sans: 'Nunito', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-05 {
  width: 100%;
  min-height: 100svh;
}
```
