---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-transparent-navbar-frosted-glass-on-scroll/"
title: "Tailwind Transparent Navbar That Turns Frosted Glass on Scroll"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "A header that is fully transparent over a full-bleed photo and frosts into glass as you scroll &mdash; driven by CSS animation-timeline: scroll(), with no…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Transparent Navbar That Turns Frosted Glass on Scroll
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/tailwind-transparent-navbar-frosted-glass-on-scroll/

A header that is fully transparent over a full-bleed photo and frosts into glass as you scroll &mdash; driven by CSS animation-timeline: scroll(), with no scroll listener. Because Tailwind can't guarantee that a timeline utility is emitted after the animation shorthand that resets it, the three animation lines live in one custom @utility, applied behind supports-[animation-timeline:scroll()]:.
## HTML
```html
<div class="tgn-02 w-full min-h-svh bg-tgn02-paper font-tgn02-sans">
  <div data-tgn02-stage class="relative h-svh overflow-y-auto scroll-smooth">
    <header data-tgn02-bar class="sticky top-0 z-10 flex h-16 items-center gap-6 border-b border-transparent px-5 text-white supports-[animation-timeline:scroll()]:motion-safe:tgn02-frost data-stuck:bg-white/60 data-stuck:text-tgn02-ink data-stuck:border-b-white/50 data-stuck:shadow-[0_6px_24px_-6px_oklch(0.2_0.03_250/0.25)] data-stuck:backdrop-blur-[14px] data-stuck:backdrop-saturate-[1.7] motion-reduce:bg-white/60 motion-reduce:text-tgn02-ink motion-reduce:border-b-white/50 motion-reduce:shadow-[0_6px_24px_-6px_oklch(0.2_0.03_250/0.25)] motion-reduce:backdrop-blur-[14px] transition-colors duration-300 max-sm:gap-3 max-sm:px-3.5">
      <a class="rounded-md font-tgn02-serif text-[26px] leading-none tracking-[-0.01em] text-current italic focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-current" href="#">Vista</a>
      <nav class="ml-auto" aria-label="Primary">
        <ul class="flex gap-1 max-sm:gap-0">
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3 text-sm font-semibold text-current transition-colors hover:bg-current/12 aria-[current=page]:underline aria-[current=page]:decoration-2 aria-[current=page]:underline-offset-[6px] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current max-sm:px-2.5 max-sm:text-[13px]">Stays</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3 text-sm font-semibold text-current transition-colors hover:bg-current/12 aria-[current=page]:underline aria-[current=page]:decoration-2 aria-[current=page]:underline-offset-[6px] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current max-sm:px-2.5 max-sm:text-[13px]">Experiences</a></li>
          <li><a href="#" aria-current="page" class="flex h-11 items-center rounded-[10px] px-3 text-sm font-semibold text-current transition-colors hover:bg-current/12 aria-[current=page]:underline aria-[current=page]:decoration-2 aria-[current=page]:underline-offset-[6px] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current max-sm:px-2.5 max-sm:text-[13px]">Guides</a></li>
        </ul>
      </nav>
    </header>
    <section class="-mt-16 flex min-h-[78svh] items-end bg-tgn02-dusk bg-[linear-gradient(180deg,oklch(0.2_0.05_260/0.35),transparent_30%,oklch(0.15_0.05_260/0.7)),url(https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1800&auto=format&fit=crop)] bg-cover bg-center px-5 pt-28 pb-10 sm:px-8 sm:pb-14">
      <div class="max-w-xl">
        <h2 class="font-tgn02-serif text-[clamp(40px,7vw,72px)]/[0.98] tracking-[-0.02em] text-balance text-white [text-shadow:0_2px_30px_oklch(0_0_0/0.35)]">Wake up somewhere <em>better.</em></h2>
        <p class="mt-4 text-[15px]/relaxed font-medium text-white/90">Scroll &mdash; the bar frosts as the photo slides under it.</p>
      </div>
    </section>
    <section class="mx-auto max-w-2xl px-6 pt-10 pb-24 text-tgn02-body sm:px-8 [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_p]:text-base/[1.7] [&_p]:font-normal [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-tgn02-ink [&_h3]:font-tgn02-serif [&_h3]:text-[26px] [&_h3]:font-normal [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn02-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:bg-tgn02-chip [&_code]:text-tgn02-ink">
      <p>Scroll — the transparent bar frosts into glass as you move down the page.</p>
      <p>All of it driven by <code>animation-timeline: scroll()</code>, no JS on the modern path. The browser interpolates the keyframes from the scroll position; there is no <code>scroll</code> listener anywhere.</p>
      <p>Every glass surface pairs <code>backdrop-filter: blur() saturate()</code> with a semi-transparent fill and a 1px hairline — the trio that makes the pane read as physical glass rather than a washed-out box.</p>
      <p>The <code>animation-range</code> value is the tuning dial: shorten it to frost sooner, lengthen it to keep the transparent state longer while the hero is still in view.</p>
      <p>Everything runs on the compositor, so scrolling stays at 60fps even as the frost re-samples the moving content behind it.</p>
      <h3>Why this beats the JS scroll-handler pattern</h3>
      <p>The 2018-2023 pattern was: attach a <code>scroll</code> event listener, read <code>window.scrollY</code>, imperatively toggle a class past a threshold. That reads the DOM on every scroll frame and forces a style recalc.</p>
      <p>On a real mid-tier Android device, that pattern tanks Interaction to Next Paint by 20-40ms per frame. On a high-end desktop you never notice; in the field, Google's Core Web Vitals report catches it.</p>
      <p>Scroll-driven animations move the entire computation to the compositor thread. The main thread stays free for touch handlers, text input, hydration — the things that actually matter for INP.</p>
      <h3>The IntersectionObserver fallback</h3>
      <p>For engines without scroll-driven animations (before Chrome 115, Firefox 129, Safari 26), the fallback uses a 1px sentinel element inserted at the top of the hero. An <code>IntersectionObserver</code> toggles <code>.is-stuck</code> on the bar when the sentinel leaves the viewport.</p>
      <p>Detection is a single line: <code>if (!CSS.supports('animation-timeline: scroll()'))</code>. Modern browsers get the CSS path; older ones get identical visual behaviour via 8 lines of JS. See the JS tab for the copy-paste snippet.</p>
      <p>The observer callback runs once per intersection change, not per scroll frame. Even in the fallback path, the main thread stays quiet.</p>
      <h3>Design decisions worth knowing</h3>
      <p>Keep the transparent-state text light (white with a subtle text-shadow) and the frosted-state text dark. Interpolating <code>color</code> across the range handles the crossover automatically as the fill lightens.</p>
      <p>Extend the animation to tween more than fill + blur. Shrinking the bar's <code>height</code> from 72px to 56px as it frosts is a common polish move — but keep it above 48px for touch targets to stay compliant.</p>
      <p>Add a <code>box-shadow</code> that only appears in the frosted state to lift the bar off the page. A tight, low-opacity shadow reads as elevation without competing with the frost itself.</p>
      <p>Test with a slow-motion scroll (Chrome DevTools has a slow-scroll toggle) to confirm the interpolation looks smooth across the full range, not just at the endpoints.</p>
      <p>Keep scrolling — the bar stays pinned and frosted, letting content pass underneath cleanly.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@keyframes tgn02frost {
  to {
    background-color: rgb(255 255 255 / 0.6);
    color: var(--color-tgn02-ink);
    border-bottom-color: rgb(255 255 255 / 0.5);
    -webkit-backdrop-filter: blur(14px) saturate(170%);
    backdrop-filter: blur(14px) saturate(170%);
    box-shadow: 0 6px 24px -6px oklch(0.2 0.03 250 / 0.25);
  }
}
/* One utility on purpose: the animation shorthand resets animation-timeline, so the three lines
   must be emitted together and in this order. */

@utility tgn02-frost {
  animation: tgn02frost linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 200px;
}

@theme {
  --color-tgn02-paper: #fcfaf6;
  --color-tgn02-paper: oklch(0.985 0.005 80);
  --color-tgn02-dusk: #543282;
  --color-tgn02-dusk: oklch(0.4 0.13 300);
  --color-tgn02-ink: #14202d;
  --color-tgn02-ink: oklch(0.24 0.03 250);
  --color-tgn02-body: #404952;
  --color-tgn02-body: oklch(0.4 0.02 250);
  --color-tgn02-chip: #e6ecf2;
  --color-tgn02-chip: oklch(0.94 0.01 250);
  --font-tgn02-serif: 'Instrument Serif', Georgia, serif;
  --font-tgn02-sans: 'Manrope', system-ui, sans-serif;
  --font-tgn02-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-02 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
/* Modern path is pure CSS (tgn02-frost). Fallback for engines without scroll timelines:
   a sentinel below the top of the stage toggles data-stuck on the header. */
(() => {
  if (CSS.supports('animation-timeline: scroll()')) return;
  document.querySelectorAll('[data-tgn02-stage]').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';
    const bar = stage.querySelector('[data-tgn02-bar]');
    const sentinel = Object.assign(document.createElement('div'), { ariaHidden: 'true' });
    sentinel.style.cssText = 'position:absolute;top:180px;height:1px;width:1px';
    stage.prepend(sentinel);
    new IntersectionObserver(([e]) => bar.toggleAttribute('data-stuck', !e.isIntersecting), { root: stage }).observe(sentinel);
  });
})();
```
