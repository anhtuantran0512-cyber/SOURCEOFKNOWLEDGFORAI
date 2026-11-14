---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-bg-clip-text-gradient-utility-classes-cheat-sheet/"
title: "Tailwind bg-clip-text Gradient Utility Classes Cheat Sheet"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "The reference the original could only imitate: every utility behind Tailwind gradient text, with the v3 name, the v4 name and the CSS it compiles to &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind bg-clip-text Gradient Utility Classes Cheat Sheet
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-bg-clip-text-gradient-utility-classes-cheat-sheet/

The reference the original could only imitate: every utility behind Tailwind gradient text, with the v3 name, the v4 name and the CSS it compiles to &mdash; then six live examples rendered by real Tailwind, from bg-linear-to-r through bg-radial, bg-conic and /oklch interpolation.
## HTML
```html
<section class="ttg-18 w-full min-h-svh bg-ttg18-bg font-ttg18-sans text-ttg18-ink" aria-labelledby="ttg18-title">
  <div class="mx-auto max-w-3xl px-5 py-14">
    <h2 id="ttg18-title" class="text-[clamp(1.75rem,4.5vw,2.5rem)] leading-[1.12] font-extrabold tracking-[-0.03em]">Tailwind gradient text<br><span class="bg-linear-to-r from-indigo-500 to-purple-600 bg-clip-text text-transparent">utility cheat sheet</span></h2>
    <p class="mt-3 max-w-xl text-[15px]/[1.7] text-ttg18-mut">Four ideas, a handful of classes. Here's every one, its v3 name and the CSS it compiles to.</p>
    <div class="mt-8 max-h-[22rem] overflow-auto rounded-2xl border border-ttg18-line bg-white">
      <table class="w-full min-w-[34rem] border-collapse text-left text-[13.5px]">
        <thead class="sticky top-0 bg-ttg18-head text-[11px] font-semibold tracking-[0.1em] text-ttg18-mut uppercase">
          <tr><th class="px-4 py-3">v4 utility</th><th class="px-4 py-3">v3</th><th class="px-4 py-3">Compiles to</th></tr>
        </thead>
        <tbody class="divide-y divide-ttg18-line font-ttg18-mono text-[12.5px]">
          <tr><td class="px-4 py-3 text-indigo-600">bg-linear-to-r</td><td class="px-4 py-3 text-ttg18-mut">bg-gradient-to-r</td><td class="px-4 py-3">linear-gradient(to right in oklab, …)</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">bg-linear-45</td><td class="px-4 py-3 text-ttg18-mut">—</td><td class="px-4 py-3">linear-gradient(45deg in oklab, …)</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">bg-radial</td><td class="px-4 py-3 text-ttg18-mut">—</td><td class="px-4 py-3">radial-gradient(in oklab, …)</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">bg-conic</td><td class="px-4 py-3 text-ttg18-mut">—</td><td class="px-4 py-3">conic-gradient(in oklab, …)</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">from-indigo-500</td><td class="px-4 py-3 text-ttg18-mut">same</td><td class="px-4 py-3">--tw-gradient-from: var(--color-indigo-500)</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">via-fuchsia-500</td><td class="px-4 py-3 text-ttg18-mut">same</td><td class="px-4 py-3">--tw-gradient-via: …</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">to-purple-600 to-80%</td><td class="px-4 py-3 text-ttg18-mut">same</td><td class="px-4 py-3">--tw-gradient-to + position</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">bg-linear-to-r/oklch</td><td class="px-4 py-3 text-ttg18-mut">—</td><td class="px-4 py-3">… in oklch …</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">bg-clip-text</td><td class="px-4 py-3 text-ttg18-mut">same</td><td class="px-4 py-3">background-clip: text</td></tr>
          <tr><td class="px-4 py-3 text-indigo-600">text-transparent</td><td class="px-4 py-3 text-ttg18-mut">same</td><td class="px-4 py-3">color: transparent</td></tr>
        </tbody>
      </table>
    </div>
    <div class="mt-6 grid gap-3 rounded-2xl border border-ttg18-line bg-white p-6">
      <p class="text-[11px] font-semibold tracking-[0.1em] text-ttg18-mut uppercase">Live — rendered by Tailwind</p>
      <p class="w-fit bg-linear-to-r from-cyan-400 to-blue-600 bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-linear-to-r from-cyan-400 to-blue-600</p>
      <p class="w-fit bg-linear-to-br from-rose-400 via-fuchsia-500 to-indigo-500 bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-linear-to-br from-rose-400 via-fuchsia-500 to-indigo-500</p>
      <p class="w-fit bg-linear-45 from-emerald-400 to-teal-700 bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-linear-45 from-emerald-400 to-teal-700</p>
      <p class="w-fit bg-radial from-amber-300 to-orange-600 to-70% bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-radial from-amber-300 to-orange-600 to-70%</p>
      <p class="w-fit bg-conic from-sky-500 via-violet-500 to-sky-500 bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-conic from-sky-500 via-violet-500 to-sky-500</p>
      <p class="w-fit bg-linear-to-r/longer from-pink-500 to-pink-500 bg-clip-text text-2xl font-extrabold tracking-tight text-transparent">bg-linear-to-r/longer from-pink-500 to-pink-500</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg18-bg: #f7f8fa;
  --color-ttg18-bg: oklch(0.978 0.004 260);
  --color-ttg18-head: #f1f3f7;
  --color-ttg18-head: oklch(0.962 0.006 260);
  --color-ttg18-ink: #0f172a;
  --color-ttg18-ink: oklch(0.21 0.04 265);
  --color-ttg18-mut: #535d70;
  --color-ttg18-mut: oklch(0.47 0.03 262);
  --color-ttg18-line: #e3e7ee;
  --color-ttg18-line: oklch(0.925 0.008 260);
  --font-ttg18-sans: 'Geist', system-ui, sans-serif;
  --font-ttg18-mono: 'Geist Mono', ui-monospace, monospace;
}

.ttg-18 {
  width: 100%;
  min-height: 100svh;
}
```
