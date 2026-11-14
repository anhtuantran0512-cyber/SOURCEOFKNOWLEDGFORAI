---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-retro-led-pixel-button-group/"
title: "Tailwind Retro LED Pixel Button Group (Dot-Matrix Display Buttons)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A hardware-style transport panel: three keys drawn as dot-matrix LED displays that light up green, amber or red when selected."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Retro LED Pixel Button Group (Dot-Matrix Display Buttons)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-retro-led-pixel-button-group/

A hardware-style transport panel: three keys drawn as dot-matrix LED displays that light up green, amber or red when selected. The dot grid is a tiled radial-gradient on before: (before:bg-size-[7px_7px]), scanlines sit on after:, and each key swaps one variable &mdash; has-checked:[--led:#3dff6e] &mdash; to re-colour dots, text and glow at once. Labels are set in Doto, a true dot-matrix face, and a status line reports the current mode.
## HTML
```html
<section class="tbg-17 w-full min-h-svh grid place-items-center bg-tbg17-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg17-glow),transparent_70%)] px-5 py-14 font-tbg17-mono text-tbg17-ink" aria-label="Retro LED pixel button group demo">
  <div class="group/panel w-full max-w-[33rem] rounded-[1.25rem] border border-tbg17-line bg-linear-to-b from-tbg17-panel to-tbg17-panel2 p-6 shadow-tbg17-panel">
    <div class="mb-4 flex items-center justify-between">
      <p id="tbg17-label" class="text-[11px] font-semibold uppercase tracking-[0.24em] text-tbg17-mut">Transport</p>
      <p class="text-[11px] tracking-[0.12em] text-tbg17-mut">SYS ▸ <span class="hidden text-tbg17-go group-has-[#tbg17-run:checked]/panel:inline">RUNNING</span><span class="hidden text-tbg17-wait group-has-[#tbg17-wait:checked]/panel:inline">ON HOLD</span><span class="hidden text-tbg17-stop group-has-[#tbg17-stop:checked]/panel:inline">HALTED</span></p>
    </div>
    <div role="radiogroup" aria-labelledby="tbg17-label" class="grid grid-cols-3 gap-3">
      <label class="relative isolate grid min-h-22 cursor-pointer place-items-center overflow-hidden rounded-xl border-[1.5px] border-tbg17-key-line bg-tbg17-key shadow-[inset_0_2px_6px_rgb(0_0_0/0.7)] [--led:rgb(120_120_120/0.22)] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(circle,var(--led)_30%,transparent_34%)] before:bg-size-[7px_7px] before:transition-[filter] before:duration-250 before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(0deg,rgb(255_255_255/0.04)_0_1px,transparent_1px_3px)] after:content-[''] hover:border-tbg17-hover has-checked:border-tbg17-go-d has-checked:[--led:var(--color-tbg17-go)] has-checked:shadow-[inset_0_2px_6px_rgb(0_0_0/0.7),0_0_22px_-6px_var(--led)] has-checked:before:drop-shadow-[0_0_5px_var(--led)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-white"><input type="radio" name="tbg17" id="tbg17-run" class="sr-only" checked><span class="font-tbg17-dot text-[26px] font-black tracking-[0.08em] text-(--led) transition-[color,text-shadow] duration-250 group-has-[#tbg17-run:checked]/panel:text-white group-has-[#tbg17-run:checked]/panel:[text-shadow:0_0_8px_var(--color-tbg17-go),0_0_16px_var(--color-tbg17-go)]">RUN</span></label>
      <label class="relative isolate grid min-h-22 cursor-pointer place-items-center overflow-hidden rounded-xl border-[1.5px] border-tbg17-key-line bg-tbg17-key shadow-[inset_0_2px_6px_rgb(0_0_0/0.7)] [--led:rgb(120_120_120/0.22)] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(circle,var(--led)_30%,transparent_34%)] before:bg-size-[7px_7px] before:transition-[filter] before:duration-250 before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(0deg,rgb(255_255_255/0.04)_0_1px,transparent_1px_3px)] after:content-[''] hover:border-tbg17-hover has-checked:border-tbg17-wait-d has-checked:[--led:var(--color-tbg17-wait)] has-checked:shadow-[inset_0_2px_6px_rgb(0_0_0/0.7),0_0_22px_-6px_var(--led)] has-checked:before:drop-shadow-[0_0_5px_var(--led)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-white"><input type="radio" name="tbg17" id="tbg17-wait" class="sr-only"><span class="font-tbg17-dot text-[26px] font-black tracking-[0.08em] text-(--led) transition-[color,text-shadow] duration-250 group-has-[#tbg17-wait:checked]/panel:text-white group-has-[#tbg17-wait:checked]/panel:[text-shadow:0_0_8px_var(--color-tbg17-wait),0_0_16px_var(--color-tbg17-wait)]">WAIT</span></label>
      <label class="relative isolate grid min-h-22 cursor-pointer place-items-center overflow-hidden rounded-xl border-[1.5px] border-tbg17-key-line bg-tbg17-key shadow-[inset_0_2px_6px_rgb(0_0_0/0.7)] [--led:rgb(120_120_120/0.22)] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(circle,var(--led)_30%,transparent_34%)] before:bg-size-[7px_7px] before:transition-[filter] before:duration-250 before:content-[''] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(0deg,rgb(255_255_255/0.04)_0_1px,transparent_1px_3px)] after:content-[''] hover:border-tbg17-hover has-checked:border-tbg17-stop-d has-checked:[--led:var(--color-tbg17-stop)] has-checked:shadow-[inset_0_2px_6px_rgb(0_0_0/0.7),0_0_22px_-6px_var(--led)] has-checked:before:drop-shadow-[0_0_5px_var(--led)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-white"><input type="radio" name="tbg17" id="tbg17-stop" class="sr-only"><span class="font-tbg17-dot text-[26px] font-black tracking-[0.08em] text-(--led) transition-[color,text-shadow] duration-250 group-has-[#tbg17-stop:checked]/panel:text-white group-has-[#tbg17-stop:checked]/panel:[text-shadow:0_0_8px_var(--color-tbg17-stop),0_0_16px_var(--color-tbg17-stop)]">STOP</span></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg17-bg: #050505;
  --color-tbg17-glow: #181818;
  --color-tbg17-panel: #1c1c1c;
  --color-tbg17-panel2: #0e0e0e;
  --color-tbg17-line: #2c2c2c;
  --color-tbg17-key: #0a0a0a;
  --color-tbg17-key-line: #262626;
  --color-tbg17-hover: #3a3a3a;
  --color-tbg17-ink: #e8e8e8;
  --color-tbg17-mut: #8f8f8f;
  --color-tbg17-go: #3dff6e;
  --color-tbg17-go-d: #1c7a3a;
  --color-tbg17-wait: #ffb000;
  --color-tbg17-wait-d: #8a6000;
  --color-tbg17-stop: #ff4242;
  --color-tbg17-stop-d: #8a2020;
  --shadow-tbg17-panel: inset 0 2px 10px rgb(0 0 0 / 0.8), 0 30px 70px -40px #000;
  --font-tbg17-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --font-tbg17-dot: 'Doto', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-17 {
  width: 100%;
  min-height: 100svh;
}
```
