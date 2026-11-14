---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-material-design-3-switch-state-layer/"
title: "Tailwind Material Design 3 Switch with State Layer"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A spec-faithful Material 3 switch in utilities: a 52&times;32 outlined track, a thumb that grows 16 &rarr; 24 &rarr; 28dp as it slides and presses, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design 3 Switch with State Layer
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-material-design-3-switch-state-layer/

A spec-faithful Material 3 switch in utilities: a 52&times;32 outlined track, a thumb that grows 16 &rarr; 24 &rarr; 28dp as it slides and presses, a checkmark that fades in on the handle, and the M3 state-layer halo blooming on hover and focus.
## HTML
```html
<section class="ttg-14 w-full min-h-svh flex flex-col items-center justify-center gap-6 px-5 py-14 bg-ttg14-bg font-ttg14-sans" aria-label="Material Design 3 switch">
  <label for="ttg-14-sw" class="flex items-center gap-8 w-[min(380px,100%)] px-6 py-4 rounded-2xl bg-ttg14-surface border border-ttg14-edge cursor-pointer transition-colors duration-200 hover:bg-ttg14-tint">
    <span class="flex-1 flex flex-col gap-0.5">
      <b class="text-[15px] font-medium text-ttg14-ink">Sync over Wi-Fi only</b>
      <small class="text-[12.5px] text-ttg14-mute">Pause large uploads on mobile data</small>
    </span>
    <input type="checkbox" id="ttg-14-sw" role="switch" checked class="appearance-none shrink-0 w-13 h-8 rounded-2xl relative cursor-pointer bg-ttg14-trackoff border-2 border-ttg14-outline transition-[background-color,border-color] duration-250 checked:bg-ttg14-primary checked:border-ttg14-primary before:content-[''] before:absolute before:top-0 before:left-0 before:w-7 before:h-7 before:rounded-full before:bg-ttg14-outline before:scale-[0.5715] before:transition-[transform,background-color,box-shadow] before:duration-250 before:ease-[cubic-bezier(0.2,0,0,1)] checked:before:bg-white checked:before:translate-x-5 checked:before:scale-[0.857] hover:before:shadow-[0_0_0_10px_--alpha(var(--color-ttg14-primary)/8%)] focus-visible:before:shadow-[0_0_0_10px_--alpha(var(--color-ttg14-primary)/12%)] active:before:scale-100 checked:active:before:translate-x-5 checked:active:before:scale-100 after:content-[''] after:absolute after:top-1.5 after:left-1.5 after:w-4 after:h-4 after:bg-ttg14-primary after:opacity-0 after:translate-x-5 after:scale-50 after:transition-[opacity,transform] after:duration-250 after:ease-[cubic-bezier(0.2,0,0,1)] after:[mask:url(data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2016%2016'%3E%3Cpath%20fill='none'%20stroke='black'%20stroke-width='2.4'%20stroke-linecap='round'%20stroke-linejoin='round'%20d='M3%208.5l3.2%203.2L13%205'/%3E%3C/svg%3E)_center/contain_no-repeat] checked:after:opacity-100 checked:after:scale-100 focus-visible:outline-3 focus-visible:outline-ttg14-primary focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none motion-reduce:after:transition-none">
  </label>
  <p class="text-[12px] tracking-[0.1em] uppercase text-ttg14-mute">M3 spec &middot; growing thumb + state layer</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg14-bg: #fdf7ff;
  --color-ttg14-bg: oklch(0.98 0.012 310);
  --color-ttg14-surface: #ffffff;
  --color-ttg14-surface: oklch(1 0 0);
  --color-ttg14-tint: #f9f2fc;
  --color-ttg14-tint: oklch(0.97 0.014 310);
  --color-ttg14-edge: #e7e0ec;
  --color-ttg14-edge: oklch(0.91 0.012 310);
  --color-ttg14-primary: #6750a4;
  --color-ttg14-primary: oklch(0.47 0.13 296);
  --color-ttg14-outline: #6f6779;
  --color-ttg14-outline: oklch(0.52 0.02 300);
  --color-ttg14-trackoff: #e6e0e9;
  --color-ttg14-trackoff: oklch(0.91 0.01 310);
  --color-ttg14-ink: #1d1b20;
  --color-ttg14-ink: oklch(0.23 0.008 300);
  --color-ttg14-mute: #6b6572;
  --color-ttg14-mute: oklch(0.51 0.018 300);
  --font-ttg14-sans: Roboto, 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-14 {
  width: 100%;
  min-height: 100svh;
}

.ttg-14 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* Safari still needs the prefixed mask on the checkmark pseudo-element. */

.ttg-14 input[type="checkbox"]::after {
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='none' stroke='black' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round' d='M3 8.5l3.2 3.2L13 5'/%3E%3C/svg%3E") center/contain no-repeat;
}
```
