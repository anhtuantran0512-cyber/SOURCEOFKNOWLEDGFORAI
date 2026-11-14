---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-clip-path-text-reveal-hover-animation/"
title: "Tailwind Clip-Path Text Reveal Hover Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Three title-sequence reveals for a motion studio's reel index: a diagonal polygon() wipe, a circle() bloom that uncovers a photo inside the letters, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Clip-Path Text Reveal Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-clip-path-text-reveal-hover-animation/

Three title-sequence reveals for a motion studio's reel index: a diagonal polygon() wipe, a circle() bloom that uncovers a photo inside the letters, and 12-point venetian blinds. Each row is one class list: [clip-path:…] at rest, group-hover/row:[clip-path:…] on hover — same function, same point count, so it tweens.
## HTML
```html
<section class="tth-30 @container w-full min-h-svh grid place-items-center bg-tth30-bg bg-[radial-gradient(90%_75%_at_50%_15%,var(--color-tth30-glow),var(--color-tth30-bg)_72%)] px-5 py-14 font-tth30-sans text-tth30-ink" aria-label="Clip path reveal demo">
  <div class="flex w-full max-w-[48.75rem] flex-col gap-[clamp(16px,3cqi,26px)]">
    <header class="flex flex-wrap items-center justify-between gap-3.5 border-b border-tth30-line pb-3.5">
      <p class="text-xs font-bold uppercase tracking-[0.22em] text-tth30-mut">Studio Meridian &mdash; title sequences &amp; type systems</p>
      <span class="rounded-full border border-tth30-acc/40 px-3 py-1.5 font-tth30-mono text-[11px] text-tth30-acc @max-[35rem]:hidden">same shape, same points &rarr; it tweens</span>
    </header>
    <div class="flex flex-col">
      <a id="tth30-top" href="#tth30-top" class="group/row flex items-end justify-between gap-4 rounded-md border-b border-tth30-line px-1 py-[clamp(14px,2.6cqi,22px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth30-acc">
        <span class="flex flex-col gap-1.5"><span class="font-tth30-mono text-[10.5px] uppercase tracking-[0.1em] text-tth30-mut">01 &middot; diagonal wipe &middot; polygon()</span><span class="relative inline-block w-fit font-tth30-display text-[clamp(44px,9cqi,88px)] font-black uppercase leading-[1.02] tracking-[0.01em]"><span class="block text-tth30-ink/34">SEQUENCE</span><span aria-hidden="true" class="pointer-events-none absolute inset-0 block text-tth30-acc [clip-path:polygon(-15%_0%,0%_0%,-15%_100%,-30%_100%)] transition-[clip-path] duration-650 ease-[cubic-bezier(.7,0,.2,1)] group-hover/row:[clip-path:polygon(0%_0%,130%_0%,115%_100%,-15%_100%)] group-focus-visible/row:[clip-path:polygon(0%_0%,130%_0%,115%_100%,-15%_100%)] motion-reduce:transition-none">SEQUENCE</span></span></span>
        <span class="mb-2 flex -translate-x-2 items-center gap-2 whitespace-nowrap text-[13px] font-semibold text-tth30-acc opacity-0 transition-[opacity,translate] duration-400 group-hover/row:translate-x-0 group-hover/row:opacity-100 group-focus-visible/row:opacity-100 pointer-coarse:translate-x-0 pointer-coarse:opacity-100 @max-[30rem]:hidden">View reel <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a href="#tth30-top" class="group/row flex items-end justify-between gap-4 rounded-md border-b border-tth30-line px-1 py-[clamp(14px,2.6cqi,22px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth30-acc">
        <span class="flex flex-col gap-1.5"><span class="font-tth30-mono text-[10.5px] uppercase tracking-[0.1em] text-tth30-mut">02 &middot; circle bloom &middot; circle() + photo-in-text</span><span class="relative inline-block w-fit font-tth30-display text-[clamp(44px,9cqi,88px)] font-black uppercase leading-[1.02] tracking-[0.01em]"><span class="block text-tth30-ink/34">HORIZON</span><span aria-hidden="true" style="--tth30-photo:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1400&auto=format&fit=crop')" class="pointer-events-none absolute inset-0 block bg-[image:linear-gradient(oklch(0.6_0.1_260/0.15),oklch(0.6_0.1_260/0.15)),var(--tth30-photo),linear-gradient(160deg,var(--color-tth30-acc),oklch(0.6_0.17_330))] bg-cover bg-center bg-clip-text text-transparent [clip-path:circle(0%_at_50%_55%)] transition-[clip-path] duration-700 ease-[cubic-bezier(.3,.85,.25,1)] group-hover/row:[clip-path:circle(75%_at_50%_55%)] group-focus-visible/row:[clip-path:circle(75%_at_50%_55%)] motion-reduce:transition-none">HORIZON</span></span></span>
        <span class="mb-2 flex -translate-x-2 items-center gap-2 whitespace-nowrap text-[13px] font-semibold text-tth30-acc opacity-0 transition-[opacity,translate] duration-400 group-hover/row:translate-x-0 group-hover/row:opacity-100 group-focus-visible/row:opacity-100 pointer-coarse:translate-x-0 pointer-coarse:opacity-100 @max-[30rem]:hidden">View reel <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a href="#tth30-top" class="group/row flex items-end justify-between gap-4 rounded-md border-b border-tth30-line px-1 py-[clamp(14px,2.6cqi,22px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth30-acc">
        <span class="flex flex-col gap-1.5"><span class="font-tth30-mono text-[10.5px] uppercase tracking-[0.1em] text-tth30-mut">03 &middot; blinds &middot; 12-point polygon</span><span class="relative inline-block w-fit font-tth30-display text-[clamp(44px,9cqi,88px)] font-black uppercase leading-[1.02] tracking-[0.01em]"><span class="block text-tth30-ink/34">INTERVAL</span><span aria-hidden="true" class="pointer-events-none absolute inset-0 block text-tth30-acc [clip-path:polygon(0%_100%,0%_0%,0%_0%,0%_100%,33.3%_100%,33.3%_0%,33.3%_0%,33.3%_100%,66.6%_100%,66.6%_0%,66.6%_0%,66.6%_100%)] transition-[clip-path] duration-600 ease-[cubic-bezier(.6,0,.25,1)] group-hover/row:[clip-path:polygon(0%_100%,0%_0%,33.3%_0%,33.3%_100%,33.3%_100%,33.3%_0%,66.6%_0%,66.6%_100%,66.6%_100%,66.6%_0%,100%_0%,100%_100%)] group-focus-visible/row:[clip-path:polygon(0%_100%,0%_0%,33.3%_0%,33.3%_100%,33.3%_100%,33.3%_0%,66.6%_0%,66.6%_100%,66.6%_100%,66.6%_0%,100%_0%,100%_100%)] motion-reduce:transition-none">INTERVAL</span></span></span>
        <span class="mb-2 flex -translate-x-2 items-center gap-2 whitespace-nowrap text-[13px] font-semibold text-tth30-acc opacity-0 transition-[opacity,translate] duration-400 group-hover/row:translate-x-0 group-hover/row:opacity-100 group-focus-visible/row:opacity-100 pointer-coarse:translate-x-0 pointer-coarse:opacity-100 @max-[30rem]:hidden">View reel <span aria-hidden="true">&rarr;</span></span>
      </a>
    </div>
    <p class="max-w-[62ch] text-[12.5px] leading-[1.7] text-tth30-mut">Hover each row. Three shapes, one law: clip-path only interpolates between the same function with the same point count &mdash; design the two states as siblings first.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth30-bg: #13121a;
  --color-tth30-bg: oklch(0.2 0.012 285);
  --color-tth30-glow: #1c1a25;
  --color-tth30-glow: oklch(0.24 0.016 290);
  --color-tth30-ink: #eeedf3;
  --color-tth30-ink: oklch(0.94 0.008 280);
  --color-tth30-mut: #a29fae;
  --color-tth30-mut: oklch(0.73 0.02 285);
  --color-tth30-acc: #f3a53c;
  --color-tth30-acc: oklch(0.78 0.16 65);
  --color-tth30-line: #35333f;
  --color-tth30-line: oklch(0.34 0.02 285);
  --font-tth30-display: 'Big Shoulders Display', Impact, sans-serif;
  --font-tth30-sans: 'Outfit', system-ui, sans-serif;
  --font-tth30-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-30 {
  width: 100%;
  min-height: 100svh;
}
```
