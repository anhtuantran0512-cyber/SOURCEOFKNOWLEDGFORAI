---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/toast-dismiss/"
title: "Tailwind Toast Notification Dismiss Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A success toast with a draining countdown bar that owns the clock: animate-tcb25-life shrinks it over 5s and animationend dismisses the toast — no duplicate…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toast Notification Dismiss Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/toast-dismiss/

A success toast with a draining countdown bar that owns the clock: animate-tcb25-life shrinks it over 5s and animationend dismisses the toast — no duplicate timer. Hover or keyboard focus pauses it with group-hover/toast:[animation-play-state:paused], satisfying WCAG 2.2.1 (Timing Adjustable). The × is a 40px padded target pulled into the corner with negative margins.
## HTML
```html
<section class="tcb-25 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb25-bg),var(--color-tcb25-bg2))] px-6 py-12 font-tcb25-sans" aria-label="Toast notification dismiss button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="grid w-full max-w-[23rem] justify-items-center gap-4">
      <div id="tcb-25-toast" role="status" class="group/toast relative flex w-full items-center gap-3 overflow-hidden rounded-[14px] border border-tcb25-line/60 bg-tcb25-card py-3.5 ps-4 pe-3 shadow-[0_20px_46px_-24px_rgb(0_0_0/0.85)] transition duration-300 data-leaving:translate-x-6 data-leaving:opacity-0 motion-reduce:transition-none">
        <span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-full bg-tcb25-edge/25 text-tcb25-edge"><svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m3.5 8.5 3 3 6-7"/></svg></span>
        <div class="flex min-w-0 flex-1 flex-col gap-0.5">
          <strong class="text-[13.5px] font-semibold text-tcb25-ink">Changes saved</strong>
          <span class="text-xs text-tcb25-mut">Hover or focus to pause the countdown</span>
        </div>
        <button id="tcb-25-close" type="button" aria-label="Dismiss notification" class="relative -my-2 grid size-11 flex-none cursor-pointer place-items-center rounded-[10px] transition-colors hover:bg-white/8 focus-visible:outline-[2.5px] focus-visible:-outline-offset-2 focus-visible:outline-tcb25-edge motion-reduce:transition-none">
          <span aria-hidden="true" class="relative block size-4 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb25-x after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb25-x"></span>
        </button>
        <span id="tcb-25-bar" aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[3px] origin-left bg-tcb25-edge animate-tcb25-life group-hover/toast:[animation-play-state:paused] group-focus-within/toast:[animation-play-state:paused] motion-reduce:[animation-duration:20s]"></span>
      </div>
      <button id="tcb-25-reset" type="button" hidden class="min-h-11 cursor-pointer px-2 text-[13px] font-medium text-tcb25-mut underline decoration-dashed underline-offset-4 hover:text-tcb25-ink focus-visible:outline-2 focus-visible:outline-tcb25-edge">Show toast again</button>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb25-mono text-[11.5px] text-tcb25-mut ring-1 ring-white/12">animate-tcb25-life · group-focus-within/toast:[animation-play-state:paused]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb25-bg: #1e2430;
  --color-tcb25-bg: oklch(0.23 0.02 250);
  --color-tcb25-bg2: #141922;
  --color-tcb25-bg2: oklch(0.17 0.015 250);
  --color-tcb25-card: #2a303c;
  --color-tcb25-card: oklch(0.28 0.02 250);
  --color-tcb25-line: #4a5160;
  --color-tcb25-line: oklch(0.4 0.02 250);
  --color-tcb25-ink: #eceef3;
  --color-tcb25-ink: oklch(0.94 0.01 250);
  --color-tcb25-mut: #a9afbb;
  --color-tcb25-mut: oklch(0.75 0.02 250);
  --color-tcb25-x: #c3c8d2;
  --color-tcb25-x: oklch(0.83 0.02 250);
  --color-tcb25-edge: #3fcf94;
  --color-tcb25-edge: oklch(0.76 0.15 160);
  --font-tcb25-sans: 'Geist', system-ui, sans-serif;
  --font-tcb25-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb25-life: tcb25-life 5s linear forwards;

  @keyframes tcb25-life {
    from {
      transform: scaleX(1);
    }

    to {
      transform: scaleX(0);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const toast = document.getElementById('tcb-25-toast');
  if (!toast || toast.dataset.wired) return;
  toast.dataset.wired = '1';
  const bar = document.getElementById('tcb-25-bar');
  const reset = document.getElementById('tcb-25-reset');
  const leave = () => {
    if (toast.hasAttribute('data-leaving')) return;
    toast.setAttribute('data-leaving', '');
    setTimeout(() => { toast.hidden = true; reset.hidden = false; reset.focus(); }, 300);
  };
  bar.addEventListener('animationend', leave);
  document.getElementById('tcb-25-close').addEventListener('click', leave);
  reset.addEventListener('click', () => {
    toast.hidden = false;
    toast.removeAttribute('data-leaving');
    reset.hidden = true;
    bar.style.animation = 'none';
    requestAnimationFrame(() => { bar.style.animation = ''; });
  });
})();
```
