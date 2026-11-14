---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-full-screen-mobile-navigation-overlay/"
title: "Tailwind Full Screen Mobile Navigation Overlay"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The fashion-house takeover: the menu becomes the page, and five oversized links reveal themselves line by line from under invisible masks."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Screen Mobile Navigation Overlay
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-full-screen-mobile-navigation-overlay/

The fashion-house takeover: the menu becomes the page, and five oversized links reveal themselves line by line from under invisible masks. The technique to steal is two utilities deep &mdash; overflow-hidden on the <li>, translate-y-[110%] on the link &mdash; and in the port both halves of the reveal sit in the same class list as the stagger that drives them.
## HTML
```html
<section class="thb-11 w-full min-h-svh grid justify-center content-start @container bg-thb11-paper font-thb11-sans text-thb11-sheet px-5 py-9" aria-label="Fullscreen overlay navigation demo">
  <div class="group relative w-[min(400px,88vw)] h-140 rounded-3xl overflow-hidden bg-thb11-paper border border-thb11-edge">
    <div class="absolute inset-0 grid content-start gap-4 px-6.5 py-23" aria-hidden="true">
      <div class="flex flex-col justify-between h-62.5 p-4.5 rounded bg-linear-[160deg,oklch(0.85_0.02_75),oklch(0.72_0.045_60)]">
        <span class="text-[11px] font-bold tracking-[0.3em]">AW&middot;26</span>
        <b class="text-[29px] leading-[1.04] font-bold tracking-[-0.02em]">Silhouettes<br>in Static</b>
      </div>
      <div class="h-2.5 w-[76%] rounded-full bg-thb11-line"></div>
      <div class="h-2.5 w-[58%] rounded-full bg-thb11-line"></div>
    </div>
    <nav id="thb11-sheet" aria-label="Site" class="absolute inset-0 z-2 flex flex-col justify-center px-7.5 bg-thb11-sheet opacity-0 scale-[1.03] invisible [transition:opacity_.35s,scale_.45s_var(--ease-thb11),visibility_0s_.45s] group-data-open:opacity-100 group-data-open:scale-100 group-data-open:visible group-data-open:[transition:opacity_.35s,scale_.45s_var(--ease-thb11),visibility_0s_0s]">
      <ul class="list-none">
        <li style="--i:0" class="overflow-hidden"><a href="#collections" class="block py-1.75 text-[clamp(34px,9cqi,44px)] font-extrabold leading-[1.08] tracking-[-0.02em] uppercase no-underline text-transparent [-webkit-text-stroke:1.5px_var(--color-thb11-paper)] translate-y-[110%] transition-[translate,color] duration-600 ease-thb11 hover:text-thb11-paper focus-visible:text-thb11-paper focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(250ms+var(--i)*70ms)] motion-reduce:duration-150"><span class="align-super mr-2 text-xs font-semibold tracking-[0.2em] text-thb11-acc [-webkit-text-stroke:0]" aria-hidden="true">01</span>Collections</a></li>
        <li style="--i:1" class="overflow-hidden"><a href="#runway" class="block py-1.75 text-[clamp(34px,9cqi,44px)] font-extrabold leading-[1.08] tracking-[-0.02em] uppercase no-underline text-transparent [-webkit-text-stroke:1.5px_var(--color-thb11-paper)] translate-y-[110%] transition-[translate,color] duration-600 ease-thb11 hover:text-thb11-paper focus-visible:text-thb11-paper focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(250ms+var(--i)*70ms)] motion-reduce:duration-150"><span class="align-super mr-2 text-xs font-semibold tracking-[0.2em] text-thb11-acc [-webkit-text-stroke:0]" aria-hidden="true">02</span>Runway</a></li>
        <li style="--i:2" class="overflow-hidden"><a href="#atelier" class="block py-1.75 text-[clamp(34px,9cqi,44px)] font-extrabold leading-[1.08] tracking-[-0.02em] uppercase no-underline text-transparent [-webkit-text-stroke:1.5px_var(--color-thb11-paper)] translate-y-[110%] transition-[translate,color] duration-600 ease-thb11 hover:text-thb11-paper focus-visible:text-thb11-paper focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(250ms+var(--i)*70ms)] motion-reduce:duration-150"><span class="align-super mr-2 text-xs font-semibold tracking-[0.2em] text-thb11-acc [-webkit-text-stroke:0]" aria-hidden="true">03</span>Atelier</a></li>
        <li style="--i:3" class="overflow-hidden"><a href="#stockists" class="block py-1.75 text-[clamp(34px,9cqi,44px)] font-extrabold leading-[1.08] tracking-[-0.02em] uppercase no-underline text-transparent [-webkit-text-stroke:1.5px_var(--color-thb11-paper)] translate-y-[110%] transition-[translate,color] duration-600 ease-thb11 hover:text-thb11-paper focus-visible:text-thb11-paper focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(250ms+var(--i)*70ms)] motion-reduce:duration-150"><span class="align-super mr-2 text-xs font-semibold tracking-[0.2em] text-thb11-acc [-webkit-text-stroke:0]" aria-hidden="true">04</span>Stockists</a></li>
        <li style="--i:4" class="overflow-hidden"><a href="#contact" class="block py-1.75 text-[clamp(34px,9cqi,44px)] font-extrabold leading-[1.08] tracking-[-0.02em] uppercase no-underline text-transparent [-webkit-text-stroke:1.5px_var(--color-thb11-paper)] translate-y-[110%] transition-[translate,color] duration-600 ease-thb11 hover:text-thb11-paper focus-visible:text-thb11-paper focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(250ms+var(--i)*70ms)] motion-reduce:duration-150"><span class="align-super mr-2 text-xs font-semibold tracking-[0.2em] text-thb11-acc [-webkit-text-stroke:0]" aria-hidden="true">05</span>Contact</a></li>
      </ul>
      <footer class="flex items-baseline gap-4.5 mt-8.5 text-xs text-thb11-mut opacity-0 transition-[opacity] duration-400 group-data-open:opacity-100 group-data-open:delay-500">
        <a href="#instagram" class="pb-0.5 text-thb11-paper no-underline border-b border-[oklch(1_0_0/0.25)] transition-[color,border-color] duration-200 hover:text-thb11-acc hover:border-thb11-acc focus-visible:text-thb11-acc focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-2">Instagram</a>
        <a href="#pinterest" class="pb-0.5 text-thb11-paper no-underline border-b border-[oklch(1_0_0/0.25)] transition-[color,border-color] duration-200 hover:text-thb11-acc hover:border-thb11-acc focus-visible:text-thb11-acc focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-2">Pinterest</a>
        <span class="ml-auto">Paris &mdash; Tokyo</span>
      </footer>
    </nav>
    <header class="absolute inset-x-0 top-0 z-3 flex items-center justify-between h-18 px-5.5 mix-blend-difference text-thb11-paper">
      <span class="text-[15px] font-extrabold tracking-[0.34em]">VESTIGE</span>
      <button type="button" aria-expanded="false" aria-controls="thb11-sheet" class="flex items-center gap-3 min-h-11 border-0 bg-transparent text-inherit cursor-pointer font-thb11-sans text-xs font-semibold tracking-[0.18em] uppercase focus-visible:outline-2 focus-visible:outline-thb11-acc focus-visible:outline-offset-4 focus-visible:rounded">
        <span class="relative block h-[15px] overflow-hidden">
          <i class="block h-[15px] leading-[15px] not-italic transition-[translate] duration-400 ease-thb11 group-data-open:-translate-y-[15px]">Menu</i>
          <i class="block h-[15px] leading-[15px] not-italic transition-[translate] duration-400 ease-thb11 group-data-open:-translate-y-[15px]">Close</i>
        </span>
        <span class="relative block w-6.5 h-2.5" aria-hidden="true">
          <b class="absolute left-0 top-0 w-6.5 h-[1.5px] bg-current transition-[translate,rotate] duration-350 ease-thb11 group-data-open:translate-y-1 group-data-open:rotate-20 motion-reduce:transition-none"></b>
          <b class="absolute left-0 top-2 w-6.5 h-[1.5px] bg-current transition-[translate,rotate] duration-350 ease-thb11 group-data-open:-translate-y-1 group-data-open:-rotate-20 motion-reduce:transition-none"></b>
        </span>
      </button>
    </header>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb11-paper: #f3f1eb;
  --color-thb11-paper: oklch(0.95 0.007 80);
  --color-thb11-sheet: #24211d;
  --color-thb11-sheet: oklch(0.16 0.012 70);
  --color-thb11-edge: #dcd8d0;
  --color-thb11-edge: oklch(0.86 0.01 80);
  --color-thb11-line: #dfdbd3;
  --color-thb11-line: oklch(0.87 0.012 80);
  --color-thb11-mut: #918b81;
  --color-thb11-mut: oklch(0.6 0.015 70);
  --color-thb11-acc: #dbab4e;
  --color-thb11-acc: oklch(0.78 0.15 75);
  --font-thb11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb11: cubic-bezier(0.2, 0.75, 0.15, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-11 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb11-sheet"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
