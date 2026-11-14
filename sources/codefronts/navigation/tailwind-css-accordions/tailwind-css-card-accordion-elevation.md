---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-card-accordion-elevation/"
title: "Tailwind CSS Card Accordion with Elevation on Open"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Depth as state: closed plan cards sit flat on a lavender stage, and the open one lifts toward you &mdash; open:scale-[1.02], a three-layer contact + key +…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Card Accordion with Elevation on Open
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-card-accordion-elevation/

Depth as state: closed plan cards sit flat on a lavender stage, and the open one lifts toward you &mdash; open:scale-[1.02], a three-layer contact + key + ambient shadow token, clearance margins that push its neighbours back and a gradient light-edge along the top. Built on <details name>, so only one plan is ever lifted.
## HTML
```html
<section class="tac-14 w-full min-h-svh grid place-items-center bg-tac14-bg bg-[radial-gradient(60%_45%_at_50%_0%,var(--color-tac14-glow),transparent_75%)] px-5 py-14 font-tac14-sans text-tac14-ink [interpolate-size:allow-keywords]" aria-label="Card accordion with elevation on open demo">
  <div class="grid w-full max-w-xl gap-9">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="text-[13px] font-bold tracking-[0.14em] text-tac14-acc uppercase">Pricing</p>
      <h2 class="text-[clamp(28px,5vw,38px)] leading-[1.1] font-extrabold tracking-[-0.03em] text-balance">Pick the plan that grows with you</h2>
      <p class="max-w-md text-[15px] leading-relaxed text-tac14-mut">Start free, upgrade when your team does. Every plan includes unlimited viewers and SOC 2 hosting.</p>
    </header>

    <div class="flex flex-col gap-2.5">
      <details name="tac14-plans" class="group relative rounded-2xl bg-white/55 ring-1 ring-tac14-line transition-[scale,box-shadow,margin,background-color] duration-500 ease-[cubic-bezier(0.3,1.25,0.4,1)] hover:bg-white/80 open:my-3 open:scale-[1.02] open:bg-white open:shadow-tac14-lift open:ring-tac14-acc/15 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-[background-color] motion-reduce:open:my-0 motion-reduce:open:scale-100 motion-reduce:details-content:transition-none" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac14-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute inset-x-6 top-0 h-[3px] rounded-b-full bg-linear-to-r from-tac14-acc to-tac14-acc2 opacity-0 transition-opacity duration-500 group-open:opacity-100"></span>
          <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-xl bg-tac14-soft text-tac14-acc ring-1 ring-tac14-acc/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac14-acc group-open:to-tac14-acc2 group-open:text-white"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 3v4M12 17v4M3 12h4M17 12h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="3" fill="currentColor"/></svg></span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="text-[17px] font-bold tracking-[-0.01em]">Starter</span>
            <span class="text-[13px] text-tac14-mut">For solo builders</span>
          </span>
          <span class="text-right text-[22px] font-extrabold tracking-[-0.02em] transition-colors duration-300 group-open:text-tac14-acc">$0</span>
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac14-soft text-tac14-mut transition duration-300 group-open:rotate-180 group-open:bg-tac14-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="grid gap-5 px-5 pb-5">
          <ul class="grid gap-x-6 gap-y-2.5 border-t border-tac14-line pt-5 text-[14px] text-tac14-ink sm:grid-cols-2">
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>3 active projects</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>1 GB file storage</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Community support</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Custom domain</li>
          </ul>
          <button type="button" class="min-h-11 w-full rounded-xl bg-tac14-ink px-5 text-[14.5px] font-semibold text-white shadow-[0_1px_2px_oklch(0.25_0.05_290/0.3)] transition hover:bg-tac14-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac14-acc">Start for free</button>
        </div>
      </details>

      <details name="tac14-plans" class="group relative rounded-2xl bg-white/55 ring-1 ring-tac14-line transition-[scale,box-shadow,margin,background-color] duration-500 ease-[cubic-bezier(0.3,1.25,0.4,1)] hover:bg-white/80 open:my-3 open:scale-[1.02] open:bg-white open:shadow-tac14-lift open:ring-tac14-acc/15 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-[background-color] motion-reduce:open:my-0 motion-reduce:open:scale-100 motion-reduce:details-content:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac14-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute inset-x-6 top-0 h-[3px] rounded-b-full bg-linear-to-r from-tac14-acc to-tac14-acc2 opacity-0 transition-opacity duration-500 group-open:opacity-100"></span>
          <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-xl bg-tac14-soft text-tac14-acc ring-1 ring-tac14-acc/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac14-acc group-open:to-tac14-acc2 group-open:text-white"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M4 18 10 12l3 3 7-8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 7h5v5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="flex flex-wrap items-center gap-x-2 gap-y-1 text-[17px] font-bold tracking-[-0.01em]">Pro <span class="rounded-full bg-tac14-acc/10 px-2 py-0.5 text-[11px] font-bold tracking-wide text-tac14-acc uppercase">Popular</span></span>
            <span class="text-[13px] text-tac14-mut">For growing teams</span>
          </span>
          <span class="text-right text-[22px] font-extrabold tracking-[-0.02em] transition-colors duration-300 group-open:text-tac14-acc">$24<span class="text-[13px] font-semibold text-tac14-mut">/mo</span></span>
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac14-soft text-tac14-mut transition duration-300 group-open:rotate-180 group-open:bg-tac14-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="grid gap-5 px-5 pb-5">
          <ul class="grid gap-x-6 gap-y-2.5 border-t border-tac14-line pt-5 text-[14px] text-tac14-ink sm:grid-cols-2">
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited projects</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>100 GB file storage</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Preview deploys per branch</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Priority email support</li>
          </ul>
          <button type="button" class="min-h-11 w-full rounded-xl bg-linear-to-r from-tac14-acc to-tac14-acc2 px-5 text-[14.5px] font-semibold text-white shadow-[0_8px_20px_-8px_oklch(0.53_0.21_290/0.7)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac14-acc">Start 14-day trial</button>
        </div>
      </details>

      <details name="tac14-plans" class="group relative rounded-2xl bg-white/55 ring-1 ring-tac14-line transition-[scale,box-shadow,margin,background-color] duration-500 ease-[cubic-bezier(0.3,1.25,0.4,1)] hover:bg-white/80 open:my-3 open:scale-[1.02] open:bg-white open:shadow-tac14-lift open:ring-tac14-acc/15 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-[background-color] motion-reduce:open:my-0 motion-reduce:open:scale-100 motion-reduce:details-content:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-2xl px-5 py-4 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac14-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute inset-x-6 top-0 h-[3px] rounded-b-full bg-linear-to-r from-tac14-acc to-tac14-acc2 opacity-0 transition-opacity duration-500 group-open:opacity-100"></span>
          <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-xl bg-tac14-soft text-tac14-acc ring-1 ring-tac14-acc/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac14-acc group-open:to-tac14-acc2 group-open:text-white"><svg viewBox="0 0 24 24" width="20" height="20"><rect x="4" y="4" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="13" y="4" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="4" y="13" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="13" y="13" width="7" height="7" rx="1.5" fill="currentColor"/></svg></span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="text-[17px] font-bold tracking-[-0.01em]">Scale</span>
            <span class="text-[13px] text-tac14-mut">For companies</span>
          </span>
          <span class="text-right text-[22px] font-extrabold tracking-[-0.02em] transition-colors duration-300 group-open:text-tac14-acc">Custom</span>
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac14-soft text-tac14-mut transition duration-300 group-open:rotate-180 group-open:bg-tac14-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="grid gap-5 px-5 pb-5">
          <ul class="grid gap-x-6 gap-y-2.5 border-t border-tac14-line pt-5 text-[14px] text-tac14-ink sm:grid-cols-2">
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>SSO / SAML &amp; SCIM</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Audit logs, 1-year retention</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>4-hour support SLA</li>
            <li class="flex items-center gap-2.5"><svg aria-hidden="true" class="flex-none text-tac14-acc" viewBox="0 0 16 16" width="16" height="16"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Invoicing &amp; procurement</li>
          </ul>
          <button type="button" class="min-h-11 w-full rounded-xl bg-white px-5 text-[14.5px] font-semibold text-tac14-ink ring-1 ring-tac14-line transition hover:bg-tac14-soft focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac14-acc">Talk to sales</button>
        </div>
      </details>
    </div>

    <p aria-hidden="true" class="justify-self-center rounded-full border border-tac14-line bg-white/70 px-3.5 py-2 text-center font-tac14-mono text-[11.5px] text-tac14-mut">open:scale-[1.02] · open:shadow-tac14-lift · details name</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac14-bg: #f4f1ff;
  --color-tac14-bg: oklch(0.965 0.018 295);
  --color-tac14-glow: #e6dfff;
  --color-tac14-glow: oklch(0.92 0.045 295);
  --color-tac14-soft: #f4f1ff;
  --color-tac14-soft: oklch(0.965 0.018 295);
  --color-tac14-line: #d9d3f0;
  --color-tac14-line: oklch(0.88 0.04 295);
  --color-tac14-ink: #211d38;
  --color-tac14-ink: oklch(0.25 0.05 290);
  --color-tac14-mut: #5a5770;
  --color-tac14-mut: oklch(0.47 0.04 290);
  --color-tac14-acc: #7048d9;
  --color-tac14-acc: oklch(0.53 0.21 290);
  --color-tac14-acc2: #df67b0;
  --color-tac14-acc2: oklch(0.68 0.17 345);
  --font-tac14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tac14-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tac14-lift: 0 1px 2px oklch(0.25 0.05 290 / 0.08), 0 6px 14px -6px oklch(0.25 0.05 290 / 0.14), 0 30px 60px -18px oklch(0.45 0.15 290 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-14 {
  width: 100%;
  min-height: 100svh;
}
```
