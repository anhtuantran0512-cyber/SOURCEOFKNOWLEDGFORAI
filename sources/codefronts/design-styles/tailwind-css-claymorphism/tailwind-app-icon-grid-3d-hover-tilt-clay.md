---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-app-icon-grid-3d-hover-tilt-clay/"
title: "Tailwind App Icon Grid with 3D Hover Tilt (Clay Tiles)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Nine clay app tiles on a squircle grid, each colour generated from one [--tcl17-h:28] hue, with a real 3D tilt (perspective-[900px] + hover:rotate-x-13) and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind App Icon Grid with 3D Hover Tilt (Clay Tiles)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-app-icon-grid-3d-hover-tilt-clay/

Nine clay app tiles on a squircle grid, each colour generated from one [--tcl17-h:28] hue, with a real 3D tilt (perspective-[900px] + hover:rotate-x-13) and a staggered pop-in whose delay is calc(var(--tcl17-i) * 60ms). New: an Edit mode switch makes the grid jiggle like a phone launcher — a second keyframe swapped in by group-has-checked:.
## HTML
```html
<section class="tcl-17 group/demo w-full min-h-svh grid place-items-center bg-tcl17-bg bg-[radial-gradient(85%_60%_at_50%_0%,var(--color-tcl17-glow),transparent_70%)] px-5 py-14 font-tcl17-sans text-tcl17-ink" aria-label="Clay icon tiles and app grid demo">
  <div class="grid w-full justify-items-center gap-[clamp(24px,4vw,38px)]">
    <header class="grid max-w-[56ch] justify-items-center gap-3 text-center">
      <h2 class="font-tcl17-display text-[clamp(28px,4.2vw,40px)] font-semibold leading-[1.05] tracking-[-0.01em] text-balance">Nine tiles, one hue variable</h2>
      <p class="text-[15px] leading-relaxed text-tcl17-mut text-pretty">Hover to tilt. Fill and both shadow colours are derived from each tile's <code class="font-tcl17-mono text-[13.5px]">--tcl17-h</code>, so nothing needs per-colour tuning.</p>
      <label class="mt-1 inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-white/70 py-1 pr-4.5 pl-1.5 text-[13.5px] font-semibold shadow-tcl17-chip has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl17-ink">
        <input type="checkbox" role="switch" id="tcl-17-edit" class="peer sr-only">
        <span aria-hidden="true" class="relative h-8 w-13 rounded-full bg-tcl17-track shadow-[inset_0_6px_10px_-5px_var(--color-tcl17-shade)] transition-colors peer-checked:bg-tcl17-ink after:absolute after:top-1 after:left-1 after:size-6 after:rounded-full after:bg-white after:shadow-[0_4px_8px_-3px_var(--color-tcl17-shade)] after:transition-[translate] after:duration-300 after:ease-[cubic-bezier(.34,1.5,.5,1)] peer-checked:after:translate-x-5"></span>
        Edit mode
      </label>
    </header>
    <ul class="grid grid-cols-[repeat(3,minmax(88px,132px))] gap-[clamp(14px,2.6vw,24px)] p-1.5 perspective-[900px]">
      <li class="grid [--tcl17-h:28] [--tcl17-i:0]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M4 11.2 12 4l8 7.2V20a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z" fill="currentColor"/></svg><span class="text-xs font-semibold">Home</span></button></li>
      <li class="grid [--tcl17-h:62] [--tcl17-i:1]"><button type="button" class="tcl17-tile relative" aria-describedby="tcl-17-badge">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 3.5 14.6 9l6 .9-4.3 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.4 9.9 9.4 9z" fill="currentColor"/></svg><span class="text-xs font-semibold">Streaks</span><b id="tcl-17-badge" class="absolute -top-1.5 -right-1.5 grid h-6.5 min-w-6.5 place-items-center rounded-full bg-tcl17-badge px-1.5 text-xs font-bold text-white tabular-nums shadow-[0_0_0_3px_var(--color-tcl17-bg),0_6px_10px_-4px_var(--color-tcl17-shade)]">3<span class="sr-only"> new</span></b></button></li>
      <li class="grid [--tcl17-h:145] [--tcl17-i:2]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M5 4h9l5 5v11a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm8 1.8V10h4.2z" fill="currentColor"/></svg><span class="text-xs font-semibold">Docs</span></button></li>
      <li class="grid [--tcl17-h:190] [--tcl17-i:3]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M4 5h16v11H4zm5 13h6v2H9z" fill="currentColor"/></svg><span class="text-xs font-semibold">Watch</span></button></li>
      <li class="grid [--tcl17-h:232] [--tcl17-i:4]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zm.9 4h-1.8v5.5l4.4 2.6.9-1.5-3.5-2z" fill="currentColor"/></svg><span class="text-xs font-semibold">Focus</span></button></li>
      <li class="grid [--tcl17-h:280] [--tcl17-i:5]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 20.3 10.6 19C6 14.9 3.5 12.6 3.5 9.6A4.1 4.1 0 0 1 7.6 5.5c1.5 0 2.9.7 3.8 1.9.9-1.2 2.3-1.9 3.8-1.9a4.1 4.1 0 0 1 4.1 4.1c0 3-2.5 5.3-7.1 9.4z" fill="currentColor"/></svg><span class="text-xs font-semibold">Saved</span></button></li>
      <li class="grid [--tcl17-h:318] [--tcl17-i:6]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm0 2c-4 0-7 2.2-7 5v1h14v-1c0-2.8-3-5-7-5z" fill="currentColor"/></svg><span class="text-xs font-semibold">People</span></button></li>
      <li class="grid [--tcl17-h:352] [--tcl17-i:7]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M11 3h2l.4 2.3 2 .8 1.9-1.3 1.4 1.4-1.3 1.9.8 2L20.7 11v2l-2.3.4-.8 2 1.3 1.9-1.4 1.4-1.9-1.3-2 .8L13 20.7h-2l-.4-2.3-2-.8-1.9 1.3-1.4-1.4 1.3-1.9-.8-2L3.3 13v-2l2.3-.4.8-2L5.1 6.7l1.4-1.4 1.9 1.3 2-.8zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" fill="currentColor"/></svg><span class="text-xs font-semibold">Settings</span></button></li>
      <li class="grid [--tcl17-h:12] [--tcl17-i:8]"><button type="button" class="tcl17-tile">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M11 4h2v7h7v2h-7v7h-2v-7H4v-2h7z" fill="currentColor"/></svg><span class="text-xs font-semibold">Add</span></button></li>
    </ul>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-4 py-2 text-center font-tcl17-mono text-[11.5px] text-tcl17-mut">oklch hue rotation · perspective-[900px] hover:rotate-x-13 · delay = --tcl17-i × 60ms</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl17-bg: #e2edf8;
  --color-tcl17-bg: oklch(0.94 0.02 250);
  --color-tcl17-glow: #effaff;
  --color-tcl17-glow: oklch(0.98 0.02 250);
  --color-tcl17-track: #c3d3e4;
  --color-tcl17-track: oklch(0.86 0.03 250);
  --color-tcl17-badge: #cc272e;
  --color-tcl17-badge: oklch(0.55 0.2 25);
  --color-tcl17-ink: #142537;
  --color-tcl17-ink: oklch(0.26 0.04 250);
  --color-tcl17-mut: #475768;
  --color-tcl17-mut: oklch(0.45 0.035 250);
  --color-tcl17-shade: #57759466;
  --color-tcl17-shade: oklch(0.55 0.06 250 / 0.4);
  --font-tcl17-display: 'Fredoka', system-ui, sans-serif;
  --font-tcl17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl17-chip: inset 0 -4px 10px -8px var(--color-tcl17-shade), inset 0 6px 10px -6px white, 0 10px 18px -12px var(--color-tcl17-shade);
  --animate-tcl17-pop: tcl17-pop 0.55s cubic-bezier(0.34, 1.5, 0.5, 1) backwards;
  --animate-tcl17-wiggle: tcl17-wiggle 0.32s ease-in-out infinite alternate;

  @keyframes tcl17-pop {
    from {
      opacity: 0;
      scale: 0.7;
      translate: 0 16px;
    }

    to {
      opacity: 1;
      scale: 1;
      translate: 0 0;
    }
  }

  @keyframes tcl17-wiggle {
    from {
      rotate: calc(var(--tcl17-dir, 1) * -2.4deg);
    }

    to {
      rotate: calc(var(--tcl17-dir, 1) * 2.4deg);
    }
  }
}
/* Hue-driven clay tile: set [--tcl17-h:<hue>] and [--tcl17-i:<index>] on the parent. */

@utility tcl17-tile {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 9px;
  aspect-ratio: 1;
  padding: 10px;
  border-radius: 34px;
  cursor: pointer;
  color: oklch(0.28 0.08 var(--tcl17-h));
  background: oklch(0.85 0.1 var(--tcl17-h));
  transform-style: preserve-3d;
  box-shadow: 0 18px 30px -10px oklch(0.52 0.13 var(--tcl17-h) / 0.5), inset 0 -13px 20px -9px oklch(0.52 0.13 var(--tcl17-h) / 0.55), inset 0 15px 20px -7px oklch(1 0.02 var(--tcl17-h) / 0.95);
  animation: var(--animate-tcl17-pop);
  animation-delay: calc(var(--tcl17-i) * 60ms);
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.3, 1.1), translate 0.4s cubic-bezier(0.34, 1.35, 0.5, 1), scale 0.4s cubic-bezier(0.34, 1.35, 0.5, 1), box-shadow 0.4s;

  &:hover {
    transform: rotateX(13deg);
    translate: 0 -7px;
    scale: 1.05;
    box-shadow: 0 30px 44px -12px oklch(0.52 0.13 var(--tcl17-h) / 0.55), inset 0 -13px 20px -9px oklch(0.52 0.13 var(--tcl17-h) / 0.55), inset 0 17px 22px -7px oklch(1 0.02 var(--tcl17-h) / 0.98);
  }

  &:active {
    transform: rotateX(0deg);
    translate: 0 2px;
    scale: 0.95;
    box-shadow: 0 0 0 0 transparent, inset 0 14px 22px -8px oklch(0.52 0.13 var(--tcl17-h) / 0.6), inset 0 -10px 18px -10px oklch(1 0.02 var(--tcl17-h) / 0.8);
  }

  &:focus-visible {
    outline: 3px solid oklch(0.32 0.09 var(--tcl17-h));
    outline-offset: 4px;
  }

  li:nth-child(even) > & {
    --tcl17-dir: -1;
  }

  :where(.tcl-17:has(#tcl-17-edit:checked)) & {
    animation: var(--animate-tcl17-wiggle);
    animation-delay: calc(var(--tcl17-i) * -45ms);
  }

  @supports (corner-shape: squircle) {
    border-radius: 36%;
    corner-shape: squircle;
  }

  @media (prefers-reduced-motion: reduce) {
    animation: none;
    transition-duration: 0.01ms;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-17 {
  width: 100%;
  min-height: 100svh;
}
```
