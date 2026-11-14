---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-glassmorphism-faq-accordion-frosted-blur/"
title: "Tailwind Glassmorphism FAQ Accordion with Frosted Backdrop Blur"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Frosted-glass panels floating over a photographic backdrop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism FAQ Accordion with Frosted Backdrop Blur
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-glassmorphism-faq-accordion-frosted-blur/

Frosted-glass panels floating over a photographic backdrop. Tailwind has utilities for all four glass layers — the tint, backdrop-blur-[18px] backdrop-saturate-150, a translucent border and an inset highlight inside shadow-[...] — so the whole material is a class list, and the open state simply frosts deeper. Includes the two rules most glassmorphism tutorials miss: the saturation boost and the top-edge highlight.
## HTML
```html
<section class="tfa-07 w-full min-h-svh font-tfa07-sans">
  <div class="grid min-h-svh w-full place-items-center bg-[linear-gradient(160deg,oklch(0.45_0.2_290/0.55),oklch(0.5_0.22_340/0.35)_55%,oklch(0.55_0.18_240/0.5)),url('https://images.unsplash.com/photo-1518098268026-4e89f1a2cd8e?q=80&w=1800&auto=format&fit=crop')] bg-cover bg-center px-5 py-12">
    <div class="w-[min(620px,100%)]">
      <header>
        <h1 class="text-[clamp(30px,5vw,42px)] font-extrabold leading-[1.06] tracking-[-0.025em] text-white [text-shadow:0_2px_24px_oklch(0.2_0.08_290/0.6)]">Membership FAQ</h1>
        <p class="mt-3 max-w-[52ch] text-[14.5px] leading-relaxed text-white/90 [text-shadow:0_1px_12px_oklch(0.2_0.08_290/0.65)]">Four layers make the glass: tint, frost, edge, highlight. The open panel frosts deeper — no accent colour needed.</p>
      </header>

      <div data-panel class="mt-7 flex flex-col gap-3">
        <details class="group rounded-[18px] border border-white/30 bg-white/15 shadow-[inset_0_1px_0_oklch(1_0_0/0.35),0_24px_48px_oklch(0.3_0.12_290/0.35)] backdrop-blur-[18px] backdrop-saturate-150 transition-[background-color,box-shadow,backdrop-filter] duration-350 open:bg-white/25 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_30px_60px_oklch(0.3_0.12_290/0.45)] open:backdrop-blur-[26px] open:backdrop-saturate-[1.8]" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] text-white [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.55)] focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [&::-webkit-details-marker]:hidden">What does membership include?
            <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-full border border-white/40 transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-white/20 group-open:rotate-180 group-open:bg-white/20 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-white/90 [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.5)]">Unlimited access to every studio location, all live classes, and the on-demand library. Founding members also lock their rate for life — it never increases while the membership stays active.</p>
        </details>
        <details class="group rounded-[18px] border border-white/30 bg-white/15 shadow-[inset_0_1px_0_oklch(1_0_0/0.35),0_24px_48px_oklch(0.3_0.12_290/0.35)] backdrop-blur-[18px] backdrop-saturate-150 transition-[background-color,box-shadow,backdrop-filter] duration-350 open:bg-white/25 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_30px_60px_oklch(0.3_0.12_290/0.45)] open:backdrop-blur-[26px] open:backdrop-saturate-[1.8]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] text-white [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.55)] focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [&::-webkit-details-marker]:hidden">Can I freeze my membership?
            <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-full border border-white/40 transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-white/20 group-open:rotate-180 group-open:bg-white/20 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-white/90 [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.5)]">Yes — up to 3 months per year, in one-month blocks, straight from the app. Frozen months push your renewal date back, so you never pay for time you cannot use.</p>
        </details>
        <details class="group rounded-[18px] border border-white/30 bg-white/15 shadow-[inset_0_1px_0_oklch(1_0_0/0.35),0_24px_48px_oklch(0.3_0.12_290/0.35)] backdrop-blur-[18px] backdrop-saturate-150 transition-[background-color,box-shadow,backdrop-filter] duration-350 open:bg-white/25 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_30px_60px_oklch(0.3_0.12_290/0.45)] open:backdrop-blur-[26px] open:backdrop-saturate-[1.8]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] text-white [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.55)] focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [&::-webkit-details-marker]:hidden">Do you offer day passes for guests?
            <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-full border border-white/40 transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-white/20 group-open:rotate-180 group-open:bg-white/20 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-white/90 [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.5)]">Every member gets 2 free guest passes a month. Additional passes are $15, and guests who join within 7 days get their pass credited toward the first month.</p>
        </details>
        <details class="group rounded-[18px] border border-white/30 bg-white/15 shadow-[inset_0_1px_0_oklch(1_0_0/0.35),0_24px_48px_oklch(0.3_0.12_290/0.35)] backdrop-blur-[18px] backdrop-saturate-150 transition-[background-color,box-shadow,backdrop-filter] duration-350 open:bg-white/25 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_30px_60px_oklch(0.3_0.12_290/0.45)] open:backdrop-blur-[26px] open:backdrop-saturate-[1.8]">
          <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15.5px] font-semibold tracking-[-0.01em] text-white [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.55)] focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [&::-webkit-details-marker]:hidden">Which locations are open 24/7?
            <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-full border border-white/40 transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-white/20 group-open:rotate-180 group-open:bg-white/20 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-white/90 [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.5)]">All flagship locations run 24/7 with app-based entry. Neighbourhood studios open 5am–11pm; the app map badges each one with live hours and current capacity.</p>
        </details>
      </div>

      <p class="mt-6 font-tfa07-mono text-[11.5px] text-white/85 [text-shadow:0_1px_10px_oklch(0.2_0.08_290/0.6)]">backdrop-blur-[18px] backdrop-saturate-150 — the saturate is what makes it glass, not smear.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tfa07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa07-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-07 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 prefix — Tailwind does not emit -webkit-backdrop-filter for arbitrary values. */

.tfa-07 details {
  -webkit-backdrop-filter: blur(18px) saturate(1.5);
}

.tfa-07 details[open] {
  -webkit-backdrop-filter: blur(26px) saturate(1.8);
}
/* Contrast floor where backdrop-filter is unavailable (forced colours, blocklisted GPUs). */

@supports not (backdrop-filter: blur(1px)) {
  .tfa-07 details {
    background: oklch(0.35 0.08 290 / 0.92);
  }

  .tfa-07 details[open] {
    background: oklch(0.32 0.08 290 / 0.96);
  }
}

.tfa-07 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-07 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1), opacity .32s, content-visibility .4s allow-discrete;
  }

  .tfa-07 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-07 details::details-content {
    transition-duration: 1ms;
  }
}
```
