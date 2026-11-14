---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-drifting-aurora-ribbons-card/"
title: "Tailwind Drifting Aurora Ribbons Card with Blurred Gradient Bands"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Two blurred gradient ribbons drift across a starfield and sharpen on hover &mdash; the blur drops from 28px to 20px and the opacity climbs, so the aurora…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Drifting Aurora Ribbons Card with Blurred Gradient Bands
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-drifting-aurora-ribbons-card/

Two blurred gradient ribbons drift across a starfield and sharpen on hover &mdash; the blur drops from 28px to 20px and the opacity climbs, so the aurora seems to gather strength. The second band reuses the first's keyframe with a longer duration and reverse direction, which is what breaks the symmetry.
## HTML
```html
<section class="tch-33 w-full min-h-svh grid place-items-center bg-tch33-bg font-tch33-sans p-8">
  <article tabindex="0" class="group relative w-[340px] h-[450px] rounded-[22px] overflow-hidden cursor-pointer outline-none bg-[linear-gradient(180deg,#050b1a_0%,#02040a_100%)] border border-tch33-a/10 focus-visible:outline-2 focus-visible:outline-tch33-a focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:opacity-70 before:bg-[radial-gradient(1px_1px_at_20%_30%,#fff,transparent),radial-gradient(1px_1px_at_70%_20%,#ccffee,transparent),radial-gradient(1px_1px_at_40%_60%,#fff,transparent),radial-gradient(1px_1px_at_85%_75%,#ddffff,transparent),radial-gradient(1px_1px_at_55%_85%,#fff,transparent),radial-gradient(1px_1px_at_10%_80%,#cceeff,transparent)]">
    <div class="absolute -inset-x-[30%] top-[5%] h-3/5 z-1 pointer-events-none opacity-55 blur-[28px] animate-tch33-drift transition-[opacity,filter] duration-600 group-hover:opacity-85 group-hover:blur-[20px] group-focus-visible:opacity-85 group-focus-visible:blur-[20px] motion-reduce:animate-none bg-[radial-gradient(ellipse_60%_100%_at_30%_50%,#2cffa6_0%,transparent_60%),radial-gradient(ellipse_50%_100%_at_60%_40%,#3ad0ff_0%,transparent_60%),radial-gradient(ellipse_55%_100%_at_80%_60%,#b06cff_0%,transparent_60%)]"></div>
    <div class="absolute -inset-x-[30%] top-[20%] h-3/5 z-1 pointer-events-none opacity-40 blur-[28px] animate-tch33-drift [animation-duration:13s] [animation-direction:reverse] transition-[opacity,filter] duration-600 group-hover:opacity-65 group-hover:blur-[20px] group-focus-visible:opacity-65 motion-reduce:animate-none bg-[radial-gradient(ellipse_50%_100%_at_50%_50%,#5affc4_0%,transparent_60%),radial-gradient(ellipse_50%_100%_at_75%_40%,#6a8cff_0%,transparent_60%)]"></div>
    <div class="relative z-2 h-full p-[2.6rem] flex flex-col justify-end text-tch33-ink">
      <span class="text-[0.72rem] font-medium tracking-[0.3em] uppercase text-tch33-a">Arctic Expeditions</span>
      <h2 class="font-tch33-display font-medium text-[3rem] leading-none mt-2.5 mb-3">Chasing<br>the Lights</h2>
      <p class="font-light text-[0.9rem] leading-[1.65] text-tch33-body">Seven nights in Tromsø under the polar sky. Glass-roof cabins, dog sleds, and the slow green fire overhead.</p>
      <div class="flex justify-between mt-6 pt-4 text-[0.78rem] tracking-[0.08em] text-tch33-a border-t border-tch33-a/20"><span>Sept – March</span><span>from $2,400</span></div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch33-drift {
  0%,
    100% {
    transform: translateX(-6%) translateY(0) skewX(-6deg);
  }

  50% {
    transform: translateX(8%) translateY(-12px) skewX(4deg);
  }
}

@theme {
  --color-tch33-bg: #03060d;
  --color-tch33-bg: oklch(0.08 0.01 250);
  --color-tch33-ink: #eafff6;
  --color-tch33-ink: oklch(0.97 0.02 165);
  --color-tch33-body: #b9d6cc;
  --color-tch33-body: oklch(0.84 0.03 170);
  --color-tch33-a: #7ff0c4;
  --color-tch33-a: oklch(0.89 0.12 165);
  --color-tch33-b: #3ad0ff;
  --color-tch33-b: oklch(0.81 0.13 225);
  --color-tch33-c: #b06cff;
  --color-tch33-c: oklch(0.65 0.21 295);
  --font-tch33-sans: 'Jost', system-ui, sans-serif;
  --font-tch33-display: 'Cormorant Garamond', Georgia, serif;
  --animate-tch33-drift: tch33-drift 9s ease-in-out infinite;
}

.tch-33 {
  width: 100%;
  min-height: 100svh;
}
```
