---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-animated-gradient-border/"
title: "Tailwind Accordion with Animated Gradient Border"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A launch-week accordion on a near-black stage: closed days are quiet slots with a hairline seam; the open one ignites — a holographic conic gradient orbits…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion with Animated Gradient Border
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-animated-gradient-border/

A launch-week accordion on a near-black stage: closed days are quiet slots with a hairline seam; the open one ignites — a holographic conic gradient orbits its border, a blurred twin of the same gradient glows behind it, and an iridescent sheen sweeps once across its title. The angle is a registered @property animated only on the open item (zero idle cost); everything else, including the two-way height animation, is utilities on <details name>.
## HTML
```html
<section class="tac-23 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tac23-bg px-4 py-16 font-tac23-sans text-tac23-ink [interpolate-size:allow-keywords]" aria-label="Accordion with animated gradient border demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[linear-gradient(to_right,oklch(1_0_0/0.045)_1px,transparent_1px),linear-gradient(to_bottom,oklch(1_0_0/0.045)_1px,transparent_1px)] bg-[size:44px_44px] [mask-image:radial-gradient(70%_60%_at_50%_30%,#000,transparent)]"></div>
  <div aria-hidden="true" class="pointer-events-none absolute left-1/2 top-0 -z-10 h-72 w-[min(42rem,100%)] -translate-x-1/2 bg-[radial-gradient(closest-side,var(--color-tac23-haze),transparent)]"></div>

  <div class="grid w-full max-w-2xl gap-9">
    <header class="text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-white/5 px-3 py-1.5 font-tac23-mono text-[11.5px] tracking-[0.06em] text-tac23-mut ring-1 ring-white/10"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac23-c1 shadow-[0_0_10px_var(--color-tac23-c1)]"></span>Launch Week 04 · Oct 13–17</p>
      <h2 class="mt-5 text-[clamp(30px,5vw,44px)] leading-[1.05] font-bold tracking-[-0.035em] text-balance">Five days. Five ships.</h2>
      <p class="mx-auto mt-3 max-w-md text-[15px] leading-relaxed text-tac23-mut text-pretty">Everything we shipped for the Nova platform this week — open a day to see what's live.</p>
    </header>

    <div class="isolate grid gap-3">
      <div class="relative rounded-2xl before:pointer-events-none before:absolute before:-inset-px before:-z-10 before:rounded-[inherit] before:opacity-0 before:blur-2xl before:transition-opacity before:duration-700 before:[background:conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))] has-[[open]]:animate-tac23-spin has-[[open]]:before:opacity-55 motion-reduce:animate-none">
        <details name="tac23-day" class="group rounded-2xl border-[1.5px] border-white/10 bg-tac23-card transition-colors duration-300 hover:border-white/20 open:border-transparent open:[background:linear-gradient(var(--color-tac23-card),var(--color-tac23-card))_padding-box,conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))_border-box] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 rounded-[14px] px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac23-c1 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-xl bg-white/5 font-tac23-mono text-[13px] font-semibold text-tac23-mut ring-1 ring-white/10 transition-colors group-open:bg-tac23-c1/10 group-open:text-tac23-c1 group-open:ring-tac23-c1/30">01</span>
            <span class="min-w-0 flex-1">
              <span class="block font-tac23-mono text-[11px] tracking-[0.08em] uppercase text-tac23-mut">Monday · Day 1</span>
              <span class="mt-0.5 block text-[17px] font-semibold tracking-[-0.01em]"><span class="group-open:bg-[linear-gradient(100deg,var(--color-tac23-ink)_35%,var(--color-tac23-c1)_45%,var(--color-tac23-c2)_50%,var(--color-tac23-c3)_55%,var(--color-tac23-ink)_65%)] bg-[length:300%_100%] bg-[position:0%_0] group-open:bg-clip-text group-open:text-transparent group-open:animate-tac23-sheen motion-reduce:animate-none">Realtime Voice API</span></span>
            </span>
            <span class="hidden rounded-full bg-tac23-ok/12 px-2.5 py-1 font-tac23-mono text-[11px] font-medium text-tac23-ok ring-1 ring-tac23-ok/25 sm:inline">Live</span>
            <svg class="size-5 flex-none text-tac23-mut transition-transform duration-300 group-open:rotate-45 group-open:text-tac23-ink motion-reduce:transition-none" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M4 10h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-relaxed text-tac23-soft text-pretty">Stream speech in and out of any Nova model over a single WebSocket. Interruptions, turn detection and function calls work mid-sentence — no separate transcription step.</p>
            <dl class="mt-4 grid grid-cols-3 gap-2 font-tac23-mono">
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Latency</dt><dd class="mt-0.5 text-[15px] font-semibold">230 ms</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Voices</dt><dd class="mt-0.5 text-[15px] font-semibold">14</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Langs</dt><dd class="mt-0.5 text-[15px] font-semibold">38</dd></div>
            </dl>
          </div>
        </details>
      </div>

      <div class="relative rounded-2xl before:pointer-events-none before:absolute before:-inset-px before:-z-10 before:rounded-[inherit] before:opacity-0 before:blur-2xl before:transition-opacity before:duration-700 before:[background:conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))] has-[[open]]:animate-tac23-spin has-[[open]]:before:opacity-55 motion-reduce:animate-none">
        <details name="tac23-day" class="group rounded-2xl border-[1.5px] border-white/10 bg-tac23-card transition-colors duration-300 hover:border-white/20 open:border-transparent open:[background:linear-gradient(var(--color-tac23-card),var(--color-tac23-card))_padding-box,conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))_border-box] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 rounded-[14px] px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac23-c1 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-xl bg-white/5 font-tac23-mono text-[13px] font-semibold text-tac23-mut ring-1 ring-white/10 transition-colors group-open:bg-tac23-c1/10 group-open:text-tac23-c1 group-open:ring-tac23-c1/30">02</span>
            <span class="min-w-0 flex-1">
              <span class="block font-tac23-mono text-[11px] tracking-[0.08em] uppercase text-tac23-mut">Tuesday · Day 2</span>
              <span class="mt-0.5 block text-[17px] font-semibold tracking-[-0.01em]"><span class="group-open:bg-[linear-gradient(100deg,var(--color-tac23-ink)_35%,var(--color-tac23-c1)_45%,var(--color-tac23-c2)_50%,var(--color-tac23-c3)_55%,var(--color-tac23-ink)_65%)] bg-[length:300%_100%] bg-[position:0%_0] group-open:bg-clip-text group-open:text-transparent group-open:animate-tac23-sheen motion-reduce:animate-none">Agents SDK 2.0</span></span>
            </span>
            <span class="hidden rounded-full bg-tac23-ok/12 px-2.5 py-1 font-tac23-mono text-[11px] font-medium text-tac23-ok ring-1 ring-tac23-ok/25 sm:inline">Live</span>
            <svg class="size-5 flex-none text-tac23-mut transition-transform duration-300 group-open:rotate-45 group-open:text-tac23-ink motion-reduce:transition-none" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M4 10h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-relaxed text-tac23-soft text-pretty">Durable agents that survive restarts: every tool call is checkpointed, so a run can pause for human approval on Friday and resume on Monday exactly where it stopped.</p>
            <dl class="mt-4 grid grid-cols-3 gap-2 font-tac23-mono">
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Runtimes</dt><dd class="mt-0.5 text-[15px] font-semibold">TS · Py</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Tools</dt><dd class="mt-0.5 text-[15px] font-semibold">MCP</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Max run</dt><dd class="mt-0.5 text-[15px] font-semibold">30 days</dd></div>
            </dl>
          </div>
        </details>
      </div>

      <div class="relative rounded-2xl before:pointer-events-none before:absolute before:-inset-px before:-z-10 before:rounded-[inherit] before:opacity-0 before:blur-2xl before:transition-opacity before:duration-700 before:[background:conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))] has-[[open]]:animate-tac23-spin has-[[open]]:before:opacity-55 motion-reduce:animate-none">
        <details name="tac23-day" class="group rounded-2xl border-[1.5px] border-white/10 bg-tac23-card transition-colors duration-300 hover:border-white/20 open:border-transparent open:[background:linear-gradient(var(--color-tac23-card),var(--color-tac23-card))_padding-box,conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))_border-box] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 rounded-[14px] px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac23-c1 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-xl bg-white/5 font-tac23-mono text-[13px] font-semibold text-tac23-mut ring-1 ring-white/10 transition-colors group-open:bg-tac23-c1/10 group-open:text-tac23-c1 group-open:ring-tac23-c1/30">03</span>
            <span class="min-w-0 flex-1">
              <span class="block font-tac23-mono text-[11px] tracking-[0.08em] uppercase text-tac23-mut">Wednesday · Day 3</span>
              <span class="mt-0.5 block text-[17px] font-semibold tracking-[-0.01em]"><span class="group-open:bg-[linear-gradient(100deg,var(--color-tac23-ink)_35%,var(--color-tac23-c1)_45%,var(--color-tac23-c2)_50%,var(--color-tac23-c3)_55%,var(--color-tac23-ink)_65%)] bg-[length:300%_100%] bg-[position:0%_0] group-open:bg-clip-text group-open:text-transparent group-open:animate-tac23-sheen motion-reduce:animate-none">Fine-tuning on your own GPUs</span></span>
            </span>
            <span class="hidden rounded-full bg-tac23-ok/12 px-2.5 py-1 font-tac23-mono text-[11px] font-medium text-tac23-ok ring-1 ring-tac23-ok/25 sm:inline">Live</span>
            <svg class="size-5 flex-none text-tac23-mut transition-transform duration-300 group-open:rotate-45 group-open:text-tac23-ink motion-reduce:transition-none" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M4 10h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-relaxed text-tac23-soft text-pretty">Bring a Kubernetes cluster and a dataset; Nova schedules LoRA or full fine-tunes on your hardware and streams eval curves back to the dashboard. Weights never leave your VPC.</p>
            <dl class="mt-4 grid grid-cols-3 gap-2 font-tac23-mono">
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">GPUs</dt><dd class="mt-0.5 text-[15px] font-semibold">H100+</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Methods</dt><dd class="mt-0.5 text-[15px] font-semibold">LoRA</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Egress</dt><dd class="mt-0.5 text-[15px] font-semibold">Zero</dd></div>
            </dl>
          </div>
        </details>
      </div>

      <div class="relative rounded-2xl before:pointer-events-none before:absolute before:-inset-px before:-z-10 before:rounded-[inherit] before:opacity-0 before:blur-2xl before:transition-opacity before:duration-700 before:[background:conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))] has-[[open]]:animate-tac23-spin has-[[open]]:before:opacity-55 motion-reduce:animate-none">
        <details name="tac23-day" class="group rounded-2xl border-[1.5px] border-white/10 bg-tac23-card transition-colors duration-300 hover:border-white/20 open:border-transparent open:[background:linear-gradient(var(--color-tac23-card),var(--color-tac23-card))_padding-box,conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))_border-box] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 rounded-[14px] px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac23-c1 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-xl bg-white/5 font-tac23-mono text-[13px] font-semibold text-tac23-mut ring-1 ring-white/10 transition-colors group-open:bg-tac23-c1/10 group-open:text-tac23-c1 group-open:ring-tac23-c1/30">04</span>
            <span class="min-w-0 flex-1">
              <span class="block font-tac23-mono text-[11px] tracking-[0.08em] uppercase text-tac23-mut">Thursday · Day 4</span>
              <span class="mt-0.5 block text-[17px] font-semibold tracking-[-0.01em]"><span class="group-open:bg-[linear-gradient(100deg,var(--color-tac23-ink)_35%,var(--color-tac23-c1)_45%,var(--color-tac23-c2)_50%,var(--color-tac23-c3)_55%,var(--color-tac23-ink)_65%)] bg-[length:300%_100%] bg-[position:0%_0] group-open:bg-clip-text group-open:text-transparent group-open:animate-tac23-sheen motion-reduce:animate-none">Edge inference in 31 regions</span></span>
            </span>
            <span class="hidden rounded-full bg-tac23-ok/12 px-2.5 py-1 font-tac23-mono text-[11px] font-medium text-tac23-ok ring-1 ring-tac23-ok/25 sm:inline">Live</span>
            <svg class="size-5 flex-none text-tac23-mut transition-transform duration-300 group-open:rotate-45 group-open:text-tac23-ink motion-reduce:transition-none" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M4 10h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-relaxed text-tac23-soft text-pretty">Small models now run at the edge, within 50 ms of 94% of the world's internet users. Requests route to the nearest healthy region automatically.</p>
            <dl class="mt-4 grid grid-cols-3 gap-2 font-tac23-mono">
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Regions</dt><dd class="mt-0.5 text-[15px] font-semibold">31</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">p50 TTFT</dt><dd class="mt-0.5 text-[15px] font-semibold">41 ms</dd></div>
              <div class="rounded-xl bg-white/[0.04] px-3 py-2.5 ring-1 ring-white/8"><dt class="text-[10.5px] tracking-[0.06em] uppercase text-tac23-mut">Uptime</dt><dd class="mt-0.5 text-[15px] font-semibold">99.99%</dd></div>
            </dl>
          </div>
        </details>
      </div>

      <div class="relative rounded-2xl before:pointer-events-none before:absolute before:-inset-px before:-z-10 before:rounded-[inherit] before:opacity-0 before:blur-2xl before:transition-opacity before:duration-700 before:[background:conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))] has-[[open]]:animate-tac23-spin has-[[open]]:before:opacity-55 motion-reduce:animate-none">
        <details name="tac23-day" class="group rounded-2xl border-[1.5px] border-white/10 bg-tac23-card transition-colors duration-300 hover:border-white/20 open:border-transparent open:[background:linear-gradient(var(--color-tac23-card),var(--color-tac23-card))_padding-box,conic-gradient(from_var(--tac23-a),var(--color-tac23-c1),var(--color-tac23-c2),var(--color-tac23-c3),var(--color-tac23-c4),var(--color-tac23-c1))_border-box] details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-4 rounded-[14px] px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tac23-c1 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="grid size-11 flex-none place-items-center rounded-xl bg-white/5 font-tac23-mono text-[13px] font-semibold text-tac23-mut ring-1 ring-white/10 transition-colors group-open:bg-tac23-c1/10 group-open:text-tac23-c1 group-open:ring-tac23-c1/30">05</span>
            <span class="min-w-0 flex-1">
              <span class="block font-tac23-mono text-[11px] tracking-[0.08em] uppercase text-tac23-mut">Friday · Day 5</span>
              <span class="mt-0.5 block text-[17px] font-semibold tracking-[-0.01em]"><span class="group-open:bg-[linear-gradient(100deg,var(--color-tac23-ink)_35%,var(--color-tac23-c1)_45%,var(--color-tac23-c2)_50%,var(--color-tac23-c3)_55%,var(--color-tac23-ink)_65%)] bg-[length:300%_100%] bg-[position:0%_0] group-open:bg-clip-text group-open:text-transparent group-open:animate-tac23-sheen motion-reduce:animate-none">One more thing…</span></span>
            </span>
            <span class="hidden rounded-full bg-white/5 px-2.5 py-1 font-tac23-mono text-[11px] font-medium text-tac23-mut ring-1 ring-white/10 sm:inline">Fri 10am PT</span>
            <svg class="size-5 flex-none text-tac23-mut transition-transform duration-300 group-open:rotate-45 group-open:text-tac23-ink motion-reduce:transition-none" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12M4 10h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[5.25rem] sm:pe-6">
            <p class="text-[14.5px] leading-relaxed text-tac23-soft text-pretty">We're keeping this one under wraps until the keynote. Here's a hint: it's the feature you've asked for most in every survey since 2024.</p>
            <p class="mt-4 inline-flex items-center gap-2 rounded-xl bg-white/[0.04] px-3 py-2.5 font-tac23-mono text-[12.5px] text-tac23-soft ring-1 ring-white/8"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac23-c3 shadow-[0_0_10px_var(--color-tac23-c3)]"></span>Livestream starts Friday, 10:00 PT</p>
          </div>
        </details>
      </div>
    </div>

    <p aria-hidden="true" class="mx-auto max-w-full rounded-full px-3.5 py-2 text-center font-tac23-mono text-[11.5px] text-tac23-mut ring-1 ring-white/10">@property &lt;angle&gt; · has-[[open]]:animate-tac23-spin · padding-box / border-box</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac23-bg: #08080b;
  --color-tac23-bg: oklch(0.13 0.006 285);
  --color-tac23-haze: #3a2c6a59;
  --color-tac23-haze: oklch(0.35 0.1 290 / 0.35);
  --color-tac23-card: #111116;
  --color-tac23-card: oklch(0.18 0.008 285);
  --color-tac23-ink: #f4f4f7;
  --color-tac23-ink: oklch(0.97 0.004 285);
  --color-tac23-soft: #cfcfd8;
  --color-tac23-soft: oklch(0.86 0.012 285);
  --color-tac23-mut: #9d9daa;
  --color-tac23-mut: oklch(0.72 0.016 285);
  --color-tac23-ok: #5ee0a0;
  --color-tac23-ok: oklch(0.82 0.15 160);
  --color-tac23-c1: #5ce1f2;
  --color-tac23-c1: oklch(0.84 0.13 205);
  --color-tac23-c2: #a78bfa;
  --color-tac23-c2: oklch(0.71 0.16 295);
  --color-tac23-c3: #f472b6;
  --color-tac23-c3: oklch(0.73 0.18 350);
  --color-tac23-c4: #fcd34d;
  --color-tac23-c4: oklch(0.88 0.15 90);
  --font-tac23-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tac23-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tac23-spin: tac23-spin 4s linear infinite;
  --animate-tac23-sheen: tac23-sheen 1.4s cubic-bezier(0.3, 0.6, 0.2, 1) forwards;

  @keyframes tac23-spin {
    to {
      --tac23-a: 360deg;
    }
  }

  @keyframes tac23-sheen {
    from {
      background-position: 100% 0;
    }

    to {
      background-position: 0% 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-23 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the conic angle interpolates; inherits:true lets the details border and the
   wrapper's before: glow read the angle the wrapper animates. No utility exists for an at-rule. */

@property --tac23-a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}
```
