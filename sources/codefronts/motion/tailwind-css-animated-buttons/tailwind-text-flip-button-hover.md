---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-text-flip-button-hover/"
title: "Tailwind Text Flip Button Hover with 3D Rotation"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "The label pivots away on a horizontal axis and a second message pivots in behind it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Text Flip Button Hover with 3D Rotation
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-text-flip-button-hover/

The label pivots away on a horizontal axis and a second message pivots in behind it. The port's structural gain is group: the button declares it once and both panels read group-hover:, so the two halves of the flip are described on the elements that actually rotate.
## HTML
```html
<section class="tab-10 w-full min-h-svh grid place-items-center bg-tab10-bg font-tab10-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab10-mut m-0">Hover to flip text</p>
    <div class="flex flex-wrap justify-center gap-5">
      <button type="button" class="group p-0 bg-tab10-indigo rounded-[10px] cursor-pointer perspective-[600px] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab10-indigo">
        <span class="relative block w-36 h-12 overflow-hidden transform-3d">
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:-translate-y-full group-hover:rotate-x-90 group-focus-visible:-translate-y-full group-focus-visible:rotate-x-90 motion-reduce:transition-opacity motion-reduce:group-hover:translate-y-0 motion-reduce:group-hover:rotate-x-0 motion-reduce:group-hover:opacity-0">View Pricing</span>
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden translate-y-full -rotate-x-90 transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:translate-y-0 group-hover:rotate-x-0 group-focus-visible:translate-y-0 group-focus-visible:rotate-x-0 motion-reduce:translate-y-0 motion-reduce:rotate-x-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-hover:opacity-100">From $9/mo &rarr;</span>
        </span>
      </button>
      <button type="button" class="group p-0 bg-tab10-teal rounded-[10px] cursor-pointer perspective-[600px] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab10-teal">
        <span class="relative block w-36 h-12 overflow-hidden transform-3d">
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:-translate-y-full group-hover:rotate-x-90 group-focus-visible:-translate-y-full group-focus-visible:rotate-x-90 motion-reduce:transition-opacity motion-reduce:group-hover:translate-y-0 motion-reduce:group-hover:rotate-x-0 motion-reduce:group-hover:opacity-0">Follow Us</span>
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden translate-y-full -rotate-x-90 transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:translate-y-0 group-hover:rotate-x-0 group-focus-visible:translate-y-0 group-focus-visible:rotate-x-0 motion-reduce:translate-y-0 motion-reduce:rotate-x-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-hover:opacity-100">@codefronts</span>
        </span>
      </button>
      <button type="button" class="group p-0 bg-tab10-rose rounded-[10px] cursor-pointer perspective-[600px] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab10-rose">
        <span class="relative block w-36 h-12 overflow-hidden transform-3d">
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:-translate-y-full group-hover:rotate-x-90 group-focus-visible:-translate-y-full group-focus-visible:rotate-x-90 motion-reduce:transition-opacity motion-reduce:group-hover:translate-y-0 motion-reduce:group-hover:rotate-x-0 motion-reduce:group-hover:opacity-0">Join Beta</span>
          <span class="absolute inset-0 flex items-center justify-center text-[0.95rem] font-bold tracking-[0.04em] text-white whitespace-nowrap backface-hidden translate-y-full -rotate-x-90 transition-transform duration-[350ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:translate-y-0 group-hover:rotate-x-0 group-focus-visible:translate-y-0 group-focus-visible:rotate-x-0 motion-reduce:translate-y-0 motion-reduce:rotate-x-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-hover:opacity-100">Spots Left: 3</span>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab10-bg: #0f0c1f;
  --color-tab10-bg: oklch(0.14 0.04 285);
  --color-tab10-mut: #818cf8;
  --color-tab10-mut: oklch(0.7 0.14 279);
  --color-tab10-indigo: #4f46e5;
  --color-tab10-indigo: oklch(0.51 0.24 277);
  --color-tab10-teal: #0d9488;
  --color-tab10-teal: oklch(0.56 0.11 184);
  --color-tab10-rose: #e11d48;
  --color-tab10-rose: oklch(0.57 0.22 13);
  --font-tab10-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-10 {
  width: 100%;
  min-height: 100svh;
}

.tab-10 ::selection {
  background: var(--color-tab10-indigo);
  color: #fff;
}
```
