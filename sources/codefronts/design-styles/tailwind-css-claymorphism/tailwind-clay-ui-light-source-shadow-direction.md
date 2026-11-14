---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-clay-ui-light-source-shadow-direction/"
title: "Tailwind Clay UI Light Source & Shadow Direction System"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "A whole dashboard lit by one pair of numbers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Clay UI Light Source & Shadow Direction System
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-clay-ui-light-source-shadow-direction/

A whole dashboard lit by one pair of numbers. Pick a light direction and every card, bar, avatar and button re-lights together, because each shadow is a calc() of two inherited, @property-registered numbers. In Tailwind the formula becomes one custom utility — @utility tcl06-lit — and the direction is four has-[#…:checked]:[--tcl06-lx:1] classes on the root. New: a sun marker orbits the panel so you can see where the light is.
## HTML
```html
<section class="tcl-06 w-full min-h-svh grid place-items-center bg-tcl06-bg px-5 py-14 font-tcl06-sans text-tcl06-ink transition-[--tcl06-lx,--tcl06-ly] duration-[600ms] ease-[cubic-bezier(.4,0,.2,1)] has-[#tcl-06-tr:checked]:[--tcl06-lx:1] has-[#tcl-06-bl:checked]:[--tcl06-ly:1] has-[#tcl-06-br:checked]:[--tcl06-lx:1] has-[#tcl-06-br:checked]:[--tcl06-ly:1] motion-reduce:transition-none" aria-label="Light source consistency across a clay layout demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="relative grid w-full max-w-[960px] gap-[clamp(22px,3vw,32px)] rounded-[44px] bg-tcl06-panel p-[clamp(22px,3.4vw,40px)] tcl06-lit-lg">
      <span aria-hidden="true" class="pointer-events-none absolute top-[calc(50%+var(--tcl06-ly)*50%)] left-[calc(50%+var(--tcl06-lx)*50%)] size-9 -translate-1/2 rounded-full bg-tcl06-sun shadow-[0_0_0_8px_oklch(0.92_0.14_95/0.35),0_0_40px_12px_oklch(0.92_0.14_95/0.55)]"></span>
      <header class="flex flex-wrap items-start justify-between gap-5">
        <div>
          <h2 class="font-tcl06-display text-[clamp(24px,3.2vw,32px)] font-extrabold tracking-[-0.03em]">One light, whole layout</h2>
          <p class="mt-1.5 max-w-[44ch] text-[14.5px] leading-relaxed text-tcl06-mut text-pretty">Every shadow below is derived from two inherited numbers. Move the light and the entire dashboard re-lights.</p>
        </div>
        <fieldset class="grid grid-cols-2 gap-2 border-0">
          <legend class="col-span-full pb-1.5 text-[11px] font-bold uppercase tracking-[0.14em] text-tcl06-mut">Light</legend>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-[18px] bg-tcl06-soft px-3.5 text-[12.5px] font-semibold text-tcl06-mut tcl06-lit-sm transition-colors duration-300 hover:text-tcl06-ink has-checked:bg-tcl06-accent has-checked:text-tcl06-ink has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl06-ink"><input class="sr-only" type="radio" name="tcl-06-dir" id="tcl-06-tl" checked><span aria-hidden="true">↖</span>Top left</label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-[18px] bg-tcl06-soft px-3.5 text-[12.5px] font-semibold text-tcl06-mut tcl06-lit-sm transition-colors duration-300 hover:text-tcl06-ink has-checked:bg-tcl06-accent has-checked:text-tcl06-ink has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl06-ink"><input class="sr-only" type="radio" name="tcl-06-dir" id="tcl-06-tr"><span aria-hidden="true">↗</span>Top right</label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-[18px] bg-tcl06-soft px-3.5 text-[12.5px] font-semibold text-tcl06-mut tcl06-lit-sm transition-colors duration-300 hover:text-tcl06-ink has-checked:bg-tcl06-accent has-checked:text-tcl06-ink has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl06-ink"><input class="sr-only" type="radio" name="tcl-06-dir" id="tcl-06-bl"><span aria-hidden="true">↙</span>Bottom left</label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-[18px] bg-tcl06-soft px-3.5 text-[12.5px] font-semibold text-tcl06-mut tcl06-lit-sm transition-colors duration-300 hover:text-tcl06-ink has-checked:bg-tcl06-accent has-checked:text-tcl06-ink has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl06-ink"><input class="sr-only" type="radio" name="tcl-06-dir" id="tcl-06-br"><span aria-hidden="true">↘</span>Bottom right</label>
        </fieldset>
      </header>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(214px,1fr))] gap-[clamp(14px,2.4vw,22px)]">
        <article class="grid content-start gap-2 rounded-[32px] bg-tcl06-clay px-6 py-5.5 tcl06-lit transition-[translate] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
          <p class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl06-ink/70">Active learners</p>
          <p class="font-tcl06-display text-[clamp(26px,3.4vw,32px)] font-extrabold tracking-[-0.03em] tabular-nums">12,480</p>
          <span aria-hidden="true" class="mt-1 flex h-12 items-end gap-1.5">
            <i class="h-[38%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i><i class="h-[62%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i><i class="h-[48%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i><i class="h-[80%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i><i class="h-[66%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i><i class="h-[94%] flex-1 rounded-lg bg-tcl06-bar tcl06-lit-xs"></i>
          </span>
        </article>
        <article class="grid content-start gap-2 rounded-[32px] bg-tcl06-clay px-6 py-5.5 tcl06-lit transition-[translate] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
          <p class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl06-ink/70">Lesson streak</p>
          <p class="font-tcl06-display text-[clamp(26px,3.4vw,32px)] font-extrabold tracking-[-0.03em] tabular-nums">18 days</p>
          <div class="mt-1 flex items-center gap-3">
            <span aria-hidden="true" class="size-[58px] rounded-full bg-[conic-gradient(var(--color-tcl06-accent)_0_62%,var(--color-tcl06-soft)_62%_100%)] [mask:radial-gradient(circle,transparent_56%,black_57%)]"></span>
            <span class="text-[13px] font-semibold text-tcl06-ink/75">62% of this week’s goal</span>
          </div>
        </article>
        <article class="grid content-start gap-2 rounded-[32px] bg-tcl06-clay px-6 py-5.5 tcl06-lit transition-[translate] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
          <p class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl06-ink/70">Study group</p>
          <ul class="mt-0.5 flex items-center gap-2" aria-label="9 members">
            <li aria-hidden="true" class="size-10 rounded-full bg-[oklch(0.82_0.11_25)] tcl06-lit-xs"></li>
            <li aria-hidden="true" class="size-10 rounded-full bg-[oklch(0.83_0.1_195)] tcl06-lit-xs"></li>
            <li aria-hidden="true" class="size-10 rounded-full bg-[oklch(0.85_0.11_290)] tcl06-lit-xs"></li>
            <li class="grid size-10 place-items-center rounded-full bg-tcl06-soft text-[11.5px] font-bold text-tcl06-mut tcl06-lit-xs">+6</li>
          </ul>
          <button type="button" class="mt-2 min-h-12 cursor-pointer justify-self-start rounded-[22px] bg-tcl06-accent px-5.5 text-sm font-bold text-tcl06-ink tcl06-lit-sm transition-[translate] duration-200 hover:-translate-y-0.5 active:translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl06-ink">Invite</button>
        </article>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl06-mono text-[11.5px] text-tcl06-mut">@utility tcl06-lit · --tcl06-lx / --tcl06-ly inherited · transition the inputs</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcl06-lx {
  syntax: '<number>';
  inherits: true;
  initial-value: -1;
}

@property --tcl06-ly {
  syntax: '<number>';
  inherits: true;
  initial-value: -1;
}

@theme {
  --color-tcl06-bg: #ededd9;
  --color-tcl06-bg: oklch(0.94 0.026 105);
  --color-tcl06-panel: #f3f3e4;
  --color-tcl06-panel: oklch(0.96 0.02 105);
  --color-tcl06-soft: #f0f0df;
  --color-tcl06-soft: oklch(0.95 0.022 105);
  --color-tcl06-clay: #e2d9a4;
  --color-tcl06-clay: oklch(0.88 0.07 100);
  --color-tcl06-accent: #86d489;
  --color-tcl06-accent: oklch(0.8 0.13 145);
  --color-tcl06-bar: #a5e0a5;
  --color-tcl06-bar: oklch(0.85 0.1 145);
  --color-tcl06-sun: #ffee8e;
  --color-tcl06-sun: oklch(0.95 0.12 95);
  --color-tcl06-shade: #91803c99;
  --color-tcl06-shade: oklch(0.6 0.09 95 / 0.6);
  --color-tcl06-light: #fffff1f2;
  --color-tcl06-light: oklch(1 0.02 100 / 0.95);
  --color-tcl06-ink: #2d2911;
  --color-tcl06-ink: oklch(0.28 0.04 100);
  --color-tcl06-mut: #5a563c;
  --color-tcl06-mut: oklch(0.45 0.04 100);
  --font-tcl06-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Light-aware shadows are functions of --tcl06-lx / --tcl06-ly, so they are utilities, not tokens. */

@utility tcl06-lit {
  box-shadow: calc(var(--tcl06-lx) * -12px) calc(var(--tcl06-ly) * -12px) 30px -14px var(--color-tcl06-shade), inset calc(var(--tcl06-lx) * 14px) calc(var(--tcl06-ly) * 14px) 24px -10px var(--color-tcl06-light), inset calc(var(--tcl06-lx) * -14px) calc(var(--tcl06-ly) * -14px) 24px -14px var(--color-tcl06-shade);
}

@utility tcl06-lit-lg {
  box-shadow: calc(var(--tcl06-lx) * -18px) calc(var(--tcl06-ly) * -18px) 46px -18px var(--color-tcl06-shade), inset calc(var(--tcl06-lx) * 16px) calc(var(--tcl06-ly) * 16px) 30px -14px var(--color-tcl06-light), inset calc(var(--tcl06-lx) * -16px) calc(var(--tcl06-ly) * -16px) 30px -18px var(--color-tcl06-shade);
}

@utility tcl06-lit-sm {
  box-shadow: inset calc(var(--tcl06-lx) * 10px) calc(var(--tcl06-ly) * 10px) 16px -10px var(--color-tcl06-light), inset calc(var(--tcl06-lx) * -10px) calc(var(--tcl06-ly) * -10px) 16px -12px var(--color-tcl06-shade);
}

@utility tcl06-lit-xs {
  box-shadow: inset calc(var(--tcl06-lx) * 7px) calc(var(--tcl06-ly) * 7px) 10px -6px var(--color-tcl06-light), inset calc(var(--tcl06-lx) * -7px) calc(var(--tcl06-ly) * -7px) 10px -7px var(--color-tcl06-shade);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-06 {
  width: 100%;
  min-height: 100svh;
}
```
