---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-course-progress-card-3d-tilt/"
title: "Tailwind Course Progress Card with 3D Tilt"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "An EdTech course card where progress is the hero: a 68%-complete pill floats highest at translate-z-[40px], the progress fill carries a glint that slides…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Course Progress Card with 3D Tilt
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-course-progress-card-3d-tilt/

An EdTech course card where progress is the hero: a 68%-complete pill floats highest at translate-z-[40px], the progress fill carries a glint that slides with the cursor via --mx, and module metadata sits calmly lower. Depth encodes hierarchy. The port adds a labelled progress row (module 9 of 12) with a proper aria-valuetext.
## HTML
```html
<section class="ttc-14 w-full min-h-svh grid place-items-center bg-linear-to-b from-ttc14-bg to-ttc14-bg2 px-6 pt-16 pb-14 font-ttc14-sans text-ttc14-ink" aria-label="Course progress card with 3D tilt demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc14-card class="group/card relative w-full max-w-[19.5rem] rounded-[22px] border border-ttc14-line bg-white p-6 shadow-[0_18px_44px_-30px_var(--color-ttc14-shadow)] transform-3d [transform:perspective(1100px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear data-live:shadow-[0_30px_56px_-26px_var(--color-ttc14-shadow)] motion-reduce:transition-none">
      <span class="absolute -top-3.5 right-5 rounded-full bg-linear-120 from-ttc14-acc to-ttc14-acc2 px-3.5 py-2 text-[11.5px] leading-none font-bold text-white shadow-[0_10px_22px_-10px_var(--color-ttc14-acc)] translate-z-[40px] animate-ttc14-bob motion-reduce:animate-none">68% complete</span>
      <div aria-hidden="true" class="grid aspect-[2/1] w-full place-items-center rounded-[14px] bg-[radial-gradient(80%_100%_at_30%_20%,var(--color-ttc14-thumb1),var(--color-ttc14-thumb2))] translate-z-[18px]"><span class="font-ttc14-mono text-[34px] font-bold text-ttc14-glyph">{ }</span></div>
      <h3 class="mt-4 text-[19px] leading-snug font-bold tracking-[-0.01em] text-pretty translate-z-[24px]">Advanced CSS Architecture</h3>
      <p class="mt-1.5 text-[12.5px] text-ttc14-mut translate-z-[12px]">12 modules · 6.5 hrs · Certificate included</p>
      <div class="mt-5 translate-z-[20px]">
        <div class="mb-2 flex justify-between text-[12px] font-semibold"><span>Module 9 of 12</span><span class="text-ttc14-accink tabular-nums">68%</span></div>
        <div role="progressbar" aria-label="Course progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="68" aria-valuetext="68 percent, module 9 of 12" class="h-2 overflow-hidden rounded-full bg-ttc14-track">
          <div style="--progress:68%" class="h-full w-[var(--progress)] rounded-full [background:linear-gradient(115deg,transparent_40%,oklch(1_0_0/0.55)_50%,transparent_60%)_var(--mx,50%)_0/300%_100%_no-repeat,linear-gradient(90deg,var(--color-ttc14-acc),var(--color-ttc14-acc2))]"></div>
        </div>
      </div>
      <button type="button" class="mt-5 min-h-11 w-full cursor-pointer rounded-xl bg-ttc14-btn text-[13.5px] font-semibold text-white translate-z-[30px] transition-colors hover:bg-ttc14-ink focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-ttc14-acc">Resume · Module 9</button>
    </article>
    <p aria-hidden="true" class="rounded-full border border-ttc14-line bg-white/70 px-3.5 py-2 font-ttc14-mono text-[11.5px] text-ttc14-mut">translate-z = hierarchy · glint at var(--mx) · aria-valuetext</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc14-bg: #f2f8f4;
  --color-ttc14-bg: oklch(0.97 0.008 155);
  --color-ttc14-bg2: #e1efea;
  --color-ttc14-bg2: oklch(0.93 0.015 170);
  --color-ttc14-line: #dde9e3;
  --color-ttc14-line: oklch(0.91 0.012 160);
  --color-ttc14-ink: #1a2a2c;
  --color-ttc14-ink: oklch(0.25 0.02 200);
  --color-ttc14-mut: #566668;
  --color-ttc14-mut: oklch(0.48 0.02 200);
  --color-ttc14-acc: #2fb872;
  --color-ttc14-acc: oklch(0.7 0.16 155);
  --color-ttc14-acc2: #1f9aa0;
  --color-ttc14-acc2: oklch(0.62 0.11 195);
  --color-ttc14-accink: #17804c;
  --color-ttc14-accink: oklch(0.52 0.12 155);
  --color-ttc14-track: #e7efeb;
  --color-ttc14-track: oklch(0.94 0.01 160);
  --color-ttc14-thumb1: #2d5a4c;
  --color-ttc14-thumb1: oklch(0.42 0.07 170);
  --color-ttc14-thumb2: #172a33;
  --color-ttc14-thumb2: oklch(0.24 0.03 220);
  --color-ttc14-glyph: #98e6bd;
  --color-ttc14-glyph: oklch(0.87 0.1 155);
  --color-ttc14-btn: #33494d;
  --color-ttc14-btn: oklch(0.37 0.03 200);
  --color-ttc14-shadow: #3c6b5599;
  --color-ttc14-shadow: oklch(0.45 0.07 160 / 0.6);
  --font-ttc14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttc14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc14-bob: ttc14-bob 3.8s ease-in-out infinite;

  @keyframes ttc14-bob {
    50% {
      margin-top: -5px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc14-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 8; // grid-safe motion budget for catalog pages
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--mx', (px * 100).toFixed(1) + '%'); // slides the bar glint
      card.setAttribute('data-live', '');
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
