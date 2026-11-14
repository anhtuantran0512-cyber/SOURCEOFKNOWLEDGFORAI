---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-dark-mode-vertical-tabs-with-theme-toggle/"
title: "Tailwind Dark Mode Vertical Tabs with Theme Toggle"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A design-tokens guide with a real light/dark theme toggle: a <button aria-pressed> writes data-theme on the demo root, and because every colour is an @theme…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Vertical Tabs with Theme Toggle
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-dark-mode-vertical-tabs-with-theme-toggle/

A design-tokens guide with a real light/dark theme toggle: a <button aria-pressed> writes data-theme on the demo root, and because every colour is an @theme token re-pointed under .tvt-16[data-theme="dark"], the whole UI flips without a single dark: class. It starts from prefers-color-scheme, offers &ldquo;Use system&rdquo; to drop the override, morphs a sun into a moon with an SVG mask, and reveals the new theme in a circle from the switch via the View Transitions API.
## HTML
```html
<section id="tvt-16-root" class="tvt-16 w-full min-h-svh grid place-items-center bg-tvt16-bg bg-[radial-gradient(60%_45%_at_50%_0%,var(--color-tvt16-glow),transparent_72%)] px-4 py-14 font-tvt16-sans text-tvt16-ink antialiased transition-[background-color,color] duration-500 sm:px-6" aria-label="Tailwind dark mode vertical tabs with theme toggle demo">
  <div class="grid w-full max-w-[58rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt16-surface px-3 py-1.5 font-tvt16-mono text-[11.5px] text-tvt16-acc-ink ring-1 ring-tvt16-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt16-acc shadow-[0_0_0_3px] shadow-tvt16-acc/25"></span>data-theme · aria-pressed</p>
      <h2 class="text-[clamp(30px,4.6vw,46px)] leading-[1.02] font-extrabold tracking-[-0.04em] text-balance">Light, dark, <span class="text-tvt16-acc-ink">and the switch</span></h2>
      <p class="max-w-[48ch] text-[15px] leading-relaxed text-tvt16-mut text-pretty">The toggle writes one attribute on the demo root; every utility reads re-pointed tokens. It starts from your system setting.</p>
    </header>

    <div class="@container w-full">
    <div class="w-full overflow-hidden rounded-[22px] bg-tvt16-surface shadow-tvt16-card ring-1 ring-tvt16-line transition-[background-color,box-shadow,opacity,translate] duration-500 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <div class="flex items-center gap-3 border-b border-tvt16-line px-4 py-3 sm:px-5">
        <p class="flex items-center gap-2.5 text-[15px] font-bold tracking-[-0.02em]"><span aria-hidden="true" class="size-6 rounded-[7px] bg-[linear-gradient(135deg,var(--color-tvt16-acc)_0_50%,var(--color-tvt16-ink)_50%_100%)] shadow-sm"></span>Tokens</p>
        <span class="ms-2 hidden items-center gap-2 rounded-lg bg-tvt16-raised px-3 py-1.5 text-[13px] text-tvt16-mut ring-1 ring-tvt16-line sm:inline-flex"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>Search tokens<kbd class="ms-6 rounded bg-tvt16-surface px-1.5 font-tvt16-mono text-[10.5px] ring-1 ring-tvt16-line">⌘K</kbd></span>
        <button type="button" data-system disabled class="ms-auto min-h-11 cursor-pointer rounded-lg px-2.5 text-[12.5px] font-medium text-tvt16-mut transition-colors hover:text-tvt16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring disabled:invisible">Use system</button>
        <button type="button" data-toggle aria-pressed="false" aria-label="Dark mode" class="group/t relative min-h-11 shrink-0 cursor-pointer rounded-full focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring">
          <span aria-hidden="true" class="relative flex h-9 w-[4.25rem] items-center rounded-full bg-tvt16-raised p-1 ring-1 ring-tvt16-line transition-colors duration-500 ring-inset group-aria-pressed/t:bg-tvt16-night">
            <svg viewBox="0 0 68 36" class="pointer-events-none absolute inset-0 size-full text-white opacity-0 transition-opacity duration-500 group-aria-pressed/t:opacity-100" focusable="false"><circle cx="14" cy="11" r="1.2" fill="currentColor"/><circle cx="22" cy="23" r="0.9" fill="currentColor"/><circle cx="10" cy="22" r="0.7" fill="currentColor"/><circle cx="26" cy="13" r="0.6" fill="currentColor"/></svg>
            <span class="relative grid size-7 place-items-center rounded-full bg-tvt16-surface text-tvt16-sun shadow-tvt16-knob transition-[translate,color,background-color] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] group-aria-pressed/t:translate-x-8 group-aria-pressed/t:text-tvt16-moon motion-reduce:transition-none">
              <svg viewBox="0 0 24 24" width="18" height="18" focusable="false">
                <mask id="tvt-16-crescent"><rect width="24" height="24" fill="#fff"/><circle cx="17" cy="7.5" r="6.5" fill="#000" class="translate-x-[9px] -translate-y-[9px] transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] group-aria-pressed/t:translate-0 motion-reduce:transition-none"/></mask>
                <circle cx="12" cy="12" r="5" fill="currentColor" mask="url(#tvt-16-crescent)" class="origin-center scale-100 transition-transform duration-500 [transform-box:fill-box] group-aria-pressed/t:scale-[1.6] motion-reduce:transition-none"/>
                <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" class="origin-center transition-[rotate,scale,opacity] duration-500 [transform-box:view-box] group-aria-pressed/t:scale-50 group-aria-pressed/t:rotate-90 group-aria-pressed/t:opacity-0 motion-reduce:transition-none"><path d="M12 1.8v2.3M12 19.9v2.3M1.8 12h2.3M19.9 12h2.3M4.8 4.8l1.6 1.6M17.6 17.6l1.6 1.6M19.2 4.8l-1.6 1.6M6.4 17.6l-1.6 1.6"/></g>
              </svg>
            </span>
          </span>
        </button>
      </div>

      <div class="grid grid-cols-[minmax(13rem,15.5rem)_minmax(0,1fr)] @max-[44rem]:grid-cols-1">
        <div class="flex flex-col gap-4 border-e border-tvt16-line bg-tvt16-raised p-3 transition-colors duration-500 @max-[44rem]:border-e-0 @max-[44rem]:border-b">
          <p class="px-3 pt-1 font-tvt16-mono text-[10.5px] tracking-[0.14em] text-tvt16-mut uppercase @max-[44rem]:hidden">Theming guide</p>
          <div role="tablist" aria-orientation="vertical" aria-label="Theming topics" class="grid gap-1 @max-[44rem]:flex @max-[44rem]:overflow-x-auto @max-[44rem]:pb-1">

            <button type="button" role="tab" id="tvt-16-tab1" aria-controls="tvt-16-p1" aria-selected="true" class="group/tab flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-start text-[14px] font-medium text-tvt16-mut transition-[background-color,color,box-shadow] duration-200 hover:bg-tvt16-ink/[0.05] hover:text-tvt16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring aria-selected:bg-tvt16-surface aria-selected:font-semibold aria-selected:text-tvt16-ink aria-selected:shadow-tvt16-tab @max-[44rem]:shrink-0 @max-[44rem]:w-auto">
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 transition-colors group-aria-selected/tab:text-tvt16-acc-ink"><path d="M10 3 17 6.8 10 10.6 3 6.8Z M3 10.2l7 3.8 7-3.8 M3 13.6l7 3.8 7-3.8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              <span class="flex-1 whitespace-nowrap">Two token layers</span>
              <span aria-hidden="true" class="font-tvt16-mono text-[10.5px] text-tvt16-mut/70 group-aria-selected/tab:text-tvt16-acc-ink @max-[44rem]:hidden">01</span>
            </button>

            <button type="button" role="tab" id="tvt-16-tab2" aria-controls="tvt-16-p2" aria-selected="false" tabindex="-1" class="group/tab flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-start text-[14px] font-medium text-tvt16-mut transition-[background-color,color,box-shadow] duration-200 hover:bg-tvt16-ink/[0.05] hover:text-tvt16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring aria-selected:bg-tvt16-surface aria-selected:font-semibold aria-selected:text-tvt16-ink aria-selected:shadow-tvt16-tab @max-[44rem]:shrink-0 @max-[44rem]:w-auto">
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 transition-colors group-aria-selected/tab:text-tvt16-acc-ink"><path d="M4 5.5h12M4 10h12M4 14.5h7" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="15" cy="14.5" r="2" fill="currentColor"/></svg>
              <span class="flex-1 whitespace-nowrap">System vs override</span>
              <span aria-hidden="true" class="font-tvt16-mono text-[10.5px] text-tvt16-mut/70 group-aria-selected/tab:text-tvt16-acc-ink @max-[44rem]:hidden">02</span>
            </button>

            <button type="button" role="tab" id="tvt-16-tab3" aria-controls="tvt-16-p3" aria-selected="false" tabindex="-1" class="group/tab flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-start text-[14px] font-medium text-tvt16-mut transition-[background-color,color,box-shadow] duration-200 hover:bg-tvt16-ink/[0.05] hover:text-tvt16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring aria-selected:bg-tvt16-surface aria-selected:font-semibold aria-selected:text-tvt16-ink aria-selected:shadow-tvt16-tab @max-[44rem]:shrink-0 @max-[44rem]:w-auto">
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 transition-colors group-aria-selected/tab:text-tvt16-acc-ink"><path d="M11 2.5 4.5 11h5l-1 6.5L15.5 9h-5Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              <span class="flex-1 whitespace-nowrap">No flash on load</span>
              <span aria-hidden="true" class="font-tvt16-mono text-[10.5px] text-tvt16-mut/70 group-aria-selected/tab:text-tvt16-acc-ink @max-[44rem]:hidden">03</span>
            </button>

            <button type="button" role="tab" id="tvt-16-tab4" aria-controls="tvt-16-p4" aria-selected="false" tabindex="-1" class="group/tab flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-start text-[14px] font-medium text-tvt16-mut transition-[background-color,color,box-shadow] duration-200 hover:bg-tvt16-ink/[0.05] hover:text-tvt16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt16-ring aria-selected:bg-tvt16-surface aria-selected:font-semibold aria-selected:text-tvt16-ink aria-selected:shadow-tvt16-tab @max-[44rem]:shrink-0 @max-[44rem]:w-auto">
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0 transition-colors group-aria-selected/tab:text-tvt16-acc-ink"><path d="M2.5 10s2.8-5.5 7.5-5.5 7.5 5.5 7.5 5.5-2.8 5.5-7.5 5.5S2.5 10 2.5 10Z" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="10" cy="10" r="2.3" fill="currentColor"/></svg>
              <span class="flex-1 whitespace-nowrap">Contrast, carefully</span>
              <span aria-hidden="true" class="font-tvt16-mono text-[10.5px] text-tvt16-mut/70 group-aria-selected/tab:text-tvt16-acc-ink @max-[44rem]:hidden">04</span>
            </button>
          </div>
          <div class="mt-auto rounded-xl bg-tvt16-surface p-3.5 ring-1 ring-tvt16-line @max-[44rem]:hidden">
            <p class="text-[12px] text-tvt16-mut">Active theme</p>
            <p class="mt-0.5 font-tvt16-mono text-[13px] font-medium text-tvt16-ink" data-readout>system</p>
          </div>
        </div>

        <div class="min-h-[22rem] p-5 sm:p-8">
          <article role="tabpanel" id="tvt-16-p1" aria-labelledby="tvt-16-tab1" tabindex="0" class="grid content-start gap-4 rounded-xl transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt16-ring starting:translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <h3 class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Primitives, then semantics</h3>
            <p class="max-w-[54ch] text-[14.5px] leading-[1.68] text-tvt16-mut text-pretty">Components reference <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">bg-tvt16-surface</code> and <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">text-tvt16-ink</code>, never a raw grey. The dark theme re-points those few semantic tokens &mdash; no component class changes.</p>
            <div class="rounded-2xl p-3 ring-1 ring-tvt16-line">
              <p class="mb-2 flex justify-between font-tvt16-mono text-[11px] text-tvt16-mut"><span>gray-50</span><span>primitives</span><span>gray-950</span></p>
              <div aria-hidden="true" class="grid grid-cols-10 gap-1"><span class="h-8 rounded-md bg-[oklch(0.985_0.002_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.95_0.004_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.9_0.006_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.8_0.008_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.66_0.01_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.52_0.012_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.4_0.012_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.29_0.01_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.21_0.008_260)] ring-1 ring-tvt16-ink/12"></span><span class="h-8 rounded-md bg-[oklch(0.16_0.006_260)] ring-1 ring-tvt16-ink/12"></span></div>
            </div>
            <ul class="divide-y divide-tvt16-line rounded-2xl ring-1 ring-tvt16-line">
              <li class="flex items-center gap-3 px-3.5 py-2.5"><span aria-hidden="true" class="size-7 shrink-0 rounded-lg bg-tvt16-surface ring-1 ring-tvt16-ink/15 transition-colors duration-500"></span><code class="font-tvt16-mono text-[12.5px] text-tvt16-ink">--surface</code><span class="ms-auto truncate font-tvt16-mono text-[11.5px] text-tvt16-mut">gray-50 · gray-900</span></li>
              <li class="flex items-center gap-3 px-3.5 py-2.5"><span aria-hidden="true" class="size-7 shrink-0 rounded-lg bg-tvt16-raised ring-1 ring-tvt16-ink/15 transition-colors duration-500"></span><code class="font-tvt16-mono text-[12.5px] text-tvt16-ink">--raised</code><span class="ms-auto truncate font-tvt16-mono text-[11.5px] text-tvt16-mut">gray-100 · gray-950</span></li>
              <li class="flex items-center gap-3 px-3.5 py-2.5"><span aria-hidden="true" class="size-7 shrink-0 rounded-lg bg-tvt16-ink ring-1 ring-tvt16-ink/15 transition-colors duration-500"></span><code class="font-tvt16-mono text-[12.5px] text-tvt16-ink">--ink</code><span class="ms-auto truncate font-tvt16-mono text-[11.5px] text-tvt16-mut">gray-950 · gray-50</span></li>
              <li class="flex items-center gap-3 px-3.5 py-2.5"><span aria-hidden="true" class="size-7 shrink-0 rounded-lg bg-tvt16-acc ring-1 ring-tvt16-ink/15 transition-colors duration-500"></span><code class="font-tvt16-mono text-[12.5px] text-tvt16-ink">--accent</code><span class="ms-auto truncate font-tvt16-mono text-[11.5px] text-tvt16-mut">amber-600 · amber-300</span></li>
            </ul>
          </article>
          <article role="tabpanel" id="tvt-16-p2" aria-labelledby="tvt-16-tab2" tabindex="0" hidden class="grid content-start gap-4 rounded-xl transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt16-ring starting:translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <h3 class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">The override always wins</h3>
            <p class="max-w-[54ch] text-[14.5px] leading-[1.68] text-tvt16-mut text-pretty">Defaults come from <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">prefers-color-scheme</code>; an explicit <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">data-theme</code> on the root outranks them because the media block is written as <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">:not([data-theme="light"])</code>.</p>
            <ol class="grid gap-2">
              <li class="flex items-center gap-3 rounded-xl bg-tvt16-raised px-3.5 py-3 ring-1 ring-tvt16-line"><span class="grid size-7 place-items-center rounded-full bg-tvt16-ink/10 font-tvt16-mono text-[11px] font-semibold">1</span><span class="min-w-0 text-[13.5px]"><b class="font-semibold">Default</b> <span class="text-tvt16-mut">· @media (prefers-color-scheme: dark)</span></span></li>
              <li class="flex items-center gap-3 rounded-xl bg-tvt16-raised px-3.5 py-3 ring-1 ring-tvt16-line"><span class="grid size-7 place-items-center rounded-full bg-tvt16-ink/10 font-tvt16-mono text-[11px] font-semibold">2</span><span class="min-w-0 text-[13.5px]"><b class="font-semibold">Override</b> <span class="text-tvt16-mut">· .tvt-16[data-theme="dark"]</span></span></li>
              <li class="flex items-center gap-3 rounded-xl bg-tvt16-acc/12 px-3.5 py-3 ring-1 ring-tvt16-acc/35"><span class="grid size-7 place-items-center rounded-full bg-tvt16-acc text-tvt16-on-acc"><svg viewBox="0 0 20 20" width="13" height="13" aria-hidden="true" focusable="false"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="text-[13.5px]"><b class="font-semibold">Result</b> <span class="font-tvt16-mono text-[12.5px] text-tvt16-acc-ink" data-readout>system</span></span></li>
            </ol>
          </article>
          <article role="tabpanel" id="tvt-16-p3" aria-labelledby="tvt-16-tab3" tabindex="0" hidden class="grid content-start gap-4 rounded-xl transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt16-ring starting:translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <h3 class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Set it before first paint</h3>
            <p class="max-w-[54ch] text-[14.5px] leading-[1.68] text-tvt16-mut text-pretty">A stored preference read in a deferred script paints the wrong theme first. Read it inline in the <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">&lt;head&gt;</code>, and set <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">color-scheme</code> so scrollbars and form controls follow.</p>
            <pre class="overflow-x-auto rounded-2xl bg-tvt16-code px-4 py-4 font-tvt16-mono text-[12.5px] leading-[1.75] text-[oklch(0.9_0.005_260)] ring-1 ring-black/10"><code><span class="text-[oklch(0.65_0.01_260)] italic">&lt;!-- inline, in &lt;head&gt;, before CSS --&gt;</span>
<span class="text-[oklch(0.78_0.12_25)]">&lt;script&gt;</span>
  <span class="text-[oklch(0.8_0.12_300)]">try</span> {
    <span class="text-[oklch(0.8_0.12_300)]">const</span> t = localStorage.getItem(<span class="text-[oklch(0.84_0.13_150)]">'theme'</span>);
    <span class="text-[oklch(0.8_0.12_300)]">if</span> (t) document.documentElement.dataset.theme = t;
  } <span class="text-[oklch(0.8_0.12_300)]">catch</span> {}
<span class="text-[oklch(0.78_0.12_25)]">&lt;/script&gt;</span></code></pre>
            <p class="font-tvt16-mono text-[12px] text-tvt16-mut">color-scheme: light dark · no flash, no white scrollbar</p>
          </article>
          <article role="tabpanel" id="tvt-16-p4" aria-labelledby="tvt-16-tab4" tabindex="0" hidden class="grid content-start gap-4 rounded-xl transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt16-ring starting:translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <h3 class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Not pure black</h3>
            <p class="max-w-[54ch] text-[14.5px] leading-[1.68] text-tvt16-mut text-pretty">Maximum contrast causes halation for readers with astigmatism. This theme bottoms out near <code class="rounded-md bg-tvt16-ink/[0.07] px-1.5 py-0.5 font-tvt16-mono text-[12px] text-tvt16-ink">oklch(0.16)</code> &mdash; about 15:1, not 21:1 &mdash; and muted copy still clears 4.5:1.</p>
            <div class="grid gap-3 sm:grid-cols-2">
              <div class="rounded-2xl bg-black p-4 text-white ring-1 ring-tvt16-line"><p class="text-[15px] font-semibold">Pure #000 / #fff</p><p class="mt-1 text-[12.5px] text-white/75">21:1 · text can glow and smear</p><p class="mt-3 inline-flex rounded-full bg-white/12 px-2 py-0.5 font-tvt16-mono text-[11px]">halation risk</p></div>
              <div class="rounded-2xl bg-tvt16-raised p-4 ring-1 ring-tvt16-line"><p class="text-[15px] font-semibold">This theme</p><p class="mt-1 text-[12.5px] text-tvt16-mut">≈15:1 ink · ≈7:1 muted</p><p class="mt-3 inline-flex rounded-full bg-tvt16-ok/12 px-2 py-0.5 font-tvt16-mono text-[11px] text-tvt16-ok">AAA comfortable</p></div>
            </div>
          </article>
        </div>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt16-surface px-3.5 py-2 text-center font-tvt16-mono text-[11.5px] text-tvt16-mut ring-1 ring-tvt16-line">.tvt-16[data-theme="dark"] · group-aria-pressed/t: · color-scheme</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt16-bg: #f4f6f8;
  --color-tvt16-bg: oklch(0.972 0.004 260);
  --color-tvt16-glow: #fae5c3b3;
  --color-tvt16-glow: oklch(0.93 0.05 80 / 0.7);
  --color-tvt16-surface: #ffffff;
  --color-tvt16-surface: oklch(1 0 0);
  --color-tvt16-raised: #f3f4f7;
  --color-tvt16-raised: oklch(0.968 0.004 260);
  --color-tvt16-ink: #13161b;
  --color-tvt16-ink: oklch(0.2 0.01 260);
  --color-tvt16-mut: #575b62;
  --color-tvt16-mut: oklch(0.47 0.012 260);
  --color-tvt16-line: #dcdee2;
  --color-tvt16-line: oklch(0.9 0.006 260);
  --color-tvt16-acc: #df8600;
  --color-tvt16-acc: oklch(0.7 0.16 65);
  --color-tvt16-acc-ink: #974c00;
  --color-tvt16-acc-ink: oklch(0.5 0.13 55);
  --color-tvt16-on-acc: #201308;
  --color-tvt16-on-acc: oklch(0.2 0.03 60);
  --color-tvt16-ring: #a75c00;
  --color-tvt16-ring: oklch(0.55 0.14 60);
  --color-tvt16-sun: #ef8600;
  --color-tvt16-sun: oklch(0.72 0.17 60);
  --color-tvt16-moon: #5761d8;
  --color-tvt16-moon: oklch(0.55 0.18 275);
  --color-tvt16-night: #272d60;
  --color-tvt16-night: oklch(0.32 0.09 275);
  --color-tvt16-code: #13161b;
  --color-tvt16-code: oklch(0.2 0.01 260);
  --color-tvt16-ok: #00764c;
  --color-tvt16-ok: oklch(0.5 0.12 160);
  --font-tvt16-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-tvt16-mono: 'Martian Mono', ui-monospace, monospace;
  --shadow-tvt16-card: 0 1px 2px oklch(0.2 0.01 260 / 0.06), 0 30px 70px -34px oklch(0.2 0.02 260 / 0.45);
  --shadow-tvt16-tab: 0 1px 2px oklch(0.2 0.01 260 / 0.1), 0 4px 12px -6px oklch(0.2 0.01 260 / 0.25), inset 0 0 0 1px oklch(0.5 0.01 260 / 0.12);
  --shadow-tvt16-knob: 0 2px 6px -1px oklch(0 0 0 / 0.35), inset 0 1px 0 oklch(1 0 0 / 0.3);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-16 {
  width: 100%;
  min-height: 100svh;
}
/* color-scheme follows the same precedence as the tokens, so native scrollbars and controls match. */

.tvt-16 {
  color-scheme: light;
}

@media (prefers-color-scheme: dark) {
  .tvt-16:not([data-theme="light"]) {
    color-scheme: dark;
  }
}

.tvt-16[data-theme="dark"] {
  color-scheme: dark;
}
/* Circular reveal: only while the script marks the document with data-tvt16-flip, so other demos' view
   transitions keep the default cross-fade. The circle grows from the switch (--tvt16-x / --tvt16-y). */

html[data-tvt16-flip]::view-transition-old(root),
html[data-tvt16-flip]::view-transition-new(root) {
  mix-blend-mode: normal;
}

html[data-tvt16-flip]::view-transition-old(root) {
  animation: none;
}

html[data-tvt16-flip]::view-transition-new(root) {
  animation: tvt16-reveal .62s cubic-bezier(.65, 0, .35, 1);
}

@keyframes tvt16-reveal {
  from {
    clip-path: circle(0 at var(--tvt16-x, 50%) var(--tvt16-y, 0));
  }

  to {
    clip-path: circle(150vmax at var(--tvt16-x, 50%) var(--tvt16-y, 0));
  }
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-16:not([data-theme="light"]) {
    --color-tvt16-bg: #0b0c0f;
    --color-tvt16-bg: oklch(0.155 0.006 260);
    --color-tvt16-glow: #23295573;
    --color-tvt16-glow: oklch(0.3 0.08 275 / 0.45);
    --color-tvt16-surface: #15171b;
    --color-tvt16-surface: oklch(0.205 0.008 260);
    --color-tvt16-raised: #101215;
    --color-tvt16-raised: oklch(0.18 0.007 260);
    --color-tvt16-ink: #f2f3f6;
    --color-tvt16-ink: oklch(0.965 0.004 260);
    --color-tvt16-mut: #aaaeb4;
    --color-tvt16-mut: oklch(0.75 0.01 260);
    --color-tvt16-line: #2b2e33;
    --color-tvt16-line: oklch(0.3 0.01 260);
    --color-tvt16-acc: #fcb442;
    --color-tvt16-acc: oklch(0.82 0.15 75);
    --color-tvt16-acc-ink: #fcc364;
    --color-tvt16-acc-ink: oklch(0.85 0.13 78);
    --color-tvt16-on-acc: #201308;
    --color-tvt16-on-acc: oklch(0.2 0.03 60);
    --color-tvt16-ring: #f9b64f;
    --color-tvt16-ring: oklch(0.82 0.14 75);
    --color-tvt16-sun: #fea92f;
    --color-tvt16-sun: oklch(0.8 0.16 70);
    --color-tvt16-moon: #b0b7ff;
    --color-tvt16-moon: oklch(0.8 0.11 280);
    --color-tvt16-night: #21265f;
    --color-tvt16-night: oklch(0.3 0.1 275);
    --color-tvt16-code: #06070a;
    --color-tvt16-code: oklch(0.13 0.006 260);
    --color-tvt16-ok: #68d7a1;
    --color-tvt16-ok: oklch(0.8 0.13 160);
  }
}

.tvt-16[data-theme="dark"] {
  --color-tvt16-bg: #0b0c0f;
  --color-tvt16-bg: oklch(0.155 0.006 260);
  --color-tvt16-glow: #23295573;
  --color-tvt16-glow: oklch(0.3 0.08 275 / 0.45);
  --color-tvt16-surface: #15171b;
  --color-tvt16-surface: oklch(0.205 0.008 260);
  --color-tvt16-raised: #101215;
  --color-tvt16-raised: oklch(0.18 0.007 260);
  --color-tvt16-ink: #f2f3f6;
  --color-tvt16-ink: oklch(0.965 0.004 260);
  --color-tvt16-mut: #aaaeb4;
  --color-tvt16-mut: oklch(0.75 0.01 260);
  --color-tvt16-line: #2b2e33;
  --color-tvt16-line: oklch(0.3 0.01 260);
  --color-tvt16-acc: #fcb442;
  --color-tvt16-acc: oklch(0.82 0.15 75);
  --color-tvt16-acc-ink: #fcc364;
  --color-tvt16-acc-ink: oklch(0.85 0.13 78);
  --color-tvt16-on-acc: #201308;
  --color-tvt16-on-acc: oklch(0.2 0.03 60);
  --color-tvt16-ring: #f9b64f;
  --color-tvt16-ring: oklch(0.82 0.14 75);
  --color-tvt16-sun: #fea92f;
  --color-tvt16-sun: oklch(0.8 0.16 70);
  --color-tvt16-moon: #b0b7ff;
  --color-tvt16-moon: oklch(0.8 0.11 280);
  --color-tvt16-night: #21265f;
  --color-tvt16-night: oklch(0.3 0.1 275);
  --color-tvt16-code: #06070a;
  --color-tvt16-code: oklch(0.13 0.006 260);
  --color-tvt16-ok: #68d7a1;
  --color-tvt16-ok: oklch(0.8 0.13 160);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-16-root');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const toggle = root.querySelector('[data-toggle]');
  const system = root.querySelector('[data-system]');
  const readouts = root.querySelectorAll('[data-readout]');
  const tabs = [...root.querySelectorAll('[role="tab"]')];
  const mq = matchMedia('(prefers-color-scheme: dark)');
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  const html = document.documentElement;
  const current = () => root.dataset.theme || (mq.matches ? 'dark' : 'light');
  const sync = () => {
    const t = current();
    toggle.setAttribute('aria-pressed', String(t === 'dark'));
    system.disabled = !root.dataset.theme;
    readouts.forEach((el) => { el.textContent = t + (root.dataset.theme ? ' · override' : ' · system'); });
  };
  const flip = (change) => {
    if (typeof document.startViewTransition !== 'function' || calm.matches) { change(); sync(); return; }
    const r = toggle.getBoundingClientRect();
    html.style.setProperty('--tvt16-x', (r.left + r.width / 2) + 'px');
    html.style.setProperty('--tvt16-y', (r.top + r.height / 2) + 'px');
    html.setAttribute('data-tvt16-flip', '');
    document.startViewTransition(() => { change(); sync(); }).finished.finally(() => html.removeAttribute('data-tvt16-flip'));
  };
  toggle.addEventListener('click', () => flip(() => { root.dataset.theme = current() === 'dark' ? 'light' : 'dark'; }));
  system.addEventListener('click', () => flip(() => { root.removeAttribute('data-theme'); }));
  mq.addEventListener('change', sync);
  const select = (tab) => tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute('aria-selected', String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
  });
  tabs.forEach((t) => t.addEventListener('click', () => select(t)));
  root.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
    const i = tabs.indexOf(document.activeElement);
    let to = -1;
    if (step) to = (i + step + tabs.length) % tabs.length;
    else if (e.key === 'Home') to = 0;
    else if (e.key === 'End') to = tabs.length - 1;
    if (to < 0) return;
    e.preventDefault();
    tabs[to].focus();
    select(tabs[to]);
  });
  sync();
})();
```
