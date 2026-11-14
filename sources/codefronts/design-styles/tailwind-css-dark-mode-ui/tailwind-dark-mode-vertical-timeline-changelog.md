---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-vertical-timeline-changelog/"
title: "Tailwind Dark Mode Vertical Timeline Changelog"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A changelog you would actually read: five releases alternating either side of a central rail, each in an elevated onyx card with a monospaced timestamp, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Vertical Timeline Changelog
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-vertical-timeline-changelog/

A changelog you would actually read: five releases alternating either side of a central rail, each in an elevated onyx card with a monospaced timestamp, a typed badge and a node that sits on the rail. The alternation is pure layout — md:odd: / md:even: — and collapses to a single left rail on phones. Cards rise in on load with starting:.
## HTML
```html
<div class="tdm-19 scheme-dark w-full min-h-svh bg-tdm19-bg bg-[radial-gradient(100%_55%_at_50%_0%,#0e1117,transparent_62%)] font-tdm19-sans text-tdm19-ink antialiased">
  <div class="mx-auto grid max-w-5xl gap-12 px-5 py-14 sm:px-8">
    <header class="grid gap-2.5 md:text-center">
      <p class="font-tdm19-mono text-[11px] uppercase tracking-[0.18em] text-tdm19-acc">Changelog</p>
      <h1 class="text-[clamp(1.9rem,4vw,2.8rem)] font-semibold tracking-[-0.04em]">Shipped this week</h1>
      <p class="max-w-[52ch] text-[15px]/relaxed text-pretty text-tdm19-muted md:mx-auto">Five releases, one rail. Timestamps are tabular so the column reads as a single edge.</p>
    </header>
    <ol class="relative grid gap-6 before:absolute before:inset-y-2 before:left-4 before:w-px before:bg-linear-to-b before:from-transparent before:via-tdm19-rail before:to-transparent before:content-[''] md:gap-2 md:before:left-1/2">
      <li class="group/item relative grid grid-cols-[2rem_minmax(0,1fr)] gap-4 transition duration-700 ease-out delay-[0ms] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:grid-cols-[minmax(0,1fr)_3rem_minmax(0,1fr)] md:gap-0">
        <span aria-hidden="true" class="relative z-10 col-start-1 row-start-1 mt-6 ml-[9px] size-3.5 rounded-full border-2 border-tdm19-bg bg-tdm19-feature ring-4 ring-tdm19-feature/20 md:col-start-2 md:mx-auto"></span>
        <article class="col-start-2 row-start-1 grid gap-2.5 rounded-2xl border border-tdm19-line bg-tdm19-raised p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.04)] transition hover:border-tdm19-feature/40 md:col-start-1 md:mr-4 md:group-even/item:col-start-3 md:group-even/item:mr-0 md:group-even/item:ml-4">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="rounded-md bg-tdm19-feature/12 px-2 py-1 font-tdm19-mono text-[11px] font-medium text-tdm19-feature">Feature</span>
            <time datetime="2026-08-14T09:12" class="font-tdm19-mono text-xs text-tdm19-muted tabular-nums">14 Aug · 09:12</time>
          </div>
          <h2 class="text-[16px] font-semibold tracking-tight">Three-state theme switcher</h2>
          <p class="text-sm/relaxed text-pretty text-tdm19-muted">System / Light / Dark now persists per workspace, and the rendering path stays pure CSS.</p>
          <p class="flex items-center gap-2 pt-1 text-xs text-tdm19-muted"><span class="grid size-5 place-items-center rounded-full bg-tdm19-line text-[9px] font-semibold text-tdm19-ink" aria-hidden="true">AC</span>Alex Chen</p>
        </article>
      </li>
      <li class="group/item relative grid grid-cols-[2rem_minmax(0,1fr)] gap-4 transition duration-700 ease-out delay-[110ms] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:grid-cols-[minmax(0,1fr)_3rem_minmax(0,1fr)] md:gap-0">
        <span aria-hidden="true" class="relative z-10 col-start-1 row-start-1 mt-6 ml-[9px] size-3.5 rounded-full border-2 border-tdm19-bg bg-tdm19-fix ring-4 ring-tdm19-fix/20 md:col-start-2 md:mx-auto"></span>
        <article class="col-start-2 row-start-1 grid gap-2.5 rounded-2xl border border-tdm19-line bg-tdm19-raised p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.04)] transition hover:border-tdm19-fix/40 md:col-start-1 md:mr-4 md:group-even/item:col-start-3 md:group-even/item:mr-0 md:group-even/item:ml-4">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="rounded-md bg-tdm19-fix/12 px-2 py-1 font-tdm19-mono text-[11px] font-medium text-tdm19-fix">Fix</span>
            <time datetime="2026-08-13T17:48" class="font-tdm19-mono text-xs text-tdm19-muted tabular-nums">13 Aug · 17:48</time>
          </div>
          <h2 class="text-[16px] font-semibold tracking-tight">Toggle flipped one way only</h2>
          <p class="text-sm/relaxed text-pretty text-tdm19-muted">Added the flip-back utility so the switch works for visitors whose OS already matched the default.</p>
          <p class="flex items-center gap-2 pt-1 text-xs text-tdm19-muted"><span class="grid size-5 place-items-center rounded-full bg-tdm19-line text-[9px] font-semibold text-tdm19-ink" aria-hidden="true">PS</span>Priya Sharma</p>
        </article>
      </li>
      <li class="group/item relative grid grid-cols-[2rem_minmax(0,1fr)] gap-4 transition duration-700 ease-out delay-[220ms] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:grid-cols-[minmax(0,1fr)_3rem_minmax(0,1fr)] md:gap-0">
        <span aria-hidden="true" class="relative z-10 col-start-1 row-start-1 mt-6 ml-[9px] size-3.5 rounded-full border-2 border-tdm19-bg bg-tdm19-perf ring-4 ring-tdm19-perf/20 md:col-start-2 md:mx-auto"></span>
        <article class="col-start-2 row-start-1 grid gap-2.5 rounded-2xl border border-tdm19-line bg-tdm19-raised p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.04)] transition hover:border-tdm19-perf/40 md:col-start-1 md:mr-4 md:group-even/item:col-start-3 md:group-even/item:mr-0 md:group-even/item:ml-4">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="rounded-md bg-tdm19-perf/12 px-2 py-1 font-tdm19-mono text-[11px] font-medium text-tdm19-perf">Perf</span>
            <time datetime="2026-08-13T11:02" class="font-tdm19-mono text-xs text-tdm19-muted tabular-nums">13 Aug · 11:02</time>
          </div>
          <h2 class="text-[16px] font-semibold tracking-tight">Dropped 12 kB from the theme layer</h2>
          <p class="text-sm/relaxed text-pretty text-tdm19-muted">Semantic tokens now derive from four primitives, so the second theme costs one light-dark() pair per token.</p>
          <p class="flex items-center gap-2 pt-1 text-xs text-tdm19-muted"><span class="grid size-5 place-items-center rounded-full bg-tdm19-line text-[9px] font-semibold text-tdm19-ink" aria-hidden="true">JL</span>Jordan Lee</p>
        </article>
      </li>
      <li class="group/item relative grid grid-cols-[2rem_minmax(0,1fr)] gap-4 transition duration-700 ease-out delay-[330ms] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:grid-cols-[minmax(0,1fr)_3rem_minmax(0,1fr)] md:gap-0">
        <span aria-hidden="true" class="relative z-10 col-start-1 row-start-1 mt-6 ml-[9px] size-3.5 rounded-full border-2 border-tdm19-bg bg-tdm19-a11y ring-4 ring-tdm19-a11y/20 md:col-start-2 md:mx-auto"></span>
        <article class="col-start-2 row-start-1 grid gap-2.5 rounded-2xl border border-tdm19-line bg-tdm19-raised p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.04)] transition hover:border-tdm19-a11y/40 md:col-start-1 md:mr-4 md:group-even/item:col-start-3 md:group-even/item:mr-0 md:group-even/item:ml-4">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="rounded-md bg-tdm19-a11y/12 px-2 py-1 font-tdm19-mono text-[11px] font-medium text-tdm19-a11y">Access</span>
            <time datetime="2026-08-12T20:31" class="font-tdm19-mono text-xs text-tdm19-muted tabular-nums">12 Aug · 20:31</time>
          </div>
          <h2 class="text-[16px] font-semibold tracking-tight">Focus rings audited at 3:1</h2>
          <p class="text-sm/relaxed text-pretty text-tdm19-muted">Every interactive control has a per-theme ring token with a 2px outline and a 2px offset.</p>
          <p class="flex items-center gap-2 pt-1 text-xs text-tdm19-muted"><span class="grid size-5 place-items-center rounded-full bg-tdm19-line text-[9px] font-semibold text-tdm19-ink" aria-hidden="true">SR</span>Sam Rivera</p>
        </article>
      </li>
      <li class="group/item relative grid grid-cols-[2rem_minmax(0,1fr)] gap-4 transition duration-700 ease-out delay-[440ms] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none md:grid-cols-[minmax(0,1fr)_3rem_minmax(0,1fr)] md:gap-0">
        <span aria-hidden="true" class="relative z-10 col-start-1 row-start-1 mt-6 ml-[9px] size-3.5 rounded-full border-2 border-tdm19-bg bg-tdm19-feature ring-4 ring-tdm19-feature/20 md:col-start-2 md:mx-auto"></span>
        <article class="col-start-2 row-start-1 grid gap-2.5 rounded-2xl border border-tdm19-line bg-tdm19-raised p-5 shadow-[inset_0_1px_0_rgb(255_255_255/.04)] transition hover:border-tdm19-feature/40 md:col-start-1 md:mr-4 md:group-even/item:col-start-3 md:group-even/item:mr-0 md:group-even/item:ml-4">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="rounded-md bg-tdm19-feature/12 px-2 py-1 font-tdm19-mono text-[11px] font-medium text-tdm19-feature">Feature</span>
            <time datetime="2026-08-11T15:20" class="font-tdm19-mono text-xs text-tdm19-muted tabular-nums">11 Aug · 15:20</time>
          </div>
          <h2 class="text-[16px] font-semibold tracking-tight">theme-color syncs per scheme</h2>
          <p class="text-sm/relaxed text-pretty text-tdm19-muted">Mobile browser chrome now follows the active surface instead of the operating system.</p>
          <p class="flex items-center gap-2 pt-1 text-xs text-tdm19-muted"><span class="grid size-5 place-items-center rounded-full bg-tdm19-line text-[9px] font-semibold text-tdm19-ink" aria-hidden="true">AC</span>Alex Chen</p>
        </article>
      </li>
    </ol>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm19-bg: #07080a;
  --color-tdm19-raised: #12151a;
  --color-tdm19-ink: #eceef1;
  --color-tdm19-muted: #949ba7;
  --color-tdm19-line: #222631;
  --color-tdm19-rail: rgb(236 238 241 / .2);
  --color-tdm19-acc: #c4b5fd;
  --color-tdm19-feature: #a5b4fc;
  --color-tdm19-fix: #fcd34d;
  --color-tdm19-perf: #7ee0b0;
  --color-tdm19-a11y: #7dd3fc;
  --font-tdm19-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm19-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
