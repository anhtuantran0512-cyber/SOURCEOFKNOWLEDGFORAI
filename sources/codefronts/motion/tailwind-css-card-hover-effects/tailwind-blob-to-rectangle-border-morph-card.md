---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-blob-to-rectangle-border-morph-card/"
title: "Tailwind Blob-to-Rectangle Border Morph Card"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A meditation card that rests as an organic blob and settles into a clean rounded rectangle on hover, with the icon and button reshaping in sync."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blob-to-Rectangle Border Morph Card
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-blob-to-rectangle-border-morph-card/

A meditation card that rests as an organic blob and settles into a clean rounded rectangle on hover, with the icon and button reshaping in sync. Three elements morph on one spring curve, and because the curve is shared it becomes a @theme easing token.
## HTML
```html
<section class="tch-22 w-full min-h-svh grid place-items-center bg-tch22-bg bg-[radial-gradient(circle_at_80%_10%,#ffe0cc,transparent_50%)] font-tch22-sans p-8">
  <article tabindex="0" class="group relative w-[320px] h-[420px] overflow-hidden cursor-pointer outline-none text-white bg-[linear-gradient(155deg,#ff7e54,#ff4d8d)] rounded-[38%_62%_63%_37%/41%_44%_56%_59%] shadow-[0_20px_45px_rgb(255_77_141/0.35)] transition-[border-radius,translate,box-shadow] duration-700 ease-tch22-settle hover:rounded-[28px] hover:-translate-y-1.5 hover:shadow-[0_30px_60px_rgb(255_77_141/0.45)] focus-visible:rounded-[28px] focus-visible:-translate-y-1.5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:duration-150 before:content-[''] before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_30%_20%,rgb(255_255_255/0.35),transparent_55%)]">
    <div class="relative z-2 h-full p-[2.6rem] flex flex-col justify-between">
      <div class="grid place-items-center size-14 rounded-full bg-white/25 text-[1.6rem] transition-[border-radius] duration-700 ease-tch22-settle group-hover:rounded-2xl group-focus-visible:rounded-2xl motion-reduce:duration-150">🫧</div>
      <div>
        <h2 class="font-tch22-display font-bold text-[2.5rem] leading-none">Bubble<br>Wellness</h2>
        <p class="text-[0.9rem] leading-[1.6] text-white/90 mt-2">A meditation app that breathes with you. Shapes soften and settle as you exhale.</p>
      </div>
      <a href="#" class="self-start inline-flex items-center min-h-11 px-6 rounded-full bg-white text-tch22-acc font-tch22-display font-semibold text-[0.9rem] no-underline transition-[border-radius] duration-700 ease-tch22-settle group-hover:rounded-xl focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:duration-150">Try a session</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch22-bg: #fef0e6;
  --color-tch22-bg: oklch(0.96 0.02 55);
  --color-tch22-acc: #ff4d8d;
  --color-tch22-acc: oklch(0.68 0.22 5);
  --font-tch22-sans: 'DM Sans', system-ui, sans-serif;
  --font-tch22-display: 'Fredoka', system-ui, sans-serif;
  --ease-tch22-settle: cubic-bezier(0.34, 1.4, 0.5, 1);
}

.tch-22 {
  width: 100%;
  min-height: 100svh;
}
```
