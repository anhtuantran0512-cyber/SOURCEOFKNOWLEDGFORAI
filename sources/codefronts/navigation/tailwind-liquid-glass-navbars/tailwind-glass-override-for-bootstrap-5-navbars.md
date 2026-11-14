---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-glass-override-for-bootstrap-5-navbars/"
title: "Tailwind Glass Override for Bootstrap 5 Navbars"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The liquid-glass look retro-fitted onto Bootstrap's navbar shape, and the port with the most real-world friction: Tailwind's generated sheet lives in cascade…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glass Override for Bootstrap 5 Navbars
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-glass-override-for-bootstrap-5-navbars/

The liquid-glass look retro-fitted onto Bootstrap's navbar shape, and the port with the most real-world friction: Tailwind's generated sheet lives in cascade layers, Bootstrap's does not, and an unlayered stylesheet always wins. The markup keeps Bootstrap's structural semantics while the glass comes from utilities, and the notes state plainly what you must configure to make that work.
## HTML
```html
<section class="nbtw-12 grid place-items-start justify-center w-full min-h-svh px-4.5 py-6.5 font-nb12-sans bg-[linear-gradient(120deg,#2b5876,#4e4376_60%,#c94b4b)] bg-[length:180%_180%] animate-nb12-bg motion-reduce:animate-none" aria-label="Bootstrap 5 glass navbar demo">
  <nav class="flex flex-wrap items-center gap-3.5 w-[min(900px,100%)] px-4.5 py-3 rounded-[14px] text-white bg-white/[0.12] border border-white/[0.32] shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_16px_38px_-22px_rgba(0,0,0,.6)] backdrop-blur-[18px] backdrop-saturate-[1.7]" aria-label="Primary">
    <a class="text-lg font-extrabold tracking-[-0.01em] no-underline text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-12">✦ Enterprise</a>
    <button class="hidden ms-auto w-11 h-[38px] rounded-[9px] border border-white/40 bg-white/[0.14] text-white text-xl cursor-pointer max-[640px]:block focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Toggle navigation"><span aria-hidden="true">≡</span></button>
    <div class="flex flex-1 flex-wrap items-center gap-3.5 max-[640px]:basis-full max-[640px]:flex-col max-[640px]:items-stretch">
      <ul class="flex flex-wrap gap-1 list-none ms-auto max-[640px]:flex-col max-[640px]:ms-0">
        <li><a class="flex items-center min-h-10 px-3.5 rounded-[9px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/[0.24] aria-[current=page]:text-white" href="#nbtw-12" aria-current="page">Dashboard</a></li>
        <li><a class="flex items-center min-h-10 px-3.5 rounded-[9px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-12">Projects</a></li>
        <li><a class="flex items-center min-h-10 px-3.5 rounded-[9px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-12">Team</a></li>
        <li><a class="flex items-center min-h-10 px-3.5 rounded-[9px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-12">Billing</a></li>
      </ul>
      <button class="min-h-10 px-4.5 rounded-[9px] border border-[color-mix(in_oklab,var(--color-nb12-accent)_40%,white)] bg-nb12-accent text-white text-sm font-bold cursor-pointer focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button">Log in</button>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-nb12-accent: #3b74e8;
  --color-nb12-accent: oklch(0.6 0.2 255);
  --font-nb12-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb12-bg: nb12-bg 18s ease-in-out infinite;
}

@keyframes nb12-bg {
  50% {
    background-position: 100% 100%;
  }
}
/* In a real Bootstrap project, declare the layer order BEFORE importing either
   framework, so Tailwind's utilities can win without !important:

   @layer bootstrap, theme, base, components, utilities;
   @import "bootstrap/dist/css/bootstrap.css" layer(bootstrap);
   @import "tailwindcss";                                          */
```
