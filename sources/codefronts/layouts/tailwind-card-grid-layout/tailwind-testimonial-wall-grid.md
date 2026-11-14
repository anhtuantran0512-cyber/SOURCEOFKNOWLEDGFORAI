---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-testimonial-wall-grid/"
title: "Tailwind Testimonial Wall Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "Six customer quotes on a four-column wall, with one dark 2&times;2 hero quote anchoring it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Testimonial Wall Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-testimonial-wall-grid/

Six customer quotes on a four-column wall, with one dark 2&times;2 hero quote anchoring it. The port's interesting part is the inversion: the featured card's dark treatment is a class group on one element (bg-tcg11-featbg text-tcg11-featink) and its children inherit, so the CSS version's six .card--featured .x descendant rules shrink to two text-* overrides.
## HTML
```html
<section class="tcg-11 w-full min-h-svh bg-tcg11-bg font-tcg11-sans text-tcg11-ink px-[clamp(20px,3vw,48px)] py-[clamp(32px,4vw,64px)]" aria-label="Testimonial wall grid demo">

  <header class="max-w-[600px] mx-auto text-center mb-[clamp(32px,4vw,48px)]">
    <span class="inline-block mb-2.5 text-[.72rem] font-bold tracking-[0.2em] uppercase text-tcg11-muted">Customer love</span>
    <h2 class="text-[clamp(1.8rem,3.4vw,2.6rem)] font-extrabold tracking-[-0.02em] leading-[1.1]">2,400+ teams ship faster.</h2>
  </header>

  <div class="max-w-[1180px] mx-auto grid grid-cols-4 max-[960px]:grid-cols-2 max-[560px]:grid-cols-1 [grid-auto-rows:minmax(200px,auto)] gap-[clamp(14px,1.6vw,20px)]">

    <figure class="col-span-2 row-span-2 max-[960px]:row-span-1 max-[560px]:col-span-1 flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-featbg bg-tcg11-featbg text-tcg11-featink p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.35)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[1.1rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote class="text-[clamp(1.15rem,1.8vw,1.5rem)] font-medium leading-[1.35] tracking-[-0.005em] text-pretty">We replaced four tools with one. Our deploys went from 12 minutes to under 90 seconds, and the whole engineering team finally agrees on something. Worth every penny.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-12 h-12 rounded-full bg-linear-[135deg,#f9c1cf,#d97a99]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Maya Chen</span>
          <span class="text-[.78rem] text-tcg11-featdim">VP Engineering &middot; <strong class="font-bold text-tcg11-featink">Linear</strong></span>
        </div>
      </figcaption>
    </figure>

    <figure class="flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-line bg-tcg11-card p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[.95rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote class="text-[clamp(.94rem,1.05vw,1rem)] leading-[1.5] text-pretty">The onboarding alone saved us a week. We were live in three hours.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-10 h-10 rounded-full bg-linear-[135deg,#a7c8e7,#5b8fd9]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Liam Okonkwo</span>
          <span class="text-[.78rem] text-tcg11-muted">CTO &middot; <strong class="font-bold text-tcg11-ink">Plaid</strong></span>
        </div>
      </figcaption>
    </figure>

    <figure class="flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-line bg-tcg11-card p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[.95rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote class="text-[clamp(.94rem,1.05vw,1rem)] leading-[1.5] text-pretty">Honestly the best support team I have worked with in 12 years of building SaaS.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-10 h-10 rounded-full bg-linear-[135deg,#c5da9c,#7aa852]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Aria Patel</span>
          <span class="text-[.78rem] text-tcg11-muted">Founder &middot; <strong class="font-bold text-tcg11-ink">Resend</strong></span>
        </div>
      </figcaption>
    </figure>

    <figure class="flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-line bg-tcg11-card p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[.95rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 4 out of 5">&#9733;&#9733;&#9733;&#9733;<span class="text-tcg11-star-off">&#9733;</span></div>
      <blockquote class="text-[clamp(.94rem,1.05vw,1rem)] leading-[1.5] text-pretty">4 stars only because we keep finding new things we wish it did. It does most of them next quarter.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-10 h-10 rounded-full bg-linear-[135deg,#f7b88a,#d97f4f]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Noah Reyes</span>
          <span class="text-[.78rem] text-tcg11-muted">Eng Lead &middot; <strong class="font-bold text-tcg11-ink">Vercel</strong></span>
        </div>
      </figcaption>
    </figure>

    <figure class="flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-line bg-tcg11-card p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[.95rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote class="text-[clamp(.94rem,1.05vw,1rem)] leading-[1.5] text-pretty">Our incident response time dropped 73%. Board noticed.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-10 h-10 rounded-full bg-linear-[135deg,#c4b5fd,#9b87e5]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Zoe Larsson</span>
          <span class="text-[.78rem] text-tcg11-muted">SRE Manager &middot; <strong class="font-bold text-tcg11-ink">Stripe</strong></span>
        </div>
      </figcaption>
    </figure>

    <figure class="flex flex-col justify-between gap-4 rounded-2xl border border-tcg11-line bg-tcg11-card p-[clamp(18px,2vw,24px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_28px_-14px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="text-[.95rem] tracking-[0.1em] tabular-nums text-tcg11-accent" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <blockquote class="text-[clamp(.94rem,1.05vw,1rem)] leading-[1.5] text-pretty">We tried five alternatives. Came back here on day three.</blockquote>
      <figcaption class="flex items-center gap-3">
        <div class="shrink-0 w-10 h-10 rounded-full bg-linear-[135deg,#fef0a3,#e6c54a]" aria-hidden="true"></div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="text-[.92rem] font-bold">Sam Okafor</span>
          <span class="text-[.78rem] text-tcg11-muted">Product &middot; <strong class="font-bold text-tcg11-ink">Notion</strong></span>
        </div>
      </figcaption>
    </figure>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg11-bg: #f8fafc;
  --color-tcg11-bg: oklch(0.98 0.004 250);
  --color-tcg11-card: #ffffff;
  --color-tcg11-card: oklch(1 0 0);
  --color-tcg11-ink: #0f172a;
  --color-tcg11-ink: oklch(0.21 0.04 260);
  --color-tcg11-muted: #64748b;
  --color-tcg11-muted: oklch(0.55 0.03 257);
  --color-tcg11-line: #e2e8f0;
  --color-tcg11-line: oklch(0.92 0.01 255);
  --color-tcg11-accent: #f59e0b;
  --color-tcg11-accent: oklch(0.77 0.16 70);
  --color-tcg11-star-off: #94a3b8;
  --color-tcg11-star-off: oklch(0.71 0.03 257);
  --color-tcg11-featbg: #0f172a;
  --color-tcg11-featbg: oklch(0.21 0.04 260);
  --color-tcg11-featink: #f8fafc;
  --color-tcg11-featink: oklch(0.98 0.004 250);
  --color-tcg11-featdim: #a4b0c2;
  --color-tcg11-featdim: oklch(0.76 0.02 257);
  --font-tcg11-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-11 {
  width: 100%;
  min-height: 100svh;
}

.tcg-11 ::selection {
  background: #0f172a;
  color: #fff;
}
```
