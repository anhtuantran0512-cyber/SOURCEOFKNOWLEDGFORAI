---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-inner-shadow-inset-highlight-clay-ui/"
title: "Tailwind Inner Shadow & Inset Highlight for Clay UI"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Isolate the two inset layers and the material becomes obvious: highlight alone looks inflated, shade alone looks hollow, together they look like clay."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inner Shadow & Inset Highlight for Clay UI
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-inner-shadow-inset-highlight-clay-ui/

Isolate the two inset layers and the material becomes obvious: highlight alone looks inflated, shade alone looks hollow, together they look like clay. The comparison balls use v4's dedicated inset-shadow-* utilities, and the hero sphere orbits its light with two @property-registered lengths — a genuinely animatable inset shadow. New: a pause button, because an infinite animation needs one.
## HTML
```html
<section class="tcl-02 w-full min-h-svh grid place-items-center bg-tcl02-bg bg-[radial-gradient(80%_60%_at_78%_4%,var(--color-tcl02-glow),transparent_62%)] px-5 py-14 font-tcl02-sans text-tcl02-ink" aria-label="Inner shadow and inset highlight demo">
  <div class="grid w-full justify-items-center gap-[clamp(32px,5vw,56px)]">
    <div class="group/hero grid w-full max-w-[880px] items-center justify-items-center gap-[clamp(24px,4vw,48px)] text-center min-[820px]:grid-cols-[auto_1fr] min-[820px]:text-left">
      <div aria-hidden="true" class="aspect-square w-[clamp(168px,24vw,210px)] animate-tcl02-orbit rounded-full bg-tcl02-clay [box-shadow:0_26px_44px_-14px_var(--color-tcl02-shade),inset_var(--tcl02-lx)_var(--tcl02-ly)_30px_-8px_var(--color-tcl02-light),inset_calc(var(--tcl02-lx)*-1)_calc(var(--tcl02-ly)*-1)_30px_-8px_var(--color-tcl02-shade)] group-has-[:checked]/hero:[animation-play-state:paused] motion-reduce:animate-none"></div>
      <div class="grid max-w-[46ch] justify-items-center gap-3.5 min-[820px]:justify-items-start">
        <h2 class="font-tcl02-display text-[clamp(26px,3.6vw,36px)] font-extrabold leading-[1.08] tracking-[-0.03em] text-balance">Two insets make the material</h2>
        <p class="text-[15px] leading-[1.65] text-tcl02-mut text-pretty">The highlight is the lit face, the shade is the far wall. Keep them diametrically opposed and the object holds one light source — even while the light orbits.</p>
        <div class="flex flex-wrap items-center gap-2.5">
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl02-soft px-4.5 text-[13.5px] font-semibold shadow-tcl02-pill transition-transform hover:-translate-y-0.5 has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tcl02-ink">
            <input type="checkbox" class="peer sr-only">
            <svg class="size-3.5 peer-checked:hidden" viewBox="0 0 16 16" aria-hidden="true"><rect x="3.5" y="2.5" width="3" height="11" rx="1" fill="currentColor"/><rect x="9.5" y="2.5" width="3" height="11" rx="1" fill="currentColor"/></svg>
            <svg class="hidden size-3.5 peer-checked:block" viewBox="0 0 16 16" aria-hidden="true"><path d="M4.5 2.8v10.4a.6.6 0 0 0 .9.5l8.2-5.2a.6.6 0 0 0 0-1L5.4 2.3a.6.6 0 0 0-.9.5z" fill="currentColor"/></svg>
            <span class="peer-checked:hidden">Pause light</span><span class="hidden peer-checked:inline">Play light</span>
          </label>
          <p class="rounded-full bg-tcl02-soft px-4 py-2.5 font-tcl02-mono text-[11.5px] shadow-tcl02-pill">@property &lt;length&gt; → animatable inset</p>
        </div>
      </div>
    </div>
    <ul class="grid w-full max-w-[780px] grid-cols-[repeat(auto-fit,minmax(160px,1fr))] gap-[clamp(16px,3vw,28px)]">
      <li class="grid justify-items-center gap-2 rounded-[34px] bg-tcl02-soft px-4.5 pt-7 pb-6 text-center shadow-tcl02-card transition-transform duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5 motion-reduce:transition-none">
        <span aria-hidden="true" class="mb-2 size-[84px] rounded-full bg-tcl02-clay inset-shadow-tcl02-light"></span>
        <b class="font-tcl02-display text-[15px] font-bold tracking-[-0.01em]">Highlight only</b>
        <span class="text-[12.5px] text-tcl02-mut">inflated · no thickness</span>
      </li>
      <li class="grid justify-items-center gap-2 rounded-[34px] bg-tcl02-soft px-4.5 pt-7 pb-6 text-center shadow-tcl02-card transition-transform duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5 motion-reduce:transition-none">
        <span aria-hidden="true" class="mb-2 size-[84px] rounded-full bg-tcl02-clay inset-shadow-tcl02-dark"></span>
        <b class="font-tcl02-display text-[15px] font-bold tracking-[-0.01em]">Shade only</b>
        <span class="text-[12.5px] text-tcl02-mut">hollow · reads as a bowl</span>
      </li>
      <li class="grid justify-items-center gap-2 rounded-[34px] bg-tcl02-soft px-4.5 pt-7 pb-6 text-center shadow-tcl02-card ring-2 ring-tcl02-clay/60 transition-transform duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5 motion-reduce:transition-none">
        <span aria-hidden="true" class="mb-2 size-[84px] rounded-full bg-tcl02-clay inset-shadow-tcl02-both shadow-tcl02-ball"></span>
        <b class="font-tcl02-display text-[15px] font-bold tracking-[-0.01em]">Both layers</b>
        <span class="text-[12.5px] text-tcl02-mut">clay · pressable mass</span>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcl02-lx {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

@property --tcl02-ly {
  syntax: '<length>';
  inherits: false;
  initial-value: 20px;
}

@theme {
  --color-tcl02-bg: #e8e9ff;
  --color-tcl02-bg: oklch(0.94 0.03 285);
  --color-tcl02-glow: #faf2ff;
  --color-tcl02-glow: oklch(0.975 0.035 300);
  --color-tcl02-clay: #bfb2f9;
  --color-tcl02-clay: oklch(0.8 0.1 292);
  --color-tcl02-shade: color-mix(in oklch, var(--color-tcl02-clay) 45%, oklch(0.38 0.13 290));
  --color-tcl02-light: #fef9fff2;
  --color-tcl02-light: oklch(0.99 0.02 300 / 0.95);
  --color-tcl02-ink: #2a2344;
  --color-tcl02-ink: oklch(0.28 0.06 292);
  --color-tcl02-mut: #595277;
  --color-tcl02-mut: oklch(0.46 0.06 292);
  --color-tcl02-soft: color-mix(in oklch, var(--color-tcl02-bg) 84%, white);
  --font-tcl02-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --inset-shadow-tcl02-light: inset 0 20px 28px -8px var(--color-tcl02-light);
  --inset-shadow-tcl02-dark: inset 0 -20px 28px -8px var(--color-tcl02-shade);
  --inset-shadow-tcl02-both: inset 0 20px 28px -8px var(--color-tcl02-light), inset 0 -20px 28px -8px var(--color-tcl02-shade);
  --shadow-tcl02-ball: 0 12px 20px -10px var(--color-tcl02-shade);
  --shadow-tcl02-card: 0 18px 34px -18px var(--color-tcl02-shade), inset 0 -10px 18px -12px var(--color-tcl02-shade), inset 0 12px 18px -10px var(--color-tcl02-light);
  --shadow-tcl02-pill: inset 0 -6px 12px -8px var(--color-tcl02-shade), inset 0 8px 12px -6px var(--color-tcl02-light);
  --animate-tcl02-orbit: tcl02-orbit 9s linear infinite;

  @keyframes tcl02-orbit {
    0%,
        100% {
      --tcl02-lx: 0px;
      --tcl02-ly: 20px;
    }

    25% {
      --tcl02-lx: 20px;
      --tcl02-ly: 0px;
    }

    50% {
      --tcl02-lx: 0px;
      --tcl02-ly: -20px;
    }

    75% {
      --tcl02-lx: -20px;
      --tcl02-ly: 0px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-02 {
  width: 100%;
  min-height: 100svh;
}
```
