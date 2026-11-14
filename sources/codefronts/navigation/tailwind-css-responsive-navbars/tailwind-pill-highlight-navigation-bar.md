---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-pill-highlight-navigation-bar/"
title: "Tailwind Pill Highlight Navigation Bar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A floating glass pill with white-pill active state — and the demo where the port pays for itself twice over."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pill Highlight Navigation Bar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-pill-highlight-navigation-bar/

A floating glass pill with white-pill active state — and the demo where the port pays for itself twice over. The CSS original ships a completely separate mobile bar and mobile menu; here the pill itself reflows: the links collapse, the hamburger appears inside the same capsule, and the panel drops out of it.
## HTML
```html
<div class="tnb-05 group w-full min-h-svh bg-tnb05-page font-tnb05-sans text-tnb05-paper" aria-label="Pill highlight navigation bar demo">
  <input type="checkbox" id="tnb05-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <div class="sticky top-0 z-100 flex justify-center px-4 py-5">
    <nav class="relative flex items-center gap-2 rounded-full border border-white/10 bg-white/6 p-1.5 backdrop-blur-md shadow-[0_8px_32px_oklch(0_0_0/0.4),inset_0_1px_0_oklch(1_0_0/0.08)]" aria-label="Primary">
      <a href="#home" class="shrink-0 px-4 py-1.5 text-[15px] font-bold tracking-[-0.02em] text-tnb05-paper no-underline">&#11041; Helix</a>
      <span class="hidden h-5 w-px shrink-0 bg-white/15 md:block" aria-hidden="true"></span>
      <ul class="hidden list-none items-center gap-1 md:flex">
        <li><a href="#home" aria-current="page" class="block rounded-full px-3.5 py-1.5 text-sm font-medium whitespace-nowrap text-tnb05-mut no-underline transition-colors duration-200 hover:bg-white/10 hover:text-tnb05-paper aria-[current=page]:bg-white aria-[current=page]:text-tnb05-ink aria-[current=page]:shadow-[0_1px_4px_oklch(0_0_0/0.25)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Home</a></li>
        <li><a href="#features" class="block rounded-full px-3.5 py-1.5 text-sm font-medium whitespace-nowrap text-tnb05-mut no-underline transition-colors duration-200 hover:bg-white/10 hover:text-tnb05-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Features</a></li>
        <li><a href="#pricing" class="block rounded-full px-3.5 py-1.5 text-sm font-medium whitespace-nowrap text-tnb05-mut no-underline transition-colors duration-200 hover:bg-white/10 hover:text-tnb05-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Pricing</a></li>
        <li><a href="#blog" class="block rounded-full px-3.5 py-1.5 text-sm font-medium whitespace-nowrap text-tnb05-mut no-underline transition-colors duration-200 hover:bg-white/10 hover:text-tnb05-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Blog</a></li>
        <li><a href="#about" class="block rounded-full px-3.5 py-1.5 text-sm font-medium whitespace-nowrap text-tnb05-mut no-underline transition-colors duration-200 hover:bg-white/10 hover:text-tnb05-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">About</a></li>
      </ul>
      <span class="hidden h-5 w-px shrink-0 bg-white/15 md:block" aria-hidden="true"></span>
      <a href="#access" class="hidden shrink-0 rounded-full bg-linear-[135deg,var(--color-tnb05-acc),var(--color-tnb05-acc2)] px-4 py-1.5 text-sm font-semibold text-white no-underline shadow-[0_2px_8px_oklch(0.55_0.2_280/0.45)] transition-transform duration-150 hover:scale-97 md:block motion-reduce:transition-none motion-reduce:hover:scale-100">Get access</a>
      <label for="tnb05-menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1 rounded-full md:hidden" aria-hidden="true">
        <span class="block h-px w-5 rounded-sm bg-tnb05-paper transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb05-paper transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb05-paper transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
      <div class="absolute inset-x-0 top-[calc(100%+10px)] hidden rounded-3xl border border-white/10 bg-tnb05-page/95 p-2 backdrop-blur-md shadow-[0_16px_40px_oklch(0_0_0/0.5)] max-md:group-has-checked:grid">
        <a href="#home" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-medium text-tnb05-paper no-underline">Home</a>
        <a href="#features" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-medium text-tnb05-mut no-underline transition-colors hover:bg-white/8 hover:text-tnb05-paper">Features</a>
        <a href="#pricing" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-medium text-tnb05-mut no-underline transition-colors hover:bg-white/8 hover:text-tnb05-paper">Pricing</a>
        <a href="#blog" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-medium text-tnb05-mut no-underline transition-colors hover:bg-white/8 hover:text-tnb05-paper">Blog</a>
        <a href="#about" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-medium text-tnb05-mut no-underline transition-colors hover:bg-white/8 hover:text-tnb05-paper">About</a>
        <a href="#access" class="mt-1 flex min-h-11 items-center justify-center rounded-full bg-linear-[135deg,var(--color-tnb05-acc),var(--color-tnb05-acc2)] text-sm font-semibold text-white no-underline">Get access</a>
      </div>
    </nav>
  </div>
  <main class="mx-auto max-w-2xl px-6 py-16 text-center">
    <h1 class="mb-4 text-4xl font-bold tracking-[-0.04em] text-tnb05-paper md:text-5xl">Pill Highlight<br>Navigation Bar</h1>
    <p class="text-lg leading-relaxed text-tnb05-mut">One capsule at every width. The CSS original needed a second bar and a second menu below 640px; the utility version just changes which children are <code class="rounded bg-white/10 px-1.5 py-0.5 text-[0.9em]">hidden</code>.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb05-page: #0a0a0f;
  --color-tnb05-page: oklch(0.15 0.01 280);
  --color-tnb05-ink: #111827;
  --color-tnb05-ink: oklch(0.21 0.02 265);
  --color-tnb05-paper: #f9fafb;
  --color-tnb05-paper: oklch(0.98 0.002 265);
  --color-tnb05-mut: #9ca3af;
  --color-tnb05-mut: oklch(0.71 0.02 265);
  --color-tnb05-acc: #6366f1;
  --color-tnb05-acc: oklch(0.59 0.2 278);
  --color-tnb05-acc2: #8b5cf6;
  --color-tnb05-acc2: oklch(0.63 0.22 295);
  --font-tnb05-sans: 'Sora', system-ui, sans-serif;
}

.tnb-05 {
  width: 100%;
  min-height: 100svh;
}

.tnb-05 ::selection {
  background: var(--color-tnb05-acc);
  color: #fff;
}
```
