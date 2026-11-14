---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/smooth-animated-tailwind-accordion-height-transition/"
title: "Smooth Animated Tailwind Accordion with Height Transition"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The most-searched accordion problem, solved entirely in class lists: a native <details> changelog that slides open and closed with a real height: auto…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smooth Animated Tailwind Accordion with Height Transition
Source: https://codefronts.com/navigation/tailwind-css-accordions/smooth-animated-tailwind-accordion-height-transition/

The most-searched accordion problem, solved entirely in class lists: a native <details> changelog that slides open and closed with a real height: auto transition. Tailwind v4's details-content: variant styles the ::details-content box, [interpolate-size:allow-keywords] on the root makes auto animatable, and transition-discrete holds the content visible until the close finishes.
## HTML
```html
<section class="tac-05 w-full min-h-svh grid place-items-center bg-tac05-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tac05-glow),transparent_72%)] px-5 py-14 font-tac05-sans text-tac05-ink [interpolate-size:allow-keywords]" aria-label="Smooth animated accordion with height transition demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="w-full max-w-2xl rounded-[28px] bg-tac05-card p-[clamp(20px,4.5vw,36px)] shadow-tac05-card ring-1 ring-tac05-ink/6">
      <header class="mb-7 flex flex-wrap items-end justify-between gap-x-6 gap-y-4">
        <div class="min-w-0">
          <p class="inline-flex items-center gap-2 rounded-full bg-tac05-tint px-3 py-1 text-xs font-bold tracking-[0.08em] uppercase text-tac05-acc-ink ring-1 ring-tac05-acc/20">
            <span aria-hidden="true" class="relative flex size-2"><span class="absolute inset-0 animate-ping rounded-full bg-tac05-acc/60 motion-reduce:hidden"></span><span class="relative size-2 rounded-full bg-tac05-acc"></span></span>
            Changelog · Q3 2026
          </p>
          <h2 class="mt-3.5 text-[clamp(24px,3.8vw,31px)] leading-tight font-extrabold tracking-[-0.03em] text-balance">What shipped this quarter</h2>
          <p class="mt-1.5 text-[15px] text-tac05-mut">Three releases, forty-one fixes, zero breaking changes.</p>
        </div>
        <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-tac05-ink px-4.5 text-sm font-semibold text-white shadow-[0_1px_2px_oklch(0.2_0.02_170/0.3)] transition-[background-color,translate] duration-200 hover:-translate-y-px hover:bg-tac05-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac05-acc motion-reduce:transition-none">
          <svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16"><path d="M4 10.5a5.5 5.5 0 0 1 5.5 5.5M4 5a11 11 0 0 1 11 11" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="4.6" cy="15.4" r="1.4" fill="currentColor"/></svg>
          Subscribe
        </button>
      </header>

      <div class="grid gap-3">
        <details class="group rounded-2xl bg-tac05-card ring-1 ring-tac05-line transition-[background-color,box-shadow] duration-300 hover:ring-tac05-acc/30 open:bg-tac05-tint/45 open:shadow-tac05-open open:ring-tac05-acc/35 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac05-acc focus-visible:ring-offset-2 focus-visible:ring-offset-tac05-card sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="w-14 flex-none rounded-lg bg-tac05-acc/10 py-1 text-center font-tac05-mono text-xs font-semibold text-tac05-acc-ink ring-1 ring-tac05-acc/20 transition-colors duration-300 group-open:bg-tac05-acc-ink group-open:text-white group-open:ring-transparent">v3.4</span>
            <span class="min-w-0 flex-1">
              <span class="block text-base font-bold tracking-[-0.01em]">Realtime collaboration</span>
              <span class="mt-0.5 flex flex-wrap items-center gap-x-2 text-[13px] text-tac05-mut"><span>Sep 24</span><span class="inline-flex items-center gap-2 before:size-1 before:rounded-full before:bg-tac05-mut/50 before:content-[''] font-semibold text-tac05-acc-ink">New</span></span>
            </span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac05-ink/5 text-tac05-mut transition-[rotate,background-color,color] duration-300 group-open:rotate-180 group-open:bg-tac05-acc/15 group-open:text-tac05-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="translate-y-1.5 px-4 pb-5 transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)] group-open:translate-y-0 motion-reduce:transition-none sm:ps-[5.75rem] sm:pe-6">
            <p class="text-[15px] leading-relaxed text-tac05-body text-pretty">Multiplayer cursors, presence avatars and conflict-free co-editing landed across every document type. Sessions reconnect on their own, and offline edits merge cleanly when you're back.</p>
            <ul class="mt-3.5 grid gap-2 text-sm text-tac05-body">
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Live cursors with names and selection colours</li>
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>CRDT merge for documents, boards and tables</li>
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Offline queue keeps up to 2,000 pending edits</li>
            </ul>
          </div>
        </details>

        <details class="group rounded-2xl bg-tac05-card ring-1 ring-tac05-line transition-[background-color,box-shadow] duration-300 hover:ring-tac05-acc/30 open:bg-tac05-tint/45 open:shadow-tac05-open open:ring-tac05-acc/35 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac05-acc focus-visible:ring-offset-2 focus-visible:ring-offset-tac05-card sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="w-14 flex-none rounded-lg bg-tac05-acc/10 py-1 text-center font-tac05-mono text-xs font-semibold text-tac05-acc-ink ring-1 ring-tac05-acc/20 transition-colors duration-300 group-open:bg-tac05-acc-ink group-open:text-white group-open:ring-transparent">v3.3</span>
            <span class="min-w-0 flex-1">
              <span class="block text-base font-bold tracking-[-0.01em]">Command palette</span>
              <span class="mt-0.5 flex flex-wrap items-center gap-x-2 text-[13px] text-tac05-mut"><span>Aug 13</span><span class="inline-flex items-center gap-2 before:size-1 before:rounded-full before:bg-tac05-mut/50 before:content-[''] font-semibold text-tac05-acc-ink">New</span></span>
            </span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac05-ink/5 text-tac05-mut transition-[rotate,background-color,color] duration-300 group-open:rotate-180 group-open:bg-tac05-acc/15 group-open:text-tac05-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="translate-y-1.5 px-4 pb-5 transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)] group-open:translate-y-0 motion-reduce:transition-none sm:ps-[5.75rem] sm:pe-6">
            <p class="text-[15px] leading-relaxed text-tac05-body text-pretty">Press <kbd class="rounded-md bg-tac05-card px-1.5 py-0.5 font-tac05-mono text-xs font-semibold text-tac05-ink shadow-[0_1px_0_oklch(0.2_0.02_170/0.18)] ring-1 ring-tac05-line">⌘K</kbd> anywhere to search actions, files and people. Fuzzy matching, recent-first ranking and full keyboard operation come out of the box.</p>
            <ul class="mt-3.5 grid gap-2 text-sm text-tac05-body">
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Scoped search with <span class="font-tac05-mono text-[13px]">&gt;</span> for actions and <span class="font-tac05-mono text-[13px]">@</span> for people</li>
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Results in under 40 ms on workspaces with 100k files</li>
            </ul>
          </div>
        </details>

        <details class="group rounded-2xl bg-tac05-card ring-1 ring-tac05-line transition-[background-color,box-shadow] duration-300 hover:ring-tac05-acc/30 open:bg-tac05-tint/45 open:shadow-tac05-open open:ring-tac05-acc/35 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-500 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac05-acc focus-visible:ring-offset-2 focus-visible:ring-offset-tac05-card sm:px-5 [&::-webkit-details-marker]:hidden">
            <span class="w-14 flex-none rounded-lg bg-tac05-acc/10 py-1 text-center font-tac05-mono text-xs font-semibold text-tac05-acc-ink ring-1 ring-tac05-acc/20 transition-colors duration-300 group-open:bg-tac05-acc-ink group-open:text-white group-open:ring-transparent">v3.2</span>
            <span class="min-w-0 flex-1">
              <span class="block text-base font-bold tracking-[-0.01em]">Audit log export</span>
              <span class="mt-0.5 flex flex-wrap items-center gap-x-2 text-[13px] text-tac05-mut"><span>Jul 2</span><span class="inline-flex items-center gap-2 before:size-1 before:rounded-full before:bg-tac05-mut/50 before:content-[''] font-semibold text-tac05-ink">Enterprise</span></span>
            </span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac05-ink/5 text-tac05-mut transition-[rotate,background-color,color] duration-300 group-open:rotate-180 group-open:bg-tac05-acc/15 group-open:text-tac05-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="translate-y-1.5 px-4 pb-5 transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)] group-open:translate-y-0 motion-reduce:transition-none sm:ps-[5.75rem] sm:pe-6">
            <p class="text-[15px] leading-relaxed text-tac05-body text-pretty">Admins can stream audit events to S3 or download signed CSV exports. Retention is configurable per workspace, and SOC 2 evidence bundles are one click away.</p>
            <ul class="mt-3.5 grid gap-2 text-sm text-tac05-body">
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Hourly S3 delivery with SHA-256 manifests</li>
              <li class="flex items-start gap-2.5"><svg aria-hidden="true" class="mt-0.5 flex-none text-tac05-acc" viewBox="0 0 16 16" width="16" height="16"><path d="m3.5 8.5 3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Retention from 90 days to 7 years</li>
            </ul>
          </div>
        </details>
      </div>

      <footer class="mt-6 flex flex-wrap items-center justify-between gap-3 border-t border-tac05-line pt-5 text-sm text-tac05-mut">
        <span>Showing 3 of 28 releases</span>
        <button type="button" class="-mx-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-2 font-semibold text-tac05-acc-ink transition-colors hover:text-tac05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac05-acc">View full archive <span aria-hidden="true">→</span></button>
      </footer>
    </article>
    <p aria-hidden="true" class="rounded-full bg-tac05-card/70 px-3.5 py-2 text-center font-tac05-mono text-[11.5px] text-tac05-mut ring-1 ring-tac05-ink/8">details-content:h-0 · open:details-content:h-auto · [interpolate-size:allow-keywords]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac05-bg: #f3f8f6;
  --color-tac05-bg: oklch(0.975 0.006 165);
  --color-tac05-glow: #d8f7e6;
  --color-tac05-glow: oklch(0.95 0.04 162);
  --color-tac05-card: #ffffff;
  --color-tac05-card: oklch(1 0 0);
  --color-tac05-tint: #ebfaf2;
  --color-tac05-tint: oklch(0.975 0.022 162);
  --color-tac05-line: #e2e9e6;
  --color-tac05-line: oklch(0.93 0.008 170);
  --color-tac05-ink: #111e19;
  --color-tac05-ink: oklch(0.22 0.02 170);
  --color-tac05-body: #3a4843;
  --color-tac05-body: oklch(0.39 0.018 170);
  --color-tac05-mut: #505f59;
  --color-tac05-mut: oklch(0.47 0.02 170);
  --color-tac05-acc: #00a76f;
  --color-tac05-acc: oklch(0.64 0.15 162);
  --color-tac05-acc-ink: #00774d;
  --color-tac05-acc-ink: oklch(0.5 0.12 162);
  --font-tac05-sans: 'Manrope', system-ui, sans-serif;
  --font-tac05-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tac05-card: 0 1px 2px oklch(0.3 0.03 170 / 0.06), 0 24px 60px -28px oklch(0.35 0.06 165 / 0.3);
  --shadow-tac05-open: 0 1px 2px oklch(0.4 0.08 162 / 0.08), 0 14px 32px -16px oklch(0.5 0.12 162 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-05 {
  width: 100%;
  min-height: 100svh;
}
```
