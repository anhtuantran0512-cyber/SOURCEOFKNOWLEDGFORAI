---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-tabbed-product-tour-feature-section/"
title: "Tailwind Tabbed Product Tour Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A SaaS product tour: a segmented tab strip swaps a drawn product screenshot and three benefit bullets."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabbed Product Tour Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-tabbed-product-tour-feature-section/

A SaaS product tour: a segmented tab strip swaps a drawn product screenshot and three benefit bullets. State lives in a native radio group read by group-has-[#id:checked]/tour:, so switching costs zero script — and because the inputs are real radios, arrow keys rove the strip for free, which retires the CSS original's 20-line controller.
## HTML
```html
<section class="tfs-01 w-full min-h-svh bg-tfs01-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tfs01-glow),transparent_70%)] px-5 py-20 font-tfs01-sans text-tfs01-ink antialiased sm:py-28" aria-labelledby="tfs-01-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12">
    <header class="mx-auto grid max-w-2xl justify-items-center gap-4 text-center">
      <p class="inline-flex items-center gap-2 rounded-full border border-tfs01-acc/20 bg-white px-3 py-1 text-xs font-semibold tracking-wide text-tfs01-acc shadow-sm"><span class="size-1.5 rounded-full bg-tfs01-acc"></span>Product tour</p>
      <h2 id="tfs-01-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Four surfaces, one control plane</h2>
      <p class="text-pretty text-lg text-tfs01-mut">Every team touches a different part of Meridian. Step through the ones yours will live in.</p>
    </header>
    <div class="group/tour grid gap-8">
      <fieldset class="mx-auto flex max-w-full snap-x gap-1 overflow-x-auto rounded-2xl border border-tfs01-line bg-white/80 p-1.5 shadow-[0_1px_2px_rgb(0_0_0/0.04),0_8px_24px_-12px_rgb(15_23_42/0.18)] backdrop-blur [scrollbar-width:none]">
        <legend class="sr-only">Product tour sections</legend>
        <label class="flex min-h-11 flex-none cursor-pointer snap-start items-center gap-2 rounded-xl px-4 text-sm font-medium text-tfs01-mut transition hover:text-tfs01-ink has-checked:bg-tfs01-ink has-checked:text-white has-checked:shadow-md has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs01-acc"><input type="radio" name="tfs-01-tab" id="tfs-01-t1" class="sr-only" checked><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="m12 2 10 5-10 5L2 7l10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>Overview</label>
        <label class="flex min-h-11 flex-none cursor-pointer snap-start items-center gap-2 rounded-xl px-4 text-sm font-medium text-tfs01-mut transition hover:text-tfs01-ink has-checked:bg-tfs01-ink has-checked:text-white has-checked:shadow-md has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs01-acc"><input type="radio" name="tfs-01-tab" id="tfs-01-t2" class="sr-only"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg>Analytics</label>
        <label class="flex min-h-11 flex-none cursor-pointer snap-start items-center gap-2 rounded-xl px-4 text-sm font-medium text-tfs01-mut transition hover:text-tfs01-ink has-checked:bg-tfs01-ink has-checked:text-white has-checked:shadow-md has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs01-acc"><input type="radio" name="tfs-01-tab" id="tfs-01-t3" class="sr-only"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 3h6v6H3zM15 15h6v6h-6zM6 9v3a3 3 0 0 0 3 3h6"/></svg>Automations</label>
        <label class="flex min-h-11 flex-none cursor-pointer snap-start items-center gap-2 rounded-xl px-4 text-sm font-medium text-tfs01-mut transition hover:text-tfs01-ink has-checked:bg-tfs01-ink has-checked:text-white has-checked:shadow-md has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs01-acc"><input type="radio" name="tfs-01-tab" id="tfs-01-t4" class="sr-only"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Security</label>
      </fieldset>
      <div class="rounded-[1.75rem] border border-tfs01-line bg-white p-3 shadow-[0_30px_80px_-30px_rgb(15_23_42/0.35)] sm:p-4">
        <article class="hidden animate-tfs01-in gap-8 lg:min-h-[26rem] lg:grid-cols-[1.35fr_1fr] group-has-[#tfs-01-t1:checked]/tour:grid" aria-label="Overview">
          <div class="overflow-hidden rounded-2xl border border-tfs01-line bg-tfs01-bg">
            <div class="flex items-center gap-1.5 border-b border-tfs01-line bg-white px-4 py-3"><span class="size-2.5 rounded-full bg-[#ff5f57]"></span><span class="size-2.5 rounded-full bg-[#febc2e]"></span><span class="size-2.5 rounded-full bg-[#28c840]"></span><span class="ml-3 rounded-md bg-tfs01-bg px-2.5 py-1 font-tfs01-mono text-[11px] text-tfs01-mut">app.meridian.dev/overview</span></div>
            <div class="grid grid-cols-3 gap-3 p-4">
              <div class="col-span-2 rounded-xl bg-white p-4 shadow-sm"><p class="text-xs font-semibold text-tfs01-mut">Warehouse sync</p><p class="mt-1 text-2xl font-semibold tabular-nums">99.98%</p><div class="mt-3 h-1.5 rounded-full bg-tfs01-line"><div class="h-full w-[92%] rounded-full bg-tfs01-acc"></div></div></div>
              <div class="rounded-xl bg-white p-4 shadow-sm"><p class="text-xs font-semibold text-tfs01-mut">Freshness</p><p class="mt-1 text-2xl font-semibold tabular-nums">4m</p><p class="mt-2 text-[11px] font-medium text-emerald-600">● within SLA</p></div>
              <div class="rounded-xl bg-white p-4 shadow-sm"><p class="text-xs font-semibold text-tfs01-mut">Owners</p><div class="mt-3 flex -space-x-2"><span class="grid size-7 place-items-center rounded-full bg-indigo-100 text-[10px] font-bold text-indigo-700 ring-2 ring-white">AC</span><span class="grid size-7 place-items-center rounded-full bg-amber-100 text-[10px] font-bold text-amber-700 ring-2 ring-white">PS</span><span class="grid size-7 place-items-center rounded-full bg-emerald-100 text-[10px] font-bold text-emerald-700 ring-2 ring-white">JL</span></div></div>
              <div class="col-span-2 rounded-xl bg-white p-4 shadow-sm"><p class="text-xs font-semibold text-tfs01-mut">Run history</p><div class="mt-3 flex items-end gap-1 h-12"><i class="flex-1 rounded-sm bg-tfs01-acc/30 h-[40%]"></i><i class="flex-1 rounded-sm bg-tfs01-acc/30 h-[65%]"></i><i class="flex-1 rounded-sm bg-tfs01-acc/30 h-[50%]"></i><i class="flex-1 rounded-sm bg-tfs01-acc/30 h-[80%]"></i><i class="flex-1 rounded-sm bg-rose-400 h-[30%]"></i><i class="flex-1 rounded-sm bg-tfs01-acc/30 h-[72%]"></i><i class="flex-1 rounded-sm bg-tfs01-acc h-[95%]"></i></div></div>
            </div>
          </div>
          <div class="grid content-center gap-5 p-2 sm:p-4">
            <h3 class="text-2xl font-semibold tracking-tight">One place every pipeline reports to</h3>
            <ul class="grid gap-3 text-tfs01-mut">
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Model, run and owner in one view — no tab archaeology</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Freshness SLAs per dataset with a breach timeline</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Column-level lineage read from the warehouse itself</li>
            </ul>
            <a href="#tfs-01-h" class="group inline-flex min-h-11 w-fit items-center gap-2 rounded-xl text-sm font-semibold text-tfs01-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tfs01-acc">Read the overview docs <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-1"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          </div>
        </article>
        <article class="hidden animate-tfs01-in gap-8 lg:min-h-[26rem] lg:grid-cols-[1.35fr_1fr] group-has-[#tfs-01-t2:checked]/tour:grid" aria-label="Analytics">
          <div class="overflow-hidden rounded-2xl border border-tfs01-line bg-tfs01-bg">
            <div class="flex items-center justify-between border-b border-tfs01-line bg-white px-4 py-3"><span class="text-xs font-semibold">Query cost · last 14 days</span><span class="rounded-md bg-emerald-50 px-2 py-0.5 text-[11px] font-semibold text-emerald-700">−31%</span></div>
            <div class="flex h-64 items-end gap-2 p-5"><i class="flex-1 rounded-t-md bg-tfs01-acc/25 h-[70%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/25 h-[82%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/25 h-[76%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/25 h-[88%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/40 h-[64%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/50 h-[58%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/60 h-[52%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/70 h-[49%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc/80 h-[45%]"></i><i class="flex-1 rounded-t-md bg-tfs01-acc h-[41%]"></i></div>
          </div>
          <div class="grid content-center gap-5 p-2 sm:p-4">
            <h3 class="text-2xl font-semibold tracking-tight">See the bill before finance does</h3>
            <ul class="grid gap-3 text-tfs01-mut">
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Cost per model, per team, per run</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Regression alerts when a deploy doubles spend</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Exports straight to your FinOps sheet</li>
            </ul>
          </div>
        </article>
        <article class="hidden animate-tfs01-in gap-8 lg:min-h-[26rem] lg:grid-cols-[1.35fr_1fr] group-has-[#tfs-01-t3:checked]/tour:grid" aria-label="Automations">
          <div class="grid place-items-center gap-3 rounded-2xl border border-tfs01-line bg-tfs01-bg bg-[radial-gradient(var(--color-tfs01-line)_1px,transparent_1px)] bg-size-[16px_16px] p-8">
            <div class="flex w-full max-w-xs items-center gap-3 rounded-xl bg-white p-3 shadow-sm"><span class="grid size-8 place-items-center rounded-lg bg-amber-100 text-amber-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2"/></svg></span><span class="text-sm font-medium">Every day · 06:00 UTC</span></div>
            <span class="h-6 w-px bg-tfs01-acc/40"></span>
            <div class="flex w-full max-w-xs items-center gap-3 rounded-xl bg-white p-3 shadow-sm ring-2 ring-tfs01-acc/30"><span class="grid size-8 place-items-center rounded-lg bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span><span class="text-sm font-medium">Rebuild stale models</span></div>
            <span class="h-6 w-px bg-tfs01-acc/40"></span>
            <div class="flex w-full max-w-xs items-center gap-3 rounded-xl bg-white p-3 shadow-sm"><span class="grid size-8 place-items-center rounded-lg bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></span><span class="text-sm font-medium">Post summary to #data-ops</span></div>
          </div>
          <div class="grid content-center gap-5 p-2 sm:p-4">
            <h3 class="text-2xl font-semibold tracking-tight">Runbooks that run themselves</h3>
            <ul class="grid gap-3 text-tfs01-mut">
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Triggers on schedule, on schema change or on failure</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Retries with back-off, then pages the owner</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Versioned in Git next to the models they touch</li>
            </ul>
          </div>
        </article>
        <article class="hidden animate-tfs01-in gap-8 lg:min-h-[26rem] lg:grid-cols-[1.35fr_1fr] group-has-[#tfs-01-t4:checked]/tour:grid" aria-label="Security">
          <div class="grid content-center gap-2.5 rounded-2xl border border-tfs01-line bg-tfs01-bg p-5">
            <div class="flex items-center justify-between rounded-xl bg-white px-4 py-3 shadow-sm"><span class="flex items-center gap-2 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tfs01-acc"><path d="M2 18v3h3l7.4-7.4A5 5 0 1 0 9.4 10.6L2 18zM16 8h.01"/></svg>SSO · Okta</span><span class="rounded-full bg-emerald-50 px-2 py-0.5 text-[11px] font-semibold text-emerald-700">Enforced</span></div>
            <div class="flex items-center justify-between rounded-xl bg-white px-4 py-3 shadow-sm"><span class="flex items-center gap-2 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tfs01-acc"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>SCIM provisioning</span><span class="rounded-full bg-emerald-50 px-2 py-0.5 text-[11px] font-semibold text-emerald-700">Synced</span></div>
            <div class="flex items-center justify-between rounded-xl bg-white px-4 py-3 shadow-sm"><span class="flex items-center gap-2 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tfs01-acc"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg>Column masking · PII</span><span class="rounded-full bg-tfs01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tfs01-acc">14 rules</span></div>
          </div>
          <div class="grid content-center gap-5 p-2 sm:p-4">
            <h3 class="text-2xl font-semibold tracking-tight">Access your auditors will sign off</h3>
            <ul class="grid gap-3 text-tfs01-mut">
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>SAML SSO and SCIM on every plan</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Column-level masking driven by tags</li>
              <li class="flex gap-3"><span class="mt-0.5 grid size-5 flex-none place-items-center rounded-full bg-tfs01-acc/10 text-tfs01-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span>Immutable audit log, streamed to your SIEM</li>
            </ul>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs01-bg: #f6f7fb;
  --color-tfs01-bg: oklch(0.977 0.005 275);
  --color-tfs01-glow: #e8e9ff;
  --color-tfs01-glow: oklch(0.94 0.03 284);
  --color-tfs01-ink: #0f172a;
  --color-tfs01-ink: oklch(0.208 0.04 266);
  --color-tfs01-mut: #4b5468;
  --color-tfs01-mut: oklch(0.446 0.035 266);
  --color-tfs01-line: #e3e6ee;
  --color-tfs01-line: oklch(0.925 0.011 270);
  --color-tfs01-acc: #4f46e5;
  --color-tfs01-acc: oklch(0.511 0.23 277);
  --font-tfs01-sans: 'Geist', system-ui, sans-serif;
  --font-tfs01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tfs01-in: tfs01-in 0.45s cubic-bezier(0.2, 0.8, 0.2, 1) both;

  @keyframes tfs01-in {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-01 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfs-01 * {
    animation: none !important;
  }
}
```
