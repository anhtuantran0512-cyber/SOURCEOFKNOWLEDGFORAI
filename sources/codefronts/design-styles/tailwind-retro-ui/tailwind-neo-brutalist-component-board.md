---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-neo-brutalist-component-board/"
title: "Tailwind Neo Brutalist Component Board"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A single board of components in the hard-edged neo-brutalist style &mdash; thick black borders, solid offset shadows, clashing flats, no gradients and no…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neo Brutalist Component Board
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-neo-brutalist-component-board/

A single board of components in the hard-edged neo-brutalist style &mdash; thick black borders, solid offset shadows, clashing flats, no gradients and no radius. It is deliberately one board rather than a component library, because the point is the lineage: this is what the era's chunky, unapologetic chrome turned into once designers stopped apologising for it. It is also the style utilities were practically designed for.
## HTML
```html
<section class="twr-12 relative block w-full min-h-svh box-border bg-twr12-bg text-twr12-k font-twr12-sans" aria-labelledby="twr-12-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-12-title">Neo brutalist component board</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-12-theme">
    <label class="grid place-items-center size-11 cursor-pointer bg-twr12-a text-twr12-k border-[length:var(--twr-12-bord)] border-twr12-k [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] peer-focus-visible:outline-[3px] peer-focus-visible:outline-twr12-acc peer-focus-visible:outline-offset-[3px]" for="twr-12-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark ground</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-7 max-w-[66rem] mx-auto px-[clamp(0.9rem,0.6rem+2vw,2rem)] pt-[clamp(3.75rem,3rem+3vw,5rem)] pb-[calc(4rem+var(--twr-12-off))]">
    <header class="min-w-0 grid gap-2">
      <p class="m-0 font-twr12-mono text-[0.7rem] tracking-[0.14em] uppercase">Lineage &middot; thick borders, flat fills, no ornament</p>
      <h3 class="m-0 min-w-0 text-balance uppercase font-black leading-[0.94] tracking-[-0.045em] text-[clamp(2rem,1rem+6vw,4rem)]">One board.<br>Not a kit.</h3>
    </header>

    <div class="grid gap-[calc(1.25rem+var(--twr-12-off))] grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))]">
      <article class="min-w-0 grid content-start gap-3.5 p-[clamp(1rem,0.7rem+1.4vw,1.5rem)] border-[length:var(--twr-12-bord)] border-twr12-k [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] bg-twr12-a text-twr12-k">
        <h4 class="m-0 text-[0.75rem] font-black tracking-[0.16em] uppercase">Buttons</h4>
        <div class="flex flex-wrap gap-[calc(0.75rem+var(--twr-12-off))]">
          <button class="min-h-11 px-4 py-2.5 border-[length:var(--twr-12-bord)] border-twr12-k font-inherit text-[0.82rem] font-black tracking-[0.1em] cursor-pointer transition-none [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] active:translate-x-[var(--twr-12-off)] active:translate-y-[var(--twr-12-off)] active:shadow-none focus-visible:outline-[3px] focus-visible:outline-twr12-acc focus-visible:outline-offset-[3px] bg-twr12-b text-twr12-w" type="button">PRIMARY</button>
          <button class="min-h-11 px-4 py-2.5 border-[length:var(--twr-12-bord)] border-twr12-k font-inherit text-[0.82rem] font-black tracking-[0.1em] cursor-pointer transition-none [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] active:translate-x-[var(--twr-12-off)] active:translate-y-[var(--twr-12-off)] active:shadow-none focus-visible:outline-[3px] focus-visible:outline-twr12-acc focus-visible:outline-offset-[3px] bg-twr12-c text-twr12-k" type="button">SECOND</button>
          <button class="min-h-11 px-4 py-2.5 border-[length:var(--twr-12-bord)] border-twr12-k font-inherit text-[0.82rem] font-black tracking-[0.1em] cursor-pointer transition-none [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] active:translate-x-[var(--twr-12-off)] active:translate-y-[var(--twr-12-off)] active:shadow-none focus-visible:outline-[3px] focus-visible:outline-twr12-acc focus-visible:outline-offset-[3px] bg-twr12-w text-twr12-k" type="button">GHOST</button>
        </div>
        <p class="m-0 min-w-0 text-[0.8rem] leading-normal text-pretty">Press translates by the shadow offset and drops the shadow. Footprint unchanged.</p>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 p-[clamp(1rem,0.7rem+1.4vw,1.5rem)] border-[length:var(--twr-12-bord)] border-twr12-k [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] bg-twr12-c text-twr12-k">
        <h4 class="m-0 text-[0.75rem] font-black tracking-[0.16em] uppercase">Switch and tags</h4>
        <div class="flex flex-wrap gap-3">
          <span class="relative inline-flex">
            <input class="peer absolute size-px opacity-0 m-0" type="checkbox" id="twr-12-sw" checked>
            <label class="flex items-center gap-2.5 min-h-11 px-3 py-2 cursor-pointer font-black text-[0.78rem] tracking-[0.12em] bg-twr12-w border-[length:var(--twr-12-bord)] border-twr12-k peer-focus-visible:outline-[3px] peer-focus-visible:outline-twr12-acc peer-focus-visible:outline-offset-[3px] peer-checked:[&_[data-knob]]:translate-x-[1.25rem]" for="twr-12-sw">
              <span class="block w-11 h-6 p-0.5 bg-twr12-bg border-[length:var(--twr-12-bord)] border-twr12-k"><span class="block size-4 bg-twr12-k transition-none" data-knob aria-hidden="true"></span></span>NOTIFY
            </label>
          </span>
        </div>
        <ul class="list-none m-0 p-0 flex flex-wrap gap-2 text-[0.7rem] font-black tracking-[0.12em]">
          <li class="px-2 py-1 bg-twr12-k text-twr12-w">FLAT</li>
          <li class="px-2 py-1 bg-twr12-k text-twr12-w">3PX</li>
          <li class="px-2 py-1 bg-twr12-k text-twr12-w">NO RADIUS</li>
          <li class="px-2 py-1 bg-twr12-k text-twr12-w">NO BLUR</li>
        </ul>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 p-[clamp(1rem,0.7rem+1.4vw,1.5rem)] border-[length:var(--twr-12-bord)] border-twr12-k [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] bg-twr12-b text-twr12-w">
        <h4 class="m-0 text-[0.75rem] font-black tracking-[0.16em] uppercase">Stat</h4>
        <p class="m-0 font-black leading-none tracking-[-0.05em] text-[clamp(3rem,2rem+6vw,5.5rem)]">147</p>
        <p class="m-0 min-w-0 text-[0.8rem] leading-normal text-pretty">Offset shadows read as ink misregistration, not elevation.</p>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 p-[clamp(1rem,0.7rem+1.4vw,1.5rem)] border-[length:var(--twr-12-bord)] border-twr12-k [box-shadow:var(--twr-12-off)_var(--twr-12-off)_0_0_var(--color-twr12-k)] bg-twr12-d text-twr12-k">
        <h4 class="m-0 text-[0.75rem] font-black tracking-[0.16em] uppercase">Notice</h4>
        <p class="m-0 min-w-0 text-[0.92rem] leading-normal text-pretty">Every fill carries its own verified text colour. A single ink across five grounds does not pass.</p>
        <p class="m-0 font-twr12-mono text-[0.75rem] tabular-nums">4.9:1 &middot; 8.2:1 &middot; 11.4:1</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr12-k: #0c0c0c;
  --color-twr12-w: #ffffff;
  --color-twr12-a: #ffe500;
  --color-twr12-b: #ff4d2d;
  --color-twr12-c: #00d3c1;
  --color-twr12-d: #b7a6ff;
  --color-twr12-bg: #f4f1e8;
  --color-twr12-bg: oklch(0.95 0.014 92);
  --color-twr12-acc: #1f3bd8;
  --color-twr12-acc: oklch(0.45 0.22 265);
  --font-twr12-sans: 'Archivo', ui-sans-serif, Helvetica, 'Arial Black', Arial, sans-serif;
  --font-twr12-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-12 {
  --twr-12-off: 6px;
  --twr-12-bord: 3px;
}
/* The only rule in the file: a custom-property write from a nested input's
   state, which no variant can perform. Everything else is markup. */

.twr-12:has(#twr-12-theme:checked) {
  --color-twr12-bg: #16150f;
  --color-twr12-bg: oklch(0.19 0.01 92);
}
```
