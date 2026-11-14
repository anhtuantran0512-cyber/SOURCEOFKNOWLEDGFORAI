---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-elevation-layered-card/"
title: "Tailwind Dark Mode Elevation Layers — Layered Surface Card"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The elevation reference for a dark design system: four surface tokens, each a measured step lighter than the last, drawn as a visual ramp so the scale is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Elevation Layers — Layered Surface Card
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-elevation-layered-card/

The elevation reference for a dark design system: four surface tokens, each a measured step lighter than the last, drawn as a visual ramp so the scale is legible at a glance. A release card holds three nested sub-cards, every level labelled with its token, and hover lifts a row one step — the way dark UIs signal depth when shadows can't.
## HTML
```html
<div class="tdm-17 scheme-light-dark has-[#tdm-17-toggle:checked]:scheme-dark dark:has-[#tdm-17-toggle:checked]:scheme-light w-full min-h-svh bg-tdm17-base font-tdm17-sans text-tdm17-ink antialiased transition-colors duration-300">
  <div class="mx-auto grid min-h-svh max-w-5xl content-center gap-8 px-5 py-12 sm:px-8">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div class="grid gap-2"><p class="font-tdm17-mono text-[11px] uppercase tracking-[0.16em] text-tdm17-acc">Elevation reference</p><h1 class="text-[clamp(1.7rem,3.4vw,2.4rem)] font-semibold tracking-[-0.035em]">Four surfaces, no shadows</h1></div>
      <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm17-line bg-tdm17-surface transition duration-200 hover:-translate-y-px hover:border-tdm17-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm17-focus motion-reduce:transition-none ">
        <input id="tdm-17-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm17-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm17-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
    </header>
    <div class="grid items-center gap-8 lg:grid-cols-[17rem_minmax(0,1fr)]">
      <div class="relative h-56 lg:h-72" aria-hidden="true">
        <div class="absolute flex items-end justify-between rounded-2xl border border-tdm17-hair bg-tdm17-s0 px-4 pb-3 font-tdm17-mono text-[11px] text-tdm17-muted forced-colors:border-[CanvasText]" style="inset:0rem 2.7rem auto 0rem;height:7rem"><em class="not-italic text-tdm17-ink">--s0</em><b class="font-medium">base +4%</b></div>
        <div class="absolute flex items-end justify-between rounded-2xl border border-tdm17-hair bg-tdm17-s1 px-4 pb-3 font-tdm17-mono text-[11px] text-tdm17-muted forced-colors:border-[CanvasText]" style="inset:2.6rem 1.8rem auto 0.9rem;height:7rem"><em class="not-italic text-tdm17-ink">--s1</em><b class="font-medium">+8%</b></div>
        <div class="absolute flex items-end justify-between rounded-2xl border border-tdm17-hair bg-tdm17-s2 px-4 pb-3 font-tdm17-mono text-[11px] text-tdm17-muted forced-colors:border-[CanvasText]" style="inset:5.2rem 0.9rem auto 1.8rem;height:7rem"><em class="not-italic text-tdm17-ink">--s2</em><b class="font-medium">+13%</b></div>
        <div class="absolute flex items-end justify-between rounded-2xl border border-tdm17-hair bg-tdm17-s3 px-4 pb-3 font-tdm17-mono text-[11px] text-tdm17-muted forced-colors:border-[CanvasText]" style="inset:7.800000000000001rem 0rem auto 2.7rem;height:7rem"><em class="not-italic text-tdm17-ink">--s3</em><b class="font-medium">+19%</b></div>
      </div>
      <article class="grid gap-4 rounded-[26px] border border-tdm17-hair bg-tdm17-s1 p-5 sm:p-6 forced-colors:border-[CanvasText]">
        <div class="flex items-start justify-between gap-3">
          <div><h2 class="text-lg font-semibold tracking-tight">Release 4.2 checklist</h2><p class="mt-1 text-sm text-tdm17-muted">Nested panels climb the ramp instead of stacking shadows.</p></div>
          <span class="rounded-md bg-tdm17-s2 px-2 py-1 font-tdm17-mono text-[11px] text-tdm17-muted">s1</span>
        </div>
        <section class="grid gap-2.5 rounded-2xl bg-tdm17-s2 p-4 transition hover:bg-tdm17-s3 forced-colors:border forced-colors:border-[CanvasText]">
          <div class="flex items-center justify-between gap-3"><p class="text-sm font-medium">Contrast audit</p><span class="font-tdm17-mono text-[11px] text-tdm17-muted">s2 → s3</span></div>
          <p class="text-[13px] text-tdm17-muted">148 pairs · all pass</p>
          <div class="h-1.5 overflow-hidden rounded-full bg-tdm17-s0"><i class="block h-full w-full rounded-full bg-tdm17-acc"></i></div>
        </section>
        <section class="grid gap-2.5 rounded-2xl bg-tdm17-s2 p-4 transition hover:bg-tdm17-s3 forced-colors:border forced-colors:border-[CanvasText]">
          <div class="flex items-center justify-between gap-3"><p class="text-sm font-medium">Token coverage</p><span class="font-tdm17-mono text-[11px] text-tdm17-muted">s2 → s3</span></div>
          <p class="text-[13px] text-tdm17-muted">92% of components</p>
          <div class="h-1.5 overflow-hidden rounded-full bg-tdm17-s0"><i class="block h-full w-[92%] rounded-full bg-tdm17-acc"></i></div>
        </section>
        <section class="grid gap-2.5 rounded-2xl bg-tdm17-s2 p-4 transition hover:bg-tdm17-s3 forced-colors:border forced-colors:border-[CanvasText]">
          <div class="flex items-center justify-between gap-3"><p class="text-sm font-medium">Focus rings</p><span class="font-tdm17-mono text-[11px] text-tdm17-muted">s2 → s3</span></div>
          <p class="text-[13px] text-tdm17-muted">2px · offset 2 · 76%</p>
          <div class="h-1.5 overflow-hidden rounded-full bg-tdm17-s0"><i class="block h-full w-[76%] rounded-full bg-tdm17-acc"></i></div>
        </section>
        <footer class="flex items-center justify-between gap-3 pt-1">
          <span class="font-tdm17-mono text-[11px] text-tdm17-muted">hover a row → s3</span>
          <button type="button" class="min-h-11 rounded-xl bg-tdm17-acc px-4 text-sm font-semibold text-tdm17-acc-ink transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm17-focus">Open report</button>
        </footer>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm17-base: light-dark(#f1f3f6, #0a0c10);
  --color-tdm17-s0: light-dark(#ffffff, #0f1217);
  --color-tdm17-s1: light-dark(#f8f9fb, #161a21);
  --color-tdm17-s2: light-dark(#eef0f4, #1e232c);
  --color-tdm17-s3: light-dark(#e3e7ed, #282e3a);
  --color-tdm17-surface: light-dark(#ffffff, #161a21);
  --color-tdm17-ink: light-dark(#0b0d12, #edf0f5);
  --color-tdm17-muted: light-dark(#566070, #9aa4b4);
  --color-tdm17-hair: light-dark(rgb(11 13 18 / .1), rgb(237 240 245 / .08));
  --color-tdm17-line: light-dark(rgb(11 13 18 / .12), rgb(237 240 245 / .1));
  --color-tdm17-acc: light-dark(#2563eb, #7aa2ff);
  --color-tdm17-acc-ink: light-dark(#ffffff, #071027);
  --color-tdm17-focus: light-dark(#2563eb, #a9c2ff);
  --color-tdm17-sun: light-dark(#b45309, transparent);
  --color-tdm17-moon: light-dark(transparent, #a9c2ff);
  --font-tdm17-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm17-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
