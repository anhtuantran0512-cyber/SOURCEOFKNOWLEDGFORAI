---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-svg-displacement-liquid-glass-background/"
title: "Tailwind SVG Displacement Liquid Glass Background"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "The real thing: feTurbulence plus feDisplacementMap physically bending the image beneath the glass, with warp intensity following the cursor."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SVG Displacement Liquid Glass Background
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-svg-displacement-liquid-glass-background/

The real thing: feTurbulence plus feDisplacementMap physically bending the image beneath the glass, with warp intensity following the cursor. Tailwind styles the panel, the stage and the layout; the filter stays SVG because displacement is geometry, not styling &mdash; and that division is exactly the point of the port.
## HTML
```html
<section id="lgt-08-root" class="lgt-08 relative grid w-full min-h-svh place-items-center bg-lgt08-bg p-15 font-lgt08-sans" aria-label="Tailwind SVG displacement liquid glass background">
  <svg id="lgt-08-svg" viewBox="0 0 600 380" width="600" height="380" preserveAspectRatio="xMidYMid slice" aria-hidden="true" class="pointer-events-none absolute col-start-1 row-start-1 h-auto w-[min(720px,94vw)] overflow-hidden rounded-[26px] saturate-120 shadow-[0_40px_80px_-34px_rgba(0,0,0,.8)]">
    <defs>
      <filter id="lgt-08-warp" x="-20%" y="-20%" width="140%" height="140%">
        <feTurbulence id="lgt-08-turb" type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="2" seed="7" result="noise"/>
        <feDisplacementMap id="lgt-08-disp" in="SourceGraphic" in2="noise" scale="14" xChannelSelector="R" yChannelSelector="G"/>
      </filter>
    </defs>
    <image href="https://picsum.photos/seed/lgwarp/600/380" x="0" y="0" width="600" height="380" preserveAspectRatio="xMidYMid slice" filter="url(#lgt-08-warp)"/>
  </svg>

  <div class="relative z-2 col-start-1 row-start-1 w-[min(360px,84vw)] rounded-[22px] border border-white/32 bg-white/10 p-7 text-white backdrop-blur-[6px] backdrop-saturate-150 shadow-[inset_0_1px_0_rgba(255,255,255,.45),0_20px_50px_-26px_rgba(0,0,0,.6)]">
    <span class="inline-block rounded-full border border-white/35 bg-white/20 px-2.75 py-1.25 text-[11px] font-bold uppercase tracking-[0.1em]">SVG feDisplacementMap</span>
    <h3 class="mt-3.5 mb-2 text-[28px] font-extrabold tracking-[-0.02em]">Real refraction</h3>
    <p class="text-[15px] leading-relaxed text-white [text-shadow:0_1px_8px_rgba(0,0,0,.45)]">Move your cursor &mdash; the image bends through the glass. This is displacement, not blur.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt08-bg: #0c0a16;
  --font-lgt08-sans: 'Manrope', system-ui, sans-serif;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-08-root');
  const disp = root.querySelector('#lgt-08-disp');
  const turb = root.querySelector('#lgt-08-turb');
  const svg = root.querySelector('#lgt-08-svg');
  if (!disp) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const BASE = 14, MAX = 40;
  let target = BASE, current = BASE, raf = null;

  const tick = () => {
    current += (target - current) * 0.12;
    disp.setAttribute('scale', current.toFixed(2));
    if (Math.abs(target - current) > 0.2) { raf = requestAnimationFrame(tick); }
    else { disp.setAttribute('scale', target.toFixed(2)); raf = null; }
  };
  const kick = () => { if (!raf) raf = requestAnimationFrame(tick); };

  root.addEventListener('pointermove', e => {
    if (reduce) return;
    const r = svg.getBoundingClientRect();
    const dx = Math.abs((e.clientX - (r.left + r.width / 2)) / (r.width / 2));
    const dy = Math.abs((e.clientY - (r.top + r.height / 2)) / (r.height / 2));
    const t = Math.min(1, (dx + dy) / 2);
    target = BASE + t * (MAX - BASE);
    const f = 0.012 + t * 0.02;
    turb.setAttribute('baseFrequency', f.toFixed(4) + ' ' + (f * 1.6).toFixed(4));
    kick();
  });
  root.addEventListener('pointerleave', () => { target = BASE; kick(); });
})();
```
