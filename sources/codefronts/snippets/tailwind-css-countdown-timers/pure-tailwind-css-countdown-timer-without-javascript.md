---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/pure-tailwind-css-countdown-timer-without-javascript/"
title: "Pure Tailwind CSS Countdown Timer Without JavaScript"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A twenty-minute exam clock with zero JavaScript: four registered @property integers step down on keyframes, and CSS counters print them."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Countdown Timer Without JavaScript
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/pure-tailwind-css-countdown-timer-without-javascript/

A twenty-minute exam clock with zero JavaScript: four registered @property integers step down on keyframes, and CSS counters print them. Tailwind holds the counters as arbitrary properties ([counter-reset:tcd02mt_var(--tcd02-mt)] + before:content-[counter(tcd02mt)]), the keyframes live in @theme, and a new depleting bar shows the whole window at a glance.
## HTML
```html
<section class="tcd-02 w-full min-h-svh grid place-items-center bg-tcd02-page bg-[radial-gradient(80%_60%_at_50%_42%,var(--color-tcd02-glow),transparent_70%)] px-5 py-14 font-tcd02-mono text-tcd02-ink" aria-labelledby="tcd-02-title">
  <div class="grid w-full max-w-[760px] justify-items-center gap-6">
    <header class="min-w-0 text-center">
      <span class="mb-3.5 inline-flex items-center gap-2 rounded-full border border-tcd02-acc/40 bg-tcd02-acc/10 px-3 py-1.5 text-[10.5px] uppercase tracking-[0.2em] text-tcd02-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd02-acc animate-tcd02-blink motion-reduce:animate-none"></span>zero javascript</span>
      <h2 id="tcd-02-title" class="mb-2 text-[clamp(19px,3.4vw,26px)] font-medium leading-tight tracking-[-0.01em] text-balance">Practice set — Basalt certification</h2>
      <p class="mx-auto max-w-[52ch] text-[13px] leading-relaxed text-tcd02-mut text-pretty"><time datetime="PT20M">Twenty minutes</time> from the moment this page rendered. The clock below is animated CSS, not a script.</p>
    </header>

    <div role="timer" aria-label="Twenty minute practice timer, counting down from page load" class="relative w-full overflow-hidden rounded-2xl border border-tcd02-rule bg-tcd02-panel px-[clamp(14px,4vw,32px)] pt-[clamp(28px,6vw,48px)] pb-7 text-center shadow-[inset_0_0_90px_rgb(0_0_0/0.55),0_30px_60px_-30px_rgb(0_0_0/0.8)] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(to_bottom,rgb(255_255_255/0.045)_0_1px,transparent_1px_3px)] after:content-[''] motion-reduce:after:hidden">
      <div aria-hidden="true" class="flex items-baseline justify-center gap-0.5 tabular-nums text-tcd02-acc [text-shadow:0_0_26px_var(--color-tcd02-acc-glow)]">
        <em class="text-[clamp(52px,17vw,116px)] font-medium not-italic leading-[0.9] tracking-[-0.04em] animate-tcd02-mt [counter-reset:tcd02mt_var(--tcd02-mt)] before:content-[counter(tcd02mt)]"></em>
        <em class="text-[clamp(52px,17vw,116px)] font-medium not-italic leading-[0.9] tracking-[-0.04em] animate-tcd02-mu [counter-reset:tcd02mu_var(--tcd02-mu)] before:content-[counter(tcd02mu)]"></em>
        <span class="text-[clamp(40px,12vw,88px)] leading-[0.9] animate-tcd02-blink motion-reduce:animate-none motion-reduce:opacity-50">:</span>
        <em class="text-[clamp(52px,17vw,116px)] font-medium not-italic leading-[0.9] tracking-[-0.04em] animate-tcd02-st [counter-reset:tcd02st_var(--tcd02-st)] before:content-[counter(tcd02st)]"></em>
        <em class="text-[clamp(52px,17vw,116px)] font-medium not-italic leading-[0.9] tracking-[-0.04em] animate-tcd02-su [counter-reset:tcd02su_var(--tcd02-su)] before:content-[counter(tcd02su)]"></em>
      </div>
      <p class="mt-4 text-[10.5px] uppercase tracking-[0.22em] text-tcd02-mut">minutes · seconds remaining</p>
      <div aria-hidden="true" class="mx-auto mt-6 h-1 max-w-[420px] overflow-hidden rounded-full bg-tcd02-rule">
        <span class="block h-full origin-left rounded-full bg-tcd02-acc shadow-[0_0_12px_var(--color-tcd02-acc-glow)] animate-tcd02-bar"></span>
      </div>
      <div role="status" class="invisible absolute inset-0 z-10 grid place-content-center gap-1.5 bg-tcd02-panel opacity-0 animate-tcd02-over">
        <strong class="text-[clamp(26px,7vw,44px)] font-medium tracking-[-0.02em] text-tcd02-acc">Time up</strong>
        <span class="text-xs text-tcd02-mut">Answers submitted automatically</span>
      </div>
    </div>

    <p class="flex min-w-0 items-start gap-2.5 rounded-xl border border-dashed border-tcd02-rule px-4 py-3.5 text-[12.5px] leading-relaxed text-tcd02-mut text-pretty">
      <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" class="mt-0.5 flex-none text-tcd02-acc"><path d="M8 1.6 1.2 13.4h13.6L8 1.6Z" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M8 6v3.4M8 11.2v.9" stroke="currentColor" stroke-width="1.3"/></svg>
      <span>A CSS-only countdown measures a duration from render, not the distance to a timestamp. It fits session and quiz clocks. For "sale ends Friday" you need the real clock, which means script.</span>
    </p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Registered integers: the one thing utilities cannot declare. */

@property --tcd02-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --tcd02-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --tcd02-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd02-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@theme {
  --color-tcd02-page: #05070a;
  --color-tcd02-page: oklch(0.14 0.02 190);
  --color-tcd02-glow: #0c1a16;
  --color-tcd02-glow: oklch(0.21 0.04 170);
  --color-tcd02-panel: #0a0f14;
  --color-tcd02-panel: oklch(0.19 0.025 185);
  --color-tcd02-ink: #d8fff0;
  --color-tcd02-ink: oklch(0.94 0.07 165);
  --color-tcd02-mut: #7fa598;
  --color-tcd02-mut: oklch(0.7 0.05 168);
  --color-tcd02-rule: #1d2b26;
  --color-tcd02-rule: oklch(0.28 0.03 180);
  --color-tcd02-acc: #37e58f;
  --color-tcd02-acc: oklch(0.8 0.18 155);
  --color-tcd02-acc-glow: rgb(55 229 143 / 0.38);
  --font-tcd02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tcd02-mt: tcd02-mt 1200s steps(2, end) forwards;
  --animate-tcd02-mu: tcd02-mu 600s steps(10, end) 2;
  --animate-tcd02-st: tcd02-st 60s steps(6, end) infinite;
  --animate-tcd02-su: tcd02-su 10s steps(10, end) infinite;
  --animate-tcd02-bar: tcd02-bar 1200s linear forwards;
  --animate-tcd02-over: tcd02-over 0.01s linear 1200s forwards;
  --animate-tcd02-blink: tcd02-blink 2s steps(2, end) infinite;

  @keyframes tcd02-mt {
    from {
      --tcd02-mt: 1;
    }

    to {
      --tcd02-mt: -1;
    }
  }

  @keyframes tcd02-mu {
    from {
      --tcd02-mu: 9;
    }

    to {
      --tcd02-mu: -1;
    }
  }

  @keyframes tcd02-st {
    from {
      --tcd02-st: 5;
    }

    to {
      --tcd02-st: -1;
    }
  }

  @keyframes tcd02-su {
    from {
      --tcd02-su: 9;
    }

    to {
      --tcd02-su: -1;
    }
  }

  @keyframes tcd02-bar {
    from {
      transform: scaleX(1);
    }

    to {
      transform: scaleX(0);
    }
  }

  @keyframes tcd02-over {
    to {
      opacity: 1;
      visibility: visible;
    }
  }

  @keyframes tcd02-blink {
    0%,
        50% {
      opacity: 0.55;
    }

    51%,
        100% {
      opacity: 0.15;
    }
  }
}

.tcd-02 {
  width: 100%;
  min-height: 100svh;
}
```
