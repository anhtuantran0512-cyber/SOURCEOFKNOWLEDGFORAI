---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-center-div/tailwind-flexbox-center-a-div/"
title: "Tailwind Flexbox Center a Div Horizontally and Vertically"
section: "layouts"
category: "tailwind-css-center-div"
category_name: "Tailwind CSS Ways to Center Div"
description: "The #1 Tailwind centering search, answered three ways and then made playable: flex items-center justify-center on both axes, a centered row of cards with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Flexbox Center a Div Horizontally and Vertically
Source: https://codefronts.com/layouts/tailwind-css-center-div/tailwind-flexbox-center-a-div/

The #1 Tailwind centering search, answered three ways and then made playable: flex items-center justify-center on both axes, a centered row of cards with gap-4, and a flex-col stack. The first stage is a live justify/align picker built from real radio inputs and group-has-[#id:checked]: — the class readout rewrites itself as you click.
## HTML
```html
<section class="tcd-01 group/pg w-full min-h-svh grid place-items-center bg-tcd01-bg bg-[radial-gradient(80%_55%_at_50%_-10%,var(--color-tcd01-glow),transparent_70%)] px-5 py-14 font-tcd01-sans text-tcd01-ink selection:bg-tcd01-acc selection:text-white" aria-label="Tailwind flexbox center a div demo">
  <div class="w-full max-w-4xl">
    <header class="mb-10 text-center">
      <p class="inline-flex items-center gap-2 rounded-full border border-tcd01-acc2/30 bg-tcd01-acc/10 px-3 py-1 font-tcd01-mono text-[11px] uppercase tracking-[0.14em] text-tcd01-acc2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd01-acc2"></span>Pure Tailwind</p>
      <h1 class="mt-5 text-[clamp(28px,5vw,46px)] font-semibold leading-[1.06] tracking-[-0.035em] text-balance">Center a div with <span class="bg-linear-to-r from-tcd01-acc2 to-tcd01-acc3 bg-clip-text text-transparent">Tailwind Flexbox</span></h1>
      <p class="mx-auto mt-3 max-w-lg text-[15px] leading-relaxed text-tcd01-mut text-pretty">Three classes, both axes. Pick an alignment below and watch the classes rewrite themselves.</p>
    </header>

    <div class="grid gap-5">
      <article class="overflow-hidden rounded-2xl border border-white/8 bg-tcd01-card shadow-[0_30px_80px_-40px_oklch(0_0_0/0.9)] transition duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-white/8 px-5 py-3.5">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd01-mut">Center both axes · live</h2>
          <code class="rounded-md bg-tcd01-acc/15 px-2.5 py-1 font-tcd01-mono text-xs text-tcd01-acc2">flex justify-<span class="group-has-[#tcd01-js:checked]/pg:hidden group-has-[#tcd01-je:checked]/pg:hidden">center</span><span class="hidden group-has-[#tcd01-js:checked]/pg:inline">start</span><span class="hidden group-has-[#tcd01-je:checked]/pg:inline">end</span> items-<span class="group-has-[#tcd01-is:checked]/pg:hidden group-has-[#tcd01-ie:checked]/pg:hidden">center</span><span class="hidden group-has-[#tcd01-is:checked]/pg:inline">start</span><span class="hidden group-has-[#tcd01-ie:checked]/pg:inline">end</span></code>
        </div>
        <div class="flex flex-wrap items-center gap-x-7 gap-y-3 border-b border-white/8 px-5 py-3">
          <div class="flex items-center gap-3" role="radiogroup" aria-label="justify-content">
            <span aria-hidden="true" class="w-14 font-tcd01-mono text-xs text-tcd01-mut">justify</span>
            <div class="flex gap-1 rounded-xl bg-white/5 p-1 ring-1 ring-white/8">
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-j" id="tcd01-js">start</label>
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-j" id="tcd01-jc" checked>center</label>
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-j" id="tcd01-je">end</label>
            </div>
          </div>
          <div class="flex items-center gap-3" role="radiogroup" aria-label="align-items">
            <span aria-hidden="true" class="w-14 font-tcd01-mono text-xs text-tcd01-mut">items</span>
            <div class="flex gap-1 rounded-xl bg-white/5 p-1 ring-1 ring-white/8">
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-i" id="tcd01-is">start</label>
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-i" id="tcd01-ic" checked>center</label>
              <label class="grid min-h-11 cursor-pointer place-items-center rounded-lg px-3.5 text-[13px] font-medium text-tcd01-mut transition hover:text-tcd01-ink has-checked:bg-tcd01-acc has-checked:text-white has-checked:shadow-[0_6px_20px_-6px_var(--color-tcd01-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd01-acc2"><input class="sr-only" type="radio" name="tcd01-i" id="tcd01-ie">end</label>
            </div>
          </div>
        </div>
        <div class="relative flex h-80 items-center justify-center bg-[linear-gradient(var(--color-tcd01-line)_1px,transparent_1px),linear-gradient(90deg,var(--color-tcd01-line)_1px,transparent_1px)] bg-[length:40px_40px] bg-center p-6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd01-acc2/25 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd01-acc2/25 group-has-[#tcd01-js:checked]/pg:justify-start group-has-[#tcd01-je:checked]/pg:justify-end group-has-[#tcd01-is:checked]/pg:items-start group-has-[#tcd01-ie:checked]/pg:items-end">
          <div class="relative z-10 rounded-2xl border border-tcd01-acc2/35 bg-linear-to-br from-tcd01-acc/30 to-tcd01-acc3/10 px-9 py-7 text-center shadow-[0_14px_44px_-14px_var(--color-tcd01-acc)] backdrop-blur-md">
            <h3 class="text-lg font-semibold tracking-[-0.01em]">Perfectly centered</h3>
            <p class="mt-1 text-[13px] text-tcd01-mut">Any size, both axes</p>
          </div>
        </div>
      </article>

      <div class="grid gap-5 md:grid-cols-2">
        <article class="overflow-hidden rounded-2xl border border-white/8 bg-tcd01-card transition delay-100 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/8 px-5 py-3.5">
            <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd01-mut">Row of items</h2>
            <code class="rounded-md bg-tcd01-acc/15 px-2.5 py-1 font-tcd01-mono text-xs text-tcd01-acc2">flex justify-center gap-3</code>
          </div>
          <div class="relative flex min-h-64 flex-wrap items-center justify-center gap-3 p-6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd01-acc2/20">
            <div class="relative rounded-xl border border-tcd01-acc2/30 bg-tcd01-acc/15 px-5 py-4 text-center transition hover:-translate-y-1 hover:border-tcd01-acc2/60 motion-reduce:transition-none"><h3 class="text-sm font-semibold">One</h3><p class="mt-0.5 text-xs text-tcd01-mut">auto width</p></div>
            <div class="relative rounded-xl border border-tcd01-acc2/30 bg-tcd01-acc/15 px-5 py-4 text-center transition hover:-translate-y-1 hover:border-tcd01-acc2/60 motion-reduce:transition-none"><h3 class="text-sm font-semibold">Two</h3><p class="mt-0.5 text-xs text-tcd01-mut">gap-3</p></div>
            <div class="relative rounded-xl border border-tcd01-acc2/30 bg-tcd01-acc/15 px-5 py-4 text-center transition hover:-translate-y-1 hover:border-tcd01-acc2/60 motion-reduce:transition-none"><h3 class="text-sm font-semibold">Three</h3><p class="mt-0.5 text-xs text-tcd01-mut">wraps</p></div>
          </div>
        </article>
        <article class="overflow-hidden rounded-2xl border border-white/8 bg-tcd01-card transition delay-200 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/8 px-5 py-3.5">
            <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd01-mut">Column stack</h2>
            <code class="rounded-md bg-tcd01-acc/15 px-2.5 py-1 font-tcd01-mono text-xs text-tcd01-acc2">flex-col items-center</code>
          </div>
          <div class="relative flex min-h-64 flex-col items-center justify-center gap-4 p-6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd01-acc2/20">
            <div class="relative rounded-xl border border-tcd01-acc2/30 bg-tcd01-acc/15 px-6 py-4 text-center"><h3 class="text-sm font-semibold">Stacked &amp; centered</h3><p class="mt-0.5 text-xs text-tcd01-mut">items-center is now horizontal</p></div>
            <button type="button" class="relative min-h-11 rounded-full bg-linear-to-r from-tcd01-acc to-tcd01-acc3 px-6 text-sm font-semibold text-white shadow-[0_8px_24px_-8px_var(--color-tcd01-acc)] transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd01-acc2 motion-reduce:transition-none">Call to action</button>
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
  --color-tcd01-bg: #0a0a12;
  --color-tcd01-bg: oklch(0.13 0.015 280);
  --color-tcd01-glow: #2d2b6e73;
  --color-tcd01-glow: oklch(0.32 0.12 278 / 0.45);
  --color-tcd01-card: #12121d;
  --color-tcd01-card: oklch(0.18 0.02 280);
  --color-tcd01-ink: #f2f1ff;
  --color-tcd01-ink: oklch(0.96 0.015 290);
  --color-tcd01-mut: #aeadc8;
  --color-tcd01-mut: oklch(0.76 0.03 285);
  --color-tcd01-acc: #5457e6;
  --color-tcd01-acc: oklch(0.55 0.21 277);
  --color-tcd01-acc2: #a5b4fc;
  --color-tcd01-acc2: oklch(0.79 0.1 281);
  --color-tcd01-acc3: #8b5cf6;
  --color-tcd01-acc3: oklch(0.61 0.22 293);
  --color-tcd01-line: #6366f114;
  --color-tcd01-line: oklch(0.59 0.2 277 / 0.08);
  --font-tcd01-sans: 'Geist', system-ui, sans-serif;
  --font-tcd01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities. */

.tcd-01 {
  width: 100%;
  min-height: 100svh;
}
```
