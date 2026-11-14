---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/bento-grid-card-tabs-tailwind-css/"
title: "Bento Grid Card Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A three-tile bento where the tabs are the cards: each shows an icon, a metric and a caption before it's even opened."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Card Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/bento-grid-card-tabs-tailwind-css/

A three-tile bento where the tabs are the cards: each shows an icon, a metric and a caption before it's even opened. The checked card lifts, gains a violet ring and a tinted shadow, and its panel becomes the full-width fourth cell beneath — entering with starting:.
## HTML
```html
<section class="ttb-07 group/tabs grid min-h-svh w-full place-items-center bg-ttb07-bg px-5 py-14 font-ttb07-sans text-ttb07-ink" aria-label="Bento grid card tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Dashboard view" class="grid grid-cols-3 gap-2.5">
        <label class="group/tab flex min-w-0 cursor-pointer flex-col gap-3 rounded-2xl bg-ttb07-card p-4 ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-300 hover:bg-ttb07-hover has-checked:-translate-y-0.5 has-checked:bg-ttb07-active has-checked:shadow-[0_10px_24px_-8px_color-mix(in_oklab,var(--color-ttb07-acc)_45%,transparent)] has-checked:ring-2 has-checked:ring-ttb07-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb07-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb07" id="ttb07-r1" checked><span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-white/6 text-ttb07-mut transition-colors group-has-checked/tab:bg-ttb07-acc group-has-checked/tab:text-white"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 19V10M10 19V5M16 19v-6M22 19H2"/></svg></span><span><span class="block text-[15px] font-bold">Stats</span><span class="block truncate text-xs text-ttb07-mut">Real-time data</span></span></label>
        <label class="group/tab flex min-w-0 cursor-pointer flex-col gap-3 rounded-2xl bg-ttb07-card p-4 ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-300 hover:bg-ttb07-hover has-checked:-translate-y-0.5 has-checked:bg-ttb07-active has-checked:shadow-[0_10px_24px_-8px_color-mix(in_oklab,var(--color-ttb07-acc)_45%,transparent)] has-checked:ring-2 has-checked:ring-ttb07-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb07-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb07" id="ttb07-r2"><span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-white/6 text-ttb07-mut transition-colors group-has-checked/tab:bg-ttb07-acc group-has-checked/tab:text-white"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18v12H3zM3 7l9 7 9-7"/></svg></span><span><span class="block text-[15px] font-bold">Inbox</span><span class="block truncate text-xs text-ttb07-mut">12 new</span></span></label>
        <label class="group/tab flex min-w-0 cursor-pointer flex-col gap-3 rounded-2xl bg-ttb07-card p-4 ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-300 hover:bg-ttb07-hover has-checked:-translate-y-0.5 has-checked:bg-ttb07-active has-checked:shadow-[0_10px_24px_-8px_color-mix(in_oklab,var(--color-ttb07-acc)_45%,transparent)] has-checked:ring-2 has-checked:ring-ttb07-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb07-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb07" id="ttb07-r3"><span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-white/6 text-ttb07-mut transition-colors group-has-checked/tab:bg-ttb07-acc group-has-checked/tab:text-white"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5L20 6"/></svg></span><span><span class="block text-[15px] font-bold">Tasks</span><span class="block truncate text-xs text-ttb07-mut">3 pending</span></span></label>
      </div>
      <div class="mt-2.5 rounded-2xl bg-ttb07-card p-5 ring-1 ring-white/8">
        <div class="hidden transition-[opacity,scale] duration-300 group-has-[#ttb07-r1:checked]/tabs:block starting:scale-[0.98] starting:opacity-0 motion-reduce:transition-none"><p class="font-ttb07-mono text-[11px] tracking-[0.12em] text-ttb07-acc-ink uppercase">Stats</p><p class="mt-1.5 text-[15px] leading-relaxed text-ttb07-soft">Daily and weekly metrics summarised, with anomalies flagged at the top.</p></div>
        <div class="hidden transition-[opacity,scale] duration-300 group-has-[#ttb07-r2:checked]/tabs:block starting:scale-[0.98] starting:opacity-0 motion-reduce:transition-none"><p class="font-ttb07-mono text-[11px] tracking-[0.12em] text-ttb07-acc-ink uppercase">Inbox</p><p class="mt-1.5 text-[15px] leading-relaxed text-ttb07-soft">Unread messages from your team, grouped by thread and priority.</p></div>
        <div class="hidden transition-[opacity,scale] duration-300 group-has-[#ttb07-r3:checked]/tabs:block starting:scale-[0.98] starting:opacity-0 motion-reduce:transition-none"><p class="font-ttb07-mono text-[11px] tracking-[0.12em] text-ttb07-acc-ink uppercase">Tasks</p><p class="mt-1.5 text-[15px] leading-relaxed text-ttb07-soft">Items due in the next seven days, sorted by deadline.</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb07-mono text-[11.5px] text-ttb07-mut">labels as cards · has-checked:ring-2 · starting: panel</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb07-bg: #0a0a0e;
  --color-ttb07-bg: oklch(0.147 0.009 285.3);
  --color-ttb07-card: #17171e;
  --color-ttb07-card: oklch(0.208 0.014 285.1);
  --color-ttb07-hover: #1d1d26;
  --color-ttb07-hover: oklch(0.235 0.017 285.0);
  --color-ttb07-active: #1d1b2b;
  --color-ttb07-active: oklch(0.232 0.031 289.5);
  --color-ttb07-ink: #f5f5f8;
  --color-ttb07-ink: oklch(0.971 0.004 286.3);
  --color-ttb07-soft: #cbcad6;
  --color-ttb07-soft: oklch(0.843 0.017 289.9);
  --color-ttb07-mut: #9897a8;
  --color-ttb07-mut: oklch(0.683 0.025 288.4);
  --color-ttb07-acc: #7c6cff;
  --color-ttb07-acc: oklch(0.624 0.210 283.4);
  --color-ttb07-acc-ink: #a99fff;
  --color-ttb07-acc-ink: oklch(0.749 0.136 287.4);
  --font-ttb07-sans: 'Geist', system-ui, sans-serif;
  --font-ttb07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-07 {
  width: 100%;
  min-height: 100svh;
}
```
