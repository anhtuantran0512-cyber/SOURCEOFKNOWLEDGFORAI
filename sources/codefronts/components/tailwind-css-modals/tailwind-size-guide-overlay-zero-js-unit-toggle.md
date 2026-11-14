---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-size-guide-overlay-zero-js-unit-toggle/"
title: "Tailwind Size Guide Overlay with Zero-JS cm/inch Toggle"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "An apparel size chart that opens from a text link and flips between centimetres and inches — no JavaScript in either interaction."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Size Guide Overlay with Zero-JS cm/inch Toggle
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-size-guide-overlay-zero-js-unit-toggle/

An apparel size chart that opens from a text link and flips between centimetres and inches — no JavaScript in either interaction. Two checkbox/radio gates, read with group-has-checked: and group-has-[#tm-08-in:checked]:, do what two :has() rules did before.
## HTML
```html
<section class="tm-08 group relative w-full min-h-svh grid place-items-center bg-tm08-bg font-tm08-sans px-6 py-10">
  <div class="flex flex-col items-start gap-4 p-6 rounded-2xl bg-tm08-panel border border-tm08-edge">
    <div class="flex items-center gap-2">
      <span class="mr-1.5 text-xs uppercase tracking-[0.16em] text-tm08-mut">Size</span>
      <span class="grid place-items-center min-w-11 min-h-11 px-3 rounded-lg text-[13px] font-semibold text-tm08-ink border border-tm08-edge bg-tm08-well">S</span>
      <span class="grid place-items-center min-w-11 min-h-11 px-3 rounded-lg text-[13px] font-semibold text-white border border-tm08-acc bg-tm08-acctint">M</span>
      <span class="grid place-items-center min-w-11 min-h-11 px-3 rounded-lg text-[13px] font-semibold text-tm08-ink border border-tm08-edge bg-tm08-well">L</span>
      <span class="grid place-items-center min-w-11 min-h-11 px-3 rounded-lg text-[13px] font-semibold text-tm08-ink border border-tm08-edge bg-tm08-well">XL</span>
    </div>
    <input type="checkbox" id="tm-08-t" class="peer sr-only">
    <label for="tm-08-t" class="inline-flex items-center gap-1.5 min-h-11 px-1 text-[13px] font-semibold text-tm08-acc underline underline-offset-[3px] cursor-pointer transition-[filter] duration-200 hover:brightness-125 peer-focus-visible:outline-2 peer-focus-visible:outline-tm08-acc peer-focus-visible:outline-offset-2 peer-focus-visible:rounded-md"><span aria-hidden="true">📏</span> Size guide</label>
  </div>

  <div role="dialog" aria-modal="true" aria-labelledby="tm-08-title" class="fixed inset-0 z-10 grid place-items-center p-6 bg-tm08-scrim backdrop-blur-[4px] opacity-0 invisible pointer-events-none transition-[opacity,visibility] duration-[280ms] group-has-checked:opacity-100 group-has-checked:visible group-has-checked:pointer-events-auto motion-reduce:transition-none">
    <div class="flex flex-col w-[min(460px,94vw)] max-h-[88dvh] rounded-[18px] bg-tm08-card border border-tm08-cardedge shadow-[0_40px_90px_-30px_#000] scale-[0.96] transition-transform duration-[280ms] group-has-checked:scale-100 motion-reduce:transition-none">
      <div class="flex items-center gap-3.5 px-5 py-4 border-b border-tm08-edge">
        <h2 id="tm-08-title" class="flex-1 text-lg font-bold text-tm08-hi">Size guide</h2>
        <div class="inline-flex rounded-[9px] border border-tm08-edge overflow-hidden">
          <input type="radio" name="tm-08-u" id="tm-08-cm" checked class="peer/cm sr-only">
          <label for="tm-08-cm" class="grid place-items-center min-h-11 px-4 text-xs font-semibold text-tm08-mut bg-tm08-well cursor-pointer transition-colors duration-150 peer-checked/cm:bg-tm08-acctint peer-checked/cm:text-white peer-focus-visible/cm:outline-2 peer-focus-visible/cm:outline-tm08-acc peer-focus-visible/cm:-outline-offset-2">cm</label>
          <input type="radio" name="tm-08-u" id="tm-08-in" class="peer/in sr-only">
          <label for="tm-08-in" class="grid place-items-center min-h-11 px-4 text-xs font-semibold text-tm08-mut bg-tm08-well cursor-pointer transition-colors duration-150 peer-checked/in:bg-tm08-acctint peer-checked/in:text-white peer-focus-visible/in:outline-2 peer-focus-visible/in:outline-tm08-acc peer-focus-visible/in:-outline-offset-2">in</label>
        </div>
        <label for="tm-08-t" aria-label="Close size guide" class="grid place-items-center size-11 rounded-lg text-[22px] leading-none text-tm08-mut cursor-pointer transition-colors duration-200 hover:bg-tm08-well hover:text-white">&times;</label>
      </div>

      <div class="overflow-auto px-2 py-1.5">
        <table class="w-full border-collapse text-sm">
          <thead>
            <tr>
              <th scope="col" class="sticky top-0 px-2.5 py-3 text-center text-xs font-semibold uppercase tracking-[0.05em] text-tm08-mut bg-tm08-thead border-b border-tm08-edge">Size</th>
              <th scope="col" class="sticky top-0 px-2.5 py-3 text-center text-xs font-semibold uppercase tracking-[0.05em] text-tm08-mut bg-tm08-thead border-b border-tm08-edge">Chest</th>
              <th scope="col" class="sticky top-0 px-2.5 py-3 text-center text-xs font-semibold uppercase tracking-[0.05em] text-tm08-mut bg-tm08-thead border-b border-tm08-edge">Waist</th>
              <th scope="col" class="sticky top-0 px-2.5 py-3 text-center text-xs font-semibold uppercase tracking-[0.05em] text-tm08-mut bg-tm08-thead border-b border-tm08-edge">Length</th>
            </tr>
          </thead>
          <tbody class="group-has-[#tm-08-in:checked]:hidden">
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">XS</th><td class="px-2.5 py-3 text-center text-tm08-ink">86</td><td class="px-2.5 py-3 text-center text-tm08-ink">71</td><td class="px-2.5 py-3 text-center text-tm08-ink">68</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">S</th><td class="px-2.5 py-3 text-center text-tm08-ink">91</td><td class="px-2.5 py-3 text-center text-tm08-ink">76</td><td class="px-2.5 py-3 text-center text-tm08-ink">70</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">M</th><td class="px-2.5 py-3 text-center text-tm08-ink">97</td><td class="px-2.5 py-3 text-center text-tm08-ink">81</td><td class="px-2.5 py-3 text-center text-tm08-ink">72</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">L</th><td class="px-2.5 py-3 text-center text-tm08-ink">102</td><td class="px-2.5 py-3 text-center text-tm08-ink">86</td><td class="px-2.5 py-3 text-center text-tm08-ink">74</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">XL</th><td class="px-2.5 py-3 text-center text-tm08-ink">109</td><td class="px-2.5 py-3 text-center text-tm08-ink">94</td><td class="px-2.5 py-3 text-center text-tm08-ink">76</td></tr>
          </tbody>
          <tbody class="hidden group-has-[#tm-08-in:checked]:table-row-group">
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">XS</th><td class="px-2.5 py-3 text-center text-tm08-ink">34</td><td class="px-2.5 py-3 text-center text-tm08-ink">28</td><td class="px-2.5 py-3 text-center text-tm08-ink">26.8</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">S</th><td class="px-2.5 py-3 text-center text-tm08-ink">36</td><td class="px-2.5 py-3 text-center text-tm08-ink">30</td><td class="px-2.5 py-3 text-center text-tm08-ink">27.6</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">M</th><td class="px-2.5 py-3 text-center text-tm08-ink">38</td><td class="px-2.5 py-3 text-center text-tm08-ink">32</td><td class="px-2.5 py-3 text-center text-tm08-ink">28.3</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">L</th><td class="px-2.5 py-3 text-center text-tm08-ink">40</td><td class="px-2.5 py-3 text-center text-tm08-ink">34</td><td class="px-2.5 py-3 text-center text-tm08-ink">29.1</td></tr>
            <tr class="odd:bg-white/[0.02] hover:bg-tm08-rowhover"><th scope="row" class="pl-4 py-3 text-left font-bold text-tm08-hi">XL</th><td class="px-2.5 py-3 text-center text-tm08-ink">43</td><td class="px-2.5 py-3 text-center text-tm08-ink">37</td><td class="px-2.5 py-3 text-center text-tm08-ink">29.9</td></tr>
          </tbody>
        </table>
      </div>
      <p class="px-5 pt-4 pb-5 text-[12.5px] leading-relaxed text-tm08-mut border-t border-tm08-edge">Body measurements. Between sizes? Size up for a relaxed fit. Press <kbd class="px-1.5 py-0.5 rounded border border-tm08-edge text-[11px]">Space</kbd> on the focused control to open or close this guide.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm08-bg: #07080b;
  --color-tm08-bg: oklch(0.15 0.012 260);
  --color-tm08-panel: #12151d;
  --color-tm08-panel: oklch(0.2 0.015 260);
  --color-tm08-card: #141822;
  --color-tm08-card: oklch(0.21 0.017 260);
  --color-tm08-thead: #161b26;
  --color-tm08-thead: oklch(0.22 0.018 260);
  --color-tm08-well: #0e1119;
  --color-tm08-well: oklch(0.18 0.015 260);
  --color-tm08-edge: #2a3140;
  --color-tm08-edge: oklch(0.3 0.018 260);
  --color-tm08-cardedge: #262c3c;
  --color-tm08-cardedge: oklch(0.29 0.018 260);
  --color-tm08-hi: #f2f5fc;
  --color-tm08-hi: oklch(0.97 0.006 260);
  --color-tm08-ink: #c7cedb;
  --color-tm08-ink: oklch(0.84 0.012 260);
  --color-tm08-mut: #98a1b4;
  --color-tm08-mut: oklch(0.71 0.018 260);
  --color-tm08-acc: #7fb0ff;
  --color-tm08-acc: oklch(0.75 0.14 250);
  --color-tm08-acctint: #24344f;
  --color-tm08-acctint: oklch(0.33 0.06 250);
  --color-tm08-rowhover: #7fb0ff1f;
  --color-tm08-rowhover: oklch(0.75 0.14 250 / 0.12);
  --color-tm08-scrim: #06080ca8;
  --color-tm08-scrim: oklch(0.13 0.01 260 / 0.66);
  --font-tm08-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tm-08 {
  width: 100%;
}
```
