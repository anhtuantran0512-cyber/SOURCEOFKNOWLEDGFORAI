---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/color-coded-tailwind-css-tabs-component/"
title: "Color-Coded Tailwind CSS Tabs Component"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Violet, rose, cyan and lime: four tabs that keep their identity whether active or not."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color-Coded Tailwind CSS Tabs Component
Source: https://codefronts.com/navigation/tailwind-css-tabs/color-coded-tailwind-css-tabs-component/

Violet, rose, cyan and lime: four tabs that keep their identity whether active or not. At rest each is a 6% wash with a 30% border; checked, the wash rises to 18%, the border solidifies and a glow appears. The original's four modifier classes and four checked rules collapsed into one shared class list keyed on [--c:…].
## HTML
```html
<section class="ttb-04 group/tabs grid min-h-svh w-full place-items-center bg-ttb04-bg px-5 py-14 font-ttb04-sans text-ttb04-ink [--c:var(--color-ttb04-violet)] has-[#ttb04-r2:checked]:[--c:var(--color-ttb04-rose)] has-[#ttb04-r3:checked]:[--c:var(--color-ttb04-cyan)] has-[#ttb04-r4:checked]:[--c:var(--color-ttb04-lime)]" aria-label="Color-coded tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div role="radiogroup" aria-label="Category" class="grid w-full grid-cols-2 gap-2 sm:grid-cols-4">
      <label class="group/tab flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-(--c)/30 bg-(--c)/6 text-[13px] font-bold tracking-[0.04em] text-(--c) transition-[background-color,border-color,box-shadow] duration-300 [--c:var(--color-ttb04-violet)] hover:bg-(--c)/12 has-checked:border-(--c) has-checked:bg-(--c)/18 has-checked:shadow-[0_0_18px_color-mix(in_oklab,var(--c)_35%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb04" id="ttb04-r1" checked><span aria-hidden="true" class="size-1.5 rounded-full bg-(--c) transition-transform group-has-checked/tab:scale-150"></span>Violet</label>
      <label class="group/tab flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-(--c)/30 bg-(--c)/6 text-[13px] font-bold tracking-[0.04em] text-(--c) transition-[background-color,border-color,box-shadow] duration-300 [--c:var(--color-ttb04-rose)] hover:bg-(--c)/12 has-checked:border-(--c) has-checked:bg-(--c)/18 has-checked:shadow-[0_0_18px_color-mix(in_oklab,var(--c)_35%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb04" id="ttb04-r2"><span aria-hidden="true" class="size-1.5 rounded-full bg-(--c) transition-transform group-has-checked/tab:scale-150"></span>Rose</label>
      <label class="group/tab flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-(--c)/30 bg-(--c)/6 text-[13px] font-bold tracking-[0.04em] text-(--c) transition-[background-color,border-color,box-shadow] duration-300 [--c:var(--color-ttb04-cyan)] hover:bg-(--c)/12 has-checked:border-(--c) has-checked:bg-(--c)/18 has-checked:shadow-[0_0_18px_color-mix(in_oklab,var(--c)_35%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb04" id="ttb04-r3"><span aria-hidden="true" class="size-1.5 rounded-full bg-(--c) transition-transform group-has-checked/tab:scale-150"></span>Cyan</label>
      <label class="group/tab flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-lg border border-(--c)/30 bg-(--c)/6 text-[13px] font-bold tracking-[0.04em] text-(--c) transition-[background-color,border-color,box-shadow] duration-300 [--c:var(--color-ttb04-lime)] hover:bg-(--c)/12 has-checked:border-(--c) has-checked:bg-(--c)/18 has-checked:shadow-[0_0_18px_color-mix(in_oklab,var(--c)_35%,transparent)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-(--c) motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb04" id="ttb04-r4"><span aria-hidden="true" class="size-1.5 rounded-full bg-(--c) transition-transform group-has-checked/tab:scale-150"></span>Lime</label>
    </div>
    <div class="w-full rounded-xl border border-(--c)/25 bg-(--c)/5 p-5 transition-colors duration-300">
      <p class="hidden text-[15px] leading-relaxed text-ttb04-soft group-has-[#ttb04-r1:checked]/tabs:block"><b class="text-(--c)">Violet</b> — deep and contemplative; for research, long reads and archives.</p>
      <p class="hidden text-[15px] leading-relaxed text-ttb04-soft group-has-[#ttb04-r2:checked]/tabs:block"><b class="text-(--c)">Rose</b> — warm and inviting; for community, people and conversations.</p>
      <p class="hidden text-[15px] leading-relaxed text-ttb04-soft group-has-[#ttb04-r3:checked]/tabs:block"><b class="text-(--c)">Cyan</b> — crisp and technical; for docs, APIs and changelogs.</p>
      <p class="hidden text-[15px] leading-relaxed text-ttb04-soft group-has-[#ttb04-r4:checked]/tabs:block"><b class="text-(--c)">Lime</b> — fresh and urgent; for launches, alerts and what's new.</p>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb04-mono text-[11.5px] text-ttb04-mut">one class list · [--c:…] per tab · bg-(--c)/6 → /18</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb04-bg: #0f0f17;
  --color-ttb04-bg: oklch(0.172 0.017 284.5);
  --color-ttb04-ink: #f4f3f9;
  --color-ttb04-ink: oklch(0.967 0.008 293.9);
  --color-ttb04-soft: #cfcdda;
  --color-ttb04-soft: oklch(0.854 0.018 293.1);
  --color-ttb04-mut: #9a98ab;
  --color-ttb04-mut: oklch(0.688 0.028 290.5);
  --color-ttb04-violet: #c4b5fd;
  --color-ttb04-violet: oklch(0.811 0.101 293.6);
  --color-ttb04-rose: #fda4af;
  --color-ttb04-rose: oklch(0.810 0.106 11.6);
  --color-ttb04-cyan: #67e8f9;
  --color-ttb04-cyan: oklch(0.865 0.115 207.1);
  --color-ttb04-lime: #bef264;
  --color-ttb04-lime: oklch(0.897 0.179 126.7);
  --font-ttb04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttb04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-04 {
  width: 100%;
  min-height: 100svh;
}
```
