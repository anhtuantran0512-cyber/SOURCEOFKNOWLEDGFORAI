---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-testimonial-flip-card-star-rating-reviewer-profile/"
title: "Tailwind Testimonial Flip Card with Star Rating & Reviewer Profile"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A customer quote with a five-star rating on the front and the reviewer's full profile plus a per-category breakdown on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Testimonial Flip Card with Star Rating & Reviewer Profile
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-testimonial-flip-card-star-rating-reviewer-profile/

A customer quote with a five-star rating on the front and the reviewer's full profile plus a per-category breakdown on the back. The port makes the quote a real <blockquote> with a <cite>, and gives every star row an aria-label &mdash; five Unicode glyphs announce as "black star black star black star&hellip;" otherwise, which is the collection's most common accessibility defect.
## HTML
```html
<section class="tfc-11 w-full min-h-svh grid place-items-center bg-tfc11-bg font-tfc11-sans px-5 py-10 text-tfc11-ink">
  <div class="group relative w-[360px] max-w-full h-[430px] [perspective:1200px] rounded-3xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc11-violet has-[:focus-visible]:outline-offset-4">
    <input id="tfc-11-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-11-flip" class="absolute inset-0 z-20 cursor-pointer rounded-3xl"><span class="sr-only">Show Marcus Klein's full reviewer profile</span></label>

    <div class="relative w-full h-full transition-transform duration-[750ms] ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <figure class="absolute inset-0 m-0 flex flex-col gap-4 rounded-3xl overflow-hidden px-8 py-9 bg-linear-145 from-tfc11-panel to-tfc11-panel2 border border-tfc11-violet/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.45_0.2_300/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <blockquote class="flex-1 text-lg font-semibold leading-[1.65] text-tfc11-ink/85 text-pretty before:block before:font-serif before:text-[80px] before:leading-[0.7] before:text-tfc11-violet/25 before:content-['\201C']">Switching to this platform <strong class="bg-linear-135 from-tfc11-violet to-tfc11-pink bg-clip-text font-bold text-transparent">cut our design-to-production time in half.</strong> The component library alone saved us three months of custom work.</blockquote>
        <p role="img" aria-label="Rated 5 out of 5" class="flex gap-1 text-lg text-tfc11-gold"><span aria-hidden="true">&#9733;</span><span aria-hidden="true">&#9733;</span><span aria-hidden="true">&#9733;</span><span aria-hidden="true">&#9733;</span><span aria-hidden="true">&#9733;</span></p>
        <figcaption class="flex items-center gap-3 border-t border-white/7 pt-4">
          <span class="grid size-11 shrink-0 place-items-center rounded-full bg-linear-135 from-tfc11-violet to-tfc11-pink text-base font-extrabold text-white">MK</span>
          <span>
            <cite class="block text-sm font-bold not-italic text-white">Marcus Klein</cite>
            <span class="block text-[11px] text-tfc11-muted">VP of Engineering &middot; Prism Labs</span>
          </span>
        </figcaption>
        <p class="text-right text-[10px] tracking-[0.08em] text-tfc11-dim">Hover, tap or press Space for the profile &rarr;</p>
      </figure>

      <div class="absolute inset-0 flex flex-col gap-3.5 rounded-3xl overflow-hidden p-7 bg-linear-145 from-tfc11-back to-tfc11-back2 border border-tfc11-pink/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.5_0.2_350/0.4)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc11-pink">Reviewer profile</h3>
        <div class="flex flex-col items-center gap-2.5 rounded-2xl border border-white/7 bg-white/3 p-5">
          <span class="grid size-18 place-items-center rounded-full border-[3px] border-tfc11-violet/30 bg-linear-135 from-tfc11-violet to-tfc11-pink text-[28px] font-black text-white">MK</span>
          <p class="text-lg font-extrabold text-white">Marcus Klein</p>
          <p class="text-center text-xs text-tfc11-muted">VP of Engineering &middot; 12 years in SaaS infrastructure</p>
          <p class="flex items-center gap-2 rounded-xl border border-tfc11-violet/20 bg-tfc11-violet/10 px-4 py-2">
            <span class="grid size-7 shrink-0 place-items-center rounded-lg bg-linear-135 from-tfc11-indigo to-tfc11-violet text-xs font-extrabold text-white">PL</span>
            <span>
              <span class="block text-[13px] font-bold text-tfc11-ink/80">Prism Labs</span>
              <span class="block text-[10px] text-tfc11-dim">Series B &middot; 340 employees</span>
            </span>
          </p>
        </div>
        <dl class="rounded-2xl border border-white/7 bg-white/3 p-3.5">
          <div class="mb-1.5 flex items-center justify-between"><dt class="text-[11px] text-tfc11-muted">Overall</dt><dd role="img" aria-label="5 out of 5" class="text-[13px] tracking-[1px] text-tfc11-gold"><span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span></dd></div>
          <div class="mb-1.5 flex items-center justify-between"><dt class="text-[11px] text-tfc11-muted">Ease of use</dt><dd role="img" aria-label="5 out of 5" class="text-[13px] tracking-[1px] text-tfc11-gold"><span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span></dd></div>
          <div class="flex items-center justify-between"><dt class="text-[11px] text-tfc11-muted">Support</dt><dd role="img" aria-label="5 out of 5" class="text-[13px] tracking-[1px] text-tfc11-gold"><span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span></dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc11-bg: #09050f;
  --color-tfc11-bg: oklch(0.13 0.025 300);
  --color-tfc11-panel: #110822;
  --color-tfc11-panel: oklch(0.18 0.06 300);
  --color-tfc11-panel2: #0d0518;
  --color-tfc11-panel2: oklch(0.15 0.05 300);
  --color-tfc11-back: #0f0120;
  --color-tfc11-back: oklch(0.16 0.08 300);
  --color-tfc11-back2: #14022a;
  --color-tfc11-back2: oklch(0.18 0.09 300);
  --color-tfc11-violet: #7c3aed;
  --color-tfc11-violet: oklch(0.55 0.24 295);
  --color-tfc11-indigo: #4f46e5;
  --color-tfc11-indigo: oklch(0.51 0.22 275);
  --color-tfc11-pink: #db2777;
  --color-tfc11-pink: oklch(0.6 0.22 355);
  --color-tfc11-gold: #f59e0b;
  --color-tfc11-gold: oklch(0.77 0.16 70);
  --color-tfc11-ink: #fdf4ff;
  --color-tfc11-ink: oklch(0.97 0.02 315);
  --color-tfc11-muted: #b9a8c4;
  --color-tfc11-muted: oklch(0.77 0.04 310);
  --color-tfc11-dim: #8b7d97;
  --color-tfc11-dim: oklch(0.63 0.03 310);
  --font-tfc11-sans: 'Sora', system-ui, sans-serif;
}

.tfc-11 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-11 * {
    transition-duration: 1ms !important;
  }
}
```
