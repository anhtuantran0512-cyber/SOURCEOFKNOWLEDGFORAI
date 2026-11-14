---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-hamburger-menu-clip-path-circle-expansion/"
title: "Tailwind Hamburger Menu with Clip-Path Circle Expansion"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The reveal every design-award site uses, ported to variants: tap the burger and the menu grows out of the button as a perfect circle, because the panel…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hamburger Menu with Clip-Path Circle Expansion
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-hamburger-menu-clip-path-circle-expansion/

The reveal every design-award site uses, ported to variants: tap the burger and the menu grows out of the button as a perfect circle, because the panel carries its closed and open clip-path as two arbitrary utilities on one element. The state is a data-open attribute on the stage, so the panel, the icon bars and the link stagger all read it through group-data-open: — the stylesheet keeps nothing but tokens.
## HTML
```html
<section class="thb-01 w-full min-h-svh grid justify-center content-start bg-thb01-bg font-thb01-sans text-thb01-ink px-5 py-9" aria-label="Clip-path circle expansion hamburger menu demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb01-bg border border-thb01-edge shadow-[0_30px_60px_-35px_oklch(0.3_0.05_285/0.45)]">
    <header class="relative z-1 flex items-center h-19 px-6">
      <span class="flex items-center gap-2.5 text-[15px] font-bold tracking-[-0.01em]">
        <i class="w-5.5 h-5.5 rounded-full bg-[conic-gradient(from_210deg,var(--color-thb01-acc),oklch(0.55_0.2_300),var(--color-thb01-acc))]" aria-hidden="true"></i>orbit.studio
      </span>
    </header>
    <div class="grid gap-3.5 px-6 pt-2" aria-hidden="true">
      <div class="h-47 mb-2 rounded-2xl bg-linear-[140deg,oklch(0.9_0.03_265),oklch(0.84_0.05_300)]"></div>
      <div class="h-3 w-[82%] rounded-full bg-thb01-line"></div>
      <div class="h-3 w-[64%] rounded-full bg-thb01-line"></div>
      <div class="h-3 w-[74%] rounded-full bg-thb01-line"></div>
      <div class="h-3 w-[46%] rounded-full bg-thb01-line"></div>
    </div>
    <nav id="thb01-menu" aria-label="Site" class="absolute inset-0 z-2 flex flex-col justify-center gap-1.5 px-8.5 bg-[radial-gradient(120%_100%_at_100%_0%,oklch(0.3_0.08_295),var(--color-thb01-menu)_55%)] invisible [clip-path:circle(0px_at_calc(100%-46px)_46px)] [transition:clip-path_.65s_var(--ease-thb01),visibility_0s_.65s] group-data-open:visible group-data-open:[clip-path:circle(150%_at_calc(100%-46px)_46px)] group-data-open:[transition:clip-path_.65s_var(--ease-thb01),visibility_0s_0s] motion-reduce:[clip-path:none] motion-reduce:opacity-0 motion-reduce:[transition:opacity_.15s,visibility_0s_.15s] motion-reduce:group-data-open:opacity-100 motion-reduce:group-data-open:[transition:opacity_.15s]">
      <a href="#work" style="--i:0" class="flex items-baseline gap-3.5 py-3 px-0.5 rounded-md text-[31px] font-bold tracking-[-0.02em] text-thb01-paper no-underline opacity-0 translate-y-4.5 transition-[opacity,translate,color] duration-400 ease-thb01 hover:text-thb01-acc focus-visible:text-thb01-acc focus-visible:outline-2 focus-visible:outline-thb01-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(180ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><small class="font-thb01-mono text-[11px] font-semibold text-thb01-acc tabular-nums">01</small>Work</a>
      <a href="#studio" style="--i:1" class="flex items-baseline gap-3.5 py-3 px-0.5 rounded-md text-[31px] font-bold tracking-[-0.02em] text-thb01-paper no-underline opacity-0 translate-y-4.5 transition-[opacity,translate,color] duration-400 ease-thb01 hover:text-thb01-acc focus-visible:text-thb01-acc focus-visible:outline-2 focus-visible:outline-thb01-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(180ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><small class="font-thb01-mono text-[11px] font-semibold text-thb01-acc tabular-nums">02</small>Studio</a>
      <a href="#journal" style="--i:2" class="flex items-baseline gap-3.5 py-3 px-0.5 rounded-md text-[31px] font-bold tracking-[-0.02em] text-thb01-paper no-underline opacity-0 translate-y-4.5 transition-[opacity,translate,color] duration-400 ease-thb01 hover:text-thb01-acc focus-visible:text-thb01-acc focus-visible:outline-2 focus-visible:outline-thb01-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(180ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><small class="font-thb01-mono text-[11px] font-semibold text-thb01-acc tabular-nums">03</small>Journal</a>
      <a href="#contact" style="--i:3" class="flex items-baseline gap-3.5 py-3 px-0.5 rounded-md text-[31px] font-bold tracking-[-0.02em] text-thb01-paper no-underline opacity-0 translate-y-4.5 transition-[opacity,translate,color] duration-400 ease-thb01 hover:text-thb01-acc focus-visible:text-thb01-acc focus-visible:outline-2 focus-visible:outline-thb01-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(180ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><small class="font-thb01-mono text-[11px] font-semibold text-thb01-acc tabular-nums">04</small>Contact</a>
      <p style="--i:4" class="mt-6.5 font-thb01-mono text-xs text-thb01-dim opacity-0 translate-y-4.5 transition-[opacity,translate] duration-400 ease-thb01 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(180ms+var(--i)*60ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">[email protected] &middot; NYC &mdash; LDN</p>
    </nav>
    <button type="button" aria-expanded="false" aria-controls="thb01-menu" aria-label="Open menu" class="absolute z-3 top-5.5 right-5.5 grid place-items-center w-12 h-12 rounded-full border-0 bg-thb01-ink cursor-pointer transition-[background,scale] duration-300 hover:scale-106 active:scale-94 focus-visible:outline-2 focus-visible:outline-thb01-acc focus-visible:outline-offset-3 group-data-open:bg-thb01-btnopen motion-reduce:transition-none">
      <span class="relative block w-5 h-3.5" aria-hidden="true">
        <i class="absolute left-0 top-0 w-5 h-0.5 rounded-sm bg-thb01-bg transition-[translate,rotate] duration-300 group-data-open:translate-y-1.5 group-data-open:rotate-45 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-1.5 w-5 h-0.5 rounded-sm bg-thb01-bg transition-[opacity,translate] duration-200 group-data-open:opacity-0 group-data-open:-translate-x-1.5 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-3 w-5 h-0.5 rounded-sm bg-thb01-bg transition-[translate,rotate] duration-300 group-data-open:-translate-y-1.5 group-data-open:-rotate-45 motion-reduce:transition-none"></i>
      </span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb01-bg: #f7f7fa;
  --color-thb01-bg: oklch(0.97 0.005 250);
  --color-thb01-ink: #2c2f3d;
  --color-thb01-ink: oklch(0.22 0.02 260);
  --color-thb01-edge: #dfe0e6;
  --color-thb01-edge: oklch(0.88 0.01 260);
  --color-thb01-line: #e4e4ea;
  --color-thb01-line: oklch(0.9 0.008 260);
  --color-thb01-menu: #2f2549;
  --color-thb01-menu: oklch(0.23 0.06 285);
  --color-thb01-btnopen: #453a63;
  --color-thb01-btnopen: oklch(0.32 0.07 295);
  --color-thb01-paper: #f6f5f0;
  --color-thb01-paper: oklch(0.96 0.01 90);
  --color-thb01-dim: #a49ab5;
  --color-thb01-dim: oklch(0.68 0.03 290);
  --color-thb01-acc: #e5b45c;
  --color-thb01-acc: oklch(0.8 0.16 85);
  --font-thb01-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb01: cubic-bezier(0.65, 0, 0.35, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-01 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-01 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb01-menu"]');
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
