---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-split-button-dropdown-details/"
title: "Tailwind Split Button Dropdown with Native Details Menu (Save Options)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "The universal split button — primary Save plus a caret menu — built on <details>/<summary>, which works in every browser with zero script."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Button Dropdown with Native Details Menu (Save Options)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-split-button-dropdown-details/

The universal split button — primary Save plus a caret menu — built on <details>/<summary>, which works in every browser with zero script. group-open/more: rotates the chevron and plays the menu's entrance (animate-tbg06-in), the marker is removed with list-none [&::-webkit-details-marker]:hidden, and each item shows its keyboard shortcut.
## HTML
```html
<section class="tbg-06 w-full min-h-svh grid justify-items-center content-start bg-tbg06-bg bg-linear-160 from-tbg06-bg to-tbg06-bg2 px-5 pt-32 pb-16 font-tbg06-sans text-tbg06-ink" aria-label="Split button dropdown demo">
  <div class="relative inline-flex rounded-2xl shadow-tbg06-lift">
    <button type="button" class="inline-flex h-12 cursor-pointer items-center gap-2.5 rounded-l-2xl bg-tbg06-acc pr-5 pl-4.5 text-[15.5px] font-bold text-tbg06-ink transition hover:brightness-105 active:brightness-95 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg06-ink">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h11l3 3v13H5z"/><path d="M8 4v5h7V4M8 20v-6h8v6"/></svg>
      Save changes
    </button>
    <details class="group/more relative">
      <summary aria-label="More save options" class="grid h-12 w-12 cursor-pointer list-none place-items-center rounded-r-2xl border-l border-tbg06-ink/20 bg-tbg06-acc-d text-tbg06-ink transition hover:brightness-105 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg06-ink [&::-webkit-details-marker]:hidden">
        <svg class="transition-transform duration-300 group-open/more:-rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </summary>
      <div class="absolute top-[calc(100%+0.5rem)] right-0 z-20 hidden w-64 flex-col gap-0.5 rounded-2xl border border-tbg06-line bg-white p-1.5 shadow-tbg06-menu group-open/more:flex group-open/more:animate-tbg06-in motion-reduce:animate-none">
        <button type="button" class="flex min-h-11 w-full cursor-pointer items-center rounded-xl px-3 text-left text-[14.5px] font-semibold text-tbg06-body hover:bg-tbg06-tint focus-visible:bg-tbg06-tint focus-visible:outline-2 focus-visible:outline-tbg06-acc-d">Save as… <kbd class="ml-auto font-sans text-xs font-medium text-tbg06-mut">⇧⌘S</kbd></button>
        <button type="button" class="flex min-h-11 w-full cursor-pointer items-center rounded-xl px-3 text-left text-[14.5px] font-semibold text-tbg06-body hover:bg-tbg06-tint focus-visible:bg-tbg06-tint focus-visible:outline-2 focus-visible:outline-tbg06-acc-d">Save a copy <kbd class="ml-auto font-sans text-xs font-medium text-tbg06-mut">⌥⌘S</kbd></button>
        <button type="button" class="flex min-h-11 w-full cursor-pointer items-center rounded-xl px-3 text-left text-[14.5px] font-semibold text-tbg06-body hover:bg-tbg06-tint focus-visible:bg-tbg06-tint focus-visible:outline-2 focus-visible:outline-tbg06-acc-d">Save as template</button>
        <div role="separator" class="mx-2 my-1.5 h-px bg-tbg06-line"></div>
        <button type="button" class="flex min-h-11 w-full cursor-pointer items-center gap-2.5 rounded-xl px-3 text-left text-[14.5px] font-semibold text-tbg06-danger hover:bg-tbg06-danger/8 focus-visible:bg-tbg06-danger/8 focus-visible:outline-2 focus-visible:outline-tbg06-danger"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>Discard changes</button>
      </div>
    </details>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg06-bg: #fff7ea;
  --color-tbg06-bg2: #ffedd0;
  --color-tbg06-ink: #3a2508;
  --color-tbg06-body: #4f3714;
  --color-tbg06-mut: #82694a;
  --color-tbg06-mut: oklch(0.53 0.05 70);
  --color-tbg06-line: #f0dcbb;
  --color-tbg06-tint: #fdf1dd;
  --color-tbg06-acc: #f7a23a;
  --color-tbg06-acc: oklch(0.77 0.15 65);
  --color-tbg06-acc-d: #e48a1c;
  --color-tbg06-acc-d: oklch(0.7 0.16 60);
  --color-tbg06-danger: #b23b2e;
  --color-tbg06-danger: oklch(0.5 0.16 30);
  --shadow-tbg06-lift: 0 12px 30px -14px rgb(150 90 10 / 0.7);
  --shadow-tbg06-menu: 0 24px 50px -22px rgb(120 70 5 / 0.55);
  --font-tbg06-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-tbg06-in: tbg06-in 0.22s cubic-bezier(0.2, 0.7, 0.3, 1);

  @keyframes tbg06-in {
    from {
      opacity: 0;
      translate: 0 -8px;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-06 {
  width: 100%;
  min-height: 100svh;
}
```
