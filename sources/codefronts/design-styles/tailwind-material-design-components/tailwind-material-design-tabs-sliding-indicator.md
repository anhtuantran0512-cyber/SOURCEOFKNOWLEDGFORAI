---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-tabs-sliding-indicator/"
title: "Tailwind Material Design Tabs with Sliding Indicator"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Primary tabs with a single sliding indicator, scrollable tabs with snap, and icon-and-label tabs &mdash; all zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Tabs with Sliding Indicator
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-tabs-sliding-indicator/

Primary tabs with a single sliding indicator, scrollable tabs with snap, and icon-and-label tabs &mdash; all zero JavaScript. The indicator is the interesting port: instead of four ::after rules, one absolutely-positioned bar reads an index custom property set by has-checked:, so it glides between tabs and any number of tabs needs no new rule.
## HTML
```html
<section class="tmd-07 w-full min-h-svh bg-tmd07-bg font-tmd07-sans text-tmd07-onsurface px-5 py-9" aria-label="Material Design tabs demo">
  <div class="w-[min(900px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Tabs with a travelling indicator</h2>
      <p class="text-sm text-tmd07-onvariant">One indicator element, one index custom property, zero JavaScript.</p>
    </header>

    <div class="group/tabs rounded-3xl overflow-hidden bg-tmd07-surface shadow-tmd07-1">
      <div class="relative grid grid-cols-3 border-b border-tmd07-outlinevariant [--tab-i:0] has-[#tmd07-t1:checked]:[--tab-i:0] has-[#tmd07-t2:checked]:[--tab-i:1] has-[#tmd07-t3:checked]:[--tab-i:2]">
        <input type="radio" name="tmd07-primary" id="tmd07-t1" class="peer/t1 sr-only" checked>
        <label for="tmd07-t1" class="relative overflow-hidden grid place-items-center min-h-12 px-3 cursor-pointer text-sm font-medium text-tmd07-onvariant transition-colors duration-200 peer-checked/t1:text-tmd07-primary peer-focus-visible/t1:outline-2 peer-focus-visible/t1:-outline-offset-2 peer-focus-visible/t1:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Overview</label>
        <input type="radio" name="tmd07-primary" id="tmd07-t2" class="peer/t2 sr-only">
        <label for="tmd07-t2" class="relative overflow-hidden grid place-items-center min-h-12 px-3 cursor-pointer text-sm font-medium text-tmd07-onvariant transition-colors duration-200 peer-checked/t2:text-tmd07-primary peer-focus-visible/t2:outline-2 peer-focus-visible/t2:-outline-offset-2 peer-focus-visible/t2:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Readings</label>
        <input type="radio" name="tmd07-primary" id="tmd07-t3" class="peer/t3 sr-only">
        <label for="tmd07-t3" class="relative overflow-hidden grid place-items-center min-h-12 px-3 cursor-pointer text-sm font-medium text-tmd07-onvariant transition-colors duration-200 peer-checked/t3:text-tmd07-primary peer-focus-visible/t3:outline-2 peer-focus-visible/t3:-outline-offset-2 peer-focus-visible/t3:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Notes</label>
        <span class="absolute bottom-0 left-0 w-1/3 h-0.75 rounded-t-sm bg-tmd07-primary pointer-events-none [transform:translateX(calc(var(--tab-i)*100%))] transition-transform duration-250 ease-out motion-reduce:transition-none" aria-hidden="true"></span>
      </div>
      <div class="p-5">
        <div class="hidden gap-2 group-has-[#tmd07-t1:checked]/tabs:grid">
          <h3 class="text-lg font-medium">Overview</h3>
          <p class="text-sm leading-6 text-tmd07-onvariant text-pretty">Eighteen stations reporting. The indicator you just moved is a single <span class="font-tmd07-mono text-[12px]">&lt;span&gt;</span> translated by an index &mdash; add a fourth tab and it keeps working.</p>
        </div>
        <div class="hidden gap-2 group-has-[#tmd07-t2:checked]/tabs:grid">
          <h3 class="text-lg font-medium">Readings</h3>
          <p class="text-sm leading-6 text-tmd07-onvariant text-pretty">Panels are <span class="font-tmd07-mono text-[12px]">hidden</span> until their radio is checked, so find-in-page only reaches the visible one.</p>
        </div>
        <div class="hidden gap-2 group-has-[#tmd07-t3:checked]/tabs:grid">
          <h3 class="text-lg font-medium">Notes</h3>
          <p class="text-sm leading-6 text-tmd07-onvariant text-pretty">Arrow-key traversal comes from the native radio group, which is why this pattern beats a <span class="font-tmd07-mono text-[12px]">div role=&quot;tab&quot;</span> rebuild.</p>
        </div>
      </div>
    </div>

    <div class="rounded-3xl overflow-hidden bg-tmd07-surface shadow-tmd07-1">
      <span class="block px-5 pt-4 font-tmd07-mono text-[11px] uppercase tracking-[0.1em] text-tmd07-onvariant">Scrollable tabs &middot; snap</span>
      <div class="flex gap-1 px-3 py-3 overflow-x-auto overscroll-x-contain snap-x snap-mandatory [scrollbar-width:none]">
        <input type="radio" name="tmd07-scroll" id="tmd07-s1" class="peer/s1 sr-only" checked>
        <label for="tmd07-s1" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s1:bg-tmd07-secondarycontainer peer-checked/s1:text-tmd07-onsecondarycontainer peer-checked/s1:border-transparent peer-focus-visible/s1:outline-2 peer-focus-visible/s1:outline-offset-2 peer-focus-visible/s1:outline-tmd07-primary">All stations</label>
        <input type="radio" name="tmd07-scroll" id="tmd07-s2" class="peer/s2 sr-only">
        <label for="tmd07-s2" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s2:bg-tmd07-secondarycontainer peer-checked/s2:text-tmd07-onsecondarycontainer peer-checked/s2:border-transparent peer-focus-visible/s2:outline-2 peer-focus-visible/s2:outline-offset-2 peer-focus-visible/s2:outline-tmd07-primary">North Atlantic</label>
        <input type="radio" name="tmd07-scroll" id="tmd07-s3" class="peer/s3 sr-only">
        <label for="tmd07-s3" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s3:bg-tmd07-secondarycontainer peer-checked/s3:text-tmd07-onsecondarycontainer peer-checked/s3:border-transparent peer-focus-visible/s3:outline-2 peer-focus-visible/s3:outline-offset-2 peer-focus-visible/s3:outline-tmd07-primary">Baltic</label>
        <input type="radio" name="tmd07-scroll" id="tmd07-s4" class="peer/s4 sr-only">
        <label for="tmd07-s4" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s4:bg-tmd07-secondarycontainer peer-checked/s4:text-tmd07-onsecondarycontainer peer-checked/s4:border-transparent peer-focus-visible/s4:outline-2 peer-focus-visible/s4:outline-offset-2 peer-focus-visible/s4:outline-tmd07-primary">Mediterranean</label>
        <input type="radio" name="tmd07-scroll" id="tmd07-s5" class="peer/s5 sr-only">
        <label for="tmd07-s5" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s5:bg-tmd07-secondarycontainer peer-checked/s5:text-tmd07-onsecondarycontainer peer-checked/s5:border-transparent peer-focus-visible/s5:outline-2 peer-focus-visible/s5:outline-offset-2 peer-focus-visible/s5:outline-tmd07-primary">Norwegian Sea</label>
        <input type="radio" name="tmd07-scroll" id="tmd07-s6" class="peer/s6 sr-only">
        <label for="tmd07-s6" class="snap-start shrink-0 relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd07-onvariant border border-tmd07-outlinevariant transition-colors duration-200 peer-checked/s6:bg-tmd07-secondarycontainer peer-checked/s6:text-tmd07-onsecondarycontainer peer-checked/s6:border-transparent peer-focus-visible/s6:outline-2 peer-focus-visible/s6:outline-offset-2 peer-focus-visible/s6:outline-tmd07-primary">Irish Shelf</label>
      </div>
    </div>

    <div class="rounded-3xl overflow-hidden bg-tmd07-surface shadow-tmd07-1">
      <span class="block px-5 pt-4 font-tmd07-mono text-[11px] uppercase tracking-[0.1em] text-tmd07-onvariant">Icon + label tabs</span>
      <div class="relative grid grid-cols-3 mt-2 border-b border-tmd07-outlinevariant [--tab-i:0] has-[#tmd07-i1:checked]:[--tab-i:0] has-[#tmd07-i2:checked]:[--tab-i:1] has-[#tmd07-i3:checked]:[--tab-i:2]">
        <input type="radio" name="tmd07-icon" id="tmd07-i1" class="peer/i1 sr-only" checked>
        <label for="tmd07-i1" class="relative overflow-hidden grid justify-items-center gap-1 pt-2.5 pb-3 cursor-pointer text-xs font-medium text-tmd07-onvariant peer-checked/i1:text-tmd07-primary peer-focus-visible/i1:outline-2 peer-focus-visible/i1:-outline-offset-2 peer-focus-visible/i1:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd07-icon text-[22px] leading-none" aria-hidden="true">map</span>Map</label>
        <input type="radio" name="tmd07-icon" id="tmd07-i2" class="peer/i2 sr-only">
        <label for="tmd07-i2" class="relative overflow-hidden grid justify-items-center gap-1 pt-2.5 pb-3 cursor-pointer text-xs font-medium text-tmd07-onvariant peer-checked/i2:text-tmd07-primary peer-focus-visible/i2:outline-2 peer-focus-visible/i2:-outline-offset-2 peer-focus-visible/i2:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="relative font-tmd07-icon text-[22px] leading-none" aria-hidden="true">insights<b class="absolute -top-1 -right-3 min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd07-primary text-white font-tmd07-mono text-[10px] not-italic tabular-nums">4</b></span>Trends</label>
        <input type="radio" name="tmd07-icon" id="tmd07-i3" class="peer/i3 sr-only">
        <label for="tmd07-i3" class="relative overflow-hidden grid justify-items-center gap-1 pt-2.5 pb-3 cursor-pointer text-xs font-medium text-tmd07-onvariant peer-checked/i3:text-tmd07-primary peer-focus-visible/i3:outline-2 peer-focus-visible/i3:-outline-offset-2 peer-focus-visible/i3:outline-tmd07-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd07-icon text-[22px] leading-none" aria-hidden="true">download</span>Exports</label>
        <span class="absolute bottom-0 left-0 w-1/3 h-0.75 rounded-t-sm bg-tmd07-primary pointer-events-none [transform:translateX(calc(var(--tab-i)*100%))] transition-transform duration-250 ease-out motion-reduce:transition-none" aria-hidden="true"></span>
      </div>
      <p class="p-5 text-sm leading-6 text-tmd07-onvariant text-pretty">Icon tabs use the same indicator recipe. The badge is absolutely positioned on the glyph, so the label text never shifts when the count changes.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd07-bg: #f1f8e9;
  --color-tmd07-bg: oklch(0.97 0.021 127.4);
  --color-tmd07-surface: #ffffff;
  --color-tmd07-surface: oklch(1 0 89.9);
  --color-tmd07-primary: #2e7d32;
  --color-tmd07-primary: oklch(0.523 0.135 144.2);
  --color-tmd07-secondarycontainer: #d7f0d2;
  --color-tmd07-secondarycontainer: oklch(0.929 0.048 140.5);
  --color-tmd07-onsecondarycontainer: #0d2a10;
  --color-tmd07-onsecondarycontainer: oklch(0.255 0.059 145.6);
  --color-tmd07-onsurface: #1a1c19;
  --color-tmd07-onsurface: oklch(0.223 0.006 135);
  --color-tmd07-onvariant: #4a5348;
  --color-tmd07-onvariant: oklch(0.431 0.021 140);
  --color-tmd07-outlinevariant: #d3e0cd;
  --color-tmd07-outlinevariant: oklch(0.892 0.029 135.6);
  --font-tmd07-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd07-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd07-icon: 'Material Symbols Outlined';
  --shadow-tmd07-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-07 {
  width: 100%;
  min-height: 100svh;
}

.tmd-07 .font-tmd07-icon {
  font-feature-settings: 'liga';
}
/* Scrollbar removal on the scrollable strip: -webkit- shims have no utility form. */

.tmd-07 .overflow-x-auto::-webkit-scrollbar {
  display: none;
}
```
