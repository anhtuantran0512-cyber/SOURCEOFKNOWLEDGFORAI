---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-center-div/tailwind-css-grid-center-a-div/"
title: "Tailwind CSS Grid Center a Div with place-items-center"
section: "layouts"
category: "tailwind-css-center-div"
category_name: "Tailwind CSS Ways to Center Div"
description: "The shortest centering in Tailwind is two classes: grid place-items-center."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Grid Center a Div with place-items-center
Source: https://codefronts.com/layouts/tailwind-css-center-div/tailwind-css-grid-center-a-div/

The shortest centering in Tailwind is two classes: grid place-items-center. This demo pairs it with grid + m-auto on the child, then turns the classic 3×3 template (grid-cols-[1fr_auto_1fr]) into a clickable board: every cell is a radio, and the card jumps to whichever you pick via group-has-[.tcd02-col3:checked]:col-start-3. Zero JS.
## HTML
```html
<section class="tcd-02 group/t w-full min-h-svh grid place-items-center bg-tcd02-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tcd02-glow),transparent_70%)] px-5 py-14 font-tcd02-sans text-tcd02-ink selection:bg-tcd02-acc selection:text-tcd02-bg" aria-label="Tailwind CSS grid center a div demo">
  <div class="w-full max-w-4xl">
    <header class="mb-10 text-center">
      <p class="inline-flex items-center gap-2 rounded-full border border-tcd02-acc/30 bg-tcd02-acc/10 px-3 py-1 font-tcd02-mono text-[11px] uppercase tracking-[0.14em] text-tcd02-acc2"><span aria-hidden="true" class="size-1.5 rotate-45 bg-tcd02-acc"></span>Pure Tailwind</p>
      <h1 class="mt-5 text-[clamp(28px,5vw,46px)] font-bold leading-[1.05] tracking-[-0.035em] text-balance">Center a div with <span class="text-tcd02-acc">grid place-items-center</span></h1>
      <p class="mx-auto mt-3 max-w-lg text-[15px] leading-relaxed text-tcd02-mut text-pretty">Two classes on the parent, or one on the child. Then click any cell of the 3×3 board to move the card.</p>
    </header>

    <div class="grid gap-5 md:grid-cols-2">
      <article class="overflow-hidden rounded-2xl border border-tcd02-acc/15 bg-tcd02-card transition duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-tcd02-acc/12 px-5 py-3.5">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd02-mut">Parent only</h2>
          <code class="rounded-md bg-tcd02-acc/15 px-2.5 py-1 font-tcd02-mono text-xs text-tcd02-acc2">grid place-items-center</code>
        </div>
        <div class="relative grid h-64 place-items-center bg-[radial-gradient(var(--color-tcd02-dot)_1px,transparent_1px)] bg-[length:24px_24px] bg-center before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd02-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd02-acc/20">
          <div class="relative z-10 rounded-2xl border border-tcd02-acc/35 bg-tcd02-card/80 px-8 py-6 text-center shadow-[0_14px_40px_-16px_var(--color-tcd02-acc)] backdrop-blur-sm">
            <h3 class="text-lg font-bold tracking-[-0.01em]">Grid centered</h3>
            <p class="mt-1 text-[13px] text-tcd02-mut">Two classes, both axes</p>
          </div>
        </div>
      </article>
      <article class="overflow-hidden rounded-2xl border border-tcd02-acc/15 bg-tcd02-card transition delay-100 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-tcd02-acc/12 px-5 py-3.5">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd02-mut">Child only</h2>
          <code class="rounded-md bg-tcd02-acc/15 px-2.5 py-1 font-tcd02-mono text-xs text-tcd02-acc2">grid → m-auto</code>
        </div>
        <div class="relative grid h-64 bg-[radial-gradient(var(--color-tcd02-dot)_1px,transparent_1px)] bg-[length:24px_24px] bg-center before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd02-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd02-acc/20">
          <div class="relative z-10 m-auto rounded-2xl border border-tcd02-acc/35 bg-tcd02-card/80 px-8 py-6 text-center shadow-[0_14px_40px_-16px_var(--color-tcd02-acc)] backdrop-blur-sm">
            <h3 class="text-lg font-bold tracking-[-0.01em]">Margin auto</h3>
            <p class="mt-1 text-[13px] text-tcd02-mut">Grid absorbs free space</p>
          </div>
        </div>
      </article>

      <article class="overflow-hidden rounded-2xl border border-tcd02-acc/15 bg-tcd02-card transition delay-200 duration-700 starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:col-span-2">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-tcd02-acc/12 px-5 py-3.5">
          <h2 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-tcd02-mut">3×3 template · click a cell</h2>
          <code class="rounded-md bg-tcd02-acc/15 px-2.5 py-1 font-tcd02-mono text-xs text-tcd02-acc2">col-start-<span class="group-has-[.tcd02-col1:checked]/t:hidden group-has-[.tcd02-col3:checked]/t:hidden">2</span><span class="hidden group-has-[.tcd02-col1:checked]/t:inline">1</span><span class="hidden group-has-[.tcd02-col3:checked]/t:inline">3</span> row-start-<span class="group-has-[.tcd02-row1:checked]/t:hidden group-has-[.tcd02-row3:checked]/t:hidden">2</span><span class="hidden group-has-[.tcd02-row1:checked]/t:inline">1</span><span class="hidden group-has-[.tcd02-row3:checked]/t:inline">3</span></code>
        </div>
        <div class="grid h-80 grid-cols-[1fr_minmax(13rem,auto)_1fr] grid-rows-[1fr_minmax(6.5rem,auto)_1fr] bg-[radial-gradient(var(--color-tcd02-dot)_1px,transparent_1px)] bg-[length:24px_24px] bg-center" role="radiogroup" aria-label="Grid cell for the card">
          <label class="col-start-1 row-start-1 grid cursor-pointer place-items-center border-r border-b border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col1 tcd02-row1" type="radio" name="tcd02-cell" data-col="1" data-row="1" aria-label="Column 1, row 1">1 / 1</label>
          <label class="col-start-2 row-start-1 grid cursor-pointer place-items-center border-r border-b border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col2 tcd02-row1" type="radio" name="tcd02-cell" data-col="2" data-row="1" aria-label="Column 2, row 1">2 / 1</label>
          <label class="col-start-3 row-start-1 grid cursor-pointer place-items-center border-b border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col3 tcd02-row1" type="radio" name="tcd02-cell" data-col="3" data-row="1" aria-label="Column 3, row 1">3 / 1</label>
          <label class="col-start-1 row-start-2 grid cursor-pointer place-items-center border-r border-b border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col1 tcd02-row2" type="radio" name="tcd02-cell" data-col="1" data-row="2" aria-label="Column 1, row 2">1 / 2</label>
          <label class="col-start-2 row-start-2 grid cursor-pointer place-items-center border-r border-b border-dashed border-tcd02-acc/20 bg-tcd02-acc/5 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/10 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col2 tcd02-row2" type="radio" name="tcd02-cell" data-col="2" data-row="2" aria-label="Column 2, row 2 (centre)" checked>2 / 2</label>
          <label class="col-start-3 row-start-2 grid cursor-pointer place-items-center border-b border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col3 tcd02-row2" type="radio" name="tcd02-cell" data-col="3" data-row="2" aria-label="Column 3, row 2">3 / 2</label>
          <label class="col-start-1 row-start-3 grid cursor-pointer place-items-center border-r border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col1 tcd02-row3" type="radio" name="tcd02-cell" data-col="1" data-row="3" aria-label="Column 1, row 3">1 / 3</label>
          <label class="col-start-2 row-start-3 grid cursor-pointer place-items-center border-r border-dashed border-tcd02-acc/20 font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col2 tcd02-row3" type="radio" name="tcd02-cell" data-col="2" data-row="3" aria-label="Column 2, row 3">2 / 3</label>
          <label class="col-start-3 row-start-3 grid cursor-pointer place-items-center font-tcd02-mono text-[11px] text-transparent transition hover:bg-tcd02-acc/8 hover:text-tcd02-mut has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tcd02-acc"><input class="sr-only tcd02-col3 tcd02-row3" type="radio" name="tcd02-cell" data-col="3" data-row="3" aria-label="Column 3, row 3">3 / 3</label>
          <div aria-hidden="true" class="pointer-events-none z-10 col-start-2 row-start-2 m-3 place-self-center rounded-2xl bg-tcd02-acc px-6 py-4 text-center text-tcd02-bg shadow-[0_16px_40px_-14px_var(--color-tcd02-acc)] group-has-[.tcd02-col1:checked]/t:col-start-1 group-has-[.tcd02-col3:checked]/t:col-start-3 group-has-[.tcd02-row1:checked]/t:row-start-1 group-has-[.tcd02-row3:checked]/t:row-start-3">
            <p class="text-base font-bold tracking-[-0.01em]">Exact placement</p>
            <p class="mt-0.5 font-tcd02-mono text-[11px] font-medium opacity-80">col-start · row-start</p>
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
  --color-tcd02-bg: #110e06;
  --color-tcd02-bg: oklch(0.15 0.02 80);
  --color-tcd02-glow: #4a330b66;
  --color-tcd02-glow: oklch(0.33 0.07 70 / 0.4);
  --color-tcd02-card: #1b1710;
  --color-tcd02-card: oklch(0.2 0.02 80);
  --color-tcd02-ink: #fdf9e9;
  --color-tcd02-ink: oklch(0.98 0.02 95);
  --color-tcd02-mut: #c9bc98;
  --color-tcd02-mut: oklch(0.8 0.045 88);
  --color-tcd02-acc: #f59e0b;
  --color-tcd02-acc: oklch(0.77 0.16 70);
  --color-tcd02-acc2: #fcd34d;
  --color-tcd02-acc2: oklch(0.87 0.15 92);
  --color-tcd02-dot: #f59e0b33;
  --color-tcd02-dot: oklch(0.77 0.16 70 / 0.2);
  --font-tcd02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcd02-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tcd-02 {
  width: 100%;
  min-height: 100svh;
}
```
