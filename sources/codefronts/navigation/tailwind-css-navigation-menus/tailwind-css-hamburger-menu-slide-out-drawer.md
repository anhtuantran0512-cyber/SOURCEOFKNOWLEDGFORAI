---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-hamburger-menu-slide-out-drawer/"
title: "Tailwind CSS Hamburger Menu with Slide-Out Drawer"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A mobile-first header whose three-bar icon morphs into an X and slides a dark drawer in from the right, with a blurred backdrop and links that cascade in one…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hamburger Menu with Slide-Out Drawer
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-hamburger-menu-slide-out-drawer/

A mobile-first header whose three-bar icon morphs into an X and slides a dark drawer in from the right, with a blurred backdrop and links that cascade in one after another. State comes from one sr-only checkbox read by group-has-checked/root:, so the toggle works from the keyboard too. Zero JavaScript.
## HTML
```html
<div class="tnv-04 group/root min-h-svh w-full bg-tnv04-bg font-tnv04-sans text-tnv04-ink antialiased selection:bg-tnv04-acc selection:text-white">
  <input type="checkbox" id="tnv04-toggle" class="sr-only" aria-controls="tnv04-drawer">
  <header class="sticky top-0 z-50 border-b-2 border-tnv04-line bg-white/90 backdrop-blur-md">
    <nav aria-label="Main" class="mx-auto flex h-16 max-w-6xl items-center justify-between px-5">
      <a href="#" class="text-[1.35rem] font-bold tracking-[-0.03em]">Mo<span class="text-tnv04-acc">ve</span></a>
      <label for="tnv04-toggle" aria-label="Toggle menu" class="relative z-50 grid size-11 cursor-pointer place-items-center rounded-xl transition-colors select-none hover:bg-tnv04-line group-has-checked/root:bg-tnv04-drawer group-has-[#tnv04-toggle:focus-visible]/root:ring-2 group-has-[#tnv04-toggle:focus-visible]/root:ring-tnv04-acc group-has-[#tnv04-toggle:focus-visible]/root:ring-offset-2">
        <span class="grid gap-[5px]">
          <span class="block h-0.5 w-[22px] rounded-full bg-tnv04-ink transition-[translate,rotate,background-color] duration-300 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-y-[7px] group-has-checked/root:rotate-45 group-has-checked/root:bg-white"></span>
          <span class="block h-0.5 w-[14px] justify-self-end rounded-full bg-tnv04-ink transition-[opacity,scale] duration-200 group-has-checked/root:scale-x-0 group-has-checked/root:opacity-0"></span>
          <span class="block h-0.5 w-[22px] rounded-full bg-tnv04-ink transition-[translate,rotate,background-color] duration-300 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:-translate-y-[7px] group-has-checked/root:-rotate-45 group-has-checked/root:bg-white"></span>
        </span>
      </label>
    </nav>
  </header>
  <label for="tnv04-toggle" aria-hidden="true" class="pointer-events-none fixed inset-0 z-30 bg-stone-950/0 transition-[background-color,backdrop-filter] duration-300 group-has-checked/root:pointer-events-auto group-has-checked/root:bg-stone-950/50 group-has-checked/root:backdrop-blur-[3px]"></label>
  <aside id="tnv04-drawer" aria-label="Navigation drawer" class="invisible fixed inset-y-0 right-0 z-40 flex w-[min(20rem,86vw)] translate-x-full flex-col overflow-y-auto bg-tnv04-drawer pt-16 text-white shadow-[-24px_0_60px_-20px_rgb(0_0_0/0.5)] transition-[translate,visibility] duration-[400ms] ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:visible group-has-checked/root:translate-x-0 motion-reduce:transition-none">
    <ul class="flex-1 space-y-0.5 p-4 [&_a]:flex [&_a]:min-h-12 [&_a]:items-center [&_a]:gap-3 [&_a]:rounded-xl [&_a]:px-3.5 [&_a]:text-[15px] [&_a]:font-medium [&_a]:text-white/75 [&_a]:outline-none [&_a]:transition-colors [&_a:focus-visible]:ring-2 [&_a:focus-visible]:ring-tnv04-acc [&_a:hover]:bg-white/[0.06] [&_a:hover]:text-white [&_svg]:size-[18px] [&_svg]:flex-none [&_svg]:opacity-60">
      <li style="--i:1" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#" aria-current="page" class="aria-[current=page]:!bg-tnv04-acc/15 aria-[current=page]:!text-white aria-[current=page]:[&_svg]:!text-tnv04-acc aria-[current=page]:[&_svg]:!opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/></svg>Home</a></li>
      <li style="--i:2" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>Products</a></li>
      <li style="--i:3" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><path d="M7 7h.01"/></svg>Pricing</a></li>
      <li style="--i:4" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2zM22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>Docs</a></li>
      <li role="separator" class="mx-3.5 my-2 h-px bg-white/[0.08]"></li>
      <li style="--i:5" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>Community</a></li>
      <li style="--i:6" class="translate-x-6 opacity-0 transition-[translate,opacity] delay-[calc(var(--i)*45ms)] duration-500 ease-[cubic-bezier(.23,1,.32,1)] group-has-checked/root:translate-x-0 group-has-checked/root:opacity-100 motion-reduce:transition-none"><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>Support</a></li>
    </ul>
    <div class="border-t border-white/[0.08] p-4">
      <a href="#" class="flex min-h-12 items-center justify-center gap-2 rounded-xl bg-tnv04-acc font-semibold text-white shadow-[0_10px_30px_-10px_var(--color-tnv04-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Get started free<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      <p class="mt-3 text-center text-xs text-white/55">No credit card required</p>
    </div>
  </aside>
  <main class="grid place-items-center px-5 py-24 text-center [&_code]:rounded [&_code]:bg-tnv04-line [&_code]:px-1.5 [&_code]:font-tnv04-mono [&_code]:text-[0.85em]">
    <h1 class="max-w-xl text-[clamp(2.25rem,6vw,3.5rem)] leading-[1.08] font-bold tracking-[-0.035em] text-balance">A drawer that opens from the keyboard, too</h1>
    <p class="mt-4 max-w-md text-base/[1.7] text-tnv04-mut text-pretty">One <code>sr-only</code> checkbox, read by <code>group-has-checked/root:</code>. The icon morphs, the drawer slides with <code>translate-x</code>, and the links cascade in on every open.</p>
    <span class="mt-8 inline-flex items-center gap-2 rounded-full border-2 border-tnv04-line bg-white px-4 py-2.5 text-sm font-semibold text-tnv04-acc-ink">
      <svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>Tap the menu icon, or Tab to it and press Space
    </span>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv04-bg: #fffbf7;
  --color-tnv04-bg: oklch(0.991 0.006 60);
  --color-tnv04-line: #fde8d8;
  --color-tnv04-line: oklch(0.94 0.03 55);
  --color-tnv04-ink: #1c1917;
  --color-tnv04-ink: oklch(0.216 0.006 56);
  --color-tnv04-mut: #57534e;
  --color-tnv04-mut: oklch(0.444 0.011 74);
  --color-tnv04-drawer: #1c1917;
  --color-tnv04-drawer: oklch(0.216 0.006 56);
  --color-tnv04-acc: #f97316;
  --color-tnv04-acc: oklch(0.705 0.213 48);
  --color-tnv04-acc-ink: #c2410c;
  --color-tnv04-acc-ink: oklch(0.553 0.195 38);
  --font-tnv04-sans: 'Outfit', system-ui, sans-serif;
  --font-tnv04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-04 {
  width: 100%;
  min-height: 100svh;
}
```
