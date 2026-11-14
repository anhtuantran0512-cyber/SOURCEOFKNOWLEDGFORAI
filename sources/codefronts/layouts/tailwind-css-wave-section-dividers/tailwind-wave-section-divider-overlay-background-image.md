---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-section-divider-overlay-background-image/"
title: "Tailwind Wave Section Divider with an Overlay Background Image"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "A crisp wave over a full-bleed photo, with the contrast scrim, focal-point crop and LCP hygiene handled properly &mdash; the combination that usually goes…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Wave Section Divider with an Overlay Background Image
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-section-divider-overlay-background-image/

A crisp wave over a full-bleed photo, with the contrast scrim, focal-point crop and LCP hygiene handled properly &mdash; the combination that usually goes wrong when a divider is dropped onto imagery. The second variant masks the photo itself into a wave-edged ribbon.
## HTML
```html
<section class="twd-13 w-full min-h-svh flex flex-col bg-twd13-paper font-twd13-sans">

  <!-- Photo hero with scrim + wave -->
  <header class="relative isolate overflow-hidden text-white px-6 pt-21 pb-[clamp(96px,13vw,150px)] text-center before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-[linear-gradient(180deg,oklch(0.15_0.03_260/0.3),oklch(0.13_0.03_260/0.82))]">
    <img src="https://picsum.photos/seed/twd13a/1600/900" width="1600" height="900" alt="" fetchpriority="high" decoding="async" class="absolute inset-0 -z-20 w-full h-full object-cover object-[50%_35%]">
    <div class="relative max-w-[46ch] mx-auto">
      <p class="text-xs tracking-[0.2em] uppercase text-twd13-eyebrow mb-3">Full-bleed imagery</p>
      <h2 class="text-[clamp(27px,4.6vw,46px)] leading-[1.06] font-semibold mb-2.5 [text-shadow:0_2px_18px_oklch(0.15_0.03_260/0.55)]">Legible over any photo</h2>
      <p class="text-[15px]">Gradient scrim below, wave on top, text in the safe zone.</p>
    </div>
    <svg class="absolute inset-x-0 -bottom-px z-10 block w-full h-[clamp(56px,9vw,116px)] text-twd13-next [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,62 C280,118 560,10 840,54 C1080,92 1250,106 1440,74 L1440,120 L0,120 Z"></path>
    </svg>
  </header>
  <div class="bg-twd13-next text-twd13-nextink px-6 pt-6 pb-15 text-center">
    <p class="text-[15px]">The wave fill matches this section exactly &mdash; no sticker effect.</p>
  </div>

  <!-- Wave-masked image band -->
  <div class="bg-twd13-paper text-twd13-paperink px-6 py-10 text-center">
    <p class="text-[15px]">Text section</p>
  </div>
  <div role="img" aria-label="Coastline photograph shown inside a wave-shaped band" class="-my-6 h-[clamp(220px,32vw,380px)] bg-twd13-bandfallback bg-[url('https://picsum.photos/seed/twd13b/1600/700')] bg-cover bg-center bg-no-repeat [mask:var(--twd13-band)_no-repeat_center/100%_100%]"></div>
  <div class="bg-twd13-paper text-twd13-paperink px-6 py-10 text-center">
    <p class="text-[15px] max-w-[52ch] mx-auto">The photo itself is masked into a wave band &mdash; both edges curved, no SVG node.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd13-next: #f6f7fa;
  --color-twd13-next: oklch(0.97 0.01 250);
  --color-twd13-nextink: #3f4655;
  --color-twd13-nextink: oklch(0.42 0.03 250);
  --color-twd13-eyebrow: #dfe4ee;
  --color-twd13-eyebrow: oklch(0.91 0.01 250);
  --color-twd13-paper: #f3f5f8;
  --color-twd13-paper: oklch(0.96 0.01 230);
  --color-twd13-paperink: #414a55;
  --color-twd13-paperink: oklch(0.43 0.03 230);
  --color-twd13-bandfallback: #35657f;
  --color-twd13-bandfallback: oklch(0.45 0.07 230);
  --font-twd13-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* The ribbon cutter: a wave on the top AND bottom edge of one mask. */

.twd-13 {
  width: 100%;
  min-height: 100svh;
  --twd13-band: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201440%20400'%20preserveAspectRatio='none'%3E%3Cpath%20d='M0,70%20C360,-10%20700,120%201000,70%20C1180,40%201300,40%201440,66%20L1440,330%20C1200,410%20900,270%20620,326%20C420,366%20180,366%200,334%20Z'%20fill='%23000'/%3E%3C/svg%3E");
}
/* Safari < 15.4 mask shim for the photo band. */

.twd-13 [role="img"] {
  -webkit-mask: var(--twd13-band) no-repeat center/100% 100%;
}
```
