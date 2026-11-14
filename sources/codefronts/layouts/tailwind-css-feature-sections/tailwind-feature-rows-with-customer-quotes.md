---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-rows-with-customer-quotes/"
title: "Tailwind Feature Rows with Customer Quotes"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Every feature claim backed by a customer: three feature cards, each closing on a short quote, a named person and the metric they saw."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Rows with Customer Quotes
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-rows-with-customer-quotes/

Every feature claim backed by a customer: three feature cards, each closing on a short quote, a named person and the metric they saw. Cards use grid-rows-subgrid so titles, descriptions and quotes line up across the row regardless of copy length.
## HTML
```html
<section class="tfs-11 w-full min-h-svh bg-tfs11-bg px-5 py-20 font-tfs11-sans text-tfs11-ink antialiased sm:py-28" aria-labelledby="tfs-11-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="grid gap-4 lg:grid-cols-2 lg:items-end">
      <h2 id="tfs-11-h" class="text-balance font-tfs11-serif text-5xl leading-[1.05] sm:text-6xl">Features our customers <em class="text-tfs11-acc">actually</em> talk about</h2>
      <p class="max-w-md text-pretty text-lg text-tfs11-mut lg:justify-self-end">Every claim below comes with the team that measured it.</p>
    </header>
    <div class="grid gap-6 lg:grid-cols-3">
      <article class="grid gap-6 rounded-[1.75rem] bg-white p-7 shadow-[0_1px_0_rgb(0_0_0/0.04),0_20px_50px_-30px_rgb(68_40_20/0.35)] ring-1 ring-tfs11-line lg:row-span-3 lg:grid-rows-subgrid">
        <div class="flex items-center gap-3"><span class="grid size-10 place-items-center rounded-full bg-tfs11-ink text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg></span><h3 class="text-xl font-semibold">Instant search</h3></div>
        <p class="text-pretty text-tfs11-mut">Find any message, file or decision across every workspace in under 50 ms.</p>
        <figure class="grid content-start gap-4 rounded-2xl bg-tfs11-bg p-5">
          <blockquote class="font-tfs11-serif text-xl leading-snug text-pretty">“We stopped asking “where did we decide that?” Search just answers it.”</blockquote>
          <figcaption class="flex flex-wrap items-center gap-3 text-sm"><span class="grid size-10 place-items-center rounded-full bg-amber-200 text-amber-900 text-xs font-bold">AC</span><span class="min-w-0 flex-1"><strong class="block font-semibold">Alex Chen</strong><span class="text-tfs11-mut">Eng Lead, Orbit</span></span><span class="rounded-full bg-tfs11-acc px-2.5 py-1 text-xs font-semibold text-white">4× faster lookups</span></figcaption>
        </figure>
      </article>
      <article class="grid gap-6 rounded-[1.75rem] bg-white p-7 shadow-[0_1px_0_rgb(0_0_0/0.04),0_20px_50px_-30px_rgb(68_40_20/0.35)] ring-1 ring-tfs11-line lg:row-span-3 lg:grid-rows-subgrid">
        <div class="flex items-center gap-3"><span class="grid size-10 place-items-center rounded-full bg-tfs11-ink text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M3 3h6v6H3zM15 15h6v6h-6zM6 9v3a3 3 0 0 0 3 3h6"/></svg></span><h3 class="text-xl font-semibold">Automated handoffs</h3></div>
        <p class="text-pretty text-tfs11-mut">Tickets route themselves to the right owner based on code ownership and on-call.</p>
        <figure class="grid content-start gap-4 rounded-2xl bg-tfs11-bg p-5">
          <blockquote class="font-tfs11-serif text-xl leading-snug text-pretty">“Our handoff backlog went from forty tickets to zero in a fortnight.”</blockquote>
          <figcaption class="flex flex-wrap items-center gap-3 text-sm"><span class="grid size-10 place-items-center rounded-full bg-rose-200 text-rose-900 text-xs font-bold">PS</span><span class="min-w-0 flex-1"><strong class="block font-semibold">Priya Sharma</strong><span class="text-tfs11-mut">Head of Support, Vale</span></span><span class="rounded-full bg-tfs11-acc px-2.5 py-1 text-xs font-semibold text-white">−92% backlog</span></figcaption>
        </figure>
      </article>
      <article class="grid gap-6 rounded-[1.75rem] bg-white p-7 shadow-[0_1px_0_rgb(0_0_0/0.04),0_20px_50px_-30px_rgb(68_40_20/0.35)] ring-1 ring-tfs11-line lg:row-span-3 lg:grid-rows-subgrid">
        <div class="flex items-center gap-3"><span class="grid size-10 place-items-center rounded-full bg-tfs11-ink text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg></span><h3 class="text-xl font-semibold">Usage insights</h3></div>
        <p class="text-pretty text-tfs11-mut">See which features each account uses, and which ones are quietly churning.</p>
        <figure class="grid content-start gap-4 rounded-2xl bg-tfs11-bg p-5">
          <blockquote class="font-tfs11-serif text-xl leading-snug text-pretty">“We caught three at-risk enterprise renewals a full quarter early.”</blockquote>
          <figcaption class="flex flex-wrap items-center gap-3 text-sm"><span class="grid size-10 place-items-center rounded-full bg-emerald-200 text-emerald-900 text-xs font-bold">JL</span><span class="min-w-0 flex-1"><strong class="block font-semibold">Jordan Lee</strong><span class="text-tfs11-mut">VP Customer Success, Talon</span></span><span class="rounded-full bg-tfs11-acc px-2.5 py-1 text-xs font-semibold text-white">$1.2M saved</span></figcaption>
        </figure>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs11-bg: #f7f1ea;
  --color-tfs11-bg: oklch(0.961 0.011 72);
  --color-tfs11-ink: #2a1d14;
  --color-tfs11-ink: oklch(0.244 0.026 56);
  --color-tfs11-mut: #5f5046;
  --color-tfs11-mut: oklch(0.443 0.026 56);
  --color-tfs11-line: #ebe1d6;
  --color-tfs11-line: oklch(0.915 0.018 70);
  --color-tfs11-acc: #b45309;
  --color-tfs11-acc: oklch(0.555 0.146 49);
  --font-tfs11-serif: 'Instrument Serif', Georgia, serif;
  --font-tfs11-sans: 'DM Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-11 {
  width: 100%;
  min-height: 100svh;
}
```
