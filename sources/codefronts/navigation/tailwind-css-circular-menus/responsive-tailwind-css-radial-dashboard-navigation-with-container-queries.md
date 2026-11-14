---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/responsive-tailwind-css-radial-dashboard-navigation-with-container-queries/"
title: "Responsive Tailwind CSS Radial Dashboard Navigation with Container Queries"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A hub-and-spoke ops dashboard: six module tiles orbit a live KPI core with a conic progress ring, faint spokes light up toward the selected tile, and the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind CSS Radial Dashboard Navigation with Container Queries
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/responsive-tailwind-css-radial-dashboard-navigation-with-container-queries/

A hub-and-spoke ops dashboard: six module tiles orbit a live KPI core with a conic progress ring, faint spokes light up toward the selected tile, and the whole constellation scales with its card because every radius is a container unit &mdash; [--r:34cqi] under @container. Zero media queries; the tiles are a native radio group, so arrow keys cycle modules.
## HTML
```html
<section class="tcm-06 w-full min-h-svh grid place-items-center bg-tcm06-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm06-glow),transparent_72%)] px-4 py-14 font-tcm06-sans text-tcm06-ink antialiased sm:px-5" aria-label="Responsive radial dashboard navigation demo">
  <div class="grid w-full justify-items-center gap-6">
    <header class="flex w-full max-w-[30rem] items-center justify-between gap-4">
      <div>
        <p class="font-tcm06-mono text-[11px] tracking-[0.14em] text-tcm06-acc-ink uppercase">Ops · Overview</p>
        <h2 class="text-xl font-semibold tracking-[-0.02em]">Northwind Console</h2>
      </div>
      <p class="inline-flex items-center gap-2 rounded-full bg-tcm06-ok/10 px-2.5 py-1 font-tcm06-mono text-[11px] text-tcm06-ok ring-1 ring-tcm06-ok/25"><span aria-hidden="true" class="size-1.5 animate-pulse rounded-full bg-tcm06-ok motion-reduce:animate-none"></span>Live</p>
    </header>
    <fieldset id="tcm-06-hub" class="group/hub @container w-full max-w-[30rem]">
      <legend class="sr-only">Dashboard module</legend>
      <div class="relative aspect-square [--n:6] [--r:34cqi]">
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m0:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m0:checked]/hub:h-0.5"></span>
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m1:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m1:checked]/hub:h-0.5"></span>
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m2:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m2:checked]/hub:h-0.5"></span>
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m3:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m3:checked]/hub:h-0.5"></span>
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m4:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m4:checked]/hub:h-0.5"></span>
        <span aria-hidden="true" class="absolute top-1/2 left-1/2 h-px w-(--r) origin-left rotate-(--a) bg-linear-to-r from-transparent from-35% to-tcm06-line transition-colors duration-300 [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)] group-has-[#tcm-06-m5:checked]/hub:to-tcm06-acc group-has-[#tcm-06-m5:checked]/hub:h-0.5"></span>
        <div data-core class="absolute top-1/2 left-1/2 size-[40cqi] -translate-1/2 rounded-full bg-[conic-gradient(var(--color-tcm06-acc)_calc(var(--p)*1%),var(--color-tcm06-track)_0)] p-[1.6cqi] shadow-tcm06-core [--p:72]">
          <div class="grid size-full place-content-center justify-items-center gap-[0.6cqi] rounded-full bg-tcm06-core text-center">
            <span data-label class="font-tcm06-mono text-[clamp(9px,2.4cqi,11px)] tracking-[0.16em] text-tcm06-mut uppercase">Revenue</span>
            <strong data-stat class="text-[clamp(20px,7.2cqi,34px)] leading-none font-bold tracking-[-0.03em] tabular-nums">$84.2k</strong>
            <span class="text-[clamp(9px,2.4cqi,11.5px)] text-tcm06-mut"><b data-delta class="font-semibold text-tcm06-acc-ink">+12.4%</b> <span data-sub>this month</span></span>
          </div>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m0" value="Revenue" data-stat="$84.2k" data-delta="+12.4%" data-sub="this month" data-pct="72" class="peer sr-only" checked>
          <label for="tcm-06-m0" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 19 9 13l4 4 7-8M4 5v14h16"/></svg>Revenue</label>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m1" value="Users" data-stat="12,408" data-delta="+318" data-sub="new this week" data-pct="58" class="peer sr-only">
          <label for="tcm-06-m1" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M9 4.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zM3 20c0-3.5 2.7-5.5 6-5.5s6 2 6 5.5M16 4.6a3.5 3.5 0 0 1 0 6.8M17.5 14.7c2.1.7 3.5 2.4 3.5 5.3"/></svg>Users</label>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m2" value="Uptime" data-stat="99.98%" data-delta="30 days" data-sub="all regions" data-pct="99" class="peer sr-only">
          <label for="tcm-06-m2" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 4h16v7H4zM4 13h16v7H4zM8 7.5h.01M8 16.5h.01"/></svg>Uptime</label>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m3" value="Orders" data-stat="1,294" data-delta="-3.1%" data-sub="in queue" data-pct="41" class="peer sr-only">
          <label for="tcm-06-m3" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 7l8-4 8 4v10l-8 4-8-4zM4 7l8 4m0 0 8-4m-8 4v10"/></svg>Orders</label>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m4" value="Reviews" data-stat="4.8 / 5" data-delta="+0.2" data-sub="average score" data-pct="96" class="peer sr-only">
          <label for="tcm-06-m4" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/></svg>Reviews</label>
        </div>
        <div class="tcm06-polar absolute top-1/2 left-1/2 -mt-[8.5cqi] -ml-[10cqi] [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <input type="radio" name="tcm-06-mod" id="tcm-06-m5" value="Support" data-stat="37" data-delta="-11" data-sub="open tickets" data-pct="24" class="peer sr-only">
          <label for="tcm-06-m5" class="grid h-[17cqi] w-[20cqi] min-w-[4.25rem] cursor-pointer content-center justify-items-center gap-1 rounded-2xl bg-tcm06-tile text-[clamp(10px,2.6cqi,12.5px)] font-semibold text-tcm06-ink shadow-tcm06-tile ring-1 ring-tcm06-line backdrop-blur-md transition-[translate,background-color,box-shadow,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:ring-tcm06-acc/50 peer-checked:bg-linear-to-br peer-checked:from-tcm06-acc peer-checked:to-tcm06-acc2 peer-checked:text-tcm06-on peer-checked:shadow-tcm06-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm06-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-[clamp(16px,5cqi,22px)]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zM5.7 5.7l3.8 3.8M14.5 14.5l3.8 3.8M18.3 5.7l-3.8 3.8M9.5 14.5l-3.8 3.8"/></svg>Support</label>
        </div>
      </div>
    </fieldset>
    <p class="text-[13px] text-tcm06-mut" aria-live="polite" data-live>Revenue: $84.2k, +12.4% this month</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm06-card px-3.5 py-2 text-center font-tcm06-mono text-[11.5px] text-tcm06-mut ring-1 ring-tcm06-line ">@container · [--r:34cqi] · peer-checked: · conic ring var(--p)</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm06-bg: #eef6f7;
  --color-tcm06-bg: oklch(0.967 0.009 205.9);
  --color-tcm06-glow: #99f6e480;
  --color-tcm06-glow: oklch(0.91 0.093 180.4 / 0.5);
  --color-tcm06-core: #fbfeff;
  --color-tcm06-core: oklch(0.995 0.003 219.5);
  --color-tcm06-tile: #ffffffd9;
  --color-tcm06-tile: oklch(1 0 0 / 0.85);
  --color-tcm06-track: #d6e6e8;
  --color-tcm06-track: oklch(0.914 0.017 205.8);
  --color-tcm06-ink: #0c2328;
  --color-tcm06-ink: oklch(0.24 0.03 213.8);
  --color-tcm06-mut: #4a6469;
  --color-tcm06-mut: oklch(0.484 0.032 210.7);
  --color-tcm06-line: #c7dfe2;
  --color-tcm06-line: oklch(0.887 0.026 205.8);
  --color-tcm06-acc: #0891b2;
  --color-tcm06-acc: oklch(0.609 0.111 221.7);
  --color-tcm06-acc2: #0d9488;
  --color-tcm06-acc2: oklch(0.6 0.104 184.7);
  --color-tcm06-acc-ink: #0e7490;
  --color-tcm06-acc-ink: oklch(0.52 0.094 223.1);
  --color-tcm06-on: #ffffff;
  --color-tcm06-on: oklch(1 0 0);
  --color-tcm06-ok: #047857;
  --color-tcm06-ok: oklch(0.508 0.105 165.6);
  --color-tcm06-ring: #0e7490;
  --color-tcm06-ring: oklch(0.52 0.094 223.1);
  --color-tcm06-card: #ffffff;
  --color-tcm06-card: oklch(1 0 0);
  --font-tcm06-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tcm06-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tcm06-tile: 0 8px 20px -12px oklch(0.35 0.08 210 / 0.45);
  --shadow-tcm06-glow: 0 12px 28px -10px oklch(0.6 0.13 210 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tcm06-core: 0 30px 60px -24px oklch(0.4 0.1 210 / 0.5), 0 0 0 8px oklch(0.7 0.1 200 / 0.08);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-06 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm06-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: ops night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-06:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm06-bg: #081418;
    --color-tcm06-bg: oklch(0.182 0.019 221.1);
    --color-tcm06-glow: #155e7566;
    --color-tcm06-glow: oklch(0.45 0.077 224.3 / 0.4);
    --color-tcm06-core: #0d1f24;
    --color-tcm06-core: oklch(0.226 0.026 217.8);
    --color-tcm06-tile: #13292fe6;
    --color-tcm06-tile: oklch(0.266 0.03 217.5 / 0.9);
    --color-tcm06-track: #1d3a41;
    --color-tcm06-track: oklch(0.329 0.037 215.2);
    --color-tcm06-ink: #e4f6f8;
    --color-tcm06-ink: oklch(0.96 0.019 204.8);
    --color-tcm06-mut: #93b7bd;
    --color-tcm06-mut: oklch(0.755 0.04 208.8);
    --color-tcm06-line: #21434b;
    --color-tcm06-line: oklch(0.361 0.042 214.8);
    --color-tcm06-acc: #22d3ee;
    --color-tcm06-acc: oklch(0.797 0.134 211.5);
    --color-tcm06-acc2: #2dd4bf;
    --color-tcm06-acc2: oklch(0.785 0.133 181.9);
    --color-tcm06-acc-ink: #67e8f9;
    --color-tcm06-acc-ink: oklch(0.865 0.115 207.1);
    --color-tcm06-on: #062a30;
    --color-tcm06-on: oklch(0.263 0.041 211);
    --color-tcm06-ok: #34d399;
    --color-tcm06-ok: oklch(0.773 0.153 163.2);
    --color-tcm06-ring: #67e8f9;
    --color-tcm06-ring: oklch(0.865 0.115 207.1);
    --color-tcm06-card: #0d1f24;
    --color-tcm06-card: oklch(0.226 0.026 217.8);
  }
}

.tcm-06[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm06-bg: #081418;
  --color-tcm06-bg: oklch(0.182 0.019 221.1);
  --color-tcm06-glow: #155e7566;
  --color-tcm06-glow: oklch(0.45 0.077 224.3 / 0.4);
  --color-tcm06-core: #0d1f24;
  --color-tcm06-core: oklch(0.226 0.026 217.8);
  --color-tcm06-tile: #13292fe6;
  --color-tcm06-tile: oklch(0.266 0.03 217.5 / 0.9);
  --color-tcm06-track: #1d3a41;
  --color-tcm06-track: oklch(0.329 0.037 215.2);
  --color-tcm06-ink: #e4f6f8;
  --color-tcm06-ink: oklch(0.96 0.019 204.8);
  --color-tcm06-mut: #93b7bd;
  --color-tcm06-mut: oklch(0.755 0.04 208.8);
  --color-tcm06-line: #21434b;
  --color-tcm06-line: oklch(0.361 0.042 214.8);
  --color-tcm06-acc: #22d3ee;
  --color-tcm06-acc: oklch(0.797 0.134 211.5);
  --color-tcm06-acc2: #2dd4bf;
  --color-tcm06-acc2: oklch(0.785 0.133 181.9);
  --color-tcm06-acc-ink: #67e8f9;
  --color-tcm06-acc-ink: oklch(0.865 0.115 207.1);
  --color-tcm06-on: #062a30;
  --color-tcm06-on: oklch(0.263 0.041 211);
  --color-tcm06-ok: #34d399;
  --color-tcm06-ok: oklch(0.773 0.153 163.2);
  --color-tcm06-ring: #67e8f9;
  --color-tcm06-ring: oklch(0.865 0.115 207.1);
  --color-tcm06-card: #0d1f24;
  --color-tcm06-card: oklch(0.226 0.026 217.8);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-06-hub');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const core = root.querySelector('[data-core]');
  const f = (s) => root.querySelector(s);
  const live = document.querySelector('.tcm-06 [data-live]');
  root.addEventListener('change', (e) => {
    const r = e.target;
    if (r.name !== 'tcm-06-mod') return;
    const swap = () => {
      f('[data-label]').textContent = r.value;
      f('[data-stat]').textContent = r.dataset.stat;
      f('[data-delta]').textContent = r.dataset.delta;
      f('[data-sub]').textContent = r.dataset.sub;
      core.style.setProperty('--p', r.dataset.pct);
      if (live) live.textContent = r.value + ': ' + r.dataset.stat + ', ' + r.dataset.delta + ' ' + r.dataset.sub;
    };
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { swap(); return; }
    core.animate([{ opacity: 1 }, { opacity: 0.25, scale: '0.97' }], { duration: 120, fill: 'forwards' }).finished.then(() => {
      swap();
      core.animate([{ opacity: 0.25, scale: '0.97' }, { opacity: 1, scale: '1' }], { duration: 260, easing: 'cubic-bezier(.16,1,.3,1)', fill: 'forwards' });
    });
  });
})();
```
