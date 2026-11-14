---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-magnetic-hover-effect-for-buttons-and-text/"
title: "Tailwind Magnetic Hover Effect for Buttons and Text"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Awwwards-style magnetic pills and a giant email link that lean toward the cursor."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Hover Effect for Buttons and Text
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-magnetic-hover-effect-for-buttons-and-text/

Awwwards-style magnetic pills and a giant email link that lean toward the cursor. A tiny script writes --tth14-mx/--tth14-my; the markup reads them with translate-x-[var(--tth14-mx,0px)], and the label leans 55% further for parallax. Release snaps back on an elastic not-hover:ease-[cubic-bezier(.22,1.6,.36,1)].
## HTML
```html
<section class="tth-14 w-full min-h-svh grid place-items-center bg-tth14-bg bg-[radial-gradient(80%_60%_at_50%_40%,var(--color-tth14-glow),var(--color-tth14-bg)_75%)] px-5 py-14 font-tth14-sans text-tth14-ink" aria-label="Magnetic cursor tracking text demo">
  <div class="flex flex-col items-center gap-[clamp(26px,5vw,44px)] text-center">
    <p class="text-xs font-bold uppercase tracking-[0.26em] text-tth14-mut">Bureau Nocturne &mdash; digital practice, Toronto</p>
    <div class="flex flex-wrap justify-center gap-[clamp(14px,3vw,26px)]">
      <a id="tth14-top" href="#tth14-top" data-tth14-magnet data-pull="0.42" class="grid min-h-14 place-items-center rounded-full bg-tth14-acc px-[30px] text-base font-extrabold tracking-[0.01em] text-tth14-on-acc no-underline translate-x-[var(--tth14-mx,0px)] translate-y-[var(--tth14-my,0px)] transition-[translate,box-shadow] duration-150 ease-out not-hover:duration-600 not-hover:ease-[cubic-bezier(.22,1.6,.36,1)] hover:shadow-[0_14px_40px_-10px_var(--color-tth14-acc)] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth14-acc motion-reduce:transition-none"><span class="inline-block translate-x-[calc(var(--tth14-mx,0px)*.55)] translate-y-[calc(var(--tth14-my,0px)*.55)] [transition:inherit]">View work</span></a>
      <a href="#tth14-top" data-tth14-magnet data-pull="0.42" class="grid min-h-14 place-items-center rounded-full bg-tth14-acc px-[30px] text-base font-extrabold tracking-[0.01em] text-tth14-on-acc no-underline translate-x-[var(--tth14-mx,0px)] translate-y-[var(--tth14-my,0px)] transition-[translate,box-shadow] duration-150 ease-out not-hover:duration-600 not-hover:ease-[cubic-bezier(.22,1.6,.36,1)] hover:shadow-[0_14px_40px_-10px_var(--color-tth14-acc)] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth14-acc motion-reduce:transition-none"><span class="inline-block translate-x-[calc(var(--tth14-mx,0px)*.55)] translate-y-[calc(var(--tth14-my,0px)*.55)] [transition:inherit]">Process</span></a>
      <a href="#tth14-top" data-tth14-magnet data-pull="0.42" class="grid min-h-14 place-items-center rounded-full border-[1.5px] border-tth14-ink/35 px-[30px] text-base font-extrabold tracking-[0.01em] no-underline translate-x-[var(--tth14-mx,0px)] translate-y-[var(--tth14-my,0px)] transition-[translate,border-color,background-color] duration-150 ease-out not-hover:duration-600 not-hover:ease-[cubic-bezier(.22,1.6,.36,1)] hover:border-tth14-ink hover:bg-tth14-ink/6 focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth14-acc motion-reduce:transition-none"><span class="inline-block translate-x-[calc(var(--tth14-mx,0px)*.55)] translate-y-[calc(var(--tth14-my,0px)*.55)] [transition:inherit]">About</span></a>
    </div>
    <a href="#tth14-top" data-tth14-magnet data-pull="0.2" class="group/mail inline-flex items-baseline gap-[0.35em] border-b-2 border-tth14-ink/25 pb-[0.12em] font-tth14-display text-[clamp(26px,5.6vw,52px)] font-semibold tracking-[-0.02em] no-underline translate-x-[var(--tth14-mx,0px)] translate-y-[var(--tth14-my,0px)] transition-[translate,border-color] duration-150 ease-out not-hover:duration-600 not-hover:ease-[cubic-bezier(.22,1.6,.36,1)] hover:border-tth14-acc focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth14-acc motion-reduce:transition-none"><span class="inline-block translate-x-[calc(var(--tth14-mx,0px)*.55)] translate-y-[calc(var(--tth14-my,0px)*.55)] [transition:inherit]">[email protected]</span><span aria-hidden="true" class="inline-block text-tth14-acc translate-x-[calc(var(--tth14-mx,0px)*.55)] translate-y-[calc(var(--tth14-my,0px)*.55)] [transition:inherit] group-hover/mail:rotate-45">&#8599;</span></a>
    <p class="max-w-[54ch] text-[12.5px] leading-[1.7] text-tth14-mut">Circle the cursor around a pill &mdash; it leans in, the label leans further, release snaps back on an elastic bezier. JS measures; Tailwind moves.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth14-bg: #100e15;
  --color-tth14-bg: oklch(0.16 0.01 290);
  --color-tth14-glow: #1a1721;
  --color-tth14-glow: oklch(0.21 0.017 295);
  --color-tth14-ink: #f1eff5;
  --color-tth14-ink: oklch(0.95 0.005 290);
  --color-tth14-mut: #a29eaa;
  --color-tth14-mut: oklch(0.72 0.015 290);
  --color-tth14-acc: #f7a93b;
  --color-tth14-acc: oklch(0.8 0.15 70);
  --color-tth14-on-acc: #2c1b06;
  --color-tth14-on-acc: oklch(0.22 0.04 70);
  --font-tth14-sans: 'Onest', system-ui, sans-serif;
  --font-tth14-display: 'Familjen Grotesk', system-ui, sans-serif;
}

.tth-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var magnets = document.querySelectorAll('[data-tth14-magnet]');
  if (!magnets.length) return;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)');
  var fine = matchMedia('(pointer: fine)');
  magnets.forEach(function (el) {
    var pull = parseFloat(el.getAttribute('data-pull')) || 0.35;
    el.addEventListener('pointermove', function (e) {
      if (reduced.matches || !fine.matches) return;
      var r = el.getBoundingClientRect();
      var x = (e.clientX - r.left - r.width / 2) * pull;
      var y = (e.clientY - r.top - r.height / 2) * pull;
      el.style.setProperty('--tth14-mx', x.toFixed(1) + 'px');
      el.style.setProperty('--tth14-my', y.toFixed(1) + 'px');
    });
    el.addEventListener('pointerleave', function () {
      el.style.setProperty('--tth14-mx', '0px');
      el.style.setProperty('--tth14-my', '0px');
    });
  });
})();
```
