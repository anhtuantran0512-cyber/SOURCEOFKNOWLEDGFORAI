---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-icon-dot-indicator-navbar/"
title: "Tailwind Icon Dot Indicator Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "An icon-plus-label capsule where the current item is marked by a small glowing dot that springs in."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Dot Indicator Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-icon-dot-indicator-navbar/

An icon-plus-label capsule where the current item is marked by a small glowing dot that springs in. The CSS original needed li:has(a.is-active) in the stylesheet; the port reads the same thing as a variant — has-aria-[current=page]: on the item — so the marker is derived from the accessible state, in the markup.
## HTML
```html
<div class="tnb-13 group w-full min-h-svh bg-tnb13-page font-tnb13-sans text-tnb13-ink" aria-label="Icon dot indicator navbar demo">
  <input type="checkbox" id="tnb13-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <div class="sticky top-0 z-100 flex justify-center px-4 py-5">
    <nav class="relative flex items-center gap-4 rounded-[20px] border border-white/8 bg-tnb13-glass/85 p-3 backdrop-blur-xl shadow-[0_8px_32px_oklch(0_0_0/0.5)] md:gap-6" aria-label="Primary">
      <a href="#home" class="flex shrink-0 items-center gap-2 px-1 text-base font-bold text-tnb13-ink no-underline">
        <span class="size-2 rounded-full bg-tnb13-acc shadow-[0_0_8px_var(--color-tnb13-acc)]" aria-hidden="true"></span>Orbit
      </a>
      <span class="hidden h-6 w-px bg-white/10 md:block" aria-hidden="true"></span>
      <ul class="hidden list-none items-center gap-1 md:flex">
        <li class="relative after:absolute after:bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:scale-0 after:rounded-full after:bg-tnb13-acc after:shadow-[0_0_6px_var(--color-tnb13-acc)] after:transition-transform after:duration-250 after:ease-tnb13 after:content-[''] has-aria-[current=page]:after:scale-100 motion-reduce:after:transition-none">
          <a href="#home" aria-current="page" class="flex min-w-14 flex-col items-center gap-1 rounded-xl px-3.5 py-1.5 no-underline transition-colors duration-200 aria-[current=page]:bg-tnb13-acc/12"><span class="text-lg leading-none" aria-hidden="true">&#127968;</span><span class="text-[10px] font-semibold tracking-[0.04em] text-tnb13-acc">Home</span></a>
        </li>
        <li class="relative after:absolute after:bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:scale-0 after:rounded-full after:bg-tnb13-acc after:shadow-[0_0_6px_var(--color-tnb13-acc)] after:transition-transform after:duration-250 after:ease-tnb13 after:content-[''] has-aria-[current=page]:after:scale-100 motion-reduce:after:transition-none">
          <a href="#explore" class="flex min-w-14 flex-col items-center gap-1 rounded-xl px-3.5 py-1.5 no-underline transition-colors duration-200 hover:bg-white/5"><span class="text-lg leading-none" aria-hidden="true">&#128269;</span><span class="text-[10px] font-semibold tracking-[0.04em] text-tnb13-mut transition-colors hover:text-tnb13-ink">Explore</span></a>
        </li>
        <li class="relative after:absolute after:bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:scale-0 after:rounded-full after:bg-tnb13-acc after:shadow-[0_0_6px_var(--color-tnb13-acc)] after:transition-transform after:duration-250 after:ease-tnb13 after:content-[''] has-aria-[current=page]:after:scale-100 motion-reduce:after:transition-none">
          <a href="#alerts" class="flex min-w-14 flex-col items-center gap-1 rounded-xl px-3.5 py-1.5 no-underline transition-colors duration-200 hover:bg-white/5"><span class="relative text-lg leading-none" aria-hidden="true">&#128276;<span class="absolute -top-0.5 -right-1 size-2 rounded-full bg-tnb13-danger ring-2 ring-tnb13-glass"></span></span><span class="text-[10px] font-semibold tracking-[0.04em] text-tnb13-mut transition-colors hover:text-tnb13-ink">Alerts</span></a>
        </li>
        <li class="relative after:absolute after:bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:scale-0 after:rounded-full after:bg-tnb13-acc after:shadow-[0_0_6px_var(--color-tnb13-acc)] after:transition-transform after:duration-250 after:ease-tnb13 after:content-[''] has-aria-[current=page]:after:scale-100 motion-reduce:after:transition-none">
          <a href="#premium" class="flex min-w-14 flex-col items-center gap-1 rounded-xl px-3.5 py-1.5 no-underline transition-colors duration-200 hover:bg-white/5"><span class="text-lg leading-none" aria-hidden="true">&#128142;</span><span class="text-[10px] font-semibold tracking-[0.04em] text-tnb13-mut transition-colors hover:text-tnb13-ink">Premium</span></a>
        </li>
        <li class="relative after:absolute after:bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:scale-0 after:rounded-full after:bg-tnb13-acc after:shadow-[0_0_6px_var(--color-tnb13-acc)] after:transition-transform after:duration-250 after:ease-tnb13 after:content-[''] has-aria-[current=page]:after:scale-100 motion-reduce:after:transition-none">
          <a href="#profile" class="flex min-w-14 flex-col items-center gap-1 rounded-xl px-3.5 py-1.5 no-underline transition-colors duration-200 hover:bg-white/5"><span class="text-lg leading-none" aria-hidden="true">&#128100;</span><span class="text-[10px] font-semibold tracking-[0.04em] text-tnb13-mut transition-colors hover:text-tnb13-ink">Profile</span></a>
        </li>
      </ul>
      <span class="hidden h-6 w-px bg-white/10 md:block" aria-hidden="true"></span>
      <a href="#upgrade" class="hidden shrink-0 rounded-xl bg-linear-[135deg,var(--color-tnb13-acc),var(--color-tnb13-acc2)] px-4 py-2 text-[13px] font-bold whitespace-nowrap text-white no-underline shadow-[0_2px_12px_oklch(0.65_0.25_330/0.35)] transition-transform duration-150 hover:scale-97 md:block motion-reduce:transition-none motion-reduce:hover:scale-100">Upgrade</a>
      <label for="tnb13-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-px w-5 rounded-sm bg-tnb13-ink transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb13-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb13-ink transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
      <div class="absolute inset-x-0 top-[calc(100%+10px)] hidden rounded-[20px] border border-white/8 bg-tnb13-glass/95 p-2 backdrop-blur-xl max-md:group-has-checked:grid">
        <a href="#home" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tnb13-acc no-underline"><span aria-hidden="true">&#127968;</span>Home</a>
        <a href="#explore" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tnb13-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb13-ink"><span aria-hidden="true">&#128269;</span>Explore</a>
        <a href="#alerts" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tnb13-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb13-ink"><span aria-hidden="true">&#128276;</span>Alerts</a>
        <a href="#premium" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tnb13-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb13-ink"><span aria-hidden="true">&#128142;</span>Premium</a>
        <a href="#upgrade" class="mt-1 flex min-h-11 items-center justify-center rounded-xl bg-linear-[135deg,var(--color-tnb13-acc),var(--color-tnb13-acc2)] text-[13px] font-bold text-white no-underline">Upgrade</a>
      </div>
    </nav>
  </div>
  <main class="mx-auto max-w-2xl px-6 py-16 text-center">
    <h1 class="mb-4 text-4xl font-bold tracking-[-0.03em] text-tnb13-ink">Icon + Dot Indicator</h1>
    <p class="text-base leading-relaxed text-tnb13-mut">The dot belongs to the list item, which asks whether it contains the current link: <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em] text-tnb13-acc">has-aria-[current=page]:after:scale-100</code>. No <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em] text-tnb13-acc">:has()</code> rule in the stylesheet, and no class to keep in sync.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb13-page: #0d0418;
  --color-tnb13-page: oklch(0.15 0.05 300);
  --color-tnb13-glass: #140828;
  --color-tnb13-glass: oklch(0.19 0.06 300);
  --color-tnb13-ink: #f0e6ff;
  --color-tnb13-ink: oklch(0.94 0.03 300);
  --color-tnb13-mut: #a294bb;
  --color-tnb13-mut: oklch(0.7 0.05 300);
  --color-tnb13-acc: #d946ef;
  --color-tnb13-acc: oklch(0.7 0.26 328);
  --color-tnb13-acc2: #9333ea;
  --color-tnb13-acc2: oklch(0.54 0.26 300);
  --color-tnb13-danger: #f43f5e;
  --color-tnb13-danger: oklch(0.65 0.22 15);
  --font-tnb13-sans: 'Poppins', system-ui, sans-serif;
  --ease-tnb13: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tnb-13 {
  width: 100%;
  min-height: 100svh;
}

.tnb-13 ::selection {
  background: var(--color-tnb13-acc);
  color: #0d0418;
}
```
