---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-minimalist-floating-hamburger-button/"
title: "Tailwind Minimalist Floating Hamburger Button"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Navigation reduced to a single floating disc: a 56px FAB opening a vertical speed-dial of pill links that spring upward with staggered, slightly overshooting…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Floating Hamburger Button
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-minimalist-floating-hamburger-button/

Navigation reduced to a single floating disc: a 56px FAB opening a vertical speed-dial of pill links that spring upward with staggered, slightly overshooting motion. The technique to study is that the spring is transitions only &mdash; no keyframes &mdash; so a close mid-open reverses gracefully, and in utilities the overshoot curve and the plain opacity ease are visibly split.
## HTML
```html
<section class="thb-14 w-full min-h-svh grid justify-center content-start bg-thb14-bg font-thb14-sans text-thb14-ink px-5 py-9" aria-label="Floating hamburger button demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb14-bg border border-thb14-edge">
    <div class="grid content-start gap-3.75 px-7.5 py-10" aria-hidden="true">
      <h2 class="text-[26px] font-bold tracking-[-0.02em]">Notes on less</h2>
      <p class="max-w-[34ch] mb-2.5 text-[13.5px] leading-relaxed text-thb14-mut text-pretty">A reading page with no header at all &mdash; navigation lives in one floating disc, bottom-right.</p>
      <div class="h-2.5 w-full rounded-full bg-thb14-line"></div>
      <div class="h-2.5 w-[92%] rounded-full bg-thb14-line"></div>
      <div class="h-2.5 w-[97%] rounded-full bg-thb14-line"></div>
      <div class="h-2.5 w-[64%] rounded-full bg-thb14-line"></div>
      <div class="h-2.5 w-[88%] rounded-full bg-thb14-line"></div>
      <div class="h-2.5 w-[71%] rounded-full bg-thb14-line"></div>
    </div>
    <nav id="thb14-dial" aria-label="Site" class="absolute right-4.5 bottom-21.5 flex flex-col items-end gap-2.5">
      <a href="#writing" style="--i:2" class="flex items-center gap-2.25 min-h-11 pl-3.5 pr-4.5 rounded-full bg-white border border-thb14-edge shadow-[0_10px_24px_-14px_oklch(0.2_0.01_90/0.5)] text-[13.5px] font-semibold text-thb14-ink no-underline opacity-0 translate-y-3.5 scale-60 pointer-events-none [transition:opacity_.25s,translate_.45s_var(--ease-thb14spring),scale_.45s_var(--ease-thb14spring),border-color_.2s,color_.2s] hover:border-thb14-acc hover:text-thb14-acc focus-visible:border-thb14-acc focus-visible:text-thb14-acc focus-visible:outline-2 focus-visible:outline-thb14-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:pointer-events-auto group-data-open:[transition-delay:calc(var(--i)*50ms)] motion-reduce:[transition:opacity_.15s] motion-reduce:translate-y-0 motion-reduce:scale-100">
        <svg viewBox="0 0 24 24" class="w-4.25 h-4.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M5 4h11l3 3v13H5Z"/><path d="M15.5 4v3.5H19M8.5 12h7M8.5 16h5"/></svg>Writing
      </a>
      <a href="#about" style="--i:1" class="flex items-center gap-2.25 min-h-11 pl-3.5 pr-4.5 rounded-full bg-white border border-thb14-edge shadow-[0_10px_24px_-14px_oklch(0.2_0.01_90/0.5)] text-[13.5px] font-semibold text-thb14-ink no-underline opacity-0 translate-y-3.5 scale-60 pointer-events-none [transition:opacity_.25s,translate_.45s_var(--ease-thb14spring),scale_.45s_var(--ease-thb14spring),border-color_.2s,color_.2s] hover:border-thb14-acc hover:text-thb14-acc focus-visible:border-thb14-acc focus-visible:text-thb14-acc focus-visible:outline-2 focus-visible:outline-thb14-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:pointer-events-auto group-data-open:[transition-delay:calc(var(--i)*50ms)] motion-reduce:[transition:opacity_.15s] motion-reduce:translate-y-0 motion-reduce:scale-100">
        <svg viewBox="0 0 24 24" class="w-4.25 h-4.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>About
      </a>
      <a href="#contact" style="--i:0" class="flex items-center gap-2.25 min-h-11 pl-3.5 pr-4.5 rounded-full bg-white border border-thb14-edge shadow-[0_10px_24px_-14px_oklch(0.2_0.01_90/0.5)] text-[13.5px] font-semibold text-thb14-ink no-underline opacity-0 translate-y-3.5 scale-60 pointer-events-none [transition:opacity_.25s,translate_.45s_var(--ease-thb14spring),scale_.45s_var(--ease-thb14spring),border-color_.2s,color_.2s] hover:border-thb14-acc hover:text-thb14-acc focus-visible:border-thb14-acc focus-visible:text-thb14-acc focus-visible:outline-2 focus-visible:outline-thb14-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:pointer-events-auto group-data-open:[transition-delay:calc(var(--i)*50ms)] motion-reduce:[transition:opacity_.15s] motion-reduce:translate-y-0 motion-reduce:scale-100">
        <svg viewBox="0 0 24 24" class="w-4.25 h-4.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4.5 7 7.5 6L19.5 7"/></svg>Contact
      </a>
    </nav>
    <button type="button" aria-expanded="false" aria-controls="thb14-dial" aria-label="Open menu" class="absolute right-4.5 bottom-4.5 grid place-items-center w-14 h-14 rounded-full border-0 bg-thb14-fab text-thb14-fabink cursor-pointer shadow-[0_14px_30px_-12px_color-mix(in_oklch,var(--color-thb14-fab)_70%,transparent)] transition-[translate,scale,box-shadow,background] duration-250 hover:-translate-y-0.5 hover:shadow-[0_20px_36px_-12px_color-mix(in_oklch,var(--color-thb14-fab)_65%,transparent)] active:scale-92 focus-visible:outline-2 focus-visible:outline-thb14-acc focus-visible:outline-offset-3 motion-reduce:transition-none">
      <span class="relative block w-4.5 h-3" aria-hidden="true">
        <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
      </span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb14-bg: #fcfcfa;
  --color-thb14-bg: oklch(0.985 0.002 90);
  --color-thb14-edge: #e6e6e3;
  --color-thb14-edge: oklch(0.9 0.004 90);
  --color-thb14-line: #ececea;
  --color-thb14-line: oklch(0.93 0.003 90);
  --color-thb14-ink: #2e2d2a;
  --color-thb14-ink: oklch(0.22 0.008 90);
  --color-thb14-mut: #7c7a74;
  --color-thb14-mut: oklch(0.55 0.008 90);
  --color-thb14-fab: #2e2d2a;
  --color-thb14-fab: oklch(0.22 0.008 90);
  --color-thb14-fabink: #fcfcfa;
  --color-thb14-fabink: oklch(0.985 0.002 90);
  --color-thb14-acc: #4a7ae0;
  --color-thb14-acc: oklch(0.62 0.15 255);
  --font-thb14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb14spring: cubic-bezier(0.2, 1.4, 0.35, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-14 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb14-dial"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
