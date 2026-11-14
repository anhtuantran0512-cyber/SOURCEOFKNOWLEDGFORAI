---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-subscribe-confetti-button/"
title: "Tailwind Subscribe Confetti Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Subscribe once and eighteen paper shards fan out on individual trajectories, the bell rings, and the label flips to \"Subscribed\"."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Subscribe Confetti Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-subscribe-confetti-button/

Subscribe once and eighteen paper shards fan out on individual trajectories, the bell rings, and the label flips to "Subscribed". Every particle's angle, distance, spin and delay is a custom property in its style attribute — the one place where inline style beats a utility, and the port says so.
## HTML
```html
<div class="tb-14 w-full min-h-svh grid place-items-center font-tb14-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative z-10 cursor-pointer inline-grid place-items-center min-h-14 px-8 rounded-full text-base font-extrabold tracking-[-0.01em] text-tb14-ink bg-[linear-gradient(180deg,var(--color-tb14-accent-lift),var(--color-tb14-accent))] shadow-[inset_0_1px_0_var(--color-tb14-sheen),0_16px_34px_-16px_var(--color-tb14-glow)] transition-[scale,background,box-shadow] duration-[350ms] ease-tb14-spring [-webkit-tap-highlight-color:transparent] hover:scale-[1.03] active:scale-[0.97] has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tb14-c1 has-checked:bg-[linear-gradient(180deg,var(--color-tb14-surface-lift),var(--color-tb14-surface))] has-checked:shadow-[inset_0_0_0_1px_var(--color-tb14-edge)] motion-reduce:transition-none motion-reduce:hover:scale-100">
    <input type="checkbox" aria-label="Subscribe to the newsletter" class="sr-only">
    <span aria-hidden="true" class="absolute inset-0 pointer-events-none motion-reduce:hidden">
      <span style="--x:-.95;--y:-.65;--r:180deg;--d:0ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-.6;--y:-1;--r:-140deg;--d:20ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-.25;--y:-1.1;--r:220deg;--d:40ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.1;--y:-1.15;--r:-90deg;--d:10ms" class="absolute top-1/2 left-1/2 w-[0.28rem] h-[0.6rem] -mt-[0.3rem] -ml-[0.14rem] rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.45;--y:-1;--r:160deg;--d:50ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.8;--y:-.75;--r:-200deg;--d:30ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:1.05;--y:-.4;--r:120deg;--d:60ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-1.1;--y:-.3;--r:-160deg;--d:70ms" class="absolute top-1/2 left-1/2 w-[0.28rem] h-[0.6rem] -mt-[0.3rem] -ml-[0.14rem] rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-1.15;--y:.1;--r:200deg;--d:90ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:1.15;--y:.05;--r:-240deg;--d:80ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-.9;--y:.5;--r:140deg;--d:120ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.95;--y:.45;--r:-120deg;--d:110ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-.5;--y:.85;--r:260deg;--d:150ms" class="absolute top-1/2 left-1/2 w-[0.28rem] h-[0.6rem] -mt-[0.3rem] -ml-[0.14rem] rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.55;--y:.8;--r:-180deg;--d:140ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:0;--y:1;--r:90deg;--d:170ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:-.3;--y:-.5;--r:-60deg;--d:0ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c1 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.3;--y:-.55;--r:60deg;--d:15ms" class="absolute top-1/2 left-1/2 w-2 h-[0.32rem] -mt-[0.16rem] -ml-1 rounded-[0.06rem] bg-tb14-c3 opacity-0 group-has-checked:animate-tb14-burst"></span>
      <span style="--x:.7;--y:.2;--r:-300deg;--d:100ms" class="absolute top-1/2 left-1/2 size-[0.34rem] -mt-[0.17rem] -ml-[0.17rem] rounded-full bg-tb14-c2 opacity-0 group-has-checked:animate-tb14-burst"></span>
    </span>
    <span class="grid grid-flow-col items-center gap-2">
      <span aria-hidden="true" class="grid place-items-center size-5 [transform-origin:50%_15%] group-has-checked:animate-tb14-ring motion-reduce:group-has-checked:animate-none">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M18 15.5V11a6 6 0 1 0-12 0v4.5L4.5 18h15L18 15.5z"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0"/></svg>
      </span>
      <span class="grid">
        <span class="col-start-1 row-start-1 transition-[opacity,translate] duration-300 ease-tb14-out group-has-checked:opacity-0 group-has-checked:-translate-y-1.5 motion-reduce:transition-none">Subscribe</span>
        <span class="col-start-1 row-start-1 opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 ease-tb14-out group-has-checked:opacity-100 group-has-checked:translate-y-0 motion-reduce:transition-none">Subscribed</span>
      </span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb14-bg: #100c1a;
  --color-tb14-bg: oklch(0.16 0.03 295);
  --color-tb14-surface: #1d1730;
  --color-tb14-surface: oklch(0.25 0.05 295);
  --color-tb14-surface-lift: #272040;
  --color-tb14-surface-lift: oklch(0.3 0.05 295);
  --color-tb14-ink: #f8f5ff;
  --color-tb14-ink: oklch(0.97 0.012 295);
  --color-tb14-accent: #f43f5e;
  --color-tb14-accent: oklch(0.64 0.21 12);
  --color-tb14-accent-lift: #f76b83;
  --color-tb14-accent-lift: oklch(0.7 0.18 12);
  --color-tb14-c1: #fbbf24;
  --color-tb14-c1: oklch(0.84 0.16 82);
  --color-tb14-c2: #34d399;
  --color-tb14-c2: oklch(0.8 0.14 165);
  --color-tb14-c3: #60a5fa;
  --color-tb14-c3: oklch(0.76 0.13 253);
  --color-tb14-sheen: #ffffff4d;
  --color-tb14-edge: #f8f5ff2e;
  --color-tb14-edge: oklch(0.97 0.012 295 / 0.18);
  --color-tb14-glow: #f43f5ed9;
  --color-tb14-glow: oklch(0.64 0.21 12 / 0.85);
  --font-tb14-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb14-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-tb14-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb14-burst: tb-14-burst 0.95s cubic-bezier(0.2, 0.7, 0.3, 1) var(--d, 0ms) forwards;
  --animate-tb14-ring: tb-14-ring 0.8s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb14-spring: linear(0, 0.42 8%, 0.86 17%, 1.12 25%, 1.06 36%, 1 50%, 1);
  }
}

@keyframes tb-14-burst {
  0% {
    opacity: 0;
    translate: 0 0;
    scale: 0.3;
    rotate: 0deg;
  }

  12% {
    opacity: 1;
  }

  100% {
    opacity: 0;
    translate: calc(var(--x) * 5.5rem) calc(var(--y) * 5.5rem);
    rotate: var(--r);
    scale: 1;
  }
}

@keyframes tb-14-ring {
  0%,
    100% {
    rotate: 0deg;
  }

  15% {
    rotate: 16deg;
  }

  32% {
    rotate: -13deg;
  }

  50% {
    rotate: 9deg;
  }

  68% {
    rotate: -6deg;
  }

  85% {
    rotate: 3deg;
  }
}

.tb-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(46rem 28rem at 50% 40%, color-mix(in oklab, var(--color-tb14-accent) 14%, transparent), transparent 70%), var(--color-tb14-bg);
}

@media (prefers-color-scheme: light) {
  .tb-14:not([data-theme="dark"]) {
    --color-tb14-bg: oklch(0.96 0.012 295);
    --color-tb14-surface: #ffffff;
    --color-tb14-surface-lift: oklch(0.99 0.004 295);
    --color-tb14-ink: oklch(0.18 0.05 295);
    --color-tb14-edge: oklch(0.18 0.05 295 / 0.18);
  }
}

.tb-14[data-theme="light"] {
  --color-tb14-bg: oklch(0.96 0.012 295);
  --color-tb14-surface: #ffffff;
  --color-tb14-ink: oklch(0.18 0.05 295);
}

@media (forced-colors: active) {
  .tb-14 label {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-14 label > span[aria-hidden] span {
    display: none;
  }
}
```
