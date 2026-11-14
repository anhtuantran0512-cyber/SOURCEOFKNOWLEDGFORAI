---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-glassmorphism-float-panel-dropdown/"
title: "Tailwind Glassmorphism Float Panel Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "Frosted glass over a vivid gradient, where the port is almost free: backdrop-blur-xl and backdrop-saturate-200 are real utilities, the translucent border is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Float Panel Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-glassmorphism-float-panel-dropdown/

Frosted glass over a vivid gradient, where the port is almost free: backdrop-blur-xl and backdrop-saturate-200 are real utilities, the translucent border is border-white/35, and the layered inner glow is one arbitrary shadow-[…] because a composed inset shadow is not a design-scale value.
## HTML
```html
<section class="tdd-05 relative w-full min-h-svh overflow-hidden bg-linear-[135deg,var(--color-tdd05-g1),var(--color-tdd05-g2)_40%,var(--color-tdd05-g3)] font-tdd05-sans px-5 py-8" aria-label="Glassmorphism float panel dropdown demo">
  <div class="pointer-events-none absolute -top-25 -left-20 size-75 rounded-full bg-tdd05-g3 opacity-50 blur-[60px]" aria-hidden="true"></div>
  <div class="pointer-events-none absolute -bottom-20 right-0 size-62 rounded-full bg-tdd05-g4 opacity-50 blur-[60px]" aria-hidden="true"></div>
  <div class="pointer-events-none absolute top-[40%] left-[40%] size-50 rounded-full bg-tdd05-g5 opacity-50 blur-[60px]" aria-hidden="true"></div>
  <nav class="relative z-10 mx-auto flex w-fit items-center gap-2 rounded-full border border-white/30 bg-white/15 py-2 pr-2 pl-6 backdrop-blur-xl backdrop-saturate-[1.8] shadow-[0_8px_32px_oklch(0_0_0/0.2),inset_0_1px_0_oklch(1_0_0/0.4)]" aria-label="Primary">
    <span class="mr-2 text-lg font-bold tracking-[-0.3px] text-white">Aura</span>
    <div class="flex gap-0.5">
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-3 after:content-['']">
        <a href="#features" class="block rounded-full px-4 py-2 text-sm font-medium text-white/85 no-underline transition-colors duration-200 group-hover:bg-white/20 group-hover:text-white focus-visible:bg-white/20 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Features &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+12px)] left-1/2 flex min-w-53 -translate-x-1/2 -translate-y-3 flex-col gap-0.5 rounded-2xl border border-white/35 bg-white/18 p-2 opacity-0 backdrop-blur-2xl backdrop-saturate-200 shadow-[0_16px_48px_oklch(0_0_0/0.25),inset_0_1px_0_oklch(1_0_0/0.5)] transition-[opacity,translate] duration-320 ease-tdd05 group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#ai" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#127775; AI Insights</a>
          <a href="#dashboard" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#128202; Live Dashboard</a>
          <a href="#zero-trust" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#128274; Zero Trust Security</a>
          <a href="#sync" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#9889; Real-time Sync</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-3 after:content-['']">
        <a href="#pricing" class="block rounded-full px-4 py-2 text-sm font-medium text-white/85 no-underline transition-colors duration-200 group-hover:bg-white/20 group-hover:text-white focus-visible:bg-white/20 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Pricing &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+12px)] left-1/2 flex min-w-53 -translate-x-1/2 -translate-y-3 flex-col gap-0.5 rounded-2xl border border-white/35 bg-white/18 p-2 opacity-0 backdrop-blur-2xl backdrop-saturate-200 shadow-[0_16px_48px_oklch(0_0_0/0.25),inset_0_1px_0_oklch(1_0_0/0.5)] transition-[opacity,translate] duration-320 ease-tdd05 group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#free" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#127381; Free Plan</a>
          <a href="#pro" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#128640; Pro Plan</a>
          <a href="#enterprise" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#127959; Enterprise</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-3 after:content-['']">
        <a href="#about" class="block rounded-full px-4 py-2 text-sm font-medium text-white/85 no-underline transition-colors duration-200 group-hover:bg-white/20 group-hover:text-white focus-visible:bg-white/20 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">About &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+12px)] left-1/2 flex min-w-53 -translate-x-1/2 -translate-y-3 flex-col gap-0.5 rounded-2xl border border-white/35 bg-white/18 p-2 opacity-0 backdrop-blur-2xl backdrop-saturate-200 shadow-[0_16px_48px_oklch(0_0_0/0.25),inset_0_1px_0_oklch(1_0_0/0.5)] transition-[opacity,translate] duration-320 ease-tdd05 group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#team" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#128101; Our Team</a>
          <a href="#mission" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#127759; Mission</a>
          <a href="#press" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-white/90 no-underline transition-colors duration-150 hover:bg-white/20 hover:text-white focus-visible:bg-white/20 focus-visible:outline-none">&#128240; Press Kit</a>
        </div>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd05-g1: #667eea;
  --color-tdd05-g1: oklch(0.63 0.16 275);
  --color-tdd05-g2: #764ba2;
  --color-tdd05-g2: oklch(0.46 0.16 305);
  --color-tdd05-g3: #f093fb;
  --color-tdd05-g3: oklch(0.76 0.19 325);
  --color-tdd05-g4: #4facfe;
  --color-tdd05-g4: oklch(0.72 0.15 240);
  --color-tdd05-g5: #f5af19;
  --color-tdd05-g5: oklch(0.79 0.16 75);
  --font-tdd05-sans: 'Outfit', system-ui, sans-serif;
  --ease-tdd05: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-05 {
  width: 100%;
  min-height: 100svh;
}

.tdd-05 ::selection {
  background: oklch(1 0 0 / 0.4);
  color: #fff;
}
```
