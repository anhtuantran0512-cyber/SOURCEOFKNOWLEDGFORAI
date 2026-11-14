---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-glassmorphism-backdrop-blur-hamburger-navigation/"
title: "Tailwind Glassmorphism Backdrop Blur Hamburger Navigation"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Real frosted glass, not grey-with-opacity &mdash; and Tailwind happens to have the exact utilities for it: backdrop-blur-[18px] backdrop-saturate-[1.7]…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Backdrop Blur Hamburger Navigation
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-glassmorphism-backdrop-blur-hamburger-navigation/

Real frosted glass, not grey-with-opacity &mdash; and Tailwind happens to have the exact utilities for it: backdrop-blur-[18px] backdrop-saturate-[1.7] compose into one backdrop-filter, no prefix juggling, no stacking order to remember. The stage runs drifting gradient blobs so you can see the glass working, and the mandatory @supports not fallback stays in CSS, where it belongs.
## HTML
```html
<section class="thb-07 w-full min-h-svh grid justify-center content-start bg-thb07-bg font-thb07-sans text-thb07-ink px-5 py-9" aria-label="Glassmorphism backdrop blur menu demo">
  <div class="group relative isolate w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb07-bg border border-thb07-edge">
    <i class="absolute z-0 -left-20 top-15 w-75 h-75 rounded-full blur-[70px] bg-thb07-blob1 animate-[thb07-drift_11s_ease-in-out_infinite_alternate] motion-reduce:animate-none" aria-hidden="true"></i>
    <i class="absolute z-0 -right-17.5 -bottom-10 w-65 h-65 rounded-full blur-[70px] bg-thb07-blob2 animate-[thb07-drift_13s_ease-in-out_infinite_alternate-reverse] motion-reduce:animate-none" aria-hidden="true"></i>
    <header class="relative z-3 flex items-center justify-between h-18 px-5.5">
      <span class="text-[17px] font-bold tracking-[0.22em] uppercase">lumen</span>
      <button type="button" aria-expanded="false" aria-controls="thb07-menu" aria-label="Open menu" class="grid place-items-center w-11.5 h-11.5 rounded-[14px] border border-[oklch(1_0_0/0.28)] bg-[oklch(0.97_0.01_260/0.1)] backdrop-blur-[12px] backdrop-saturate-[1.6] text-thb07-ink cursor-pointer transition-[background,scale] duration-250 hover:bg-[oklch(0.97_0.01_260/0.2)] hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-3">
        <span class="relative block w-4.5 h-3" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
        </span>
      </button>
    </header>
    <div class="relative z-1 grid justify-items-start gap-3.5 px-6.5 py-11.5" aria-hidden="true">
      <h2 class="text-[37px] leading-[1.05] font-bold tracking-[-0.03em] text-balance">Light, refracted.</h2>
      <p class="max-w-[26ch] text-sm leading-relaxed text-thb07-mut text-pretty">Studio for luminous interfaces &mdash; glass, gradients and grain.</p>
      <div class="mt-2.5 px-4 py-2.25 rounded-full border border-[oklch(1_0_0/0.25)] bg-[oklch(0.97_0.01_260/0.08)] backdrop-blur-[8px] text-[11.5px] font-semibold tracking-[0.12em] uppercase">Scroll &darr;</div>
    </div>
    <nav id="thb07-menu" aria-label="Site" class="thb07-glass absolute z-2 inset-x-4 top-21.5 bottom-4 flex flex-col justify-center gap-0.5 px-6.5 rounded-[20px] bg-[oklch(0.97_0.01_260/0.12)] backdrop-blur-[18px] backdrop-saturate-[1.7] border border-[oklch(1_0_0/0.28)] shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_24px_48px_-20px_oklch(0.2_0.05_280/0.5)] opacity-0 -translate-y-3.5 scale-[0.98] invisible [transition:opacity_.35s,translate_.4s_var(--ease-thb07),scale_.4s_var(--ease-thb07),visibility_0s_.4s] group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:visible group-data-open:[transition:opacity_.35s,translate_.4s_var(--ease-thb07),scale_.4s_var(--ease-thb07),visibility_0s_0s]">
      <a href="#work" style="--i:0" class="group/l flex items-center justify-between py-3.75 px-0.5 rounded-md border-b border-[oklch(1_0_0/0.14)] text-[28px] font-bold tracking-[-0.02em] text-thb07-ink no-underline opacity-0 translate-y-3 transition-[color,opacity,translate] duration-350 ease-thb07 hover:text-thb07-acc focus-visible:text-thb07-acc focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*55ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Work</span><span class="text-base opacity-0 -translate-x-1.5 translate-y-1 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-hover/l:translate-y-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0 group-focus-visible/l:translate-y-0" aria-hidden="true">&#8599;</span></a>
      <a href="#services" style="--i:1" class="group/l flex items-center justify-between py-3.75 px-0.5 rounded-md border-b border-[oklch(1_0_0/0.14)] text-[28px] font-bold tracking-[-0.02em] text-thb07-ink no-underline opacity-0 translate-y-3 transition-[color,opacity,translate] duration-350 ease-thb07 hover:text-thb07-acc focus-visible:text-thb07-acc focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*55ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Services</span><span class="text-base opacity-0 -translate-x-1.5 translate-y-1 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-hover/l:translate-y-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0 group-focus-visible/l:translate-y-0" aria-hidden="true">&#8599;</span></a>
      <a href="#about" style="--i:2" class="group/l flex items-center justify-between py-3.75 px-0.5 rounded-md border-b border-[oklch(1_0_0/0.14)] text-[28px] font-bold tracking-[-0.02em] text-thb07-ink no-underline opacity-0 translate-y-3 transition-[color,opacity,translate] duration-350 ease-thb07 hover:text-thb07-acc focus-visible:text-thb07-acc focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*55ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>About</span><span class="text-base opacity-0 -translate-x-1.5 translate-y-1 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-hover/l:translate-y-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0 group-focus-visible/l:translate-y-0" aria-hidden="true">&#8599;</span></a>
      <a href="#contact" style="--i:3" class="group/l flex items-center justify-between py-3.75 px-0.5 rounded-md border-b border-[oklch(1_0_0/0.14)] text-[28px] font-bold tracking-[-0.02em] text-thb07-ink no-underline opacity-0 translate-y-3 transition-[color,opacity,translate] duration-350 ease-thb07 hover:text-thb07-acc focus-visible:text-thb07-acc focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-4 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*55ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><span>Contact</span><span class="text-base opacity-0 -translate-x-1.5 translate-y-1 transition-[opacity,translate] duration-250 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-hover/l:translate-y-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0 group-focus-visible/l:translate-y-0" aria-hidden="true">&#8599;</span></a>
      <footer style="--i:4" class="flex items-center justify-between mt-5.5 text-xs text-thb07-mut opacity-0 translate-y-3 transition-[opacity,translate] duration-350 ease-thb07 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*55ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
        <span>&copy; 2026 lumen</span>
        <a href="#privacy" class="text-xs text-thb07-mut no-underline transition-[color] duration-200 hover:text-thb07-acc focus-visible:text-thb07-acc focus-visible:outline-2 focus-visible:outline-thb07-acc focus-visible:outline-offset-2">Privacy</a>
      </footer>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb07-bg: #322a4d;
  --color-thb07-bg: oklch(0.22 0.045 285);
  --color-thb07-edge: #55496f;
  --color-thb07-edge: oklch(0.35 0.05 285);
  --color-thb07-ink: #f6f4fb;
  --color-thb07-ink: oklch(0.97 0.008 285);
  --color-thb07-mut: #c3bcd4;
  --color-thb07-mut: oklch(0.78 0.03 285);
  --color-thb07-acc: #6fd7e0;
  --color-thb07-acc: oklch(0.82 0.14 190);
  --color-thb07-blob1: #a03fd8;
  --color-thb07-blob1: oklch(0.62 0.23 310);
  --color-thb07-blob2: #4bc0d8;
  --color-thb07-blob2: oklch(0.75 0.16 200);
  --font-thb07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb07: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Keyframes are a rule, not a value — no utility form exists. */

@keyframes thb07-drift {
  from {
    translate: 0 0;
    scale: 1;
  }

  to {
    translate: 40px -30px;
    scale: 1.15;
  }
}
/* The one thing that MUST stay a feature query: without it, an engine with no
   backdrop-filter paints a 12%-alpha panel and page text crashes through the links. */

@supports not (backdrop-filter: blur(1px)) {
  .thb-07 .thb07-glass {
    background: oklch(0.25 0.04 280 / 0.94);
  }

  .thb-07 button[aria-controls="thb07-menu"] {
    background: oklch(0.3 0.05 280 / 0.85);
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-07 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb07-menu"]');
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
