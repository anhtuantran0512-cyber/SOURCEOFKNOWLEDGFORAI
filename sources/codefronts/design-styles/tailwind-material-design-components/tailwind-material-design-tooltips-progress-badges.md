---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-tooltips-progress-badges/"
title: "Tailwind Material Design Tooltips, Progress and Badges"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Plain tooltips in all four positions, a rich tooltip, linear and circular progress (determinate and indeterminate) and the badge family."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Tooltips, Progress and Badges
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-tooltips-progress-badges/

Plain tooltips in all four positions, a rich tooltip, linear and circular progress (determinate and indeterminate) and the badge family. Two things are better than the CSS original: tooltips appear on focus-visible as well as hover, so keyboard users get them; and the circular indicator animates a real @property angle instead of a rotating mask.
## HTML
```html
<section class="tmd-10 w-full min-h-svh bg-tmd10-bg font-tmd10-sans text-tmd10-onsurface px-5 py-9" aria-label="Material Design tooltips and progress demo">
  <div class="w-[min(880px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Tooltips, progress &amp; badges</h2>
      <p class="text-sm text-tmd10-onvariant">Tooltips answer to <code class="font-tmd10-mono text-[12px]">focus-visible</code> as well as hover; the ring animates a registered angle.</p>
    </header>

    <div class="grid gap-6 p-6 rounded-3xl bg-tmd10-surface shadow-tmd10-1">
      <span class="font-tmd10-mono text-[11px] uppercase tracking-[0.1em] text-tmd10-onvariant">Tooltips &mdash; tab to them, don't just hover</span>
      <div class="flex flex-wrap justify-center gap-8 py-6">
        <span class="group relative inline-block">
          <button type="button" aria-describedby="tmd10-tip-t" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border border-tmd10-outlinevariant bg-tmd10-surface cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-0 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[20px] leading-none" aria-hidden="true">north</span></button>
          <span id="tmd10-tip-t" role="tooltip" class="absolute bottom-full left-1/2 [transform:translateX(-50%)] mb-2 px-2.5 py-1.5 rounded bg-tmd10-inverse text-tmd10-oninverse text-xs whitespace-nowrap opacity-0 invisible transition-[opacity,visibility] duration-150 group-hover:opacity-100 group-hover:visible group-focus-visible:opacity-100 group-focus-visible:visible after:absolute after:top-full after:left-1/2 after:[transform:translateX(-50%)] after:border-4 after:border-transparent after:border-t-tmd10-inverse">Above the trigger</span>
        </span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="tmd10-tip-b" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border border-tmd10-outlinevariant bg-tmd10-surface cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-0 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[20px] leading-none" aria-hidden="true">south</span></button>
          <span id="tmd10-tip-b" role="tooltip" class="absolute top-full left-1/2 [transform:translateX(-50%)] mt-2 px-2.5 py-1.5 rounded bg-tmd10-inverse text-tmd10-oninverse text-xs whitespace-nowrap opacity-0 invisible transition-[opacity,visibility] duration-150 group-hover:opacity-100 group-hover:visible group-focus-visible:opacity-100 group-focus-visible:visible after:absolute after:bottom-full after:left-1/2 after:[transform:translateX(-50%)] after:border-4 after:border-transparent after:border-b-tmd10-inverse">Below the trigger</span>
        </span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="tmd10-tip-l" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border border-tmd10-outlinevariant bg-tmd10-surface cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-0 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[20px] leading-none" aria-hidden="true">west</span></button>
          <span id="tmd10-tip-l" role="tooltip" class="absolute right-full top-1/2 [transform:translateY(-50%)] mr-2 px-2.5 py-1.5 rounded bg-tmd10-inverse text-tmd10-oninverse text-xs whitespace-nowrap opacity-0 invisible transition-[opacity,visibility] duration-150 group-hover:opacity-100 group-hover:visible group-focus-visible:opacity-100 group-focus-visible:visible after:absolute after:left-full after:top-1/2 after:[transform:translateY(-50%)] after:border-4 after:border-transparent after:border-l-tmd10-inverse">To the left</span>
        </span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="tmd10-tip-r" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-4 rounded-full border border-tmd10-outlinevariant bg-tmd10-surface cursor-pointer text-sm font-medium text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-0 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[18px] leading-none" aria-hidden="true">info</span>Rich tooltip</button>
          <span id="tmd10-tip-r" role="tooltip" class="absolute left-full top-1/2 ml-2 w-56 p-3 rounded-xl bg-tmd10-surface border border-tmd10-outlinevariant shadow-tmd10-2 text-left opacity-0 invisible [transform:translate(4px,-50%)] transition-[opacity,visibility,transform] duration-200 group-hover:opacity-100 group-hover:visible group-hover:[transform:translate(0,-50%)] group-focus-visible:opacity-100 group-focus-visible:visible group-focus-visible:[transform:translate(0,-50%)] motion-reduce:transition-none">
            <b class="block mb-1 text-[13px] font-medium">Calibration drift</b>
            <span class="block text-xs leading-5 text-tmd10-onvariant">A rich tooltip carries a title, body copy and an action. It is a surface, not an inverse bubble.</span>
          </span>
        </span>
      </div>
    </div>

    <div class="grid gap-5 p-6 rounded-3xl bg-tmd10-surface shadow-tmd10-1">
      <span class="font-tmd10-mono text-[11px] uppercase tracking-[0.1em] text-tmd10-onvariant">Progress indicators</span>
      <div class="grid gap-1.5">
        <div class="flex justify-between text-xs text-tmd10-onvariant"><span>Determinate &mdash; upload</span><span class="font-tmd10-mono tabular-nums">68%</span></div>
        <div role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Upload progress" class="h-1 rounded-full bg-tmd10-track overflow-hidden"><div class="h-full w-[68%] rounded-full bg-tmd10-primary transition-[width] duration-300"></div></div>
      </div>
      <div class="grid gap-1.5">
        <span class="text-xs text-tmd10-onvariant">Indeterminate &mdash; syncing</span>
        <div role="progressbar" aria-label="Syncing" class="relative h-1 rounded-full bg-tmd10-track overflow-hidden"><div class="absolute inset-y-0 w-2/5 rounded-full bg-tmd10-primary animate-tmd10-indeterminate motion-reduce:animate-none motion-reduce:w-full motion-reduce:opacity-40"></div></div>
      </div>
      <div class="flex flex-wrap items-center gap-8 pt-2">
        <div class="grid justify-items-center gap-2">
          <div class="relative grid place-items-center w-20 h-20 rounded-full [--tmd10-deg:245deg] [background:conic-gradient(var(--color-tmd10-primary)_var(--tmd10-deg),var(--color-tmd10-track)_0)] transition-[--tmd10-deg] duration-700 hover:[--tmd10-deg:324deg] motion-reduce:transition-none" role="img" aria-label="68 percent complete">
            <div class="absolute inset-1.5 rounded-full bg-tmd10-surface"></div>
            <span class="relative font-tmd10-mono text-sm font-medium tabular-nums">68%</span>
          </div>
          <span class="text-[11px] text-tmd10-onvariant">hover to animate</span>
        </div>
        <div class="grid justify-items-center gap-2">
          <div class="w-20 h-20 rounded-full [background:conic-gradient(var(--color-tmd10-primary)_0_90deg,var(--color-tmd10-track)_90deg_360deg)] [mask:radial-gradient(farthest-side,transparent_calc(100%-6px),black_calc(100%-6px))] animate-spin [animation-duration:1.1s] motion-reduce:animate-none" role="progressbar" aria-label="Loading"></div>
          <span class="text-[11px] text-tmd10-onvariant">indeterminate ring</span>
        </div>
      </div>
    </div>

    <div class="grid gap-4 p-6 rounded-3xl bg-tmd10-surface shadow-tmd10-1">
      <span class="font-tmd10-mono text-[11px] uppercase tracking-[0.1em] text-tmd10-onvariant">Badges</span>
      <div class="flex flex-wrap items-center gap-7">
        <span class="relative inline-block">
          <button type="button" aria-label="Notifications, 3 unread" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[22px] leading-none" aria-hidden="true">notifications</span></button>
          <span class="absolute top-1 right-1 min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd10-error text-white font-tmd10-mono text-[10px] tabular-nums pointer-events-none" aria-hidden="true">3</span>
        </span>
        <span class="relative inline-block">
          <button type="button" aria-label="Mail, 128 unread" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[22px] leading-none" aria-hidden="true">mail</span></button>
          <span class="absolute top-0.5 right-0 min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd10-error text-white font-tmd10-mono text-[10px] tabular-nums pointer-events-none" aria-hidden="true">128</span>
        </span>
        <span class="relative inline-block">
          <button type="button" aria-label="Updates available" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd10-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd10-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd10-icon text-[22px] leading-none" aria-hidden="true">cloud_sync</span></button>
          <span class="absolute top-2 right-2 w-2 h-2 rounded-full bg-tmd10-error pointer-events-none" aria-hidden="true"></span>
        </span>
        <span class="inline-flex items-center gap-2 h-8 px-3 rounded-full bg-tmd10-primarycontainer text-tmd10-onprimarycontainer text-xs font-medium"><span class="w-1.5 h-1.5 rounded-full bg-tmd10-primary"></span>Live &middot; 18 stations</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd10-bg: #e0f2f1;
  --color-tmd10-bg: oklch(0.948 0.019 192.8);
  --color-tmd10-surface: #ffffff;
  --color-tmd10-surface: oklch(1 0 89.9);
  --color-tmd10-primary: #00695c;
  --color-tmd10-primary: oklch(0.467 0.084 180.4);
  --color-tmd10-primarycontainer: #cfe9e5;
  --color-tmd10-primarycontainer: oklch(0.914 0.028 185.5);
  --color-tmd10-onprimarycontainer: #002019;
  --color-tmd10-onprimarycontainer: oklch(0.217 0.041 175.3);
  --color-tmd10-track: #cfe0dd;
  --color-tmd10-track: oklch(0.893 0.019 184.2);
  --color-tmd10-onsurface: #161d1c;
  --color-tmd10-onsurface: oklch(0.223 0.01 185.9);
  --color-tmd10-onvariant: #4a5b58;
  --color-tmd10-onvariant: oklch(0.456 0.022 183.5);
  --color-tmd10-outlinevariant: #c4d6d3;
  --color-tmd10-outlinevariant: oklch(0.862 0.02 184.8);
  --color-tmd10-inverse: #2b3231;
  --color-tmd10-inverse: oklch(0.31 0.01 186.3);
  --color-tmd10-oninverse: #eff1f0;
  --color-tmd10-oninverse: oklch(0.956 0.003 165.1);
  --color-tmd10-error: #b3261e;
  --color-tmd10-error: oklch(0.501 0.178 28.7);
  --font-tmd10-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd10-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd10-icon: 'Material Symbols Outlined';
  --shadow-tmd10-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
  --shadow-tmd10-2: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 2px 6px 2px rgb(0 0 0 / 0.15);
  --animate-tmd10-indeterminate: tmd10-indeterminate 1.6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
/* Keyframes cannot be utilities — but the animation that uses them can, because the
   @theme --animate-* entry above mints the animate-tmd10-indeterminate utility. */

@keyframes tmd10-indeterminate {
  0% {
    left: -40%;
  }

  100% {
    left: 100%;
  }
}
/* A custom property must be registered to interpolate. Without this the conic ring
   jumps between angles instead of sweeping — and there is no utility for @property. */

@property --tmd10-deg {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.tmd-10 {
  width: 100%;
  min-height: 100svh;
}

.tmd-10 .font-tmd10-icon {
  font-feature-settings: 'liga';
}
```
