---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-hover-reveal-spread/"
title: "Tailwind Stacked Cards Hover Reveal Spread"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "The editorial portfolio deck: four gradient cards in a slight pile that fan into an arc when you approach, then lift individually."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Cards Hover Reveal Spread
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-hover-reveal-spread/

The editorial portfolio deck: four gradient cards in a slight pile that fan into an arc when you approach, then lift individually. The port's real subject is the flicker guard &mdash; the fan must apply on stage hover except when a card itself is hovered, and no built-in variant expresses that, so it becomes one honest arbitrary variant. All four cards then share a single identical class list, with their destinations as custom properties.
## HTML
```html
<section class="stk-28 relative grid w-full min-h-svh place-items-center overflow-hidden bg-stk28-void font-stk28-sans">
  <div class="pointer-events-none absolute -inset-[30%] blur-[20px] animate-stk28-drift motion-reduce:animate-none [background-image:radial-gradient(40%_40%_at_20%_30%,var(--color-stk28-aur1),transparent_70%),radial-gradient(45%_45%_at_80%_25%,var(--color-stk28-aur2),transparent_70%),radial-gradient(50%_50%_at_50%_85%,var(--color-stk28-aur3),transparent_70%)]" aria-hidden="true"></div>
  <div class="pointer-events-none absolute inset-0 mix-blend-overlay [background-image:repeating-linear-gradient(0deg,rgba(255,255,255,0.022)_0_1px,transparent_1px_3px)]" aria-hidden="true"></div>
  <div class="stk-28__stage relative z-1 h-100 w-75 [perspective:1300px]" aria-label="Selected works, four case studies">
    <div class="stk-28__card group absolute inset-0 cursor-pointer overflow-hidden rounded-3xl [transform-style:preserve-3d] [z-index:calc(4-var(--i))] brightness-[calc(1-var(--i)*0.13)] shadow-[0_30px_60px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:translateZ(calc(var(--i)*-40px))_translateY(calc(var(--i)*10px))_rotate(var(--r0))] transition-[transform,box-shadow,filter] duration-800 ease-stk28 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:brightness-100 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:[transform:translate(var(--fx),var(--fy))_translateZ(var(--fz))_rotate(var(--fr))] hover:z-9 hover:brightness-105 hover:shadow-[0_50px_90px_rgba(0,0,0,0.65),inset_0_0_0_1px_rgba(255,255,255,0.18),0_0_40px_rgba(255,255,255,0.12)] hover:[transform:translate(var(--fx),calc(var(--fy)-26px))_translateZ(90px)_rotate(var(--fr))_scale(1.06)] motion-reduce:transition-none" style="--i:0;--r0:-3deg;--fx:-165px;--fy:-30px;--fr:-12deg;--fz:40px">
      <div class="absolute inset-0 backdrop-blur-[8px]" aria-hidden="true">
        <div class="absolute inset-0 opacity-90 bg-[size:200%_200%] animate-stk28-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk28-a1),var(--color-stk28-a2)_40%,var(--color-stk28-a3)]"></div>
        <div class="absolute inset-0 opacity-0 mix-blend-soft-light transition-opacity duration-500 group-hover:opacity-100 [background-image:radial-gradient(280px_circle_at_50%_40%,rgba(255,255,255,0.4),transparent_60%)]"></div>
        <div class="absolute -top-[60%] -left-[30%] h-[220%] w-[60%] [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.5),transparent)] [transform:rotate(18deg)_translateX(-220px)] transition-transform duration-900 ease-stk28 group-hover:[transform:rotate(18deg)_translateX(560px)] motion-reduce:transition-none"></div>
      </div>
      <div class="absolute inset-0 flex flex-col justify-between p-7 [transform:translateZ(50px)]">
        <div class="flex items-center gap-2.5">
          <span class="rounded-full border border-white/25 bg-white/16 px-3 py-1.5 text-[0.62rem] font-medium tracking-[0.22em] uppercase text-white backdrop-blur-[6px]">Index</span>
          <span class="ml-auto font-stk28-serif text-[1.3rem] italic text-white/75">01</span>
        </div>
        <div class="flex flex-col gap-4">
          <p class="m-0 font-stk28-serif text-5xl leading-[0.92] tracking-[-0.01em] text-white [text-shadow:0_2px_20px_rgba(0,0,0,0.3)]">Selected<br><em class="italic">works</em></p>
          <p class="m-0 max-w-[24ch] text-[0.8rem] leading-relaxed text-white/80">Hover to open the deck. Move across to explore each case.</p>
          <span class="inline-flex translate-y-2 items-center gap-1.5 text-[0.78rem] text-white opacity-0 transition-[opacity,transform] duration-500 delay-100 group-hover:translate-y-0 group-hover:opacity-100 motion-reduce:transition-none">Begin <span class="grid size-5.5 place-items-center rounded-full bg-white/20 text-[0.8rem]" aria-hidden="true">&rarr;</span></span>
        </div>
      </div>
    </div>
    <div class="stk-28__card group absolute inset-0 cursor-pointer overflow-hidden rounded-3xl [transform-style:preserve-3d] [z-index:calc(4-var(--i))] brightness-[calc(1-var(--i)*0.13)] shadow-[0_30px_60px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:translateZ(calc(var(--i)*-40px))_translateY(calc(var(--i)*10px))_rotate(var(--r0))] transition-[transform,box-shadow,filter] duration-800 ease-stk28 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:brightness-100 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:[transform:translate(var(--fx),var(--fy))_translateZ(var(--fz))_rotate(var(--fr))] hover:z-9 hover:brightness-105 hover:shadow-[0_50px_90px_rgba(0,0,0,0.65),inset_0_0_0_1px_rgba(255,255,255,0.18),0_0_40px_rgba(255,255,255,0.12)] hover:[transform:translate(var(--fx),calc(var(--fy)-26px))_translateZ(90px)_rotate(var(--fr))_scale(1.06)] motion-reduce:transition-none" style="--i:1;--r0:2deg;--fx:-55px;--fy:18px;--fr:-4deg;--fz:20px">
      <div class="absolute inset-0 backdrop-blur-[8px]" aria-hidden="true">
        <div class="absolute inset-0 opacity-90 bg-[size:200%_200%] animate-stk28-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk28-b1),var(--color-stk28-b2)_45%,var(--color-stk28-b3)]"></div>
        <div class="absolute inset-0 opacity-0 mix-blend-soft-light transition-opacity duration-500 group-hover:opacity-100 [background-image:radial-gradient(280px_circle_at_50%_40%,rgba(255,255,255,0.4),transparent_60%)]"></div>
        <div class="absolute -top-[60%] -left-[30%] h-[220%] w-[60%] [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.5),transparent)] [transform:rotate(18deg)_translateX(-220px)] transition-transform duration-900 ease-stk28 group-hover:[transform:rotate(18deg)_translateX(560px)] motion-reduce:transition-none"></div>
      </div>
      <div class="absolute inset-0 flex flex-col justify-between p-7 [transform:translateZ(50px)]">
        <div class="flex items-center gap-2.5">
          <span class="rounded-full border border-white/25 bg-white/16 px-3 py-1.5 text-[0.62rem] font-medium tracking-[0.22em] uppercase text-white backdrop-blur-[6px]">Color</span>
          <span class="ml-auto font-stk28-serif text-[1.3rem] italic text-white/75">02</span>
        </div>
        <div class="flex flex-col gap-4">
          <p class="m-0 font-stk28-serif text-5xl leading-[0.92] tracking-[-0.01em] text-white [text-shadow:0_2px_20px_rgba(0,0,0,0.3)]">Warm<br><em class="italic">tones</em></p>
          <p class="m-0 max-w-[24ch] text-[0.8rem] leading-relaxed text-white/80">Palette and art direction with a deliberate human warmth.</p>
          <span class="inline-flex translate-y-2 items-center gap-1.5 text-[0.78rem] text-white opacity-0 transition-[opacity,transform] duration-500 delay-100 group-hover:translate-y-0 group-hover:opacity-100 motion-reduce:transition-none">View case <span class="grid size-5.5 place-items-center rounded-full bg-white/20 text-[0.8rem]" aria-hidden="true">&rarr;</span></span>
        </div>
      </div>
    </div>
    <div class="stk-28__card group absolute inset-0 cursor-pointer overflow-hidden rounded-3xl [transform-style:preserve-3d] [z-index:calc(4-var(--i))] brightness-[calc(1-var(--i)*0.13)] shadow-[0_30px_60px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:translateZ(calc(var(--i)*-40px))_translateY(calc(var(--i)*10px))_rotate(var(--r0))] transition-[transform,box-shadow,filter] duration-800 ease-stk28 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:brightness-100 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:[transform:translate(var(--fx),var(--fy))_translateZ(var(--fz))_rotate(var(--fr))] hover:z-9 hover:brightness-105 hover:shadow-[0_50px_90px_rgba(0,0,0,0.65),inset_0_0_0_1px_rgba(255,255,255,0.18),0_0_40px_rgba(255,255,255,0.12)] hover:[transform:translate(var(--fx),calc(var(--fy)-26px))_translateZ(90px)_rotate(var(--fr))_scale(1.06)] motion-reduce:transition-none" style="--i:2;--r0:-2deg;--fx:55px;--fy:18px;--fr:4deg;--fz:20px">
      <div class="absolute inset-0 backdrop-blur-[8px]" aria-hidden="true">
        <div class="absolute inset-0 opacity-90 bg-[size:200%_200%] animate-stk28-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk28-c1),var(--color-stk28-c2)_50%,var(--color-stk28-c3)]"></div>
        <div class="absolute inset-0 opacity-0 mix-blend-soft-light transition-opacity duration-500 group-hover:opacity-100 [background-image:radial-gradient(280px_circle_at_50%_40%,rgba(255,255,255,0.4),transparent_60%)]"></div>
        <div class="absolute -top-[60%] -left-[30%] h-[220%] w-[60%] [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.5),transparent)] [transform:rotate(18deg)_translateX(-220px)] transition-transform duration-900 ease-stk28 group-hover:[transform:rotate(18deg)_translateX(560px)] motion-reduce:transition-none"></div>
      </div>
      <div class="absolute inset-0 flex flex-col justify-between p-7 [transform:translateZ(50px)]">
        <div class="flex items-center gap-2.5">
          <span class="rounded-full border border-white/25 bg-white/16 px-3 py-1.5 text-[0.62rem] font-medium tracking-[0.22em] uppercase text-white backdrop-blur-[6px]">Motion</span>
          <span class="ml-auto font-stk28-serif text-[1.3rem] italic text-white/75">03</span>
        </div>
        <div class="flex flex-col gap-4">
          <p class="m-0 font-stk28-serif text-5xl leading-[0.92] tracking-[-0.01em] text-white [text-shadow:0_2px_20px_rgba(0,0,0,0.3)]">In<br><em class="italic">motion</em></p>
          <p class="m-0 max-w-[24ch] text-[0.8rem] leading-relaxed text-white/80">A kinetic brand identity that moves with real intent.</p>
          <span class="inline-flex translate-y-2 items-center gap-1.5 text-[0.78rem] text-white opacity-0 transition-[opacity,transform] duration-500 delay-100 group-hover:translate-y-0 group-hover:opacity-100 motion-reduce:transition-none">View case <span class="grid size-5.5 place-items-center rounded-full bg-white/20 text-[0.8rem]" aria-hidden="true">&rarr;</span></span>
        </div>
      </div>
    </div>
    <div class="stk-28__card group absolute inset-0 cursor-pointer overflow-hidden rounded-3xl [transform-style:preserve-3d] [z-index:calc(4-var(--i))] brightness-[calc(1-var(--i)*0.13)] shadow-[0_30px_60px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:translateZ(calc(var(--i)*-40px))_translateY(calc(var(--i)*10px))_rotate(var(--r0))] transition-[transform,box-shadow,filter] duration-800 ease-stk28 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:brightness-100 [.stk-28__stage:hover:not(:has(.stk-28__card:hover))_&]:[transform:translate(var(--fx),var(--fy))_translateZ(var(--fz))_rotate(var(--fr))] hover:z-9 hover:brightness-105 hover:shadow-[0_50px_90px_rgba(0,0,0,0.65),inset_0_0_0_1px_rgba(255,255,255,0.18),0_0_40px_rgba(255,255,255,0.12)] hover:[transform:translate(var(--fx),calc(var(--fy)-26px))_translateZ(90px)_rotate(var(--fr))_scale(1.06)] motion-reduce:transition-none" style="--i:3;--r0:3deg;--fx:165px;--fy:-30px;--fr:12deg;--fz:40px">
      <div class="absolute inset-0 backdrop-blur-[8px]" aria-hidden="true">
        <div class="absolute inset-0 opacity-90 bg-[size:200%_200%] animate-stk28-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk28-d1),var(--color-stk28-d2)_45%,var(--color-stk28-d3)]"></div>
        <div class="absolute inset-0 opacity-0 mix-blend-soft-light transition-opacity duration-500 group-hover:opacity-100 [background-image:radial-gradient(280px_circle_at_50%_40%,rgba(255,255,255,0.4),transparent_60%)]"></div>
        <div class="absolute -top-[60%] -left-[30%] h-[220%] w-[60%] [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.5),transparent)] [transform:rotate(18deg)_translateX(-220px)] transition-transform duration-900 ease-stk28 group-hover:[transform:rotate(18deg)_translateX(560px)] motion-reduce:transition-none"></div>
      </div>
      <div class="absolute inset-0 flex flex-col justify-between p-7 [transform:translateZ(50px)]">
        <div class="flex items-center gap-2.5">
          <span class="rounded-full border border-white/25 bg-white/16 px-3 py-1.5 text-[0.62rem] font-medium tracking-[0.22em] uppercase text-white backdrop-blur-[6px]">Type</span>
          <span class="ml-auto font-stk28-serif text-[1.3rem] italic text-white/75">04</span>
        </div>
        <div class="flex flex-col gap-4">
          <p class="m-0 font-stk28-serif text-5xl leading-[0.92] tracking-[-0.01em] text-white [text-shadow:0_2px_20px_rgba(0,0,0,0.3)]">Letter<br><em class="italic">forms</em></p>
          <p class="m-0 max-w-[24ch] text-[0.8rem] leading-relaxed text-white/80">An editorial typography system built for screens first.</p>
          <span class="inline-flex translate-y-2 items-center gap-1.5 text-[0.78rem] text-white opacity-0 transition-[opacity,transform] duration-500 delay-100 group-hover:translate-y-0 group-hover:opacity-100 motion-reduce:transition-none">View case <span class="grid size-5.5 place-items-center rounded-full bg-white/20 text-[0.8rem]" aria-hidden="true">&rarr;</span></span>
        </div>
      </div>
    </div>
    <div class="absolute -bottom-[70px] left-1/2 h-10 w-60 -translate-x-1/2 blur-[8px] [background-image:radial-gradient(ellipse,rgba(0,0,0,0.6),transparent_70%)]" aria-hidden="true"></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk28-void: #05060a;
  --color-stk28-void: oklch(0.08 0.012 275);
  --color-stk28-aur1: rgba(99, 102, 241, 0.35);
  --color-stk28-aur2: rgba(236, 72, 153, 0.30);
  --color-stk28-aur3: rgba(45, 212, 191, 0.28);
  --color-stk28-a1: #1e1b4b;
  --color-stk28-a2: #4338ca;
  --color-stk28-a3: #6d28d9;
  --color-stk28-b1: #831843;
  --color-stk28-b2: #be185d;
  --color-stk28-b3: #f43f5e;
  --color-stk28-c1: #064e3b;
  --color-stk28-c2: #0d9488;
  --color-stk28-c3: #2dd4bf;
  --color-stk28-d1: #7c2d12;
  --color-stk28-d2: #ea580c;
  --color-stk28-d3: #f59e0b;
  --font-stk28-sans: 'Geist', system-ui, sans-serif;
  --font-stk28-serif: 'Instrument Serif', Georgia, serif;
  --ease-stk28: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-stk28-flow: stk-28-flow 8s ease infinite;
  --animate-stk28-drift: stk-28-drift 18s ease-in-out infinite alternate;
}

@keyframes stk-28-flow {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

@keyframes stk-28-drift {
  from {
    transform: translate(-3%, -2%) scale(1);
  }

  to {
    transform: translate(4%, 3%) scale(1.12);
  }
}
```
