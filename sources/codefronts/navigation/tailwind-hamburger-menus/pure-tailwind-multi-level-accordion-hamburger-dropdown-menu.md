---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-multi-level-accordion-hamburger-dropdown-menu/"
title: "Pure Tailwind Multi-Level Accordion Hamburger Dropdown Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Nested navigation with zero JavaScript and zero fake semantics: every level is a native <details>/<summary>, so keyboard support and screen-reader disclosure…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Multi-Level Accordion Hamburger Dropdown Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-multi-level-accordion-hamburger-dropdown-menu/

Nested navigation with zero JavaScript and zero fake semantics: every level is a native <details>/<summary>, so keyboard support and screen-reader disclosure announcements come free. Tailwind's open: and group-open: variants read the element's own state, the name attribute makes the top level exclusive, and native toggling stays instant &mdash; the ::details-content animation is documented but deliberately not shipped.
## HTML
```html
<section class="thb-22 w-full min-h-svh bg-thb22-bg font-thb22-sans text-thb22-ink px-5 py-9" aria-label="Multi-level accordion menu demo">
  <div class="min-h-120 flex flex-col items-center justify-center gap-3.5 p-6.5 rounded-[18px] border border-thb22-edge bg-thb22-bg">
    <aside aria-label="Menu" class="w-[min(340px,100%)] overflow-hidden rounded-[18px] border border-thb22-edge bg-thb22-panel shadow-[0_22px_48px_-30px_oklch(0.3_0.05_145/0.55)]">
      <header class="flex items-center justify-between px-4.5 pt-4 pb-3 border-b border-thb22-edge">
        <b class="text-base font-bold tracking-[-0.01em]">Browse</b>
        <span class="relative block w-4.5 h-3 opacity-50" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-thb22-ink"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-thb22-ink"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-thb22-ink"></i>
        </span>
      </header>
      <nav aria-label="Categories" class="grid px-2.5 pt-2 pb-3">
        <details name="thb22-top" open class="thb22-d">
          <summary class="flex items-center gap-2.5 min-h-11.5 px-2.5 rounded-[10px] text-[14.5px] font-bold cursor-pointer list-none marker:hidden [&amp;::-webkit-details-marker]:hidden transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2 [details[open]>&]:text-thb22-acc">
            <svg viewBox="0 0 24 24" class="w-3.75 h-3.75 shrink-0 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] text-thb22-mut transition-[rotate,color] duration-250 ease-thb22 [details[open]>summary>&]:rotate-90 [details[open]>summary>&]:text-thb22-acc motion-reduce:transition-none" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Shop
            <b class="ml-auto px-2 py-0.5 rounded-full bg-thb22-badge text-[10.5px] font-bold text-thb22-mut tabular-nums">312</b>
          </summary>
          <ul class="list-none grid ml-4 pl-3.5 pt-0.5 pb-2 border-l-[1.5px] border-thb22-edge">
            <li><a href="#new" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">New arrivals</a></li>
            <li>
              <details class="thb22-d">
                <summary class="flex items-center gap-2.5 min-h-10.5 px-2.5 rounded-[10px] text-[13.5px] font-semibold text-thb22-mut cursor-pointer list-none marker:hidden [&amp;::-webkit-details-marker]:hidden transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2 [details[open]>&]:text-thb22-acc">
                  <svg viewBox="0 0 24 24" class="w-3.75 h-3.75 shrink-0 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-250 ease-thb22 [details[open]>summary>&]:rotate-90 motion-reduce:transition-none" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Clothing
                </summary>
                <ul class="list-none grid ml-4 pl-3.5 pt-0.5 pb-1.5 border-l-[1.5px] border-thb22-edge">
                  <li><a href="#knitwear" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Knitwear</a></li>
                  <li><a href="#outerwear" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Outerwear</a></li>
                  <li><a href="#denim" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Denim</a></li>
                </ul>
              </details>
            </li>
            <li>
              <details class="thb22-d">
                <summary class="flex items-center gap-2.5 min-h-10.5 px-2.5 rounded-[10px] text-[13.5px] font-semibold text-thb22-mut cursor-pointer list-none marker:hidden [&amp;::-webkit-details-marker]:hidden transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2 [details[open]>&]:text-thb22-acc">
                  <svg viewBox="0 0 24 24" class="w-3.75 h-3.75 shrink-0 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-250 ease-thb22 [details[open]>summary>&]:rotate-90 motion-reduce:transition-none" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Objects
                </summary>
                <ul class="list-none grid ml-4 pl-3.5 pt-0.5 pb-1.5 border-l-[1.5px] border-thb22-edge">
                  <li><a href="#ceramics" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Ceramics</a></li>
                  <li><a href="#lighting" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Lighting</a></li>
                </ul>
              </details>
            </li>
            <li><a href="#archive-sale" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Archive sale</a></li>
          </ul>
        </details>
        <details name="thb22-top" class="thb22-d">
          <summary class="flex items-center gap-2.5 min-h-11.5 px-2.5 rounded-[10px] text-[14.5px] font-bold cursor-pointer list-none marker:hidden [&amp;::-webkit-details-marker]:hidden transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2 [details[open]>&]:text-thb22-acc">
            <svg viewBox="0 0 24 24" class="w-3.75 h-3.75 shrink-0 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] text-thb22-mut transition-[rotate,color] duration-250 ease-thb22 [details[open]>summary>&]:rotate-90 [details[open]>summary>&]:text-thb22-acc motion-reduce:transition-none" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Stories
          </summary>
          <ul class="list-none grid ml-4 pl-3.5 pt-0.5 pb-2 border-l-[1.5px] border-thb22-edge">
            <li><a href="#studio-visits" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Studio visits</a></li>
            <li><a href="#process" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Process notes</a></li>
          </ul>
        </details>
        <details name="thb22-top" class="thb22-d">
          <summary class="flex items-center gap-2.5 min-h-11.5 px-2.5 rounded-[10px] text-[14.5px] font-bold cursor-pointer list-none marker:hidden [&amp;::-webkit-details-marker]:hidden transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2 [details[open]>&]:text-thb22-acc">
            <svg viewBox="0 0 24 24" class="w-3.75 h-3.75 shrink-0 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] text-thb22-mut transition-[rotate,color] duration-250 ease-thb22 [details[open]>summary>&]:rotate-90 [details[open]>summary>&]:text-thb22-acc motion-reduce:transition-none" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Support
          </summary>
          <ul class="list-none grid ml-4 pl-3.5 pt-0.5 pb-2 border-l-[1.5px] border-thb22-edge">
            <li><a href="#shipping" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Shipping &amp; returns</a></li>
            <li><a href="#care" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Care guides</a></li>
            <li><a href="#contact" class="flex items-center min-h-10.5 px-2.5 rounded-[9px] text-[13.5px] font-semibold text-thb22-mut no-underline transition-[background,color,translate] duration-150 hover:bg-thb22-hover hover:text-thb22-ink hover:translate-x-0.5 focus-visible:bg-thb22-hover focus-visible:text-thb22-ink focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Contact</a></li>
          </ul>
        </details>
        <a href="#account" class="flex items-center min-h-10.5 mt-1.5 pt-1 px-2.5 border-t border-thb22-edge text-[13.5px] font-bold text-thb22-ink no-underline transition-[background,color] duration-150 hover:bg-thb22-hover focus-visible:bg-thb22-hover focus-visible:outline-2 focus-visible:outline-thb22-acc focus-visible:-outline-offset-2">Account</a>
      </nav>
    </aside>
    <p class="text-center text-xs text-thb22-mut text-pretty" aria-hidden="true">native <code class="font-thb22-mono text-[11px] px-1.5 py-0.5 rounded bg-thb22-badge">&lt;details name&gt;</code> &mdash; top level is exclusive, keyboard &amp; screen-reader support built in, 0 JS</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb22-bg: #f6f8f4;
  --color-thb22-bg: oklch(0.97 0.006 130);
  --color-thb22-panel: #ffffff;
  --color-thb22-panel: oklch(1 0 0);
  --color-thb22-hover: #f0f4ee;
  --color-thb22-hover: oklch(0.96 0.01 135);
  --color-thb22-badge: #e7ece4;
  --color-thb22-badge: oklch(0.94 0.01 135);
  --color-thb22-edge: #dde3d9;
  --color-thb22-edge: oklch(0.89 0.012 130);
  --color-thb22-ink: #313a30;
  --color-thb22-ink: oklch(0.24 0.02 140);
  --color-thb22-mut: #6e766c;
  --color-thb22-mut: oklch(0.5 0.018 140);
  --color-thb22-acc: #4f8a5c;
  --color-thb22-acc: oklch(0.55 0.14 150);
  --font-thb22-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb22-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb22: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* The ::details-content expansion animation is deliberately NOT shipped, and the recipe lives in
   the "How it works" notes rather than in commented-out CSS here. Engines differ on whether that
   slot reserves layout while its block-size animates; where it does not, an expanding submenu
   paints over its siblings — worse than no animation. Native toggling is instant and correct. */
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-22 {
  width: 100%;
  min-height: 100svh;
}
```
