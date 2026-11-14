---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-checkbox-hack-hamburger-navigation-no-javascript/"
title: "Pure Tailwind Checkbox Hack Hamburger Navigation (No JavaScript)"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The classic zero-dependency pattern, and the port is the most instructive in the collection: peer-checked: handles the panel beautifully, but the burger's…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Checkbox Hack Hamburger Navigation (No JavaScript)
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-checkbox-hack-hamburger-navigation-no-javascript/

The classic zero-dependency pattern, and the port is the most instructive in the collection: peer-checked: handles the panel beautifully, but the burger's bars are descendants of a sibling &mdash; not siblings themselves &mdash; so they need arbitrary variants. That friction is exactly the argument for demo 09's has-checked:. Both accessibility fixes survive: the input stays focusable, and its focus ring is re-projected onto the visible label.
## HTML
```html
<section class="thb-05 w-full min-h-svh grid justify-center content-start bg-thb05-bg font-thb05-sans text-thb05-ink px-5 py-9" aria-label="Pure Tailwind checkbox hack hamburger menu demo">
  <div class="relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb05-bg border border-thb05-edge">
    <input type="checkbox" id="thb05-t" class="thb05-state peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
    <header class="relative z-3 flex items-center justify-between h-17.5 pl-6 pr-4">
      <span class="flex items-center gap-2.25 text-[15px] font-bold tracking-[-0.01em]">
        <i class="w-4.75 h-4.75 rounded-full bg-[conic-gradient(from_160deg,var(--color-thb05-acc),oklch(0.75_0.13_110))]" aria-hidden="true"></i>papertrail
      </span>
      <label for="thb05-t" class="flex items-center gap-2.5 min-h-11 px-3.5 rounded-full border-[1.5px] border-thb05-ink cursor-pointer select-none text-[12.5px] font-bold tracking-[0.08em] uppercase transition-[background,color,border-color] duration-250 hover:bg-thb05-ink hover:text-thb05-bg peer-focus-visible:outline-2 peer-focus-visible:outline-thb05-acc peer-focus-visible:outline-offset-3 [.thb05-state:checked~header_&]:border-thb05-panelink [.thb05-state:checked~header_&]:text-thb05-panelink [.thb05-state:checked~header_&]:hover:bg-thb05-panelink [.thb05-state:checked~header_&]:hover:text-thb05-panel">
        <span class="relative block w-4.5 h-3" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 [.thb05-state:checked~header_&]:translate-y-[5px] [.thb05-state:checked~header_&]:rotate-45 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 [.thb05-state:checked~header_&]:opacity-0 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 [.thb05-state:checked~header_&]:-translate-y-[5px] [.thb05-state:checked~header_&]:-rotate-45 motion-reduce:transition-none"></i>
        </span>
        <span class="block [.thb05-state:checked~header_&]:hidden" aria-hidden="true">Menu</span>
        <span class="hidden [.thb05-state:checked~header_&]:block" aria-hidden="true">Close</span>
      </label>
    </header>
    <nav aria-label="Primary" class="absolute inset-0 z-2 flex flex-col justify-center gap-1 px-8 bg-thb05-panel -translate-y-[105%] invisible [transition:translate_.5s_var(--ease-thb05),visibility_0s_.5s] peer-checked:translate-y-0 peer-checked:visible peer-checked:[transition:translate_.5s_var(--ease-thb05),visibility_0s_0s] motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
      <a href="#features" style="--i:0" class="py-3.25 px-0.5 text-[27px] font-bold tracking-[-0.02em] text-thb05-panelink no-underline border-b border-thb05-panedge opacity-0 -translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb05in hover:text-thb05-panacc focus-visible:text-thb05-panacc focus-visible:outline-2 focus-visible:outline-thb05-panacc focus-visible:outline-offset-4 [.thb05-state:checked~nav_&]:opacity-100 [.thb05-state:checked~nav_&]:translate-y-0 [.thb05-state:checked~nav_&]:[transition-delay:calc(160ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">Features</a>
      <a href="#pricing" style="--i:1" class="py-3.25 px-0.5 text-[27px] font-bold tracking-[-0.02em] text-thb05-panelink no-underline border-b border-thb05-panedge opacity-0 -translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb05in hover:text-thb05-panacc focus-visible:text-thb05-panacc focus-visible:outline-2 focus-visible:outline-thb05-panacc focus-visible:outline-offset-4 [.thb05-state:checked~nav_&]:opacity-100 [.thb05-state:checked~nav_&]:translate-y-0 [.thb05-state:checked~nav_&]:[transition-delay:calc(160ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">Pricing</a>
      <a href="#changelog" style="--i:2" class="py-3.25 px-0.5 text-[27px] font-bold tracking-[-0.02em] text-thb05-panelink no-underline border-b border-thb05-panedge opacity-0 -translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb05in hover:text-thb05-panacc focus-visible:text-thb05-panacc focus-visible:outline-2 focus-visible:outline-thb05-panacc focus-visible:outline-offset-4 [.thb05-state:checked~nav_&]:opacity-100 [.thb05-state:checked~nav_&]:translate-y-0 [.thb05-state:checked~nav_&]:[transition-delay:calc(160ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">Changelog</a>
      <a href="#docs" style="--i:3" class="py-3.25 px-0.5 text-[27px] font-bold tracking-[-0.02em] text-thb05-panelink no-underline border-b border-thb05-panedge opacity-0 -translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb05in hover:text-thb05-panacc focus-visible:text-thb05-panacc focus-visible:outline-2 focus-visible:outline-thb05-panacc focus-visible:outline-offset-4 [.thb05-state:checked~nav_&]:opacity-100 [.thb05-state:checked~nav_&]:translate-y-0 [.thb05-state:checked~nav_&]:[transition-delay:calc(160ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">Docs</a>
      <a href="#signin" style="--i:4" class="mt-4.5 py-3.25 px-0.5 text-base font-bold tracking-[-0.02em] text-thb05-panacc no-underline opacity-0 -translate-y-3.5 transition-[color,opacity,translate] duration-350 ease-thb05in hover:text-thb05-panelink focus-visible:outline-2 focus-visible:outline-thb05-panacc focus-visible:outline-offset-4 [.thb05-state:checked~nav_&]:opacity-100 [.thb05-state:checked~nav_&]:translate-y-0 [.thb05-state:checked~nav_&]:[transition-delay:calc(160ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">Sign in &rarr;</a>
    </nav>
    <div class="grid gap-3.25 px-6 pt-4" aria-hidden="true">
      <div class="flex flex-col justify-end h-42.5 mb-1.5 p-4.5 rounded-2xl bg-linear-[150deg,oklch(0.9_0.04_120),oklch(0.84_0.06_145)]">
        <b class="text-[26px] font-bold tracking-[-0.02em]">0 bytes</b>
        <span class="text-[12.5px] text-thb05-mut">of JavaScript in this menu</span>
      </div>
      <div class="h-2.75 w-[84%] rounded-full bg-thb05-line"></div>
      <div class="h-2.75 w-[66%] rounded-full bg-thb05-line"></div>
      <div class="h-2.75 w-[75%] rounded-full bg-thb05-line"></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb05-bg: #f5f4e9;
  --color-thb05-bg: oklch(0.96 0.012 100);
  --color-thb05-panel: #2f4438;
  --color-thb05-panel: oklch(0.27 0.04 145);
  --color-thb05-panelink: #eef2ec;
  --color-thb05-panelink: oklch(0.95 0.02 145);
  --color-thb05-panedge: #47604f;
  --color-thb05-panedge: oklch(0.36 0.04 145);
  --color-thb05-panacc: #cbd96a;
  --color-thb05-panacc: oklch(0.85 0.14 110);
  --color-thb05-edge: #dcdac9;
  --color-thb05-edge: oklch(0.87 0.02 100);
  --color-thb05-line: #e2e0d0;
  --color-thb05-line: oklch(0.89 0.012 100);
  --color-thb05-ink: #363c33;
  --color-thb05-ink: oklch(0.26 0.02 130);
  --color-thb05-mut: #6f766a;
  --color-thb05-mut: oklch(0.52 0.02 130);
  --color-thb05-acc: #5a8f5f;
  --color-thb05-acc: oklch(0.55 0.13 145);
  --font-thb05-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb05: cubic-bezier(0.7, 0, 0.25, 1);
  --ease-thb05in: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-05 {
  width: 100%;
  min-height: 100svh;
}
```
