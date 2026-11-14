---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-navbar-animated-hover-underline/"
title: "Tailwind CSS Navbar with Animated Hover Underline"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "The foundation of every site header, rebuilt in utilities: a sticky, frosted navbar whose links draw an underline with after:scale-x-*."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Navbar with Animated Hover Underline
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-navbar-animated-hover-underline/

The foundation of every site header, rebuilt in utilities: a sticky, frosted navbar whose links draw an underline with after:scale-x-*. The line grows in from the left and retracts to the right, the active page is styled from aria-current itself, and a native <details> menu takes over below md.
## HTML
```html
<div class="tnv-01 flex min-h-svh w-full flex-col bg-tnv01-bg font-tnv01-sans text-tnv01-ink antialiased selection:bg-tnv01-acc selection:text-white">
  <header class="sticky top-0 z-20 border-b border-tnv01-line bg-white/80 backdrop-blur-md">
    <nav aria-label="Main" class="relative mx-auto flex h-16 max-w-6xl items-center justify-between gap-6 px-5 sm:px-8">
      <a href="#" class="flex items-center gap-2.5 rounded-md text-lg font-semibold tracking-[-0.02em] outline-none focus-visible:ring-2 focus-visible:ring-tnv01-acc/40"><span aria-hidden="true" class="size-2 rounded-full bg-tnv01-acc shadow-[0_0_0_4px_var(--color-tnv01-acc-soft)]"></span>Clarity</a>
      <ul class="hidden items-center gap-0.5 md:flex">
        <li><a href="#" aria-current="page" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Home</a></li>
        <li><a href="#" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Products</a></li>
        <li><a href="#" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Features</a></li>
        <li><a href="#" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Pricing</a></li>
        <li><a href="#" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Blog</a></li>
        <li><a href="#" class="relative flex h-11 items-center rounded-md px-3.5 text-sm font-medium text-tnv01-mut outline-none transition-colors duration-200 after:pointer-events-none after:absolute after:inset-x-3.5 after:bottom-1.5 after:h-0.5 after:origin-right after:scale-x-0 after:rounded-full after:bg-tnv01-acc after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] after:content-[''] hover:text-tnv01-ink hover:after:origin-left hover:after:scale-x-100 focus-visible:text-tnv01-ink focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:text-tnv01-ink aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">About</a></li>
      </ul>
      <div class="flex items-center gap-2.5">
        <a href="#" class="hidden h-10 items-center rounded-lg border border-tnv01-line px-4 text-sm font-medium transition-colors hover:border-slate-300 hover:bg-tnv01-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv01-acc sm:inline-flex">Sign in</a>
        <a href="#" class="inline-flex h-10 items-center gap-1.5 rounded-lg bg-tnv01-acc px-4 text-sm font-medium text-white shadow-[0_1px_0_0_rgb(255_255_255/0.2)_inset,0_6px_16px_-6px_var(--color-tnv01-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv01-acc">Get started</a>
        <details class="group/m md:hidden">
          <summary aria-label="Menu" class="grid size-11 cursor-pointer list-none place-items-center rounded-lg border border-tnv01-line bg-white outline-none focus-visible:ring-2 focus-visible:ring-tnv01-acc/40 [&::-webkit-details-marker]:hidden">
            <svg class="size-5 group-open/m:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>
            <svg class="hidden size-5 group-open/m:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
          </summary>
          <ul class="absolute inset-x-3 top-[calc(100%+8px)] grid gap-0.5 rounded-2xl border border-tnv01-line bg-white p-2 text-[15px] font-medium shadow-[0_24px_48px_-16px_rgb(15_23_42/0.25)] transition-[opacity,translate] duration-200 starting:-translate-y-1 starting:opacity-0">
            <li><a href="#" aria-current="page" class="flex min-h-11 items-center rounded-lg px-3 aria-[current=page]:bg-tnv01-acc-soft aria-[current=page]:text-tnv01-acc hover:bg-tnv01-bg">Home</a></li>
            <li><a href="#" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-tnv01-bg">Products</a></li>
            <li><a href="#" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-tnv01-bg">Features</a></li>
            <li><a href="#" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-tnv01-bg">Pricing</a></li>
            <li><a href="#" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-tnv01-bg">Blog</a></li>
            <li><a href="#" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-tnv01-bg">About</a></li>
          </ul>
        </details>
      </div>
    </nav>
  </header>
  <main class="grid flex-1 place-items-center px-5 py-20 text-center [&_code]:rounded [&_code]:bg-slate-100 [&_code]:px-1.5 [&_code]:py-px [&_code]:font-tnv01-mono [&_code]:text-[0.85em] [&_code]:text-tnv01-ink">
    <div class="grid max-w-2xl justify-items-center">
      <span class="mb-6 inline-flex items-center gap-2 rounded-full bg-tnv01-acc-soft px-3 py-1 text-xs font-semibold tracking-[0.08em] text-tnv01-acc uppercase">Pure Tailwind · zero JS</span>
      <h1 class="text-[clamp(2.25rem,5.5vw,3.75rem)] leading-[1.06] font-semibold tracking-[-0.035em] text-balance">Hover the nav. The underline follows your intent.</h1>
      <p class="mt-5 max-w-xl text-[17px]/[1.65] text-tnv01-mut text-pretty">Each link draws its indicator with <code>after:scale-x-*</code>. It grows in from the left and retracts to the right, and keyboard focus gets exactly the same treatment.</p>
      <div class="mt-10 flex max-w-lg items-start gap-3 rounded-xl border border-tnv01-line bg-white p-4 text-left text-[13px]/[1.55] text-tnv01-mut shadow-[0_1px_2px_rgb(15_23_42/0.04)]">
        <svg class="mt-px size-[18px] flex-none text-tnv01-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
        <span>Press <kbd class="rounded border border-tnv01-line bg-tnv01-bg px-1.5 font-tnv01-mono text-[11px]">Tab</kbd> to walk the links. The active page is styled from <code>aria-current</code>, so the visual state and the screen-reader state can never drift apart.</span>
      </div>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv01-bg: #f8fafc;
  --color-tnv01-bg: oklch(0.984 0.003 248);
  --color-tnv01-line: #e2e8f0;
  --color-tnv01-line: oklch(0.929 0.013 256);
  --color-tnv01-ink: #1e293b;
  --color-tnv01-ink: oklch(0.279 0.041 260);
  --color-tnv01-mut: #475569;
  --color-tnv01-mut: oklch(0.446 0.043 257);
  --color-tnv01-acc: #2563eb;
  --color-tnv01-acc: oklch(0.546 0.245 263);
  --color-tnv01-acc-soft: #dbeafe;
  --color-tnv01-acc-soft: oklch(0.932 0.032 256);
  --font-tnv01-sans: 'Geist', system-ui, sans-serif;
  --font-tnv01-mono: 'Geist Mono', ui-monospace, monospace;
}

.tnv-01 {
  width: 100%;
  min-height: 100svh;
}
```
