---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-radial-fab-menu-circular-navigation/"
title: "Tailwind Radial Menu — Circular FAB Fan-Out Navigation"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A floating action button whose plus spins into an X while five labelled actions spring out along a 140px arc, each 50ms behind the last."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radial Menu — Circular FAB Fan-Out Navigation
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-radial-fab-menu-circular-navigation/

A floating action button whose plus spins into an X while five labelled actions spring out along a 140px arc, each 50ms behind the last. The port fixes the original's dead overlay &mdash; it was a plain <div>, so tapping outside never closed the menu &mdash; by making it a <label>. Zero JavaScript.
## HTML
```html
<section class="tmn-05 w-full min-h-svh grid place-items-center bg-tmn05-stage bg-[radial-gradient(70%_50%_at_50%_100%,var(--color-tmn05-glow),transparent)] px-4 py-6 font-tmn05-sans antialiased" aria-label="Tailwind radial FAB menu demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn05-bg text-tmn05-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/8">
    <input type="checkbox" id="tmn-05-toggle" class="peer sr-only" aria-label="Toggle quick actions">
    <main class="absolute inset-0 overflow-y-auto px-5 pt-6 pb-28">
      <p class="mb-8 text-[22px] font-extrabold tracking-[-0.03em]">Spark<span class="text-tmn05-acc">AI</span></p>
      <h1 class="mb-2 text-[28px] leading-[1.15] font-bold tracking-[-0.03em] text-balance">Your creative workspace</h1>
      <p class="mb-6 text-sm leading-relaxed text-tmn05-mut">Generate, edit and share visuals with AI-powered tools.</p>
      <dl class="mb-6 grid grid-cols-3 gap-2.5">
        <div class="rounded-2xl border border-white/6 bg-tmn05-surface p-3.5"><dt class="text-[11px] text-tmn05-mut">Creations</dt><dd class="text-xl font-bold">248</dd></div>
        <div class="rounded-2xl border border-white/6 bg-tmn05-surface p-3.5"><dt class="text-[11px] text-tmn05-mut">Views</dt><dd class="text-xl font-bold">12k</dd></div>
        <div class="rounded-2xl border border-white/6 bg-tmn05-surface p-3.5"><dt class="text-[11px] text-tmn05-mut">Likes</dt><dd class="text-xl font-bold">94</dd></div>
      </dl>
      <p class="mb-3 text-[13px] font-semibold text-tmn05-mut">Recent</p>
      <div class="grid grid-cols-2 gap-2.5">
        <div class="aspect-square rounded-2xl bg-[conic-gradient(from_200deg_at_30%_70%,#6366f1,#ec4899,#f59e0b,#6366f1)]"></div>
        <div class="aspect-square rounded-2xl bg-[radial-gradient(circle_at_70%_30%,#14b8a6,#0f172a_70%)]"></div>
      </div>
    </main>

    <label for="tmn-05-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 bg-tmn05-bg/70 opacity-0 backdrop-blur-[2px] transition-opacity duration-300 group-has-checked:pointer-events-auto group-has-checked:opacity-100"></label>

    <nav aria-label="Quick actions">
      <a href="#" class="invisible absolute right-[53px] bottom-[171px] z-20 flex translate-y-5 scale-70 flex-row-reverse items-center gap-2 opacity-0 transition duration-400 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[30ms] focus-visible:outline-none"><span class="grid size-12 place-items-center rounded-full bg-teal-500 text-white shadow-lg shadow-black/40 ring-tmn05-ink focus-visible:ring-2"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/></svg></span><span class="rounded-full bg-black/70 px-2.5 py-1 text-[11px] font-semibold whitespace-nowrap">Gallery</span></a>
      <a href="#" class="invisible absolute right-[103px] bottom-[152px] z-20 flex translate-y-5 scale-70 flex-row-reverse items-center gap-2 opacity-0 transition duration-400 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[80ms]"><span class="grid size-12 place-items-center rounded-full bg-amber-500 text-white shadow-lg shadow-black/40"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 1 1 3 3L7 19l-4 1 1-4z"/></svg></span><span class="rounded-full bg-black/70 px-2.5 py-1 text-[11px] font-semibold whitespace-nowrap">Edit</span></a>
      <a href="#" class="invisible absolute right-[136px] bottom-[123px] z-20 flex translate-y-5 scale-70 flex-row-reverse items-center gap-2 opacity-0 transition duration-400 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[130ms]"><span class="grid size-12 place-items-center rounded-full bg-green-500 text-white shadow-lg shadow-black/40"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8M16 6l-4-4-4 4M12 2v13"/></svg></span><span class="rounded-full bg-black/70 px-2.5 py-1 text-[11px] font-semibold whitespace-nowrap">Share</span></a>
      <a href="#" class="invisible absolute right-[159px] bottom-[86px] z-20 flex translate-y-5 scale-70 flex-row-reverse items-center gap-2 opacity-0 transition duration-400 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[180ms]"><span class="grid size-12 place-items-center rounded-full bg-tmn05-acc2 text-white shadow-lg shadow-black/40"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/></svg></span><span class="rounded-full bg-black/70 px-2.5 py-1 text-[11px] font-semibold whitespace-nowrap">Favorites</span></a>
      <a href="#" class="invisible absolute right-[168px] bottom-[45px] z-20 flex translate-y-5 scale-70 flex-row-reverse items-center gap-2 opacity-0 transition duration-400 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:visible group-has-checked:translate-y-0 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:delay-[230ms]"><span class="grid size-12 place-items-center rounded-full bg-sky-500 text-white shadow-lg shadow-black/40"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg></span><span class="rounded-full bg-black/70 px-2.5 py-1 text-[11px] font-semibold whitespace-nowrap">Settings</span></a>
    </nav>

    <label for="tmn-05-toggle" class="absolute right-6 bottom-7 z-30 grid size-[58px] cursor-pointer place-items-center rounded-full bg-tmn05-acc text-white shadow-[0_10px_30px_-6px_var(--color-tmn05-acc)] transition duration-300 hover:scale-105 active:scale-95 group-has-checked:bg-tmn05-acc2 group-has-checked:shadow-[0_10px_30px_-6px_var(--color-tmn05-acc2)] peer-focus-visible:ring-2 peer-focus-visible:ring-white peer-focus-visible:ring-offset-2 peer-focus-visible:ring-offset-tmn05-bg">
      <svg viewBox="0 0 24 24" class="size-6 stroke-[2.2] transition-transform duration-300 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-checked:rotate-45" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn05-stage: #060a16;
  --color-tmn05-stage: oklch(0.15 0.025 265);
  --color-tmn05-glow: #2b2a6b80;
  --color-tmn05-glow: oklch(0.32 0.11 278 / 0.5);
  --color-tmn05-bg: #0f172a;
  --color-tmn05-bg: oklch(0.21 0.04 265);
  --color-tmn05-surface: #1e293b;
  --color-tmn05-surface: oklch(0.28 0.04 260);
  --color-tmn05-ink: #f1f5f9;
  --color-tmn05-ink: oklch(0.97 0.007 248);
  --color-tmn05-mut: #94a3b8;
  --color-tmn05-mut: oklch(0.71 0.035 257);
  --color-tmn05-acc: #6366f1;
  --color-tmn05-acc: oklch(0.59 0.2 277);
  --color-tmn05-acc2: #ec4899;
  --color-tmn05-acc2: oklch(0.66 0.21 354);
  --font-tmn05-sans: 'Sora', system-ui, sans-serif;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-05 svg {
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

.tmn-05 {
  width: 100%;
  min-height: 100svh;
}
```
