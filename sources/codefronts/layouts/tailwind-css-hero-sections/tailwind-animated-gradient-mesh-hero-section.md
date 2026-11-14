---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-gradient-mesh-hero-section/"
title: "Tailwind CSS Animated Gradient Mesh Hero Section"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A sunset mesh gradient — four blurred radial blobs in mango, papaya and dragon fruit drifting on a deep coral base, with a fine grain overlay, glass eyebrow…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Animated Gradient Mesh Hero Section
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-gradient-mesh-hero-section/

A sunset mesh gradient — four blurred radial blobs in mango, papaya and dragon fruit drifting on a deep coral base, with a fine grain overlay, glass eyebrow pill and a white pill CTA. Animation lives in @theme; everything else is utilities.
## HTML
```html
<section class="ths-03 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths03-bg px-5 py-16 font-ths03-sans text-white sm:px-14" aria-label="Animated gradient mesh hero">
  <div aria-hidden="true" class="absolute inset-0 -z-10">
    <span class="absolute -top-[10%] left-[10%] size-[min(460px,80vw)] animate-ths03-drift rounded-full bg-[radial-gradient(circle,var(--color-ths03-mango),transparent_70%)] blur-[64px] motion-reduce:animate-none"></span>
    <span class="absolute top-[20%] right-0 size-[min(420px,75vw)] animate-ths03-drift rounded-full bg-[radial-gradient(circle,var(--color-ths03-dragon),transparent_70%)] blur-[64px] [animation-delay:-4s] motion-reduce:animate-none"></span>
    <span class="absolute bottom-0 left-[30%] size-[min(460px,80vw)] animate-ths03-drift rounded-full bg-[radial-gradient(circle,var(--color-ths03-papaya),transparent_70%)] blur-[64px] [animation-delay:-8s] motion-reduce:animate-none"></span>
    <span class="absolute top-[30%] -left-[8%] size-[min(360px,65vw)] animate-ths03-drift rounded-full bg-[radial-gradient(circle,var(--color-ths03-peach),transparent_70%)] blur-[64px] [animation-delay:-12s] motion-reduce:animate-none"></span>
    <span class="absolute inset-0 bg-[radial-gradient(50%_45%_at_50%_50%,var(--color-ths03-scrim),transparent_75%)]"></span>
    <span class="absolute inset-0 bg-[url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22160%22 height=%22160%22><filter id=%22n%22><feTurbulence type=%22fractalNoise%22 baseFrequency=%22.8%22 numOctaves=%223%22/></filter><rect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22 opacity=%22.35%22/></svg>')] opacity-30 mix-blend-overlay"></span>
  </div>
  <div class="max-w-[42rem] text-center">
    <span class="inline-flex items-center gap-2 rounded-full border border-white/40 bg-white/15 px-4 py-1.5 text-[11px] font-semibold tracking-[0.14em] uppercase backdrop-blur-md">
      <span aria-hidden="true" class="size-1.5 rounded-full bg-ths03-mango shadow-[0_0_10px_var(--color-ths03-mango)]"></span>Launch · Summer collection
    </span>
    <h1 class="mt-6 font-ths03-display text-[clamp(40px,7vw,80px)] leading-[0.98] font-extrabold tracking-[-0.03em] text-balance [text-shadow:0_2px_30px_rgb(120_20_40/0.3)]">Make your weekends <em class="font-bold text-ths03-cream">feel like vacation.</em></h1>
    <p class="mx-auto mt-6 max-w-[30rem] text-lg/relaxed text-pretty text-white">The mood-board planner that turns scattered Pinterest tabs into the trip you actually take.</p>
    <div class="mt-9 flex flex-wrap justify-center gap-3">
      <a href="#start" class="inline-flex min-h-12 items-center gap-2 rounded-full bg-white px-7 text-[15px] font-bold text-ths03-dragon shadow-[0_14px_34px_-8px_rgb(150_20_50/0.5)] transition hover:-translate-y-0.5 hover:shadow-[0_20px_40px_-8px_rgb(150_20_50/0.55)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none">Plan a trip →</a>
      <a href="#ideas" class="inline-flex min-h-12 items-center rounded-full border border-white/50 px-6 text-[15px] font-semibold text-white backdrop-blur-sm transition hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white">Browse ideas</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths03-bg: #e0404f;
  --color-ths03-bg: oklch(0.61 0.196 20.2);
  --color-ths03-scrim: #8a1c2e66;
  --color-ths03-scrim: oklch(0.419 0.144 17.6 / 0.4);
  --color-ths03-mango: #ffd23f;
  --color-ths03-mango: oklch(0.879 0.162 90.9);
  --color-ths03-dragon: #e23a62;
  --color-ths03-dragon: oklch(0.612 0.204 12.2);
  --color-ths03-papaya: #ff7e5f;
  --color-ths03-papaya: oklch(0.736 0.164 34.7);
  --color-ths03-peach: #ffa552;
  --color-ths03-peach: oklch(0.797 0.144 60.8);
  --color-ths03-cream: #fff5d2;
  --color-ths03-cream: oklch(0.969 0.047 93.9);
  --font-ths03-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ths03-sans: 'Geist', system-ui, sans-serif;
  --animate-ths03-drift: ths03-drift 16s ease-in-out infinite alternate;

  @keyframes ths03-drift {
    0% {
      transform: translate(0, 0) scale(1);
    }

    50% {
      transform: translate(40px, -30px) scale(1.08);
    }

    100% {
      transform: translate(-40px, 40px) scale(0.96);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-03 {
  width: 100%;
  min-height: 100svh;
}
```
