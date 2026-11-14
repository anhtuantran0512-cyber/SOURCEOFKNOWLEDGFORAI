---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-hamburger-menu-morphing-to-close-icon-animation/"
title: "Tailwind Hamburger Menu Morphing to Close Icon Animation"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Not a rotate trick &mdash; a true shape morph."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hamburger Menu Morphing to Close Icon Animation
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-hamburger-menu-morphing-to-close-icon-animation/

Not a rotate trick &mdash; a true shape morph. The line geometry lives in CSS as d: path(), and because that property is animatable the browser interpolates the actual coordinates from &#9776; to &#10005;. This is also the collection's clearest example of a technique that must NOT become a utility: path data plus its @supports fallback belongs in the stylesheet, and the markup stays utility-only.
## HTML
```html
<section class="thb-10 w-full min-h-svh bg-thb10-bg font-thb10-sans text-thb10-ink px-5 py-9" aria-label="SVG path morph hamburger icon demo">
  <div class="min-h-100 flex flex-col items-center justify-center gap-4.5 p-6.5 rounded-[18px] border border-thb10-edge bg-thb10-bg">
    <div class="group w-[min(420px,100%)] overflow-hidden rounded-2xl border-[1.5px] border-thb10-ink bg-thb10-panel shadow-[5px_5px_0_oklch(0.2_0.01_90/0.1)]">
      <header class="flex items-center justify-between p-3.5 pl-5">
        <span class="text-[15.5px] font-bold tracking-[-0.01em]">monoline<i class="not-italic align-super text-[10px] text-thb10-mut">&reg;</i></span>
        <button type="button" aria-expanded="false" aria-controls="thb10-panel" aria-label="Open menu" class="grid place-items-center w-11.5 h-11.5 rounded-xl border-[1.5px] border-thb10-ink bg-thb10-panel text-thb10-ink cursor-pointer transition-[background,color,translate] duration-200 hover:bg-thb10-ink hover:text-thb10-panel active:translate-x-px active:translate-y-px focus-visible:outline-2 focus-visible:outline-thb10-acc focus-visible:outline-offset-3">
          <svg class="thb10-ico" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
            <path class="thb10-top fill-none stroke-current stroke-2 [stroke-linecap:round]" d="M 3 6 L 21 6"/>
            <path class="thb10-mid fill-none stroke-current stroke-2 [stroke-linecap:round]" d="M 3 12 L 21 12"/>
            <path class="thb10-bot fill-none stroke-current stroke-2 [stroke-linecap:round]" d="M 3 18 L 21 18"/>
          </svg>
        </button>
      </header>
      <nav id="thb10-panel" aria-label="Primary" class="grid opacity-0 [grid-template-rows:0fr] transition-[grid-template-rows,opacity] duration-400 ease-thb10 group-data-open:opacity-100 group-data-open:[grid-template-rows:1fr] motion-reduce:transition-none">
        <ul class="list-none min-h-0 overflow-hidden">
          <li><a href="#shop" class="flex items-center justify-between min-h-13 px-5 border-t-[1.5px] border-thb10-ink no-underline text-[15px] font-bold tracking-[0.02em] uppercase text-thb10-ink transition-[background,color,padding] duration-150 hover:bg-thb10-ink hover:text-thb10-panel hover:pl-6.5 focus-visible:bg-thb10-ink focus-visible:text-thb10-panel focus-visible:outline-2 focus-visible:outline-thb10-acc focus-visible:-outline-offset-4">Shop<span aria-hidden="true">&rarr;</span></a></li>
          <li><a href="#lookbook" class="flex items-center justify-between min-h-13 px-5 border-t-[1.5px] border-thb10-ink no-underline text-[15px] font-bold tracking-[0.02em] uppercase text-thb10-ink transition-[background,color,padding] duration-150 hover:bg-thb10-ink hover:text-thb10-panel hover:pl-6.5 focus-visible:bg-thb10-ink focus-visible:text-thb10-panel focus-visible:outline-2 focus-visible:outline-thb10-acc focus-visible:-outline-offset-4">Lookbook<span aria-hidden="true">&rarr;</span></a></li>
          <li><a href="#stores" class="flex items-center justify-between min-h-13 px-5 border-t-[1.5px] border-thb10-ink no-underline text-[15px] font-bold tracking-[0.02em] uppercase text-thb10-ink transition-[background,color,padding] duration-150 hover:bg-thb10-ink hover:text-thb10-panel hover:pl-6.5 focus-visible:bg-thb10-ink focus-visible:text-thb10-panel focus-visible:outline-2 focus-visible:outline-thb10-acc focus-visible:-outline-offset-4">Stores<span aria-hidden="true">&rarr;</span></a></li>
          <li><a href="#journal" class="flex items-center justify-between min-h-13 px-5 border-t-[1.5px] border-thb10-ink no-underline text-[15px] font-bold tracking-[0.02em] uppercase text-thb10-ink transition-[background,color,padding] duration-150 hover:bg-thb10-ink hover:text-thb10-panel hover:pl-6.5 focus-visible:bg-thb10-ink focus-visible:text-thb10-panel focus-visible:outline-2 focus-visible:outline-thb10-acc focus-visible:-outline-offset-4">Journal<span aria-hidden="true">&rarr;</span></a></li>
        </ul>
      </nav>
    </div>
    <p class="w-[min(420px,100%)] text-center text-xs leading-relaxed text-thb10-mut text-pretty" aria-hidden="true">the <code class="font-thb10-mono text-[11px] px-1.5 py-0.5 rounded bg-thb10-code">d</code> attribute itself is transitioning &mdash; slow it in DevTools and watch the endpoints travel</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb10-bg: #f8f8f5;
  --color-thb10-bg: oklch(0.97 0.003 90);
  --color-thb10-panel: #ffffff;
  --color-thb10-panel: oklch(1 0 0);
  --color-thb10-edge: #dededa;
  --color-thb10-edge: oklch(0.88 0.005 90);
  --color-thb10-code: #e9e9e5;
  --color-thb10-code: oklch(0.92 0.005 90);
  --color-thb10-ink: #2b2a27;
  --color-thb10-ink: oklch(0.2 0.01 90);
  --color-thb10-mut: #77756f;
  --color-thb10-mut: oklch(0.52 0.01 90);
  --color-thb10-acc: #cf5327;
  --color-thb10-acc: oklch(0.62 0.19 30);
  --font-thb10-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb10: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Path geometry stays CSS on purpose: arbitrary values mangle the spaces inside
   path data, and the fallback below has to be a feature query anyway. */

.thb-10 .thb10-top,
.thb-10 .thb10-mid,
.thb-10 .thb10-bot {
  transition: d .45s cubic-bezier(0.65, 0, 0.35, 1), opacity .3s;
}

.thb-10 .thb10-top {
  d: path("M 3 6 L 21 6");
}

.thb-10 .thb10-mid {
  d: path("M 3 12 L 21 12");
}

.thb-10 .thb10-bot {
  d: path("M 3 18 L 21 18");
}

.thb-10 [data-open] .thb10-top {
  d: path("M 5 5 L 19 19");
}

.thb-10 [data-open] .thb10-mid {
  d: path("M 12 12 L 12 12");
  opacity: 0;
}

.thb-10 [data-open] .thb10-bot {
  d: path("M 5 19 L 19 5");
}

@supports not (d: path("M0 0h1")) {
  .thb-10 .thb10-ico path {
    transition: translate .3s, rotate .3s .05s, opacity .2s;
    transform-origin: 12px 12px;
  }

  .thb-10 [data-open] .thb10-top {
    translate: 0 6px;
    rotate: 45deg;
  }

  .thb-10 [data-open] .thb10-mid {
    opacity: 0;
  }

  .thb-10 [data-open] .thb10-bot {
    translate: 0 -6px;
    rotate: -45deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .thb-10 .thb10-ico path {
    transition-duration: .01s;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-10 div.group').forEach(function (bar) {
    if (bar.dataset.bound) return; bar.dataset.bound = '1';
    var btn = bar.querySelector('button[aria-controls="thb10-panel"]');
    function set(open) {
      bar.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    bar.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && bar.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
