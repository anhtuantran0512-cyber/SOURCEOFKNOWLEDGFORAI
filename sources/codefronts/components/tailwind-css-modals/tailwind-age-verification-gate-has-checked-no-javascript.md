---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-age-verification-gate-has-checked-no-javascript/"
title: "Tailwind Age Verification Gate with :has() and Zero JavaScript"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A full-screen entry gate that blurs and blocks the page until the visitor confirms their age — still zero JavaScript, now keyboard-operable."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Age Verification Gate with :has() and Zero JavaScript
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-age-verification-gate-has-checked-no-javascript/

A full-screen entry gate that blurs and blocks the page until the visitor confirms their age — still zero JavaScript, now keyboard-operable. The port reads one checkbox from two directions: has-checked: on the wrapper un-blurs the article, and peer-checked: on the gate fades it out.
## HTML
```html
<section class="tm-03 group relative w-full min-h-svh overflow-hidden bg-tm03-bg font-tm03-sans">
  <article class="min-h-svh flex flex-col items-center justify-center gap-5 p-10 text-center blur-[9px] scale-[1.02] transition-[filter,transform] duration-500 group-has-checked:blur-none group-has-checked:scale-100 motion-reduce:transition-none">
    <h1 class="text-[clamp(38px,9vw,74px)] font-extrabold tracking-[0.12em] text-tm03-hi">CASK &amp; OAK</h1>
    <p class="max-w-[44ch] text-base leading-relaxed text-tm03-mut">Small-batch single malt, aged in highland oak. Explore the reserve collection.</p>
    <div aria-hidden="true" class="flex gap-4 mt-2">
      <span class="w-[90px] h-[120px] rounded-xl border border-tm03-edge bg-tm03-tile"></span>
      <span class="w-[90px] h-[120px] rounded-xl border border-tm03-edge bg-tm03-tile"></span>
      <span class="w-[90px] h-[120px] rounded-xl border border-tm03-edge bg-tm03-tile"></span>
    </div>
  </article>

  <input type="checkbox" id="tm-03-ok" class="peer sr-only">
  <div role="dialog" aria-modal="true" aria-labelledby="tm-03-t" aria-describedby="tm-03-d" class="fixed inset-0 z-10 grid place-items-center p-6 bg-tm03-scrim backdrop-blur-[3px] transition-[opacity,visibility] duration-[450ms] peer-checked:opacity-0 peer-checked:invisible motion-reduce:transition-none">
    <div class="w-[min(430px,94vw)] px-8 py-10 text-center rounded-[20px] bg-tm03-panel border border-tm03-edge shadow-[0_40px_90px_-30px_#000]">
      <div aria-hidden="true" class="grid place-items-center size-20 mx-auto mb-5 rounded-full border-2 border-tm03-accedge text-[26px] font-extrabold text-tm03-acc shadow-[0_0_40px_-10px_var(--color-tm03-acc),inset_0_0_24px_-12px_var(--color-tm03-acc)]">21+</div>
      <h2 id="tm-03-t" class="mb-2.5 text-[22px] font-bold text-tm03-hi">Are you of legal drinking age?</h2>
      <p id="tm-03-d" class="mb-6 text-sm text-tm03-mut">You must be 21 or older to enter this site.</p>
      <div class="flex flex-wrap justify-center gap-3">
        <label for="tm-03-ok" class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-sm font-semibold cursor-pointer bg-tm03-acc text-tm03-onacc border border-tm03-acc transition-[filter] duration-200 hover:brightness-110 group-has-[#tm-03-ok:focus-visible]:outline-2 group-has-[#tm-03-ok:focus-visible]:outline-tm03-acc group-has-[#tm-03-ok:focus-visible]:outline-offset-[3px]">Yes, I am 21+</label>
        <a href="https://responsibility.org" class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-sm font-semibold no-underline text-tm03-mut border border-tm03-edge transition-colors duration-200 hover:text-tm03-ink hover:border-tm03-accedge focus-visible:outline-2 focus-visible:outline-tm03-acc focus-visible:outline-offset-[3px]">No, exit</a>
      </div>
      <p class="mt-5 text-xs tracking-[0.06em] text-tm03-faint">Press <kbd class="px-1.5 py-0.5 rounded border border-tm03-edge text-[11px]">Space</kbd> to confirm &middot; please enjoy responsibly.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm03-bg: #0b0805;
  --color-tm03-bg: oklch(0.15 0.015 70);
  --color-tm03-panel: #1a1309;
  --color-tm03-panel: oklch(0.21 0.025 70);
  --color-tm03-tile: #241a0f;
  --color-tm03-tile: oklch(0.25 0.03 70);
  --color-tm03-edge: #3a2c1a;
  --color-tm03-edge: oklch(0.32 0.035 70);
  --color-tm03-hi: #f3e9d8;
  --color-tm03-hi: oklch(0.93 0.025 80);
  --color-tm03-ink: #d9cdb8;
  --color-tm03-ink: oklch(0.85 0.03 80);
  --color-tm03-mut: #b6a894;
  --color-tm03-mut: oklch(0.73 0.03 80);
  --color-tm03-faint: #8a7b64;
  --color-tm03-faint: oklch(0.6 0.03 80);
  --color-tm03-acc: #e0a04d;
  --color-tm03-acc: oklch(0.76 0.13 70);
  --color-tm03-accedge: #a87a3c;
  --color-tm03-accedge: oklch(0.6 0.1 70);
  --color-tm03-onacc: #1c1206;
  --color-tm03-onacc: oklch(0.2 0.03 70);
  --color-tm03-scrim: #080604c7;
  --color-tm03-scrim: oklch(0.13 0.012 70 / 0.78);
  --font-tm03-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tm-03 {
  width: 100%;
}
```
