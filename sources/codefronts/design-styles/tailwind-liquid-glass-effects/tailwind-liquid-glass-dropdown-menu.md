---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-dropdown-menu/"
title: "Tailwind Liquid Glass Dropdown Menu"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A dropdown that snaps in like a liquid drop, built on native <details> so open/close, keyboard toggling and focus are free."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Dropdown Menu
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-dropdown-menu/

A dropdown that snaps in like a liquid drop, built on native <details> so open/close, keyboard toggling and focus are free. The port's clean move is group on the <details> element itself: group-open: rotates the chevron and runs the panel's spring, and there is no state anywhere else.
## HTML
```html
<section class="lgt-09 relative flex w-full min-h-svh items-start justify-center overflow-hidden px-5 py-30 font-lgt09-sans [background:radial-gradient(circle_at_20%_30%,#4a2f8a,transparent_55%),radial-gradient(circle_at_80%_20%,#1e5aa8,transparent_50%),radial-gradient(circle_at_50%_90%,#a83d7a,transparent_50%),#0a0620]" aria-label="Tailwind liquid glass dropdown menu">
  <div aria-hidden="true" class="pointer-events-none absolute -inset-10 opacity-70 blur-[60px] [background:radial-gradient(circle_at_30%_40%,#7c3aed,transparent_45%),radial-gradient(circle_at_70%_60%,#0891b2,transparent_45%),radial-gradient(circle_at_50%_80%,#db2777,transparent_40%)]"></div>

  <details class="group relative z-2 w-[min(240px,80vw)]">
    <summary class="flex cursor-pointer list-none items-center justify-between rounded-[14px] border border-white/35 bg-white/14 px-4.5 py-3.25 text-[15px] font-bold text-white backdrop-blur-[16px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_12px_26px_-16px_rgba(0,0,0,.6)] transition-colors duration-200 hover:bg-white/20 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white [&amp;::-webkit-details-marker]:hidden">
      Workspace
      <span aria-hidden="true" class="transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none">&#9662;</span>
    </summary>

    <div role="menu" class="absolute inset-x-0 mt-2.5 origin-top rounded-[16px] border border-white/30 bg-white/12 p-2 backdrop-blur-[22px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_26px_50px_-24px_rgba(0,0,0,.7)] group-open:animate-lgt09-drop motion-reduce:group-open:animate-none">
      <a role="menuitem" href="#lgt-09" class="block rounded-[10px] px-3.5 py-2.75 text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/18 focus-visible:bg-white/18 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white">Projects</a>
      <a role="menuitem" href="#lgt-09" class="block rounded-[10px] px-3.5 py-2.75 text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/18 focus-visible:bg-white/18 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white">Team</a>
      <a role="menuitem" href="#lgt-09" class="block rounded-[10px] px-3.5 py-2.75 text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/18 focus-visible:bg-white/18 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white">Settings</a>
      <hr class="mx-2 my-1.5 border-0 border-t border-white/18">
      <a role="menuitem" href="#lgt-09" class="block rounded-[10px] px-3.5 py-2.75 text-sm font-semibold text-white no-underline transition-colors duration-200 hover:bg-white/18 focus-visible:bg-white/18 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white">Sign out</a>
    </div>
  </details>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-lgt09-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt09-drop: lgt-09-drop 0.4s cubic-bezier(0.3, 1.3, 0.5, 1);
}

@keyframes lgt-09-drop {
  0% {
    opacity: 0;
    transform: translateY(-10px) scaleY(0.6);
  }

  60% {
    opacity: 1;
    transform: translateY(2px) scaleY(1.05);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scaleY(1);
  }
}
```
