---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/neumorphic-sticky-navbar-tailwind-css/"
title: "Neumorphic Sticky Navbar in Tailwind CSS"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "Soft-UI done responsibly: a floating sticky bar extruded from the page with paired light/dark shadows, links that rise on hover and press into the surface…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Sticky Navbar in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/neumorphic-sticky-navbar-tailwind-css/

Soft-UI done responsibly: a floating sticky bar extruded from the page with paired light/dark shadows, links that rise on hover and press into the surface when active. The shadows are @theme tokens (shadow-tsn15-out, shadow-tsn15-in), and the usual neumorphism failure — invisible text and focus — is fixed with full-strength ink and an accent focus ring.
## HTML
```html
<div class="tsn-15 w-full min-h-svh bg-tsn15-bg font-tsn15-sans text-tsn15-ink antialiased" aria-label="Neumorphic sticky navbar demo">
  <a href="#tsn-15-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn15-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn15-bg">Skip to content</a>
  <header class="sticky top-3 z-40 mx-[max(0.75rem,calc((100%-72rem)/2))] flex min-h-[4.25rem] items-center gap-3 rounded-[1.75rem] bg-tsn15-bg px-3 shadow-tsn15-out sm:gap-6">
    <a href="#tsn-15-s1" class="flex min-h-11 flex-none items-center gap-2.5 rounded-2xl pl-1 pr-2 font-bold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc"><span aria-hidden="true" class="grid size-10 place-items-center rounded-2xl bg-tsn15-bg text-tsn15-acc shadow-tsn15-in"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span><span class="max-sm:sr-only">Soft OS</span></a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-2 overflow-x-auto p-2 [scrollbar-width:none]">
      <a href="#tsn-15-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-2xl px-4 text-sm font-semibold text-tsn15-mut transition-[box-shadow,color] duration-200 hover:text-tsn15-ink hover:shadow-tsn15-out active:shadow-tsn15-in focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc aria-[current=page]:text-tsn15-acc aria-[current=page]:shadow-tsn15-in">Home</a>
      <a href="#tsn-15-s2" class="inline-flex min-h-11 flex-none items-center rounded-2xl px-4 text-sm font-semibold text-tsn15-mut transition-[box-shadow,color] duration-200 hover:text-tsn15-ink hover:shadow-tsn15-out active:shadow-tsn15-in focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc">Devices</a>
      <a href="#tsn-15-s3" class="inline-flex min-h-11 flex-none items-center rounded-2xl px-4 text-sm font-semibold text-tsn15-mut transition-[box-shadow,color] duration-200 hover:text-tsn15-ink hover:shadow-tsn15-out active:shadow-tsn15-in focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc">Scenes</a>
      <a href="#tsn-15-s4" class="inline-flex min-h-11 flex-none items-center rounded-2xl px-4 text-sm font-semibold text-tsn15-mut transition-[box-shadow,color] duration-200 hover:text-tsn15-ink hover:shadow-tsn15-out active:shadow-tsn15-in focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc">Energy</a>
    </nav>
    <a href="#tsn-15-s4" class="grid size-11 flex-none place-items-center rounded-2xl text-tsn15-mut shadow-tsn15-out transition-[box-shadow,color] hover:text-tsn15-acc active:shadow-tsn15-in focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn15-acc"><span class="sr-only">Account</span><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn15-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn15-acc">shadow-tsn15-out · shadow-tsn15-in</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">Soft to the touch, sharp to the eye</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn15-mut text-pretty">Hover a link to raise it, press to push it in. The current page stays pressed — and turns accent, because a shadow alone is not a state.</p>
  </div>
  <main id="tsn-15-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-15-s1" class="scroll-mt-28 min-h-[44svh] rounded-[2rem] bg-tsn15-bg p-[clamp(1.5rem,4vw,3rem)] shadow-tsn15-out" aria-labelledby="tsn-15-h1">
      <p class="font-tsn15-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn15-acc">Home</p>
      <h2 id="tsn-15-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Two shadows make a surface</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn15-mut text-pretty">A dark shadow bottom-right and a white one top-left, on an element the colour of the page, read as moulded plastic. Inset, they read as pressed.</p>
    </section>
    <section id="tsn-15-s2" class="scroll-mt-28 min-h-[44svh] rounded-[2rem] bg-tsn15-bg p-[clamp(1.5rem,4vw,3rem)] shadow-tsn15-out" aria-labelledby="tsn-15-h2">
      <p class="font-tsn15-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn15-acc">Devices</p>
      <h2 id="tsn-15-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Shadows as tokens</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn15-mut text-pretty">Registered in <code class="rounded-md bg-tsn15-acc/10 px-1.5 py-0.5 font-tsn15-mono text-[0.86em] text-tsn15-ink">@theme</code>, each shadow mints a utility that works with every variant: <code class="rounded-md bg-tsn15-acc/10 px-1.5 py-0.5 font-tsn15-mono text-[0.86em] text-tsn15-ink">hover:</code>, <code class="rounded-md bg-tsn15-acc/10 px-1.5 py-0.5 font-tsn15-mono text-[0.86em] text-tsn15-ink">active:</code>, <code class="rounded-md bg-tsn15-acc/10 px-1.5 py-0.5 font-tsn15-mono text-[0.86em] text-tsn15-ink">aria-[current=page]:</code>.</p>
    </section>
    <section id="tsn-15-s3" class="scroll-mt-28 min-h-[44svh] rounded-[2rem] bg-tsn15-bg p-[clamp(1.5rem,4vw,3rem)] shadow-tsn15-out" aria-labelledby="tsn-15-h3">
      <p class="font-tsn15-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn15-acc">Scenes</p>
      <h2 id="tsn-15-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Fixing soft-UI’s blind spot</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn15-mut text-pretty">Neumorphism usually greys out text and hides focus. Here ink is full strength and focus draws a 2px accent ring that the shadows cannot swallow.</p>
    </section>
    <section id="tsn-15-s4" class="scroll-mt-28 min-h-[44svh] rounded-[2rem] bg-tsn15-bg p-[clamp(1.5rem,4vw,3rem)] shadow-tsn15-out" aria-labelledby="tsn-15-h4">
      <p class="font-tsn15-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn15-acc">Energy</p>
      <h2 id="tsn-15-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Floating, not bolted on</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn15-mut text-pretty">The bar sits 12px from the top with <code class="rounded-md bg-tsn15-acc/10 px-1.5 py-0.5 font-tsn15-mono text-[0.86em] text-tsn15-ink">sticky top-3</code> and rounded corners, so the page’s soft surface continues around it.</p>
    </section>
  </main>
  <footer class="border-t border-tsn15-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn15-mono text-xs text-tsn15-mut">Tailwind sticky navigation · pattern 15 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn15-bg: #e4e8ef;
  --color-tsn15-bg: oklch(0.925 0.01 260);
  --color-tsn15-surface: #e4e8ef;
  --color-tsn15-surface: oklch(0.925 0.01 260);
  --color-tsn15-ink: #1f2533;
  --color-tsn15-ink: oklch(0.25 0.025 265);
  --color-tsn15-mut: #4f5668;
  --color-tsn15-mut: oklch(0.44 0.03 265);
  --color-tsn15-acc: #3d5bd9;
  --color-tsn15-acc: oklch(0.52 0.19 268);
  --color-tsn15-line: #1f25331a;
  --color-tsn15-line: oklch(0.25 0.025 265 / 0.1);
  --font-tsn15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsn15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tsn15-out: 7px 7px 16px #bec4d0, -7px -7px 16px #ffffff;
  --shadow-tsn15-in: inset 4px 4px 9px #bec4d0, inset -4px -4px 9px #ffffff;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-15 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-15) {
    scroll-behavior: smooth;
  }
}
```
