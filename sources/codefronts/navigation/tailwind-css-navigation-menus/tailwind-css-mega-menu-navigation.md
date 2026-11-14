---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-mega-menu-navigation/"
title: "Tailwind CSS Mega Menu Navigation"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A dark developer-platform header with a true mega panel: six icon-led product links in a two-column grid, a featured promo card, and a footer of release tags."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Mega Menu Navigation
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-mega-menu-navigation/

A dark developer-platform header with a true mega panel: six icon-led product links in a two-column grid, a featured promo card, and a footer of release tags. The panel anchors to the nav, not the menu item, so it is always centred and never clips off-screen. Opens on hover and keyboard focus. Zero JavaScript.
## HTML
```html
<div class="tnv-03 min-h-svh w-full bg-tnv03-bg bg-[radial-gradient(60%_50%_at_50%_0%,var(--color-tnv03-glow),transparent)] font-tnv03-sans text-tnv03-ink antialiased selection:bg-tnv03-acc selection:text-white">
  <header class="sticky top-0 z-30 border-b border-white/[0.07] bg-tnv03-surface/85 backdrop-blur-xl">
    <nav aria-label="Main" class="relative mx-auto flex h-[68px] max-w-6xl items-center justify-between gap-6 px-5 sm:px-10">
      <a href="#" class="text-xl font-bold tracking-[-0.02em]">Arc<span class="text-tnv03-acc">OS</span></a>
      <ul class="hidden items-center gap-0.5 md:flex">
        <li class="group/mm static">
          <button type="button" aria-haspopup="true" class="flex h-11 items-center gap-1.5 rounded-lg px-3.5 text-sm font-medium text-tnv03-mut transition-colors group-hover/mm:bg-white/5 group-hover/mm:text-tnv03-ink group-focus-within/mm:bg-white/5 group-focus-within/mm:text-tnv03-ink focus-visible:outline-2 focus-visible:outline-tnv03-acc">Platform<svg class="size-3.5 opacity-60 transition-transform duration-200 group-hover/mm:rotate-180 group-focus-within/mm:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <div class="invisible absolute top-full left-1/2 z-40 mt-2.5 w-[min(46rem,calc(100vw-2rem))] -translate-x-1/2 translate-y-2 rounded-2xl border border-white/[0.08] bg-tnv03-surface p-5 opacity-0 shadow-[0_32px_80px_-20px_rgb(0_0_0/0.7)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(.16,1,.3,1)] before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover/mm:visible group-hover/mm:translate-y-0 group-hover/mm:opacity-100 group-focus-within/mm:visible group-focus-within/mm:translate-y-0 group-focus-within/mm:opacity-100 motion-reduce:transition-none">
            <div class="grid grid-cols-[1fr_1fr_15rem] gap-1.5">
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-sky-500/10 text-sky-400 ring-1 ring-sky-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">Cloud IDE</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">Full-stack dev environment</span></span></a>
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-emerald-500/10 text-emerald-400 ring-1 ring-emerald-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">Code Review</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">AI-powered PR analysis</span></span></a>
              <a href="#" class="row-span-3 flex flex-col justify-between overflow-hidden rounded-xl bg-linear-160 from-sky-500/25 via-tnv03-surface2 to-tnv03-surface2 p-4 ring-1 ring-sky-400/20 outline-none transition hover:ring-sky-400/50 focus-visible:ring-2 focus-visible:ring-tnv03-acc"><span class="w-fit rounded-full bg-sky-400/15 px-2 py-0.5 font-tnv03-mono text-[10px] font-medium tracking-wider text-sky-300 uppercase">Featured</span><span class="mt-6 block text-base/[1.3] font-semibold text-tnv03-ink">Edge Functions are GA</span><span class="mt-1.5 block text-xs/[1.5] text-tnv03-mut">Run code in 300+ regions with sub-10ms cold starts.</span><span class="mt-4 inline-flex items-center gap-1 text-xs font-semibold text-sky-300">Read the launch post<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span></a>
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-amber-500/10 text-amber-400 ring-1 ring-amber-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">Security</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">Secrets &amp; vulnerability scan</span></span></a>
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-pink-500/10 text-pink-400 ring-1 ring-pink-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">Observability</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">Logs, traces, metrics</span></span></a>
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-violet-500/10 text-violet-400 ring-1 ring-violet-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">AI Assistant</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">Context-aware completion</span></span></a>
              <a href="#" class="flex items-start gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv03-surface2 focus-visible:bg-tnv03-surface2 focus-visible:ring-2 focus-visible:ring-tnv03-acc/50"><span class="grid size-10 flex-none place-items-center rounded-lg bg-cyan-500/10 text-cyan-400 ring-1 ring-cyan-400/20"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg></span><span><span class="block text-[13px] font-semibold text-tnv03-ink">Deployments</span><span class="mt-0.5 block text-xs/[1.4] text-tnv03-mut">One-click to production</span></span></a>
            </div>
            <div class="mt-4 flex flex-wrap items-center gap-2 border-t border-white/[0.07] pt-4 text-[11px] font-semibold">
              <a href="#" class="rounded-full bg-sky-400/10 px-2.5 py-1 text-sky-300 transition hover:bg-sky-400/20">New: Edge Functions</a>
              <a href="#" class="rounded-full bg-emerald-400/10 px-2.5 py-1 text-emerald-300 transition hover:bg-emerald-400/20">New: AI Reviews</a>
              <a href="#" class="ml-auto rounded-full px-2.5 py-1 text-tnv03-mut transition hover:bg-white/5 hover:text-tnv03-ink">View all products →</a>
            </div>
          </div>
        </li>
        <li class="group/mm relative">
          <button type="button" aria-haspopup="true" class="flex h-11 items-center gap-1.5 rounded-lg px-3.5 text-sm font-medium text-tnv03-mut transition-colors group-hover/mm:bg-white/5 group-hover/mm:text-tnv03-ink group-focus-within/mm:bg-white/5 group-focus-within/mm:text-tnv03-ink focus-visible:outline-2 focus-visible:outline-tnv03-acc">Solutions<svg class="size-3.5 opacity-60 transition-transform duration-200 group-hover/mm:rotate-180 group-focus-within/mm:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <div class="invisible absolute top-full left-1/2 z-40 mt-2.5 grid w-[23rem] -translate-x-1/2 translate-y-2 grid-cols-2 gap-1 rounded-2xl border border-white/[0.08] bg-tnv03-surface p-3 opacity-0 shadow-[0_32px_80px_-20px_rgb(0_0_0/0.7)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(.16,1,.3,1)] before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover/mm:visible group-hover/mm:translate-y-0 group-hover/mm:opacity-100 group-focus-within/mm:visible group-focus-within/mm:translate-y-0 group-focus-within/mm:opacity-100 motion-reduce:transition-none [&_a]:rounded-xl [&_a]:p-3 [&_a]:outline-none [&_a]:transition-colors [&_a:focus-visible]:bg-tnv03-surface2 [&_a:hover]:bg-tnv03-surface2 [&_b]:block [&_b]:text-[13px] [&_b]:font-semibold [&_small]:mt-0.5 [&_small]:block [&_small]:text-xs [&_small]:text-tnv03-mut">
            <a href="#"><b>Enterprise</b><small>SSO, audit logs, SLA</small></a>
            <a href="#"><b>Startups</b><small>Credits &amp; fast scaling</small></a>
            <a href="#"><b>Open Source</b><small>Free for maintainers</small></a>
            <a href="#"><b>Education</b><small>Free for students</small></a>
          </div>
        </li>
        <li><a href="#" class="flex h-11 items-center rounded-lg px-3.5 text-sm font-medium text-tnv03-mut transition-colors hover:bg-white/5 hover:text-tnv03-ink focus-visible:outline-2 focus-visible:outline-tnv03-acc">Pricing</a></li>
        <li><a href="#" class="flex h-11 items-center rounded-lg px-3.5 text-sm font-medium text-tnv03-mut transition-colors hover:bg-white/5 hover:text-tnv03-ink focus-visible:outline-2 focus-visible:outline-tnv03-acc">Docs</a></li>
      </ul>
      <div class="flex items-center gap-2.5">
        <a href="#" class="hidden h-10 items-center rounded-lg border-[1.5px] border-white/10 px-4 text-sm font-semibold text-tnv03-mut transition hover:border-white/20 hover:text-tnv03-ink sm:inline-flex">Sign in</a>
        <a href="#" class="group/cta inline-flex h-10 items-center gap-1.5 rounded-lg bg-tnv03-acc px-4 text-sm font-semibold text-white shadow-[0_0_0_1px_rgb(255_255_255/0.1)_inset,0_8px_24px_-8px_var(--color-tnv03-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv03-acc">Start building<svg class="size-3.5 transition-transform group-hover/cta:translate-x-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        <details class="group/m relative md:hidden">
          <summary aria-label="Menu" class="grid size-11 cursor-pointer list-none place-items-center rounded-lg border border-white/10 bg-white/5 outline-none focus-visible:ring-2 focus-visible:ring-tnv03-acc [&::-webkit-details-marker]:hidden"><svg class="size-5 group-open/m:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg><svg class="hidden size-5 group-open/m:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></summary>
          <ul class="absolute top-[calc(100%+10px)] right-0 z-40 grid w-64 gap-0.5 rounded-2xl border border-white/[0.08] bg-tnv03-surface p-2 text-[15px] font-medium shadow-[0_32px_80px_-20px_rgb(0_0_0/0.7)] transition-[opacity,translate] duration-200 starting:-translate-y-1 starting:opacity-0 [&_a]:flex [&_a]:min-h-11 [&_a]:items-center [&_a]:rounded-lg [&_a]:px-3 [&_a:hover]:bg-tnv03-surface2">
            <li><a href="#">Platform</a></li><li><a href="#">Solutions</a></li><li><a href="#">Pricing</a></li><li><a href="#">Docs</a></li><li><a href="#" class="text-tnv03-acc2">Sign in</a></li>
          </ul>
        </details>
      </div>
    </nav>
  </header>
  <main class="grid place-items-center px-5 py-28 text-center [&_code]:rounded [&_code]:bg-white/[0.08] [&_code]:px-1.5 [&_code]:font-tnv03-mono [&_code]:text-[0.85em] [&_code]:text-tnv03-ink">
    <h1 class="max-w-2xl text-[clamp(2.25rem,5.5vw,3.75rem)] leading-[1.08] font-bold tracking-[-0.035em] text-balance">A <span class="bg-linear-to-r from-tnv03-acc to-tnv03-acc2 bg-clip-text text-transparent">mega menu</span> that never falls off the screen</h1>
    <p class="mt-5 max-w-lg text-base/[1.7] text-tnv03-mut text-pretty">Hover or Tab to &ldquo;Platform&rdquo;. The panel anchors to the nav with <code>static</code> + <code>left-1/2</code>, lays out with <code>grid-cols-[1fr_1fr_15rem]</code>, and adds a featured card for focus.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv03-bg: #0c1222;
  --color-tnv03-bg: oklch(0.18 0.03 264);
  --color-tnv03-glow: #0ea5e926;
  --color-tnv03-glow: oklch(0.685 0.169 237 / 0.15);
  --color-tnv03-surface: #111827;
  --color-tnv03-surface: oklch(0.21 0.034 265);
  --color-tnv03-surface2: #1e2a3d;
  --color-tnv03-surface2: oklch(0.28 0.035 258);
  --color-tnv03-ink: #f1f5f9;
  --color-tnv03-ink: oklch(0.968 0.007 248);
  --color-tnv03-mut: #a3b1c6;
  --color-tnv03-mut: oklch(0.76 0.03 256);
  --color-tnv03-acc: #0ea5e9;
  --color-tnv03-acc: oklch(0.685 0.169 237);
  --color-tnv03-acc2: #38bdf8;
  --color-tnv03-acc2: oklch(0.746 0.16 233);
  --font-tnv03-sans: 'DM Sans', system-ui, sans-serif;
  --font-tnv03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-03 {
  width: 100%;
  min-height: 100svh;
}
```
