---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-onboarding-stepper-css-counters/"
title: "Tailwind Onboarding Stepper with CSS Counters"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A deploy-platform setup checklist: self-numbering circles from CSS counters, a connector drawn per step so it stops cleanly at the last one, completed steps…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Onboarding Stepper with CSS Counters
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-onboarding-stepper-css-counters/

A deploy-platform setup checklist: self-numbering circles from CSS counters, a connector drawn per step so it stops cleanly at the last one, completed steps marked by a data attribute and the current step announced with aria-current.
## HTML
```html
<section class="tgx-25 w-full min-h-svh bg-tgx25-bg font-tgx25-sans px-6 py-10">
  <div class="w-[min(560px,100%)] mx-auto flex flex-col gap-6">
    <header class="flex flex-col gap-2">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx25-gold">Relay · Setup</p>
      <h2 class="text-[1.4rem] font-semibold text-white tracking-[-0.01em]">Two steps left before your first deploy</h2>
      <div class="flex items-center gap-3">
        <div role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" aria-label="Setup progress" class="h-1.5 flex-1 rounded-full bg-tgx25-line overflow-hidden"><span class="block h-full w-1/2 bg-tgx25-gold"></span></div>
        <span class="text-[0.74rem] tabular-nums text-tgx25-dim">2 / 4</span>
      </div>
    </header>
    <ol class="list-none [counter-reset:tgx25] flex flex-col gap-7 m-0 p-0">
      <li data-done class="[counter-increment:tgx25] relative grid grid-cols-[44px_minmax(0,1fr)] gap-x-3.5 *:col-start-2 before:col-start-1 before:row-start-1 before:content-[counter(tgx25)] before:w-9 before:aspect-square before:rounded-full before:grid before:place-items-center before:font-bold before:text-[0.9rem] before:text-tgx25-dim before:bg-tgx25-bg before:border-2 before:border-tgx25-line before:z-10 after:content-[''] after:absolute after:left-[17px] after:top-10 after:w-0.5 after:h-[calc(100%-36px+1.75rem)] after:bg-tgx25-line last:after:content-none data-done:before:content-['✓'] data-done:before:text-tgx25-bg data-done:before:bg-tgx25-gold data-done:before:border-tgx25-gold data-done:after:bg-tgx25-gold">
        <h3 class="text-[0.95rem] font-semibold text-tgx25-ink pt-1.5">Create your workspace</h3>
        <p class="text-[0.82rem] leading-[1.6] text-tgx25-dim mt-1">northwind-freight · 6 members invited</p>
      </li>
      <li data-done class="[counter-increment:tgx25] relative grid grid-cols-[44px_minmax(0,1fr)] gap-x-3.5 *:col-start-2 before:col-start-1 before:row-start-1 before:content-[counter(tgx25)] before:w-9 before:aspect-square before:rounded-full before:grid before:place-items-center before:font-bold before:text-[0.9rem] before:text-tgx25-dim before:bg-tgx25-bg before:border-2 before:border-tgx25-line before:z-10 after:content-[''] after:absolute after:left-[17px] after:top-10 after:w-0.5 after:h-[calc(100%-36px+1.75rem)] after:bg-tgx25-line last:after:content-none data-done:before:content-['✓'] data-done:before:text-tgx25-bg data-done:before:bg-tgx25-gold data-done:before:border-tgx25-gold data-done:after:bg-tgx25-gold">
        <h3 class="text-[0.95rem] font-semibold text-tgx25-ink pt-1.5">Connect a repository</h3>
        <p class="text-[0.82rem] leading-[1.6] text-tgx25-dim mt-1">GitHub · northwind/freight-api on <code class="font-tgx25-mono text-tgx25-ink">main</code></p>
      </li>
      <li aria-current="step" class="[counter-increment:tgx25] relative grid grid-cols-[44px_minmax(0,1fr)] gap-x-3.5 *:col-start-2 before:col-start-1 before:row-start-1 before:content-[counter(tgx25)] before:w-9 before:aspect-square before:rounded-full before:grid before:place-items-center before:font-bold before:text-[0.9rem] before:text-tgx25-dim before:bg-tgx25-bg before:border-2 before:border-tgx25-line before:z-10 after:content-[''] after:absolute after:left-[17px] after:top-10 after:w-0.5 after:h-[calc(100%-36px+1.75rem)] after:bg-tgx25-line last:after:content-none aria-[current=step]:before:text-tgx25-gold aria-[current=step]:before:border-tgx25-gold aria-[current=step]:before:animate-tgx25-pulse motion-reduce:aria-[current=step]:before:animate-none">
        <h3 class="text-[0.95rem] font-semibold text-tgx25-ink pt-1.5">Configure the build</h3>
        <p class="text-[0.82rem] leading-[1.6] text-tgx25-dim mt-1">Set the build command and the output directory. We detected a Vite project.</p>
        <div class="flex gap-2 mt-3 flex-wrap">
          <button type="button" class="inline-flex items-center min-h-11 px-4 rounded-full bg-tgx25-gold text-tgx25-bg text-[0.82rem] font-semibold cursor-pointer transition-colors hover:bg-tgx25-goldhover focus-visible:outline-2 focus-visible:outline-tgx25-gold focus-visible:outline-offset-2">Use detected settings</button>
          <button type="button" class="inline-flex items-center min-h-11 px-4 rounded-full border border-tgx25-line text-tgx25-ink text-[0.82rem] font-medium cursor-pointer transition-colors hover:bg-tgx25-hover focus-visible:outline-2 focus-visible:outline-tgx25-gold focus-visible:outline-offset-2">Edit manually</button>
        </div>
      </li>
      <li class="[counter-increment:tgx25] relative grid grid-cols-[44px_minmax(0,1fr)] gap-x-3.5 *:col-start-2 before:col-start-1 before:row-start-1 before:content-[counter(tgx25)] before:w-9 before:aspect-square before:rounded-full before:grid before:place-items-center before:font-bold before:text-[0.9rem] before:text-tgx25-dim before:bg-tgx25-bg before:border-2 before:border-tgx25-line before:z-10 after:content-[''] after:absolute after:left-[17px] after:top-10 after:w-0.5 after:h-[calc(100%-36px+1.75rem)] after:bg-tgx25-line last:after:content-none">
        <h3 class="text-[0.95rem] font-semibold text-tgx25-ink pt-1.5">Ship to production</h3>
        <p class="text-[0.82rem] leading-[1.6] text-tgx25-dim mt-1">No line below this step — the <code class="font-tgx25-mono text-tgx25-ink">last:</code> variant suppresses the connector.</p>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx25-bg: #1d1a14;
  --color-tgx25-bg: oklch(0.2 0.015 85);
  --color-tgx25-line: #4a4234;
  --color-tgx25-line: oklch(0.38 0.03 85);
  --color-tgx25-hover: #2a251c;
  --color-tgx25-hover: oklch(0.26 0.02 85);
  --color-tgx25-gold: #edc167;
  --color-tgx25-gold: oklch(0.83 0.13 85);
  --color-tgx25-goldhover: #f3d089;
  --color-tgx25-goldhover: oklch(0.87 0.11 85);
  --color-tgx25-ink: #f0ebe1;
  --color-tgx25-ink: oklch(0.94 0.01 85);
  --color-tgx25-dim: #bab1a0;
  --color-tgx25-dim: oklch(0.78 0.02 85);
  --font-tgx25-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx25-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tgx25-pulse: tgx25-pulse 2s ease-in-out infinite;
}

@keyframes tgx25-pulse {
  50% {
    box-shadow: 0 0 0 6px color-mix(in oklab, var(--color-tgx25-gold) 25%, transparent);
  }
}

.tgx-25 {
  width: 100%;
  min-height: 100svh;
}
```
