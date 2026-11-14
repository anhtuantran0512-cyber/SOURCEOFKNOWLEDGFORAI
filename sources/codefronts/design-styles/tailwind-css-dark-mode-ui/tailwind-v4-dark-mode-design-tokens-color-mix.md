---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-v4-dark-mode-design-tokens-color-mix/"
title: "Tailwind v4 Dark Mode Design Tokens with color-mix()"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The architecture that stops a dark theme becoming forty hand-picked hex codes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind v4 Dark Mode Design Tokens with color-mix()
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-v4-dark-mode-design-tokens-color-mix/

The architecture that stops a dark theme becoming forty hand-picked hex codes. Declare a three-stop primitive ramp once as light-dark() pairs, then derive every semantic token — surface, raised, hairline, muted ink, accent wash — inside @theme with color-mix(in oklab, …). Two cards pinned to opposite schemes prove the recipes adapt instead of inverting.
## HTML
```html
<div class="tdm-03 scheme-light-dark has-[#tdm-03-toggle:checked]:scheme-dark dark:has-[#tdm-03-toggle:checked]:scheme-light w-full min-h-svh bg-tdm03-surface font-tdm03-sans text-tdm03-ink antialiased transition-colors duration-300">
  <div class="mx-auto grid min-h-svh max-w-6xl content-center gap-8 px-5 py-14 sm:px-10">
    <header class="flex flex-wrap items-end justify-between gap-5">
      <div class="grid gap-2.5">
        <p class="font-tdm03-mono text-[11px] uppercase tracking-[0.16em] text-tdm03-brand">Token layer</p>
        <h1 class="text-[clamp(1.75rem,3.6vw,2.6rem)] font-semibold tracking-[-0.04em] text-balance">Primitives in, semantics out</h1>
        <p class="max-w-[60ch] text-[15px]/relaxed text-pretty text-tdm03-muted">Six semantic tokens derived from a three-stop ramp with <code class="font-tdm03-mono text-[13px] text-tdm03-ink">color-mix(in oklab)</code>. Flip the theme and only the ends of the ramp swap.</p>
      </div>
      <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm03-line bg-tdm03-surface transition duration-200 hover:-translate-y-px hover:border-tdm03-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm03-focus motion-reduce:transition-none ">
        <input id="tdm-03-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm03-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm03-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
    </header>
    <div class="grid items-start gap-5 lg:grid-cols-[20rem_minmax(0,1fr)]">
      <section class="grid gap-5 rounded-3xl border border-tdm03-line bg-tdm03-raised p-5" aria-label="Token ramp">
        <div class="grid gap-2.5">
          <h2 class="font-tdm03-mono text-[11px] uppercase tracking-[0.12em] text-tdm03-muted">Primitives</h2>
          <ul class="grid gap-1.5">
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-g0"></span><code>--g0</code><em class="text-[11px] not-italic text-tdm03-muted">surface end</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-g6"></span><code>--g6</code><em class="text-[11px] not-italic text-tdm03-muted">midpoint</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-g12"></span><code>--g12</code><em class="text-[11px] not-italic text-tdm03-muted">ink end</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-brand"></span><code>--brand</code><em class="text-[11px] not-italic text-tdm03-muted">accent</em></li>
          </ul>
        </div>
        <div class="grid gap-2.5">
          <h2 class="font-tdm03-mono text-[11px] uppercase tracking-[0.12em] text-tdm03-muted">Derived semantics</h2>
          <ul class="grid gap-1.5">
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-surface"></span><code>--surface</code><em class="text-[11px] not-italic text-tdm03-muted">g12 3%</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-raised"></span><code>--raised</code><em class="text-[11px] not-italic text-tdm03-muted">g12 7%</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-line"></span><code>--line</code><em class="text-[11px] not-italic text-tdm03-muted">g12 12%</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-muted"></span><code>--muted</code><em class="text-[11px] not-italic text-tdm03-muted">g0 42%</em></li>
            <li class="grid grid-cols-[1.5rem_1fr_auto] items-center gap-3 rounded-xl px-1.5 py-1 font-tdm03-mono text-[12.5px] hover:bg-tdm03-surface"><span class="size-6 rounded-lg border border-tdm03-line bg-tdm03-wash"></span><code>--wash</code><em class="text-[11px] not-italic text-tdm03-muted">brand 14%</em></li>
          </ul>
        </div>
      </section>
      <div class="grid gap-4 sm:grid-cols-2">
        <article class="scheme-light grid gap-4 rounded-3xl border border-tdm03-line bg-tdm03-raised p-5 text-tdm03-ink shadow-[0_30px_60px_-40px_rgb(0_0_0/.5)]">
          <div class="flex items-center justify-between"><p class="rounded-full bg-tdm03-wash px-2.5 py-1 font-tdm03-mono text-[11px] text-tdm03-brand">Light ramp</p><code class="font-tdm03-mono text-[11px] text-tdm03-muted">scheme-light</code></div>
          <div><h3 class="text-sm font-medium text-tdm03-muted">Usage volume</h3><p class="mt-1 flex items-baseline gap-2 text-[34px] font-semibold tracking-[-0.04em] tabular-nums">184,204<span class="text-sm font-normal tracking-normal text-tdm03-muted">events</span></p></div>
          <div class="flex h-24 items-end gap-1.5 rounded-2xl border border-tdm03-line bg-tdm03-surface p-3" aria-hidden="true"><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:38%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:54%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:44%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:72%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:61%"></i><i class="flex-1 rounded-md bg-tdm03-brand" style="height:88%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:76%"></i></div>
          <div class="flex items-center justify-between gap-3"><span class="text-[13px] text-tdm03-muted">Same token names</span><button type="button" class="min-h-11 rounded-xl bg-tdm03-brand px-4 text-sm font-medium text-tdm03-brand-ink transition hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm03-focus">Inspect</button></div>
        </article>
        <article class="scheme-dark grid gap-4 rounded-3xl border border-tdm03-line bg-tdm03-raised p-5 text-tdm03-ink shadow-[0_30px_60px_-40px_rgb(0_0_0/.5)]">
          <div class="flex items-center justify-between"><p class="rounded-full bg-tdm03-wash px-2.5 py-1 font-tdm03-mono text-[11px] text-tdm03-brand">Dark ramp</p><code class="font-tdm03-mono text-[11px] text-tdm03-muted">scheme-dark</code></div>
          <div><h3 class="text-sm font-medium text-tdm03-muted">Usage volume</h3><p class="mt-1 flex items-baseline gap-2 text-[34px] font-semibold tracking-[-0.04em] tabular-nums">184,204<span class="text-sm font-normal tracking-normal text-tdm03-muted">events</span></p></div>
          <div class="flex h-24 items-end gap-1.5 rounded-2xl border border-tdm03-line bg-tdm03-surface p-3" aria-hidden="true"><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:38%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:54%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:44%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:72%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:61%"></i><i class="flex-1 rounded-md bg-tdm03-brand" style="height:88%"></i><i class="flex-1 rounded-md bg-tdm03-brand/35" style="height:76%"></i></div>
          <div class="flex items-center justify-between gap-3"><span class="text-[13px] text-tdm03-muted">Recipes unchanged</span><button type="button" class="min-h-11 rounded-xl bg-tdm03-brand px-4 text-sm font-medium text-tdm03-brand-ink transition hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm03-focus">Inspect</button></div>
        </article>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm03-g0: light-dark(#ffffff, #0b0b0f);
  --color-tdm03-g6: light-dark(#71717a, #8b8b96);
  --color-tdm03-g12: light-dark(#09090b, #fafafa);
  --color-tdm03-brand: light-dark(#0369a1, #38bdf8);
  --color-tdm03-brand-ink: light-dark(#ffffff, #04121b);
  --color-tdm03-focus: light-dark(#0369a1, #7dd3fc);
  --color-tdm03-surface: color-mix(in oklab, var(--color-tdm03-g0), var(--color-tdm03-g12) 3%);
  --color-tdm03-raised: color-mix(in oklab, var(--color-tdm03-g0), var(--color-tdm03-g12) 7%);
  --color-tdm03-line: color-mix(in oklab, var(--color-tdm03-g0), var(--color-tdm03-g12) 12%);
  --color-tdm03-ink: var(--color-tdm03-g12);
  --color-tdm03-muted: color-mix(in oklab, var(--color-tdm03-g12), var(--color-tdm03-g0) 42%);
  --color-tdm03-wash: color-mix(in oklab, var(--color-tdm03-brand) 14%, var(--color-tdm03-g0));
  --color-tdm03-acc: var(--color-tdm03-brand);
  --color-tdm03-sun: light-dark(#b45309, transparent);
  --color-tdm03-moon: light-dark(transparent, #bae6fd);
  --font-tdm03-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm03-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
