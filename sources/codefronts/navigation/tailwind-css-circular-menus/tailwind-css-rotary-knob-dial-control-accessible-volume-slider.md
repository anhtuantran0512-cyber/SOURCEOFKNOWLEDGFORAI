---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-rotary-knob-dial-control-accessible-volume-slider/"
title: "Tailwind CSS Rotary Knob Dial Control (Accessible Volume Slider)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A hi-fi amplifier knob driven by one custom property: --val fills a conic value arc, rotates the brushed cap, and lights each of 28 LED ticks through…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Rotary Knob Dial Control (Accessible Volume Slider)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-rotary-knob-dial-control-accessible-volume-slider/

A hi-fi amplifier knob driven by one custom property: --val fills a conic value arc, rotates the brushed cap, and lights each of 28 LED ticks through [opacity:clamp(0,calc((var(--val)-k)*10),1)] &mdash; no per-tick JavaScript. It is a real ARIA slider: drag around it, scroll, use arrow keys, Home/End or the three presets.
## HTML
```html
<section class="tcm-08 w-full min-h-svh grid place-items-center bg-tcm08-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm08-glow),transparent_72%)] px-5 py-14 font-tcm08-sans text-tcm08-ink antialiased" aria-label="Rotary knob dial control demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tcm-08-amp" class="grid w-full max-w-[24rem] justify-items-center gap-6 rounded-[2rem] bg-linear-to-b from-tcm08-face to-tcm08-face2 px-6 pt-6 pb-8 shadow-tcm08-amp ring-1 ring-tcm08-line [--val:62]">
      <div class="flex w-full items-center justify-between">
        <p class="font-tcm08-mono text-[11px] tracking-[0.22em] text-tcm08-mut uppercase">Aster · A-40</p>
        <p class="inline-flex items-center gap-1.5 font-tcm08-mono text-[11px] text-tcm08-acc-ink"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcm08-acc shadow-tcm08-led"></span>Phono</p>
      </div>
      <div class="relative grid size-[16rem] place-items-center">
        <div aria-hidden="true" class="absolute inset-0">
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(225deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-0.0)*10),1)] [--k:0]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(235deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-3.7)*10),1)] [--k:1]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(245deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-7.4)*10),1)] [--k:2]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(255deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-11.1)*10),1)] [--k:3]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(265deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-14.8)*10),1)] [--k:4]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(275deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-18.5)*10),1)] [--k:5]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(285deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-22.2)*10),1)] [--k:6]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(295deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-25.9)*10),1)] [--k:7]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(305deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-29.6)*10),1)] [--k:8]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(315deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-33.3)*10),1)] [--k:9]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(325deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-37.0)*10),1)] [--k:10]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(335deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-40.7)*10),1)] [--k:11]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(345deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-44.4)*10),1)] [--k:12]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(355deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-48.1)*10),1)] [--k:13]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(365deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-51.9)*10),1)] [--k:14]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(375deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-55.6)*10),1)] [--k:15]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(385deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-59.3)*10),1)] [--k:16]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(395deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-63.0)*10),1)] [--k:17]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(405deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-66.7)*10),1)] [--k:18]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(415deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-70.4)*10),1)] [--k:19]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(425deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-74.1)*10),1)] [--k:20]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(435deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-77.8)*10),1)] [--k:21]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(445deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-81.5)*10),1)] [--k:22]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(455deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-85.2)*10),1)] [--k:23]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(465deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-88.9)*10),1)] [--k:24]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(475deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-92.6)*10),1)] [--k:25]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(485deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-96.3)*10),1)] [--k:26]"></i>
          <i class="absolute top-1/2 left-1/2 -ml-px h-2.5 w-0.5 rounded-full bg-tcm08-tick [transform:rotate(495deg)_translateY(-7.4rem)] after:absolute after:inset-0 after:rounded-full after:bg-tcm08-acc after:shadow-tcm08-led after:[opacity:clamp(0,calc((var(--val)-100.0)*10),1)] [--k:27]"></i>
        </div>
        <div data-knob role="slider" tabindex="0" aria-label="Volume" aria-valuemin="0" aria-valuemax="100" aria-valuenow="62" aria-valuetext="62 percent" class="relative grid size-[12rem] cursor-grab touch-none place-items-center rounded-full bg-[conic-gradient(from_225deg,var(--color-tcm08-acc)_calc(var(--val)*2.7deg),var(--color-tcm08-track)_calc(var(--val)*2.7deg)_270deg,transparent_270deg)] p-1.5 select-none active:cursor-grabbing focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-tcm08-ring">
          <span class="relative size-full rounded-full bg-[radial-gradient(circle_at_35%_28%,var(--color-tcm08-cap-hi),var(--color-tcm08-cap)_70%)] shadow-tcm08-cap rotate-[calc(var(--val)*2.7deg-135deg)]">
            <span class="absolute inset-[18%] rounded-full bg-[repeating-conic-gradient(var(--color-tcm08-grain)_0_1deg,transparent_1deg_4deg)] opacity-40"></span>
            <i class="absolute top-3 left-1/2 -ml-1.5 size-3 rounded-full bg-tcm08-acc shadow-tcm08-led"></i>
          </span>
        </div>
      </div>
      <div class="flex w-full items-end justify-between">
        <p class="font-tcm08-mono text-[10px] tracking-[0.2em] text-tcm08-mut uppercase">Min</p>
        <p class="grid justify-items-center"><output data-val class="font-tcm08-mono text-[2.4rem] leading-none font-semibold tabular-nums">62</output><span class="mt-1 text-[10.5px] tracking-[0.3em] text-tcm08-mut uppercase">Volume</span></p>
        <p class="font-tcm08-mono text-[10px] tracking-[0.2em] text-tcm08-mut uppercase">Max</p>
      </div>
      <div class="flex gap-2" role="group" aria-label="Presets">
        <button type="button" data-preset="20" class="min-h-11 cursor-pointer rounded-xl bg-tcm08-key px-4 font-tcm08-mono text-[12px] text-tcm08-ink shadow-tcm08-key ring-1 ring-tcm08-line transition-colors hover:text-tcm08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm08-ring">Quiet</button>
        <button type="button" data-preset="55" class="min-h-11 cursor-pointer rounded-xl bg-tcm08-key px-4 font-tcm08-mono text-[12px] text-tcm08-ink shadow-tcm08-key ring-1 ring-tcm08-line transition-colors hover:text-tcm08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm08-ring">Room</button>
        <button type="button" data-preset="88" class="min-h-11 cursor-pointer rounded-xl bg-tcm08-key px-4 font-tcm08-mono text-[12px] text-tcm08-ink shadow-tcm08-key ring-1 ring-tcm08-line transition-colors hover:text-tcm08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm08-ring">Party</button>
      </div>
    </div>
    <p class="text-[13px] text-tcm08-mut">Drag around the knob · scroll · arrow keys · Home / End</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm08-card px-3.5 py-2 text-center font-tcm08-mono text-[11.5px] text-tcm08-mut ring-1 ring-tcm08-line ">role="slider" · conic-gradient(…calc(var(--val)*2.7deg)) · [opacity:clamp(…)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm08-bg: #eef3ec;
  --color-tcm08-bg: oklch(0.958 0.011 136.6);
  --color-tcm08-glow: #d9f99d80;
  --color-tcm08-glow: oklch(0.938 0.122 124.3 / 0.5);
  --color-tcm08-face: #fbfcf8;
  --color-tcm08-face: oklch(0.989 0.005 117.9);
  --color-tcm08-face2: #eef1ea;
  --color-tcm08-face2: oklch(0.954 0.01 125.7);
  --color-tcm08-cap: #e6e9e2;
  --color-tcm08-cap: oklch(0.93 0.01 125.7);
  --color-tcm08-cap-hi: #ffffff;
  --color-tcm08-cap-hi: oklch(1 0 0);
  --color-tcm08-grain: #8a9585;
  --color-tcm08-grain: oklch(0.656 0.026 135.7);
  --color-tcm08-track: #dde3d8;
  --color-tcm08-track: oklch(0.908 0.016 130.4);
  --color-tcm08-tick: #c9d1c4;
  --color-tcm08-tick: oklch(0.851 0.02 133.1);
  --color-tcm08-key: #f7f9f4;
  --color-tcm08-key: oklch(0.979 0.007 124.4);
  --color-tcm08-ink: #161c14;
  --color-tcm08-ink: oklch(0.217 0.018 137.9);
  --color-tcm08-mut: #5b6656;
  --color-tcm08-mut: oklch(0.496 0.028 135.8);
  --color-tcm08-line: #d7ddd1;
  --color-tcm08-line: oklch(0.89 0.017 128.7);
  --color-tcm08-acc: #65a30d;
  --color-tcm08-acc: oklch(0.648 0.175 131.7);
  --color-tcm08-acc-ink: #3f6212;
  --color-tcm08-acc-ink: oklch(0.453 0.113 130.9);
  --color-tcm08-ring: #4d7c0f;
  --color-tcm08-ring: oklch(0.532 0.141 131.6);
  --color-tcm08-card: #fbfcf8;
  --color-tcm08-card: oklch(0.989 0.005 117.9);
  --font-tcm08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcm08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm08-amp: 0 1px 0 oklch(1 0 0 / 0.6) inset, 0 34px 70px -30px oklch(0.25 0.04 130 / 0.55);
  --shadow-tcm08-cap: 0 16px 30px -10px oklch(0 0 0 / 0.45), inset 0 1px 0 oklch(1 0 0 / 0.35), inset 0 -8px 16px oklch(0 0 0 / 0.18);
  --shadow-tcm08-led: 0 0 10px oklch(0.8 0.2 130 / 0.85);
  --shadow-tcm08-key: 0 1px 0 oklch(1 0 0 / 0.5) inset, 0 2px 4px oklch(0 0 0 / 0.08);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-08 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: studio black: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-08:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm08-bg: #0b0e0b;
    --color-tcm08-bg: oklch(0.159 0.008 145.2);
    --color-tcm08-glow: #3f621259;
    --color-tcm08-glow: oklch(0.453 0.113 130.9 / 0.35);
    --color-tcm08-face: #1a1f19;
    --color-tcm08-face: oklch(0.232 0.014 140.4);
    --color-tcm08-face2: #121611;
    --color-tcm08-face2: oklch(0.194 0.012 139.4);
    --color-tcm08-cap: #20261e;
    --color-tcm08-cap: oklch(0.26 0.017 137.9);
    --color-tcm08-cap-hi: #3a4237;
    --color-tcm08-cap-hi: oklch(0.368 0.021 137.1);
    --color-tcm08-grain: #000000;
    --color-tcm08-grain: oklch(0 0 0);
    --color-tcm08-track: #2a3128;
    --color-tcm08-track: oklch(0.303 0.019 138.7);
    --color-tcm08-tick: #323a30;
    --color-tcm08-tick: oklch(0.338 0.02 139.4);
    --color-tcm08-key: #1c211b;
    --color-tcm08-key: oklch(0.24 0.013 140.4);
    --color-tcm08-ink: #eef3ea;
    --color-tcm08-ink: oklch(0.958 0.013 130.8);
    --color-tcm08-mut: #9aa694;
    --color-tcm08-mut: oklch(0.71 0.029 135);
    --color-tcm08-line: #2b3329;
    --color-tcm08-line: oklch(0.31 0.021 139.4);
    --color-tcm08-acc: #a3e635;
    --color-tcm08-acc: oklch(0.849 0.207 128.8);
    --color-tcm08-acc-ink: #bef264;
    --color-tcm08-acc-ink: oklch(0.897 0.179 126.7);
    --color-tcm08-ring: #bef264;
    --color-tcm08-ring: oklch(0.897 0.179 126.7);
    --color-tcm08-card: #151a14;
    --color-tcm08-card: oklch(0.21 0.014 140.4);
  }
}

.tcm-08[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm08-bg: #0b0e0b;
  --color-tcm08-bg: oklch(0.159 0.008 145.2);
  --color-tcm08-glow: #3f621259;
  --color-tcm08-glow: oklch(0.453 0.113 130.9 / 0.35);
  --color-tcm08-face: #1a1f19;
  --color-tcm08-face: oklch(0.232 0.014 140.4);
  --color-tcm08-face2: #121611;
  --color-tcm08-face2: oklch(0.194 0.012 139.4);
  --color-tcm08-cap: #20261e;
  --color-tcm08-cap: oklch(0.26 0.017 137.9);
  --color-tcm08-cap-hi: #3a4237;
  --color-tcm08-cap-hi: oklch(0.368 0.021 137.1);
  --color-tcm08-grain: #000000;
  --color-tcm08-grain: oklch(0 0 0);
  --color-tcm08-track: #2a3128;
  --color-tcm08-track: oklch(0.303 0.019 138.7);
  --color-tcm08-tick: #323a30;
  --color-tcm08-tick: oklch(0.338 0.02 139.4);
  --color-tcm08-key: #1c211b;
  --color-tcm08-key: oklch(0.24 0.013 140.4);
  --color-tcm08-ink: #eef3ea;
  --color-tcm08-ink: oklch(0.958 0.013 130.8);
  --color-tcm08-mut: #9aa694;
  --color-tcm08-mut: oklch(0.71 0.029 135);
  --color-tcm08-line: #2b3329;
  --color-tcm08-line: oklch(0.31 0.021 139.4);
  --color-tcm08-acc: #a3e635;
  --color-tcm08-acc: oklch(0.849 0.207 128.8);
  --color-tcm08-acc-ink: #bef264;
  --color-tcm08-acc-ink: oklch(0.897 0.179 126.7);
  --color-tcm08-ring: #bef264;
  --color-tcm08-ring: oklch(0.897 0.179 126.7);
  --color-tcm08-card: #151a14;
  --color-tcm08-card: oklch(0.21 0.014 140.4);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-08-amp');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const knob = root.querySelector('[data-knob]');
  const out = root.querySelector('[data-val]');
  let val = 62;
  const setVal = (v) => {
    val = Math.max(0, Math.min(100, Math.round(v)));
    root.style.setProperty('--val', val);
    knob.setAttribute('aria-valuenow', val);
    knob.setAttribute('aria-valuetext', val + ' percent');
    out.textContent = val;
  };
  const fromPointer = (e) => {
    const r = knob.getBoundingClientRect();
    let deg = Math.atan2(e.clientY - (r.top + r.height / 2), e.clientX - (r.left + r.width / 2)) * 180 / Math.PI;
    deg = (deg - 135 + 360) % 360;
    if (deg > 270) deg = deg < 315 ? 270 : 0;
    setVal(deg / 270 * 100);
  };
  knob.addEventListener('pointerdown', (e) => {
    knob.setPointerCapture(e.pointerId); fromPointer(e);
    const move = (ev) => fromPointer(ev);
    knob.addEventListener('pointermove', move);
    knob.addEventListener('pointerup', () => knob.removeEventListener('pointermove', move), { once: true });
  });
  knob.addEventListener('wheel', (e) => { e.preventDefault(); setVal(val + (e.deltaY < 0 ? 2 : -2)); }, { passive: false });
  knob.addEventListener('keydown', (e) => {
    const step = { ArrowUp: 1, ArrowRight: 1, ArrowDown: -1, ArrowLeft: -1, PageUp: 10, PageDown: -10 }[e.key];
    if (step) { e.preventDefault(); setVal(val + step); }
    if (e.key === 'Home') { e.preventDefault(); setVal(0); }
    if (e.key === 'End') { e.preventDefault(); setVal(100); }
  });
  root.querySelectorAll('[data-preset]').forEach((b) => b.addEventListener('click', () => setVal(Number(b.dataset.preset))));
  setVal(val);
})();
```
