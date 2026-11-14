---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-3d-flip-canvas-mobile-hamburger-navigation/"
title: "Tailwind 3D Flip Canvas Mobile Hamburger Navigation"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The theatrical finale: the entire page tilts back in 3D &mdash; rotateY around its right edge with real perspective &mdash; swinging aside like a door to…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Canvas Mobile Hamburger Navigation
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-3d-flip-canvas-mobile-hamburger-navigation/

The theatrical finale: the entire page tilts back in 3D &mdash; rotateY around its right edge with real perspective &mdash; swinging aside like a door to reveal the nav standing behind it, whose links counter-rotate into place. Three properties produce the drama, and in utilities all three are arbitrary on purpose: perspective, transform-origin and a composed transform are scene geometry, not design tokens.
## HTML
```html
<section class="thb-28 w-full min-h-svh grid justify-center content-start bg-thb28-bg font-thb28-sans text-thb28-ink px-5 py-9" aria-label="3D flip canvas navigation demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden border border-thb28-edge bg-thb28-bg bg-[radial-gradient(130%_100%_at_90%_50%,oklch(0.25_0.06_320/0.85),transparent_60%)] [perspective:1400px]">
    <nav id="thb28-menu" aria-label="Site" class="absolute inset-y-0 right-0 left-[44%] flex flex-col gap-0.5 px-6.5 py-8.5 text-thb28-menuink opacity-35 [transform:rotateY(18deg)_translateX(40px)] [transition:transform_.6s_var(--ease-thb28),opacity_.5s] group-data-open:opacity-100 group-data-open:[transform:rotateY(0)_translateX(0)] motion-reduce:[transform:none] motion-reduce:[transition:opacity_.15s]">
      <b style="--i:0" class="mb-4 font-thb28-mono text-xs font-bold tracking-[0.26em] uppercase text-thb28-acc">Menu</b>
      <a href="#work" style="--i:1" class="py-3 text-[21px] font-bold tracking-[-0.01em] text-thb28-menuink no-underline border-b border-[oklch(1_0_0/0.1)] opacity-0 translate-x-4.5 transition-[opacity,translate,color] duration-450 ease-thb28in hover:text-thb28-acc focus-visible:text-thb28-acc focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-4 focus-visible:rounded group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(150ms+var(--i)*50ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Selected work</a>
      <a href="#reel" style="--i:2" class="py-3 text-[21px] font-bold tracking-[-0.01em] text-thb28-menuink no-underline border-b border-[oklch(1_0_0/0.1)] opacity-0 translate-x-4.5 transition-[opacity,translate,color] duration-450 ease-thb28in hover:text-thb28-acc focus-visible:text-thb28-acc focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-4 focus-visible:rounded group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(150ms+var(--i)*50ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Show reel</a>
      <a href="#process" style="--i:3" class="py-3 text-[21px] font-bold tracking-[-0.01em] text-thb28-menuink no-underline border-b border-[oklch(1_0_0/0.1)] opacity-0 translate-x-4.5 transition-[opacity,translate,color] duration-450 ease-thb28in hover:text-thb28-acc focus-visible:text-thb28-acc focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-4 focus-visible:rounded group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(150ms+var(--i)*50ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Process</a>
      <a href="#studio" style="--i:4" class="py-3 text-[21px] font-bold tracking-[-0.01em] text-thb28-menuink no-underline border-b border-[oklch(1_0_0/0.1)] opacity-0 translate-x-4.5 transition-[opacity,translate,color] duration-450 ease-thb28in hover:text-thb28-acc focus-visible:text-thb28-acc focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-4 focus-visible:rounded group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(150ms+var(--i)*50ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Studio</a>
      <a href="#contact" style="--i:5" class="py-3 text-[21px] font-bold tracking-[-0.01em] text-thb28-menuink no-underline border-b border-[oklch(1_0_0/0.1)] opacity-0 translate-x-4.5 transition-[opacity,translate,color] duration-450 ease-thb28in hover:text-thb28-acc focus-visible:text-thb28-acc focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-4 focus-visible:rounded group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(150ms+var(--i)*50ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Contact</a>
      <span style="--i:6" class="mt-auto font-thb28-mono text-[11.5px] text-thb28-menudim opacity-0 transition-[opacity] duration-400 group-data-open:opacity-100 group-data-open:delay-450">&copy; 2026 &mdash; Antwerp</span>
    </nav>
    <div id="thb28-canvas" class="absolute inset-0 z-1 flex flex-col bg-thb28-page [transform-origin:88%_50%] [transition:transform_.6s_var(--ease-thb28),box-shadow_.6s,border-radius_.6s] group-data-open:[transform:translateX(-58%)_rotateY(34deg)_scale(0.92)] group-data-open:rounded-[18px] group-data-open:shadow-[40px_30px_80px_-30px_oklch(0.08_0.03_310/0.8)] motion-reduce:group-data-open:[transform:translateX(-58%)] motion-reduce:[transition:transform_.15s]">
      <header class="flex items-center justify-between h-17 pl-6 pr-4.5 border-b border-thb28-pageedge">
        <span class="text-[13px] font-extrabold tracking-[0.24em]">DEPTH.WORKS</span>
        <button type="button" aria-expanded="false" aria-controls="thb28-menu" aria-label="Open menu" class="grid place-items-center w-11.5 h-11.5 rounded-xl border-0 bg-thb28-ink2 text-thb28-page cursor-pointer transition-[background,scale] duration-250 hover:scale-105 active:scale-93 focus-visible:outline-2 focus-visible:outline-thb28-acc focus-visible:outline-offset-3 motion-reduce:transition-none">
          <span class="relative block w-4.5 h-3" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </button>
      </header>
      <div class="flex-1 grid content-start gap-3.5 p-5.5" aria-hidden="true">
        <div class="grid content-end h-62.5 p-5 rounded-2xl bg-linear-[155deg,oklch(0.85_0.06_330),oklch(0.62_0.16_320)]">
          <span class="text-[30px] font-extrabold leading-[1.02] tracking-[-0.02em] text-thb28-posterink">MOTION<br>&amp; SPACE</span>
        </div>
        <div class="h-2.75 w-[74%] rounded-full bg-thb28-line"></div>
        <div class="h-2.75 w-[58%] rounded-full bg-thb28-line"></div>
      </div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-y-0 left-0 right-[56%] z-5 hidden border-0 bg-transparent cursor-e-resize group-data-open:block"></button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb28-bg: #2a1f33;
  --color-thb28-bg: oklch(0.17 0.03 310);
  --color-thb28-edge: #47394f;
  --color-thb28-edge: oklch(0.3 0.04 310);
  --color-thb28-page: #f5f2f6;
  --color-thb28-page: oklch(0.96 0.006 310);
  --color-thb28-pageedge: #ded8e0;
  --color-thb28-pageedge: oklch(0.88 0.01 310);
  --color-thb28-line: #e3dde5;
  --color-thb28-line: oklch(0.89 0.008 310);
  --color-thb28-ink: #eee9f0;
  --color-thb28-ink: oklch(0.94 0.01 320);
  --color-thb28-ink2: #38304a;
  --color-thb28-ink2: oklch(0.24 0.02 310);
  --color-thb28-menuink: #eee9f0;
  --color-thb28-menuink: oklch(0.94 0.01 320);
  --color-thb28-menudim: #9a8fa4;
  --color-thb28-menudim: oklch(0.62 0.03 320);
  --color-thb28-posterink: #2f1c33;
  --color-thb28-posterink: oklch(0.2 0.05 320);
  --color-thb28-acc: #e069b4;
  --color-thb28-acc: oklch(0.75 0.17 340);
  --font-thb28-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb28-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb28: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-thb28in: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-28 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-28 > .group').forEach(function (vp) {
    if (vp.dataset.bound) return; vp.dataset.bound = '1';
    var btn = vp.querySelector('button[aria-controls="thb28-menu"]'),
        canvas = vp.querySelector('#thb28-canvas'),
        catcher = vp.querySelector('button[aria-hidden="true"]');
    function set(open) {
      vp.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) { canvas.setAttribute('inert', ''); vp.querySelector('#thb28-menu a').focus(); }
      else { canvas.removeAttribute('inert'); btn.focus(); }
    }
    btn.addEventListener('click', function () { set(true); });
    catcher.addEventListener('click', function () { set(false); });
    vp.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && vp.hasAttribute('data-open')) set(false);
    });
  });
})();
```
