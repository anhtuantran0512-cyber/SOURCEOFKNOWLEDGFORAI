---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-button-with-glossy-highlight/"
title: "Tailwind Liquid Glass Button with Glossy Highlight"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A capsule CTA in the macOS Tahoe / iOS 26 language, and a clean demonstration of what group buys you: the sweep lives on an after: layer parked off-screen,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Button with Glossy Highlight
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-button-with-glossy-highlight/

A capsule CTA in the macOS Tahoe / iOS 26 language, and a clean demonstration of what group buys you: the sweep lives on an after: layer parked off-screen, and group-hover:after:[transform:...] plus its group-focus-visible: twin drives it across. Two buttons, one shared class string, and the primary variant differs only by its gradient fill.
## HTML
```html
<section class="lgt-02 grid w-full min-h-svh place-items-center p-15 font-lgt02-sans bg-[image:url('https://picsum.photos/seed/lgbtn/1200/900')] bg-cover bg-center bg-fixed" aria-label="Tailwind liquid glass buttons">
  <div class="flex flex-wrap items-center justify-center gap-5">
    <button type="button" class="group relative isolate overflow-hidden cursor-pointer rounded-full border border-lgt02-accent/60 bg-linear-to-b from-lgt02-accent-top to-lgt02-accent px-8.5 py-4 text-base font-bold text-white backdrop-blur-[16px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.6),inset_0_-8px_18px_-10px_rgba(0,0,0,.5),0_14px_30px_-16px_rgba(0,0,0,.6)] transition-[transform,box-shadow] duration-200 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 active:translate-y-0 active:scale-97 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white after:pointer-events-none after:absolute after:inset-y-0 after:left-0 after:z-2 after:w-3/5 after:[background:linear-gradient(105deg,transparent_20%,rgba(255,255,255,.55)_50%,transparent_80%)] after:[transform:translateX(-160%)_skewX(-12deg)] after:transition-transform after:duration-700 after:ease-lgt02 group-hover:after:[transform:translateX(230%)_skewX(-12deg)] group-focus-visible:after:[transform:translateX(230%)_skewX(-12deg)] motion-reduce:transition-none motion-reduce:after:transition-none motion-reduce:group-hover:after:[transform:translateX(-160%)_skewX(-12deg)]">Get started</button>

    <button type="button" class="group relative isolate overflow-hidden cursor-pointer rounded-full border border-white/40 bg-white/14 px-8.5 py-4 text-base font-bold text-white backdrop-blur-[16px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.6),inset_0_-8px_18px_-10px_rgba(0,0,0,.5),0_14px_30px_-16px_rgba(0,0,0,.6)] transition-[transform,box-shadow] duration-200 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 active:translate-y-0 active:scale-97 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white after:pointer-events-none after:absolute after:inset-y-0 after:left-0 after:z-2 after:w-3/5 after:[background:linear-gradient(105deg,transparent_20%,rgba(255,255,255,.55)_50%,transparent_80%)] after:[transform:translateX(-160%)_skewX(-12deg)] after:transition-transform after:duration-700 after:ease-lgt02 group-hover:after:[transform:translateX(230%)_skewX(-12deg)] group-focus-visible:after:[transform:translateX(230%)_skewX(-12deg)] motion-reduce:transition-none motion-reduce:after:transition-none motion-reduce:group-hover:after:[transform:translateX(-160%)_skewX(-12deg)]">Learn more</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt02-accent: #6a4bff;
  --color-lgt02-accent: oklch(0.62 0.2 275);
  --color-lgt02-accent-top: #8168ff;
  --color-lgt02-accent-top: oklch(0.68 0.18 275);
  --font-lgt02-sans: 'Manrope', system-ui, sans-serif;
  --ease-lgt02: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```
