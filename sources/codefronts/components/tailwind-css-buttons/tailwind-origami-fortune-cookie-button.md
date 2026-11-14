---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-origami-fortune-cookie-button/"
title: "Tailwind Origami Fortune Cookie Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Press the cookie and it cracks: two clipped halves rotate apart, a paper slip slides out, and a fortune is written into a real aria-live region — so the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Origami Fortune Cookie Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-origami-fortune-cookie-button/

Press the cookie and it cracks: two clipped halves rotate apart, a paper slip slides out, and a fortune is written into a real aria-live region — so the message is announced, not merely displayed. The animation is garnish on a working disclosure.
## HTML
```html
<div class="tb-28 w-full min-h-svh grid place-items-center font-tb28-sans p-[clamp(1.5rem,6vw,4rem)]">
  <div class="tb-28__wrap group grid justify-items-center gap-3.5">
    <p role="status" aria-live="polite" class="tb-28__slip m-0 max-w-88 h-0 overflow-hidden px-4.5 rounded-[0.2rem] font-tb28-serif text-[1.0625rem] italic leading-relaxed text-center text-tb28-slip-ink bg-tb28-slip shadow-[0_8px_18px_-12px_#000000b3] scale-[0.72] opacity-0 transition-[scale,opacity,height,padding] duration-500 ease-tb28-out group-[.is-open]:scale-100 group-[.is-open]:opacity-100 group-[.is-open]:h-auto group-[.is-open]:py-3.5 motion-reduce:transition-none"></p>
    <button type="button" aria-expanded="false" class="tb-28__btn relative cursor-pointer border-0 bg-transparent pt-[4.9rem] min-w-52 text-[0.9375rem] font-bold text-tb28-ink [-webkit-tap-highlight-color:transparent] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb28-cookie focus-visible:rounded-2xl">
      <span aria-hidden="true" class="tb-28__half absolute inset-x-0 top-0 h-17 z-10 rounded-l-[2.2rem] origin-left [clip-path:polygon(0_0,52%_0,45%_50%,52%_100%,0_100%)] shadow-[inset_0_-2px_4px_#00000040,0_12px_22px_-12px_#000000b3] transition-[rotate,translate,filter] duration-[550ms] ease-tb28-out hover:brightness-105 group-hover:-rotate-2 group-[.is-open]:-rotate-9 group-[.is-open]:-translate-x-[1.1rem] group-[.is-open]:translate-y-[0.2rem] group-active:scale-[0.98] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="tb-28__half absolute inset-x-0 top-0 h-17 z-10 rounded-r-[2.2rem] origin-right [clip-path:polygon(52%_0,100%_0,100%_100%,52%_100%,45%_50%)] shadow-[inset_0_-2px_4px_#00000040,0_12px_22px_-12px_#000000b3] transition-[rotate,translate,filter] duration-[550ms] ease-tb28-out group-hover:rotate-2 group-[.is-open]:rotate-9 group-[.is-open]:translate-x-[1.1rem] group-[.is-open]:translate-y-[0.2rem] group-active:scale-[0.98] motion-reduce:transition-none"></span>
      <span class="relative z-30 block text-[0.9375rem] font-bold tracking-[0.01em] text-tb28-label transition-colors duration-300 group-[.is-open]:text-tb28-label-dim">Open your fortune</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb28-bg: #2a1a1c;
  --color-tb28-bg: oklch(0.24 0.03 25);
  --color-tb28-cookie: #e8b874;
  --color-tb28-cookie: oklch(0.82 0.1 76);
  --color-tb28-cookie-lo: #b8843f;
  --color-tb28-cookie-lo: oklch(0.65 0.11 66);
  --color-tb28-ink: #4a2a10;
  --color-tb28-ink: oklch(0.32 0.07 62);
  --color-tb28-label: #f2ddb9;
  --color-tb28-label: oklch(0.91 0.04 82);
  --color-tb28-label-dim: #d8c4a3;
  --color-tb28-label-dim: oklch(0.82 0.04 82);
  --color-tb28-slip: #fdfaf3;
  --color-tb28-slip-ink: #3b2b22;
  --color-tb28-slip-ink: oklch(0.3 0.03 50);
  --font-tb28-sans: "DM Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tb28-serif: "Cormorant Garamond", ui-serif, Georgia, serif;
  --ease-tb28-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-28 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 46%, color-mix(in oklab, var(--color-tb28-cookie) 18%, transparent), transparent 72%), var(--color-tb28-bg);
}
/* BAKED SURFACE: one specular over a diagonal base, shared by both halves. */

.tb-28__half {
  background: radial-gradient(120% 90% at 30% 20%, color-mix(in oklab, var(--color-tb28-cookie) 70%, white), transparent 60%), linear-gradient(160deg, var(--color-tb28-cookie), var(--color-tb28-cookie-lo));
}

@media (prefers-color-scheme: light) {
  .tb-28:not([data-theme="dark"]) {
    --color-tb28-bg: oklch(0.3 0.035 25);
  }
}

.tb-28[data-theme="light"] {
  --color-tb28-bg: oklch(0.3 0.035 25);
}

@media (forced-colors: active) {
  .tb-28__half {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-28__btn span:last-child {
    color: CanvasText;
  }

  .tb-28__slip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const wrap = document.querySelector('.tb-28__wrap');
  const btn = wrap && wrap.querySelector('.tb-28__btn');
  const slip = wrap && wrap.querySelector('.tb-28__slip');
  if (!btn) return;
  const fortunes = [
    'The bug you fear is a typo you already fixed.',
    'Ship the small thing today; the big thing will follow.',
    'A stranger will use your CSS at 3am and be grateful.',
    'Delete one thing before you add three.',
    'Your next idea arrives while you are away from the keyboard.',
  ];
  let open = false;
  let last = -1;
  const pick = () => {
    let i = last;
    while (i === last) i = Math.floor(Math.random() * fortunes.length);
    last = i;
    return fortunes[i];
  };
  btn.addEventListener('click', () => {
    open = !open;
    wrap.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
    slip.textContent = open ? pick() : '';
  });
})();
```
