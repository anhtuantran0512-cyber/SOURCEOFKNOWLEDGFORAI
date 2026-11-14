---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-accordion/"
title: "Tailwind Liquid Glass Accordion"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "An FAQ where each panel is a glass card that opens fluidly &mdash; the 0fr &rarr; 1fr grid trick, written as two utilities."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Accordion
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-accordion/

An FAQ where each panel is a glass card that opens fluidly &mdash; the 0fr &rarr; 1fr grid trick, written as two utilities. It is the cleanest answer to 'you cannot animate height:auto', it needs no JavaScript, and on native <details> the keyboard and screen-reader behaviour is already correct.
## HTML
```html
<section class="lgt-16 grid w-full min-h-svh place-items-center p-15 font-lgt16-sans bg-[image:url('https://picsum.photos/seed/lgfaq/1100/800')] bg-cover bg-center bg-fixed" aria-label="Tailwind liquid glass FAQ accordion">
  <div class="flex w-[min(560px,94vw)] flex-col gap-3.5">

    <details open class="group overflow-hidden rounded-[18px] border border-white/28 bg-white/10 backdrop-blur-[18px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_16px_34px_-22px_rgba(0,0,0,.6)] transition-colors duration-300 open:border-white/50">
      <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-5 py-4.5 text-base font-bold text-white focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-white [&amp;::-webkit-details-marker]:hidden">
        What is Liquid Glass?
        <span aria-hidden="true" class="relative size-5 flex-none before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-3.5 before:-translate-x-1/2 before:-translate-y-1/2 before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-3.5 after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-90 after:bg-white after:transition-transform after:duration-300 group-open:after:rotate-0 motion-reduce:after:transition-none"></span>
      </summary>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out group-open:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-[15px] leading-relaxed text-white/90">A translucent material that samples and refracts what's behind it &mdash; frosted blur plus specular light and, at its richest, real SVG displacement. It's the design language Apple introduced at WWDC 2025.</p></div>
      </div>
    </details>

    <details class="group overflow-hidden rounded-[18px] border border-white/28 bg-white/10 backdrop-blur-[18px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_16px_34px_-22px_rgba(0,0,0,.6)] transition-colors duration-300 open:border-white/50">
      <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-5 py-4.5 text-base font-bold text-white focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-white [&amp;::-webkit-details-marker]:hidden">
        Is it good for performance?
        <span aria-hidden="true" class="relative size-5 flex-none before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-3.5 before:-translate-x-1/2 before:-translate-y-1/2 before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-3.5 after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-90 after:bg-white after:transition-transform after:duration-300 group-open:after:rotate-0 motion-reduce:after:transition-none"></span>
      </summary>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out group-open:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-[15px] leading-relaxed text-white/90">Yes, when disciplined: animate transform, opacity and filter only, cap blur radii, isolate paint with <code>isolate</code>, and reserve boxes so layout shift stays at zero. This demo ships no JavaScript at all.</p></div>
      </div>
    </details>

    <details class="group overflow-hidden rounded-[18px] border border-white/28 bg-white/10 backdrop-blur-[18px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_16px_34px_-22px_rgba(0,0,0,.6)] transition-colors duration-300 open:border-white/50">
      <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-5 py-4.5 text-base font-bold text-white focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-white [&amp;::-webkit-details-marker]:hidden">
        Is it accessible?
        <span aria-hidden="true" class="relative size-5 flex-none before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-3.5 before:-translate-x-1/2 before:-translate-y-1/2 before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-3.5 after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-90 after:bg-white after:transition-transform after:duration-300 group-open:after:rotate-0 motion-reduce:after:transition-none"></span>
      </summary>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out group-open:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-[15px] leading-relaxed text-white/90">Built on native details/summary, so keyboard toggling and disclosure semantics come free. Keep text on a solid-enough tint to hold WCAG contrast over busy backdrops.</p></div>
      </div>
    </details>

    <details class="group overflow-hidden rounded-[18px] border border-white/28 bg-white/10 backdrop-blur-[18px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_16px_34px_-22px_rgba(0,0,0,.6)] transition-colors duration-300 open:border-white/50">
      <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-5 py-4.5 text-base font-bold text-white focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-white [&amp;::-webkit-details-marker]:hidden">
        How does it map to Tailwind?
        <span aria-hidden="true" class="relative size-5 flex-none before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-3.5 before:-translate-x-1/2 before:-translate-y-1/2 before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-3.5 after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-90 after:bg-white after:transition-transform after:duration-300 group-open:after:rotate-0 motion-reduce:after:transition-none"></span>
      </summary>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out group-open:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-[15px] leading-relaxed text-white/90">Directly: <code>backdrop-blur-[18px] backdrop-saturate-170 bg-white/10 border-white/28 rounded-[18px]</code>. Colours become <code>@theme</code> entries, states become variants, and only <code>@property</code>, <code>@keyframes</code> and vendor pseudo-elements stay as CSS.</p></div>
      </div>
    </details>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-lgt16-sans: 'Manrope', system-ui, sans-serif;
}
```
