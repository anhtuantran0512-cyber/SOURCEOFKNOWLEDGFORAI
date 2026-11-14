---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-css-blockquote-testimonial-component/"
title: "Tailwind CSS Blockquote Testimonial Component"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "The canonical Tailwind testimonial — logo, quote, avatar, name and role on a ringed dark card — now in its native language."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Blockquote Testimonial Component
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-css-blockquote-testimonial-component/

The canonical Tailwind testimonial — logo, quote, avatar, name and role on a ringed dark card — now in its native language. The CSS original emulated ring-1 ring-white/10 with box-shadow; here the ring is the ring, the avatar gets ring-offset, and the footer re-stacks with v4's built-in @container / @max-[26rem]: variants instead of a hand-written container query.
## HTML
```html
<section class="tbq-02 w-full min-h-svh grid place-items-center bg-tbq02-bg bg-[radial-gradient(90%_70%_at_50%_110%,var(--color-tbq02-glow),transparent)] px-5 py-14 font-tbq02-sans text-tbq02-ink" aria-label="Tailwind blockquote testimonial component demo">
  <div class="grid w-full justify-items-center gap-7">
    <figure class="@container relative w-full max-w-xl rounded-2xl bg-tbq02-card p-8 shadow-[0_24px_60px_-20px_oklch(0_0_0/0.6)] ring-1 ring-white/10">
      <span aria-hidden="true" class="pointer-events-none absolute inset-x-10 -top-px h-px bg-linear-to-r from-transparent via-tbq02-acc to-transparent"></span>
      <svg class="mb-6 block size-8 text-tbq02-acc" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 4l12 7v10l-12 7L4 21V11z" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="16" cy="16" r="4.2" fill="currentColor"/></svg>
      <blockquote>
        <p class="text-lg/[1.65] font-semibold tracking-[-0.01em] text-pretty">“Utility classes made our design system reviewable. Every visual decision is right there in the diff — no hunting through stylesheets to find who set that margin.”</p>
      </blockquote>
      <figcaption class="mt-7 flex flex-wrap items-center gap-x-4 gap-y-3">
        <img class="size-11 flex-none rounded-full bg-linear-to-br from-tbq02-acc to-tbq02-acc2 object-cover ring-2 ring-tbq02-acc ring-offset-2 ring-offset-tbq02-card" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=160&auto=format&fit=crop" alt="" width="44" height="44" loading="lazy">
        <div>
          <div class="text-[15px] font-semibold">Judith Black</div>
          <div class="mt-0.5 text-sm text-tbq02-mut">CEO of Workcation</div>
        </div>
        <span aria-hidden="true" class="ml-auto h-7 w-px bg-white/12 @max-[26rem]:hidden"></span>
        <div aria-hidden="true" class="font-tbq02-mono text-[11px] text-tbq02-mut @max-[26rem]:hidden">ring-1 · ring-white/10</div>
      </figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tbq02-mono text-[11.5px] text-tbq02-mut ring-1 ring-white/10">@container · ring-offset avatar · text-lg/[1.65]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq02-bg: #06090f;
  --color-tbq02-bg: oklch(0.14 0.015 265);
  --color-tbq02-glow: #171c3b99;
  --color-tbq02-glow: oklch(0.24 0.06 275 / 0.6);
  --color-tbq02-card: #141822;
  --color-tbq02-card: oklch(0.21 0.02 265);
  --color-tbq02-ink: #f3f5f8;
  --color-tbq02-ink: oklch(0.97 0.005 250);
  --color-tbq02-mut: #b0b8c5;
  --color-tbq02-mut: oklch(0.78 0.02 260);
  --color-tbq02-acc: #7c8cff;
  --color-tbq02-acc: oklch(0.68 0.17 275);
  --color-tbq02-acc2: #5e4784;
  --color-tbq02-acc2: oklch(0.45 0.1 300);
  --font-tbq02-sans: 'Geist', system-ui, sans-serif;
  --font-tbq02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-02 {
  width: 100%;
  min-height: 100svh;
}
```
