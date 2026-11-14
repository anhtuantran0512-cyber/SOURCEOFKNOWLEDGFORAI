---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/neon-glow-checkbox-tailwind-dark-mode/"
title: "Neon Glow Checkbox in Tailwind CSS — Dark Mode Gaming UI"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A cyan glow that breathes around every checked box: a layered shadow-tcb08-glow token on a before: pseudo-element, pulsed with animate-tcb08-pulse — opacity…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Checkbox in Tailwind CSS — Dark Mode Gaming UI
Source: https://codefronts.com/components/tailwind-css-checkboxes/neon-glow-checkbox-tailwind-dark-mode/

A cyan glow that breathes around every checked box: a layered shadow-tcb08-glow token on a before: pseudo-element, pulsed with animate-tcb08-pulse — opacity only, so the glow never repaints the layout. Checked labels brighten to full white.
## HTML
```html
<section class="tcb-08 w-full min-h-svh grid place-items-center bg-tcb08-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tcb08-glowbg),transparent_70%)] px-5 py-14 font-tcb08-sans text-tcb08-ink selection:bg-tcb08-neon selection:text-tcb08-bg" aria-label="Neon glow checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-white/10 bg-white/[0.03] p-3.5">
    <p class="px-3.5 pb-2 pt-1 text-[11px] font-bold uppercase tracking-[0.2em] text-tcb08-neon">Performance</p>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3.5 transition-colors hover:bg-white/[0.04]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb08-line bg-white/[0.02] text-tcb08-neon transition-colors duration-300 peer-checked:border-tcb08-neon peer-checked:bg-tcb08-neon/10 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb08-neon before:pointer-events-none before:absolute before:-inset-px before:rounded-[7px] before:opacity-0 before:shadow-tcb08-glow before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb08-pulse group-has-checked:before:opacity-100 motion-reduce:transition-none motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] tracking-[0.01em] transition-colors group-has-checked:text-white">Enable RGB sync</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3.5 transition-colors hover:bg-white/[0.04]"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb08-line bg-white/[0.02] text-tcb08-neon transition-colors duration-300 peer-checked:border-tcb08-neon peer-checked:bg-tcb08-neon/10 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb08-neon before:pointer-events-none before:absolute before:-inset-px before:rounded-[7px] before:opacity-0 before:shadow-tcb08-glow before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb08-pulse group-has-checked:before:opacity-100 motion-reduce:transition-none motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] tracking-[0.01em] transition-colors group-has-checked:text-white">Overclock profile</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3.5 transition-colors hover:bg-white/[0.04]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb08-line bg-white/[0.02] text-tcb08-neon transition-colors duration-300 peer-checked:border-tcb08-neon peer-checked:bg-tcb08-neon/10 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb08-neon before:pointer-events-none before:absolute before:-inset-px before:rounded-[7px] before:opacity-0 before:shadow-tcb08-glow before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb08-pulse group-has-checked:before:opacity-100 motion-reduce:transition-none motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] tracking-[0.01em] transition-colors group-has-checked:text-white">Low-latency mode</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb08-bg: #0a0d11;
  --color-tcb08-bg: oklch(0.16 0.01 250);
  --color-tcb08-glowbg: #141b22;
  --color-tcb08-glowbg: oklch(0.22 0.015 245);
  --color-tcb08-ink: #b6c0ca;
  --color-tcb08-ink: oklch(0.8 0.02 245);
  --color-tcb08-line: #3a4652;
  --color-tcb08-line: oklch(0.4 0.025 245);
  --color-tcb08-neon: #00ffcc;
  --color-tcb08-neon: oklch(0.9 0.18 172);
  --font-tcb08-sans: 'Space Grotesk', system-ui, sans-serif;
  --shadow-tcb08-glow: 0 0 6px #00ffcc, 0 0 14px #00ffcc, 0 0 26px rgb(0 255 204 / 0.8), inset 0 0 8px rgb(0 255 204 / 0.5);
  --animate-tcb08-pulse: tcb08-pulse 2.4s ease-in-out infinite;

  @keyframes tcb08-pulse {
    0%,
        100% {
      opacity: 0.7;
    }

    50% {
      opacity: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-08 {
  width: 100%;
  min-height: 100svh;
}
```
