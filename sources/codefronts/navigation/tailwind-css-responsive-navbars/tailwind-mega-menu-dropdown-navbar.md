---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-mega-menu-dropdown-navbar/"
title: "Tailwind Mega Menu Dropdown Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The three-column mega panel with icon cards, ported without a single descendant selector: group on the nav item, group-hover:/group-focus-within: on the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu Dropdown Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-mega-menu-dropdown-navbar/

The three-column mega panel with icon cards, ported without a single descendant selector: group on the nav item, group-hover:/group-focus-within: on the panel, grid-cols-3 inside it. On mobile the same sections become native <details> disclosures — which is what the CSS version's flattened link list wanted to be.
## HTML
```html
<div class="tnb-02 group w-full min-h-svh bg-tnb02-page font-tnb02-sans text-tnb02-ink" aria-label="Mega menu dropdown navbar demo">
  <input type="checkbox" id="tnb02-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-200 border-b border-tnb02-edge bg-white shadow-[0_1px_3px_oklch(0_0_0/0.06)]">
    <nav class="mx-auto flex h-17 max-w-6xl items-center gap-6 px-5 md:px-8" aria-label="Primary">
      <a href="#home" class="shrink-0 text-xl font-bold tracking-[-0.03em] text-tnb02-ink no-underline">Nova<span class="text-tnb02-acc">.</span></a>
      <ul class="hidden flex-1 list-none items-center gap-0 md:flex">
        <li class="group/item relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
          <a href="#products" class="flex items-center gap-1 rounded-lg px-4 py-2 text-sm font-medium whitespace-nowrap text-tnb02-ink no-underline transition-colors duration-150 hover:bg-tnb02-tint hover:text-tnb02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb02-acc">Products <span class="inline-block text-[11px] leading-none text-tnb02-mut transition-transform duration-200 group-hover/item:rotate-180 group-hover/item:text-tnb02-acc group-focus-within/item:rotate-180 motion-reduce:transition-none" aria-hidden="true">&#9662;</span></a>
          <div class="pointer-events-none invisible absolute top-[calc(100%+8px)] -left-4 grid w-175 -translate-y-2 grid-cols-3 gap-6 rounded-2xl border border-tnb02-edge bg-white p-6 opacity-0 shadow-[0_20px_60px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-200 ease-out group-hover/item:pointer-events-auto group-hover/item:visible group-hover/item:translate-y-0 group-hover/item:opacity-100 group-focus-within/item:pointer-events-auto group-focus-within/item:visible group-focus-within/item:translate-y-0 group-focus-within/item:opacity-100 motion-reduce:transition-none">
            <div>
              <p class="mb-3 text-[11px] font-semibold tracking-[0.08em] uppercase text-tnb02-mut">Core tools</p>
              <a href="#design" class="group/card mb-1 flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base transition-colors group-hover/card:bg-tnb02-tint2" aria-hidden="true">&#127912;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Design Studio</span><span class="block text-xs leading-snug text-tnb02-mut">Pixel-perfect interfaces</span></span></a>
              <a href="#proto" class="group/card flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base transition-colors group-hover/card:bg-tnb02-tint2" aria-hidden="true">&#9889;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Prototyping</span><span class="block text-xs leading-snug text-tnb02-mut">Interactive mockups in minutes</span></span></a>
            </div>
            <div>
              <p class="mb-3 text-[11px] font-semibold tracking-[0.08em] uppercase text-tnb02-mut">Collaboration</p>
              <a href="#teams" class="group/card mb-1 flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base transition-colors group-hover/card:bg-tnb02-tint2" aria-hidden="true">&#128101;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Teams</span><span class="block text-xs leading-snug text-tnb02-mut">Real-time multiplayer editing</span></span></a>
              <a href="#comments" class="group/card flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base transition-colors group-hover/card:bg-tnb02-tint2" aria-hidden="true">&#128172;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Comments</span><span class="block text-xs leading-snug text-tnb02-mut">Contextual feedback flows</span></span></a>
            </div>
            <div class="rounded-xl bg-linear-[135deg,var(--color-tnb02-tint),var(--color-tnb02-tint2)] p-5">
              <p class="mb-2 text-[11px] font-semibold tracking-[0.08em] uppercase text-tnb02-acc">Featured</p>
              <p class="mb-1.5 text-base font-bold text-tnb02-ink">Nova 3.0 is here</p>
              <p class="mb-4 text-xs leading-snug text-tnb02-mut">Variable fonts, live components and an API that finally makes sense.</p>
              <a href="#whats-new" class="text-sm font-semibold text-tnb02-acc no-underline hover:underline">What's new &rarr;</a>
            </div>
          </div>
        </li>
        <li class="group/item relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
          <a href="#solutions" class="flex items-center gap-1 rounded-lg px-4 py-2 text-sm font-medium whitespace-nowrap text-tnb02-ink no-underline transition-colors duration-150 hover:bg-tnb02-tint hover:text-tnb02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb02-acc">Solutions <span class="inline-block text-[11px] leading-none text-tnb02-mut transition-transform duration-200 group-hover/item:rotate-180 group-hover/item:text-tnb02-acc group-focus-within/item:rotate-180 motion-reduce:transition-none" aria-hidden="true">&#9662;</span></a>
          <div class="pointer-events-none invisible absolute top-[calc(100%+8px)] -left-4 grid w-140 -translate-y-2 grid-cols-2 gap-6 rounded-2xl border border-tnb02-edge bg-white p-6 opacity-0 shadow-[0_20px_60px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-200 ease-out group-hover/item:pointer-events-auto group-hover/item:visible group-hover/item:translate-y-0 group-hover/item:opacity-100 group-focus-within/item:pointer-events-auto group-focus-within/item:visible group-focus-within/item:translate-y-0 group-focus-within/item:opacity-100 motion-reduce:transition-none">
            <div>
              <p class="mb-3 text-[11px] font-semibold tracking-[0.08em] uppercase text-tnb02-mut">By team</p>
              <a href="#enterprise" class="mb-1 flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base" aria-hidden="true">&#127970;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Enterprise</span><span class="block text-xs leading-snug text-tnb02-mut">Advanced security &amp; compliance</span></span></a>
              <a href="#startups" class="flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base" aria-hidden="true">&#128640;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Startups</span><span class="block text-xs leading-snug text-tnb02-mut">Move fast, ship beautiful</span></span></a>
            </div>
            <div>
              <p class="mb-3 text-[11px] font-semibold tracking-[0.08em] uppercase text-tnb02-mut">By role</p>
              <a href="#designers" class="mb-1 flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base" aria-hidden="true">&#9999;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Designers</span><span class="block text-xs leading-snug text-tnb02-mut">Your complete design OS</span></span></a>
              <a href="#developers" class="flex items-start gap-3 rounded-xl p-2.5 no-underline transition-colors duration-150 hover:bg-tnb02-tint focus-visible:bg-tnb02-tint focus-visible:outline-none"><span class="grid size-9 shrink-0 place-items-center rounded-lg bg-tnb02-tint text-base" aria-hidden="true">&#128187;</span><span><span class="block text-sm font-semibold text-tnb02-ink">Developers</span><span class="block text-xs leading-snug text-tnb02-mut">Inspect &amp; export real code</span></span></a>
            </div>
          </div>
        </li>
        <li><a href="#pricing" class="flex rounded-lg px-4 py-2 text-sm font-medium text-tnb02-ink no-underline transition-colors duration-150 hover:bg-tnb02-tint hover:text-tnb02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb02-acc">Pricing</a></li>
        <li><a href="#blog" class="flex rounded-lg px-4 py-2 text-sm font-medium text-tnb02-ink no-underline transition-colors duration-150 hover:bg-tnb02-tint hover:text-tnb02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb02-acc">Blog</a></li>
      </ul>
      <div class="hidden shrink-0 items-center gap-3 md:flex">
        <a href="#login" class="rounded-lg px-4 py-2 text-sm font-semibold text-tnb02-ink no-underline transition-colors hover:bg-tnb02-hover">Log in</a>
        <a href="#try" class="rounded-lg bg-tnb02-acc px-4 py-2 text-sm font-semibold text-white no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb02-accdark motion-reduce:transition-none motion-reduce:hover:translate-y-0">Try for free</a>
      </div>
      <label for="tnb02-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb02-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb02-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb02-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-t border-tnb02-edge px-5 py-3 max-md:group-has-checked:block">
      <details class="group/dis border-b border-tnb02-edge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between text-[15px] font-semibold text-tnb02-ink marker:content-none">Products <span class="text-xs text-tnb02-mut transition-transform duration-200 group-open/dis:rotate-180" aria-hidden="true">&#9662;</span></summary>
        <div class="grid pb-2">
          <a href="#design" class="flex min-h-11 items-center gap-2.5 rounded-lg px-2 text-sm text-tnb02-mut no-underline hover:text-tnb02-acc"><span aria-hidden="true">&#127912;</span>Design Studio</a>
          <a href="#proto" class="flex min-h-11 items-center gap-2.5 rounded-lg px-2 text-sm text-tnb02-mut no-underline hover:text-tnb02-acc"><span aria-hidden="true">&#9889;</span>Prototyping</a>
          <a href="#teams" class="flex min-h-11 items-center gap-2.5 rounded-lg px-2 text-sm text-tnb02-mut no-underline hover:text-tnb02-acc"><span aria-hidden="true">&#128101;</span>Teams</a>
        </div>
      </details>
      <details class="group/dis border-b border-tnb02-edge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between text-[15px] font-semibold text-tnb02-ink marker:content-none">Solutions <span class="text-xs text-tnb02-mut transition-transform duration-200 group-open/dis:rotate-180" aria-hidden="true">&#9662;</span></summary>
        <div class="grid pb-2">
          <a href="#enterprise" class="flex min-h-11 items-center gap-2.5 rounded-lg px-2 text-sm text-tnb02-mut no-underline hover:text-tnb02-acc"><span aria-hidden="true">&#127970;</span>Enterprise</a>
          <a href="#startups" class="flex min-h-11 items-center gap-2.5 rounded-lg px-2 text-sm text-tnb02-mut no-underline hover:text-tnb02-acc"><span aria-hidden="true">&#128640;</span>Startups</a>
        </div>
      </details>
      <a href="#pricing" class="flex min-h-11 items-center border-b border-tnb02-edge text-[15px] font-semibold text-tnb02-ink no-underline">Pricing</a>
      <a href="#blog" class="flex min-h-11 items-center border-b border-tnb02-edge text-[15px] font-semibold text-tnb02-ink no-underline">Blog</a>
      <a href="#try" class="mt-3 flex min-h-11 items-center justify-center rounded-lg bg-tnb02-acc text-sm font-semibold text-white no-underline">Try for free</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 text-4xl font-bold tracking-[-0.03em] text-tnb02-ink">Mega Menu Dropdown Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb02-mut">Hover — or <strong class="font-semibold text-tnb02-ink">Tab into</strong> — Products or Solutions. The panel is a <code class="rounded bg-tnb02-tint px-1.5 py-0.5 text-[0.9em] text-tnb02-acc">grid-cols-3</code> inside a <code class="rounded bg-tnb02-tint px-1.5 py-0.5 text-[0.9em] text-tnb02-acc">group-hover:</code> panel, and keyboard users get the same menu the mouse does.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb02-page: #ffffff;
  --color-tnb02-page: oklch(1 0 0);
  --color-tnb02-ink: #1a1a2e;
  --color-tnb02-ink: oklch(0.24 0.04 280);
  --color-tnb02-mut: #6b7280;
  --color-tnb02-mut: oklch(0.55 0.02 265);
  --color-tnb02-edge: #e5e7eb;
  --color-tnb02-edge: oklch(0.91 0.005 265);
  --color-tnb02-hover: #f3f4f6;
  --color-tnb02-hover: oklch(0.96 0.003 265);
  --color-tnb02-tint: #fdf2f8;
  --color-tnb02-tint: oklch(0.97 0.02 340);
  --color-tnb02-tint2: #fce7f3;
  --color-tnb02-tint2: oklch(0.94 0.04 345);
  --color-tnb02-acc: #e84393;
  --color-tnb02-acc: oklch(0.63 0.21 350);
  --color-tnb02-accdark: #d1236a;
  --color-tnb02-accdark: oklch(0.56 0.21 350);
  --font-tnb02-sans: 'DM Sans', system-ui, sans-serif;
}

.tnb-02 {
  width: 100%;
  min-height: 100svh;
}

.tnb-02 ::selection {
  background: var(--color-tnb02-acc);
  color: #fff;
}
/* <summary> marker removal needs a pseudo-element selector with no variant form. */

.tnb-02 summary::-webkit-details-marker {
  display: none;
}
```
