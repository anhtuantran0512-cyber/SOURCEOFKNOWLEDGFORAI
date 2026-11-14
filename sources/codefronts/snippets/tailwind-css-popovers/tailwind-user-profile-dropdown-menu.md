---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-user-profile-dropdown-menu/"
title: "Tailwind User Profile Dropdown Menu"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "The canonical app-header pattern with no script: an avatar anchors an account menu that opens toward the page interior, flips at the edge, and — because it…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind User Profile Dropdown Menu
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-user-profile-dropdown-menu/

The canonical app-header pattern with no script: an avatar anchors an account menu that opens toward the page interior, flips at the edge, and — because it lives in the top layer — ignores the header's overflow-hidden and needs no z-index. The port adds a real menu entrance: it scales out of the avatar's corner with origin-top-right, and the avatar gains a ring while its menu is open.
## HTML
```html
<section class="tpop-13 transition-[--tpop13-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop13-d:1] [[data-theme=dark]_&]:[--tpop13-d:1] [[data-theme=light]_&]:[--tpop13-d:0] group/root w-full min-h-svh bg-tpop13-bg px-4.5 py-10 font-tpop13-sans text-tpop13-ink" aria-label="User profile dropdown menu demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="isolate w-full min-w-0 max-w-[32rem] overflow-hidden rounded-2xl border border-tpop13-rule bg-tpop13-surface shadow-[0_20px_44px_-32px_oklch(0.2_0.02_255/0.5)]">
      <header class="flex items-center gap-2.5 overflow-hidden border-b border-tpop13-rule bg-tpop13-head py-2 pr-2.5 pl-4">
        <span aria-hidden="true" class="grid size-6 place-items-center rounded-md bg-tpop13-accent text-[11px] font-extrabold text-tpop13-surface">N</span>
        <span class="text-[13.5px] font-bold tracking-[-0.01em]">Northwind</span>
        <span class="min-w-0 flex-auto"></span>
        <span class="text-[12.5px] text-tpop13-mut">Pipeline</span>
        <button id="tpop-13-trigger" type="button" popovertarget="tpop-13-menu" aria-label="Account menu for Priya Sharma" class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-full bg-tpop13-accent text-[12.5px] font-bold tracking-[0.04em] text-tpop13-surface ring-tpop13-accent/35 ring-offset-2 ring-offset-tpop13-head transition-shadow [anchor-name:--tpop13-a] hover:ring-2 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop13-accent group-has-[#tpop-13-menu:popover-open]/root:ring-2 group-has-[#tpop-13-menu:popover-open]/root:ring-tpop13-accent">
          PS
          <span aria-hidden="true" class="absolute right-0.5 bottom-0.5 size-2.5 rounded-full bg-tpop13-ok ring-2 ring-tpop13-head"></span>
        </button>
      </header>
      <div class="p-4">
        <p class="mb-2.5 flex min-w-0 justify-between gap-3 text-sm"><span>Acme Foods</span><span class="text-tpop13-mut tabular-nums">$41,200</span></p>
        <p class="mb-2.5 flex min-w-0 justify-between gap-3 text-sm"><span>Harbor Logistics</span><span class="text-tpop13-mut tabular-nums">$18,750</span></p>
        <p class="mb-2.5 flex min-w-0 justify-between gap-3 text-sm"><span>Verity Health</span><span class="text-tpop13-mut tabular-nums">$96,400</span></p>
        <p class="mt-4 border-t border-tpop13-rule pt-3 text-[12.5px] text-tpop13-mut">The header clips its own overflow. The menu does not care.</p>
      </div>

      <div popover="auto" id="tpop-13-menu" role="menu" aria-label="Account" class="fixed m-auto w-[min(16.5rem,calc(100vw-28px))] origin-top-right rounded-2xl border border-tpop13-rule bg-tpop13-surface p-1.5 text-tpop13-ink opacity-0 scale-95 shadow-[0_24px_48px_-24px_oklch(0.2_0.02_255/0.55)] transition-[opacity,scale,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop13-a] [position-area:block-end_span-inline-start] [position-try-fallbacks:flip-inline,flip-block] open:scale-100 open:opacity-100 starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2">
        <div class="mb-1 flex items-center gap-3 border-b border-tpop13-rule px-2.5 pt-2.5 pb-3">
          <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-tpop13-accent text-xs font-bold text-tpop13-surface">PS</span>
          <span class="grid min-w-0 gap-0.5"><span class="text-[13.5px] font-semibold">Priya Sharma</span><span class="truncate text-xs text-tpop13-mut">[email protected]</span></span>
        </div>
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center gap-2.5 rounded-xl px-2.5 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop13-head focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop13-accent">
          <svg class="flex-none text-tpop13-mut" viewBox="0 0 18 18" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="9" cy="6.4" r="3.1"/><path d="M3.4 15c.9-2.7 3-4 5.6-4s4.7 1.3 5.6 4"/></svg>
          Profile and preferences
        </button>
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center gap-2.5 rounded-xl px-2.5 text-left text-[13.5px] font-medium transition-colors hover:bg-tpop13-head focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop13-accent">
          <svg class="flex-none text-tpop13-mut" viewBox="0 0 18 18" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="4" width="12" height="10" rx="1.6"/><path d="M3 7.5h12"/></svg>
          <span class="min-w-0 flex-auto">Billing</span><span class="rounded-full bg-tpop13-accent/10 px-2 py-0.5 text-[11px] font-semibold text-tpop13-accent">Team</span>
        </button>
        <span role="separator" class="mx-1 my-1 block h-px bg-tpop13-rule"></span>
        <button type="button" role="menuitem" class="flex min-h-11 w-full min-w-0 cursor-pointer items-center gap-2.5 rounded-xl px-2.5 text-left text-[13.5px] font-medium text-tpop13-danger transition-colors hover:bg-tpop13-danger/8 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop13-danger">
          <svg class="flex-none" viewBox="0 0 18 18" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M11 5V3.6H4v10.8h7V13M8 9h7M12.6 6.6 15 9l-2.4 2.4"/></svg>
          Sign out
        </button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop13-bg: #eceff2;
  --color-tpop13-bg: oklch(0.95 0.005 255);
  --color-tpop13-surface: #ffffff;
  --color-tpop13-surface: oklch(1 0 0);
  --color-tpop13-head: #f5f7f9;
  --color-tpop13-head: oklch(0.975 0.004 255);
  --color-tpop13-ink: #14191f;
  --color-tpop13-ink: oklch(0.21 0.015 255);
  --color-tpop13-mut: #565e69;
  --color-tpop13-mut: oklch(0.48 0.02 255);
  --color-tpop13-rule: #dee2e7;
  --color-tpop13-rule: oklch(0.91 0.008 255);
  --color-tpop13-accent: #314c7e;
  --color-tpop13-accent: oklch(0.42 0.09 262);
  --color-tpop13-ok: #43b966;
  --color-tpop13-ok: oklch(0.7 0.16 150);
  --color-tpop13-danger: #ac312a;
  --color-tpop13-danger: oklch(0.5 0.16 28);
  --font-tpop13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop13-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-13 {
  width: 100%;
  min-height: 100svh;
  --color-tpop13-bg: color-mix(in oklch, oklch(0.16 0.01 255) calc(var(--tpop13-d) * 100%), oklch(0.95 0.005 255));
  --color-tpop13-surface: color-mix(in oklch, oklch(0.21 0.012 255) calc(var(--tpop13-d) * 100%), oklch(1 0 0));
  --color-tpop13-head: color-mix(in oklch, oklch(0.185 0.011 255) calc(var(--tpop13-d) * 100%), oklch(0.975 0.004 255));
  --color-tpop13-ink: color-mix(in oklch, oklch(0.94 0.008 255) calc(var(--tpop13-d) * 100%), oklch(0.21 0.015 255));
  --color-tpop13-mut: color-mix(in oklch, oklch(0.72 0.02 255) calc(var(--tpop13-d) * 100%), oklch(0.48 0.02 255));
  --color-tpop13-rule: color-mix(in oklch, oklch(0.3 0.014 255) calc(var(--tpop13-d) * 100%), oklch(0.91 0.008 255));
  --color-tpop13-accent: color-mix(in oklch, oklch(0.74 0.08 262) calc(var(--tpop13-d) * 100%), oklch(0.42 0.09 262));
  --color-tpop13-ok: color-mix(in oklch, oklch(0.74 0.16 150) calc(var(--tpop13-d) * 100%), oklch(0.7 0.16 150));
  --color-tpop13-danger: color-mix(in oklch, oklch(0.74 0.13 28) calc(var(--tpop13-d) * 100%), oklch(0.5 0.16 28));
}
```
