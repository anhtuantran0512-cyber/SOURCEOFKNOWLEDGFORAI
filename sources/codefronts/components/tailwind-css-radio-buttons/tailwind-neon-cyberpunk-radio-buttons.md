---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-neon-cyberpunk-radio-buttons/"
title: "Tailwind Neon Cyberpunk Radio Buttons"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A sci-fi loadout selector: notch-cornered chips with neon ring indicators that ignite on selection — a conic energy arc spins around the checked ring while…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Cyberpunk Radio Buttons
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-neon-cyberpunk-radio-buttons/

A sci-fi loadout selector: notch-cornered chips with neon ring indicators that ignite on selection — a conic energy arc spins around the checked ring while scanlines texture the chip. The arc's angle is registered with @property (the one piece that stays CSS); notches are [clip-path:polygon(…)], the ring cut is before:[mask:radial-gradient(…)].
## HTML
```html
<section class="trb-16 w-full min-h-svh grid place-items-center bg-trb16-bg bg-[radial-gradient(110%_110%_at_50%_0%,var(--color-trb16-top),transparent_70%)] px-6 py-14 font-trb16-display text-trb16-ink" aria-label="Cyberpunk neon ring radio buttons demo">
  <fieldset>
    <legend class="text-center text-xl font-bold tracking-[0.24em] uppercase [text-shadow:0_0_18px_oklch(0.85_0.15_205/0.6)]">Select loadout</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-[18px]">
      <label class="group relative cursor-pointer has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-white">
        <input type="radio" name="trb-16" value="ghost" class="sr-only" checked>
        <span class="relative isolate grid w-40 justify-items-center gap-0.5 border border-trb16-neon/25 bg-[linear-gradient(170deg,#12172e,#0a0d1c)] px-4 pt-6 pb-5 transition-colors duration-300 [clip-path:polygon(10px_0,100%_0,100%_calc(100%-10px),calc(100%-10px)_100%,0_100%,0_10px)] before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:bg-[repeating-linear-gradient(0deg,oklch(0.85_0.15_205/0.05)_0_1px,transparent_1px_3px)] before:content-[''] group-hover:border-trb16-neon/55 group-has-checked:border-trb16-neon group-has-checked:bg-[linear-gradient(170deg,#16204a,#0b1024)]">
          <span aria-hidden="true" class="relative mb-2.5 size-10 rounded-full border-2 border-trb16-ring transition-colors duration-300 before:absolute before:-inset-[7px] before:rounded-full before:bg-[conic-gradient(from_var(--trb16-a),transparent_0%,var(--color-trb16-neon)_12%,var(--color-trb16-neon2)_22%,transparent_32%)] before:opacity-0 before:transition-opacity before:duration-300 before:[mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3px))] before:content-[''] after:absolute after:inset-2 after:scale-0 after:rounded-full after:bg-trb16-neon after:shadow-trb16-core after:transition-transform after:duration-300 after:ease-trb16-spring after:content-[''] group-has-checked:border-trb16-neon/60 group-has-checked:before:animate-trb16-spin group-has-checked:before:opacity-100 group-has-checked:after:scale-100 motion-reduce:group-has-checked:before:animate-none motion-reduce:group-has-checked:before:bg-trb16-neon/50"></span>
          <span class="text-base font-bold tracking-[0.2em] text-trb16-ink/85 group-has-checked:text-white group-has-checked:[text-shadow:0_0_12px_oklch(0.85_0.15_205/0.7)]">GHOST</span>
          <span class="font-trb16-mono text-[11px] tracking-[0.14em] text-trb16-mut uppercase">Stealth</span>
          <span aria-hidden="true" class="mt-3 flex w-full gap-1 *:h-1 *:flex-1 *:bg-trb16-neon/20 group-has-checked:*:bg-trb16-neon/40"><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i></i><i></i></span>
        </span>
      </label>
      <label class="group relative cursor-pointer has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-white">
        <input type="radio" name="trb-16" value="viper" class="sr-only">
        <span class="relative isolate grid w-40 justify-items-center gap-0.5 border border-trb16-neon/25 bg-[linear-gradient(170deg,#12172e,#0a0d1c)] px-4 pt-6 pb-5 transition-colors duration-300 [clip-path:polygon(10px_0,100%_0,100%_calc(100%-10px),calc(100%-10px)_100%,0_100%,0_10px)] before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:bg-[repeating-linear-gradient(0deg,oklch(0.85_0.15_205/0.05)_0_1px,transparent_1px_3px)] before:content-[''] group-hover:border-trb16-neon/55 group-has-checked:border-trb16-neon group-has-checked:bg-[linear-gradient(170deg,#16204a,#0b1024)]">
          <span aria-hidden="true" class="relative mb-2.5 size-10 rounded-full border-2 border-trb16-ring transition-colors duration-300 before:absolute before:-inset-[7px] before:rounded-full before:bg-[conic-gradient(from_var(--trb16-a),transparent_0%,var(--color-trb16-neon)_12%,var(--color-trb16-neon2)_22%,transparent_32%)] before:opacity-0 before:transition-opacity before:duration-300 before:[mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3px))] before:content-[''] after:absolute after:inset-2 after:scale-0 after:rounded-full after:bg-trb16-neon after:shadow-trb16-core after:transition-transform after:duration-300 after:ease-trb16-spring after:content-[''] group-has-checked:border-trb16-neon/60 group-has-checked:before:animate-trb16-spin group-has-checked:before:opacity-100 group-has-checked:after:scale-100 motion-reduce:group-has-checked:before:animate-none motion-reduce:group-has-checked:before:bg-trb16-neon/50"></span>
          <span class="text-base font-bold tracking-[0.2em] text-trb16-ink/85 group-has-checked:text-white group-has-checked:[text-shadow:0_0_12px_oklch(0.85_0.15_205/0.7)]">VIPER</span>
          <span class="font-trb16-mono text-[11px] tracking-[0.14em] text-trb16-mut uppercase">Assault</span>
          <span aria-hidden="true" class="mt-3 flex w-full gap-1 *:h-1 *:flex-1 *:bg-trb16-neon/20 group-has-checked:*:bg-trb16-neon/40"><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i></span>
        </span>
      </label>
      <label class="group relative cursor-pointer has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-white">
        <input type="radio" name="trb-16" value="atlas" class="sr-only">
        <span class="relative isolate grid w-40 justify-items-center gap-0.5 border border-trb16-neon/25 bg-[linear-gradient(170deg,#12172e,#0a0d1c)] px-4 pt-6 pb-5 transition-colors duration-300 [clip-path:polygon(10px_0,100%_0,100%_calc(100%-10px),calc(100%-10px)_100%,0_100%,0_10px)] before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:bg-[repeating-linear-gradient(0deg,oklch(0.85_0.15_205/0.05)_0_1px,transparent_1px_3px)] before:content-[''] group-hover:border-trb16-neon/55 group-has-checked:border-trb16-neon group-has-checked:bg-[linear-gradient(170deg,#16204a,#0b1024)]">
          <span aria-hidden="true" class="relative mb-2.5 size-10 rounded-full border-2 border-trb16-ring transition-colors duration-300 before:absolute before:-inset-[7px] before:rounded-full before:bg-[conic-gradient(from_var(--trb16-a),transparent_0%,var(--color-trb16-neon)_12%,var(--color-trb16-neon2)_22%,transparent_32%)] before:opacity-0 before:transition-opacity before:duration-300 before:[mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3px))] before:content-[''] after:absolute after:inset-2 after:scale-0 after:rounded-full after:bg-trb16-neon after:shadow-trb16-core after:transition-transform after:duration-300 after:ease-trb16-spring after:content-[''] group-has-checked:border-trb16-neon/60 group-has-checked:before:animate-trb16-spin group-has-checked:before:opacity-100 group-has-checked:after:scale-100 motion-reduce:group-has-checked:before:animate-none motion-reduce:group-has-checked:before:bg-trb16-neon/50"></span>
          <span class="text-base font-bold tracking-[0.2em] text-trb16-ink/85 group-has-checked:text-white group-has-checked:[text-shadow:0_0_12px_oklch(0.85_0.15_205/0.7)]">ATLAS</span>
          <span class="font-trb16-mono text-[11px] tracking-[0.14em] text-trb16-mut uppercase">Tank</span>
          <span aria-hidden="true" class="mt-3 flex w-full gap-1 *:h-1 *:flex-1 *:bg-trb16-neon/20 group-has-checked:*:bg-trb16-neon/40"><i class="bg-trb16-neon! group-has-checked:shadow-trb16-core"></i><i></i><i></i><i></i></span>
        </span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb16-bg: #06070f;
  --color-trb16-bg: oklch(0.13 0.02 275);
  --color-trb16-top: #111531;
  --color-trb16-top: oklch(0.2 0.06 275);
  --color-trb16-ink: #dfe9ff;
  --color-trb16-ink: oklch(0.93 0.03 265);
  --color-trb16-mut: #8f9cc4;
  --color-trb16-mut: oklch(0.7 0.05 270);
  --color-trb16-ring: #3a4668;
  --color-trb16-ring: oklch(0.38 0.05 270);
  --color-trb16-neon: #22e3ff;
  --color-trb16-neon: oklch(0.85 0.15 205);
  --color-trb16-neon2: #ff2bd6;
  --color-trb16-neon2: oklch(0.67 0.29 340);
  --shadow-trb16-core: 0 0 10px oklch(0.85 0.15 205), 0 0 26px oklch(0.85 0.15 205 / 0.55);
  --ease-trb16-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb16-display: 'Chakra Petch', ui-monospace, sans-serif;
  --font-trb16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-trb16-spin: trb16-spin 1.6s linear infinite;

  @keyframes trb16-spin {
    to {
      --trb16-a: 360deg;
    }
  }
}
/* Registered so the conic start angle interpolates — the one at-rule utilities can't express. */

@property --trb16-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-16 {
  width: 100%;
  min-height: 100svh;
}
```
