---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-aurora-gradient-horizontal-accordion/"
title: "Tailwind CSS Aurora Gradient Horizontal Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Dark glass columns over one living aurora: a registered @property --tac32-hue cycles the whole palette through oklch(…&nbsp;var(--tac32-hue)) gradients,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Aurora Gradient Horizontal Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-aurora-gradient-horizontal-accordion/

Dark glass columns over one living aurora: a registered @property --tac32-hue cycles the whole palette through oklch(…&nbsp;var(--tac32-hue)) gradients, collapsed strips dim it to slits, and the chosen panel's glass clears (has-checked:bg-tac32-glass/20) to open a window onto it. Because the hue animates on the stage and inherits, every accent — status dots, the panel's top hairline, the icon tint — drifts in sync with the sky behind it. Stacks to a vertical list below lg.
## HTML
```html
<section class="tac-32 w-full min-h-svh grid place-items-center bg-tac32-bg px-5 py-14 font-tac32-sans text-white" aria-label="Aurora gradient horizontal accordion demo">
  <div class="grid w-full max-w-5xl justify-items-center gap-8">
    <header class="grid w-full justify-items-center gap-3 text-center">
      <p class="rounded-full bg-white/6 px-3 py-1.5 font-tac32-mono text-[11.5px] tracking-[0.16em] text-white/75 uppercase ring-1 ring-white/12">Lumen OS · Design principles</p>
      <h2 class="max-w-[18ch] text-[clamp(32px,5vw,52px)] leading-[1.02] font-bold tracking-[-0.035em] text-balance">Software that behaves like <span class="bg-linear-to-r from-[#9ad8ff] via-[#c7a6ff] to-[#7ff0c8] bg-clip-text text-transparent">weather</span>.</h2>
      <p class="max-w-md text-[15px] leading-[1.6] text-white/70 text-balance">Four rules every Lumen screen is reviewed against before it ships.</p>
    </header>
    <div class="relative isolate flex w-full animate-tac32-cycle flex-col gap-2 overflow-hidden rounded-[28px] bg-tac32-stage p-2.5 shadow-[0_40px_90px_-40px_oklch(0.5_0.2_280/0.6)] ring-1 ring-white/10 lg:h-[27rem] lg:flex-row motion-reduce:animate-none" role="radiogroup" aria-label="Product principles">
      <div aria-hidden="true" class="pointer-events-none absolute -inset-[30%] -z-10 [background:radial-gradient(50%_60%_at_25%_30%,oklch(0.72_0.19_var(--tac32-hue)/0.8),transparent_70%),radial-gradient(45%_55%_at_75%_40%,oklch(0.7_0.18_calc(var(--tac32-hue)_+_80)/0.7),transparent_70%),radial-gradient(60%_50%_at_50%_85%,oklch(0.65_0.2_calc(var(--tac32-hue)_+_160)/0.65),transparent_70%)]">
        <span class="absolute inset-0 animate-tac32-shimmer bg-[linear-gradient(115deg,transparent_35%,rgb(255_255_255/.08)_50%,transparent_65%)] motion-reduce:animate-none"></span>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-2xl bg-tac32-glass/75 ring-1 ring-white/12 transition-[height,flex-grow,background-color,box-shadow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] ring-inset hover:ring-white/30 has-checked:h-[21rem] has-checked:bg-tac32-glass/20 has-checked:ring-white/30 has-focus-visible:ring-2 has-focus-visible:ring-white sm:has-checked:h-[17rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[5] motion-reduce:transition-none">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 transition-opacity duration-300 group-has-checked:pointer-events-none group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac32-principle" id="tac32-a" class="sr-only" checked>
          <span class="font-tac32-mono text-[11px] text-white/70">01</span>
          <span class="flex-1 text-[13px] font-semibold tracking-[0.18em] text-white/85 uppercase lg:flex-none lg:rotate-180 lg:[writing-mode:vertical-rl]">Calm</span>
          <span aria-hidden="true" class="size-2 rounded-full bg-[oklch(0.8_0.15_calc(var(--tac32-hue)_+_0))] shadow-[0_0_12px_oklch(0.8_0.15_calc(var(--tac32-hue)_+_0))]"></span>
        </label>
        <div class="invisible absolute inset-0 flex flex-col justify-end opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,30rem)] motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute inset-x-6 top-0 h-px bg-linear-to-r from-transparent via-[oklch(0.85_0.12_calc(var(--tac32-hue)_+_0))] to-transparent"></span>
          <div class="flex translate-y-3 flex-col gap-3 bg-linear-to-t from-tac32-scrim/85 via-tac32-scrim/45 via-55% to-transparent p-6 pt-16 transition-transform duration-500 group-has-checked:translate-y-0 group-has-checked:delay-200 sm:p-7 sm:pt-20 motion-reduce:translate-y-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="grid size-11 place-items-center rounded-xl bg-white/10 text-[oklch(0.9_0.1_calc(var(--tac32-hue)_+_0))] ring-1 ring-white/20 backdrop-blur-md"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15c2.5-4 5.5-4 8 0s5.5 4 8 0" /><path d="M4 9c2.5-4 5.5-4 8 0s5.5 4 8 0" opacity="0.5"/></svg></span>
            <h3 class="text-[clamp(22px,2.6vw,28px)] leading-tight font-bold tracking-[-0.02em] text-white">Calm by default</h3>
            <p class="max-w-[44ch] text-[14.5px] leading-[1.6] text-white/80 text-pretty">No badges, no streaks, no red dots. The interface waits for you — never the other way around.</p>
            <dl class="mt-1 flex flex-wrap gap-x-6 gap-y-2 border-t border-white/12 pt-3">
              <div class="flex items-baseline gap-2"><dt class="sr-only">notification badges</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">0</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">notification badges</span></div>
              <div class="flex items-baseline gap-2"><dt class="sr-only">daily digest, opt-in</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">1</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">daily digest, opt-in</span></div>
            </dl>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-2xl bg-tac32-glass/75 ring-1 ring-white/12 transition-[height,flex-grow,background-color,box-shadow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] ring-inset hover:ring-white/30 has-checked:h-[21rem] has-checked:bg-tac32-glass/20 has-checked:ring-white/30 has-focus-visible:ring-2 has-focus-visible:ring-white sm:has-checked:h-[17rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[5] motion-reduce:transition-none">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 transition-opacity duration-300 group-has-checked:pointer-events-none group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac32-principle" id="tac32-b" class="sr-only">
          <span class="font-tac32-mono text-[11px] text-white/70">02</span>
          <span class="flex-1 text-[13px] font-semibold tracking-[0.18em] text-white/85 uppercase lg:flex-none lg:rotate-180 lg:[writing-mode:vertical-rl]">Ambient</span>
          <span aria-hidden="true" class="size-2 rounded-full bg-[oklch(0.8_0.15_calc(var(--tac32-hue)_+_80))] shadow-[0_0_12px_oklch(0.8_0.15_calc(var(--tac32-hue)_+_80))]"></span>
        </label>
        <div class="invisible absolute inset-0 flex flex-col justify-end opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,30rem)] motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute inset-x-6 top-0 h-px bg-linear-to-r from-transparent via-[oklch(0.85_0.12_calc(var(--tac32-hue)_+_80))] to-transparent"></span>
          <div class="flex translate-y-3 flex-col gap-3 bg-linear-to-t from-tac32-scrim/85 via-tac32-scrim/45 via-55% to-transparent p-6 pt-16 transition-transform duration-500 group-has-checked:translate-y-0 group-has-checked:delay-200 sm:p-7 sm:pt-20 motion-reduce:translate-y-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="grid size-11 place-items-center rounded-xl bg-white/10 text-[oklch(0.9_0.1_calc(var(--tac32-hue)_+_80))] ring-1 ring-white/20 backdrop-blur-md"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.5"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"/></svg></span>
            <h3 class="text-[clamp(22px,2.6vw,28px)] leading-tight font-bold tracking-[-0.02em] text-white">Ambient awareness</h3>
            <p class="max-w-[44ch] text-[14.5px] leading-[1.6] text-white/80 text-pretty">State lives in colour and light, not counters. You sense change peripherally, the way you notice weather.</p>
            <dl class="mt-1 flex flex-wrap gap-x-6 gap-y-2 border-t border-white/12 pt-3">
              <div class="flex items-baseline gap-2"><dt class="sr-only">status hues</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">12</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">status hues</span></div>
              <div class="flex items-baseline gap-2"><dt class="sr-only">pop-ups</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">0</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">pop-ups</span></div>
            </dl>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-2xl bg-tac32-glass/75 ring-1 ring-white/12 transition-[height,flex-grow,background-color,box-shadow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] ring-inset hover:ring-white/30 has-checked:h-[21rem] has-checked:bg-tac32-glass/20 has-checked:ring-white/30 has-focus-visible:ring-2 has-focus-visible:ring-white sm:has-checked:h-[17rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[5] motion-reduce:transition-none">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 transition-opacity duration-300 group-has-checked:pointer-events-none group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac32-principle" id="tac32-c" class="sr-only">
          <span class="font-tac32-mono text-[11px] text-white/70">03</span>
          <span class="flex-1 text-[13px] font-semibold tracking-[0.18em] text-white/85 uppercase lg:flex-none lg:rotate-180 lg:[writing-mode:vertical-rl]">Yours</span>
          <span aria-hidden="true" class="size-2 rounded-full bg-[oklch(0.8_0.15_calc(var(--tac32-hue)_+_160))] shadow-[0_0_12px_oklch(0.8_0.15_calc(var(--tac32-hue)_+_160))]"></span>
        </label>
        <div class="invisible absolute inset-0 flex flex-col justify-end opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,30rem)] motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute inset-x-6 top-0 h-px bg-linear-to-r from-transparent via-[oklch(0.85_0.12_calc(var(--tac32-hue)_+_160))] to-transparent"></span>
          <div class="flex translate-y-3 flex-col gap-3 bg-linear-to-t from-tac32-scrim/85 via-tac32-scrim/45 via-55% to-transparent p-6 pt-16 transition-transform duration-500 group-has-checked:translate-y-0 group-has-checked:delay-200 sm:p-7 sm:pt-20 motion-reduce:translate-y-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="grid size-11 place-items-center rounded-xl bg-white/10 text-[oklch(0.9_0.1_calc(var(--tac32-hue)_+_160))] ring-1 ring-white/20 backdrop-blur-md"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="4" width="15" height="16" rx="2.5"/><path d="M8.5 9h7M8.5 12.5h7M8.5 16h4"/></svg></span>
            <h3 class="text-[clamp(22px,2.6vw,28px)] leading-tight font-bold tracking-[-0.02em] text-white">Yours to keep</h3>
            <p class="max-w-[44ch] text-[14.5px] leading-[1.6] text-white/80 text-pretty">Local-first files, open formats, and an export button that produces something genuinely useful elsewhere.</p>
            <dl class="mt-1 flex flex-wrap gap-x-6 gap-y-2 border-t border-white/12 pt-3">
              <div class="flex items-baseline gap-2"><dt class="sr-only">offline capable</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">100%</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">offline capable</span></div>
              <div class="flex items-baseline gap-2"><dt class="sr-only">native format</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">.md</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">native format</span></div>
            </dl>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-2xl bg-tac32-glass/75 ring-1 ring-white/12 transition-[height,flex-grow,background-color,box-shadow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] ring-inset hover:ring-white/30 has-checked:h-[21rem] has-checked:bg-tac32-glass/20 has-checked:ring-white/30 has-focus-visible:ring-2 has-focus-visible:ring-white sm:has-checked:h-[17rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[5] motion-reduce:transition-none">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-4 px-5 transition-opacity duration-300 group-has-checked:pointer-events-none group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-6 motion-reduce:transition-none">
          <input type="radio" name="tac32-principle" id="tac32-d" class="sr-only">
          <span class="font-tac32-mono text-[11px] text-white/70">04</span>
          <span class="flex-1 text-[13px] font-semibold tracking-[0.18em] text-white/85 uppercase lg:flex-none lg:rotate-180 lg:[writing-mode:vertical-rl]">Quick</span>
          <span aria-hidden="true" class="size-2 rounded-full bg-[oklch(0.8_0.15_calc(var(--tac32-hue)_+_240))] shadow-[0_0_12px_oklch(0.8_0.15_calc(var(--tac32-hue)_+_240))]"></span>
        </label>
        <div class="invisible absolute inset-0 flex flex-col justify-end opacity-0 transition-[opacity,visibility] duration-200 group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 lg:right-auto lg:w-[max(100%,30rem)] motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute inset-x-6 top-0 h-px bg-linear-to-r from-transparent via-[oklch(0.85_0.12_calc(var(--tac32-hue)_+_240))] to-transparent"></span>
          <div class="flex translate-y-3 flex-col gap-3 bg-linear-to-t from-tac32-scrim/85 via-tac32-scrim/45 via-55% to-transparent p-6 pt-16 transition-transform duration-500 group-has-checked:translate-y-0 group-has-checked:delay-200 sm:p-7 sm:pt-20 motion-reduce:translate-y-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="grid size-11 place-items-center rounded-xl bg-white/10 text-[oklch(0.9_0.1_calc(var(--tac32-hue)_+_240))] ring-1 ring-white/20 backdrop-blur-md"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3 5 13.5h6L10 21l8-10.5h-6z"/></svg></span>
            <h3 class="text-[clamp(22px,2.6vw,28px)] leading-tight font-bold tracking-[-0.02em] text-white">Quick on purpose</h3>
            <p class="max-w-[44ch] text-[14.5px] leading-[1.6] text-white/80 text-pretty">Every interaction answers inside 100 milliseconds. Nothing spins while it waits on a server it never needed.</p>
            <dl class="mt-1 flex flex-wrap gap-x-6 gap-y-2 border-t border-white/12 pt-3">
              <div class="flex items-baseline gap-2"><dt class="sr-only">input to paint</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">&lt;100ms</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">input to paint</span></div>
              <div class="flex items-baseline gap-2"><dt class="sr-only">loading spinners</dt><dd class="font-tac32-mono text-[15px] font-semibold text-white">0</dd><span aria-hidden="true" class="text-[12.5px] text-white/70">loading spinners</span></div>
            </dl>
          </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-tac32-mono text-[11.5px] text-white/70">@property --tac32-hue · oklch(…_var(--tac32-hue)) · has-checked:bg-tac32-glass/20</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac32-bg: #070913;
  --color-tac32-bg: oklch(0.14 0.02 275);
  --color-tac32-stage: #0d1020;
  --color-tac32-stage: oklch(0.18 0.03 275);
  --color-tac32-glass: #080a16;
  --color-tac32-glass: oklch(0.15 0.025 275);
  --color-tac32-scrim: #05060e;
  --color-tac32-scrim: oklch(0.12 0.02 275);
  --font-tac32-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tac32-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tac32-cycle: tac32-cycle 24s linear infinite;
  --animate-tac32-shimmer: tac32-shimmer 9s ease-in-out infinite alternate;

  @keyframes tac32-cycle {
    to {
      --tac32-hue: 570;
    }
  }

  @keyframes tac32-shimmer {
    from {
      translate: -12% -6%;
    }

    to {
      translate: 12% 6%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-32 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the hue interpolates; inherits:true lets every accent in the stage read the live value. */

@property --tac32-hue {
  syntax: '<number>';
  inherits: true;
  initial-value: 210;
}
```
