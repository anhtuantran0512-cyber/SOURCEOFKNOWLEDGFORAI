---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/thick-vertical-accent-rail-tailwind-blockquote/"
title: "Thick Vertical Accent Rail Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A 14px gradient rail in its own grid column, carrying vertical label text ([writing-mode:vertical-rl] rotate-180), beside a large quote with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Thick Vertical Accent Rail Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/thick-vertical-accent-rail-tailwind-blockquote/

A 14px gradient rail in its own grid column, carrying vertical label text ([writing-mode:vertical-rl] rotate-180), beside a large quote with a gradient-clipped author name. The port makes the rail draw in on load with starting:scale-y-0 and fixes the rail label, which was near-invisible dark text on the orange-to-magenta gradient.
## HTML
```html
<section class="tbq-13 w-full min-h-svh grid place-items-center bg-linear-200 from-tbq13-top to-tbq13-bg to-60% px-5 py-14 font-tbq13-sans text-tbq13-ink" aria-label="Thick vertical accent rail blockquote demo">
  <div class="grid w-full justify-items-center gap-9">
    <figure class="grid w-full max-w-[620px] grid-cols-[14px_1fr] gap-6.5">
      <div aria-hidden="true" class="grid origin-top place-items-end justify-center bg-linear-to-b from-tbq13-a via-tbq13-b via-55% to-tbq13-c py-3.5 transition-transform duration-700 ease-[cubic-bezier(0.2,0.7,0.2,1)] starting:scale-y-0 motion-reduce:transition-none"><span class="rotate-180 font-tbq13-mono text-[10px] font-bold tracking-[0.22em] whitespace-nowrap text-tbq13-railink [writing-mode:vertical-rl]">FIELD NOTES — VOL 7</span></div>
      <div class="transition-opacity delay-300 duration-700 starting:opacity-0 motion-reduce:transition-none">
        <blockquote>
          <p class="text-[clamp(21px,2.9vw,30px)] leading-[1.38] font-semibold tracking-[-0.02em] text-pretty">We didn't set out to build infrastructure. We set out to answer one support ticket properly, and infrastructure is what answering it properly turned out to require.</p>
        </blockquote>
        <figcaption class="mt-5 text-sm text-tbq13-mut"><strong class="bg-linear-to-r from-tbq13-a to-tbq13-b bg-clip-text font-semibold text-transparent">Yusuf Adeyemi</strong> · Founding Engineer, Cachet</figcaption>
      </div>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/14 px-3.5 py-2 font-tbq13-mono text-[11.5px] text-tbq13-mut">grid-cols-[14px_1fr] · [writing-mode:vertical-rl] · starting:scale-y-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq13-bg: #12161d;
  --color-tbq13-bg: oklch(0.2 0.015 260);
  --color-tbq13-top: #1b1f29;
  --color-tbq13-top: oklch(0.24 0.02 270);
  --color-tbq13-ink: #eef2f7;
  --color-tbq13-ink: oklch(0.96 0.008 250);
  --color-tbq13-mut: #a9b2be;
  --color-tbq13-mut: oklch(0.76 0.02 255);
  --color-tbq13-a: #e7b643;
  --color-tbq13-a: oklch(0.8 0.14 85);
  --color-tbq13-b: #f35c49;
  --color-tbq13-b: oklch(0.67 0.19 30);
  --color-tbq13-c: #be47b8;
  --color-tbq13-c: oklch(0.6 0.2 330);
  --color-tbq13-railink: #050911;
  --color-tbq13-railink: oklch(0.14 0.02 260);
  --font-tbq13-sans: 'Geist', system-ui, sans-serif;
  --font-tbq13-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-13 {
  width: 100%;
  min-height: 100svh;
}
```
