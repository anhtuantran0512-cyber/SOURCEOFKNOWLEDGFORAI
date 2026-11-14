---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-numbered-steps-accordion-onboarding/"
title: "Tailwind CSS Numbered Steps Accordion for Onboarding"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "An onboarding checklist that reads as a process: numbered badges joined by a connector line, a progress header, and one focal step at a time."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Numbered Steps Accordion for Onboarding
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-numbered-steps-accordion-onboarding/

An onboarding checklist that reads as a process: numbered badges joined by a connector line, a progress header, and one focal step at a time. Each step is a <details name="tac08-steps">; its connector segment is a before: pseudo-element on the item, completed steps carry a bare data-done attribute that turns their segment and badge blue via data-done:, and the open step's badge fills and gains a halo with group-open:.
## HTML
```html
<section class="tac-08 w-full min-h-svh grid place-items-center bg-tac08-bg bg-[radial-gradient(60%_45%_at_50%_0%,var(--color-tac08-glow),transparent_72%)] px-5 py-14 font-tac08-sans text-tac08-ink [interpolate-size:allow-keywords]" aria-label="Numbered steps onboarding accordion demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="w-full max-w-xl rounded-[28px] bg-tac08-card p-[clamp(20px,4.5vw,36px)] shadow-tac08-card ring-1 ring-tac08-ink/6">
      <header>
        <div class="flex items-start justify-between gap-4">
          <div class="min-w-0">
            <p class="text-xs font-bold tracking-[0.14em] uppercase text-tac08-acc-ink">Getting started</p>
            <h2 class="mt-2 text-[clamp(22px,3.6vw,27px)] leading-tight font-extrabold tracking-[-0.025em] text-balance">Set up Lumen in five steps</h2>
          </div>
          <span aria-hidden="true" class="grid size-12 flex-none place-items-center rounded-2xl bg-linear-to-br from-tac08-acc2 to-tac08-acc text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.3),0_10px_24px_-10px_var(--color-tac08-acc)]"><svg viewBox="0 0 24 24" width="24" height="24"><path d="M5 19V9M10 19V5M15 19v-7M20 19v-4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>
        </div>
        <div class="mt-6 rounded-2xl bg-tac08-soft p-4 ring-1 ring-tac08-line">
          <div class="flex items-baseline justify-between gap-3 text-sm"><span class="font-semibold">2 of 5 complete</span><span class="font-tac08-mono text-[12.5px] text-tac08-mut">about 9 min left</span></div>
          <div role="progressbar" aria-label="Onboarding progress" aria-valuemin="0" aria-valuemax="5" aria-valuenow="2" class="mt-3 h-2 overflow-hidden rounded-full bg-tac08-line">
            <div class="h-full w-[40%] rounded-full bg-linear-to-r from-tac08-acc2 to-tac08-acc"></div>
          </div>
        </div>
      </header>

      <div class="mt-6 grid">
        <details name="tac08-steps" data-done="true" class="group relative pb-1 before:absolute before:top-[52px] before:-bottom-1 before:left-5 before:w-0.5 before:-translate-x-1/2 before:rounded-full before:bg-tac08-line data-done:before:bg-tac08-acc details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl py-2 pe-2 outline-none focus-visible:ring-2 focus-visible:ring-tac08-acc focus-visible:ring-offset-4 focus-visible:ring-offset-tac08-card [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="relative z-10 grid size-10 flex-none place-items-center rounded-full bg-tac08-acc text-white shadow-[0_4px_12px_-4px_var(--color-tac08-acc)] transition-[scale,box-shadow] duration-300 group-open:scale-105 group-open:ring-4 group-open:ring-tac08-acc/15 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="18" height="18"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="min-w-0 flex-1 text-[16px] font-bold tracking-[-0.01em] text-tac08-mut transition-colors group-hover:text-tac08-ink group-open:text-tac08-acc-ink!"><span class="sr-only">Completed: </span>Create your workspace</span>
            <span class="flex-none rounded-full bg-tac08-acc/10 px-2.5 py-1 text-xs font-semibold text-tac08-acc-ink max-[420px]:hidden">Done</span>
            <svg aria-hidden="true" class="flex-none text-tac08-mut transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-4 ps-14 pe-2 pt-1">
            <p class="text-[14.5px] leading-relaxed text-tac08-body text-pretty">Your workspace lives at <span class="font-tac08-mono text-[13px] text-tac08-ink">lumen.app/harbor</span>. Everything is soft-deleted for 30 days, so explore freely.</p>
          </div>
        </details>
        <details name="tac08-steps" data-done="true" class="group relative pb-1 before:absolute before:top-[52px] before:-bottom-1 before:left-5 before:w-0.5 before:-translate-x-1/2 before:rounded-full before:bg-tac08-line data-done:before:bg-tac08-acc details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl py-2 pe-2 outline-none focus-visible:ring-2 focus-visible:ring-tac08-acc focus-visible:ring-offset-4 focus-visible:ring-offset-tac08-card [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="relative z-10 grid size-10 flex-none place-items-center rounded-full bg-tac08-acc text-white shadow-[0_4px_12px_-4px_var(--color-tac08-acc)] transition-[scale,box-shadow] duration-300 group-open:scale-105 group-open:ring-4 group-open:ring-tac08-acc/15 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="18" height="18"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="min-w-0 flex-1 text-[16px] font-bold tracking-[-0.01em] text-tac08-mut transition-colors group-hover:text-tac08-ink group-open:text-tac08-acc-ink!"><span class="sr-only">Completed: </span>Invite your teammates</span>
            <span class="flex-none rounded-full bg-tac08-acc/10 px-2.5 py-1 text-xs font-semibold text-tac08-acc-ink max-[420px]:hidden">Done</span>
            <svg aria-hidden="true" class="flex-none text-tac08-mut transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-4 ps-14 pe-2 pt-1">
            <p class="text-[14.5px] leading-relaxed text-tac08-body text-pretty">Priya and Jonas accepted their invites. Teammates you add later start as <strong class="font-semibold text-tac08-ink">Viewers</strong> until you promote them.</p>
          </div>
        </details>
        <details name="tac08-steps" open class="group relative pb-1 before:absolute before:top-[52px] before:-bottom-1 before:left-5 before:w-0.5 before:-translate-x-1/2 before:rounded-full before:bg-tac08-line data-done:before:bg-tac08-acc details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl py-2 pe-2 outline-none focus-visible:ring-2 focus-visible:ring-tac08-acc focus-visible:ring-offset-4 focus-visible:ring-offset-tac08-card [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="relative z-10 grid size-10 flex-none place-items-center rounded-full bg-tac08-card font-tac08-mono text-[13px] font-semibold text-tac08-mut ring-2 ring-tac08-line transition-[background-color,color,box-shadow,scale] duration-300 group-hover:text-tac08-acc group-hover:ring-tac08-acc/50 group-open:scale-105 group-open:bg-tac08-acc group-open:text-white! group-open:shadow-[0_0_0_6px_var(--color-tac08-halo),0_8px_18px_-6px_var(--color-tac08-acc)] group-open:ring-tac08-acc! motion-reduce:transition-none">03</span>
            <span class="min-w-0 flex-1 text-[16px] font-bold tracking-[-0.01em] text-tac08-ink transition-colors group-hover:text-tac08-ink group-open:text-tac08-acc-ink!">Connect your data</span>
            <span class="flex-none rounded-full bg-tac08-soft px-2.5 py-1 font-tac08-mono text-[11.5px] text-tac08-mut ring-1 ring-tac08-line max-[420px]:hidden">~3 min</span>
            <svg aria-hidden="true" class="flex-none text-tac08-mut transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-4 ps-14 pe-2 pt-1">
            <p class="text-[14.5px] leading-relaxed text-tac08-body text-pretty">OAuth into Snowflake, BigQuery or Postgres &mdash; or drop in a CSV. Schemas are inferred automatically and every column gets a profiling report.</p>
            <div class="mt-4 flex flex-wrap items-center gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tac08-acc px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.2),0_6px_16px_-6px_var(--color-tac08-acc)] transition-[background-color,translate] hover:-translate-y-px hover:bg-tac08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac08-acc motion-reduce:transition-none">Connect a source <span aria-hidden="true">→</span></button>
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl bg-tac08-card px-4 text-[13.5px] font-semibold text-tac08-ink ring-1 ring-tac08-line transition-colors hover:bg-tac08-soft focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac08-acc">Upload a CSV</button>
            </div>
          </div>
        </details>
        <details name="tac08-steps" class="group relative pb-1 before:absolute before:top-[52px] before:-bottom-1 before:left-5 before:w-0.5 before:-translate-x-1/2 before:rounded-full before:bg-tac08-line data-done:before:bg-tac08-acc details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl py-2 pe-2 outline-none focus-visible:ring-2 focus-visible:ring-tac08-acc focus-visible:ring-offset-4 focus-visible:ring-offset-tac08-card [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="relative z-10 grid size-10 flex-none place-items-center rounded-full bg-tac08-card font-tac08-mono text-[13px] font-semibold text-tac08-mut ring-2 ring-tac08-line transition-[background-color,color,box-shadow,scale] duration-300 group-hover:text-tac08-acc group-hover:ring-tac08-acc/50 group-open:scale-105 group-open:bg-tac08-acc group-open:text-white! group-open:shadow-[0_0_0_6px_var(--color-tac08-halo),0_8px_18px_-6px_var(--color-tac08-acc)] group-open:ring-tac08-acc! motion-reduce:transition-none">04</span>
            <span class="min-w-0 flex-1 text-[16px] font-bold tracking-[-0.01em] text-tac08-ink transition-colors group-hover:text-tac08-ink group-open:text-tac08-acc-ink!">Build your first dashboard</span>
            <span class="flex-none rounded-full bg-tac08-soft px-2.5 py-1 font-tac08-mono text-[11.5px] text-tac08-mut ring-1 ring-tac08-line max-[420px]:hidden">~5 min</span>
            <svg aria-hidden="true" class="flex-none text-tac08-mut transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-4 ps-14 pe-2 pt-1">
            <p class="text-[14.5px] leading-relaxed text-tac08-body text-pretty">Start from one of 40 templates or a blank canvas. Charts stay linked to their source queries, so refreshed data flows straight through.</p>
            <div class="mt-4 flex flex-wrap items-center gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tac08-acc px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.2),0_6px_16px_-6px_var(--color-tac08-acc)] transition-[background-color,translate] hover:-translate-y-px hover:bg-tac08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac08-acc motion-reduce:transition-none">Browse templates <span aria-hidden="true">→</span></button>
            </div>
          </div>
        </details>
        <details name="tac08-steps" class="group relative pb-1 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-2xl py-2 pe-2 outline-none focus-visible:ring-2 focus-visible:ring-tac08-acc focus-visible:ring-offset-4 focus-visible:ring-offset-tac08-card [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="relative z-10 grid size-10 flex-none place-items-center rounded-full bg-tac08-card font-tac08-mono text-[13px] font-semibold text-tac08-mut ring-2 ring-tac08-line transition-[background-color,color,box-shadow,scale] duration-300 group-hover:text-tac08-acc group-hover:ring-tac08-acc/50 group-open:scale-105 group-open:bg-tac08-acc group-open:text-white! group-open:shadow-[0_0_0_6px_var(--color-tac08-halo),0_8px_18px_-6px_var(--color-tac08-acc)] group-open:ring-tac08-acc! motion-reduce:transition-none">05</span>
            <span class="min-w-0 flex-1 text-[16px] font-bold tracking-[-0.01em] text-tac08-ink transition-colors group-hover:text-tac08-ink group-open:text-tac08-acc-ink!">Share it with your team</span>
            <span class="flex-none rounded-full bg-tac08-soft px-2.5 py-1 font-tac08-mono text-[11.5px] text-tac08-mut ring-1 ring-tac08-line max-[420px]:hidden">~1 min</span>
            <svg aria-hidden="true" class="flex-none text-tac08-mut transition-transform duration-300 group-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-4 ps-14 pe-2 pt-1">
            <p class="text-[14.5px] leading-relaxed text-tac08-body text-pretty">Publish to a link, embed in Notion, or schedule a Monday-morning email digest. Viewers never need a paid seat.</p>
            <div class="mt-4 flex flex-wrap items-center gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tac08-acc px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.2),0_6px_16px_-6px_var(--color-tac08-acc)] transition-[background-color,translate] hover:-translate-y-px hover:bg-tac08-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac08-acc motion-reduce:transition-none">Set up sharing <span aria-hidden="true">→</span></button>
            </div>
          </div>
        </details>
      </div>

      <footer class="mt-5 flex flex-wrap items-center gap-3 border-t border-tac08-line pt-5">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-linear-to-br from-[oklch(0.82_0.1_70)] to-[oklch(0.65_0.16_35)] text-sm font-bold text-white">MO</span>
        <p class="min-w-0 flex-1 text-sm text-tac08-mut"><span class="font-semibold text-tac08-ink">Stuck?</span> Maya from onboarding can walk you through it.</p>
        <button type="button" class="inline-flex min-h-11 items-center rounded-xl px-3 text-[13.5px] font-semibold text-tac08-acc-ink transition-colors hover:bg-tac08-soft focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac08-acc">Book 15 min</button>
      </footer>
    </article>
    <p aria-hidden="true" class="rounded-full bg-tac08-card/70 px-3.5 py-2 text-center font-tac08-mono text-[11.5px] text-tac08-mut ring-1 ring-tac08-ink/8">before:left-5 per-step connector · data-done: · group-open:bg-tac08-acc</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac08-bg: #f3f7fc;
  --color-tac08-bg: oklch(0.975 0.008 250);
  --color-tac08-glow: #daedff;
  --color-tac08-glow: oklch(0.94 0.04 255);
  --color-tac08-card: #ffffff;
  --color-tac08-card: oklch(1 0 0);
  --color-tac08-soft: #f4f8fe;
  --color-tac08-soft: oklch(0.977 0.01 255);
  --color-tac08-line: #dde3ed;
  --color-tac08-line: oklch(0.915 0.015 258);
  --color-tac08-ink: #131b29;
  --color-tac08-ink: oklch(0.22 0.03 262);
  --color-tac08-body: #3f4858;
  --color-tac08-body: oklch(0.4 0.03 262);
  --color-tac08-mut: #5a6475;
  --color-tac08-mut: oklch(0.5 0.03 262);
  --color-tac08-acc: #2c6be7;
  --color-tac08-acc: oklch(0.56 0.2 262);
  --color-tac08-acc-ink: #1f55c4;
  --color-tac08-acc-ink: oklch(0.49 0.19 262);
  --color-tac08-acc2: #249ff3;
  --color-tac08-acc2: oklch(0.68 0.16 245);
  --color-tac08-halo: #dce8ff;
  --color-tac08-halo: oklch(0.93 0.035 262);
  --font-tac08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tac08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tac08-card: 0 1px 2px oklch(0.3 0.04 262 / 0.06), 0 28px 64px -30px oklch(0.35 0.1 262 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-08 {
  width: 100%;
  min-height: 100svh;
}
```
