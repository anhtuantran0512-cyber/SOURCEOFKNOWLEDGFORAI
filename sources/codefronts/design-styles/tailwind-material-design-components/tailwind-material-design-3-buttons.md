---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-3-buttons/"
title: "Tailwind Material Design 3 Buttons"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Every Material 3 button in one stage &mdash; filled, tonal, elevated, outlined, text, four FAB sizes, four icon-button flavours and a segmented group &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design 3 Buttons
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-3-buttons/

Every Material 3 button in one stage &mdash; filled, tonal, elevated, outlined, text, four FAB sizes, four icon-button flavours and a segmented group &mdash; and the port replaces Material's twenty .btn--x blocks with one class list per variant. The M3 state layer is the interesting part: it is a before: pseudo-element at bg-current, and hover/focus/active are just three opacity variants on the same element.
## HTML
```html
<section class="tmd-01 w-full min-h-svh bg-tmd01-bg font-tmd01-sans text-tmd01-onsurface px-5 py-9" aria-label="Material Design 3 buttons demo">
  <div class="w-[min(1040px,100%)] mx-auto grid gap-7">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Material Design 3 buttons</h2>
      <p class="text-sm text-tmd01-onvariant">Five container variants, four FAB sizes, four icon flavours and a segmented group &mdash; utilities only, no JavaScript.</p>
    </header>

    <div class="grid gap-3.5 p-5.5 rounded-3xl bg-tmd01-surface shadow-tmd01-1">
      <span class="font-tmd01-mono text-[11px] uppercase tracking-[0.1em] text-tmd01-onvariant">Common buttons</span>
      <div class="flex flex-wrap gap-3">
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 cursor-pointer bg-tmd01-primary text-tmd01-onprimary text-sm font-medium tracking-[0.01em] transition-shadow duration-200 hover:shadow-tmd01-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] focus-visible:before:opacity-[0.1] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">rocket_launch</span>Filled</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 cursor-pointer bg-tmd01-secondarycontainer text-tmd01-onsecondarycontainer text-sm font-medium tracking-[0.01em] transition-shadow duration-200 hover:shadow-tmd01-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] focus-visible:before:opacity-[0.1] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">bookmark</span>Tonal</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 cursor-pointer bg-tmd01-surface text-tmd01-primary text-sm font-medium tracking-[0.01em] shadow-tmd01-1 transition-shadow duration-200 hover:shadow-tmd01-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] focus-visible:before:opacity-[0.1] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">layers</span>Elevated</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full cursor-pointer bg-transparent border border-tmd01-outline text-tmd01-primary text-sm font-medium tracking-[0.01em] transition-colors duration-200 hover:border-tmd01-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] focus-visible:before:opacity-[0.1] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">favorite</span>Outlined</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-3 rounded-full border-0 cursor-pointer bg-transparent text-tmd01-primary text-sm font-medium tracking-[0.01em] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] focus-visible:before:opacity-[0.1] active:before:opacity-[0.12]">Text</button>
        <button type="button" disabled class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 bg-tmd01-onsurface/12 text-tmd01-onsurface text-sm font-medium tracking-[0.01em] opacity-38 cursor-not-allowed before:absolute before:inset-0 before:bg-current before:opacity-0 disabled:before:hidden">Disabled</button>
      </div>
    </div>

    <div class="grid gap-3.5 p-5.5 rounded-3xl bg-tmd01-surface shadow-tmd01-1">
      <span class="font-tmd01-mono text-[11px] uppercase tracking-[0.1em] text-tmd01-onvariant">Floating action buttons</span>
      <div class="flex flex-wrap items-center gap-4">
        <button type="button" aria-label="Create, small" class="relative overflow-hidden grid place-items-center w-11 h-11 rounded-xl border-0 cursor-pointer bg-tmd01-primarycontainer text-tmd01-onprimarycontainer shadow-tmd01-2 transition-shadow duration-200 hover:shadow-tmd01-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">add</span></button>
        <button type="button" aria-label="Create" class="relative overflow-hidden grid place-items-center w-14 h-14 rounded-2xl border-0 cursor-pointer bg-tmd01-primarycontainer text-tmd01-onprimarycontainer shadow-tmd01-3 transition-shadow duration-200 hover:shadow-tmd01-4 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[26px] leading-none" aria-hidden="true">edit</span></button>
        <button type="button" aria-label="Create, large" class="relative overflow-hidden grid place-items-center w-24 h-24 rounded-[28px] border-0 cursor-pointer bg-tmd01-tertiarycontainer text-tmd01-ontertiarycontainer shadow-tmd01-3 transition-shadow duration-200 hover:shadow-tmd01-4 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[36px] leading-none" aria-hidden="true">photo_camera</span></button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-3 h-14 px-5 rounded-2xl border-0 cursor-pointer bg-tmd01-primarycontainer text-tmd01-onprimarycontainer text-sm font-medium shadow-tmd01-3 transition-shadow duration-200 hover:shadow-tmd01-4 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12] motion-reduce:transition-none"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">create</span>Compose</button>
      </div>
    </div>

    <div class="grid gap-3.5 p-5.5 rounded-3xl bg-tmd01-surface shadow-tmd01-1">
      <span class="font-tmd01-mono text-[11px] uppercase tracking-[0.1em] text-tmd01-onvariant">Icon buttons &amp; toggles</span>
      <div class="flex flex-wrap items-center gap-2.5">
        <button type="button" aria-label="Add to favourites" aria-pressed="false" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 cursor-pointer bg-transparent text-tmd01-onvariant transition-colors duration-150 aria-pressed:text-tmd01-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">favorite</span></button>
        <button type="button" aria-label="Save" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 cursor-pointer bg-tmd01-primary text-tmd01-onprimary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">bookmark</span></button>
        <button type="button" aria-label="Edit" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 cursor-pointer bg-tmd01-secondarycontainer text-tmd01-onsecondarycontainer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">edit</span></button>
        <button type="button" aria-label="Share" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full cursor-pointer bg-transparent border border-tmd01-outlinevariant text-tmd01-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd01-icon text-[22px] leading-none" aria-hidden="true">ios_share</span></button>
      </div>
    </div>

    <div class="grid gap-3.5 p-5.5 rounded-3xl bg-tmd01-surface shadow-tmd01-1">
      <span class="font-tmd01-mono text-[11px] uppercase tracking-[0.1em] text-tmd01-onvariant">Segmented button &mdash; peer-checked, zero JS</span>
      <fieldset class="border-0 p-0 m-0">
        <legend class="sr-only">Choose a view</legend>
        <div class="inline-flex rounded-full border border-tmd01-outline overflow-hidden">
          <input type="radio" name="tmd01-view" id="tmd01-view-list" class="peer/list sr-only" checked>
          <label for="tmd01-view-list" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-5 cursor-pointer text-sm font-medium text-tmd01-onsurface border-r border-tmd01-outline transition-colors duration-150 peer-checked/list:bg-tmd01-secondarycontainer peer-checked/list:text-tmd01-onsecondarycontainer peer-focus-visible/list:outline-2 peer-focus-visible/list:-outline-offset-2 peer-focus-visible/list:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08]"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">format_list_bulleted</span>List</label>
          <input type="radio" name="tmd01-view" id="tmd01-view-grid" class="peer/grid sr-only">
          <label for="tmd01-view-grid" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-5 cursor-pointer text-sm font-medium text-tmd01-onsurface border-r border-tmd01-outline transition-colors duration-150 peer-checked/grid:bg-tmd01-secondarycontainer peer-checked/grid:text-tmd01-onsecondarycontainer peer-focus-visible/grid:outline-2 peer-focus-visible/grid:-outline-offset-2 peer-focus-visible/grid:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08]"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">grid_view</span>Grid</label>
          <input type="radio" name="tmd01-view" id="tmd01-view-chart" class="peer/chart sr-only">
          <label for="tmd01-view-chart" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-5 cursor-pointer text-sm font-medium text-tmd01-onsurface transition-colors duration-150 peer-checked/chart:bg-tmd01-secondarycontainer peer-checked/chart:text-tmd01-onsecondarycontainer peer-focus-visible/chart:outline-2 peer-focus-visible/chart:-outline-offset-2 peer-focus-visible/chart:outline-tmd01-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-150 hover:before:opacity-[0.08]"><span class="font-tmd01-icon text-[18px] leading-none" aria-hidden="true">bar_chart</span>Insights</label>
        </div>
      </fieldset>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd01-bg: #f4eff7;
  --color-tmd01-bg: oklch(0.958 0.012 313.2);
  --color-tmd01-surface: #fffbfe;
  --color-tmd01-surface: oklch(0.992 0.006 334);
  --color-tmd01-primary: #6750a4;
  --color-tmd01-primary: oklch(0.496 0.13 293.7);
  --color-tmd01-onprimary: #ffffff;
  --color-tmd01-onprimary: oklch(1 0 89.9);
  --color-tmd01-primarycontainer: #eaddff;
  --color-tmd01-primarycontainer: oklch(0.918 0.048 302.8);
  --color-tmd01-onprimarycontainer: #21005d;
  --color-tmd01-onprimarycontainer: oklch(0.242 0.14 286.1);
  --color-tmd01-secondarycontainer: #e8def8;
  --color-tmd01-secondarycontainer: oklch(0.916 0.037 303.1);
  --color-tmd01-onsecondarycontainer: #1d192b;
  --color-tmd01-onsecondarycontainer: oklch(0.227 0.035 293.7);
  --color-tmd01-tertiarycontainer: #ffd8e4;
  --color-tmd01-tertiarycontainer: oklch(0.918 0.046 357.6);
  --color-tmd01-ontertiarycontainer: #31111d;
  --color-tmd01-ontertiarycontainer: oklch(0.232 0.054 358.6);
  --color-tmd01-onsurface: #1c1b1f;
  --color-tmd01-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd01-onvariant: #49454f;
  --color-tmd01-onvariant: oklch(0.398 0.017 303.7);
  --color-tmd01-outline: #79747e;
  --color-tmd01-outline: oklch(0.567 0.016 308.1);
  --color-tmd01-outlinevariant: #cac4d0;
  --color-tmd01-outlinevariant: oklch(0.829 0.018 308.2);
  --font-tmd01-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd01-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd01-icon: 'Material Symbols Outlined';
  --shadow-tmd01-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
  --shadow-tmd01-2: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 2px 6px 2px rgb(0 0 0 / 0.15);
  --shadow-tmd01-3: 0 4px 8px 3px rgb(0 0 0 / 0.15), 0 1px 3px 0 rgb(0 0 0 / 0.3);
  --shadow-tmd01-4: 0 6px 10px 4px rgb(0 0 0 / 0.15), 0 2px 3px 0 rgb(0 0 0 / 0.3);
  --shadow-tmd01-5: 0 8px 12px 6px rgb(0 0 0 / 0.15), 0 4px 4px 0 rgb(0 0 0 / 0.3);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tmd-01 {
  width: 100%;
  min-height: 100svh;
}
/* Material Symbols needs its ligature and axis setup, which is font plumbing rather
   than a design-scale value — the only rule utilities cannot express here. */

.tmd-01 [class*="font-tmd01-icon"] {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  font-feature-settings: 'liga';
}
```
