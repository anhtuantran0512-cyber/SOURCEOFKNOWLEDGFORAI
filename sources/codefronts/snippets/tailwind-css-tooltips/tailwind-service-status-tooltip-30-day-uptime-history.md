---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-service-status-tooltip-30-day-uptime-history/"
title: "Tailwind Service Status Tooltip with 30-Day Uptime History"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A status list where each service dot pulses with its state and hovering a row opens a side card: 30-day uptime bars, three live metrics and the last incident."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Service Status Tooltip with 30-Day Uptime History
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-service-status-tooltip-30-day-uptime-history/

A status list where each service dot pulses with its state and hovering a row opens a side card: 30-day uptime bars, three live metrics and the last incident. The port's lesson is the opposite of clever &mdash; 120 uptime bars is where @apply beats repeating twelve utilities, and the per-bar colour and height stay inline because they are data.
## HTML
```html
<section class="ttp-08 w-full min-h-svh bg-ttp08-bg py-9 pr-[320px] pl-7 font-ttp08-mono max-xl:pr-7">
  <div class="mx-auto max-w-[440px]">

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp08-s1" class="flex cursor-help items-center gap-3 border-b border-white/6 py-2.75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp08-ok">
        <span class="h-2.25 w-2.25 shrink-0 rounded-full bg-ttp08-ok shadow-[0_0_6px_rgba(63,185,80,0.5)] animate-ttp08-pulse motion-reduce:animate-none"></span>
        <span class="flex-1 text-[12.5px] tracking-[0.02em] text-ttp08-ink">API Gateway</span>
        <span class="text-[11px] text-ttp08-dim">99.98%</span>
      </div>
      <span id="ttp08-s1" role="tooltip" class="ttp08-card">
        <span class="flex items-center gap-2.5 border-b border-white/6 px-3.5 pt-3 pb-2.5"><span class="h-2 w-2 shrink-0 rounded-full bg-ttp08-ok"></span><span class="flex-1 text-[12.5px] text-ttp08-bright">API Gateway</span><span class="rounded-full border border-ttp08-ok/25 bg-ttp08-ok/15 px-1.75 py-0.5 text-[9.5px] font-medium tracking-[0.06em] text-ttp08-ok">Operational</span></span>
        <span class="block px-3.5 pt-2.5 pb-1.25 text-[9px] uppercase tracking-[0.1em] text-ttp08-dim">30-day uptime</span>
        <span class="flex h-8.5 items-end gap-0.5 px-3.5 pb-2.5"><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-[80%]"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-warn h-[60%]"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i></span>
        <span class="grid grid-cols-3 border-t border-white/6">
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Uptime</span><span class="block text-[12.5px] text-ttp08-ok">99.98%</span></span>
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">p95 latency</span><span class="block text-[12.5px] text-ttp08-ink">38ms</span></span>
          <span class="block px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Req/min</span><span class="block text-[12.5px] text-ttp08-ink">12.4k</span></span>
        </span>
        <span class="block border-t border-white/6 px-3.5 py-2.25 font-ttp08-sans text-[10.5px] leading-[1.5] text-ttp08-dim">Last incident: <strong class="font-medium text-ttp08-ink">Feb 14 · 18 min partial degradation</strong> — elevated error rates on /auth endpoints. Resolved.</span>
      </span>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp08-s2" class="flex cursor-help items-center gap-3 border-b border-white/6 py-2.75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp08-ok">
        <span class="h-2.25 w-2.25 shrink-0 rounded-full bg-ttp08-ok shadow-[0_0_6px_rgba(63,185,80,0.5)] animate-ttp08-pulse motion-reduce:animate-none"></span>
        <span class="flex-1 text-[12.5px] tracking-[0.02em] text-ttp08-ink">Auth Service</span>
        <span class="text-[11px] text-ttp08-dim">100.00%</span>
      </div>
      <span id="ttp08-s2" role="tooltip" class="ttp08-card">
        <span class="flex items-center gap-2.5 border-b border-white/6 px-3.5 pt-3 pb-2.5"><span class="h-2 w-2 shrink-0 rounded-full bg-ttp08-ok"></span><span class="flex-1 text-[12.5px] text-ttp08-bright">Auth Service</span><span class="rounded-full border border-ttp08-ok/25 bg-ttp08-ok/15 px-1.75 py-0.5 text-[9.5px] font-medium tracking-[0.06em] text-ttp08-ok">Operational</span></span>
        <span class="block px-3.5 pt-2.5 pb-1.25 text-[9px] uppercase tracking-[0.1em] text-ttp08-dim">30-day uptime</span>
        <span class="flex h-8.5 items-end gap-0.5 px-3.5 pb-2.5"><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i></span>
        <span class="grid grid-cols-3 border-t border-white/6">
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Uptime</span><span class="block text-[12.5px] text-ttp08-ok">100%</span></span>
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">p95 latency</span><span class="block text-[12.5px] text-ttp08-ink">18ms</span></span>
          <span class="block px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Token/min</span><span class="block text-[12.5px] text-ttp08-ink">84k</span></span>
        </span>
        <span class="block border-t border-white/6 px-3.5 py-2.25 font-ttp08-sans text-[10.5px] leading-[1.5] text-ttp08-dim">No incidents in the last 90 days.</span>
      </span>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp08-s3" class="flex cursor-help items-center gap-3 border-b border-white/6 py-2.75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp08-ok">
        <span class="h-2.25 w-2.25 shrink-0 rounded-full bg-ttp08-ok shadow-[0_0_6px_rgba(63,185,80,0.5)] animate-ttp08-pulse motion-reduce:animate-none"></span>
        <span class="flex-1 text-[12.5px] tracking-[0.02em] text-ttp08-ink">PostgreSQL Primary</span>
        <span class="text-[11px] text-ttp08-dim">99.94%</span>
      </div>
      <span id="ttp08-s3" role="tooltip" class="ttp08-card">
        <span class="flex items-center gap-2.5 border-b border-white/6 px-3.5 pt-3 pb-2.5"><span class="h-2 w-2 shrink-0 rounded-full bg-ttp08-ok"></span><span class="flex-1 text-[12.5px] text-ttp08-bright">PostgreSQL Primary</span><span class="rounded-full border border-ttp08-ok/25 bg-ttp08-ok/15 px-1.75 py-0.5 text-[9.5px] font-medium tracking-[0.06em] text-ttp08-ok">Operational</span></span>
        <span class="block px-3.5 pt-2.5 pb-1.25 text-[9px] uppercase tracking-[0.1em] text-ttp08-dim">30-day uptime</span>
        <span class="flex h-8.5 items-end gap-0.5 px-3.5 pb-2.5"><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-down h-[40%]"></i><i class="ttp08-b bg-ttp08-warn h-[70%]"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i></span>
        <span class="grid grid-cols-3 border-t border-white/6">
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Uptime</span><span class="block text-[12.5px] text-ttp08-ok">99.94%</span></span>
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">p95 latency</span><span class="block text-[12.5px] text-ttp08-ink">6ms</span></span>
          <span class="block px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Conns</span><span class="block text-[12.5px] text-ttp08-ink">142/500</span></span>
        </span>
        <span class="block border-t border-white/6 px-3.5 py-2.25 font-ttp08-sans text-[10.5px] leading-[1.5] text-ttp08-dim">Last incident: <strong class="font-medium text-ttp08-ink">Mar 2 · 34 min outage</strong> — connection pool exhaustion during traffic spike. Failover to replica triggered.</span>
      </span>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp08-s4" class="flex cursor-help items-center gap-3 py-2.75 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp08-warn">
        <span class="h-2.25 w-2.25 shrink-0 rounded-full bg-ttp08-warn shadow-[0_0_6px_rgba(210,153,34,0.5)]"></span>
        <span class="flex-1 text-[12.5px] tracking-[0.02em] text-ttp08-ink">Email Delivery</span>
        <span class="text-[11px] text-ttp08-dim">98.42%</span>
      </div>
      <span id="ttp08-s4" role="tooltip" class="ttp08-card">
        <span class="flex items-center gap-2.5 border-b border-white/6 px-3.5 pt-3 pb-2.5"><span class="h-2 w-2 shrink-0 rounded-full bg-ttp08-warn"></span><span class="flex-1 text-[12.5px] text-ttp08-bright">Email Delivery</span><span class="rounded-full border border-ttp08-warn/25 bg-ttp08-warn/15 px-1.75 py-0.5 text-[9.5px] font-medium tracking-[0.06em] text-ttp08-warn">Degraded</span></span>
        <span class="block px-3.5 pt-2.5 pb-1.25 text-[9px] uppercase tracking-[0.1em] text-ttp08-dim">30-day uptime</span>
        <span class="flex h-8.5 items-end gap-0.5 px-3.5 pb-2.5"><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-warn h-[55%]"></i><i class="ttp08-b bg-ttp08-warn h-[50%]"></i><i class="ttp08-b bg-ttp08-down h-[30%]"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-ok h-full"></i><i class="ttp08-b bg-ttp08-warn h-[60%]"></i><i class="ttp08-b bg-ttp08-warn h-[55%]"></i><i class="ttp08-b bg-ttp08-warn h-[65%]"></i><i class="ttp08-b bg-ttp08-warn h-[58%]"></i><i class="ttp08-b bg-ttp08-warn h-[62%]"></i><i class="ttp08-b bg-ttp08-warn h-[57%]"></i><i class="ttp08-b bg-ttp08-warn h-[60%]"></i></span>
        <span class="grid grid-cols-3 border-t border-white/6">
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Uptime</span><span class="block text-[12.5px] text-ttp08-warn">98.42%</span></span>
          <span class="block border-r border-white/6 px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Delivery</span><span class="block text-[12.5px] text-ttp08-warn">91.3%</span></span>
          <span class="block px-3.25 py-2.5"><span class="mb-1 block text-[8px] uppercase tracking-[0.1em] text-ttp08-dim">Avg delay</span><span class="block text-[12.5px] text-ttp08-warn">340ms</span></span>
        </span>
        <span class="block border-t border-white/6 px-3.5 py-2.25 font-ttp08-sans text-[10.5px] leading-[1.5] text-ttp08-dim">Active: <strong class="font-medium text-ttp08-ink">Elevated bounce rates on Gmail / Yahoo</strong> — IP reputation issue with third-party relay. Investigation ongoing since May 11.</span>
      </span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp08-bg: #0d1117;
  --color-ttp08-bg: oklch(0.18 0.02 265);
  --color-ttp08-card: #161b22;
  --color-ttp08-card: oklch(0.22 0.02 265);
  --color-ttp08-bright: #eef2f6;
  --color-ttp08-bright: oklch(0.95 0.005 265);
  --color-ttp08-ink: #c2cad3;
  --color-ttp08-ink: oklch(0.83 0.012 265);
  --color-ttp08-dim: #99a3ae;
  --color-ttp08-dim: oklch(0.7 0.014 265);
  --color-ttp08-ok: #3fb950;
  --color-ttp08-ok: oklch(0.7 0.18 145);
  --color-ttp08-warn: #d29922;
  --color-ttp08-warn: oklch(0.71 0.14 82);
  --color-ttp08-down: #f85149;
  --color-ttp08-down: oklch(0.65 0.2 22);
  --font-ttp08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp08-sans: 'Inter', system-ui, sans-serif;
  --animate-ttp08-pulse: ttp08-pulse 2.5s ease-in-out infinite;
}

@keyframes ttp08-pulse {
  0%,
    100% {
    box-shadow: 0 0 6px rgba(63, 185, 80, 0.5);
  }

  50% {
    box-shadow: 0 0 14px rgba(63, 185, 80, 0.8);
  }
}

.ttp-08 {
  width: 100%;
  min-height: 100svh;
}
/* 120 uptime bars and four identical cards: the two places in this
   collection where repeating a class list would be noise rather than
   clarity. Data (height, state colour) still rides the element. */

.ttp-08 .ttp08-b {
  @apply block min-h-1 flex-1 rounded-[1px];
}

.ttp-08 .ttp08-card {
  @apply pointer-events-none invisible absolute top-1/2 left-[calc(100%+14px)] z-30 block w-70 -translate-y-1/2 translate-x-1.5 overflow-hidden rounded-[9px] border border-white/10 bg-ttp08-card text-left opacity-0 shadow-[0_16px_44px_rgba(0,0,0,0.8)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}
/* Under 1280px the stage drops its right gutter, so the card stacks
   under its row instead of overflowing the viewport. */

@media (max-width: 1279px) {
  .ttp-08 .ttp08-card {
    @apply static hidden w-full translate-x-0 translate-y-0 mt-2 group-hover:block group-focus-within:block;
  }
}
```
