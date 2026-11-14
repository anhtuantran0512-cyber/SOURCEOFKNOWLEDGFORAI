---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/minimalist-tailwind-dark-mode-settings-panel/"
title: "Minimalist Tailwind Dark Mode Settings Panel"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "Maximum restraint: no borders, no shadows, no second accent — just surface separation, one hue and a lot of air."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Tailwind Dark Mode Settings Panel
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/minimalist-tailwind-dark-mode-settings-panel/

Maximum restraint: no borders, no shadows, no second accent — just surface separation, one hue and a lot of air. A preferences panel covering the four control types you actually ship (checkbox, switch, radio pair, select), all styled from three tokens. The Dark appearance switch is the page's theme control, and its knob follows the effective scheme, not just its checked state.
## HTML
```html
<div class="tdm-12 scheme-light-dark has-[#tdm-12-toggle:checked]:scheme-dark dark:has-[#tdm-12-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-tdm12-bg px-4 py-12 font-tdm12-sans text-tdm12-ink antialiased transition-colors duration-300">
  <section aria-labelledby="tdm-12-h" class="grid w-full max-w-[36rem] gap-6 rounded-[28px] bg-tdm12-panel p-5 sm:p-7">
    <header class="grid gap-1 px-1">
      <h1 id="tdm-12-h" class="text-xl font-semibold tracking-tight">Preferences</h1>
      <p class="text-sm text-tdm12-mut">Workspace defaults for Sam Rivera</p>
    </header>
    <div class="grid gap-1.5">
      <label class="group/ck flex min-h-16 cursor-pointer items-center justify-between gap-4 rounded-2xl bg-tdm12-row px-4 py-4 transition hover:bg-tdm12-row-hover has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm12-focus">
        <span class="grid gap-0.5"><span class="text-[15px] font-medium">Weekly digest</span><span class="text-[13px] text-tdm12-mut">One summary email each Monday at 09:00.</span></span>
        <input type="checkbox" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-lg bg-tdm12-field transition group-has-checked/ck:bg-tdm12-acc"><svg class="size-4 text-tdm12-acc-ink opacity-0 transition group-has-checked/ck:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>
      </label>
      <label class="group/sw flex min-h-16 cursor-pointer items-center justify-between gap-4 rounded-2xl bg-tdm12-row px-4 py-4 transition hover:bg-tdm12-row-hover has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm12-focus">
        <span class="grid gap-0.5"><span class="text-[15px] font-medium">Dark appearance</span><span class="text-[13px] text-tdm12-mut">Flips your system setting for this workspace.</span></span>
        <input type="checkbox" id="tdm-12-toggle" class="sr-only">
        <span aria-hidden="true" class="relative h-7 w-12 flex-none rounded-full bg-tdm12-track transition-colors duration-300"><span class="absolute top-1 left-1 grid size-5 place-items-center rounded-full bg-tdm12-knob shadow-[0_1px_3px_rgb(0_0_0/.3)] transition-transform duration-300 group-has-checked/sw:translate-x-5 dark:translate-x-5 dark:group-has-checked/sw:translate-x-0! motion-reduce:transition-none"><svg class="size-3 text-tdm12-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg></span></span>
      </label>
      <div role="group" aria-labelledby="tdm-12-view" class="flex min-h-16 flex-wrap items-center justify-between gap-4 rounded-2xl bg-tdm12-row px-4 py-4">
        <span class="grid gap-0.5"><span id="tdm-12-view" class="text-[15px] font-medium">Default view</span><span class="text-[13px] text-tdm12-mut">Where new sessions land.</span></span>
        <span class="flex gap-1 rounded-xl bg-tdm12-field p-1">
          <label class="flex min-h-10 cursor-pointer items-center gap-2 rounded-lg px-3.5 text-sm text-tdm12-mut transition hover:text-tdm12-ink has-checked:bg-tdm12-acc has-checked:text-tdm12-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm12-focus"><input type="radio" name="tdm-12-view" class="sr-only" checked><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg>Board</label>
          <label class="flex min-h-10 cursor-pointer items-center gap-2 rounded-lg px-3.5 text-sm text-tdm12-mut transition hover:text-tdm12-ink has-checked:bg-tdm12-acc has-checked:text-tdm12-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm12-focus"><input type="radio" name="tdm-12-view" class="sr-only"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5Z"/><path d="m3 13 9 5 9-5"/></svg>List</label>
        </span>
      </div>
      <label class="flex min-h-16 flex-wrap items-center justify-between gap-4 rounded-2xl bg-tdm12-row px-4 py-4">
        <span class="grid gap-0.5"><span class="text-[15px] font-medium">Time zone</span><span class="text-[13px] text-tdm12-mut">Used for schedules and digests.</span></span>
        <span class="relative">
          <select class="min-h-11 appearance-none rounded-xl bg-tdm12-field ps-3.5 pe-10 text-sm text-tdm12-ink transition hover:bg-tdm12-row-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm12-focus">
            <option>Europe/London</option><option selected>America/New_York</option><option>Asia/Singapore</option><option>Australia/Sydney</option>
          </select>
          <svg class="pointer-events-none absolute end-3 top-1/2 size-4 -translate-y-1/2 text-tdm12-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m7 15 5 5 5-5M7 9l5-5 5 5"/></svg>
        </span>
      </label>
    </div>
    <footer class="flex flex-wrap justify-end gap-2 px-1">
      <button type="button" class="min-h-11 rounded-xl px-4 text-sm font-medium text-tdm12-mut transition hover:bg-tdm12-row hover:text-tdm12-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm12-focus">Reset to defaults</button>
      <button type="button" class="min-h-11 rounded-xl bg-tdm12-acc px-5 text-sm font-semibold text-tdm12-acc-ink transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm12-focus">Save changes</button>
    </footer>
  </section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm12-bg: light-dark(#f4f3f7, #09090c);
  --color-tdm12-panel: light-dark(#ecebf1, #111114);
  --color-tdm12-row: light-dark(#ffffff, #17171c);
  --color-tdm12-row-hover: light-dark(#f8f7fb, #1e1e25);
  --color-tdm12-field: light-dark(#eeedf3, #0e0e12);
  --color-tdm12-ink: light-dark(#121117, #f0f0f2);
  --color-tdm12-mut: light-dark(#5d5b68, #96969f);
  --color-tdm12-acc: light-dark(#7e22ce, #c084fc);
  --color-tdm12-acc-ink: light-dark(#ffffff, #1c0a2e);
  --color-tdm12-focus: light-dark(#7e22ce, #d8b4fe);
  --color-tdm12-track: light-dark(rgb(18 17 23 / .16), #c084fc);
  --color-tdm12-knob: light-dark(#ffffff, #1c0a2e);
  --color-tdm12-moon: light-dark(transparent, #e9d5ff);
  --font-tdm12-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
