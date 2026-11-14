---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/glassmorphism-striped-table-tailwind-css/"
title: "Glassmorphism Striped Table in Tailwind CSS"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A campaign-analytics table frosted over drifting gradient orbs, with zebra stripes written as odd:bg-white/7 even:bg-white/2 so the blurred colour shows…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Striped Table in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-tables/glassmorphism-striped-table-tailwind-css/

A campaign-analytics table frosted over drifting gradient orbs, with zebra stripes written as odd:bg-white/7 even:bg-white/2 so the blurred colour shows through at two intensities. Progress bars now grow in on first paint with starting:w-0, and a supports-[backdrop-filter:blur(1px)]: fallback keeps it legible where blur is unavailable.
## HTML
```html
<section class="ttb-06 grid-cols-1 relative isolate w-full min-h-svh grid place-items-center overflow-hidden px-5 py-14 font-ttb06-sans text-white" aria-label="Glassmorphism striped table demo">
  <div aria-hidden="true" class="absolute inset-0 -z-20 animate-ttb06-shift bg-[linear-gradient(135deg,#1e1b4b_0%,#312e81_25%,#4c1d95_50%,#7e22ce_75%,#0f172a_100%)] bg-size-[400%_400%] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute -top-20 -left-16 -z-10 size-96 animate-ttb06-drift rounded-full bg-violet-500/40 blur-3xl motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute -right-10 -bottom-24 -z-10 size-80 animate-ttb06-drift rounded-full bg-cyan-400/30 blur-3xl [animation-delay:-4s] motion-reduce:animate-none"></div>
  <div class="w-full max-w-4xl">
    <header class="mb-6">
      <p class="text-[11px] font-semibold tracking-[0.3em] text-violet-200 uppercase">Q3 · Marketing</p>
      <h2 class="mt-1.5 text-2xl font-bold tracking-tight">Campaign performance</h2>
      <p class="mt-1 text-sm text-white/75">Five active campaigns across all channels</p>
    </header>
    <div class="relative overflow-x-auto rounded-[20px] border border-white/15 bg-ttb06-fallback shadow-[0_24px_64px_-16px_oklch(0_0_0/0.5),inset_0_1px_0_oklch(1_0_0/0.18)] supports-[backdrop-filter:blur(1px)]:bg-white/6 supports-[backdrop-filter:blur(1px)]:backdrop-blur-2xl">
      <table class="w-full min-w-[680px] border-collapse text-left text-sm">
        <caption class="sr-only">Campaign reach, conversion and budget progress</caption>
        <thead class="bg-white/8">
          <tr class="border-b border-white/12 [&_th]:px-5 [&_th]:py-3.5 [&_th]:text-[10.5px] [&_th]:font-semibold [&_th]:tracking-[0.18em] [&_th]:text-white/75 [&_th]:uppercase">
            <th scope="col">Campaign</th><th scope="col">Owner</th><th scope="col">Status</th><th scope="col" class="text-right">Reach</th><th scope="col" class="text-right">Conv.</th><th scope="col" class="text-right">Budget used</th>
          </tr>
        </thead>
        <tbody class="[&_td]:px-5 [&_td]:py-4 [&_td]:align-middle [&_tr]:border-b [&_tr]:border-white/6 [&_tr:last-child]:border-0">
          <tr class="transition-colors odd:bg-white/7 even:bg-white/2 hover:bg-violet-300/15">
            <th scope="row" class="px-5 py-4 font-semibold">Q3 Product Launch</th>
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-violet-500 to-cyan-500 text-[11px] font-bold ring-1 ring-white/25">AK</span><span class="text-white/80">Arya K.</span></div></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs font-semibold ring-1 ring-white/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-400 shadow-[0_0_8px_var(--color-emerald-400)]"></span>Live</span></td>
            <td class="text-right font-semibold tabular-nums">248K</td>
            <td class="text-right tabular-nums">4.2%</td>
            <td><div class="flex items-center justify-end gap-3"><div class="h-1.5 w-24 overflow-hidden rounded-full bg-white/12"><div style="--w:72%" class="h-full w-(--w) rounded-full bg-linear-to-r from-violet-300 to-cyan-400 transition-[width] duration-1000 ease-out starting:w-0 motion-reduce:transition-none"></div></div><span class="w-9 text-right text-xs font-bold tabular-nums">72%</span></div></td>
          </tr>
          <tr class="transition-colors odd:bg-white/7 even:bg-white/2 hover:bg-violet-300/15">
            <th scope="row" class="px-5 py-4 font-semibold">Black Friday Promo</th>
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-amber-400 to-red-500 text-[11px] font-bold ring-1 ring-white/25">MR</span><span class="text-white/80">Marcus R.</span></div></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs font-semibold ring-1 ring-white/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-amber-300"></span>Scheduled</span></td>
            <td class="text-right font-semibold tabular-nums">1.1M</td>
            <td class="text-right text-white/60 tabular-nums">—</td>
            <td><div class="flex items-center justify-end gap-3"><div class="h-1.5 w-24 overflow-hidden rounded-full bg-white/12"><div style="--w:18%" class="h-full w-(--w) rounded-full bg-linear-to-r from-violet-300 to-cyan-400 transition-[width] delay-75 duration-1000 ease-out starting:w-0 motion-reduce:transition-none"></div></div><span class="w-9 text-right text-xs font-bold tabular-nums">18%</span></div></td>
          </tr>
          <tr class="transition-colors odd:bg-white/7 even:bg-white/2 hover:bg-violet-300/15">
            <th scope="row" class="px-5 py-4 font-semibold">Creator Collab Series</th>
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-emerald-500 to-sky-500 text-[11px] font-bold ring-1 ring-white/25">SN</span><span class="text-white/80">Selin N.</span></div></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs font-semibold ring-1 ring-white/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-400 shadow-[0_0_8px_var(--color-emerald-400)]"></span>Live</span></td>
            <td class="text-right font-semibold tabular-nums">640K</td>
            <td class="text-right font-semibold text-emerald-300 tabular-nums">7.8%</td>
            <td><div class="flex items-center justify-end gap-3"><div class="h-1.5 w-24 overflow-hidden rounded-full bg-white/12"><div style="--w:91%" class="h-full w-(--w) rounded-full bg-linear-to-r from-emerald-300 to-cyan-300 transition-[width] delay-150 duration-1000 ease-out starting:w-0 motion-reduce:transition-none"></div></div><span class="w-9 text-right text-xs font-bold tabular-nums">91%</span></div></td>
          </tr>
          <tr class="transition-colors odd:bg-white/7 even:bg-white/2 hover:bg-violet-300/15">
            <th scope="row" class="px-5 py-4 font-semibold">Retargeting Wave</th>
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-pink-500 to-violet-500 text-[11px] font-bold ring-1 ring-white/25">TW</span><span class="text-white/80">Theo W.</span></div></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs font-semibold ring-1 ring-white/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-rose-400"></span>Paused</span></td>
            <td class="text-right font-semibold tabular-nums">82K</td>
            <td class="text-right tabular-nums">1.1%</td>
            <td><div class="flex items-center justify-end gap-3"><div class="h-1.5 w-24 overflow-hidden rounded-full bg-white/12"><div style="--w:35%" class="h-full w-(--w) rounded-full bg-linear-to-r from-rose-300 to-orange-300 transition-[width] delay-200 duration-1000 ease-out starting:w-0 motion-reduce:transition-none"></div></div><span class="w-9 text-right text-xs font-bold tabular-nums">35%</span></div></td>
          </tr>
          <tr class="transition-colors odd:bg-white/7 even:bg-white/2 hover:bg-violet-300/15">
            <th scope="row" class="px-5 py-4 font-semibold">Brand Awareness APAC</th>
            <td><div class="flex items-center gap-2.5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-135 from-sky-500 to-indigo-500 text-[11px] font-bold ring-1 ring-white/25">JP</span><span class="text-white/80">James P.</span></div></td>
            <td><span class="inline-flex items-center gap-1.5 rounded-full bg-white/10 px-2.5 py-1 text-xs font-semibold ring-1 ring-white/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-400 shadow-[0_0_8px_var(--color-emerald-400)]"></span>Live</span></td>
            <td class="text-right font-semibold tabular-nums">2.4M</td>
            <td class="text-right tabular-nums">2.9%</td>
            <td><div class="flex items-center justify-end gap-3"><div class="h-1.5 w-24 overflow-hidden rounded-full bg-white/12"><div style="--w:58%" class="h-full w-(--w) rounded-full bg-linear-to-r from-violet-300 to-cyan-400 transition-[width] delay-300 duration-1000 ease-out starting:w-0 motion-reduce:transition-none"></div></div><span class="w-9 text-right text-xs font-bold tabular-nums">58%</span></div></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb06-fallback: #2a2068;
  --color-ttb06-fallback: oklch(0.3 0.13 285 / 0.94);
  --font-ttb06-sans: 'Sora', system-ui, sans-serif;
  --animate-ttb06-shift: ttb06-shift 14s ease infinite;
  --animate-ttb06-drift: ttb06-drift 9s ease-in-out infinite;

  @keyframes ttb06-shift {
    0%,
        100% {
      background-position: 0% 50%;
    }

    50% {
      background-position: 100% 50%;
    }
  }

  @keyframes ttb06-drift {
    0%,
        100% {
      transform: translate(0, 0) scale(1);
    }

    50% {
      transform: translate(24px, 18px) scale(1.1);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-06 {
  width: 100%;
  min-height: 100svh;
}
```
