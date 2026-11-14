---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-risograph-print-misregistration-texture/"
title: "Tailwind Risograph Print Misregistration Texture"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Risograph's charm is its failure mode: a paper feed that never lines up, so every colour lands a few millimetres off and the overlaps print as a third ink."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Risograph Print Misregistration Texture
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-risograph-print-misregistration-texture/

Risograph's charm is its failure mode: a paper feed that never lines up, so every colour lands a few millimetres off and the overlaps print as a third ink. Two offset ink layers, misregistered display type built from attr() pseudo-elements, and paper grain on top — four pixels of error, deliberately.
## HTML
```html
<section class="gtw-17 relative block w-full min-h-svh bg-gtw17-paper text-gtw17-ink" aria-labelledby="gtw-17-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-17-theme" class="gtw-17-theme peer sr-only">
    <label for="gtw-17-theme" class="grid place-items-center w-11 h-11 rounded-none border-2 border-gtw17-ink bg-gtw17-paper text-gtw17-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw17-inkb peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(2rem,6vw,3.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(1.8rem,4.5vw,2.8rem)]">
    <article class="relative isolate overflow-hidden grid items-end min-h-[min(80svh,44rem)] border-2 border-gtw17-ink bg-gtw17-paper">
      <span aria-hidden="true" class="absolute -inset-[8%] pointer-events-none mix-blend-multiply bg-no-repeat opacity-[0.92] translate-x-[calc(var(--gtw17-shift)*-1)] translate-y-[calc(var(--gtw17-shift)*0.6)] bg-[radial-gradient(38%_30%_at_74%_16%,var(--color-gtw17-inka)_0_62%,transparent_64%),radial-gradient(26%_22%_at_18%_76%,var(--color-gtw17-inka)_0_60%,transparent_62%),linear-gradient(178deg,transparent_0_72%,var(--color-gtw17-inka)_72%_80%,transparent_80%)]"></span>
      <span aria-hidden="true" class="absolute -inset-[8%] pointer-events-none mix-blend-multiply bg-no-repeat opacity-[0.88] rotate-[0.3deg] translate-x-[var(--gtw17-shift)] translate-y-[calc(var(--gtw17-shift)*-0.5)] bg-[radial-gradient(34%_27%_at_66%_22%,var(--color-gtw17-inkb)_0_62%,transparent_64%),radial-gradient(30%_24%_at_26%_82%,var(--color-gtw17-inkb)_0_60%,transparent_62%),linear-gradient(178deg,transparent_0_74%,var(--color-gtw17-inkb)_74%_81%,transparent_81%)]"></span>
      <span aria-hidden="true" class="absolute inset-0 pointer-events-none bg-[image:var(--gtw17-noise)] opacity-[var(--gtw17-grain)] mix-blend-multiply"></span>

      <div class="relative z-[3] grid gap-[0.9rem] max-w-[46rem] p-[clamp(1.5rem,5vw,3.2rem)]">
        <p class="m-0 font-gtw17-mono text-[0.74rem] leading-none tracking-[0.2em] uppercase">Bracken Press · Open studio</p>
        <h1 id="gtw-17-title" class="m-0 grid gap-[0.1rem] font-gtw17-display text-[clamp(2.4rem,9vw,5.6rem)] font-normal leading-[0.9] tracking-[-0.03em] uppercase">
          <span data-gtw-17-text="Two Inks" class="relative isolate block text-gtw17-ink before:content-[attr(data-gtw-17-text)] before:absolute before:top-0 before:left-0 before:pointer-events-none before:mix-blend-multiply before:text-gtw17-inka before:translate-x-[calc(var(--gtw17-shift)*-0.7)] before:translate-y-[calc(var(--gtw17-shift)*0.35)] after:content-[attr(data-gtw-17-text)] after:absolute after:top-0 after:left-0 after:pointer-events-none after:mix-blend-multiply after:text-gtw17-inkb after:translate-x-[calc(var(--gtw17-shift)*0.7)] after:translate-y-[calc(var(--gtw17-shift)*-0.35)]">Two Inks</span>
          <span data-gtw-17-text="One Pass" class="relative isolate block text-gtw17-ink before:content-[attr(data-gtw-17-text)] before:absolute before:top-0 before:left-0 before:pointer-events-none before:mix-blend-multiply before:text-gtw17-inka before:translate-x-[calc(var(--gtw17-shift)*-0.7)] before:translate-y-[calc(var(--gtw17-shift)*0.35)] after:content-[attr(data-gtw-17-text)] after:absolute after:top-0 after:left-0 after:pointer-events-none after:mix-blend-multiply after:text-gtw17-inkb after:translate-x-[calc(var(--gtw17-shift)*0.7)] after:translate-y-[calc(var(--gtw17-shift)*-0.35)]">One Pass</span>
          <span data-gtw-17-text="Slightly Wrong" class="relative isolate block text-gtw17-ink before:content-[attr(data-gtw-17-text)] before:absolute before:top-0 before:left-0 before:pointer-events-none before:mix-blend-multiply before:text-gtw17-inka before:translate-x-[calc(var(--gtw17-shift)*-0.7)] before:translate-y-[calc(var(--gtw17-shift)*0.35)] after:content-[attr(data-gtw-17-text)] after:absolute after:top-0 after:left-0 after:pointer-events-none after:mix-blend-multiply after:text-gtw17-inkb after:translate-x-[calc(var(--gtw17-shift)*0.7)] after:translate-y-[calc(var(--gtw17-shift)*-0.35)]">Slightly Wrong</span>
        </h1>
        <p class="m-0 max-w-[32rem] text-[clamp(0.97rem,2vw,1.12rem)] text-pretty">Fourteen printers, one drum, and a paper feed that has never once lined up. Two nights of riso, screen and letterpress in the Sackville Yard workshops.</p>
        <dl class="flex flex-wrap gap-y-2 gap-x-[1.8rem] mt-[0.4rem] mb-0 pt-[0.9rem] border-t-2 border-gtw17-ink">
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw17-mono text-[0.66rem] leading-none tracking-[0.14em] uppercase text-gtw17-mut">When</dt><dd class="m-0 font-gtw17-mono text-[0.98rem] font-medium leading-tight">19–20 June, 6pm</dd></div>
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw17-mono text-[0.66rem] leading-none tracking-[0.14em] uppercase text-gtw17-mut">Where</dt><dd class="m-0 font-gtw17-mono text-[0.98rem] font-medium leading-tight">Unit 7, Sackville Yard</dd></div>
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw17-mono text-[0.66rem] leading-none tracking-[0.14em] uppercase text-gtw17-mut">Entry</dt><dd class="m-0 font-gtw17-mono text-[0.98rem] font-medium leading-tight">Free, bring paper</dd></div>
        </dl>
        <a href="#gtw-17-title" class="justify-self-start inline-flex items-center min-h-[50px] mt-[0.4rem] px-6 border-2 border-gtw17-ink bg-gtw17-inka text-[#14110c] no-underline font-gtw17-display text-[0.9rem] leading-none tracking-[0.06em] uppercase shadow-[var(--gtw17-shift)_var(--gtw17-shift)_0_var(--color-gtw17-inkb)] transition-[translate,box-shadow] duration-150 hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0_var(--color-gtw17-inkb)] focus-visible:outline-2 focus-visible:outline-gtw17-ink focus-visible:outline-offset-[3px] motion-reduce:transition-none">Reserve a press slot</a>
      </div>
    </article>

    <section class="grid gap-[0.8rem] p-[clamp(1.2rem,3vw,1.8rem)] border-2 border-gtw17-ink" aria-labelledby="gtw-17-h-notes">
      <h2 id="gtw-17-h-notes" class="m-0 font-gtw17-display text-[clamp(1.1rem,2.8vw,1.5rem)] font-normal leading-[1.15] tracking-[-0.01em] uppercase">How the misregistration is built</h2>
      <ol class="m-0 pl-[1.4rem] grid gap-2 text-gtw17-mut text-[0.92rem]">
        <li><b class="font-semibold text-gtw17-ink">Duplicate the shape set.</b> Two absolutely positioned layers, identical geometry.</li>
        <li><b class="font-semibold text-gtw17-ink">Offset each by a few pixels.</b> Different directions. 2–5px reads as print; 8px reads as a bug.</li>
        <li><b class="font-semibold text-gtw17-ink">Blend both in multiply.</b> Overlaps darken into a third colour, exactly like overprinted ink.</li>
        <li><b class="font-semibold text-gtw17-ink">Put the grain on top.</b> It is the paper showing through, not dust on the ink.</li>
      </ol>
    </section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw17-paper: #f6f1e4;
  --color-gtw17-paper: oklch(0.95 0.02 90);
  --color-gtw17-inka: #ff48a0;
  --color-gtw17-inka: oklch(0.7 0.28 5);
  --color-gtw17-inkb: #1f4bd8;
  --color-gtw17-inkb: oklch(0.48 0.24 265);
  --color-gtw17-ink: #14110c;
  --color-gtw17-ink: oklch(0.2 0.01 85);
  --color-gtw17-mut: #5c5445;
  --color-gtw17-mut: oklch(0.44 0.02 85);
  --font-gtw17-display: 'Archivo Black', 'Anton', 'Helvetica Neue', Impact, sans-serif;
  --font-gtw17-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-17 {
  width: 100%;
  min-height: 100svh;
  --gtw17-shift: 4px;
  --gtw17-grain: 0.09;
  --gtw17-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='190' height='190'%3E%3Cfilter id='gtw17n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='190' height='190' filter='url(%23gtw17n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-17:has(.gtw-17-theme:checked) {
  --color-gtw17-paper: #14120d;
  --color-gtw17-paper: oklch(0.18 0.01 90);
  --color-gtw17-ink: #f5efe1;
  --color-gtw17-ink: oklch(0.94 0.02 88);
  --color-gtw17-mut: #a49a86;
  --color-gtw17-mut: oklch(0.7 0.02 85);
  --color-gtw17-inka: #ff5fae;
  --color-gtw17-inka: oklch(0.74 0.26 3);
  --color-gtw17-inkb: #4d79ff;
  --color-gtw17-inkb: oklch(0.62 0.22 268);
  --gtw17-grain: 0.12;
}

@media (prefers-color-scheme: dark) {
  .gtw-17 {
    --color-gtw17-paper: #14120d;
    --color-gtw17-paper: oklch(0.18 0.01 90);
    --color-gtw17-ink: #f5efe1;
    --color-gtw17-ink: oklch(0.94 0.02 88);
    --color-gtw17-mut: #a49a86;
    --color-gtw17-mut: oklch(0.7 0.02 85);
    --color-gtw17-inka: #ff5fae;
    --color-gtw17-inka: oklch(0.74 0.26 3);
    --color-gtw17-inkb: #4d79ff;
    --color-gtw17-inkb: oklch(0.62 0.22 268);
    --gtw17-grain: 0.12;
  }

  .gtw-17:has(.gtw-17-theme:checked) {
    --color-gtw17-paper: #f6f1e4;
    --color-gtw17-paper: oklch(0.95 0.02 90);
    --color-gtw17-ink: #14110c;
    --color-gtw17-ink: oklch(0.2 0.01 85);
    --color-gtw17-mut: #5c5445;
    --color-gtw17-mut: oklch(0.44 0.02 85);
    --color-gtw17-inka: #ff48a0;
    --color-gtw17-inka: oklch(0.7 0.28 5);
    --color-gtw17-inkb: #1f4bd8;
    --color-gtw17-inkb: oklch(0.48 0.24 265);
    --gtw17-grain: 0.09;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-17:has(.gtw-17-theme:checked) {
    --color-gtw17-paper: #14120d;
    --color-gtw17-paper: oklch(0.18 0.01 90);
    --color-gtw17-ink: #f5efe1;
    --color-gtw17-ink: oklch(0.94 0.02 88);
    --color-gtw17-mut: #a49a86;
    --color-gtw17-mut: oklch(0.7 0.02 85);
    --color-gtw17-inka: #ff5fae;
    --color-gtw17-inka: oklch(0.74 0.26 3);
    --color-gtw17-inkb: #4d79ff;
    --color-gtw17-inkb: oklch(0.62 0.22 268);
    --gtw17-grain: 0.12;
  }
}
```
