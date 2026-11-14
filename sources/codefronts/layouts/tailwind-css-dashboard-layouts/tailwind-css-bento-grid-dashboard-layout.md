---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-bento-grid-dashboard-layout/"
title: "Tailwind CSS Bento Grid Dashboard Layout"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "A dark, Vercel-generation bento that now fills the viewport and packs perfectly: hero MRR tile at 2×2, a full-height activity rail, a 30-day uptime strip and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Bento Grid Dashboard Layout
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-bento-grid-dashboard-layout/

A dark, Vercel-generation bento that now fills the viewport and packs perfectly: hero MRR tile at 2×2, a full-height activity rail, a 30-day uptime strip and a 12-week traffic chart, laid out with col-span-2 row-span-2 on a grid-cols-4 auto-rows-[minmax(8rem,1fr)] board. Hover a tile and one arbitrary :has() variant on the board dims its neighbours; the board re-packs to two columns with @max-[44rem]/page:.
## HTML
```html
<section class="tdl-01 @container/page w-full min-h-svh bg-tdl01-bg font-tdl01-sans text-tdl01-ink antialiased" aria-label="Bento grid dashboard demo">
  <div class="flex h-svh min-h-[38rem] flex-col gap-4 bg-[radial-gradient(120%_90%_at_85%_-10%,var(--color-tdl01-glow),transparent_60%),radial-gradient(90%_80%_at_-10%_110%,var(--color-tdl01-glow2),transparent_55%)] p-4 sm:p-6">
    <header class="flex flex-none items-center gap-3 text-sm">
      <span aria-hidden="true" class="size-6 rounded-lg bg-[conic-gradient(from_220deg,var(--color-tdl01-acc),var(--color-tdl01-acc2),var(--color-tdl01-acc))] shadow-[0_0_24px_-4px_var(--color-tdl01-acc)]"></span>
      <strong class="font-semibold tracking-tight">Pulse</strong>
      <span class="text-tdl01-mut">/ Overview</span>
      <span class="ml-auto flex items-center gap-2 rounded-full border border-tdl01-good/35 bg-tdl01-good/12 px-3 py-1.5 text-[11px] font-semibold tracking-[0.1em] text-tdl01-good uppercase"><i aria-hidden="true" class="size-1.75 rounded-full bg-tdl01-good animate-tdl01-pulse"></i>Live</span>
    </header>
    <div class="grid min-h-0 flex-1 auto-rows-[minmax(8rem,1fr)] grid-cols-4 gap-3.5 overflow-y-auto overscroll-contain @max-[44rem]/page:grid-cols-2 [&:has(>article:hover)>article:not(:hover)]:opacity-55 [&:has(>article:hover)>article:not(:hover)]:scale-[.985] [&:has(>article:hover)>article:not(:hover)]:saturate-75">
      <article class="relative col-span-2 row-span-2 flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% p-5 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:0ms">
        <h3 class="text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Monthly recurring revenue</h3>
        <p class="flex flex-wrap items-baseline gap-3 text-[clamp(32px,5cqi,52px)] font-bold tracking-[-0.03em] tabular-nums">$482,910<span class="rounded-full bg-tdl01-good/14 px-2.5 py-1 text-[13px] font-semibold tracking-normal text-tdl01-good">▲ 12.4%</span></p>
        <p class="text-[13px] text-tdl01-mut">vs. $429,644 last month</p>
        <svg class="mt-auto h-[45%] min-h-20 w-full" viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true">
          <defs><linearGradient id="tdl01g-area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--color-tdl01-acc)" stop-opacity=".5"/><stop offset="1" stop-color="var(--color-tdl01-acc)" stop-opacity="0"/></linearGradient></defs>
          <path d="M0 94 L36 80 L72 86 L112 62 L152 70 L192 48 L232 56 L272 36 L312 43 L352 19 L400 26 L400 120 L0 120Z" fill="url(#tdl01g-area)"/>
          <path d="M0 94 L36 80 L72 86 L112 62 L152 70 L192 48 L232 56 L272 36 L312 43 L352 19 L400 26" fill="none" stroke="var(--color-tdl01-acc)" stroke-width="2.5" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
        </svg>
      </article>
      <article class="flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:55ms">
        <h3 class="text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Active users</h3>
        <p class="text-[26px] font-bold tracking-tight tabular-nums">18,442</p>
        <div aria-hidden="true" class="mt-auto flex h-11 items-end gap-1.25 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-tdl01-acc/55 *:animate-tdl01-rise [&>i:last-child]:bg-tdl01-acc"><i style="--h:42%"></i><i style="--h:58%"></i><i style="--h:50%"></i><i style="--h:72%"></i><i style="--h:64%"></i><i style="--h:88%"></i><i style="--h:100%"></i></div>
      </article>
      <article class="row-span-2 flex flex-col gap-3 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:110ms">
        <h3 class="text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Activity</h3>
        <ul class="flex min-h-0 flex-1 flex-col gap-3.5 overflow-hidden mask-b-from-70%">
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-good"></i><div><b class="block text-[13px] font-semibold">Deploy shipped</b><span class="text-xs text-tdl01-mut">prod · 2m ago</span></div></li>
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-acc"></i><div><b class="block text-[13px] font-semibold">Invoice #2291 paid</b><span class="text-xs text-tdl01-mut">$1,900 · 14m ago</span></div></li>
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-acc2"></i><div><b class="block text-[13px] font-semibold">New teammate joined</b><span class="text-xs text-tdl01-mut">ana@ · 1h ago</span></div></li>
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-good"></i><div><b class="block text-[13px] font-semibold">Alert resolved</b><span class="text-xs text-tdl01-mut">api-eu · 3h ago</span></div></li>
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-acc"></i><div><b class="block text-[13px] font-semibold">Backup completed</b><span class="text-xs text-tdl01-mut">db-01 · 5h ago</span></div></li>
          <li class="flex items-start gap-2.5"><i aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tdl01-acc2"></i><div><b class="block text-[13px] font-semibold">SSL renewed</b><span class="text-xs text-tdl01-mut">pulse.app · 9h ago</span></div></li>
        </ul>
      </article>
      <article class="flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:165ms">
        <h3 class="flex justify-between text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Uptime · 30d<span class="font-tdl01-mono tracking-normal text-tdl01-good normal-case">99.98%</span></h3>
        <div role="img" aria-label="30-day uptime: 29 healthy days, 1 degraded day" class="mt-auto flex h-9 gap-0.75 *:flex-1 *:rounded-[2px] *:bg-tdl01-good/80"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i class="bg-tdl01-warn!"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <p class="flex justify-between font-tdl01-mono text-[10.5px] text-tdl01-mut"><span>30d ago</span><span>today</span></p>
      </article>
      <article class="col-span-2 flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:220ms">
        <h3 class="flex justify-between text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Traffic · last 12 weeks<span class="tracking-normal text-tdl01-ink normal-case">1.2M visits</span></h3>
        <div aria-hidden="true" class="mt-auto flex h-[60%] min-h-12 items-end gap-1.75 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[4px] *:bg-linear-to-t *:from-tdl01-acc2/30 *:to-tdl01-acc2 *:animate-tdl01-rise"><i style="--h:34%"></i><i style="--h:48%"></i><i style="--h:41%"></i><i style="--h:56%"></i><i style="--h:52%"></i><i style="--h:63%"></i><i style="--h:58%"></i><i style="--h:74%"></i><i style="--h:69%"></i><i style="--h:82%"></i><i style="--h:78%"></i><i style="--h:96%"></i></div>
      </article>
      <article class="flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:275ms">
        <h3 class="text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">Top region</h3>
        <p class="flex items-center gap-2 text-[26px] font-bold tracking-tight tabular-nums"><span class="rounded-md border border-tdl01-edge bg-tdl01-bg px-1.5 py-0.5 font-tdl01-mono text-xs font-semibold text-tdl01-mut">US</span>41%</p>
        <div aria-hidden="true" class="mt-auto h-1.5 overflow-hidden rounded-full bg-tdl01-track"><i class="block h-full w-[41%] rounded-full bg-linear-to-r from-tdl01-acc to-tdl01-acc2"></i></div>
        <p class="text-xs text-tdl01-mut">UK 22% · CA 12% · AU 9%</p>
      </article>
      <article class="flex flex-col gap-2 overflow-hidden rounded-2xl border border-tdl01-edge bg-linear-160 from-tdl01-card2 to-tdl01-card to-55% px-4.5 py-4 transition-[opacity,scale,filter,border-color] duration-300 animate-tdl01-in hover:border-tdl01-acc/60" style="animation-delay:330ms">
        <h3 class="text-[11px] font-semibold tracking-[0.12em] text-tdl01-mut uppercase">P95 latency</h3>
        <p class="text-[26px] font-bold tracking-tight tabular-nums">184<small class="text-sm font-semibold text-tdl01-mut"> ms</small></p>
        <p class="mt-auto text-[12.5px] font-semibold text-tdl01-acc2 tabular-nums">▼ 23 ms this week</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl01-bg: #110f1f;
  --color-tdl01-bg: oklch(0.16 0.028 288);
  --color-tdl01-card: #1b1930;
  --color-tdl01-card: oklch(0.215 0.03 288);
  --color-tdl01-card2: #24223a;
  --color-tdl01-card2: oklch(0.255 0.03 288);
  --color-tdl01-edge: #34314d;
  --color-tdl01-edge: oklch(0.32 0.035 288);
  --color-tdl01-track: #2e2b45;
  --color-tdl01-track: oklch(0.3 0.03 288);
  --color-tdl01-ink: #f1effa;
  --color-tdl01-ink: oklch(0.955 0.01 288);
  --color-tdl01-mut: #aca7c4;
  --color-tdl01-mut: oklch(0.74 0.03 288);
  --color-tdl01-acc: #ad82ff;
  --color-tdl01-acc: oklch(0.72 0.17 295);
  --color-tdl01-acc2: #4fd2e0;
  --color-tdl01-acc2: oklch(0.79 0.12 205);
  --color-tdl01-good: #4fd88e;
  --color-tdl01-good: oklch(0.79 0.16 155);
  --color-tdl01-warn: #f2b23d;
  --color-tdl01-warn: oklch(0.8 0.15 75);
  --color-tdl01-glow: #3a2763;
  --color-tdl01-glow: oklch(0.3 0.09 295 / 0.6);
  --color-tdl01-glow2: #12333d;
  --color-tdl01-glow2: oklch(0.26 0.06 210 / 0.5);
  --font-tdl01-sans: 'Geist', system-ui, sans-serif;
  --font-tdl01-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tdl01-in: tdl01-in 0.6s cubic-bezier(0.2,0.7,0.2,1) backwards;
  --animate-tdl01-rise: tdl01-rise 0.7s cubic-bezier(0.2,0.7,0.2,1) 0.3s backwards;
  --animate-tdl01-pulse: tdl01-pulse 2s infinite;

  @keyframes tdl01-in {
    from {
      opacity: 0;
      translate: 0 14px;
    }
  }

  @keyframes tdl01-rise {
    from {
      scale: 1 0;
    }
  }

  @keyframes tdl01-pulse {
    0%,
        100% {
      box-shadow: 0 0 0 0 var(--color-tdl01-good);
    }

    70% {
      box-shadow: 0 0 0 7px transparent;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS too so the stage is sized before the browser build compiles. */

.tdl-01 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-01 * {
    animation: none !important;
    transition-duration: 0.01s !important;
  }
}
```
