---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-card-flip-hover-effect/"
title: "Tailwind Card Flip Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four flips — horizontal, vertical, a diagonal rotate3d peel and a fanning stack."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Card Flip Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-card-flip-hover-effect/

Four flips — horizontal, vertical, a diagonal rotate3d peel and a fanning stack. backface-hidden and transform-3d are core utilities, so the three-element scene/card/face structure ports without a single custom rule.
## HTML
```html
<section class="thv-14 w-full min-h-svh grid place-items-center bg-thv14-bg font-thv14-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-10">
    <button type="button" class="group perspective-[800px] block w-full h-[220px] bg-transparent border-0 p-0 cursor-pointer rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv14-rose">
      <span class="relative block w-full h-full transform-3d transition-transform duration-650 ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-y-180 group-focus-visible:rotate-y-180 motion-reduce:transition-none">
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden bg-thv14-rose/20 border border-thv14-rose/40 text-thv14-text">
          <span class="text-3xl">♦</span><span class="text-base font-bold">Hover Me</span><span class="text-xs tracking-[0.05em] text-thv14-dim">horizontal flip →</span>
        </span>
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden rotate-y-180 bg-thv14-rose text-white">
          <span class="text-3xl">✦</span><span class="text-base font-bold">Revealed!</span><span class="text-xs tracking-[0.05em] text-white/80">back face content</span>
        </span>
      </span>
    </button>
    <button type="button" class="group perspective-[800px] block w-full h-[220px] bg-transparent border-0 p-0 cursor-pointer rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv14-teal">
      <span class="relative block w-full h-full transform-3d transition-transform duration-650 ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-x-180 group-focus-visible:rotate-x-180 motion-reduce:transition-none">
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden bg-thv14-teal/20 border border-thv14-teal/40 text-thv14-text">
          <span class="text-3xl">◈</span><span class="text-base font-bold">Vertical</span><span class="text-xs tracking-[0.05em] text-thv14-dim">↓ flip over top</span>
        </span>
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden rotate-x-180 bg-thv14-indigo text-white">
          <span class="text-3xl">❋</span><span class="text-base font-bold">Back Face</span><span class="text-xs tracking-[0.05em] text-white/80">rotateX flip</span>
        </span>
      </span>
    </button>
    <button type="button" class="group perspective-[800px] block w-full h-[220px] bg-transparent border-0 p-0 cursor-pointer rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv14-amber">
      <span class="relative block w-full h-full transform-3d transition-transform duration-650 ease-[cubic-bezier(.4,0,.2,1)] group-hover:[transform:rotate3d(1,1,0,180deg)] group-focus-visible:[transform:rotate3d(1,1,0,180deg)] motion-reduce:transition-none">
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden bg-thv14-amber/20 border border-thv14-amber/40 text-thv14-text">
          <span class="text-3xl">◬</span><span class="text-base font-bold">Diagonal</span><span class="text-xs tracking-[0.05em] text-thv14-dim">corner-peel axis</span>
        </span>
        <span class="absolute inset-0 flex flex-col items-center justify-center gap-2.5 p-6 rounded-2xl backface-hidden [transform:rotate3d(1,1,0,180deg)] bg-thv14-orange text-white">
          <span class="text-3xl">⟡</span><span class="text-base font-bold">Peeled!</span><span class="text-xs tracking-[0.05em] text-white/80">rotate3d(1,1,0)</span>
        </span>
      </span>
    </button>
    <button type="button" class="group perspective-[900px] relative block w-full h-[220px] bg-transparent border-0 p-0 cursor-pointer rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv14-violet">
      <span class="absolute inset-0 z-30 flex items-center justify-center rounded-2xl border border-white/10 bg-thv14-violet/25 origin-bottom transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)]"><span class="text-lg font-bold text-thv14-lilac">Fan</span></span>
      <span class="absolute inset-0 z-20 rounded-2xl border border-white/10 bg-thv14-violet/20 origin-bottom transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-y-[-30deg] group-focus-visible:rotate-y-[-30deg] motion-reduce:transition-none"></span>
      <span class="absolute inset-0 z-10 rounded-2xl border border-white/10 bg-thv14-violet/15 origin-bottom transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-y-[-55deg] group-focus-visible:rotate-y-[-55deg] motion-reduce:transition-none"></span>
      <span class="absolute -bottom-7 inset-x-0 text-[11px] tracking-[0.12em] uppercase text-thv14-dim">hover the stack</span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv14-bg: #0a0008;
  --color-thv14-bg: oklch(0.11 0.02 350);
  --color-thv14-text: #ffe4e6;
  --color-thv14-text: oklch(0.94 0.03 10);
  --color-thv14-dim: #7d7480;
  --color-thv14-dim: oklch(0.6 0.02 350);
  --color-thv14-rose: #be123c;
  --color-thv14-rose: oklch(0.52 0.2 15);
  --color-thv14-teal: #0d9488;
  --color-thv14-teal: oklch(0.6 0.12 180);
  --color-thv14-indigo: #4338ca;
  --color-thv14-indigo: oklch(0.45 0.22 274);
  --color-thv14-amber: #b45309;
  --color-thv14-amber: oklch(0.55 0.14 55);
  --color-thv14-orange: #c2410c;
  --color-thv14-orange: oklch(0.55 0.18 40);
  --color-thv14-violet: #8b5cf6;
  --color-thv14-violet: oklch(0.63 0.21 295);
  --color-thv14-lilac: #c4b5fd;
  --color-thv14-lilac: oklch(0.83 0.09 295);
  --font-thv14-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-14 {
  width: 100%;
  min-height: 100svh;
}

.thv-14 ::selection {
  background: var(--color-thv14-rose);
  color: #fff;
}
```
