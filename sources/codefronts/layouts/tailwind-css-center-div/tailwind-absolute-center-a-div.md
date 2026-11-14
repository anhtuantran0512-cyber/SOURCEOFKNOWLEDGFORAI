---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-center-div/tailwind-absolute-center-a-div/"
title: "Tailwind Absolute Center a Div with translate and inset-0"
section: "layouts"
category: "tailwind-css-center-div"
category_name: "Tailwind CSS Ways to Center Div"
description: "Three ways to center an absolutely positioned element over a glass UI: the classic top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2, the cleaner inset-0…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Absolute Center a Div with translate and inset-0
Source: https://codefronts.com/layouts/tailwind-css-center-div/tailwind-absolute-center-a-div/

Three ways to center an absolutely positioned element over a glass UI: the classic top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2, the cleaner inset-0 m-auto size-fit, and a real known-size calc() offset. Edge ticks on every card line up with the stage crosshair, so you can see each method land dead centre.
## HTML
```html
<section class="tcd-03 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tcd03-bg px-5 py-14 font-tcd03-sans text-tcd03-ink selection:bg-tcd03-acc selection:text-white" aria-label="Tailwind absolute center a div demo">
  <span aria-hidden="true" class="pointer-events-none absolute -left-32 -top-40 -z-10 size-[32rem] rounded-full bg-tcd03-acc opacity-35 blur-[90px] animate-tcd03-drift motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="pointer-events-none absolute -bottom-40 -right-24 -z-10 size-[28rem] rounded-full bg-tcd03-blue opacity-35 blur-[90px] animate-tcd03-drift [animation-delay:-9s] motion-reduce:animate-none"></span>

  <div class="w-full max-w-6xl">
    <header class="mb-10 text-center">
      <p class="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-3 py-1 font-tcd03-mono text-[11px] uppercase tracking-[0.14em] text-tcd03-acc2 backdrop-blur"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd03-acc2"></span>Pure Tailwind</p>
      <h1 class="mt-5 text-[clamp(28px,5vw,46px)] font-extrabold leading-[1.05] tracking-[-0.035em] text-balance">Absolute center a div <span class="bg-linear-to-r from-tcd03-acc2 to-tcd03-blue bg-clip-text text-transparent">in Tailwind</span></h1>
      <p class="mx-auto mt-3 max-w-lg text-[15px] leading-relaxed text-tcd03-mut text-pretty">Three positioning methods. The pink ticks on each card meet the crosshair — that's the proof.</p>
    </header>

    <div class="grid gap-5 lg:grid-cols-3">
      <article class="overflow-hidden rounded-3xl border border-white/10 bg-tcd03-card/55 backdrop-blur-xl transition duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="border-b border-white/10 px-5 py-4">
          <h2 class="flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd03-mut"><span class="font-tcd03-mono text-tcd03-acc2">01</span>Translate trick</h2>
          <code class="mt-2 block font-tcd03-mono text-xs leading-relaxed text-tcd03-acc2">absolute top-1/2 left-1/2<br>-translate-x-1/2 -translate-y-1/2</code>
        </div>
        <div class="relative h-72 overflow-hidden before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd03-acc/25 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd03-acc/25">
          <span aria-hidden="true" class="absolute left-4 top-4 size-3.5 border-l border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute right-4 top-4 size-3.5 border-r border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 left-4 size-3.5 border-b border-l border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 right-4 size-3.5 border-b border-r border-tcd03-acc/50"></span>
          <div class="absolute left-1/2 top-1/2 z-10 w-max max-w-[calc(100%-2rem)] -translate-x-1/2 -translate-y-1/2 rounded-2xl border border-white/15 bg-white/6 px-8 py-6 text-center shadow-[0_10px_40px_-10px_oklch(0.66_0.22_354/0.5),inset_0_1px_0_oklch(1_0_0/0.12)] backdrop-blur-2xl before:absolute before:-top-2 before:left-1/2 before:h-4 before:w-px before:bg-tcd03-acc2 after:absolute after:-left-2 after:top-1/2 after:h-px after:w-4 after:bg-tcd03-acc2">
            <h3 class="text-base font-bold">Translate trick</h3>
            <p class="mt-1 text-[13px] text-tcd03-mut">Any unknown size</p>
          </div>
        </div>
      </article>

      <article class="overflow-hidden rounded-3xl border border-white/10 bg-tcd03-card/55 backdrop-blur-xl transition delay-100 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="border-b border-white/10 px-5 py-4">
          <h2 class="flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd03-mut"><span class="font-tcd03-mono text-tcd03-acc2">02</span>Inset + margin auto</h2>
          <code class="mt-2 block font-tcd03-mono text-xs leading-relaxed text-tcd03-acc2">absolute inset-0<br>m-auto size-fit</code>
        </div>
        <div class="relative h-72 overflow-hidden before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd03-acc/25 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd03-acc/25">
          <span aria-hidden="true" class="absolute left-4 top-4 size-3.5 border-l border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute right-4 top-4 size-3.5 border-r border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 left-4 size-3.5 border-b border-l border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 right-4 size-3.5 border-b border-r border-tcd03-acc/50"></span>
          <div class="absolute inset-0 z-10 m-auto size-fit max-w-[calc(100%-2rem)] rounded-2xl border border-white/15 bg-white/6 px-8 py-6 text-center shadow-[0_10px_40px_-10px_oklch(0.66_0.22_354/0.5),inset_0_1px_0_oklch(1_0_0/0.12)] backdrop-blur-2xl before:absolute before:-top-2 before:left-1/2 before:h-4 before:w-px before:bg-tcd03-acc2 after:absolute after:-left-2 after:top-1/2 after:h-px after:w-4 after:bg-tcd03-acc2">
            <h3 class="text-base font-bold">Inset + m-auto</h3>
            <p class="mt-1 text-[13px] text-tcd03-mut">No transform at all</p>
          </div>
        </div>
      </article>

      <article class="overflow-hidden rounded-3xl border border-white/10 bg-tcd03-card/55 backdrop-blur-xl transition delay-200 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="border-b border-white/10 px-5 py-4">
          <h2 class="flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd03-mut"><span class="font-tcd03-mono text-tcd03-acc2">03</span>Known-size calc</h2>
          <code class="mt-2 block font-tcd03-mono text-xs leading-relaxed text-tcd03-acc2">absolute h-28 w-64<br>top-[calc(50%-3.5rem)] left-[calc(50%-8rem)]</code>
        </div>
        <div class="relative h-72 overflow-hidden before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd03-acc/25 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd03-acc/25">
          <span aria-hidden="true" class="absolute left-4 top-4 size-3.5 border-l border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute right-4 top-4 size-3.5 border-r border-t border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 left-4 size-3.5 border-b border-l border-tcd03-acc/50"></span><span aria-hidden="true" class="absolute bottom-4 right-4 size-3.5 border-b border-r border-tcd03-acc/50"></span>
          <div class="absolute left-[calc(50%-8rem)] top-[calc(50%-3.5rem)] z-10 grid h-28 w-64 content-center rounded-2xl border border-white/15 bg-white/6 text-center shadow-[0_10px_40px_-10px_oklch(0.66_0.22_354/0.5),inset_0_1px_0_oklch(1_0_0/0.12)] backdrop-blur-2xl before:absolute before:-top-2 before:left-1/2 before:h-4 before:w-px before:bg-tcd03-acc2 after:absolute after:-left-2 after:top-1/2 after:h-px after:w-4 after:bg-tcd03-acc2">
            <h3 class="text-base font-bold">Calc offset</h3>
            <p class="mt-1 text-[13px] text-tcd03-mut">16rem × 7rem, maths by hand</p>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd03-bg: #0e0818;
  --color-tcd03-bg: oklch(0.14 0.04 300);
  --color-tcd03-card: #170f26;
  --color-tcd03-card: oklch(0.18 0.045 300);
  --color-tcd03-ink: #fdf2f8;
  --color-tcd03-ink: oklch(0.97 0.015 345);
  --color-tcd03-mut: #dcc3d2;
  --color-tcd03-mut: oklch(0.83 0.04 340);
  --color-tcd03-acc: #ec4899;
  --color-tcd03-acc: oklch(0.66 0.22 354);
  --color-tcd03-acc2: #f9a8d4;
  --color-tcd03-acc2: oklch(0.83 0.11 349);
  --color-tcd03-blue: #818cf8;
  --color-tcd03-blue: oklch(0.67 0.16 277);
  --font-tcd03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcd03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tcd03-drift: tcd03-drift 18s ease-in-out infinite alternate;

  @keyframes tcd03-drift {
    to {
      transform: translate(70px, 50px) scale(1.12);
    }
  }
}

.tcd-03 {
  width: 100%;
  min-height: 100svh;
}
```
