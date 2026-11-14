---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-scheduled-maintenance-countdown-status-page/"
title: "Tailwind Scheduled Maintenance Countdown Status Page"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A scheduled-maintenance card that counts down to the window opening, then hands over to a second clock counting down to it closing &mdash; with per-service…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scheduled Maintenance Countdown Status Page
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-scheduled-maintenance-countdown-status-page/

A scheduled-maintenance card that counts down to the window opening, then hands over to a second clock counting down to it closing &mdash; with per-service impact beside it, because during a window the only question is what still works. The port prints each clock with one counter in decimal-leading-zero, and a phase rail plus status pill now advance on schedule with zero JavaScript.
## HTML
```html
<section class="tcd-14 w-full min-h-svh bg-tcd14-page font-tcd14-sans text-tcd14-ink antialiased" aria-labelledby="tcd-14-title">
  <div class="mx-auto grid min-h-svh max-w-[820px] content-center gap-5 px-[clamp(16px,4vw,44px)] py-14">
    <header class="flex flex-wrap items-center justify-between gap-3">
      <p class="flex items-center gap-2 text-sm font-semibold"><span aria-hidden="true" class="grid size-6 place-items-center rounded-md bg-tcd14-acc font-tcd14-mono text-[11px] font-bold text-tcd14-page">T</span>Talon status</p>
      <span class="relative grid rounded-full border border-tcd14-acc/40 bg-tcd14-acc/10 px-3 py-1.5 text-xs font-semibold text-tcd14-acc">
        <span class="col-start-1 row-start-1 animate-tcd14-p1">Scheduled maintenance</span>
        <span class="col-start-1 row-start-1 opacity-0 animate-tcd14-p2">Maintenance in progress</span>
        <span class="col-start-1 row-start-1 text-tcd14-ok opacity-0 animate-tcd14-p3">Completed · all systems normal</span>
      </span>
    </header>

    <article class="rounded-2xl border border-tcd14-rule bg-tcd14-card p-[clamp(18px,4vw,30px)] shadow-[0_40px_80px_-50px_rgb(0_0_0/0.9)]">
      <h2 id="tcd-14-title" class="mb-1.5 text-[clamp(20px,3.6vw,26px)] font-semibold leading-tight tracking-[-0.015em] text-balance">Primary database failover · region eu-west</h2>
      <p class="mb-6 font-tcd14-mono text-[12.5px] text-tcd14-mut"><time datetime="2026-08-22T01:00:00Z">Sat 22 Aug, 01:00 UTC</time> → <time datetime="2026-08-22T02:30:00Z">02:30 UTC</time> · <time datetime="PT90M">90 min</time></p>

      <div aria-hidden="true" class="mb-4 grid grid-cols-[8fr_9fr] gap-1.5">
        <span class="h-1.5 overflow-hidden rounded-full bg-tcd14-rule"><span class="block h-full origin-left bg-tcd14-mut animate-tcd14-ra"></span></span>
        <span class="h-1.5 overflow-hidden rounded-full bg-tcd14-rule"><span class="block h-full origin-left scale-x-0 bg-tcd14-acc animate-tcd14-rb"></span></span>
      </div>

      <div role="timer" aria-label="Maintenance window countdown" class="grid gap-3 sm:grid-cols-2">
        <div class="rounded-xl border border-tcd14-rule bg-tcd14-sunk p-4 animate-tcd14-fa">
          <p class="text-[11px] font-semibold uppercase tracking-[0.14em] text-tcd14-mut">Window opens in</p>
          <p aria-hidden="true" class="my-2 font-tcd14-mono text-[clamp(34px,7vw,46px)] font-semibold leading-none tracking-[-0.03em] tabular-nums"><em class="not-italic animate-tcd14-am [counter-reset:tcd14am_var(--tcd14-am)] before:content-[counter(tcd14am,decimal-leading-zero)]"></em><span class="text-tcd14-mut">:</span><em class="not-italic animate-tcd14-as [counter-reset:tcd14as_var(--tcd14-as)] before:content-[counter(tcd14as,decimal-leading-zero)]"></em></p>
          <p class="text-[12.5px] leading-relaxed text-tcd14-mut">Finish long-running exports before this reaches zero.</p>
        </div>
        <div class="rounded-xl border border-tcd14-rule bg-tcd14-sunk p-4 opacity-50 animate-tcd14-fb">
          <p class="text-[11px] font-semibold uppercase tracking-[0.14em] text-tcd14-acc">Window closes in</p>
          <p aria-hidden="true" class="my-2 font-tcd14-mono text-[clamp(34px,7vw,46px)] font-semibold leading-none tracking-[-0.03em] tabular-nums"><em class="not-italic animate-tcd14-bm [counter-reset:tcd14bm_var(--tcd14-bm)] before:content-[counter(tcd14bm,decimal-leading-zero)]"></em><span class="text-tcd14-mut">:</span><em class="not-italic animate-tcd14-bs [counter-reset:tcd14bs_var(--tcd14-bs)] before:content-[counter(tcd14bs,decimal-leading-zero)]"></em></p>
          <p class="text-[12.5px] leading-relaxed text-tcd14-mut">Failover in progress. Writes resume automatically when this reaches zero.</p>
        </div>
      </div>

      <h3 class="mt-7 mb-2 text-[11px] font-semibold uppercase tracking-[0.14em] text-tcd14-mut">Service impact during the window</h3>
      <dl class="divide-y divide-tcd14-rule overflow-hidden rounded-xl border border-tcd14-rule">
        <div class="grid gap-1 px-4 py-3 sm:grid-cols-[180px_minmax(0,1fr)] sm:gap-4"><dt class="text-sm font-semibold">API · writes</dt><dd data-impact="down" class="flex items-start gap-2 text-[13px] text-tcd14-mut before:mt-1.5 before:size-2 before:flex-none before:rounded-full before:bg-current before:content-[''] data-[impact=down]:text-tcd14-down data-[impact=ok]:text-tcd14-ok data-[impact=partial]:text-tcd14-acc"><span class="text-tcd14-ink/85">Rejected with 503 for the full window</span></dd></div>
        <div class="grid gap-1 px-4 py-3 sm:grid-cols-[180px_minmax(0,1fr)] sm:gap-4"><dt class="text-sm font-semibold">API · reads</dt><dd data-impact="ok" class="flex items-start gap-2 text-[13px] text-tcd14-mut before:mt-1.5 before:size-2 before:flex-none before:rounded-full before:bg-current before:content-[''] data-[impact=down]:text-tcd14-down data-[impact=ok]:text-tcd14-ok data-[impact=partial]:text-tcd14-acc"><span class="text-tcd14-ink/85">Unaffected, served from replicas</span></dd></div>
        <div class="grid gap-1 px-4 py-3 sm:grid-cols-[180px_minmax(0,1fr)] sm:gap-4"><dt class="text-sm font-semibold">Dashboards</dt><dd data-impact="partial" class="flex items-start gap-2 text-[13px] text-tcd14-mut before:mt-1.5 before:size-2 before:flex-none before:rounded-full before:bg-current before:content-[''] data-[impact=down]:text-tcd14-down data-[impact=ok]:text-tcd14-ok data-[impact=partial]:text-tcd14-acc"><span class="text-tcd14-ink/85">Read-only, cached up to 5 minutes stale</span></dd></div>
        <div class="grid gap-1 px-4 py-3 sm:grid-cols-[180px_minmax(0,1fr)] sm:gap-4"><dt class="text-sm font-semibold">Scheduled exports</dt><dd data-impact="partial" class="flex items-start gap-2 text-[13px] text-tcd14-mut before:mt-1.5 before:size-2 before:flex-none before:rounded-full before:bg-current before:content-[''] data-[impact=down]:text-tcd14-down data-[impact=ok]:text-tcd14-ok data-[impact=partial]:text-tcd14-acc"><span class="text-tcd14-ink/85">Queued and replayed after the window</span></dd></div>
        <div class="grid gap-1 px-4 py-3 sm:grid-cols-[180px_minmax(0,1fr)] sm:gap-4"><dt class="text-sm font-semibold">Webhooks</dt><dd data-impact="partial" class="flex items-start gap-2 text-[13px] text-tcd14-mut before:mt-1.5 before:size-2 before:flex-none before:rounded-full before:bg-current before:content-[''] data-[impact=down]:text-tcd14-down data-[impact=ok]:text-tcd14-ok data-[impact=partial]:text-tcd14-acc"><span class="text-tcd14-ink/85">Retried with backoff for 24 hours</span></dd></div>
      </dl>
      <p class="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-[11.5px] text-tcd14-mut" aria-hidden="true"><span class="flex items-center gap-1.5"><span class="size-2 rounded-full bg-tcd14-down"></span>Unavailable</span><span class="flex items-center gap-1.5"><span class="size-2 rounded-full bg-tcd14-acc"></span>Degraded</span><span class="flex items-center gap-1.5"><span class="size-2 rounded-full bg-tcd14-ok"></span>Unaffected</span></p>

      <p class="mt-5 border-t border-tcd14-rule pt-4 text-[12px] leading-relaxed text-tcd14-mut text-pretty">Posted by Jordan Lee · updates every 15 minutes during the window. Counters are CSS-only, so they measure from render; a live page seeds both remaining durations from the server.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcd14-am {
  syntax: '<integer>';
  inherits: false;
  initial-value: 79;
}

@property --tcd14-as {
  syntax: '<integer>';
  inherits: false;
  initial-value: 59;
}

@property --tcd14-bm {
  syntax: '<integer>';
  inherits: false;
  initial-value: 90;
}

@property --tcd14-bs {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@theme {
  --color-tcd14-page: #14120f;
  --color-tcd14-page: oklch(0.18 0.008 70);
  --color-tcd14-card: #1c1a16;
  --color-tcd14-card: oklch(0.22 0.01 70);
  --color-tcd14-sunk: #23201b;
  --color-tcd14-sunk: oklch(0.25 0.012 70);
  --color-tcd14-ink: #f4f0e8;
  --color-tcd14-ink: oklch(0.95 0.012 80);
  --color-tcd14-mut: #aaa294;
  --color-tcd14-mut: oklch(0.72 0.02 78);
  --color-tcd14-rule: #2e2a23;
  --color-tcd14-rule: oklch(0.3 0.012 70);
  --color-tcd14-acc: #f0a92c;
  --color-tcd14-acc: oklch(0.79 0.15 75);
  --color-tcd14-ok: #63c98a;
  --color-tcd14-ok: oklch(0.77 0.14 152);
  --color-tcd14-down: #f2705f;
  --color-tcd14-down: oklch(0.7 0.16 30);
  --font-tcd14-sans: 'Geist', system-ui, sans-serif;
  --font-tcd14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tcd14-am: tcd14-am 4800s steps(80, end) forwards;
  --animate-tcd14-as: tcd14-as 60s steps(60, end) 80;
  --animate-tcd14-bm: tcd14-bm 5400s steps(90, end) 4800s forwards;
  --animate-tcd14-bs: tcd14-bs 60s steps(60, end) 4800s 90;
  --animate-tcd14-fa: tcd14-dim 0.6s ease 4800s forwards;
  --animate-tcd14-fb: tcd14-lift 0.6s ease 4800s forwards;
  --animate-tcd14-ra: tcd14-fill 4800s linear forwards;
  --animate-tcd14-rb: tcd14-fill 5400s linear 4800s forwards;
  --animate-tcd14-p1: tcd14-out 0.01s linear 4800s forwards;
  --animate-tcd14-p2: tcd14-in 0.01s linear 4800s forwards, tcd14-out 0.01s linear 10200s forwards;
  --animate-tcd14-p3: tcd14-in 0.01s linear 10200s forwards;

  @keyframes tcd14-am {
    from {
      --tcd14-am: 79;
    }

    to {
      --tcd14-am: -1;
    }
  }

  @keyframes tcd14-as {
    from {
      --tcd14-as: 59;
    }

    to {
      --tcd14-as: -1;
    }
  }

  @keyframes tcd14-bm {
    from {
      --tcd14-bm: 89;
    }

    to {
      --tcd14-bm: -1;
    }
  }

  @keyframes tcd14-bs {
    from {
      --tcd14-bs: 59;
    }

    to {
      --tcd14-bs: -1;
    }
  }

  @keyframes tcd14-dim {
    to {
      opacity: 0.5;
    }
  }

  @keyframes tcd14-lift {
    to {
      opacity: 1;
      border-color: var(--color-tcd14-acc);
    }
  }

  @keyframes tcd14-fill {
    from {
      transform: scaleX(0);
    }

    to {
      transform: scaleX(1);
    }
  }

  @keyframes tcd14-in {
    to {
      opacity: 1;
    }
  }

  @keyframes tcd14-out {
    to {
      opacity: 0;
    }
  }
}

.tcd-14 {
  width: 100%;
  min-height: 100svh;
}
```
