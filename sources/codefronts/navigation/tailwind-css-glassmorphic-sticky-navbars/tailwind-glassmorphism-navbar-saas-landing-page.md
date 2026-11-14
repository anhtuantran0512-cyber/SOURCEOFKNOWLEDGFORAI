---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-glassmorphism-navbar-saas-landing-page/"
title: "Tailwind Glassmorphism Navbar for SaaS Landing Pages"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "The query everyone types: a floating frosted-glass SaaS header over a vibrant gradient hero — brand, centred links, ghost sign-in and a gradient CTA."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Navbar for SaaS Landing Pages
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-glassmorphism-navbar-saas-landing-page/

The query everyone types: a floating frosted-glass SaaS header over a vibrant gradient hero — brand, centred links, ghost sign-in and a gradient CTA. The CSS original's glass trio is now bg-white/50 border-white/60 backdrop-blur-lg backdrop-saturate-[1.8], and the links it simply hid on phones now live in a zero-JS Popover API glass menu.
## HTML
```html
<div class="tgn-01 w-full min-h-svh bg-tgn01-g2 bg-[radial-gradient(120%_120%_at_12%_0%,var(--color-tgn01-g1)_0%,var(--color-tgn01-g2)_40%,var(--color-tgn01-g3)_100%)] font-tgn01-sans">
  <div class="relative h-svh overflow-y-auto scroll-smooth p-3 sm:p-5">
    <header class="sticky top-3 z-10 flex h-16 items-center gap-4 rounded-2xl border border-white/60 bg-white/50 py-2.5 pr-2.5 pl-4 shadow-[0_8px_30px_-6px_oklch(0.25_0.1_285/0.35)] backdrop-blur-lg backdrop-saturate-[1.8] not-supports-[backdrop-filter:blur(1px)]:bg-white/90 sm:pl-5">
      <a class="flex items-center gap-2.5 rounded-lg font-tgn01-display text-lg font-extrabold tracking-[-0.03em] text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink" href="#"><span aria-hidden="true" class="grid size-8 place-items-center rounded-[10px] bg-linear-to-br from-tgn01-cta1 to-tgn01-cta2 text-xs text-white shadow-[0_4px_12px_-2px_var(--color-tgn01-cta2)]">◆</span>Nimbus</a>
      <nav class="mx-auto max-md:hidden" aria-label="Primary">
        <ul class="flex gap-1">
          <li><a href="#" aria-current="page" class="flex h-11 items-center rounded-xl px-3.5 text-sm font-semibold text-tgn01-ink/80 transition-colors hover:bg-white/55 hover:text-tgn01-ink aria-[current=page]:bg-white/70 aria-[current=page]:text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Product</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-xl px-3.5 text-sm font-semibold text-tgn01-ink/80 transition-colors hover:bg-white/55 hover:text-tgn01-ink aria-[current=page]:bg-white/70 aria-[current=page]:text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Pricing</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-xl px-3.5 text-sm font-semibold text-tgn01-ink/80 transition-colors hover:bg-white/55 hover:text-tgn01-ink aria-[current=page]:bg-white/70 aria-[current=page]:text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Docs</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-xl px-3.5 text-sm font-semibold text-tgn01-ink/80 transition-colors hover:bg-white/55 hover:text-tgn01-ink aria-[current=page]:bg-white/70 aria-[current=page]:text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Blog</a></li>
        </ul>
      </nav>
      <div class="flex items-center gap-1.5 max-md:ml-auto">
        <a href="#" class="flex h-11 items-center rounded-xl px-3.5 text-sm font-semibold text-tgn01-ink/80 transition-colors hover:bg-white/55 hover:text-tgn01-ink aria-[current=page]:bg-white/70 aria-[current=page]:text-tgn01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink max-sm:hidden">Sign in</a>
        <a href="#" class="group flex h-11 items-center gap-1.5 rounded-xl bg-linear-to-br from-tgn01-cta1 to-tgn01-cta2 px-4 text-sm font-bold text-white shadow-[0_8px_20px_-4px_var(--color-tgn01-cta2)] transition-[translate,box-shadow] duration-150 hover:-translate-y-0.5 hover:shadow-[0_12px_26px_-4px_var(--color-tgn01-cta2)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none sm:px-5">Start free<span aria-hidden="true" class="transition-transform group-hover:translate-x-0.5">→</span></a>
        <button type="button" popovertarget="tgn01-menu" aria-label="Open menu" class="grid size-11 cursor-pointer place-items-center rounded-xl text-tgn01-ink hover:bg-white/55 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink md:hidden"><svg class="size-5" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg></button>
      </div>
    </header>
    <nav id="tgn01-menu" popover aria-label="Mobile primary" class="fixed inset-x-3 top-20 bottom-auto m-0 w-auto rounded-2xl border border-white/70 bg-white/65 p-2 font-tgn01-sans text-tgn01-ink opacity-0 shadow-[0_20px_50px_-12px_oklch(0.25_0.1_285/0.45)] backdrop-blur-xl backdrop-saturate-[1.8] transition-[opacity,translate,overlay,display] transition-discrete duration-200 -translate-y-2 open:translate-y-0 open:opacity-100 starting:open:-translate-y-2 starting:open:opacity-0 motion-reduce:transition-none">
      <a href="#" aria-current="page" class="flex h-12 items-center rounded-xl px-4 text-[15px] font-semibold text-tgn01-ink hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Product</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[15px] font-semibold text-tgn01-ink hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Pricing</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[15px] font-semibold text-tgn01-ink hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Docs</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[15px] font-semibold text-tgn01-ink hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink">Blog</a>
      <a href="#" class="flex h-12 items-center rounded-xl px-4 text-[15px] font-semibold text-tgn01-ink hover:bg-white/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn01-ink mt-1 border-t border-tgn01-ink/10 rounded-t-none">Sign in</a>
    </nav>
    <div class="max-w-xl px-2 pt-16 pb-6 sm:px-3.5">
      <p class="mb-4 inline-flex rounded-full border border-white/40 bg-white/20 px-3 py-1.5 text-xs font-bold tracking-[0.14em] text-white uppercase backdrop-blur-sm">Ship faster</p>
      <h2 class="font-tgn01-display text-[clamp(30px,5.4vw,46px)]/[1.04] font-extrabold tracking-[-0.035em] text-balance text-white [text-shadow:0_2px_24px_oklch(0.2_0.1_300/0.3)]">The workspace your whole team ships from.</h2>
    </div>
    <div class="max-w-2xl px-2 pt-6 pb-20 text-white/95 [text-shadow:0_1px_6px_oklch(0.25_0.1_300/0.35)] sm:px-3.5 [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:font-tgn01-display [&_:is(h2,h3)]:text-white [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn01-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-white/40 [&_code]:bg-white/25 [&_code]:text-white [&_code]:[text-shadow:none]">
      <p>The floating glass header stays pinned to the top as you scroll. Translucent white fill + <code>backdrop-filter:blur(16px) saturate(180%)</code> + a 1px hairline — the classic trio.</p>
      <p>The <code>saturate(180%)</code> boost is the secret sauce most Tailwind snippets miss. Plain <code>blur()</code> alone looks grey and dead; boosting saturation makes the frosted pane feel like it's actually made of the colours behind it.</p>
      <p>Dark link text stays high-contrast even as the gradient shifts underneath, because the fill is white-ish and ≥45% opaque. The blur alone is never enough to guarantee contrast; the fill opacity is the actual floor.</p>
      <p>The CTA is a linear-gradient pill with its own coloured shadow so it reads as the single most important control on the page. It lifts on hover with a subtle <code>translateY(-2px)</code>.</p>
      <p>For a darker product, flip the fill to <code>rgba(17,17,20,.5)</code> and link colour to near-white — the same structure works as a dark SaaS header without changing a single selector.</p>
      <p>Tailwind users: the class equivalent is <code>sticky top-4 backdrop-blur-xl backdrop-saturate-150 bg-white/50 border border-white/60 rounded-2xl shadow-lg</code>. Every declaration maps to a utility class or arbitrary value.</p>
      <h3>Why saturate matters more than blur radius</h3>
      <p>Increasing the blur radius past 20-24px starts to cost frames on low-end Android hardware. Increasing the saturation stops at zero cost — saturation is a colour matrix operation, not a spatial convolution.</p>
      <p>Practical range: <code>blur(12px)</code> at <code>saturate(180%)</code> reads as premium and stays smooth. <code>blur(24px)</code> at <code>saturate(120%)</code> reads as heavy privacy-glass but taxes older devices. Pick the trade-off deliberately.</p>
      <p>Test the header over your <em>lightest</em> hero, not your darkest. Dark heroes hide contrast bugs; light heroes reveal them.</p>
      <h3>Layout hygiene for sticky glass headers</h3>
      <p>The header must have a fixed <code>height</code> declaration (56px in this demo). Sticky elements with intrinsic height can shift as fonts swap in — a real Cumulative Layout Shift hit that Google's Core Web Vitals reports.</p>
      <p>Keep the sticky header out of ancestors with <code>overflow:hidden</code> on the block axis. This is the single most common sticky-fails-silently bug — the header renders once at the top and never moves.</p>
      <p>Give the containing element a defined block-size (the outer wrapper here is <code>min-height:100vh</code>). Sticky without a resolvable containing block behaves like static.</p>
      <p>Above 1200px viewport, consider raising the nav's max-width to keep the CTA anchored to the right edge rather than floating in a wide gap. Below 640px, collapse the primary links into a hamburger and keep the CTA prominent.</p>
      <h3>Real SaaS marketing sites shipping this pattern</h3>
      <p>Stripe uses a variant with heavier saturation over its animated gradient hero. Linear uses a near-black variant with cyan accent. Vercel uses white glass with brand purple CTA. Superhuman uses navy glass with peach CTA. Framer uses a pill variant of the same recipe (see Demo 04).</p>
      <p>Every one of them ships the same three-declaration recipe: translucent fill + <code>backdrop-filter:blur() saturate()</code> + 1px hairline. The palette differs; the structure doesn't.</p>
      <p>Keep scrolling — the sticky bar demonstrates its main job by staying pinned as the content flows underneath it.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn01-g1: #b981ff;
  --color-tgn01-g1: oklch(0.72 0.2 300);
  --color-tgn01-g2: #438aff;
  --color-tgn01-g2: oklch(0.65 0.19 260);
  --color-tgn01-g3: #00bac5;
  --color-tgn01-g3: oklch(0.7 0.16 200);
  --color-tgn01-ink: #211c48;
  --color-tgn01-ink: oklch(0.26 0.08 285);
  --color-tgn01-cta1: #e20c35;
  --color-tgn01-cta1: oklch(0.58 0.23 22);
  --color-tgn01-cta2: #c4008d;
  --color-tgn01-cta2: oklch(0.54 0.24 345);
  --font-tgn01-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tgn01-sans: 'Geist', system-ui, sans-serif;
  --font-tgn01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-01 {
  width: 100%;
  min-height: 100svh;
}
```
