---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-neumorphic-bottom-navigation-bar/"
title: "Tailwind Neumorphic Bottom Navigation Bar"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A soft-UI fitness app on #e0e5ec: raised cards, recessed wells, and a bottom bar whose active tab presses into the surface."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Bottom Navigation Bar
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-neumorphic-bottom-navigation-bar/

A soft-UI fitness app on #e0e5ec: raised cards, recessed wells, and a bottom bar whose active tab presses into the surface. Every shadow pair is a --shadow-tmn16-* theme token, so shadow-tmn16-up and shadow-tmn16-in are the whole design language. Zero JavaScript.
## HTML
```html
<section class="tmn-16 w-full min-h-svh grid place-items-center bg-tmn16-stage px-4 py-6 font-tmn16-sans antialiased" aria-label="Tailwind neumorphic bottom navigation demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn16-bg text-tmn16-ink shadow-[0_40px_100px_-30px_oklch(0.3_0.03_255/0.55)]">
    <input type="radio" name="tmn-16-tab" id="tmn-16-t1" class="sr-only" checked>
    <input type="radio" name="tmn-16-tab" id="tmn-16-t2" class="sr-only">
    <input type="radio" name="tmn-16-tab" id="tmn-16-t3" class="sr-only">
    <input type="radio" name="tmn-16-tab" id="tmn-16-t4" class="sr-only">

    <div class="absolute inset-x-0 top-0 bottom-[92px]">
      <div class="invisible absolute inset-0 translate-y-3 overflow-y-auto px-6 pt-8 pb-4 opacity-0 transition duration-300 group-has-[#tmn-16-t1:checked]:visible group-has-[#tmn-16-t1:checked]:translate-y-0 group-has-[#tmn-16-t1:checked]:opacity-100">
        <h2 class="text-[26px] font-bold tracking-[-0.02em]">Overview</h2>
        <p class="mb-6 text-[13px] text-tmn16-mut">Good morning, Taylor</p>
        <dl class="mb-4 grid grid-cols-3 gap-3 text-center">
          <div class="rounded-2xl bg-tmn16-bg px-2 py-3.5 shadow-tmn16-up-sm"><dd class="text-xl font-bold">7.4k</dd><dt class="text-[11px] text-tmn16-mut">Steps</dt></div>
          <div class="rounded-2xl bg-tmn16-bg px-2 py-3.5 shadow-tmn16-up-sm"><dd class="text-xl font-bold">420</dd><dt class="text-[11px] text-tmn16-mut">Calories</dt></div>
          <div class="rounded-2xl bg-tmn16-bg px-2 py-3.5 shadow-tmn16-up-sm"><dd class="text-xl font-bold">6.5h</dd><dt class="text-[11px] text-tmn16-mut">Sleep</dt></div>
        </dl>
        <div class="mb-4 flex items-center gap-4 rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up">
          <span class="relative grid size-16 flex-none place-items-center rounded-full bg-[conic-gradient(var(--color-tmn16-acc)_0_74%,transparent_74%)] p-1.5 shadow-tmn16-in-sm"><span class="grid size-full place-items-center rounded-full bg-tmn16-bg text-sm font-bold">74%</span></span>
          <div><h3 class="mb-1 text-sm font-semibold">Daily goal</h3><p class="text-xs leading-relaxed text-tmn16-mut">Keep going &mdash; 2,600 steps to go.</p></div>
        </div>
        <div class="rounded-2xl bg-tmn16-bg p-4 shadow-tmn16-in">
          <h3 class="mb-2.5 text-[13px] font-semibold">Steps progress</h3>
          <div class="mb-1.5 h-2 overflow-hidden rounded-full shadow-tmn16-in-sm"><div class="h-full w-[74%] rounded-full bg-linear-to-r from-tmn16-acc to-tmn16-acc3"></div></div>
          <p class="flex justify-between text-[11px] text-tmn16-mut"><span>7,400 steps</span><span>10,000</span></p>
        </div>
      </div>

      <div class="invisible absolute inset-0 translate-y-3 overflow-y-auto px-6 pt-8 pb-4 opacity-0 transition duration-300 group-has-[#tmn-16-t2:checked]:visible group-has-[#tmn-16-t2:checked]:translate-y-0 group-has-[#tmn-16-t2:checked]:opacity-100">
        <h2 class="text-[26px] font-bold tracking-[-0.02em]">Workouts</h2>
        <p class="mb-6 text-[13px] text-tmn16-mut">This week's activity</p>
        <div class="mb-4 flex gap-3">
          <button type="button" class="grid size-13 place-items-center rounded-2xl bg-tmn16-bg text-tmn16-acc2 shadow-tmn16-up-sm transition-shadow active:shadow-tmn16-in-sm"><span class="sr-only">Run</span><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><circle cx="14" cy="4" r="2"/><path d="m6 20 3-5 3 2 2-6 4 3M9 11l3-3 3 1"/></svg></button>
          <button type="button" class="grid size-13 place-items-center rounded-2xl bg-tmn16-bg text-tmn16-acc2 shadow-tmn16-up-sm transition-shadow active:shadow-tmn16-in-sm"><span class="sr-only">Cycle</span><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="18.5" cy="17.5" r="3.5"/><path d="M15 6h2l3 11.5M5.5 17.5 9 9h6l-3 8.5"/></svg></button>
          <button type="button" class="grid size-13 place-items-center rounded-2xl bg-tmn16-bg text-tmn16-acc2 shadow-tmn16-up-sm transition-shadow active:shadow-tmn16-in-sm"><span class="sr-only">Swim</span><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M2 18c2 1.3 4 1.3 6 0s4-1.3 6 0 4 1.3 6 0M2 13c2 1.3 4 1.3 6 0s4-1.3 6 0 4 1.3 6 0"/><circle cx="16" cy="6" r="2"/></svg></button>
          <button type="button" class="grid size-13 place-items-center rounded-2xl bg-tmn16-bg text-tmn16-acc2 shadow-tmn16-up-sm transition-shadow active:shadow-tmn16-in-sm"><span class="sr-only">Yoga</span><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><circle cx="12" cy="4" r="2"/><path d="M4 11c3 1 5 1 8 1s5 0 8-1M12 12v4l-4 5M12 16l4 5"/></svg></button>
        </div>
        <div class="mb-3.5 rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up"><h3 class="mb-1 text-sm font-semibold">Morning run</h3><p class="text-xs text-tmn16-mut">5.2 km · 28 min · 310 kcal</p></div>
        <div class="rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up"><h3 class="mb-1 text-sm font-semibold">Strength training</h3><p class="text-xs text-tmn16-mut">45 min · Full body · 280 kcal</p></div>
      </div>

      <div class="invisible absolute inset-0 translate-y-3 overflow-y-auto px-6 pt-8 pb-4 opacity-0 transition duration-300 group-has-[#tmn-16-t3:checked]:visible group-has-[#tmn-16-t3:checked]:translate-y-0 group-has-[#tmn-16-t3:checked]:opacity-100">
        <h2 class="text-[26px] font-bold tracking-[-0.02em]">Nutrition</h2>
        <p class="mb-6 text-[13px] text-tmn16-mut">Today's intake</p>
        <div class="mb-4 rounded-2xl bg-tmn16-bg p-4 shadow-tmn16-in">
          <h3 class="mb-2.5 text-[13px] font-semibold">Calories</h3>
          <div class="mb-1.5 h-2 overflow-hidden rounded-full shadow-tmn16-in-sm"><div class="h-full w-3/5 rounded-full bg-linear-to-r from-tmn16-acc3 to-tmn16-acc"></div></div>
          <p class="flex justify-between text-[11px] text-tmn16-mut"><span>1,240 eaten</span><span>2,000 goal</span></p>
        </div>
        <div class="mb-3.5 rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up"><h3 class="mb-1 text-sm font-semibold">Protein · 68 g</h3><p class="text-xs text-tmn16-mut">Chicken, eggs, Greek yoghurt</p></div>
        <div class="rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up"><h3 class="mb-1 text-sm font-semibold">Carbs · 142 g</h3><p class="text-xs text-tmn16-mut">Oats, rice, banana</p></div>
      </div>

      <div class="invisible absolute inset-0 translate-y-3 overflow-y-auto px-6 pt-8 pb-4 opacity-0 transition duration-300 group-has-[#tmn-16-t4:checked]:visible group-has-[#tmn-16-t4:checked]:translate-y-0 group-has-[#tmn-16-t4:checked]:opacity-100">
        <h2 class="text-[26px] font-bold tracking-[-0.02em]">Profile</h2>
        <p class="mb-6 text-[13px] text-tmn16-mut">Your health data</p>
        <div class="mb-4 flex items-center gap-4 rounded-[20px] bg-tmn16-bg p-5 shadow-tmn16-up">
          <span class="grid size-13 place-items-center rounded-full bg-linear-135 from-tmn16-acc to-tmn16-acc3 text-base font-bold text-white shadow-tmn16-up-sm">TK</span>
          <div><h3 class="text-sm font-semibold">Taylor Kim</h3><p class="text-xs text-tmn16-mut">Premium · since 2022</p></div>
        </div>
        <div class="rounded-2xl bg-tmn16-bg p-4 shadow-tmn16-in">
          <h3 class="mb-3 text-[13px] font-semibold">Weekly streak · 5 of 7</h3>
          <ol class="grid grid-cols-7 gap-2 text-center text-[10px] text-tmn16-mut">
            <li><span class="mb-1 block h-8 rounded-lg bg-linear-135 from-tmn16-acc to-tmn16-acc3"></span>M</li>
            <li><span class="mb-1 block h-8 rounded-lg bg-linear-135 from-tmn16-acc to-tmn16-acc3"></span>T</li>
            <li><span class="mb-1 block h-8 rounded-lg bg-linear-135 from-tmn16-acc to-tmn16-acc3"></span>W</li>
            <li><span class="mb-1 block h-8 rounded-lg bg-linear-135 from-tmn16-acc to-tmn16-acc3 opacity-40"></span>T</li>
            <li><span class="mb-1 block h-8 rounded-lg bg-linear-135 from-tmn16-acc to-tmn16-acc3"></span>F</li>
            <li><span class="mb-1 block h-8 rounded-lg shadow-tmn16-in-sm"></span>S</li>
            <li><span class="mb-1 block h-8 rounded-lg shadow-tmn16-in-sm"></span>S</li>
          </ol>
        </div>
      </div>
    </div>

    <nav aria-label="Tabs" class="absolute inset-x-0 bottom-0 flex h-[92px] items-center justify-around bg-tmn16-bg px-3 pb-3 shadow-[0_-4px_20px_oklch(0.75_0.03_255/0.35)]">
      <label for="tmn-16-t1" class="flex min-h-14 min-w-16 cursor-pointer flex-col items-center justify-center gap-1 rounded-2xl text-tmn16-mut transition duration-200 group-has-[#tmn-16-t1:checked]:text-tmn16-acc group-has-[#tmn-16-t1:checked]:shadow-tmn16-in group-has-[#tmn-16-t1:focus-visible]:ring-2 group-has-[#tmn-16-t1:focus-visible]:ring-tmn16-acc/60"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg><span class="text-[10px] font-semibold">Home</span></label>
      <label for="tmn-16-t2" class="flex min-h-14 min-w-16 cursor-pointer flex-col items-center justify-center gap-1 rounded-2xl text-tmn16-mut transition duration-200 group-has-[#tmn-16-t2:checked]:text-tmn16-acc2 group-has-[#tmn-16-t2:checked]:shadow-tmn16-in group-has-[#tmn-16-t2:focus-visible]:ring-2 group-has-[#tmn-16-t2:focus-visible]:ring-tmn16-acc/60"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><span class="text-[10px] font-semibold">Workout</span></label>
      <label for="tmn-16-t3" class="flex min-h-14 min-w-16 cursor-pointer flex-col items-center justify-center gap-1 rounded-2xl text-tmn16-mut transition duration-200 group-has-[#tmn-16-t3:checked]:text-tmn16-acc3 group-has-[#tmn-16-t3:checked]:shadow-tmn16-in group-has-[#tmn-16-t3:focus-visible]:ring-2 group-has-[#tmn-16-t3:focus-visible]:ring-tmn16-acc/60"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><path d="M12 21a9 9 0 0 0 9-9H3a9 9 0 0 0 9 9zM7 12a5 5 0 0 1 10 0M12 7V3"/></svg><span class="text-[10px] font-semibold">Nutrition</span></label>
      <label for="tmn-16-t4" class="flex min-h-14 min-w-16 cursor-pointer flex-col items-center justify-center gap-1 rounded-2xl text-tmn16-mut transition duration-200 group-has-[#tmn-16-t4:checked]:text-tmn16-acc4 group-has-[#tmn-16-t4:checked]:shadow-tmn16-in group-has-[#tmn-16-t4:focus-visible]:ring-2 group-has-[#tmn-16-t4:focus-visible]:ring-tmn16-acc/60"><svg viewBox="0 0 24 24" class="size-5.5" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg><span class="text-[10px] font-semibold">Profile</span></label>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn16-stage: #cfd6e0;
  --color-tmn16-stage: oklch(0.87 0.015 255);
  --color-tmn16-bg: #e0e5ec;
  --color-tmn16-bg: oklch(0.92 0.012 255);
  --color-tmn16-light: #ffffffd9;
  --color-tmn16-light: oklch(1 0 0 / 0.85);
  --color-tmn16-dark: #a3b1c6b3;
  --color-tmn16-dark: oklch(0.75 0.035 258 / 0.7);
  --color-tmn16-ink: #2d3748;
  --color-tmn16-ink: oklch(0.33 0.03 260);
  --color-tmn16-mut: #5f6b7a;
  --color-tmn16-mut: oklch(0.51 0.025 255);
  --color-tmn16-acc: #3d63e0;
  --color-tmn16-acc: oklch(0.55 0.19 266);
  --color-tmn16-acc2: #d63f74;
  --color-tmn16-acc2: oklch(0.58 0.19 0);
  --color-tmn16-acc3: #12937a;
  --color-tmn16-acc3: oklch(0.58 0.11 172);
  --color-tmn16-acc4: #b8641a;
  --color-tmn16-acc4: oklch(0.58 0.13 60);
  --shadow-tmn16-up: 6px 6px 14px var(--color-tmn16-dark), -6px -6px 14px var(--color-tmn16-light);
  --shadow-tmn16-up-sm: 4px 4px 10px var(--color-tmn16-dark), -4px -4px 10px var(--color-tmn16-light);
  --shadow-tmn16-in: inset 4px 4px 10px var(--color-tmn16-dark), inset -4px -4px 10px var(--color-tmn16-light);
  --shadow-tmn16-in-sm: inset 2px 2px 5px var(--color-tmn16-dark), inset -2px -2px 5px var(--color-tmn16-light);
  --font-tmn16-sans: 'Lexend', system-ui, sans-serif;
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-16 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-16 {
  width: 100%;
  min-height: 100svh;
}
```
