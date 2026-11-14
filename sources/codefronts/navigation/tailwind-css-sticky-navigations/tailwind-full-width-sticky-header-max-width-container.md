---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-full-width-sticky-header-max-width-container/"
title: "Tailwind Full-Width Sticky Header with Max-Width Container"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "Full-bleed bar, contained content, no wrapper div."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Width Sticky Header with Max-Width Container
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-full-width-sticky-header-max-width-container/

Full-bleed bar, contained content, no wrapper div. The header's background runs edge to edge while its logo and links align to the same 72rem measure as the page, using one arbitrary padding: px-[max(1.25rem,calc((100%-72rem)/2))]. Tick “Show measure” to overlay the column guides — a zero-JS has-[:checked] toggle.
## HTML
```html
<div class="tsn-04 group/root w-full min-h-svh bg-tsn04-bg font-tsn04-sans text-tsn04-ink antialiased" aria-label="Full-bleed sticky header with max-width content demo">
  <a href="#tsn-04-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn04-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn04-bg">Skip to content</a>
  <header class="sticky top-0 z-40 bg-tsn04-bar text-white shadow-[0_1px_0_rgb(255_255_255/0.06),0_10px_30px_-12px_rgb(0_0_0/0.45)]">
    <div class="flex h-16 items-center gap-6 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-04-s1" class="flex min-h-11 items-center gap-2.5 rounded-lg font-bold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn04-acc"><span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-tsn04-acc font-tsn04-mono text-sm text-tsn04-bar">A</span>Atlas Docs</a>
      <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
        <a href="#tsn-04-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-md px-3 text-sm font-medium text-white/70 hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn04-acc aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_-2px_0_var(--color-tsn04-acc)]">Guides</a>
        <a href="#tsn-04-s2" class="inline-flex min-h-11 flex-none items-center rounded-md px-3 text-sm font-medium text-white/70 hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn04-acc">API</a>
        <a href="#tsn-04-s3" class="inline-flex min-h-11 flex-none items-center rounded-md px-3 text-sm font-medium text-white/70 hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn04-acc">SDKs</a>
        <a href="#tsn-04-s4" class="inline-flex min-h-11 flex-none items-center rounded-md px-3 text-sm font-medium text-white/70 hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn04-acc">Status</a>
      </nav>
      <label class="inline-flex min-h-11 flex-none cursor-pointer items-center gap-2 rounded-full border border-white/15 px-3.5 text-xs font-semibold text-white/80 select-none hover:border-white/30 has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsn04-acc has-[:checked]:border-tsn04-acc has-[:checked]:text-white">
        <input id="tsn-04-guides" type="checkbox" class="peer sr-only">
        <span aria-hidden="true" class="size-3 rounded-[3px] border border-white/40 peer-checked:border-tsn04-acc peer-checked:bg-tsn04-acc"></span>Show measure
      </label>
    </div>
  </header>
  <div aria-hidden="true" class="pointer-events-none fixed inset-0 z-50 hidden px-[max(1.25rem,calc((100%-72rem)/2))] group-has-[#tsn-04-guides:checked]/root:block">
    <div class="h-full bg-[repeating-linear-gradient(90deg,var(--color-tsn04-guide)_0_calc((100%-11*1.5rem)/12),transparent_calc((100%-11*1.5rem)/12)_calc((100%-11*1.5rem)/12+1.5rem))] outline outline-1 outline-tsn04-acc/60"></div>
  </div>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn04-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn04-acc">full-bleed bar · 72rem measure</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">Edge-to-edge bar, perfectly measured content</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn04-mut text-pretty">Tick “Show measure” in the header. The logo, the links and every section below sit on the same twelve-column grid — and no wrapper div was harmed.</p>
  </div>
  <main id="tsn-04-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-04-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn04-line bg-tsn04-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-04-h1">
      <p class="font-tsn04-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn04-acc">Guides</p>
      <h2 id="tsn-04-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Padding is the container</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn04-mut text-pretty">One arbitrary utility, <code class="rounded-md bg-tsn04-acc/10 px-1.5 py-0.5 font-tsn04-mono text-[0.86em] text-tsn04-ink">px-[max(1.25rem,calc((100%-72rem)/2))]</code>, centres the content while the background keeps running to the edges.</p>
    </section>
    <section id="tsn-04-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn04-line bg-tsn04-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-04-h2">
      <p class="font-tsn04-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn04-acc">API</p>
      <h2 id="tsn-04-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Same formula, every row</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn04-mut text-pretty">Header, main and footer all carry the identical padding utility, so their content edges line up to the pixel at any viewport width.</p>
    </section>
    <section id="tsn-04-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn04-line bg-tsn04-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-04-h3">
      <p class="font-tsn04-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn04-acc">SDKs</p>
      <h2 id="tsn-04-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Percent beats viewport units</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn04-mut text-pretty"><code class="rounded-md bg-tsn04-acc/10 px-1.5 py-0.5 font-tsn04-mono text-[0.86em] text-tsn04-ink">100%</code> is the element’s own width. <code class="rounded-md bg-tsn04-acc/10 px-1.5 py-0.5 font-tsn04-mono text-[0.86em] text-tsn04-ink">100vw</code> includes the scrollbar on Windows and causes a horizontal scroll — this formula never does.</p>
    </section>
    <section id="tsn-04-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn04-line bg-tsn04-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-04-h4">
      <p class="font-tsn04-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn04-acc">Status</p>
      <h2 id="tsn-04-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A toggle with no script</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn04-mut text-pretty">The checkbox sits in the header; the overlay listens through <code class="rounded-md bg-tsn04-acc/10 px-1.5 py-0.5 font-tsn04-mono text-[0.86em] text-tsn04-ink">group-has-[#tsn-04-guides:checked]/root:</code>. State lives in the DOM, styling lives in the class list.</p>
    </section>
  </main>
  <footer class="border-t border-tsn04-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn04-mono text-xs text-tsn04-mut">Tailwind sticky navigation · pattern 04 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn04-bg: #f6f8fb;
  --color-tsn04-bg: oklch(0.977 0.006 250);
  --color-tsn04-surface: #ffffff;
  --color-tsn04-surface: oklch(1 0 0);
  --color-tsn04-bar: #0e1a33;
  --color-tsn04-bar: oklch(0.22 0.05 262);
  --color-tsn04-ink: #141c2e;
  --color-tsn04-ink: oklch(0.23 0.03 262);
  --color-tsn04-mut: #525c70;
  --color-tsn04-mut: oklch(0.47 0.03 262);
  --color-tsn04-acc: #2fc6e0;
  --color-tsn04-acc: oklch(0.77 0.13 210);
  --color-tsn04-line: #141c2e1a;
  --color-tsn04-line: oklch(0.23 0.03 262 / 0.1);
  --color-tsn04-guide: #2fc6e014;
  --color-tsn04-guide: oklch(0.77 0.13 210 / 0.08);
  --font-tsn04-sans: 'Public Sans', system-ui, sans-serif;
  --font-tsn04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-04 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-04) {
    scroll-behavior: smooth;
  }
}
```
