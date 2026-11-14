---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-dark-mode-glowing-radio-button/"
title: "Tailwind Dark Mode Glowing Radio Button"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Radio rows designed for dark UI: the custom indicator ignites with a three-layer cyan glow that breathes on a slow loop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Glowing Radio Button
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-dark-mode-glowing-radio-button/

Radio rows designed for dark UI: the custom indicator ignites with a three-layer cyan glow that breathes on a slow loop. The glow is a --animate-trb04-breathe theme token whose keyframes live inside @theme, and the solid inner dot keeps the checked state readable without glow (WCAG 1.4.1).
## HTML
```html
<section class="trb-04 w-full min-h-svh grid place-items-center bg-trb04-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-trb04-top),transparent_70%)] px-6 py-14 font-trb04-sans text-trb04-ink" aria-label="Dark mode glowing radio buttons demo">
  <fieldset class="w-full max-w-[26rem]">
    <legend class="text-2xl font-bold tracking-[-0.02em]">Terminal theme</legend>
    <div class="mt-5 grid gap-2.5">
      <label class="group relative grid min-h-14 cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-[13px] border border-white/9 bg-white/3 px-[18px] transition duration-250 hover:border-trb04-glow/40 has-checked:border-trb04-glow/65 has-checked:bg-trb04-glow/7 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb04-glow">
        <input type="radio" name="trb-04" value="midnight" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-5 place-items-center rounded-full border-2 border-trb04-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb04-glow after:transition-transform after:duration-300 after:ease-trb04-spring after:content-[''] group-has-checked:animate-trb04-breathe group-has-checked:border-trb04-glow group-has-checked:after:scale-100 motion-reduce:group-has-checked:animate-none motion-reduce:group-has-checked:shadow-trb04-still"></span>
        <span class="text-[15px] font-semibold">Midnight</span>
        <span class="flex items-center gap-2.5 font-trb04-mono text-xs text-trb04-mut"><span aria-hidden="true" class="flex -space-x-1 *:size-3 *:rounded-full *:ring-2 *:ring-trb04-bg"><i class="bg-black"></i><i class="bg-[#22e3ff]"></i><i class="bg-[#9dff7a]"></i></span>OLED black</span>
      </label>
      <label class="group relative grid min-h-14 cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-[13px] border border-white/9 bg-white/3 px-[18px] transition duration-250 hover:border-trb04-glow/40 has-checked:border-trb04-glow/65 has-checked:bg-trb04-glow/7 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb04-glow">
        <input type="radio" name="trb-04" value="dim" class="sr-only">
        <span aria-hidden="true" class="grid size-5 place-items-center rounded-full border-2 border-trb04-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb04-glow after:transition-transform after:duration-300 after:ease-trb04-spring after:content-[''] group-has-checked:animate-trb04-breathe group-has-checked:border-trb04-glow group-has-checked:after:scale-100 motion-reduce:group-has-checked:animate-none motion-reduce:group-has-checked:shadow-trb04-still"></span>
        <span class="text-[15px] font-semibold">Dim</span>
        <span class="flex items-center gap-2.5 font-trb04-mono text-xs text-trb04-mut"><span aria-hidden="true" class="flex -space-x-1 *:size-3 *:rounded-full *:ring-2 *:ring-trb04-bg"><i class="bg-[#2a3142]"></i><i class="bg-[#8ab4ff]"></i><i class="bg-[#f5c07a]"></i></span>Soft slate</span>
      </label>
      <label class="group relative grid min-h-14 cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-[13px] border border-white/9 bg-white/3 px-[18px] transition duration-250 hover:border-trb04-glow/40 has-checked:border-trb04-glow/65 has-checked:bg-trb04-glow/7 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb04-glow">
        <input type="radio" name="trb-04" value="auto" class="sr-only">
        <span aria-hidden="true" class="grid size-5 place-items-center rounded-full border-2 border-trb04-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb04-glow after:transition-transform after:duration-300 after:ease-trb04-spring after:content-[''] group-has-checked:animate-trb04-breathe group-has-checked:border-trb04-glow group-has-checked:after:scale-100 motion-reduce:group-has-checked:animate-none motion-reduce:group-has-checked:shadow-trb04-still"></span>
        <span class="text-[15px] font-semibold">Sync with system</span>
        <span class="flex items-center gap-2.5 font-trb04-mono text-xs text-trb04-mut"><span aria-hidden="true" class="flex -space-x-1 *:size-3 *:rounded-full *:ring-2 *:ring-trb04-bg"><i class="bg-black"></i><i class="bg-white"></i></span>Auto</span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb04-bg: #07090f;
  --color-trb04-bg: oklch(0.14 0.01 265);
  --color-trb04-top: #141b2e;
  --color-trb04-top: oklch(0.22 0.035 265);
  --color-trb04-ink: #e3e8f4;
  --color-trb04-ink: oklch(0.93 0.015 265);
  --color-trb04-mut: #939cb5;
  --color-trb04-mut: oklch(0.7 0.03 265);
  --color-trb04-ring: #5a6482;
  --color-trb04-ring: oklch(0.5 0.04 265);
  --color-trb04-glow: #3fd3ec;
  --color-trb04-glow: oklch(0.8 0.13 205);
  --shadow-trb04-still: 0 0 6px oklch(0.8 0.13 205), 0 0 18px oklch(0.8 0.13 205 / 0.55);
  --ease-trb04-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-trb04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-trb04-breathe: trb04-breathe 2.6s ease-in-out infinite;

  @keyframes trb04-breathe {
    0%,
        100% {
      box-shadow: 0 0 4px oklch(0.8 0.13 205), 0 0 14px oklch(0.8 0.13 205 / 0.55), 0 0 34px oklch(0.8 0.13 205 / 0.3);
    }

    50% {
      box-shadow: 0 0 6px oklch(0.8 0.13 205), 0 0 22px oklch(0.8 0.13 205 / 0.65), 0 0 48px oklch(0.8 0.13 205 / 0.4);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-04 {
  width: 100%;
  min-height: 100svh;
}
```
