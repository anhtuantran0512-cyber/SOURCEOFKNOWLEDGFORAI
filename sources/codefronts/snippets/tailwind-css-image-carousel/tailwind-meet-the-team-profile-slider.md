---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-meet-the-team-profile-slider/"
title: "Tailwind Meet the Team Profile Slider with Circular Portraits"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A gently gliding rail of circular staff portraits with names and roles — the 'our people' section on about pages."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Meet the Team Profile Slider with Circular Portraits
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-meet-the-team-profile-slider/

A gently gliding rail of circular staff portraits with names and roles — the 'our people' section on about pages. The whole interaction is two group-hover/group-focus-within pairs, which is the port at its most ordinary and most convincing.
## HTML
```html
<section class="tcar-07 w-full min-h-svh grid place-items-center bg-tcar07-bg font-tcar07-sans px-3 py-10" aria-label="Meet the team">
  <ul tabindex="0" role="group" aria-label="Team members, scrollable" class="list-none flex gap-5 w-[min(720px,100%)] overflow-x-auto px-4 pt-4 pb-6 m-0 snap-x snap-mandatory [scroll-padding:16px] [scrollbar-width:thin] [scrollbar-color:var(--color-tcar07-track)_transparent] focus-visible:outline-3 focus-visible:outline-tcar07-acc focus-visible:outline-offset-2 focus-visible:rounded-2xl">
    <li class="group flex-none basis-[150px] snap-center text-center transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.06] focus-within:scale-[1.06] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
      <img src="https://picsum.photos/seed/team-1/300/300" width="300" height="300" decoding="async" alt="Portrait of Dana Osei" class="size-[130px] mx-auto rounded-full object-cover border-4 border-white bg-tcar07-ph shadow-[0_14px_30px_-18px_oklch(0.35_0.05_200/0.7)] transition-shadow duration-300 group-hover:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)] group-focus-within:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)]">
      <h4 class="mt-4 mb-0.5 text-[15px] font-bold text-tcar07-ink">Dana Osei</h4><p class="text-[12.5px] text-tcar07-mute m-0">Head of Design</p>
    </li>
    <li class="group flex-none basis-[150px] snap-center text-center transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.06] focus-within:scale-[1.06] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
      <img src="https://picsum.photos/seed/team-2/300/300" width="300" height="300" loading="lazy" decoding="async" alt="Portrait of Ravi Menon" class="size-[130px] mx-auto rounded-full object-cover border-4 border-white bg-tcar07-ph shadow-[0_14px_30px_-18px_oklch(0.35_0.05_200/0.7)] transition-shadow duration-300 group-hover:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)] group-focus-within:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)]">
      <h4 class="mt-4 mb-0.5 text-[15px] font-bold text-tcar07-ink">Ravi Menon</h4><p class="text-[12.5px] text-tcar07-mute m-0">Principal Engineer</p>
    </li>
    <li class="group flex-none basis-[150px] snap-center text-center transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.06] focus-within:scale-[1.06] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
      <img src="https://picsum.photos/seed/team-3/300/300" width="300" height="300" loading="lazy" decoding="async" alt="Portrait of Elin Broer" class="size-[130px] mx-auto rounded-full object-cover border-4 border-white bg-tcar07-ph shadow-[0_14px_30px_-18px_oklch(0.35_0.05_200/0.7)] transition-shadow duration-300 group-hover:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)] group-focus-within:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)]">
      <h4 class="mt-4 mb-0.5 text-[15px] font-bold text-tcar07-ink">Elin Broer</h4><p class="text-[12.5px] text-tcar07-mute m-0">Product Manager</p>
    </li>
    <li class="group flex-none basis-[150px] snap-center text-center transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.06] focus-within:scale-[1.06] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
      <img src="https://picsum.photos/seed/team-4/300/300" width="300" height="300" loading="lazy" decoding="async" alt="Portrait of Tomas Vega" class="size-[130px] mx-auto rounded-full object-cover border-4 border-white bg-tcar07-ph shadow-[0_14px_30px_-18px_oklch(0.35_0.05_200/0.7)] transition-shadow duration-300 group-hover:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)] group-focus-within:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)]">
      <h4 class="mt-4 mb-0.5 text-[15px] font-bold text-tcar07-ink">Tomas Vega</h4><p class="text-[12.5px] text-tcar07-mute m-0">UX Researcher</p>
    </li>
    <li class="group flex-none basis-[150px] snap-center text-center transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.06] focus-within:scale-[1.06] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
      <img src="https://picsum.photos/seed/team-5/300/300" width="300" height="300" loading="lazy" decoding="async" alt="Portrait of Yuki Sato" class="size-[130px] mx-auto rounded-full object-cover border-4 border-white bg-tcar07-ph shadow-[0_14px_30px_-18px_oklch(0.35_0.05_200/0.7)] transition-shadow duration-300 group-hover:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)] group-focus-within:shadow-[0_18px_34px_-14px_oklch(0.35_0.05_200/0.6),0_0_0_4px_var(--color-tcar07-acc)]">
      <h4 class="mt-4 mb-0.5 text-[15px] font-bold text-tcar07-ink">Yuki Sato</h4><p class="text-[12.5px] text-tcar07-mute m-0">Design Engineer</p>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar07-bg: #eef4f4;
  --color-tcar07-bg: oklch(0.96 0.012 200);
  --color-tcar07-ph: #d7e6e6;
  --color-tcar07-ph: oklch(0.91 0.02 200);
  --color-tcar07-track: #c4dada;
  --color-tcar07-track: oklch(0.86 0.025 200);
  --color-tcar07-ink: #1c3535;
  --color-tcar07-ink: oklch(0.29 0.03 195);
  --color-tcar07-mute: #4f6b6b;
  --color-tcar07-mute: oklch(0.48 0.03 195);
  --color-tcar07-acc: #3f9c9c;
  --color-tcar07-acc: oklch(0.6 0.13 200);
  --font-tcar07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-07 {
  width: 100%;
  min-height: 100svh;
}

.tcar-07 ::selection {
  background: var(--color-tcar07-acc);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .tcar-07 ul {
    scroll-behavior: auto;
  }
}
```
