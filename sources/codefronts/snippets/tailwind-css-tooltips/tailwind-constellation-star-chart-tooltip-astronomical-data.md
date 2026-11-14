---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-constellation-star-chart-tooltip-astronomical-data/"
title: "Tailwind Constellation Star Chart Tooltip with Astronomical Data"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Orion rendered as inline SVG with six labelled stars: hover one and a card gives Bayer designation, spectral class, distance, magnitude and a five-star…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Constellation Star Chart Tooltip with Astronomical Data
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-constellation-star-chart-tooltip-astronomical-data/

Orion rendered as inline SVG with six labelled stars: hover one and a card gives Bayer designation, spectral class, distance, magnitude and a five-star brightness scale. The port's practical move is flip-side placement &mdash; one modifier class puts the card left instead of right for the two stars near the chart's edge.
## HTML
```html
<section class="ttp-15 w-full min-h-svh flex items-center justify-center bg-ttp15-bg px-[280px] py-10 font-ttp15-mono max-xl:px-7">
  <div class="relative h-100 w-100 shrink-0">
    <svg viewBox="0 0 400 400" class="block h-full w-full" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <circle cx="22" cy="18" r="0.6" fill="rgba(200,220,255,0.35)"/><circle cx="80" cy="10" r="0.7" fill="rgba(200,220,255,0.45)"/><circle cx="140" cy="22" r="0.4" fill="rgba(200,220,255,0.25)"/><circle cx="170" cy="38" r="0.6" fill="rgba(200,220,255,0.35)"/><circle cx="265" cy="18" r="0.7" fill="rgba(200,220,255,0.4)"/><circle cx="330" cy="22" r="0.4" fill="rgba(200,220,255,0.22)"/><circle cx="360" cy="55" r="0.6" fill="rgba(200,220,255,0.38)"/><circle cx="30" cy="80" r="0.4" fill="rgba(200,220,255,0.2)"/><circle cx="320" cy="75" r="0.6" fill="rgba(200,220,255,0.32)"/><circle cx="55" cy="145" r="0.5" fill="rgba(200,220,255,0.28)"/><circle cx="360" cy="150" r="0.5" fill="rgba(200,220,255,0.28)"/><circle cx="35" cy="260" r="0.5" fill="rgba(200,220,255,0.3)"/><circle cx="380" cy="260" r="0.5" fill="rgba(200,220,255,0.28)"/><circle cx="58" cy="360" r="0.4" fill="rgba(200,220,255,0.2)"/><circle cx="90" cy="380" r="0.5" fill="rgba(200,220,255,0.28)"/><circle cx="340" cy="355" r="0.5" fill="rgba(200,220,255,0.3)"/><circle cx="392" cy="360" r="0.6" fill="rgba(200,220,255,0.35)"/>
      <line x1="200" y1="48" x2="148" y2="155" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/><line x1="200" y1="48" x2="262" y2="142" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/><line x1="148" y1="155" x2="168" y2="228" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/><line x1="262" y1="142" x2="232" y2="224" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/><line x1="168" y1="228" x2="200" y2="230" stroke="rgba(140,160,255,0.26)" stroke-width="0.8"/><line x1="200" y1="230" x2="232" y2="224" stroke="rgba(140,160,255,0.26)" stroke-width="0.8"/><line x1="168" y1="228" x2="136" y2="342" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/><line x1="232" y1="224" x2="278" y2="330" stroke="rgba(140,160,255,0.22)" stroke-width="0.8"/>
      <circle cx="200" cy="48" r="6" fill="rgba(160,180,255,0.08)"/><circle cx="200" cy="48" r="2.5" fill="#d0daff" opacity="0.85"/><circle cx="148" cy="155" r="10" fill="rgba(255,120,60,0.06)"/><circle cx="148" cy="155" r="5" fill="#ffb890" opacity="0.9"/><circle cx="262" cy="142" r="6" fill="rgba(160,200,255,0.06)"/><circle cx="262" cy="142" r="3" fill="#c0d8ff" opacity="0.85"/><circle cx="168" cy="228" r="5" fill="rgba(160,180,255,0.06)"/><circle cx="168" cy="228" r="2.8" fill="#d0daff" opacity="0.85"/><circle cx="200" cy="230" r="5" fill="rgba(160,180,255,0.06)"/><circle cx="200" cy="230" r="3" fill="#d0daff" opacity="0.85"/><circle cx="232" cy="224" r="5" fill="rgba(160,200,255,0.06)"/><circle cx="232" cy="224" r="2.5" fill="#c8d8ff" opacity="0.85"/><circle cx="136" cy="342" r="5" fill="rgba(160,200,255,0.06)"/><circle cx="136" cy="342" r="2.5" fill="#c0d4ff" opacity="0.8"/><circle cx="278" cy="330" r="14" fill="rgba(160,200,255,0.05)"/><circle cx="278" cy="330" r="6" fill="#dce8ff" opacity="0.95"/>
    </svg>

    <div class="group absolute left-[37%] top-[38.75%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s1" aria-label="Betelgeuse, alpha Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s1" role="tooltip" class="ttp15-card">
        <div class="ttp15-top"><div class="ttp15-bayer">α Orionis</div><div class="ttp15-name">Betelgeuse</div><div class="ttp15-const">Orion · Upper left shoulder</div><span class="ttp15-pill">M1–2 Iaab · Red Supergiant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">700 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">0.42 (variable)</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~126,000 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Radius</span><span class="ttp15-val">~700 R☉</span></div>
          <div class="ttp15-mag"><span class="ttp15-key">Brightness</span><span class="flex gap-0.5" role="img" aria-label="4 out of 5"><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star opacity-30">★</span></span></div>
        </div>
      </div>
    </div>

    <div class="group absolute left-[69.5%] top-[82.5%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s2" aria-label="Rigel, beta Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s2" role="tooltip" class="ttp15-card ttp15-card-left">
        <div class="ttp15-top"><div class="ttp15-bayer">β Orionis</div><div class="ttp15-name">Rigel</div><div class="ttp15-const">Orion · Lower right</div><span class="ttp15-pill">B8 Ia · Blue Supergiant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">860 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">0.13 (brightest)</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~120,000 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Temp</span><span class="ttp15-val">12,100 K</span></div>
          <div class="ttp15-mag"><span class="ttp15-key">Brightness</span><span class="flex gap-0.5" role="img" aria-label="5 out of 5"><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span></span></div>
        </div>
      </div>
    </div>

    <div class="group absolute left-[65.5%] top-[35.5%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s3" aria-label="Bellatrix, gamma Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s3" role="tooltip" class="ttp15-card ttp15-card-left">
        <div class="ttp15-top"><div class="ttp15-bayer">γ Orionis</div><div class="ttp15-name">Bellatrix</div><div class="ttp15-const">Orion · Upper right shoulder</div><span class="ttp15-pill">B2 III · Blue Giant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">250 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">1.64</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~6,400 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Temp</span><span class="ttp15-val">22,000 K</span></div>
          <div class="ttp15-mag"><span class="ttp15-key">Brightness</span><span class="flex gap-0.5" role="img" aria-label="3 out of 5"><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star">★</span><span class="ttp15-star opacity-30">★</span><span class="ttp15-star opacity-30">★</span></span></div>
        </div>
      </div>
    </div>

    <div class="group absolute left-1/2 top-[57.5%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s4" aria-label="Alnilam, epsilon Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s4" role="tooltip" class="ttp15-card">
        <div class="ttp15-top"><div class="ttp15-bayer">ε Orionis</div><div class="ttp15-name">Alnilam</div><div class="ttp15-const">Orion · Belt, central star</div><span class="ttp15-pill">B0 Ia · Blue Supergiant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">2,000 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">1.69</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~375,000 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Temp</span><span class="ttp15-val">27,500 K</span></div>
        </div>
      </div>
    </div>

    <div class="group absolute left-1/2 top-[12%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s5" aria-label="Meissa, lambda Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s5" role="tooltip" class="ttp15-card">
        <div class="ttp15-top"><div class="ttp15-bayer">λ Orionis</div><div class="ttp15-name">Meissa</div><div class="ttp15-const">Orion · Head</div><span class="ttp15-pill">O8 III · Blue-White Giant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">1,100 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">3.39</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~28,000 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Temp</span><span class="ttp15-val">35,000 K</span></div>
        </div>
      </div>
    </div>

    <div class="group absolute left-[34%] top-[85.5%] z-10 -translate-x-1/2 -translate-y-1/2">
      <button type="button" aria-describedby="ttp15-s6" aria-label="Saiph, kappa Orionis" class="ttp15-hit"></button>
      <div id="ttp15-s6" role="tooltip" class="ttp15-card">
        <div class="ttp15-top"><div class="ttp15-bayer">κ Orionis</div><div class="ttp15-name">Saiph</div><div class="ttp15-const">Orion · Lower left</div><span class="ttp15-pill">B0.5 Ia · Blue Supergiant</span></div>
        <div class="px-3.25 py-2.5">
          <div class="ttp15-row"><span class="ttp15-key">Distance</span><span class="ttp15-val">720 ly</span></div>
          <div class="ttp15-row"><span class="ttp15-key">App. mag</span><span class="ttp15-val">2.07</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Luminosity</span><span class="ttp15-val">~57,500 L☉</span></div>
          <div class="ttp15-row"><span class="ttp15-key">Temp</span><span class="ttp15-val">26,500 K</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp15-bg: #04060e;
  --color-ttp15-bg: oklch(0.1 0.02 265);
  --color-ttp15-card: #080c1c;
  --color-ttp15-card: oklch(0.14 0.03 265);
  --color-ttp15-edge: #3a4680;
  --color-ttp15-edge: oklch(0.38 0.08 275);
  --color-ttp15-name: #dce6ff;
  --color-ttp15-name: oklch(0.92 0.03 270);
  --color-ttp15-val: #aec2f0;
  --color-ttp15-val: oklch(0.8 0.06 270);
  --color-ttp15-key: #8b9ccc;
  --color-ttp15-key: oklch(0.68 0.05 270);
  --color-ttp15-bayer: #9aa9e8;
  --color-ttp15-bayer: oklch(0.72 0.09 275);
  --color-ttp15-star: #ffdc50;
  --color-ttp15-star: oklch(0.88 0.15 92);
  --font-ttp15-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttp-15 {
  width: 100%;
  min-height: 100svh;
}
/* Six hotspots, one card at two placements. The flip is a modifier
   class rather than a script, because the chart is fixed geometry. */

.ttp-15 .ttp15-hit {
  @apply block h-11 w-11 cursor-help rounded-full border-0 bg-transparent p-0 transition-[background,box-shadow] duration-200 group-hover:bg-[rgba(180,200,255,0.08)] group-hover:shadow-[0_0_18px_6px_rgba(160,180,255,0.12)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp15-bayer;
}

.ttp-15 .ttp15-card {
  @apply pointer-events-none invisible absolute top-1/2 left-[calc(100%+14px)] z-50 w-[230px] -translate-y-1/2 translate-x-1.5 overflow-hidden rounded-lg border border-ttp15-edge/50 bg-ttp15-card/96 text-left opacity-0 shadow-[0_12px_38px_rgba(0,0,0,0.9),0_0_0_1px_rgba(100,120,200,0.06)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}

.ttp-15 .ttp15-card-left {
  @apply left-auto right-[calc(100%+14px)] -translate-x-1.5 group-hover:translate-x-0 group-focus-within:translate-x-0;
}

.ttp-15 .ttp15-top {
  @apply border-b border-ttp15-edge/30 px-3.25 pt-3 pb-2.5;
}

.ttp-15 .ttp15-bayer {
  @apply mb-0.75 text-[9.5px] tracking-[0.1em] text-ttp15-bayer;
}

.ttp-15 .ttp15-name {
  @apply mb-px text-[15px] font-medium text-ttp15-name;
}

.ttp-15 .ttp15-const {
  @apply text-[10px] text-ttp15-key;
}

.ttp-15 .ttp15-pill {
  @apply mt-1.5 inline-block rounded-[3px] border border-ttp15-edge/50 px-1.75 py-0.5 text-[9px] tracking-[0.06em] text-ttp15-val;
}

.ttp-15 .ttp15-row {
  @apply mb-1.25 flex justify-between;
}

.ttp-15 .ttp15-key {
  @apply text-[9.5px] tracking-[0.08em] text-ttp15-key;
}

.ttp-15 .ttp15-val {
  @apply text-[10px] text-ttp15-val;
}

.ttp-15 .ttp15-mag {
  @apply mt-2 flex items-center gap-2 border-t border-ttp15-edge/25 pt-2;
}

.ttp-15 .ttp15-star {
  @apply text-[10px] text-ttp15-star;
}

@media (max-width: 1279px) {
  .ttp-15 .ttp15-card,
    .ttp-15 .ttp15-card-left {
    /* position:fixed resolves against the nearest transformed ancestor,
           not the viewport, and the star hotspots sit inside one — so
           inset-x-4 + w-auto collapsed the card to 12px instead of
           spanning the screen. Stay absolute with an explicit width. */

    @apply absolute left-1/2 right-auto top-full bottom-auto mt-3 w-[230px] -translate-x-1/2 translate-y-0;
  }
}
```
