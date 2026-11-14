---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-oled-true-black-product-card/"
title: "Tailwind OLED True Black Dark Mode Product Card"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A product card for OLED panels, where an unlit pixel is genuinely off: the page is #000 and every layer above it climbs a short surface ramp — #0a0a0a,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind OLED True Black Dark Mode Product Card
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-oled-true-black-product-card/

A product card for OLED panels, where an unlit pixel is genuinely off: the page is #000 and every layer above it climbs a short surface ramp — #0a0a0a, #141414, #1c1c1c — instead of relying on shadows a true-black substrate swallows. Finish swatches and a save toggle are pure-CSS state, and the card is pinned with scheme-only-dark so forced-dark tools leave it alone.
## HTML
```html
<div class="tdm-11 scheme-only-dark grid w-full min-h-svh place-items-center bg-tdm11-void bg-[radial-gradient(80%_55%_at_50%_0%,#0d0d0d,transparent_70%)] px-4 py-12 font-tdm11-sans text-tdm11-body antialiased">
  <article class="grid w-full max-w-[60rem] overflow-hidden rounded-[30px] bg-tdm11-s0 inset-shadow-[0_1px_0_var(--color-tdm11-sheen)] ring-1 ring-tdm11-hair md:grid-cols-[1.05fr_1fr]">
    <div class="relative m-3 overflow-hidden rounded-[22px] bg-tdm11-s1 md:mr-0">
      <img src="https://picsum.photos/seed/oled-1024/900/900" width="900" height="900" alt="Halo desk lamp in anodised graphite — replace with your product photograph" loading="lazy" decoding="async" class="aspect-square size-full object-cover brightness-90 saturate-[.85]">
      <span class="absolute top-3 left-3 inline-flex items-center gap-1.5 rounded-full bg-tdm11-void/70 px-3 py-1.5 font-tdm11-mono text-[11px] text-tdm11-ink ring-1 ring-tdm11-hair backdrop-blur-md"><svg class="size-3.5 text-tdm11-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2.5 4.5 13.5H12l-1 8 8.5-11H12Z"/></svg>Power-optimised for OLED</span>
    </div>
    <div class="grid content-center gap-6 p-6 sm:p-9">
      <div class="grid gap-2">
        <p class="font-tdm11-mono text-[11px] uppercase tracking-[0.18em] text-tdm11-mut">Nocturne Series</p>
        <h1 class="text-[clamp(1.8rem,3.4vw,2.5rem)] font-semibold tracking-[-0.04em] text-tdm11-ink">Halo Desk Lamp</h1>
        <p class="max-w-[42ch] text-[15px]/relaxed text-pretty">Continuous 1800K–5000K dimming with a matte anodised shell. Reads beautifully against a true-black interface.</p>
      </div>
      <fieldset class="grid gap-2.5">
        <legend class="mb-2.5 text-[13px] text-tdm11-mut">Finish</legend>
        <div class="flex gap-2">
          <label class="grid size-11 cursor-pointer place-items-center rounded-full ring-1 ring-tdm11-hair transition hover:ring-tdm11-mut has-checked:ring-2 has-checked:ring-tdm11-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm11-acc" title="Graphite"><input type="radio" name="tdm-11-finish" class="sr-only" checked><span class="sr-only">Graphite</span><span class="size-7 rounded-full bg-[#2a2a2a] shadow-[inset_0_1px_1px_rgb(255_255_255/.3)]"></span></label>
          <label class="grid size-11 cursor-pointer place-items-center rounded-full ring-1 ring-tdm11-hair transition hover:ring-tdm11-mut has-checked:ring-2 has-checked:ring-tdm11-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm11-acc" title="Silver"><input type="radio" name="tdm-11-finish" class="sr-only"><span class="sr-only">Silver</span><span class="size-7 rounded-full bg-[#c9ccd1] shadow-[inset_0_1px_1px_rgb(255_255_255/.3)]"></span></label>
          <label class="grid size-11 cursor-pointer place-items-center rounded-full ring-1 ring-tdm11-hair transition hover:ring-tdm11-mut has-checked:ring-2 has-checked:ring-tdm11-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm11-acc" title="Brass"><input type="radio" name="tdm-11-finish" class="sr-only"><span class="sr-only">Brass</span><span class="size-7 rounded-full bg-[#b99a5b] shadow-[inset_0_1px_1px_rgb(255_255_255/.3)]"></span></label>
        </div>
      </fieldset>
      <dl class="grid divide-y divide-tdm11-hair rounded-2xl bg-tdm11-s1 text-sm">
        <div class="flex justify-between gap-4 px-4 py-3"><dt class="text-tdm11-mut">Finish</dt><dd class="text-tdm11-ink">Anodised graphite</dd></div>
        <div class="flex justify-between gap-4 px-4 py-3"><dt class="text-tdm11-mut">Output</dt><dd class="text-tdm11-ink">420 lm · CRI 97</dd></div>
        <div class="flex justify-between gap-4 px-4 py-3"><dt class="text-tdm11-mut">Ships</dt><dd class="text-tdm11-ink">Free, 2–4 days</dd></div>
      </dl>
      <div class="flex flex-wrap items-center justify-between gap-4">
        <p class="flex items-baseline gap-2"><span class="text-3xl font-semibold tracking-[-0.03em] text-tdm11-ink tabular-nums">$248</span><s class="text-sm text-tdm11-mut">$310</s><span class="rounded-md bg-tdm11-s2 px-1.5 py-0.5 font-tdm11-mono text-[11px] text-tdm11-acc">−20%</span></p>
        <div class="flex gap-2">
          <label class="group/save inline-flex min-h-12 cursor-pointer items-center gap-2 rounded-2xl bg-tdm11-s2 px-4 text-sm font-medium text-tdm11-ink transition hover:bg-tdm11-s3 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm11-acc">
            <input type="checkbox" class="sr-only"><svg class="size-[18px] transition group-has-checked/save:fill-current group-has-checked/save:text-tdm11-love" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 3c0 5.4-7.5 10-7.5 10Z"/></svg><span class="group-has-checked/save:hidden">Save</span><span class="hidden group-has-checked/save:inline">Saved</span>
          </label>
          <button type="button" class="min-h-12 rounded-2xl bg-tdm11-acc px-6 text-sm font-semibold text-tdm11-acc-ink transition hover:-translate-y-px hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm11-acc motion-reduce:transition-none">Add to bag</button>
        </div>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm11-void: #000000;
  --color-tdm11-s0: #0a0a0a;
  --color-tdm11-s1: #141414;
  --color-tdm11-s2: #1c1c1c;
  --color-tdm11-s3: #262626;
  --color-tdm11-hair: rgb(255 255 255 / .08);
  --color-tdm11-sheen: rgb(255 255 255 / .07);
  --color-tdm11-ink: #fafafa;
  --color-tdm11-body: #d4d4d4;
  --color-tdm11-mut: #8f8f8f;
  --color-tdm11-acc: #e8ecf2;
  --color-tdm11-acc-ink: #050505;
  --color-tdm11-love: #fb7185;
  --font-tdm11-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm11-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
