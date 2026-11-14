---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/ios-segmented-control-tailwind-css/"
title: "iOS Segmented Control in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Apple's segmented control: a grey track, a white thumb that slides between segments, and the hairline dividers iOS draws between unselected segments."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS Segmented Control in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/ios-segmented-control-tailwind-css/

Apple's segmented control: a grey track, a white thumb that slides between segments, and the hairline dividers iOS draws between unselected segments. The port deletes the measuring script — the thumb moves with translate-x-[calc(var(--i)*100%)] — and adds the divider detail with an arbitrary sibling variant.
## HTML
```html
<section class="ttb-06 group/tabs grid min-h-svh w-full place-items-center bg-ttb06-bg px-5 py-14 font-ttb06-sans text-ttb06-ink" aria-label="iOS segmented control demo">
  <div class="grid w-full max-w-sm justify-items-center gap-7">
    <div class="w-full rounded-[22px] bg-white p-4 shadow-[0_1px_2px_rgb(0_0_0/0.04),0_12px_30px_-12px_rgb(0_0_0/0.15)]">
      <div role="radiogroup" aria-label="Calendar range" class="relative flex rounded-[9px] bg-ttb06-track p-0.5 [--i:0] has-[#ttb06-r2:checked]:[--i:1] has-[#ttb06-r3:checked]:[--i:2]">
        <label class="relative z-10 flex min-h-8 flex-1 cursor-pointer items-center justify-center rounded-[7px] text-[13px] font-medium transition-[font-weight] has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-ttb06-acc"><input class="sr-only" type="radio" name="ttb06" id="ttb06-r1" checked>Day</label>
        <label class="relative z-10 flex min-h-8 flex-1 cursor-pointer items-center justify-center rounded-[7px] text-[13px] font-medium transition-[font-weight] before:absolute before:inset-y-2 before:left-0 before:w-px before:bg-black/12 before:transition-opacity has-checked:font-semibold has-checked:before:opacity-0 has-focus-visible:outline-2 has-focus-visible:outline-ttb06-acc [:has(:checked)+&]:before:opacity-0"><input class="sr-only" type="radio" name="ttb06" id="ttb06-r2">Week</label>
        <label class="relative z-10 flex min-h-8 flex-1 cursor-pointer items-center justify-center rounded-[7px] text-[13px] font-medium transition-[font-weight] before:absolute before:inset-y-2 before:left-0 before:w-px before:bg-black/12 before:transition-opacity has-checked:font-semibold has-checked:before:opacity-0 has-focus-visible:outline-2 has-focus-visible:outline-ttb06-acc [:has(:checked)+&]:before:opacity-0"><input class="sr-only" type="radio" name="ttb06" id="ttb06-r3">Month</label>
        <span aria-hidden="true" class="pointer-events-none absolute inset-y-0.5 left-0.5 w-[calc((100%-4px)/3)] translate-x-[calc(var(--i)*100%)] rounded-[7px] bg-white shadow-[0_3px_8px_rgb(0_0_0/0.12),0_1px_1px_rgb(0_0_0/0.04)] ring-[0.5px] ring-black/4 transition-transform duration-[340ms] ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
      </div>
      <div class="mt-4 min-h-[88px]">
        <div class="hidden group-has-[#ttb06-r1:checked]/tabs:block"><p class="text-[22px] font-bold tracking-tight">Today</p><p class="mt-1 text-[15px] text-ttb06-mut">3 events · first at 9:30</p></div>
        <div class="hidden group-has-[#ttb06-r2:checked]/tabs:block"><p class="text-[22px] font-bold tracking-tight">This week</p><p class="mt-1 text-[15px] text-ttb06-mut">11 events across 5 days</p></div>
        <div class="hidden group-has-[#ttb06-r3:checked]/tabs:block"><p class="text-[22px] font-bold tracking-tight">This month</p><p class="mt-1 text-[15px] text-ttb06-mut">38 events · 4 all-day</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white px-3.5 py-2 font-ttb06-mono text-[11.5px] text-ttb06-mut shadow-sm">CSS thumb · [:has(:checked)+&amp;]:before:opacity-0 dividers</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb06-bg: #f2f2f7;
  --color-ttb06-bg: oklch(0.963 0.007 286.3);
  --color-ttb06-track: #e3e3e8;
  --color-ttb06-track: oklch(0.917 0.007 286.3);
  --color-ttb06-ink: #1c1c1e;
  --color-ttb06-ink: oklch(0.227 0.004 286.1);
  --color-ttb06-mut: #636366;
  --color-ttb06-mut: oklch(0.501 0.005 286.2);
  --color-ttb06-acc: #007aff;
  --color-ttb06-acc: oklch(0.603 0.218 257.4);
  --font-ttb06-sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif;
  --font-ttb06-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-06 {
  width: 100%;
  min-height: 100svh;
}
```
