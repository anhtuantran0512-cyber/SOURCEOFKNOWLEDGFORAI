---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/font-specimen-glyph-tabs-tailwind-css/"
title: "Font Specimen Glyph Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A foundry specimen card: the foundry mark on the left, large glyph tabs on the right — Aa for the roman, Bb for the bold, Cc for small caps."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Font Specimen Glyph Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/font-specimen-glyph-tabs-tailwind-css/

A foundry specimen card: the foundry mark on the left, large glyph tabs on the right — Aa for the roman, Bb for the bold, Cc for small caps. The chosen glyph pulses vermilion; the panel now shows a full pangram in that cut, set in Fraunces.
## HTML
```html
<section class="ttb-28 group/tabs grid min-h-svh w-full place-items-center bg-ttb28-bg px-5 py-14 font-ttb28-serif text-ttb28-paper" aria-label="Font specimen glyph tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full rounded-2xl bg-ttb28-card p-6 ring-1 ring-ttb28-paper/10">
      <div class="flex items-stretch gap-6 border-b border-ttb28-paper/18 pb-4">
        <div class="border-r border-ttb28-paper/18 pr-6 font-ttb28-mono">
          <p class="text-[11px] leading-snug font-extrabold tracking-[0.2em] uppercase">CodeFronts<br>Foundry</p>
          <p class="mt-2 text-[10px] font-medium tracking-[0.2em] text-ttb28-mut">SPEC · 2026</p>
        </div>
        <div role="radiogroup" aria-label="Cut" class="flex items-baseline gap-5">
          <label class="min-h-11 origin-bottom-left cursor-pointer text-[32px] leading-none font-bold text-ttb28-mut transition-[color,scale] duration-400 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:text-ttb28-paper has-checked:scale-115 has-checked:text-ttb28-red has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb28-red motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb28" id="ttb28-r1" checked><span class="sr-only">Roman</span><span aria-hidden="true" class="font-normal">Aa</span></label>
          <label class="min-h-11 origin-bottom-left cursor-pointer text-[32px] leading-none font-bold text-ttb28-mut transition-[color,scale] duration-400 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:text-ttb28-paper has-checked:scale-115 has-checked:text-ttb28-red has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb28-red motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb28" id="ttb28-r2"><span class="sr-only">Bold</span><span aria-hidden="true" class="font-black">Bb</span></label>
          <label class="min-h-11 origin-bottom-left cursor-pointer text-[32px] leading-none font-bold text-ttb28-mut transition-[color,scale] duration-400 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:text-ttb28-paper has-checked:scale-115 has-checked:text-ttb28-red has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb28-red motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb28" id="ttb28-r3"><span class="sr-only">Small caps</span><span aria-hidden="true" class="font-medium [font-variant-caps:small-caps]">Cc</span></label>
        </div>
      </div>
      <div class="pt-5">
        <div class="hidden group-has-[#ttb28-r1:checked]/tabs:block"><p class="text-[28px] leading-tight font-normal text-balance">Sphinx of black quartz, judge my vow.</p><p class="mt-2 text-[13px] text-ttb28-mut italic">Upright Roman · 400 · optical size auto</p></div>
        <div class="hidden group-has-[#ttb28-r2:checked]/tabs:block"><p class="text-[28px] leading-tight font-black text-balance">Sphinx of black quartz, judge my vow.</p><p class="mt-2 text-[13px] text-ttb28-mut italic">Bold · 900 · display weight</p></div>
        <div class="hidden group-has-[#ttb28-r3:checked]/tabs:block"><p class="text-[28px] leading-tight font-medium text-balance [font-variant-caps:small-caps]">Sphinx of black quartz, judge my vow.</p><p class="mt-2 text-[13px] text-ttb28-mut italic">Small caps · 500 · for running heads</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb28-paper/12 px-3.5 py-2 font-ttb28-mono text-[11.5px] text-ttb28-mut">items-baseline · has-checked:scale-115 · live pangram per cut</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb28-bg: #141414;
  --color-ttb28-bg: oklch(0.191 0 0);
  --color-ttb28-card: #1c1c1c;
  --color-ttb28-card: oklch(0.226 0 0);
  --color-ttb28-paper: #ece6d4;
  --color-ttb28-paper: oklch(0.925 0.025 91.6);
  --color-ttb28-mut: #a8a293;
  --color-ttb28-mut: oklch(0.713 0.022 88.8);
  --color-ttb28-red: #e0574c;
  --color-ttb28-red: oklch(0.635 0.173 27.6);
  --font-ttb28-serif: 'Fraunces', Georgia, serif;
  --font-ttb28-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-28 {
  width: 100%;
  min-height: 100svh;
}
```
