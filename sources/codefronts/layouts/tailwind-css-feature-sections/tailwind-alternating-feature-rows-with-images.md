---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-alternating-feature-rows-with-images/"
title: "Tailwind Alternating Feature Rows with Images"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "The zig-zag feature section: three rows, each a copy block beside a product visual, flipping sides on every other row."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Alternating Feature Rows with Images
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-alternating-feature-rows-with-images/

The zig-zag feature section: three rows, each a copy block beside a product visual, flipping sides on every other row. The flip is one variant on the parent — lg:even:[&>figure]:order-first — so rows can be added, removed or reordered without touching a class.
## HTML
```html
<section class="tfs-02 w-full min-h-svh bg-tfs02-bg px-5 py-20 font-tfs02-sans text-tfs02-ink antialiased sm:py-28" aria-labelledby="tfs-02-h">
  <div class="mx-auto grid w-full max-w-6xl gap-20 lg:gap-28">
    <header class="grid max-w-2xl gap-4">
      <p class="text-sm font-semibold text-tfs02-acc">Why teams switch to Basalt</p>
      <h2 id="tfs-02-h" class="text-balance font-tfs02-display text-4xl font-bold tracking-tight sm:text-6xl">Infrastructure that explains itself</h2>
    </header>
    <div class="grid gap-20 lg:gap-28">
      <article class="grid items-center gap-10 lg:grid-cols-2 lg:gap-16 lg:even:[&>figure]:order-first">
        <div class="grid gap-5">
          <span class="grid size-11 place-items-center rounded-xl bg-tfs02-acc text-white shadow-lg shadow-tfs02-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span>
          <h3 class="text-balance font-tfs02-display text-3xl font-semibold tracking-tight">Deploy to 32 regions with one config file</h3>
          <p class="text-pretty text-lg leading-relaxed text-tfs02-mut">Write the topology once. Basalt plans the rollout, canaries each region and rolls back on its own when error budgets burn.</p>
          <dl class="mt-2 grid grid-cols-2 gap-6 border-t border-tfs02-line pt-6"><div><dt class="text-sm text-tfs02-mut">Median deploy</dt><dd class="font-tfs02-display text-3xl font-bold tabular-nums">48s</dd></div><div><dt class="text-sm text-tfs02-mut">Auto-rollbacks</dt><dd class="font-tfs02-display text-3xl font-bold tabular-nums">100%</dd></div></dl>
        </div>
        <figure class="relative aspect-[5/4] overflow-hidden rounded-[2rem] bg-linear-to-br from-tfs02-acc to-tfs02-acc2 shadow-2xl shadow-tfs02-acc/25">
          <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgb(255_255_255/0.35),transparent_45%)]"></div>
          <div class="absolute left-[8%] top-[14%] w-[62%] rounded-2xl bg-white/95 p-4 shadow-xl"><p class="text-xs font-semibold text-tfs02-mut">Rollout · v2.14.0</p><div class="mt-3 grid gap-2"><div class="flex items-center gap-2 text-sm"><span class="size-2 rounded-full bg-emerald-500"></span>us-east-1<span class="ml-auto text-xs text-tfs02-mut">live</span></div><div class="flex items-center gap-2 text-sm"><span class="size-2 rounded-full bg-emerald-500"></span>eu-west-2<span class="ml-auto text-xs text-tfs02-mut">live</span></div><div class="flex items-center gap-2 text-sm"><span class="size-2 animate-pulse rounded-full bg-amber-500"></span>ap-south-1<span class="ml-auto text-xs text-tfs02-mut">canary 10%</span></div></div></div>
          <div class="absolute bottom-[12%] right-[8%] rounded-2xl bg-tfs02-ink/90 px-4 py-3 text-white shadow-xl backdrop-blur"><p class="text-xs text-white/70">Error budget</p><p class="font-tfs02-display text-2xl font-bold">99.2%</p></div>
          <figcaption class="sr-only">Rollout panel showing three regions and remaining error budget</figcaption>
        </figure>
      </article>
      <article class="grid items-center gap-10 lg:grid-cols-2 lg:gap-16 lg:even:[&>figure]:order-first">
        <div class="grid gap-5">
          <span class="grid size-11 place-items-center rounded-xl bg-tfs02-acc text-white shadow-lg shadow-tfs02-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.3-4.3"/></svg></span>
          <h3 class="text-balance font-tfs02-display text-3xl font-semibold tracking-tight">Every incident arrives with its root cause</h3>
          <p class="text-pretty text-lg leading-relaxed text-tfs02-mut">Traces, logs and the diff that shipped are stitched into one timeline, so on-call starts at the answer instead of the dashboard.</p>
          <ul class="mt-2 grid gap-3 text-tfs02-mut"><li class="flex items-center gap-3"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5 text-tfs02-acc"><path d="M20 6 9 17l-5-5"/></svg>Correlates deploys with error spikes</li><li class="flex items-center gap-3"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5 text-tfs02-acc"><path d="M20 6 9 17l-5-5"/></svg>Names the commit and its author</li></ul>
        </div>
        <figure class="relative aspect-[5/4] overflow-hidden rounded-[2rem] bg-tfs02-ink shadow-2xl">
          <div class="absolute inset-0 bg-[linear-gradient(rgb(255_255_255/0.05)_1px,transparent_1px),linear-gradient(90deg,rgb(255_255_255/0.05)_1px,transparent_1px)] bg-size-[32px_32px]"></div>
          <svg aria-hidden="true" viewBox="0 0 400 200" class="absolute inset-x-[8%] top-[22%] w-[84%]" fill="none"><path d="M0 150 L60 140 L110 145 L160 120 L200 130 L230 40 L260 125 L320 110 L400 100" stroke="currentColor" stroke-width="3" class="text-tfs02-acc2"/><circle cx="230" cy="40" r="7" class="fill-rose-500"/></svg>
          <div class="absolute bottom-[10%] left-[8%] right-[8%] rounded-2xl border border-white/10 bg-white/10 p-4 text-white backdrop-blur-md"><p class="flex items-center gap-2 text-xs font-semibold text-rose-300"><span class="size-1.5 rounded-full bg-rose-400"></span>Root cause found in 41s</p><p class="mt-1 text-sm">Commit <span class="font-mono text-tfs02-acc2">a3f9c21</span> raised p99 latency in checkout-api</p></div>
          <figcaption class="sr-only">Latency chart with a spike traced to a specific commit</figcaption>
        </figure>
      </article>
      <article class="grid items-center gap-10 lg:grid-cols-2 lg:gap-16 lg:even:[&>figure]:order-first">
        <div class="grid gap-5">
          <span class="grid size-11 place-items-center rounded-xl bg-tfs02-acc text-white shadow-lg shadow-tfs02-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg></span>
          <h3 class="text-balance font-tfs02-display text-3xl font-semibold tracking-tight">Spend that scales down as fast as it scales up</h3>
          <p class="text-pretty text-lg leading-relaxed text-tfs02-mut">Idle services sleep in seconds and wake on the first request. Most teams cut their compute bill by a third in the first month.</p>
          <a href="#tfs-02-h" class="group mt-2 inline-flex min-h-11 w-fit items-center gap-2 rounded-full bg-tfs02-ink px-5 text-sm font-semibold text-white transition hover:bg-tfs02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs02-acc">Estimate your savings <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-0.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
        <figure class="relative aspect-[5/4] overflow-hidden rounded-[2rem] bg-tfs02-soft shadow-2xl shadow-tfs02-ink/10">
          <div class="absolute inset-[10%] grid grid-cols-6 items-end gap-3"><i class="h-[85%] rounded-t-xl bg-tfs02-ink/15"></i><i class="h-[78%] rounded-t-xl bg-tfs02-ink/15"></i><i class="h-[62%] rounded-t-xl bg-tfs02-acc/50"></i><i class="h-[51%] rounded-t-xl bg-tfs02-acc/70"></i><i class="h-[44%] rounded-t-xl bg-tfs02-acc/85"></i><i class="h-[38%] rounded-t-xl bg-tfs02-acc"></i></div>
          <div class="absolute right-[8%] top-[10%] rounded-2xl bg-white px-4 py-3 shadow-xl"><p class="text-xs text-tfs02-mut">Monthly compute</p><p class="font-tfs02-display text-2xl font-bold text-tfs02-acc">−34%</p></div>
          <figcaption class="sr-only">Bar chart of monthly compute falling by a third</figcaption>
        </figure>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs02-bg: #fbf8f3;
  --color-tfs02-bg: oklch(0.98 0.007 81);
  --color-tfs02-soft: #f1ebe1;
  --color-tfs02-soft: oklch(0.942 0.015 81);
  --color-tfs02-ink: #1c1917;
  --color-tfs02-ink: oklch(0.216 0.006 56);
  --color-tfs02-mut: #57534e;
  --color-tfs02-mut: oklch(0.444 0.01 74);
  --color-tfs02-line: #e7e0d5;
  --color-tfs02-line: oklch(0.909 0.017 79);
  --color-tfs02-acc: #ea580c;
  --color-tfs02-acc: oklch(0.646 0.194 41);
  --color-tfs02-acc2: #fbbf24;
  --color-tfs02-acc2: oklch(0.837 0.164 84);
  --font-tfs02-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tfs02-sans: 'DM Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-02 {
  width: 100%;
  min-height: 100svh;
}
```
