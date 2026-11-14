---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pulsing-glow-radio-button-status-picker/"
title: "Tailwind Pulsing Glow Radio Button (Status Picker)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A calm signal: the checked radio emits soft glow rings that swell outward and dissolve like a sonar ping, one ring then another on a slow four-second cycle."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pulsing Glow Radio Button (Status Picker)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pulsing-glow-radio-button-status-picker/

A calm signal: the checked radio emits soft glow rings that swell outward and dissolve like a sonar ping, one ring then another on a slow four-second cycle. Each option's colour is one arbitrary property, [--c:oklch(…)]; the second ring is offset with [animation-delay:2s]; and a live presence preview at the top shows how you'll appear.
## HTML
```html
<section class="trb-24 w-full min-h-svh grid place-items-center bg-trb24-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-trb24-top),transparent_70%)] px-6 py-14 font-trb24-sans text-trb24-ink" aria-label="Outer glow pulse radio buttons demo">
  <fieldset class="group/status w-full max-w-[24rem]">
    <legend class="text-2xl font-bold tracking-[-0.02em]">Set your status</legend>
    <div aria-hidden="true" class="mt-4 flex items-center gap-3.5 rounded-2xl border border-white/8 bg-white/4 p-3.5">
      <span class="relative size-11 flex-none rounded-full bg-linear-to-br from-trb24-av1 to-trb24-av2"><span class="absolute -right-0.5 -bottom-0.5 size-3.5 rounded-full bg-trb24-online ring-3 ring-trb24-bg transition-colors duration-300 group-has-[[value=away]:checked]/status:bg-trb24-away group-has-[[value=busy]:checked]/status:bg-trb24-busy"></span></span>
      <span class="grid"><span class="text-[15px] font-semibold">Jordan Lee</span><span class="text-[13px] text-trb24-mut">You appear as <span class="font-semibold text-trb24-ink group-has-[[value=away]:checked]/status:hidden group-has-[[value=busy]:checked]/status:hidden">Online</span><span class="hidden font-semibold text-trb24-ink group-has-[[value=away]:checked]/status:inline">Away</span><span class="hidden font-semibold text-trb24-ink group-has-[[value=busy]:checked]/status:inline">Do not disturb</span></span></span>
    </div>
    <div class="mt-5 grid gap-2.5">
      <label class="group relative flex min-h-[3.75rem] cursor-pointer items-center gap-4 rounded-2xl border border-white/8 bg-white/3 px-[18px] transition-colors duration-250 [--c:var(--color-trb24-online)] hover:border-(--c)/45 has-checked:border-(--c)/60 has-checked:bg-(--c)/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c)">
        <input type="radio" name="trb-24" value="online" class="sr-only" checked>
        <span aria-hidden="true" class="relative grid size-[22px] flex-none place-items-center"><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping motion-reduce:group-has-checked:animate-none"></span><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping [animation-delay:2s] motion-reduce:group-has-checked:animate-none"></span><span class="relative size-3.5 rounded-full border-[2.5px] border-trb24-ring transition-[border-color,background-color,box-shadow] duration-250 group-has-checked:border-(--c) group-has-checked:bg-(--c) group-has-checked:shadow-[0_0_8px_var(--c)]"></span></span>
        <span class="grid"><span class="text-[15px] font-semibold">Online</span><span class="text-[13px] text-trb24-mut">Visible to everyone</span></span>
      </label>
      <label class="group relative flex min-h-[3.75rem] cursor-pointer items-center gap-4 rounded-2xl border border-white/8 bg-white/3 px-[18px] transition-colors duration-250 [--c:var(--color-trb24-away)] hover:border-(--c)/45 has-checked:border-(--c)/60 has-checked:bg-(--c)/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c)">
        <input type="radio" name="trb-24" value="away" class="sr-only">
        <span aria-hidden="true" class="relative grid size-[22px] flex-none place-items-center"><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping motion-reduce:group-has-checked:animate-none"></span><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping [animation-delay:2s] motion-reduce:group-has-checked:animate-none"></span><span class="relative size-3.5 rounded-full border-[2.5px] border-trb24-ring transition-[border-color,background-color,box-shadow] duration-250 group-has-checked:border-(--c) group-has-checked:bg-(--c) group-has-checked:shadow-[0_0_8px_var(--c)]"></span></span>
        <span class="grid"><span class="text-[15px] font-semibold">Away</span><span class="text-[13px] text-trb24-mut">Back in a bit</span></span>
      </label>
      <label class="group relative flex min-h-[3.75rem] cursor-pointer items-center gap-4 rounded-2xl border border-white/8 bg-white/3 px-[18px] transition-colors duration-250 [--c:var(--color-trb24-busy)] hover:border-(--c)/45 has-checked:border-(--c)/60 has-checked:bg-(--c)/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-(--c)">
        <input type="radio" name="trb-24" value="busy" class="sr-only">
        <span aria-hidden="true" class="relative grid size-[22px] flex-none place-items-center"><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping motion-reduce:group-has-checked:animate-none"></span><span class="pointer-events-none absolute inset-0 rounded-full bg-(--c) opacity-0 group-has-checked:animate-trb24-ping [animation-delay:2s] motion-reduce:group-has-checked:animate-none"></span><span class="relative size-3.5 rounded-full border-[2.5px] border-trb24-ring transition-[border-color,background-color,box-shadow] duration-250 group-has-checked:border-(--c) group-has-checked:bg-(--c) group-has-checked:shadow-[0_0_8px_var(--c)]"></span></span>
        <span class="grid"><span class="text-[15px] font-semibold">Do not disturb</span><span class="text-[13px] text-trb24-mut">Mute all notifications</span></span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb24-bg: #0b0e16;
  --color-trb24-bg: oklch(0.16 0.015 265);
  --color-trb24-top: #182032;
  --color-trb24-top: oklch(0.24 0.035 265);
  --color-trb24-ink: #e3e7f3;
  --color-trb24-ink: oklch(0.93 0.015 265);
  --color-trb24-mut: #959db6;
  --color-trb24-mut: oklch(0.71 0.03 265);
  --color-trb24-ring: #56607d;
  --color-trb24-ring: oklch(0.49 0.04 265);
  --color-trb24-online: #3ecf7a;
  --color-trb24-online: oklch(0.75 0.17 150);
  --color-trb24-away: #f0bc3a;
  --color-trb24-away: oklch(0.82 0.15 85);
  --color-trb24-busy: #e5484d;
  --color-trb24-busy: oklch(0.63 0.2 25);
  --color-trb24-av1: #7c5cff;
  --color-trb24-av1: oklch(0.6 0.22 285);
  --color-trb24-av2: #ff7a9c;
  --color-trb24-av2: oklch(0.73 0.16 5);
  --font-trb24-sans: 'Geist', system-ui, sans-serif;
  --animate-trb24-ping: trb24-ping 4s cubic-bezier(0.2, 0.6, 0.4, 1) infinite;

  @keyframes trb24-ping {
    0% {
      scale: 1;
      opacity: 0.45;
    }

    70%,
        100% {
      scale: 2.4;
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-24 {
  width: 100%;
  min-height: 100svh;
}
```
