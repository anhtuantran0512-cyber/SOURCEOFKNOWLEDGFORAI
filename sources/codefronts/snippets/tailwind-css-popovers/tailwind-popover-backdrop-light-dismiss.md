---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-backdrop-light-dismiss/"
title: "Tailwind Popover Backdrop and Light Dismiss"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Every popover gets a ::backdrop, and in Tailwind it is just the backdrop: variant — stack it as open:backdrop: and starting:open:backdrop: and the page dim…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Popover Backdrop and Light Dismiss
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-backdrop-light-dismiss/

Every popover gets a ::backdrop, and in Tailwind it is just the backdrop: variant — stack it as open:backdrop: and starting:open:backdrop: and the page dim fades with the panel. Light dismiss stays intact: the backdrop decorates, it does not shield, so a click on the dimmed page still closes an auto popover. The manual twin has the same dim and none of the dismissal.
## HTML
```html
<section class="tpop-05 transition-[--tpop05-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop05-d:1] [[data-theme=dark]_&]:[--tpop05-d:1] [[data-theme=light]_&]:[--tpop05-d:0] w-full min-h-svh bg-tpop05-paper px-4.5 py-10 font-tpop05-sans text-tpop05-ink" aria-label="Popover backdrop and light dismiss demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[32rem] rounded-2xl border border-tpop05-rule bg-tpop05-sheet px-5.5 pt-6.5 pb-5.5 shadow-[0_20px_50px_-36px_oklch(0.3_0.03_60/0.6)]">
      <p class="mb-2.5 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop05-acc">Settings · Workspace</p>
      <h2 class="mb-3 font-tpop05-serif text-[clamp(26px,5vw,34px)] font-medium leading-[1.1] tracking-[-0.015em]">Transfer ownership</h2>
      <p class="mb-5 text-[15px] leading-[1.7] text-tpop05-mut text-pretty">Ownership moves the billing contact and the audit trail with it. The workspace keeps its integrations. Sam Rivera will be notified by email.</p>
      <div class="flex flex-wrap gap-2.5">
        <button id="tpop-05-trigger" type="button" popovertarget="tpop-05-auto" class="min-h-11 cursor-pointer rounded-xl bg-tpop05-acc px-4 text-[13.5px] font-semibold text-tpop05-sheet transition-colors hover:bg-tpop05-acc/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop05-acc">Review transfer</button>
        <button type="button" popovertarget="tpop-05-manual" popovertargetaction="show" class="min-h-11 cursor-pointer rounded-xl border border-tpop05-acc px-4 text-[13.5px] font-semibold text-tpop05-acc transition-colors hover:bg-tpop05-acc/8 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop05-acc">Open sticky version</button>
      </div>
      <p class="mt-4 text-[12.5px] leading-relaxed text-tpop05-mut">The first dims and frosts the page, and still closes on an outside click. The second dims it and refuses.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-05-auto" role="group" aria-labelledby="tpop-05-t1" class="fixed inset-0 m-auto h-fit w-[min(23rem,calc(100vw-32px))] rounded-2xl border border-tpop05-rule bg-tpop05-sheet p-5 text-tpop05-ink opacity-0 scale-[0.97] shadow-[0_30px_60px_-28px_oklch(0.3_0.03_60/0.6)] transition-[opacity,scale,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-[0.97] backdrop:bg-tpop05-ink/0 backdrop:backdrop-blur-[3px] backdrop:transition-[background-color,display,overlay] backdrop:duration-200 backdrop:transition-discrete open:backdrop:bg-tpop05-ink/45 starting:open:backdrop:bg-tpop05-ink/0 motion-reduce:transition-none motion-reduce:backdrop:transition-none">
    <p id="tpop-05-t1" class="mb-2.5 text-[11px] font-bold uppercase tracking-[0.16em] text-tpop05-acc">Review transfer</p>
    <div class="mb-3.5 flex items-center gap-3">
      <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-tpop05-acc/12 text-[13px] font-bold text-tpop05-acc">AC</span>
      <p class="text-sm leading-relaxed text-tpop05-mut text-pretty"><strong class="font-semibold text-tpop05-ink">Alex Chen</strong> becomes owner. You keep admin. Two seats change price on the next invoice.</p>
    </div>
    <p class="border-t border-tpop05-rule pt-3 text-xs text-tpop05-mut">popover="auto" · click the dimmed page to dismiss</p>
  </div>

  <div popover="manual" id="tpop-05-manual" role="group" aria-labelledby="tpop-05-t2" class="fixed inset-0 m-auto h-fit w-[min(23rem,calc(100vw-32px))] rounded-2xl border-2 border-tpop05-acc bg-tpop05-sheet p-5 text-tpop05-ink opacity-0 scale-[0.97] shadow-[0_30px_60px_-28px_oklch(0.3_0.03_60/0.6)] transition-[opacity,scale,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-[0.97] backdrop:bg-tpop05-ink/0 backdrop:transition-[background-color,display,overlay] backdrop:duration-200 backdrop:transition-discrete open:backdrop:bg-tpop05-ink/45 starting:open:backdrop:bg-tpop05-ink/0 motion-reduce:transition-none motion-reduce:backdrop:transition-none">
    <p id="tpop-05-t2" class="mb-2.5 text-[11px] font-bold uppercase tracking-[0.16em] text-tpop05-acc">Sticky version</p>
    <p class="mb-3.5 text-sm leading-relaxed text-tpop05-mut text-pretty">Same backdrop, no dismissal. <kbd class="rounded-md border border-b-2 border-tpop05-rule px-1.5 py-0.5 text-[11px] text-tpop05-ink">Esc</kbd> does nothing here — manual popovers hand the whole job to you, so this needs a real button.</p>
    <button type="button" popovertarget="tpop-05-manual" popovertargetaction="hide" class="min-h-11 w-full cursor-pointer rounded-xl bg-tpop05-ink px-3.5 text-[13.5px] font-semibold text-tpop05-sheet transition-colors hover:bg-tpop05-ink/90 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop05-acc">Close panel</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop05-paper: #eee5d6;
  --color-tpop05-paper: oklch(0.925 0.022 80);
  --color-tpop05-sheet: #f9f5eb;
  --color-tpop05-sheet: oklch(0.97 0.014 85);
  --color-tpop05-ink: #312317;
  --color-tpop05-ink: oklch(0.27 0.03 65);
  --color-tpop05-mut: #675440;
  --color-tpop05-mut: oklch(0.46 0.04 70);
  --color-tpop05-rule: #d8ccb8;
  --color-tpop05-rule: oklch(0.85 0.03 80);
  --color-tpop05-acc: #7c4523;
  --color-tpop05-acc: oklch(0.45 0.09 50);
  --font-tpop05-serif: 'Newsreader', Georgia, serif;
  --font-tpop05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop05-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-05 {
  width: 100%;
  min-height: 100svh;
  --color-tpop05-paper: color-mix(in oklch, oklch(0.17 0.014 65) calc(var(--tpop05-d) * 100%), oklch(0.925 0.022 80));
  --color-tpop05-sheet: color-mix(in oklch, oklch(0.22 0.016 65) calc(var(--tpop05-d) * 100%), oklch(0.97 0.014 85));
  --color-tpop05-ink: color-mix(in oklch, oklch(0.94 0.016 80) calc(var(--tpop05-d) * 100%), oklch(0.27 0.03 65));
  --color-tpop05-mut: color-mix(in oklch, oklch(0.74 0.03 75) calc(var(--tpop05-d) * 100%), oklch(0.46 0.04 70));
  --color-tpop05-rule: color-mix(in oklch, oklch(0.33 0.02 65) calc(var(--tpop05-d) * 100%), oklch(0.85 0.03 80));
  --color-tpop05-acc: color-mix(in oklch, oklch(0.76 0.09 55) calc(var(--tpop05-d) * 100%), oklch(0.45 0.09 50));
}
```
