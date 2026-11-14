---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-slide-in-side-menu-animated-hamburger/"
title: "Tailwind Slide-In Side Menu with Animated Hamburger Icon"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A navigation drawer that slides in from the left when the hamburger is pressed, with the three bars morphing into an ✕ and each link easing in on a stagger."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-In Side Menu with Animated Hamburger Icon
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-slide-in-side-menu-animated-hamburger/

A navigation drawer that slides in from the left when the hamburger is pressed, with the three bars morphing into an ✕ and each link easing in on a stagger. The whole state machine is one visually hidden checkbox read by v4's group-has-checked: variant — so the drawer, the icon, the scrim and the link cascade all hang off the root. Zero JavaScript.
## HTML
```html
<section class="tsm-01 group relative isolate w-full min-h-svh overflow-hidden bg-tsm01-bg bg-[radial-gradient(80%_60%_at_100%_0%,var(--color-tsm01-glow),transparent_70%)] font-tsm01-sans text-tsm01-ink" aria-label="Slide-in side menu demo">
  <input type="checkbox" id="tsm-01-toggle" class="peer sr-only">
  <label for="tsm-01-toggle" data-tsm01-burger class="absolute top-5 left-5 z-50 grid size-11 cursor-pointer place-content-center gap-[5px] rounded-xl border border-tsm01-acc/30 bg-tsm01-surface transition-colors hover:border-tsm01-acc hover:bg-tsm01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsm01-acc2">
    <span class="sr-only">Toggle navigation menu</span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm01-ink transition-transform duration-400 group-has-checked:translate-y-[7px] group-has-checked:rotate-45 motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm01-ink transition-[opacity,scale] duration-400 group-has-checked:scale-x-0 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm01-ink transition-transform duration-400 group-has-checked:-translate-y-[7px] group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
  </label>
  <label for="tsm-01-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-30 bg-black/0 transition-colors duration-400 group-has-checked:pointer-events-auto group-has-checked:bg-black/45"></label>
  <nav aria-label="Main" class="invisible absolute inset-y-0 left-0 z-40 flex w-[min(280px,86vw)] -translate-x-full flex-col border-r border-tsm01-acc/20 bg-tsm01-menu pt-20 pb-6 shadow-[8px_0_40px_oklch(0_0_0/0.45)] transition-[translate,visibility] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked:visible group-has-checked:translate-x-0 motion-reduce:transition-none">
    <div class="mx-6 mb-4 flex items-center gap-3 border-b border-tsm01-acc/20 pb-5">
      <span aria-hidden="true" class="grid size-9 place-items-center rounded-[10px] bg-linear-135 from-tsm01-acc to-tsm01-acc2 font-bold">V</span>
      <div><p class="font-bold">Velocity</p><p class="text-[11px] text-tsm01-mut">Design System</p></div>
    </div>
    <ul class="grid flex-1 content-start gap-1 px-3">
      <li class="opacity-0 -translate-x-3 transition-[opacity,translate] duration-300 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[80ms] motion-reduce:transition-none"><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsm01-mut transition-colors hover:bg-tsm01-acc/15 hover:text-tsm01-ink focus-visible:outline-2 focus-visible:outline-tsm01-acc2 aria-[current=page]:bg-tsm01-acc/20 aria-[current=page]:text-tsm01-ink" aria-current="page"><span class="grid size-9 place-items-center rounded-lg bg-white/5 transition-colors group-hover/l:bg-tsm01-acc group-aria-[current=page]/l:bg-tsm01-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>Dashboard</a></li>
      <li class="opacity-0 -translate-x-3 transition-[opacity,translate] duration-300 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[125ms] motion-reduce:transition-none"><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsm01-mut transition-colors hover:bg-tsm01-acc/15 hover:text-tsm01-ink focus-visible:outline-2 focus-visible:outline-tsm01-acc2 aria-[current=page]:bg-tsm01-acc/20 aria-[current=page]:text-tsm01-ink"><span class="grid size-9 place-items-center rounded-lg bg-white/5 transition-colors group-hover/l:bg-tsm01-acc group-aria-[current=page]/l:bg-tsm01-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg></span>Analytics</a></li>
      <li class="opacity-0 -translate-x-3 transition-[opacity,translate] duration-300 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[170ms] motion-reduce:transition-none"><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsm01-mut transition-colors hover:bg-tsm01-acc/15 hover:text-tsm01-ink focus-visible:outline-2 focus-visible:outline-tsm01-acc2 aria-[current=page]:bg-tsm01-acc/20 aria-[current=page]:text-tsm01-ink"><span class="grid size-9 place-items-center rounded-lg bg-white/5 transition-colors group-hover/l:bg-tsm01-acc group-aria-[current=page]/l:bg-tsm01-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></span>Projects</a></li>
      <li class="opacity-0 -translate-x-3 transition-[opacity,translate] duration-300 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[215ms] motion-reduce:transition-none"><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsm01-mut transition-colors hover:bg-tsm01-acc/15 hover:text-tsm01-ink focus-visible:outline-2 focus-visible:outline-tsm01-acc2 aria-[current=page]:bg-tsm01-acc/20 aria-[current=page]:text-tsm01-ink"><span class="grid size-9 place-items-center rounded-lg bg-white/5 transition-colors group-hover/l:bg-tsm01-acc group-aria-[current=page]/l:bg-tsm01-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg></span>Messages</a></li>
      <li class="opacity-0 -translate-x-3 transition-[opacity,translate] duration-300 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[260ms] motion-reduce:transition-none"><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsm01-mut transition-colors hover:bg-tsm01-acc/15 hover:text-tsm01-ink focus-visible:outline-2 focus-visible:outline-tsm01-acc2 aria-[current=page]:bg-tsm01-acc/20 aria-[current=page]:text-tsm01-ink"><span class="grid size-9 place-items-center rounded-lg bg-white/5 transition-colors group-hover/l:bg-tsm01-acc group-aria-[current=page]/l:bg-tsm01-acc"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg></span>Settings</a></li>
    </ul>
    <div class="mx-6 flex items-center gap-3 border-t border-tsm01-acc/20 pt-4">
      <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-linear-135 from-amber-500 to-red-500 text-[13px] font-bold">JD</span>
      <div><p class="text-[13px] font-semibold">Jane Doe</p><p class="text-[11px] text-tsm01-mut">Pro plan</p></div>
    </div>
  </nav>
  <div class="mx-auto w-full max-w-3xl px-6 pt-24 pb-10">
    <h1 class="text-[clamp(22px,3vw,28px)] font-bold tracking-tight">Welcome back, Jane</h1>
    <p class="mt-2 mb-7 max-w-prose text-sm leading-relaxed text-tsm01-mut text-pretty">Press the menu button to slide the drawer in. Click the dimmed page or press the button again to close it.</p>
    <div class="grid grid-cols-2 gap-3 md:grid-cols-4">
      <div class="rounded-2xl border border-tsm01-acc/20 bg-tsm01-surface p-4"><p class="text-2xl font-bold tabular-nums text-tsm01-acc2">2,847</p><p class="mt-1 text-xs text-tsm01-mut">Page views</p></div>
      <div class="rounded-2xl border border-tsm01-acc/20 bg-tsm01-surface p-4"><p class="text-2xl font-bold tabular-nums text-tsm01-acc2">94%</p><p class="mt-1 text-xs text-tsm01-mut">Uptime</p></div>
      <div class="rounded-2xl border border-tsm01-acc/20 bg-tsm01-surface p-4"><p class="text-2xl font-bold tabular-nums text-tsm01-acc2">$12.4k</p><p class="mt-1 text-xs text-tsm01-mut">Revenue</p></div>
      <div class="rounded-2xl border border-tsm01-acc/20 bg-tsm01-surface p-4"><p class="text-2xl font-bold tabular-nums text-tsm01-acc2">483</p><p class="mt-1 text-xs text-tsm01-mut">Users</p></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm01-bg: #0f172a;
  --color-tsm01-bg: oklch(0.208 0.04 265.8);
  --color-tsm01-glow: #2a1650;
  --color-tsm01-glow: oklch(0.265 0.101 294.4);
  --color-tsm01-surface: #1e293b;
  --color-tsm01-surface: oklch(0.279 0.037 260);
  --color-tsm01-menu: #1a1033;
  --color-tsm01-menu: oklch(0.209 0.066 293);
  --color-tsm01-acc: #7c3aed;
  --color-tsm01-acc: oklch(0.541 0.247 293);
  --color-tsm01-acc2: #a78bfa;
  --color-tsm01-acc2: oklch(0.709 0.159 293.5);
  --color-tsm01-ink: #e2e8f0;
  --color-tsm01-ink: oklch(0.929 0.013 255.5);
  --color-tsm01-mut: #a3aec2;
  --color-tsm01-mut: oklch(0.749 0.031 262.5);
  --font-tsm01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-01 {
  width: 100%;
  min-height: 100svh;
}
```
