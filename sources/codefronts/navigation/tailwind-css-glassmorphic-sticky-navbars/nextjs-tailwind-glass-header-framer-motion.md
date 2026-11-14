---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/nextjs-tailwind-glass-header-framer-motion/"
title: "Next.js Tailwind Glass Header with Framer Motion"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "The React / Next.js App Router pattern: a light glass header that frosts harder past the hero and slides away on scroll-down, back on scroll-up. The preview…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Next.js Tailwind Glass Header with Framer Motion
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/nextjs-tailwind-glass-header-framer-motion/

The React / Next.js App Router pattern: a light glass header that frosts harder past the hero and slides away on scroll-down, back on scroll-up. The preview is vanilla (two data-* attributes read by data-[scrolled=true]: and data-hidden: variants); the js field also carries the production Header.tsx using motion's useScroll.
## HTML
```html
<div class="tgn-10 w-full min-h-svh bg-tgn10-paper font-tgn10-sans">
  <div data-tgn10-stage class="relative h-svh overflow-y-auto">
    <header data-tgn10-bar data-scrolled="false" class="sticky top-0 z-10 flex h-15 items-center gap-5 border-b border-white/25 bg-white/28 px-5 backdrop-blur-sm backdrop-saturate-[1.4] transition-[translate,opacity,background-color,box-shadow,backdrop-filter,border-color] duration-300 ease-[cubic-bezier(.2,.7,.2,1)] starting:-translate-y-full starting:opacity-0 data-hidden:-translate-y-full data-[scrolled=true]:border-white/60 data-[scrolled=true]:bg-white/65 data-[scrolled=true]:shadow-[0_6px_24px_-6px_oklch(0.25_0.05_235/0.2)] data-[scrolled=true]:backdrop-blur-lg data-[scrolled=true]:backdrop-saturate-[1.8] motion-reduce:transition-none max-sm:gap-2 max-sm:px-3.5">
      <a class="flex items-center gap-2 rounded-md text-lg font-bold tracking-[-0.03em] text-tgn10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn10-acc" href="#"><span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-tgn10-ink text-[13px] font-bold text-white">L</span>Loomly</a>
      <nav class="ml-auto max-sm:hidden" aria-label="Primary">
        <ul class="flex gap-1">
          <li><a href="#" aria-current="page" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-semibold text-tgn10-text transition-colors hover:bg-white/50 aria-[current=page]:text-tgn10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn10-acc">Home</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-semibold text-tgn10-text transition-colors hover:bg-white/50 aria-[current=page]:text-tgn10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn10-acc">Features</a></li>
          <li><a href="#" class="flex h-11 items-center rounded-[10px] px-3.5 text-sm font-semibold text-tgn10-text transition-colors hover:bg-white/50 aria-[current=page]:text-tgn10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn10-acc">Pricing</a></li>
        </ul>
      </nav>
      <a href="#" class="flex h-10 items-center rounded-[10px] bg-tgn10-acc px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_rgb(255_255_255/0.2)] transition-colors hover:bg-tgn10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn10-acc max-sm:ml-auto">Get started</a>
    </header>
    <section class="-mt-15 grid min-h-80 place-items-center bg-tgn10-b bg-linear-135 from-tgn10-a via-tgn10-b to-tgn10-c px-6 pt-24 pb-14 text-center">
      <div>
        <p class="mb-3 font-tgn10-mono text-xs font-medium tracking-[0.12em] text-white/90 uppercase">app/components/Header.tsx</p>
        <h2 class="text-[clamp(28px,5vw,44px)]/[1.05] font-bold tracking-[-0.04em] text-balance text-white">A Next.js glass header, live.</h2>
      </div>
    </section>
    <section class="mx-auto max-w-2xl px-6 pt-10 pb-[60svh] text-tgn10-text [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:text-tgn10-ink [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn10-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:bg-tgn10-chip [&_code]:text-tgn10-ink">
      <p>Scroll — the bar frosts harder past the hero, exactly like the Framer Motion state flip in the code.</p>
      <p>The preview here is plain HTML/CSS/JS reproducing the same visual language: a low-blur transparent bar over the hero, a full-frost translucent bar past it, with a smooth transition between the two states.</p>
      <p>In the real component, <code>useScroll</code> from Framer Motion (now <code>motion</code>) tracks the scroll position and <code>useMotionValueEvent</code> flips a boolean past your threshold. That boolean drives the visual state — same idea, running inside React.</p>
      <h3>Why the state flip beats continuous interpolation</h3>
      <p>You could tween the frost continuously with <code>useTransform</code>, mapping scroll offset to opacity. That's tempting but tanks INP on real devices because Motion recomputes the transform on every frame.</p>
      <p>The threshold flip only updates state at one scroll position — when the boolean changes. Every other frame is a no-op. React only re-renders once, and Motion tweens between the two states over a fixed duration.</p>
      <p>The user perceives it as a smooth frost transition. The compositor perceives it as a single state change. Best of both.</p>
      <h3>Compositor-safe animation properties only</h3>
      <p>Because the transition tweens <code>opacity</code>, <code>filter</code> and <code>backdrop-filter</code> (never <code>top</code> or <code>height</code>), the animation stays on the compositor. INP stays low even during scroll.</p>
      <p>Never animate <code>height</code>, <code>padding</code>, <code>margin</code>, or <code>top</code>/<code>left</code> in response to scroll. Those trigger the layout + paint pipeline on every frame and destroy INP scores on real mobile hardware.</p>
      <p>If you must shrink the header on scroll, animate <code>padding</code> only inside a fixed-height container so the containing block never changes size. This preserves CLS 0.</p>
      <h3>The 'use client' directive</h3>
      <p>Mark the file <code>'use client'</code> because hooks like <code>useScroll</code>, <code>useMotionValueEvent</code>, and <code>useState</code> can't run in a React Server Component. A glass header that reacts to scroll is inherently client-side.</p>
      <p>The initial render matches the server output (the bar starts at its transparent state), then hydrates without visual jump. The scroll listener attaches after hydration.</p>
      <p>For the no-FOUC pattern with streaming SSR, pre-set the initial <code>data-scrolled</code> attribute in the server-rendered HTML based on route context. The client picks up the same value and never flashes.</p>
      <h3>CSS Modules variant</h3>
      <p>The full <code>Header.tsx</code> in the JS tab is copy-paste ready for the Next.js App Router. Swap Tailwind for CSS Modules by moving the utility strings into a <code>.module.css</code> file and referencing <code>styles.bar</code>.</p>
      <p>The component logic doesn't change — only the class name delivery mechanism. Same <code>useState</code>, same <code>useScroll</code>, same <code>data-scrolled</code> attribute on the bar element.</p>
      <p>CSS Modules gives you deterministic class names for SSR and no Tailwind dependency. Trade-off is verbosity — more files, more explicit selectors.</p>
      <h3>Framework portability</h3>
      <p>The same state-flip pattern works in Vue 3 with <code>ref</code> + <code>onMounted</code> attaching a scroll listener. Svelte with <code>$state</code> + <code>onMount</code>. Solid with <code>createSignal</code> + <code>createEffect</code>.</p>
      <p>Astro islands wrap this component as a client:load or client:visible hydration boundary. The scroll listener still fires client-side; the server pre-rendered the initial transparent state.</p>
      <p>Qwik uses <code>useSignal</code> + <code>useVisibleTask$</code>. The mental model is identical: track a boolean, drive the visual state from it, let CSS handle the tween.</p>
      <h3>Where this pattern belongs</h3>
      <p>SaaS marketing sites with a full-bleed hero and a sticky header. The transparent-over-hero, frost-past-hero pattern reads as premium and matches the Stripe / Linear / Vercel aesthetic.</p>
      <p>Landing pages with animated gradient heroes. The bar stays quiet over the animation and firms up over the content that follows.</p>
      <p>Product marketing pages with a scroll-through story format. The frost transition provides a subtle indicator that the user has moved past the hero without needing a separate progress indicator.</p>
      <p>Keep scrolling to feel the state flip. The bar behind the frost never moves — only its opacity, blur radius, border and shadow interpolate between the two states.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn10-paper: #f8fafd;
  --color-tgn10-paper: oklch(0.985 0.004 250);
  --color-tgn10-a: #009ee0;
  --color-tgn10-a: oklch(0.66 0.15 235);
  --color-tgn10-b: #0092b0;
  --color-tgn10-b: oklch(0.6 0.13 215);
  --color-tgn10-c: #6292e1;
  --color-tgn10-c: oklch(0.66 0.13 260);
  --color-tgn10-ink: #042234;
  --color-tgn10-ink: oklch(0.24 0.05 240);
  --color-tgn10-text: #2f3f4b;
  --color-tgn10-text: oklch(0.36 0.03 240);
  --color-tgn10-acc: #006ab4;
  --color-tgn10-acc: oklch(0.5 0.16 240);
  --color-tgn10-chip: #e4ecf3;
  --color-tgn10-chip: oklch(0.94 0.012 240);
  --font-tgn10-sans: 'Geist', system-ui, sans-serif;
  --font-tgn10-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
/* Preview behaviour — stand-in for the Framer Motion state in Header.tsx below. */
(() => {
  document.querySelectorAll('[data-tgn10-stage]').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';
    const bar = stage.querySelector('[data-tgn10-bar]');
    let last = 0, queued = false;
    const update = () => {
      const y = stage.scrollTop;
      bar.dataset.scrolled = y > 60 ? 'true' : 'false';
      bar.toggleAttribute('data-hidden', y > last && y > 240 && !bar.matches(':focus-within'));
      last = y;
      queued = false;
    };
    stage.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(update); } }, { passive: true });
  });
})();

/* ── app/components/Header.tsx — Next.js App Router + motion + Tailwind v4 ──
'use client';
import { useState } from 'react';
import { motion, useScroll, useMotionValueEvent } from 'motion/react';

const link = 'flex h-11 items-center rounded-[10px] px-3.5 text-sm font-semibold text-slate-600 hover:bg-white/50 aria-[current=page]:text-slate-900';

export default function Header() {
  const [scrolled, setScrolled] = useState(false);
  const [hidden, setHidden] = useState(false);
  const { scrollY } = useScroll();

  useMotionValueEvent(scrollY, 'change', (y) => {
    const prev = scrollY.getPrevious() ?? 0;
    setScrolled(y > 60);
    setHidden(y > prev && y > 240);
  });

  return (
    <motion.header
      data-scrolled={scrolled}
      initial={{ y: -64, opacity: 0 }}
      animate={{ y: hidden ? -64 : 0, opacity: 1 }}
      transition={{ duration: 0.3, ease: [0.2, 0.7, 0.2, 1] }}
      className="sticky top-0 z-50 flex h-15 items-center gap-5 border-b border-white/25 bg-white/28 px-5 backdrop-blur-sm transition-[background-color,box-shadow,backdrop-filter] duration-300 data-[scrolled=true]:bg-white/65 data-[scrolled=true]:shadow-lg data-[scrolled=true]:backdrop-blur-lg"
    >
      <a href="/" className="text-lg font-bold tracking-tight text-slate-900">Loomly</a>
      <nav aria-label="Primary" className="ml-auto hidden gap-1 sm:flex">
        <a href="/" aria-current="page" className={link}>Home</a>
        <a href="/features" className={link}>Features</a>
        <a href="/pricing" className={link}>Pricing</a>
      </nav>
      <a href="/signup" className="flex h-10 items-center rounded-[10px] bg-sky-700 px-4 text-sm font-semibold text-white max-sm:ml-auto">Get started</a>
    </motion.header>
  );
}
── */
```
