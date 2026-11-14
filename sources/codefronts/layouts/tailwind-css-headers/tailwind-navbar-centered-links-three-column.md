---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-navbar-centered-links-three-column/"
title: "Tailwind Navbar with Centered Links — Three Column Flexbox"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "Logo left, nav truly centred, actions right — and it stays centred when the logo and button are wildly different widths."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Navbar with Centered Links — Three Column Flexbox
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-navbar-centered-links-three-column/

Logo left, nav truly centred, actions right — and it stays centred when the logo and button are wildly different widths. The trick is flex-1 basis-0 on both outer columns so they split leftover space equally, rather than trusting justify-between. A Show tracks switch outlines the three columns so you can see it work.
## HTML
```html
<div class="thd-14 group/thd14 w-full min-h-svh bg-thd14-bg font-thd14-sans text-thd14-ink antialiased">
  <a href="#thd-14-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:bg-thd14-ink focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-thd14-bg">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd14-ink bg-thd14-bg">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-4 px-[clamp(.75rem,3vw,1.5rem)]">
      <div data-track="flex-1 basis-0" class="relative flex min-w-0 flex-1 basis-0 items-center before:absolute before:-top-3 before:left-0 before:hidden before:bg-thd14-acc before:px-1 before:font-thd14-mono before:text-[9px] before:leading-4 before:text-white before:content-[attr(data-track)] group-has-[#thd-14-tracks:checked]/thd14:outline-1 group-has-[#thd-14-tracks:checked]/thd14:outline-offset-4 group-has-[#thd-14-tracks:checked]/thd14:outline-thd14-acc group-has-[#thd-14-tracks:checked]/thd14:outline-dashed group-has-[#thd-14-tracks:checked]/thd14:before:block">
        <a href="#thd-14-main" class="flex items-center gap-2 truncate text-[1.05rem] font-extrabold uppercase tracking-[.02em]"><span aria-hidden="true" class="grid size-6 flex-none grid-cols-2 border border-thd14-ink"><span class="border-r border-b border-thd14-ink bg-thd14-ink"></span><span class="border-b border-thd14-ink"></span><span class="border-r border-thd14-ink"></span><span class="bg-thd14-acc"></span></span><span class="truncate">Grid &amp; Rule Studio</span></a>
      </div>
      <nav aria-label="Main" data-track="flex-none" class="relative hidden flex-none before:absolute before:-top-3 before:left-0 before:hidden before:bg-thd14-acc before:px-1 before:font-thd14-mono before:text-[9px] before:leading-4 before:text-white before:content-[attr(data-track)] md:block group-has-[#thd-14-tracks:checked]/thd14:outline-1 group-has-[#thd-14-tracks:checked]/thd14:outline-offset-4 group-has-[#thd-14-tracks:checked]/thd14:outline-thd14-acc group-has-[#thd-14-tracks:checked]/thd14:outline-dashed group-has-[#thd-14-tracks:checked]/thd14:before:block">
        <ul class="flex items-center gap-7 text-sm font-medium">
          <li><a href="#thd-14-main" aria-current="page" class="relative py-2 hover:text-thd14-acc aria-[current=page]:before:absolute aria-[current=page]:before:-left-3 aria-[current=page]:before:top-1/2 aria-[current=page]:before:size-1.5 aria-[current=page]:before:-translate-y-1/2 aria-[current=page]:before:bg-thd14-acc aria-[current=page]:before:content-['']">Work</a></li>
          <li><a href="#thd-14-main" class="py-2 hover:text-thd14-acc">Studio</a></li>
          <li><a href="#thd-14-main" class="py-2 hover:text-thd14-acc">Writing</a></li>
          <li><a href="#thd-14-main" class="py-2 hover:text-thd14-acc">Contact</a></li>
        </ul>
      </nav>
      <div data-track="flex-1 basis-0" class="relative flex min-w-0 flex-1 basis-0 items-center justify-end gap-1 before:absolute before:-top-3 before:right-0 before:hidden before:bg-thd14-acc before:px-1 before:font-thd14-mono before:text-[9px] before:leading-4 before:text-white before:content-[attr(data-track)] group-has-[#thd-14-tracks:checked]/thd14:outline-1 group-has-[#thd-14-tracks:checked]/thd14:outline-offset-4 group-has-[#thd-14-tracks:checked]/thd14:outline-thd14-acc group-has-[#thd-14-tracks:checked]/thd14:outline-dashed group-has-[#thd-14-tracks:checked]/thd14:before:block">
        <input id="thd-14-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-14-t" class="grid size-11 cursor-pointer place-items-center hover:bg-thd14-ink/5 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd14-ink">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-14-t:checked]/thd14:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-14-t:checked]/thd14:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-14-main" class="grid min-h-11 place-items-center whitespace-nowrap bg-thd14-ink px-4 text-sm font-semibold text-thd14-bg transition-colors hover:bg-thd14-acc hover:text-white">Start a project</a>
      </div>
    </div>
  </header>
  <main id="thd-14-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <label class="inline-flex min-h-11 cursor-pointer items-center gap-3 border border-thd14-ink px-3 font-thd14-mono text-xs uppercase tracking-wider">
      <input id="thd-14-tracks" type="checkbox" class="peer/tr sr-only">
      <span aria-hidden="true" class="relative h-5 w-9 border border-thd14-ink transition-colors after:absolute after:left-0.5 after:top-0.5 after:size-3.5 after:bg-thd14-ink after:transition-transform after:content-[''] peer-checked/tr:bg-thd14-acc peer-checked/tr:after:translate-x-4 peer-checked/tr:after:bg-white peer-focus-visible/tr:outline-2 peer-focus-visible/tr:outline-offset-2 peer-focus-visible/tr:outline-thd14-ink"></span>
      Show tracks
    </label>
    <div class="mt-10 grid gap-8 border-t border-thd14-ink pt-6 md:grid-cols-12">
      <p class="font-thd14-mono text-xs uppercase tracking-wider text-thd14-mut md:col-span-3">Index / 014</p>
      <div class="md:col-span-9">
        <h1 class="max-w-[18ch] text-[clamp(2.2rem,6vw,4.2rem)] font-extrabold uppercase leading-[.95] tracking-[-.02em]">The middle stays in the middle.</h1>
        <p class="mt-5 max-w-[52ch] text-thd14-mut">The logo column is far wider than the button column, yet the nav sits on the exact centre line. Flip <em>Show tracks</em> to see the equal <code class="font-thd14-mono">flex-1 basis-0</code> columns.</p>
      </div>
    </div>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd14-bg: var(--thd14-bg);
  --color-thd14-ink: var(--thd14-ink);
  --color-thd14-mut: var(--thd14-mut);
  --color-thd14-acc: var(--thd14-acc);
}

@theme {
  --font-thd14-sans: 'Archivo', system-ui, sans-serif;
  --font-thd14-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.thd-14 {
  width: 100%;
  min-height: 100svh;
  --thd14-bg: #f4f3ef;
  --thd14-ink: #111111;
  --thd14-mut: #555350;
  --thd14-acc: #e1251b;
}

.thd-14:has(#thd-14-t:checked) {
  --thd14-bg: #111111;
  --thd14-ink: #f1efe9;
  --thd14-mut: #aeaba4;
  --thd14-acc: #ff4a3d;
}
```
