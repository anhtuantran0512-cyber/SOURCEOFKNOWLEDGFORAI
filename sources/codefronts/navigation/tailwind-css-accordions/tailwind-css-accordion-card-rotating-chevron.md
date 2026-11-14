---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-accordion-card-rotating-chevron/"
title: "Tailwind CSS Accordion Card with Rotating Chevron"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The accordion you actually ship, finished to shadcn/ui standards: separated zinc cards with hairline rings, an SVG chevron in a fixed chip that turns…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Accordion Card with Rotating Chevron
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-accordion-card-rotating-chevron/

The accordion you actually ship, finished to shadcn/ui standards: separated zinc cards with hairline rings, an SVG chevron in a fixed chip that turns group-open:rotate-180, a 1px hover lift, an open-state ring tint, and a divider that exists only inside the open card. Set in a dark help-centre page, with a two-way height animation from the details-content: variant.
## HTML
```html
<section class="tac-10 w-full min-h-svh grid place-items-center bg-tac10-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tac10-glow),transparent)] px-5 py-14 font-tac10-sans text-tac10-ink [interpolate-size:allow-keywords]" aria-label="Rotating chevron card accordion demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[600px]">
      <nav aria-label="Breadcrumb" class="mb-5 flex items-center gap-2 text-[13px] text-tac10-mut">
        <span>Help center</span><svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="m6 4 4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="text-tac10-ink">Account &amp; security</span>
      </nav>
      <header class="mb-7 flex items-start gap-4">
        <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-xl bg-tac10-card ring-1 ring-white/10 shadow-[inset_0_1px_0_oklch(1_0_0/0.06)]"><svg viewBox="0 0 24 24" width="20" height="20"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="15.5" r="1.4" fill="currentColor"/></svg></span>
        <div>
          <h2 class="text-2xl font-semibold tracking-[-0.025em]">Account &amp; security</h2>
          <p class="mt-1 text-sm text-tac10-mut">4 articles · Updated 2 days ago</p>
        </div>
      </header>

      <div class="flex flex-col gap-3">
        <details class="group rounded-xl bg-tac10-card shadow-[0_1px_2px_oklch(0_0_0/0.4)] ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-200 hover:-translate-y-px hover:bg-tac10-card-hi hover:shadow-[0_10px_30px_-12px_oklch(0_0_0/0.7)] open:bg-tac10-card-hi open:ring-white/16 motion-reduce:transition-none motion-reduce:hover:translate-y-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-300 details-content:ease-[cubic-bezier(.4,0,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-xl py-3 pr-4 pl-5 text-[15px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc [&::-webkit-details-marker]:hidden">
            <span class="flex-1">How do I reset a teammate's password?</span>
            <span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-md bg-white/4 text-tac10-mut ring-1 ring-white/10 transition-[rotate,color,background-color] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:text-tac10-ink group-open:rotate-180 group-open:bg-white/10 group-open:text-tac10-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="mx-5 border-t border-white/8 pt-4 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-tac10-quiet text-pretty">Admins can send a reset link from <kbd class="whitespace-nowrap rounded-md bg-white/6 px-1.5 py-0.5 font-tac10-mono text-[12.5px] text-tac10-ink ring-1 ring-white/10">Members → ⋯ → Reset password</kbd>. The link expires in 30 minutes and signs that person out of every active session.</p>
            <a href="#tac10-contact" class="mt-3 inline-flex min-h-11 items-center gap-1.5 rounded-md text-[13.5px] font-medium text-tac10-acc hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc">Read the full guide<svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="M3.5 8h9m-3.5-3.5L12.5 8 9 11.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
          </div>
        </details>

        <details class="group rounded-xl bg-tac10-card shadow-[0_1px_2px_oklch(0_0_0/0.4)] ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-200 hover:-translate-y-px hover:bg-tac10-card-hi hover:shadow-[0_10px_30px_-12px_oklch(0_0_0/0.7)] open:bg-tac10-card-hi open:ring-white/16 motion-reduce:transition-none motion-reduce:hover:translate-y-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-300 details-content:ease-[cubic-bezier(.4,0,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-xl py-3 pr-4 pl-5 text-[15px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Where do I find my API keys?</span>
            <span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-md bg-white/4 text-tac10-mut ring-1 ring-white/10 transition-[rotate,color,background-color] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:text-tac10-ink group-open:rotate-180 group-open:bg-white/10 group-open:text-tac10-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="mx-5 border-t border-white/8 pt-4 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-tac10-quiet text-pretty">Under <kbd class="whitespace-nowrap rounded-md bg-white/6 px-1.5 py-0.5 font-tac10-mono text-[12.5px] text-tac10-ink ring-1 ring-white/10">Settings → Developers</kbd>. Keys are shown once at creation, so store them in a secret manager &mdash; and rotate them from the same screen without downtime.</p>
          </div>
        </details>

        <details class="group rounded-xl bg-tac10-card shadow-[0_1px_2px_oklch(0_0_0/0.4)] ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-200 hover:-translate-y-px hover:bg-tac10-card-hi hover:shadow-[0_10px_30px_-12px_oklch(0_0_0/0.7)] open:bg-tac10-card-hi open:ring-white/16 motion-reduce:transition-none motion-reduce:hover:translate-y-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-300 details-content:ease-[cubic-bezier(.4,0,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-xl py-3 pr-4 pl-5 text-[15px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Can I enforce two-factor authentication?</span>
            <span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-md bg-white/4 text-tac10-mut ring-1 ring-white/10 transition-[rotate,color,background-color] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:text-tac10-ink group-open:rotate-180 group-open:bg-white/10 group-open:text-tac10-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="mx-5 border-t border-white/8 pt-4 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-tac10-quiet text-pretty">Yes, on Team and Enterprise plans. Turn on <span class="font-medium text-tac10-ink">Require 2FA</span> under Security; members without it are prompted at next sign-in and can't open the workspace until they enrol.</p>
          </div>
        </details>

        <details class="group rounded-xl bg-tac10-card shadow-[0_1px_2px_oklch(0_0_0/0.4)] ring-1 ring-white/8 transition-[translate,box-shadow,background-color] duration-200 hover:-translate-y-px hover:bg-tac10-card-hi hover:shadow-[0_10px_30px_-12px_oklch(0_0_0/0.7)] open:bg-tac10-card-hi open:ring-white/16 motion-reduce:transition-none motion-reduce:hover:translate-y-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-300 details-content:ease-[cubic-bezier(.4,0,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-xl py-3 pr-4 pl-5 text-[15px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Can I export my workspace data?</span>
            <span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-md bg-white/4 text-tac10-mut ring-1 ring-white/10 transition-[rotate,color,background-color] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:text-tac10-ink group-open:rotate-180 group-open:bg-white/10 group-open:text-tac10-ink motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="mx-5 border-t border-white/8 pt-4 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-tac10-quiet text-pretty">Full exports (JSON plus attachments) run from <kbd class="whitespace-nowrap rounded-md bg-white/6 px-1.5 py-0.5 font-tac10-mono text-[12.5px] text-tac10-ink ring-1 ring-white/10">Settings → Export</kbd> and email you a signed download link, usually within five minutes.</p>
          </div>
        </details>
      </div>

      <div id="tac10-contact" class="mt-6 flex flex-wrap items-center justify-between gap-4 rounded-xl border border-dashed border-white/12 px-5 py-4">
        <p class="text-sm text-tac10-mut"><span class="font-medium text-tac10-ink">Still stuck?</span> Support replies in under 2 hours.</p>
        <a href="#tac10-contact" class="inline-flex min-h-11 items-center rounded-lg bg-tac10-ink px-4 text-sm font-medium text-tac10-bg shadow-[0_1px_2px_oklch(0_0_0/0.4)] transition-colors hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac10-acc">Contact support</a>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-xl px-3.5 py-2 text-center font-tac10-mono text-[11.5px] text-tac10-mut ring-1 ring-white/10">group-open:rotate-180 · ring-white/8 · details-content:h-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac10-bg: #09090b;
  --color-tac10-bg: oklch(0.141 0.005 286);
  --color-tac10-glow: #1d1d2466;
  --color-tac10-glow: oklch(0.24 0.015 286 / 0.4);
  --color-tac10-card: #121215;
  --color-tac10-card: oklch(0.18 0.005 286);
  --color-tac10-card-hi: #17171b;
  --color-tac10-card-hi: oklch(0.205 0.006 286);
  --color-tac10-ink: #fafafa;
  --color-tac10-ink: oklch(0.985 0 0);
  --color-tac10-quiet: #c4c4cb;
  --color-tac10-quiet: oklch(0.82 0.008 286);
  --color-tac10-mut: #9f9fa9;
  --color-tac10-mut: oklch(0.71 0.013 286);
  --color-tac10-acc: #8b9cff;
  --color-tac10-acc: oklch(0.72 0.14 275);
  --font-tac10-sans: 'Geist', system-ui, sans-serif;
  --font-tac10-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-10 {
  width: 100%;
  min-height: 100svh;
}
```
