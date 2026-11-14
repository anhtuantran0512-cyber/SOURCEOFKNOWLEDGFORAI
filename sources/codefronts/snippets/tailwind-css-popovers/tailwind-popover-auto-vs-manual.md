---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-auto-vs-manual/"
title: "Tailwind Auto vs Manual Popover Behavior"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Two state machines, side by side, clickable."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto vs Manual Popover Behavior
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-auto-vs-manual/

Two state machines, side by side, clickable. popover="auto" light-dismisses, answers Escape and closes other autos; popover="manual" ignores all three. The port adds what the original only described: a live status LED beside every invoker, lit by group-has-[#id:popover-open]/root:, so you watch opening Activity switch Notifications off.
## HTML
```html
<section class="tpop-02 group/root w-full min-h-svh bg-tpop02-navy bg-[linear-gradient(var(--color-tpop02-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-tpop02-grid)_1px,transparent_1px)] bg-[size:32px_32px] px-4 py-9 font-tpop02-sans text-tpop02-ink" aria-label="Auto versus manual popover demo">
  <div class="grid min-h-[calc(100svh-72px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[44rem] rounded-sm border border-tpop02-rule bg-tpop02-board px-5 pt-6 pb-6.5 shadow-[0_30px_60px_-30px_oklch(0_0_0/0.7)]">
      <header class="mb-5.5">
        <h2 class="mb-1.5 text-[clamp(21px,4.4vw,28px)] font-semibold leading-tight tracking-[-0.02em]">Dismissal is a state, not a style</h2>
        <p class="text-[13.5px] text-tpop02-mut">Open all three. Then click the empty board — and watch the lights.</p>
      </header>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-4.5">
        <div class="min-w-0 rounded-sm border border-tpop02-rule bg-tpop02-navy px-3.5 py-4">
          <p class="mb-3.5 inline-block rounded-sm bg-tpop02-ok px-2 py-1.5 font-tpop02-mono text-[11px] font-semibold leading-none text-tpop02-navy">popover="auto"</p>
          <div class="mb-4 grid gap-2">
            <button id="tpop-02-trigger" type="button" popovertarget="tpop-02-auto" class="flex min-h-11 cursor-pointer items-center justify-between gap-3 rounded-sm bg-tpop02-ink px-3.5 text-[13px] font-semibold text-tpop02-navy transition-colors hover:bg-tpop02-ink/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop02-ok">
              Toggle notifications
              <span aria-hidden="true" class="size-2 rounded-full bg-tpop02-navy/25 transition-[background-color,box-shadow] duration-200 group-has-[#tpop-02-auto:popover-open]/root:bg-tpop02-okdeep group-has-[#tpop-02-auto:popover-open]/root:shadow-[0_0_0_3px_oklch(0.62_0.12_180/0.3)]"></span>
            </button>
            <button type="button" popovertarget="tpop-02-auto2" class="flex min-h-11 cursor-pointer items-center justify-between gap-3 rounded-sm border border-tpop02-rule px-3.5 text-[13px] font-semibold text-tpop02-ink transition-colors hover:border-tpop02-mut focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop02-ok">
              Toggle activity
              <span aria-hidden="true" class="size-2 rounded-full bg-tpop02-rule transition-[background-color,box-shadow] duration-200 group-has-[#tpop-02-auto2:popover-open]/root:bg-tpop02-ok group-has-[#tpop-02-auto2:popover-open]/root:shadow-[0_0_10px_var(--color-tpop02-ok)]"></span>
            </button>
          </div>
          <ul class="grid gap-2">
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-ok">Outside click closes it</li>
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-ok">Escape closes it</li>
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-ok">Opening another auto closes it</li>
          </ul>
        </div>
        <div class="min-w-0 rounded-sm border border-tpop02-rule bg-tpop02-navy px-3.5 py-4">
          <p class="mb-3.5 inline-block rounded-sm bg-tpop02-warn px-2 py-1.5 font-tpop02-mono text-[11px] font-semibold leading-none text-tpop02-navy">popover="manual"</p>
          <div class="mb-4 grid gap-2">
            <button type="button" popovertarget="tpop-02-manual" popovertargetaction="show" class="flex min-h-11 cursor-pointer items-center justify-between gap-3 rounded-sm bg-tpop02-ink px-3.5 text-[13px] font-semibold text-tpop02-navy transition-colors hover:bg-tpop02-ink/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop02-warn">
              Show inspector
              <span aria-hidden="true" class="size-2 rounded-full bg-tpop02-navy/25 transition-[background-color,box-shadow] duration-200 group-has-[#tpop-02-manual:popover-open]/root:bg-tpop02-warndeep group-has-[#tpop-02-manual:popover-open]/root:shadow-[0_0_0_3px_oklch(0.7_0.13_65/0.35)]"></span>
            </button>
            <button type="button" popovertarget="tpop-02-manual" popovertargetaction="hide" class="flex min-h-11 cursor-pointer items-center justify-between gap-3 rounded-sm border border-tpop02-rule px-3.5 text-[13px] font-semibold text-tpop02-ink transition-colors hover:border-tpop02-mut focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop02-warn">Hide inspector</button>
          </div>
          <ul class="grid gap-2">
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-warn">Outside click does nothing</li>
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-warn">Escape does nothing</li>
            <li class="relative min-w-0 pl-4 text-[13px] leading-normal text-tpop02-mut before:absolute before:top-[7px] before:left-0 before:size-1.5 before:bg-tpop02-warn">You own dismissal</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div popover="auto" id="tpop-02-auto" role="group" aria-label="Notifications" class="fixed inset-auto bottom-6 left-6 w-[min(19rem,calc(100vw-28px))] rounded-sm border border-tpop02-rule border-l-2 border-l-tpop02-ok bg-tpop02-surface px-4 pt-4 pb-3.5 text-tpop02-ink opacity-0 shadow-[0_26px_50px_-24px_oklch(0_0_0/0.85)] transition-[opacity,translate,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 starting:open:translate-y-3 starting:open:opacity-0 motion-reduce:transition-none max-[560px]:inset-x-3.5 max-[560px]:bottom-3.5 max-[560px]:w-auto">
    <p class="mb-2 text-xs font-semibold uppercase tracking-[0.08em] text-tpop02-mut">Notifications</p>
    <p class="mb-1.5 text-[13.5px] leading-normal">Priya Sharma approved deploy <span class="font-tpop02-mono text-[0.9em] text-tpop02-ok">web-4821</span>.</p>
    <p class="mb-1.5 text-[13.5px] leading-normal">Nightly export finished in 4m 12s.</p>
    <p class="mt-2.5 border-t border-tpop02-rule pt-2.5 text-xs text-tpop02-mut">Auto · light dismiss on</p>
  </div>

  <div popover="auto" id="tpop-02-auto2" role="group" aria-label="Activity" class="fixed inset-auto top-6 right-6 w-[min(19rem,calc(100vw-28px))] rounded-sm border border-tpop02-rule border-l-2 border-l-tpop02-ok bg-tpop02-surface px-4 pt-4 pb-3.5 text-tpop02-ink opacity-0 shadow-[0_26px_50px_-24px_oklch(0_0_0/0.85)] transition-[opacity,translate,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 starting:open:-translate-y-3 starting:open:opacity-0 motion-reduce:transition-none max-[560px]:inset-x-3.5 max-[560px]:top-3.5 max-[560px]:w-auto">
    <p class="mb-2 text-xs font-semibold uppercase tracking-[0.08em] text-tpop02-mut">Activity</p>
    <p class="mb-1.5 text-[13.5px] leading-normal">Jordan Lee opened a draft on Billing.</p>
    <p class="mt-2.5 border-t border-tpop02-rule pt-2.5 text-xs text-tpop02-mut">Opening me closed the other auto panel</p>
  </div>

  <div popover="manual" id="tpop-02-manual" role="group" aria-label="Request inspector" class="fixed inset-auto right-6 bottom-6 w-[min(19rem,calc(100vw-28px))] rounded-sm border border-tpop02-warn bg-tpop02-surface px-4 pt-4 pb-3.5 text-tpop02-ink opacity-0 shadow-[0_26px_50px_-24px_oklch(0_0_0/0.85)] transition-[opacity,translate,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 starting:open:translate-y-3 starting:open:opacity-0 motion-reduce:transition-none max-[560px]:inset-x-3.5 max-[560px]:bottom-21 max-[560px]:w-auto">
    <div class="flex items-center justify-between gap-2">
      <p class="mb-2 text-xs font-semibold uppercase tracking-[0.08em] text-tpop02-mut">Request inspector</p>
      <button type="button" popovertarget="tpop-02-manual" popovertargetaction="hide" aria-label="Close inspector" class="-mt-3.5 -mr-3 inline-flex size-11 cursor-pointer items-center justify-center text-tpop02-warn focus-visible:outline-3 focus-visible:outline-offset-1 focus-visible:outline-tpop02-warn">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
      </button>
    </div>
    <p class="mb-1.5 text-[13.5px] leading-normal"><span class="font-tpop02-mono text-[0.9em] text-tpop02-ok">GET /v2/accounts</span> · 200 · 84ms</p>
    <p class="mb-1.5 text-[13.5px] leading-normal"><span class="font-tpop02-mono text-[0.9em] text-tpop02-ok">POST /v2/tokens</span> · 201 · 132ms</p>
    <p class="mt-2.5 border-t border-tpop02-rule pt-2.5 text-xs text-tpop02-warn">Manual · nothing dismisses me but that button</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop02-navy: #0a152a;
  --color-tpop02-navy: oklch(0.2 0.045 262);
  --color-tpop02-grid: #16243c8c;
  --color-tpop02-grid: oklch(0.26 0.05 262 / 0.55);
  --color-tpop02-board: #13213c;
  --color-tpop02-board: oklch(0.25 0.055 262);
  --color-tpop02-surface: #1c3051;
  --color-tpop02-surface: oklch(0.31 0.065 260);
  --color-tpop02-ink: #e8eff9;
  --color-tpop02-ink: oklch(0.95 0.015 255);
  --color-tpop02-mut: #a6b9d5;
  --color-tpop02-mut: oklch(0.78 0.045 258);
  --color-tpop02-rule: #29415f;
  --color-tpop02-rule: oklch(0.37 0.06 255);
  --color-tpop02-ok: #61d5c0;
  --color-tpop02-ok: oklch(0.8 0.11 180);
  --color-tpop02-okdeep: #007b6b;
  --color-tpop02-okdeep: oklch(0.52 0.1 180);
  --color-tpop02-warn: #f6b069;
  --color-tpop02-warn: oklch(0.81 0.12 65);
  --color-tpop02-warndeep: #b3621e;
  --color-tpop02-warndeep: oklch(0.58 0.13 55);
  --font-tpop02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpop02-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpop-02 {
  width: 100%;
  min-height: 100svh;
}
```
