---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-waitlist-landing-page-launch-countdown/"
title: "Tailwind Waitlist Landing Page with Launch Countdown"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A launch page built around the conversion surface rather than the clock: email capture first, a referral-position chip, and the countdown as supporting glass…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Waitlist Landing Page with Launch Countdown
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-waitlist-landing-page-launch-countdown/

A launch page built around the conversion surface rather than the clock: email capture first, a referral-position chip, and the countdown as supporting glass chrome over a slowly turning violet-cyan field. New in the port: zero-JS email validation via user-invalid: and peer-user-invalid:, a social-proof avatar stack, and supports-[backdrop-filter]: fallbacks.
## HTML
```html
<section class="tcd-09 relative w-full min-h-svh overflow-hidden bg-tcd09-page font-tcd09-sans text-tcd09-ink antialiased" aria-labelledby="tcd-09-title">
  <div aria-hidden="true" class="pointer-events-none absolute -inset-[30%] bg-[conic-gradient(from_210deg_at_40%_45%,var(--color-tcd09-f1),var(--color-tcd09-f2),var(--color-tcd09-f3),var(--color-tcd09-f1))] opacity-50 blur-[90px] animate-[spin_44s_linear_infinite] motion-reduce:animate-none"></div>
  <div class="relative mx-auto grid min-h-svh max-w-[1040px] grid-cols-1 content-center items-center gap-6 px-[clamp(16px,5vw,48px)] py-14 lg:grid-cols-[minmax(0,1.35fr)_minmax(0,1fr)]">
    <div class="min-w-0 rounded-3xl border border-white/15 bg-tcd09-solid p-[clamp(22px,4.6vw,44px)] shadow-[0_40px_80px_-40px_rgb(0_0_0/0.7)] supports-[backdrop-filter:blur(1px)]:bg-white/7 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl transition duration-700 starting:translate-y-3 starting:opacity-0">
      <p class="mb-4 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-3 py-1.5 font-tcd09-display text-[11px] font-semibold uppercase tracking-[0.18em] text-tcd09-acc2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd09-acc2"></span>Prism · early access</p>
      <h2 id="tcd-09-title" class="mb-3 font-tcd09-display text-[clamp(30px,5.6vw,54px)] font-semibold leading-[1.02] tracking-[-0.03em] text-balance">The waitlist opens before the <span class="bg-gradient-to-r from-tcd09-acc to-tcd09-acc2 bg-clip-text text-transparent">product does</span></h2>
      <p class="mb-7 max-w-[44ch] text-[15px] leading-relaxed text-tcd09-mut text-pretty">Invites go out in batches, top of the list first. Share your link and you move up.</p>

      <div class="grid gap-2">
        <label for="tcd-09-email" class="text-xs font-semibold tracking-[0.04em] text-tcd09-mut">Work email</label>
        <div class="flex flex-wrap gap-2.5">
          <input id="tcd-09-email" type="email" inputmode="email" autocomplete="email" required placeholder="[email protected]" class="peer min-h-12 min-w-0 flex-[1_1_220px] rounded-xl border border-white/20 bg-black/25 px-4 text-[15px] text-tcd09-ink placeholder:text-tcd09-mut/70 transition focus-visible:border-tcd09-acc2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd09-acc2/50 user-invalid:border-tcd09-danger">
          <button type="button" class="min-h-12 flex-[0_1_auto] cursor-pointer rounded-xl bg-gradient-to-r from-tcd09-acc to-tcd09-acc2 px-5 font-tcd09-display text-[15px] font-semibold text-tcd09-page shadow-[0_12px_30px_-12px_var(--color-tcd09-acc)] transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Join the waitlist</button>
          <p class="hidden w-full text-[12.5px] font-medium text-tcd09-danger peer-user-invalid:block">Enter a valid work email so we can send your invite.</p>
        </div>
        <div class="mt-2 flex flex-wrap items-center gap-3 text-[13px] text-tcd09-mut">
          <span aria-hidden="true" class="flex -space-x-2"><span class="size-7 rounded-full bg-tcd09-acc ring-2 ring-tcd09-page"></span><span class="size-7 rounded-full bg-tcd09-acc2 ring-2 ring-tcd09-page"></span><span class="size-7 rounded-full bg-tcd09-f3 ring-2 ring-tcd09-page"></span></span>
          <span><strong class="font-semibold text-tcd09-ink">3,418</strong> people already on the list · invites in batches of 250</span>
        </div>
      </div>

      <dl class="mt-7 grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-white/12 bg-white/12">
        <div class="bg-tcd09-page/70 px-4 py-3.5"><dt class="text-[11px] font-semibold uppercase tracking-[0.12em] text-tcd09-mut">Your position</dt><dd class="mt-1 font-tcd09-display text-2xl font-semibold tabular-nums">#1,204</dd></div>
        <div class="bg-tcd09-page/70 px-4 py-3.5"><dt class="text-[11px] font-semibold uppercase tracking-[0.12em] text-tcd09-mut">Each referral</dt><dd class="mt-1 font-tcd09-display text-2xl font-semibold tabular-nums text-tcd09-acc2">−40 places</dd></div>
      </dl>
    </div>

    <aside role="timer" aria-label="Countdown to first invite batch" class="relative min-w-0 overflow-hidden rounded-3xl border border-white/15 bg-tcd09-solid p-[clamp(20px,4vw,32px)] text-center supports-[backdrop-filter:blur(1px)]:bg-white/5 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl transition delay-150 duration-700 starting:translate-y-3 starting:opacity-0">
      <p class="text-xs font-semibold uppercase tracking-[0.16em] text-tcd09-mut">First batch goes out in</p>
      <p aria-hidden="true" class="mt-4 flex justify-center gap-[clamp(10px,3vw,18px)] font-tcd09-display font-medium tabular-nums">
        <span class="grid gap-1.5"><span class="text-[clamp(40px,10vw,56px)] leading-none tracking-[-0.04em]"><em class="not-italic animate-tcd09-h [counter-reset:tcd09h_var(--tcd09-h)] before:content-[counter(tcd09h)]"></em></span><i class="text-[10.5px] not-italic uppercase tracking-[0.18em] text-tcd09-mut">hrs</i></span>
        <span class="grid gap-1.5"><span class="text-[clamp(40px,10vw,56px)] leading-none tracking-[-0.04em]"><em class="not-italic animate-tcd09-mt [counter-reset:tcd09mt_var(--tcd09-mt)] before:content-[counter(tcd09mt)]"></em><em class="not-italic animate-tcd09-mu [counter-reset:tcd09mu_var(--tcd09-mu)] before:content-[counter(tcd09mu)]"></em></span><i class="text-[10.5px] not-italic uppercase tracking-[0.18em] text-tcd09-mut">min</i></span>
        <span class="grid gap-1.5"><span class="text-[clamp(40px,10vw,56px)] leading-none tracking-[-0.04em] text-tcd09-acc2"><em class="not-italic animate-tcd09-st [counter-reset:tcd09st_var(--tcd09-st)] before:content-[counter(tcd09st)]"></em><em class="not-italic animate-tcd09-su [counter-reset:tcd09su_var(--tcd09-su)] before:content-[counter(tcd09su)]"></em></span><i class="text-[10.5px] not-italic uppercase tracking-[0.18em] text-tcd09-mut">sec</i></span>
      </p>
      <p class="mx-auto mt-5 max-w-[30ch] text-[12.5px] leading-relaxed text-tcd09-mut text-pretty">Batch window <time datetime="PT3H">3 hours</time> · the timer is supporting chrome, the list is the point.</p>
      <div role="status" class="invisible absolute inset-0 grid place-content-center gap-1 bg-tcd09-page/95 opacity-0 animate-tcd09-done">
        <strong class="font-tcd09-display text-2xl font-semibold text-tcd09-acc2">Invites are going out</strong>
        <span class="text-[13px] text-tcd09-mut">Check your inbox</span>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd09-h {
  syntax: '<integer>';
  inherits: false;
  initial-value: 2;
}

@property --tcd09-mt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd09-mu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --tcd09-st {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --tcd09-su {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@theme {
  --color-tcd09-page: #0a0618;
  --color-tcd09-page: oklch(0.14 0.06 295);
  --color-tcd09-solid: #1a1233;
  --color-tcd09-solid: oklch(0.22 0.07 295);
  --color-tcd09-ink: #f3eeff;
  --color-tcd09-ink: oklch(0.96 0.02 300);
  --color-tcd09-mut: #b7abdb;
  --color-tcd09-mut: oklch(0.78 0.06 300);
  --color-tcd09-acc: #9b6bff;
  --color-tcd09-acc: oklch(0.7 0.2 295);
  --color-tcd09-acc2: #35e0e8;
  --color-tcd09-acc2: oklch(0.84 0.14 195);
  --color-tcd09-danger: #ff8a94;
  --color-tcd09-danger: oklch(0.76 0.15 18);
  --color-tcd09-f1: #9b6bff;
  --color-tcd09-f2: #35e0e8;
  --color-tcd09-f3: #2b1a5e;
  --font-tcd09-display: 'Space Grotesk', system-ui, sans-serif;
  --font-tcd09-sans: 'Geist', system-ui, sans-serif;
  --animate-tcd09-h: tcd09-h 10800s steps(3, end) forwards;
  --animate-tcd09-mt: tcd09-mt 3600s steps(6, end) infinite;
  --animate-tcd09-mu: tcd09-mu 600s steps(10, end) infinite;
  --animate-tcd09-st: tcd09-st 60s steps(6, end) infinite;
  --animate-tcd09-su: tcd09-su 10s steps(10, end) infinite;
  --animate-tcd09-done: tcd09-done 0.01s linear 10800s forwards;

  @keyframes tcd09-h {
    from {
      --tcd09-h: 2;
    }

    to {
      --tcd09-h: -1;
    }
  }

  @keyframes tcd09-mt {
    from {
      --tcd09-mt: 5;
    }

    to {
      --tcd09-mt: -1;
    }
  }

  @keyframes tcd09-mu {
    from {
      --tcd09-mu: 9;
    }

    to {
      --tcd09-mu: -1;
    }
  }

  @keyframes tcd09-st {
    from {
      --tcd09-st: 5;
    }

    to {
      --tcd09-st: -1;
    }
  }

  @keyframes tcd09-su {
    from {
      --tcd09-su: 9;
    }

    to {
      --tcd09-su: -1;
    }
  }

  @keyframes tcd09-done {
    to {
      opacity: 1;
      visibility: visible;
    }
  }
}

.tcd-09 {
  width: 100%;
  min-height: 100svh;
}
```
