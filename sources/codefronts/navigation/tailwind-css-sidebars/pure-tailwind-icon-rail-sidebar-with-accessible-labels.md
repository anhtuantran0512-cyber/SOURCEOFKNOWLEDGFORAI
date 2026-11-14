---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-icon-rail-sidebar-with-accessible-labels/"
title: "Pure Tailwind Icon Rail Sidebar with Accessible Labels"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "An icon-only rail has one hard requirement and one nice-to-have, and most implementations get them backwards."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Icon Rail Sidebar with Accessible Labels
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-icon-rail-sidebar-with-accessible-labels/

An icon-only rail has one hard requirement and one nice-to-have, and most implementations get them backwards. The requirement is an accessible name on every link &mdash; here a visually hidden <span>, never title. The nice-to-have is the sighted user's tooltip, and in utilities it is group-hover: and group-focus-visible: on a second span. Zero script.
## HTML
```html
<section class="tsb-13 block relative w-full min-h-svh bg-tsb13-bg text-tsb13-ink font-tsb13-sans leading-[1.55]" aria-label="Aperture media library">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-13-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-13-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb13-line bg-tsb13-surf text-tsb13-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb13-acc peer-focus-visible:outline-offset-2" for="tsb-13-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="flex min-w-0 min-h-svh bg-tsb13-surf">
    <nav class="flex-none min-w-0 w-[var(--tsb13-w)] bg-tsb13-surf2 border-r border-tsb13-line" aria-label="Aperture library">
      <ul class="list-none m-0 p-1 grid gap-1">
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb13-accsoft aria-[current=page]:text-tsb13-acc aria-[current=page]:shadow-[inset_3px_0_0_var(--color-tsb13-acc)]" href="#tsb-13-main" aria-current="page">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="4" y="5" width="16" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4 15l4-4 4 4 3-3 5 5" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">All media</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">All media</span></a></li>
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2" href="#tsb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h6l2 2h8v9H4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Collections</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">Collections</span></a></li>
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2" href="#tsb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M15.5 15.5L20 20" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Saved searches</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">Saved searches</span></a></li>
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2" href="#tsb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4l7 4v8l-7 4-7-4V8Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Renditions</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">Renditions</span></a></li>
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2" href="#tsb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19V5h9l5 5v9Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 13h6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Licences</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">Licences</span></a></li>
        <li><a class="group relative grid place-items-center h-11 min-h-11 text-tsb13-mut no-underline [&>svg]:w-5.5 [&>svg]:h-5.5 hover:bg-tsb13-surf hover:text-tsb13-ink focus-visible:outline-2 focus-visible:outline-tsb13-acc focus-visible:-outline-offset-2" href="#tsb-13-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 4h12v16l-6-4-6 4Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Archive</span><span class="absolute left-[calc(100%+0.55rem)] top-1/2 -translate-y-1/2 z-8 px-2 py-1 whitespace-nowrap pointer-events-none invisible opacity-0 bg-tsb13-ink text-tsb13-bg font-tsb13-display text-[0.8rem] tracking-[0.04em] uppercase transition-[opacity,visibility] duration-[120ms] group-hover:visible group-hover:opacity-100 group-focus-visible:visible group-focus-visible:opacity-100 motion-reduce:transition-none" aria-hidden="true">Archive</span></a></li>
      </ul>
    </nav>

    <main class="flex-1 min-w-0 grid gap-4.5 content-start px-5 pt-5.5 pb-10 r46:px-8 r46:pt-9 r46:pb-12" id="tsb-13-main">
      <div class="min-w-0">
        <h2 class="m-0 mb-1 font-tsb13-display text-[clamp(1.5rem,3.6vw,2rem)] tracking-[0.02em] uppercase">All media</h2>
        <p class="m-0 text-[0.84rem] tabular-nums text-tsb13-mut">1,842 assets &middot; 41 GB &middot; last ingest 14:02</p>
      </div>
      <div class="grid grid-cols-[repeat(auto-fill,minmax(7rem,1fr))] gap-2 [&>span]:aspect-[4/3] [&>span]:bg-tsb13-surf2 [&>span]:border [&>span]:border-tsb13-line [&>span:nth-child(3n)]:bg-tsb13-accsoft" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb13-bg: #f4f4f5;
  --color-tsb13-bg: oklch(96% 0.002 285);
  --color-tsb13-surf: #ffffff;
  --color-tsb13-surf: oklch(100% 0 0);
  --color-tsb13-surf2: #e9e9ec;
  --color-tsb13-surf2: oklch(92.5% 0.004 285);
  --color-tsb13-line: #d3d3d8;
  --color-tsb13-line: oklch(86.5% 0.006 285);
  --color-tsb13-ink: #131316;
  --color-tsb13-ink: oklch(19% 0.004 285);
  --color-tsb13-mut: #5c5c66;
  --color-tsb13-mut: oklch(46% 0.012 285);
  --color-tsb13-acc: #0f5c8c;
  --color-tsb13-acc: oklch(45% 0.1 232);
  --color-tsb13-accsoft: #dceaf4;
  --color-tsb13-accsoft: oklch(92% 0.03 232);
  --font-tsb13-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb13-display: 'Roboto Condensed', 'Archivo Narrow', ui-sans-serif, system-ui, sans-serif;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract plus the rail width, which is geometry read by
   w-[var(--tsb13-w)] rather than a colour scale. */

.tsb-13 {
  width: 100%;
  min-height: 100svh;
  --tsb13-w: 4rem;
}

.tsb-13 *,
.tsb-13 *::before,
.tsb-13 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-13:has(.tsb-13-theme-input:checked) {
  --color-tsb13-bg: #0d0d0f;
  --color-tsb13-surf: #15151a;
  --color-tsb13-surf2: #1d1d23;
  --color-tsb13-line: #2a2a31;
  --color-tsb13-ink: #eeeef1;
  --color-tsb13-mut: #9a9aa4;
  --color-tsb13-acc: #6fbde8;
  --color-tsb13-acc: oklch(78% 0.1 232);
  --color-tsb13-accsoft: #16283a;
}

@media (prefers-color-scheme: dark) {
  .tsb-13 {
    --color-tsb13-bg: #0d0d0f;
    --color-tsb13-surf: #15151a;
    --color-tsb13-surf2: #1d1d23;
    --color-tsb13-line: #2a2a31;
    --color-tsb13-ink: #eeeef1;
    --color-tsb13-mut: #9a9aa4;
    --color-tsb13-acc: #6fbde8;
    --color-tsb13-acc: oklch(78% 0.1 232);
    --color-tsb13-accsoft: #16283a;
  }

  .tsb-13:has(.tsb-13-theme-input:checked) {
    --color-tsb13-bg: #f4f4f5;
    --color-tsb13-surf: #ffffff;
    --color-tsb13-surf2: #e9e9ec;
    --color-tsb13-line: #d3d3d8;
    --color-tsb13-ink: #131316;
    --color-tsb13-mut: #5c5c66;
    --color-tsb13-acc: #0f5c8c;
    --color-tsb13-acc: oklch(45% 0.1 232);
    --color-tsb13-accsoft: #dceaf4;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-13:has(.tsb-13-theme-input:checked) {
    --color-tsb13-bg: #0d0d0f;
    --color-tsb13-surf: #15151a;
    --color-tsb13-surf2: #1d1d23;
    --color-tsb13-line: #2a2a31;
    --color-tsb13-ink: #eeeef1;
    --color-tsb13-mut: #9a9aa4;
    --color-tsb13-acc: #6fbde8;
    --color-tsb13-acc: oklch(78% 0.1 232);
    --color-tsb13-accsoft: #16283a;
  }
}
```
