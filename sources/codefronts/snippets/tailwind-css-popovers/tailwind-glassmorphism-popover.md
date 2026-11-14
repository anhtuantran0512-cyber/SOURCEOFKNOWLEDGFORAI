---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-glassmorphism-popover/"
title: "Tailwind Glassmorphism Popover"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "A frosted panel over a rich aurora, with the opaque fallback as the base class and the frost layered on with supports-[backdrop-filter:blur(1px)]: — so an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Popover
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-glassmorphism-popover/

A frosted panel over a rich aurora, with the opaque fallback as the base class and the frost layered on with supports-[backdrop-filter:blur(1px)]: — so an unsupporting engine shows a solid card, never text over raw colour. Because the panel lives in the top layer it has no transformed ancestor to become its backdrop root: the blur samples the real page.
## HTML
```html
<section class="tpop-18 group/root w-full min-h-svh bg-tpop18-night bg-[radial-gradient(46rem_30rem_at_12%_8%,var(--color-tpop18-violet),transparent_62%),radial-gradient(38rem_26rem_at_88%_22%,var(--color-tpop18-teal),transparent_60%),radial-gradient(34rem_28rem_at_62%_92%,var(--color-tpop18-rose),transparent_58%)] px-4.5 py-10 font-tpop18-sans text-tpop18-ink" aria-label="Glassmorphism popover demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[28rem]">
      <div aria-hidden="true" class="mb-6 size-28 rounded-3xl bg-[conic-gradient(from_210deg,var(--color-tpop18-rose),var(--color-tpop18-violet),var(--color-tpop18-teal),var(--color-tpop18-rose))] shadow-[0_24px_50px_-18px_oklch(0_0_0/0.7),inset_0_1px_0_oklch(1_0_0/0.3)]"></div>
      <p class="mb-2.5 text-[10.5px] font-bold uppercase tracking-[0.24em] text-tpop18-mut">Now playing</p>
      <h2 class="mb-1.5 text-[clamp(34px,8vw,52px)] font-bold leading-[0.98] tracking-[-0.035em]">Wickfield No. 5</h2>
      <p class="mb-5 text-[15px] text-tpop18-mut">Marisa Ault · Slow Water · 2026</p>
      <div class="mb-5 flex items-center gap-3 font-tpop18-mono text-[11.5px] text-tpop18-mut">
        <span class="tabular-nums">2:14</span>
        <span class="h-1 flex-auto overflow-hidden rounded-full bg-white/15"><span class="block h-full w-1/3 rounded-full bg-tpop18-ink"></span></span>
        <span class="tabular-nums">6:41</span>
      </div>
      <button id="tpop-18-trigger" type="button" popovertarget="tpop-18-panel" aria-label="Track details" class="inline-flex size-11 cursor-pointer items-center justify-center rounded-full border border-white/30 bg-white/12 text-tpop18-ink transition-[background-color,box-shadow] duration-200 [anchor-name:--tpop18-a] hover:bg-white/20 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tpop18-ink group-has-[#tpop-18-panel:popover-open]/root:bg-white/25 group-has-[#tpop-18-panel:popover-open]/root:shadow-[0_0_24px_oklch(1_0_0/0.35)]">
        <svg viewBox="0 0 22 22" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M11 10v5.4M11 7.2v.9"/></svg>
      </button>
      <p class="mt-5 max-w-[24rem] text-[13px] leading-relaxed text-tpop18-mut text-pretty">Open the panel: it blurs the top layer's view of this page, not a mocked-up copy of it.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-18-panel" role="group" aria-label="Track details" class="fixed m-auto w-[min(18rem,calc(100vw-28px))] rounded-3xl border border-white/30 bg-tpop18-glass p-4.5 text-tpop18-ink opacity-0 translate-y-1.5 shadow-[0_26px_60px_-28px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.22)] transition-[opacity,translate,display,overlay] duration-200 ease-out transition-discrete [position-anchor:--tpop18-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block,flip-inline] open:translate-y-0 open:opacity-100 starting:open:translate-y-1.5 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5 supports-[backdrop-filter:blur(1px)]:bg-tpop18-glass/55 supports-[backdrop-filter:blur(1px)]:backdrop-blur-[18px] supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150">
    <p class="mb-3 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop18-mut">Track details</p>
    <dl class="grid gap-2">
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop18-mut">Length</dt><dd class="font-tpop18-mono text-[13px] font-semibold">6:41</dd></div>
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop18-mut">Key</dt><dd class="text-[13px] font-semibold">D minor</dd></div>
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop18-mut">Tempo</dt><dd class="font-tpop18-mono text-[13px] font-semibold">72 bpm</dd></div>
      <div class="flex min-w-0 justify-between gap-3"><dt class="text-[13px] text-tpop18-mut">Mastered</dt><dd class="text-[13px] font-semibold">Alex Chen</dd></div>
    </dl>
    <p class="mt-3.5 border-t border-white/16 pt-3 text-xs text-tpop18-mut">Opaque fallback first, frost second.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop18-night: #0f091c;
  --color-tpop18-night: oklch(0.16 0.04 295);
  --color-tpop18-violet: #4a237a;
  --color-tpop18-violet: oklch(0.36 0.14 300);
  --color-tpop18-teal: #005b6e;
  --color-tpop18-teal: oklch(0.43 0.09 215);
  --color-tpop18-rose: #9f2346;
  --color-tpop18-rose: oklch(0.47 0.16 10);
  --color-tpop18-glass: #221838;
  --color-tpop18-glass: oklch(0.24 0.06 295);
  --color-tpop18-ink: #f5f3ff;
  --color-tpop18-ink: oklch(0.97 0.015 295);
  --color-tpop18-mut: #ccc6e3;
  --color-tpop18-mut: oklch(0.84 0.04 295);
  --font-tpop18-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpop18-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpop-18 {
  width: 100%;
  min-height: 100svh;
}
```
