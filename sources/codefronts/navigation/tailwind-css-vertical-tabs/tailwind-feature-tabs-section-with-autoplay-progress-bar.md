---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-feature-tabs-section-with-autoplay-progress-bar/"
title: "Tailwind Feature Tabs Section with Autoplay Progress Bar"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A SaaS landing-page section where three feature tabs auto-advance while a gradient progress bar fills beside the active one, and each tab swaps a fully drawn…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Tabs Section with Autoplay Progress Bar
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-feature-tabs-section-with-autoplay-progress-bar/

A SaaS landing-page section where three feature tabs auto-advance while a gradient progress bar fills beside the active one, and each tab swaps a fully drawn product scene &mdash; a preview deploy, an edge-network globe, a trace waterfall. The script writes one attribute, data-state="playing|paused|stopped"; utilities like group-aria-selected/tab:group-data-[state=playing]/sc:animate-tvt12-fill run the bar, and the bar's own animationend is the timer. Hover, focus, click and reduced motion all pause or stop it, as WCAG 2.2.2 requires.
## HTML
```html
<section class="tvt-12 w-full min-h-svh grid place-items-center overflow-hidden bg-tvt12-bg bg-[radial-gradient(55%_45%_at_15%_0%,var(--color-tvt12-glow),transparent_70%),radial-gradient(50%_50%_at_100%_100%,var(--color-tvt12-glow2),transparent_70%)] px-4 py-16 font-tvt12-sans text-tvt12-ink antialiased sm:px-6" aria-label="Tailwind feature tabs section with autoplay progress bar demo">
  <div id="tvt-12-showcase" class="group/sc @container grid w-full max-w-[72rem] gap-10">
    <div class="grid items-center gap-10 grid-cols-[minmax(0,26rem)_minmax(0,1fr)] @max-[54rem]:grid-cols-1">
      <div class="grid content-start gap-7 starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
        <div class="grid gap-4">
          <p class="inline-flex items-center gap-2 justify-self-start rounded-full bg-tvt12-card px-3 py-1.5 font-tvt12-mono text-[11.5px] tracking-[0.06em] text-tvt12-acc-ink ring-1 ring-tvt12-line uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt12-acc2 shadow-[0_0_8px] shadow-tvt12-acc2"></span>Why teams switch</p>
          <h2 class="text-[clamp(32px,4.6vw,50px)] leading-[1.02] font-bold tracking-[-0.045em] text-balance">Ship the whole pipeline, <span class="bg-linear-to-r from-tvt12-hl to-tvt12-hl2 bg-clip-text pe-1 text-transparent">not just the demo</span></h2>
          <p class="max-w-[40ch] text-[16px] leading-relaxed text-tvt12-mut text-pretty">Previews, global delivery and production telemetry in one platform. Pick a feature &mdash; or let it play.</p>
        </div>
        <div role="tablist" aria-orientation="vertical" aria-label="Product features" class="grid gap-1.5">

          <button type="button" role="tab" id="tvt-12-tab1" aria-controls="tvt-12-panel1" aria-selected="true" class="group/tab relative grid min-h-11 w-full cursor-pointer grid-cols-[auto_minmax(0,1fr)] items-start gap-x-3.5 rounded-2xl py-4 ps-6 pe-4 text-start transition-[background-color,box-shadow] duration-300 hover:bg-tvt12-card/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt12-ring aria-selected:bg-tvt12-card aria-selected:shadow-tvt12-tab motion-reduce:transition-none">
            <span aria-hidden="true" class="absolute inset-y-4 start-2.5 w-[3px] overflow-hidden rounded-full bg-tvt12-line"><span data-fill class="block size-full origin-top scale-y-0 rounded-full bg-linear-to-b from-tvt12-acc to-tvt12-acc2 group-aria-selected/tab:scale-y-100 group-aria-selected/tab:group-data-[state=playing]/sc:animate-tvt12-fill group-aria-selected/tab:group-data-[state=paused]/sc:animate-tvt12-fill group-data-[state=paused]/sc:[animation-play-state:paused]"></span></span>
            <span aria-hidden="true" class="grid size-10 place-items-center rounded-xl bg-tvt12-ink/[0.05] text-tvt12-mut ring-1 ring-tvt12-line transition-colors duration-300 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt12-acc group-aria-selected/tab:to-tvt12-acc2 group-aria-selected/tab:text-tvt12-on group-aria-selected/tab:ring-transparent"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M11 2 4.5 11H10l-1 7 6.5-9H10Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
            <span class="grid">
              <span class="pt-2 text-[16.5px] font-semibold tracking-[-0.015em] text-tvt12-mut transition-colors group-hover/tab:text-tvt12-ink group-aria-selected/tab:text-tvt12-ink">Instant previews</span>
              <span class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-aria-selected/tab:grid-rows-[1fr] motion-reduce:transition-none"><span class="overflow-hidden"><span class="block pt-1.5 text-[14.5px] leading-relaxed text-tvt12-mut text-pretty">Every branch gets a shareable, production-identical URL in under nine seconds &mdash; reviewers comment right on the page.</span></span></span>
            </span>
          </button>

          <button type="button" role="tab" id="tvt-12-tab2" aria-controls="tvt-12-panel2" aria-selected="false" tabindex="-1" class="group/tab relative grid min-h-11 w-full cursor-pointer grid-cols-[auto_minmax(0,1fr)] items-start gap-x-3.5 rounded-2xl py-4 ps-6 pe-4 text-start transition-[background-color,box-shadow] duration-300 hover:bg-tvt12-card/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt12-ring aria-selected:bg-tvt12-card aria-selected:shadow-tvt12-tab motion-reduce:transition-none">
            <span aria-hidden="true" class="absolute inset-y-4 start-2.5 w-[3px] overflow-hidden rounded-full bg-tvt12-line"><span data-fill class="block size-full origin-top scale-y-0 rounded-full bg-linear-to-b from-tvt12-acc to-tvt12-acc2 group-aria-selected/tab:scale-y-100 group-aria-selected/tab:group-data-[state=playing]/sc:animate-tvt12-fill group-aria-selected/tab:group-data-[state=paused]/sc:animate-tvt12-fill group-data-[state=paused]/sc:[animation-play-state:paused]"></span></span>
            <span aria-hidden="true" class="grid size-10 place-items-center rounded-xl bg-tvt12-ink/[0.05] text-tvt12-mut ring-1 ring-tvt12-line transition-colors duration-300 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt12-acc group-aria-selected/tab:to-tvt12-acc2 group-aria-selected/tab:text-tvt12-on group-aria-selected/tab:ring-transparent"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2.5 10h15M10 2.5c2.2 2.2 3 4.8 3 7.5s-.8 5.3-3 7.5c-2.2-2.2-3-4.8-3-7.5s.8-5.3 3-7.5Z" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
            <span class="grid">
              <span class="pt-2 text-[16.5px] font-semibold tracking-[-0.015em] text-tvt12-mut transition-colors group-hover/tab:text-tvt12-ink group-aria-selected/tab:text-tvt12-ink">Edge everywhere</span>
              <span class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-aria-selected/tab:grid-rows-[1fr] motion-reduce:transition-none"><span class="overflow-hidden"><span class="block pt-1.5 text-[14.5px] leading-relaxed text-tvt12-mut text-pretty">318 regions, one deploy, no config file. Requests are served from the closest city, with p95 under 45ms.</span></span></span>
            </span>
          </button>

          <button type="button" role="tab" id="tvt-12-tab3" aria-controls="tvt-12-panel3" aria-selected="false" tabindex="-1" class="group/tab relative grid min-h-11 w-full cursor-pointer grid-cols-[auto_minmax(0,1fr)] items-start gap-x-3.5 rounded-2xl py-4 ps-6 pe-4 text-start transition-[background-color,box-shadow] duration-300 hover:bg-tvt12-card/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt12-ring aria-selected:bg-tvt12-card aria-selected:shadow-tvt12-tab motion-reduce:transition-none">
            <span aria-hidden="true" class="absolute inset-y-4 start-2.5 w-[3px] overflow-hidden rounded-full bg-tvt12-line"><span data-fill class="block size-full origin-top scale-y-0 rounded-full bg-linear-to-b from-tvt12-acc to-tvt12-acc2 group-aria-selected/tab:scale-y-100 group-aria-selected/tab:group-data-[state=playing]/sc:animate-tvt12-fill group-aria-selected/tab:group-data-[state=paused]/sc:animate-tvt12-fill group-data-[state=paused]/sc:[animation-play-state:paused]"></span></span>
            <span aria-hidden="true" class="grid size-10 place-items-center rounded-xl bg-tvt12-ink/[0.05] text-tvt12-mut ring-1 ring-tvt12-line transition-colors duration-300 group-aria-selected/tab:bg-linear-to-br group-aria-selected/tab:from-tvt12-acc group-aria-selected/tab:to-tvt12-acc2 group-aria-selected/tab:text-tvt12-on group-aria-selected/tab:ring-transparent"><svg viewBox="0 0 20 20" width="18" height="18" focusable="false"><path d="M2.5 10h3l2-5 3.5 10 2-5h4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="grid">
              <span class="pt-2 text-[16.5px] font-semibold tracking-[-0.015em] text-tvt12-mut transition-colors group-hover/tab:text-tvt12-ink group-aria-selected/tab:text-tvt12-ink">Observability built in</span>
              <span class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-aria-selected/tab:grid-rows-[1fr] motion-reduce:transition-none"><span class="overflow-hidden"><span class="block pt-1.5 text-[14.5px] leading-relaxed text-tvt12-mut text-pretty">Traces, logs and Core Web Vitals on one timeline, so a slow query and the INP regression it caused sit side by side.</span></span></span>
            </span>
          </button>
        </div>
        <div class="flex items-center gap-3 ps-2">
          <button type="button" data-autoplay aria-pressed="false" class="group/ap inline-flex min-h-11 items-center gap-2 rounded-full px-3.5 text-[13px] font-semibold text-tvt12-mut ring-1 ring-tvt12-line transition-colors hover:bg-tvt12-card hover:text-tvt12-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt12-ring">
            <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true" focusable="false" class="group-aria-pressed/ap:hidden"><path d="M5 3.5v9M11 3.5v9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true" focusable="false" class="hidden group-aria-pressed/ap:block"><path d="M5 3.2v9.6L12.5 8Z" fill="currentColor"/></svg>
            <span class="group-aria-pressed/ap:hidden">Pause autoplay</span><span class="hidden group-aria-pressed/ap:inline">Play autoplay</span>
          </button>
          <p class="text-[12.5px] text-tvt12-mut"><span class="group-data-[state=paused]/sc:hidden group-data-[state=stopped]/sc:hidden">Advancing every 6s</span><span class="hidden group-data-[state=paused]/sc:inline">Paused while you look</span><span class="hidden group-data-[state=stopped]/sc:inline">Autoplay off</span></p>
        </div>
      </div>

      <div class="relative grid">
        <div aria-hidden="true" class="absolute -inset-6 -z-0 rounded-[40px] bg-linear-to-br from-tvt12-acc/25 via-transparent to-tvt12-acc2/25 blur-3xl"></div>

        <div role="tabpanel" id="tvt-12-panel1" aria-labelledby="tvt-12-tab1" tabindex="0" aria-label="Instant previews scene" class="relative col-start-1 row-start-1 rounded-[20px] transition-[opacity,translate,scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt12-ring starting:translate-y-3 starting:scale-[.985] starting:opacity-0 motion-reduce:transition-none">
          <div class="overflow-hidden rounded-[20px] bg-tvt12-scr text-tvt12-sink shadow-tvt12-window ring-1 ring-white/10">
            <div class="flex items-center gap-3 border-b border-white/[0.08] px-4 py-3">
              <span aria-hidden="true" class="flex gap-1.5"><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i></span>
              <span class="mx-auto flex min-w-0 items-center gap-2 rounded-lg bg-white/[0.06] px-3 py-1 font-tvt12-mono text-[11.5px] text-tvt12-smut"><svg viewBox="0 0 16 16" width="11" height="11" aria-hidden="true" focusable="false" class="shrink-0"><rect x="3.5" y="7" width="9" height="6.5" rx="1.5" fill="currentColor"/><path d="M5.5 7V5.5a2.5 2.5 0 0 1 5 0V7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg><span class="truncate">feat-checkout-git-acme.app</span></span>
              <span aria-hidden="true" class="w-[46px]"></span>
            </div>
            <div class="grid gap-4 p-5 sm:grid-cols-[1.1fr_1fr] sm:p-6">
              <div class="grid content-start gap-3">
                <p class="flex items-center gap-2 text-[13px] font-semibold text-white"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false"><circle cx="4" cy="3.5" r="1.8" fill="none" stroke="currentColor" stroke-width="1.4"/><circle cx="4" cy="12.5" r="1.8" fill="none" stroke="currentColor" stroke-width="1.4"/><circle cx="12" cy="6" r="1.8" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M4 5.3v5.4M12 7.8c0 2.6-3 2.4-6.5 3.6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>feat/checkout-v2 <span class="font-tvt12-mono text-[11px] font-normal text-tvt12-smut">#412</span></p>
                <ol class="grid gap-2 font-tvt12-mono text-[12px]">
                  <li class="flex items-center gap-2.5 rounded-lg bg-white/[0.04] px-3 py-2"><span aria-hidden="true" class="grid size-4 place-items-center rounded-full bg-tvt12-sok/20 text-tvt12-sok">✓</span>Install<span class="ms-auto text-tvt12-smut">1.2s</span></li>
                  <li class="flex items-center gap-2.5 rounded-lg bg-white/[0.04] px-3 py-2"><span aria-hidden="true" class="grid size-4 place-items-center rounded-full bg-tvt12-sok/20 text-tvt12-sok">✓</span>Build<span class="ms-auto text-tvt12-smut">5.9s</span></li>
                  <li class="flex items-center gap-2.5 rounded-lg bg-white/[0.04] px-3 py-2"><span aria-hidden="true" class="grid size-4 place-items-center rounded-full bg-tvt12-sok/20 text-tvt12-sok">✓</span>Deploy to edge<span class="ms-auto text-tvt12-smut">1.3s</span></li>
                </ol>
                <p class="mt-1 inline-flex items-center gap-2 justify-self-start rounded-full bg-linear-to-r from-tvt12-sacc/20 to-tvt12-sacc2/20 px-3 py-1.5 text-[12.5px] font-semibold text-white ring-1 ring-tvt12-sacc2/40"><span aria-hidden="true" class="size-2 rounded-full bg-tvt12-sacc2 shadow-[0_0_10px] shadow-tvt12-sacc2 motion-safe:animate-tvt12-pulse"></span>Preview ready · 8.4s</p>
              </div>
              <div aria-hidden="true" class="overflow-hidden rounded-xl bg-white p-3 text-[oklch(0.3_0.03_250)] shadow-lg">
                <div class="flex items-center justify-between"><span class="h-2 w-14 rounded-full bg-[oklch(0.3_0.03_250)]"></span><span class="flex gap-1.5"><i class="h-1.5 w-6 rounded-full bg-[oklch(0.85_0.01_250)]"></i><i class="h-1.5 w-6 rounded-full bg-[oklch(0.85_0.01_250)]"></i></span></div>
                <div class="mt-3 grid grid-cols-[1fr_auto] gap-3">
                  <div class="grid gap-2"><span class="h-2 rounded-full bg-[oklch(0.88_0.01_250)]"></span><span class="h-2 w-4/5 rounded-full bg-[oklch(0.88_0.01_250)]"></span><span class="mt-1 h-10 rounded-lg bg-[oklch(0.95_0.01_250)] ring-1 ring-[oklch(0.9_0.01_250)]"></span><span class="h-10 rounded-lg bg-[oklch(0.95_0.01_250)] ring-1 ring-[oklch(0.9_0.01_250)]"></span></div>
                  <div class="grid w-20 content-start gap-2 rounded-lg bg-[oklch(0.96_0.02_200)] p-2"><span class="h-1.5 rounded-full bg-[oklch(0.8_0.03_220)]"></span><span class="h-1.5 w-2/3 rounded-full bg-[oklch(0.8_0.03_220)]"></span><span class="mt-2 h-5 rounded-md bg-linear-to-r from-[oklch(0.62_0.13_210)] to-[oklch(0.68_0.17_150)]"></span></div>
                </div>
              </div>
            </div>
            <div class="flex flex-wrap items-center gap-x-5 gap-y-1 border-t border-white/[0.08] px-5 py-3 font-tvt12-mono text-[11.5px] text-tvt12-smut sm:px-6"><span>3 reviewers</span><span>2 comments on preview</span><span class="ms-auto text-tvt12-sok">All checks passed</span></div>
          </div>
        </div>

        <div role="tabpanel" id="tvt-12-panel2" aria-labelledby="tvt-12-tab2" tabindex="0" aria-label="Edge everywhere scene" hidden class="relative col-start-1 row-start-1 rounded-[20px] transition-[opacity,translate,scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt12-ring starting:translate-y-3 starting:scale-[.985] starting:opacity-0 motion-reduce:transition-none">
          <div class="overflow-hidden rounded-[20px] bg-tvt12-scr text-tvt12-sink shadow-tvt12-window ring-1 ring-white/10">
            <div class="flex items-center gap-3 border-b border-white/[0.08] px-4 py-3">
              <span aria-hidden="true" class="flex gap-1.5"><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i></span>
              <span class="mx-auto flex min-w-0 items-center gap-2 rounded-lg bg-white/[0.06] px-3 py-1 font-tvt12-mono text-[11.5px] text-tvt12-smut"><svg viewBox="0 0 16 16" width="11" height="11" aria-hidden="true" focusable="false" class="shrink-0"><rect x="3.5" y="7" width="9" height="6.5" rx="1.5" fill="currentColor"/><path d="M5.5 7V5.5a2.5 2.5 0 0 1 5 0V7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg><span class="truncate">acme.app/regions</span></span>
              <span aria-hidden="true" class="w-[46px]"></span>
            </div>
            <div class="grid items-center gap-4 p-5 sm:grid-cols-[1.25fr_1fr] sm:p-6">
              <svg viewBox="0 0 300 250" class="w-full" aria-hidden="true" focusable="false">
                <defs>
                  <radialGradient id="tvt-12-globe" cx="38%" cy="32%" r="75%"><stop offset="0" stop-color="oklch(0.42 0.1 230)"/><stop offset="1" stop-color="oklch(0.18 0.05 260)"/></radialGradient>
                  <linearGradient id="tvt-12-arc" x1="0" x2="1"><stop offset="0" stop-color="var(--color-tvt12-sacc)"/><stop offset="1" stop-color="var(--color-tvt12-sacc2)"/></linearGradient>
                  <clipPath id="tvt-12-clip"><circle cx="150" cy="125" r="105"/></clipPath>
                </defs>
                <circle cx="150" cy="125" r="118" fill="none" stroke="var(--color-tvt12-sacc)" stroke-opacity=".12" stroke-width="10"/>
                <circle cx="150" cy="125" r="105" fill="url(#tvt-12-globe)"/>
                <g clip-path="url(#tvt-12-clip)" fill="none" stroke="white" stroke-opacity=".12" stroke-width="1">
                  <ellipse cx="150" cy="125" rx="35" ry="105"/><ellipse cx="150" cy="125" rx="72" ry="105"/><ellipse cx="150" cy="125" rx="100" ry="105"/>
                  <path d="M45 125h210M55 80h190M55 170h190M80 40h140M80 210h140"/>
                </g>
                <g clip-path="url(#tvt-12-clip)" fill="white" fill-opacity=".22">
                  <path d="M88 70c14-10 36-12 46-2 6 6-2 14 6 20s4 18-8 20c-10 2-14 12-24 10s-10-14-20-18-16-20 0-30Z"/>
                  <path d="M160 58c18-6 46-4 58 8 8 8-4 16 4 24 6 6 18 4 20 14 2 8-14 12-22 8-10-5-16 4-28 2s-10-12-20-14-20-6-18-18 2-20 6-24Z"/>
                  <path d="M118 140c10-4 24 2 26 12s-6 26-12 38c-4 8-14 6-16-4s-10-16-8-28 4-16 10-18Z"/>
                  <path d="M196 150c10-2 22 4 22 14s-12 16-20 12-14-6-12-14 4-11 10-12Z"/>
                </g>
                <g fill="none" stroke="url(#tvt-12-arc)" stroke-width="2" stroke-linecap="round" stroke-dasharray="6 8" class="motion-safe:animate-tvt12-dash">
                  <path d="M104 86Q150 30 196 80"/><path d="M196 80Q240 120 206 160"/><path d="M104 86Q90 140 128 160"/><path d="M128 160Q170 200 206 160"/>
                </g>
                <g fill="var(--color-tvt12-sacc2)">
                  <circle cx="104" cy="86" r="4"/><circle cx="196" cy="80" r="4"/><circle cx="128" cy="160" r="4"/><circle cx="206" cy="160" r="4"/><circle cx="150" cy="118" r="5" fill="white"/>
                </g>
                <g fill="none" stroke="var(--color-tvt12-sacc2)" stroke-width="1.5"><circle cx="150" cy="118" r="10" class="origin-[150px_118px] motion-safe:animate-tvt12-ring"/></g>
              </svg>
              <div class="grid gap-3">
                <p class="text-[13px] font-semibold text-white">Global latency <span class="font-tvt12-mono text-[11px] font-normal text-tvt12-smut">p95, last 24h</span></p>
                <ul class="grid gap-2 font-tvt12-mono text-[12px]">
                  <li class="grid gap-1"><span class="flex justify-between"><span>iad1 · Virginia</span><span class="text-white">28ms</span></span><span class="h-1.5 rounded-full bg-white/10"><span class="block h-full w-[30%] rounded-full bg-linear-to-r from-tvt12-sacc to-tvt12-sacc2"></span></span></li>
                  <li class="grid gap-1"><span class="flex justify-between"><span>lhr1 · London</span><span class="text-white">34ms</span></span><span class="h-1.5 rounded-full bg-white/10"><span class="block h-full w-[38%] rounded-full bg-linear-to-r from-tvt12-sacc to-tvt12-sacc2"></span></span></li>
                  <li class="grid gap-1"><span class="flex justify-between"><span>syd1 · Sydney</span><span class="text-white">41ms</span></span><span class="h-1.5 rounded-full bg-white/10"><span class="block h-full w-[46%] rounded-full bg-linear-to-r from-tvt12-sacc to-tvt12-sacc2"></span></span></li>
                  <li class="grid gap-1"><span class="flex justify-between"><span>yyz1 · Toronto</span><span class="text-white">31ms</span></span><span class="h-1.5 rounded-full bg-white/10"><span class="block h-full w-[34%] rounded-full bg-linear-to-r from-tvt12-sacc to-tvt12-sacc2"></span></span></li>
                </ul>
                <p class="mt-1 text-[12.5px] text-tvt12-smut"><b class="text-[20px] font-semibold tracking-[-0.02em] text-white tabular-nums">318</b> edge regions · one deploy</p>
              </div>
            </div>
          </div>
        </div>

        <div role="tabpanel" id="tvt-12-panel3" aria-labelledby="tvt-12-tab3" tabindex="0" aria-label="Observability scene" hidden class="relative col-start-1 row-start-1 rounded-[20px] transition-[opacity,translate,scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt12-ring starting:translate-y-3 starting:scale-[.985] starting:opacity-0 motion-reduce:transition-none">
          <div class="overflow-hidden rounded-[20px] bg-tvt12-scr text-tvt12-sink shadow-tvt12-window ring-1 ring-white/10">
            <div class="flex items-center gap-3 border-b border-white/[0.08] px-4 py-3">
              <span aria-hidden="true" class="flex gap-1.5"><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i><i class="size-2.5 rounded-full bg-white/20"></i></span>
              <span class="mx-auto flex min-w-0 items-center gap-2 rounded-lg bg-white/[0.06] px-3 py-1 font-tvt12-mono text-[11.5px] text-tvt12-smut"><svg viewBox="0 0 16 16" width="11" height="11" aria-hidden="true" focusable="false" class="shrink-0"><rect x="3.5" y="7" width="9" height="6.5" rx="1.5" fill="currentColor"/><path d="M5.5 7V5.5a2.5 2.5 0 0 1 5 0V7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg><span class="truncate">acme.app/observability/trace/9f2c</span></span>
              <span aria-hidden="true" class="w-[46px]"></span>
            </div>
            <div class="grid gap-4 p-5 sm:p-6">
              <div class="flex flex-wrap gap-2">
                <p class="flex items-center gap-2 rounded-xl bg-white/[0.05] px-3 py-2 text-[12px] ring-1 ring-white/10"><span aria-hidden="true" class="size-2 rounded-full bg-tvt12-sok"></span>LCP <b class="font-tvt12-mono text-white">1.1s</b></p>
                <p class="flex items-center gap-2 rounded-xl bg-white/[0.05] px-3 py-2 text-[12px] ring-1 ring-white/10"><span aria-hidden="true" class="size-2 rounded-full bg-tvt12-sok"></span>INP <b class="font-tvt12-mono text-white">86ms</b></p>
                <p class="flex items-center gap-2 rounded-xl bg-white/[0.05] px-3 py-2 text-[12px] ring-1 ring-white/10"><span aria-hidden="true" class="size-2 rounded-full bg-tvt12-sok"></span>CLS <b class="font-tvt12-mono text-white">0.00</b></p>
              </div>
              <div class="rounded-xl bg-black/25 p-4 ring-1 ring-white/[0.06]">
                <p class="flex justify-between font-tvt12-mono text-[11px] text-tvt12-smut"><span>GET /checkout</span><span>0 — 420ms</span></p>
                <ol class="mt-3 grid gap-2 font-tvt12-mono text-[11.5px]">
                <li class="grid grid-cols-[6.5rem_minmax(0,1fr)] items-center gap-3"><span class="truncate">edge.request</span><span class="relative h-5"><span class="absolute inset-y-0 flex items-center rounded-md bg-tvt12-sacc px-1.5 text-[10.5px] font-medium text-[oklch(0.18_0.04_250)] start-[0%] w-[100%]">420ms</span></span></li>
                <li class="grid grid-cols-[6.5rem_minmax(0,1fr)] items-center gap-3"><span class="truncate">auth.session</span><span class="relative h-5"><span class="absolute inset-y-0 flex items-center rounded-md bg-[oklch(0.8_0.12_280)] px-1.5 text-[10.5px] font-medium text-[oklch(0.18_0.04_250)] start-[4%] w-[18%]">74</span></span></li>
                <li class="grid grid-cols-[6.5rem_minmax(0,1fr)] items-center gap-3"><span class="truncate">db.cart.query</span><span class="relative h-5"><span class="absolute inset-y-0 flex items-center rounded-md bg-tvt12-sacc2 px-1.5 text-[10.5px] font-medium text-[oklch(0.18_0.04_250)] start-[22%] w-[34%]">142ms</span></span></li>
                <li class="grid grid-cols-[6.5rem_minmax(0,1fr)] items-center gap-3"><span class="truncate">pricing.api</span><span class="relative h-5"><span class="absolute inset-y-0 flex items-center rounded-md bg-[oklch(0.85_0.13_85)] px-1.5 text-[10.5px] font-medium text-[oklch(0.18_0.04_250)] start-[30%] w-[22%]">96</span></span></li>
                <li class="grid grid-cols-[6.5rem_minmax(0,1fr)] items-center gap-3"><span class="truncate">render.ssr</span><span class="relative h-5"><span class="absolute inset-y-0 flex items-center rounded-md bg-[oklch(0.8_0.12_330)] px-1.5 text-[10.5px] font-medium text-[oklch(0.18_0.04_250)] start-[58%] w-[38%]">160ms</span></span></li>
                </ol>
              </div>
              <p class="font-tvt12-mono text-[11.5px] text-tvt12-smut"><span class="text-tvt12-sok">▲ 31%</span> faster than last release · 2.4M sessions sampled</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt12-bg: #eef8fc;
  --color-tvt12-bg: oklch(0.972 0.012 230);
  --color-tvt12-glow: #96e7f1a6;
  --color-tvt12-glow: oklch(0.88 0.08 205 / 0.65);
  --color-tvt12-glow2: #b7f0ab8c;
  --color-tvt12-glow2: oklch(0.9 0.11 140 / 0.55);
  --color-tvt12-card: #feffff;
  --color-tvt12-card: oklch(0.998 0.003 230);
  --color-tvt12-ink: #0b1b2f;
  --color-tvt12-ink: oklch(0.22 0.045 255);
  --color-tvt12-mut: #4a5d71;
  --color-tvt12-mut: oklch(0.47 0.04 250);
  --color-tvt12-line: #d3e0ea;
  --color-tvt12-line: oklch(0.9 0.02 240);
  --color-tvt12-acc: #0090a8;
  --color-tvt12-acc: oklch(0.6 0.13 215);
  --color-tvt12-acc2: #35ad44;
  --color-tvt12-acc2: oklch(0.66 0.18 145);
  --color-tvt12-acc-ink: #005f75;
  --color-tvt12-acc-ink: oklch(0.45 0.1 220);
  --color-tvt12-on: #03172c;
  --color-tvt12-on: oklch(0.2 0.05 250);
  --color-tvt12-hl: #007e9a;
  --color-tvt12-hl: oklch(0.55 0.13 220);
  --color-tvt12-hl2: #009342;
  --color-tvt12-hl2: oklch(0.58 0.17 150);
  --color-tvt12-ring: #007e9a;
  --color-tvt12-ring: oklch(0.55 0.13 220);
  --color-tvt12-scr: #09162a;
  --color-tvt12-scr: oklch(0.2 0.045 260);
  --color-tvt12-sink: #c6d3dd;
  --color-tvt12-sink: oklch(0.86 0.02 240);
  --color-tvt12-smut: #94a8b6;
  --color-tvt12-smut: oklch(0.72 0.03 240);
  --color-tvt12-sacc: #2ad5e5;
  --color-tvt12-sacc: oklch(0.8 0.13 205);
  --color-tvt12-sacc2: #9ef269;
  --color-tvt12-sacc2: oklch(0.88 0.19 135);
  --color-tvt12-sok: #5ee295;
  --color-tvt12-sok: oklch(0.82 0.16 155);
  --font-tvt12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tvt12-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tvt12-tab: 0 1px 2px oklch(0.3 0.05 250 / 0.08), 0 18px 40px -22px oklch(0.4 0.12 220 / 0.45), inset 0 0 0 1px oklch(0.6 0.1 220 / 0.12);
  --shadow-tvt12-window: 0 40px 90px -40px oklch(0.2 0.1 250 / 0.75), 0 2px 6px oklch(0.2 0.05 250 / 0.25);
  --animate-tvt12-fill: tvt12-fill 6s linear both;
  --animate-tvt12-pulse: tvt12-pulse 1.8s ease-in-out infinite;
  --animate-tvt12-dash: tvt12-dash 1.6s linear infinite;
  --animate-tvt12-ring: tvt12-ring 2.4s cubic-bezier(0.16, 1, 0.3, 1) infinite;

  @keyframes tvt12-fill {
    from {
      scale: 1 0;
    }

    to {
      scale: 1 1;
    }
  }

  @keyframes tvt12-pulse {
    50% {
      opacity: 0.45;
    }
  }

  @keyframes tvt12-dash {
    to {
      stroke-dashoffset: -28;
    }
  }

  @keyframes tvt12-ring {
    from {
      scale: 0.6;
      opacity: 1;
    }

    to {
      scale: 2.6;
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-12 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-12:not([data-theme="light"]) {
    --color-tvt12-bg: #040b1d;
    --color-tvt12-bg: oklch(0.155 0.04 262);
    --color-tvt12-glow: #003f4b80;
    --color-tvt12-glow: oklch(0.34 0.09 215 / 0.5);
    --color-tvt12-glow2: #013f0b59;
    --color-tvt12-glow2: oklch(0.32 0.1 145 / 0.35);
    --color-tvt12-card: #0a182d;
    --color-tvt12-card: oklch(0.21 0.045 258);
    --color-tvt12-ink: #ecf5fa;
    --color-tvt12-ink: oklch(0.965 0.012 230);
    --color-tvt12-mut: #9eb5c5;
    --color-tvt12-mut: oklch(0.76 0.035 240);
    --color-tvt12-line: #21344c;
    --color-tvt12-line: oklch(0.32 0.05 255);
    --color-tvt12-acc: #2ad5e5;
    --color-tvt12-acc: oklch(0.8 0.13 205);
    --color-tvt12-acc2: #9ef269;
    --color-tvt12-acc2: oklch(0.88 0.19 135);
    --color-tvt12-acc-ink: #6ce7ed;
    --color-tvt12-acc-ink: oklch(0.86 0.11 200);
    --color-tvt12-on: #021127;
    --color-tvt12-on: oklch(0.18 0.05 255);
    --color-tvt12-hl: #55e1f0;
    --color-tvt12-hl: oklch(0.84 0.12 205);
    --color-tvt12-hl2: #a8f878;
    --color-tvt12-hl2: oklch(0.9 0.18 135);
    --color-tvt12-ring: #3fe4ec;
    --color-tvt12-ring: oklch(0.84 0.13 200);
    --color-tvt12-scr: #071125;
    --color-tvt12-scr: oklch(0.18 0.045 262);
    --color-tvt12-sink: #c6d3dd;
    --color-tvt12-sink: oklch(0.86 0.02 240);
    --color-tvt12-smut: #94a8b6;
    --color-tvt12-smut: oklch(0.72 0.03 240);
    --color-tvt12-sacc: #2ad5e5;
    --color-tvt12-sacc: oklch(0.8 0.13 205);
    --color-tvt12-sacc2: #9ef269;
    --color-tvt12-sacc2: oklch(0.88 0.19 135);
    --color-tvt12-sok: #5ee295;
    --color-tvt12-sok: oklch(0.82 0.16 155);
  }
}

.tvt-12[data-theme="dark"] {
  --color-tvt12-bg: #040b1d;
  --color-tvt12-bg: oklch(0.155 0.04 262);
  --color-tvt12-glow: #003f4b80;
  --color-tvt12-glow: oklch(0.34 0.09 215 / 0.5);
  --color-tvt12-glow2: #013f0b59;
  --color-tvt12-glow2: oklch(0.32 0.1 145 / 0.35);
  --color-tvt12-card: #0a182d;
  --color-tvt12-card: oklch(0.21 0.045 258);
  --color-tvt12-ink: #ecf5fa;
  --color-tvt12-ink: oklch(0.965 0.012 230);
  --color-tvt12-mut: #9eb5c5;
  --color-tvt12-mut: oklch(0.76 0.035 240);
  --color-tvt12-line: #21344c;
  --color-tvt12-line: oklch(0.32 0.05 255);
  --color-tvt12-acc: #2ad5e5;
  --color-tvt12-acc: oklch(0.8 0.13 205);
  --color-tvt12-acc2: #9ef269;
  --color-tvt12-acc2: oklch(0.88 0.19 135);
  --color-tvt12-acc-ink: #6ce7ed;
  --color-tvt12-acc-ink: oklch(0.86 0.11 200);
  --color-tvt12-on: #021127;
  --color-tvt12-on: oklch(0.18 0.05 255);
  --color-tvt12-hl: #55e1f0;
  --color-tvt12-hl: oklch(0.84 0.12 205);
  --color-tvt12-hl2: #a8f878;
  --color-tvt12-hl2: oklch(0.9 0.18 135);
  --color-tvt12-ring: #3fe4ec;
  --color-tvt12-ring: oklch(0.84 0.13 200);
  --color-tvt12-scr: #071125;
  --color-tvt12-scr: oklch(0.18 0.045 262);
  --color-tvt12-sink: #c6d3dd;
  --color-tvt12-sink: oklch(0.86 0.02 240);
  --color-tvt12-smut: #94a8b6;
  --color-tvt12-smut: oklch(0.72 0.03 240);
  --color-tvt12-sacc: #2ad5e5;
  --color-tvt12-sacc: oklch(0.8 0.13 205);
  --color-tvt12-sacc2: #9ef269;
  --color-tvt12-sacc2: oklch(0.88 0.19 135);
  --color-tvt12-sok: #5ee295;
  --color-tvt12-sok: oklch(0.82 0.16 155);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-12-showcase');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const tabs = [...root.querySelectorAll('[role="tab"]')];
  const toggle = root.querySelector('[data-autoplay]');
  let stopped = matchMedia('(prefers-reduced-motion: reduce)').matches, held = false, onScreen = true;
  // One attribute drives every visual: playing | paused | stopped. CSS owns the 6s timer.
  const sync = () => {
    root.dataset.state = stopped ? 'stopped' : (held || !onScreen) ? 'paused' : 'playing';
    toggle.setAttribute('aria-pressed', String(stopped));
  };
  const select = (tab, focus) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  };
  const stop = () => { stopped = true; sync(); };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => { stop(); select(t); });
    // The progress fill finishing IS the timer: no setInterval to drift out of sync with a paused bar.
    t.querySelector('[data-fill]').addEventListener('animationend', () => {
      if (root.dataset.state === 'playing') select(tabs[(i + 1) % tabs.length]);
    });
  });
  root.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const to = { ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (i < 0 || to === undefined) return;
    e.preventDefault(); stop(); select(tabs[(to + tabs.length) % tabs.length], true);
  });
  toggle.addEventListener('click', () => { stopped = !stopped; sync(); });
  root.addEventListener('pointerenter', () => { held = true; sync(); });
  root.addEventListener('pointerleave', () => { held = root.contains(document.activeElement); sync(); });
  root.addEventListener('focusin', () => { held = true; sync(); });
  root.addEventListener('focusout', (e) => { if (!root.contains(e.relatedTarget)) { held = root.matches(':hover'); sync(); } });
  if ('IntersectionObserver' in window) new IntersectionObserver((es) => { onScreen = es[0].isIntersecting; sync(); }, { threshold: 0.35 }).observe(root);
  sync();
})();
```
