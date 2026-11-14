---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-radial-vu-meter-mute-toggle/"
title: "Tailwind Radial VU Meter Mute Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The waveform idea rebuilt as studio hardware: a radial VU meter whose needle sweeps while audio is live and drops to the peg when muted, over a masked conic…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radial VU Meter Mute Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-radial-vu-meter-mute-toggle/

The waveform idea rebuilt as studio hardware: a radial VU meter whose needle sweeps while audio is live and drops to the peg when muted, over a masked conic arc that runs green through amber to red. Same job as demo 09, a completely different read.
## HTML
```html
<section class="ttg-29 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg29-bg font-ttg29-sans" aria-label="Radial VU meter mute toggle">
  <label for="ttg-29-sw" class="flex flex-col items-center gap-5 px-9 py-7 rounded-[24px] cursor-pointer bg-ttg29-card border border-ttg29-edge has-checked:[&_.ttg29-arc]:saturate-150 has-checked:[&_.ttg29-needle]:animate-ttg29-needle has-checked:[&_.ttg29-lamp]:bg-ttg29-live has-checked:[&_.ttg29-lamp]:shadow-[0_0_10px_var(--color-ttg29-live)] motion-reduce:has-checked:[&_.ttg29-needle]:animate-none motion-reduce:has-checked:[&_.ttg29-needle]:rotate-[8deg]">
    <span class="relative grid place-items-center w-38 h-38 rounded-full bg-ttg29-face shadow-[inset_0_2px_10px_oklch(0_0_0/0.55)]">
      <span aria-hidden="true" class="ttg29-arc absolute inset-2 rounded-full saturate-50 transition-[filter] duration-500 [background:conic-gradient(from_230deg,var(--color-ttg29-ok)_0deg,var(--color-ttg29-ok)_70deg,var(--color-ttg29-warn)_110deg,var(--color-ttg29-hot)_145deg,transparent_150deg)] [mask:radial-gradient(circle,transparent_52px,#000_53px)]"></span>
      <span aria-hidden="true" class="ttg29-needle absolute bottom-1/2 left-1/2 -ml-[1.5px] w-[3px] h-14 rounded-full bg-ttg29-needle origin-bottom rotate-[-52deg] transition-transform duration-500 ease-out shadow-[0_0_6px_oklch(0_0_0/0.5)]"></span>
      <span aria-hidden="true" class="absolute bottom-1/2 left-1/2 -ml-2 -mb-2 w-4 h-4 rounded-full bg-ttg29-pivot shadow-[inset_0_-1px_2px_oklch(0_0_0/0.6)]"></span>
      <span aria-hidden="true" class="ttg29-lamp absolute bottom-6 w-2 h-2 rounded-full bg-ttg29-lampoff transition-[background-color,box-shadow] duration-300"></span>
      <input type="checkbox" id="ttg-29-sw" role="switch" checked aria-label="Studio monitor" class="appearance-none absolute inset-0 w-full h-full rounded-full bg-transparent cursor-pointer z-10 focus-visible:outline-3 focus-visible:outline-ttg29-live focus-visible:outline-offset-4">
    </span>
    <span class="flex flex-col items-center gap-0.5 text-center">
      <span class="text-[15.5px] font-semibold text-ttg29-ink">Studio monitor</span>
      <span class="font-ttg29-mono text-[11px] tracking-[0.14em] uppercase text-ttg29-mute">Needle swinging = live &middot; pegged = muted</span>
    </span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg29-bg: #0e1115;
  --color-ttg29-bg: oklch(0.17 0.008 255);
  --color-ttg29-card: #171b21;
  --color-ttg29-card: oklch(0.23 0.01 255);
  --color-ttg29-edge: #272d36;
  --color-ttg29-edge: oklch(0.31 0.012 255);
  --color-ttg29-face: #12161b;
  --color-ttg29-face: oklch(0.2 0.01 255);
  --color-ttg29-ok: #3ddc9a;
  --color-ttg29-ok: oklch(0.82 0.16 165);
  --color-ttg29-warn: #f0c04a;
  --color-ttg29-warn: oklch(0.84 0.14 90);
  --color-ttg29-hot: #ff5d4a;
  --color-ttg29-hot: oklch(0.68 0.21 27);
  --color-ttg29-needle: #f2f5fa;
  --color-ttg29-needle: oklch(0.96 0.005 255);
  --color-ttg29-pivot: #3b434f;
  --color-ttg29-pivot: oklch(0.4 0.014 255);
  --color-ttg29-live: #3ddc9a;
  --color-ttg29-live: oklch(0.82 0.16 165);
  --color-ttg29-lampoff: #2b323c;
  --color-ttg29-lampoff: oklch(0.32 0.012 255);
  --color-ttg29-ink: #d5dce6;
  --color-ttg29-ink: oklch(0.9 0.01 255);
  --color-ttg29-mute: #8f97a5;
  --color-ttg29-mute: oklch(0.67 0.015 255);
  --font-ttg29-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg29-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-ttg29-needle: ttg29-needle 1.7s ease-in-out infinite alternate;
}

@keyframes ttg29-needle {
  0% {
    transform: rotate(-14deg);
  }

  35% {
    transform: rotate(22deg);
  }

  60% {
    transform: rotate(2deg);
  }

  100% {
    transform: rotate(34deg);
  }
}

.ttg-29 {
  width: 100%;
  min-height: 100svh;
}

.ttg-29 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
