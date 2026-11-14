---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/react-next-js-component-pattern/"
title: "React / Next.js Component Pattern"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The nextjs-sticky-glass-header-framer-motion pattern: a reusable client component with a smooth entrance animation, a sticky blur state that intensifies once…"
has_js: "true"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: React / Next.js Component Pattern
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/react-next-js-component-pattern/

The nextjs-sticky-glass-header-framer-motion pattern: a reusable client component with a smooth entrance animation, a sticky blur state that intensifies once you scroll past the hero, and clean Tailwind / CSS-Modules styling. The preview below is a faithful vanilla render; the js field holds the real Next.js + Framer Motion component you'd drop into app/.
## HTML
```html
<div class="gn-10">
  <div class="gn-10__stage">
    <header class="gn-10-bar" data-scrolled="false">
      <a class="gn-10-brand" href="#">Loomly</a>
      <nav aria-label="Primary">
        <ul>
          <li><a href="#" aria-current="page">Home</a></li>
          <li><a href="#">Features</a></li>
          <li><a href="#">Pricing</a></li>
        </ul>
      </nav>
      <a class="gn-10-cta" href="#">Get started</a>
    </header>
    <section class="gn-10-hero"><h2>A Next.js glass header, live.</h2></section>
    <section class="gn-10-body">
      <p>Scroll &mdash; the bar frosts harder past the hero, exactly like the Framer Motion state flip in the code.</p>
      <p>The preview here is plain HTML/CSS/JS reproducing the same visual language: a low-blur transparent bar over the hero, a full-frost translucent bar past it, with a smooth transition between the two states.</p>
      <p>In the real component, <code>useScroll</code> from Framer Motion (now <code>motion</code>) tracks the scroll position and <code>useMotionValueEvent</code> flips a boolean past your threshold. That boolean drives the visual state &mdash; same idea, running inside React.</p>
      <h3>Why the state flip beats continuous interpolation</h3>
      <p>You could tween the frost continuously with <code>useTransform</code>, mapping scroll offset to opacity. That's tempting but tanks INP on real devices because Motion recomputes the transform on every frame.</p>
      <p>The threshold flip only updates state at one scroll position &mdash; when the boolean changes. Every other frame is a no-op. React only re-renders once, and Motion tweens between the two states over a fixed duration.</p>
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
      <p>The component logic doesn't change &mdash; only the class name delivery mechanism. Same <code>useState</code>, same <code>useScroll</code>, same <code>data-scrolled</code> attribute on the bar element.</p>
      <p>CSS Modules gives you deterministic class names for SSR and no Tailwind dependency. Trade-off is verbosity &mdash; more files, more explicit selectors.</p>
      <h3>Framework portability</h3>
      <p>The same state-flip pattern works in Vue 3 with <code>ref</code> + <code>onMounted</code> attaching a scroll listener. Svelte with <code>$state</code> + <code>onMount</code>. Solid with <code>createSignal</code> + <code>createEffect</code>.</p>
      <p>Astro islands wrap this component as a client:load or client:visible hydration boundary. The scroll listener still fires client-side; the server pre-rendered the initial transparent state.</p>
      <p>Qwik uses <code>useSignal</code> + <code>useVisibleTask$</code>. The mental model is identical: track a boolean, drive the visual state from it, let CSS handle the tween.</p>
      <h3>Where this pattern belongs</h3>
      <p>SaaS marketing sites with a full-bleed hero and a sticky header. The transparent-over-hero, frost-past-hero pattern reads as premium and matches the Stripe / Linear / Vercel aesthetic.</p>
      <p>Landing pages with animated gradient heroes. The bar stays quiet over the animation and firms up over the content that follows.</p>
      <p>Product marketing pages with a scroll-through story format. The frost transition provides a subtle indicator that the user has moved past the hero without needing a separate progress indicator.</p>
      <p>Keep scrolling to feel the state flip. The bar behind the frost never moves &mdash; only its opacity, blur radius, border and shadow interpolate between the two states.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.gn-10 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: oklch(0.98 0.005 265);
}

.gn-10 * {
  box-sizing: border-box;
}

.gn-10__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.gn-10-bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 20px;
  height: 58px;
  padding: 0 18px;
  background: rgba(255,255,255,.28);
  border-bottom: 1px solid rgba(255,255,255,.25);
  -webkit-backdrop-filter: blur(6px) saturate(140%);
  backdrop-filter: blur(6px) saturate(140%);
  transition: background-color .3s ease,box-shadow .3s ease,backdrop-filter .3s ease,-webkit-backdrop-filter .3s ease;
  animation: gn10in .5s cubic-bezier(.2,.7,.2,1) both;
}

.gn-10-bar[data-scrolled="true"] {
  background: rgba(255,255,255,.62);
  border-bottom-color: rgba(255,255,255,.6);
  box-shadow: 0 6px 24px rgba(20,20,40,.14);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  backdrop-filter: blur(16px) saturate(180%);
}

@keyframes gn10in {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.gn-10-brand {
  font-weight: 800;
  font-size: 17px;
  color: oklch(0.3 0.06 235);
  text-decoration: none;
}

.gn-10-bar nav ul {
  display: flex;
  gap: 4px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline-start: auto;
}

.gn-10-bar nav a {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 13px;
  border-radius: 9px;
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.34 0.04 235);
  text-decoration: none;
  transition: background-color .15s ease;
}

.gn-10-bar nav a:hover {
  background: rgba(255,255,255,.5);
}

.gn-10-cta {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 16px;
  border-radius: 10px;
  font: 700 13.5px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  background: oklch(0.52 0.16 235);
}

.gn-10-bar a:focus-visible {
  outline: 2.5px solid oklch(0.52 0.16 235);
  outline-offset: 2px;
}

.gn-10-hero {
  height: 260px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,oklch(0.72 0.15 235),oklch(0.68 0.13 210) 55%,oklch(0.76 0.12 255));
}

.gn-10-hero h2 {
  margin: 0;
  font: 800 28px/1.1 system-ui,sans-serif;
  color: #fff;
  text-shadow: 0 2px 16px rgba(20,0,50,.3);
}

.gn-10-body {
  padding: 32px 28px 80px;
  min-height: 1200px;
  background: oklch(0.98 0.005 265);
}

.gn-10-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
  color: oklch(0.36 0.04 235);
  max-width: 560px;
}

.gn-10-body h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: oklch(0.26 0.05 235);
  max-width: 560px;
}

.gn-10-body code {
  background: oklch(0.94 0.01 235);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
}

@media (max-width: 640px) {
  .gn-10-bar {
    gap: 10px;
    padding: 0 12px;
    height: 52px;
  }

  .gn-10-brand {
    font-size: 15px;
  }

  .gn-10-bar nav {
    display: none;
  }

  .gn-10-cta {
    padding: 0 12px;
    font-size: 12px;
    height: 36px;
  }

  .gn-10-hero {
    height: 200px;
  }

  .gn-10-hero h2 {
    font-size: 22px;
  }
}

@media (max-width: 400px) {
  .gn-10-cta {
    padding: 0 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-10-bar {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
/* Preview behaviour: flip data-scrolled past the hero (stand-in for the Framer Motion state). */
document.querySelectorAll('.gn-10__stage').forEach((stage) => {
  const bar = stage.querySelector('.gn-10-bar');
  stage.addEventListener('scroll', () => {
    bar.dataset.scrolled = stage.scrollTop > 60 ? 'true' : 'false';
  }, { passive: true });
});

/* ── The real component — app/components/Header.tsx (Next.js App Router + Framer Motion + Tailwind) ──
'use client';
import { useState } from 'react';
import { motion, useScroll, useMotionValueEvent } from 'framer-motion';

export default function Header() {
  const [scrolled, setScrolled] = useState(false);
  const { scrollY } = useScroll();
  useMotionValueEvent(scrollY, 'change', (y) => setScrolled(y > 60));

  return (
    <motion.header
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5, ease: [0.2, 0.7, 0.2, 1] }}
      className={[
        'sticky top-0 z-50 flex items-center gap-5 h-14 px-5',
        'backdrop-blur-md backdrop-saturate-150 transition-colors duration-300',
        scrolled
          ? 'bg-white/60 border-b border-white/60 shadow-lg backdrop-blur-xl'
          : 'bg-white/25 border-b border-white/20',
      ].join(' ')}
    >
      <a href="/" className="font-extrabold text-lg text-slate-800">Loomly</a>
      <nav aria-label="Primary" className="ml-auto flex gap-1">
        <a href="/" aria-current="page" className="px-3 h-10 grid place-items-center rounded-lg font-semibold text-slate-700 hover:bg-white/50">Home</a>
        <a href="/features" className="px-3 h-10 grid place-items-center rounded-lg font-semibold text-slate-700 hover:bg-white/50">Features</a>
        <a href="/pricing" className="px-3 h-10 grid place-items-center rounded-lg font-semibold text-slate-700 hover:bg-white/50">Pricing</a>
      </nav>
      <a href="/signup" className="h-10 px-4 grid place-items-center rounded-xl font-bold text-white bg-sky-600">Get started</a>
    </motion.header>
  );
}
── CSS Modules variant: move the utility strings into Header.module.css and reference styles.bar; keep the useState + useScroll logic unchanged. ── */
```
