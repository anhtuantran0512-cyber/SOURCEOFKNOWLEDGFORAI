---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-tooltip-on-hover-and-focus/"
title: "Tailwind Tooltip on Hover and Focus"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Popover's built-in trigger is click, so hover and focus call showPopover()/hidePopover() themselves: a 150ms open delay for hover intent, instant close,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tooltip on Hover and Focus
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-tooltip-on-hover-and-focus/

Popover's built-in trigger is click, so hover and focus call showPopover()/hidePopover() themselves: a 150ms open delay for hover intent, instant close, instant open on keyboard focus. The bubble is popover="manual" so it never fights the auto stack. The port keeps the controller to twenty lines and moves every visual — the dotted term, the rise-in, the definition card — into utilities.
## HTML
```html
<section class="tpop-12 transition-[--tpop12-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop12-d:1] [[data-theme=dark]_&]:[--tpop12-d:1] [[data-theme=light]_&]:[--tpop12-d:0] w-full min-h-svh bg-tpop12-paper px-5 py-11 font-tpop12-serif text-tpop12-ink" aria-label="Tooltip on hover and focus demo">
  <div class="grid min-h-[calc(100svh-88px)] max-w-full place-items-center">
    <article class="w-full min-w-0 max-w-[32rem]">
      <p class="mb-3 font-tpop12-sans text-[10.5px] font-bold uppercase tracking-[0.22em] text-tpop12-acc">Field notes · Typesetting</p>
      <h2 class="mb-4.5 text-[clamp(30px,6.5vw,44px)] font-medium leading-[1.05] tracking-[-0.02em]">The measure of a column</h2>
      <p class="mb-4 text-[clamp(17px,3.6vw,19px)] leading-[1.72] text-pretty">Set a column too wide and the eye loses the return sweep; too narrow and hyphenation does the reading for you. The old compositors aimed for a
        <button id="tpop-12-trigger" type="button" aria-describedby="tpop-12-tip" class="inline cursor-help rounded-sm p-0 font-[inherit] text-tpop12-acc underline decoration-tpop12-acc/60 decoration-dotted decoration-2 underline-offset-[5px] transition-[text-decoration-color] [anchor-name:--tpop12-a] hover:decoration-tpop12-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tpop12-acc">measure</button>
        of sixty-six characters and were rarely wrong, which is why the figure survives in every style manual written since.</p>
      <p class="font-tpop12-sans text-[13px] leading-relaxed text-tpop12-mut">Hover the term, or tab to it. The hint appears after a short pause and leaves the moment you move on.</p>
    </article>
  </div>

  <div popover="manual" id="tpop-12-tip" role="tooltip" class="fixed m-auto w-[min(16.5rem,calc(100vw-28px))] rounded-lg bg-tpop12-ink px-3.5 py-2.5 font-tpop12-sans text-[13px] leading-normal text-tpop12-paper opacity-0 shadow-[0_14px_28px_-12px_oklch(0.2_0.01_80/0.45)] text-pretty transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop12-a] [position-area:block-start_center] [justify-self:anchor-center] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mb-2">
    <span class="mb-0.5 block font-tpop12-serif text-[15px] italic text-tpop12-paper">measure <span class="font-tpop12-sans text-[11px] not-italic text-tpop12-paper/70">n.</span></span>
    The number of characters, including spaces, on a single line of set text.
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop12-paper: #fcfaf6;
  --color-tpop12-paper: oklch(0.985 0.006 90);
  --color-tpop12-ink: #191816;
  --color-tpop12-ink: oklch(0.21 0.005 90);
  --color-tpop12-mut: #5f5a51;
  --color-tpop12-mut: oklch(0.47 0.015 85);
  --color-tpop12-acc: #932d1c;
  --color-tpop12-acc: oklch(0.45 0.14 32);
  --font-tpop12-serif: 'Newsreader', Georgia, serif;
  --font-tpop12-sans: 'Geist', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop12-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-12 {
  width: 100%;
  min-height: 100svh;
  --color-tpop12-paper: color-mix(in oklch, oklch(0.17 0.006 85) calc(var(--tpop12-d) * 100%), oklch(0.985 0.006 90));
  --color-tpop12-ink: color-mix(in oklch, oklch(0.95 0.01 90) calc(var(--tpop12-d) * 100%), oklch(0.21 0.005 90));
  --color-tpop12-mut: color-mix(in oklch, oklch(0.74 0.015 85) calc(var(--tpop12-d) * 100%), oklch(0.47 0.015 85));
  --color-tpop12-acc: color-mix(in oklch, oklch(0.74 0.12 35) calc(var(--tpop12-d) * 100%), oklch(0.45 0.14 32));
}
```

## JavaScript
```js
(() => {
  const trigger = document.getElementById('tpop-12-trigger');
  const tip = document.getElementById('tpop-12-tip');
  if (!trigger || !tip || trigger.dataset.wired || !HTMLElement.prototype.hasOwnProperty('popover')) return;
  trigger.dataset.wired = '1';
  let timer = 0;
  const open = (delay) => {
    clearTimeout(timer);
    timer = setTimeout(() => { if (!tip.matches(':popover-open')) tip.showPopover(); }, delay);
  };
  const close = () => {
    clearTimeout(timer);
    if (tip.matches(':popover-open')) tip.hidePopover();
  };
  trigger.addEventListener('pointerenter', () => open(150));
  trigger.addEventListener('pointerleave', close);
  trigger.addEventListener('focusin', () => open(0));
  trigger.addEventListener('focusout', close);
  trigger.addEventListener('click', () => open(0));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
})();
```
