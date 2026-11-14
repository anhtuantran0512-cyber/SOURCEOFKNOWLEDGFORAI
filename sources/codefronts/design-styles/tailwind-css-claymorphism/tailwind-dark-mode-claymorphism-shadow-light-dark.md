---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-dark-mode-claymorphism-shadow-light-dark/"
title: "Tailwind Dark Mode Claymorphism: Shadow Recalibration with light-dark()"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Dark mode is where naive clay dies: black shadows on a dark page vanish and the object flattens."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Claymorphism: Shadow Recalibration with light-dark()
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-dark-mode-claymorphism-shadow-light-dark/

Dark mode is where naive clay dies: black shadows on a dark page vanish and the object flattens. Every colour token here is a light-dark() pair in @theme, so a single has-[#tcl-19-dark:checked]:[color-scheme:dark] on the root re-themes all three shadow layers at once — longer near-black drop, halved inset shade, and a 1px rim that becomes the primary edge. New: a Light / Dark / System control.
## HTML
```html
<section class="tcl-19 w-full min-h-svh grid place-items-center bg-tcl19-bg px-5 py-14 font-tcl19-sans text-tcl19-ink [color-scheme:light] transition-[background-color,color] duration-500 has-[#tcl-19-dark:checked]:[color-scheme:dark] has-[#tcl-19-sys:checked]:[color-scheme:light_dark]" aria-label="Clay dark mode shadow recalibration demo">
  <div class="grid w-full justify-items-center gap-[clamp(22px,3.5vw,34px)]">
    <header class="grid max-w-[60ch] justify-items-center gap-3.5 text-center">
      <h2 class="font-tcl19-display text-[clamp(28px,4.2vw,40px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">Same object, recalibrated</h2>
      <p class="text-[15px] leading-relaxed text-tcl19-mut text-pretty">Flip the theme. The drop shadow gets darker and longer, the inset shade halves, and a 1px rim highlight takes over as the edge.</p>
      <fieldset class="flex gap-1 rounded-full bg-tcl19-well p-1 shadow-tcl19-well transition-[background-color,box-shadow] duration-500">
        <legend class="sr-only">Theme</legend>
        <label class="grid min-h-11 cursor-pointer place-items-center rounded-full px-4.5 text-[13.5px] font-semibold text-tcl19-mut transition-colors hover:text-tcl19-ink has-checked:bg-tcl19-clay has-checked:text-tcl19-ink has-checked:shadow-tcl19-btn has-focus-visible:outline-3 has-focus-visible:outline-tcl19-ink"><input type="radio" name="tcl-19-theme" id="tcl-19-light" class="sr-only" checked>☀ Light</label>
        <label class="grid min-h-11 cursor-pointer place-items-center rounded-full px-4.5 text-[13.5px] font-semibold text-tcl19-mut transition-colors hover:text-tcl19-ink has-checked:bg-tcl19-clay has-checked:text-tcl19-ink has-checked:shadow-tcl19-btn has-focus-visible:outline-3 has-focus-visible:outline-tcl19-ink"><input type="radio" name="tcl-19-theme" id="tcl-19-dark" class="sr-only">☾ Dark</label>
        <label class="grid min-h-11 cursor-pointer place-items-center rounded-full px-4.5 text-[13.5px] font-semibold text-tcl19-mut transition-colors hover:text-tcl19-ink has-checked:bg-tcl19-clay has-checked:text-tcl19-ink has-checked:shadow-tcl19-btn has-focus-visible:outline-3 has-focus-visible:outline-tcl19-ink"><input type="radio" name="tcl-19-theme" id="tcl-19-sys" class="sr-only">◐ System</label>
      </fieldset>
    </header>
    <div class="grid w-full max-w-[900px] items-center gap-[clamp(16px,2.6vw,24px)] min-[820px]:grid-cols-[1.15fr_.85fr]">
      <article class="grid gap-2.75 rounded-[40px] bg-tcl19-clay p-[clamp(24px,3.2vw,34px)] shadow-tcl19-card transition-[background-color,box-shadow,translate] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
        <span aria-hidden="true" class="size-14 rounded-[22px] bg-tcl19-accent shadow-tcl19-puck transition-[background-color,box-shadow] duration-500"></span>
        <p class="mt-1 text-[11px] font-bold uppercase tracking-[0.15em] text-tcl19-mut">Tier 3 · floating</p>
        <h3 class="font-tcl19-display text-[clamp(21px,2.8vw,26px)] font-bold tracking-[-0.02em]">Recalibrated clay</h3>
        <p class="text-sm leading-relaxed text-tcl19-mut text-pretty">Fill sits 8% lighter than the page in both themes, so the object stays lifted rather than dissolving into the background.</p>
        <ul class="mt-1.5 mb-0.5 grid gap-2 rounded-3xl bg-tcl19-well px-4.5 py-4 shadow-tcl19-well transition-[background-color,box-shadow] duration-500">
          <li class="flex items-center justify-between gap-3 font-tcl19-mono text-xs text-tcl19-mut"><b class="font-semibold">drop</b><span aria-hidden="true" class="h-4 w-18.5 rounded-full bg-tcl19-drop"></span></li>
          <li class="flex items-center justify-between gap-3 font-tcl19-mono text-xs text-tcl19-mut"><b class="font-semibold">inset shade</b><span aria-hidden="true" class="h-4 w-18.5 rounded-full bg-tcl19-inshade"></span></li>
          <li class="flex items-center justify-between gap-3 font-tcl19-mono text-xs text-tcl19-mut"><b class="font-semibold">rim + sheen</b><span aria-hidden="true" class="h-4 w-18.5 rounded-full bg-tcl19-inlight ring-1 ring-tcl19-mut ring-inset"></span></li>
        </ul>
        <div class="mt-1.5 flex flex-wrap gap-2.5">
          <button type="button" class="min-h-12.5 cursor-pointer rounded-[22px] bg-tcl19-accent px-5.5 text-sm font-bold text-tcl19-accentink shadow-tcl19-btn transition-[translate,scale,box-shadow,background-color] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl19-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl19-ink">Apply theme</button>
          <button type="button" class="min-h-12.5 cursor-pointer rounded-[22px] bg-tcl19-well px-5.5 text-sm font-bold text-tcl19-ink shadow-tcl19-btn transition-[translate,scale,box-shadow,background-color] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl19-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl19-ink">Copy tokens</button>
        </div>
      </article>
      <aside class="grid gap-2.5 rounded-[36px] bg-tcl19-well p-[clamp(22px,3vw,30px)] shadow-tcl19-aside transition-[background-color,box-shadow] duration-500">
        <h4 class="text-[11.5px] font-bold uppercase tracking-[0.14em] text-tcl19-mut">Dark-mode rules</h4>
        <ol class="grid list-decimal gap-2.5 pl-5 text-[13.5px] leading-normal text-tcl19-mut marker:font-bold marker:text-tcl19-ink">
          <li><b class="text-tcl19-ink">Lift the fill</b> — +6 to 10% lightness over the page.</li>
          <li><b class="text-tcl19-ink">Add a 1px rim</b> — <code class="font-tcl19-mono text-[11.5px]">inset 0 1px 0 oklch(1 0 0/.16)</code>.</li>
          <li><b class="text-tcl19-ink">Halve the inset shade</b> — dark on dark is mud.</li>
          <li><b class="text-tcl19-ink">Longer, darker drop</b> — near-black at 70%+ alpha.</li>
        </ol>
      </aside>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tcl19-well px-4 py-2 text-center font-tcl19-mono text-[11.5px] text-tcl19-mut shadow-tcl19-well transition-[background-color] duration-500">light-dark() tokens in @theme · has-[#dark:checked]:[color-scheme:dark] · rim-led depth</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl19-bg: light-dark(oklch(0.94 0.025 285), oklch(0.19 0.02 285));
  --color-tcl19-clay: light-dark(oklch(0.9 0.05 285), oklch(0.3 0.03 285));
  --color-tcl19-well: light-dark(oklch(0.95 0.028 285), oklch(0.25 0.025 285));
  --color-tcl19-accent: light-dark(oklch(0.79 0.13 290), oklch(0.62 0.16 290));
  --color-tcl19-accentink: light-dark(oklch(0.24 0.06 290), oklch(0.99 0.01 290));
  --color-tcl19-drop: light-dark(oklch(0.55 0.09 285 / 0.5), oklch(0 0 0 / 0.72));
  --color-tcl19-inshade: light-dark(oklch(0.55 0.09 285 / 0.55), oklch(0 0 0 / 0.5));
  --color-tcl19-inlight: light-dark(oklch(1 0 0 / 0.9), oklch(1 0 0 / 0.1));
  --color-tcl19-rim: light-dark(oklch(1 0 0 / 0), oklch(1 0 0 / 0.16));
  --color-tcl19-ink: light-dark(oklch(0.26 0.05 285), oklch(0.96 0.01 285));
  --color-tcl19-mut: light-dark(oklch(0.45 0.045 285), oklch(0.78 0.02 285));
  --font-tcl19-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl19-card: 0 30px 56px -18px var(--color-tcl19-drop), inset 0 1px 0 0 var(--color-tcl19-rim), inset 0 -16px 26px -12px var(--color-tcl19-inshade), inset 0 18px 30px -10px var(--color-tcl19-inlight);
  --shadow-tcl19-aside: 0 22px 42px -20px var(--color-tcl19-drop), inset 0 1px 0 0 var(--color-tcl19-rim), inset 0 -14px 24px -14px var(--color-tcl19-inshade), inset 0 16px 26px -12px var(--color-tcl19-inlight);
  --shadow-tcl19-puck: 0 14px 24px -10px var(--color-tcl19-drop), inset 0 1px 0 0 var(--color-tcl19-rim), inset 0 -10px 16px -9px var(--color-tcl19-inshade), inset 0 12px 16px -7px var(--color-tcl19-inlight);
  --shadow-tcl19-btn: 0 12px 20px -12px var(--color-tcl19-drop), inset 0 1px 0 0 var(--color-tcl19-rim), inset 0 -9px 15px -9px var(--color-tcl19-inshade), inset 0 11px 15px -7px var(--color-tcl19-inlight);
  --shadow-tcl19-press: 0 0 0 0 transparent, inset 0 1px 0 0 transparent, inset 0 12px 18px -8px var(--color-tcl19-inshade), inset 0 0 0 0 transparent;
  --shadow-tcl19-well: 0 0 0 0 transparent, inset 0 1px 0 0 var(--color-tcl19-rim), inset 0 9px 16px -8px var(--color-tcl19-inshade), inset 0 -6px 12px -10px var(--color-tcl19-inlight);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-19 {
  width: 100%;
  min-height: 100svh;
}
```
