---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-fallback-with-supports/"
title: "Tailwind Gradient Text Fallback with @supports"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A three-layer progressive-enhancement reference in pure utilities."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text Fallback with @supports
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-fallback-with-supports/

A three-layer progressive-enhancement reference in pure utilities. Layer 1 is a solid colour every browser renders; layer 2 adds the gradient only inside supports-[background-clip:text]:; layer 3 shows the complete pattern with a not-supports-[…]: underline as a designed fallback &mdash; so no engine ever shows invisible text.
## HTML
```html
<section class="ttg-17 w-full min-h-svh grid place-items-start justify-center bg-ttg17-bg px-5 py-14 font-ttg17-sans text-ttg17-ink" aria-labelledby="ttg17-title">
  <div class="w-full max-w-2xl">
    <h2 id="ttg17-title" class="text-[28px] font-extrabold tracking-[-0.025em]">Gradient text that never disappears</h2>
    <p class="mt-2 max-w-xl text-[15px]/[1.7] text-ttg17-mut text-pretty">A layered fallback: modern engines get the gradient, everything else gets readable solid colour — no JavaScript.</p>
    <ol class="mt-8 grid gap-4">
      <li class="grid gap-4 rounded-2xl border border-ttg17-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:grid-cols-[auto_1fr]">
        <span class="grid size-9 place-items-center rounded-lg bg-ttg17-l1 font-ttg17-mono text-sm font-medium text-ttg17-l1-ink">1</span>
        <div>
          <h3 class="font-semibold">Solid colour first</h3>
          <p class="mt-1 text-sm/[1.6] text-ttg17-mut">Every browser renders a plain <code class="font-ttg17-mono text-[12.5px] text-ttg17-b">text-*</code> colour.</p>
          <p class="mt-3 text-[34px] leading-tight font-extrabold tracking-tight text-ttg17-a">Solid fallback</p>
          <pre class="mt-3 overflow-x-auto rounded-lg bg-ttg17-code px-3.5 py-2.5 font-ttg17-mono text-[12px] text-ttg17-code-ink">text-ttg17-a</pre>
        </div>
      </li>
      <li class="grid gap-4 rounded-2xl border border-ttg17-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:grid-cols-[auto_1fr]">
        <span class="grid size-9 place-items-center rounded-lg bg-ttg17-l2 font-ttg17-mono text-sm font-medium text-ttg17-l2-ink">2</span>
        <div>
          <h3 class="font-semibold">Guard the gradient</h3>
          <p class="mt-1 text-sm/[1.6] text-ttg17-mut">Clip and transparency only apply inside <code class="font-ttg17-mono text-[12.5px] text-ttg17-b">supports-[background-clip:text]:</code>.</p>
          <p class="mt-3 w-fit text-[34px] leading-tight font-extrabold tracking-tight text-ttg17-a supports-[background-clip:text]:bg-linear-to-r supports-[background-clip:text]:from-ttg17-a supports-[background-clip:text]:to-ttg17-b supports-[background-clip:text]:bg-clip-text supports-[background-clip:text]:text-transparent">Guarded gradient</p>
          <pre class="mt-3 overflow-x-auto rounded-lg bg-ttg17-code px-3.5 py-2.5 font-ttg17-mono text-[12px] text-ttg17-code-ink">supports-[background-clip:text]:bg-clip-text
supports-[background-clip:text]:text-transparent</pre>
        </div>
      </li>
      <li class="grid gap-4 rounded-2xl border border-ttg17-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:grid-cols-[auto_1fr]">
        <span class="grid size-9 place-items-center rounded-lg bg-ttg17-l3 font-ttg17-mono text-sm font-medium text-ttg17-l3-ink">3</span>
        <div>
          <h3 class="font-semibold">Design the fallback</h3>
          <p class="mt-1 text-sm/[1.6] text-ttg17-mut">Unsupported engines get a deliberate underline accent via <code class="font-ttg17-mono text-[12.5px] text-ttg17-b">not-supports-[…]:</code>.</p>
          <p class="mt-3 w-fit text-[34px] leading-tight font-extrabold tracking-tight text-ttg17-a decoration-ttg17-b decoration-4 underline-offset-8 not-supports-[background-clip:text]:underline supports-[background-clip:text]:bg-linear-to-r supports-[background-clip:text]:from-ttg17-a supports-[background-clip:text]:to-ttg17-b supports-[background-clip:text]:bg-clip-text supports-[background-clip:text]:text-transparent">Final output</p>
          <pre class="mt-3 overflow-x-auto rounded-lg bg-ttg17-code px-3.5 py-2.5 font-ttg17-mono text-[12px] text-ttg17-code-ink">not-supports-[background-clip:text]:underline</pre>
        </div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg17-bg: #f6f8fb;
  --color-ttg17-bg: oklch(0.977 0.005 255);
  --color-ttg17-ink: #0f172a;
  --color-ttg17-ink: oklch(0.21 0.04 265);
  --color-ttg17-mut: #525c6e;
  --color-ttg17-mut: oklch(0.47 0.03 260);
  --color-ttg17-line: #e2e7ef;
  --color-ttg17-line: oklch(0.925 0.01 260);
  --color-ttg17-code: #0f172a;
  --color-ttg17-code: oklch(0.21 0.04 265);
  --color-ttg17-code-ink: #cdd6f4;
  --color-ttg17-code-ink: oklch(0.88 0.04 275);
  --color-ttg17-a: #2257e0;
  --color-ttg17-a: oklch(0.52 0.21 264);
  --color-ttg17-b: #d42b84;
  --color-ttg17-b: oklch(0.58 0.22 355);
  --color-ttg17-l1: #fef3c7;
  --color-ttg17-l1: oklch(0.96 0.06 95);
  --color-ttg17-l1-ink: #854d0e;
  --color-ttg17-l1-ink: oklch(0.47 0.11 65);
  --color-ttg17-l2: #dbeafe;
  --color-ttg17-l2: oklch(0.93 0.04 255);
  --color-ttg17-l2-ink: #1e40af;
  --color-ttg17-l2-ink: oklch(0.42 0.18 265);
  --color-ttg17-l3: #fce7f3;
  --color-ttg17-l3: oklch(0.94 0.035 350);
  --color-ttg17-l3-ink: #9d174d;
  --color-ttg17-l3-ink: oklch(0.45 0.17 0);
  --font-ttg17-sans: 'Geist', system-ui, sans-serif;
  --font-ttg17-mono: 'Geist Mono', ui-monospace, monospace;
}

.ttg-17 {
  width: 100%;
  min-height: 100svh;
}
```
