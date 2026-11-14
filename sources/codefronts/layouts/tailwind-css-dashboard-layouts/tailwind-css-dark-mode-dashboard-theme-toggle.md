---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-dark-mode-dashboard-theme-toggle/"
title: "Tailwind CSS Dark Mode Dashboard with Light / Dark / System Toggle"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Dark mode as a data change, not a redesign."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dark Mode Dashboard with Light / Dark / System Toggle
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-dark-mode-dashboard-theme-toggle/

Dark mode as a data change, not a redesign. Components use semantic utilities only (bg-tdl10-card, text-tdl10-ink); @theme inline maps those to runtime variables; and the app root flips the variables with has-[#tdl10-dark:checked]:[--tdl10-bg:…]. New in the port: a Light / Dark / System segmented switch, where System follows the OS through the built-in dark: variant.
## HTML
```html
<section class="tdl-10 w-full min-h-svh font-tdl10-sans antialiased" aria-label="Dark mode token dashboard demo">
  <div class="@container/body grid h-svh min-h-[36rem] grid-rows-[auto_minmax(0,1fr)_auto] gap-4 bg-tdl10-bg p-4 text-tdl10-ink transition-colors duration-300 scheme-light sm:p-6 [--tdl10-bg:oklch(0.975_0.005_260)] [--tdl10-card:oklch(1_0_0)] [--tdl10-ink:oklch(0.25_0.02_260)] [--tdl10-mut:oklch(0.48_0.02_260)] [--tdl10-edge:oklch(0.9_0.01_260)] [--tdl10-acc:oklch(0.53_0.19_268)] [--tdl10-good:oklch(0.52_0.13_155)] [--tdl10-shadow:oklch(0.4_0.05_260/0.35)] has-[#tdl10-dark:checked]:scheme-dark has-[#tdl10-dark:checked]:[--tdl10-bg:oklch(0.17_0.02_260)] has-[#tdl10-dark:checked]:[--tdl10-card:oklch(0.22_0.025_260)] has-[#tdl10-dark:checked]:[--tdl10-ink:oklch(0.94_0.01_260)] has-[#tdl10-dark:checked]:[--tdl10-mut:oklch(0.72_0.02_260)] has-[#tdl10-dark:checked]:[--tdl10-edge:oklch(0.32_0.02_260)] has-[#tdl10-dark:checked]:[--tdl10-acc:oklch(0.74_0.15_268)] has-[#tdl10-dark:checked]:[--tdl10-good:oklch(0.78_0.15_155)] has-[#tdl10-dark:checked]:[--tdl10-shadow:oklch(0_0_0/0.7)] dark:has-[#tdl10-sys:checked]:scheme-dark dark:has-[#tdl10-sys:checked]:[--tdl10-bg:oklch(0.17_0.02_260)] dark:has-[#tdl10-sys:checked]:[--tdl10-card:oklch(0.22_0.025_260)] dark:has-[#tdl10-sys:checked]:[--tdl10-ink:oklch(0.94_0.01_260)] dark:has-[#tdl10-sys:checked]:[--tdl10-mut:oklch(0.72_0.02_260)] dark:has-[#tdl10-sys:checked]:[--tdl10-edge:oklch(0.32_0.02_260)] dark:has-[#tdl10-sys:checked]:[--tdl10-acc:oklch(0.74_0.15_268)] dark:has-[#tdl10-sys:checked]:[--tdl10-good:oklch(0.78_0.15_155)] dark:has-[#tdl10-sys:checked]:[--tdl10-shadow:oklch(0_0_0/0.7)]">
    <header class="flex flex-wrap items-center justify-between gap-3">
      <strong class="flex items-center gap-2.5 text-base font-bold tracking-tight"><span aria-hidden="true" class="size-6 rounded-lg bg-[conic-gradient(from_200deg,var(--tdl10-acc),oklch(0.7_0.13_320),var(--tdl10-acc))]"></span>Nightshift</strong>
      <fieldset class="flex gap-1 rounded-xl border border-tdl10-edge bg-tdl10-card p-1 transition-colors duration-300 [&>label]:flex [&>label]:h-9 [&>label]:cursor-pointer [&>label]:items-center [&>label]:gap-1.5 [&>label]:rounded-lg [&>label]:px-3 [&>label]:text-xs [&>label]:font-semibold [&>label]:text-tdl10-mut [&>label]:transition [&>label:hover]:text-tdl10-ink [&>label:has(:checked)]:bg-tdl10-acc/14 [&>label:has(:checked)]:text-tdl10-acc [&>label:has(:focus-visible)]:outline-2 [&>label:has(:focus-visible)]:outline-offset-1 [&>label:has(:focus-visible)]:outline-tdl10-acc [&_svg]:size-3.75 [&_svg]:fill-none [&_svg]:stroke-current [&_svg]:stroke-2 [&_svg]:[stroke-linecap:round]">
        <legend class="sr-only">Theme</legend>
        <label><input class="sr-only" type="radio" name="tdl10-theme" id="tdl10-light" checked><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>Light</label>
        <label><input class="sr-only" type="radio" name="tdl10-theme" id="tdl10-dark"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/></svg>Dark</label>
        <label><input class="sr-only" type="radio" name="tdl10-theme" id="tdl10-sys"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>System</label>
      </fieldset>
    </header>
    <div class="grid min-h-0 auto-rows-min grid-cols-1 gap-3 @min-[36rem]/body:grid-cols-3 overflow-y-auto overscroll-contain [&>article]:rounded-2xl [&>article]:border [&>article]:border-tdl10-edge [&>article]:bg-tdl10-card [&>article]:px-4.5 [&>article]:py-4 [&>article]:shadow-[0_18px_40px_-26px_var(--tdl10-shadow)] [&>article]:transition-colors [&>article]:duration-300 [&_h3]:text-[10.5px] [&_h3]:font-bold [&_h3]:tracking-[0.11em] [&_h3]:text-tdl10-mut [&_h3]:uppercase">
      <article><h3>Sessions</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tracking-tight tabular-nums">24,981</p><small class="text-[11.5px] font-semibold text-tdl10-good">▲ 6.1% this week</small></article>
      <article><h3>Bounce rate</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tracking-tight tabular-nums">31.4%</p><small class="text-[11.5px] font-semibold text-tdl10-good">▼ 1.2 pts this week</small></article>
      <article><h3>Avg. duration</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tracking-tight tabular-nums">4m 12s</p><small class="text-[11.5px] font-semibold text-tdl10-good">▲ 18s this week</small></article>
      <article class="col-span-full"><h3 class="flex justify-between">Traffic by hour<span class="tracking-normal text-tdl10-ink normal-case">Peak 14:00</span></h3>
        <div aria-hidden="true" class="mt-3 flex h-24 items-end gap-1.75 *:h-(--h) *:flex-1 *:rounded-t-[4px] *:bg-linear-to-t *:from-tdl10-acc/25 *:to-tdl10-acc"><i style="--h:30%"></i><i style="--h:44%"></i><i style="--h:38%"></i><i style="--h:58%"></i><i style="--h:50%"></i><i style="--h:72%"></i><i style="--h:64%"></i><i style="--h:86%"></i><i style="--h:76%"></i><i style="--h:94%"></i><i style="--h:68%"></i><i style="--h:52%"></i></div>
      </article>
      <article class="col-span-full grid gap-1.5"><h3>Release notes</h3><p class="text-[13.5px]/[1.6] text-tdl10-mut">Theme tokens now cover charts, borders and native controls. Scrollbars follow <code class="rounded-[5px] border border-tdl10-edge bg-tdl10-bg px-1.25 font-tdl10-mono text-[11.5px] font-semibold">color-scheme</code> automatically.</p><a href="#changelog" class="justify-self-start rounded-sm text-[13px] font-bold text-tdl10-acc no-underline underline-offset-3 hover:underline focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdl10-acc">View changelog →</a></article>
    </div>
    <footer aria-label="Live token values" class="flex flex-wrap items-center gap-4 border-t border-dashed border-tdl10-edge pt-3.25 font-tdl10-mono text-[11px] font-semibold text-tdl10-mut [&>span]:flex [&>span]:items-center [&>span]:gap-1.75 [&_i]:size-3.5 [&_i]:rounded-[4px] [&_i]:border [&_i]:border-tdl10-edge [&_i]:transition-colors [&_i]:duration-300">
      <span><i aria-hidden="true" class="bg-tdl10-bg"></i>--tdl10-bg</span>
      <span><i aria-hidden="true" class="bg-tdl10-card"></i>--tdl10-card</span>
      <span><i aria-hidden="true" class="bg-tdl10-ink"></i>--tdl10-ink</span>
      <span><i aria-hidden="true" class="bg-tdl10-acc"></i>--tdl10-acc</span>
      <em class="ml-auto font-tdl10-sans text-[11.5px] font-normal">one radio re-themes everything above</em>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* inline: utilities reference the variables directly, so the root can swap them at runtime */

@theme inline {
  --color-tdl10-bg: var(--tdl10-bg);
  --color-tdl10-card: var(--tdl10-card);
  --color-tdl10-ink: var(--tdl10-ink);
  --color-tdl10-mut: var(--tdl10-mut);
  --color-tdl10-edge: var(--tdl10-edge);
  --color-tdl10-acc: var(--tdl10-acc);
  --color-tdl10-good: var(--tdl10-good);
}

@theme {
  --font-tdl10-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-tdl10-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Light values stated here too, so the stage paints correctly before the browser build compiles. */

.tdl-10 {
  width: 100%;
  min-height: 100svh;
  background: #f7f8fb;
  background: oklch(0.975 0.005 260);
}

@media (prefers-reduced-motion: reduce) {
  .tdl-10 * {
    transition-duration: 0.01s !important;
  }
}
```
