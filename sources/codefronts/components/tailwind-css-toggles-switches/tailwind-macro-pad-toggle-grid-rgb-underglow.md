---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-macro-pad-toggle-grid-rgb-underglow/"
title: "Tailwind Macro-Pad Toggle Grid with RGB Underglow"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Demo 08's keycap idea taken to a six-key macro pad: a 3&times;2 grid of latching keys over an RGB underglow that blooms through the chassis gaps, each key…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Macro-Pad Toggle Grid with RGB Underglow
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-macro-pad-toggle-grid-rgb-underglow/

Demo 08's keycap idea taken to a six-key macro pad: a 3&times;2 grid of latching keys over an RGB underglow that blooms through the chassis gaps, each key showing its shortcut, and a live count of what is armed. Denser, louder, and it scans in one glance.
## HTML
```html
<section class="ttg-28 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg28-bg font-ttg28-mono" aria-label="Macro pad toggle grid">
  <div id="ttg-28-pad" class="relative grid grid-cols-3 gap-3.5 p-6 rounded-[26px] bg-linear-160 from-ttg28-boardhi to-ttg28-boardlo shadow-[0_30px_60px_-30px_oklch(0_0_0/0.95),inset_0_1px_0_oklch(1_0_0/0.08)]">
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.78 0.15 220)" data-action="mic">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" checked aria-label="Microphone" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">MIC</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F13</i>
      </span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.8 0.16 150)" data-action="cam">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" aria-label="Camera" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">CAM</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F14</i>
      </span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.72 0.19 22)" data-action="rec">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" aria-label="Recording" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">REC</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F15</i>
      </span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.82 0.15 95)" data-action="light">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" checked aria-label="Key light" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">LIGHT</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F16</i>
      </span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.76 0.16 300)" data-action="chat">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" aria-label="Chat overlay" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">CHAT</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F17</i>
      </span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.8 0.13 195)" data-action="mute">
      <span aria-hidden="true" class="ttg28-under pointer-events-none absolute inset-2 rounded-2xl bg-(--glow) blur-2xl opacity-0 transition-opacity duration-300"></span>
      <input type="checkbox" role="switch" aria-label="Alerts" class="peer appearance-none absolute inset-[-3px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 z-[5] flex flex-col items-center justify-center gap-1 rounded-xl bg-linear-to-b from-ttg28-caphi to-ttg28-caplo text-ttg28-legend shadow-[0_7px_0_var(--color-ttg28-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-checked:translate-y-[3px] peer-checked:text-(--glow) peer-checked:shadow-[0_4px_0_var(--color-ttg28-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),0_0_22px_-2px_var(--glow)] peer-checked:[&~.ttg28-under]:opacity-70 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg28-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,box-shadow]">
        <b class="text-[14px] font-bold tracking-[0.12em]">ALERT</b>
        <i class="not-italic text-[9px] tracking-[0.16em] text-ttg28-hint">F18</i>
      </span>
    </label>
  </div>
  <p id="ttg-28-count" aria-live="polite" class="font-ttg28-sans text-[11px] tracking-[0.14em] uppercase text-ttg28-mute">2 of 6 armed</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg28-bg: #111318;
  --color-ttg28-bg: oklch(0.18 0.006 265);
  --color-ttg28-boardhi: #272b33;
  --color-ttg28-boardhi: oklch(0.29 0.008 265);
  --color-ttg28-boardlo: #1a1d23;
  --color-ttg28-boardlo: oklch(0.23 0.007 265);
  --color-ttg28-caphi: #3e434c;
  --color-ttg28-caphi: oklch(0.38 0.01 265);
  --color-ttg28-caplo: #2c3038;
  --color-ttg28-caplo: oklch(0.3 0.009 265);
  --color-ttg28-stem: #15161a;
  --color-ttg28-stem: oklch(0.19 0.006 265);
  --color-ttg28-legend: #a0a7b3;
  --color-ttg28-legend: oklch(0.72 0.012 265);
  --color-ttg28-hint: #6d7480;
  --color-ttg28-hint: oklch(0.56 0.012 265);
  --color-ttg28-mute: #7d838f;
  --color-ttg28-mute: oklch(0.61 0.012 265);
  --color-ttg28-focus: #7db1ff;
  --color-ttg28-focus: oklch(0.76 0.13 250);
  --font-ttg28-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --font-ttg28-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-28 {
  width: 100%;
  min-height: 100svh;
}

.ttg-28 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* The underglow disc precedes the input in source order, so no sibling variant can reach
   it from the cap. One scoped rule is cheaper than restructuring six keys. */

.ttg-28 label:has(input:checked) .ttg28-under {
  opacity: 0.7;
}
```

## JavaScript
```js
(() => {
  const pad = document.querySelector('#ttg-28-pad');
  const count = document.querySelector('#ttg-28-count');
  if (!pad || !count) return;
  const inputs = () => [...pad.querySelectorAll('input[type="checkbox"]')];
  pad.addEventListener('change', () => {
    navigator.vibrate?.(8);
    const on = inputs().filter((i) => i.checked).length;
    count.textContent = on + ' of ' + inputs().length + ' armed';
  });
})();
```
