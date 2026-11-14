---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-vaporwave-aesthetic-scene/"
title: "Tailwind Vaporwave Aesthetic Scene"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A perspective grid running to a banded sunset, with chrome lettering and a palm silhouette &mdash; the outrun scene built from a rotated grid plane,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vaporwave Aesthetic Scene
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-vaporwave-aesthetic-scene/

A perspective grid running to a banded sunset, with chrome lettering and a palm silhouette &mdash; the outrun scene built from a rotated grid plane, repeating gradients and a clipped text fill, no images. It also names what it is: this aesthetic comes from 1980s marketing and album art, not from 1980s computers, which makes it the odd one out here on purpose.
## HTML
```html
<section class="twr-14 relative block w-full min-h-svh box-border overflow-hidden bg-twr14-deep text-white font-twr14-geo" aria-labelledby="twr-14-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-14-title">Vaporwave grid horizon scene</h2>

  <div class="absolute top-4 right-4 z-9">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-14-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer bg-[rgba(10,3,32,0.65)] text-twr14-cyan border border-[rgba(53,232,255,0.55)] peer-focus-visible:outline-2 peer-focus-visible:outline-twr14-cyan peer-focus-visible:outline-offset-[3px]" for="twr-14-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle night scene</span>
    </label>
  </div>

  <div class="relative isolate grid grid-cols-[minmax(0,1fr)] content-center min-h-svh min-w-0 px-[clamp(1rem,0.6rem+3vw,3rem)] py-[clamp(4rem,3rem+4vw,6rem)]">
    <div class="absolute inset-x-0 top-0 h-[62%] z-0 [background:linear-gradient(180deg,var(--twr-14-sky-a)_0%,var(--twr-14-sky-b)_62%,var(--twr-14-sky-c)_100%)]" aria-hidden="true">
      <span class="absolute left-1/2 bottom-0 -translate-x-1/2 w-[clamp(180px,34vw,340px)] aspect-square rounded-full [background:repeating-linear-gradient(180deg,var(--color-twr14-amber)_0_10px,rgba(0,0,0,0)_10px_14px)] [mask-image:radial-gradient(circle_at_50%_50%,#000_98%,transparent_100%)]"></span>
      <span class="absolute inset-0 [background-image:radial-gradient(1px_1px_at_20%_18%,rgba(255,255,255,0.7),transparent),radial-gradient(1px_1px_at_62%_28%,rgba(255,255,255,0.55),transparent),radial-gradient(1px_1px_at_82%_12%,rgba(255,255,255,0.6),transparent)]"></span>
    </div>

    <div class="absolute inset-x-0 bottom-0 h-[42%] z-1 overflow-hidden perspective-[280px]" aria-hidden="true">
      <span class="twr-14__plane block absolute inset-x-[-40%] bottom-0 h-[160%] origin-top rotate-x-[70deg] animate-twr14-travel motion-reduce:animate-none [background-color:var(--color-twr14-deep)] [background-image:repeating-linear-gradient(90deg,rgba(53,232,255,0.55)_0_1px,rgba(0,0,0,0)_1px_44px),repeating-linear-gradient(180deg,rgba(255,47,180,0.5)_0_1px,rgba(0,0,0,0)_1px_44px)]"></span>
    </div>

    <span class="absolute bottom-[36%] left-[6%] z-2 w-[clamp(60px,10vw,120px)] h-[clamp(120px,22vw,240px)] bg-twr14-deep [clip-path:polygon(46%_100%,42%_46%,20%_34%,4%_18%,26%_26%,42%_34%,30%_10%,50%_0,70%_10%,58%_32%,76%_24%,96%_16%,80%_34%,58%_46%,54%_100%)]" aria-hidden="true"></span>

    <div class="relative z-3 grid justify-items-center gap-5 min-w-0 text-center">
      <p class="m-0 font-twr14-mono text-[0.68rem] tracking-[0.22em] uppercase text-twr14-cyan">Airbrush, chrome and grid &middot; 1984 record sleeve</p>
      <p class="m-0 min-w-0 font-extrabold uppercase leading-none tracking-[0.03em] text-[clamp(2.5rem,1rem+9vw,6rem)] text-twr14-amber bg-clip-text supports-[background-clip:text]:text-transparent [background-image:linear-gradient(180deg,#dff6ff_0_49.5%,#ffffff_49.5%_50.5%,#ff9ad6_50.5%_100%)] [text-shadow:0_2px_0_rgba(109,43,217,0.55)]">NIGHT DRIVE</p>

      <div class="min-w-0 max-w-[46rem] grid gap-3.5 rounded-lg border border-[rgba(53,232,255,0.35)] bg-[rgba(8,2,26,0.82)] p-[clamp(1rem,0.7rem+1.6vw,1.75rem)] text-start">
        <h3 class="m-0 text-[1.05rem] font-semibold tracking-[0.02em] text-twr14-cyan">Not an interface</h3>
        <p class="m-0 min-w-0 text-[0.92rem] leading-relaxed text-pretty text-white/85">This is how the decade advertised computing, not how it looked to use one. Everything else in this collection reproduces a system someone sat in front of. Treat this as a title card or a splash, and put the working interface somewhere else.</p>
        <div class="flex flex-wrap gap-3">
          <button class="min-h-11 px-5 py-2.5 border-0 cursor-pointer font-inherit text-[0.85rem] font-semibold tracking-[0.14em] uppercase transition-transform duration-150 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-twr14-cyan focus-visible:outline-offset-[3px] bg-twr14-magenta text-[#1a0526]" type="button">Enter</button>
          <button class="min-h-11 px-5 py-2.5 border-0 cursor-pointer font-inherit text-[0.85rem] font-semibold tracking-[0.14em] uppercase transition-transform duration-150 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-twr14-cyan focus-visible:outline-offset-[3px] bg-transparent border border-twr14-cyan text-twr14-cyan" type="button">Track list</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr14-magenta: #ff2fb4;
  --color-twr14-cyan: #35e8ff;
  --color-twr14-violet: #6d2bd9;
  --color-twr14-amber: #ffb24d;
  --color-twr14-deep: #16062e;
  --font-twr14-geo: 'Outfit', ui-rounded, 'Avenir Next', 'Century Gothic', system-ui, sans-serif;
  --font-twr14-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --animate-twr14-travel: twr-14-travel 3.2s linear infinite;
}

.twr-14 {
  --twr-14-sky-a: #2a0a4a;
  --twr-14-sky-b: #a3247f;
  --twr-14-sky-c: #ff7a4d;
}
/* Position, not transform: the lines travel and the horizon stays put. */

@keyframes twr-14-travel {
  from {
    background-position: 0 0, 0 0;
  }

  to {
    background-position: 0 0, 0 44px;
  }
}

.twr-14:has(#twr-14-theme:checked) {
  --twr-14-sky-a: #0a0320;
  --twr-14-sky-b: #4c1152;
  --twr-14-sky-c: #b8433f;
  --color-twr14-deep: #08021a;
}
```
