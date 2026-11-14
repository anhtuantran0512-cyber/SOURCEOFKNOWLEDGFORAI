---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-center-div/tailwind-mx-auto-center-a-div/"
title: "Tailwind mx-auto Center a Div with max-w Container"
section: "layouts"
category: "tailwind-css-center-div"
category_name: "Tailwind CSS Ways to Center Div"
description: "Horizontal centering, told honestly."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind mx-auto Center a Div with max-w Container
Source: https://codefronts.com/layouts/tailwind-css-center-div/tailwind-mx-auto-center-a-div/

Horizontal centering, told honestly. mx-auto w-fit centers on the inline axis only; flip the stage to RTL and watch mx-auto hold, logical ms-auto follow the direction and physical ml-auto stay stuck. Then m-auto inside a flex parent for both axes, and the page-level max-w-* mx-auto content column with a live width picker. Zero JS.
## HTML
```html
<section class="tcd-04 w-full min-h-svh grid place-items-center bg-tcd04-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tcd04-glow),transparent_70%)] px-5 py-14 font-tcd04-sans text-tcd04-ink selection:bg-tcd04-acc selection:text-tcd04-bg" aria-label="Tailwind mx-auto center a div demo">
  <div class="w-full max-w-4xl">
    <header class="mb-10 text-center">
      <p class="inline-flex items-center gap-2 rounded-full border border-tcd04-acc/30 bg-tcd04-acc/10 px-3 py-1 font-tcd04-mono text-[11px] uppercase tracking-[0.14em] text-tcd04-acc2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd04-acc"></span>Pure Tailwind</p>
      <h1 class="mt-5 text-[clamp(30px,5.4vw,52px)] font-semibold leading-[1.02] tracking-[-0.03em] text-balance">Center a div with <em class="font-tcd04-serif font-normal italic text-tcd04-acc2">mx-auto</em></h1>
      <p class="mx-auto mt-3 max-w-lg text-[15px] leading-relaxed text-tcd04-mut text-pretty">Auto margins split free space on the inline axis. Flip the direction, change the width, see what holds.</p>
    </header>

    <div class="grid gap-5 md:grid-cols-[1.35fr_1fr]">
      <article class="group/s1 overflow-hidden rounded-2xl border border-tcd04-acc/15 bg-tcd04-card transition duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-tcd04-acc/12 px-5 py-3">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd04-mut">Inline axis only</h2>
          <div class="flex gap-1 rounded-xl bg-white/5 p-1 ring-1 ring-white/8" role="radiogroup" aria-label="Writing direction">
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-dir" id="tcd04-ltr" checked>LTR</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-dir" id="tcd04-rtl">RTL</label>
          </div>
        </div>
        <div class="relative flex min-h-72 flex-col gap-3 p-5 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:border-l before:border-dashed before:border-tcd04-acc/35 group-has-[#tcd04-rtl:checked]/s1:[direction:rtl]">
          <div class="relative mx-auto flex w-fit items-center gap-3 rounded-xl border border-tcd04-acc/40 bg-tcd04-acc/15 px-4 py-3 transition-all duration-500 motion-reduce:transition-none">
            <code class="font-tcd04-mono text-xs font-semibold text-tcd04-acc2">mx-auto</code><span class="text-[13px] text-tcd04-mut">always centered</span>
          </div>
          <div class="relative ms-auto flex w-fit items-center gap-3 rounded-xl border border-tcd04-acc2/30 bg-white/4 px-4 py-3">
            <code class="font-tcd04-mono text-xs font-semibold text-tcd04-acc2">ms-auto</code><span class="text-[13px] text-tcd04-mut">follows direction</span>
          </div>
          <div class="relative ml-auto flex w-fit items-center gap-3 rounded-xl border border-tcd04-warn/40 bg-tcd04-warn/8 px-4 py-3">
            <code class="font-tcd04-mono text-xs font-semibold text-tcd04-warn">ml-auto</code><span class="text-[13px] text-tcd04-mut">stuck right</span>
          </div>
          <p class="relative mt-auto text-center text-xs text-tcd04-mut">Note the cards sit at the top — <code class="font-tcd04-mono text-tcd04-acc2">my-auto</code> is 0 in normal flow.</p>
        </div>
      </article>

      <article class="overflow-hidden rounded-2xl border border-tcd04-acc/15 bg-tcd04-card transition delay-100 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="flex min-h-[4.25rem] flex-wrap items-center justify-between gap-2 border-b border-tcd04-acc/12 px-5 py-3">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd04-mut">Both axes</h2>
          <code class="rounded-md bg-tcd04-acc/15 px-2.5 py-1 font-tcd04-mono text-xs text-tcd04-acc2">flex → m-auto</code>
        </div>
        <div class="relative flex min-h-72 p-5 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd04-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd04-acc/20">
          <div class="relative z-10 m-auto rounded-2xl border border-tcd04-acc/40 bg-linear-to-br from-tcd04-acc/25 to-tcd04-acc2/5 px-8 py-6 text-center shadow-[0_14px_40px_-16px_var(--color-tcd04-acc)]">
            <h3 class="font-tcd04-serif text-2xl italic">m-auto</h3>
            <p class="mt-1 text-[13px] text-tcd04-mut">Flex parent, every side</p>
          </div>
        </div>
      </article>

      <article class="group/s3 overflow-hidden rounded-2xl border border-tcd04-acc/15 bg-tcd04-card transition delay-200 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:col-span-2">
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-tcd04-acc/12 px-5 py-3">
          <div class="flex flex-wrap items-center gap-3">
            <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd04-mut">Content column</h2>
            <code class="rounded-md bg-tcd04-acc/15 px-2.5 py-1 font-tcd04-mono text-xs text-tcd04-acc2">w-full mx-auto max-w-<span class="hidden group-has-[#tcd04-w-sm:checked]/s3:inline">sm</span><span class="group-has-[#tcd04-w-sm:checked]/s3:hidden group-has-[#tcd04-w-xl:checked]/s3:hidden group-has-[#tcd04-w-full:checked]/s3:hidden">md</span><span class="hidden group-has-[#tcd04-w-xl:checked]/s3:inline">xl</span><span class="hidden group-has-[#tcd04-w-full:checked]/s3:inline">full</span></code>
          </div>
          <div class="flex gap-1 rounded-xl bg-white/5 p-1 ring-1 ring-white/8" role="radiogroup" aria-label="Column max width">
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-w" id="tcd04-w-sm">sm</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-w" id="tcd04-w-md" checked>md</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-w" id="tcd04-w-xl">xl</label>
            <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3 font-tcd04-mono text-xs font-medium text-tcd04-mut transition hover:text-tcd04-ink has-checked:bg-tcd04-acc has-checked:text-tcd04-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd04-acc2"><input class="sr-only" type="radio" name="tcd04-w" id="tcd04-w-full">full</label>
          </div>
        </div>
        <div class="bg-[repeating-linear-gradient(135deg,transparent_0_10px,var(--color-tcd04-hatch)_10px_11px)] py-8">
          <div class="mx-auto w-full border-x border-dashed border-tcd04-acc/50 bg-tcd04-card px-6 py-7 transition-[max-width] duration-500 ease-out motion-reduce:transition-none group-has-[#tcd04-w-sm:checked]/s3:max-w-sm group-has-[#tcd04-w-md:checked]/s3:max-w-md group-has-[#tcd04-w-xl:checked]/s3:max-w-xl group-has-[#tcd04-w-full:checked]/s3:max-w-full">
            <p class="font-tcd04-mono text-[11px] uppercase tracking-[0.14em] text-tcd04-acc2">Article</p>
            <h3 class="mt-2 font-tcd04-serif text-[28px] leading-[1.1] text-balance">Constrain the width, let the margins do the rest</h3>
            <p class="mt-3 text-[14px] leading-relaxed text-tcd04-mut text-pretty">On wide screens the column caps at its max-width and sits in the middle; on phones it fills the screen edge to edge. The dashed edges are the column itself, so the guide always tells the truth.</p>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd04-bg: #04130d;
  --color-tcd04-bg: oklch(0.16 0.025 165);
  --color-tcd04-glow: #0d3d2b66;
  --color-tcd04-glow: oklch(0.33 0.06 165 / 0.4);
  --color-tcd04-card: #0b1f17;
  --color-tcd04-card: oklch(0.21 0.03 165);
  --color-tcd04-ink: #ecfdf5;
  --color-tcd04-ink: oklch(0.98 0.02 165);
  --color-tcd04-mut: #a9cbbb;
  --color-tcd04-mut: oklch(0.82 0.04 165);
  --color-tcd04-acc: #10b981;
  --color-tcd04-acc: oklch(0.7 0.15 163);
  --color-tcd04-acc2: #6ee7b7;
  --color-tcd04-acc2: oklch(0.85 0.13 163);
  --color-tcd04-warn: #fbbf24;
  --color-tcd04-warn: oklch(0.84 0.16 84);
  --color-tcd04-hatch: #10b9811f;
  --color-tcd04-hatch: oklch(0.7 0.15 163 / 0.12);
  --font-tcd04-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tcd04-serif: 'Instrument Serif', Georgia, serif;
  --font-tcd04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tcd-04 {
  width: 100%;
  min-height: 100svh;
}
```
