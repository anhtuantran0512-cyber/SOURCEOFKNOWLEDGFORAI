---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-photo-grid-exif-tooltip-camera-settings-card/"
title: "Tailwind Photo Grid EXIF Tooltip with Camera Settings Card"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A contact-sheet grid where hovering a frame shows its EXIF: body, lens, date, then aperture, shutter and ISO in three columns, with focal length, white…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Photo Grid EXIF Tooltip with Camera Settings Card
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-photo-grid-exif-tooltip-camera-settings-card/

A contact-sheet grid where hovering a frame shows its EXIF: body, lens, date, then aperture, shutter and ISO in three columns, with focal length, white balance and location beneath. Eight identical cards, eight different gradients &mdash; the port's split of shell into @apply and image into inline values, one more time.
## HTML
```html
<section class="ttp-17 w-full min-h-svh bg-ttp17-bg px-7 pt-[220px] pb-10 font-ttp17-mono">
  <div class="mx-auto grid max-w-[600px] grid-cols-4 gap-[3px] max-sm:grid-cols-2">

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p1" aria-label="Photograph: Malibu, March 2024" class="ttp17-frame bg-[linear-gradient(160deg,#c86020_0%,#e8a030_40%,#f0c060_70%,#a04010_100%)]"></button>
      <div id="ttp17-p1" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Sony A7 IV</div><div class="ttp17-lens">FE 24-70mm f/2.8 GM</div></div><div class="ttp17-date">Mar 14, 2024</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/8.0</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/250s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">100</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>35mm</strong></span><span>WB: <strong>Daylight</strong></span><span>Malibu, CA</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p2" aria-label="Photograph: portrait, January 2024" class="ttp17-frame bg-[linear-gradient(145deg,#1a1218_0%,#2c1828_50%,#180c14_100%)]"></button>
      <div id="ttp17-p2" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Nikon Z6 III</div><div class="ttp17-lens">NIKKOR Z 85mm f/1.8 S</div></div><div class="ttp17-date">Jan 8, 2024</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/1.8</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/160s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">800</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>85mm</strong></span><span>WB: <strong>Tungsten</strong></span><span>Flash: <strong>Off</strong></span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p3" aria-label="Photograph: Big Sur, February 2024" class="ttp17-frame bg-[linear-gradient(180deg,#082840_0%,#0c4060_35%,#1060a0_70%,#082040_100%)]"></button>
      <div id="ttp17-p3" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Fujifilm X-T5</div><div class="ttp17-lens">XF 16-80mm f/4 R</div></div><div class="ttp17-date">Feb 22, 2024</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/11</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/500s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">200</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>16mm</strong></span><span>WB: <strong>Cloudy</strong></span><span>Big Sur, CA</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p4" aria-label="Photograph: Olympic National Park, April 2024" class="ttp17-frame bg-[linear-gradient(135deg,#0c1e10_0%,#1a3818_40%,#2a5a28_70%,#0c2010_100%)]"></button>
      <div id="ttp17-p4" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Canon EOS R5</div><div class="ttp17-lens">RF 24-105mm f/4L IS</div></div><div class="ttp17-date">Apr 5, 2024</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/5.6</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/60s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">400</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Shade</strong></span><span>Olympic NP</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p5" aria-label="Photograph: Tokyo, December 2023" class="ttp17-frame bg-[linear-gradient(160deg,#080c18_0%,#101428_40%,#181c30_70%,#0c0e20_100%)]"></button>
      <div id="ttp17-p5" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Sony A7 IV</div><div class="ttp17-lens">FE 50mm f/1.4 GM</div></div><div class="ttp17-date">Dec 18, 2023</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/2.0</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/30s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">3200</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Auto</strong></span><span>Tokyo, JP</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p6" aria-label="Photograph: Sahara, November 2023" class="ttp17-frame bg-[linear-gradient(155deg,#604020_0%,#d09050_40%,#f0c880_70%,#806030_100%)]"></button>
      <div id="ttp17-p6" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Hasselblad X2D</div><div class="ttp17-lens">XCD 45mm f/3.5</div></div><div class="ttp17-date">Nov 3, 2023</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/16</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/1000s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">64</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>45mm</strong></span><span>WB: <strong>Daylight</strong></span><span>Sahara, MA</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p7" aria-label="Photograph: Scottish Highlands, October 2023" class="ttp17-frame bg-[linear-gradient(170deg,#c8c8cc_0%,#a8a8b0_40%,#d0d0d4_70%,#b0b0b8_100%)]"></button>
      <div id="ttp17-p7" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Leica M11</div><div class="ttp17-lens">Summicron 50mm f/2</div></div><div class="ttp17-date">Oct 14, 2023</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/4.0</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">1/125s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">200</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>50mm</strong></span><span>WB: <strong>Cloudy</strong></span><span>Highlands, UK</span></div>
      </div>
    </div>

    <div class="group relative aspect-[3/2]">
      <button type="button" aria-describedby="ttp17-p8" aria-label="Photograph: Iceland aurora, September 2023" class="ttp17-frame bg-[linear-gradient(150deg,#200830_0%,#401060_40%,#602080_65%,#100420_100%)]"></button>
      <div id="ttp17-p8" role="tooltip" class="ttp17-card">
        <div class="ttp17-chead"><div><div class="ttp17-cam">Nikon Z6 III</div><div class="ttp17-lens">NIKKOR Z 14-30mm f/4 S</div></div><div class="ttp17-date">Sep 27, 2023</div></div>
        <div class="ttp17-grid"><div class="ttp17-set"><div class="ttp17-key">Aperture</div><div class="ttp17-val">f/2.8</div></div><div class="ttp17-set"><div class="ttp17-key">Shutter</div><div class="ttp17-val">20s</div></div><div class="ttp17-set border-r-0"><div class="ttp17-key">ISO</div><div class="ttp17-val">1600</div></div></div>
        <div class="ttp17-extra"><span>Focal: <strong>14mm</strong></span><span>WB: <strong>3200K</strong></span><span>Iceland</span></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp17-bg: #080808;
  --color-ttp17-bg: oklch(0.14 0 0);
  --color-ttp17-card: #111111;
  --color-ttp17-card: oklch(0.18 0 0);
  --color-ttp17-bright: #e8e8e8;
  --color-ttp17-bright: oklch(0.92 0 0);
  --color-ttp17-ink: #bdbdbd;
  --color-ttp17-ink: oklch(0.8 0 0);
  --color-ttp17-dim: #969696;
  --color-ttp17-dim: oklch(0.66 0 0);
  --font-ttp17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttp-17 {
  width: 100%;
  min-height: 100svh;
}
/* Eight frames, eight identical EXIF cards. Only the gradient that
   stands in for the photograph differs, and that stays inline. */

.ttp-17 .ttp17-frame {
  @apply block h-full w-full cursor-help border-0 p-0 transition-[filter] duration-200 group-hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp17-bright;
}

.ttp-17 .ttp17-card {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+8px)] left-1/2 z-100 w-[230px] max-w-[calc(100vw-48px)] -translate-x-1/2 -translate-y-1.5 overflow-hidden rounded-md border border-white/10 bg-ttp17-card text-left opacity-0 shadow-[0_16px_44px_rgba(0,0,0,0.98)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}

.ttp-17 .ttp17-chead {
  @apply flex items-end justify-between gap-2 border-b border-white/8 px-3.25 py-2.75;
}

.ttp-17 .ttp17-cam {
  @apply text-[10.5px] text-ttp17-bright;
}

.ttp-17 .ttp17-lens {
  @apply mt-0.5 text-[9px] text-ttp17-dim;
}

.ttp-17 .ttp17-date {
  @apply text-[9px] text-ttp17-dim;
}

.ttp-17 .ttp17-grid {
  @apply grid grid-cols-3 border-b border-white/8;
}

.ttp-17 .ttp17-set {
  @apply border-r border-white/8 px-3.25 py-2.25;
}

.ttp-17 .ttp17-key {
  @apply mb-0.5 text-[8px] uppercase tracking-[0.1em] text-ttp17-dim;
}

.ttp-17 .ttp17-val {
  @apply text-[10.5px] text-ttp17-ink;
}

.ttp-17 .ttp17-extra {
  @apply flex justify-between gap-1.5 px-3.25 py-2 text-[9px] text-ttp17-dim;
}

.ttp-17 .ttp17-extra strong {
  @apply font-medium text-ttp17-ink;
}
```
