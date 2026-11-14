---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-magnetic-mercury-ripple-button/"
title: "Tailwind Magnetic Mercury Ripple Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "The button leans toward your cursor like it is magnetised, a mercury highlight tracks the pointer across its surface, and clicks ripple from the exact point…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Mercury Ripple Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-magnetic-mercury-ripple-button/

The button leans toward your cursor like it is magnetised, a mercury highlight tracks the pointer across its surface, and clicks ripple from the exact point of contact. The JS writes four custom properties; every visual is a utility that reads them — the cleanest division of labour in the collection.
## HTML
```html
<div class="tb-15 w-full min-h-svh grid place-items-center font-tb15-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-15__btn group relative overflow-hidden isolate cursor-pointer min-h-15 px-9 border border-tb15-line rounded-[1.15rem] text-base font-semibold tracking-[-0.01em] text-tb15-ink bg-[linear-gradient(180deg,var(--color-tb15-btn-lift),var(--color-tb15-btn))] shadow-[0_20px_44px_-24px_#000000e6,inset_0_1px_0_var(--color-tb15-sheen)] translate-x-[calc(var(--dx)*var(--tb-15-pull))] translate-y-[calc(var(--dy)*var(--tb-15-pull)*0.6)] transition-[translate,transform,border-color,box-shadow] duration-[450ms] ease-tb15-spring touch-manipulation [-webkit-tap-highlight-color:transparent] hover:border-tb15-accent-line active:scale-[0.985] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb15-accent motion-reduce:transition-none motion-reduce:translate-x-0 motion-reduce:translate-y-0">
    <span aria-hidden="true" class="absolute -inset-px z-10 rounded-[inherit] opacity-0 blur-[2px] saturate-[1.2] transition-opacity duration-[350ms] bg-[radial-gradient(9rem_6rem_at_var(--mx)_var(--my),var(--color-tb15-mercury),transparent_62%),radial-gradient(3.2rem_3.2rem_at_var(--mx)_var(--my),var(--color-tb15-mercury-hot),transparent_70%)] group-hover:opacity-90 motion-reduce:hidden"></span>
    <span aria-hidden="true" class="absolute z-10 top-[var(--my)] left-[var(--mx)] size-4 -mt-2 -ml-2 rounded-full pointer-events-none opacity-0 bg-[radial-gradient(circle,var(--color-tb15-ripple),transparent_70%)] group-[.is-rippling]:animate-tb15-ripple motion-reduce:hidden"></span>
    <span class="relative z-20 inline-block transition-transform duration-500 ease-tb15-spring group-hover:translate-x-[calc(var(--dx)*4px)] group-hover:translate-y-[calc(var(--dy)*3px)] motion-reduce:transition-none motion-reduce:group-hover:translate-x-0 motion-reduce:group-hover:translate-y-0">Explore the system</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb15-bg: #08090c;
  --color-tb15-bg: oklch(0.12 0.008 260);
  --color-tb15-btn: #101319;
  --color-tb15-btn: oklch(0.2 0.015 260);
  --color-tb15-btn-lift: #171b23;
  --color-tb15-btn-lift: oklch(0.24 0.015 260);
  --color-tb15-line: #262b36;
  --color-tb15-line: oklch(0.31 0.02 260);
  --color-tb15-ink: #f2f5fa;
  --color-tb15-ink: oklch(0.96 0.006 260);
  --color-tb15-accent: #a3e635;
  --color-tb15-accent: oklch(0.87 0.19 124);
  --color-tb15-accent-line: #6d9b2a;
  --color-tb15-accent-line: oklch(0.62 0.13 124);
  --color-tb15-mercury: #a3e6358c;
  --color-tb15-mercury: oklch(0.87 0.19 124 / 0.55);
  --color-tb15-mercury-hot: #ffffff8c;
  --color-tb15-ripple: #a3e635b3;
  --color-tb15-ripple: oklch(0.87 0.19 124 / 0.7);
  --color-tb15-sheen: #ffffff1f;
  --font-tb15-sans: "Sora", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb15-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb15-ripple: tb-15-ripple 0.62s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb15-spring: linear(0, 0.35 6%, 0.78 14%, 1.05 22%, 1.09 27%, 1.03 36%, 1 50%, 1);
  }
}

@keyframes tb-15-ripple {
  0% {
    opacity: 0.85;
    scale: 0;
  }

  100% {
    opacity: 0;
    scale: 22;
  }
}

.tb-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(38rem 24rem at 50% 50%, color-mix(in oklab, var(--color-tb15-accent) 8%, transparent), transparent 70%), var(--color-tb15-bg);
}
/* Pointer state defaults — the JS overwrites these; the button is correct without JS. */

.tb-15__btn {
  --mx: 50%;
  --my: 50%;
  --dx: 0;
  --dy: 0;
  --tb-15-pull: 13px;
}

@media (prefers-color-scheme: light) {
  .tb-15:not([data-theme="dark"]) {
    --color-tb15-bg: oklch(0.95 0.004 260);
  }
}

.tb-15[data-theme="light"] {
  --color-tb15-bg: oklch(0.95 0.004 260);
}

@media (forced-colors: active) {
  .tb-15__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-15__btn > span[aria-hidden] {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-15__btn');
  if (!btn) return;
  let box = null;
  btn.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
  btn.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    box = box || btn.getBoundingClientRect();
    const nx = (e.clientX - box.left) / box.width;
    const ny = (e.clientY - box.top) / box.height;
    btn.style.setProperty('--mx', (nx * 100).toFixed(2) + '%');
    btn.style.setProperty('--my', (ny * 100).toFixed(2) + '%');
    btn.style.setProperty('--dx', (nx - 0.5).toFixed(3));
    btn.style.setProperty('--dy', (ny - 0.5).toFixed(3));
  });
  btn.addEventListener('pointerleave', () => {
    box = null;
    btn.style.setProperty('--dx', '0');
    btn.style.setProperty('--dy', '0');
  });
  btn.addEventListener('click', () => {
    btn.classList.remove('is-rippling');
    void btn.offsetWidth; // restart the keyframes
    btn.classList.add('is-rippling');
  });
})();
```
