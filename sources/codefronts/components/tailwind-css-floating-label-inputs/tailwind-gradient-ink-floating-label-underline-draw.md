---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-gradient-ink-floating-label-underline-draw/"
title: "Tailwind Gradient-Ink Floating Label with Animated Underline Draw"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The floated label fills with flowing gradient ink while a matching underline draws itself beneath the field."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient-Ink Floating Label with Animated Underline Draw
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-gradient-ink-floating-label-underline-draw/

The floated label fills with flowing gradient ink while a matching underline draws itself beneath the field. The gradient lives once, as an arbitrary custom property on the root ([--tfl02-ink:linear-gradient(…)]), and every surface reads it with bg-[image:var(--tfl02-ink)]. bg-clip-text plus a [-webkit-text-fill-color:…] flip reveals it.
## HTML
```html
<section class="tfl-02 w-full min-h-svh grid place-items-center bg-tfl02-bg bg-[radial-gradient(70%_60%_at_50%_0%,var(--color-tfl02-glow),transparent_70%)] px-5 py-12 font-tfl02-sans [--tfl02-ink:linear-gradient(90deg,var(--color-tfl02-a),var(--color-tfl02-b),var(--color-tfl02-c),var(--color-tfl02-a))]" aria-label="Gradient ink floating label demo">
  <form class="flex w-full max-w-[390px] flex-col gap-6 rounded-3xl border border-tfl02-edge bg-tfl02-card p-8 shadow-[0_30px_80px_-40px_oklch(0_0_0/0.8)]" novalidate>
    <div class="grid gap-1.5">
      <p class="w-fit bg-[image:var(--tfl02-ink)] bg-[length:220%_100%] bg-clip-text text-xs font-bold uppercase tracking-[0.14em] text-transparent">Private beta</p>
      <h3 class="text-2xl font-bold tracking-[-0.02em] text-tfl02-ink">Reserve your invite</h3>
    </div>
    <div class="relative after:pointer-events-none after:absolute after:inset-x-0 after:bottom-0 after:h-[2.5px] after:origin-left after:scale-x-0 after:rounded-full after:bg-[image:var(--tfl02-ink)] after:bg-[length:220%_100%] after:transition-[scale] after:duration-400 after:delay-120 after:ease-[cubic-bezier(.25,.8,.3,1)] after:content-[''] focus-within:after:scale-x-100 focus-within:after:animate-tfl02-flow has-[input:not(:placeholder-shown)]:after:scale-x-100 has-[input:not(:placeholder-shown)]:after:animate-tfl02-flow motion-reduce:after:animate-none">
      <input class="peer h-14 w-full rounded-t-xl rounded-b-sm border-[1.5px] border-tfl02-line bg-tfl02-field px-4 pt-[22px] pb-1.5 text-base text-tfl02-ink outline-hidden transition-[border-color] duration-200 focus:border-tfl02-line-focus" type="text" id="tfl-02-handle" name="nickname" placeholder=" " autocomplete="nickname">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 bg-[image:var(--tfl02-ink)] bg-[length:220%_100%] bg-clip-text text-base [-webkit-text-fill-color:var(--color-tfl02-mut)] transition-[translate,scale,-webkit-text-fill-color] duration-[250ms] ease-[cubic-bezier(.3,1.2,.4,1)] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-74 peer-focus:font-bold peer-focus:[-webkit-text-fill-color:transparent] peer-focus:animate-tfl02-flow peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-74 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:[-webkit-text-fill-color:transparent] peer-[:not(:placeholder-shown)]:animate-tfl02-flow motion-reduce:animate-none! motion-reduce:transition-none" for="tfl-02-handle">Pick a handle</label>
    </div>
    <div class="relative after:pointer-events-none after:absolute after:inset-x-0 after:bottom-0 after:h-[2.5px] after:origin-left after:scale-x-0 after:rounded-full after:bg-[image:var(--tfl02-ink)] after:bg-[length:220%_100%] after:transition-[scale] after:duration-400 after:delay-120 after:ease-[cubic-bezier(.25,.8,.3,1)] after:content-[''] focus-within:after:scale-x-100 focus-within:after:animate-tfl02-flow has-[input:not(:placeholder-shown)]:after:scale-x-100 has-[input:not(:placeholder-shown)]:after:animate-tfl02-flow motion-reduce:after:animate-none">
      <input class="peer h-14 w-full rounded-t-xl rounded-b-sm border-[1.5px] border-tfl02-line bg-tfl02-field px-4 pt-[22px] pb-1.5 text-base text-tfl02-ink outline-hidden transition-[border-color] duration-200 focus:border-tfl02-line-focus" type="email" id="tfl-02-mail" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 bg-[image:var(--tfl02-ink)] bg-[length:220%_100%] bg-clip-text text-base [-webkit-text-fill-color:var(--color-tfl02-mut)] transition-[translate,scale,-webkit-text-fill-color] duration-[250ms] ease-[cubic-bezier(.3,1.2,.4,1)] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-74 peer-focus:font-bold peer-focus:[-webkit-text-fill-color:transparent] peer-focus:animate-tfl02-flow peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-74 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:[-webkit-text-fill-color:transparent] peer-[:not(:placeholder-shown)]:animate-tfl02-flow motion-reduce:animate-none! motion-reduce:transition-none" for="tfl-02-mail">Email address</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-[image:var(--tfl02-ink)] bg-[length:220%_100%] text-[15px] font-extrabold text-white [text-shadow:0_1px_2px_oklch(0_0_0/0.35)] transition-[filter,scale] duration-150 hover:animate-tfl02-flow hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl02-b motion-reduce:hover:animate-none" type="button">Join the waitlist</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl02-bg: #141118;
  --color-tfl02-bg: oklch(0.18 0.015 300);
  --color-tfl02-glow: #2a1f3a;
  --color-tfl02-glow: oklch(0.27 0.05 300);
  --color-tfl02-card: #1d1924;
  --color-tfl02-card: oklch(0.22 0.018 300);
  --color-tfl02-edge: #2e2839;
  --color-tfl02-edge: oklch(0.29 0.025 300);
  --color-tfl02-field: #161320;
  --color-tfl02-field: oklch(0.19 0.02 295);
  --color-tfl02-line: #332c42;
  --color-tfl02-line: oklch(0.31 0.035 300);
  --color-tfl02-line-focus: #4a4060;
  --color-tfl02-line-focus: oklch(0.39 0.05 300);
  --color-tfl02-ink: #f2eef7;
  --color-tfl02-ink: oklch(0.95 0.01 300);
  --color-tfl02-mut: #a39bb5;
  --color-tfl02-mut: oklch(0.7 0.03 300);
  --color-tfl02-a: #a06cf0;
  --color-tfl02-a: oklch(0.65 0.18 300);
  --color-tfl02-b: #3ea5e8;
  --color-tfl02-b: oklch(0.7 0.14 235);
  --color-tfl02-c: #f07a82;
  --color-tfl02-c: oklch(0.72 0.14 15);
  --font-tfl02-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tfl02-flow: tfl02-flow 4s linear infinite;

  @keyframes tfl02-flow {
    to {
      background-position: -220% 0;
    }
  }
}

.tfl-02 {
  width: 100%;
  min-height: 100svh;
}
```
