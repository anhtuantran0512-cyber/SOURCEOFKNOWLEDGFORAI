---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-text-scramble-and-matrix-decrypt-hover-effect/"
title: "Tailwind Text Scramble and Matrix Decrypt Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A terminal ops menu whose actions decrypt on hover: random glyphs cycle and lock left to right in 28ms ticks."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Text Scramble and Matrix Decrypt Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-text-scramble-and-matrix-decrypt-hover-effect/

A terminal ops menu whose actions decrypt on hover: random glyphs cycle and lock left to right in 28ms ticks. Monospace type plus min-w-[16ch] widths keep rows from breathing as characters change, and each link carries a stable aria-label so screen readers never hear the noise.
## HTML
```html
<section class="tth-17 w-full min-h-svh grid place-items-center bg-tth17-bg bg-[radial-gradient(100%_80%_at_50%_0%,var(--color-tth17-glow),var(--color-tth17-bg)_70%)] px-5 py-14 font-tth17-mono text-tth17-ink" aria-label="Text scramble decrypt demo">
  <div class="relative w-full max-w-[40rem] overflow-hidden rounded-[14px] border border-tth17-line bg-tth17-panel shadow-[0_24px_70px_oklch(0.05_0.02_155/0.55),0_0_0_1px_oklch(0.1_0.02_155)] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(0deg,oklch(0_0_0/0.14)_0_1px,transparent_1px_3px)] after:mix-blend-multiply after:content-['']">
    <header class="flex items-center gap-[7px] border-b border-tth17-line bg-tth17-bar px-4 py-3">
      <i class="size-2.5 rounded-full bg-[oklch(0.6_0.16_25)]"></i><i class="size-2.5 rounded-full bg-tth17-line"></i><i class="size-2.5 rounded-full bg-tth17-line"></i>
      <span class="ml-2 text-[11.5px] tracking-[0.08em] text-tth17-dim">krypta &mdash; ops console v3.1</span>
      <span class="ml-auto flex items-center gap-1.5 text-[10.5px] tracking-[0.12em] text-tth17-hot"><span aria-hidden="true" class="size-1.5 rounded-full bg-current animate-pulse motion-reduce:animate-none"></span>LIVE</span>
    </header>
    <p class="px-5 pt-[18px] pb-1 text-[12.5px] leading-[1.8] text-tth17-dim">&gt; session verified &middot; clearance <b class="font-bold text-tth17-hot">ONYX</b> &middot; 3 actions armed</p>
    <nav class="flex flex-col px-3 pt-3 pb-2" aria-label="Operations">
      <a id="tth17-top" href="#tth17-top" data-tth17-op data-text="ACCESS THE VAULT" aria-label="Access the vault" class="flex min-h-[52px] min-w-[16ch] items-center whitespace-nowrap rounded-lg px-3 text-[clamp(15px,2.6vw,19px)] font-bold tracking-[0.06em] no-underline transition-[background-color,color,text-shadow] duration-200 before:text-tth17-dim before:transition-colors before:content-['>_'] hover:bg-tth17-hover hover:text-tth17-hot hover:[text-shadow:0_0_0.5em_color-mix(in_oklch,var(--color-tth17-hot)_60%,transparent)] hover:before:text-tth17-hot focus-visible:bg-tth17-hover focus-visible:text-tth17-hot focus-visible:before:text-tth17-hot focus-visible:outline-[1.5px] focus-visible:-outline-offset-1 focus-visible:outline-tth17-hot">ACCESS THE VAULT</a>
      <a href="#tth17-top" data-tth17-op data-text="ROTATE ALL KEYS" aria-label="Rotate all keys" class="flex min-h-[52px] min-w-[15ch] items-center whitespace-nowrap rounded-lg px-3 text-[clamp(15px,2.6vw,19px)] font-bold tracking-[0.06em] no-underline transition-[background-color,color,text-shadow] duration-200 before:text-tth17-dim before:transition-colors before:content-['>_'] hover:bg-tth17-hover hover:text-tth17-hot hover:[text-shadow:0_0_0.5em_color-mix(in_oklch,var(--color-tth17-hot)_60%,transparent)] hover:before:text-tth17-hot focus-visible:bg-tth17-hover focus-visible:text-tth17-hot focus-visible:before:text-tth17-hot focus-visible:outline-[1.5px] focus-visible:-outline-offset-1 focus-visible:outline-tth17-hot">ROTATE ALL KEYS</a>
      <a href="#tth17-top" data-tth17-op data-text="BURN THIS SESSION" aria-label="Burn this session" class="flex min-h-[52px] min-w-[17ch] items-center whitespace-nowrap rounded-lg px-3 text-[clamp(15px,2.6vw,19px)] font-bold tracking-[0.06em] no-underline transition-[background-color,color,text-shadow] duration-200 before:text-tth17-dim before:transition-colors before:content-['>_'] hover:bg-tth17-hover hover:text-tth17-danger hover:[text-shadow:0_0_0.5em_color-mix(in_oklch,var(--color-tth17-danger)_60%,transparent)] hover:before:text-tth17-danger focus-visible:bg-tth17-hover focus-visible:text-tth17-danger focus-visible:before:text-tth17-danger focus-visible:outline-[1.5px] focus-visible:-outline-offset-1 focus-visible:outline-tth17-danger">BURN THIS SESSION</a>
    </nav>
    <p class="px-5 pt-2.5 pb-5 text-[11.5px] leading-[1.7] text-tth17-dim">Hover an action &mdash; characters cycle, then lock left to right. Monospace + <code class="rounded bg-tth17-hover px-1.5 py-px text-tth17-ink">ch</code> widths keep the row from breathing.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth17-bg: #07110b;
  --color-tth17-bg: oklch(0.14 0.01 155);
  --color-tth17-glow: #0c1a12;
  --color-tth17-glow: oklch(0.18 0.016 155);
  --color-tth17-panel: #0e1a13;
  --color-tth17-panel: oklch(0.18 0.015 155);
  --color-tth17-bar: #0b160f;
  --color-tth17-bar: oklch(0.16 0.012 155);
  --color-tth17-hover: #142519;
  --color-tth17-hover: oklch(0.23 0.025 152);
  --color-tth17-ink: #8fe6a2;
  --color-tth17-ink: oklch(0.87 0.12 150);
  --color-tth17-dim: #6fa27a;
  --color-tth17-dim: oklch(0.68 0.07 150);
  --color-tth17-hot: #b1ff9e;
  --color-tth17-hot: oklch(0.92 0.16 145);
  --color-tth17-danger: #ff8a6b;
  --color-tth17-danger: oklch(0.76 0.15 35);
  --color-tth17-line: #213528;
  --color-tth17-line: oklch(0.3 0.03 152);
  --font-tth17-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tth-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var CHARS = '#$%&@[]{}<>/=+*^!?:;0123456789';
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-tth17-op]').forEach(function (el) {
    function scramble() {
      if (reduced.matches) return;
      var txt = el.getAttribute('data-text'), tick = 0;
      clearInterval(el._tth17);
      el._tth17 = setInterval(function () {
        var out = '';
        for (var i = 0; i < txt.length; i++) {
          out += (tick > i * 2.6 || txt.charAt(i) === ' ') ? txt.charAt(i) : CHARS.charAt((Math.random() * CHARS.length) | 0);
        }
        el.textContent = out;
        if (tick++ > txt.length * 2.6 + 2) { clearInterval(el._tth17); el.textContent = txt; }
      }, 28);
    }
    el.addEventListener('pointerenter', scramble);
    el.addEventListener('focus', scramble);
  });
})();
```
