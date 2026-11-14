---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/risograph-print-effect-tabs-tailwind-css/"
title: "Risograph Print Effect Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A two-plate riso pull: the chosen tab gets a fluoro-orange plate with a cyan plate misregistered 4px down-left, multiplied together into a third ink where…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Risograph Print Effect Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/risograph-print-effect-tabs-tailwind-css/

A two-plate riso pull: the chosen tab gets a fluoro-orange plate with a cyan plate misregistered 4px down-left, multiplied together into a third ink where they overlap. The port moves the bar onto paper stock — multiply only reads correctly on light paper, which is how a riso actually prints — and adds a halftone texture.
## HTML
```html
<section class="ttb-26 group/tabs grid min-h-svh w-full place-items-center bg-ttb26-paper bg-[radial-gradient(var(--color-ttb26-dot)_1px,transparent_1.2px)] bg-size-[6px_6px] px-5 py-14 font-ttb26-display text-ttb26-ink" aria-label="Risograph print effect tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-8">
    <div class="w-full">
      <div role="radiogroup" aria-label="Issue" class="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <label class="group/tab relative isolate flex min-h-14 cursor-pointer items-center justify-center text-[15px] tracking-[0.06em] uppercase ring-2 ring-ttb26-ink/80 transition-[box-shadow] has-checked:ring-0 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb26-ink"><input class="sr-only" type="radio" name="ttb26" id="ttb26-r1" checked><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb26-orange opacity-0 transition-opacity duration-50 ease-[steps(1,end)] before:absolute before:inset-0 before:translate-x-[-4px] before:translate-y-[4px] before:bg-ttb26-cyan before:mix-blend-multiply group-has-checked/tab:opacity-100 group-has-checked/tab:before:animate-ttb26-shift motion-reduce:group-has-checked/tab:before:animate-none"></span>Issue 01</label>
        <label class="group/tab relative isolate flex min-h-14 cursor-pointer items-center justify-center text-[15px] tracking-[0.06em] uppercase ring-2 ring-ttb26-ink/80 transition-[box-shadow] has-checked:ring-0 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb26-ink"><input class="sr-only" type="radio" name="ttb26" id="ttb26-r2"><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb26-orange opacity-0 transition-opacity duration-50 ease-[steps(1,end)] before:absolute before:inset-0 before:translate-x-[-4px] before:translate-y-[4px] before:bg-ttb26-cyan before:mix-blend-multiply group-has-checked/tab:opacity-100 group-has-checked/tab:before:animate-ttb26-shift motion-reduce:group-has-checked/tab:before:animate-none"></span>Issue 02</label>
        <label class="group/tab relative isolate flex min-h-14 cursor-pointer items-center justify-center text-[15px] tracking-[0.06em] uppercase ring-2 ring-ttb26-ink/80 transition-[box-shadow] has-checked:ring-0 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb26-ink"><input class="sr-only" type="radio" name="ttb26" id="ttb26-r3"><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb26-orange opacity-0 transition-opacity duration-50 ease-[steps(1,end)] before:absolute before:inset-0 before:translate-x-[-4px] before:translate-y-[4px] before:bg-ttb26-cyan before:mix-blend-multiply group-has-checked/tab:opacity-100 group-has-checked/tab:before:animate-ttb26-shift motion-reduce:group-has-checked/tab:before:animate-none"></span>Issue 03</label>
        <label class="group/tab relative isolate flex min-h-14 cursor-pointer items-center justify-center text-[15px] tracking-[0.06em] uppercase ring-2 ring-ttb26-ink/80 transition-[box-shadow] has-checked:ring-0 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb26-ink"><input class="sr-only" type="radio" name="ttb26" id="ttb26-r4"><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb26-orange opacity-0 transition-opacity duration-50 ease-[steps(1,end)] before:absolute before:inset-0 before:translate-x-[-4px] before:translate-y-[4px] before:bg-ttb26-cyan before:mix-blend-multiply group-has-checked/tab:opacity-100 group-has-checked/tab:before:animate-ttb26-shift motion-reduce:group-has-checked/tab:before:animate-none"></span>Issue 04</label>
      </div>
      <div class="pt-6 font-ttb26-mono text-[13px] leading-relaxed">
        <p class="hidden group-has-[#ttb26-r1:checked]/tabs:block"><b>No. 01</b> — Orange & Teal. Forty pages, two drums, one long night.</p>
        <p class="hidden group-has-[#ttb26-r2:checked]/tabs:block"><b>No. 02</b> — The Halftone Issue. Every image screened at 60 lpi.</p>
        <p class="hidden group-has-[#ttb26-r3:checked]/tabs:block"><b>No. 03</b> — Misregistered. A celebration of things slightly off.</p>
        <p class="hidden group-has-[#ttb26-r4:checked]/tabs:block"><b>No. 04</b> — Overprint. What happens where two inks meet.</p>
      </div>
    </div>
    <p aria-hidden="true" class="bg-ttb26-paper px-3.5 py-2 font-ttb26-mono text-[11.5px] ring-1 ring-ttb26-ink/30">isolate · before:mix-blend-multiply · plate shift −7 → −4px</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb26-paper: #f3ece0;
  --color-ttb26-paper: oklch(0.945 0.018 81.3);
  --color-ttb26-dot: #e2d8c6;
  --color-ttb26-dot: oklch(0.885 0.027 82.4);
  --color-ttb26-ink: #1b1b1b;
  --color-ttb26-ink: oklch(0.222 0 0);
  --color-ttb26-orange: #ff6a3d;
  --color-ttb26-orange: oklch(0.704 0.192 37.1);
  --color-ttb26-cyan: #00a5c8;
  --color-ttb26-cyan: oklch(0.668 0.122 220.1);
  --font-ttb26-display: 'Archivo Black', Impact, sans-serif;
  --font-ttb26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttb26-shift: ttb26-shift 0.34s cubic-bezier(0.65, 0, 0.35, 1);

  @keyframes ttb26-shift {
    0% {
      translate: 0 0;
      opacity: 0;
    }

    55% {
      translate: -7px 7px;
      opacity: 0.92;
    }

    100% {
      translate: -4px 4px;
      opacity: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-26 {
  width: 100%;
  min-height: 100svh;
}
```
