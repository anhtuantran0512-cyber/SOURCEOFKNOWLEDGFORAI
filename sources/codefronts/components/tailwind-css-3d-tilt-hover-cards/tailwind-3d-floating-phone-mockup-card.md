---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-floating-phone-mockup-card/"
title: "Tailwind 3D Floating Phone Mockup Card for App Landing Pages"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "An app-landing hero card: a CSS-drawn phone rests at a 3D angle and straightens toward you as the cursor approaches, while rating and download badges bob in…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Floating Phone Mockup Card for App Landing Pages
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-floating-phone-mockup-card/

An app-landing hero card: a CSS-drawn phone rests at a 3D angle and straightens toward you as the cursor approaches, while rating and download badges bob in front of it and a specular streak sweeps the glass. The port fixes a flattening bug — the phone now carries its own perspective(900px), because the card's overflow-hidden was collapsing its rotation to a squash — and adds a real download CTA.
## HTML
```html
<section class="ttc-13 w-full min-h-svh grid place-items-center bg-ttc13-bg bg-[radial-gradient(90%_100%_at_20%_0%,var(--color-ttc13-lobe),transparent_60%)] px-6 py-14 font-ttc13-sans text-white" aria-label="3D floating phone mockup card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc13-card class="group/card relative w-full max-w-[20rem] overflow-hidden rounded-[26px] border border-white/10 bg-linear-170 from-ttc13-card1 to-ttc13-card2 px-6 pt-6 shadow-[0_32px_64px_-28px_oklch(0_0_0/0.85)] [transform:perspective(1400px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none">
      <div class="flex items-start justify-between gap-3">
        <div>
          <h3 class="text-[24px] leading-none font-extrabold tracking-[-0.02em]">Tidepool</h3>
          <p class="mt-1.5 text-[13.5px] text-ttc13-mut">Sleep sounds, tuned to your night.</p>
        </div>
        <a href="#" class="inline-flex min-h-11 flex-none items-center rounded-full bg-white px-4 text-[13px] font-bold text-ttc13-bg no-underline transition-transform hover:scale-105 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-ttc13-acc">Get it free</a>
      </div>
      <div aria-hidden="true" class="relative mt-5 h-64">
        <div class="absolute -bottom-10 left-1/2 -ml-[75px] h-[300px] w-[150px] rounded-[30px] border border-white/18 bg-ttc13-frame p-[9px] shadow-[24px_30px_50px_-20px_oklch(0_0_0/0.7)] [transform:perspective(900px)_rotateY(calc(-18deg_+_var(--ry,0deg)*1.4))_rotateX(calc(8deg_+_var(--rx,0deg)*0.6))] transition-transform duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] group-data-live/card:duration-80 group-data-live/card:ease-linear motion-reduce:transition-none">
          <span class="absolute top-4 left-1/2 z-10 h-[9px] w-11 -translate-x-1/2 rounded-full bg-ttc13-notch"></span>
          <div class="relative flex size-full flex-col items-center overflow-hidden rounded-[22px] bg-linear-190 from-ttc13-screen1 to-ttc13-screen2 px-3 pt-9 after:absolute after:-inset-[60%] after:-translate-x-[70%] after:bg-[linear-gradient(115deg,transparent_44%,oklch(1_0_0/0.28)_50%,transparent_56%)] after:transition-transform after:duration-900 after:content-[''] group-data-live/card:after:translate-x-[55%]">
            <p class="text-[22px] leading-none font-bold tabular-nums">23:42</p>
            <p class="mt-1 text-[9px] font-semibold tracking-[0.14em] text-white/75">OCEAN DRIFT · 45 MIN</p>
            <div class="mt-5 size-20 rounded-full bg-[conic-gradient(var(--color-ttc13-acc)_0_62%,oklch(1_0_0/0.14)_62%)] p-[5px]"><div class="size-full rounded-full bg-ttc13-screen2"></div></div>
            <div class="mt-5 h-6 w-full rounded-lg bg-white/16"></div>
            <div class="mt-2 h-6 w-full rounded-lg bg-white/10"></div>
          </div>
        </div>
        <span class="absolute top-5 left-0 rounded-full border border-white/20 bg-white/10 px-3 py-2 text-[11.5px] font-bold backdrop-blur-sm animate-ttc13-bob motion-reduce:animate-none">★ 4.9 rating</span>
        <span class="absolute top-28 right-0 rounded-full border border-white/20 bg-white/10 px-3 py-2 text-[11.5px] font-bold backdrop-blur-sm animate-ttc13-bob [animation-delay:-1.7s] motion-reduce:animate-none">2M+ downloads</span>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc13-mono text-[11.5px] text-ttc13-mut">perspective(900px)_rotateY(calc(-18deg_+_var(--ry)*1.4))</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc13-bg: #0d1220;
  --color-ttc13-bg: oklch(0.15 0.02 250);
  --color-ttc13-lobe: #1b2f52e6;
  --color-ttc13-lobe: oklch(0.26 0.06 240 / 0.9);
  --color-ttc13-card1: #182a3f;
  --color-ttc13-card1: oklch(0.22 0.04 235);
  --color-ttc13-card2: #0f1726;
  --color-ttc13-card2: oklch(0.16 0.025 250);
  --color-ttc13-frame: #232a36;
  --color-ttc13-frame: oklch(0.25 0.02 250);
  --color-ttc13-notch: #0b0e14;
  --color-ttc13-notch: oklch(0.12 0.01 250);
  --color-ttc13-screen1: #2e6fa8;
  --color-ttc13-screen1: oklch(0.45 0.12 230);
  --color-ttc13-screen2: #14203f;
  --color-ttc13-screen2: oklch(0.22 0.06 260);
  --color-ttc13-acc: #52b8e8;
  --color-ttc13-acc: oklch(0.74 0.12 225);
  --color-ttc13-mut: #bcc5d4;
  --color-ttc13-mut: oklch(0.82 0.02 255);
  --font-ttc13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttc13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc13-bob: ttc13-bob 3.4s ease-in-out infinite;

  @keyframes ttc13-bob {
    50% {
      margin-top: -7px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-13 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc13-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 9; // the phone amplifies this 1.4x through its calc() pose
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.setAttribute('data-live', ''); // also fires the specular sweep across the glass
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
