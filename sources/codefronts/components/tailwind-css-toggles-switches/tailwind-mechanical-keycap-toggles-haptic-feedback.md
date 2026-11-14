---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-mechanical-keycap-toggles-haptic-feedback/"
title: "Tailwind Mechanical Keycap Toggles with Haptic Feedback"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A bank of mechanical keycaps that latch: each cap travels down into its socket on press, stays seated and backlit when on, and fires an 8ms navigator.vibrate…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mechanical Keycap Toggles with Haptic Feedback
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-mechanical-keycap-toggles-haptic-feedback/

A bank of mechanical keycaps that latch: each cap travels down into its socket on press, stays seated and backlit when on, and fires an 8ms navigator.vibrate tick on hardware that supports it. The stem is a solid shadow-[0_7px_0_...] that shortens as the key bottoms out.
## HTML
```html
<section class="ttg-08 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg08-bg font-ttg08-mono" aria-label="Mechanical keycap toggles">
  <div id="ttg-08-board" class="flex gap-5 px-7 py-6 rounded-[22px] bg-linear-160 from-ttg08-boardhi to-ttg08-boardlo shadow-[0_24px_50px_-26px_oklch(0_0_0/0.9),inset_0_1px_0_oklch(1_0_0/0.07)]">
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.78 0.15 220)">
      <input type="checkbox" role="switch" checked aria-label="Microphone" class="peer appearance-none absolute inset-[-4px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 flex items-center justify-center rounded-[11px] bg-linear-to-b from-ttg08-caphi to-ttg08-caplo text-ttg08-legend text-[15px] font-bold tracking-[0.12em] shadow-[0_7px_0_var(--color-ttg08-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-active:shadow-[0_2px_0_var(--color-ttg08-stem),0_5px_10px_-4px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:translate-y-[3px] peer-checked:shadow-[0_4px_0_var(--color-ttg08-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:text-(--glow) peer-checked:[text-shadow:0_0_10px_var(--glow),0_0_26px_color-mix(in_oklab,var(--glow)_55%,transparent)] peer-checked:peer-active:translate-y-[5px] peer-focus-visible:outline-3 peer-focus-visible:outline-ttg08-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,text-shadow]">MIC</span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.8 0.16 150)">
      <input type="checkbox" role="switch" aria-label="Camera" class="peer appearance-none absolute inset-[-4px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 flex items-center justify-center rounded-[11px] bg-linear-to-b from-ttg08-caphi to-ttg08-caplo text-ttg08-legend text-[15px] font-bold tracking-[0.12em] shadow-[0_7px_0_var(--color-ttg08-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-active:shadow-[0_2px_0_var(--color-ttg08-stem),0_5px_10px_-4px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:translate-y-[3px] peer-checked:shadow-[0_4px_0_var(--color-ttg08-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:text-(--glow) peer-checked:[text-shadow:0_0_10px_var(--glow),0_0_26px_color-mix(in_oklab,var(--glow)_55%,transparent)] peer-checked:peer-active:translate-y-[5px] peer-focus-visible:outline-3 peer-focus-visible:outline-ttg08-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,text-shadow]">CAM</span>
    </label>
    <label class="relative block w-20 h-20 cursor-pointer" style="--glow:oklch(0.72 0.19 22)">
      <input type="checkbox" role="switch" aria-label="Recording" class="peer appearance-none absolute inset-[-4px] z-10 rounded-xl cursor-pointer">
      <span class="absolute inset-0 flex items-center justify-center rounded-[11px] bg-linear-to-b from-ttg08-caphi to-ttg08-caplo text-ttg08-legend text-[15px] font-bold tracking-[0.12em] shadow-[0_7px_0_var(--color-ttg08-stem),0_12px_18px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.1)] transition-[transform,box-shadow,color,text-shadow] duration-100 ease-out peer-active:translate-y-[5px] peer-active:shadow-[0_2px_0_var(--color-ttg08-stem),0_5px_10px_-4px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:translate-y-[3px] peer-checked:shadow-[0_4px_0_var(--color-ttg08-stem),0_8px_14px_-6px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.08)] peer-checked:text-(--glow) peer-checked:[text-shadow:0_0_10px_var(--glow),0_0_26px_color-mix(in_oklab,var(--glow)_55%,transparent)] peer-checked:peer-active:translate-y-[5px] peer-focus-visible:outline-3 peer-focus-visible:outline-ttg08-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-[color,text-shadow]">REC</span>
    </label>
  </div>
  <p class="font-ttg08-sans text-[11px] tracking-[0.14em] uppercase text-ttg08-mute">Latching keys &middot; haptic tick on supported devices</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg08-bg: #16181c;
  --color-ttg08-bg: oklch(0.2 0.006 265);
  --color-ttg08-boardhi: #262a31;
  --color-ttg08-boardhi: oklch(0.28 0.008 265);
  --color-ttg08-boardlo: #1b1e23;
  --color-ttg08-boardlo: oklch(0.23 0.007 265);
  --color-ttg08-caphi: #3d424b;
  --color-ttg08-caphi: oklch(0.38 0.01 265);
  --color-ttg08-caplo: #2c3038;
  --color-ttg08-caplo: oklch(0.3 0.009 265);
  --color-ttg08-stem: #15161a;
  --color-ttg08-stem: oklch(0.19 0.006 265);
  --color-ttg08-legend: #9aa1ad;
  --color-ttg08-legend: oklch(0.7 0.012 265);
  --color-ttg08-mute: #6b7280;
  --color-ttg08-mute: oklch(0.56 0.015 265);
  --color-ttg08-focus: #7db1ff;
  --color-ttg08-focus: oklch(0.76 0.13 250);
  --font-ttg08-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --font-ttg08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-08 {
  width: 100%;
  min-height: 100svh;
}

.ttg-08 input[type="checkbox"] {
  -webkit-appearance: none;
}
```

## JavaScript
```js
(() => {
  // Haptic tick: an 8ms vibration pulse per toggle, on hardware that supports it.
  // Everything visual is Tailwind — delete this file and the keys still latch.
  const board = document.querySelector('#ttg-08-board');
  if (!board) return;
  board.addEventListener('change', () => { navigator.vibrate?.(8); });
})();
```
