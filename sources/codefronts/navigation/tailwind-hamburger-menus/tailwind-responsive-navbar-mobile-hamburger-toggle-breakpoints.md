---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-responsive-navbar-mobile-hamburger-toggle-breakpoints/"
title: "Tailwind Responsive Navbar Mobile Hamburger Toggle Breakpoints"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The breakpoint swap every site ships &mdash; inline links wide, hamburger narrow &mdash; and Tailwind v4's container-query variants make it read like a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Navbar Mobile Hamburger Toggle Breakpoints
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-responsive-navbar-mobile-hamburger-toggle-breakpoints/

The breakpoint swap every site ships &mdash; inline links wide, hamburger narrow &mdash; and Tailwind v4's container-query variants make it read like a sentence: @max-lg:hidden on the desktop row, @max-lg:grid on the burger. Drag the stage's right edge and watch the swap happen live. Zero JavaScript, because the toggle is a peer checkbox.
## HTML
```html
<section class="thb-13 w-full min-h-svh bg-thb13-bg font-thb13-sans text-thb13-ink px-5 py-9" aria-label="Responsive navbar breakpoint demo">
  <div class="p-5 rounded-[18px] border border-thb13-edge bg-thb13-bg">
    <p class="mb-3.5 font-thb13-mono text-xs text-thb13-mut" aria-hidden="true">&harr; drag the right edge &mdash; the navbar watches its own width</p>
    <div class="resize-x overflow-hidden w-full max-w-full min-w-[min(300px,100%)] pr-3.5 border-r-[3px] border-dashed border-[color-mix(in_oklch,var(--color-thb13-acc)_45%,var(--color-thb13-edge))]">
      <div class="@container">
        <header class="group relative flex flex-wrap items-center gap-6.5 min-h-16 px-5 py-2 rounded-[14px] border border-thb13-edge bg-thb13-panel shadow-[0_12px_30px_-22px_oklch(0.35_0.05_265/0.5)]">
          <input type="checkbox" id="thb13-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
          <span class="flex items-center gap-2.25 text-[15px] font-extrabold tracking-[-0.01em]">
            <i class="w-4.75 h-4.75 rounded-md rotate-8 bg-[conic-gradient(from_210deg,var(--color-thb13-acc),oklch(0.72_0.13_200))]" aria-hidden="true"></i>Statement
          </span>
          <nav aria-label="Primary" class="flex gap-1 ml-1.5 @max-lg:hidden">
            <a href="#product" aria-current="page" class="group relative px-3 py-2.25 rounded-md text-[13.5px] font-semibold text-thb13-mut no-underline transition-[color] duration-200 hover:text-thb13-ink focus-visible:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:outline-offset-2 aria-current:text-thb13-ink">Product<span class="absolute inset-x-3 bottom-1 h-0.5 rounded-sm bg-thb13-acc scale-x-0 origin-left transition-[scale] duration-250 ease-thb13 group-hover:scale-x-100 group-focus-visible:scale-x-100 group-aria-current:scale-x-100" aria-hidden="true"></span></a>
            <a href="#method" class="group relative px-3 py-2.25 rounded-md text-[13.5px] font-semibold text-thb13-mut no-underline transition-[color] duration-200 hover:text-thb13-ink focus-visible:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:outline-offset-2">Method<span class="absolute inset-x-3 bottom-1 h-0.5 rounded-sm bg-thb13-acc scale-x-0 origin-left transition-[scale] duration-250 ease-thb13 group-hover:scale-x-100 group-focus-visible:scale-x-100" aria-hidden="true"></span></a>
            <a href="#pricing" class="group relative px-3 py-2.25 rounded-md text-[13.5px] font-semibold text-thb13-mut no-underline transition-[color] duration-200 hover:text-thb13-ink focus-visible:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:outline-offset-2">Pricing<span class="absolute inset-x-3 bottom-1 h-0.5 rounded-sm bg-thb13-acc scale-x-0 origin-left transition-[scale] duration-250 ease-thb13 group-hover:scale-x-100 group-focus-visible:scale-x-100" aria-hidden="true"></span></a>
            <a href="#company" class="group relative px-3 py-2.25 rounded-md text-[13.5px] font-semibold text-thb13-mut no-underline transition-[color] duration-200 hover:text-thb13-ink focus-visible:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:outline-offset-2">Company<span class="absolute inset-x-3 bottom-1 h-0.5 rounded-sm bg-thb13-acc scale-x-0 origin-left transition-[scale] duration-250 ease-thb13 group-hover:scale-x-100 group-focus-visible:scale-x-100" aria-hidden="true"></span></a>
          </nav>
          <a href="#start" class="inline-flex items-center ml-auto min-h-10 px-4.5 rounded-[10px] bg-thb13-ink text-thb13-bg text-[13px] font-bold no-underline transition-[background,translate] duration-200 hover:bg-thb13-acc active:translate-y-px focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:outline-offset-2">Get started</a>
          <label for="thb13-t" class="hidden order-5 w-11 h-11 place-items-center rounded-[11px] border border-thb13-edge cursor-pointer select-none transition-[background] duration-200 hover:bg-thb13-hover peer-focus-visible:outline-2 peer-focus-visible:outline-thb13-acc peer-focus-visible:outline-offset-2 @max-lg:grid" aria-hidden="true">
            <span class="relative block w-4.5 h-3">
              <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-thb13-ink transition-[translate,rotate] duration-280 group-has-checked:translate-y-[5px] group-has-checked:rotate-45 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-thb13-ink transition-[opacity] duration-200 group-has-checked:opacity-0 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-thb13-ink transition-[translate,rotate] duration-280 group-has-checked:-translate-y-[5px] group-has-checked:-rotate-45 motion-reduce:transition-none"></i>
            </span>
          </label>
          <nav aria-label="Primary mobile" class="hidden basis-full min-w-0 opacity-0 [grid-template-rows:0fr] transition-[grid-template-rows,opacity] duration-350 ease-thb13 group-has-checked:opacity-100 group-has-checked:[grid-template-rows:1fr] @max-lg:grid @min-lg:hidden motion-reduce:transition-none">
            <ul class="list-none grid min-h-0 overflow-hidden pt-1.5 group-has-checked:mt-1 group-has-checked:border-t group-has-checked:border-thb13-edge">
              <li><a href="#product" aria-current="page" class="flex items-center min-h-11.5 px-3 rounded-[9px] text-sm font-semibold text-thb13-mut no-underline transition-[background,color] duration-150 hover:bg-thb13-hover hover:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:-outline-offset-2 aria-current:text-thb13-acc">Product</a></li>
              <li><a href="#method" class="flex items-center min-h-11.5 px-3 rounded-[9px] text-sm font-semibold text-thb13-mut no-underline transition-[background,color] duration-150 hover:bg-thb13-hover hover:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:-outline-offset-2">Method</a></li>
              <li><a href="#pricing" class="flex items-center min-h-11.5 px-3 rounded-[9px] text-sm font-semibold text-thb13-mut no-underline transition-[background,color] duration-150 hover:bg-thb13-hover hover:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:-outline-offset-2">Pricing</a></li>
              <li><a href="#company" class="flex items-center min-h-11.5 px-3 rounded-[9px] text-sm font-semibold text-thb13-mut no-underline transition-[background,color] duration-150 hover:bg-thb13-hover hover:text-thb13-ink focus-visible:outline-2 focus-visible:outline-thb13-acc focus-visible:-outline-offset-2">Company</a></li>
            </ul>
          </nav>
        </header>
        <div class="grid gap-3 px-1 py-4.5" aria-hidden="true">
          <div class="h-2.75 w-[64%] rounded-full bg-thb13-line"></div>
          <div class="h-2.75 w-[82%] rounded-full bg-thb13-line"></div>
          <div class="h-2.75 w-[47%] rounded-full bg-thb13-line"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb13-bg: #fafafc;
  --color-thb13-bg: oklch(0.975 0.004 260);
  --color-thb13-panel: #ffffff;
  --color-thb13-panel: oklch(1 0 0);
  --color-thb13-hover: #f2f2f7;
  --color-thb13-hover: oklch(0.96 0.008 260);
  --color-thb13-edge: #e2e2e9;
  --color-thb13-edge: oklch(0.89 0.009 260);
  --color-thb13-line: #e6e6ed;
  --color-thb13-line: oklch(0.9 0.007 260);
  --color-thb13-ink: #32334a;
  --color-thb13-ink: oklch(0.24 0.018 262);
  --color-thb13-mut: #71738c;
  --color-thb13-mut: oklch(0.53 0.015 262);
  --color-thb13-acc: #5340e0;
  --color-thb13-acc: oklch(0.58 0.2 275);
  --font-thb13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb13: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-13 {
  width: 100%;
  min-height: 100svh;
}
```
