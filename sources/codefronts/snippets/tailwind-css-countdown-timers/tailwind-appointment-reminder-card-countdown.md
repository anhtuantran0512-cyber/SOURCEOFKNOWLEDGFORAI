---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-appointment-reminder-card-countdown/"
title: "Tailwind Appointment Reminder Card with Countdown"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "An upcoming-visit card that changes precision as the appointment approaches: days and hours while it is far off, a live H:MM:SS clock inside the last day,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Appointment Reminder Card with Countdown
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-appointment-reminder-card-countdown/

An upcoming-visit card that changes precision as the appointment approaches: days and hours while it is far off, a live H:MM:SS clock inside the last day, with Reschedule and Cancel surfaced only then. Both states sit side by side. New in the port: calendar date tiles, a data-state="soon" card styled entirely by data-[state=soon]: variants, and a zero-JS check-in state when the clock runs out.
## HTML
```html
<section class="tcd-11 w-full min-h-svh bg-tcd11-page font-tcd11-sans text-tcd11-ink antialiased" aria-labelledby="tcd-11-title">
  <div class="mx-auto grid min-h-svh max-w-[760px] content-center gap-4 px-[clamp(18px,4vw,40px)] py-14">
    <header class="mb-2 min-w-0">
      <p class="mb-2 text-[11px] font-bold uppercase tracking-[0.16em] text-tcd11-acc">Vale Family Practice</p>
      <h2 id="tcd-11-title" class="mb-1.5 font-tcd11-serif text-[clamp(26px,4.4vw,36px)] font-normal leading-tight tracking-[-0.015em]">Upcoming appointments</h2>
      <p class="max-w-[54ch] text-[14px] leading-relaxed text-tcd11-mut text-pretty">The card changes precision inside the last day, and surfaces the two actions that matter then.</p>
    </header>

    <article class="group/card grid grid-cols-[auto_minmax(0,1fr)] gap-x-4 gap-y-1 rounded-2xl border border-tcd11-rule bg-tcd11-card p-[clamp(16px,3.4vw,24px)] transition data-[state=soon]:border-tcd11-acc data-[state=soon]:ring-4 data-[state=soon]:ring-tcd11-acc/10">
      <div aria-hidden="true" class="row-span-4 grid h-[68px] w-[60px] grid-rows-[22px_1fr] overflow-hidden rounded-xl border border-tcd11-rule text-center"><span class="bg-tcd11-sunk text-[10px] font-bold uppercase leading-[22px] tracking-[0.1em] text-tcd11-mut">Aug</span><span class="grid place-items-center font-tcd11-serif text-[26px] leading-none">24</span></div>
      <header class="flex flex-wrap items-center justify-between gap-2">
        <span class="rounded-full bg-tcd11-sunk px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.08em] text-tcd11-mut">Scheduled</span>
        <time datetime="2026-08-24T09:20:00+01:00" class="text-[12.5px] font-medium text-tcd11-mut">Mon 24 Aug, 9:20 am</time>
      </header>
      <h3 class="mt-1.5 font-tcd11-serif text-[clamp(18px,3vw,21px)] font-medium leading-snug">Annual review with Dr Priya Sharma</h3>
      <p class="text-[13px] leading-relaxed text-tcd11-mut">Room 2, Ground floor · 14 Basalt Road · bring your current prescriptions</p>
      <p role="timer" class="mt-2 text-[15px] font-semibold">In <time datetime="P2DT4H">2 days 4 hours</time></p>
      <p class="col-span-2 mt-3 border-t border-dashed border-tcd11-rule pt-3 text-xs text-tcd11-mut">More than a day out: days and hours only. No actions surfaced.</p>
    </article>

    <article data-state="soon" class="group/card relative grid grid-cols-[auto_minmax(0,1fr)] gap-x-4 gap-y-1 overflow-hidden rounded-2xl border border-tcd11-rule bg-tcd11-card p-[clamp(16px,3.4vw,24px)] shadow-tcd11-card transition data-[state=soon]:border-tcd11-acc data-[state=soon]:ring-4 data-[state=soon]:ring-tcd11-acc/10">
      <div aria-hidden="true" class="row-span-4 grid h-[68px] w-[60px] grid-rows-[22px_1fr] overflow-hidden rounded-xl border border-tcd11-rule text-center group-data-[state=soon]/card:border-tcd11-acc"><span class="bg-tcd11-sunk text-[10px] font-bold uppercase leading-[22px] tracking-[0.1em] text-tcd11-mut group-data-[state=soon]/card:bg-tcd11-acc group-data-[state=soon]/card:text-white">Aug</span><span class="grid place-items-center font-tcd11-serif text-[26px] leading-none">22</span></div>
      <header class="flex flex-wrap items-center justify-between gap-2">
        <span class="inline-flex items-center gap-1.5 rounded-full bg-tcd11-sunk px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.08em] text-tcd11-mut group-data-[state=soon]/card:bg-tcd11-acc/12 group-data-[state=soon]/card:text-tcd11-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-current animate-pulse motion-reduce:animate-none"></span>Tomorrow</span>
        <time datetime="2026-08-22T14:00:00+01:00" class="text-[12.5px] font-medium text-tcd11-mut">Sat 22 Aug, 2:00 pm</time>
      </header>
      <h3 class="mt-1.5 font-tcd11-serif text-[clamp(18px,3vw,21px)] font-medium leading-snug">Blood work · fasting from midnight</h3>
      <p class="text-[13px] leading-relaxed text-tcd11-mut">Pathology desk, Level 1 · Jordan Lee, phlebotomist</p>
      <p role="timer" aria-label="Time until appointment" class="mt-2 flex items-baseline gap-2 text-[15px] font-semibold">In
        <span aria-hidden="true" class="inline-flex rounded-lg bg-tcd11-sunk px-2.5 py-1 font-tcd11-serif text-[clamp(24px,5vw,30px)] font-medium leading-none tabular-nums text-tcd11-acc">
          <em class="not-italic animate-tcd11-h [counter-reset:tcd11h_var(--tcd11-h)] before:content-[counter(tcd11h)]"></em><span class="opacity-50">:</span><em class="not-italic animate-tcd11-mt [counter-reset:tcd11mt_var(--tcd11-mt)] before:content-[counter(tcd11mt)]"></em><em class="not-italic animate-tcd11-mu [counter-reset:tcd11mu_var(--tcd11-mu)] before:content-[counter(tcd11mu)]"></em><span class="opacity-50">:</span><em class="not-italic animate-tcd11-st [counter-reset:tcd11st_var(--tcd11-st)] before:content-[counter(tcd11st)]"></em><em class="not-italic animate-tcd11-su [counter-reset:tcd11su_var(--tcd11-su)] before:content-[counter(tcd11su)]"></em>
        </span>
      </p>
      <div class="col-span-2 mt-4 grid gap-3 border-t border-dashed border-tcd11-rule pt-4">
        <p class="text-xs text-tcd11-mut">Inside twenty-four hours: hour and minute precision, actions available.</p>
        <div class="flex flex-wrap gap-2.5">
          <button type="button" class="min-h-11 flex-[1_1_140px] cursor-pointer rounded-xl bg-tcd11-acc px-4 text-sm font-bold text-white transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd11-ink">Reschedule</button>
          <button type="button" class="min-h-11 flex-[1_1_140px] cursor-pointer rounded-xl border border-tcd11-rule px-4 text-sm font-bold text-tcd11-mut transition hover:border-tcd11-ink/30 hover:text-tcd11-ink active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd11-acc">Cancel visit</button>
        </div>
        <p class="rounded-lg bg-tcd11-sunk px-3 py-2.5 text-[12px] leading-relaxed text-tcd11-mut text-pretty">Cancelling inside four hours is recorded as a late cancellation. Call the desk if you are running behind — the slot is held ten minutes.</p>
      </div>
      <div role="status" class="invisible absolute inset-0 grid place-content-center gap-1 bg-tcd11-acc px-6 text-center text-white opacity-0 animate-tcd11-due">
        <strong class="font-tcd11-serif text-[clamp(22px,5vw,28px)] font-medium">It's time — check in at the desk</strong>
        <span class="text-[13px] opacity-90">Pathology, Level 1 · your slot is held ten minutes</span>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd11-h {
  syntax: '<integer>';
  inherits: false;
  initial-value: 3;
}

@property --tcd11-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd11-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --tcd11-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd11-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@theme {
  --color-tcd11-page: #f0f4f2;
  --color-tcd11-page: oklch(0.96 0.012 170);
  --color-tcd11-card: #ffffff;
  --color-tcd11-card: oklch(1 0 0);
  --color-tcd11-sunk: #e9f0ed;
  --color-tcd11-sunk: oklch(0.95 0.014 170);
  --color-tcd11-ink: #1c2b28;
  --color-tcd11-ink: oklch(0.26 0.024 175);
  --color-tcd11-mut: #54665f;
  --color-tcd11-mut: oklch(0.47 0.022 175);
  --color-tcd11-rule: #dbe6e2;
  --color-tcd11-rule: oklch(0.91 0.014 170);
  --color-tcd11-acc: #0d7d6b;
  --color-tcd11-acc: oklch(0.5 0.1 172);
  --font-tcd11-serif: 'Fraunces', Georgia, serif;
  --font-tcd11-sans: 'Public Sans', system-ui, sans-serif;
  --shadow-tcd11-card: 0 26px 50px -34px rgb(28 43 40 / 0.45);
  --animate-tcd11-h: tcd11-h 14400s steps(4, end) forwards;
  --animate-tcd11-mt: tcd11-mt 3600s steps(6, end) infinite;
  --animate-tcd11-mu: tcd11-mu 600s steps(10, end) infinite;
  --animate-tcd11-st: tcd11-st 60s steps(6, end) infinite;
  --animate-tcd11-su: tcd11-su 10s steps(10, end) infinite;
  --animate-tcd11-due: tcd11-due 0.01s linear 14400s forwards;

  @keyframes tcd11-h {
    from {
      --tcd11-h: 3;
    }

    to {
      --tcd11-h: -1;
    }
  }

  @keyframes tcd11-mt {
    from {
      --tcd11-mt: 5;
    }

    to {
      --tcd11-mt: -1;
    }
  }

  @keyframes tcd11-mu {
    from {
      --tcd11-mu: 9;
    }

    to {
      --tcd11-mu: -1;
    }
  }

  @keyframes tcd11-st {
    from {
      --tcd11-st: 5;
    }

    to {
      --tcd11-st: -1;
    }
  }

  @keyframes tcd11-su {
    from {
      --tcd11-su: 9;
    }

    to {
      --tcd11-su: -1;
    }
  }

  @keyframes tcd11-due {
    to {
      opacity: 1;
      visibility: visible;
    }
  }
}

.tcd-11 {
  width: 100%;
  min-height: 100svh;
}
```
