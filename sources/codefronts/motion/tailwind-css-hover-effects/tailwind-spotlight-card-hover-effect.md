---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-spotlight-card-hover-effect/"
title: "Tailwind Spotlight Card Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four lighting treatments — centre spotlight, corner lamp, a travelling scan band and a vignette that lifts."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spotlight Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-spotlight-card-hover-effect/

Four lighting treatments — centre spotlight, corner lamp, a travelling scan band and a vignette that lifts. Each is one gradient on a before: layer whose opacity (or position) changes on hover.
## HTML
```html
<section class="thv-16 w-full min-h-svh grid place-items-center bg-thv16-bg font-thv16-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-8">
    <button type="button" class="relative overflow-hidden min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-white/10 cursor-pointer transition-[border-color,transform] duration-400 hover:border-thv16-teal/30 hover:-translate-y-1 focus-visible:border-thv16-teal/30 focus-visible:-translate-y-1 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv16-teal before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:opacity-0 before:transition-opacity before:duration-400 before:[background:radial-gradient(circle_at_50%_50%,rgba(20,184,166,.18)_0%,transparent_65%)] hover:before:opacity-100 focus-visible:before:opacity-100 motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <span class="relative z-10 flex flex-col gap-3 p-8">
        <span class="text-2xl text-thv16-teal">◎</span>
        <span class="text-base font-bold text-thv16-text">Center Spot</span>
        <span class="text-sm leading-relaxed text-thv16-dim">Radial gradient fades in from the centre on hover.</span>
      </span>
    </button>
    <button type="button" class="relative overflow-hidden min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-white/10 cursor-pointer transition-[border-color,transform] duration-400 hover:border-thv16-cyan/30 hover:-translate-y-1 focus-visible:border-thv16-cyan/30 focus-visible:-translate-y-1 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv16-cyan before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:opacity-0 before:transition-opacity before:duration-400 before:[background:conic-gradient(from_225deg_at_0%_0%,rgba(6,182,212,.25),transparent_40%)] hover:before:opacity-100 focus-visible:before:opacity-100 motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <span class="relative z-10 flex flex-col gap-3 p-8">
        <span class="text-2xl text-thv16-cyan">◤</span>
        <span class="text-base font-bold text-thv16-text">Corner Light</span>
        <span class="text-sm leading-relaxed text-thv16-dim">Conic sweep from a lamp at the top-left corner.</span>
      </span>
    </button>
    <button type="button" class="relative overflow-hidden min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-white/10 cursor-pointer transition-[border-color,transform] duration-400 hover:border-thv16-teal/30 hover:-translate-y-1 focus-visible:border-thv16-teal/30 focus-visible:-translate-y-1 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv16-teal before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:opacity-0 before:-translate-y-full before:transition-[opacity,transform] before:duration-500 before:ease-[cubic-bezier(.4,0,.2,1)] before:[background:linear-gradient(180deg,transparent_0%,rgba(20,184,166,.15)_40%,rgba(20,184,166,.15)_60%,transparent_100%)] hover:before:opacity-100 hover:before:translate-y-[60%] focus-visible:before:opacity-100 focus-visible:before:translate-y-[60%] motion-reduce:before:transition-opacity motion-reduce:hover:before:translate-y-0">
      <span class="relative z-10 flex flex-col gap-3 p-8">
        <span class="text-2xl text-thv16-teal">▤</span>
        <span class="text-base font-bold text-thv16-text">Edge Scan</span>
        <span class="text-sm leading-relaxed text-thv16-dim">A bright band sweeps top to bottom on hover.</span>
      </span>
    </button>
    <button type="button" class="relative overflow-hidden min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-white/10 cursor-pointer transition-[border-color,transform] duration-400 hover:border-thv16-green/30 hover:-translate-y-1 focus-visible:border-thv16-green/30 focus-visible:-translate-y-1 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv16-green before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:opacity-100 before:transition-opacity before:duration-400 before:[background:radial-gradient(ellipse_at_center,transparent_40%,rgba(0,0,0,.7)_100%)] hover:before:opacity-0 focus-visible:before:opacity-0 motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <span class="relative z-10 flex flex-col gap-3 p-8">
        <span class="text-2xl text-thv16-green">◉</span>
        <span class="text-base font-bold text-thv16-text">Vignette Lift</span>
        <span class="text-sm leading-relaxed text-thv16-dim">The dark vignette fades out, revealing the full card face.</span>
      </span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv16-bg: #020c0b;
  --color-thv16-bg: oklch(0.13 0.02 180);
  --color-thv16-text: #ccfbf1;
  --color-thv16-text: oklch(0.94 0.05 175);
  --color-thv16-dim: #94a3a0;
  --color-thv16-dim: oklch(0.71 0.01 175);
  --color-thv16-teal: #14b8a6;
  --color-thv16-teal: oklch(0.72 0.13 180);
  --color-thv16-green: #10b981;
  --color-thv16-green: oklch(0.7 0.15 163);
  --color-thv16-cyan: #06b6d4;
  --color-thv16-cyan: oklch(0.71 0.14 208);
  --font-thv16-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-16 {
  width: 100%;
  min-height: 100svh;
}

.thv-16 ::selection {
  background: var(--color-thv16-teal);
  color: #fff;
}
```
