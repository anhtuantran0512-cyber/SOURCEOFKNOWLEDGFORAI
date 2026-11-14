---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-mouse-following-border-glow-cards/"
title: "Tailwind Mouse-Following Border Glow Cards"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "The dev-tool feature grid: near-black cards whose 1px border lights up in a radial glow that follows the cursor — and bleeds onto a neighbour's edge before…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mouse-Following Border Glow Cards
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-mouse-following-border-glow-cards/

The dev-tool feature grid: near-black cards whose 1px border lights up in a radial glow that follows the cursor — and bleeds onto a neighbour's edge before the pointer arrives — plus a whisper of tilt (±5°). The ring is one before: layer masked to the border with [mask-composite:exclude]; each card now owns its own accent via [--color-ttc06-edge:…].
## HTML
```html
<section class="ttc-06 w-full min-h-svh grid place-items-center bg-ttc06-bg px-5 py-14 font-ttc06-sans text-ttc06-ink" aria-label="Mouse-following border glow cards demo">
  <div class="grid w-full max-w-3xl justify-items-center gap-8">
    <div data-ttc06-grid class="grid w-full grid-cols-[repeat(auto-fit,minmax(12.5rem,1fr))] gap-4">
      <article class="group/card relative overflow-hidden rounded-2xl border border-white/7 bg-ttc06-card p-6 [--color-ttc06-edge:oklch(0.74_0.15_160)] [transform:perspective(1200px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-500 data-live:duration-90 data-live:ease-linear motion-reduce:transition-none before:pointer-events-none before:absolute before:-inset-px before:rounded-[inherit] before:p-px before:bg-[radial-gradient(220px_circle_at_var(--px,-999px)_var(--py,-999px),var(--color-ttc06-edge),transparent_70%)] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:bg-[radial-gradient(340px_circle_at_var(--px,-999px)_var(--py,-999px),color-mix(in_oklab,var(--color-ttc06-edge)_12%,transparent),transparent_70%)] after:content-[''] has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-3 has-[a:focus-visible]:outline-ttc06-edge">
        <div aria-hidden="true" class="grid size-10 place-items-center rounded-[11px] border border-ttc06-edge/35 bg-linear-140 from-ttc06-edge/30 to-ttc06-tile text-ttc06-edge"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3L5 13.5h6L10 21l8-10.5h-6z"/></svg></div>
        <h3 class="mt-5 text-base font-semibold tracking-[-0.01em]"><a href="#" class="no-underline text-inherit outline-none after:absolute after:inset-0 after:z-10 after:content-['']">Edge Functions</a></h3>
        <p class="mt-2 text-[13.5px] leading-[1.6] text-ttc06-mut text-pretty">Deploy globally in milliseconds. Zero cold starts, zero config.</p>
        <p aria-hidden="true" class="mt-4 flex items-center gap-1.5 text-[13px] font-medium text-ttc06-edge">Read the docs <span class="transition-transform group-hover/card:translate-x-1">→</span></p>
      </article>
      <article class="group/card relative overflow-hidden rounded-2xl border border-white/7 bg-ttc06-card p-6 [--color-ttc06-edge:oklch(0.74_0.13_220)] [transform:perspective(1200px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-500 data-live:duration-90 data-live:ease-linear motion-reduce:transition-none before:pointer-events-none before:absolute before:-inset-px before:rounded-[inherit] before:p-px before:bg-[radial-gradient(220px_circle_at_var(--px,-999px)_var(--py,-999px),var(--color-ttc06-edge),transparent_70%)] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:bg-[radial-gradient(340px_circle_at_var(--px,-999px)_var(--py,-999px),color-mix(in_oklab,var(--color-ttc06-edge)_12%,transparent),transparent_70%)] after:content-[''] has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-3 has-[a:focus-visible]:outline-ttc06-edge">
        <div aria-hidden="true" class="grid size-10 place-items-center rounded-[11px] border border-ttc06-edge/35 bg-linear-140 from-ttc06-edge/30 to-ttc06-tile text-ttc06-edge"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7a8 8 0 0 0-14.3-2.3M4 17a8 8 0 0 0 14.3 2.3"/><path d="M20 3v4h-4M4 21v-4h4"/></svg></div>
        <h3 class="mt-5 text-base font-semibold tracking-[-0.01em]"><a href="#" class="no-underline text-inherit outline-none after:absolute after:inset-0 after:z-10 after:content-['']">Realtime Sync</a></h3>
        <p class="mt-2 text-[13.5px] leading-[1.6] text-ttc06-mut text-pretty">Postgres changes stream to every client over WebSockets.</p>
        <p aria-hidden="true" class="mt-4 flex items-center gap-1.5 text-[13px] font-medium text-ttc06-edge">Read the docs <span class="transition-transform group-hover/card:translate-x-1">→</span></p>
      </article>
      <article class="group/card relative overflow-hidden rounded-2xl border border-white/7 bg-ttc06-card p-6 [--color-ttc06-edge:oklch(0.72_0.15_290)] [transform:perspective(1200px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-500 data-live:duration-90 data-live:ease-linear motion-reduce:transition-none before:pointer-events-none before:absolute before:-inset-px before:rounded-[inherit] before:p-px before:bg-[radial-gradient(220px_circle_at_var(--px,-999px)_var(--py,-999px),var(--color-ttc06-edge),transparent_70%)] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:bg-[radial-gradient(340px_circle_at_var(--px,-999px)_var(--py,-999px),color-mix(in_oklab,var(--color-ttc06-edge)_12%,transparent),transparent_70%)] after:content-[''] has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-3 has-[a:focus-visible]:outline-ttc06-edge">
        <div aria-hidden="true" class="grid size-10 place-items-center rounded-[11px] border border-ttc06-edge/35 bg-linear-140 from-ttc06-edge/30 to-ttc06-tile text-ttc06-edge"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/></svg></div>
        <h3 class="mt-5 text-base font-semibold tracking-[-0.01em]"><a href="#" class="no-underline text-inherit outline-none after:absolute after:inset-0 after:z-10 after:content-['']">Row-Level Auth</a></h3>
        <p class="mt-2 text-[13.5px] leading-[1.6] text-ttc06-mut text-pretty">Policies live next to your data. Security by default.</p>
        <p aria-hidden="true" class="mt-4 flex items-center gap-1.5 text-[13px] font-medium text-ttc06-edge">Read the docs <span class="transition-transform group-hover/card:translate-x-1">→</span></p>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttc06-mono text-[11.5px] text-ttc06-mut">before:[mask-composite:exclude] · --px/--py · [--color-ttc06-edge:…]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc06-bg: #0b0c10;
  --color-ttc06-bg: oklch(0.13 0.008 260);
  --color-ttc06-card: #131519;
  --color-ttc06-card: oklch(0.17 0.01 260);
  --color-ttc06-tile: #1a1c21;
  --color-ttc06-tile: oklch(0.21 0.015 260);
  --color-ttc06-ink: #ebedf1;
  --color-ttc06-ink: oklch(0.94 0.005 260);
  --color-ttc06-mut: #a8acb6;
  --color-ttc06-mut: oklch(0.74 0.012 260);
  --color-ttc06-edge: #3fcf9a;
  --color-ttc06-edge: oklch(0.74 0.15 160);
  --font-ttc06-sans: 'Geist', system-ui, sans-serif;
  --font-ttc06-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc06-grid]').forEach((grid) => {
    if (grid.dataset.wired) return;
    grid.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const cards = [...grid.children];
    const MAX = 5; // dev-tool aesthetics: whisper, don't wobble
    grid.addEventListener('pointermove', (e) => {
      // One listener updates EVERY card, so the glow flows across the gaps.
      cards.forEach((card) => {
        const r = card.getBoundingClientRect();
        const x = e.clientX - r.left, y = e.clientY - r.top;
        const inside = x >= 0 && x <= r.width && y >= 0 && y <= r.height;
        card.style.setProperty('--px', x.toFixed(1) + 'px');
        card.style.setProperty('--py', y.toFixed(1) + 'px');
        card.toggleAttribute('data-live', inside);
        card.style.setProperty('--rx', inside ? ((0.5 - y / r.height) * MAX).toFixed(2) + 'deg' : '0deg');
        card.style.setProperty('--ry', inside ? ((x / r.width - 0.5) * MAX).toFixed(2) + 'deg' : '0deg');
      });
    });
    grid.addEventListener('pointerleave', () => {
      cards.forEach((card) => {
        card.removeAttribute('data-live');
        card.style.setProperty('--px', '-999px');
        card.style.setProperty('--py', '-999px');
        card.style.setProperty('--rx', '0deg');
        card.style.setProperty('--ry', '0deg');
      });
    });
  });
})();
```
