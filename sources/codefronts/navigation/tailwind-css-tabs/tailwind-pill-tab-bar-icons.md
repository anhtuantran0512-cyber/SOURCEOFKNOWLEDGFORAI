---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/tailwind-pill-tab-bar-icons/"
title: "Tailwind Pill Tab Bar with Icons"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A dark capsule of icon tabs; the active one becomes a hot-pink pill that grows to make room for its label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pill Tab Bar with Icons
Source: https://codefronts.com/navigation/tailwind-css-tabs/tailwind-pill-tab-bar-icons/

A dark capsule of icon tabs; the active one becomes a hot-pink pill that grows to make room for its label. Flex growth, icon scale and label reveal share one spring curve. The port gives the pill a soft pink bloom and keeps every collapsed label in the accessibility tree.
## HTML
```html
<section class="ttb-25 grid min-h-svh w-full place-items-center bg-ttb25-bg px-5 py-14 font-ttb25-sans text-ttb25-paper" aria-label="Pill tab bar with icons demo">
  <div class="grid w-full max-w-md justify-items-center gap-8">
    <div role="radiogroup" aria-label="Library" class="flex w-full gap-1.5 rounded-full bg-white/[0.04] p-1.5 ring-1 ring-white/8">
      <label class="group/tab flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-bold text-ttb25-mut transition-[flex-grow,background-color,color,box-shadow] duration-450 ease-[cubic-bezier(0.34,1.4,0.5,1)] hover:text-ttb25-paper has-checked:flex-[2.4] has-checked:bg-ttb25-pink has-checked:text-ttb25-ink has-checked:shadow-[0_6px_18px_-6px_color-mix(in_oklab,var(--color-ttb25-pink)_70%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb25-pink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb25" id="ttb25-r1" checked><svg aria-hidden="true" class="size-[18px] flex-none transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8M5 9.5V20h5v-6h4v6h5V9.5"/></svg><span class="max-w-0 overflow-hidden whitespace-nowrap transition-[max-width] delay-50 duration-450 group-has-checked/tab:max-w-24 motion-reduce:transition-none">Home</span></label>
      <label class="group/tab flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-bold text-ttb25-mut transition-[flex-grow,background-color,color,box-shadow] duration-450 ease-[cubic-bezier(0.34,1.4,0.5,1)] hover:text-ttb25-paper has-checked:flex-[2.4] has-checked:bg-ttb25-pink has-checked:text-ttb25-ink has-checked:shadow-[0_6px_18px_-6px_color-mix(in_oklab,var(--color-ttb25-pink)_70%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb25-pink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb25" id="ttb25-r2"><svg aria-hidden="true" class="size-[18px] flex-none transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/></svg><span class="max-w-0 overflow-hidden whitespace-nowrap transition-[max-width] delay-50 duration-450 group-has-checked/tab:max-w-24 motion-reduce:transition-none">Search</span></label>
      <label class="group/tab flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-bold text-ttb25-mut transition-[flex-grow,background-color,color,box-shadow] duration-450 ease-[cubic-bezier(0.34,1.4,0.5,1)] hover:text-ttb25-paper has-checked:flex-[2.4] has-checked:bg-ttb25-pink has-checked:text-ttb25-ink has-checked:shadow-[0_6px_18px_-6px_color-mix(in_oklab,var(--color-ttb25-pink)_70%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb25-pink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb25" id="ttb25-r3"><svg aria-hidden="true" class="size-[18px] flex-none transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M6 3h12v18l-6-4-6 4z"/></svg><span class="max-w-0 overflow-hidden whitespace-nowrap transition-[max-width] delay-50 duration-450 group-has-checked/tab:max-w-24 motion-reduce:transition-none">Saved</span></label>
      <label class="group/tab flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-bold text-ttb25-mut transition-[flex-grow,background-color,color,box-shadow] duration-450 ease-[cubic-bezier(0.34,1.4,0.5,1)] hover:text-ttb25-paper has-checked:flex-[2.4] has-checked:bg-ttb25-pink has-checked:text-ttb25-ink has-checked:shadow-[0_6px_18px_-6px_color-mix(in_oklab,var(--color-ttb25-pink)_70%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb25-pink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb25" id="ttb25-r4"><svg aria-hidden="true" class="size-[18px] flex-none transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 7-7h2a7 7 0 0 1 7 7v1"/></svg><span class="max-w-0 overflow-hidden whitespace-nowrap transition-[max-width] delay-50 duration-450 group-has-checked/tab:max-w-24 motion-reduce:transition-none">Profile</span></label>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb25-mono text-[11.5px] text-ttb25-mut">has-checked:flex-[2.4] · label max-w-0 → 24 · spring ease</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb25-bg: #1d2124;
  --color-ttb25-bg: oklch(0.245 0.008 240.2);
  --color-ttb25-paper: #ece6d4;
  --color-ttb25-paper: oklch(0.925 0.025 91.6);
  --color-ttb25-mut: #aaa598;
  --color-ttb25-mut: oklch(0.722 0.019 89.4);
  --color-ttb25-pink: #f0559f;
  --color-ttb25-pink: oklch(0.677 0.202 354.4);
  --color-ttb25-ink: #1a1a1a;
  --color-ttb25-ink: oklch(0.218 0 0);
  --font-ttb25-sans: 'Geist', system-ui, sans-serif;
  --font-ttb25-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-25 {
  width: 100%;
  min-height: 100svh;
}
```
