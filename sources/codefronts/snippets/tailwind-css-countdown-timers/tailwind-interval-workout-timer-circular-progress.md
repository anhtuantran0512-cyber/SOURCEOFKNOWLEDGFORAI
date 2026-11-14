---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-interval-workout-timer-circular-progress/"
title: "Tailwind Interval Workout Timer with Circular Progress"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "An interval session timer with a depleting ring, Work and Rest phases and a play/pause control that runs entirely on CSS: one checkbox and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Interval Workout Timer with Circular Progress
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-interval-workout-timer-circular-progress/

An interval session timer with a depleting ring, Work and Rest phases and a play/pause control that runs entirely on CSS: one checkbox and has-checked:**:[animation-play-state:paused] freeze the ring, digits and phase label in the same frame. New in the port: a looping 60s work / 30s rest cycle with phase-coloured ring, an interval progress strip, and a single-integer clock printed with decimal-leading-zero.
## HTML
```html
<section class="tcd-21 group/root w-full min-h-svh grid place-items-center bg-tcd21-page px-5 py-12 font-tcd21-sans text-tcd21-ink antialiased has-checked:**:[animation-play-state:paused]" aria-labelledby="tcd-21-title">
  <div class="grid w-full max-w-[560px] justify-items-center gap-7 text-center">
    <header class="grid justify-items-center gap-1.5">
      <p class="text-[11px] font-extrabold uppercase tracking-[0.2em] text-tcd21-work-ink">Talon Train</p>
      <h2 id="tcd-21-title" class="text-[clamp(20px,4vw,26px)] font-extrabold tracking-[-0.01em]">Interval 3 of 8 · lower body</h2>
      <ol aria-hidden="true" class="mt-2 flex gap-1.5"><li class="h-1.5 w-6 rounded-full bg-tcd21-ink"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-ink"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-work"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-shade"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-shade"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-shade"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-shade"></li><li class="h-1.5 w-6 rounded-full bg-tcd21-shade"></li></ol>
    </header>

    <input type="checkbox" id="tcd-21-pause" class="peer sr-only">
    <div role="timer" aria-label="Interval timer, sixty seconds work then thirty seconds rest" class="relative aspect-square w-[clamp(230px,62vw,330px)] rounded-full bg-tcd21-card shadow-[0_30px_60px_-30px_rgb(43_22_32/0.45),inset_0_0_0_1px_var(--color-tcd21-shade)]">
      <span aria-hidden="true" class="absolute inset-[6%] rounded-full bg-tcd21-work/15 animate-tcd21-halo motion-reduce:animate-none"></span>
      <svg viewBox="0 0 120 120" aria-hidden="true" class="relative size-full -rotate-90">
        <circle cx="60" cy="60" r="51" pathLength="100" class="fill-none stroke-tcd21-shade [stroke-width:10]"/>
        <circle cx="60" cy="60" r="51" pathLength="100" class="fill-none stroke-tcd21-work [stroke-dasharray:100] [stroke-linecap:round] [stroke-width:10] animate-tcd21-arc"/>
      </svg>
      <div class="absolute inset-0 grid place-content-center justify-items-center gap-1">
        <p aria-hidden="true" class="relative grid text-[12px] font-black uppercase tracking-[0.24em]"><span class="col-start-1 row-start-1 text-tcd21-work-ink animate-tcd21-work">Work</span><span class="col-start-1 row-start-1 text-tcd21-rest opacity-0 animate-tcd21-rest">Rest</span></p>
        <p aria-hidden="true" class="text-[clamp(52px,15vw,76px)] font-black leading-none tracking-[-0.03em] tabular-nums">0:<em class="not-italic animate-tcd21-t [counter-reset:tcd21t_var(--tcd21-t)] before:content-[counter(tcd21t,decimal-leading-zero)]"></em></p>
        <p class="text-[12px] font-bold text-tcd21-mut">work <time datetime="PT1M">1:00</time> · rest <time datetime="PT30S">0:30</time></p>
      </div>
    </div>

    <label for="tcd-21-pause" class="inline-flex min-h-12 cursor-pointer items-center gap-2.5 rounded-full bg-tcd21-ink px-6 text-[15px] font-extrabold text-tcd21-card shadow-[0_12px_24px_-12px_rgb(43_22_32/0.6)] transition hover:brightness-125 active:scale-[0.97] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcd21-work">
      <svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" class="group-has-checked/root:hidden"><rect x="5" y="3.5" width="3.6" height="13" rx="1.2" fill="currentColor"/><rect x="11.4" y="3.5" width="3.6" height="13" rx="1.2" fill="currentColor"/></svg>
      <svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" class="hidden group-has-checked/root:block"><path d="M6 3.6 16 10 6 16.4V3.6Z" fill="currentColor"/></svg>
      <span class="group-has-checked/root:hidden">Pause interval</span><span class="hidden group-has-checked/root:inline">Resume interval</span>
    </label>

    <p class="max-w-[52ch] text-[12.5px] leading-relaxed text-tcd21-mut text-pretty">Pause is a checkbox and <code class="rounded bg-tcd21-shade/60 px-1 py-0.5 text-[11.5px] text-tcd21-ink">has-checked:**:[animation-play-state:paused]</code>, so the ring, digits and phase label freeze in the same frame. An interval is a duration, so measuring from render is correct here — cues and session logs would need script.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd21-t {
  syntax: '<integer>';
  inherits: false;
  initial-value: 59;
}

@theme {
  --color-tcd21-page: #f6ecea;
  --color-tcd21-page: oklch(0.94 0.02 30);
  --color-tcd21-card: #fdf5f3;
  --color-tcd21-card: oklch(0.97 0.014 30);
  --color-tcd21-ink: #2b1620;
  --color-tcd21-ink: oklch(0.26 0.05 350);
  --color-tcd21-mut: #6e505b;
  --color-tcd21-mut: oklch(0.46 0.05 350);
  --color-tcd21-shade: #e2cfcb;
  --color-tcd21-shade: oklch(0.87 0.02 30);
  --color-tcd21-work: #ff6a4d;
  --color-tcd21-work: oklch(0.68 0.19 34);
  --color-tcd21-work-ink: #c23d22;
  --color-tcd21-work-ink: oklch(0.54 0.18 34);
  --color-tcd21-rest: #7a4fd6;
  --color-tcd21-rest: oklch(0.54 0.19 295);
  --font-tcd21-sans: 'Nunito', ui-rounded, system-ui, sans-serif;
  --animate-tcd21-t: tcd21-t 90s infinite;
  --animate-tcd21-arc: tcd21-arc 90s infinite;
  --animate-tcd21-work: tcd21-work 90s steps(1, end) infinite;
  --animate-tcd21-rest: tcd21-rest 90s steps(1, end) infinite;
  --animate-tcd21-halo: tcd21-halo 2s ease-in-out infinite;

  @keyframes tcd21-t {
    0% {
      --tcd21-t: 59;
      animation-timing-function: steps(60, end);
    }

    66.66% {
      --tcd21-t: -1;
    }

    66.67% {
      --tcd21-t: 29;
      animation-timing-function: steps(30, end);
    }

    100% {
      --tcd21-t: -1;
    }
  }

  @keyframes tcd21-arc {
    0% {
      stroke-dashoffset: 0;
      stroke: var(--color-tcd21-work);
      animation-timing-function: linear;
    }

    66.66% {
      stroke-dashoffset: 100;
      stroke: var(--color-tcd21-work);
    }

    66.67% {
      stroke-dashoffset: 0;
      stroke: var(--color-tcd21-rest);
      animation-timing-function: linear;
    }

    100% {
      stroke-dashoffset: 100;
      stroke: var(--color-tcd21-rest);
    }
  }

  @keyframes tcd21-work {
    0% {
      opacity: 1;
    }

    66.67%,
        100% {
      opacity: 0;
    }
  }

  @keyframes tcd21-rest {
    0% {
      opacity: 0;
    }

    66.67%,
        100% {
      opacity: 1;
    }
  }

  @keyframes tcd21-halo {
    0%,
        100% {
      transform: scale(0.94);
      opacity: 0.5;
    }

    50% {
      transform: scale(1);
      opacity: 1;
    }
  }
}

.tcd-21 {
  width: 100%;
  min-height: 100svh;
}
```
