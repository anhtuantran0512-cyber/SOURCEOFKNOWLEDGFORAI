---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-css-claymorphism-box-shadow-recipe/"
title: "Tailwind CSS Claymorphism Box Shadow Recipe (3-Layer Formula)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "The reference build for the whole trend, ported to utilities: one clay object, four radio steps, and the shadow assembled one layer at a time — flat fill,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Claymorphism Box Shadow Recipe (3-Layer Formula)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-css-claymorphism-box-shadow-recipe/

The reference build for the whole trend, ported to utilities: one clay object, four radio steps, and the shadow assembled one layer at a time — flat fill, outer drop, inset far-side shade, inset lit-side highlight. Each step is a --shadow-tcl01-s* theme token with the same layer count, so group-has-[#tcl-01-s3:checked]/lab:shadow-tcl01-s3 animates instead of snapping. A new layer meter under the object counts the layers as they land.
## HTML
```html
<section class="tcl-01 w-full min-h-svh grid place-items-center bg-tcl01-bg bg-[radial-gradient(90%_70%_at_20%_0%,var(--color-tcl01-glow),transparent_65%)] px-5 py-14 font-tcl01-sans text-tcl01-ink" aria-label="Claymorphism box shadow recipe demo">
  <div class="grid w-full justify-items-center gap-[clamp(28px,4vw,44px)]">
    <header class="grid max-w-[58ch] gap-2.5 text-center">
      <p class="text-xs font-bold uppercase tracking-[0.16em] text-tcl01-mut">Recipe reference</p>
      <h2 class="font-tcl01-display text-[clamp(28px,4.4vw,42px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">Clay is three shadow layers</h2>
      <p class="text-[15px] leading-relaxed text-tcl01-mut text-pretty">Step through the build. One outer drop for mass, one inset shade for thickness, one inset highlight for the sheen.</p>
    </header>
    <div class="group/lab grid w-full max-w-[960px] justify-items-center gap-[clamp(22px,3vw,36px)] min-[900px]:grid-cols-[auto_auto_1fr] min-[900px]:items-center">
      <fieldset class="grid min-w-[210px] gap-2.5 border-0">
        <legend class="pb-2 text-[11.5px] font-bold uppercase tracking-[0.12em] text-tcl01-mut">Shadow layers</legend>
        <input class="peer/s1 sr-only" type="radio" name="tcl-01-step" id="tcl-01-s1">
        <label for="tcl-01-s1" class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[20px] bg-tcl01-soft px-4.5 text-[14.5px] font-semibold text-tcl01-mut shadow-tcl01-sm transition-[color,translate,box-shadow,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.5 peer-checked/s1:translate-x-1.5 peer-checked/s1:bg-tcl01-clay peer-checked/s1:text-tcl01-ink peer-checked/s1:shadow-tcl01-md peer-focus-visible/s1:outline-3 peer-focus-visible/s1:outline-offset-3 peer-focus-visible/s1:outline-tcl01-ink motion-reduce:transition-none"><b class="grid size-6 place-items-center rounded-full bg-white/65 text-xs text-tcl01-ink">1</b>Flat fill</label>
        <input class="peer/s2 sr-only" type="radio" name="tcl-01-step" id="tcl-01-s2">
        <label for="tcl-01-s2" class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[20px] bg-tcl01-soft px-4.5 text-[14.5px] font-semibold text-tcl01-mut shadow-tcl01-sm transition-[color,translate,box-shadow,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.5 peer-checked/s2:translate-x-1.5 peer-checked/s2:bg-tcl01-clay peer-checked/s2:text-tcl01-ink peer-checked/s2:shadow-tcl01-md peer-focus-visible/s2:outline-3 peer-focus-visible/s2:outline-offset-3 peer-focus-visible/s2:outline-tcl01-ink motion-reduce:transition-none"><b class="grid size-6 place-items-center rounded-full bg-white/65 text-xs text-tcl01-ink">2</b>+ outer drop</label>
        <input class="peer/s3 sr-only" type="radio" name="tcl-01-step" id="tcl-01-s3">
        <label for="tcl-01-s3" class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[20px] bg-tcl01-soft px-4.5 text-[14.5px] font-semibold text-tcl01-mut shadow-tcl01-sm transition-[color,translate,box-shadow,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.5 peer-checked/s3:translate-x-1.5 peer-checked/s3:bg-tcl01-clay peer-checked/s3:text-tcl01-ink peer-checked/s3:shadow-tcl01-md peer-focus-visible/s3:outline-3 peer-focus-visible/s3:outline-offset-3 peer-focus-visible/s3:outline-tcl01-ink motion-reduce:transition-none"><b class="grid size-6 place-items-center rounded-full bg-white/65 text-xs text-tcl01-ink">3</b>+ inset shade</label>
        <input class="peer/s4 sr-only" type="radio" name="tcl-01-step" id="tcl-01-s4" checked>
        <label for="tcl-01-s4" class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[20px] bg-tcl01-soft px-4.5 text-[14.5px] font-semibold text-tcl01-mut shadow-tcl01-sm transition-[color,translate,box-shadow,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.5 peer-checked/s4:translate-x-1.5 peer-checked/s4:bg-tcl01-clay peer-checked/s4:text-tcl01-ink peer-checked/s4:shadow-tcl01-md peer-focus-visible/s4:outline-3 peer-focus-visible/s4:outline-offset-3 peer-focus-visible/s4:outline-tcl01-ink motion-reduce:transition-none"><b class="grid size-6 place-items-center rounded-full bg-white/65 text-xs text-tcl01-ink">4</b>+ inset highlight</label>
      </fieldset>
      <div class="grid place-items-center gap-5 p-3.5">
        <div class="grid aspect-square w-[clamp(180px,26vw,224px)] content-center place-items-center gap-2.5 rounded-[44px] bg-tcl01-clay shadow-tcl01-s1 transition-[box-shadow,translate] duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tcl-01-s2:checked]/lab:-translate-y-1 group-has-[#tcl-01-s2:checked]/lab:shadow-tcl01-s2 group-has-[#tcl-01-s3:checked]/lab:-translate-y-1.5 group-has-[#tcl-01-s3:checked]/lab:shadow-tcl01-s3 group-has-[#tcl-01-s4:checked]/lab:-translate-y-2 group-has-[#tcl-01-s4:checked]/lab:shadow-tcl01-s4 motion-reduce:transition-none">
          <span aria-hidden="true" class="size-16 rounded-[26px] bg-[color-mix(in_oklch,var(--color-tcl01-clay)_60%,white)] shadow-tcl01-glyph"></span>
          <p class="font-tcl01-mono text-xs uppercase tracking-[0.22em] text-tcl01-ink/80">clay</p>
        </div>
        <div class="flex items-center gap-2" aria-hidden="true">
          <i class="h-1.5 w-7 rounded-full bg-tcl01-ink/15 transition-colors duration-300 group-has-[#tcl-01-s2:checked]/lab:bg-tcl01-ink group-has-[#tcl-01-s3:checked]/lab:bg-tcl01-ink group-has-[#tcl-01-s4:checked]/lab:bg-tcl01-ink"></i>
          <i class="h-1.5 w-7 rounded-full bg-tcl01-ink/15 transition-colors duration-300 group-has-[#tcl-01-s3:checked]/lab:bg-tcl01-ink group-has-[#tcl-01-s4:checked]/lab:bg-tcl01-ink"></i>
          <i class="h-1.5 w-7 rounded-full bg-tcl01-ink/15 transition-colors duration-300 group-has-[#tcl-01-s4:checked]/lab:bg-tcl01-ink"></i>
          <span class="ml-1 font-tcl01-mono text-[11px] text-tcl01-mut">layers</span>
        </div>
      </div>
      <pre class="m-0 w-full max-w-[440px] overflow-x-auto rounded-[28px] bg-tcl01-well px-6 py-5.5 font-tcl01-mono text-[12.5px] leading-[1.85] text-tcl01-ink shadow-tcl01-well"><code><span>.clay {
  border-radius: 44px;
  background: var(--clay);</span>
<span class="opacity-25 transition-opacity duration-500 group-has-[#tcl-01-s2:checked]/lab:opacity-100 group-has-[#tcl-01-s3:checked]/lab:opacity-100 group-has-[#tcl-01-s4:checked]/lab:opacity-100">  box-shadow:
    0 22px 40px -10px var(--shade),</span><span class="opacity-25 transition-opacity duration-500 group-has-[#tcl-01-s3:checked]/lab:opacity-100 group-has-[#tcl-01-s4:checked]/lab:opacity-100">
    inset 0 -16px 26px -10px var(--shade),</span><span class="opacity-25 transition-opacity duration-500 group-has-[#tcl-01-s4:checked]/lab:opacity-100">
    inset 0 18px 26px -8px var(--light)</span><span>;
}</span></code></pre>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl01-mono text-[11.5px] text-tcl01-mut shadow-tcl01-chip">shadow-tcl01-s4 · group-has-[#s4:checked]/lab: · fixed layer count = animatable</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl01-bg: #fae7d9;
  --color-tcl01-bg: oklch(0.94 0.028 60);
  --color-tcl01-glow: #fff4dd;
  --color-tcl01-glow: oklch(0.975 0.035 75);
  --color-tcl01-clay: #ffad9a;
  --color-tcl01-clay: oklch(0.83 0.11 32);
  --color-tcl01-shade: color-mix(in oklch, var(--color-tcl01-clay) 55%, oklch(0.42 0.12 30));
  --color-tcl01-light: #fffbe5e6;
  --color-tcl01-light: oklch(0.99 0.03 85 / 0.9);
  --color-tcl01-ink: #402218;
  --color-tcl01-ink: oklch(0.29 0.05 40);
  --color-tcl01-mut: #735245;
  --color-tcl01-mut: oklch(0.47 0.05 42);
  --color-tcl01-soft: color-mix(in oklch, var(--color-tcl01-bg) 88%, white);
  --color-tcl01-well: color-mix(in oklch, var(--color-tcl01-bg) 80%, white);
  --font-tcl01-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl01-s1: 0 22px 40px -10px transparent, inset 0 -16px 26px -10px transparent, inset 0 18px 26px -8px transparent;
  --shadow-tcl01-s2: 0 22px 40px -10px var(--color-tcl01-shade), inset 0 -16px 26px -10px transparent, inset 0 18px 26px -8px transparent;
  --shadow-tcl01-s3: 0 22px 40px -10px var(--color-tcl01-shade), inset 0 -16px 26px -10px var(--color-tcl01-shade), inset 0 18px 26px -8px transparent;
  --shadow-tcl01-s4: 0 22px 40px -10px var(--color-tcl01-shade), inset 0 -16px 26px -10px var(--color-tcl01-shade), inset 0 18px 26px -8px var(--color-tcl01-light);
  --shadow-tcl01-sm: 0 8px 16px -8px var(--color-tcl01-shade), inset 0 -6px 12px -8px var(--color-tcl01-shade), inset 0 8px 12px -6px var(--color-tcl01-light);
  --shadow-tcl01-md: 0 14px 24px -10px var(--color-tcl01-shade), inset 0 -8px 14px -8px var(--color-tcl01-shade), inset 0 10px 16px -6px var(--color-tcl01-light);
  --shadow-tcl01-glyph: inset 0 -8px 14px -8px var(--color-tcl01-shade), inset 0 10px 14px -6px var(--color-tcl01-light);
  --shadow-tcl01-well: inset 0 -10px 20px -12px var(--color-tcl01-shade), inset 0 12px 20px -10px var(--color-tcl01-light), 0 16px 30px -14px var(--color-tcl01-shade);
  --shadow-tcl01-chip: inset 0 -4px 10px -8px var(--color-tcl01-shade), inset 0 6px 10px -6px white;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-01 {
  width: 100%;
  min-height: 100svh;
}
```
