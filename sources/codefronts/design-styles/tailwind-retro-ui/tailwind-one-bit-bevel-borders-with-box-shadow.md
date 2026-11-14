---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-one-bit-bevel-borders-with-box-shadow/"
title: "Tailwind One Bit Bevel Borders with Box Shadow"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "Every raised or sunken control of the 16-bit desktop era is the same object: four box-shadow insets in a fixed order &mdash; outer light, outer dark, inner…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind One Bit Bevel Borders with Box Shadow
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-one-bit-bevel-borders-with-box-shadow/

Every raised or sunken control of the 16-bit desktop era is the same object: four box-shadow insets in a fixed order &mdash; outer light, outer dark, inner light, inner dark &mdash; with the order reversed for the pressed state. This is the demo where a four-layer shadow is too long to keep repeating in a class list, so it becomes a real named utility with @utility, and active:twr04-sunken gets the pressed state for free.
## HTML
```html
<section class="twr-04 relative block w-full min-h-svh box-border bg-twr04-bg text-twr04-ink font-twr04-sans" aria-labelledby="twr-04-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-04-title">One-bit bevel border states</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-04-theme">
    <label class="grid place-items-center size-11 cursor-pointer bg-twr04-face text-[#101010] twr04-raised peer-focus-visible:outline-2 peer-focus-visible:outline-dotted peer-focus-visible:outline-[#000] peer-focus-visible:outline-offset-[-6px]" for="twr-04-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-5 max-w-[70rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="grid gap-1.5 min-w-0">
      <p class="m-0 font-twr04-mono text-[0.68rem] tracking-[0.14em] uppercase text-[#d7f0f0]">Windows 95 &middot; system metrics, 3D objects</p>
      <h3 class="m-0 min-w-0 text-balance text-[clamp(1.3rem,1rem+1.9vw,2.1rem)] font-bold leading-tight tracking-[-0.02em] text-white [text-shadow:1px_1px_0_rgba(0,0,0,0.45)]">Four insets, one fixed order</h3>
    </header>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-5 lg:grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)]">
      <article class="min-w-0 grid content-start gap-3.5 p-4 bg-twr04-panel twr04-raised" aria-labelledby="twr-04-g1">
        <h4 class="m-0 text-[0.78rem] tracking-[0.1em] uppercase text-twr04-ink2" id="twr-04-g1">States</h4>
        <div class="grid gap-4 grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))]">
          <div class="min-w-0 grid justify-items-start gap-2">
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-pointer border-0 bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken active:pt-[calc(0.5rem+1px)] active:ps-[calc(1.125rem+1px)] active:pb-[calc(0.5rem-1px)] active:pe-[calc(1.125rem-1px)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-6px]" type="button">Raised</button>
            <p class="m-0 min-w-0 [overflow-wrap:anywhere] font-twr04-mono text-[0.66rem] leading-snug text-twr04-ink2">default &middot; light outer top-left</p>
          </div>
          <div class="min-w-0 grid justify-items-start gap-2">
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-pointer border-0 bg-twr04-face text-[#101010] twr04-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-6px]" type="button" aria-pressed="true">Pressed</button>
            <p class="m-0 min-w-0 [overflow-wrap:anywhere] font-twr04-mono text-[0.66rem] leading-snug text-twr04-ink2">order reversed &middot; caption offset 1px</p>
          </div>
          <div class="min-w-0 grid justify-items-start gap-2">
            <div class="min-h-11 min-w-0 flex items-center px-3.5 py-2 text-[0.9rem] bg-white text-[#101010] twr04-well">Sunken well</div>
            <p class="m-0 min-w-0 [overflow-wrap:anywhere] font-twr04-mono text-[0.66rem] leading-snug text-twr04-ink2">reversed, no caption offset</p>
          </div>
          <div class="min-w-0 grid justify-items-start gap-2">
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-not-allowed border-0 bg-twr04-face text-twr04-shadow twr04-raised [text-shadow:1px_1px_0_var(--color-twr04-hilite)]" type="button" disabled>Disabled</button>
            <p class="m-0 min-w-0 [overflow-wrap:anywhere] font-twr04-mono text-[0.66rem] leading-snug text-twr04-ink2">etched caption &middot; shadow + highlight</p>
          </div>
        </div>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 p-4 bg-twr04-panel twr04-raised" aria-labelledby="twr-04-g2">
        <h4 class="m-0 text-[0.78rem] tracking-[0.1em] uppercase text-twr04-ink2" id="twr-04-g2">Exploded edge</h4>
        <div class="grid gap-1.5 min-w-0">
          <div class="min-w-0 flex items-center gap-2.5 [overflow-wrap:anywhere] font-twr04-mono text-[0.72rem] px-2.5 py-2.5 bg-twr04-face text-[#101010] [box-shadow:inset_0_3px_0_0_var(--color-twr04-hilite),inset_3px_0_0_0_var(--color-twr04-hilite)]"><span class="flex-none grid place-items-center size-[22px] bg-[#101010] text-twr04-face text-[0.7rem]">1</span> inset 1px 1px 0 #ffffff</div>
          <div class="min-w-0 flex items-center gap-2.5 [overflow-wrap:anywhere] font-twr04-mono text-[0.72rem] px-2.5 py-2.5 bg-twr04-face text-[#101010] [box-shadow:inset_0_-3px_0_0_var(--color-twr04-dark),inset_-3px_0_0_0_var(--color-twr04-dark)]"><span class="flex-none grid place-items-center size-[22px] bg-[#101010] text-twr04-face text-[0.7rem]">2</span> inset -1px -1px 0 #000000</div>
          <div class="min-w-0 flex items-center gap-2.5 [overflow-wrap:anywhere] font-twr04-mono text-[0.72rem] px-2.5 py-2.5 bg-twr04-face text-[#101010] [box-shadow:inset_0_3px_0_0_var(--color-twr04-light),inset_3px_0_0_0_var(--color-twr04-light)]"><span class="flex-none grid place-items-center size-[22px] bg-[#101010] text-twr04-face text-[0.7rem]">3</span> inset 2px 2px 0 #dfdfdf</div>
          <div class="min-w-0 flex items-center gap-2.5 [overflow-wrap:anywhere] font-twr04-mono text-[0.72rem] px-2.5 py-2.5 bg-twr04-face text-[#101010] [box-shadow:inset_0_-3px_0_0_var(--color-twr04-shadow),inset_-3px_0_0_0_var(--color-twr04-shadow)]"><span class="flex-none grid place-items-center size-[22px] bg-[#101010] text-twr04-face text-[0.7rem]">4</span> inset -2px -2px 0 #808080</div>
        </div>
        <p class="m-0 min-w-0 text-[0.8rem] leading-normal text-pretty text-twr04-ink2">Painted first to last, top to bottom. Later layers sit underneath.</p>
      </article>
    </div>

    <article class="min-w-0 grid content-start gap-3.5 p-4 bg-twr04-panel twr04-raised" aria-labelledby="twr-04-g3">
      <h4 class="m-0 text-[0.78rem] tracking-[0.1em] uppercase text-twr04-ink2" id="twr-04-g3">Applied &mdash; a dialog built only from insets</h4>
      <div class="min-w-0 p-[3px] bg-twr04-face twr04-raised">
        <div class="flex items-center justify-between gap-2 min-w-0 m-[3px] py-1.5 pe-1.5 ps-2.5 [background:linear-gradient(90deg,var(--color-twr04-titlea),var(--color-twr04-titleb))]">
          <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-white text-[0.85rem] font-bold">Display Properties</span>
          <span class="flex flex-none gap-[3px]">
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer font-inherit text-[0.8rem] leading-none bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-7px]" type="button" aria-label="Minimise"><span aria-hidden="true">_</span></button>
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer font-inherit text-[0.8rem] leading-none bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-7px]" type="button" aria-label="Maximise"><span aria-hidden="true">&#9633;</span></button>
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer font-inherit text-[0.8rem] leading-none bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-7px]" type="button" aria-label="Close"><span aria-hidden="true">&#215;</span></button>
          </span>
        </div>
        <div class="grid gap-3.5 min-w-0 px-3 pt-4 pb-3.5">
          <p class="m-0 min-w-0 text-[0.88rem] leading-normal text-pretty text-[#101010]">The bevel unit is a single custom property. Every control below shares it.</p>
          <div class="flex flex-wrap items-center gap-2.5 min-w-0">
            <span class="min-w-0 text-[0.85rem] text-[#101010]" id="twr-04-fl">Colour palette</span>
            <span class="min-h-11 flex-1 basis-40 flex items-center px-3.5 py-2 bg-white text-[#101010] font-twr04-mono text-[0.82rem] twr04-well" role="status" aria-labelledby="twr-04-fl">256 Colour</span>
          </div>
          <div class="flex flex-wrap gap-2">
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-pointer border-0 bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken active:pt-[calc(0.5rem+1px)] active:ps-[calc(1.125rem+1px)] active:pb-[calc(0.5rem-1px)] active:pe-[calc(1.125rem-1px)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-6px]" type="button">OK</button>
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-pointer border-0 bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken active:pt-[calc(0.5rem+1px)] active:ps-[calc(1.125rem+1px)] active:pb-[calc(0.5rem-1px)] active:pe-[calc(1.125rem-1px)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-6px]" type="button">Cancel</button>
            <button class="min-h-11 min-w-11 px-4.5 py-2 font-inherit text-[0.9rem] cursor-pointer border-0 bg-twr04-face text-[#101010] twr04-raised active:twr04-sunken active:pt-[calc(0.5rem+1px)] active:ps-[calc(1.125rem+1px)] active:pb-[calc(0.5rem-1px)] active:pe-[calc(1.125rem-1px)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-[#000] focus-visible:outline-offset-[-6px]" type="button">Apply</button>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr04-face: #c0c0c0;
  --color-twr04-hilite: #ffffff;
  --color-twr04-light: #dfdfdf;
  --color-twr04-shadow: #808080;
  --color-twr04-dark: #000000;
  --color-twr04-titlea: #000080;
  --color-twr04-titleb: #1084d0;
  --color-twr04-panel: #d8d8d0;
  --color-twr04-bg: #008080;
  --color-twr04-ink: #101214;
  --color-twr04-ink: oklch(0.18 0.006 240);
  --color-twr04-ink2: #3d4348;
  --color-twr04-ink2: oklch(0.38 0.01 240);
  --font-twr04-sans: system-ui, -apple-system, 'Segoe UI', Tahoma, Arial, sans-serif;
  --font-twr04-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-04 {
  --twr-04-b: 2px;
}
/* A repeated VALUE becomes an @theme token; a repeated DECLARATION BLOCK becomes
   an @utility. These register in the utility layer, so active:, hover: and
   breakpoint variants compose with them exactly like built-ins — which @apply
   would not allow. */

@utility twr04-raised {
  box-shadow: inset var(--twr-04-b) var(--twr-04-b) 0 0 var(--color-twr04-hilite), inset calc(var(--twr-04-b) * -1) calc(var(--twr-04-b) * -1) 0 0 var(--color-twr04-dark), inset calc(var(--twr-04-b) * 2) calc(var(--twr-04-b) * 2) 0 0 var(--color-twr04-light), inset calc(var(--twr-04-b) * -2) calc(var(--twr-04-b) * -2) 0 0 var(--color-twr04-shadow);
}

@utility twr04-sunken {
  box-shadow: inset var(--twr-04-b) var(--twr-04-b) 0 0 var(--color-twr04-dark), inset calc(var(--twr-04-b) * -1) calc(var(--twr-04-b) * -1) 0 0 var(--color-twr04-hilite), inset calc(var(--twr-04-b) * 2) calc(var(--twr-04-b) * 2) 0 0 var(--color-twr04-shadow), inset calc(var(--twr-04-b) * -2) calc(var(--twr-04-b) * -2) 0 0 var(--color-twr04-light);
}
/* A well is sunken against white rather than face grey, so the tone pairs differ. */

@utility twr04-well {
  box-shadow: inset var(--twr-04-b) var(--twr-04-b) 0 0 var(--color-twr04-shadow), inset calc(var(--twr-04-b) * -1) calc(var(--twr-04-b) * -1) 0 0 var(--color-twr04-hilite), inset calc(var(--twr-04-b) * 2) calc(var(--twr-04-b) * 2) 0 0 var(--color-twr04-dark), inset calc(var(--twr-04-b) * -2) calc(var(--twr-04-b) * -2) 0 0 var(--color-twr04-light);
}

.twr-04:has(#twr-04-theme:checked) {
  --color-twr04-bg: #0a2c2c;
  --color-twr04-bg: oklch(0.26 0.045 195);
  --color-twr04-panel: #cfcfc7;
}
```
