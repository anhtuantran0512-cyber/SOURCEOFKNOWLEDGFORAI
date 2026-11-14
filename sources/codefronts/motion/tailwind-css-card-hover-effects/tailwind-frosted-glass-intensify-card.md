---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-frosted-glass-intensify-card/"
title: "Tailwind Frosted Glass Intensify Card with Deepening Backdrop Blur"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A weather widget over a vivid colour field whose frost deepens on hover &mdash; backdrop-blur-[4px] to [22px], with saturation rising alongside."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Frosted Glass Intensify Card with Deepening Backdrop Blur
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-frosted-glass-intensify-card/

A weather widget over a vivid colour field whose frost deepens on hover &mdash; backdrop-blur-[4px] to [22px], with saturation rising alongside. Two utilities and a transition; the port's only subtlety is naming backdrop-filter in the transition property list.
## HTML
```html
<section class="tch-27 w-full min-h-svh grid place-items-center bg-tch27-bg bg-[radial-gradient(circle_at_20%_30%,#ff5ea0_0_22%,transparent_23%),radial-gradient(circle_at_75%_25%,#ffd23f_0_18%,transparent_19%),radial-gradient(circle_at_60%_80%,#2bd9c4_0_26%,transparent_27%),radial-gradient(circle_at_30%_75%,#6a5cff_0_20%,transparent_21%)] font-tch27-sans p-8">
  <article class="group relative w-[340px] h-[440px] rounded-[26px] overflow-hidden cursor-pointer bg-white/8 border border-white/22 backdrop-blur-[4px] backdrop-saturate-[1.1] shadow-[0_18px_50px_rgb(0_0_0/0.3)] transition-[backdrop-filter,background-color,border-color,translate] duration-500 hover:bg-white/16 hover:border-white/40 hover:backdrop-blur-[22px] hover:backdrop-saturate-[1.6] hover:-translate-y-1.5 focus-within:bg-white/16 focus-within:backdrop-blur-[22px] focus-within:-translate-y-1.5 motion-reduce:transition-[backdrop-filter,background-color] motion-reduce:hover:translate-y-0 before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-[45%] before:opacity-50 before:bg-linear-to-b before:from-white/25 before:to-transparent">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-white">
      <span class="self-start text-[0.7rem] tracking-[0.16em] uppercase px-3.5 py-1.5 rounded-full bg-white/20 border border-white/30">Weather · Now</span>
      <h2 class="font-extrabold text-[2.5rem] leading-none [text-shadow:0_2px_20px_rgb(0_0_0/0.35)]">Coastal<br>Forecast</h2>
      <p class="text-[0.88rem] leading-[1.6] text-white/92">A glass widget over a living wallpaper. Hover and the frost thickens, melting the color behind it.</p>
      <div class="flex justify-between items-center text-[0.8rem]"><span>Light fog · breezy</span><b class="text-2xl font-extrabold">18°</b></div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch27-bg: #1a0f2e;
  --color-tch27-bg: oklch(0.2 0.06 295);
  --font-tch27-sans: 'Hanken Grotesk', system-ui, sans-serif;
}

.tch-27 {
  width: 100%;
  min-height: 100svh;
}
```
