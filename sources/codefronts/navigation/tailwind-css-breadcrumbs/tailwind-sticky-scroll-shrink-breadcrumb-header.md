---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-sticky-scroll-shrink-breadcrumb-header/"
title: "Tailwind Sticky Scroll-Shrink Breadcrumb Header with Scroll-Driven Animation"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A sticky docs header whose breadcrumb trail contracts as you scroll: padding, logo and type scale all shrink into a slim pinned bar."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Scroll-Shrink Breadcrumb Header with Scroll-Driven Animation
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-sticky-scroll-shrink-breadcrumb-header/

A sticky docs header whose breadcrumb trail contracts as you scroll: padding, logo and type scale all shrink into a slim pinned bar. The shrink state is a data-shrunk attribute on the scroll container, so every contracting element reads it through group-data-shrunk: &mdash; and the whole animation-timeline alternative is documented as a two-utility swap.
## HTML
```html
<section class="tbc-07 w-full min-h-svh grid place-items-center bg-tbc07-stage font-tbc07-sans px-5 py-9">
  <div class="group w-[min(760px,100%)] h-75 overflow-y-auto rounded-2xl border border-tbc07-edge bg-tbc07-bg [scrollbar-width:thin]">
    <header class="sticky top-0 z-100 flex items-center gap-3.5 px-6 py-5 bg-white/85 backdrop-blur-[10px] border-b border-tbc07-edge shadow-none transition-[padding,box-shadow] duration-300 group-data-shrunk:py-2 group-data-shrunk:shadow-[0_4px_18px_oklch(0_0_0/0.1)] motion-reduce:transition-none">
      <span aria-hidden="true" class="flex-none w-8.5 h-8.5 rounded-[9px] bg-[conic-gradient(from_210deg,oklch(0.62_0.17_265),oklch(0.6_0.16_210))] transition-[width,height] duration-300 group-data-shrunk:w-6 group-data-shrunk:h-6 motion-reduce:transition-none"></span>
      <nav aria-label="Breadcrumb">
        <ol class="flex flex-wrap items-center list-none m-0 p-0">
          <li class="flex items-center"><a href="#" class="flex items-center px-1.5 py-1 rounded-md text-[15px] font-semibold text-tbc07-link no-underline transition-[font-size,color] duration-300 hover:text-tbc07-linkhover focus-visible:outline-2 focus-visible:outline-tbc07-acc focus-visible:outline-offset-2 group-data-shrunk:text-[13px] motion-reduce:transition-none">Home</a></li>
          <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc07-sep"><a href="#" class="flex items-center px-1.5 py-1 rounded-md text-[15px] font-semibold text-tbc07-link no-underline transition-[font-size,color] duration-300 hover:text-tbc07-linkhover focus-visible:outline-2 focus-visible:outline-tbc07-acc focus-visible:outline-offset-2 group-data-shrunk:text-[13px] motion-reduce:transition-none">Docs</a></li>
          <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc07-sep"><a href="#" aria-current="page" class="flex items-center px-1.5 py-1 rounded-md text-[15px] font-bold text-tbc07-strong no-underline transition-[font-size] duration-300 focus-visible:outline-2 focus-visible:outline-tbc07-acc focus-visible:outline-offset-2 group-data-shrunk:text-[13px] motion-reduce:transition-none">Scroll-driven UI</a></li>
        </ol>
      </nav>
    </header>
    <div id="tbc07-sentinel" aria-hidden="true" class="h-px"></div>
    <div class="px-6 pt-6 pb-10">
      <h1 class="m-0 mb-2 text-[22px]/[1.3] font-bold text-tbc07-h">Scroll-driven sticky breadcrumb header</h1>
      <p class="max-w-[60ch] m-0 mb-5 text-[15px]/[1.55] font-medium text-tbc07-body">Scroll this panel and watch the header compress into a slim pinned bar. Padding, logo size and type scale all contract from one <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">data-shrunk</code> attribute.</p>
      <h2 class="mt-6 mb-1.5 text-[15px]/[1.3] font-bold text-tbc07-h">How the shrink is wired</h2>
      <p class="max-w-[60ch] m-0 mb-3.5 text-sm/[1.65] text-tbc07-body">A 1px sentinel sits below the header. An <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">IntersectionObserver</code> scoped to this panel toggles the attribute when it scrolls out of view, and every <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">group-data-shrunk:</code> utility answers.</p>
      <h2 class="mt-6 mb-1.5 text-[15px]/[1.3] font-bold text-tbc07-h">The pure-CSS alternative</h2>
      <p class="max-w-[60ch] m-0 mb-3.5 text-sm/[1.65] text-tbc07-body">Swap the observer for <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">animate-tbc07-shrink [animation-timeline:scroll(nearest)]</code> on the header. The keyframes ship in the stylesheet; the observer ships because it runs everywhere.</p>
      <h2 class="mt-6 mb-1.5 text-[15px]/[1.3] font-bold text-tbc07-h">Accessibility contract</h2>
      <p class="max-w-[60ch] m-0 mb-3.5 text-sm/[1.65] text-tbc07-body">Both states hold AA contrast against the frosted bar, the trail keeps its landmark and <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">aria-current</code>, and <code class="px-1.5 py-0.5 rounded font-tbc07-mono text-[12.5px] bg-tbc07-code text-tbc07-codeink">motion-reduce:transition-none</code> turns the contraction into an instant swap rather than a slow one.</p>
      <p class="max-w-[60ch] m-0 mb-3.5 text-sm/[1.65] text-tbc07-body">Keep scrolling &mdash; the shrink holds at the compact size and expands again when the sentinel returns. The animation is bidirectional because the attribute is.</p>
      <p class="max-w-[60ch] m-0 text-sm/[1.65] text-tbc07-body">End of scroll region.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc07-stage: #f1f2f6;
  --color-tbc07-stage: oklch(0.95 0.005 255);
  --color-tbc07-bg: #f8f9fb;
  --color-tbc07-bg: oklch(0.97 0.006 255);
  --color-tbc07-edge: #e0e2e9;
  --color-tbc07-edge: oklch(0.9 0.01 255);
  --color-tbc07-link: #5163b5;
  --color-tbc07-link: oklch(0.5 0.1 260);
  --color-tbc07-linkhover: #3f52a6;
  --color-tbc07-linkhover: oklch(0.42 0.14 260);
  --color-tbc07-strong: #35383f;
  --color-tbc07-strong: oklch(0.28 0.02 255);
  --color-tbc07-sep: #adb0ba;
  --color-tbc07-sep: oklch(0.72 0.02 255);
  --color-tbc07-h: #303339;
  --color-tbc07-h: oklch(0.26 0.02 255);
  --color-tbc07-body: #5b5f68;
  --color-tbc07-body: oklch(0.45 0.02 255);
  --color-tbc07-code: #eaecf1;
  --color-tbc07-code: oklch(0.93 0.01 255);
  --color-tbc07-codeink: #464b5c;
  --color-tbc07-codeink: oklch(0.38 0.04 260);
  --color-tbc07-acc: #4457b3;
  --color-tbc07-acc: oklch(0.5 0.15 260);
  --font-tbc07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbc07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbc07-shrink: tbc07-shrink linear both;
}
/* The scroll-driven alternative: keyframes cannot be utilities, so they stay here.
   Add animate-tbc07-shrink [animation-timeline:scroll(nearest)] to the header and
   delete the IntersectionObserver. */

@keyframes tbc07-shrink {
  0%,
    8% {
    padding-block: 1.25rem;
  }

  20%,
    100% {
    padding-block: 0.5rem;
    box-shadow: 0 4px 18px oklch(0 0 0 / 0.1);
  }
}

.tbc-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tbc-07 > .group').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var sentinel = root.querySelector('#tbc07-sentinel');
    new IntersectionObserver(function (entries) {
      root.toggleAttribute('data-shrunk', !entries[0].isIntersecting);
    }, { root: root, threshold: 0 }).observe(sentinel);
  });
})();
```
