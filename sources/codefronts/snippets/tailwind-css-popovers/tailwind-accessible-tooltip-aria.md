---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-accessible-tooltip-aria/"
title: "Tailwind Accessible Tooltip with ARIA"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "A ledger of what the API gives you — top layer, light dismiss, Escape, focus return — and what it doesn't: a role, a name, a described-by relationship."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible Tooltip with ARIA
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-accessible-tooltip-aria/

A ledger of what the API gives you — top layer, light dismiss, Escape, focus return — and what it doesn't: a role, a name, a described-by relationship. The demo wires both correctly: a click-opened hint with aria-describedby and no tooltip role, and a role="menu" panel. The port fixes the original's always-visible menu (display: grid outranked the UA's closed state) with open:grid.
## HTML
```html
<section class="tpop-20 transition-[--tpop20-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop20-d:1] [[data-theme=dark]_&]:[--tpop20-d:1] [[data-theme=light]_&]:[--tpop20-d:0] group/root w-full min-h-svh bg-tpop20-sepia px-5 py-11 font-tpop20-sans text-tpop20-ink" aria-label="Accessible popover with ARIA roles demo">
  <div class="grid min-h-[calc(100svh-88px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[32rem] rounded-t-[12rem] rounded-b-3xl border border-tpop20-rule bg-tpop20-paper px-6.5 pt-12 pb-6.5 shadow-[0_24px_50px_-40px_oklch(0.3_0.03_50/0.6)]">
      <p class="mb-2.5 text-center text-[10.5px] font-bold uppercase tracking-[0.22em] text-tpop20-mut">Accessibility ledger</p>
      <h2 class="mb-6 text-center font-tpop20-serif text-[clamp(24px,5vw,32px)] font-medium leading-[1.15] tracking-[-0.015em] text-balance">What the API does, and does not, hand you</h2>
      <div class="mb-6 grid grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4">
        <ul class="grid gap-2 rounded-2xl bg-tpop20-yes/10 px-4 py-3.5" aria-label="Provided by popover">
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[6px] before:left-0.5 before:h-1.5 before:w-2.5 before:-rotate-45 before:border-b-2 before:border-l-2 before:border-tpop20-yes before:content-['']">Top layer</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[6px] before:left-0.5 before:h-1.5 before:w-2.5 before:-rotate-45 before:border-b-2 before:border-l-2 before:border-tpop20-yes before:content-['']">Light dismiss</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[6px] before:left-0.5 before:h-1.5 before:w-2.5 before:-rotate-45 before:border-b-2 before:border-l-2 before:border-tpop20-yes before:content-['']">Escape to close</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[6px] before:left-0.5 before:h-1.5 before:w-2.5 before:-rotate-45 before:border-b-2 before:border-l-2 before:border-tpop20-yes before:content-['']">Focus back to the trigger</li>
        </ul>
        <ul class="grid gap-2 rounded-2xl bg-tpop20-no/9 px-4 py-3.5" aria-label="Not provided by popover">
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[10px] before:left-0.5 before:h-0.5 before:w-2.5 before:bg-tpop20-no before:content-['']">A role</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[10px] before:left-0.5 before:h-0.5 before:w-2.5 before:bg-tpop20-no before:content-['']">An accessible name</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[10px] before:left-0.5 before:h-0.5 before:w-2.5 before:bg-tpop20-no before:content-['']">A described-by relationship</li>
          <li class="relative min-w-0 pl-5 text-[13.5px] leading-normal before:absolute before:top-[10px] before:left-0.5 before:h-0.5 before:w-2.5 before:bg-tpop20-no before:content-['']">Any keyboard model inside</li>
        </ul>
      </div>
      <div class="flex flex-wrap items-center justify-between gap-3.5 border-t border-tpop20-rule pt-4.5">
        <p class="flex min-w-0 items-center gap-2 text-[14.5px] font-semibold">
          Retention window
          <button id="tpop-20-trigger" type="button" popovertarget="tpop-20-hint" aria-describedby="tpop-20-hint" aria-label="What the retention window means" class="inline-flex size-11 cursor-pointer items-center justify-center rounded-full border border-tpop20-rule text-tpop20-mut transition-colors [anchor-name:--tpop20-hint] hover:bg-tpop20-sepia hover:text-tpop20-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop20-yes group-has-[#tpop-20-hint:popover-open]/root:border-tpop20-ink group-has-[#tpop-20-hint:popover-open]/root:text-tpop20-ink">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M10 9v5M10 6.3v.8"/></svg>
          </button>
        </p>
        <button type="button" popovertarget="tpop-20-menu" aria-haspopup="menu" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full bg-tpop20-ink px-4 text-[13px] font-semibold text-tpop20-paper transition-colors [anchor-name:--tpop20-menu] hover:bg-tpop20-ink/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop20-yes">
          Row actions
          <svg class="transition-transform duration-200 motion-reduce:transition-none group-has-[#tpop-20-menu:popover-open]/root:rotate-180" viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 9.5 8 5.5 12 9.5"/></svg>
        </button>
      </div>
      <p class="mt-4.5 text-center text-[12.5px] leading-relaxed text-tpop20-mut">The hint is described-by. The menu is role=menu. Neither came for free.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-20-hint" class="fixed m-auto w-[min(17rem,calc(100vw-32px))] rounded-2xl border border-tpop20-rule bg-tpop20-paper px-4 py-3 text-[13px] leading-normal text-tpop20-ink opacity-0 shadow-[0_18px_38px_-24px_oklch(0.3_0.03_50/0.5)] text-pretty transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop20-hint] [position-area:block-start_center] [justify-self:anchor-center] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mb-2.5">Deleted records stay recoverable for <strong class="font-semibold">30 days</strong>, then are purged nightly.</div>

  <div popover="auto" id="tpop-20-menu" role="menu" aria-label="Row actions" class="fixed m-auto w-[min(14.5rem,calc(100vw-32px))] gap-0.5 rounded-3xl border border-tpop20-rule bg-tpop20-paper p-1.5 text-tpop20-ink opacity-0 shadow-[0_18px_38px_-24px_oklch(0.3_0.03_50/0.5)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop20-menu] [position-area:block-start_span-inline-start] [position-try-fallbacks:flip-block,flip-inline] open:grid open:opacity-100 starting:open:translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mb-2.5">
    <button type="button" role="menuitem" class="min-h-11 w-full min-w-0 cursor-pointer rounded-full px-3.5 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop20-sepia focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop20-yes">Extend retention</button>
    <button type="button" role="menuitem" class="min-h-11 w-full min-w-0 cursor-pointer rounded-full px-3.5 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop20-sepia focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop20-yes">Export audit trail</button>
    <span role="separator" class="mx-3 my-0.5 block h-px bg-tpop20-rule"></span>
    <button type="button" role="menuitem" class="min-h-11 w-full min-w-0 cursor-pointer rounded-full px-3.5 text-left text-[13.5px] font-medium text-tpop20-no transition-colors hover:bg-tpop20-no/9 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop20-no">Purge now</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop20-sepia: #f0e6da;
  --color-tpop20-sepia: oklch(0.93 0.02 75);
  --color-tpop20-paper: #fbf6ed;
  --color-tpop20-paper: oklch(0.975 0.013 80);
  --color-tpop20-ink: #2f241e;
  --color-tpop20-ink: oklch(0.27 0.02 50);
  --color-tpop20-mut: #68574a;
  --color-tpop20-mut: oklch(0.47 0.03 60);
  --color-tpop20-rule: #ddcfbc;
  --color-tpop20-rule: oklch(0.86 0.03 75);
  --color-tpop20-yes: #476536;
  --color-tpop20-yes: oklch(0.47 0.08 135);
  --color-tpop20-no: #983d1f;
  --color-tpop20-no: oklch(0.48 0.13 38);
  --font-tpop20-serif: 'Newsreader', Georgia, serif;
  --font-tpop20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop20-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-20 {
  width: 100%;
  min-height: 100svh;
  --color-tpop20-sepia: color-mix(in oklch, oklch(0.17 0.014 60) calc(var(--tpop20-d) * 100%), oklch(0.93 0.02 75));
  --color-tpop20-paper: color-mix(in oklch, oklch(0.215 0.016 60) calc(var(--tpop20-d) * 100%), oklch(0.975 0.013 80));
  --color-tpop20-ink: color-mix(in oklch, oklch(0.94 0.016 75) calc(var(--tpop20-d) * 100%), oklch(0.27 0.02 50));
  --color-tpop20-mut: color-mix(in oklch, oklch(0.74 0.03 65) calc(var(--tpop20-d) * 100%), oklch(0.47 0.03 60));
  --color-tpop20-rule: color-mix(in oklch, oklch(0.33 0.022 60) calc(var(--tpop20-d) * 100%), oklch(0.86 0.03 75));
  --color-tpop20-yes: color-mix(in oklch, oklch(0.78 0.1 135) calc(var(--tpop20-d) * 100%), oklch(0.47 0.08 135));
  --color-tpop20-no: color-mix(in oklch, oklch(0.76 0.13 38) calc(var(--tpop20-d) * 100%), oklch(0.48 0.13 38));
}
```
