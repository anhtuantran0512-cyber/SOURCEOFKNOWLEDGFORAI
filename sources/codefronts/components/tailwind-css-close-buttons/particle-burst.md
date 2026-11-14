---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/particle-burst/"
title: "Particle Burst Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Eight particles from one 6px dot: a single keyframe animates eight box-shadow copies outward and shrinks them, while the × squashes and pops."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Burst Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/particle-burst/

Eight particles from one 6px dot: a single keyframe animates eight box-shadow copies outward and shrinks them, while the × squashes and pops. The CSS original played it on :active, so a quick tap cut the burst off after a frame or two; the port triggers it with a data-burst attribute that the script clears on animationend, so every tap gets the full 550ms.
## HTML
```html
<section class="tcb-19 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb19-bg),var(--color-tcb19-bg2))] px-6 py-12 font-tcb19-sans" aria-label="Particle burst close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button id="tcb-19-btn" type="button" aria-label="Close" class="group relative grid size-16 cursor-pointer place-items-center rounded-full border-[1.5px] border-tcb19-p1/40 bg-tcb19-btn shadow-[0_16px_36px_-18px_rgb(0_0_0/0.8)] transition-colors duration-200 hover:border-tcb19-p1 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb19-p1 motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-5 before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb19-x after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb19-x group-data-burst:animate-tcb19-pop motion-reduce:animate-none!"></span>
      <span data-burst-dot aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 -m-[3px] size-1.5 rounded-full group-data-burst:animate-tcb19-boom motion-reduce:animate-none!"></span>
    </button>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb19-mono text-[11.5px] text-tcb19-mut ring-1 ring-white/12">8× box-shadow particles · group-data-burst: · animationend</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb19-bg: #211a2e;
  --color-tcb19-bg: oklch(0.2 0.03 300);
  --color-tcb19-bg2: #16121f;
  --color-tcb19-bg2: oklch(0.15 0.02 290);
  --color-tcb19-btn: #2a2138;
  --color-tcb19-btn: oklch(0.24 0.035 300);
  --color-tcb19-p1: #f0a23a;
  --color-tcb19-p1: oklch(0.77 0.16 65);
  --color-tcb19-p2: #e04aa6;
  --color-tcb19-p2: oklch(0.65 0.22 340);
  --color-tcb19-x: #f7efe6;
  --color-tcb19-x: oklch(0.95 0.02 60);
  --color-tcb19-mut: #bcaecb;
  --color-tcb19-mut: oklch(0.77 0.04 300);
  --font-tcb19-sans: 'Geist', system-ui, sans-serif;
  --font-tcb19-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb19-boom: tcb19-boom 0.55s cubic-bezier(0.2,0.7,0.3,1) forwards;
  --animate-tcb19-pop: tcb19-pop 0.55s cubic-bezier(0.34,1.56,0.64,1) forwards;

  @keyframes tcb19-boom {
    0% {
      background: var(--color-tcb19-p1);
      box-shadow: 0 0 0 0 var(--color-tcb19-p1), 0 0 0 0 var(--color-tcb19-p2), 0 0 0 0 var(--color-tcb19-p1), 0 0 0 0 var(--color-tcb19-p2), 0 0 0 0 var(--color-tcb19-p1), 0 0 0 0 var(--color-tcb19-p2), 0 0 0 0 var(--color-tcb19-p1), 0 0 0 0 var(--color-tcb19-p2);
    }

    60% {
      background: transparent;
      box-shadow: 22px 0 0 0 var(--color-tcb19-p1), 15px -15px 0 0 var(--color-tcb19-p2), 0 -22px 0 0 var(--color-tcb19-p1), -15px -15px 0 0 var(--color-tcb19-p2), -22px 0 0 0 var(--color-tcb19-p1), -15px 15px 0 0 var(--color-tcb19-p2), 0 22px 0 0 var(--color-tcb19-p1), 15px 15px 0 0 var(--color-tcb19-p2);
    }

    100% {
      background: transparent;
      box-shadow: 26px 0 0 -3px transparent, 18px -18px 0 -3px transparent, 0 -26px 0 -3px transparent, -18px -18px 0 -3px transparent, -26px 0 0 -3px transparent, -18px 18px 0 -3px transparent, 0 26px 0 -3px transparent, 18px 18px 0 -3px transparent;
    }
  }

  @keyframes tcb19-pop {
    0% {
      transform: scale(1);
    }

    30% {
      transform: scale(0.8);
    }

    70% {
      transform: scale(1.12);
    }

    100% {
      transform: scale(1);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-19 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('tcb-19-btn');
  if (!btn || btn.dataset.wired) return;
  btn.dataset.wired = '1';
  const dot = btn.querySelector('[data-burst-dot]');
  const fire = () => {
    btn.removeAttribute('data-burst');
    requestAnimationFrame(() => requestAnimationFrame(() => btn.setAttribute('data-burst', '')));
  };
  btn.addEventListener('pointerdown', fire);
  btn.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && !e.repeat) fire(); });
  dot.addEventListener('animationend', () => btn.removeAttribute('data-burst'));
})();
```
