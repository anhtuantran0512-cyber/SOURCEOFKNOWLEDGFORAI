---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-music-player-card-spring-physics/"
title: "Tailwind 3D Tilt Music Player Card with Spring Physics"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "A streaming-app album card driven by a requestAnimationFrame spring that overshoots and settles like a physical object."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Music Player Card with Spring Physics
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-music-player-card-spring-physics/

A streaming-app album card driven by a requestAnimationFrame spring that overshoots and settles like a physical object. The port makes the player actually play: the play button is a real aria-pressed toggle, and group-has-[[data-play][aria-pressed=true]]/card: spins the vinyl, slides it out, starts the equaliser and runs the progress bar — all in CSS.
## HTML
```html
<section class="ttc-07 w-full min-h-svh grid place-items-center bg-ttc07-bg bg-[radial-gradient(90%_100%_at_50%_110%,var(--color-ttc07-lobe),transparent_60%)] px-6 py-14 font-ttc07-sans text-white" aria-label="3D tilt music player card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc07-card class="group/card relative w-full max-w-[18rem] rounded-[22px] border border-white/10 bg-ttc07-card p-3.5 shadow-[0_30px_60px_-28px_oklch(0_0_0/0.85)] transform-3d [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))]" aria-label="Midnight Static by Velvet Antenna">
      <div aria-hidden="true" class="relative aspect-square w-full overflow-hidden rounded-[14px] bg-ttc07-art translate-z-[20px]">
        <img class="absolute inset-0 size-full object-cover" src="https://picsum.photos/seed/midnight-static/520/520" alt="" loading="lazy">
        <div class="absolute top-1/2 right-[-30%] aspect-square w-[88%] -translate-y-1/2 rounded-full border-[14px] border-transparent bg-[repeating-radial-gradient(circle,var(--color-ttc07-groove1)_0_2px,var(--color-ttc07-groove2)_2px_4px)] shadow-[-12px_0_30px_oklch(0_0_0/0.5)] transition-[right] duration-500 ease-[cubic-bezier(0.2,0.9,0.3,1.2)] group-data-live/card:right-[-18%] group-has-[[data-play][aria-pressed=true]]/card:right-[-6%] group-has-[[data-play][aria-pressed=true]]/card:animate-ttc07-spin motion-reduce:animate-none after:absolute after:inset-[36%] after:rounded-full after:bg-ttc07-acc after:content-['']"></div>
      </div>
      <div class="flex items-center gap-3 px-1 pt-3.5 translate-z-[50px]">
        <button data-play type="button" aria-pressed="false" aria-label="Play Midnight Static" class="group/play grid size-12 flex-none cursor-pointer place-items-center rounded-full bg-ttc07-acc text-ttc07-bg shadow-[0_10px_22px_-8px_var(--color-ttc07-acc)] transition-transform hover:scale-108 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">
          <svg aria-hidden="true" viewBox="0 0 24 24" class="ml-0.5 size-5 group-aria-pressed/play:hidden" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg>
          <svg aria-hidden="true" viewBox="0 0 24 24" class="hidden size-5 group-aria-pressed/play:block" fill="currentColor"><path d="M6 4h4.5v16H6zM13.5 4H18v16h-4.5z"/></svg>
        </button>
        <div class="min-w-0 flex-1">
          <div class="flex items-center gap-2">
            <h3 class="truncate text-[15px] font-bold">Midnight Static</h3>
            <span aria-hidden="true" class="hidden h-3 items-end gap-[2px] group-has-[[data-play][aria-pressed=true]]/card:flex"><i class="block h-full w-[3px] origin-bottom rounded-full bg-ttc07-acc animate-ttc07-eq motion-reduce:animate-none"></i><i class="block h-full w-[3px] origin-bottom rounded-full bg-ttc07-acc animate-ttc07-eq [animation-delay:-0.3s] motion-reduce:animate-none"></i><i class="block h-full w-[3px] origin-bottom rounded-full bg-ttc07-acc animate-ttc07-eq [animation-delay:-0.6s] motion-reduce:animate-none"></i></span>
          </div>
          <p class="mt-0.5 text-[12.5px] text-ttc07-mut">Velvet Antenna</p>
        </div>
        <button data-like type="button" aria-pressed="false" aria-label="Like Midnight Static" class="group/like grid size-11 flex-none cursor-pointer place-items-center rounded-full text-ttc07-mut transition-colors hover:text-ttc07-acc aria-pressed:text-ttc07-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttc07-acc">
          <svg aria-hidden="true" viewBox="0 0 24 24" class="size-5 fill-none group-aria-pressed/like:fill-current" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 20s-7.5-4.6-7.5-10.1A4.4 4.4 0 0 1 12 7.3a4.4 4.4 0 0 1 7.5 2.6C19.5 15.4 12 20 12 20z"/></svg>
        </button>
      </div>
      <div aria-hidden="true" class="mx-1 mt-3 mb-1 h-1 overflow-hidden rounded-full bg-white/12 translate-z-[30px]"><div class="h-full w-[32%] rounded-full bg-ttc07-acc animate-ttc07-progress [animation-play-state:paused] group-has-[[data-play][aria-pressed=true]]/card:[animation-play-state:running] motion-reduce:animate-none"></div></div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc07-mono text-[11.5px] text-ttc07-mut">rAF spring · group-has-[[aria-pressed=true]]/card: · animation-play-state</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc07-bg: #0f0b14;
  --color-ttc07-bg: oklch(0.14 0.015 300);
  --color-ttc07-lobe: #4a1837cc;
  --color-ttc07-lobe: oklch(0.26 0.08 340 / 0.8);
  --color-ttc07-card: #1f1720;
  --color-ttc07-card: oklch(0.2 0.02 320);
  --color-ttc07-art: #3a1a36;
  --color-ttc07-art: oklch(0.26 0.06 320);
  --color-ttc07-groove1: #141017;
  --color-ttc07-groove1: oklch(0.16 0.01 300);
  --color-ttc07-groove2: #1c171f;
  --color-ttc07-groove2: oklch(0.2 0.015 300);
  --color-ttc07-acc: #f07ab5;
  --color-ttc07-acc: oklch(0.75 0.16 345);
  --color-ttc07-mut: #bfb3bf;
  --color-ttc07-mut: oklch(0.79 0.02 320);
  --font-ttc07-sans: 'DM Sans', system-ui, sans-serif;
  --font-ttc07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc07-spin: ttc07-spin 2.4s linear infinite;
  --animate-ttc07-eq: ttc07-eq 0.9s ease-in-out infinite;
  --animate-ttc07-progress: ttc07-progress 156s linear forwards;

  @keyframes ttc07-spin {
    to {
      rotate: 360deg;
    }
  }

  @keyframes ttc07-eq {
    0%,
        100% {
      scale: 1 0.3;
    }

    50% {
      scale: 1 1;
    }
  }

  @keyframes ttc07-progress {
    from {
      width: 32%;
    }

    to {
      width: 100%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc07-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    // Toggles: flip aria-pressed only; the vinyl, EQ, progress and heart all read it in CSS.
    card.querySelectorAll('[data-play], [data-like]').forEach((btn) => btn.addEventListener('click', () => {
      btn.setAttribute('aria-pressed', String(btn.getAttribute('aria-pressed') !== 'true'));
    }));
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 12, EASE = 0.12; // EASE is the spring: 0.08 heavy, 0.2 snappy
    let tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
    const tick = () => {
      cx += (tx - cx) * EASE;
      cy += (ty - cy) * EASE;
      card.style.setProperty('--rx', cx.toFixed(3) + 'deg');
      card.style.setProperty('--ry', cy.toFixed(3) + 'deg');
      // Self-suspend when settled: idle cost drops to zero.
      raf = (Math.abs(tx - cx) > 0.01 || Math.abs(ty - cy) > 0.01) ? requestAnimationFrame(tick) : null;
    };
    const wake = () => { if (!raf) raf = requestAnimationFrame(tick); };
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      tx = (0.5 - (e.clientY - r.top) / r.height) * MAX;
      ty = ((e.clientX - r.left) / r.width - 0.5) * MAX;
      card.setAttribute('data-live', '');
      wake();
    });
    card.addEventListener('pointerleave', () => {
      tx = 0; ty = 0; // spring home along the same physics
      card.removeAttribute('data-live');
      wake();
    });
  });
})();
```
