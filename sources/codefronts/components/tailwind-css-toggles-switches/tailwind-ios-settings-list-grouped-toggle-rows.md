---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-settings-list-grouped-toggle-rows/"
title: "Tailwind iOS Settings List with Grouped Toggle Rows"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The whole iOS Settings context, not just the switch: a grouped light list with inset hairlines, coloured glyph tiles and three native-geometry toggles…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind iOS Settings List with Grouped Toggle Rows
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-settings-list-grouped-toggle-rows/

The whole iOS Settings context, not just the switch: a grouped light list with inset hairlines, coloured glyph tiles and three native-geometry toggles &mdash; the pattern to copy when you need an entire preferences screen, section header and footnote included.
## HTML
```html
<section class="ttg-23 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg23-bg font-ttg23-sans" aria-label="iOS settings list with toggles">
  <div class="w-[min(370px,100%)]">
    <p class="mx-4 mb-2 text-[13px] uppercase tracking-[0.05em] text-ttg23-mute">Notifications</p>
    <div class="rounded-xl bg-white overflow-hidden">
      <label style="--g:oklch(0.62 0.22 27)" class="relative flex items-center gap-3 h-13 px-4 cursor-pointer transition-colors duration-150 hover:bg-ttg23-tint not-last:after:content-[''] not-last:after:absolute not-last:after:left-[58px] not-last:after:right-0 not-last:after:bottom-0 not-last:after:h-px not-last:after:bg-ttg23-hair">
        <span aria-hidden="true" class="shrink-0 grid place-items-center w-7.5 h-7.5 rounded-[7px] bg-(--g) text-white text-[15px]">&#9687;</span>
        <span class="flex-1 text-[16px] text-ttg23-ink">Allow Notifications</span>
        <input type="checkbox" role="switch" checked aria-label="Allow Notifications" class="appearance-none shrink-0 w-[51px] h-[31px] rounded-2xl bg-ttg23-off relative cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[27px] before:h-[27px] before:rounded-full before:bg-white before:shadow-[0_3px_8px_oklch(0_0_0/0.15),0_1px_1px_oklch(0_0_0/0.16)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.2,0.9,0.25,1.05)] checked:bg-ttg23-on checked:before:translate-x-5 focus-visible:outline-3 focus-visible:outline-ttg23-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
      </label>
      <label style="--g:oklch(0.58 0.2 258)" class="relative flex items-center gap-3 h-13 px-4 cursor-pointer transition-colors duration-150 hover:bg-ttg23-tint not-last:after:content-[''] not-last:after:absolute not-last:after:left-[58px] not-last:after:right-0 not-last:after:bottom-0 not-last:after:h-px not-last:after:bg-ttg23-hair">
        <span aria-hidden="true" class="shrink-0 grid place-items-center w-7.5 h-7.5 rounded-[7px] bg-(--g) text-white text-[15px]">&#9677;</span>
        <span class="flex-1 text-[16px] text-ttg23-ink">Time Sensitive</span>
        <input type="checkbox" role="switch" checked aria-label="Time Sensitive" class="appearance-none shrink-0 w-[51px] h-[31px] rounded-2xl bg-ttg23-off relative cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[27px] before:h-[27px] before:rounded-full before:bg-white before:shadow-[0_3px_8px_oklch(0_0_0/0.15),0_1px_1px_oklch(0_0_0/0.16)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.2,0.9,0.25,1.05)] checked:bg-ttg23-on checked:before:translate-x-5 focus-visible:outline-3 focus-visible:outline-ttg23-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
      </label>
      <label style="--g:oklch(0.6 0.2 310)" class="relative flex items-center gap-3 h-13 px-4 cursor-pointer transition-colors duration-150 hover:bg-ttg23-tint">
        <span aria-hidden="true" class="shrink-0 grid place-items-center w-7.5 h-7.5 rounded-[7px] bg-(--g) text-white text-[15px]">&#9684;</span>
        <span class="flex-1 text-[16px] text-ttg23-ink">Scheduled Summary</span>
        <input type="checkbox" role="switch" aria-label="Scheduled Summary" class="appearance-none shrink-0 w-[51px] h-[31px] rounded-2xl bg-ttg23-off relative cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[27px] before:h-[27px] before:rounded-full before:bg-white before:shadow-[0_3px_8px_oklch(0_0_0/0.15),0_1px_1px_oklch(0_0_0/0.16)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.2,0.9,0.25,1.05)] checked:bg-ttg23-on checked:before:translate-x-5 focus-visible:outline-3 focus-visible:outline-ttg23-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
      </label>
    </div>
    <p class="mx-4 mt-2 text-[13px] leading-[1.45] text-ttg23-mute">Time Sensitive notifications are delivered immediately and stay on the Lock Screen for an hour.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg23-bg: #f1f1f6;
  --color-ttg23-bg: oklch(0.96 0.004 285);
  --color-ttg23-tint: #f8f8fb;
  --color-ttg23-tint: oklch(0.98 0.003 285);
  --color-ttg23-hair: #c8c8cc;
  --color-ttg23-hair: oklch(0.83 0.004 285);
  --color-ttg23-ink: #0b0b0d;
  --color-ttg23-ink: oklch(0.15 0.004 285);
  --color-ttg23-mute: #62626a;
  --color-ttg23-mute: oklch(0.51 0.008 285);
  --color-ttg23-off: #e6e6ea;
  --color-ttg23-off: oklch(0.93 0.003 285);
  --color-ttg23-on: #2fbf5b;
  --color-ttg23-on: oklch(0.72 0.18 149);
  --color-ttg23-focus: #0a84ff;
  --color-ttg23-focus: oklch(0.62 0.2 256);
  --font-ttg23-sans: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif;
}

.ttg-23 {
  width: 100%;
  min-height: 100svh;
}

.ttg-23 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
