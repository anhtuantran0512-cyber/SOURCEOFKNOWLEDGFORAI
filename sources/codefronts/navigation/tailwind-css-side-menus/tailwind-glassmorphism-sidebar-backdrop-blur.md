---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-glassmorphism-sidebar-backdrop-blur/"
title: "Tailwind Glassmorphism Sidebar with Backdrop Blur"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A frosted-glass sidebar floating over three slowly drifting colour blobs, blurred and colour-boosted with backdrop-blur-xl backdrop-saturate-180."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Sidebar with Backdrop Blur
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-glassmorphism-sidebar-backdrop-blur/

A frosted-glass sidebar floating over three slowly drifting colour blobs, blurred and colour-boosted with backdrop-blur-xl backdrop-saturate-180. The port adds what most glass tutorials skip: a supports-[backdrop-filter:blur(1px)]: fallback to a near-opaque panel, a specular top edge, and legible 72%-white text instead of the original's 50%.
## HTML
```html
<section class="tsm-10 relative isolate flex w-full min-h-svh overflow-hidden bg-tsm10-bg font-tsm10-sans text-white" aria-label="Glassmorphism sidebar with backdrop blur demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10">
    <div class="absolute -top-16 left-5 size-72 rounded-full bg-tsm10-violet opacity-60 blur-[64px] animate-tsm10-drift-a motion-reduce:animate-none"></div>
    <div class="absolute -bottom-10 left-24 size-56 rounded-full bg-tsm10-sky opacity-60 blur-[64px] animate-tsm10-drift-b motion-reduce:animate-none"></div>
    <div class="absolute top-[40%] right-[6%] size-52 rounded-full bg-tsm10-mint opacity-55 blur-[64px] animate-tsm10-drift-c motion-reduce:animate-none"></div>
  </div>
  <nav aria-label="Main" class="flex w-[232px] shrink-0 flex-col border-r border-white/12 py-6 shadow-[inset_0_1px_0_oklch(1_0_0/0.18),4px_0_40px_oklch(0_0_0/0.3)] bg-tsm10-bg/80 supports-[backdrop-filter:blur(1px)]:bg-white/7 backdrop-blur-xl backdrop-saturate-180">
    <div class="mx-[18px] mb-4 flex items-center gap-3 border-b border-white/8 pb-[18px]">
      <span aria-hidden="true" class="grid size-9 place-items-center rounded-[10px] border border-white/20 bg-white/12"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg></span>
      <p class="text-[15px] font-bold">Crystal</p>
    </div>
    <ul class="grid gap-1 px-2.5">
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]" aria-current="page"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/></svg>Home</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>Explore</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19a2 2 0 0 1 2-2h14V3H6a2 2 0 0 0-2 2z"/><path d="M4 19a2 2 0 0 0 2 2h14v-4"/></svg>Library<span class="ml-auto rounded-full bg-white/16 px-2 py-0.5 text-[10px] font-bold text-white">7</span></a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>Messages<span class="ml-auto rounded-full bg-white/16 px-2 py-0.5 text-[10px] font-bold text-white">3</span></a></li>
      <li aria-hidden="true" class="mx-2.5 my-2 h-px bg-white/8"></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Account</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-xl border border-transparent px-3.5 text-[13px] font-semibold text-white/72 transition-[color,background-color,border-color] duration-250 hover:border-white/12 hover:bg-white/9 hover:text-white focus-visible:outline-2 focus-visible:outline-white/80 aria-[current=page]:border-white/20 aria-[current=page]:bg-white/14 aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg>Settings</a></li>
    </ul>
    <div class="mx-2.5 mt-auto flex items-center gap-2.5 rounded-xl border border-white/12 bg-white/7 p-3">
      <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full bg-linear-135 from-violet-600 to-sky-500 text-xs font-bold">LM</span>
      <div><p class="text-xs font-bold">Lena M.</p><p class="text-[10px] text-white/72">Creator</p></div>
    </div>
  </nav>
  <div class="min-w-0 flex-1 p-6">
    <div class="mx-auto max-w-3xl">
      <h1 class="text-xl font-bold">Home feed</h1>
      <p class="mt-1.5 mb-6 max-w-prose text-[13px] leading-relaxed text-white/72 text-pretty">The sidebar and cards are frosted glass: whatever colour drifts behind them is blurred and boosted. Without backdrop-filter they fall back to a solid tint.</p>
      <div class="grid grid-cols-2 gap-3 md:grid-cols-4">
        <div class="rounded-2xl border border-white/12 p-4 shadow-[inset_0_1px_0_oklch(1_0_0/0.12)] bg-tsm10-bg/80 supports-[backdrop-filter:blur(1px)]:bg-white/7 backdrop-blur-xl backdrop-saturate-180"><p class="text-[22px] font-bold tabular-nums">12.4k</p><p class="mt-1 text-xs text-white/72">Followers</p></div>
        <div class="rounded-2xl border border-white/12 p-4 shadow-[inset_0_1px_0_oklch(1_0_0/0.12)] bg-tsm10-bg/80 supports-[backdrop-filter:blur(1px)]:bg-white/7 backdrop-blur-xl backdrop-saturate-180"><p class="text-[22px] font-bold tabular-nums">892</p><p class="mt-1 text-xs text-white/72">Likes today</p></div>
        <div class="rounded-2xl border border-white/12 p-4 shadow-[inset_0_1px_0_oklch(1_0_0/0.12)] bg-tsm10-bg/80 supports-[backdrop-filter:blur(1px)]:bg-white/7 backdrop-blur-xl backdrop-saturate-180"><p class="text-[22px] font-bold tabular-nums">47</p><p class="mt-1 text-xs text-white/72">Published</p></div>
        <div class="rounded-2xl border border-white/12 p-4 shadow-[inset_0_1px_0_oklch(1_0_0/0.12)] bg-tsm10-bg/80 supports-[backdrop-filter:blur(1px)]:bg-white/7 backdrop-blur-xl backdrop-saturate-180"><p class="text-[22px] font-bold tabular-nums">3.2k</p><p class="mt-1 text-xs text-white/72">Views</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm10-bg: #0d0d1a;
  --color-tsm10-bg: oklch(0.166 0.027 283.1);
  --color-tsm10-violet: #7c3aed;
  --color-tsm10-violet: oklch(0.541 0.247 293);
  --color-tsm10-sky: #0ea5e9;
  --color-tsm10-sky: oklch(0.685 0.148 237.3);
  --color-tsm10-mint: #10b981;
  --color-tsm10-mint: oklch(0.696 0.149 162.5);
  --font-tsm10-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tsm10-drift-a: tsm10-drift-a 12s ease-in-out infinite alternate;
  --animate-tsm10-drift-b: tsm10-drift-b 14s ease-in-out infinite alternate;
  --animate-tsm10-drift-c: tsm10-drift-c 10s ease-in-out infinite alternate;

  @keyframes tsm10-drift-a {
    to {
      translate: 30px 40px;
      scale: 1.1;
    }
  }

  @keyframes tsm10-drift-b {
    to {
      translate: -20px -30px;
      scale: 0.9;
    }
  }

  @keyframes tsm10-drift-c {
    to {
      translate: 10px 20px;
      scale: 1.05;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-10 {
  width: 100%;
  min-height: 100svh;
}
```
