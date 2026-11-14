---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-divider-full-width-responsive-mobile-fix/"
title: "Tailwind Wave Divider Full Width Responsive Mobile Fix"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "The bug-fix demo: broken and fixed dividers side by side, so you can see exactly what causes the white gap, the hairline seam and the smeared curve on narrow…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Wave Divider Full Width Responsive Mobile Fix
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-divider-full-width-responsive-mobile-fix/

The bug-fix demo: broken and fixed dividers side by side, so you can see exactly what causes the white gap, the hairline seam and the smeared curve on narrow screens &mdash; plus a live squeeze slider that reproduces the failure without resizing the browser, and a breakpoint mask swap.
## HTML
```html
<section class="twd-08 w-full min-h-svh bg-twd08-paper text-twd08-ink font-twd08-sans px-5 pt-7 pb-9">

  <!-- Broken vs fixed, with a viewport squeeze slider -->
  <div class="max-w-[720px] mx-auto mb-6">
    <label for="twd08-range" class="block text-[13px] font-bold mb-2">Simulated viewport width: <output id="twd08-out" class="font-twd08-mono font-semibold">100%</output></label>
    <input id="twd08-range" type="range" min="32" max="100" value="100" step="1" aria-describedby="twd08-hint" class="w-full accent-twd08-brand focus-visible:outline-3 focus-visible:outline-twd08-brand focus-visible:outline-offset-4">
    <p id="twd08-hint" class="text-[12.5px] text-twd08-mute mt-2">Drag to squeeze both panes. The left pane shows the classic bugs; the right pane is the fixed recipe.</p>
  </div>

  <div id="twd08-panes" class="grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-5 max-w-[920px] mx-auto">
    <div class="min-w-0">
      <p class="inline-block text-[11px] font-extrabold tracking-[0.12em] uppercase text-white bg-twd08-bad px-2.5 py-1 rounded-full mb-2.5">Broken</p>
      <div class="border border-twd08-edge rounded-xl overflow-hidden">
        <div class="relative bg-twd08-ink text-white text-xs tracking-[0.1em] uppercase px-3 pt-8 pb-14 text-center">
          <span>Hero</span>
          <svg class="absolute left-0 bottom-0 w-full h-[46px] text-twd08-next [&_path]:fill-current" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,60 C300,120 620,0 940,54 C1160,90 1300,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        </div>
        <div class="bg-twd08-next text-twd08-ink text-xs tracking-[0.1em] uppercase px-3 py-5 text-center"><span>Next section</span></div>
      </div>
      <ul class="list-none mt-2.5 flex flex-col gap-1.5 font-twd08-mono text-[12.5px] text-twd08-mute">
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-bad">inline SVG baseline gap</li>
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-bad">seam at fractional DPR</li>
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-bad">curve smears when narrow</li>
      </ul>
    </div>
    <div class="min-w-0">
      <p class="inline-block text-[11px] font-extrabold tracking-[0.12em] uppercase text-white bg-twd08-good px-2.5 py-1 rounded-full mb-2.5">Fixed</p>
      <div class="border border-twd08-edge rounded-xl overflow-hidden overflow-x-clip">
        <div class="relative bg-twd08-ink text-white text-xs tracking-[0.1em] uppercase px-3 pt-8 pb-14 text-center">
          <span>Hero</span>
          <svg class="absolute left-1/2 -translate-x-1/2 -bottom-px block w-full min-w-[520px] h-[clamp(38px,6vw,52px)] text-twd08-next [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,60 C300,120 620,0 940,54 C1160,90 1300,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        </div>
        <div class="bg-twd08-next text-twd08-ink text-xs tracking-[0.1em] uppercase px-3 py-5 text-center"><span>Next section</span></div>
      </div>
      <ul class="list-none mt-2.5 flex flex-col gap-1.5 font-twd08-mono text-[12.5px] text-twd08-mute">
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-good">block</li>
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-good">-bottom-px overlap</li>
        <li class="before:content-['›'] before:mr-1.5 before:text-twd08-good">min-w keeps the ratio</li>
      </ul>
    </div>
  </div>

  <!-- Breakpoint mask swap -->
  <div class="max-w-[920px] mx-auto mt-10 rounded-xl overflow-hidden border border-twd08-edge">
    <div class="bg-twd08-violet text-white px-6 pt-13 pb-8 text-center">
      <h2 class="text-[clamp(23px,3.6vw,34px)] font-semibold mb-2">Different wave per breakpoint</h2>
      <p class="text-[15px] text-twd08-onviolet max-w-[50ch] mx-auto">Below <code class="font-twd08-mono text-[13.5px]">md</code> a taller, shorter-wavelength mask takes over so the curve stays legible.</p>
    </div>
    <div class="bg-twd08-violet">
      <div role="presentation" class="-mt-px h-[clamp(52px,8vw,100px)] bg-twd08-lilac [mask:var(--twd08-wave)_no-repeat_center/100%_100%]"></div>
    </div>
    <div class="bg-twd08-lilac text-twd08-violetink px-6 pt-2 pb-13 text-center">
      <p class="text-[15px]">Swapping the mask beats stretching one path across every viewport.</p>
    </div>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd08-paper: #f7f7f9;
  --color-twd08-paper: oklch(0.97 0.005 250);
  --color-twd08-ink: #1e2430;
  --color-twd08-ink: oklch(0.24 0.02 250);
  --color-twd08-mute: #5b6373;
  --color-twd08-mute: oklch(0.48 0.02 250);
  --color-twd08-edge: #dcdfe6;
  --color-twd08-edge: oklch(0.88 0.01 250);
  --color-twd08-next: #c3cee0;
  --color-twd08-next: oklch(0.84 0.03 250);
  --color-twd08-bad: #c4442a;
  --color-twd08-bad: oklch(0.55 0.18 28);
  --color-twd08-good: #1f7a4d;
  --color-twd08-good: oklch(0.48 0.12 155);
  --color-twd08-brand: #4a5fd0;
  --color-twd08-brand: oklch(0.52 0.17 270);
  --color-twd08-violet: #4a2a6b;
  --color-twd08-violet: oklch(0.33 0.11 300);
  --color-twd08-onviolet: #ddcdea;
  --color-twd08-onviolet: oklch(0.87 0.04 300);
  --color-twd08-lilac: #f4eefa;
  --color-twd08-lilac: oklch(0.96 0.02 300);
  --color-twd08-violetink: #4d3170;
  --color-twd08-violetink: oklch(0.38 0.1 300);
  --font-twd08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* The two wave shapes, swapped at the md breakpoint by reassigning one property.
   Geometry, not a design-scale value — so no @theme entry. */

.twd-08 {
  width: 100%;
  min-height: 100svh;
  --twd08-wave: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20110'%20preserveAspectRatio='none'%3E%3Cpath%20d='M0,48%20C80,104%20160,6%20240,48%20C320,90%20400,104%20480,60%20L480,110%20L0,110%20Z'%20fill='%23000'/%3E%3C/svg%3E");
}

@media (width >= 48rem) {
  .twd-08 {
    --twd08-wave: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201440%20110'%20preserveAspectRatio='none'%3E%3Cpath%20d='M0,54%20C300,110%20620,4%20940,52%20C1160,86%201300,96%201440,66%20L1440,110%20L0,110%20Z'%20fill='%23000'/%3E%3C/svg%3E");
  }
}
/* Safari < 15.4 mask shim. */

.twd-08 [role="presentation"] {
  -webkit-mask: var(--twd08-wave) no-repeat center/100% 100%;
}
```

## JavaScript
```js
(() => {
  const range = document.querySelector('#twd08-range');
  const panes = document.querySelector('#twd08-panes');
  const out = document.querySelector('#twd08-out');
  if (!range || !panes || !out) return;
  // Only the PANE WRAPPER is resized. Nothing measures or resizes a wave:
  // wave geometry stays declarative (clamp + min-w), which is why there is no CLS.
  const apply = () => {
    panes.style.width = range.value + '%';
    panes.style.marginInline = 'auto';
    out.textContent = range.value + '%';
  };
  range.addEventListener('input', apply);
  apply();
})();
```
