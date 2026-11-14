---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-center-div/how-to-center-a-div-in-tailwind-css/"
title: "How to Center a Div in Tailwind CSS — All 6 Methods Compared"
section: "layouts"
category: "tailwind-css-center-div"
category_name: "Tailwind CSS Ways to Center Div"
description: "Every Tailwind centering technique on one board: flex, grid place-items-center, absolute + translate, inset-0 m-auto, table-cell align-middle and a real…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: How to Center a Div in Tailwind CSS — All 6 Methods Compared
Source: https://codefronts.com/layouts/tailwind-css-center-div/how-to-center-a-div-in-tailwind-css/

Every Tailwind centering technique on one board: flex, grid place-items-center, absolute + translate, inset-0 m-auto, table-cell align-middle and a real writing-mode trick. A Grow content switch swells every box at once to prove each method survives unknown sizes, and each tile has a one-click Copy HTML button. Tiles reflow with grid-cols-[repeat(auto-fit,minmax(17rem,1fr))] — no breakpoints.
## HTML
```html
<section class="tcd-05 group/all w-full min-h-svh grid place-items-center bg-tcd05-bg bg-[radial-gradient(70%_45%_at_50%_0%,var(--color-tcd05-glow),transparent_70%)] px-5 py-14 font-tcd05-sans text-tcd05-ink selection:bg-tcd05-acc selection:text-white" aria-label="Tailwind center a div all methods comparison">
  <div class="w-full max-w-6xl">
    <header class="mb-8 flex flex-wrap items-end justify-between gap-6">
      <div>
        <p class="inline-flex items-center gap-2 rounded-full border border-tcd05-acc2/30 bg-tcd05-acc/10 px-3 py-1 font-tcd05-mono text-[11px] uppercase tracking-[0.14em] text-tcd05-acc2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd05-acc2"></span>Tailwind + JS</p>
        <h1 class="mt-4 text-[clamp(30px,5vw,52px)] font-extrabold leading-[1] tracking-[-0.04em] text-balance">Center a div: <span class="text-tcd05-acc2">all 6 methods</span></h1>
        <p class="mt-3 max-w-md text-[15px] leading-relaxed text-tcd05-mut text-pretty">Same stage, same box, six techniques. Grow the content to prove none of them care about size.</p>
      </div>
      <label class="group/sw flex min-h-11 cursor-pointer items-center gap-3 rounded-full border border-white/10 bg-white/5 py-1.5 pl-4 pr-1.5 text-sm font-semibold transition hover:bg-white/8 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcd05-acc2">
        <input class="peer sr-only" type="checkbox" id="tcd05-grow" role="switch">
        Grow content
        <span aria-hidden="true" class="relative h-8 w-14 rounded-full bg-white/12 transition peer-checked:bg-tcd05-acc after:absolute after:left-1 after:top-1 after:size-6 after:rounded-full after:bg-white after:shadow after:transition-transform peer-checked:after:translate-x-6 motion-reduce:after:transition-none"></span>
      </label>
    </header>

    <div class="grid grid-cols-[repeat(auto-fit,minmax(17rem,1fr))] gap-4">

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m1/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m1">01</span>Flexbox</h2>
          <button type="button" data-copy="flex" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">flex items-center justify-center</code>
        <div class="relative mt-4 flex h-48 items-center justify-center border-y border-white/6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="relative z-10 rounded-xl border border-tcd05-m1/45 bg-tcd05-m1/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m1)] transition-all duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Flexbox<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-ok/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-ok">Recommended</span><span class="rounded-full bg-tcd05-info/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-info">2-axis</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">Chrome 29+</span></div>
      </article>

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m2/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m2">02</span>CSS Grid</h2>
          <button type="button" data-copy="grid" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">grid place-items-center</code>
        <div class="relative mt-4 grid h-48 place-items-center border-y border-white/6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="relative z-10 rounded-xl border border-tcd05-m2/45 bg-tcd05-m2/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m2)] transition-all duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Grid<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-ok/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-ok">Shortest</span><span class="rounded-full bg-tcd05-info/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-info">2-axis</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">Chrome 59+</span></div>
      </article>

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m3/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m3">03</span>Absolute + translate</h2>
          <button type="button" data-copy="abs" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2</code>
        <div class="relative mt-4 h-48 border-y border-white/6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="absolute left-1/2 top-1/2 z-10 w-max -translate-x-1/2 -translate-y-1/2 rounded-xl border border-tcd05-m3/45 bg-tcd05-m3/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m3)] transition-[padding] duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Absolute<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-ok/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-ok">Overlays</span><span class="rounded-full bg-tcd05-warn/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-warn">Needs relative parent</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">IE9+</span></div>
      </article>

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m4/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m4">04</span>Inset + m-auto</h2>
          <button type="button" data-copy="inset" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">absolute inset-0 m-auto size-fit</code>
        <div class="relative mt-4 h-48 border-y border-white/6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="absolute inset-0 z-10 m-auto size-fit rounded-xl border border-tcd05-m4/45 bg-tcd05-m4/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m4)] transition-[padding] duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Inset<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-ok/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-ok">Modals</span><span class="rounded-full bg-tcd05-info/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-info">No transform</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">Chrome 87+</span></div>
      </article>

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m5/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m5">05</span>Table-cell</h2>
          <button type="button" data-copy="table" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">table → table-cell align-middle text-center</code>
        <div class="relative mt-4 table h-48 w-full border-y border-white/6 before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="table-cell text-center align-middle">
            <div class="relative z-10 inline-block rounded-xl border border-tcd05-m5/45 bg-tcd05-m5/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m5)] transition-all duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Table cell<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
          </div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-ok/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-ok">HTML email</span><span class="rounded-full bg-tcd05-warn/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-warn">Legacy</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">IE8+</span></div>
      </article>

      <article class="flex flex-col overflow-hidden rounded-2xl border border-white/8 bg-tcd05-card transition duration-300 hover:border-tcd05-m6/45 motion-reduce:transition-none">
        <div class="flex items-start justify-between gap-3 px-5 pb-3 pt-4">
          <h2 class="text-[17px] font-bold tracking-[-0.01em]"><span class="mr-2 font-tcd05-mono text-xs font-medium text-tcd05-m6">06</span>Writing-mode</h2>
          <button type="button" data-copy="writing" class="group/btn -mr-2 -mt-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-3 text-xs font-semibold text-tcd05-mut ring-1 ring-white/10 transition hover:bg-white/6 hover:text-tcd05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc2 data-copied:text-tcd05-ok data-copied:ring-tcd05-ok/45"><span class="group-data-copied/btn:hidden">Copy HTML</span><span class="hidden group-data-copied/btn:inline">Copied ✓</span></button>
        </div>
        <code class="mx-5 block rounded-lg bg-black/30 px-3 py-2 font-tcd05-mono text-[11.5px] leading-relaxed text-tcd05-acc2 ring-1 ring-white/6">[writing-mode:vertical-lr] text-center → reset child</code>
        <div class="relative mt-4 h-48 border-y border-white/6 text-center [writing-mode:vertical-lr] before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-tcd05-acc/20 after:pointer-events-none after:absolute after:inset-x-0 after:top-1/2 after:h-px after:bg-tcd05-acc/20">
          <div class="inline-block w-full text-center [writing-mode:horizontal-tb]">
            <div class="relative z-10 inline-block rounded-xl border border-tcd05-m6/45 bg-tcd05-m6/15 px-5 py-3.5 text-center text-sm font-semibold shadow-[0_0_28px_-6px_var(--color-tcd05-m6)] transition-all duration-300 group-has-[#tcd05-grow:checked]/all:px-9 group-has-[#tcd05-grow:checked]/all:py-6 motion-reduce:transition-none">Writing-mode<span class="mt-1 hidden text-xs font-normal text-tcd05-mut group-has-[#tcd05-grow:checked]/all:block">+ unknown content</span></div>
          </div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-5 py-3.5"><span class="rounded-full bg-tcd05-warn/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-warn">Obscure</span><span class="rounded-full bg-tcd05-info/12 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-info">Text-flow based</span><span class="rounded-full bg-white/6 px-2.5 py-0.5 text-[11px] font-semibold text-tcd05-mut">Chrome 48+</span></div>
      </article>

    </div>
    <p class="sr-only" role="status" aria-live="polite" data-tcd05-status></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd05-bg: #0a0714;
  --color-tcd05-bg: oklch(0.13 0.025 290);
  --color-tcd05-glow: #33206a66;
  --color-tcd05-glow: oklch(0.3 0.1 290 / 0.4);
  --color-tcd05-card: #130f22;
  --color-tcd05-card: oklch(0.18 0.03 290);
  --color-tcd05-ink: #f5f3ff;
  --color-tcd05-ink: oklch(0.97 0.015 295);
  --color-tcd05-mut: #bbb4d6;
  --color-tcd05-mut: oklch(0.79 0.045 290);
  --color-tcd05-acc: #8b5cf6;
  --color-tcd05-acc: oklch(0.61 0.22 293);
  --color-tcd05-acc2: #c4b5fd;
  --color-tcd05-acc2: oklch(0.81 0.1 294);
  --color-tcd05-ok: #6ee7b7;
  --color-tcd05-ok: oklch(0.85 0.13 163);
  --color-tcd05-info: #a5b4fc;
  --color-tcd05-info: oklch(0.79 0.1 281);
  --color-tcd05-warn: #fcd34d;
  --color-tcd05-warn: oklch(0.87 0.15 92);
  --color-tcd05-m1: #818cf8;
  --color-tcd05-m1: oklch(0.67 0.16 277);
  --color-tcd05-m2: #f59e0b;
  --color-tcd05-m2: oklch(0.77 0.16 70);
  --color-tcd05-m3: #ec4899;
  --color-tcd05-m3: oklch(0.66 0.22 354);
  --color-tcd05-m4: #2dd4bf;
  --color-tcd05-m4: oklch(0.78 0.13 182);
  --color-tcd05-m5: #10b981;
  --color-tcd05-m5: oklch(0.7 0.15 163);
  --color-tcd05-m6: #fb923c;
  --color-tcd05-m6: oklch(0.75 0.16 55);
  --font-tcd05-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcd05-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tcd-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const snippets = {
    flex: '<div class="flex h-48 items-center justify-center">\n  <div>Centered</div>\n</div>',
    grid: '<div class="grid h-48 place-items-center">\n  <div>Centered</div>\n</div>',
    abs: '<div class="relative h-48">\n  <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">Centered</div>\n</div>',
    inset: '<div class="relative h-48">\n  <div class="absolute inset-0 m-auto size-fit">Centered</div>\n</div>',
    table: '<div class="table h-48 w-full">\n  <div class="table-cell align-middle text-center">\n    <div class="inline-block">Centered</div>\n  </div>\n</div>',
    writing: '<div class="h-48 text-center [writing-mode:vertical-lr]">\n  <div class="inline-block w-full text-center [writing-mode:horizontal-tb]">\n    <div class="inline-block">Centered</div>\n  </div>\n</div>'
  };
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch (e) {
      const ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (err) {}
      ta.remove();
      return ok;
    }
  };
  document.querySelectorAll('.tcd-05').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const status = root.querySelector('[data-tcd05-status]');
    root.querySelectorAll('[data-copy]').forEach((btn) => {
      let t = 0;
      btn.addEventListener('click', async () => {
        const ok = await copyText(snippets[btn.dataset.copy] || '');
        clearTimeout(t);
        if (ok) { btn.setAttribute('data-copied', ''); status.textContent = 'HTML copied to clipboard'; }
        else status.textContent = 'Copy failed, select the code instead';
        t = setTimeout(() => { btn.removeAttribute('data-copied'); status.textContent = ''; }, 1600);
      });
    });
  });
})();
```
