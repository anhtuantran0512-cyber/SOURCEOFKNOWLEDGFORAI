---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-tabs/"
title: "Tailwind CSS Horizontal Accordion Tabs"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The foundational horizontal accordion as a careers-page studio picker: collapsed columns read their city vertically with [writing-mode:vertical-rl], and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Horizontal Accordion Tabs
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-horizontal-accordion-tabs/

The foundational horizontal accordion as a careers-page studio picker: collapsed columns read their city vertically with [writing-mode:vertical-rl], and the checked radio's column animates has-checked:grow-[6] sideways while its siblings compress. A @container query flips the whole row into a stacked grid-rows-[0fr]→[1fr] accordion on narrow stages.
## HTML
```html
<section class="tac-25 w-full min-h-svh grid place-items-center bg-tac25-bg bg-[radial-gradient(90%_60%_at_50%_0%,var(--color-tac25-glow),transparent_70%)] px-5 py-14 font-tac25-sans text-tac25-ink" aria-label="Horizontal accordion tabs demo">
  <div class="grid w-full max-w-5xl gap-9">
    <header class="grid gap-3 sm:grid-cols-[1fr_auto] sm:items-end">
      <div>
        <p class="font-tac25-mono text-xs font-medium tracking-[0.14em] text-tac25-acc uppercase">Careers · Studios</p>
        <h2 class="mt-2 text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-bold tracking-[-0.03em] text-balance">Four studios. One remote-first team.</h2>
      </div>
      <p class="max-w-[34ch] text-[15px] leading-relaxed text-tac25-mut">Pick a city to see who sits there, what they ship and which roles are open right now.</p>
    </header>

    <div class="@container w-full">
      <div role="radiogroup" aria-label="Choose a studio location" class="flex h-[25rem] gap-3 @max-2xl:h-auto @max-2xl:flex-col @max-2xl:gap-2.5">

        <label class="group/p relative flex min-w-16 grow basis-0 cursor-pointer overflow-hidden rounded-2xl bg-tac25-card shadow-tac25-soft ring-1 ring-tac25-line transition-[flex-grow,box-shadow] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:ring-tac25-acc/35 has-checked:grow-[6] has-checked:shadow-tac25-lift has-checked:ring-tac25-acc/45 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac25-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac25-studio" id="tac25-cph" class="sr-only" checked>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(circle,var(--color-tac25-dot)_1px,transparent_1.5px),radial-gradient(120%_80%_at_100%_0%,var(--color-tac25-tint),transparent_60%)] bg-[size:16px_16px,auto] [mask-image:radial-gradient(90%_75%_at_100%_0%,#000_20%,transparent_75%)] opacity-0 transition-opacity duration-500 group-has-checked/p:opacity-100"></span>
          <span class="absolute inset-0 flex flex-col items-center justify-between py-5 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3.5 @max-2xl:px-5 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100">
            <i class="font-tac25-mono text-xs font-semibold not-italic text-tac25-acc">01</i>
            <b class="rotate-180 text-[15px] font-semibold tracking-[0.12em] text-tac25-mut uppercase transition-colors group-hover/p:text-tac25-ink [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:text-tac25-ink @max-2xl:[writing-mode:horizontal-tb]">Copenhagen</b>
            <span class="size-2 rounded-full bg-tac25-ok shadow-[0_0_0_4px_var(--color-tac25-ok-soft)] @max-2xl:ml-auto"></span>
          </span>
          <span class="relative flex min-w-0 flex-1 items-end opacity-0 transition-[opacity,translate] duration-300 translate-y-2 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[21rem] overflow-hidden @max-2xl:min-w-0 @max-2xl:min-h-0"><span class="block p-7 @max-2xl:px-5 @max-2xl:pt-0 @max-2xl:pb-5">
              <span class="flex flex-wrap items-center gap-2 @max-2xl:hidden">
                <span class="inline-flex items-center gap-1.5 rounded-full bg-tac25-ok-soft px-2.5 py-1 text-xs font-semibold text-tac25-ok-ink"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac25-ok"></span>HQ · Hiring</span>
                <span class="rounded-full bg-tac25-chip px-2.5 py-1 font-tac25-mono text-xs text-tac25-mut">UTC+1 · Nørrebro</span>
              </span>
              <b class="mt-4 block text-[clamp(30px,4vw,44px)] leading-none font-bold tracking-[-0.035em] @max-2xl:hidden">Copenhagen</b>
              <span class="mt-3 block max-w-[46ch] text-[15px] leading-relaxed text-tac25-mut @max-2xl:mt-0">Fourteen people over a bike shop in Nørrebro. Product, platform engineering — and the espresso machine that started the company.</span>
              <span class="mt-6 grid max-w-md grid-cols-3 divide-x divide-tac25-line rounded-xl bg-tac25-chip/70 ring-1 ring-tac25-line">
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">14</b><span class="text-xs text-tac25-mut">people</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">3</b><span class="text-xs text-tac25-mut">open roles</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">2019</b><span class="text-xs text-tac25-mut">founded</span></span>
              </span>
            </span></span>
          </span>
        </label>

        <label class="group/p relative flex min-w-16 grow basis-0 cursor-pointer overflow-hidden rounded-2xl bg-tac25-card shadow-tac25-soft ring-1 ring-tac25-line transition-[flex-grow,box-shadow] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:ring-tac25-acc/35 has-checked:grow-[6] has-checked:shadow-tac25-lift has-checked:ring-tac25-acc/45 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac25-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac25-studio" id="tac25-yyz" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(circle,var(--color-tac25-dot)_1px,transparent_1.5px),radial-gradient(120%_80%_at_100%_0%,var(--color-tac25-tint),transparent_60%)] bg-[size:16px_16px,auto] [mask-image:radial-gradient(90%_75%_at_100%_0%,#000_20%,transparent_75%)] opacity-0 transition-opacity duration-500 group-has-checked/p:opacity-100"></span>
          <span class="absolute inset-0 flex flex-col items-center justify-between py-5 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3.5 @max-2xl:px-5 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100">
            <i class="font-tac25-mono text-xs font-semibold not-italic text-tac25-acc">02</i>
            <b class="rotate-180 text-[15px] font-semibold tracking-[0.12em] text-tac25-mut uppercase transition-colors group-hover/p:text-tac25-ink [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:text-tac25-ink @max-2xl:[writing-mode:horizontal-tb]">Toronto</b>
            <span class="size-2 rounded-full bg-tac25-ok shadow-[0_0_0_4px_var(--color-tac25-ok-soft)] @max-2xl:ml-auto"></span>
          </span>
          <span class="relative flex min-w-0 flex-1 items-end opacity-0 transition-[opacity,translate] duration-300 translate-y-2 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[21rem] overflow-hidden @max-2xl:min-w-0 @max-2xl:min-h-0"><span class="block p-7 @max-2xl:px-5 @max-2xl:pt-0 @max-2xl:pb-5">
              <span class="flex flex-wrap items-center gap-2 @max-2xl:hidden">
                <span class="inline-flex items-center gap-1.5 rounded-full bg-tac25-ok-soft px-2.5 py-1 text-xs font-semibold text-tac25-ok-ink"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac25-ok"></span>Americas · Hiring</span>
                <span class="rounded-full bg-tac25-chip px-2.5 py-1 font-tac25-mono text-xs text-tac25-mut">UTC−5 · King West</span>
              </span>
              <b class="mt-4 block text-[clamp(30px,4vw,44px)] leading-none font-bold tracking-[-0.035em] @max-2xl:hidden">Toronto</b>
              <span class="mt-3 block max-w-[46ch] text-[15px] leading-relaxed text-tac25-mut @max-2xl:mt-0">Customer engineering and support, covering every timezone from UTC−8 to −3. The office dog is named Pixel and has a badge.</span>
              <span class="mt-6 grid max-w-md grid-cols-3 divide-x divide-tac25-line rounded-xl bg-tac25-chip/70 ring-1 ring-tac25-line">
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">9</b><span class="text-xs text-tac25-mut">people</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">2</b><span class="text-xs text-tac25-mut">open roles</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">2022</b><span class="text-xs text-tac25-mut">founded</span></span>
              </span>
            </span></span>
          </span>
        </label>

        <label class="group/p relative flex min-w-16 grow basis-0 cursor-pointer overflow-hidden rounded-2xl bg-tac25-card shadow-tac25-soft ring-1 ring-tac25-line transition-[flex-grow,box-shadow] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:ring-tac25-acc/35 has-checked:grow-[6] has-checked:shadow-tac25-lift has-checked:ring-tac25-acc/45 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac25-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac25-studio" id="tac25-lis" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(circle,var(--color-tac25-dot)_1px,transparent_1.5px),radial-gradient(120%_80%_at_100%_0%,var(--color-tac25-tint),transparent_60%)] bg-[size:16px_16px,auto] [mask-image:radial-gradient(90%_75%_at_100%_0%,#000_20%,transparent_75%)] opacity-0 transition-opacity duration-500 group-has-checked/p:opacity-100"></span>
          <span class="absolute inset-0 flex flex-col items-center justify-between py-5 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3.5 @max-2xl:px-5 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100">
            <i class="font-tac25-mono text-xs font-semibold not-italic text-tac25-acc">03</i>
            <b class="rotate-180 text-[15px] font-semibold tracking-[0.12em] text-tac25-mut uppercase transition-colors group-hover/p:text-tac25-ink [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:text-tac25-ink @max-2xl:[writing-mode:horizontal-tb]">Lisbon</b>
            <span class="size-2 rounded-full bg-tac25-idle shadow-[0_0_0_4px_var(--color-tac25-chip)] @max-2xl:ml-auto"></span>
          </span>
          <span class="relative flex min-w-0 flex-1 items-end opacity-0 transition-[opacity,translate] duration-300 translate-y-2 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[21rem] overflow-hidden @max-2xl:min-w-0 @max-2xl:min-h-0"><span class="block p-7 @max-2xl:px-5 @max-2xl:pt-0 @max-2xl:pb-5">
              <span class="flex flex-wrap items-center gap-2 @max-2xl:hidden">
                <span class="inline-flex items-center gap-1.5 rounded-full bg-tac25-chip px-2.5 py-1 text-xs font-semibold text-tac25-mut"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac25-idle"></span>EMEA · Full</span>
                <span class="rounded-full bg-tac25-chip px-2.5 py-1 font-tac25-mono text-xs text-tac25-mut">UTC+0 · Príncipe Real</span>
              </span>
              <b class="mt-4 block text-[clamp(30px,4vw,44px)] leading-none font-bold tracking-[-0.035em] @max-2xl:hidden">Lisbon</b>
              <span class="mt-3 block max-w-[46ch] text-[15px] leading-relaxed text-tac25-mut @max-2xl:mt-0">Design and research, in a tiled 1890s townhouse with a rooftop that hosts every quarterly review. No open seats until spring.</span>
              <span class="mt-6 grid max-w-md grid-cols-3 divide-x divide-tac25-line rounded-xl bg-tac25-chip/70 ring-1 ring-tac25-line">
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">7</b><span class="text-xs text-tac25-mut">people</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">0</b><span class="text-xs text-tac25-mut">open roles</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">2023</b><span class="text-xs text-tac25-mut">founded</span></span>
              </span>
            </span></span>
          </span>
        </label>

        <label class="group/p relative flex min-w-16 grow basis-0 cursor-pointer overflow-hidden rounded-2xl bg-tac25-card shadow-tac25-soft ring-1 ring-tac25-line transition-[flex-grow,box-shadow] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:ring-tac25-acc/35 has-checked:grow-[6] has-checked:shadow-tac25-lift has-checked:ring-tac25-acc/45 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tac25-acc motion-reduce:transition-none @max-2xl:basis-auto @max-2xl:flex-col">
          <input type="radio" name="tac25-studio" id="tac25-mel" class="sr-only">
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(circle,var(--color-tac25-dot)_1px,transparent_1.5px),radial-gradient(120%_80%_at_100%_0%,var(--color-tac25-tint),transparent_60%)] bg-[size:16px_16px,auto] [mask-image:radial-gradient(90%_75%_at_100%_0%,#000_20%,transparent_75%)] opacity-0 transition-opacity duration-500 group-has-checked/p:opacity-100"></span>
          <span class="absolute inset-0 flex flex-col items-center justify-between py-5 transition-opacity duration-200 group-has-checked/p:opacity-0 @max-2xl:relative @max-2xl:min-h-16 @max-2xl:flex-row @max-2xl:justify-start @max-2xl:gap-3.5 @max-2xl:px-5 @max-2xl:py-0 @max-2xl:group-has-checked/p:opacity-100">
            <i class="font-tac25-mono text-xs font-semibold not-italic text-tac25-acc">04</i>
            <b class="rotate-180 text-[15px] font-semibold tracking-[0.12em] text-tac25-mut uppercase transition-colors group-hover/p:text-tac25-ink [writing-mode:vertical-rl] @max-2xl:rotate-0 @max-2xl:text-tac25-ink @max-2xl:[writing-mode:horizontal-tb]">Melbourne</b>
            <span class="size-2 rounded-full bg-tac25-ok shadow-[0_0_0_4px_var(--color-tac25-ok-soft)] @max-2xl:ml-auto"></span>
          </span>
          <span class="relative flex min-w-0 flex-1 items-end opacity-0 transition-[opacity,translate] duration-300 translate-y-2 group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100 group-has-checked/p:delay-200 motion-reduce:transition-none @max-2xl:grid @max-2xl:grid-rows-[0fr] @max-2xl:translate-y-0 @max-2xl:transition-[grid-template-rows,opacity] @max-2xl:group-has-checked/p:grid-rows-[1fr] @max-2xl:group-has-checked/p:delay-0">
            <span class="block w-full min-w-[21rem] overflow-hidden @max-2xl:min-w-0 @max-2xl:min-h-0"><span class="block p-7 @max-2xl:px-5 @max-2xl:pt-0 @max-2xl:pb-5">
              <span class="flex flex-wrap items-center gap-2 @max-2xl:hidden">
                <span class="inline-flex items-center gap-1.5 rounded-full bg-tac25-ok-soft px-2.5 py-1 text-xs font-semibold text-tac25-ok-ink"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac25-ok"></span>APAC · Hiring</span>
                <span class="rounded-full bg-tac25-chip px-2.5 py-1 font-tac25-mono text-xs text-tac25-mut">UTC+10 · Fitzroy</span>
              </span>
              <b class="mt-4 block text-[clamp(30px,4vw,44px)] leading-none font-bold tracking-[-0.035em] @max-2xl:hidden">Melbourne</b>
              <span class="mt-3 block max-w-[46ch] text-[15px] leading-relaxed text-tac25-mut @max-2xl:mt-0">Our newest studio: three engineers, one designer, and the best coffee of the four offices — a claim hotly contested on Slack.</span>
              <span class="mt-6 grid max-w-md grid-cols-3 divide-x divide-tac25-line rounded-xl bg-tac25-chip/70 ring-1 ring-tac25-line">
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">4</b><span class="text-xs text-tac25-mut">people</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">5</b><span class="text-xs text-tac25-mut">open roles</span></span>
                <span class="px-4 py-3"><b class="block text-xl font-bold tracking-tight">2024</b><span class="text-xs text-tac25-mut">founded</span></span>
              </span>
            </span></span>
          </span>
        </label>

      </div>
    </div>

    <p aria-hidden="true" class="max-w-full justify-self-center rounded-full border text-center text-balance border-tac25-line bg-tac25-card/70 px-3.5 py-2 font-tac25-mono text-[11.5px] text-tac25-mut">has-checked:grow-[6] · [writing-mode:vertical-rl] · @max-2xl:flex-col</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac25-bg: #f2f4f8;
  --color-tac25-bg: oklch(0.966 0.006 265);
  --color-tac25-glow: #ffffff;
  --color-tac25-glow: oklch(1 0 0);
  --color-tac25-card: #ffffff;
  --color-tac25-card: oklch(1 0 0);
  --color-tac25-chip: #f1f3f7;
  --color-tac25-chip: oklch(0.962 0.006 265);
  --color-tac25-line: #e0e4ec;
  --color-tac25-line: oklch(0.91 0.01 265);
  --color-tac25-ink: #121726;
  --color-tac25-ink: oklch(0.2 0.03 265);
  --color-tac25-mut: #4d566b;
  --color-tac25-mut: oklch(0.46 0.03 265);
  --color-tac25-acc: #3b55e0;
  --color-tac25-acc: oklch(0.52 0.2 268);
  --color-tac25-tint: #e5eaff;
  --color-tac25-tint: oklch(0.93 0.04 268);
  --color-tac25-dot: #b7c2ee;
  --color-tac25-dot: oklch(0.82 0.06 268);
  --color-tac25-ok: #1fa56b;
  --color-tac25-ok: oklch(0.64 0.14 158);
  --color-tac25-ok-soft: #dcf5e8;
  --color-tac25-ok-soft: oklch(0.95 0.04 158);
  --color-tac25-ok-ink: #11633f;
  --color-tac25-ok-ink: oklch(0.44 0.1 158);
  --color-tac25-idle: #a2a9b8;
  --color-tac25-idle: oklch(0.73 0.02 265);
  --shadow-tac25-soft: 0 1px 2px oklch(0.2 0.03 265 / 0.05);
  --shadow-tac25-lift: 0 1px 2px oklch(0.2 0.03 265 / 0.05), 0 12px 32px -8px oklch(0.35 0.1 268 / 0.22);
  --font-tac25-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tac25-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-25 {
  width: 100%;
  min-height: 100svh;
}
```
