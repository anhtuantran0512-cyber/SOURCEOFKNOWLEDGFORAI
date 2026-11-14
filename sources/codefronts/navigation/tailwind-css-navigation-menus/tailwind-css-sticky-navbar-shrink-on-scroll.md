---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-sticky-navbar-shrink-on-scroll/"
title: "Tailwind CSS Sticky Navbar That Shrinks on Scroll"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A sticky, frosted header that compresses from 72px to 52px, tightens its logo and buttons and gains a soft shadow once you scroll."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Sticky Navbar That Shrinks on Scroll
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-sticky-navbar-shrink-on-scroll/

A sticky, frosted header that compresses from 72px to 52px, tightens its logo and buttons and gains a soft shadow once you scroll. An IntersectionObserver sentinel flips one data-shrunk attribute; every visual change is a data-shrunk: or group-data-shrunk/bar: utility. The reading-progress bar is a CSS scroll-driven animation, with a JS fallback only where unsupported.
## HTML
```html
<div class="tnv-06 relative w-full min-h-svh bg-tnv06-bg font-tnv06-sans text-tnv06-ink antialiased selection:bg-tnv06-acc selection:text-white">
  <div id="tnv06-sentinel" aria-hidden="true" class="pointer-events-none absolute top-0 left-0 h-[60px] w-px"></div>
  <div id="tnv06-progress" data-tnv06-progress aria-hidden="true" class="fixed inset-x-0 top-0 z-50 h-[3px] origin-left bg-linear-to-r from-tnv06-acc to-tnv06-acc2 [scale:0_1]"></div>
  <nav id="tnv06-bar" aria-label="Main" class="group/bar sticky top-0 z-40 flex h-18 items-center justify-between gap-6 border-b border-tnv06-line bg-white/85 px-5 backdrop-blur-lg transition-[height,box-shadow,border-color] duration-300 ease-out data-shrunk:h-13 data-shrunk:border-tnv06-acc/20 data-shrunk:shadow-[0_8px_30px_-12px_var(--color-tnv06-shadow)] sm:px-12 motion-reduce:transition-none">
    <a href="#" class="flex origin-left items-center gap-2.5 text-xl font-bold tracking-[-0.02em] transition-transform duration-300 group-data-shrunk/bar:scale-90">
      <span class="grid size-7 place-items-center rounded-[50%_0_50%_50%] bg-tnv06-acc transition-[width,height] duration-300 group-data-shrunk/bar:size-6"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.25" aria-hidden="true"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0112 2a8 8 0 018 8.2c0 7.3-8 11.8-8 11.8z"/></svg></span>Verdant
    </a>
    <ul class="hidden items-center gap-1 text-sm font-semibold text-tnv06-mut md:flex [&_a]:flex [&_a]:h-10 [&_a]:items-center [&_a]:rounded-lg [&_a]:px-3.5 [&_a]:transition-colors [&_a:hover]:bg-tnv06-soft [&_a:hover]:text-tnv06-ink [&_a[aria-current]]:bg-tnv06-soft [&_a[aria-current]]:text-tnv06-acc-ink">
      <li><a href="#" aria-current="page">Home</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
    </ul>
    <div class="flex items-center gap-2.5">
      <a href="#" class="hidden h-10 items-center rounded-lg border-[1.5px] border-tnv06-line px-4 text-sm font-semibold text-tnv06-acc-ink transition-[height,padding,border-color] duration-300 hover:border-tnv06-acc2 group-data-shrunk/bar:h-9 group-data-shrunk/bar:px-3.5 sm:inline-flex">Log in</a>
      <a href="#" class="inline-flex h-10 items-center rounded-lg bg-tnv06-acc px-4 text-sm font-semibold text-white shadow-[0_6px_16px_-6px_var(--color-tnv06-acc)] transition-[height,padding,filter] duration-300 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv06-acc group-data-shrunk/bar:h-9 group-data-shrunk/bar:px-3.5">Try free</a>
    </div>
  </nav>
  <main class="mx-auto min-h-[200svh] max-w-3xl px-5 sm:px-12 [&_code]:rounded [&_code]:bg-tnv06-soft [&_code]:px-1.5 [&_code]:font-tnv06-mono [&_code]:text-[0.85em] [&_code]:text-tnv06-acc-ink">
    <section class="py-24">
      <h1 class="text-[clamp(2.5rem,6vw,4.25rem)] leading-[1.04] font-bold tracking-[-0.045em] text-balance">Sticky nav that <span class="text-tnv06-acc">shrinks on scroll</span></h1>
      <p class="mt-5 max-w-xl text-[17px]/[1.7] text-tnv06-mut text-pretty">Scroll down. The bar compresses from 72px to 52px, the logo and buttons tighten, and a shadow lifts it off the page. JS flips one attribute; Tailwind does the rest.</p>
      <p class="mt-8 inline-flex items-center gap-2 text-sm font-bold text-tnv06-acc-ink"><svg class="size-[18px] animate-bounce motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg>Scroll to trigger</p>
    </section>
    <div class="grid gap-5 pb-32 [&>article]:rounded-2xl [&>article]:border [&>article]:border-tnv06-line [&>article]:bg-white [&>article]:p-7 [&_h2]:text-lg [&_h2]:font-bold [&_h2]:tracking-[-0.01em] [&_article_p]:mt-2 [&_article_p]:text-[15px]/[1.7] [&_article_p]:text-tnv06-mut">
      <article><h2>How it works</h2><p>An <code>IntersectionObserver</code> watches a 60px sentinel at the top of the page. When it scrolls out of view the nav gets <code>data-shrunk</code>, and utilities like <code>data-shrunk:h-13</code> take over.</p></article>
      <article><h2>Performance</h2><p>No scroll handler decides the shrink. The progress bar uses <code>animation-timeline: scroll()</code> where supported, so in modern browsers the page scrolls with zero JavaScript running.</p></article>
      <article><h2>Accessibility</h2><p>The shrink is purely visual. Focus order, landmarks and the 40px+ hit areas are unchanged, and <code>motion-reduce:</code> removes the transitions entirely.</p></article>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv06-bg: #f0fdf4;
  --color-tnv06-bg: oklch(0.982 0.018 155);
  --color-tnv06-soft: #ecfdf5;
  --color-tnv06-soft: oklch(0.979 0.021 166);
  --color-tnv06-line: #d1fae5;
  --color-tnv06-line: oklch(0.95 0.052 163);
  --color-tnv06-ink: #052e16;
  --color-tnv06-ink: oklch(0.266 0.065 153);
  --color-tnv06-mut: #4b5563;
  --color-tnv06-mut: oklch(0.446 0.026 257);
  --color-tnv06-acc: #059669;
  --color-tnv06-acc: oklch(0.596 0.145 163);
  --color-tnv06-acc2: #34d399;
  --color-tnv06-acc2: oklch(0.765 0.177 163);
  --color-tnv06-acc-ink: #047857;
  --color-tnv06-acc-ink: oklch(0.508 0.118 166);
  --color-tnv06-shadow: #05966940;
  --color-tnv06-shadow: oklch(0.596 0.145 163 / 0.25);
  --font-tnv06-sans: 'Figtree', system-ui, sans-serif;
  --font-tnv06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-06 {
  width: 100%;
  min-height: 100svh;
}
/* Scroll-driven progress: the one thing left in CSS. The animation shorthand resets
   animation-timeline, so the pair must be declared together in source order. */

@keyframes tnv06-progress {
  from {
    scale: 0 1;
  }

  to {
    scale: 1 1;
  }
}

@supports (animation-timeline: scroll()) {
  .tnv-06 [data-tnv06-progress] {
    animation: tnv06-progress linear both;
    animation-timeline: scroll(root);
  }
}
```

## JavaScript
```js
(() => {
  const bar = document.getElementById('tnv06-bar');
  const sentinel = document.getElementById('tnv06-sentinel');
  const prog = document.getElementById('tnv06-progress');
  if (!bar || bar.dataset.wired) return;
  bar.dataset.wired = '1';
  new IntersectionObserver(([entry]) => {
    bar.toggleAttribute('data-shrunk', !entry.isIntersecting);
  }).observe(sentinel);
  if (CSS.supports('animation-timeline: scroll()')) return;
  let ticking = false;
  const update = () => {
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    prog.style.scale = (max > 0 ? Math.min(scrollY / max, 1) : 0) + ' 1';
    ticking = false;
  };
  addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  update();
})();
```
