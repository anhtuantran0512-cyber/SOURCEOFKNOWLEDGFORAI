---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-claymorphism-card-component-container-query/"
title: "Tailwind Claymorphism Card Component (Container Query Responsive)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "The workhorse: a clay content card with a real photo in an inset well, concentric radii, a clay avatar row and a one-tier hover lift."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Claymorphism Card Component (Container Query Responsive)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-claymorphism-card-component-container-query/

The workhorse: a clay content card with a real photo in an inset well, concentric radii, a clay avatar row and a one-tier hover lift. It switches from stacked to side-by-side at @min-[430px]: of its container. The port fixes a real bug — the CSS original queried the card from itself, which never matches — and adds a width switch so you can watch the layout flip, plus a working Save toggle.
## HTML
```html
<section class="tcl-13 group/demo w-full min-h-svh grid place-items-center bg-tcl13-bg bg-[radial-gradient(80%_60%_at_30%_0%,var(--color-tcl13-glow),transparent_66%)] px-5 py-14 font-tcl13-sans text-tcl13-ink" aria-label="Claymorphism card component demo">
  <div class="grid w-full justify-items-center gap-6">
    <fieldset class="flex gap-1 rounded-full bg-tcl13-well p-1 shadow-tcl13-well">
      <legend class="sr-only">Container width</legend>
      <label class="grid min-h-11 cursor-pointer place-items-center rounded-full px-4.5 text-[13px] font-semibold text-tcl13-mut transition-colors has-checked:bg-tcl13-clay has-checked:text-tcl13-ink has-checked:shadow-tcl13-btn has-focus-visible:outline-3 has-focus-visible:outline-tcl13-ink"><input type="radio" name="tcl-13-w" id="tcl-13-wide" class="sr-only" checked>Wide slot · 560px</label>
      <label class="grid min-h-11 cursor-pointer place-items-center rounded-full px-4.5 text-[13px] font-semibold text-tcl13-mut transition-colors has-checked:bg-tcl13-clay has-checked:text-tcl13-ink has-checked:shadow-tcl13-btn has-focus-visible:outline-3 has-focus-visible:outline-tcl13-ink"><input type="radio" name="tcl-13-w" id="tcl-13-narrow" class="sr-only">Sidebar · 340px</label>
    </fieldset>
    <div class="@container w-full max-w-[560px] transition-[max-width] duration-500 ease-[cubic-bezier(.34,1.2,.5,1)] group-has-[#tcl-13-narrow:checked]/demo:max-w-[340px] motion-reduce:transition-none">
      <article class="group grid gap-[clamp(14px,2.4vw,18px)] rounded-[40px] bg-tcl13-clay p-3.5 shadow-tcl13-card transition-[translate,box-shadow] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-2 hover:shadow-tcl13-lift @min-[430px]:grid-cols-[172px_1fr] motion-reduce:transition-none">
        <figure class="relative overflow-hidden rounded-[26px] bg-[linear-gradient(145deg,oklch(0.86_0.07_55),oklch(0.75_0.09_40))] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:shadow-[inset_0_12px_22px_-10px_var(--color-tcl13-shade),inset_0_-10px_20px_-12px_oklch(0_0_0/.35)]">
          <img width="640" height="640" loading="lazy" alt="Terracotta pottery bowls on a soft neutral background" src="https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?q=80&w=800&auto=format&fit=crop" class="block size-full min-h-[172px] object-cover transition-[scale] duration-500 ease-[cubic-bezier(.2,.7,.3,1)] group-hover:scale-104">
          <figcaption class="absolute top-3 left-3 rounded-full bg-white/85 px-3 py-1.5 text-[11px] font-bold uppercase tracking-[0.1em] shadow-tcl13-tag backdrop-blur-sm">Module 04</figcaption>
        </figure>
        <div class="grid content-center gap-2.25 px-[clamp(10px,2.4vw,18px)] pt-[clamp(6px,2vw,12px)] pb-[clamp(10px,2vw,14px)]">
          <p class="text-[11px] font-bold uppercase tracking-[0.15em] text-tcl13-ink/70">Interactive course</p>
          <h2 class="font-tcl13-display text-[clamp(21px,3vw,26px)] font-extrabold leading-[1.15] tracking-[-0.03em] text-balance">Sculpting depth with CSS shadows</h2>
          <p class="text-[13.5px] leading-relaxed text-tcl13-ink/85 text-pretty">Six lessons on layered shadows, light discipline and the elevation scale — with every example built as one copyable snippet.</p>
          <div class="mt-0.5 flex items-center gap-3">
            <ul class="flex" aria-hidden="true">
              <li class="size-7.5 rounded-full bg-[oklch(0.84_0.1_30)] shadow-tcl13-av"></li>
              <li class="-ml-2.25 size-7.5 rounded-full bg-[oklch(0.84_0.09_190)] shadow-tcl13-av"></li>
              <li class="-ml-2.25 size-7.5 rounded-full bg-[oklch(0.85_0.1_290)] shadow-tcl13-av"></li>
            </ul>
            <span class="text-[12.5px] text-tcl13-mut tabular-nums">1,204 learners</span>
          </div>
          <div class="mt-2 flex items-center gap-2.5">
            <button type="button" class="min-h-12.5 flex-1 cursor-pointer rounded-[22px] bg-tcl13-accent px-5.5 text-[14.5px] font-bold text-tcl13-accentink shadow-tcl13-btn transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl13-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl13-ink">Start module</button>
            <label class="grid size-12.5 flex-none cursor-pointer place-items-center rounded-[20px] bg-tcl13-soft text-tcl13-mut shadow-tcl13-btn transition-[translate,color,box-shadow] duration-200 hover:-translate-y-0.75 hover:text-tcl13-ink has-checked:text-tcl13-accentink has-checked:shadow-tcl13-press has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl13-ink">
              <input type="checkbox" class="peer sr-only" aria-label="Save for later">
              <svg class="peer-checked:hidden" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M7 4h10a1 1 0 011 1v15l-6-3.6L6 20V5a1 1 0 011-1z"/></svg>
              <svg class="hidden peer-checked:block" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M7 4h10a1 1 0 011 1v15l-6-3.6L6 20V5a1 1 0 011-1z" fill="currentColor"/></svg>
            </label>
          </div>
        </div>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl13-mono text-[11.5px] text-tcl13-mut">@container wrapper · @min-[430px]:grid-cols-[172px_1fr] · concentric radii 40 − 14 = 26</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl13-bg: #fce6d9;
  --color-tcl13-bg: oklch(0.94 0.03 55);
  --color-tcl13-glow: #fff2dc;
  --color-tcl13-glow: oklch(0.97 0.035 70);
  --color-tcl13-well: #f6ddcd;
  --color-tcl13-well: oklch(0.915 0.035 55);
  --color-tcl13-clay: #f9d6bf;
  --color-tcl13-clay: oklch(0.9 0.05 55);
  --color-tcl13-soft: #ffe6d6;
  --color-tcl13-soft: oklch(0.94 0.035 55);
  --color-tcl13-accent: #ffa275;
  --color-tcl13-accent: oklch(0.8 0.13 45);
  --color-tcl13-accentink: #4d1e04;
  --color-tcl13-accentink: oklch(0.3 0.08 45);
  --color-tcl13-shade: #9f64428c;
  --color-tcl13-shade: oklch(0.56 0.09 50 / 0.55);
  --color-tcl13-light: #fffdf5f2;
  --color-tcl13-light: oklch(1 0.015 60 / 0.95);
  --color-tcl13-ink: #3a1e0e;
  --color-tcl13-ink: oklch(0.27 0.05 50);
  --color-tcl13-mut: #6a4e3f;
  --color-tcl13-mut: oklch(0.45 0.045 50);
  --font-tcl13-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl13-card: 0 26px 46px -16px var(--color-tcl13-shade), inset 0 -16px 26px -12px var(--color-tcl13-shade), inset 0 18px 26px -8px var(--color-tcl13-light);
  --shadow-tcl13-lift: 0 40px 66px -20px var(--color-tcl13-shade), inset 0 -16px 26px -12px var(--color-tcl13-shade), inset 0 20px 28px -8px var(--color-tcl13-light);
  --shadow-tcl13-btn: 0 12px 20px -10px var(--color-tcl13-shade), inset 0 -9px 14px -9px var(--color-tcl13-shade), inset 0 11px 15px -7px var(--color-tcl13-light);
  --shadow-tcl13-press: 0 0 0 0 transparent, inset 0 11px 17px -8px var(--color-tcl13-shade), inset 0 -6px 12px -9px var(--color-tcl13-light);
  --shadow-tcl13-well: inset 0 8px 14px -8px var(--color-tcl13-shade), inset 0 -6px 12px -9px var(--color-tcl13-light);
  --shadow-tcl13-av: 0 0 0 3px var(--color-tcl13-clay), inset 0 -5px 8px -6px var(--color-tcl13-shade), inset 0 6px 8px -5px var(--color-tcl13-light);
  --shadow-tcl13-tag: 0 6px 12px -6px var(--color-tcl13-shade), inset 0 5px 8px -5px white;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-13 {
  width: 100%;
  min-height: 100svh;
}
```
