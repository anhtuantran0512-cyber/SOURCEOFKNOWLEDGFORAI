---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-gradient-text-hero-section/"
title: "Animated Gradient Text Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "An oversized headline with a marigold → ruby → grape gradient sweeping through two words, over a plum spotlight — plus a real inline waitlist form (email +…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Text Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-gradient-text-hero-section/

An oversized headline with a marigold → ruby → grape gradient sweeping through two words, over a plum spotlight — plus a real inline waitlist form (email + button) instead of a lone link. The Linear / Apple shimmer, made useful.
## HTML
```html
<section class="ths-20 grid w-full min-h-svh place-items-center bg-ths20-bg bg-[radial-gradient(60%_60%_at_50%_0%,var(--color-ths20-glow),transparent_70%)] px-5 py-16 font-ths20-sans text-ths20-cream sm:px-14" aria-label="Animated gradient text hero">
  <div class="max-w-[48rem] text-center">
    <span class="inline-flex items-center gap-2 rounded-full border border-ths20-amber/40 px-3 py-1 font-ths20-mono text-[11px] tracking-[0.16em] text-ths20-amber uppercase"><span aria-hidden="true" class="size-1.5 animate-pulse rounded-full bg-ths20-amber"></span>v3 launching Tuesday</span>
    <h1 class="mt-6 font-ths20-display text-[clamp(42px,6.8vw,80px)] leading-[1.02] font-extrabold tracking-[-0.03em] text-balance">Made for the way <span class="box-decoration-clone animate-ths20-sweep bg-[linear-gradient(90deg,var(--color-ths20-amber),var(--color-ths20-ruby),var(--color-ths20-grape),var(--color-ths20-amber))] bg-size-[200%_100%] bg-clip-text text-transparent motion-reduce:animate-none">creative people</span> actually work.</h1>
    <p class="mx-auto mt-6 max-w-[30rem] text-lg/relaxed text-ths20-mut">One canvas. Every layer. Zero exporting between apps to nudge a kerning pair.</p>
    <form action="#waitlist" class="mx-auto mt-9 flex max-w-md flex-col gap-2 rounded-3xl border border-white/12 bg-white/6 p-1.5 focus-within:ring-2 focus-within:ring-ths20-amber sm:flex-row sm:rounded-full">
      <label for="ths20-email" class="sr-only">Email address</label>
      <input id="ths20-email" type="email" required autocomplete="email" placeholder="[email protected]" class="min-h-12 flex-1 rounded-full bg-transparent px-5 text-[15px] text-ths20-cream placeholder:text-ths20-mut/80 focus:outline-none">
      <button type="submit" class="min-h-12 rounded-full bg-linear-to-r from-ths20-amber to-ths20-ruby px-6 text-[15px] font-bold text-ths20-bg shadow-[0_12px_30px_rgb(214_58_94/0.35)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Join the waitlist</button>
    </form>
    <p class="mt-4 text-xs text-ths20-mut">4,812 designers ahead of you · no spam, one email at launch</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths20-bg: #1a0d20;
  --color-ths20-bg: oklch(0.188 0.042 314.4);
  --color-ths20-glow: #4a1a3e;
  --color-ths20-glow: oklch(0.306 0.088 338.4);
  --color-ths20-cream: #f4e8d0;
  --color-ths20-cream: oklch(0.934 0.034 84.6);
  --color-ths20-mut: #c4b49c;
  --color-ths20-mut: oklch(0.777 0.038 78);
  --color-ths20-amber: #f5b148;
  --color-ths20-amber: oklch(0.806 0.142 74.7);
  --color-ths20-ruby: #e0466a;
  --color-ths20-ruby: oklch(0.621 0.19 10.9);
  --color-ths20-grape: #a052b8;
  --color-ths20-grape: oklch(0.574 0.168 317.7);
  --font-ths20-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ths20-sans: 'Geist', system-ui, sans-serif;
  --font-ths20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths20-sweep: ths20-sweep 4s linear infinite;

  @keyframes ths20-sweep {
    to {
      background-position: 200% 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-20 {
  width: 100%;
  min-height: 100svh;
}
```
