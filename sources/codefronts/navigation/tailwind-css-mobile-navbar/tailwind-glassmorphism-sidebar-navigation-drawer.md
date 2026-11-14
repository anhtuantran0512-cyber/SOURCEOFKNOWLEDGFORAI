---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-glassmorphism-sidebar-navigation-drawer/"
title: "Tailwind Glassmorphism Sidebar Navigation Drawer"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A frosted-glass drawer floating over three drifting colour blobs, with a glass avatar, gradient-tinted active link and an upgrade card."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Sidebar Navigation Drawer
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-glassmorphism-sidebar-navigation-drawer/

A frosted-glass drawer floating over three drifting colour blobs, with a glass avatar, gradient-tinted active link and an upgrade card. The port turns each blob's keyframes into an @theme animation token, and adds a supports-[backdrop-filter]: fallback so browsers without blur get a solid, readable panel. Zero JavaScript.
## HTML
```html
<section class="tmn-10 w-full min-h-svh grid place-items-center bg-tmn10-stage px-4 py-6 font-tmn10-sans antialiased" aria-label="Tailwind glassmorphism sidebar drawer demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] text-white shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/10">
    <div aria-hidden="true" class="absolute inset-0 bg-linear-135 from-[#1a0533] via-[#0a0a2a] to-[#001a33]">
      <span class="absolute -top-20 -left-16 size-64 rounded-full bg-[radial-gradient(circle,var(--color-tmn10-b1),transparent_70%)] opacity-70 blur-[60px] will-change-transform animate-tmn10-drift-a motion-reduce:animate-none"></span>
      <span class="absolute -right-10 -bottom-10 size-52 rounded-full bg-[radial-gradient(circle,var(--color-tmn10-b2),transparent_70%)] opacity-70 blur-[60px] will-change-transform animate-tmn10-drift-b motion-reduce:animate-none"></span>
      <span class="absolute top-1/2 left-3/5 size-40 rounded-full bg-[radial-gradient(circle,var(--color-tmn10-b3),transparent_70%)] opacity-70 blur-[60px] will-change-transform animate-tmn10-drift-c motion-reduce:animate-none"></span>
    </div>

    <input type="checkbox" id="tmn-10-toggle" class="peer sr-only" aria-label="Toggle navigation drawer">
    <header class="absolute inset-x-0 top-0 z-10 flex h-16 items-center justify-between border-b border-white/8 px-5 backdrop-blur-md">
      <p class="text-lg font-bold tracking-[-0.02em]">Aura<span class="bg-linear-to-r from-violet-300 to-sky-300 bg-clip-text text-transparent">UI</span></p>
      <label for="tmn-10-toggle" class="grid size-11 cursor-pointer place-content-center gap-[5px] rounded-xl border border-white/15 bg-white/10 transition-colors hover:bg-white/16 peer-focus-visible:ring-2 peer-focus-visible:ring-violet-300">
        <span class="block h-0.5 w-4.5 rounded-full bg-white transition-transform duration-350 group-has-checked:translate-y-[7px] group-has-checked:rotate-45"></span>
        <span class="block h-0.5 w-4.5 rounded-full bg-white transition-opacity duration-200 group-has-checked:opacity-0"></span>
        <span class="block h-0.5 w-4.5 rounded-full bg-white transition-transform duration-350 group-has-checked:-translate-y-[7px] group-has-checked:-rotate-45"></span>
      </label>
    </header>

    <main class="absolute inset-x-0 top-16 bottom-0 z-[5] overflow-y-auto px-5 py-6">
      <h1 class="mb-1.5 text-2xl font-bold tracking-[-0.03em]">Good evening, Morgan</h1>
      <p class="mb-6 text-[13px] text-white/65">Here's your workspace overview</p>
      <article class="mb-3 rounded-2xl border border-white/12 bg-white/6 p-4.5 backdrop-blur-md"><div class="mb-3 h-[3px] rounded-full bg-linear-to-r from-violet-400 to-sky-400"></div><h2 class="mb-1 text-sm font-semibold">Active projects</h2><p class="text-[13px] text-white/65">8 running &mdash; 3 due this week</p></article>
      <article class="mb-3 rounded-2xl border border-white/12 bg-white/6 p-4.5 backdrop-blur-md"><div class="mb-3 h-[3px] rounded-full bg-linear-to-r from-pink-400 to-orange-400"></div><h2 class="mb-1 text-sm font-semibold">Recent designs</h2><p class="text-[13px] text-white/65">Landing page refresh · 20 min ago</p></article>
      <article class="rounded-2xl border border-white/12 bg-white/6 p-4.5 backdrop-blur-md"><div class="mb-3 h-[3px] rounded-full bg-linear-to-r from-green-400 to-cyan-400"></div><h2 class="mb-1 text-sm font-semibold">Team activity</h2><p class="flex items-center gap-2 text-[13px] text-white/65"><span class="flex -space-x-1.5"><span class="size-5 rounded-full bg-violet-400 ring-2 ring-[#120a2e]"></span><span class="size-5 rounded-full bg-sky-400 ring-2 ring-[#120a2e]"></span><span class="size-5 rounded-full bg-pink-400 ring-2 ring-[#120a2e]"></span></span>4 collaborators online</p></article>
    </main>

    <label for="tmn-10-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-[15] bg-black/30 opacity-0 backdrop-blur-[3px] transition-opacity duration-350 group-has-checked:pointer-events-auto group-has-checked:opacity-100"></label>

    <nav aria-label="Workspace" class="invisible absolute inset-y-0 left-0 z-20 flex w-[min(285px,80%)] -translate-x-full flex-col border-r border-white/12 bg-tmn10-panel/95 backdrop-blur-2xl backdrop-saturate-180 transition-[translate,visibility] duration-400 ease-[cubic-bezier(.4,0,.2,1)] supports-[backdrop-filter:blur(1px)]:bg-white/8 group-has-checked:visible group-has-checked:translate-x-0">
      <div class="border-b border-white/8 px-6 pt-20 pb-6">
        <span class="mb-3.5 grid size-14 place-items-center rounded-full border-2 border-white/30 bg-linear-135 from-violet-400/50 to-sky-400/50 text-lg font-bold backdrop-blur">ML</span>
        <p class="text-base font-semibold">Morgan Lee</p>
        <p class="text-[13px] text-white/60">[email protected]</p>
      </div>
      <div class="flex-1 overflow-y-auto py-3 text-sm font-medium">
        <p class="px-6 pt-3 pb-1 text-[11px] font-bold tracking-[0.14em] text-white/50 uppercase">Workspace</p>
        <a href="#" aria-current="page" class="mx-3 flex min-h-11 items-center gap-3 rounded-xl bg-linear-to-r from-violet-400/25 to-sky-400/10 px-3 text-white ring-1 ring-white/12"><svg viewBox="0 0 24 24" class="size-4.5 text-violet-300" aria-hidden="true"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>Dashboard</a>
        <a href="#" class="mx-3 flex min-h-11 items-center gap-3 rounded-xl px-3 text-white/75 transition-colors hover:bg-white/8 hover:text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="13.5" cy="6.5" r="1.5"/><circle cx="17.5" cy="10.5" r="1.5"/><circle cx="8.5" cy="7.5" r="1.5"/><circle cx="6.5" cy="12.5" r="1.5"/><path d="M12 2a10 10 0 0 0 0 20 2 2 0 0 0 2-2c0-.5-.2-1-.5-1.3a2 2 0 0 1 1.5-3.3H17a5 5 0 0 0 5-5C22 6 17.5 2 12 2z"/></svg>Design<span class="ml-auto rounded-full bg-violet-400/25 px-2 py-0.5 text-[11px] font-bold text-violet-200">3</span></a>
        <a href="#" class="mx-3 flex min-h-11 items-center gap-3 rounded-xl px-3 text-white/75 transition-colors hover:bg-white/8 hover:text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M3 3v18h18M8 16v-5M13 16V8M18 16v-3"/></svg>Analytics</a>
        <a href="#" class="mx-3 flex min-h-11 items-center gap-3 rounded-xl px-3 text-white/75 transition-colors hover:bg-white/8 hover:text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>Integrations</a>
        <p class="px-6 pt-5 pb-1 text-[11px] font-bold tracking-[0.14em] text-white/50 uppercase">Account</p>
        <a href="#" class="mx-3 flex min-h-11 items-center gap-3 rounded-xl px-3 text-white/75 transition-colors hover:bg-white/8 hover:text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg>Settings</a>
      </div>
      <div class="m-4 mt-2 rounded-2xl border border-violet-300/30 bg-linear-135 from-violet-600/30 to-sky-500/15 p-4">
        <p class="mb-1 text-[13px] font-semibold">Upgrade to Pro</p>
        <p class="mb-3 text-xs leading-normal text-white/70">Unlimited projects, advanced analytics and priority support.</p>
        <a href="#" class="grid min-h-10 place-items-center rounded-lg bg-linear-to-r from-violet-600 to-sky-500 text-[13px] font-semibold">Upgrade now</a>
      </div>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn10-stage: #07051a;
  --color-tmn10-stage: oklch(0.14 0.04 285);
  --color-tmn10-panel: #1d1640;
  --color-tmn10-panel: oklch(0.24 0.07 285);
  --color-tmn10-b1: #7c3aed;
  --color-tmn10-b1: oklch(0.54 0.25 293);
  --color-tmn10-b2: #0ea5e9;
  --color-tmn10-b2: oklch(0.68 0.15 237);
  --color-tmn10-b3: #ec4899;
  --color-tmn10-b3: oklch(0.66 0.21 354);
  --font-tmn10-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tmn10-drift-a: tmn10-drift-a 9s ease-in-out infinite;
  --animate-tmn10-drift-b: tmn10-drift-b 11s ease-in-out infinite;
  --animate-tmn10-drift-c: tmn10-drift-c 13s ease-in-out infinite;

  @keyframes tmn10-drift-a {
    0%,
        100% {
      translate: 0 0;
    }

    50% {
      translate: 40px 36px;
    }
  }

  @keyframes tmn10-drift-b {
    0%,
        100% {
      translate: 0 0;
    }

    50% {
      translate: -30px -28px;
    }
  }

  @keyframes tmn10-drift-c {
    0%,
        100% {
      translate: 0 0;
      scale: 1;
    }

    50% {
      translate: -24px 16px;
      scale: 1.25;
    }
  }
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-10 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-10 {
  width: 100%;
  min-height: 100svh;
}
```
