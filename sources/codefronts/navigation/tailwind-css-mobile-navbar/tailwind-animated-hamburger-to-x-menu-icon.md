---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-animated-hamburger-to-x-menu-icon/"
title: "Tailwind Animated Hamburger to X Icon with Dropdown Menu"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A developer-dashboard navbar whose asymmetric hamburger (16 / 24 / 20px bars) morphs into a centred X while a menu panel drops in beneath with staggered rows."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Hamburger to X Icon with Dropdown Menu
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-animated-hamburger-to-x-menu-icon/

A developer-dashboard navbar whose asymmetric hamburger (16 / 24 / 20px bars) morphs into a centred X while a menu panel drops in beneath with staggered rows. The port adds the scrim the original lacked, so tapping the page closes the menu. Zero JavaScript.
## HTML
```html
<section class="tmn-04 w-full min-h-svh grid place-items-center bg-tmn04-stage px-4 py-6 font-tmn04-sans antialiased" aria-label="Tailwind animated hamburger to X menu demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn04-bg text-tmn04-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/8">
    <input type="checkbox" id="tmn-04-toggle" class="peer sr-only" aria-label="Toggle menu">
    <header class="absolute inset-x-0 top-0 z-30 flex h-[60px] items-center justify-between border-b border-tmn04-line bg-tmn04-bg px-4">
      <p class="flex items-center gap-2.5 text-base font-bold tracking-[-0.02em]"><span class="grid size-7 place-items-center rounded-lg bg-tmn04-acc text-tmn04-bg"><svg viewBox="0 0 24 24" class="size-4" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5"/></svg></span>DevHub</p>
      <label for="tmn-04-toggle" class="relative grid size-11 cursor-pointer place-items-center rounded-xl transition-colors hover:bg-white/6 group-has-[#tmn-04-toggle:focus-visible]:ring-2 group-has-[#tmn-04-toggle:focus-visible]:ring-tmn04-acc">
        <span class="absolute right-2.5 h-0.5 w-4 -translate-y-[7px] rounded-full bg-current transition-all duration-400 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked:w-6 group-has-checked:translate-y-0 group-has-checked:rotate-45"></span>
        <span class="absolute right-2.5 h-0.5 w-6 rounded-full bg-current transition-all duration-400 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked:scale-x-0 group-has-checked:opacity-0"></span>
        <span class="absolute right-2.5 h-0.5 w-5 translate-y-[7px] rounded-full bg-current transition-all duration-400 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked:w-6 group-has-checked:translate-y-0 group-has-checked:-rotate-45"></span>
      </label>
    </header>

    <label for="tmn-04-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 top-[60px] z-10 bg-black/50 opacity-0 transition-opacity duration-300 group-has-checked:pointer-events-auto group-has-checked:opacity-100"></label>

    <nav aria-label="Main" class="invisible absolute inset-x-0 top-[60px] z-20 -translate-y-3 rounded-b-3xl border-b border-tmn04-line bg-tmn04-surface pt-2 pb-4 opacity-0 shadow-[0_30px_60px_-20px_oklch(0_0_0/0.7)] transition-all duration-400 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:opacity-100">
      <p class="px-5 pt-3 pb-1 font-tmn04-mono text-[11px] tracking-[0.12em] text-tmn04-mut uppercase">Explore</p>
      <a href="#" aria-current="page" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[60ms] hover:bg-tmn04-acc/8 aria-[current=page]:text-tmn04-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>Dashboard</a>
      <a href="#" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[100ms] hover:bg-tmn04-acc/8"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/></svg>Repositories<span class="ml-auto rounded-full bg-white/8 px-2 py-0.5 font-tmn04-mono text-[11px] text-tmn04-mut">12</span></a>
      <a href="#" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[140ms] hover:bg-tmn04-acc/8"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="6" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/><path d="M6 8v8M18 16V9a3 3 0 0 0-3-3h-4"/></svg>Pull requests<span class="ml-auto rounded-full bg-tmn04-acc px-2 py-0.5 font-tmn04-mono text-[11px] font-semibold text-tmn04-bg">3</span></a>
      <a href="#" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[180ms] hover:bg-tmn04-acc/8"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="1.5"/></svg>Issues</a>
      <div class="mx-5 my-2 h-px bg-tmn04-line"></div>
      <p class="px-5 pt-2 pb-1 font-tmn04-mono text-[11px] tracking-[0.12em] text-tmn04-mut uppercase">Account</p>
      <a href="#" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[220ms] hover:bg-tmn04-acc/8"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Profile</a>
      <a href="#" class="flex min-h-11 translate-y-1 items-center gap-3 px-5 text-[15px] opacity-0 transition duration-300 group-has-checked:translate-y-0 group-has-checked:opacity-100 group-has-checked:delay-[260ms] hover:bg-tmn04-acc/8"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg>Settings</a>
    </nav>

    <main class="absolute inset-x-0 top-[60px] bottom-0 overflow-y-auto px-4 pt-6 pb-6">
      <p class="mb-1 text-[13px] text-tmn04-mut">Good morning</p>
      <h1 class="mb-5 text-[22px] font-bold tracking-[-0.02em]">Welcome back, Dev</h1>
      <article class="mb-2.5 rounded-xl border border-tmn04-line bg-tmn04-surface p-4 transition-colors hover:border-tmn04-acc/60">
        <h2 class="mb-1.5 font-tmn04-mono text-sm font-medium text-tmn04-acc">ui-components</h2>
        <p class="mb-3 text-[13px] leading-normal text-tmn04-mut">Production-ready React components built with TypeScript.</p>
        <p class="flex gap-4 text-xs text-tmn04-mut"><span class="flex items-center gap-1.5"><span class="size-2.5 rounded-full bg-[#3178c6]"></span>TypeScript</span><span>★ 842</span><span>⑂ 124</span></p>
      </article>
      <article class="mb-2.5 rounded-xl border border-tmn04-line bg-tmn04-surface p-4 transition-colors hover:border-tmn04-acc/60">
        <h2 class="mb-1.5 font-tmn04-mono text-sm font-medium text-tmn04-acc">api-gateway</h2>
        <p class="mb-3 text-[13px] leading-normal text-tmn04-mut">High-performance gateway with rate limiting and auth middleware.</p>
        <p class="flex gap-4 text-xs text-tmn04-mut"><span class="flex items-center gap-1.5"><span class="size-2.5 rounded-full bg-[#00add8]"></span>Go</span><span>★ 231</span><span>⑂ 48</span></p>
      </article>
      <article class="rounded-xl border border-tmn04-line bg-tmn04-surface p-4 transition-colors hover:border-tmn04-acc/60">
        <h2 class="mb-1.5 font-tmn04-mono text-sm font-medium text-tmn04-acc">css-animations</h2>
        <p class="mb-3 text-[13px] leading-normal text-tmn04-mut">60+ CSS animation demos with no dependencies.</p>
        <p class="flex gap-4 text-xs text-tmn04-mut"><span class="flex items-center gap-1.5"><span class="size-2.5 rounded-full bg-[#e34c26]"></span>CSS</span><span>★ 1.2k</span><span>⑂ 307</span></p>
      </article>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn04-stage: #05070b;
  --color-tmn04-stage: oklch(0.12 0.01 260);
  --color-tmn04-bg: #0d1117;
  --color-tmn04-bg: oklch(0.18 0.015 260);
  --color-tmn04-surface: #161b22;
  --color-tmn04-surface: oklch(0.22 0.015 260);
  --color-tmn04-line: #30363d;
  --color-tmn04-line: oklch(0.34 0.012 260);
  --color-tmn04-ink: #e6edf3;
  --color-tmn04-ink: oklch(0.94 0.01 250);
  --color-tmn04-mut: #9198a1;
  --color-tmn04-mut: oklch(0.68 0.012 255);
  --color-tmn04-acc: #58a6ff;
  --color-tmn04-acc: oklch(0.72 0.15 255);
  --font-tmn04-sans: 'Geist', system-ui, sans-serif;
  --font-tmn04-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-04 svg {
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

.tmn-04 {
  width: 100%;
  min-height: 100svh;
}
```
