---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-blog-index-card-stack-split-hero/"
title: "Tailwind Blog Index Card Stack with Split Hero"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A blog index rather than a lone card: a split hero with a fixed thumbnail column, then two equal tiles beneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blog Index Card Stack with Split Hero
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-blog-index-card-stack-split-hero/

A blog index rather than a lone card: a split hero with a fixed thumbnail column, then two equal tiles beneath. The port's win is that the hero's 240px 1fr split and its single-column mobile fallback sit in the same class list, so the breakpoint is legible at the element that breaks.
## HTML
```html
<section class="twc-06 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc06-bg [background-image:radial-gradient(ellipse_at_20%_20%,oklch(0.55_0.2_275/0.06),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.68_0.2_350/0.05),transparent_50%)] font-twc06-sans">
  <div class="w-full max-w-[720px] flex flex-col gap-3.5">

    <header class="flex max-[600px]:flex-col max-[600px]:items-start items-center justify-between gap-3 px-1">
      <div class="flex flex-col gap-0.5">
        <span class="inline-flex items-center gap-1.5 font-twc06-mono text-[10px] font-extrabold tracking-[0.16em] text-twc06-acc">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc06-pink shadow-[0_0_8px_oklch(0.68_0.2_350/0.5)] animate-twc06-pulse motion-reduce:animate-none"></span>
          THE JOURNAL
        </span>
        <h3 class="m-0 text-xl font-extrabold tracking-[-0.025em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Latest posts</h3>
      </div>
      <a href="#archive" class="inline-flex items-center gap-1 min-h-11 px-2.5 rounded-lg no-underline text-xs font-bold text-twc06-ink2 transition-[color,background] duration-200 hover:text-twc06-ink hover:bg-black/4 focus-visible:outline-2 focus-visible:outline-twc06-acc focus-visible:outline-offset-2">
        Archive
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </header>

    <article class="group/card grid grid-cols-[240px_1fr] max-[600px]:grid-cols-1 overflow-hidden rounded-twc06-card bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc06-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative isolate overflow-hidden bg-twc06-ink max-[600px]:min-h-40">
        <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200&q=80&auto=format&fit=crop" alt="CSS code in an editor" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-106 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
        <div aria-hidden="true" class="absolute inset-0 pointer-events-none [background:linear-gradient(180deg,transparent_0%,oklch(0_0_0/0.35)_100%)]"></div>
        <span class="absolute top-2.5 left-2.5 px-2 py-[3px] rounded-[5px] [background:linear-gradient(180deg,#fef3c7,#fde68a)] text-twc06-amberdeep font-twc06-mono text-[9px] font-extrabold tracking-[0.14em] border border-twc06-amberink/20 shadow-[0_2px_5px_oklch(0.78_0.15_70/0.28)]">FEATURED</span>
        <span class="absolute bottom-2.5 right-2.5 inline-flex items-center gap-1 px-[7px] py-[3px] rounded-[5px] bg-black/55 backdrop-blur-[6px] border border-white/16 text-white text-[10px] font-bold tracking-[0.02em]">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          6 min
        </span>
      </div>
      <div class="flex flex-col justify-center gap-2 px-6 py-5">
        <span class="self-start px-2.5 py-[3px] rounded-full font-twc06-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc06-accdeep bg-twc06-acc/8 border border-twc06-acc/16">Engineering</span>
        <h3 class="m-0 text-[17px]/[1.3] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Why Container Queries Change Everything About Responsive Design</h3>
        <p class="m-0 min-h-[3em] text-[12.5px]/[1.5] text-twc06-muted line-clamp-2">The most-requested CSS feature is finally shipping in every browser. Here's what changes about the way we think.</p>
        <div class="grid grid-cols-[30px_1fr_auto] items-center gap-2 mt-1.5 pt-2.5 border-t border-dashed border-black/10">
          <span aria-hidden="true" class="flex items-center justify-center size-7.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#6366f1,#ec4899)] text-white text-[10.5px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.08)]">AC</span>
          <div class="flex flex-col min-w-0">
            <span class="inline-flex items-center gap-1">
              <span class="text-xs font-bold text-twc06-ink">Alex Chen</span>
              <svg role="img" aria-label="Verified author" width="11" height="11" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="inline-flex items-center gap-1 text-[10.5px] text-twc06-dim [font-variant-numeric:tabular-nums]">
              <time datetime="2026-07-08">Jul 8</time>
              <span aria-hidden="true" class="text-twc06-hair">&middot;</span>
              42k reads
            </span>
          </div>
          <button type="button" aria-label="Save article" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border border-black/6 text-twc06-muted cursor-pointer transition-[color,background,border-color,transform] duration-200 hover:text-twc06-acc hover:bg-twc06-acc/6 hover:border-twc06-acc/25 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc06-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
        </div>
      </div>
    </article>

    <div class="grid grid-cols-2 max-[600px]:grid-cols-1 gap-3.5">
      <article class="group/card flex flex-col overflow-hidden rounded-twc06-card bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc06-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative isolate h-32.5 overflow-hidden bg-twc06-ink">
          <img src="https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=600&q=80&auto=format&fit=crop" alt="Design workspace with sketches" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-106 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute bottom-2.5 right-2.5 px-1.5 py-0.5 rounded-[5px] bg-black/55 backdrop-blur-[6px] border border-white/16 text-white text-[9px] font-bold tracking-[0.02em]">4 min</span>
        </div>
        <div class="flex flex-col gap-1.5 px-3.5 py-3">
          <span class="self-start px-2.5 py-[3px] rounded-full font-twc06-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc06-accdeep bg-twc06-acc/8 border border-twc06-acc/16">Design</span>
          <h4 class="m-0 mt-0.5 text-[13px]/[1.3] font-extrabold tracking-[-0.015em] text-twc06-ink line-clamp-2">The Case Against Perfect Loading States</h4>
          <div class="flex items-center gap-1.5 mt-2 pt-2 border-t border-dashed border-black/8 text-[10.5px] text-twc06-dim">
            <span aria-hidden="true" class="flex flex-none items-center justify-center size-5.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#67e8f9,#0891b2)] text-white text-[9px] font-extrabold">EK</span>
            <span class="text-[11px] font-bold text-twc06-ink truncate">Emil Kowalski</span>
            <span aria-hidden="true" class="text-twc06-hair">&middot;</span>
            <time datetime="2026-07-05">Jul 5</time>
          </div>
        </div>
      </article>

      <article class="group/card flex flex-col overflow-hidden rounded-twc06-card bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc06-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative isolate h-32.5 overflow-hidden bg-twc06-ink">
          <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80&auto=format&fit=crop" alt="Server infrastructure at night" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-106 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute top-2.5 left-2.5 px-2 py-[3px] rounded-[5px] bg-twc06-red/90 text-white font-twc06-mono text-[9px] font-extrabold tracking-[0.14em] border border-white/15 shadow-[0_2px_5px_oklch(0.58_0.22_25/0.3)]">NEW</span>
          <span class="absolute bottom-2.5 right-2.5 px-1.5 py-0.5 rounded-[5px] bg-black/55 backdrop-blur-[6px] border border-white/16 text-white text-[9px] font-bold tracking-[0.02em]">8 min</span>
        </div>
        <div class="flex flex-col gap-1.5 px-3.5 py-3">
          <span class="self-start px-2.5 py-[3px] rounded-full font-twc06-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc06-accdeep bg-twc06-acc/8 border border-twc06-acc/16">Infrastructure</span>
          <h4 class="m-0 mt-0.5 text-[13px]/[1.3] font-extrabold tracking-[-0.015em] text-twc06-ink line-clamp-2">Why Local-First is the Future of Web Apps</h4>
          <div class="flex items-center gap-1.5 mt-2 pt-2 border-t border-dashed border-black/8 text-[10.5px] text-twc06-dim">
            <span aria-hidden="true" class="flex flex-none items-center justify-center size-5.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#fdba74,#ea580c)] text-white text-[9px] font-extrabold">RF</span>
            <span class="text-[11px] font-bold text-twc06-ink truncate">Rauno Freiberg</span>
            <span aria-hidden="true" class="text-twc06-hair">&middot;</span>
            <time datetime="2026-07-08">Today</time>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc06-bg: #f5f4f0;
  --color-twc06-bg: oklch(0.96 0.005 90);
  --color-twc06-ink: #1a1a1a;
  --color-twc06-ink: oklch(0.21 0.005 270);
  --color-twc06-ink2: #4b4b57;
  --color-twc06-ink2: oklch(0.4 0.015 280);
  --color-twc06-muted: #6b6b7c;
  --color-twc06-muted: oklch(0.51 0.02 285);
  --color-twc06-dim: #9ca3af;
  --color-twc06-dim: oklch(0.71 0.02 265);
  --color-twc06-hair: #cbd5e1;
  --color-twc06-hair: oklch(0.85 0.02 250);
  --color-twc06-acc: #6366f1;
  --color-twc06-acc: oklch(0.55 0.2 275);
  --color-twc06-accdeep: #4338ca;
  --color-twc06-accdeep: oklch(0.42 0.21 275);
  --color-twc06-pink: #ec4899;
  --color-twc06-pink: oklch(0.68 0.2 350);
  --color-twc06-red: #dc2626;
  --color-twc06-red: oklch(0.58 0.22 25);
  --color-twc06-amberink: #92400e;
  --color-twc06-amberink: oklch(0.44 0.12 55);
  --color-twc06-amberdeep: #78350f;
  --color-twc06-amberdeep: oklch(0.38 0.1 55);
  --font-twc06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc06-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --radius-twc06-card: 20px;
  --animate-twc06-pulse: twc06-pulse 2s ease-in-out infinite;
}

@keyframes twc06-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

.twc-06 {
  width: 100%;
  min-height: 100svh;
}
```
