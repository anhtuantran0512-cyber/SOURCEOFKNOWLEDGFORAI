---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-checkbox-hack-mobile-nav-dropdown/"
title: "Tailwind Checkbox Hack Mobile Nav Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The no-JS mobile nav, and the demo where peer earns its keep: a visually hidden checkbox is the state, and peer-checked: drives both the burger-to-X morph…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Checkbox Hack Mobile Nav Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-checkbox-hack-mobile-nav-dropdown/

The no-JS mobile nav, and the demo where peer earns its keep: a visually hidden checkbox is the state, and peer-checked: drives both the burger-to-X morph and the panel reveal from two elements away — no ~ selectors, no stylesheet.
## HTML
```html
<section class="tdd-10 w-full min-h-svh grid justify-center content-start bg-tdd10-bg font-tdd10-sans text-tdd10-ink px-5 py-10" aria-label="Checkbox hack mobile nav dropdown demo">
  <div class="w-[min(440px,100%)] overflow-hidden rounded-2xl border border-tdd10-edge bg-linear-[160deg,#fff,var(--color-tdd10-bg)] shadow-[0_4px_24px_oklch(0_0_0/0.08)]">
    <input type="checkbox" id="tdd10-toggle" class="peer sr-only">
    <header class="relative z-10 flex items-center justify-between border-b border-tdd10-edge bg-white px-5 py-4.5">
      <a href="#home" class="text-xl font-bold tracking-[-0.5px] text-tdd10-ink no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd10-acc">Forge</a>
      <label for="tdd10-toggle" aria-label="Toggle menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-[5px] rounded-lg p-2 transition-colors duration-150 hover:bg-tdd10-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tdd10-acc">
        <span class="block h-0.5 w-5 origin-center rounded-sm bg-tdd10-ink transition-transform duration-300 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5 origin-center rounded-sm bg-tdd10-ink transition-[opacity,transform] duration-200 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5 origin-center rounded-sm bg-tdd10-ink transition-transform duration-300 motion-reduce:transition-none"></span>
      </label>
    </header>
    <nav role="navigation" aria-label="Main navigation" class="flex max-h-0 flex-col overflow-hidden bg-white opacity-0 transition-[max-height,opacity] duration-380 peer-checked:max-h-100 peer-checked:opacity-100 motion-reduce:transition-none">
      <a href="#work" class="block border-b border-tdd10-edge px-6 py-4.5 text-[22px] font-bold tracking-[-0.5px] text-tdd10-ink no-underline transition-[color,padding] duration-200 hover:pl-8 hover:text-tdd10-acc focus-visible:pl-8 focus-visible:text-tdd10-acc focus-visible:outline-none motion-reduce:transition-none">Work</a>
      <a href="#services" class="block border-b border-tdd10-edge px-6 py-4.5 text-[22px] font-bold tracking-[-0.5px] text-tdd10-ink no-underline transition-[color,padding] duration-200 hover:pl-8 hover:text-tdd10-acc focus-visible:pl-8 focus-visible:text-tdd10-acc focus-visible:outline-none motion-reduce:transition-none">Services</a>
      <a href="#about" class="block border-b border-tdd10-edge px-6 py-4.5 text-[22px] font-bold tracking-[-0.5px] text-tdd10-ink no-underline transition-[color,padding] duration-200 hover:pl-8 hover:text-tdd10-acc focus-visible:pl-8 focus-visible:text-tdd10-acc focus-visible:outline-none motion-reduce:transition-none">About</a>
      <a href="#journal" class="block border-b border-tdd10-edge px-6 py-4.5 text-[22px] font-bold tracking-[-0.5px] text-tdd10-ink no-underline transition-[color,padding] duration-200 hover:pl-8 hover:text-tdd10-acc focus-visible:pl-8 focus-visible:text-tdd10-acc focus-visible:outline-none motion-reduce:transition-none">Journal</a>
      <a href="#start" class="block px-6 py-5 text-[15px] font-semibold text-tdd10-acc no-underline transition-[color,padding] duration-200 hover:pl-8 hover:text-tdd10-accdark focus-visible:pl-8 focus-visible:outline-none motion-reduce:transition-none">Start a Project</a>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd10-bg: #f9fafb;
  --color-tdd10-bg: oklch(0.98 0.002 265);
  --color-tdd10-ink: #111827;
  --color-tdd10-ink: oklch(0.21 0.02 265);
  --color-tdd10-edge: #f3f4f6;
  --color-tdd10-edge: oklch(0.96 0.003 265);
  --color-tdd10-acc: #f59e0b;
  --color-tdd10-acc: oklch(0.75 0.16 70);
  --color-tdd10-accdark: #d97706;
  --color-tdd10-accdark: oklch(0.65 0.15 60);
  --font-tdd10-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* The three burger bars are structural siblings, not indexed content, so the
   nth-child morph is the one rule that reads better in CSS than as three
   arbitrary variants on one label. */

.tdd-10 #tdd10-toggle:checked ~ header label span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.tdd-10 #tdd10-toggle:checked ~ header label span:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}

.tdd-10 #tdd10-toggle:checked ~ header label span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.tdd-10 {
  width: 100%;
  min-height: 100svh;
}

.tdd-10 ::selection {
  background: var(--color-tdd10-ink);
  color: #f9fafb;
}
```
