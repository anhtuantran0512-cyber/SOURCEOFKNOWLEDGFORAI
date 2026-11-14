---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-3-cards/"
title: "Tailwind Material Design 3 Cards"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "The three M3 card containers &mdash; elevated, filled and outlined &mdash; plus a horizontal media card and a stat tile, laid out on a grid that reflows with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design 3 Cards
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-3-cards/

The three M3 card containers &mdash; elevated, filled and outlined &mdash; plus a horizontal media card and a stat tile, laid out on a grid that reflows with no media query. The port's real gain is group-hover:: the whole card is the hover target, so the title colour, the elevation and the media zoom all respond from one hovered ancestor instead of three descendant rules.
## HTML
```html
<section class="tmd-02 w-full min-h-svh bg-tmd02-bg font-tmd02-sans text-tmd02-onsurface px-5 py-9" aria-label="Material Design 3 cards demo">
  <div class="w-[min(1100px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Material Design 3 cards</h2>
      <p class="text-sm text-tmd02-onvariant">Elevated, filled and outlined containers &mdash; one <code class="font-tmd02-mono text-[12px]">group</code> per card drives every hover response.</p>
    </header>

    <div class="grid gap-4 grid-cols-[repeat(auto-fit,minmax(min(260px,100%),1fr))]">
      <article class="group grid rounded-xl bg-tmd02-surface shadow-tmd02-1 transition-shadow duration-250 hover:shadow-tmd02-3 focus-within:shadow-tmd02-3 motion-reduce:transition-none">
        <div class="overflow-hidden rounded-t-xl">
          <div class="aspect-[16/10] bg-linear-[145deg,#1565c0,#42a5f5_70%,#90caf9] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none" role="img" aria-label="Coastal route illustration"></div>
        </div>
        <div class="grid gap-1.5 p-4">
          <span class="font-tmd02-mono text-[11px] uppercase tracking-[0.1em] text-tmd02-onvariant">Elevated</span>
          <h3 class="text-lg font-medium tracking-[-0.005em] transition-colors duration-200 group-hover:text-tmd02-primary"><a href="#route" class="text-inherit no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary rounded-sm">Coastal route, revisited</a></h3>
          <p class="text-sm leading-6 text-tmd02-onvariant text-pretty line-clamp-2">Fourteen kilometres of cliff path, mapped for the first time since the 1998 survey.</p>
        </div>
        <div class="flex gap-2 px-3 pb-3">
          <button type="button" class="relative overflow-hidden min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd02-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]">Open</button>
          <button type="button" class="relative overflow-hidden min-h-10 px-4 rounded-full border border-tmd02-outline bg-transparent cursor-pointer text-sm font-medium text-tmd02-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]">Share</button>
        </div>
      </article>

      <article class="group grid rounded-xl bg-tmd02-surfacevariant">
        <div class="overflow-hidden rounded-t-xl">
          <div class="aspect-[16/10] bg-linear-[145deg,#00695c,#26a69a_70%,#b2dfdb] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none" role="img" aria-label="Field station illustration"></div>
        </div>
        <div class="grid gap-1.5 p-4">
          <span class="font-tmd02-mono text-[11px] uppercase tracking-[0.1em] text-tmd02-onvariant">Filled</span>
          <h3 class="text-lg font-medium tracking-[-0.005em] transition-colors duration-200 group-hover:text-tmd02-primary">Station 4 telemetry</h3>
          <p class="text-sm leading-6 text-tmd02-onvariant text-pretty line-clamp-2">Filled cards sit on surface-variant with no shadow &mdash; the flattest of the three containers.</p>
        </div>
        <div class="flex items-center gap-1 px-3 pb-3">
          <button type="button" aria-label="Add to favourites" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd02-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd02-icon text-[20px] leading-none" aria-hidden="true">favorite</span></button>
          <button type="button" aria-label="Download" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd02-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd02-icon text-[20px] leading-none" aria-hidden="true">download</span></button>
          <span class="ml-auto self-center font-tmd02-mono text-[11px] text-tmd02-onvariant">12.4 MB</span>
        </div>
      </article>

      <article class="group grid rounded-xl bg-tmd02-surface border border-tmd02-outlinevariant transition-colors duration-200 hover:border-tmd02-primary">
        <div class="grid gap-1.5 p-4">
          <span class="font-tmd02-mono text-[11px] uppercase tracking-[0.1em] text-tmd02-onvariant">Outlined</span>
          <h3 class="text-lg font-medium tracking-[-0.005em]">No shadow, one hairline</h3>
          <p class="text-sm leading-6 text-tmd02-onvariant text-pretty">Outlined is the accessible default on busy backgrounds: a 1px <span class="font-tmd02-mono text-[12px]">outline-variant</span> border reads at any elevation, and there is nothing to repaint on hover.</p>
        </div>
        <dl class="grid grid-cols-3 gap-2 px-4 pb-4 m-0">
          <div class="grid gap-0.5"><dt class="font-tmd02-mono text-[10px] uppercase tracking-[0.08em] text-tmd02-onvariant">Sites</dt><dd class="m-0 text-xl font-medium tabular-nums">18</dd></div>
          <div class="grid gap-0.5"><dt class="font-tmd02-mono text-[10px] uppercase tracking-[0.08em] text-tmd02-onvariant">Depth</dt><dd class="m-0 text-xl font-medium tabular-nums">240m</dd></div>
          <div class="grid gap-0.5"><dt class="font-tmd02-mono text-[10px] uppercase tracking-[0.08em] text-tmd02-onvariant">Uptime</dt><dd class="m-0 text-xl font-medium tabular-nums">99.1%</dd></div>
        </dl>
      </article>
    </div>

    <article class="group flex flex-wrap items-stretch gap-0 rounded-xl overflow-hidden bg-tmd02-surface shadow-tmd02-1 transition-shadow duration-250 hover:shadow-tmd02-2 motion-reduce:transition-none">
      <div class="w-[min(200px,40%)] min-h-40 bg-linear-[150deg,#7b1fa2,#ba68c8_65%,#f8bbd0] transition-transform duration-400 group-hover:scale-105 motion-reduce:transition-none" role="img" aria-label="Album artwork"></div>
      <div class="flex-1 min-w-[min(260px,100%)] grid content-center gap-2 p-5">
        <span class="font-tmd02-mono text-[11px] uppercase tracking-[0.1em] text-tmd02-onvariant">Horizontal &middot; media leading</span>
        <h3 class="text-[21px] font-medium tracking-[-0.01em]">Tidal &mdash; deluxe edition</h3>
        <p class="text-sm leading-6 text-tmd02-onvariant text-pretty">A horizontal card is the same container with <span class="font-tmd02-mono text-[12px]">flex-wrap</span> and a percentage media rail. Below 460px the rail wraps above the text with no breakpoint involved.</p>
        <div class="flex gap-2 mt-1">
          <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-5 rounded-full border-0 bg-tmd02-primary text-tmd02-onprimary cursor-pointer text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd02-icon text-[18px] leading-none" aria-hidden="true">play_arrow</span>Play</button>
          <button type="button" class="relative overflow-hidden min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd02-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd02-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Add to library</button>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd02-bg: #eceff1;
  --color-tmd02-bg: oklch(0.95 0.004 236.5);
  --color-tmd02-surface: #fffbfe;
  --color-tmd02-surface: oklch(0.992 0.006 334);
  --color-tmd02-surfacevariant: #e7e0ec;
  --color-tmd02-surfacevariant: oklch(0.916 0.018 311.6);
  --color-tmd02-primary: #1565c0;
  --color-tmd02-primary: oklch(0.513 0.16 255.7);
  --color-tmd02-onprimary: #ffffff;
  --color-tmd02-onprimary: oklch(1 0 89.9);
  --color-tmd02-onsurface: #1c1b1f;
  --color-tmd02-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd02-onvariant: #49454f;
  --color-tmd02-onvariant: oklch(0.398 0.017 303.7);
  --color-tmd02-outline: #79747e;
  --color-tmd02-outline: oklch(0.567 0.016 308.1);
  --color-tmd02-outlinevariant: #cac4d0;
  --color-tmd02-outlinevariant: oklch(0.829 0.018 308.2);
  --font-tmd02-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd02-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd02-icon: 'Material Symbols Outlined';
  --shadow-tmd02-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
  --shadow-tmd02-2: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 2px 6px 2px rgb(0 0 0 / 0.15);
  --shadow-tmd02-3: 0 4px 8px 3px rgb(0 0 0 / 0.15), 0 1px 3px 0 rgb(0 0 0 / 0.3);
}

.tmd-02 {
  width: 100%;
  min-height: 100svh;
}

.tmd-02 [class*="font-tmd02-icon"] {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  font-feature-settings: 'liga';
}
```
