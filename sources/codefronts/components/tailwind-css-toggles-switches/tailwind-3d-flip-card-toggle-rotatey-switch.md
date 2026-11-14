---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-3d-flip-card-toggle-rotatey-switch/"
title: "Tailwind 3D Flip Card Toggle (rotateY Switch)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A boolean as a physical object: the whole control rotates 180&deg; to reveal its other face &mdash; muted \"Paused\" on the front, vivid \"Active\" with a live…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Card Toggle (rotateY Switch)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-3d-flip-card-toggle-rotatey-switch/

A boolean as a physical object: the whole control rotates 180&deg; to reveal its other face &mdash; muted "Paused" on the front, vivid "Active" with a live figure on the back. v4's first-class 3D utilities mean the entire flip is five classes.
## HTML
```html
<section class="ttg-19 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg19-bg font-ttg19-sans" aria-label="3D flip card toggle">
  <input type="checkbox" id="ttg-19-sw" role="switch" aria-label="Campaign active" class="peer sr-only">
  <label for="ttg-19-sw" aria-hidden="true" class="block cursor-pointer perspective-[900px] peer-checked:[&_.ttg19-card]:rotate-y-180 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg19-focus peer-focus-visible:outline-offset-[5px] peer-focus-visible:rounded-[18px]">
    <span class="ttg19-card relative block w-[230px] h-[130px] transform-3d transition-transform duration-[650ms] ease-[cubic-bezier(0.4,0.2,0.2,1.15)] motion-reduce:duration-150">
      <span class="absolute inset-0 flex flex-col items-center justify-center gap-1.5 rounded-2xl backface-hidden bg-linear-150 from-ttg19-frontthi to-ttg19-frontlo text-ttg19-frontink shadow-[0_18px_36px_-20px_oklch(0.3_0.03_265/0.55)]">
        <b class="text-2xl font-extrabold tracking-[0.12em]">PAUSED</b>
        <small class="text-[12.5px] opacity-80">Campaign is not spending</small>
      </span>
      <span class="absolute inset-0 flex flex-col items-center justify-center gap-1.5 rounded-2xl backface-hidden rotate-y-180 bg-linear-150 from-ttg19-backhi to-ttg19-backlo text-white shadow-[0_18px_36px_-20px_oklch(0.3_0.08_160/0.55)]">
        <b class="text-2xl font-extrabold tracking-[0.12em]">ACTIVE</b>
        <small class="text-[12.5px] opacity-90">Ads are live &middot; $184/day</small>
      </span>
    </span>
  </label>
  <p class="text-[12px] tracking-[0.12em] uppercase text-ttg19-mute">Click the card to flip state</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg19-bg: #eff0f5;
  --color-ttg19-bg: oklch(0.95 0.006 265);
  --color-ttg19-frontthi: #fdfdfe;
  --color-ttg19-frontthi: oklch(0.99 0.002 265);
  --color-ttg19-frontlo: #e4e7ee;
  --color-ttg19-frontlo: oklch(0.92 0.008 265);
  --color-ttg19-frontink: #4d5566;
  --color-ttg19-frontink: oklch(0.44 0.02 265);
  --color-ttg19-backhi: #2fa368;
  --color-ttg19-backhi: oklch(0.64 0.16 155);
  --color-ttg19-backlo: #1d7a5f;
  --color-ttg19-backlo: oklch(0.51 0.12 170);
  --color-ttg19-mute: #8a91a1;
  --color-ttg19-mute: oklch(0.64 0.015 265);
  --color-ttg19-focus: #3f63e0;
  --color-ttg19-focus: oklch(0.55 0.19 265);
  --font-ttg19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-19 {
  width: 100%;
  min-height: 100svh;
}
```
