---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-css-vertical-tabs-component-aria-selected-no-alpine-js/"
title: "Tailwind CSS Vertical Tabs Component (aria-selected, No Alpine.js)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "The canonical Tailwind vertical tabs component, without Headless UI or Alpine.js: a four-step quickstart (Install, Configure, Deploy, Monitor) on a real…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Vertical Tabs Component (aria-selected, No Alpine.js)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-css-vertical-tabs-component-aria-selected-no-alpine-js/

The canonical Tailwind vertical tabs component, without Headless UI or Alpine.js: a four-step quickstart (Install, Configure, Deploy, Monitor) on a real role="tablist" where aria-selected: draws the active step, data-done: turns earlier steps into green checks and group-data-[step=3]/root:w-3/4 fills the progress bar. A 30-line script writes attributes only &mdash; never a class name.
## HTML
```html
<section class="tvt-07 w-full min-h-svh grid place-items-center bg-tvt07-bg bg-[radial-gradient(65%_50%_at_15%_0%,var(--color-tvt07-glow),transparent_70%),radial-gradient(55%_45%_at_95%_15%,var(--color-tvt07-glow2),transparent_70%)] px-4 py-14 font-tvt07-sans text-tvt07-ink antialiased sm:px-6" aria-label="Tailwind CSS vertical tabs component demo">
  <div class="grid w-full max-w-[58rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="rounded-full bg-tvt07-card px-3 py-1.5 font-tvt07-mono text-[11.5px] text-tvt07-acc-ink ring-1 ring-tvt07-line">aria-selected: · no Headless UI · no Alpine.js</p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-extrabold tracking-[-0.04em] text-balance">State in ARIA, <span class="bg-linear-to-r from-tvt07-hl to-tvt07-hl2 bg-clip-text pe-1 text-transparent">style in variants</span></h2>
      <p class="max-w-[48ch] text-[15px] leading-relaxed text-tvt07-mut text-pretty">A quickstart wizard built on a real WAI-ARIA tablist. Arrow keys move between steps; every visual state reads an attribute.</p>
    </header>

    <div id="tvt-07-guide" data-step="1" class="group/root @container w-full overflow-hidden rounded-[22px] bg-tvt07-card shadow-tvt07-card ring-1 ring-tvt07-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex flex-wrap items-center gap-x-4 gap-y-2 border-b border-tvt07-line px-5 py-4 sm:px-6">
        <span aria-hidden="true" class="grid size-9 place-items-center rounded-xl bg-linear-to-br from-tvt07-acc to-tvt07-acc2 text-white shadow-tvt07-dot"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M10.5 2.5 4 11h5l-.5 6.5L16 9h-5Z" fill="currentColor"/></svg></span>
        <div class="min-w-0 flex-1 leading-tight"><p class="text-[15px] font-bold tracking-[-0.01em]">Ship your first Skyline app</p><p class="text-[12.5px] text-tvt07-mut">About 8 minutes · Node 20+</p></div>
        <div class="flex w-40 items-center gap-2.5 max-[420px]:w-full">
          <div class="h-1.5 flex-1 overflow-hidden rounded-full bg-tvt07-line"><div class="h-full w-1/4 rounded-full bg-linear-to-r from-tvt07-acc to-tvt07-acc2 transition-[width] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-data-[step=2]/root:w-2/4 group-data-[step=3]/root:w-3/4 group-data-[step=4]/root:w-full motion-reduce:transition-none"></div></div>
          <span class="font-tvt07-mono text-[12px] text-tvt07-mut tabular-nums"><span class="group-data-[step=1]/root:inline hidden">1</span><span class="group-data-[step=2]/root:inline hidden">2</span><span class="group-data-[step=3]/root:inline hidden">3</span><span class="group-data-[step=4]/root:inline hidden">4</span>/4</span>
        </div>
      </div>

      <div class="grid grid-cols-[clamp(13rem,30%,16rem)_minmax(0,1fr)] @max-[40rem]:grid-cols-1">
        <div role="tablist" aria-orientation="vertical" aria-label="Quickstart steps" class="relative border-e border-tvt07-line bg-tvt07-rail py-3 @max-[40rem]:grid @max-[40rem]:grid-cols-4 @max-[40rem]:border-e-0 @max-[40rem]:border-b @max-[40rem]:py-0">

            <button type="button" role="tab" id="tvt-07-tab1" aria-controls="tvt-07-panel1" aria-selected="true" class="group/tab relative flex min-h-16 w-full cursor-pointer items-center gap-3.5 border-s-2 border-transparent ps-4 pe-3 text-start text-tvt07-mut transition-[color,background-color,border-color] duration-200 hover:bg-tvt07-ink/[0.035] hover:text-tvt07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt07-ring aria-selected:border-tvt07-acc aria-selected:bg-tvt07-acc/[0.07] aria-selected:text-tvt07-ink motion-reduce:transition-none @max-[40rem]:min-h-[4.5rem] @max-[40rem]:flex-col @max-[40rem]:justify-center @max-[40rem]:gap-1.5 @max-[40rem]:border-s-0 @max-[40rem]:border-b-2 @max-[40rem]:px-1 @max-[40rem]:text-center">
              <span class="relative z-10 grid size-8 shrink-0 place-items-center rounded-full bg-tvt07-card font-tvt07-mono text-[12.5px] font-semibold ring-1 ring-tvt07-line transition-[background-color,color,box-shadow] duration-200 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt07-acc group-aria-selected/tab:to-tvt07-acc2 group-aria-selected/tab:text-white group-aria-selected/tab:shadow-tvt07-dot group-aria-selected/tab:ring-0 group-data-done/tab:bg-tvt07-ok group-data-done/tab:text-white group-data-done/tab:ring-0"><span class="group-data-done/tab:hidden">1</span><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="hidden group-data-done/tab:block"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="grid min-w-0 leading-tight"><span class="text-[14.5px] font-semibold">Install</span><span class="mt-0.5 text-[12.5px] text-tvt07-mut @max-[40rem]:hidden">Add the package</span></span>
            </button>

            <button type="button" role="tab" id="tvt-07-tab2" aria-controls="tvt-07-panel2" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-16 w-full cursor-pointer items-center gap-3.5 border-s-2 border-transparent ps-4 pe-3 text-start text-tvt07-mut transition-[color,background-color,border-color] duration-200 hover:bg-tvt07-ink/[0.035] hover:text-tvt07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt07-ring aria-selected:border-tvt07-acc aria-selected:bg-tvt07-acc/[0.07] aria-selected:text-tvt07-ink motion-reduce:transition-none @max-[40rem]:min-h-[4.5rem] @max-[40rem]:flex-col @max-[40rem]:justify-center @max-[40rem]:gap-1.5 @max-[40rem]:border-s-0 @max-[40rem]:border-b-2 @max-[40rem]:px-1 @max-[40rem]:text-center">
              <span class="relative z-10 grid size-8 shrink-0 place-items-center rounded-full bg-tvt07-card font-tvt07-mono text-[12.5px] font-semibold ring-1 ring-tvt07-line transition-[background-color,color,box-shadow] duration-200 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt07-acc group-aria-selected/tab:to-tvt07-acc2 group-aria-selected/tab:text-white group-aria-selected/tab:shadow-tvt07-dot group-aria-selected/tab:ring-0 group-data-done/tab:bg-tvt07-ok group-data-done/tab:text-white group-data-done/tab:ring-0"><span class="group-data-done/tab:hidden">2</span><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="hidden group-data-done/tab:block"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="grid min-w-0 leading-tight"><span class="text-[14.5px] font-semibold">Configure</span><span class="mt-0.5 text-[12.5px] text-tvt07-mut @max-[40rem]:hidden">One CSS import</span></span>
            </button>

            <button type="button" role="tab" id="tvt-07-tab3" aria-controls="tvt-07-panel3" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-16 w-full cursor-pointer items-center gap-3.5 border-s-2 border-transparent ps-4 pe-3 text-start text-tvt07-mut transition-[color,background-color,border-color] duration-200 hover:bg-tvt07-ink/[0.035] hover:text-tvt07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt07-ring aria-selected:border-tvt07-acc aria-selected:bg-tvt07-acc/[0.07] aria-selected:text-tvt07-ink motion-reduce:transition-none @max-[40rem]:min-h-[4.5rem] @max-[40rem]:flex-col @max-[40rem]:justify-center @max-[40rem]:gap-1.5 @max-[40rem]:border-s-0 @max-[40rem]:border-b-2 @max-[40rem]:px-1 @max-[40rem]:text-center">
              <span class="relative z-10 grid size-8 shrink-0 place-items-center rounded-full bg-tvt07-card font-tvt07-mono text-[12.5px] font-semibold ring-1 ring-tvt07-line transition-[background-color,color,box-shadow] duration-200 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt07-acc group-aria-selected/tab:to-tvt07-acc2 group-aria-selected/tab:text-white group-aria-selected/tab:shadow-tvt07-dot group-aria-selected/tab:ring-0 group-data-done/tab:bg-tvt07-ok group-data-done/tab:text-white group-data-done/tab:ring-0"><span class="group-data-done/tab:hidden">3</span><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="hidden group-data-done/tab:block"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="grid min-w-0 leading-tight"><span class="text-[14.5px] font-semibold">Deploy</span><span class="mt-0.5 text-[12.5px] text-tvt07-mut @max-[40rem]:hidden">Build and ship</span></span>
            </button>

            <button type="button" role="tab" id="tvt-07-tab4" aria-controls="tvt-07-panel4" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-16 w-full cursor-pointer items-center gap-3.5 border-s-2 border-transparent ps-4 pe-3 text-start text-tvt07-mut transition-[color,background-color,border-color] duration-200 hover:bg-tvt07-ink/[0.035] hover:text-tvt07-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt07-ring aria-selected:border-tvt07-acc aria-selected:bg-tvt07-acc/[0.07] aria-selected:text-tvt07-ink motion-reduce:transition-none @max-[40rem]:min-h-[4.5rem] @max-[40rem]:flex-col @max-[40rem]:justify-center @max-[40rem]:gap-1.5 @max-[40rem]:border-s-0 @max-[40rem]:border-b-2 @max-[40rem]:px-1 @max-[40rem]:text-center">
              <span class="relative z-10 grid size-8 shrink-0 place-items-center rounded-full bg-tvt07-card font-tvt07-mono text-[12.5px] font-semibold ring-1 ring-tvt07-line transition-[background-color,color,box-shadow] duration-200 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt07-acc group-aria-selected/tab:to-tvt07-acc2 group-aria-selected/tab:text-white group-aria-selected/tab:shadow-tvt07-dot group-aria-selected/tab:ring-0 group-data-done/tab:bg-tvt07-ok group-data-done/tab:text-white group-data-done/tab:ring-0"><span class="group-data-done/tab:hidden">4</span><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="hidden group-data-done/tab:block"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="grid min-w-0 leading-tight"><span class="text-[14.5px] font-semibold">Monitor</span><span class="mt-0.5 text-[12.5px] text-tvt07-mut @max-[40rem]:hidden">Watch your vitals</span></span>
            </button>
        </div>

        <div class="min-h-[27rem] min-w-0 p-6 sm:p-8 @max-[40rem]:min-h-0">

            <div role="tabpanel" id="tvt-07-panel1" aria-labelledby="tvt-07-tab1" tabindex="0" class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt07-ring motion-safe:animate-tvt07-in">
              <p class="font-tvt07-mono text-[11.5px] font-medium tracking-[0.12em] text-tvt07-acc-ink uppercase">Step 1 · 1 min</p>
              <h3 class="mt-1.5 text-[clamp(20px,2.4vw,25px)] font-bold tracking-[-0.03em]">Install the toolchain</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt07-mut text-pretty">Add Tailwind and the Vite plugin. No PostCSS config, no <code class="font-tvt07-mono text-[13px]">tailwind.config.js</code>.</p>
              <div class="mt-5 overflow-hidden rounded-2xl bg-tvt07-code shadow-tvt07-code ring-1 ring-white/10">
                <div class="flex items-center gap-3 border-b border-white/8 px-4 py-2">
                  <span aria-hidden="true" class="flex gap-1.5"><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span></span>
                  <span class="flex-1 truncate font-tvt07-mono text-[12px] text-tvt07-code-mut">terminal</span>
                  <button type="button" data-copy="tvt-07-code1" class="group/copy inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-lg px-2.5 text-[12px] font-semibold text-tvt07-code-mut transition-colors hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tvt07-ring data-copied:text-tvt07-code-ok"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg><span class="group-data-copied/copy:hidden">Copy</span><span class="hidden group-data-copied/copy:inline">Copied</span></button>
                </div>
                <pre id="tvt-07-code1" class="overflow-x-auto px-4 py-3.5 font-tvt07-mono text-[13px] leading-[1.75] text-tvt07-code-ink"><code><span class="text-tvt07-code-ok select-none">$ </span>npm install tailwindcss @tailwindcss/vite
<span class="text-tvt07-code-mut">added 14 packages in 3.2s</span></code></pre>
              </div>
              <div class="mt-4 flex gap-3 rounded-2xl bg-tvt07-acc/[0.06] p-4 ring-1 ring-tvt07-acc/15">
                <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt07-acc-ink"><path d="M10 2.8a5 5 0 0 0-3 9v1.7h6v-1.7a5 5 0 0 0-3-9ZM8 16.5h4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <div class="min-w-0"><p class="text-[13.5px] font-semibold">One attribute, one truth</p><p class="mt-1 text-[13px] leading-relaxed text-tvt07-mut text-pretty">The <code class="font-tvt07-mono text-[12px]">aria-selected:</code> variant compiles to <code class="font-tvt07-mono text-[12px]">&amp;[aria-selected="true"]</code>, so the step you see and the step a screen reader announces can never disagree.</p><p class="mt-2 inline-block rounded-md bg-tvt07-card px-2 py-1 font-tvt07-mono text-[11.5px] text-tvt07-acc-ink ring-1 ring-tvt07-line">aria-selected:border-tvt07-acc</p></div>
              </div>
              <div class="mt-5 flex justify-end"><button type="button" data-goto="tvt-07-tab2" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl bg-linear-to-br from-tvt07-acc to-tvt07-acc2 px-4 text-[14px] font-semibold text-white shadow-tvt07-dot transition-[translate,box-shadow] duration-200 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt07-ring active:translate-y-0 motion-reduce:transition-none">Next: Configure<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4.5 10h11m-4.5-4.5L15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>
            </div>

            <div role="tabpanel" id="tvt-07-panel2" aria-labelledby="tvt-07-tab2" tabindex="0" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt07-ring motion-safe:animate-tvt07-in">
              <p class="font-tvt07-mono text-[11.5px] font-medium tracking-[0.12em] text-tvt07-acc-ink uppercase">Step 2 · 2 min</p>
              <h3 class="mt-1.5 text-[clamp(20px,2.4vw,25px)] font-bold tracking-[-0.03em]">Configure in CSS</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt07-mut text-pretty">Register the plugin, then import Tailwind once. Your theme lives in CSS with <code class="font-tvt07-mono text-[13px]">@theme</code>.</p>
              <div class="mt-5 overflow-hidden rounded-2xl bg-tvt07-code shadow-tvt07-code ring-1 ring-white/10">
                <div class="flex items-center gap-3 border-b border-white/8 px-4 py-2">
                  <span aria-hidden="true" class="flex gap-1.5"><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span></span>
                  <span class="flex-1 truncate font-tvt07-mono text-[12px] text-tvt07-code-mut">vite.config.ts · app.css</span>
                  <button type="button" data-copy="tvt-07-code2" class="group/copy inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-lg px-2.5 text-[12px] font-semibold text-tvt07-code-mut transition-colors hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tvt07-ring data-copied:text-tvt07-code-ok"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg><span class="group-data-copied/copy:hidden">Copy</span><span class="hidden group-data-copied/copy:inline">Copied</span></button>
                </div>
                <pre id="tvt-07-code2" class="overflow-x-auto px-4 py-3.5 font-tvt07-mono text-[13px] leading-[1.75] text-tvt07-code-ink"><code><span class="text-tvt07-code-k">import</span> tailwindcss <span class="text-tvt07-code-k">from</span> <span class="text-tvt07-code-s">'@tailwindcss/vite'</span>
<span class="text-tvt07-code-k">export default</span> { plugins: [tailwindcss()] }

<span class="text-tvt07-code-mut">/* app.css */</span>
<span class="text-tvt07-code-k">@import</span> <span class="text-tvt07-code-s">"tailwindcss"</span>;</code></pre>
              </div>
              <div class="mt-4 flex gap-3 rounded-2xl bg-tvt07-acc/[0.06] p-4 ring-1 ring-tvt07-acc/15">
                <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt07-acc-ink"><path d="M10 2.8a5 5 0 0 0-3 9v1.7h6v-1.7a5 5 0 0 0-3-9ZM8 16.5h4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <div class="min-w-0"><p class="text-[13.5px] font-semibold">Reserve the border</p><p class="mt-1 text-[13px] leading-relaxed text-tvt07-mut text-pretty"><code class="font-tvt07-mono text-[12px]">border-s-2 border-transparent</code> on every step means selecting one recolours 2px instead of inserting them &mdash; no sideways jolt.</p><p class="mt-2 inline-block rounded-md bg-tvt07-card px-2 py-1 font-tvt07-mono text-[11.5px] text-tvt07-acc-ink ring-1 ring-tvt07-line">border-s-2 border-transparent</p></div>
              </div>
              <div class="mt-5 flex justify-end"><button type="button" data-goto="tvt-07-tab3" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl bg-linear-to-br from-tvt07-acc to-tvt07-acc2 px-4 text-[14px] font-semibold text-white shadow-tvt07-dot transition-[translate,box-shadow] duration-200 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt07-ring active:translate-y-0 motion-reduce:transition-none">Next: Deploy<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4.5 10h11m-4.5-4.5L15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>
            </div>

            <div role="tabpanel" id="tvt-07-panel3" aria-labelledby="tvt-07-tab3" tabindex="0" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt07-ring motion-safe:animate-tvt07-in">
              <p class="font-tvt07-mono text-[11.5px] font-medium tracking-[0.12em] text-tvt07-acc-ink uppercase">Step 3 · 3 min</p>
              <h3 class="mt-1.5 text-[clamp(20px,2.4vw,25px)] font-bold tracking-[-0.03em]">Build and deploy</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt07-mut text-pretty">Production builds tree-shake every unused utility. Most apps ship under 10 KB of CSS.</p>
              <div class="mt-5 overflow-hidden rounded-2xl bg-tvt07-code shadow-tvt07-code ring-1 ring-white/10">
                <div class="flex items-center gap-3 border-b border-white/8 px-4 py-2">
                  <span aria-hidden="true" class="flex gap-1.5"><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span><span class="size-2.5 rounded-full bg-white/18"></span></span>
                  <span class="flex-1 truncate font-tvt07-mono text-[12px] text-tvt07-code-mut">terminal</span>
                  <button type="button" data-copy="tvt-07-code3" class="group/copy inline-flex min-h-9 cursor-pointer items-center gap-1.5 rounded-lg px-2.5 text-[12px] font-semibold text-tvt07-code-mut transition-colors hover:bg-white/8 hover:text-white focus-visible:outline-2 focus-visible:outline-tvt07-ring data-copied:text-tvt07-code-ok"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="6.5" y="6.5" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 6.5V5a1.5 1.5 0 0 0-1.5-1.5H5A1.5 1.5 0 0 0 3.5 5v7A1.5 1.5 0 0 0 5 13.5h1.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg><span class="group-data-copied/copy:hidden">Copy</span><span class="hidden group-data-copied/copy:inline">Copied</span></button>
                </div>
                <pre id="tvt-07-code3" class="overflow-x-auto px-4 py-3.5 font-tvt07-mono text-[13px] leading-[1.75] text-tvt07-code-ink"><code><span class="text-tvt07-code-ok select-none">$ </span>npm run build
<span class="text-tvt07-code-mut">dist/assets/index.css   8.41 kB │ gzip: 2.37 kB</span>
<span class="text-tvt07-code-ok select-none">$ </span>skyline deploy --prod
<span class="text-tvt07-code-s">✓ Live at https://atlas.skyline.app</span></code></pre>
              </div>
              <div class="mt-4 flex gap-3 rounded-2xl bg-tvt07-acc/[0.06] p-4 ring-1 ring-tvt07-acc/15">
                <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt07-acc-ink"><path d="M10 2.8a5 5 0 0 0-3 9v1.7h6v-1.7a5 5 0 0 0-3-9ZM8 16.5h4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <div class="min-w-0"><p class="text-[13.5px] font-semibold">No library needed</p><p class="mt-1 text-[13px] leading-relaxed text-tvt07-mut text-pretty">About 25 lines of vanilla JS replace Headless UI here: flip <code class="font-tvt07-mono text-[12px]">aria-selected</code>, toggle <code class="font-tvt07-mono text-[12px]">hidden</code>, move the roving <code class="font-tvt07-mono text-[12px]">tabindex</code>.</p><p class="mt-2 inline-block rounded-md bg-tvt07-card px-2 py-1 font-tvt07-mono text-[11.5px] text-tvt07-acc-ink ring-1 ring-tvt07-line">el.setAttribute('aria-selected', on)</p></div>
              </div>
              <div class="mt-5 flex justify-end"><button type="button" data-goto="tvt-07-tab4" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl bg-linear-to-br from-tvt07-acc to-tvt07-acc2 px-4 text-[14px] font-semibold text-white shadow-tvt07-dot transition-[translate,box-shadow] duration-200 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt07-ring active:translate-y-0 motion-reduce:transition-none">Next: Monitor<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4.5 10h11m-4.5-4.5L15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>
            </div>

            <div role="tabpanel" id="tvt-07-panel4" aria-labelledby="tvt-07-tab4" tabindex="0" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt07-ring motion-safe:animate-tvt07-in">
              <p class="font-tvt07-mono text-[11.5px] font-medium tracking-[0.12em] text-tvt07-acc-ink uppercase">Step 4 · 2 min</p>
              <h3 class="mt-1.5 text-[clamp(20px,2.4vw,25px)] font-bold tracking-[-0.03em]">Monitor real users</h3>
              <p class="mt-1.5 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt07-mut text-pretty">Core Web Vitals from real sessions, updated every five minutes.</p>
              <dl class="mt-5 grid grid-cols-3 gap-2.5 sm:gap-3">
                <div class="rounded-2xl bg-tvt07-rail p-3 ring-1 ring-tvt07-line sm:p-4"><dt class="text-[12px] font-medium text-tvt07-mut">LCP</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">1.1s</dd><dd class="mt-1 text-[11.5px] font-semibold text-tvt07-ok">Good</dd></div>
                <div class="rounded-2xl bg-tvt07-rail p-3 ring-1 ring-tvt07-line sm:p-4"><dt class="text-[12px] font-medium text-tvt07-mut">INP</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">84ms</dd><dd class="mt-1 text-[11.5px] font-semibold text-tvt07-ok">Good</dd></div>
                <div class="rounded-2xl bg-tvt07-rail p-3 ring-1 ring-tvt07-line sm:p-4"><dt class="text-[12px] font-medium text-tvt07-mut">CLS</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">0.01</dd><dd class="mt-1 text-[11.5px] font-semibold text-tvt07-ok">Good</dd></div>
              </dl>
              <div aria-hidden="true" class="mt-4 flex h-20 items-end gap-1.5 rounded-2xl p-4 ring-1 ring-tvt07-line"><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:38%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:52%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:44%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:61%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:57%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:70%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:66%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:78%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:72%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:85%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:80%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:92%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:88%"></span><span class="flex-1 rounded-t-[3px] bg-linear-to-t from-tvt07-acc/45 to-tvt07-acc" style="height:96%"></span></div>
              <div class="mt-4 flex gap-3 rounded-2xl bg-tvt07-acc/[0.06] p-4 ring-1 ring-tvt07-acc/15">
                <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt07-acc-ink"><path d="M10 2.8a5 5 0 0 0-3 9v1.7h6v-1.7a5 5 0 0 0-3-9ZM8 16.5h4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <div class="min-w-0"><p class="text-[13.5px] font-semibold">Watch the scanner</p><p class="mt-1 text-[13px] leading-relaxed text-tvt07-mut text-pretty">Tailwind reads your source as text. Class names built in template literals are never generated &mdash; write them whole or safelist them.</p><p class="mt-2 inline-block rounded-md bg-tvt07-card px-2 py-1 font-tvt07-mono text-[11.5px] text-tvt07-acc-ink ring-1 ring-tvt07-line">&#96;text-&#36;{c}-600&#96; → not compiled</p></div>
              </div>
            </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt07-card px-3.5 py-2 text-center font-tvt07-mono text-[11.5px] text-tvt07-mut ring-1 ring-tvt07-line">aria-selected: · data-done: · group-data-[step]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt07-bg: #ebf6fc;
  --color-tvt07-bg: oklch(0.968 0.014 230);
  --color-tvt07-glow: #9be4fcb3;
  --color-tvt07-glow: oklch(0.88 0.08 220 / 0.7);
  --color-tvt07-glow2: #c6e1ff99;
  --color-tvt07-glow2: oklch(0.9 0.07 250 / 0.6);
  --color-tvt07-card: #fdfeff;
  --color-tvt07-card: oklch(0.997 0.003 230);
  --color-tvt07-rail: #f1f9fd;
  --color-tvt07-rail: oklch(0.977 0.01 230);
  --color-tvt07-ink: #091c2c;
  --color-tvt07-ink: oklch(0.22 0.04 245);
  --color-tvt07-mut: #4d6070;
  --color-tvt07-mut: oklch(0.48 0.035 245);
  --color-tvt07-line: #d5e4ed;
  --color-tvt07-line: oklch(0.91 0.02 235);
  --color-tvt07-acc: #007db3;
  --color-tvt07-acc: oklch(0.56 0.15 237);
  --color-tvt07-acc2: #1e59cd;
  --color-tvt07-acc2: oklch(0.5 0.19 262);
  --color-tvt07-acc-ink: #005f98;
  --color-tvt07-acc-ink: oklch(0.47 0.14 245);
  --color-tvt07-hl: #0086b1;
  --color-tvt07-hl: oklch(0.58 0.15 230);
  --color-tvt07-hl2: #2955d3;
  --color-tvt07-hl2: oklch(0.5 0.2 265);
  --color-tvt07-ring: #0077bc;
  --color-tvt07-ring: oklch(0.55 0.16 245);
  --color-tvt07-ok: #008a5a;
  --color-tvt07-ok: oklch(0.56 0.14 160);
  --color-tvt07-code: #091725;
  --color-tvt07-code: oklch(0.2 0.035 250);
  --color-tvt07-code-ink: #dfe9f1;
  --color-tvt07-code-ink: oklch(0.93 0.015 240);
  --color-tvt07-code-mut: #96a7b7;
  --color-tvt07-code-mut: oklch(0.72 0.03 245);
  --color-tvt07-code-k: #59c5f5;
  --color-tvt07-code-k: oklch(0.78 0.12 230);
  --color-tvt07-code-s: #8fe1a1;
  --color-tvt07-code-s: oklch(0.84 0.12 150);
  --color-tvt07-code-ok: #59e0ad;
  --color-tvt07-code-ok: oklch(0.82 0.14 165);
  --font-tvt07-sans: 'Manrope', system-ui, sans-serif;
  --font-tvt07-mono: 'Source Code Pro', ui-monospace, monospace;
  --shadow-tvt07-card: 0 1px 2px oklch(0.3 0.06 245 / 0.06), 0 30px 70px -30px oklch(0.4 0.14 240 / 0.38);
  --shadow-tvt07-dot: 0 8px 18px -8px oklch(0.5 0.17 245 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.25);
  --shadow-tvt07-code: 0 18px 40px -24px oklch(0.2 0.08 250 / 0.6);
  --animate-tvt07-in: tvt07-in 0.34s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tvt07-in {
    from {
      opacity: 0;
      translate: 0 8px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-07 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-07:not([data-theme="light"]) {
    --color-tvt07-bg: #02101c;
    --color-tvt07-bg: oklch(0.165 0.035 245);
    --color-tvt07-glow: #003c4d80;
    --color-tvt07-glow: oklch(0.33 0.09 225 / 0.5);
    --color-tvt07-glow2: #0b2b5f73;
    --color-tvt07-glow2: oklch(0.3 0.1 260 / 0.45);
    --color-tvt07-card: #061928;
    --color-tvt07-card: oklch(0.205 0.04 245);
    --color-tvt07-rail: #041422;
    --color-tvt07-rail: oklch(0.185 0.037 245);
    --color-tvt07-ink: #eaf3f9;
    --color-tvt07-ink: oklch(0.96 0.012 235);
    --color-tvt07-mut: #9eb5c5;
    --color-tvt07-mut: oklch(0.76 0.035 240);
    --color-tvt07-line: #1b354b;
    --color-tvt07-line: oklch(0.32 0.05 245);
    --color-tvt07-acc: #0092c5;
    --color-tvt07-acc: oklch(0.62 0.15 232);
    --color-tvt07-acc2: #245fd4;
    --color-tvt07-acc2: oklch(0.52 0.19 262);
    --color-tvt07-acc-ink: #6fd2fc;
    --color-tvt07-acc-ink: oklch(0.82 0.11 228);
    --color-tvt07-hl: #59d6fa;
    --color-tvt07-hl: oklch(0.82 0.12 220);
    --color-tvt07-hl2: #8bafff;
    --color-tvt07-hl2: oklch(0.76 0.14 265);
    --color-tvt07-ring: #4bc6fa;
    --color-tvt07-ring: oklch(0.78 0.13 230);
    --color-tvt07-ok: #009f68;
    --color-tvt07-ok: oklch(0.62 0.15 160);
    --color-tvt07-code: #020a15;
    --color-tvt07-code: oklch(0.14 0.03 250);
  }
}

.tvt-07[data-theme="dark"] {
  --color-tvt07-bg: #02101c;
  --color-tvt07-bg: oklch(0.165 0.035 245);
  --color-tvt07-glow: #003c4d80;
  --color-tvt07-glow: oklch(0.33 0.09 225 / 0.5);
  --color-tvt07-glow2: #0b2b5f73;
  --color-tvt07-glow2: oklch(0.3 0.1 260 / 0.45);
  --color-tvt07-card: #061928;
  --color-tvt07-card: oklch(0.205 0.04 245);
  --color-tvt07-rail: #041422;
  --color-tvt07-rail: oklch(0.185 0.037 245);
  --color-tvt07-ink: #eaf3f9;
  --color-tvt07-ink: oklch(0.96 0.012 235);
  --color-tvt07-mut: #9eb5c5;
  --color-tvt07-mut: oklch(0.76 0.035 240);
  --color-tvt07-line: #1b354b;
  --color-tvt07-line: oklch(0.32 0.05 245);
  --color-tvt07-acc: #0092c5;
  --color-tvt07-acc: oklch(0.62 0.15 232);
  --color-tvt07-acc2: #245fd4;
  --color-tvt07-acc2: oklch(0.52 0.19 262);
  --color-tvt07-acc-ink: #6fd2fc;
  --color-tvt07-acc-ink: oklch(0.82 0.11 228);
  --color-tvt07-hl: #59d6fa;
  --color-tvt07-hl: oklch(0.82 0.12 220);
  --color-tvt07-hl2: #8bafff;
  --color-tvt07-hl2: oklch(0.76 0.14 265);
  --color-tvt07-ring: #4bc6fa;
  --color-tvt07-ring: oklch(0.78 0.13 230);
  --color-tvt07-ok: #009f68;
  --color-tvt07-ok: oklch(0.62 0.15 160);
  --color-tvt07-code: #020a15;
  --color-tvt07-code: oklch(0.14 0.03 250);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-07-guide');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const list = root.querySelector('[role="tablist"]');
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const select = (tab, focus) => {
    const at = tabs.indexOf(tab);
    tabs.forEach((t, i) => {
      const on = i === at;
      t.setAttribute('aria-selected', String(on));
      t.toggleAttribute('data-done', i < at);
      if (on) t.removeAttribute('tabindex'); else t.tabIndex = -1;
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    });
    root.dataset.step = String(at + 1);
    if (focus) tab.focus();
  };
  list.addEventListener('click', (e) => { const t = e.target.closest('[role="tab"]'); if (t) select(t); });
  list.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const to = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (to === undefined || i < 0) return;
    e.preventDefault();
    select(tabs[(to + tabs.length) % tabs.length], true);
  });
  root.querySelectorAll('[data-goto]').forEach((b) => b.addEventListener('click', () => select(document.getElementById(b.dataset.goto), true)));
  root.querySelectorAll('[data-copy]').forEach((b) => b.addEventListener('click', () => {
    const text = document.getElementById(b.dataset.copy).textContent.replace(/^\$ /gm, '');
    const done = () => { b.setAttribute('data-copied', ''); setTimeout(() => b.removeAttribute('data-copied'), 1600); };
    const pick = () => { const r = document.createRange(); r.selectNodeContents(document.getElementById(b.dataset.copy)); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, pick); else pick();
  }));
})();
```
