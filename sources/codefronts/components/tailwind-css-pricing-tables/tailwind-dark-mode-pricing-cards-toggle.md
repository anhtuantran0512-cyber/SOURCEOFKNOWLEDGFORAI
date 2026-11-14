---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-dark-mode-pricing-cards-toggle/"
title: "Tailwind Dark Mode Pricing Cards with Light / Dark Toggle"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Theme-aware pricing, the v4 way: every utility reads an @theme token (bg-tpt04-surface, text-tpt04-mut…), so one CSS rule re-points the tokens and the whole…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Pricing Cards with Light / Dark Toggle
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-dark-mode-pricing-cards-toggle/

Theme-aware pricing, the v4 way: every utility reads an @theme token (bg-tpt04-surface, text-tpt04-mut…), so one CSS rule re-points the tokens and the whole component crossfades. No dark: class is duplicated on any element — the palette stays a palette, and the switch is a real role="switch".
## HTML
```html
<section class="tpt-04 group/p w-full min-h-svh grid place-items-center bg-tpt04-bg px-5 py-16 font-tpt04-sans text-tpt04-ink antialiased transition-colors duration-500" aria-label="Theme-adaptive pricing cards">
  <div class="grid w-full max-w-5xl gap-9">
    <header class="flex flex-wrap items-center justify-between gap-5">
      <h2 class="text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">Looks right in any theme</h2>
      <input type="checkbox" id="tpt04-theme" role="switch" class="peer sr-only" aria-label="Dark theme">
      <label for="tpt04-theme" class="relative flex h-11 cursor-pointer items-center gap-1 rounded-full border border-tpt04-line bg-tpt04-surface p-1 transition-colors duration-500 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tpt04-acc">
        <span aria-hidden="true" class="absolute top-1 left-1 size-9 rounded-full bg-tpt04-acc/20 transition-transform duration-300 ease-[cubic-bezier(.5,1.5,.4,1)] group-has-checked/p:translate-x-10"></span>
        <svg aria-hidden="true" class="relative size-9 p-2 text-tpt04-acc-ink transition-opacity group-has-checked/p:opacity-45" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg aria-hidden="true" class="relative size-9 p-2 text-tpt04-acc-ink opacity-45 transition-opacity group-has-checked/p:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>
      </label>
    </header>
    <div class="grid gap-5 md:grid-cols-3">
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt04-line bg-tpt04-surface p-7 transition-colors duration-500">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt04-mut uppercase transition-colors duration-500">Solo</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$8<small class="text-[15px] font-semibold tracking-normal text-tpt04-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt04-body transition-colors duration-500 *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt04-acc-ink *:before:content-['✓']"><li>1 workspace</li><li>Core blocks</li><li>7-day history</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt04-line text-sm font-bold text-tpt04-ink no-underline transition-colors duration-300 hover:border-tpt04-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt04-acc">Choose Solo</a>
      </article>
      <article class="relative flex flex-col gap-4 rounded-[20px] bg-tpt04-surface p-7 ring-2 ring-tpt04-acc transition-colors duration-500">
        <span class="absolute -top-3 left-6 rounded-full bg-tpt04-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-tpt04-on-acc uppercase transition-colors duration-500">Most popular</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt04-acc-ink uppercase transition-colors duration-500">Craft</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$20<small class="text-[15px] font-semibold tracking-normal text-tpt04-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt04-body transition-colors duration-500 *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt04-acc-ink *:before:content-['✓']"><li>5 workspaces</li><li>All blocks</li><li>Unlimited version history</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt04-acc text-sm font-bold text-tpt04-on-acc no-underline transition duration-300 hover:brightness-105 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt04-acc">Choose Craft</a>
      </article>
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt04-line bg-tpt04-surface p-7 transition-colors duration-500">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt04-mut uppercase transition-colors duration-500">Studio</h3>
        <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$45<small class="text-[15px] font-semibold tracking-normal text-tpt04-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt04-body transition-colors duration-500 *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt04-acc-ink *:before:content-['✓']"><li>Unlimited workspaces</li><li>Team roles</li><li>Priority support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt04-line text-sm font-bold text-tpt04-ink no-underline transition-colors duration-300 hover:border-tpt04-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt04-acc">Choose Studio</a>
      </article>
    </div>
    <p aria-hidden="true" class="justify-self-center rounded-full border border-tpt04-line px-3.5 py-2 font-tpt04-mono text-[11.5px] text-tpt04-mut transition-colors duration-500">@theme tokens · one swap rule · transition-colors</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt04-bg: #f4f2ec;
  --color-tpt04-bg: oklch(0.96 0.008 90);
  --color-tpt04-surface: #ffffff;
  --color-tpt04-surface: oklch(1 0 0);
  --color-tpt04-line: #e2dfd5;
  --color-tpt04-line: oklch(0.9 0.012 90);
  --color-tpt04-ink: #211f1a;
  --color-tpt04-ink: oklch(0.23 0.01 90);
  --color-tpt04-body: #4a473f;
  --color-tpt04-body: oklch(0.41 0.012 90);
  --color-tpt04-mut: #6a665b;
  --color-tpt04-mut: oklch(0.52 0.015 90);
  --color-tpt04-acc: #d88a1e;
  --color-tpt04-acc: oklch(0.7 0.15 65);
  --color-tpt04-acc-ink: #9a5a00;
  --color-tpt04-acc-ink: oklch(0.52 0.12 62);
  --color-tpt04-on-acc: #1a1206;
  --color-tpt04-on-acc: oklch(0.2 0.03 70);
  --font-tpt04-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpt04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-04 {
  width: 100%;
  min-height: 100svh;
}
/* The whole dark theme: re-point the tokens every utility already reads.
   In production: [data-theme="dark"] .tpt-04 { … } */

.tpt-04:has(#tpt04-theme:checked) {
  --color-tpt04-bg: #14130f;
  --color-tpt04-bg: oklch(0.18 0.008 85);
  --color-tpt04-surface: #1f1d17;
  --color-tpt04-surface: oklch(0.225 0.01 85);
  --color-tpt04-line: #36332a;
  --color-tpt04-line: oklch(0.32 0.012 85);
  --color-tpt04-ink: #f1eee3;
  --color-tpt04-ink: oklch(0.95 0.012 90);
  --color-tpt04-body: #cfcabb;
  --color-tpt04-body: oklch(0.84 0.018 90);
  --color-tpt04-mut: #a7a190;
  --color-tpt04-mut: oklch(0.71 0.02 90);
  --color-tpt04-acc: #f0b44a;
  --color-tpt04-acc: oklch(0.8 0.14 75);
  --color-tpt04-acc-ink: #f0b44a;
  --color-tpt04-acc-ink: oklch(0.8 0.14 75);
}
```
