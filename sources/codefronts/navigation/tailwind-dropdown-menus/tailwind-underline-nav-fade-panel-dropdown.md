---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-underline-nav-fade-panel-dropdown/"
title: "Tailwind Underline Nav Fade Panel Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "An editorial nav where a rule sweeps left-to-right under the hovered item and a plain panel fades in below."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Underline Nav Fade Panel Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-underline-nav-fade-panel-dropdown/

An editorial nav where a rule sweeps left-to-right under the hovered item and a plain panel fades in below. Two things make the port interesting: the underline is an after: pseudo styled entirely in utilities, and the visibility trick — the one transition Tailwind's scale genuinely cannot express — stays an arbitrary shorthand.
## HTML
```html
<section class="tdd-08 w-full min-h-svh bg-tdd08-bg font-tdd08-sans text-tdd08-ink px-5 py-8" aria-label="Underline nav fade panel dropdown demo">
  <nav class="relative z-10 mx-auto flex w-[min(680px,100%)] items-center border-b-2 border-tdd08-edge bg-white px-6" aria-label="Primary">
    <a href="#home" class="mr-8 py-4.5 font-tdd08-serif text-[22px] font-semibold tracking-[-0.5px] text-tdd08-ink no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd08-ink">The&nbsp;<em class="italic text-tdd08-amber">Edit</em></a>
    <div class="flex">
      <div class="group relative" style="--accent:#d97706">
        <a href="#collections" class="relative block px-4 py-4.5 text-[13.5px] font-medium tracking-[0.02em] text-tdd08-mut no-underline transition-colors duration-200 after:absolute after:inset-x-4 after:-bottom-0.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-sm after:bg-[var(--accent)] after:transition-transform after:duration-250 after:ease-out after:content-[''] group-hover:text-tdd08-ink group-hover:after:scale-x-100 focus-visible:text-tdd08-ink focus-visible:after:scale-x-100 focus-visible:outline-none">Collections</a>
        <div class="pointer-events-none invisible absolute top-[calc(100%+2px)] left-0 flex gap-8 rounded-b-xl border border-t-0 border-tdd08-edge bg-white px-6 py-5 opacity-0 shadow-[0_12px_32px_oklch(0_0_0/0.08)] [transition:opacity_.22s_ease,visibility_0s_.22s] group-hover:pointer-events-auto group-hover:visible group-hover:opacity-100 group-hover:[transition:opacity_.22s_ease,visibility_0s_0s] group-focus-within:pointer-events-auto group-focus-within:visible group-focus-within:opacity-100">
          <div class="flex min-w-35 flex-col gap-1">
            <a href="#spring" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Spring 2025</a>
            <a href="#essentials" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Essentials</a>
            <a href="#archive" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Archive</a>
          </div>
          <div class="flex min-w-35 flex-col gap-1">
            <a href="#collabs" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Collaborations</a>
            <a href="#limited" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Limited Editions</a>
            <a href="#lookbook" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Lookbook</a>
          </div>
        </div>
      </div>
      <div class="group relative" style="--accent:#059669">
        <a href="#stories" class="relative block px-4 py-4.5 text-[13.5px] font-medium tracking-[0.02em] text-tdd08-mut no-underline transition-colors duration-200 after:absolute after:inset-x-4 after:-bottom-0.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-sm after:bg-[var(--accent)] after:transition-transform after:duration-250 after:ease-out after:content-[''] group-hover:text-tdd08-ink group-hover:after:scale-x-100 focus-visible:text-tdd08-ink focus-visible:after:scale-x-100 focus-visible:outline-none">Stories</a>
        <div class="pointer-events-none invisible absolute top-[calc(100%+2px)] left-0 flex gap-8 rounded-b-xl border border-t-0 border-tdd08-edge bg-white px-6 py-5 opacity-0 shadow-[0_12px_32px_oklch(0_0_0/0.08)] [transition:opacity_.22s_ease,visibility_0s_.22s] group-hover:pointer-events-auto group-hover:visible group-hover:opacity-100 group-hover:[transition:opacity_.22s_ease,visibility_0s_0s] group-focus-within:pointer-events-auto group-focus-within:visible group-focus-within:opacity-100">
          <div class="flex min-w-35 flex-col gap-1">
            <a href="#features" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Feature Articles</a>
            <a href="#interviews" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Interviews</a>
            <a href="#profiles" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Profiles</a>
          </div>
          <div class="flex min-w-35 flex-col gap-1">
            <a href="#photography" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Photography</a>
            <a href="#film" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Film</a>
          </div>
        </div>
      </div>
      <div class="group relative" style="--accent:#7c3aed">
        <a href="#studio" class="relative block px-4 py-4.5 text-[13.5px] font-medium tracking-[0.02em] text-tdd08-mut no-underline transition-colors duration-200 after:absolute after:inset-x-4 after:-bottom-0.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-sm after:bg-[var(--accent)] after:transition-transform after:duration-250 after:ease-out after:content-[''] group-hover:text-tdd08-ink group-hover:after:scale-x-100 focus-visible:text-tdd08-ink focus-visible:after:scale-x-100 focus-visible:outline-none">Studio</a>
        <div class="pointer-events-none invisible absolute top-[calc(100%+2px)] left-0 flex gap-8 rounded-b-xl border border-t-0 border-tdd08-edge bg-white px-6 py-5 opacity-0 shadow-[0_12px_32px_oklch(0_0_0/0.08)] [transition:opacity_.22s_ease,visibility_0s_.22s] group-hover:pointer-events-auto group-hover:visible group-hover:opacity-100 group-hover:[transition:opacity_.22s_ease,visibility_0s_0s] group-focus-within:pointer-events-auto group-focus-within:visible group-focus-within:opacity-100">
          <div class="flex min-w-35 flex-col gap-1">
            <a href="#about" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">About Us</a>
            <a href="#process" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Process</a>
            <a href="#careers" class="block border-b border-transparent py-1.5 font-tdd08-serif text-[15px] text-tdd08-mut no-underline transition-colors duration-150 hover:border-b-[var(--accent)] hover:text-tdd08-ink focus-visible:text-tdd08-ink focus-visible:outline-none">Careers</a>
          </div>
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
  --color-tdd08-bg: #fafaf8;
  --color-tdd08-bg: oklch(0.98 0.003 100);
  --color-tdd08-ink: #1e293b;
  --color-tdd08-ink: oklch(0.28 0.03 260);
  --color-tdd08-mut: #64748b;
  --color-tdd08-mut: oklch(0.55 0.03 255);
  --color-tdd08-edge: #e2e8f0;
  --color-tdd08-edge: oklch(0.92 0.01 255);
  --color-tdd08-amber: #d97706;
  --color-tdd08-amber: oklch(0.65 0.15 60);
  --font-tdd08-sans: 'Inter', system-ui, sans-serif;
  --font-tdd08-serif: 'Fraunces', Georgia, serif;
}

.tdd-08 {
  width: 100%;
  min-height: 100svh;
}

.tdd-08 ::selection {
  background: var(--color-tdd08-ink);
  color: #f8fafc;
}
```
