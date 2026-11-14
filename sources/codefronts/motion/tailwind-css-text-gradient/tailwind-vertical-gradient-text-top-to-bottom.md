---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-vertical-gradient-text-top-to-bottom/"
title: "Tailwind Vertical Gradient Text (Top to Bottom)"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "Vertical gradients in two flavours: a dark rail of [writing-mode:vertical-rl] labels and two display words that fade top-to-bottom and bottom-to-top with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Gradient Text (Top to Bottom)
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-vertical-gradient-text-top-to-bottom/

Vertical gradients in two flavours: a dark rail of [writing-mode:vertical-rl] labels and two display words that fade top-to-bottom and bottom-to-top with bg-linear-to-b / bg-linear-to-t. The fade uses the opacity modifier on the end stop (to-ttg13-amber/20) so the hue survives as it dissolves.
## HTML
```html
<section class="ttg-13 w-full min-h-svh grid grid-cols-[96px_1fr] bg-ttg13-bg font-ttg13-sans text-ttg13-ink max-sm:grid-cols-1" aria-label="Vertical gradient text demo">
  <aside class="flex items-center justify-center gap-6 bg-ttg13-rail py-8 max-sm:py-5 sm:flex-col">
    <h2 class="bg-linear-to-b from-ttg13-blue to-ttg13-blue2 bg-clip-text text-xl font-black tracking-[0.12em] text-transparent sm:rotate-180 sm:[writing-mode:vertical-rl] max-sm:bg-linear-to-r">BUILD</h2>
    <h2 class="bg-linear-to-b from-ttg13-violet to-ttg13-pink bg-clip-text text-xl font-black tracking-[0.12em] text-transparent sm:rotate-180 sm:[writing-mode:vertical-rl] max-sm:bg-linear-to-r">SHIP</h2>
    <h2 class="bg-linear-to-b from-ttg13-sky to-ttg13-sky2 bg-clip-text text-xl font-black tracking-[0.12em] text-transparent sm:rotate-180 sm:[writing-mode:vertical-rl] max-sm:bg-linear-to-r">GROW</h2>
  </aside>
  <main class="flex flex-col justify-center px-10 py-14 max-sm:px-6">
    <p class="font-ttg13-mono text-xs tracking-[0.14em] text-ttg13-mut uppercase">Vertical gradient text</p>
    <p class="mt-4 max-w-md text-[15.5px]/[1.7] text-ttg13-mut text-pretty">A top-to-bottom ramp reinforces hierarchy: the vivid top catches the eye, the fade draws it down into the content.</p>
    <div class="mt-10 grid gap-2">
      <p class="w-fit bg-linear-to-b from-ttg13-amber to-ttg13-amber/20 bg-clip-text pb-[0.1em] text-[clamp(3rem,10vw,6rem)] leading-[0.92] font-black tracking-[-0.045em] text-transparent">Framework</p>
      <p class="w-fit bg-linear-to-t from-ttg13-violet to-ttg13-violet/25 bg-clip-text pb-[0.1em] text-[clamp(3rem,10vw,6rem)] leading-[0.92] font-black tracking-[-0.045em] text-transparent">Platform</p>
    </div>
    <div class="mt-8 flex flex-wrap gap-2 font-ttg13-mono text-[12px]">
      <code class="rounded-md border border-ttg13-line bg-white px-2.5 py-1.5">bg-linear-to-b from-amber to-amber/20</code>
      <code class="rounded-md border border-ttg13-line bg-white px-2.5 py-1.5">bg-linear-to-t from-violet to-violet/25</code>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg13-bg: #f2f4f8;
  --color-ttg13-bg: oklch(0.966 0.007 260);
  --color-ttg13-rail: #0e1424;
  --color-ttg13-rail: oklch(0.19 0.03 265);
  --color-ttg13-ink: #0f172a;
  --color-ttg13-ink: oklch(0.21 0.04 265);
  --color-ttg13-mut: #535d70;
  --color-ttg13-mut: oklch(0.47 0.03 262);
  --color-ttg13-line: #dfe3eb;
  --color-ttg13-line: oklch(0.91 0.01 262);
  --color-ttg13-blue: #6ea8ff;
  --color-ttg13-blue: oklch(0.74 0.13 258);
  --color-ttg13-blue2: #2f5fe0;
  --color-ttg13-blue2: oklch(0.54 0.2 265);
  --color-ttg13-violet: #8b3df0;
  --color-ttg13-violet: oklch(0.56 0.25 298);
  --color-ttg13-pink: #f46cb5;
  --color-ttg13-pink: oklch(0.72 0.17 350);
  --color-ttg13-sky: #5fd0ff;
  --color-ttg13-sky: oklch(0.82 0.12 225);
  --color-ttg13-sky2: #0b84c6;
  --color-ttg13-sky2: oklch(0.6 0.14 240);
  --color-ttg13-amber: #f29a0b;
  --color-ttg13-amber: oklch(0.76 0.17 65);
  --font-ttg13-sans: 'Archivo', system-ui, sans-serif;
  --font-ttg13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttg-13 {
  width: 100%;
  min-height: 100svh;
}
```
