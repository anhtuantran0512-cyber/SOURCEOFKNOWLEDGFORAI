---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-3d-rotating-cube-toggle/"
title: "Tailwind 3D Rotating Cube Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A solid object, not a card: two faces of a cube joined at a real edge, rotating 90&deg; so the switch has actual thickness."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Rotating Cube Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-3d-rotating-cube-toggle/

A solid object, not a card: two faces of a cube joined at a real edge, rotating 90&deg; so the switch has actual thickness. v4's translate-z-* makes this the first Tailwind version where a cube needs no custom CSS at all.
## HTML
```html
<section class="ttg-40 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg40-bg font-ttg40-sans" aria-label="3D cube toggle">
  <input type="checkbox" id="ttg-40-sw" role="switch" aria-label="Deploy on push" class="peer sr-only">
  <label for="ttg-40-sw" class="block cursor-pointer perspective-[600px] peer-checked:[&_.ttg40-cube]:-rotate-x-90 peer-checked:[&_.ttg40-face-a]:opacity-0 peer-checked:[&_.ttg40-face-b]:opacity-100 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg40-focus peer-focus-visible:outline-offset-[6px] peer-focus-visible:rounded-2xl">
    <span aria-hidden="true" class="ttg40-cube relative grid w-[190px] h-16 transform-3d transition-transform duration-[560ms] ease-[cubic-bezier(0.4,0.15,0.2,1.05)] motion-reduce:duration-150">
      <span class="ttg40-face-a col-start-1 row-start-1 flex items-center justify-center gap-2.5 rounded-lg translate-z-[32px] transition-opacity duration-0 delay-[270ms] motion-reduce:delay-[70ms] bg-linear-160 from-ttg40-offhi to-ttg40-offlo text-ttg40-offink shadow-[inset_0_1px_0_oklch(1_0_0/0.5)]">
        <i class="not-italic w-2 h-2 rounded-full bg-ttg40-offink/50"></i>
        <b class="text-[15px] font-extrabold tracking-[0.16em]">MANUAL</b>
      </span>
      <span class="ttg40-face-b col-start-1 row-start-1 flex items-center justify-center gap-2.5 rounded-lg rotate-x-90 translate-z-[32px] opacity-0 transition-opacity duration-0 delay-[270ms] motion-reduce:delay-[70ms] bg-linear-160 from-ttg40-onhi to-ttg40-onlo text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.35)]">
        <i class="not-italic w-2 h-2 rounded-full bg-white"></i>
        <b class="text-[15px] font-extrabold tracking-[0.16em]">AUTO</b>
      </span>
    </span>
  </label>
  <span class="flex flex-col items-center gap-1 text-center">
    <b class="text-[15px] font-semibold text-ttg40-ink">Deploy on push</b>
    <span class="text-[12.5px] text-ttg40-mute">The control is a solid object &mdash; it turns, it does not flip</span>
  </span>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg40-bg: #eceef3;
  --color-ttg40-bg: oklch(0.95 0.006 265);
  --color-ttg40-offhi: #fbfbfd;
  --color-ttg40-offhi: oklch(0.98 0.003 265);
  --color-ttg40-offlo: #dcdfe8;
  --color-ttg40-offlo: oklch(0.9 0.008 265);
  --color-ttg40-offink: #4b5364;
  --color-ttg40-offink: oklch(0.44 0.02 265);
  --color-ttg40-onhi: #3d8ae8;
  --color-ttg40-onhi: oklch(0.62 0.17 250);
  --color-ttg40-onlo: #2a5fc4;
  --color-ttg40-onlo: oklch(0.5 0.18 260);
  --color-ttg40-ink: #212734;
  --color-ttg40-ink: oklch(0.27 0.015 265);
  --color-ttg40-mute: #7c8494;
  --color-ttg40-mute: oklch(0.6 0.018 265);
  --color-ttg40-focus: #3f63e0;
  --color-ttg40-focus: oklch(0.55 0.19 265);
  --font-ttg40-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-40 {
  width: 100%;
  min-height: 100svh;
}
```
