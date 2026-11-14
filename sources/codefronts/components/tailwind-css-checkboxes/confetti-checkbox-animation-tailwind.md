---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/confetti-checkbox-animation-tailwind/"
title: "Confetti Checkbox Animation in Tailwind CSS — Pure CSS Particle Burst"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Eight confetti flakes burst from the box on check — squares and dots, each flying to its own vector via per-particle custom properties ([--tx:-16px]…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Confetti Checkbox Animation in Tailwind CSS — Pure CSS Particle Burst
Source: https://codefronts.com/components/tailwind-css-checkboxes/confetti-checkbox-animation-tailwind/

Eight confetti flakes burst from the box on check — squares and dots, each flying to its own vector via per-particle custom properties ([--tx:-16px] [--ty:-14px] [--rot:120deg]) read by one shared animate-tcb27-pop keyframe. The tick springs in behind the burst. Zero JavaScript.
## HTML
```html
<section class="tcb-27 w-full min-h-svh grid place-items-center bg-tcb27-bg px-5 py-14 font-tcb27-sans text-tcb27-ink selection:bg-tcb27-acc selection:text-white" aria-label="Confetti burst checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb27-line bg-white px-4 py-2.5">
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb27-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb27-acc peer-checked:bg-tcb27-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb27-acc"><span class="pointer-events-none absolute inset-0 motion-reduce:hidden"><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:-16px] [--ty:-14px] [--rot:120deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c2 [--tx:15px] [--ty:-16px] [--rot:-90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c3 [--tx:-18px] [--ty:10px] [--rot:60deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:17px] [--ty:12px] [--rot:-140deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c5 [--tx:0px] [--ty:-21px] [--rot:200deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c6 [--tx:2px] [--ty:19px] [--rot:-40deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:-21px] [--ty:-2px] [--rot:90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:21px] [--ty:-3px] [--rot:-60deg] group-has-checked:animate-tcb27-pop"></i></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Finish onboarding</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb27-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb27-acc peer-checked:bg-tcb27-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb27-acc"><span class="pointer-events-none absolute inset-0 motion-reduce:hidden"><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:-16px] [--ty:-14px] [--rot:120deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c2 [--tx:15px] [--ty:-16px] [--rot:-90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c3 [--tx:-18px] [--ty:10px] [--rot:60deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:17px] [--ty:12px] [--rot:-140deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c5 [--tx:0px] [--ty:-21px] [--rot:200deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c6 [--tx:2px] [--ty:19px] [--rot:-40deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:-21px] [--ty:-2px] [--rot:90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:21px] [--ty:-3px] [--rot:-60deg] group-has-checked:animate-tcb27-pop"></i></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Claim your reward</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb27-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb27-acc peer-checked:bg-tcb27-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb27-acc"><span class="pointer-events-none absolute inset-0 motion-reduce:hidden"><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:-16px] [--ty:-14px] [--rot:120deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c2 [--tx:15px] [--ty:-16px] [--rot:-90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c3 [--tx:-18px] [--ty:10px] [--rot:60deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:17px] [--ty:12px] [--rot:-140deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c5 [--tx:0px] [--ty:-21px] [--rot:200deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c6 [--tx:2px] [--ty:19px] [--rot:-40deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-full bg-tcb27-c4 [--tx:-21px] [--ty:-2px] [--rot:90deg] group-has-checked:animate-tcb27-pop"></i><i class="absolute left-1/2 top-1/2 size-1.5 -translate-1/2 scale-0 opacity-0 rounded-[1px] bg-tcb27-c1 [--tx:21px] [--ty:-3px] [--rot:-60deg] group-has-checked:animate-tcb27-pop"></i></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Hit the goal</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb27-bg: #f6f4fb;
  --color-tcb27-bg: oklch(0.97 0.008 300);
  --color-tcb27-ink: #2f2a3d;
  --color-tcb27-ink: oklch(0.29 0.03 295);
  --color-tcb27-line: #e9e5f3;
  --color-tcb27-line: oklch(0.93 0.012 295);
  --color-tcb27-box: #a29bb8;
  --color-tcb27-box: oklch(0.71 0.04 295);
  --color-tcb27-acc: #8a3fc4;
  --color-tcb27-acc: oklch(0.52 0.19 305);
  --color-tcb27-c1: #ff5d73;
  --color-tcb27-c1: oklch(0.68 0.2 15);
  --color-tcb27-c2: #ffd23f;
  --color-tcb27-c2: oklch(0.88 0.17 90);
  --color-tcb27-c3: #3ddc97;
  --color-tcb27-c3: oklch(0.8 0.16 160);
  --color-tcb27-c4: #4d7fff;
  --color-tcb27-c4: oklch(0.62 0.2 265);
  --color-tcb27-c5: #c04cff;
  --color-tcb27-c5: oklch(0.64 0.26 310);
  --color-tcb27-c6: #ff9a3d;
  --color-tcb27-c6: oklch(0.77 0.16 55);
  --font-tcb27-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-tcb27-pop: tcb27-pop 0.6s ease-out;

  @keyframes tcb27-pop {
    0% {
      translate: -50% -50%;
      scale: 0;
      rotate: 0deg;
      opacity: 0;
    }

    15% {
      scale: 1;
      opacity: 1;
    }

    100% {
      translate: calc(-50% + var(--tx)) calc(-50% + var(--ty));
      scale: 0.4;
      rotate: var(--rot);
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-27 {
  width: 100%;
  min-height: 100svh;
}
```
