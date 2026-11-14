---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-toggle-switch-checkbox-segmented-control-clay/"
title: "Tailwind Toggle Switch, Checkbox & Segmented Control (Clay Style)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "A complete clay form-control set: a switch whose track is an inset well and whose knob is a puffy pebble, checkboxes with a drawn-on tick (after:rotate-45…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toggle Switch, Checkbox & Segmented Control (Clay Style)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-toggle-switch-checkbox-segmented-control-clay/

A complete clay form-control set: a switch whose track is an inset well and whose knob is a puffy pebble, checkboxes with a drawn-on tick (after:rotate-45 after:border-r-3 after:border-b-3), and a segmented radio group with a sliding clay thumb. Every control is a native input inside its own <label>, so has-checked: replaces sibling-selector plumbing. New: switches carry role="switch" and a check glyph in the knob.
## HTML
```html
<section class="tcl-10 w-full min-h-svh grid place-items-center bg-tcl10-bg px-5 py-14 font-tcl10-sans text-tcl10-ink" aria-label="Clay toggle switch and checkbox set demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="grid w-full max-w-[560px] gap-[clamp(20px,3vw,28px)] rounded-[42px] bg-tcl10-panel p-[clamp(22px,3.4vw,36px)] shadow-tcl10-panel">
      <h2 class="font-tcl10-display text-[clamp(24px,3.2vw,30px)] font-extrabold tracking-[-0.03em]">Preferences</h2>
      <ul class="grid gap-3">
        <li>
          <label class="group flex cursor-pointer items-center justify-between gap-4.5 rounded-[26px] bg-tcl10-well px-4.5 py-4 shadow-tcl10-row">
            <span class="grid gap-0.5"><b class="text-[14.5px] font-semibold">Daily practice reminder</b><span class="text-[12.5px] text-tcl10-mut">A nudge at 8:00, your time</span></span>
            <input type="checkbox" role="switch" class="sr-only" checked>
            <span aria-hidden="true" class="relative block h-9 w-[62px] flex-none rounded-full bg-tcl10-track shadow-tcl10-track transition-colors duration-300 group-has-checked:bg-tcl10-on group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-tcl10-ink">
              <span class="absolute top-1 left-1 grid size-7 place-items-center rounded-full bg-tcl10-knob text-tcl10-accent shadow-tcl10-knob transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked:translate-x-6.5 group-has-checked:scale-105 motion-reduce:transition-none"><svg class="size-3.5 scale-0 opacity-0 transition-[scale,opacity] duration-300 group-has-checked:scale-100 group-has-checked:opacity-100" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg></span>
            </span>
          </label>
        </li>
        <li>
          <label class="group flex cursor-pointer items-center justify-between gap-4.5 rounded-[26px] bg-tcl10-well px-4.5 py-4 shadow-tcl10-row">
            <span class="grid gap-0.5"><b class="text-[14.5px] font-semibold">Sound effects</b><span class="text-[12.5px] text-tcl10-mut">Clicks, chimes and streak fanfare</span></span>
            <input type="checkbox" role="switch" class="sr-only">
            <span aria-hidden="true" class="relative block h-9 w-[62px] flex-none rounded-full bg-tcl10-track shadow-tcl10-track transition-colors duration-300 group-has-checked:bg-tcl10-on group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-tcl10-ink">
              <span class="absolute top-1 left-1 grid size-7 place-items-center rounded-full bg-tcl10-knob text-tcl10-accent shadow-tcl10-knob transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked:translate-x-6.5 group-has-checked:scale-105 motion-reduce:transition-none"><svg class="size-3.5 scale-0 opacity-0 transition-[scale,opacity] duration-300 group-has-checked:scale-100 group-has-checked:opacity-100" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg></span>
            </span>
          </label>
        </li>
      </ul>
      <fieldset class="grid gap-3 border-0">
        <legend class="pb-1 text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl10-mut">Weekly digest includes</legend>
        <div class="grid gap-2.5">
          <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-3xl bg-tcl10-panel px-4.5 text-[14.5px] font-semibold shadow-tcl10-chk transition-[translate,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.75 has-checked:bg-tcl10-accent/26"><input type="checkbox" class="sr-only" checked><span aria-hidden="true" class="relative size-7 flex-none rounded-[10px] bg-tcl10-box shadow-tcl10-box transition-[background-color,box-shadow] duration-300 after:absolute after:top-1/2 after:left-1/2 after:h-3.5 after:w-2 after:-translate-x-1/2 after:-translate-y-[62%] after:rotate-45 after:scale-0 after:rounded-[1.5px] after:border-r-3 after:border-b-3 after:border-white after:opacity-0 after:transition-[scale,opacity] after:duration-300 after:ease-[cubic-bezier(.34,1.6,.5,1)] group-hover:after:scale-70 group-hover:after:opacity-30 group-has-checked:bg-tcl10-accent group-has-checked:shadow-tcl10-boxon group-has-checked:after:scale-100 group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-tcl10-ink"></span>Progress summary</label>
          <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-3xl bg-tcl10-panel px-4.5 text-[14.5px] font-semibold shadow-tcl10-chk transition-[translate,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.75 has-checked:bg-tcl10-accent/26"><input type="checkbox" class="sr-only" checked><span aria-hidden="true" class="relative size-7 flex-none rounded-[10px] bg-tcl10-box shadow-tcl10-box transition-[background-color,box-shadow] duration-300 after:absolute after:top-1/2 after:left-1/2 after:h-3.5 after:w-2 after:-translate-x-1/2 after:-translate-y-[62%] after:rotate-45 after:scale-0 after:rounded-[1.5px] after:border-r-3 after:border-b-3 after:border-white after:opacity-0 after:transition-[scale,opacity] after:duration-300 after:ease-[cubic-bezier(.34,1.6,.5,1)] group-hover:after:scale-70 group-hover:after:opacity-30 group-has-checked:bg-tcl10-accent group-has-checked:shadow-tcl10-boxon group-has-checked:after:scale-100 group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-tcl10-ink"></span>New lessons</label>
          <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-3xl bg-tcl10-panel px-4.5 text-[14.5px] font-semibold shadow-tcl10-chk transition-[translate,background-color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:translate-x-0.75 has-checked:bg-tcl10-accent/26"><input type="checkbox" class="sr-only"><span aria-hidden="true" class="relative size-7 flex-none rounded-[10px] bg-tcl10-box shadow-tcl10-box transition-[background-color,box-shadow] duration-300 after:absolute after:top-1/2 after:left-1/2 after:h-3.5 after:w-2 after:-translate-x-1/2 after:-translate-y-[62%] after:rotate-45 after:scale-0 after:rounded-[1.5px] after:border-r-3 after:border-b-3 after:border-white after:opacity-0 after:transition-[scale,opacity] after:duration-300 after:ease-[cubic-bezier(.34,1.6,.5,1)] group-hover:after:scale-70 group-hover:after:opacity-30 group-has-checked:bg-tcl10-accent group-has-checked:shadow-tcl10-boxon group-has-checked:after:scale-100 group-has-checked:after:opacity-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-tcl10-ink"></span>Community picks</label>
        </div>
      </fieldset>
      <fieldset class="grid gap-3 border-0">
        <legend class="pb-1 text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl10-mut">Difficulty</legend>
        <div class="group/seg relative grid grid-cols-3 gap-1 rounded-[26px] bg-tcl10-well p-1.25 shadow-tcl10-track">
          <span aria-hidden="true" class="absolute top-1.25 left-1.25 h-[calc(100%-10px)] w-[calc((100%-18px)/3)] rounded-[22px] bg-tcl10-accent shadow-tcl10-thumb transition-[translate] duration-[340ms] ease-[cubic-bezier(.34,1.4,.5,1)] group-has-[#tcl-10-d2:checked]/seg:translate-x-[calc(100%+4px)] group-has-[#tcl-10-d3:checked]/seg:translate-x-[calc(200%+8px)] motion-reduce:transition-none"></span>
          <label class="relative grid min-h-12 cursor-pointer place-items-center rounded-[22px] text-sm font-semibold text-tcl10-mut transition-colors duration-300 hover:text-tcl10-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcl10-ink"><input class="sr-only" type="radio" name="tcl-10-diff" id="tcl-10-d1">Gentle</label>
          <label class="relative grid min-h-12 cursor-pointer place-items-center rounded-[22px] text-sm font-semibold text-tcl10-mut transition-colors duration-300 hover:text-tcl10-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcl10-ink"><input class="sr-only" type="radio" name="tcl-10-diff" id="tcl-10-d2" checked>Steady</label>
          <label class="relative grid min-h-12 cursor-pointer place-items-center rounded-[22px] text-sm font-semibold text-tcl10-mut transition-colors duration-300 hover:text-tcl10-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcl10-ink"><input class="sr-only" type="radio" name="tcl-10-diff" id="tcl-10-d3">Intense</label>
        </div>
      </fieldset>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl10-mono text-[11.5px] text-tcl10-mut">track = well · knob = object · has-checked: in the label · group-has-[…]/seg: thumb</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl10-bg: #e5eaff;
  --color-tcl10-bg: oklch(0.94 0.028 275);
  --color-tcl10-panel: #eef1fe;
  --color-tcl10-panel: oklch(0.96 0.018 275);
  --color-tcl10-well: #e1e5fb;
  --color-tcl10-well: oklch(0.925 0.03 278);
  --color-tcl10-track: #d2d6ef;
  --color-tcl10-track: oklch(0.88 0.035 278);
  --color-tcl10-on: #a494f6;
  --color-tcl10-on: oklch(0.72 0.14 290);
  --color-tcl10-knob: #fbfbff;
  --color-tcl10-knob: oklch(0.99 0.01 290);
  --color-tcl10-box: #ced3ec;
  --color-tcl10-box: oklch(0.87 0.035 278);
  --color-tcl10-accent: #816bd8;
  --color-tcl10-accent: oklch(0.6 0.16 290);
  --color-tcl10-shade: #6a6ea88c;
  --color-tcl10-shade: oklch(0.56 0.09 280 / 0.55);
  --color-tcl10-light: #fdfefff2;
  --color-tcl10-light: oklch(1 0.012 280 / 0.95);
  --color-tcl10-ink: #242641;
  --color-tcl10-ink: oklch(0.28 0.05 280);
  --color-tcl10-mut: #535671;
  --color-tcl10-mut: oklch(0.46 0.045 280);
  --font-tcl10-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl10-panel: 0 30px 60px -24px var(--color-tcl10-shade), inset 0 -16px 28px -16px var(--color-tcl10-shade), inset 0 18px 28px -12px var(--color-tcl10-light);
  --shadow-tcl10-row: inset 0 8px 16px -10px var(--color-tcl10-shade), inset 0 -6px 12px -10px var(--color-tcl10-light);
  --shadow-tcl10-track: inset 0 9px 16px -6px var(--color-tcl10-shade), inset 0 -6px 12px -8px var(--color-tcl10-light);
  --shadow-tcl10-knob: 0 8px 14px -6px var(--color-tcl10-shade), inset 0 -6px 10px -7px var(--color-tcl10-shade), inset 0 8px 10px -6px var(--color-tcl10-light);
  --shadow-tcl10-chk: 0 12px 20px -16px var(--color-tcl10-shade), inset 0 -8px 14px -12px var(--color-tcl10-shade), inset 0 10px 14px -9px var(--color-tcl10-light);
  --shadow-tcl10-box: 0 0 0 0 transparent, inset 0 8px 13px -5px var(--color-tcl10-shade), inset 0 -5px 10px -7px var(--color-tcl10-light);
  --shadow-tcl10-boxon: 0 8px 14px -8px var(--color-tcl10-shade), inset 0 -6px 10px -8px var(--color-tcl10-shade), inset 0 8px 10px -6px var(--color-tcl10-light);
  --shadow-tcl10-thumb: 0 10px 18px -8px var(--color-tcl10-shade), inset 0 -7px 12px -8px var(--color-tcl10-shade), inset 0 9px 12px -6px var(--color-tcl10-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-10 {
  width: 100%;
  min-height: 100svh;
}
```
