---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-testimonial-card-sentiment-strip/"
title: "Tailwind Testimonial Card with Sentiment Strip"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A customer quote with a star pill, a giant decorative quote mark, a sentiment strip, a verified-customer proof row and a helpful counter."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Testimonial Card with Sentiment Strip
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-testimonial-card-sentiment-strip/

A customer quote with a star pill, a giant decorative quote mark, a sentiment strip, a verified-customer proof row and a helpful counter. The port's win is layer order made explicit: isolate on the card plus -z-10 / z-0 / relative z-1 on the three decorative planes, instead of a six-selector rule that lifted all the content at once.
## HTML
```html
<section class="twc-08 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc08-bg [background-image:radial-gradient(ellipse_at_20%_20%,oklch(0.78_0.16_70/0.06),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.48_0.09_185/0.06),transparent_50%)] font-twc08-sans">

  <article class="relative isolate w-full max-w-[400px] overflow-hidden rounded-[22px] bg-white border border-black/5 px-5.5 pt-5 pb-4 shadow-[0_30px_60px_-30px_oklch(0.45_0.06_75/0.24),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-30px_oklch(0.45_0.06_75/0.32)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div aria-hidden="true" class="absolute -top-20 -right-20 size-65 -z-10 pointer-events-none blur-[30px] [background:radial-gradient(circle,oklch(0.78_0.16_70/0.16)_0%,transparent_55%),radial-gradient(circle_at_60%_60%,oklch(0.68_0.2_350/0.09)_0%,transparent_55%)]"></div>
    <div aria-hidden="true" class="absolute -top-[30%] -left-[20%] w-3/5 h-[160%] z-0 rotate-15 pointer-events-none [background:linear-gradient(115deg,transparent_30%,oklch(0.78_0.16_70/0.04)_45%,oklch(0.68_0.2_350/0.04)_50%,oklch(0.48_0.09_185/0.04)_55%,transparent_70%)]"></div>
    <span aria-hidden="true" class="absolute -top-5 right-3 z-0 select-none pointer-events-none font-twc08-serif text-[140px]/none font-bold text-twc08-amber/10 max-[380px]:hidden">&ldquo;</span>

    <header class="relative z-1 flex items-center justify-between gap-3 mb-3.5">
      <div class="flex items-center gap-1.5">
        <div role="img" aria-label="Rated 4.9 out of 5" class="inline-flex gap-0.5 px-1.5 py-[3px] rounded-full bg-twc08-amber/10 border border-twc08-amber/22 text-twc08-amber">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        </div>
        <span class="text-sm font-extrabold tracking-[-0.02em] text-twc08-amberink [font-variant-numeric:tabular-nums]">4.9<span class="ml-px text-[11px] font-semibold text-twc08-dim">/5</span></span>
      </div>
      <span class="inline-flex items-center gap-1 px-2.5 py-[3px] rounded-full [background:linear-gradient(180deg,#fef3c7,#fde68a)] text-twc08-amberdeep font-twc08-mono text-[9.5px] font-extrabold tracking-[0.1em] uppercase border border-twc08-amberink/22 shadow-[0_2px_4px_oklch(0.78_0.15_70/0.25)]">
        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
        Staff pick
      </span>
    </header>

    <blockquote cite="https://example.com/reviews/12483" class="relative z-1 m-0 mb-3.5 text-[15.5px]/[1.55] font-medium tracking-[-0.01em] text-twc08-ink">
      We shipped 3&times; faster after switching. The team stopped worrying about infrastructure and started shipping features that actually move the needle.
    </blockquote>

    <div aria-hidden="true" class="relative z-1 h-[3px] mb-4.5 rounded-sm overflow-hidden bg-twc08-amber/15">
      <span class="block w-[65%] h-full rounded-sm [background:linear-gradient(90deg,#f59e0b,#ec4899)]"></span>
    </div>

    <div class="relative z-1 grid grid-cols-[44px_1fr] items-center gap-3 mb-3.5">
      <div class="relative">
        <span aria-hidden="true" class="flex items-center justify-center size-11 rounded-full border-2 border-white [background:linear-gradient(135deg,#f59e0b,#ef4444)] text-white text-sm font-extrabold shadow-[0_4px_12px_oklch(0.63_0.22_25/0.28)]">PS</span>
        <span aria-hidden="true" class="absolute -bottom-0.5 -right-0.5 flex items-center justify-center size-4 rounded-full bg-twc08-green border-2 border-white shadow-[0_2px_4px_oklch(0.72_0.18_145/0.35)]">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
        </span>
      </div>
      <cite class="flex flex-col gap-px min-w-0 not-italic">
        <span class="inline-flex items-center gap-1">
          <span class="text-[13.5px] font-bold tracking-[-0.01em] text-twc08-ink">Priya Sharma</span>
          <svg role="img" aria-label="Verified customer" width="12" height="12" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <span class="inline-flex items-center gap-1 text-[11.5px] text-twc08-muted">
          CTO at
          <span class="inline-flex items-center gap-1.5 font-bold text-twc08-ink">
            <span aria-hidden="true" class="inline-block flex-none size-3.5 rounded [background:linear-gradient(135deg,transparent_40%,oklch(1_0_0/0.4)_55%,transparent_70%),linear-gradient(135deg,#4338ca_0%,#a855f7_100%)] shadow-[0_1px_3px_oklch(0.42_0.21_275/0.35)]"></span>
            Meridian Labs
          </span>
        </span>
      </cite>
    </div>

    <div class="relative z-1 flex items-center justify-between gap-3 mb-3.5 px-3 py-2.5 rounded-[10px] bg-twc08-green/6 border border-twc08-green/18">
      <div class="inline-flex items-center gap-1.5 text-[11px] font-bold text-twc08-greenink">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc08-green"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        Verified customer
      </div>
      <time datetime="2026-06-14" class="text-[10.5px] text-twc08-muted [font-variant-numeric:tabular-nums]">Jun 14, 2026</time>
    </div>

    <footer class="relative z-1 flex items-center justify-between gap-2 pt-3 border-t border-dashed border-black/10">
      <button type="button" class="inline-flex items-center gap-1.5 min-h-11 px-3 rounded-full bg-transparent border border-black/8 text-twc08-ink2 text-[11.5px] font-bold cursor-pointer transition-[color,background,border-color] duration-200 hover:text-twc08-greenink hover:bg-twc08-green/6 hover:border-twc08-green/25 focus-visible:outline-2 focus-visible:outline-twc08-amber focus-visible:outline-offset-[3px]">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z"/><line x1="6" y1="10" x2="6" y2="22"/></svg>
        Helpful &middot; 234
      </button>
      <a href="#reviews" class="inline-flex items-center gap-1 min-h-11 px-2 rounded-md no-underline text-[11.5px] font-bold text-twc08-amberink transition-[color,background] duration-200 hover:text-twc08-amberdeep hover:bg-twc08-amber/8 focus-visible:outline-2 focus-visible:outline-twc08-amber focus-visible:outline-offset-[3px]">
        See all 1,247 reviews
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc08-bg: #f8f7f4;
  --color-twc08-bg: oklch(0.97 0.005 90);
  --color-twc08-ink: #1a1a1a;
  --color-twc08-ink: oklch(0.21 0.005 270);
  --color-twc08-ink2: #4b4b57;
  --color-twc08-ink2: oklch(0.4 0.015 280);
  --color-twc08-muted: #6b6b7c;
  --color-twc08-muted: oklch(0.51 0.02 285);
  --color-twc08-dim: #a1a1aa;
  --color-twc08-dim: oklch(0.7 0.01 285);
  --color-twc08-amber: #f59e0b;
  --color-twc08-amber: oklch(0.78 0.16 70);
  --color-twc08-amberink: #92400e;
  --color-twc08-amberink: oklch(0.44 0.12 55);
  --color-twc08-amberdeep: #78350f;
  --color-twc08-amberdeep: oklch(0.38 0.1 55);
  --color-twc08-green: #22c55e;
  --color-twc08-green: oklch(0.72 0.18 145);
  --color-twc08-greenink: #059669;
  --color-twc08-greenink: oklch(0.56 0.13 163);
  --font-twc08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc08-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --font-twc08-serif: Georgia, 'Times New Roman', serif;
}
/* No @keyframes: the card's only motion is a hover transition. */

.twc-08 {
  width: 100%;
  min-height: 100svh;
}
```
