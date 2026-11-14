---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-hamburger-menu-slide-out-drawer/"
title: "Tailwind CSS Hamburger Menu with Slide-Out Drawer (No JavaScript)"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "The most-searched mobile nav pattern, rebuilt in utilities: a hamburger that morphs to an X, a 280px drawer that slides over a blurred tap-to-close scrim,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hamburger Menu with Slide-Out Drawer (No JavaScript)
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-hamburger-menu-slide-out-drawer/

The most-searched mobile nav pattern, rebuilt in utilities: a hamburger that morphs to an X, a 280px drawer that slides over a blurred tap-to-close scrim, and an active-link rail. One checkbox drives everything through group-has-checked:, so the fragile :checked ~ .overlay ~ .drawer sibling chain is gone — the elements can sit anywhere inside the phone. Zero JavaScript.
## HTML
```html
<section class="tmn-01 w-full min-h-svh grid place-items-center bg-tmn01-stage bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tmn01-glow),transparent)] px-4 py-6 font-tmn01-sans antialiased" aria-label="Tailwind hamburger menu slide-out drawer demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn01-bg text-tmn01-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/10">
    <input type="checkbox" id="tmn-01-toggle" class="peer sr-only" aria-label="Toggle navigation drawer">
    <label for="tmn-01-toggle" class="absolute top-3.5 left-3.5 z-30 grid size-11 cursor-pointer place-content-center gap-[5px] rounded-xl bg-white/6 transition-colors hover:bg-white/12 peer-focus-visible:ring-2 peer-focus-visible:ring-tmn01-acc">
      <span class="block h-0.5 w-5.5 rounded-full bg-current transition-transform duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:translate-y-[7px] group-has-checked:rotate-45"></span>
      <span class="block h-0.5 w-5.5 rounded-full bg-current transition duration-350 group-has-checked:scale-x-0 group-has-checked:opacity-0"></span>
      <span class="block h-0.5 w-5.5 rounded-full bg-current transition-transform duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:-translate-y-[7px] group-has-checked:-rotate-45"></span>
    </label>
    <label for="tmn-01-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 bg-black/55 opacity-0 backdrop-blur-[3px] transition-opacity duration-350 group-has-checked:pointer-events-auto group-has-checked:opacity-100"></label>

    <nav aria-label="Main" class="invisible absolute inset-y-0 left-0 z-20 flex w-[min(280px,80%)] -translate-x-full flex-col bg-tmn01-drawer shadow-[24px_0_60px_-20px_oklch(0_0_0/0.7)] transition-[translate,visibility] duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:visible group-has-checked:translate-x-0">
      <div class="border-b border-white/8 px-6 pt-20 pb-6">
        <div class="mb-3 grid size-13 place-items-center rounded-full bg-linear-135 from-tmn01-acc to-tmn01-acc2 text-lg font-bold text-tmn01-drawer">AM</div>
        <p class="text-base font-semibold">Alex Mercer</p>
        <p class="text-[13px] text-tmn01-mut">[email protected]</p>
      </div>
      <div class="flex-1 overflow-y-auto py-3 text-[15px] font-medium">
        <p class="px-6 pt-3 pb-1.5 text-[11px] font-bold tracking-[0.14em] text-tmn01-mut uppercase">Main</p>
        <a href="#" aria-current="page" class="relative flex min-h-12 items-center gap-3.5 px-6 text-tmn01-ink bg-tmn01-acc/10 before:absolute before:inset-y-3 before:left-0 before:w-[3px] before:rounded-r before:bg-tmn01-acc before:content-['']"><svg viewBox="0 0 24 24" class="size-5 text-tmn01-acc" aria-hidden="true"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>Dashboard</a>
        <a href="#" class="flex min-h-12 items-center gap-3.5 px-6 text-tmn01-mut transition-colors hover:bg-white/5 hover:text-tmn01-ink focus-visible:bg-white/5 focus-visible:text-tmn01-ink focus-visible:outline-none"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M3 3v18h18M8 16v-5M13 16V8M18 16v-3"/></svg>Analytics</a>
        <a href="#" class="flex min-h-12 items-center gap-3.5 px-6 text-tmn01-mut transition-colors hover:bg-white/5 hover:text-tmn01-ink focus-visible:bg-white/5 focus-visible:text-tmn01-ink focus-visible:outline-none"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/></svg>Messages<span class="ml-auto rounded-full bg-tmn01-acc px-2 py-0.5 text-[11px] font-bold text-tmn01-drawer">3</span></a>
        <a href="#" class="flex min-h-12 items-center gap-3.5 px-6 text-tmn01-mut transition-colors hover:bg-white/5 hover:text-tmn01-ink focus-visible:bg-white/5 focus-visible:text-tmn01-ink focus-visible:outline-none"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>Projects</a>
        <p class="px-6 pt-5 pb-1.5 text-[11px] font-bold tracking-[0.14em] text-tmn01-mut uppercase">Account</p>
        <a href="#" class="flex min-h-12 items-center gap-3.5 px-6 text-tmn01-mut transition-colors hover:bg-white/5 hover:text-tmn01-ink focus-visible:bg-white/5 focus-visible:text-tmn01-ink focus-visible:outline-none"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg>Settings</a>
        <a href="#" class="flex min-h-12 items-center gap-3.5 px-6 text-tmn01-mut transition-colors hover:bg-white/5 hover:text-tmn01-ink focus-visible:bg-white/5 focus-visible:text-tmn01-ink focus-visible:outline-none"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>Notifications</a>
      </div>
      <a href="#" class="m-4 flex min-h-11 items-center justify-center gap-2 rounded-xl border border-white/10 text-sm font-semibold text-tmn01-mut transition-colors hover:border-tmn01-acc/50 hover:text-tmn01-ink"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg>Sign out</a>
    </nav>

    <main class="absolute inset-0 overflow-y-auto px-5 pt-20 pb-6">
      <p class="absolute inset-x-0 top-0 grid h-[72px] place-items-center text-[17px] font-semibold">Dashboard</p>
      <article class="mb-3 rounded-2xl border border-white/8 bg-linear-160 from-tmn01-acc/14 to-white/3 p-5">
        <span class="mb-2 inline-block rounded-full bg-tmn01-acc/18 px-2.5 py-1 text-[10px] font-bold tracking-[0.1em] text-tmn01-acc uppercase">New</span>
        <h2 class="mb-1 text-[15px] font-semibold">Q4 Revenue Report</h2>
        <p class="text-[13px] leading-relaxed text-tmn01-mut">Analytics are up <strong class="font-semibold text-tmn01-ink">24%</strong> this quarter. Tap to view the full breakdown.</p>
      </article>
      <article class="mb-3 rounded-2xl border border-white/8 bg-white/3 p-5">
        <h2 class="mb-1 text-[15px] font-semibold">Recent Activity</h2>
        <p class="text-[13px] leading-relaxed text-tmn01-mut">3 new messages and 2 pending approvals waiting for review.</p>
      </article>
      <article class="rounded-2xl border border-white/8 bg-white/3 p-5">
        <h2 class="mb-3 text-[15px] font-semibold">Active Projects</h2>
        <div class="h-1.5 overflow-hidden rounded-full bg-white/8"><div class="h-full w-3/5 rounded-full bg-linear-to-r from-tmn01-acc to-tmn01-acc2"></div></div>
        <p class="mt-2 text-[13px] text-tmn01-mut">5 in progress · 2 due this week</p>
      </article>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn01-stage: #0a0a12;
  --color-tmn01-stage: oklch(0.14 0.015 285);
  --color-tmn01-glow: #2a153099;
  --color-tmn01-glow: oklch(0.25 0.06 330 / 0.6);
  --color-tmn01-bg: #13131d;
  --color-tmn01-bg: oklch(0.19 0.02 285);
  --color-tmn01-drawer: #1a1a28;
  --color-tmn01-drawer: oklch(0.22 0.025 285);
  --color-tmn01-ink: #f1f1f6;
  --color-tmn01-ink: oklch(0.96 0.005 285);
  --color-tmn01-mut: #a3a3b8;
  --color-tmn01-mut: oklch(0.73 0.025 285);
  --color-tmn01-acc: #ff5a6e;
  --color-tmn01-acc: oklch(0.69 0.2 15);
  --color-tmn01-acc2: #ffb066;
  --color-tmn01-acc2: oklch(0.82 0.12 65);
  --font-tmn01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Icon base: utilities (text-*, size-*) still win because this sits in the base layer. */

@layer base {
  .tmn-01 svg {
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

.tmn-01 {
  width: 100%;
  min-height: 100svh;
}
```
