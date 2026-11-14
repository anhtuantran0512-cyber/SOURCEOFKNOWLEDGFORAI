---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-horizontal-faq-accordion-sideways-panels/"
title: "Tailwind Horizontal FAQ Accordion with Sideways Expanding Panels"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The showpiece: five photo panels standing shoulder to shoulder, the active one unfolding sideways to reveal its answer while the others compress into spines…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Horizontal FAQ Accordion with Sideways Expanding Panels
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-horizontal-faq-accordion-sideways-panels/

The showpiece: five photo panels standing shoulder to shoulder, the active one unfolding sideways to reveal its answer while the others compress into spines with vertically-written titles. Demo 10's fr-unit trick rotated 90° — grid-cols-[64px_0fr] to [64px_1fr] — plus a grow-[3.2] transition, [writing-mode:vertical-rl] spines, and radio state, so it stays pure Tailwind.
## HTML
```html
<section class="tfa-15 w-full min-h-svh font-tfa15-sans text-white">
  <div class="@container grid min-h-svh w-full place-items-center bg-tfa15-bg px-5 py-12">
    <div class="w-[min(1020px,100%)]">
      <header>
        <h1 class="text-[clamp(26px,4.4vw,40px)] font-extrabold tracking-[-0.025em]">Plan your expedition</h1>
        <p class="mt-3 max-w-[54ch] text-[14.5px] leading-relaxed text-white/85">Five questions standing sideways — the open one unfolds. Arrow keys move between panels.</p>
      </header>

      <div class="mt-7 flex min-h-[420px] gap-2.5 @max-tfa15fold:min-h-0 @max-tfa15fold:flex-col">
        <div class="group relative grid flex-1 overflow-hidden rounded-[18px] bg-[linear-gradient(oklch(0.2_0.03_260/0.25),oklch(0.15_0.03_260/0.7)),url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center outline-2 outline-offset-[3px] outline-transparent transition-[grid-template-columns,grid-template-rows,flex-grow,outline-color] duration-600 ease-[cubic-bezier(0.3,0.8,0.25,1)] grid-cols-[64px_0fr] has-checked:grid-cols-[64px_1fr] has-checked:grow-[3.2] [&:not(:has(:checked)):hover]:grow-[1.15] has-focus-visible:outline-tfa15-acc @max-tfa15fold:grid-cols-[1fr] @max-tfa15fold:grid-rows-[56px_0fr] @max-tfa15fold:has-checked:grid-cols-[1fr] @max-tfa15fold:has-checked:grid-rows-[56px_1fr] @max-tfa15fold:has-checked:grow-[1] motion-reduce:transition-none">
          <input id="tfa15-p1" type="radio" name="tfa15" class="absolute opacity-0 pointer-events-none" checked>
          <label for="tfa15-p1" class="grid min-w-11 cursor-pointer items-end justify-items-center py-[18px] @max-tfa15fold:min-h-11 @max-tfa15fold:place-items-center @max-tfa15fold:justify-items-start @max-tfa15fold:px-5 @max-tfa15fold:py-0">
            <h3 class="[writing-mode:vertical-rl] rotate-180 text-[13.5px] font-bold uppercase tracking-[0.06em] text-white [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.85)] transition-colors duration-300 group-hover:text-tfa15-acc group-has-checked:text-tfa15-acc @max-tfa15fold:[writing-mode:horizontal-tb] @max-tfa15fold:rotate-0">When to go?</h3>
          </label>
          <div class="grid min-w-0 items-end overflow-hidden @max-tfa15fold:min-h-0">
            <div class="w-[max(260px,26cqi)] translate-x-3.5 py-[22px] pl-2 pr-6 opacity-0 transition-[translate,opacity] delay-150 duration-500 ease-[cubic-bezier(0.3,0.8,0.25,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none @max-tfa15fold:w-full @max-tfa15fold:px-5 @max-tfa15fold:pb-5 @max-tfa15fold:pt-0">
              <h2 class="text-[clamp(17px,2.2vw,22px)] font-extrabold tracking-[-0.02em] text-white [text-shadow:0_1px_14px_oklch(0.15_0.03_260/0.8)]">When is the best season?</h2>
              <p class="mt-2.5 text-[13.5px] leading-[1.65] text-white/90 [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.75)]">June through September for the high passes — long days, stable weather, open refuges. Shoulder months halve the crowds but add real weather risk above 2,500m.</p>
            </div>
          </div>
        </div>
        <div class="group relative grid flex-1 overflow-hidden rounded-[18px] bg-[linear-gradient(oklch(0.2_0.03_260/0.25),oklch(0.15_0.03_260/0.7)),url('https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center outline-2 outline-offset-[3px] outline-transparent transition-[grid-template-columns,grid-template-rows,flex-grow,outline-color] duration-600 ease-[cubic-bezier(0.3,0.8,0.25,1)] grid-cols-[64px_0fr] has-checked:grid-cols-[64px_1fr] has-checked:grow-[3.2] [&:not(:has(:checked)):hover]:grow-[1.15] has-focus-visible:outline-tfa15-acc @max-tfa15fold:grid-cols-[1fr] @max-tfa15fold:grid-rows-[56px_0fr] @max-tfa15fold:has-checked:grid-cols-[1fr] @max-tfa15fold:has-checked:grid-rows-[56px_1fr] @max-tfa15fold:has-checked:grow-[1] motion-reduce:transition-none">
          <input id="tfa15-p2" type="radio" name="tfa15" class="absolute opacity-0 pointer-events-none">
          <label for="tfa15-p2" class="grid min-w-11 cursor-pointer items-end justify-items-center py-[18px] @max-tfa15fold:min-h-11 @max-tfa15fold:place-items-center @max-tfa15fold:justify-items-start @max-tfa15fold:px-5 @max-tfa15fold:py-0">
            <h3 class="[writing-mode:vertical-rl] rotate-180 text-[13.5px] font-bold uppercase tracking-[0.06em] text-white [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.85)] transition-colors duration-300 group-hover:text-tfa15-acc group-has-checked:text-tfa15-acc @max-tfa15fold:[writing-mode:horizontal-tb] @max-tfa15fold:rotate-0">Fitness level</h3>
          </label>
          <div class="grid min-w-0 items-end overflow-hidden @max-tfa15fold:min-h-0">
            <div class="w-[max(260px,26cqi)] translate-x-3.5 py-[22px] pl-2 pr-6 opacity-0 transition-[translate,opacity] delay-150 duration-500 ease-[cubic-bezier(0.3,0.8,0.25,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none @max-tfa15fold:w-full @max-tfa15fold:px-5 @max-tfa15fold:pb-5 @max-tfa15fold:pt-0">
              <h2 class="text-[clamp(17px,2.2vw,22px)] font-extrabold tracking-[-0.02em] text-white [text-shadow:0_1px_14px_oklch(0.15_0.03_260/0.8)]">How fit do I need to be?</h2>
              <p class="mt-2.5 text-[13.5px] leading-[1.65] text-white/90 [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.75)]">Comfortable hiking 6–7 hours with a daypack, two days in a row. Our grade-2 routes need no technical skills; if you can do a hilly half-day hike smiling, twelve training weeks gets you there.</p>
            </div>
          </div>
        </div>
        <div class="group relative grid flex-1 overflow-hidden rounded-[18px] bg-[linear-gradient(oklch(0.2_0.03_260/0.25),oklch(0.15_0.03_260/0.7)),url('https://images.unsplash.com/photo-1501554728187-ce583db33af7?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center outline-2 outline-offset-[3px] outline-transparent transition-[grid-template-columns,grid-template-rows,flex-grow,outline-color] duration-600 ease-[cubic-bezier(0.3,0.8,0.25,1)] grid-cols-[64px_0fr] has-checked:grid-cols-[64px_1fr] has-checked:grow-[3.2] [&:not(:has(:checked)):hover]:grow-[1.15] has-focus-visible:outline-tfa15-acc @max-tfa15fold:grid-cols-[1fr] @max-tfa15fold:grid-rows-[56px_0fr] @max-tfa15fold:has-checked:grid-cols-[1fr] @max-tfa15fold:has-checked:grid-rows-[56px_1fr] @max-tfa15fold:has-checked:grow-[1] motion-reduce:transition-none">
          <input id="tfa15-p3" type="radio" name="tfa15" class="absolute opacity-0 pointer-events-none">
          <label for="tfa15-p3" class="grid min-w-11 cursor-pointer items-end justify-items-center py-[18px] @max-tfa15fold:min-h-11 @max-tfa15fold:place-items-center @max-tfa15fold:justify-items-start @max-tfa15fold:px-5 @max-tfa15fold:py-0">
            <h3 class="[writing-mode:vertical-rl] rotate-180 text-[13.5px] font-bold uppercase tracking-[0.06em] text-white [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.85)] transition-colors duration-300 group-hover:text-tfa15-acc group-has-checked:text-tfa15-acc @max-tfa15fold:[writing-mode:horizontal-tb] @max-tfa15fold:rotate-0">What is included</h3>
          </label>
          <div class="grid min-w-0 items-end overflow-hidden @max-tfa15fold:min-h-0">
            <div class="w-[max(260px,26cqi)] translate-x-3.5 py-[22px] pl-2 pr-6 opacity-0 transition-[translate,opacity] delay-150 duration-500 ease-[cubic-bezier(0.3,0.8,0.25,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none @max-tfa15fold:w-full @max-tfa15fold:px-5 @max-tfa15fold:pb-5 @max-tfa15fold:pt-0">
              <h2 class="text-[clamp(17px,2.2vw,22px)] font-extrabold tracking-[-0.02em] text-white [text-shadow:0_1px_14px_oklch(0.15_0.03_260/0.8)]">What does the price include?</h2>
              <p class="mt-2.5 text-[13.5px] leading-[1.65] text-white/90 [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.75)]">Guides, refuge nights, breakfasts and dinners, luggage transfer between stages and safety kit. Flights, lunches and insurance are yours — full packing list on booking.</p>
            </div>
          </div>
        </div>
        <div class="group relative grid flex-1 overflow-hidden rounded-[18px] bg-[linear-gradient(oklch(0.2_0.03_260/0.25),oklch(0.15_0.03_260/0.7)),url('https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center outline-2 outline-offset-[3px] outline-transparent transition-[grid-template-columns,grid-template-rows,flex-grow,outline-color] duration-600 ease-[cubic-bezier(0.3,0.8,0.25,1)] grid-cols-[64px_0fr] has-checked:grid-cols-[64px_1fr] has-checked:grow-[3.2] [&:not(:has(:checked)):hover]:grow-[1.15] has-focus-visible:outline-tfa15-acc @max-tfa15fold:grid-cols-[1fr] @max-tfa15fold:grid-rows-[56px_0fr] @max-tfa15fold:has-checked:grid-cols-[1fr] @max-tfa15fold:has-checked:grid-rows-[56px_1fr] @max-tfa15fold:has-checked:grow-[1] motion-reduce:transition-none">
          <input id="tfa15-p4" type="radio" name="tfa15" class="absolute opacity-0 pointer-events-none">
          <label for="tfa15-p4" class="grid min-w-11 cursor-pointer items-end justify-items-center py-[18px] @max-tfa15fold:min-h-11 @max-tfa15fold:place-items-center @max-tfa15fold:justify-items-start @max-tfa15fold:px-5 @max-tfa15fold:py-0">
            <h3 class="[writing-mode:vertical-rl] rotate-180 text-[13.5px] font-bold uppercase tracking-[0.06em] text-white [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.85)] transition-colors duration-300 group-hover:text-tfa15-acc group-has-checked:text-tfa15-acc @max-tfa15fold:[writing-mode:horizontal-tb] @max-tfa15fold:rotate-0">Group size</h3>
          </label>
          <div class="grid min-w-0 items-end overflow-hidden @max-tfa15fold:min-h-0">
            <div class="w-[max(260px,26cqi)] translate-x-3.5 py-[22px] pl-2 pr-6 opacity-0 transition-[translate,opacity] delay-150 duration-500 ease-[cubic-bezier(0.3,0.8,0.25,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none @max-tfa15fold:w-full @max-tfa15fold:px-5 @max-tfa15fold:pb-5 @max-tfa15fold:pt-0">
              <h2 class="text-[clamp(17px,2.2vw,22px)] font-extrabold tracking-[-0.02em] text-white [text-shadow:0_1px_14px_oklch(0.15_0.03_260/0.8)]">How big are the groups?</h2>
              <p class="mt-2.5 text-[13.5px] leading-[1.65] text-white/90 [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.75)]">Max 10, average 7, two certified guides per group. Solo travellers are half of every departure — the refuge table does the introductions by night two.</p>
            </div>
          </div>
        </div>
        <div class="group relative grid flex-1 overflow-hidden rounded-[18px] bg-[linear-gradient(oklch(0.2_0.03_260/0.25),oklch(0.15_0.03_260/0.7)),url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center outline-2 outline-offset-[3px] outline-transparent transition-[grid-template-columns,grid-template-rows,flex-grow,outline-color] duration-600 ease-[cubic-bezier(0.3,0.8,0.25,1)] grid-cols-[64px_0fr] has-checked:grid-cols-[64px_1fr] has-checked:grow-[3.2] [&:not(:has(:checked)):hover]:grow-[1.15] has-focus-visible:outline-tfa15-acc @max-tfa15fold:grid-cols-[1fr] @max-tfa15fold:grid-rows-[56px_0fr] @max-tfa15fold:has-checked:grid-cols-[1fr] @max-tfa15fold:has-checked:grid-rows-[56px_1fr] @max-tfa15fold:has-checked:grow-[1] motion-reduce:transition-none">
          <input id="tfa15-p5" type="radio" name="tfa15" class="absolute opacity-0 pointer-events-none">
          <label for="tfa15-p5" class="grid min-w-11 cursor-pointer items-end justify-items-center py-[18px] @max-tfa15fold:min-h-11 @max-tfa15fold:place-items-center @max-tfa15fold:justify-items-start @max-tfa15fold:px-5 @max-tfa15fold:py-0">
            <h3 class="[writing-mode:vertical-rl] rotate-180 text-[13.5px] font-bold uppercase tracking-[0.06em] text-white [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.85)] transition-colors duration-300 group-hover:text-tfa15-acc group-has-checked:text-tfa15-acc @max-tfa15fold:[writing-mode:horizontal-tb] @max-tfa15fold:rotate-0">Cancellation</h3>
          </label>
          <div class="grid min-w-0 items-end overflow-hidden @max-tfa15fold:min-h-0">
            <div class="w-[max(260px,26cqi)] translate-x-3.5 py-[22px] pl-2 pr-6 opacity-0 transition-[translate,opacity] delay-150 duration-500 ease-[cubic-bezier(0.3,0.8,0.25,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:transition-none @max-tfa15fold:w-full @max-tfa15fold:px-5 @max-tfa15fold:pb-5 @max-tfa15fold:pt-0">
              <h2 class="text-[clamp(17px,2.2vw,22px)] font-extrabold tracking-[-0.02em] text-white [text-shadow:0_1px_14px_oklch(0.15_0.03_260/0.8)]">What if I need to cancel?</h2>
              <p class="mt-2.5 text-[13.5px] leading-[1.65] text-white/90 [text-shadow:0_1px_12px_oklch(0.15_0.03_260/0.75)]">Free date changes until 30 days out, full refund minus deposit until 14, and the deposit converts to credit after that. Weather cancellations on our side refund everything.</p>
            </div>
          </div>
        </div>
      </div>

      <p class="mt-5 text-[12.5px] text-white/80">grid-cols-[0fr] → [1fr] plus a grow transition — demo 10's trick, rotated. Folds vertical in narrow containers.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa15-bg: #1b1d2a;
  --color-tfa15-bg: oklch(0.2 0.02 260);
  --color-tfa15-acc: #ffc94d;
  --color-tfa15-acc: oklch(0.85 0.15 80);
  --font-tfa15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  /* Matches the CSS twin's @container (width < 720px) fold. The
       built-in 3xl is 768px, which stacked the panels while there was
       still room for the sideways layout. */
  --container-tfa15fold: 45rem;
}

.tfa-15 {
  width: 100%;
  min-height: 100svh;
}
```
