---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/pure-tailwind-css-radial-menu-with-sin-and-cos-no-javascript/"
title: "Pure Tailwind CSS Radial Menu with sin() and cos() (No JavaScript)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The reference implementation for radial maths in Tailwind v4, with zero JavaScript: a visually hidden checkbox holds the open state, group-has-checked/hub:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Radial Menu with sin() and cos() (No JavaScript)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/pure-tailwind-css-radial-menu-with-sin-and-cos-no-javascript/

The reference implementation for radial maths in Tailwind v4, with zero JavaScript: a visually hidden checkbox holds the open state, group-has-checked/hub: reads it, and six links bloom onto a perfect ring because one custom property &mdash; [--r:0rem] &rarr; group-has-checked/hub:[--r:7.5rem] &mdash; feeds a cos()/sin() utility. A hamburger morphs to a cross, a dashed orbit fades in, and every link has a hover-and-focus label.
## HTML
```html
<section class="tcm-02 w-full min-h-svh grid place-items-center bg-tcm02-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm02-glow),transparent_72%)] px-5 py-14 font-tcm02-sans text-tcm02-ink antialiased" aria-label="Pure Tailwind CSS radial menu demo">
  <div class="grid w-full justify-items-center gap-10">
    <header class="grid max-w-[30rem] justify-items-center gap-2 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tcm02-acc/10 px-3 py-1 font-tcm02-mono text-[11px] font-medium tracking-[0.08em] text-tcm02-acc-ink uppercase ring-1 ring-tcm02-acc/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcm02-acc"></span>0 KB JavaScript</p>
      <h2 class="text-[clamp(1.6rem,4vw,2.1rem)] font-bold tracking-[-0.03em] text-balance">A radial menu drawn by <span class="bg-linear-to-r from-tcm02-acc-ink to-tcm02-acc2 bg-clip-text text-transparent">sin() and cos()</span></h2>
    </header>
    <nav class="group/hub relative grid size-[19rem] place-items-center [--n:6]" aria-label="Quick launcher">
      <span aria-hidden="true" class="absolute inset-[1.6rem] rounded-full border border-dashed border-tcm02-edge scale-50 opacity-0 transition-[scale,opacity] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute size-28 rounded-full bg-tcm02-acc/25 blur-2xl opacity-60 transition-opacity duration-500 group-has-checked/hub:opacity-100"></span>
      <input type="checkbox" id="tcm-02-toggle" class="peer sr-only" aria-label="Open quick launcher">
      <ul class="absolute inset-0">
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-home" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Home">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 11l8-7 8 7v9h-5v-6h-6v6H4z"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Home</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-search" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Search">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M11 5a6 6 0 1 0 0 12 6 6 0 0 0 0-12zM20 20l-4.5-4.5"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Search</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-analytics" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Analytics">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 20V10M12 20V4M19 20v-7"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Analytics</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-messages" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Messages">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5h16v11H9l-5 4z"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Messages</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-saved" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Saved">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 4h12v17l-6-4-6 4z"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Saved</span>
          </a>
        </li>
        <li class="pointer-events-none absolute inset-0 grid place-items-center [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)] [--r:0rem] group-has-checked/hub:[--r:7.5rem]">
          <a href="#tcm-02-settings" class="group/l tcm02-polar pointer-events-auto relative grid size-13 place-items-center rounded-full bg-tcm02-chip text-tcm02-chip-ink ring-1 ring-tcm02-edge backdrop-blur-md invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-has-checked/hub:visible group-has-checked/hub:scale-100 group-has-checked/hub:opacity-100 group-has-checked/hub:delay-[calc(var(--i)*45ms)] hover:bg-linear-to-br hover:from-tcm02-acc hover:to-tcm02-acc2 hover:text-tcm02-on hover:shadow-tcm02-glow hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm02-ring motion-reduce:transition-none" aria-label="Settings">
            <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/></svg>
            <span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+0.4rem)] left-1/2 -translate-x-1/2 rounded-md bg-tcm02-tip px-2 py-1 text-[11px] font-semibold whitespace-nowrap text-tcm02-tip-ink opacity-0 transition-opacity duration-200 group-hover/l:opacity-100 group-focus-visible/l:opacity-100">Settings</span>
          </a>
        </li>
      </ul>
      <label for="tcm-02-toggle" aria-hidden="true" class="relative z-10 grid size-18 cursor-pointer place-items-center rounded-full bg-linear-to-br from-tcm02-acc to-tcm02-acc2 text-tcm02-on shadow-tcm02-hub transition-[rotate,scale,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-105 active:scale-95 group-has-checked/hub:rotate-90 group-has-focus-visible/hub:outline-2 group-has-focus-visible/hub:outline-offset-4 group-has-focus-visible/hub:outline-tcm02-ring motion-reduce:transition-none">
        <span class="relative block h-[2.5px] w-6 rounded-full bg-current transition-[rotate] duration-300 group-has-checked/hub:rotate-45 before:absolute before:inset-0 before:-translate-y-[7px] before:rounded-full before:bg-current before:transition-[translate,rotate] before:duration-300 group-has-checked/hub:before:translate-y-0 group-has-checked/hub:before:-rotate-90 after:absolute after:inset-0 after:translate-y-[7px] after:rounded-full after:bg-current after:transition-[translate,opacity] after:duration-300 group-has-checked/hub:after:translate-y-0 group-has-checked/hub:after:opacity-0"></span>
      </label>
    </nav>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm02-card px-3.5 py-2 text-center font-tcm02-mono text-[11.5px] text-tcm02-mut ring-1 ring-tcm02-line ">peer sr-only checkbox · group-has-checked/hub:[--r:7.5rem] · tcm02-polar</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm02-bg: #effaf6;
  --color-tcm02-bg: oklch(0.976 0.013 172.4);
  --color-tcm02-glow: #a7f3d0b3;
  --color-tcm02-glow: oklch(0.905 0.089 164.2 / 0.7);
  --color-tcm02-ink: #06302a;
  --color-tcm02-ink: oklch(0.279 0.046 181.1);
  --color-tcm02-mut: #3d625a;
  --color-tcm02-mut: oklch(0.466 0.045 179.1);
  --color-tcm02-card: #fbfffd;
  --color-tcm02-card: oklch(0.996 0.005 165);
  --color-tcm02-line: #cfeee3;
  --color-tcm02-line: oklch(0.924 0.036 172.1);
  --color-tcm02-chip: #ffffffcc;
  --color-tcm02-chip: oklch(1 0 0 / 0.8);
  --color-tcm02-chip-ink: #0f5a4c;
  --color-tcm02-chip-ink: oklch(0.421 0.073 176.5);
  --color-tcm02-edge: #0d948859;
  --color-tcm02-edge: oklch(0.6 0.104 184.7 / 0.35);
  --color-tcm02-acc: #0d9488;
  --color-tcm02-acc: oklch(0.6 0.104 184.7);
  --color-tcm02-acc2: #059669;
  --color-tcm02-acc2: oklch(0.596 0.127 163.2);
  --color-tcm02-acc-ink: #0f766e;
  --color-tcm02-acc-ink: oklch(0.511 0.086 186.4);
  --color-tcm02-on: #ffffff;
  --color-tcm02-on: oklch(1 0 0);
  --color-tcm02-tip: #06302a;
  --color-tcm02-tip: oklch(0.279 0.046 181.1);
  --color-tcm02-tip-ink: #ecfdf5;
  --color-tcm02-tip-ink: oklch(0.979 0.021 166.1);
  --color-tcm02-ring: #0f766e;
  --color-tcm02-ring: oklch(0.511 0.086 186.4);
  --font-tcm02-sans: 'Manrope', system-ui, sans-serif;
  --font-tcm02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm02-hub: 0 18px 40px -14px oklch(0.55 0.13 175 / 0.75), inset 0 1px 0 oklch(1 0 0 / 0.35);
  --shadow-tcm02-glow: 0 10px 24px -8px oklch(0.6 0.13 175 / 0.7);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-02 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm02-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: deep lagoon: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-02:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm02-bg: #04201c;
    --color-tcm02-bg: oklch(0.221 0.035 182.1);
    --color-tcm02-glow: #0d948859;
    --color-tcm02-glow: oklch(0.6 0.104 184.7 / 0.35);
    --color-tcm02-ink: #e6fbf4;
    --color-tcm02-ink: oklch(0.971 0.024 173.9);
    --color-tcm02-mut: #9ccdc0;
    --color-tcm02-mut: oklch(0.81 0.054 176.8);
    --color-tcm02-card: #08302a;
    --color-tcm02-card: oklch(0.28 0.045 180.8);
    --color-tcm02-line: #145247;
    --color-tcm02-line: oklch(0.397 0.064 178.3);
    --color-tcm02-chip: #ffffff14;
    --color-tcm02-chip: oklch(1 0 0 / 0.08);
    --color-tcm02-chip-ink: #c6f6e7;
    --color-tcm02-chip-ink: oklch(0.936 0.053 174.1);
    --color-tcm02-edge: #5eead44d;
    --color-tcm02-edge: oklch(0.855 0.125 181.1 / 0.3);
    --color-tcm02-acc: #14b8a6;
    --color-tcm02-acc: oklch(0.704 0.123 182.5);
    --color-tcm02-acc2: #10b981;
    --color-tcm02-acc2: oklch(0.696 0.149 162.5);
    --color-tcm02-acc-ink: #5eead4;
    --color-tcm02-acc-ink: oklch(0.855 0.125 181.1);
    --color-tcm02-on: #042f2b;
    --color-tcm02-on: oklch(0.276 0.046 185.6);
    --color-tcm02-tip: #ecfdf5;
    --color-tcm02-tip: oklch(0.979 0.021 166.1);
    --color-tcm02-tip-ink: #06302a;
    --color-tcm02-tip-ink: oklch(0.279 0.046 181.1);
    --color-tcm02-ring: #5eead4;
    --color-tcm02-ring: oklch(0.855 0.125 181.1);
  }
}

.tcm-02[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm02-bg: #04201c;
  --color-tcm02-bg: oklch(0.221 0.035 182.1);
  --color-tcm02-glow: #0d948859;
  --color-tcm02-glow: oklch(0.6 0.104 184.7 / 0.35);
  --color-tcm02-ink: #e6fbf4;
  --color-tcm02-ink: oklch(0.971 0.024 173.9);
  --color-tcm02-mut: #9ccdc0;
  --color-tcm02-mut: oklch(0.81 0.054 176.8);
  --color-tcm02-card: #08302a;
  --color-tcm02-card: oklch(0.28 0.045 180.8);
  --color-tcm02-line: #145247;
  --color-tcm02-line: oklch(0.397 0.064 178.3);
  --color-tcm02-chip: #ffffff14;
  --color-tcm02-chip: oklch(1 0 0 / 0.08);
  --color-tcm02-chip-ink: #c6f6e7;
  --color-tcm02-chip-ink: oklch(0.936 0.053 174.1);
  --color-tcm02-edge: #5eead44d;
  --color-tcm02-edge: oklch(0.855 0.125 181.1 / 0.3);
  --color-tcm02-acc: #14b8a6;
  --color-tcm02-acc: oklch(0.704 0.123 182.5);
  --color-tcm02-acc2: #10b981;
  --color-tcm02-acc2: oklch(0.696 0.149 162.5);
  --color-tcm02-acc-ink: #5eead4;
  --color-tcm02-acc-ink: oklch(0.855 0.125 181.1);
  --color-tcm02-on: #042f2b;
  --color-tcm02-on: oklch(0.276 0.046 185.6);
  --color-tcm02-tip: #ecfdf5;
  --color-tcm02-tip: oklch(0.979 0.021 166.1);
  --color-tcm02-tip-ink: #06302a;
  --color-tcm02-tip-ink: oklch(0.279 0.046 181.1);
  --color-tcm02-ring: #5eead4;
  --color-tcm02-ring: oklch(0.855 0.125 181.1);
}
```
