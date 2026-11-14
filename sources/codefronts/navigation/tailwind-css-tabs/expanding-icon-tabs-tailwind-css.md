---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/expanding-icon-tabs-tailwind-css/"
title: "Expanding Icon Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Compact icon-only tabs in a white pill; the active one fills rose and its label morphs in beside the icon."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expanding Icon Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/expanding-icon-tabs-tailwind-css/

Compact icon-only tabs in a white pill; the active one fills rose and its label morphs in beside the icon. The label animates max-w-0 → max-w-28 while the gap opens gap-0 → gap-2 on the same curve, so icon and text glide together. Inbox gains an unread badge.
## HTML
```html
<section class="ttb-10 grid min-h-svh w-full place-items-center bg-ttb10-bg px-5 py-14 font-ttb10-sans text-ttb10-ink" aria-label="Expanding icon tabs demo">
  <div class="grid justify-items-center gap-8">
    <div role="radiogroup" aria-label="Main navigation" class="flex gap-1.5 rounded-full bg-white p-1.5 shadow-[0_6px_20px_-6px_color-mix(in_oklab,var(--color-ttb10-acc)_30%,transparent)] ring-1 ring-black/5">
      <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-0 rounded-full px-3.5 text-ttb10-mut transition-[background-color,color,gap] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb10-acc-ink has-checked:gap-2 has-checked:bg-ttb10-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb10-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb10" id="ttb10-r1" checked><svg aria-hidden="true" class="size-[18px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8M5 9.5V20h5v-6h4v6h5V9.5"/></svg><span class="max-w-0 overflow-hidden text-[13px] font-bold whitespace-nowrap opacity-0 transition-[max-width,opacity] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/tab:max-w-28 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Home</span></label>
      <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-0 rounded-full px-3.5 text-ttb10-mut transition-[background-color,color,gap] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb10-acc-ink has-checked:gap-2 has-checked:bg-ttb10-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb10-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb10" id="ttb10-r2"><svg aria-hidden="true" class="size-[18px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/></svg><span class="max-w-0 overflow-hidden text-[13px] font-bold whitespace-nowrap opacity-0 transition-[max-width,opacity] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/tab:max-w-28 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Search</span></label>
      <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-0 rounded-full px-3.5 text-ttb10-mut transition-[background-color,color,gap] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb10-acc-ink has-checked:gap-2 has-checked:bg-ttb10-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb10-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb10" id="ttb10-r3"><svg aria-hidden="true" class="size-[18px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13h5l1.5 3h5L16 13h5M5 4h14l2 9v6H3v-6z"/></svg><span class="max-w-0 overflow-hidden text-[13px] font-bold whitespace-nowrap opacity-0 transition-[max-width,opacity] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/tab:max-w-28 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Inbox</span><span class="absolute top-1.5 right-2 grid size-4 place-items-center rounded-full bg-ttb10-acc text-[9.5px] font-extrabold text-white ring-2 ring-white transition-transform group-has-checked/tab:scale-0"><span class="sr-only">unread: </span>4</span></label>
      <label class="group/tab relative flex min-h-11 cursor-pointer items-center gap-0 rounded-full px-3.5 text-ttb10-mut transition-[background-color,color,gap] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb10-acc-ink has-checked:gap-2 has-checked:bg-ttb10-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb10-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb10" id="ttb10-r4"><svg aria-hidden="true" class="size-[18px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 7-7h2a7 7 0 0 1 7 7v1"/></svg><span class="max-w-0 overflow-hidden text-[13px] font-bold whitespace-nowrap opacity-0 transition-[max-width,opacity] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-checked/tab:max-w-28 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Profile</span></label>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/8 bg-white/70 px-3.5 py-2 font-ttb10-mono text-[11.5px] text-ttb10-mut">max-w-0 → max-w-28 · gap-0 → gap-2 · same curve</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb10-bg: #fbf3e8;
  --color-ttb10-bg: oklch(0.967 0.017 76.1);
  --color-ttb10-ink: #2a1d24;
  --color-ttb10-ink: oklch(0.250 0.024 345.4);
  --color-ttb10-mut: #74586a;
  --color-ttb10-mut: oklch(0.495 0.045 340.1);
  --color-ttb10-acc: #c93a76;
  --color-ttb10-acc: oklch(0.576 0.185 359.2);
  --color-ttb10-acc-ink: #a92c60;
  --color-ttb10-acc-ink: oklch(0.502 0.166 359.9);
  --font-ttb10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttb10-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-10 {
  width: 100%;
  min-height: 100svh;
}
```
