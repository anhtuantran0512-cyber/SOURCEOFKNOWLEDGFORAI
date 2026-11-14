---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-gooey-menu-with-svg-filter-animation/"
title: "Tailwind CSS Gooey Menu with SVG Filter Animation"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The liquid &ldquo;metaball&rdquo; menu on a creator profile card: four social links ooze out of a gradient button like drops of ink, stretch, and snap apart."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Gooey Menu with SVG Filter Animation
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-gooey-menu-with-svg-filter-animation/

The liquid &ldquo;metaball&rdquo; menu on a creator profile card: four social links ooze out of a gradient button like drops of ink, stretch, and snap apart. One SVG filter &mdash; blur, then a contrast-crushing colour matrix &mdash; is applied with [filter:url(#tcm-04-goo)] to a blob layer only, while the crisp icons ride the identical tcm04-polar path in a separate, unfiltered layer.
## HTML
```html
<section class="tcm-04 w-full min-h-svh grid place-items-center bg-tcm04-bg bg-[radial-gradient(55%_45%_at_25%_15%,var(--color-tcm04-glow),transparent_70%),radial-gradient(50%_45%_at_85%_90%,var(--color-tcm04-glow2),transparent_70%)] px-5 py-14 font-tcm04-sans text-tcm04-ink antialiased" aria-label="Gooey SVG filter menu demo">
  <svg class="absolute size-0" aria-hidden="true" focusable="false"><defs><filter id="tcm-04-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="9" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -10"/></filter></defs></svg>
  <div class="grid w-full justify-items-center gap-7">
    <article id="tcm-04-card" class="group/goo relative grid w-full max-w-[24rem] justify-items-center overflow-hidden rounded-[2rem] bg-tcm04-card px-6 pt-8 pb-10 text-center shadow-tcm04-card ring-1 ring-tcm04-line">
      <span aria-hidden="true" class="grid size-20 place-items-center rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b text-2xl font-bold text-white shadow-tcm04-glow ring-4 ring-tcm04-card">MK</span>
      <h2 class="mt-4 text-[1.5rem] font-bold tracking-[-0.03em]">Mira Kova</h2>
      <p class="mt-1 text-[14px] text-tcm04-mut">Motion designer · Lisbon</p>
      <dl class="mt-5 grid w-full grid-cols-3 gap-2 text-center">
        <div class="rounded-2xl bg-tcm04-sunk py-3"><dt class="text-[11px] text-tcm04-mut">Shots</dt><dd class="text-lg font-bold tabular-nums">214</dd></div>
        <div class="rounded-2xl bg-tcm04-sunk py-3"><dt class="text-[11px] text-tcm04-mut">Followers</dt><dd class="text-lg font-bold tabular-nums">48k</dd></div>
        <div class="rounded-2xl bg-tcm04-sunk py-3"><dt class="text-[11px] text-tcm04-mut">Likes</dt><dd class="text-lg font-bold tabular-nums">1.2m</dd></div>
      </dl>
      <nav class="relative mt-36 size-18" aria-label="Social links">
        <div aria-hidden="true" class="absolute -inset-36 [filter:url(#tcm-04-goo)]">
          <span class="absolute top-1/2 left-1/2 -m-9 size-18 rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b"></span>
          <span class="tcm04-polar absolute top-1/2 left-1/2 -m-7 size-14 rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b [--i:0] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem] transition-[translate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] motion-reduce:transition-none"></span>
          <span class="tcm04-polar absolute top-1/2 left-1/2 -m-7 size-14 rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b [--i:1] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem] transition-[translate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] motion-reduce:transition-none"></span>
          <span class="tcm04-polar absolute top-1/2 left-1/2 -m-7 size-14 rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b [--i:2] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem] transition-[translate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] motion-reduce:transition-none"></span>
          <span class="tcm04-polar absolute top-1/2 left-1/2 -m-7 size-14 rounded-full bg-linear-to-br from-tcm04-a to-tcm04-b [--i:3] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem] transition-[translate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] motion-reduce:transition-none"></span>
        </div>
        <ul id="tcm-04-menu" class="absolute inset-0">
          <li class="absolute top-1/2 left-1/2 [--i:0] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem]">
            <a href="#tcm-04-dribbble" data-item aria-label="Dribbble" class="tcm04-polar -m-7 grid size-14 place-items-center rounded-full text-white invisible opacity-0 transition-[translate,opacity,visibility,scale] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/goo:visible group-data-open/goo:opacity-100 hover:scale-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm04-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM5 8.5c5 2 9.5 2 13.5-1M4.5 14c5-1 10 .5 13 5M9 3.5c3 3.5 5 8 6 16"/></svg></a>
          </li>
          <li class="absolute top-1/2 left-1/2 [--i:1] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem]">
            <a href="#tcm-04-instagram" data-item aria-label="Instagram" class="tcm04-polar -m-7 grid size-14 place-items-center rounded-full text-white invisible opacity-0 transition-[translate,opacity,visibility,scale] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/goo:visible group-data-open/goo:opacity-100 hover:scale-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm04-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M8 4h8a4 4 0 0 1 4 4v8a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4zM12 8.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zM17 7h.01"/></svg></a>
          </li>
          <li class="absolute top-1/2 left-1/2 [--i:2] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem]">
            <a href="#tcm-04-youtube" data-item aria-label="YouTube" class="tcm04-polar -m-7 grid size-14 place-items-center rounded-full text-white invisible opacity-0 transition-[translate,opacity,visibility,scale] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/goo:visible group-data-open/goo:opacity-100 hover:scale-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm04-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 6h10a4 4 0 0 1 4 4v4a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4v-4a4 4 0 0 1 4-4zM10.5 9.5l4.5 2.5-4.5 2.5z"/></svg></a>
          </li>
          <li class="absolute top-1/2 left-1/2 [--i:3] [--a:calc(-155deg+var(--i)*43deg)] [--r:0rem] group-data-open/goo:[--r:7.25rem]">
            <a href="#tcm-04-email" data-item aria-label="Email" class="tcm04-polar -m-7 grid size-14 place-items-center rounded-full text-white invisible opacity-0 transition-[translate,opacity,visibility,scale] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/goo:visible group-data-open/goo:opacity-100 hover:scale-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm04-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 5h18v14H3zM4 7l8 6 8-6"/></svg></a>
          </li>
        </ul>
        <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-04-menu" aria-label="Social links" class="absolute inset-0 grid cursor-pointer place-items-center rounded-full text-white transition-[rotate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/goo:rotate-225 focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-tcm04-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14"/></svg></button>
      </nav>
      <p class="mt-5 text-[13px] text-tcm04-mut">Tap to connect</p>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm04-card px-3.5 py-2 text-center font-tcm04-mono text-[11.5px] text-tcm04-mut ring-1 ring-tcm04-line ">[filter:url(#tcm-04-goo)] · blobs + icons share tcm04-polar</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm04-bg: #fdf2fa;
  --color-tcm04-bg: oklch(0.972 0.016 335.1);
  --color-tcm04-glow: #f5d0fe99;
  --color-tcm04-glow: oklch(0.903 0.073 319.6 / 0.6);
  --color-tcm04-glow2: #fecdd399;
  --color-tcm04-glow2: oklch(0.892 0.056 10 / 0.6);
  --color-tcm04-card: #fffcfe;
  --color-tcm04-card: oklch(0.994 0.004 337.3);
  --color-tcm04-sunk: #fbf2f9;
  --color-tcm04-sunk: oklch(0.97 0.013 333);
  --color-tcm04-ink: #2a0f26;
  --color-tcm04-ink: oklch(0.221 0.058 333.3);
  --color-tcm04-mut: #73506b;
  --color-tcm04-mut: oklch(0.479 0.061 335);
  --color-tcm04-line: #f2dbec;
  --color-tcm04-line: oklch(0.915 0.034 334.9);
  --color-tcm04-a: #db2777;
  --color-tcm04-a: oklch(0.592 0.218 0.6);
  --color-tcm04-b: #9333ea;
  --color-tcm04-b: oklch(0.558 0.252 302.3);
  --color-tcm04-ring: #9333ea;
  --color-tcm04-ring: oklch(0.558 0.252 302.3);
  --font-tcm04-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcm04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm04-card: 0 1px 2px oklch(0.35 0.12 340 / 0.08), 0 30px 60px -26px oklch(0.45 0.2 330 / 0.4);
  --shadow-tcm04-glow: 0 14px 30px -10px oklch(0.55 0.24 330 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-04 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm04-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: magenta night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-04:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm04-bg: #160a19;
    --color-tcm04-bg: oklch(0.17 0.035 319.4);
    --color-tcm04-glow: #86198f59;
    --color-tcm04-glow: oklch(0.452 0.192 324.6 / 0.35);
    --color-tcm04-glow2: #9d174d4d;
    --color-tcm04-glow2: oklch(0.459 0.17 3.8 / 0.3);
    --color-tcm04-card: #200f24;
    --color-tcm04-card: oklch(0.204 0.047 319.8);
    --color-tcm04-sunk: #2b1630;
    --color-tcm04-sunk: oklch(0.242 0.056 319.7);
    --color-tcm04-ink: #fdeefb;
    --color-tcm04-ink: oklch(0.965 0.023 330);
    --color-tcm04-mut: #cfa9c8;
    --color-tcm04-mut: oklch(0.778 0.061 332.5);
    --color-tcm04-line: #3b2140;
    --color-tcm04-line: oklch(0.296 0.064 321);
    --color-tcm04-a: #ec4899;
    --color-tcm04-a: oklch(0.656 0.212 354.3);
    --color-tcm04-b: #a855f7;
    --color-tcm04-b: oklch(0.627 0.233 303.9);
    --color-tcm04-ring: #f0abfc;
    --color-tcm04-ring: oklch(0.833 0.132 321.4);
  }
}

.tcm-04[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm04-bg: #160a19;
  --color-tcm04-bg: oklch(0.17 0.035 319.4);
  --color-tcm04-glow: #86198f59;
  --color-tcm04-glow: oklch(0.452 0.192 324.6 / 0.35);
  --color-tcm04-glow2: #9d174d4d;
  --color-tcm04-glow2: oklch(0.459 0.17 3.8 / 0.3);
  --color-tcm04-card: #200f24;
  --color-tcm04-card: oklch(0.204 0.047 319.8);
  --color-tcm04-sunk: #2b1630;
  --color-tcm04-sunk: oklch(0.242 0.056 319.7);
  --color-tcm04-ink: #fdeefb;
  --color-tcm04-ink: oklch(0.965 0.023 330);
  --color-tcm04-mut: #cfa9c8;
  --color-tcm04-mut: oklch(0.778 0.061 332.5);
  --color-tcm04-line: #3b2140;
  --color-tcm04-line: oklch(0.296 0.064 321);
  --color-tcm04-a: #ec4899;
  --color-tcm04-a: oklch(0.656 0.212 354.3);
  --color-tcm04-b: #a855f7;
  --color-tcm04-b: oklch(0.627 0.233 303.9);
  --color-tcm04-ring: #f0abfc;
  --color-tcm04-ring: oklch(0.833 0.132 321.4);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-04-card');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const btn = root.querySelector('[data-toggle]');
  const items = [...root.querySelectorAll('[data-item]')];
  const set = (open, focus) => {
    root.toggleAttribute('data-open', open);
    btn.setAttribute('aria-expanded', String(open));
    if (open && focus && items[0]) setTimeout(() => items[0].focus(), 220);
  };
  btn.addEventListener('click', (e) => set(!root.hasAttribute('data-open'), e.detail === 0));
  root.querySelectorAll('[data-close]').forEach((el) => el.addEventListener('click', () => set(false)));
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && root.hasAttribute('data-open')) { set(false); btn.focus(); return; }
    const k = items.indexOf(document.activeElement);
    const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    if (k < 0 || !d) return;
    e.preventDefault();
    items[(k + d + items.length) % items.length].focus();
  });
  document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) set(false); });
})();
```
