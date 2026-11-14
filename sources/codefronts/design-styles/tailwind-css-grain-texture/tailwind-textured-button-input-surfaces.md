---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-textured-button-input-surfaces/"
title: "Tailwind Textured Button and Input Surfaces"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "A control kit where every surface is a material: buttons are raised, inputs are recessed, and both carry the same grain token."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Textured Button and Input Surfaces
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-textured-button-input-surfaces/

A control kit where every surface is a material: buttons are raised, inputs are recessed, and both carry the same grain token. Press a button and three things change at once — grain weight, highlight direction and shadow depth. The port's wins are active:after: for the pressed texture and peer-user-invalid: for validation copy that cannot drift from the field it describes.
## HTML
```html
<section class="gtw-12 relative block w-full min-h-svh bg-gtw12-bg text-gtw12-ink" aria-labelledby="gtw-12-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-12-theme" class="gtw-12-theme peer sr-only">
    <label for="gtw-12-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw12-line bg-gtw12-surf text-gtw12-ink cursor-pointer shadow-[inset_0_1px_0_var(--gtw12-hl)] peer-focus-visible:outline-2 peer-focus-visible:outline-gtw12-acc peer-focus-visible:outline-offset-2">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(76rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <header class="max-w-[44rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw12-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw12-acc">Control surfaces · 12</p>
      <h1 id="gtw-12-title" class="m-0 font-gtw12-display text-[clamp(2rem,5.4vw,3.3rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Every control is a material</h1>
      <p class="m-0 max-w-[38rem] text-gtw12-mut text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Buttons are raised, inputs are recessed, and both carry the same grain. Press a button and three things change at once — grain weight, highlight direction, shadow depth.</p>
    </header>

    <div class="grid gap-[clamp(1rem,2.4vw,1.5rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))] items-start">
      <section class="relative isolate overflow-hidden grid gap-4 content-start min-w-0 p-[clamp(1.2rem,3vw,1.7rem)] rounded-[18px] border border-gtw12-line bg-gtw12-surf shadow-[inset_0_1px_0_var(--gtw12-hl),0_12px_30px_-20px_oklch(0.2_0.03_275/0.3)] after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:opacity-[0.04] after:[mix-blend-mode:var(--gtw12-blend)]" aria-labelledby="gtw-12-h-btn">
        <h2 id="gtw-12-h-btn" class="m-0 pb-[0.6rem] border-b border-gtw12-line font-gtw12-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Buttons</h2>
        <div class="flex flex-wrap gap-[0.6rem]">
          <button type="button" class="relative isolate overflow-hidden inline-flex items-center justify-center min-h-11 px-[1.2rem] rounded-[12px] border-0 bg-gtw12-acc text-gtw12-onacc font-gtw12-display text-[0.88rem] font-semibold leading-none cursor-pointer shadow-[inset_0_1px_0_rgba(255,255,255,0.24),0_2px_5px_oklch(0.2_0.03_275/0.22)] transition-[box-shadow] duration-200 active:shadow-[inset_0_-1px_0_rgba(255,255,255,0.2),inset_0_2px_6px_oklch(0_0_0/0.3)] focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:mix-blend-overlay after:opacity-[var(--gtw12-idle)] after:transition-opacity after:duration-150 hover:after:opacity-[var(--gtw12-hover)] active:after:opacity-[var(--gtw12-active)]">Save changes</button>
          <button type="button" class="relative isolate overflow-hidden inline-flex items-center justify-center min-h-11 px-[1.2rem] rounded-[12px] border-0 bg-gtw12-sunk text-gtw12-ink font-gtw12-display text-[0.88rem] font-semibold leading-none cursor-pointer shadow-[inset_0_1px_0_var(--gtw12-hl),0_1px_3px_oklch(0.2_0.03_275/0.14)] transition-[box-shadow] duration-200 active:shadow-[inset_0_2px_6px_oklch(0_0_0/0.22)] focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:[mix-blend-mode:var(--gtw12-blend)] after:opacity-[var(--gtw12-idle)] after:transition-opacity after:duration-150 hover:after:opacity-[var(--gtw12-hover)] active:after:opacity-[var(--gtw12-active)]">Preview</button>
          <button type="button" class="inline-flex items-center justify-center min-h-11 px-[1.2rem] rounded-[12px] bg-transparent border border-gtw12-line text-gtw12-mut font-gtw12-display text-[0.88rem] font-semibold leading-none cursor-pointer transition-colors duration-200 hover:text-gtw12-ink hover:border-gtw12-acc focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2">Cancel</button>
          <button type="button" disabled class="inline-flex items-center justify-center min-h-11 px-[1.2rem] rounded-[12px] border-0 bg-gtw12-acc text-gtw12-onacc font-gtw12-display text-[0.88rem] font-semibold leading-none opacity-45 cursor-not-allowed shadow-none">Disabled</button>
        </div>
        <div role="group" aria-label="Density" class="flex flex-wrap p-1 rounded-[16px] border border-gtw12-line bg-gtw12-sunk shadow-[inset_0_2px_5px_oklch(0.2_0.03_275/0.12)]">
          <input type="radio" name="gtw-12-density" id="gtw-12-d1" checked class="peer/d1 sr-only">
          <label for="gtw-12-d1" class="relative isolate overflow-hidden flex-auto inline-flex items-center justify-center min-h-10 px-[0.8rem] rounded-[12px] text-gtw12-mut font-gtw12-display text-[0.83rem] font-semibold leading-none cursor-pointer transition-colors duration-200 peer-checked/d1:bg-gtw12-surf peer-checked/d1:text-gtw12-ink peer-checked/d1:shadow-[inset_0_1px_0_var(--gtw12-hl),0_1px_3px_oklch(0.2_0.03_275/0.18)] peer-focus-visible/d1:outline-2 peer-focus-visible/d1:outline-gtw12-acc peer-focus-visible/d1:outline-offset-2 peer-checked/d1:after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:[mix-blend-mode:var(--gtw12-blend)] after:opacity-[var(--gtw12-idle)]">Compact</label>
          <input type="radio" name="gtw-12-density" id="gtw-12-d2" class="peer/d2 sr-only">
          <label for="gtw-12-d2" class="relative isolate overflow-hidden flex-auto inline-flex items-center justify-center min-h-10 px-[0.8rem] rounded-[12px] text-gtw12-mut font-gtw12-display text-[0.83rem] font-semibold leading-none cursor-pointer transition-colors duration-200 peer-checked/d2:bg-gtw12-surf peer-checked/d2:text-gtw12-ink peer-checked/d2:shadow-[inset_0_1px_0_var(--gtw12-hl),0_1px_3px_oklch(0.2_0.03_275/0.18)] peer-focus-visible/d2:outline-2 peer-focus-visible/d2:outline-gtw12-acc peer-focus-visible/d2:outline-offset-2 peer-checked/d2:after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:[mix-blend-mode:var(--gtw12-blend)] after:opacity-[var(--gtw12-idle)]">Regular</label>
          <input type="radio" name="gtw-12-density" id="gtw-12-d3" class="peer/d3 sr-only">
          <label for="gtw-12-d3" class="relative isolate overflow-hidden flex-auto inline-flex items-center justify-center min-h-10 px-[0.8rem] rounded-[12px] text-gtw12-mut font-gtw12-display text-[0.83rem] font-semibold leading-none cursor-pointer transition-colors duration-200 peer-checked/d3:bg-gtw12-surf peer-checked/d3:text-gtw12-ink peer-checked/d3:shadow-[inset_0_1px_0_var(--gtw12-hl),0_1px_3px_oklch(0.2_0.03_275/0.18)] peer-focus-visible/d3:outline-2 peer-focus-visible/d3:outline-gtw12-acc peer-focus-visible/d3:outline-offset-2 peer-checked/d3:after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:[mix-blend-mode:var(--gtw12-blend)] after:opacity-[var(--gtw12-idle)]">Roomy</label>
        </div>
        <p class="m-0 text-gtw12-mut text-[0.8rem] text-pretty">Idle 0.05 · hover 0.06 · active 0.08 with the highlight inverted.</p>
      </section>

      <section class="relative isolate overflow-hidden grid gap-4 content-start min-w-0 p-[clamp(1.2rem,3vw,1.7rem)] rounded-[18px] border border-gtw12-line bg-gtw12-surf shadow-[inset_0_1px_0_var(--gtw12-hl),0_12px_30px_-20px_oklch(0.2_0.03_275/0.3)] after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:opacity-[0.04] after:[mix-blend-mode:var(--gtw12-blend)]" aria-labelledby="gtw-12-h-fields">
        <h2 id="gtw-12-h-fields" class="m-0 pb-[0.6rem] border-b border-gtw12-line font-gtw12-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Fields</h2>
        <div class="grid gap-[0.35rem]">
          <label for="gtw-12-name" class="font-gtw12-display text-[0.82rem] font-medium leading-[1.3]">Full name</label>
          <input type="text" id="gtw-12-name" name="gtw-12-name" placeholder="Ada Lovelace" autocomplete="name" class="min-h-[46px] px-[0.85rem] rounded-[12px] border border-gtw12-line text-gtw12-ink text-[0.95rem] leading-none [background-image:var(--gtw12-noise),linear-gradient(var(--color-gtw12-sunk),var(--color-gtw12-sunk))] [background-blend-mode:var(--gtw12-blend),normal] shadow-[inset_0_2px_5px_oklch(0.2_0.03_275/0.13),inset_0_-1px_0_var(--gtw12-hl)] placeholder:text-[color-mix(in_oklab,var(--color-gtw12-mut)_70%,transparent)] transition-colors duration-200 hover:border-[color-mix(in_oklab,var(--color-gtw12-acc)_45%,var(--color-gtw12-line))] focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2">
        </div>
        <div class="grid gap-[0.35rem]">
          <label for="gtw-12-mail" class="font-gtw12-display text-[0.82rem] font-medium leading-[1.3]">Work email</label>
          <input type="email" id="gtw-12-mail" name="gtw-12-mail" placeholder="[email protected]" autocomplete="email" required aria-describedby="gtw-12-mail-hint" class="peer/mail min-h-[46px] px-[0.85rem] rounded-[12px] border border-gtw12-line text-gtw12-ink text-[0.95rem] leading-none [background-image:var(--gtw12-noise),linear-gradient(var(--color-gtw12-sunk),var(--color-gtw12-sunk))] [background-blend-mode:var(--gtw12-blend),normal] shadow-[inset_0_2px_5px_oklch(0.2_0.03_275/0.13),inset_0_-1px_0_var(--gtw12-hl)] placeholder:text-[color-mix(in_oklab,var(--color-gtw12-mut)_70%,transparent)] transition-colors duration-200 hover:border-[color-mix(in_oklab,var(--color-gtw12-acc)_45%,var(--color-gtw12-line))] user-invalid:border-gtw12-err focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2">
          <p id="gtw-12-mail-hint" class="m-0 text-[0.8rem] text-gtw12-mut peer-user-invalid/mail:text-gtw12-err">We only email about deploys. Real address required.</p>
        </div>
        <div class="grid gap-[0.35rem]">
          <label for="gtw-12-region" class="font-gtw12-display text-[0.82rem] font-medium leading-[1.3]">Region</label>
          <select id="gtw-12-region" name="gtw-12-region" class="appearance-none min-h-[46px] pl-[0.85rem] pr-[2.2rem] rounded-[12px] border border-gtw12-line text-gtw12-ink text-[0.95rem] cursor-pointer [background-image:var(--gtw12-caret),var(--gtw12-noise),linear-gradient(var(--color-gtw12-sunk),var(--color-gtw12-sunk))] [background-position:right_0.9rem_center,0_0,0_0] [background-repeat:no-repeat,repeat,no-repeat] [background-blend-mode:normal,var(--gtw12-blend),normal] shadow-[inset_0_2px_5px_oklch(0.2_0.03_275/0.13),inset_0_-1px_0_var(--gtw12-hl)] transition-colors duration-200 hover:border-[color-mix(in_oklab,var(--color-gtw12-acc)_45%,var(--color-gtw12-line))] focus-visible:outline-2 focus-visible:outline-gtw12-acc focus-visible:outline-offset-2">
            <option>us-east-1 · N. Virginia</option>
            <option>us-west-2 · Oregon</option>
            <option>eu-west-2 · London</option>
            <option>ca-central-1 · Montréal</option>
            <option>ap-southeast-2 · Sydney</option>
          </select>
        </div>
      </section>

      <section class="relative isolate overflow-hidden grid gap-4 content-start min-w-0 p-[clamp(1.2rem,3vw,1.7rem)] rounded-[18px] border border-gtw12-line bg-gtw12-surf shadow-[inset_0_1px_0_var(--gtw12-hl),0_12px_30px_-20px_oklch(0.2_0.03_275/0.3)] after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw12-noise)] after:opacity-[0.04] after:[mix-blend-mode:var(--gtw12-blend)]" aria-labelledby="gtw-12-h-misc">
        <h2 id="gtw-12-h-misc" class="m-0 pb-[0.6rem] border-b border-gtw12-line font-gtw12-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Toggles and ranges</h2>
        <ul class="list-none m-0 p-0 grid gap-[0.1rem]">
          <li class="flex items-center gap-[0.6rem] min-h-11"><input type="checkbox" id="gtw-12-c1" checked class="w-5 h-5 m-0 cursor-pointer"><label for="gtw-12-c1" class="text-[0.92rem] cursor-pointer">Textured surfaces</label></li>
          <li class="flex items-center gap-[0.6rem] min-h-11"><input type="checkbox" id="gtw-12-c2" class="w-5 h-5 m-0 cursor-pointer"><label for="gtw-12-c2" class="text-[0.92rem] cursor-pointer">Reduce transparency</label></li>
          <li class="flex items-center gap-[0.6rem] min-h-11"><input type="radio" name="gtw-12-r" id="gtw-12-r1" checked class="w-5 h-5 m-0 cursor-pointer"><label for="gtw-12-r1" class="text-[0.92rem] cursor-pointer">Match system theme</label></li>
          <li class="flex items-center gap-[0.6rem] min-h-11"><input type="radio" name="gtw-12-r" id="gtw-12-r2" class="w-5 h-5 m-0 cursor-pointer"><label for="gtw-12-r2" class="text-[0.92rem] cursor-pointer">Always dark</label></li>
        </ul>
        <div class="grid gap-[0.35rem]">
          <label for="gtw-12-grain" class="font-gtw12-display text-[0.82rem] font-medium leading-[1.3]">Grain weight</label>
          <input type="range" id="gtw-12-grain" name="gtw-12-grain" min="0" max="20" value="6" step="1" class="w-full min-h-11 m-0 bg-transparent cursor-pointer">
          <p class="m-0 text-gtw12-mut text-[0.8rem] text-pretty">Native thumb, textured track, <code class="font-gtw12-mono text-[0.9em]">accent-color</code> for the fill.</p>
        </div>
      </section>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw12-bg: #eef0f7;
  --color-gtw12-bg: oklch(0.95 0.01 275);
  --color-gtw12-surf: #ffffff;
  --color-gtw12-surf: oklch(1 0 0);
  --color-gtw12-sunk: #e7eaf4;
  --color-gtw12-sunk: oklch(0.93 0.012 275);
  --color-gtw12-line: #d3d8e8;
  --color-gtw12-line: oklch(0.87 0.018 275);
  --color-gtw12-ink: #14162a;
  --color-gtw12-ink: oklch(0.22 0.04 275);
  --color-gtw12-mut: #5c6280;
  --color-gtw12-mut: oklch(0.47 0.04 275);
  --color-gtw12-acc: #4f46e5;
  --color-gtw12-acc: oklch(0.52 0.22 275);
  --color-gtw12-onacc: #f2f1fe;
  --color-gtw12-onacc: oklch(0.97 0.015 280);
  --color-gtw12-err: #b42318;
  --color-gtw12-err: oklch(0.5 0.18 27);
  --font-gtw12-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw12-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-12 {
  width: 100%;
  min-height: 100svh;
  --gtw12-idle: 0.05;
  --gtw12-hover: 0.06;
  --gtw12-active: 0.08;
  --gtw12-sunkw: 0.035;
  --gtw12-blend: multiply;
  --gtw12-hl: rgba(255, 255, 255, 0.85);
  --gtw12-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150'%3E%3Cfilter id='gtw12n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='150' height='150' filter='url(%23gtw12n)'/%3E%3C/svg%3E");
  --gtw12-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='9' viewBox='0 0 14 9'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%235c6280' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
  accent-color: var(--color-gtw12-acc);
}

.gtw-12:has(.gtw-12-theme:checked) {
  --color-gtw12-bg: #0c0d16;
  --color-gtw12-bg: oklch(0.16 0.02 275);
  --color-gtw12-surf: #15172a;
  --color-gtw12-surf: oklch(0.22 0.03 275);
  --color-gtw12-sunk: #10121f;
  --color-gtw12-sunk: oklch(0.18 0.025 275);
  --color-gtw12-line: #262a45;
  --color-gtw12-line: oklch(0.3 0.04 275);
  --color-gtw12-ink: #ecebfb;
  --color-gtw12-ink: oklch(0.94 0.015 280);
  --color-gtw12-mut: #9a9ac4;
  --color-gtw12-mut: oklch(0.7 0.05 280);
  --color-gtw12-acc: #a5b4fc;
  --color-gtw12-acc: oklch(0.8 0.11 278);
  --color-gtw12-onacc: #10122a;
  --color-gtw12-onacc: oklch(0.19 0.04 278);
  --color-gtw12-err: #fca5a5;
  --color-gtw12-err: oklch(0.78 0.13 22);
  --gtw12-blend: soft-light;
  --gtw12-hl: rgba(255, 255, 255, 0.12);
  --gtw12-idle: 0.07;
  --gtw12-hover: 0.085;
  --gtw12-active: 0.11;
  --gtw12-sunkw: 0.05;
  --gtw12-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='9' viewBox='0 0 14 9'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%239a9ac4' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E");
}

@media (prefers-color-scheme: dark) {
  .gtw-12 {
    --color-gtw12-bg: #0c0d16;
    --color-gtw12-bg: oklch(0.16 0.02 275);
    --color-gtw12-surf: #15172a;
    --color-gtw12-surf: oklch(0.22 0.03 275);
    --color-gtw12-sunk: #10121f;
    --color-gtw12-sunk: oklch(0.18 0.025 275);
    --color-gtw12-line: #262a45;
    --color-gtw12-line: oklch(0.3 0.04 275);
    --color-gtw12-ink: #ecebfb;
    --color-gtw12-ink: oklch(0.94 0.015 280);
    --color-gtw12-mut: #9a9ac4;
    --color-gtw12-mut: oklch(0.7 0.05 280);
    --color-gtw12-acc: #a5b4fc;
    --color-gtw12-acc: oklch(0.8 0.11 278);
    --color-gtw12-onacc: #10122a;
    --color-gtw12-onacc: oklch(0.19 0.04 278);
    --color-gtw12-err: #fca5a5;
    --color-gtw12-err: oklch(0.78 0.13 22);
    --gtw12-blend: soft-light;
    --gtw12-hl: rgba(255, 255, 255, 0.12);
    --gtw12-idle: 0.07;
    --gtw12-hover: 0.085;
    --gtw12-active: 0.11;
    --gtw12-sunkw: 0.05;
    --gtw12-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='9' viewBox='0 0 14 9'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%239a9ac4' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E");
  }

  .gtw-12:has(.gtw-12-theme:checked) {
    --color-gtw12-bg: #eef0f7;
    --color-gtw12-bg: oklch(0.95 0.01 275);
    --color-gtw12-surf: #ffffff;
    --color-gtw12-surf: oklch(1 0 0);
    --color-gtw12-sunk: #e7eaf4;
    --color-gtw12-sunk: oklch(0.93 0.012 275);
    --color-gtw12-line: #d3d8e8;
    --color-gtw12-line: oklch(0.87 0.018 275);
    --color-gtw12-ink: #14162a;
    --color-gtw12-ink: oklch(0.22 0.04 275);
    --color-gtw12-mut: #5c6280;
    --color-gtw12-mut: oklch(0.47 0.04 275);
    --color-gtw12-acc: #4f46e5;
    --color-gtw12-acc: oklch(0.52 0.22 275);
    --color-gtw12-onacc: #f2f1fe;
    --color-gtw12-onacc: oklch(0.97 0.015 280);
    --color-gtw12-err: #b42318;
    --color-gtw12-err: oklch(0.5 0.18 27);
    --gtw12-blend: multiply;
    --gtw12-hl: rgba(255, 255, 255, 0.85);
    --gtw12-idle: 0.05;
    --gtw12-hover: 0.06;
    --gtw12-active: 0.08;
    --gtw12-sunkw: 0.035;
    --gtw12-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='9' viewBox='0 0 14 9'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%235c6280' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E");
  }
}

@media (prefers-color-scheme: light) {
  .gtw-12:has(.gtw-12-theme:checked) {
    --color-gtw12-bg: #0c0d16;
    --color-gtw12-bg: oklch(0.16 0.02 275);
    --color-gtw12-surf: #15172a;
    --color-gtw12-surf: oklch(0.22 0.03 275);
    --color-gtw12-sunk: #10121f;
    --color-gtw12-sunk: oklch(0.18 0.025 275);
    --color-gtw12-line: #262a45;
    --color-gtw12-line: oklch(0.3 0.04 275);
    --color-gtw12-ink: #ecebfb;
    --color-gtw12-ink: oklch(0.94 0.015 280);
    --color-gtw12-mut: #9a9ac4;
    --color-gtw12-mut: oklch(0.7 0.05 280);
    --color-gtw12-acc: #a5b4fc;
    --color-gtw12-acc: oklch(0.8 0.11 278);
    --color-gtw12-onacc: #10122a;
    --color-gtw12-onacc: oklch(0.19 0.04 278);
    --color-gtw12-err: #fca5a5;
    --color-gtw12-err: oklch(0.78 0.13 22);
    --gtw12-blend: soft-light;
    --gtw12-hl: rgba(255, 255, 255, 0.12);
    --gtw12-idle: 0.07;
    --gtw12-hover: 0.085;
    --gtw12-active: 0.11;
    --gtw12-sunkw: 0.05;
    --gtw12-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='9' viewBox='0 0 14 9'%3E%3Cpath d='M1 1l6 6 6-6' fill='none' stroke='%239a9ac4' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E");
  }
}
```
