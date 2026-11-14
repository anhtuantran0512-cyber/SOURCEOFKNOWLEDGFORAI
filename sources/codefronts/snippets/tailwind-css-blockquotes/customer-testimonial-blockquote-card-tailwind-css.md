---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/customer-testimonial-blockquote-card-tailwind-css/"
title: "Customer Testimonial Blockquote Card in Tailwind CSS"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Conversion-grade testimonial card: star rating, verified badge, quote, avatar, a headline metric, and a case-study link."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Customer Testimonial Blockquote Card in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/customer-testimonial-blockquote-card-tailwind-css/

Conversion-grade testimonial card: star rating, verified badge, quote, avatar, a headline metric, and a case-study link. The port turns the card from a fake-focusable tabindex="0" figure into a real stretched-link card — the whole surface clicks through, and has-[a:focus-visible]: puts the focus ring on the card, not the tiny link.
## HTML
```html
<section class="tbq-14 w-full min-h-svh grid place-items-center bg-tbq14-bg bg-[radial-gradient(80%_60%_at_50%_-10%,var(--color-tbq14-glow),transparent)] px-5 py-14 font-tbq14-sans text-tbq14-ink" aria-label="Customer testimonial card demo">
  <div class="grid w-full justify-items-center gap-7">
    <figure class="@container group relative w-full max-w-[420px] rounded-[18px] border border-black/7 bg-tbq14-card px-6.5 pt-6 pb-4 shadow-[0_2px_6px_oklch(0.3_0.03_180/0.06),0_14px_34px_oklch(0.3_0.03_180/0.1)] transition-[translate,box-shadow] duration-250 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:-translate-y-1 hover:shadow-[0_4px_10px_oklch(0.3_0.03_180/0.08),0_26px_52px_oklch(0.3_0.03_180/0.16)] has-[a:focus-visible]:-translate-y-1 has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-3 has-[a:focus-visible]:outline-tbq14-acc motion-reduce:transition-none">
      <div class="flex items-center justify-between gap-3">
        <p class="leading-none"><svg class="text-tbq14-gold" role="img" aria-label="Rated 5 out of 5 stars" viewBox="0 0 128 24" width="112" height="21"><defs><path id="tbq14s" fill="currentColor" d="M12 2.2l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17l-5.8 3.1 1.1-6.5L2.6 9l6.5-.9z"/></defs><use href="#tbq14s" fill="currentColor"/><use href="#tbq14s" x="26" fill="currentColor"/><use href="#tbq14s" x="52" fill="currentColor"/><use href="#tbq14s" x="78" fill="currentColor"/><use href="#tbq14s" x="104" fill="currentColor"/></svg></p>
        <span class="inline-flex items-center gap-1.5 rounded-full bg-tbq14-acc/10 px-2.5 py-1.5 text-[11px] font-semibold whitespace-nowrap text-tbq14-acc-ink @max-[340px]:hidden"><svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 1.4l1.8 1.3 2.2-.1.7 2.1 1.9 1.2-.7 2.1.7 2.1-1.9 1.2-.7 2.1-2.2-.1L8 14.6l-1.8-1.3-2.2.1-.7-2.1L1.4 10l.7-2.1-.7-2.1 1.9-1.2.7-2.1 2.2.1z" fill="currentColor" opacity=".25"/><path d="M5.2 8.2l1.9 1.9 3.7-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified customer</span>
      </div>
      <blockquote class="mt-4">
        <p class="text-[15.5px] leading-[1.62] text-pretty">Rollouts used to be a two-week negotiation with our ops team. With Relay's staged deploys we shipped to 40 clinics in an afternoon — and nobody had to stay late.</p>
      </blockquote>
      <div class="mt-5 flex items-center justify-between gap-3.5 border-t border-black/7 pt-4 @max-[340px]:flex-col @max-[340px]:items-start">
        <figcaption class="flex items-center gap-3 text-[12.5px] leading-[1.45] text-tbq14-mut">
          <img class="size-10 flex-none rounded-full bg-linear-135 from-tbq14-av1 to-tbq14-av2 object-cover" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=120&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
          <span><strong class="block text-[13.5px] font-semibold text-tbq14-ink">Dr. Priya Raman</strong>Director of Operations, Northcare Health</span>
        </figcaption>
        <p class="flex-none text-right @max-[340px]:text-left"><b class="block text-xl font-extrabold tracking-[-0.02em] text-tbq14-acc-ink">−63%</b><span class="text-[10.5px] font-semibold tracking-[0.06em] uppercase text-tbq14-mut">deploy time</span></p>
      </div>
      <a href="#case-study" class="mt-2 inline-flex min-h-11 items-center gap-1.5 text-[13px] font-semibold text-tbq14-acc-ink after:absolute after:inset-0 after:rounded-[inherit] focus-visible:outline-none">Read the Northcare case study <span aria-hidden="true" class="transition-transform duration-200 group-hover:translate-x-1">→</span></a>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-black/9 bg-white px-3.5 py-2 font-tbq14-mono text-[11.5px] text-tbq14-mut">stretched link · has-[a:focus-visible]: · @max-[340px]: re-stack</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq14-bg: #f0f5f2;
  --color-tbq14-bg: oklch(0.965 0.006 160);
  --color-tbq14-glow: #d6efe3cc;
  --color-tbq14-glow: oklch(0.93 0.03 165 / 0.8);
  --color-tbq14-card: #ffffff;
  --color-tbq14-card: oklch(1 0 0);
  --color-tbq14-ink: #172522;
  --color-tbq14-ink: oklch(0.25 0.02 180);
  --color-tbq14-mut: #52615e;
  --color-tbq14-mut: oklch(0.48 0.02 180);
  --color-tbq14-acc: #008767;
  --color-tbq14-acc: oklch(0.55 0.12 170);
  --color-tbq14-acc-ink: #006752;
  --color-tbq14-acc-ink: oklch(0.45 0.1 175);
  --color-tbq14-gold: #e6ac3d;
  --color-tbq14-gold: oklch(0.78 0.14 80);
  --color-tbq14-av1: #88bba8;
  --color-tbq14-av1: oklch(0.75 0.06 170);
  --color-tbq14-av2: #3b8f93;
  --color-tbq14-av2: oklch(0.6 0.08 200);
  --font-tbq14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq14-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-14 {
  width: 100%;
  min-height: 100svh;
}
```
