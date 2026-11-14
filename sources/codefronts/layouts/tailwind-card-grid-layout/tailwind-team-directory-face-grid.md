---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-team-directory-face-grid/"
title: "Tailwind Team Directory Face Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A directory whose avatars break the top edge of their cards, done with the oldest trick in CSS: a negative top margin equal to half the avatar's height, over…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Team Directory Face Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-team-directory-face-grid/

A directory whose avatars break the top edge of their cards, done with the oldest trick in CSS: a negative top margin equal to half the avatar's height, over a card with matching top padding. In utilities the two numbers that must stay in sync (w-21 h-21 and -mt-12.5) finally sit on the same element.
## HTML
```html
<section class="tcg-05 w-full min-h-svh bg-tcg05-bg font-tcg05-sans text-tcg05-ink px-6 pt-16 pb-12" aria-label="Team directory face grid demo">
  <div class="max-w-[880px] mx-auto grid [grid-template-columns:repeat(auto-fit,minmax(200px,1fr))] gap-6 [row-gap:56px]">

    <article class="relative px-5 pt-14 pb-6 text-center rounded-2xl border border-tcg05-line bg-tcg05-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_16px_32px_-20px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-21 h-21 -mt-12.5 mx-auto mb-3 rounded-full border-4 border-white shadow-[0_2px_8px_oklch(0_0_0/0.12)] bg-linear-[135deg,#fbbf24,#f97316]" aria-hidden="true"></div>
      <h3 class="text-base font-bold">Dana Whitfield</h3>
      <p class="mt-1 text-[.82rem] text-tcg05-muted">Head of Product Design</p>
      <div class="flex justify-center gap-2.5 mt-4">
        <a href="#dana-linkedin" aria-label="Dana Whitfield on LinkedIn" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">in</a>
        <a href="#dana-x" aria-label="Dana Whitfield on X" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">tw</a>
        <a href="#dana-github" aria-label="Dana Whitfield on GitHub" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">gh</a>
      </div>
    </article>

    <article class="relative px-5 pt-14 pb-6 text-center rounded-2xl border border-tcg05-line bg-tcg05-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_16px_32px_-20px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-21 h-21 -mt-12.5 mx-auto mb-3 rounded-full border-4 border-white shadow-[0_2px_8px_oklch(0_0_0/0.12)] bg-linear-[135deg,#34d399,#0ea5e9]" aria-hidden="true"></div>
      <h3 class="text-base font-bold">Idris Bello</h3>
      <p class="mt-1 text-[.82rem] text-tcg05-muted">Staff Engineer</p>
      <div class="flex justify-center gap-2.5 mt-4">
        <a href="#idris-linkedin" aria-label="Idris Bello on LinkedIn" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">in</a>
        <a href="#idris-x" aria-label="Idris Bello on X" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">tw</a>
        <a href="#idris-github" aria-label="Idris Bello on GitHub" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">gh</a>
      </div>
    </article>

    <article class="relative px-5 pt-14 pb-6 text-center rounded-2xl border border-tcg05-line bg-tcg05-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_16px_32px_-20px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-21 h-21 -mt-12.5 mx-auto mb-3 rounded-full border-4 border-white shadow-[0_2px_8px_oklch(0_0_0/0.12)] bg-linear-[135deg,#f472b6,#a855f7]" aria-hidden="true"></div>
      <h3 class="text-base font-bold">Lena Ferraro</h3>
      <p class="mt-1 text-[.82rem] text-tcg05-muted">VP of Customer Success</p>
      <div class="flex justify-center gap-2.5 mt-4">
        <a href="#lena-linkedin" aria-label="Lena Ferraro on LinkedIn" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">in</a>
        <a href="#lena-x" aria-label="Lena Ferraro on X" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">tw</a>
        <a href="#lena-github" aria-label="Lena Ferraro on GitHub" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-full bg-tcg05-chip text-tcg05-ink text-[.68rem] font-bold uppercase no-underline transition-[background,color] duration-200 hover:bg-tcg05-ink hover:text-white focus-visible:outline-2 focus-visible:outline-tcg05-accent focus-visible:outline-offset-2 motion-reduce:transition-none">gh</a>
      </div>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg05-bg: #f3f1ee;
  --color-tcg05-bg: oklch(0.95 0.006 85);
  --color-tcg05-card: #ffffff;
  --color-tcg05-card: oklch(1 0 0);
  --color-tcg05-chip: #f3f1ee;
  --color-tcg05-chip: oklch(0.95 0.006 85);
  --color-tcg05-line: #e7e4dd;
  --color-tcg05-line: oklch(0.91 0.008 90);
  --color-tcg05-ink: #1f2937;
  --color-tcg05-ink: oklch(0.29 0.03 260);
  --color-tcg05-muted: #5b6270;
  --color-tcg05-muted: oklch(0.48 0.02 260);
  --color-tcg05-accent: #a855f7;
  --color-tcg05-accent: oklch(0.63 0.24 303);
  --font-tcg05-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-05 {
  width: 100%;
  min-height: 100svh;
}

.tcg-05 ::selection {
  background: #a855f7;
  color: #fff;
}
```
