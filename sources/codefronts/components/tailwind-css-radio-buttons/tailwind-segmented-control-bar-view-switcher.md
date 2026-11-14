---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-segmented-control-bar-view-switcher/"
title: "Tailwind Segmented Control Bar (View Switcher)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "List / Grid / Board switching done as a radio group: a flat toolbar of icon + label segments with a crisp underline that slides beneath the active view —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Control Bar (View Switcher)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-segmented-control-bar-view-switcher/

List / Grid / Board switching done as a radio group: a flat toolbar of icon + label segments with a crisp underline that slides beneath the active view — and, new in the port, a live preview that re-lays itself out as you switch. The underline is an after: on the bar moved by has-[label:nth-child(n)_input:checked]:after:translate-x-*.
## HTML
```html
<section class="trb-15 w-full min-h-svh grid place-items-center bg-trb15-bg px-6 py-14 font-trb15-sans text-trb15-ink" aria-label="Segmented control bar radio demo">
  <fieldset class="group/view grid w-full max-w-[26rem] justify-items-center gap-5">
    <legend class="mb-1 text-center text-2xl font-bold tracking-[-0.02em]">Project view</legend>
    <div class="relative grid w-full grid-cols-3 overflow-hidden rounded-xl border border-trb15-line bg-white shadow-trb15-bar after:absolute after:bottom-0 after:left-0 after:h-[3px] after:w-1/3 after:rounded-t-[3px] after:bg-trb15-acc after:transition-transform after:duration-300 after:ease-trb15-glide after:content-[''] has-[label:nth-child(2)_input:checked]:after:translate-x-full has-[label:nth-child(3)_input:checked]:after:translate-x-[200%] motion-reduce:after:transition-none [&>label+label]:border-l [&>label+label]:border-trb15-line">
      <label class="group relative flex min-h-12 cursor-pointer items-center justify-center gap-2 px-4 transition-colors hover:bg-trb15-hover has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb15-acc"><input type="radio" name="trb-15" value="list" class="sr-only" checked><svg class="size-[18px] text-trb15-icon transition-colors group-has-checked:text-trb15-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg><span class="text-sm font-semibold text-trb15-mut transition-colors group-has-checked:text-trb15-acc">List</span></label>
      <label class="group relative flex min-h-12 cursor-pointer items-center justify-center gap-2 px-4 transition-colors hover:bg-trb15-hover has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb15-acc"><input type="radio" name="trb-15" value="grid" class="sr-only"><svg class="size-[18px] text-trb15-icon transition-colors group-has-checked:text-trb15-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg><span class="text-sm font-semibold text-trb15-mut transition-colors group-has-checked:text-trb15-acc">Grid</span></label>
      <label class="group relative flex min-h-12 cursor-pointer items-center justify-center gap-2 px-4 transition-colors hover:bg-trb15-hover has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb15-acc"><input type="radio" name="trb-15" value="board" class="sr-only"><svg class="size-[18px] text-trb15-icon transition-colors group-has-checked:text-trb15-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3.5" y="3.5" width="5" height="17" rx="1.5"/><rect x="11" y="3.5" width="5" height="11" rx="1.5"/><rect x="18.5" y="3.5" width="2" height="7" rx="1"/></svg><span class="text-sm font-semibold text-trb15-mut transition-colors group-has-checked:text-trb15-acc">Board</span></label>
    </div>
    <div aria-hidden="true" class="grid w-full grid-cols-1 items-start gap-2 rounded-2xl border border-dashed border-trb15-line bg-white/60 p-3 group-has-[[value=grid]:checked]/view:grid-cols-3 group-has-[[value=board]:checked]/view:grid-cols-3 *:rounded-lg *:bg-trb15-block *:transition-[height] *:duration-300 *:h-7 group-has-[[value=grid]:checked]/view:*:h-16 motion-reduce:*:transition-none">
      <i></i><i></i><i></i><i class="group-has-[[value=board]:checked]/view:h-16"></i><i class="group-has-[[value=board]:checked]/view:h-10"></i><i class="group-has-[[value=board]:checked]/view:h-4"></i>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb15-bg: #f7f8fa;
  --color-trb15-bg: oklch(0.978 0.004 265);
  --color-trb15-ink: #1c2130;
  --color-trb15-ink: oklch(0.24 0.03 270);
  --color-trb15-mut: #5d6479;
  --color-trb15-mut: oklch(0.5 0.03 270);
  --color-trb15-icon: #7a8197;
  --color-trb15-icon: oklch(0.6 0.03 270);
  --color-trb15-line: #e4e6ee;
  --color-trb15-line: oklch(0.925 0.01 270);
  --color-trb15-hover: #f4f5f9;
  --color-trb15-hover: oklch(0.968 0.005 270);
  --color-trb15-block: #e6e9f4;
  --color-trb15-block: oklch(0.93 0.018 270);
  --color-trb15-acc: #3450d4;
  --color-trb15-acc: oklch(0.5 0.19 265);
  --shadow-trb15-bar: 0 1px 3px oklch(0.25 0.03 270 / 0.06);
  --ease-trb15-glide: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb15-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-15 {
  width: 100%;
  min-height: 100svh;
}
```
