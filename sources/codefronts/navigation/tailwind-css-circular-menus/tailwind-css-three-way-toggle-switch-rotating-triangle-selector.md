---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-three-way-toggle-switch-rotating-triangle-selector/"
title: "Tailwind CSS Three-Way Toggle Switch (Rotating Triangle Selector)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A focus timer&rsquo;s Work / Rest / Play switch built on a rounded triangle that turns 120&deg; per choice, so its glowing vertex always points at the active…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Three-Way Toggle Switch (Rotating Triangle Selector)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-three-way-toggle-switch-rotating-triangle-selector/

A focus timer&rsquo;s Work / Rest / Play switch built on a rounded triangle that turns 120&deg; per choice, so its glowing vertex always points at the active mode. The plate rotates with rotate-(--rot), the script always spins the short way, and the timer readout updates with the mode. Three states are a radio group &mdash; arrow keys rotate it natively.
## HTML
```html
<section class="tcm-20 w-full min-h-svh grid place-items-center bg-tcm20-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm20-glow),transparent_72%)] px-5 py-14 font-tcm20-sans text-tcm20-ink antialiased" aria-label="Three-way toggle switch demo">
  <div id="tcm-20-timer" class="grid w-full justify-items-center gap-6">
    <header class="grid justify-items-center gap-1 text-center">
      <p class="font-tcm20-mono text-[11px] tracking-[0.18em] text-tcm20-acc-ink uppercase">Tempo · Focus timer</p>
      <p data-time class="font-tcm20-mono text-[clamp(3rem,10vw,4.25rem)] leading-none font-semibold tracking-[-0.04em] tabular-nums">25:00</p>
      <p data-sub aria-live="polite" class="text-[14px] text-tcm20-mut">Deep focus, notifications off</p>
    </header>
    <fieldset class="relative my-5 size-[min(19rem,84vw)] [--r:min(8.4rem,37vw)]">
      <legend class="sr-only">Timer mode</legend>
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--r))] rounded-full border border-dashed border-tcm20-acc/45"></span>
      <svg data-plate viewBox="0 0 200 200" aria-hidden="true" class="absolute top-1/2 left-1/2 size-[58%] -translate-1/2 rotate-(--rot) drop-shadow-[0_18px_30px_oklch(0.2_0.06_270/0.45)] transition-[rotate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] [--rot:0deg] motion-reduce:transition-none">
        <defs><linearGradient id="tcm-20-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="[stop-color:var(--color-tcm20-plate-hi)]"/><stop offset="1" class="[stop-color:var(--color-tcm20-plate)]"/></linearGradient></defs>
        <path d="M100 18 L172 143 Q179 155 165 155 L35 155 Q21 155 28 143 Z" fill="url(#tcm-20-g)" class="stroke-tcm20-line [stroke-width:1.5]"/>
        <circle cx="100" cy="44" r="6" class="fill-tcm20-acc"/>
        <circle cx="100" cy="44" r="12" class="fill-tcm20-acc/25"/>
      </svg>
      <div class="tcm20-polar absolute top-1/2 left-1/2 size-0 [--i:0] [--a:calc(120deg*var(--i)-90deg)]">
        <input type="radio" name="tcm-20-mode" id="tcm-20-m0" value="Work" data-time="25:00" data-sub="Deep focus, notifications off" class="peer sr-only" checked>
        <label for="tcm-20-m0" class="grid h-11 min-w-[5.25rem] -translate-1/2 cursor-pointer place-items-center rounded-full bg-tcm20-chip px-4 text-[14px] font-semibold tracking-[0.04em] text-tcm20-ink ring-1 ring-tcm20-line transition-[background-color,color,scale,box-shadow] duration-300 hover:ring-tcm20-acc/70 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm20-acc peer-checked:to-tcm20-acc2 peer-checked:text-tcm20-on peer-checked:shadow-tcm20-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm20-ring motion-reduce:transition-none">Work</label>
      </div>
      <div class="tcm20-polar absolute top-1/2 left-1/2 size-0 [--i:1] [--a:calc(120deg*var(--i)-90deg)]">
        <input type="radio" name="tcm-20-mode" id="tcm-20-m1" value="Rest" data-time="05:00" data-sub="Stand up, look far away" class="peer sr-only">
        <label for="tcm-20-m1" class="grid h-11 min-w-[5.25rem] -translate-1/2 cursor-pointer place-items-center rounded-full bg-tcm20-chip px-4 text-[14px] font-semibold tracking-[0.04em] text-tcm20-ink ring-1 ring-tcm20-line transition-[background-color,color,scale,box-shadow] duration-300 hover:ring-tcm20-acc/70 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm20-acc peer-checked:to-tcm20-acc2 peer-checked:text-tcm20-on peer-checked:shadow-tcm20-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm20-ring motion-reduce:transition-none">Rest</label>
      </div>
      <div class="tcm20-polar absolute top-1/2 left-1/2 size-0 [--i:2] [--a:calc(120deg*var(--i)-90deg)]">
        <input type="radio" name="tcm-20-mode" id="tcm-20-m2" value="Play" data-time="15:00" data-sub="Long break, guilt-free" class="peer sr-only">
        <label for="tcm-20-m2" class="grid h-11 min-w-[5.25rem] -translate-1/2 cursor-pointer place-items-center rounded-full bg-tcm20-chip px-4 text-[14px] font-semibold tracking-[0.04em] text-tcm20-ink ring-1 ring-tcm20-line transition-[background-color,color,scale,box-shadow] duration-300 hover:ring-tcm20-acc/70 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm20-acc peer-checked:to-tcm20-acc2 peer-checked:text-tcm20-on peer-checked:shadow-tcm20-glow peer-checked:ring-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcm20-ring motion-reduce:transition-none">Play</label>
      </div>
    </fieldset>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm20-card px-3.5 py-2 text-center font-tcm20-mono text-[11.5px] text-tcm20-mut ring-1 ring-tcm20-line ">rotate-(--rot) · ±120° shortest spin · peer-checked:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm20-bg: #f2f3f9;
  --color-tcm20-bg: oklch(0.965 0.008 278.6);
  --color-tcm20-glow: #fed7aab3;
  --color-tcm20-glow: oklch(0.901 0.073 70.7 / 0.7);
  --color-tcm20-chip: #ffffff;
  --color-tcm20-chip: oklch(1 0 0);
  --color-tcm20-plate-hi: #3b3f63;
  --color-tcm20-plate-hi: oklch(0.381 0.062 278.2);
  --color-tcm20-plate: #23263f;
  --color-tcm20-plate: oklch(0.278 0.046 277.7);
  --color-tcm20-ink: #171a30;
  --color-tcm20-ink: oklch(0.227 0.043 276.5);
  --color-tcm20-mut: #585d7b;
  --color-tcm20-mut: oklch(0.486 0.049 277.1);
  --color-tcm20-line: #d5d8e8;
  --color-tcm20-line: oklch(0.885 0.022 277.5);
  --color-tcm20-acc: #f59e0b;
  --color-tcm20-acc: oklch(0.769 0.165 70.1);
  --color-tcm20-acc2: #ea580c;
  --color-tcm20-acc2: oklch(0.646 0.194 41.1);
  --color-tcm20-on: #2b1503;
  --color-tcm20-on: oklch(0.223 0.047 58.7);
  --color-tcm20-acc-ink: #b45309;
  --color-tcm20-acc-ink: oklch(0.555 0.146 49);
  --color-tcm20-ring: #b45309;
  --color-tcm20-ring: oklch(0.555 0.146 49);
  --color-tcm20-card: #ffffff;
  --color-tcm20-card: oklch(1 0 0);
  --font-tcm20-sans: 'Outfit', system-ui, sans-serif;
  --font-tcm20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm20-glow: 0 0 0 4px oklch(0.8 0.16 70 / 0.2), 0 10px 26px -8px oklch(0.7 0.18 55 / 0.7);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-20 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm20-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: midnight amber: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-20:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm20-bg: #0d0f1d;
    --color-tcm20-bg: oklch(0.174 0.029 276.7);
    --color-tcm20-glow: #9a341259;
    --color-tcm20-glow: oklch(0.47 0.143 37.3 / 0.35);
    --color-tcm20-chip: #1a1d33;
    --color-tcm20-chip: oklch(0.239 0.042 276.8);
    --color-tcm20-plate-hi: #4a4f7a;
    --color-tcm20-plate-hi: oklch(0.442 0.071 278);
    --color-tcm20-plate: #272a46;
    --color-tcm20-plate: oklch(0.296 0.051 278.1);
    --color-tcm20-ink: #eef0fb;
    --color-tcm20-ink: oklch(0.957 0.015 277.9);
    --color-tcm20-mut: #a2a7c6;
    --color-tcm20-mut: oklch(0.735 0.045 278);
    --color-tcm20-line: #2f3354;
    --color-tcm20-line: oklch(0.334 0.058 277.5);
    --color-tcm20-acc: #fbbf24;
    --color-tcm20-acc: oklch(0.837 0.164 84.4);
    --color-tcm20-acc2: #fb923c;
    --color-tcm20-acc2: oklch(0.758 0.159 55.9);
    --color-tcm20-on: #2b1503;
    --color-tcm20-on: oklch(0.223 0.047 58.7);
    --color-tcm20-acc-ink: #fcd34d;
    --color-tcm20-acc-ink: oklch(0.879 0.153 91.6);
    --color-tcm20-ring: #fcd34d;
    --color-tcm20-ring: oklch(0.879 0.153 91.6);
    --color-tcm20-card: #161930;
    --color-tcm20-card: oklch(0.223 0.045 276.5);
  }
}

.tcm-20[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm20-bg: #0d0f1d;
  --color-tcm20-bg: oklch(0.174 0.029 276.7);
  --color-tcm20-glow: #9a341259;
  --color-tcm20-glow: oklch(0.47 0.143 37.3 / 0.35);
  --color-tcm20-chip: #1a1d33;
  --color-tcm20-chip: oklch(0.239 0.042 276.8);
  --color-tcm20-plate-hi: #4a4f7a;
  --color-tcm20-plate-hi: oklch(0.442 0.071 278);
  --color-tcm20-plate: #272a46;
  --color-tcm20-plate: oklch(0.296 0.051 278.1);
  --color-tcm20-ink: #eef0fb;
  --color-tcm20-ink: oklch(0.957 0.015 277.9);
  --color-tcm20-mut: #a2a7c6;
  --color-tcm20-mut: oklch(0.735 0.045 278);
  --color-tcm20-line: #2f3354;
  --color-tcm20-line: oklch(0.334 0.058 277.5);
  --color-tcm20-acc: #fbbf24;
  --color-tcm20-acc: oklch(0.837 0.164 84.4);
  --color-tcm20-acc2: #fb923c;
  --color-tcm20-acc2: oklch(0.758 0.159 55.9);
  --color-tcm20-on: #2b1503;
  --color-tcm20-on: oklch(0.223 0.047 58.7);
  --color-tcm20-acc-ink: #fcd34d;
  --color-tcm20-acc-ink: oklch(0.879 0.153 91.6);
  --color-tcm20-ring: #fcd34d;
  --color-tcm20-ring: oklch(0.879 0.153 91.6);
  --color-tcm20-card: #161930;
  --color-tcm20-card: oklch(0.223 0.045 276.5);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-20-timer');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const plate = root.querySelector('[data-plate]');
  const time = root.querySelector('[data-time]'), sub = root.querySelector('[data-sub]');
  const radios = [...root.querySelectorAll('input[name="tcm-20-mode"]')];
  let rot = 0, cur = 0;
  root.addEventListener('change', (e) => {
    const idx = radios.indexOf(e.target);
    if (idx < 0) return;
    rot += ((idx - cur) * 120 % 360 + 540) % 360 - 180;
    cur = idx;
    plate.style.setProperty('--rot', rot + 'deg');
    time.textContent = e.target.dataset.time;
    sub.textContent = e.target.dataset.sub;
  });
})();
```
