---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/dark-tailwind-css-accordion-aurora-glow/"
title: "Dark Tailwind CSS Accordion with Aurora Glow"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A night-mode wind-down screen for a sleep app: a slow aurora drifts behind frosted session cards, and when you open one the light gathers around it — a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Tailwind CSS Accordion with Aurora Glow
Source: https://codefronts.com/navigation/tailwind-css-accordions/dark-tailwind-css-accordion-aurora-glow/

A night-mode wind-down screen for a sleep app: a slow aurora drifts behind frosted session cards, and when you open one the light gathers around it — a per-item halo in that session's own hue blooms from scale-50 to full through the glass while the card lifts. The halo is driven by has-[[open]]: on each item wrapper, so the glow "follows" the open item with no position tracking.
## HTML
```html
<section class="tac-24 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tac24-bg px-4 py-16 font-tac24-sans text-tac24-ink [interpolate-size:allow-keywords]" aria-label="Dark accordion with aurora glow demo">
  <div aria-hidden="true" class="pointer-events-none absolute -left-[20%] -top-[25%] -z-10 size-[min(70rem,140vw)] animate-tac24-drift-a rounded-full bg-[radial-gradient(closest-side,var(--color-tac24-aur1),transparent)] opacity-70 blur-3xl motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute -right-[25%] -bottom-[30%] -z-10 size-[min(64rem,130vw)] animate-tac24-drift-b rounded-full bg-[radial-gradient(closest-side,var(--color-tac24-aur2),transparent)] opacity-60 blur-3xl motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(1px_1px_at_12%_18%,oklch(1_0_0/0.7),transparent),radial-gradient(1px_1px_at_78%_12%,oklch(1_0_0/0.6),transparent),radial-gradient(1.5px_1.5px_at_64%_34%,oklch(1_0_0/0.5),transparent),radial-gradient(1px_1px_at_30%_72%,oklch(1_0_0/0.45),transparent),radial-gradient(1px_1px_at_88%_64%,oklch(1_0_0/0.5),transparent),radial-gradient(1.5px_1.5px_at_8%_88%,oklch(1_0_0/0.4),transparent)]"></div>

  <div class="grid w-full max-w-xl gap-8">
    <header class="flex items-start justify-between gap-4 px-1">
      <div>
        <p class="font-tac24-mono text-[11.5px] tracking-[0.14em] uppercase text-tac24-mut">Tonight · 10:42 pm</p>
        <h2 class="mt-2 font-tac24-serif text-[clamp(34px,6vw,46px)] leading-[1.02] tracking-[-0.01em]">Good evening, <em class="text-tac24-glow">Maya</em></h2>
        <p class="mt-2 text-[15px] text-tac24-mut">Your wind-down · 4 sessions · <span class="whitespace-nowrap">about 1 hr 30 min</span></p>
      </div>
      <svg class="mt-1 size-11 flex-none text-tac24-glow drop-shadow-[0_0_14px_var(--color-tac24-a1)]" viewBox="0 0 44 44" aria-hidden="true"><path d="M30 8a15 15 0 1 0 6 26A13 13 0 0 1 30 8Z" fill="currentColor" opacity="0.92"/><circle cx="35" cy="12" r="1.3" fill="currentColor"/><circle cx="39" cy="20" r="0.9" fill="currentColor"/></svg>
    </header>

    <div class="isolate grid gap-3.5">
      <div class="relative transition-[translate] duration-700 ease-[cubic-bezier(0.2,0.7,0.2,1)] before:pointer-events-none before:absolute before:-inset-8 before:-z-10 before:scale-50 before:rounded-[44px] before:bg-[radial-gradient(closest-side,var(--color-tac24-a1),transparent)] before:opacity-0 before:blur-2xl before:transition-[scale,opacity] before:duration-[900ms] before:ease-[cubic-bezier(0.2,0.7,0.2,1)] has-[[open]]:-translate-y-0.5 has-[[open]]:before:scale-100 has-[[open]]:before:opacity-80 motion-reduce:transition-none motion-reduce:before:scale-100 motion-reduce:before:transition-opacity">
        <details name="tac24-session" class="group rounded-[22px] bg-tac24-card/90 ring-1 ring-white/10 transition-[background-color,box-shadow] duration-500 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl open:shadow-[0_20px_50px_-20px_oklch(0.1_0.05_280/0.8)] open:ring-white/20 supports-[backdrop-filter:blur(1px)]:open:bg-white/[0.08] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-700 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-[4.5rem] cursor-pointer list-none items-center gap-4 rounded-[22px] px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac24-glow sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-2xl bg-white/[0.06] text-tac24-a1 ring-1 ring-white/10 transition-shadow duration-500 group-open:shadow-[0_0_24px_-4px_var(--color-tac24-a1)]">
              <svg class="size-5" viewBox="0 0 20 20" aria-hidden="true"><path d="M3 8h9.5a2.5 2.5 0 1 0-2.5-2.5M3 12h12a2.5 2.5 0 1 1-2.5 2.5M3 10h6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[16px] font-semibold tracking-[-0.01em]">4-7-8 Breathing</span>
              <span class="mt-0.5 block text-[13px] text-tac24-mut">Breathwork · Guided</span>
            </span>
            <span class="font-tac24-mono text-[12.5px] text-tac24-mut">5 min</span>
            <svg class="size-4 flex-none text-tac24-mut transition-transform duration-500 group-open:rotate-180 group-open:text-tac24-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-[1.7] text-tac24-soft text-pretty">Inhale for four, hold for seven, exhale for eight. Four rounds slow your heart rate and signal to your nervous system that the day is over.</p>
            <div class="mt-4 flex items-center gap-1.5" aria-hidden="true">
              <span class="h-1.5 flex-[4] rounded-full bg-tac24-a1"></span><span class="h-1.5 flex-[7] rounded-full bg-tac24-a1/45"></span><span class="h-1.5 flex-[8] rounded-full bg-tac24-a1/20"></span>
            </div>
            <p class="mt-2 flex justify-between font-tac24-mono text-[11.5px] text-tac24-mut"><span>Inhale 4</span><span>Hold 7</span><span>Exhale 8</span></p>
          </div>
        </details>
      </div>

      <div class="relative transition-[translate] duration-700 ease-[cubic-bezier(0.2,0.7,0.2,1)] before:pointer-events-none before:absolute before:-inset-8 before:-z-10 before:scale-50 before:rounded-[44px] before:bg-[radial-gradient(closest-side,var(--color-tac24-a2),transparent)] before:opacity-0 before:blur-2xl before:transition-[scale,opacity] before:duration-[900ms] before:ease-[cubic-bezier(0.2,0.7,0.2,1)] has-[[open]]:-translate-y-0.5 has-[[open]]:before:scale-100 has-[[open]]:before:opacity-80 motion-reduce:transition-none motion-reduce:before:scale-100 motion-reduce:before:transition-opacity">
        <details name="tac24-session" class="group rounded-[22px] bg-tac24-card/90 ring-1 ring-white/10 transition-[background-color,box-shadow] duration-500 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl open:shadow-[0_20px_50px_-20px_oklch(0.1_0.05_280/0.8)] open:ring-white/20 supports-[backdrop-filter:blur(1px)]:open:bg-white/[0.08] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-700 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[4.5rem] cursor-pointer list-none items-center gap-4 rounded-[22px] px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac24-glow sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-2xl bg-white/[0.06] text-tac24-a2 ring-1 ring-white/10 transition-shadow duration-500 group-open:shadow-[0_0_24px_-4px_var(--color-tac24-a2)]">
              <svg class="size-5" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="4.5" r="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 7.5v6M6 9.5l4-1 4 1M7.5 18l2.5-4.5 2.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[16px] font-semibold tracking-[-0.01em]">Body Scan for Sleep</span>
              <span class="mt-0.5 block text-[13px] text-tac24-mut">Meditation · Narrated by Ines Calloway</span>
            </span>
            <span class="font-tac24-mono text-[12.5px] text-tac24-mut">12 min</span>
            <svg class="size-4 flex-none text-tac24-mut transition-transform duration-500 group-open:rotate-180 group-open:text-tac24-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-[1.7] text-tac24-soft text-pretty">A slow sweep of attention from the crown of your head to your toes, releasing each muscle group in turn. Most listeners are asleep before the narrator reaches the knees.</p>
            <ul class="mt-4 flex flex-wrap gap-2 font-tac24-mono text-[11.5px] text-tac24-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">No music</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Fades to silence</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Played 38×</li>
            </ul>
          </div>
        </details>
      </div>

      <div class="relative transition-[translate] duration-700 ease-[cubic-bezier(0.2,0.7,0.2,1)] before:pointer-events-none before:absolute before:-inset-8 before:-z-10 before:scale-50 before:rounded-[44px] before:bg-[radial-gradient(closest-side,var(--color-tac24-a3),transparent)] before:opacity-0 before:blur-2xl before:transition-[scale,opacity] before:duration-[900ms] before:ease-[cubic-bezier(0.2,0.7,0.2,1)] has-[[open]]:-translate-y-0.5 has-[[open]]:before:scale-100 has-[[open]]:before:opacity-80 motion-reduce:transition-none motion-reduce:before:scale-100 motion-reduce:before:transition-opacity">
        <details name="tac24-session" class="group rounded-[22px] bg-tac24-card/90 ring-1 ring-white/10 transition-[background-color,box-shadow] duration-500 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl open:shadow-[0_20px_50px_-20px_oklch(0.1_0.05_280/0.8)] open:ring-white/20 supports-[backdrop-filter:blur(1px)]:open:bg-white/[0.08] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-700 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[4.5rem] cursor-pointer list-none items-center gap-4 rounded-[22px] px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac24-glow sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-2xl bg-white/[0.06] text-tac24-a3 ring-1 ring-white/10 transition-shadow duration-500 group-open:shadow-[0_0_24px_-4px_var(--color-tac24-a3)]">
              <svg class="size-5" viewBox="0 0 20 20" aria-hidden="true"><path d="M5.5 10.5a3.5 3.5 0 0 1 .4-7 4.5 4.5 0 0 1 8.6 1.2A3 3 0 0 1 14 10.5Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M6.5 13.5l-1 3M10 13.5l-1 3M13.5 13.5l-1 3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[16px] font-semibold tracking-[-0.01em]">Rain on a Tin Roof</span>
              <span class="mt-0.5 block text-[13px] text-tac24-mut">Soundscape · Recorded in Kyoto</span>
            </span>
            <span class="font-tac24-mono text-[12.5px] text-tac24-mut">45 min</span>
            <svg class="size-4 flex-none text-tac24-mut transition-transform duration-500 group-open:rotate-180 group-open:text-tac24-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-[1.7] text-tac24-soft text-pretty">Steady rain over a machiya roof, distant thunder every few minutes and nothing else. Mixed without loops, so your brain never learns the pattern and tunes back in.</p>
            <p class="mt-4 flex items-center gap-2 font-tac24-mono text-[11.5px] text-tac24-mut"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac24-a3 shadow-[0_0_10px_var(--color-tac24-a3)]"></span>Sleep timer · fades out at 45:00</p>
          </div>
        </details>
      </div>

      <div class="relative transition-[translate] duration-700 ease-[cubic-bezier(0.2,0.7,0.2,1)] before:pointer-events-none before:absolute before:-inset-8 before:-z-10 before:scale-50 before:rounded-[44px] before:bg-[radial-gradient(closest-side,var(--color-tac24-a4),transparent)] before:opacity-0 before:blur-2xl before:transition-[scale,opacity] before:duration-[900ms] before:ease-[cubic-bezier(0.2,0.7,0.2,1)] has-[[open]]:-translate-y-0.5 has-[[open]]:before:scale-100 has-[[open]]:before:opacity-80 motion-reduce:transition-none motion-reduce:before:scale-100 motion-reduce:before:transition-opacity">
        <details name="tac24-session" class="group rounded-[22px] bg-tac24-card/90 ring-1 ring-white/10 transition-[background-color,box-shadow] duration-500 supports-[backdrop-filter:blur(1px)]:bg-white/[0.05] supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl open:shadow-[0_20px_50px_-20px_oklch(0.1_0.05_280/0.8)] open:ring-white/20 supports-[backdrop-filter:blur(1px)]:open:bg-white/[0.08] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-700 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[4.5rem] cursor-pointer list-none items-center gap-4 rounded-[22px] px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac24-glow sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-2xl bg-white/[0.06] text-tac24-a4 ring-1 ring-white/10 transition-shadow duration-500 group-open:shadow-[0_0_24px_-4px_var(--color-tac24-a4)]">
              <svg class="size-5" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 5.5C8.5 4.2 6 3.8 3 4.2v11c3-.4 5.5 0 7 1.3 1.5-1.3 4-1.7 7-1.3v-11c-3-.4-5.5 0-7 1.3Zm0 0v11" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[16px] font-semibold tracking-[-0.01em]">The Lighthouse Keeper</span>
              <span class="mt-0.5 block text-[13px] text-tac24-mut">Sleep story · Read by Tomas Adeyemi</span>
            </span>
            <span class="font-tac24-mono text-[12.5px] text-tac24-mut">28 min</span>
            <svg class="size-4 flex-none text-tac24-mut transition-transform duration-500 group-open:rotate-180 group-open:text-tac24-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-[1.7] text-tac24-soft text-pretty">On a quiet island off the Hebrides, an old keeper winds the lamp one last time before the light goes automatic. Gentle, slow and deliberately uneventful.</p>
            <p class="mt-4 font-tac24-serif text-[17px] italic text-tac24-soft">“The sea had nothing left to say, so it said it softly.”</p>
          </div>
        </details>
      </div>
    </div>

    <p aria-hidden="true" class="mx-auto max-w-full rounded-full bg-white/[0.04] px-3.5 py-2 text-center font-tac24-mono text-[11.5px] text-tac24-mut ring-1 ring-white/10">has-[[open]]:before:scale-100 · backdrop-blur-xl · animate-tac24-drift-a</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac24-bg: #0b0a24;
  --color-tac24-bg: oklch(0.17 0.06 280);
  --color-tac24-card: #1a1840;
  --color-tac24-card: oklch(0.24 0.07 280);
  --color-tac24-aur1: #2f8f8ab3;
  --color-tac24-aur1: oklch(0.58 0.1 190 / 0.7);
  --color-tac24-aur2: #6a3fc2b3;
  --color-tac24-aur2: oklch(0.5 0.18 295 / 0.7);
  --color-tac24-ink: #f2f0ff;
  --color-tac24-ink: oklch(0.96 0.015 290);
  --color-tac24-soft: #d4d0ee;
  --color-tac24-soft: oklch(0.87 0.03 290);
  --color-tac24-mut: #aaa5d0;
  --color-tac24-mut: oklch(0.76 0.045 290);
  --color-tac24-glow: #b6f0e4;
  --color-tac24-glow: oklch(0.91 0.07 180);
  --color-tac24-a1: #5ee6d0;
  --color-tac24-a1: oklch(0.84 0.13 180);
  --color-tac24-a2: #b394ff;
  --color-tac24-a2: oklch(0.74 0.16 295);
  --color-tac24-a3: #7cc4ff;
  --color-tac24-a3: oklch(0.79 0.12 245);
  --color-tac24-a4: #ff9ec7;
  --color-tac24-a4: oklch(0.8 0.13 355);
  --font-tac24-serif: 'Instrument Serif', Georgia, serif;
  --font-tac24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tac24-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tac24-drift-a: tac24-drift-a 26s ease-in-out infinite alternate;
  --animate-tac24-drift-b: tac24-drift-b 19s ease-in-out infinite alternate;

  @keyframes tac24-drift-a {
    from {
      translate: 0 0;
      scale: 1;
    }

    to {
      translate: 18% 14%;
      scale: 1.15;
    }
  }

  @keyframes tac24-drift-b {
    from {
      translate: 0 0;
      scale: 1.1;
    }

    to {
      translate: -16% -12%;
      scale: 0.92;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-24 {
  width: 100%;
  min-height: 100svh;
}
```
