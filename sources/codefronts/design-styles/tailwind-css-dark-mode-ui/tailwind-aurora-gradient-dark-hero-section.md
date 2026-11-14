---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-aurora-gradient-dark-hero-section/"
title: "Tailwind Aurora Gradient Dark Hero Section"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A launch hero with a real atmosphere: three offset radial gradients — green, violet, cyan — masked into the top of the panel so the aurora fades before it…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Aurora Gradient Dark Hero Section
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-aurora-gradient-dark-hero-section/

A launch hero with a real atmosphere: three offset radial gradients — green, violet, cyan — masked into the top of the panel so the aurora fades before it reaches the text, drifting slowly under a faint grid. Headline, subhead, dual CTAs and a trust bar, sized to fill a viewport at any width. The drift stops under motion-reduce:; the gradient stays.
## HTML
```html
<div class="tdm-21 scheme-dark w-full min-h-svh bg-tdm21-bg font-tdm21-sans text-tdm21-ink antialiased">
  <section class="relative isolate grid min-h-svh grid-rows-[auto_1fr_auto] overflow-hidden px-5 sm:px-10">
    <span aria-hidden="true" class="absolute -inset-[20%] -z-10 bg-[radial-gradient(38%_32%_at_28%_18%,var(--color-tdm21-green),transparent_70%),radial-gradient(42%_36%_at_62%_10%,var(--color-tdm21-violet),transparent_70%),radial-gradient(34%_30%_at_80%_28%,var(--color-tdm21-cyan),transparent_70%)] blur-2xl [mask-image:linear-gradient(to_bottom,black_30%,transparent_68%)] animate-tdm21-drift motion-reduce:animate-none"></span>
    <span aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(var(--color-tdm21-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-tdm21-grid)_1px,transparent_1px)] bg-[size:56px_56px] [mask-image:radial-gradient(80%_60%_at_50%_30%,black,transparent)]"></span>
    <nav aria-label="Product" class="mx-auto flex w-full max-w-6xl items-center justify-between gap-4 py-5">
      <span class="flex items-center gap-2 font-tdm21-display text-lg font-bold tracking-tight"><svg class="size-5 text-tdm21-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c.6 4.3 2.7 6.4 7 7-4.3.6-6.4 2.7-7 7-.6-4.3-2.7-6.4-7-7 4.3-.6 6.4-2.7 7-7Z"/></svg>Northlight</span>
      <span class="hidden items-center gap-1 sm:flex"><a href="#tdm-21" class="rounded-lg px-3 py-2 text-sm text-tdm21-muted transition hover:text-tdm21-ink focus-visible:outline-2 focus-visible:outline-tdm21-focus">Platform</a><a href="#tdm-21" class="rounded-lg px-3 py-2 text-sm text-tdm21-muted transition hover:text-tdm21-ink focus-visible:outline-2 focus-visible:outline-tdm21-focus">Docs</a><a href="#tdm-21" class="rounded-lg px-3 py-2 text-sm text-tdm21-muted transition hover:text-tdm21-ink focus-visible:outline-2 focus-visible:outline-tdm21-focus">Pricing</a></span>
      <a href="#tdm-21" class="inline-flex min-h-10 items-center rounded-full border border-tdm21-line bg-tdm21-ink/5 px-4 text-[13px] font-medium backdrop-blur transition hover:bg-tdm21-ink/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm21-focus">Sign in</a>
    </nav>
    <div class="mx-auto grid max-w-4xl content-center justify-items-center gap-7 py-16 text-center">
      <a href="#tdm-21" class="inline-flex items-center gap-2 rounded-full border border-tdm21-line bg-tdm21-raised/60 py-1.5 pr-3.5 pl-1.5 text-[13px] text-tdm21-muted backdrop-blur transition hover:text-tdm21-ink focus-visible:outline-2 focus-visible:outline-tdm21-focus"><span class="rounded-full bg-tdm21-acc px-2 py-0.5 text-[11px] font-semibold text-tdm21-acc-ink">v4.2</span>Edge runtime · 34 regions live<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></a>
      <h1 class="font-tdm21-display text-[clamp(2.6rem,7.5vw,5.4rem)] leading-[0.98] font-extrabold tracking-[-0.045em] text-balance">Ship the dark theme you actually designed</h1>
      <p class="max-w-[58ch] text-[clamp(1rem,1.6vw,1.15rem)]/relaxed text-pretty text-tdm21-muted">Token-level theming, per-scheme contrast audits and a preview that renders both palettes side by side. No inversion filters, no second stylesheet to maintain.</p>
      <div class="flex flex-wrap justify-center gap-3">
        <a href="#tdm-21" class="group/cta inline-flex min-h-12 items-center gap-2 rounded-full bg-tdm21-acc px-6 text-[15px] font-semibold text-tdm21-acc-ink shadow-[0_0_0_1px_rgb(255_255_255/.2)_inset,0_12px_40px_-10px_var(--color-tdm21-violet)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdm21-focus">Start building<svg class="size-4 transition-transform group-hover/cta:translate-x-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></a>
        <a href="#tdm-21" class="inline-flex min-h-12 items-center gap-2 rounded-full border border-tdm21-line bg-tdm21-ink/5 px-6 text-[15px] font-medium backdrop-blur transition hover:bg-tdm21-ink/10 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdm21-focus"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m10 8.5 5.5 3.5-5.5 3.5Z"/></svg>Watch the 3-min tour</a>
      </div>
    </div>
    <div class="mx-auto grid w-full max-w-5xl justify-items-center gap-4 border-t border-tdm21-line py-8">
      <p class="font-tdm21-mono text-[11px] uppercase tracking-[0.18em] text-tdm21-muted">Powering theming at</p>
      <div class="flex flex-wrap justify-center gap-x-10 gap-y-3 font-tdm21-display text-lg font-semibold tracking-tight text-tdm21-muted"><span class="transition hover:text-tdm21-ink">MERIDIAN</span><span class="transition hover:text-tdm21-ink">Northwind</span><span class="transition hover:text-tdm21-ink">Cadence</span><span class="transition hover:text-tdm21-ink">ATLAS</span><span class="transition hover:text-tdm21-ink">Foxglove</span></div>
    </div>
  </section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm21-bg: #06070c;
  --color-tdm21-raised: #101425;
  --color-tdm21-ink: #eef1f8;
  --color-tdm21-muted: #a0a8be;
  --color-tdm21-line: rgb(238 241 248 / .12);
  --color-tdm21-grid: rgb(238 241 248 / .04);
  --color-tdm21-green: rgb(52 211 153 / .42);
  --color-tdm21-violet: rgb(139 92 246 / .5);
  --color-tdm21-cyan: rgb(56 189 248 / .4);
  --color-tdm21-acc: #e0e7ff;
  --color-tdm21-acc-ink: #0a0f22;
  --color-tdm21-focus: #a5b4fc;
  --font-tdm21-display: 'Bricolage Grotesque', 'Geist', ui-sans-serif, sans-serif;
  --font-tdm21-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm21-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tdm21-drift: tdm21-drift 24s ease-in-out infinite alternate;

  @keyframes tdm21-drift {
    from {
      translate: -3% 0;
      rotate: -2deg;
    }

    to {
      translate: 3% 2%;
      rotate: 3deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
