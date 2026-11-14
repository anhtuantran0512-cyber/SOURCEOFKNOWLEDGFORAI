---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-vs-dialog-modal/"
title: "Tailwind Popover vs Dialog Modal"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "One decision rule, shown twice: <dialog> via command=\"show-modal\" when the user must deal with it, popover when they can ignore it and carry on."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Popover vs Dialog Modal
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-vs-dialog-modal/

One decision rule, shown twice: <dialog> via command="show-modal" when the user must deal with it, popover when they can ignore it and carry on. The port animates both with the same utilities — open: matches [open] on the dialog and :popover-open on the panel — so the comparison isolates modality, and fixes the preflight trap that left the dialog pinned to the top-left.
## HTML
```html
<section class="tpop-17 transition-[--tpop17-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop17-d:1] [[data-theme=dark]_&]:[--tpop17-d:1] [[data-theme=light]_&]:[--tpop17-d:0] group/root w-full min-h-svh bg-tpop17-paper px-4.5 py-10 font-tpop17-sans text-tpop17-ink" aria-label="Popover versus dialog demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[36rem] border border-tpop17-hair bg-tpop17-surface px-5.5 pt-6.5 pb-5.5">
      <p class="mb-2 text-[10.5px] font-bold uppercase tracking-[0.22em] text-tpop17-mut">Decision</p>
      <h2 class="mb-5.5 font-tpop17-serif text-[clamp(30px,6.5vw,44px)] leading-[1.02] tracking-[-0.01em]">Can the user <em class="italic">ignore</em> it?</h2>
      <div class="mb-6 grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4.5">
        <div class="grid min-w-0 content-start gap-2 border-t-2 border-tpop17-go pt-3">
          <p class="text-xs font-bold uppercase tracking-[0.08em] text-tpop17-go">Yes → popover</p>
          <p class="mb-1.5 text-[13.5px] leading-relaxed text-tpop17-mut text-pretty">Page stays live. Focus can leave. An outside click puts it away.</p>
          <button id="tpop-17-trigger" type="button" popovertarget="tpop-17-pop" class="min-h-11 cursor-pointer border-2 border-tpop17-ink px-3.5 text-[13px] font-semibold text-tpop17-ink transition-colors [anchor-name:--tpop17-a] hover:bg-tpop17-go/8 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop17-go group-has-[#tpop-17-pop:popover-open]/root:border-tpop17-go group-has-[#tpop-17-pop:popover-open]/root:bg-tpop17-go/10">Share this board</button>
        </div>
        <div class="grid min-w-0 content-start gap-2 border-t-2 border-tpop17-stop pt-3">
          <p class="text-xs font-bold uppercase tracking-[0.08em] text-tpop17-stop">No → dialog</p>
          <p class="mb-1.5 text-[13.5px] leading-relaxed text-tpop17-mut text-pretty">Focus contained. Page inert. Backdrop blocks the click.</p>
          <button type="button" command="show-modal" commandfor="tpop-17-dialog" class="min-h-11 cursor-pointer border-2 border-tpop17-stop bg-tpop17-stop px-3.5 text-[13px] font-semibold text-tpop17-surface transition-colors hover:bg-tpop17-stop/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop17-stop">Delete workspace</button>
        </div>
      </div>
      <table class="w-full border-collapse text-[13px]">
        <thead><tr><th scope="col" class="pb-2 text-left text-[10.5px] font-bold uppercase tracking-[0.14em] text-tpop17-mut"><span class="sr-only">Behaviour</span></th><th scope="col" class="pb-2 pl-3 text-left text-[10.5px] font-bold uppercase tracking-[0.14em] text-tpop17-go">Popover</th><th scope="col" class="pb-2 text-right text-[10.5px] font-bold uppercase tracking-[0.14em] text-tpop17-stop">Dialog</th></tr></thead>
        <tbody>
          <tr class="border-t border-tpop17-hair"><th scope="row" class="py-2 text-left font-semibold text-tpop17-mut">Focus</th><td class="py-2 pl-3">free</td><td class="py-2 text-right">contained</td></tr>
          <tr class="border-t border-tpop17-hair"><th scope="row" class="py-2 text-left font-semibold text-tpop17-mut">Rest of page</th><td class="py-2 pl-3">interactive</td><td class="py-2 text-right">inert</td></tr>
          <tr class="border-t border-tpop17-hair"><th scope="row" class="py-2 text-left font-semibold text-tpop17-mut">Backdrop</th><td class="py-2 pl-3">dismisses</td><td class="py-2 text-right">blocks</td></tr>
          <tr class="border-t border-tpop17-hair"><th scope="row" class="py-2 text-left font-semibold text-tpop17-mut">Escape</th><td class="py-2 pl-3">closes top one</td><td class="py-2 text-right">closes, cancelable</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div popover="auto" id="tpop-17-pop" role="group" aria-labelledby="tpop-17-pt" class="fixed m-auto w-[min(20rem,calc(100vw-28px))] border-2 border-tpop17-go bg-tpop17-surface p-4 text-tpop17-ink opacity-0 scale-[0.97] shadow-[6px_6px_0_oklch(0.44_0.08_165/0.22)] transition-[opacity,scale,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop17-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block,flip-inline] open:scale-100 open:opacity-100 starting:open:scale-[0.97] starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5">
    <p id="tpop-17-pt" class="mb-2 text-[11.5px] font-bold uppercase tracking-[0.14em]">Share this board</p>
    <p class="mb-3 text-[13.5px] leading-relaxed text-tpop17-mut text-pretty">Anyone with the link can comment. Keep working — I'm not in your way.</p>
    <label for="tpop-17-link" class="sr-only">Share link</label>
    <input id="tpop-17-link" readonly value="board.app/s/q3-close-4821" class="mb-3 min-h-11 w-full border border-tpop17-hair bg-tpop17-paper px-3 font-tpop17-mono text-[12.5px] text-tpop17-ink focus-visible:outline-3 focus-visible:-outline-offset-1 focus-visible:outline-tpop17-go">
    <p class="border-t border-tpop17-hair pt-2.5 text-[11.5px] font-semibold text-tpop17-go">popover · non-modal</p>
  </div>

  <dialog id="tpop-17-dialog" aria-labelledby="tpop-17-dt" class="m-auto w-[min(24rem,calc(100vw-32px))] border-2 border-tpop17-stop bg-tpop17-surface p-5 text-tpop17-ink opacity-0 scale-95 transition-[opacity,scale,display,overlay] duration-200 ease-out transition-discrete open:scale-100 open:opacity-100 starting:open:scale-95 starting:open:opacity-0 backdrop:bg-tpop17-ink/0 backdrop:transition-[background-color,display,overlay] backdrop:duration-200 backdrop:transition-discrete open:backdrop:bg-tpop17-ink/55 starting:open:backdrop:bg-tpop17-ink/0 motion-reduce:transition-none motion-reduce:backdrop:transition-none">
    <p id="tpop-17-dt" class="mb-2 font-tpop17-serif text-[26px] leading-tight">Delete workspace?</p>
    <p class="mb-4 text-[13.5px] leading-relaxed text-tpop17-mut text-pretty">This removes <strong class="font-semibold text-tpop17-ink">1,284 records</strong> and cannot be undone. You must answer before continuing.</p>
    <div class="flex flex-wrap gap-2">
      <button type="button" autofocus command="close" commandfor="tpop-17-dialog" class="min-h-11 min-w-0 flex-auto cursor-pointer border-2 border-tpop17-ink bg-tpop17-ink px-3.5 text-[13px] font-semibold text-tpop17-surface focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop17-go">Cancel</button>
      <button type="button" command="close" commandfor="tpop-17-dialog" class="min-h-11 min-w-0 flex-auto cursor-pointer border-2 border-tpop17-stop px-3.5 text-[13px] font-semibold text-tpop17-stop transition-colors hover:bg-tpop17-stop hover:text-tpop17-surface focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop17-stop">Delete</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop17-paper: #f5f3ed;
  --color-tpop17-paper: oklch(0.965 0.008 90);
  --color-tpop17-surface: #ffffff;
  --color-tpop17-surface: oklch(1 0 0);
  --color-tpop17-ink: #151410;
  --color-tpop17-ink: oklch(0.19 0.008 90);
  --color-tpop17-mut: #5f5a51;
  --color-tpop17-mut: oklch(0.47 0.015 85);
  --color-tpop17-hair: #dedad2;
  --color-tpop17-hair: oklch(0.89 0.012 85);
  --color-tpop17-go: #1b6047;
  --color-tpop17-go: oklch(0.44 0.08 165);
  --color-tpop17-stop: #9d2f19;
  --color-tpop17-stop: oklch(0.47 0.15 33);
  --font-tpop17-serif: 'Instrument Serif', Georgia, serif;
  --font-tpop17-sans: 'Geist', system-ui, sans-serif;
  --font-tpop17-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop17-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-17 {
  width: 100%;
  min-height: 100svh;
  --color-tpop17-paper: color-mix(in oklch, oklch(0.16 0.008 85) calc(var(--tpop17-d) * 100%), oklch(0.965 0.008 90));
  --color-tpop17-surface: color-mix(in oklch, oklch(0.205 0.01 85) calc(var(--tpop17-d) * 100%), oklch(1 0 0));
  --color-tpop17-ink: color-mix(in oklch, oklch(0.95 0.01 90) calc(var(--tpop17-d) * 100%), oklch(0.19 0.008 90));
  --color-tpop17-mut: color-mix(in oklch, oklch(0.73 0.015 85) calc(var(--tpop17-d) * 100%), oklch(0.47 0.015 85));
  --color-tpop17-hair: color-mix(in oklch, oklch(0.3 0.012 85) calc(var(--tpop17-d) * 100%), oklch(0.89 0.012 85));
  --color-tpop17-go: color-mix(in oklch, oklch(0.76 0.1 165) calc(var(--tpop17-d) * 100%), oklch(0.44 0.08 165));
  --color-tpop17-stop: color-mix(in oklch, oklch(0.74 0.14 33) calc(var(--tpop17-d) * 100%), oklch(0.47 0.15 33));
}
```
