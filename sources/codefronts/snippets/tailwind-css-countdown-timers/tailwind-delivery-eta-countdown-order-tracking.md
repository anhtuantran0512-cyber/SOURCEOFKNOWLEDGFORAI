---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-delivery-eta-countdown-order-tracking/"
title: "Tailwind Delivery ETA Countdown with Order Tracking Steps"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "An order-tracking ETA that counts down beside a four-step status rail &mdash; and at zero flips to Arriving any moment instead of drifting into negative…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Delivery ETA Countdown with Order Tracking Steps
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-delivery-eta-countdown-order-tracking/

An order-tracking ETA that counts down beside a four-step status rail &mdash; and at zero flips to Arriving any moment instead of drifting into negative minutes. In the port, step states are data-state attributes read by group-data-[state=done]/step:, and a delayed keyframe now advances the rail to its final step at the same moment, still with zero JavaScript.
## HTML
```html
<section class="tcd-08 w-full min-h-svh grid place-items-center bg-tcd08-page px-4 py-12 font-tcd08-sans text-tcd08-ink" aria-labelledby="tcd-08-title">
  <article class="w-full max-w-[560px] rounded-[26px] bg-tcd08-card p-[clamp(20px,4.4vw,32px)] shadow-tcd08-card">
    <header class="flex flex-wrap items-start justify-between gap-x-4 gap-y-3">
      <div class="min-w-0">
        <p class="mb-1 text-[11px] font-extrabold uppercase tracking-[0.16em] text-tcd08-acc">Fern Kitchen</p>
        <h2 id="tcd-08-title" class="text-[clamp(17px,3vw,20px)] font-extrabold leading-snug text-balance">Order 8842 · two bowls, one flatbread</h2>
      </div>
      <div class="flex items-center gap-2.5 rounded-full bg-tcd08-soft py-1.5 pr-4 pl-1.5">
        <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-tcd08-acc text-xs font-black text-white">SR</span>
        <span class="text-[13px] leading-tight font-bold">Sam Rivera<br><em class="text-[11px] font-semibold not-italic text-tcd08-mut">Courier</em></span>
      </div>
    </header>

    <div role="timer" aria-label="Estimated arrival countdown" class="relative mt-6 overflow-hidden rounded-2xl bg-tcd08-soft px-5 py-6 text-center">
      <p class="text-xs font-extrabold uppercase tracking-[0.14em] text-tcd08-mut">Arriving in</p>
      <p aria-hidden="true" class="my-1 flex items-baseline justify-center text-[clamp(56px,16vw,84px)] font-black leading-none tracking-[-0.03em] tabular-nums">
        <em class="not-italic animate-tcd08-min [counter-reset:tcd08min_var(--tcd08-min)] before:content-[counter(tcd08min)]"></em><span class="px-0.5 text-tcd08-acc">:</span><em class="not-italic animate-tcd08-st [counter-reset:tcd08st_var(--tcd08-st)] before:content-[counter(tcd08st)]"></em><em class="not-italic animate-tcd08-su [counter-reset:tcd08su_var(--tcd08-su)] before:content-[counter(tcd08su)]"></em>
      </p>
      <p class="text-[13px] font-semibold text-tcd08-mut">Estimated <time datetime="PT14M">14 minutes</time> from Vale Street</p>
      <div aria-hidden="true" class="mx-auto mt-4 h-1.5 max-w-[280px] overflow-hidden rounded-full bg-tcd08-rule"><span class="block h-full origin-right rounded-full bg-tcd08-acc animate-tcd08-bar"></span></div>
      <div role="status" class="invisible absolute inset-0 grid place-content-center gap-1.5 bg-tcd08-acc px-5 text-white opacity-0 animate-tcd08-done">
        <strong class="text-[clamp(24px,6vw,32px)] font-black tracking-[-0.01em]">Arriving any moment</strong>
        <span class="text-[13px] font-semibold opacity-90">Sam is on your street — meet at the door</span>
      </div>
    </div>

    <ol class="relative mt-7 grid gap-5 before:absolute before:top-2 before:bottom-2 before:left-[9px] before:w-0.5 before:bg-tcd08-rule before:content-['']">
      <li data-state="done" class="group/step relative grid grid-cols-[20px_1fr_auto] items-center gap-3.5 text-[14px] font-bold"><span aria-hidden="true" class="relative grid size-5 place-items-center rounded-full bg-tcd08-rule group-data-[state=done]/step:bg-tcd08-acc"><svg viewBox="0 0 12 12" width="10" height="10" class="hidden text-white group-data-[state=done]/step:block"><path d="M2.5 6.2 5 8.5l4.5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>Order placed<em class="text-xs font-semibold not-italic text-tcd08-mut">7:02 pm</em></li>
      <li data-state="done" class="group/step relative grid grid-cols-[20px_1fr_auto] items-center gap-3.5 text-[14px] font-bold"><span aria-hidden="true" class="relative grid size-5 place-items-center rounded-full bg-tcd08-rule group-data-[state=done]/step:bg-tcd08-acc"><svg viewBox="0 0 12 12" width="10" height="10" class="hidden text-white group-data-[state=done]/step:block"><path d="M2.5 6.2 5 8.5l4.5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>Preparing<em class="text-xs font-semibold not-italic text-tcd08-mut">7:09 pm</em></li>
      <li data-state="active" aria-current="step" class="group/step relative grid grid-cols-[20px_1fr_auto] items-center gap-3.5 text-[14px] font-extrabold text-tcd08-acc"><span aria-hidden="true" class="relative grid size-5 place-items-center rounded-full bg-tcd08-card ring-[5px] ring-tcd08-acc ring-inset"><span class="absolute inset-0 rounded-full bg-tcd08-acc/40 animate-ping motion-reduce:hidden"></span></span>On the way<em class="text-xs font-bold not-italic">now</em></li>
      <li class="group/step relative grid grid-cols-[20px_1fr_auto] items-center gap-3.5 text-[14px] font-bold text-tcd08-mut animate-tcd08-arrive"><span aria-hidden="true" class="relative size-5 rounded-full border-2 border-tcd08-rule bg-tcd08-card"></span>Arriving<em class="text-xs font-semibold not-italic">7:36 pm</em></li>
    </ol>

    <p class="mt-6 border-t border-tcd08-rule pt-4 text-[12.5px] leading-relaxed text-tcd08-mut text-pretty">At zero this ETA flips to a terminal message instead of counting into negative minutes. Written in Tailwind only, so it measures fourteen minutes from render rather than tracking a server timestamp.</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd08-min {
  syntax: '<integer>';
  inherits: false;
  initial-value: 13;
}

@property --tcd08-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd08-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@theme {
  --color-tcd08-page: #e9efe4;
  --color-tcd08-page: oklch(0.94 0.018 140);
  --color-tcd08-card: #ffffff;
  --color-tcd08-card: oklch(1 0 0);
  --color-tcd08-soft: #eef3ea;
  --color-tcd08-soft: oklch(0.96 0.015 140);
  --color-tcd08-ink: #17231b;
  --color-tcd08-ink: oklch(0.23 0.03 150);
  --color-tcd08-mut: #546659;
  --color-tcd08-mut: oklch(0.48 0.028 155);
  --color-tcd08-rule: #d5e0d0;
  --color-tcd08-rule: oklch(0.88 0.02 145);
  --color-tcd08-acc: #2f7d4f;
  --color-tcd08-acc: oklch(0.52 0.12 150);
  --font-tcd08-sans: 'Nunito', ui-rounded, system-ui, sans-serif;
  --shadow-tcd08-card: 0 1px 2px rgb(23 35 27 / 0.05), 0 30px 60px -36px rgb(23 35 27 / 0.45);
  --animate-tcd08-min: tcd08-min 840s steps(14, end) forwards;
  --animate-tcd08-st: tcd08-st 60s steps(6, end) infinite;
  --animate-tcd08-su: tcd08-su 10s steps(10, end) infinite;
  --animate-tcd08-bar: tcd08-bar 840s linear forwards;
  --animate-tcd08-done: tcd08-done 0.01s linear 840s forwards;
  --animate-tcd08-arrive: tcd08-arrive 0.4s ease-out 840s forwards;

  @keyframes tcd08-min {
    from {
      --tcd08-min: 13;
    }

    to {
      --tcd08-min: -1;
    }
  }

  @keyframes tcd08-st {
    from {
      --tcd08-st: 5;
    }

    to {
      --tcd08-st: -1;
    }
  }

  @keyframes tcd08-su {
    from {
      --tcd08-su: 9;
    }

    to {
      --tcd08-su: -1;
    }
  }

  @keyframes tcd08-bar {
    from {
      transform: scaleX(0.04);
    }

    to {
      transform: scaleX(1);
    }
  }

  @keyframes tcd08-done {
    to {
      opacity: 1;
      visibility: visible;
    }
  }

  @keyframes tcd08-arrive {
    to {
      color: var(--color-tcd08-acc);
    }
  }
}

.tcd-08 {
  width: 100%;
  min-height: 100svh;
}
```
