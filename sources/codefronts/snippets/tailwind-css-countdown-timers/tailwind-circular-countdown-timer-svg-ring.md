---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-circular-countdown-timer-svg-ring/"
title: "Tailwind Circular Countdown Timer with SVG Progress Ring"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A five-minute hold timer whose SVG ring empties as the window closes &mdash; time depleting, not task progress."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Circular Countdown Timer with SVG Progress Ring
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-circular-countdown-timer-svg-ring/

A five-minute hold timer whose SVG ring empties as the window closes &mdash; time depleting, not task progress. pathLength="100" makes the dash maths a percentage, the stroke steps from teal to amber to red at 50% and 20%, and the legend chips now light up in sync, all with stroke-*, fill-none and @theme animate tokens. Zero JavaScript.
## HTML
```html
<section class="tcd-04 w-full min-h-svh grid place-items-center bg-tcd04-page bg-[radial-gradient(60%_50%_at_50%_45%,var(--color-tcd04-glow),transparent_70%)] px-5 py-14 font-tcd04-sans text-tcd04-ink" aria-labelledby="tcd-04-title">
  <div class="grid w-full max-w-[640px] justify-items-center gap-7 text-center">
    <header class="min-w-0">
      <h2 id="tcd-04-title" class="mb-1.5 font-tcd04-display text-[clamp(20px,4vw,30px)] font-medium uppercase leading-tight tracking-[0.06em]">Hold time remaining</h2>
      <p class="text-[13px] text-tcd04-mut">Orbit support · Priya Sharma is next · window <time datetime="PT5M">5 minutes</time></p>
    </header>

    <div role="timer" aria-label="Five minute hold timer, time remaining" class="relative aspect-square w-[clamp(216px,58vw,320px)] rounded-full bg-tcd04-panel/60 shadow-[inset_0_0_0_1px_var(--color-tcd04-rule),0_40px_80px_-40px_rgb(0_0_0/0.9)]">
      <svg viewBox="0 0 120 120" aria-hidden="true" class="size-full -rotate-90 drop-shadow-[0_0_16px_rgb(56_217_200/0.3)] motion-reduce:drop-shadow-none">
        <circle cx="60" cy="60" r="52" pathLength="100" class="fill-none stroke-tcd04-rule [stroke-width:9]"/>
        <circle cx="60" cy="60" r="52" pathLength="100" class="fill-none stroke-tcd04-calm [stroke-dasharray:100] [stroke-linecap:round] [stroke-width:9] animate-tcd04-ring"/>
      </svg>
      <div class="absolute inset-0 grid place-content-center gap-1">
        <p aria-hidden="true" class="flex items-baseline justify-center gap-px font-tcd04-display text-[clamp(44px,13vw,68px)] font-medium leading-none tabular-nums">
          <em class="not-italic animate-tcd04-m [counter-reset:tcd04m_var(--tcd04-m)] before:content-[counter(tcd04m)]"></em><span class="opacity-45">:</span><em class="not-italic animate-tcd04-st [counter-reset:tcd04st_var(--tcd04-st)] before:content-[counter(tcd04st)]"></em><em class="not-italic animate-tcd04-su [counter-reset:tcd04su_var(--tcd04-su)] before:content-[counter(tcd04su)]"></em>
        </p>
        <p class="text-[10.5px] uppercase tracking-[0.24em] text-tcd04-mut">remaining</p>
      </div>
      <div role="status" class="invisible absolute inset-0 grid place-content-center gap-1 rounded-full bg-tcd04-panel opacity-0 animate-tcd04-done">
        <strong class="font-tcd04-display text-[clamp(22px,6vw,30px)] font-medium uppercase tracking-[0.05em] text-tcd04-calm">Connecting</strong>
        <span class="text-xs text-tcd04-mut">Agent picking up</span>
      </div>
    </div>

    <ul class="flex flex-wrap justify-center gap-2">
      <li class="flex min-w-0 items-center gap-2 rounded-full border border-tcd04-rule bg-tcd04-panel px-3 py-1.5 text-xs text-tcd04-ink animate-tcd04-lc motion-reduce:animate-none"><span aria-hidden="true" class="size-2 rounded-full bg-tcd04-calm"></span>Plenty of time · above 50%</li>
      <li class="flex min-w-0 items-center gap-2 rounded-full border border-tcd04-rule bg-tcd04-panel px-3 py-1.5 text-xs text-tcd04-ink animate-tcd04-lw motion-reduce:animate-none"><span aria-hidden="true" class="size-2 rounded-full bg-tcd04-warn"></span>Wrap up · under 50%</li>
      <li class="flex min-w-0 items-center gap-2 rounded-full border border-tcd04-rule bg-tcd04-panel px-3 py-1.5 text-xs text-tcd04-ink animate-tcd04-ld motion-reduce:animate-none"><span aria-hidden="true" class="size-2 rounded-full bg-tcd04-danger"></span>Final seconds · under 20%</li>
    </ul>
    <p class="max-w-[52ch] text-[12.5px] leading-relaxed text-tcd04-mut text-pretty">Time-depleting, not task-progress: the arc shrinks because the window is closing, and the legend lights the live band so the state never depends on colour alone. Pure CSS, so it measures five minutes from render.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd04-m {
  syntax: '<integer>';
  inherits: false;
  initial-value: 4;
}

@property --tcd04-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd04-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@theme {
  --color-tcd04-page: #070c1a;
  --color-tcd04-page: oklch(0.16 0.04 265);
  --color-tcd04-glow: #101a36;
  --color-tcd04-glow: oklch(0.24 0.06 265);
  --color-tcd04-panel: #0d1428;
  --color-tcd04-panel: oklch(0.21 0.05 264);
  --color-tcd04-ink: #eaf0ff;
  --color-tcd04-ink: oklch(0.95 0.02 265);
  --color-tcd04-mut: #95a3c7;
  --color-tcd04-mut: oklch(0.73 0.05 268);
  --color-tcd04-rule: #1c2745;
  --color-tcd04-rule: oklch(0.3 0.05 265);
  --color-tcd04-calm: #38d9c8;
  --color-tcd04-calm: oklch(0.8 0.13 185);
  --color-tcd04-warn: #f2b23c;
  --color-tcd04-warn: oklch(0.8 0.15 78);
  --color-tcd04-danger: #ff5a63;
  --color-tcd04-danger: oklch(0.68 0.2 20);
  --font-tcd04-display: 'Oswald', 'Archivo Narrow', sans-serif;
  --font-tcd04-sans: 'DM Sans', system-ui, sans-serif;
  --animate-tcd04-ring: tcd04-arc 300s linear forwards, tcd04-hue 300s steps(1, end) forwards;
  --animate-tcd04-m: tcd04-m 300s steps(5, end) forwards;
  --animate-tcd04-st: tcd04-st 60s steps(6, end) infinite;
  --animate-tcd04-su: tcd04-su 10s steps(10, end) infinite;
  --animate-tcd04-done: tcd04-done 0.01s linear 300s forwards;
  --animate-tcd04-lc: tcd04-lc 300s steps(1, end) forwards;
  --animate-tcd04-lw: tcd04-lw 300s steps(1, end) forwards;
  --animate-tcd04-ld: tcd04-ld 300s steps(1, end) forwards;

  @keyframes tcd04-arc {
    from {
      stroke-dashoffset: 0;
    }

    to {
      stroke-dashoffset: 100;
    }
  }

  @keyframes tcd04-hue {
    0% {
      stroke: var(--color-tcd04-calm);
      stroke-width: 9;
    }

    50% {
      stroke: var(--color-tcd04-warn);
      stroke-width: 9;
    }

    80%,
        100% {
      stroke: var(--color-tcd04-danger);
      stroke-width: 11;
    }
  }

  @keyframes tcd04-m {
    from {
      --tcd04-m: 4;
    }

    to {
      --tcd04-m: -1;
    }
  }

  @keyframes tcd04-st {
    from {
      --tcd04-st: 5;
    }

    to {
      --tcd04-st: -1;
    }
  }

  @keyframes tcd04-su {
    from {
      --tcd04-su: 9;
    }

    to {
      --tcd04-su: -1;
    }
  }

  @keyframes tcd04-done {
    to {
      opacity: 1;
      visibility: visible;
    }
  }

  @keyframes tcd04-lc {
    0% {
      opacity: 1;
    }

    50%,
        100% {
      opacity: 0.4;
    }
  }

  @keyframes tcd04-lw {
    0% {
      opacity: 0.4;
    }

    50% {
      opacity: 1;
    }

    80%,
        100% {
      opacity: 0.4;
    }
  }

  @keyframes tcd04-ld {
    0% {
      opacity: 0.4;
    }

    80%,
        100% {
      opacity: 1;
    }
  }
}

.tcd-04 {
  width: 100%;
  min-height: 100svh;
}
```
