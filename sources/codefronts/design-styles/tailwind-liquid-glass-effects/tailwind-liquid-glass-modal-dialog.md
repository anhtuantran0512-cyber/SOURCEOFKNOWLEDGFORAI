---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-modal-dialog/"
title: "Tailwind Liquid Glass Modal Dialog"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A dialog that frosts the entire page behind it, built on native <dialog> so focus containment and Escape-to-close come for free."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Modal Dialog
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-modal-dialog/

A dialog that frosts the entire page behind it, built on native <dialog> so focus containment and Escape-to-close come for free. The port's headline is the backdrop: variant &mdash; Tailwind styles ::backdrop directly, so the scrim's blur is a utility on the same element as the panel's.
## HTML
```html
<section class="lgt-05 relative grid w-full min-h-svh place-items-center overflow-hidden bg-lgt05-bg font-lgt05-sans" aria-label="Tailwind liquid glass modal dialog">
  <img src="https://picsum.photos/seed/lgmodal/1200/800" width="1200" height="800" alt="Studio workspace" class="absolute inset-0 z-0 size-full object-cover">
  <button id="lgt-05-open" type="button" class="relative z-1 cursor-pointer rounded-full border border-white/40 bg-white/16 px-7.5 py-3.75 text-base font-bold text-white backdrop-blur-[14px] backdrop-saturate-160 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_14px_30px_-16px_rgba(0,0,0,.6)] transition-transform duration-200 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Open glass dialog</button>

  <dialog id="lgt-05-dialog" aria-labelledby="lgt-05-title" class="max-w-[min(420px,92vw)] rounded-[26px] border border-white/35 bg-white/16 p-7.5 text-white backdrop-blur-[24px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_40px_80px_-30px_rgba(0,0,0,.7)] open:animate-lgt05-in data-closing:animate-lgt05-out backdrop:bg-lgt05-scrim backdrop:backdrop-blur-[14px] backdrop:backdrop-saturate-140 motion-reduce:animate-none motion-reduce:data-closing:animate-none">
    <h3 id="lgt-05-title" class="mb-2.5 text-[22px] font-extrabold">Confirm upgrade</h3>
    <p class="text-[15px] leading-relaxed text-white [text-shadow:0_1px_6px_rgba(0,0,0,.35)]">You're switching to the Studio plan. Your new features unlock immediately and billing adjusts on your next cycle.</p>
    <div class="mt-6 flex justify-end gap-3">
      <button id="lgt-05-cancel" type="button" class="cursor-pointer rounded-full border border-white/35 bg-white/12 px-5 py-2.75 text-sm font-bold text-white transition-[background-color,transform] duration-200 hover:bg-white/22 focus-visible:bg-white/22 active:scale-96 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Cancel</button>
      <button id="lgt-05-confirm" type="button" class="cursor-pointer rounded-full border border-lgt05-accent/60 bg-lgt05-accent px-5 py-2.75 text-sm font-bold text-white transition-[background-color,transform] duration-200 hover:brightness-110 focus-visible:brightness-110 active:scale-96 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Upgrade</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt05-bg: #0e0b1a;
  --color-lgt05-bg: oklch(0.16 0.03 295);
  --color-lgt05-accent: #6a4bff;
  --color-lgt05-accent: oklch(0.62 0.2 275);
  --color-lgt05-scrim: rgb(10 8 20 / 0.4);
  --font-lgt05-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt05-in: lgt-05-in 0.35s cubic-bezier(0.2, 0.9, 0.2, 1);
  --animate-lgt05-out: lgt-05-out 0.2s ease forwards;
}

@keyframes lgt-05-in {
  from {
    transform: scale(0.9);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes lgt-05-out {
  to {
    transform: scale(0.95);
    opacity: 0;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.lgt-05');
  const dlg = root.querySelector('#lgt-05-dialog');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const close = () => {
    if (reduce) { dlg.close(); return; }
    dlg.dataset.closing = '';
    dlg.addEventListener('animationend', () => { delete dlg.dataset.closing; dlg.close(); }, { once: true });
  };
  root.querySelector('#lgt-05-open').addEventListener('click', () => dlg.showModal());
  root.querySelector('#lgt-05-cancel').addEventListener('click', close);
  root.querySelector('#lgt-05-confirm').addEventListener('click', close);
  dlg.addEventListener('click', e => {
    const r = dlg.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) close();
  });
  dlg.addEventListener('cancel', e => { e.preventDefault(); close(); });
})();
```
