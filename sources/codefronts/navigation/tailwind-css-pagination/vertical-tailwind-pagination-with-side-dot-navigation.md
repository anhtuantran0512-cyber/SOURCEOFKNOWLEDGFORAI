---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/vertical-tailwind-pagination-with-side-dot-navigation/"
title: "Vertical Tailwind Pagination with Side Dot Navigation"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A long-form plan guide that scrolls inside its own panel, with a vertical rail of labelled dots docked to its right edge."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tailwind Pagination with Side Dot Navigation
Source: https://codefronts.com/navigation/tailwind-css-pagination/vertical-tailwind-pagination-with-side-dot-navigation/

A long-form plan guide that scrolls inside its own panel, with a vertical rail of labelled dots docked to its right edge. A named scroll-timeline hoisted with timeline-scope drives the progress line from outside the scroller, a small observer moves aria-current as you read, and up/down keys step section by section. Where scroll timelines are missing, the same line snaps from dot to dot via group-has-[…]:.
## HTML
```html
<section class="tpg-17 w-full min-h-svh grid place-items-center bg-tpg17-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tpg17-glow),transparent_70%)] px-4 py-14 font-tpg17-sans text-tpg17-ink antialiased sm:px-5" aria-label="Vertical side dot pagination demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tpg-17-guide" data-card="" class="w-full max-w-[52rem] overflow-hidden rounded-[1.25rem] bg-tpg17-card shadow-tpg17-card ring-1 ring-tpg17-line">
      <header class="flex flex-wrap items-center justify-between gap-x-6 gap-y-1 border-b border-tpg17-line px-5 py-4 sm:px-8">
        <p class="text-sm font-semibold tracking-[-0.01em]">Northwind Cloud <span class="font-normal text-tpg17-mut">/ Team plan guide</span></p>
        <p class="font-tpg17-mono text-xs text-tpg17-mut tabular-nums">4 sections &middot; 6 min read</p>
      </header>
      <div class="grid grid-cols-[minmax(0,1fr)_auto]">
        <div data-pane="" tabindex="0" aria-label="Plan guide" class="relative h-[min(32rem,80svh)] snap-y snap-proximity overflow-y-auto overscroll-contain scroll-smooth focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg17-ring motion-reduce:scroll-auto [scrollbar-width:thin]">
          <section id="tpg-17-s1" data-sec="" aria-labelledby="tpg-17-h1" class="grid min-h-full snap-start content-center gap-4 border-b border-tpg17-line px-5 py-10 sm:px-10">
            <p class="font-tpg17-mono text-xs tracking-[0.12em] text-tpg17-acc tabular-nums">01 &mdash; OVERVIEW</p>
            <h2 id="tpg-17-h1" class="font-tpg17-serif text-[clamp(2rem,5vw,2.75rem)] leading-[1.05] tracking-[-0.01em]">Everything your team needs, <em class="bg-linear-to-r from-tpg17-acc to-tpg17-acc2 bg-clip-text pr-1 text-transparent">nothing it won&rsquo;t</em></h2>
            <p class="max-w-[34rem] text-[15px] leading-relaxed text-pretty text-tpg17-mut">The Team plan bundles hosting, preview deployments and audit logs for up to 25 seats. This guide walks through pricing, security and what changed this quarter &mdash; scroll the pane, or jump with the rail on the right.</p>
            <dl class="mt-2 grid max-w-[30rem] grid-cols-3 gap-px overflow-hidden rounded-xl bg-tpg17-line ring-1 ring-tpg17-line">
              <div class="bg-tpg17-card px-4 py-3"><dt class="text-xs text-tpg17-mut">Seats</dt><dd class="mt-0.5 text-lg font-semibold tabular-nums">25</dd></div>
              <div class="bg-tpg17-card px-4 py-3"><dt class="text-xs text-tpg17-mut">Regions</dt><dd class="mt-0.5 text-lg font-semibold tabular-nums">14</dd></div>
              <div class="bg-tpg17-card px-4 py-3"><dt class="text-xs text-tpg17-mut">Uptime</dt><dd class="mt-0.5 text-lg font-semibold tabular-nums">99.99%</dd></div>
            </dl>
          </section>
          <section id="tpg-17-s2" data-sec="" aria-labelledby="tpg-17-h2" class="grid min-h-full snap-start content-center gap-4 border-b border-tpg17-line px-5 py-10 sm:px-10">
            <p class="font-tpg17-mono text-xs tracking-[0.12em] text-tpg17-acc tabular-nums">02 &mdash; PRICING</p>
            <h2 id="tpg-17-h2" class="font-tpg17-serif text-[clamp(2rem,5vw,2.75rem)] leading-[1.05] tracking-[-0.01em]">One price per seat, billed monthly</h2>
            <p class="max-w-[34rem] text-[15px] leading-relaxed text-pretty text-tpg17-mut">Seats are prorated to the day. Bandwidth and build minutes are pooled across the team, so a quiet month for one project covers a launch week for another.</p>
            <div class="mt-2 flex max-w-[30rem] items-end justify-between rounded-xl bg-tpg17-well px-5 py-4 ring-1 ring-tpg17-line">
              <p class="text-sm text-tpg17-mut">Team, per seat</p>
              <p class="tabular-nums"><span class="text-3xl font-semibold tracking-[-0.03em]">$24</span><span class="text-sm text-tpg17-mut"> / month</span></p>
            </div>
          </section>
          <section id="tpg-17-s3" data-sec="" aria-labelledby="tpg-17-h3" class="grid min-h-full snap-start content-center gap-4 border-b border-tpg17-line px-5 py-10 sm:px-10">
            <p class="font-tpg17-mono text-xs tracking-[0.12em] text-tpg17-acc tabular-nums">03 &mdash; SECURITY</p>
            <h2 id="tpg-17-h3" class="font-tpg17-serif text-[clamp(2rem,5vw,2.75rem)] leading-[1.05] tracking-[-0.01em]">Audit logs and SSO, on by default</h2>
            <p class="max-w-[34rem] text-[15px] leading-relaxed text-pretty text-tpg17-mut">Every deploy, role change and secret rotation is logged for 400 days. SAML single sign-on and enforced two-factor are included rather than sold as add-ons.</p>
            <ul class="mt-1 grid max-w-[30rem] gap-2 text-sm">
              <li class="flex items-center gap-2.5"><span aria-hidden="true" class="size-1.5 rounded-full bg-linear-to-br from-tpg17-em to-tpg17-tl shadow-[0_0_8px_var(--color-tpg17-em)]"></span>SOC 2 Type II report on request</li>
              <li class="flex items-center gap-2.5"><span aria-hidden="true" class="size-1.5 rounded-full bg-linear-to-br from-tpg17-em to-tpg17-tl shadow-[0_0_8px_var(--color-tpg17-em)]"></span>Encrypted secrets with per-environment scopes</li>
              <li class="flex items-center gap-2.5"><span aria-hidden="true" class="size-1.5 rounded-full bg-linear-to-br from-tpg17-em to-tpg17-tl shadow-[0_0_8px_var(--color-tpg17-em)]"></span>IP allow-lists for preview deployments</li>
            </ul>
          </section>
          <section id="tpg-17-s4" data-sec="" aria-labelledby="tpg-17-h4" class="grid min-h-full snap-start content-center gap-4 px-5 py-10 sm:px-10">
            <p class="font-tpg17-mono text-xs tracking-[0.12em] text-tpg17-acc tabular-nums">04 &mdash; CHANGELOG</p>
            <h2 id="tpg-17-h4" class="font-tpg17-serif text-[clamp(2rem,5vw,2.75rem)] leading-[1.05] tracking-[-0.01em]">What changed this quarter</h2>
            <ol class="grid max-w-[30rem] gap-3 text-sm">
              <li class="grid grid-cols-[4.5rem_1fr] gap-3"><span class="font-tpg17-mono text-xs leading-5 text-tpg17-mut tabular-nums">Oct 02</span><span>Preview deployments now sleep after 7 days idle.</span></li>
              <li class="grid grid-cols-[4.5rem_1fr] gap-3"><span class="font-tpg17-mono text-xs leading-5 text-tpg17-mut tabular-nums">Sep 18</span><span>Two new regions: Johannesburg and Osaka.</span></li>
              <li class="grid grid-cols-[4.5rem_1fr] gap-3"><span class="font-tpg17-mono text-xs leading-5 text-tpg17-mut tabular-nums">Aug 27</span><span>Audit log export to S3 and BigQuery.</span></li>
            </ol>
          </section>
        </div>
        <nav aria-label="Pagination" class="group/rail flex w-16 flex-col items-center justify-between gap-4 border-l border-tpg17-line bg-tpg17-well py-5 sm:w-[12.5rem] sm:items-stretch sm:px-4">
          <p aria-hidden="true" class="font-tpg17-mono text-[11px] text-tpg17-mut tabular-nums sm:px-2"><span data-count="" class="font-semibold text-tpg17-acc">01</span><span class="max-sm:hidden"> / 04</span></p>
          <div class="relative">
            <span aria-hidden="true" class="absolute top-[1.375rem] bottom-[1.375rem] left-[calc(50%-1px)] w-0.5 overflow-hidden rounded-full bg-tpg17-line sm:left-[0.75rem]"><span data-fill="" class="block size-full origin-top scale-y-0 supports-[(animation-timeline:scroll())_and_(timeline-scope:--a)]:animate-tpg17-fill rounded-full bg-linear-to-b from-tpg17-em to-tpg17-tl transition-transform duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-has-[[data-s='2'][aria-current=page]]/rail:scale-y-[.3333] group-has-[[data-s='3'][aria-current=page]]/rail:scale-y-[.6667] group-has-[[data-s='4'][aria-current=page]]/rail:scale-y-100 motion-reduce:transition-none"></span></span>
            <ol class="relative grid gap-3">
              <li><a href="#tpg-17-s1" data-s="1" aria-current="page" class="group/dot flex min-h-11 min-w-11 items-center justify-center gap-3 rounded-lg px-2 text-sm text-tpg17-mut transition-colors hover:bg-tpg17-raise hover:text-tpg17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring aria-[current=page]:bg-tpg17-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tpg17-acc sm:justify-start"><span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tpg17-card ring-2 ring-tpg17-dot transition-[scale,background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/dot:ring-tpg17-mut group-aria-[current=page]/dot:scale-125 group-aria-[current=page]/dot:bg-linear-to-br group-aria-[current=page]/dot:from-tpg17-em group-aria-[current=page]/dot:to-tpg17-tl group-aria-[current=page]/dot:ring-tpg17-em/50 group-aria-[current=page]/dot:shadow-tpg17-halo"></span><span class="max-sm:sr-only">Overview</span></a></li>
              <li><a href="#tpg-17-s2" data-s="2" class="group/dot flex min-h-11 min-w-11 items-center justify-center gap-3 rounded-lg px-2 text-sm text-tpg17-mut transition-colors hover:bg-tpg17-raise hover:text-tpg17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring aria-[current=page]:bg-tpg17-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tpg17-acc sm:justify-start"><span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tpg17-card ring-2 ring-tpg17-dot transition-[scale,background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/dot:ring-tpg17-mut group-aria-[current=page]/dot:scale-125 group-aria-[current=page]/dot:bg-linear-to-br group-aria-[current=page]/dot:from-tpg17-em group-aria-[current=page]/dot:to-tpg17-tl group-aria-[current=page]/dot:ring-tpg17-em/50 group-aria-[current=page]/dot:shadow-tpg17-halo"></span><span class="max-sm:sr-only">Pricing</span></a></li>
              <li><a href="#tpg-17-s3" data-s="3" class="group/dot flex min-h-11 min-w-11 items-center justify-center gap-3 rounded-lg px-2 text-sm text-tpg17-mut transition-colors hover:bg-tpg17-raise hover:text-tpg17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring aria-[current=page]:bg-tpg17-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tpg17-acc sm:justify-start"><span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tpg17-card ring-2 ring-tpg17-dot transition-[scale,background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/dot:ring-tpg17-mut group-aria-[current=page]/dot:scale-125 group-aria-[current=page]/dot:bg-linear-to-br group-aria-[current=page]/dot:from-tpg17-em group-aria-[current=page]/dot:to-tpg17-tl group-aria-[current=page]/dot:ring-tpg17-em/50 group-aria-[current=page]/dot:shadow-tpg17-halo"></span><span class="max-sm:sr-only">Security</span></a></li>
              <li><a href="#tpg-17-s4" data-s="4" class="group/dot flex min-h-11 min-w-11 items-center justify-center gap-3 rounded-lg px-2 text-sm text-tpg17-mut transition-colors hover:bg-tpg17-raise hover:text-tpg17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring aria-[current=page]:bg-tpg17-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tpg17-acc sm:justify-start"><span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tpg17-card ring-2 ring-tpg17-dot transition-[scale,background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/dot:ring-tpg17-mut group-aria-[current=page]/dot:scale-125 group-aria-[current=page]/dot:bg-linear-to-br group-aria-[current=page]/dot:from-tpg17-em group-aria-[current=page]/dot:to-tpg17-tl group-aria-[current=page]/dot:ring-tpg17-em/50 group-aria-[current=page]/dot:shadow-tpg17-halo"></span><span class="max-sm:sr-only">Changelog</span></a></li>
            </ol>
          </div>
          <div class="flex flex-col gap-1.5 sm:flex-row">
            <button type="button" data-step="-1" aria-label="Previous section" disabled class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg17-card text-tpg17-ink shadow-tpg17-key ring-1 ring-tpg17-line transition-colors hover:bg-tpg17-raise hover:text-tpg17-acc hover:ring-tpg17-em/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring disabled:cursor-not-allowed disabled:bg-transparent disabled:text-tpg17-mut/60 disabled:shadow-none"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M5 12.5 10 7.5l5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
            <button type="button" data-step="1" aria-label="Next section" class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg17-card text-tpg17-ink shadow-tpg17-key ring-1 ring-tpg17-line transition-colors hover:bg-tpg17-raise hover:text-tpg17-acc hover:ring-tpg17-em/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg17-ring disabled:cursor-not-allowed disabled:bg-transparent disabled:text-tpg17-mut/60 disabled:shadow-none"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M5 7.5 10 12.5l5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          </div>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-2xl px-3.5 py-2 text-center font-tpg17-mono text-[11.5px] text-tpg17-mut ring-1 ring-tpg17-line">timeline-scope &middot; animation-timeline &middot; group-has-[[aria-current=page]]/rail:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg17-bg: #edf7f2;
  --color-tpg17-bg: oklch(0.968 0.018 165);
  --color-tpg17-glow: #a7f3d099;
  --color-tpg17-glow: oklch(0.9 0.08 165 / 0.6);
  --color-tpg17-card: #fbfefc;
  --color-tpg17-card: oklch(0.995 0.004 165);
  --color-tpg17-well: #f1faf5;
  --color-tpg17-well: oklch(0.98 0.012 165);
  --color-tpg17-raise: #dff3e9;
  --color-tpg17-raise: oklch(0.95 0.03 165);
  --color-tpg17-ink: #0f241c;
  --color-tpg17-ink: oklch(0.24 0.035 165);
  --color-tpg17-mut: #4b6458;
  --color-tpg17-mut: oklch(0.48 0.035 165);
  --color-tpg17-line: #d3eadf;
  --color-tpg17-line: oklch(0.92 0.025 165);
  --color-tpg17-dot: #a6cdbb;
  --color-tpg17-dot: oklch(0.82 0.05 165);
  --color-tpg17-acc: #047857;
  --color-tpg17-acc: oklch(0.508 0.118 165.6);
  --color-tpg17-acc2: #0f766e;
  --color-tpg17-acc2: oklch(0.511 0.086 186.4);
  --color-tpg17-em: #10b981;
  --color-tpg17-em: oklch(0.696 0.17 162.5);
  --color-tpg17-tl: #0d9488;
  --color-tpg17-tl: oklch(0.6 0.118 184.7);
  --color-tpg17-ring: #059669;
  --color-tpg17-ring: oklch(0.596 0.145 163.2);
  --color-tpg17-hi: #ffffff99;
  --color-tpg17-hi: oklch(1 0 0 / 0.6);
  --font-tpg17-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpg17-serif: 'Instrument Serif', Georgia, serif;
  --font-tpg17-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg17-card: 0 1px 2px oklch(0.3 0.06 165 / 0.08), 0 22px 50px -20px oklch(0.45 0.12 165 / 0.32);
  --shadow-tpg17-key: 0 1px 2px oklch(0.3 0.06 165 / 0.1), inset 0 1px 0 var(--color-tpg17-hi);
  --shadow-tpg17-halo: 0 0 0 4px oklch(0.696 0.17 162.5 / 0.2), 0 0 16px 2px oklch(0.696 0.17 162.5 / 0.7);
  --animate-tpg17-fill: tpg17-fill linear both;

  @keyframes tpg17-fill {
    from {
      scale: 1 0;
    }

    to {
      scale: 1 1;
    }
  }
}

@media (prefers-color-scheme: dark) {
  .tpg-17:not([data-theme="light"]) {
    --color-tpg17-bg: #06150f;
    --color-tpg17-bg: oklch(0.17 0.03 168);
    --color-tpg17-glow: #065f4659;
    --color-tpg17-glow: oklch(0.38 0.08 168 / 0.35);
    --color-tpg17-card: #0c1f18;
    --color-tpg17-card: oklch(0.215 0.035 168);
    --color-tpg17-well: #0a1a14;
    --color-tpg17-well: oklch(0.195 0.032 168);
    --color-tpg17-raise: #12302a;
    --color-tpg17-raise: oklch(0.28 0.045 170);
    --color-tpg17-ink: #ecfdf5;
    --color-tpg17-ink: oklch(0.98 0.02 165);
    --color-tpg17-mut: #9cc4b3;
    --color-tpg17-mut: oklch(0.79 0.05 165);
    --color-tpg17-line: #183a2e;
    --color-tpg17-line: oklch(0.31 0.045 168);
    --color-tpg17-dot: #2f5a49;
    --color-tpg17-dot: oklch(0.42 0.05 168);
    --color-tpg17-acc: #6ee7b7;
    --color-tpg17-acc: oklch(0.845 0.143 165);
    --color-tpg17-acc2: #5eead4;
    --color-tpg17-acc2: oklch(0.855 0.138 181);
    --color-tpg17-ring: #34d399;
    --color-tpg17-ring: oklch(0.765 0.177 163);
    --color-tpg17-hi: #ffffff12;
    --color-tpg17-hi: oklch(1 0 0 / 0.07);
  }
}

.tpg-17[data-theme="dark"] {
  --color-tpg17-bg: #06150f;
  --color-tpg17-bg: oklch(0.17 0.03 168);
  --color-tpg17-glow: #065f4659;
  --color-tpg17-glow: oklch(0.38 0.08 168 / 0.35);
  --color-tpg17-card: #0c1f18;
  --color-tpg17-card: oklch(0.215 0.035 168);
  --color-tpg17-well: #0a1a14;
  --color-tpg17-well: oklch(0.195 0.032 168);
  --color-tpg17-raise: #12302a;
  --color-tpg17-raise: oklch(0.28 0.045 170);
  --color-tpg17-ink: #ecfdf5;
  --color-tpg17-ink: oklch(0.98 0.02 165);
  --color-tpg17-mut: #9cc4b3;
  --color-tpg17-mut: oklch(0.79 0.05 165);
  --color-tpg17-line: #183a2e;
  --color-tpg17-line: oklch(0.31 0.045 168);
  --color-tpg17-dot: #2f5a49;
  --color-tpg17-dot: oklch(0.42 0.05 168);
  --color-tpg17-acc: #6ee7b7;
  --color-tpg17-acc: oklch(0.845 0.143 165);
  --color-tpg17-acc2: #5eead4;
  --color-tpg17-acc2: oklch(0.855 0.138 181);
  --color-tpg17-ring: #34d399;
  --color-tpg17-ring: oklch(0.765 0.177 163);
  --color-tpg17-hi: #ffffff12;
  --color-tpg17-hi: oklch(1 0 0 / 0.07);
}
/* Scroll-driven progress: the pane names its timeline, the card hoists the name so the rail (a
   sibling of the pane) can animate against it. Gated on both features; otherwise the fill keeps
   the stepped scale-y the markup sets from aria-current. */

@supports (animation-timeline: scroll()) and (timeline-scope: --a) {
  .tpg-17 [data-card] {
    timeline-scope: --tpg17-read;
  }

  .tpg-17 [data-pane] {
    scroll-timeline: --tpg17-read y;
  }

  .tpg-17 [data-fill] {
    animation-timeline: --tpg17-read;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-17-guide');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const pane = root.querySelector('[data-pane]');
  const secs = Array.from(root.querySelectorAll('[data-sec]'));
  const dots = Array.from(root.querySelectorAll('[data-s]'));
  const [prev, next] = ['-1', '1'].map((v) => root.querySelector('[data-step="' + v + '"]'));
  const count = root.querySelector('[data-count]');
  let cur = 0, hold = 0;
  const mark = (i) => {
    cur = i;
    dots.forEach((d, k) => {
      if (k === i) d.setAttribute('aria-current', 'page');
      else d.removeAttribute('aria-current');
    });
    prev.disabled = i === 0;
    next.disabled = i === secs.length - 1;
    count.textContent = '0' + (i + 1);
  };
  const go = (i) => {
    const k = Math.max(0, Math.min(secs.length - 1, i));
    hold = Date.now() + 900;
    pane.scrollTo({ top: secs[k].offsetTop });
    mark(k);
  };
  const spy = () => {
    if (Date.now() < hold) return;
    const mid = pane.scrollTop + pane.clientHeight * 0.4;
    let k = 0;
    secs.forEach((s, j) => { if (s.offsetTop <= mid) k = j; });
    if (pane.scrollTop + pane.clientHeight >= pane.scrollHeight - 2) k = secs.length - 1;
    if (k !== cur) mark(k);
  };
  pane.addEventListener('scroll', () => requestAnimationFrame(spy), { passive: true });
  dots.forEach((d, k) => {
    d.addEventListener('click', (e) => { e.preventDefault(); go(k); });
    d.addEventListener('keydown', (e) => {
      const j = e.key === 'ArrowDown' ? k + 1 : e.key === 'ArrowUp' ? k - 1 : -1;
      if (j < 0 || j >= dots.length) return;
      e.preventDefault(); dots[j].focus(); go(j);
    });
  });
  [prev, next].forEach((b, d) => b.addEventListener('click', () => go(cur + (d ? 1 : -1))));
  mark(0);
})();
```
