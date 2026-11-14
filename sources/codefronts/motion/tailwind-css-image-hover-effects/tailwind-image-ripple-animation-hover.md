---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-ripple-animation-hover/"
title: "Tailwind Image Ripple Animation Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Three concentric rings pulse outward on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Ripple Animation Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-ripple-animation-hover/

Three concentric rings pulse outward on hover. The port makes two changes on the way: the keyframe becomes an --animate-tih15-ripple token (so group-hover:animate-tih15-ripple is a real utility), and the rings expand with scale instead of width/height &mdash; the fix the CSS version lists as a customization, taken as the default.
## HTML
```html
<section class="tih-15 w-full min-h-svh grid place-items-center bg-tih15-bg font-tih15-sans px-6 py-10" aria-label="Ripple animation hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article style="--ring:oklch(0.75 0.13 230)" class="group flex flex-col items-center gap-3.5">
      <div class="relative grid place-items-center w-35 h-35">
        <span style="--i:0" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:1" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:2" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <div class="relative z-2 grid place-items-center w-25 h-25 rounded-full text-[42px] bg-[image:url('https://i.pravatar.cc/400?img=31'),radial-gradient(circle,oklch(0.3_0.05_250),oklch(0.45_0.13_240))] bg-cover bg-center bg-no-repeat transition-transform duration-300 ease-tih15 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="text-center">
        <p class="text-sm font-bold text-tih15-text">Dr. Elena Vasquez</p>
        <p class="text-[11px] text-tih15-muted">Mission Architect</p>
        <div class="flex justify-center gap-2 mt-1">
          <a href="#elena-x" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Elena on X">&#120143;</a>
          <a href="#elena-in" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Elena on LinkedIn">in</a>
          <a href="#elena-gh" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Elena on GitHub">gh</a>
        </div>
      </div>
    </article>
    <article style="--ring:oklch(0.75 0.16 305)" class="group flex flex-col items-center gap-3.5">
      <div class="relative grid place-items-center w-35 h-35">
        <span style="--i:0" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:1" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:2" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <div class="relative z-2 grid place-items-center w-25 h-25 rounded-full text-[42px] bg-[image:url('https://i.pravatar.cc/400?img=68'),radial-gradient(circle,oklch(0.25_0.13_305),oklch(0.45_0.2_300))] bg-cover bg-center bg-no-repeat transition-transform duration-300 ease-tih15 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="text-center">
        <p class="text-sm font-bold text-tih15-text">Orion Blackwood</p>
        <p class="text-[11px] text-tih15-muted">AI Research Lead</p>
        <div class="flex justify-center gap-2 mt-1">
          <a href="#orion-x" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Orion on X">&#120143;</a>
          <a href="#orion-in" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Orion on LinkedIn">in</a>
          <a href="#orion-gh" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Orion on GitHub">gh</a>
        </div>
      </div>
    </article>
    <article style="--ring:oklch(0.85 0.16 145)" class="group flex flex-col items-center gap-3.5">
      <div class="relative grid place-items-center w-35 h-35">
        <span style="--i:0" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:1" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <span style="--i:2" class="absolute w-25 h-25 rounded-full border-2 border-[var(--ring)] opacity-0 group-hover:animate-tih15-ripple group-hover:[animation-delay:calc(var(--i)*0.5s)] motion-reduce:group-hover:animate-none" aria-hidden="true"></span>
        <div class="relative z-2 grid place-items-center w-25 h-25 rounded-full text-[42px] bg-[image:url('https://i.pravatar.cc/400?img=24'),radial-gradient(circle,oklch(0.22_0.06_150),oklch(0.45_0.13_150))] bg-cover bg-center bg-no-repeat transition-transform duration-300 ease-tih15 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="text-center">
        <p class="text-sm font-bold text-tih15-text">Freya Lindqvist</p>
        <p class="text-[11px] text-tih15-muted">Growth Engineer</p>
        <div class="flex justify-center gap-2 mt-1">
          <a href="#freya-x" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Freya on X">&#120143;</a>
          <a href="#freya-in" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Freya on LinkedIn">in</a>
          <a href="#freya-gh" class="grid place-items-center w-6.5 h-6.5 rounded-full text-xs text-tih15-muted no-underline bg-[oklch(1_0_0/0.06)] border border-[oklch(1_0_0/0.08)] transition-colors duration-200 hover:bg-[oklch(1_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-tih15-acc focus-visible:outline-offset-2" aria-label="Freya on GitHub">gh</a>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih15-bg: #060d0d;
  --color-tih15-bg: oklch(0.11 0.012 190);
  --color-tih15-text: #f1f5f9;
  --color-tih15-text: oklch(0.96 0.005 250);
  --color-tih15-muted: #64748b;
  --color-tih15-muted: oklch(0.58 0.035 255);
  --color-tih15-acc: #2dd4bf;
  --color-tih15-acc: oklch(0.8 0.13 185);
  --font-tih15-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih15: cubic-bezier(0.34, 1.56, 0.64, 1);
  --animate-tih15-ripple: tih15-ripple 1.5s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
/* Keyframes have no utility form and never will - this is the category that
   belongs in CSS. The scale-based version replaces the original's width/height
   animation, so the rings expand on the compositor instead of relaying out. */

@keyframes tih15-ripple {
  0% {
    scale: 1;
    opacity: 0.6;
  }

  100% {
    scale: 1.4;
    opacity: 0;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-15 {
  width: 100%;
  min-height: 100svh;
}

.tih-15 ::selection {
  background: oklch(0.8 0.13 185);
  color: #000;
}
```
