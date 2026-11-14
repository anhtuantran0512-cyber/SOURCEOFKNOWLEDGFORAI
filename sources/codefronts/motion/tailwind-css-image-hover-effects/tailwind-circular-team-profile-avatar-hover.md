---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-circular-team-profile-avatar-hover/"
title: "Tailwind Circular Team Profile Avatar Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A comet-tail arc that spins only while hovered &mdash; not by adding the animation, but by flipping animation-play-state from paused to running, so the arc…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Circular Team Profile Avatar Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-circular-team-profile-avatar-hover/

A comet-tail arc that spins only while hovered &mdash; not by adding the animation, but by flipping animation-play-state from paused to running, so the arc resumes from wherever it stopped. In utilities that is two arbitrary properties on a before: chain, and the rest of the ring is bg-conic-[…].
## HTML
```html
<section class="tih-16 w-full min-h-svh grid place-items-center bg-tih16-bg font-tih16-sans px-6 py-10" aria-label="Circular avatar hover with spinning ring demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-2 sm:grid-cols-4">
    <article style="--ring:oklch(0.75 0.16 300)" class="group flex flex-col items-center gap-2.5">
      <div class="relative w-20 h-20 overflow-hidden rounded-full before:content-[''] before:absolute before:-inset-[3px] before:rounded-full before:bg-conic-[from_0deg,transparent_0deg_270deg,var(--ring)_270deg_360deg] before:opacity-0 before:transition-opacity before:duration-300 before:animate-tih16-spin before:[animation-play-state:paused] group-hover:before:opacity-100 group-hover:before:[animation-play-state:running] motion-reduce:group-hover:before:[animation-play-state:paused]">
        <div class="relative z-2 grid place-items-center w-[74px] h-[74px] m-[3px] rounded-full text-[34px] bg-[image:url('https://i.pravatar.cc/400?img=5'),radial-gradient(circle_at_30%_30%,oklch(0.35_0.18_295),oklch(0.2_0.03_265))] bg-cover bg-center bg-no-repeat transition-transform duration-350 ease-tih16 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <p class="text-xs font-bold text-center text-tih16-text">Yuki Tanaka</p>
      <p class="-mt-2 text-[10px] text-center text-tih16-muted">Frontend Eng.</p>
      <div class="flex gap-1.5 opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 ease-tih16 group-hover:opacity-100 group-hover:translate-y-0 focus-within:opacity-100 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">
        <a href="#yuki-x" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Yuki on X">&#120143;</a>
        <a href="#yuki-gh" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Yuki on GitHub">gh</a>
      </div>
    </article>
    <article style="--ring:oklch(0.8 0.14 163)" class="group flex flex-col items-center gap-2.5">
      <div class="relative w-20 h-20 overflow-hidden rounded-full before:content-[''] before:absolute before:-inset-[3px] before:rounded-full before:bg-conic-[from_0deg,transparent_0deg_270deg,var(--ring)_270deg_360deg] before:opacity-0 before:transition-opacity before:duration-300 before:animate-tih16-spin before:[animation-play-state:paused] group-hover:before:opacity-100 group-hover:before:[animation-play-state:running] motion-reduce:group-hover:before:[animation-play-state:paused]">
        <div class="relative z-2 grid place-items-center w-[74px] h-[74px] m-[3px] rounded-full text-[34px] bg-[image:url('https://i.pravatar.cc/400?img=14'),radial-gradient(circle_at_30%_30%,oklch(0.42_0.09_165),oklch(0.2_0.03_265))] bg-cover bg-center bg-no-repeat transition-transform duration-350 ease-tih16 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <p class="text-xs font-bold text-center text-tih16-text">Amara Diallo</p>
      <p class="-mt-2 text-[10px] text-center text-tih16-muted">UX Designer</p>
      <div class="flex gap-1.5 opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 ease-tih16 group-hover:opacity-100 group-hover:translate-y-0 focus-within:opacity-100 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">
        <a href="#amara-x" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Amara on X">&#120143;</a>
        <a href="#amara-be" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Amara on Behance">be</a>
      </div>
    </article>
    <article style="--ring:oklch(0.76 0.16 55)" class="group flex flex-col items-center gap-2.5">
      <div class="relative w-20 h-20 overflow-hidden rounded-full before:content-[''] before:absolute before:-inset-[3px] before:rounded-full before:bg-conic-[from_0deg,transparent_0deg_270deg,var(--ring)_270deg_360deg] before:opacity-0 before:transition-opacity before:duration-300 before:animate-tih16-spin before:[animation-play-state:paused] group-hover:before:opacity-100 group-hover:before:[animation-play-state:running] motion-reduce:group-hover:before:[animation-play-state:paused]">
        <div class="relative z-2 grid place-items-center w-[74px] h-[74px] m-[3px] rounded-full text-[34px] bg-[image:url('https://i.pravatar.cc/400?img=60'),radial-gradient(circle_at_30%_30%,oklch(0.45_0.11_60),oklch(0.2_0.03_265))] bg-cover bg-center bg-no-repeat transition-transform duration-350 ease-tih16 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <p class="text-xs font-bold text-center text-tih16-text">Ravi Patel</p>
      <p class="-mt-2 text-[10px] text-center text-tih16-muted">Data Scientist</p>
      <div class="flex gap-1.5 opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 ease-tih16 group-hover:opacity-100 group-hover:translate-y-0 focus-within:opacity-100 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">
        <a href="#ravi-x" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Ravi on X">&#120143;</a>
        <a href="#ravi-in" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Ravi on LinkedIn">in</a>
      </div>
    </article>
    <article style="--ring:oklch(0.74 0.14 250)" class="group flex flex-col items-center gap-2.5">
      <div class="relative w-20 h-20 overflow-hidden rounded-full before:content-[''] before:absolute before:-inset-[3px] before:rounded-full before:bg-conic-[from_0deg,transparent_0deg_270deg,var(--ring)_270deg_360deg] before:opacity-0 before:transition-opacity before:duration-300 before:animate-tih16-spin before:[animation-play-state:paused] group-hover:before:opacity-100 group-hover:before:[animation-play-state:running] motion-reduce:group-hover:before:[animation-play-state:paused]">
        <div class="relative z-2 grid place-items-center w-[74px] h-[74px] m-[3px] rounded-full text-[34px] bg-[image:url('https://i.pravatar.cc/400?img=9'),radial-gradient(circle_at_30%_30%,oklch(0.3_0.05_250),oklch(0.2_0.03_265))] bg-cover bg-center bg-no-repeat transition-transform duration-350 ease-tih16 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <p class="text-xs font-bold text-center text-tih16-text">Zoe Mercer</p>
      <p class="-mt-2 text-[10px] text-center text-tih16-muted">DevOps Lead</p>
      <div class="flex gap-1.5 opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 ease-tih16 group-hover:opacity-100 group-hover:translate-y-0 focus-within:opacity-100 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">
        <a href="#zoe-gh" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Zoe on GitHub">gh</a>
        <a href="#zoe-in" class="px-1.25 py-0.5 rounded text-xs text-tih16-muted no-underline bg-[oklch(1_0_0/0.07)] focus-visible:outline-2 focus-visible:outline-tih16-acc focus-visible:outline-offset-2" aria-label="Zoe on LinkedIn">in</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih16-bg: #080812;
  --color-tih16-bg: oklch(0.12 0.015 285);
  --color-tih16-text: #f1f5f9;
  --color-tih16-text: oklch(0.96 0.005 250);
  --color-tih16-muted: #64748b;
  --color-tih16-muted: oklch(0.58 0.035 255);
  --color-tih16-acc: #a78bfa;
  --color-tih16-acc: oklch(0.75 0.16 300);
  --font-tih16-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih16: cubic-bezier(0.34, 1.56, 0.64, 1);
  --animate-tih16-spin: tih16-spin 1.2s linear infinite;
}

@keyframes tih16-spin {
  to {
    rotate: 360deg;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-16 {
  width: 100%;
  min-height: 100svh;
}

.tih-16 ::selection {
  background: oklch(0.75 0.16 300);
  color: #000;
}
/* @supports has no variant form: engines without conic-gradient get a solid ring. */

@supports not (background: conic-gradient(red, blue)) {
  .tih-16 .group > div::before {
    background: var(--ring);
  }
}
```
