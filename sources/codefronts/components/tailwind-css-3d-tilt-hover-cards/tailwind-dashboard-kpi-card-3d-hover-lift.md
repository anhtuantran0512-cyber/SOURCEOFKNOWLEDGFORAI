---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-dashboard-kpi-card-3d-hover-lift/"
title: "Tailwind Dashboard KPI Card with 3D Hover Lift"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "A FinTech KPI widget with enterprise restraint: perspective(1600px), ±4° tilt, a 6px lift with a deepening shadow, and a CSS-only sparkline of flex bars that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dashboard KPI Card with 3D Hover Lift
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-dashboard-kpi-card-3d-hover-lift/

A FinTech KPI widget with enterprise restraint: perspective(1600px), ±4° tilt, a 6px lift with a deepening shadow, and a CSS-only sparkline of flex bars that stagger-grow when the tilt arms. The port styles all thirteen bars from the parent with v4's *: child variant, and adds hover tooltips read straight from each bar's data-v via *:after:content-[attr(data-v)].
## HTML
```html
<section class="ttc-10 w-full min-h-svh grid place-items-center bg-linear-to-b from-ttc10-bg to-ttc10-bg2 px-6 py-14 font-ttc10-sans text-ttc10-ink" aria-label="Dashboard KPI card with 3D hover lift demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc10-card class="group/card w-full max-w-[20rem] rounded-[18px] border border-ttc10-line bg-white p-6 shadow-[0_10px_24px_-18px_var(--color-ttc10-shadow)] [transform:perspective(1600px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))_translateY(var(--lift,0px))] transition-[transform,box-shadow] duration-500 ease-[cubic-bezier(0.2,0.9,0.3,1.05)] data-live:duration-90 data-live:ease-linear data-live:[--lift:-6px] data-live:shadow-[0_30px_50px_-24px_var(--color-ttc10-shadow)] motion-reduce:transition-none" aria-label="Monthly recurring revenue">
      <div class="flex items-center justify-between gap-3">
        <h3 class="text-[13px] font-semibold text-ttc10-mut">Monthly Recurring Revenue</h3>
        <span class="inline-flex items-center gap-1 rounded-full bg-ttc10-acc/14 px-2.5 py-1 text-[11.5px] font-bold text-ttc10-accink"><svg aria-hidden="true" viewBox="0 0 12 12" class="size-2.5" fill="currentColor"><path d="M6 2l4 6H2z"/></svg><span class="sr-only">Up</span>12.4%</span>
      </div>
      <p class="mt-3 text-[36px] leading-none font-extrabold tracking-[-0.03em] tabular-nums">$84,200</p>
      <div aria-hidden="true" class="mt-6 flex h-14 items-end gap-1 *:relative *:flex-1 *:h-[calc(var(--v)*1%)] *:origin-bottom *:rounded-t-[3px] *:bg-linear-to-b *:from-ttc10-acc *:to-ttc10-acc/40 *:transition-colors *:hover:from-ttc10-ink *:hover:to-ttc10-ink/50 *:group-data-live/card:animate-ttc10-grow *:[animation-delay:calc(var(--i)*22ms)] *:after:pointer-events-none *:after:absolute *:after:bottom-full *:after:left-1/2 *:after:mb-1.5 *:after:-translate-x-1/2 *:after:rounded-md *:after:bg-ttc10-ink *:after:px-1.5 *:after:py-1 *:after:font-ttc10-mono *:after:text-[10px] *:after:font-semibold *:after:whitespace-nowrap *:after:text-white *:after:opacity-0 *:after:transition-opacity *:after:content-[attr(data-v)] *:hover:after:opacity-100 motion-reduce:*:animate-none">
        <i style="--v:32;--i:0" data-v="$58.1k"></i><i style="--v:41;--i:1" data-v="$61.0k"></i><i style="--v:38;--i:2" data-v="$60.2k"></i><i style="--v:52;--i:3" data-v="$64.9k"></i><i style="--v:47;--i:4" data-v="$63.1k"></i><i style="--v:58;--i:5" data-v="$66.8k"></i><i style="--v:54;--i:6" data-v="$65.5k"></i><i style="--v:66;--i:7" data-v="$69.9k"></i><i style="--v:61;--i:8" data-v="$68.0k"></i><i style="--v:72;--i:9" data-v="$72.3k"></i><i style="--v:69;--i:10" data-v="$71.2k"></i><i style="--v:83;--i:11" data-v="$74.9k"></i><i style="--v:92;--i:12" data-v="$84.2k"></i>
      </div>
      <p class="mt-4 flex justify-between text-[12px] text-ttc10-mut"><span>vs. <span class="tabular-nums">$74,900</span> last month</span><span>13 wk</span></p>
    </article>
    <p aria-hidden="true" class="rounded-full border border-ttc10-line bg-white/70 px-3.5 py-2 font-ttc10-mono text-[11.5px] text-ttc10-mut">*:h-[calc(var(--v)*1%)] · *:after:content-[attr(data-v)] · data-live:[--lift]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc10-bg: #f6f8fb;
  --color-ttc10-bg: oklch(0.975 0.005 250);
  --color-ttc10-bg2: #e9edf3;
  --color-ttc10-bg2: oklch(0.94 0.01 250);
  --color-ttc10-line: #e0e4ea;
  --color-ttc10-line: oklch(0.91 0.008 250);
  --color-ttc10-ink: #1c222c;
  --color-ttc10-ink: oklch(0.24 0.02 255);
  --color-ttc10-mut: #5d6573;
  --color-ttc10-mut: oklch(0.49 0.02 255);
  --color-ttc10-acc: #32b16b;
  --color-ttc10-acc: oklch(0.68 0.15 152);
  --color-ttc10-accink: #1b7a45;
  --color-ttc10-accink: oklch(0.5 0.12 152);
  --color-ttc10-shadow: #4b556a8c;
  --color-ttc10-shadow: oklch(0.42 0.04 255 / 0.55);
  --font-ttc10-sans: 'Geist', system-ui, sans-serif;
  --font-ttc10-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-ttc10-grow: ttc10-grow 0.4s cubic-bezier(0.2,0.9,0.3,1.1) backwards;

  @keyframes ttc10-grow {
    from {
      scale: 1 0.55;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc10-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 4; // enterprise dose: elevation, not rotation
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.setAttribute('data-live', ''); // adds the -6px lift, deep shadow and bar re-grow
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
