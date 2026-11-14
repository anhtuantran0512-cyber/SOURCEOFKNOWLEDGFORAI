---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-permission-toggle-group-has-live-status-badge/"
title: "Tailwind Permission Toggle Group with :has() Live Status Badge"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A settings card that reads its own children: a stack of permission rows, and a header badge that flips between Full access, Partial and No access purely by…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Permission Toggle Group with :has() Live Status Badge
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-permission-toggle-group-has-live-status-badge/

A settings card that reads its own children: a stack of permission rows, and a header badge that flips between Full access, Partial and No access purely by watching the group with :has(). This is the modern replacement for the classic "JavaScript counts the checkboxes" widget &mdash; a state machine that cannot desync from the DOM.
## HTML
```html
<section class="ttg-13 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg13-bg font-ttg13-sans" aria-label="Permission toggles with live status">
  <div class="w-[min(380px,100%)] rounded-[20px] bg-white overflow-hidden shadow-[0_24px_50px_-34px_oklch(0.4_0.04_265/0.6)] border border-ttg13-hair not-has-[input:not(:checked)]:[&_.ttg13-full]:inline-block has-[input:not(:checked)]:has-[input:checked]:[&_.ttg13-part]:inline-block not-has-[input:checked]:[&_.ttg13-none]:inline-block">
    <header class="flex items-center justify-between gap-4 px-5 py-4 border-b border-ttg13-hair">
      <b class="text-[16px] font-bold text-ttg13-ink">App permissions</b>
      <span aria-hidden="true" class="relative text-[11.5px] font-extrabold tracking-[0.04em]">
        <i class="ttg13-full not-italic hidden px-2.5 py-1 rounded-full bg-ttg13-okbg text-ttg13-okink">Full access</i>
        <i class="ttg13-part not-italic hidden px-2.5 py-1 rounded-full bg-ttg13-warnbg text-ttg13-warnink">Partial</i>
        <i class="ttg13-none not-italic hidden px-2.5 py-1 rounded-full bg-ttg13-offbg text-ttg13-offink">No access</i>
      </span>
    </header>
    <label class="flex items-center gap-5 min-h-16 px-5 py-3.5 cursor-pointer transition-colors duration-200 hover:bg-ttg13-tint has-checked:[&_.ttg13-t]:text-ttg13-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg13-t text-[14.5px] font-semibold text-ttg13-dim transition-colors duration-200">Camera</b>
        <small class="text-[12px] text-ttg13-mute">Photos &amp; video capture</small>
      </span>
      <input type="checkbox" role="switch" checked aria-label="Camera" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg13-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg13-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg13-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 min-h-16 px-5 py-3.5 cursor-pointer border-t border-ttg13-hair transition-colors duration-200 hover:bg-ttg13-tint has-checked:[&_.ttg13-t]:text-ttg13-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg13-t text-[14.5px] font-semibold text-ttg13-dim transition-colors duration-200">Microphone</b>
        <small class="text-[12px] text-ttg13-mute">Voice notes &amp; calls</small>
      </span>
      <input type="checkbox" role="switch" checked aria-label="Microphone" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg13-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg13-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg13-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 min-h-16 px-5 py-3.5 cursor-pointer border-t border-ttg13-hair transition-colors duration-200 hover:bg-ttg13-tint has-checked:[&_.ttg13-t]:text-ttg13-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg13-t text-[14.5px] font-semibold text-ttg13-dim transition-colors duration-200">Location</b>
        <small class="text-[12px] text-ttg13-mute">While using the app</small>
      </span>
      <input type="checkbox" role="switch" aria-label="Location" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg13-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg13-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg13-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg13-bg: #eceef4;
  --color-ttg13-bg: oklch(0.95 0.008 265);
  --color-ttg13-hair: #eaecf2;
  --color-ttg13-hair: oklch(0.94 0.006 265);
  --color-ttg13-tint: #f7f8fc;
  --color-ttg13-tint: oklch(0.98 0.004 265);
  --color-ttg13-ink: #1f2532;
  --color-ttg13-ink: oklch(0.26 0.015 265);
  --color-ttg13-dim: #737b8d;
  --color-ttg13-dim: oklch(0.58 0.018 265);
  --color-ttg13-mute: #8f97a7;
  --color-ttg13-mute: oklch(0.65 0.015 265);
  --color-ttg13-trackoff: #dfe2ea;
  --color-ttg13-trackoff: oklch(0.9 0.008 265);
  --color-ttg13-on: #2f9e63;
  --color-ttg13-on: oklch(0.63 0.16 155);
  --color-ttg13-okbg: #d4f2e0;
  --color-ttg13-okbg: oklch(0.92 0.07 155);
  --color-ttg13-okink: #1d6944;
  --color-ttg13-okink: oklch(0.44 0.11 155);
  --color-ttg13-warnbg: #fbeccd;
  --color-ttg13-warnbg: oklch(0.93 0.07 80);
  --color-ttg13-warnink: #7a5410;
  --color-ttg13-warnink: oklch(0.48 0.1 70);
  --color-ttg13-offbg: #e9ebf1;
  --color-ttg13-offbg: oklch(0.93 0.006 265);
  --color-ttg13-offink: #5d6478;
  --color-ttg13-offink: oklch(0.5 0.02 265);
  --color-ttg13-focus: #3f63e0;
  --color-ttg13-focus: oklch(0.55 0.19 265);
  --font-ttg13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-13 {
  width: 100%;
  min-height: 100svh;
}

.ttg-13 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
