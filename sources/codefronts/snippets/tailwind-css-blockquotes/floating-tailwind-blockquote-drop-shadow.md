---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/floating-tailwind-blockquote-drop-shadow/"
title: "Floating Tailwind Blockquote with Drop Shadow"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A floating quote card on a five-layer, hue-tinted shadow ramp, with an elevation ruler showing e1–e3."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Tailwind Blockquote with Drop Shadow
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/floating-tailwind-blockquote-drop-shadow/

A floating quote card on a five-layer, hue-tinted shadow ramp, with an elevation ruler showing e1–e3. The port promotes every shadow to a --shadow-tbq17-* theme token, so shadow-tbq17-rest and shadow-tbq17-e3 are real utilities, and keeps the performant hover: the heavier shadow lives on an after: layer whose opacity animates.
## HTML
```html
<section class="tbq-17 w-full min-h-svh grid place-items-center bg-linear-160 from-tbq17-top to-tbq17-bg px-5 py-16 font-tbq17-sans text-tbq17-ink" aria-label="Floating blockquote with layered drop shadow demo">
  <div class="grid w-full justify-items-center gap-9">
    <div class="flex flex-wrap items-center justify-center gap-[clamp(28px,4vw,52px)]">
      <figure class="group relative w-[min(100%,440px)] rounded-[20px] bg-tbq17-card px-8 pt-9 pb-6.5 shadow-tbq17-rest transition-[translate] duration-300 ease-[cubic-bezier(0.2,0.7,0.2,1)] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:opacity-0 after:shadow-tbq17-lift after:transition-opacity after:duration-300 hover:-translate-y-1.5 hover:after:opacity-100 motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute -top-6 left-6 grid size-12 place-items-center rounded-[14px] bg-tbq17-acc pt-4 font-tbq17-serif text-[40px] leading-none text-white shadow-tbq17-tile transition-transform duration-300 group-hover:-rotate-6 motion-reduce:transition-none">“</span>
        <blockquote>
          <p class="mt-2 text-[16.5px] leading-[1.66] text-pretty">Depth is information. A shadow tells the eye what is interactive, what is modal, and what is furniture — before a single word is read.</p>
        </blockquote>
        <figcaption class="mt-4 text-[12.5px] text-tbq17-mut"><strong class="font-semibold text-tbq17-ink">Field Guide to Interface Light</strong> · ch. 3, Elevation</figcaption>
      </figure>
      <div aria-hidden="true" class="flex flex-col gap-4.5">
        <div class="grid h-13 w-40 place-items-center rounded-xl bg-tbq17-card font-tbq17-mono text-[10.5px] text-tbq17-mut shadow-tbq17-e1">e1 · resting</div>
        <div class="grid h-13 w-40 place-items-center rounded-xl bg-tbq17-card font-tbq17-mono text-[10.5px] text-tbq17-mut shadow-tbq17-e2">e2 · raised</div>
        <div class="grid h-13 w-40 place-items-center rounded-xl bg-tbq17-card font-tbq17-mono text-[10.5px] text-tbq17-mut shadow-tbq17-e3">e3 · floating</div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/9 bg-white px-3.5 py-2 font-tbq17-mono text-[11.5px] text-tbq17-mut">--shadow-tbq17-* tokens · after: opacity cross-fade · hue-tinted</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq17-bg: #edf0f6;
  --color-tbq17-bg: oklch(0.955 0.008 255);
  --color-tbq17-top: #f2f5f9;
  --color-tbq17-top: oklch(0.97 0.006 250);
  --color-tbq17-card: #ffffff;
  --color-tbq17-card: oklch(1 0 0);
  --color-tbq17-ink: #1e242e;
  --color-tbq17-ink: oklch(0.26 0.02 260);
  --color-tbq17-mut: #5a616c;
  --color-tbq17-mut: oklch(0.49 0.02 260);
  --color-tbq17-acc: #3a61c4;
  --color-tbq17-acc: oklch(0.52 0.16 265);
  --font-tbq17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq17-serif: 'Newsreader', Georgia, serif;
  --font-tbq17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tbq17-rest: 0 1px 1px oklch(0.2 0.02 260 / 0.05), 0 2px 2px oklch(0.2 0.02 260 / 0.05), 0 4px 4px oklch(0.2 0.02 260 / 0.06), 0 8px 8px oklch(0.2 0.02 260 / 0.06), 0 16px 24px oklch(0.2 0.02 260 / 0.08);
  --shadow-tbq17-lift: 0 2px 2px oklch(0.2 0.02 260 / 0.06), 0 4px 4px oklch(0.2 0.02 260 / 0.06), 0 8px 8px oklch(0.2 0.02 260 / 0.07), 0 16px 16px oklch(0.2 0.02 260 / 0.07), 0 32px 44px oklch(0.2 0.02 260 / 0.12);
  --shadow-tbq17-e1: 0 1px 1px oklch(0.2 0.02 260 / 0.06), 0 2px 3px oklch(0.2 0.02 260 / 0.07);
  --shadow-tbq17-e2: 0 1px 1px oklch(0.2 0.02 260 / 0.05), 0 3px 4px oklch(0.2 0.02 260 / 0.06), 0 8px 12px oklch(0.2 0.02 260 / 0.08);
  --shadow-tbq17-e3: 0 1px 1px oklch(0.2 0.02 260 / 0.05), 0 4px 4px oklch(0.2 0.02 260 / 0.06), 0 8px 10px oklch(0.2 0.02 260 / 0.07), 0 20px 32px oklch(0.2 0.02 260 / 0.12);
  --shadow-tbq17-tile: 0 2px 3px oklch(0.2 0.02 260 / 0.15), 0 8px 16px oklch(0.2 0.02 260 / 0.2);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-17 {
  width: 100%;
  min-height: 100svh;
}
```
