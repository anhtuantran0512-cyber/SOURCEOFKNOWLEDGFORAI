---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-split-navbar-centered-logo/"
title: "Tailwind Split Navbar with Centered Logo"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "Links on both sides, brand dead-centre — the fashion and hospitality header."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Navbar with Centered Logo
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-split-navbar-centered-logo/

Links on both sides, brand dead-centre — the fashion and hospitality header. grid-cols-[1fr_auto_1fr] gives true optical centring however wide each side is, and on phones a native <details> disclosure replaces both navs with a zero-JS dropdown that animates in via open: variants.
## HTML
```html
<div class="tsn-14 w-full min-h-svh bg-tsn14-bg font-tsn14-sans text-tsn14-ink antialiased" aria-label="Split navbar with centered logo demo">
  <a href="#tsn-14-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn14-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn14-bg">Skip to content</a>
  <header class="sticky top-0 z-40 grid h-[4.75rem] grid-cols-[1fr_auto_1fr] items-center gap-4 border-b border-tsn14-line bg-tsn14-bg/90 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-lg">
    <nav aria-label="Shop" class="flex min-w-0 gap-1 max-md:hidden">
      <a href="#tsn-14-s1" aria-current="page" class="inline-flex min-h-11 items-center px-3 text-[13px] uppercase tracking-[0.16em] text-tsn14-mut transition-colors hover:text-tsn14-ink focus-visible:outline-2 focus-visible:outline-tsn14-acc aria-[current=page]:text-tsn14-ink aria-[current=page]:underline aria-[current=page]:decoration-tsn14-acc aria-[current=page]:underline-offset-8">Collections</a>
      <a href="#tsn-14-s2" class="inline-flex min-h-11 items-center px-3 text-[13px] uppercase tracking-[0.16em] text-tsn14-mut transition-colors hover:text-tsn14-ink focus-visible:outline-2 focus-visible:outline-tsn14-acc">Atelier</a>
    </nav>
    <details class="group/menu relative md:hidden">
      <summary class="inline-flex min-h-11 cursor-pointer list-none items-center gap-2 text-[13px] uppercase tracking-[0.16em] focus-visible:outline-2 focus-visible:outline-tsn14-acc [&::-webkit-details-marker]:hidden">Menu <svg class="size-4 transition-transform group-open/menu:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6"/></svg></summary>
      <nav aria-label="Menu" class="absolute left-0 top-full mt-3 grid w-60 gap-1 rounded-2xl border border-tsn14-line bg-tsn14-surface p-2 shadow-[0_20px_40px_-20px_rgb(40_30_20/0.35)] starting:open:opacity-0 starting:open:-translate-y-1 transition-[opacity,translate] duration-200">
        <a href="#tsn-14-s1" class="flex min-h-11 items-center rounded-lg px-3 text-sm hover:bg-tsn14-ink/5">Collections</a>
        <a href="#tsn-14-s2" class="flex min-h-11 items-center rounded-lg px-3 text-sm hover:bg-tsn14-ink/5">Atelier</a>
        <a href="#tsn-14-s3" class="flex min-h-11 items-center rounded-lg px-3 text-sm hover:bg-tsn14-ink/5">Journal</a>
        <a href="#tsn-14-s4" class="flex min-h-11 items-center rounded-lg px-3 text-sm hover:bg-tsn14-ink/5">Appointments</a>
      </nav>
    </details>
    <a href="#tsn-14-s1" class="col-start-2 flex min-h-11 items-center justify-self-center rounded font-tsn14-serif text-[32px] uppercase leading-none tracking-[0.22em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn14-acc">Verre</a>
    <nav aria-label="Account" class="flex min-w-0 justify-end gap-1 max-md:hidden">
      <a href="#tsn-14-s3" class="inline-flex min-h-11 items-center px-3 text-[13px] uppercase tracking-[0.16em] text-tsn14-mut transition-colors hover:text-tsn14-ink focus-visible:outline-2 focus-visible:outline-tsn14-acc">Journal</a>
      <a href="#tsn-14-s4" class="inline-flex min-h-11 items-center px-3 text-[13px] uppercase tracking-[0.16em] text-tsn14-mut transition-colors hover:text-tsn14-ink focus-visible:outline-2 focus-visible:outline-tsn14-acc">Appointments</a>
    </nav>
    <div class="flex justify-end md:hidden"><a href="#tsn-14-s4" class="relative grid size-11 place-items-center rounded-full hover:bg-tsn14-ink/5 focus-visible:outline-2 focus-visible:outline-tsn14-acc"><span class="sr-only">Bag, 2 items</span><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/></svg><span aria-hidden="true" class="absolute right-1.5 top-1.5 size-2 rounded-full bg-tsn14-acc"></span></a></div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn14-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn14-acc">grid-cols-[1fr_auto_1fr]</p>
    <h1 class="mt-4 max-w-[18ch] font-tsn14-serif text-[clamp(44px,7.5vw,96px)] font-normal leading-[0.95] tracking-[-0.01em] text-balance">Centred, whatever the sides weigh</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn14-mut text-pretty">The brand sits on the true centre line even though the link groups differ in width. Narrow the window: a native disclosure takes over, no script involved.</p>
  </div>
  <main id="tsn-14-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid pb-24">
    <section id="tsn-14-s1" class="scroll-mt-24 min-h-[48svh] border-t border-tsn14-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-14-h1">
      <p class="font-tsn14-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn14-acc">Collections</p>
      <h2 id="tsn-14-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Equal tracks, honest centre</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn14-mut text-pretty">Two <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">1fr</code> columns around an <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">auto</code> centre keep the brand on the axis. Flexbox would only centre it if both sides matched.</p>
    </section>
    <section id="tsn-14-s2" class="scroll-mt-24 min-h-[48svh] border-t border-tsn14-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-14-h2">
      <p class="font-tsn14-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn14-acc">Atelier</p>
      <h2 id="tsn-14-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Hidden cells are free cells</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn14-mut text-pretty">On phones the side navs are <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">max-md:hidden</code>, so the menu and the bag button auto-place into columns one and three of the same grid.</p>
    </section>
    <section id="tsn-14-s3" class="scroll-mt-24 min-h-[48svh] border-t border-tsn14-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-14-h3">
      <p class="font-tsn14-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn14-acc">Journal</p>
      <h2 id="tsn-14-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A menu with no script</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn14-mut text-pretty">The mobile menu is a <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">&lt;details&gt;</code>. <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">group-open/menu:rotate-180</code> turns the chevron and <code class="rounded-md bg-tsn14-acc/10 px-1.5 py-0.5 font-tsn14-mono text-[0.86em] text-tsn14-ink">starting:open:</code> fades the panel in.</p>
    </section>
    <section id="tsn-14-s4" class="scroll-mt-24 min-h-[48svh] border-t border-tsn14-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-14-h4">
      <p class="font-tsn14-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn14-acc">Appointments</p>
      <h2 id="tsn-14-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Quiet luxury, legible</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn14-mut text-pretty">Small caps-style labels at 13px with wide tracking, but muted ink held at 5.9:1 — elegance never at the cost of reading.</p>
    </section>
  </main>
  <footer class="border-t border-tsn14-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn14-mono text-xs text-tsn14-mut">Tailwind sticky navigation · pattern 14 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn14-bg: #f7f3ec;
  --color-tsn14-bg: oklch(0.965 0.012 80);
  --color-tsn14-surface: #fffcf6;
  --color-tsn14-surface: oklch(0.99 0.008 80);
  --color-tsn14-ink: #231d17;
  --color-tsn14-ink: oklch(0.23 0.015 60);
  --color-tsn14-mut: #62574b;
  --color-tsn14-mut: oklch(0.47 0.025 65);
  --color-tsn14-acc: #9a6a35;
  --color-tsn14-acc: oklch(0.56 0.1 65);
  --color-tsn14-line: #231d171f;
  --color-tsn14-line: oklch(0.23 0.015 60 / 0.12);
  --font-tsn14-serif: 'Instrument Serif', Georgia, serif;
  --font-tsn14-sans: 'Jost', system-ui, sans-serif;
  --font-tsn14-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-14 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-14) {
    scroll-behavior: smooth;
  }
}
```
