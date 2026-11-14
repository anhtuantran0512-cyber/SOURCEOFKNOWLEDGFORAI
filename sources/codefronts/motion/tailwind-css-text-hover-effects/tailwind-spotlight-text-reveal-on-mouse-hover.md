---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-spotlight-text-reveal-on-mouse-hover/"
title: "Tailwind Spotlight Text Reveal on Mouse Hover"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A night-photography headline where the cursor is a torch: a city photo lives inside the glyphs (bg-clip-text), hidden by a radial mask-image centred at…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spotlight Text Reveal on Mouse Hover
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-spotlight-text-reveal-on-mouse-hover/

A night-photography headline where the cursor is a torch: a city photo lives inside the glyphs (bg-clip-text), hidden by a radial mask-image centred at var(--tth11-x) var(--tth11-y). A 12-line script writes the coordinates; Tailwind does everything else, including the typed radius that grows from 0 to 170px on hover.
## HTML
```html
<section class="tth-11 w-full min-h-svh grid place-items-center bg-tth11-bg bg-[radial-gradient(100%_80%_at_50%_100%,var(--color-tth11-glow),var(--color-tth11-bg)_65%)] px-5 py-14 font-tth11-sans text-tth11-ink" aria-label="Spotlight text reveal demo">
  <div class="flex flex-col items-center gap-[clamp(18px,3.4vw,28px)] text-center">
    <p class="text-xs font-bold uppercase tracking-[0.28em] text-tth11-mut">Night photography walks &mdash; booking winter 2026</p>
    <a id="tth11-top" href="#tth11-top" data-tth11-torch class="group/torch relative inline-block rounded-md px-[0.12em] py-[0.1em] text-[clamp(52px,11.5vw,118px)] font-black leading-[1.02] tracking-[-0.02em] [font-stretch:115%] no-underline [--tth11-r:0px] focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-tth11-acc">
      <span class="block text-tth11-bg [paint-order:stroke_fill] [-webkit-text-stroke:3px_color-mix(in_oklch,var(--color-tth11-ink)_45%,transparent)]">MIDNIGHT<br>ATLAS</span>
      <span aria-hidden="true" style="--tth11-photo:url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1600&auto=format&fit=crop')" class="absolute inset-0 block px-[0.12em] py-[0.1em] bg-[image:linear-gradient(oklch(0.5_0.1_260/0.35),oklch(0.5_0.1_260/0.35)),var(--tth11-photo),linear-gradient(120deg,var(--color-tth11-acc),oklch(0.6_0.18_300))] bg-cover bg-center bg-clip-text text-transparent [mask-image:radial-gradient(circle_var(--tth11-r)_at_var(--tth11-x,50%)_var(--tth11-y,50%),#000_38%,transparent_100%)] [-webkit-mask-image:radial-gradient(circle_var(--tth11-r)_at_var(--tth11-x,50%)_var(--tth11-y,50%),#000_38%,transparent_100%)] transition-[--tth11-r] duration-550 ease-[cubic-bezier(.3,.9,.2,1)] group-hover/torch:[--tth11-r:170px] group-focus-visible/torch:[--tth11-r:60em] pointer-coarse:[--tth11-r:60em] motion-reduce:transition-none">MIDNIGHT<br>ATLAS</span>
    </a>
    <a href="#tth11-top" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-tth11-acc px-5 text-sm font-bold text-tth11-bg no-underline transition-[translate,box-shadow] duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_30px_-8px_var(--color-tth11-acc)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth11-acc">Reserve a walk <span aria-hidden="true">&rarr;</span></a>
    <p class="max-w-[56ch] text-[12.5px] leading-[1.7] text-tth11-mut">Sweep the cursor across the letters &mdash; the photo lives inside the glyphs; a radial <code class="rounded bg-tth11-chip px-1.5 py-px font-tth11-mono text-[0.92em] text-tth11-acc">mask-image</code> at <code class="rounded bg-tth11-chip px-1.5 py-px font-tth11-mono text-[0.92em] text-tth11-acc">var(--tth11-x) var(--tth11-y)</code> is the torch. <kbd class="rounded-[5px] border border-b-2 border-white/15 bg-tth11-chip px-1.5 py-0.5 font-tth11-mono text-[11px]">Tab</kbd> floods it fully lit.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tth11-r {
  syntax: '<length>';
  inherits: true;
  initial-value: 0px;
}

@theme {
  --color-tth11-bg: #0b0e16;
  --color-tth11-bg: oklch(0.15 0.012 265);
  --color-tth11-glow: #161a29;
  --color-tth11-glow: oklch(0.2 0.025 270);
  --color-tth11-chip: #1a1e2a;
  --color-tth11-chip: oklch(0.23 0.015 265);
  --color-tth11-ink: #eaedf3;
  --color-tth11-ink: oklch(0.94 0.01 250);
  --color-tth11-mut: #9aa0ae;
  --color-tth11-mut: oklch(0.71 0.02 255);
  --color-tth11-acc: #f0c14b;
  --color-tth11-acc: oklch(0.83 0.14 85);
  --font-tth11-sans: 'Archivo', system-ui, sans-serif;
  --font-tth11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var wrap = document.querySelector('[data-tth11-torch]');
  if (!wrap) return;
  wrap.addEventListener('pointermove', function (e) {
    var r = wrap.getBoundingClientRect();
    wrap.style.setProperty('--tth11-x', (e.clientX - r.left) + 'px');
    wrap.style.setProperty('--tth11-y', (e.clientY - r.top) + 'px');
  });
  wrap.addEventListener('pointerleave', function () {
    wrap.style.removeProperty('--tth11-x');
    wrap.style.removeProperty('--tth11-y');
  });
})();
```
