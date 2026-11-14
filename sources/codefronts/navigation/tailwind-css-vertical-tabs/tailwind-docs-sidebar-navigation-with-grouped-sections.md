---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-docs-sidebar-navigation-with-grouped-sections/"
title: "Tailwind Docs Sidebar Navigation with Grouped Sections"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "An eight-page documentation site with a grouped sidebar, breadcrumb, &ldquo;On this page&rdquo; table of contents and previous/next links &mdash; switched by…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Docs Sidebar Navigation with Grouped Sections
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-docs-sidebar-navigation-with-grouped-sections/

An eight-page documentation site with a grouped sidebar, breadcrumb, &ldquo;On this page&rdquo; table of contents and previous/next links &mdash; switched by URL fragments with zero JavaScript. Every page is pre-rendered with its own sidebar, exactly like a static docs build, so the active link is a real aria-current="page" styled by aria-[current=page]:, and group headings stay pinned with sticky top-0 over a rail that scrolls with overscroll-contain.
## HTML
```html
<section class="tvt-10 w-full min-h-svh grid place-items-center bg-tvt10-bg bg-[radial-gradient(60%_45%_at_12%_0%,var(--color-tvt10-glow),transparent_70%),radial-gradient(50%_40%_at_90%_100%,var(--color-tvt10-glow2),transparent_70%)] px-4 py-14 font-tvt10-sans text-tvt10-ink antialiased sm:px-6" aria-label="Tailwind docs sidebar navigation demo">
  <div class="grid w-full max-w-[68rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt10-card px-3 py-1.5 font-tvt10-mono text-[11.5px] text-tvt10-acc-ink ring-1 ring-tvt10-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt10-acc shadow-[0_0_0_3px] shadow-tvt10-acc/25"></span>target:grid · aria-current · sticky groups</p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-extrabold tracking-[-0.04em] text-balance">A docs sidebar with <span class="bg-linear-to-r from-tvt10-hl to-tvt10-hl2 bg-clip-text pe-1 text-transparent">honest active links</span></h2>
      <p class="max-w-[52ch] text-[15px] leading-relaxed text-tvt10-mut text-pretty">Eight pages, three groups, no JavaScript. Every page carries its own pre-rendered sidebar, so the current link is announced with <code class="whitespace-nowrap font-tvt10-mono text-[13px] text-tvt10-ink">aria-current="page"</code> &mdash; not just painted.</p>
    </header>

    <div class="@container w-full overflow-hidden rounded-[20px] bg-tvt10-card shadow-tvt10-card ring-1 ring-tvt10-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex items-center gap-3 border-b border-tvt10-line px-5 py-3">
        <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-linear-to-br from-tvt10-acc to-tvt10-acc2 text-white shadow-tvt10-pill"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M4 15.5c2-5 5-8.5 12-11-1.5 6-5 9.5-12 11Zm0 0 5-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        <p class="text-[15px] font-bold tracking-[-0.02em]">Halcyon</p>
        <span class="rounded-md bg-tvt10-acc/10 px-1.5 py-0.5 font-tvt10-mono text-[11px] font-semibold text-tvt10-acc-ink ring-1 ring-tvt10-acc/25">v4.2</span>
        <p class="ms-auto flex items-center gap-5 text-[13.5px] font-medium text-tvt10-mut max-[520px]:hidden"><span class="text-tvt10-ink">Docs</span><span>Blog</span><span>Showcase</span></p>
      </div>

        <section id="tvt-10-p1" aria-label="Introduction" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1 [.tvt-10:not(:has(:target))_&]:grid">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Getting started</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Introduction</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Hierarchy without indentation<a href="#tvt-10-p1" aria-label="Link to Introduction" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Halcyon is a file-based framework for content sites. These docs double as the demo: the sidebar on the left carries three levels of structure without indenting anything.</p>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Three levers carry the hierarchy: a 10.5px mono heading, a 13.5px link, and a hairline guide. Indentation would spend width the link text needs.</span></p>
              <ul class="mt-5 grid gap-2.5 text-[14px] text-tvt10-mut sm:grid-cols-2">
                <li class="rounded-xl p-4 ring-1 ring-tvt10-line"><b class="block text-[14px] text-tvt10-ink">Static first</b>Every page is HTML at build time.</li>
                <li class="rounded-xl p-4 ring-1 ring-tvt10-line"><b class="block text-[14px] text-tvt10-ink">Zero-JS default</b>Ship scripts only where you opt in.</li>
              </ul>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><span class="hidden sm:block"></span><a href="#tvt-10-p2" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Installation →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Overview</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Group headings</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Link scale</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p2" aria-label="Installation" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Getting started</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Installation</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Install in one command<a href="#tvt-10-p2" aria-label="Link to Installation" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Halcyon needs Node 20 or later. The create script scaffolds a project, installs dependencies and opens the dev server.</p>
              <figure class="mt-5 overflow-hidden rounded-xl bg-tvt10-code shadow-tvt10-code ring-1 ring-tvt10-code-line">
                <figcaption class="flex items-center gap-2 border-b border-tvt10-code-line px-3.5 py-2 font-tvt10-mono text-[11.5px] text-tvt10-code-mut"><span aria-hidden="true" class="flex gap-1"><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i></span>terminal</figcaption>
                <pre class="overflow-x-auto px-4 py-3.5 font-tvt10-mono text-[12.5px] leading-[1.75] text-tvt10-code-ink"><code><span class="text-tvt10-code-mut"># scaffold, install and start</span>
<span class="text-tvt10-tf">npm</span> create halcyon@latest my-docs
<span class="text-tvt10-tf">cd</span> my-docs &amp;&amp; <span class="text-tvt10-tf">npm</span> run dev</code></pre>
              </figure>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span><code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">overscroll-contain</code> on the rail stops the page lurching when the sidebar hits its end &mdash; the most common complaint about docs sidebars.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p1" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Introduction</span></a><a href="#tvt-10-p3" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Project structure →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Requirements</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Create a project</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Scroll containment</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p3" aria-label="Project structure" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Getting started</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Project structure</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Project structure<a href="#tvt-10-p3" aria-label="Link to Project structure" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Pages live in <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">src/pages</code>, and the sidebar order comes from the file system plus an optional <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">_meta.json</code>.</p>
              <figure class="mt-5 overflow-hidden rounded-xl bg-tvt10-code shadow-tvt10-code ring-1 ring-tvt10-code-line">
                <figcaption class="flex items-center gap-2 border-b border-tvt10-code-line px-3.5 py-2 font-tvt10-mono text-[11.5px] text-tvt10-code-mut"><span aria-hidden="true" class="flex gap-1"><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i></span>my-docs/</figcaption>
                <pre class="overflow-x-auto px-4 py-3.5 font-tvt10-mono text-[12.5px] leading-[1.75] text-tvt10-code-ink"><code>src/
├─ pages/
│  ├─ index.mdx
│  └─ guides/<span class="text-tvt10-code-mut">        ← one sidebar group</span>
├─ components/
└─ halcyon.config.ts</code></pre>
              </figure>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>The active rail is a <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">before:</code> pseudo-element on the link, not a border &mdash; a real border would add 2px of width and nudge every label on selection.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p2" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Installation</span></a><a href="#tvt-10-p4" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Routing →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Folders</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Ordering</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Active indicator</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p4" aria-label="Routing" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Core concepts</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Routing</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Routing<a href="#tvt-10-p4" aria-label="Link to Routing" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Every file in <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">src/pages</code> becomes a route. Dynamic segments use brackets, and the current route is exposed to the sidebar automatically.</p>
              <figure class="mt-5 overflow-hidden rounded-xl bg-tvt10-code shadow-tvt10-code ring-1 ring-tvt10-code-line">
                <figcaption class="flex items-center gap-2 border-b border-tvt10-code-line px-3.5 py-2 font-tvt10-mono text-[11.5px] text-tvt10-code-mut"><span aria-hidden="true" class="flex gap-1"><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i></span>src/pages/guides/[slug].mdx</figcaption>
                <pre class="overflow-x-auto px-4 py-3.5 font-tvt10-mono text-[12.5px] leading-[1.75] text-tvt10-code-ink"><code><span class="text-tvt10-tk">export const</span> <span class="text-tvt10-tf">getStaticPaths</span> = () =&gt;
  guides.<span class="text-tvt10-tf">map</span>((g) =&gt; ({ params: { slug: g.slug } }));</code></pre>
              </figure>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Mark the active link with <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">aria-current="page"</code>, never <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">aria-selected</code> &mdash; that one belongs to tablists and is announced very differently.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p3" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Project structure</span></a><a href="#tvt-10-p5" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Data fetching →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">File routes</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Dynamic segments</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">aria-current</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p5" aria-label="Data fetching" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Core concepts</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Data fetching</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Data fetching<a href="#tvt-10-p5" aria-label="Link to Data fetching" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Fetch at build time with top-level <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">await</code> in any page. Results are cached per build and revalidated on deploy.</p>
              <figure class="mt-5 overflow-hidden rounded-xl bg-tvt10-code shadow-tvt10-code ring-1 ring-tvt10-code-line">
                <figcaption class="flex items-center gap-2 border-b border-tvt10-code-line px-3.5 py-2 font-tvt10-mono text-[11.5px] text-tvt10-code-mut"><span aria-hidden="true" class="flex gap-1"><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i></span>src/pages/changelog.mdx</figcaption>
                <pre class="overflow-x-auto px-4 py-3.5 font-tvt10-mono text-[12.5px] leading-[1.75] text-tvt10-code-ink"><code><span class="text-tvt10-tk">const</span> releases = <span class="text-tvt10-tk">await</span> <span class="text-tvt10-tf">fetch</span>(<span class="text-tvt10-ts">'https://api.halcyon.dev/releases'</span>)
  .<span class="text-tvt10-tf">then</span>((r) =&gt; r.<span class="text-tvt10-tf">json</span>());</code></pre>
              </figure>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Prose here is capped at <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">max-w-[62ch]</code> with <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">text-pretty</code>, so long paragraphs never end on an orphaned word.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p4" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Routing</span></a><a href="#tvt-10-p6" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Caching →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Build-time fetch</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Revalidation</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Measure</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p6" aria-label="Caching" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Core concepts</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Caching</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Caching<a href="#tvt-10-p6" aria-label="Link to Caching" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Static assets are fingerprinted and served with immutable cache headers. HTML is cached at the edge for 60 seconds and revalidated in the background.</p>
              <dl class="mt-5 divide-y divide-tvt10-line overflow-hidden rounded-xl ring-1 ring-tvt10-line">
                <div class="flex justify-between gap-4 px-4 py-3 text-[13.5px]"><dt class="font-semibold">/_assets/*</dt><dd class="font-tvt10-mono text-[12.5px] text-tvt10-mut">max-age=31536000, immutable</dd></div>
                <div class="flex justify-between gap-4 px-4 py-3 text-[13.5px]"><dt class="font-semibold">*.html</dt><dd class="font-tvt10-mono text-[12.5px] text-tvt10-mut">s-maxage=60, swr</dd></div>
              </dl>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Sticky group headings need an opaque (or blurred) background &mdash; <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">bg-tvt10-rail/90 backdrop-blur-md</code> here &mdash; or link text scrolls straight through them.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p5" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Data fetching</span></a><a href="#tvt-10-p7" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">CLI commands →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Assets</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">HTML</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Sticky headings</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p7" aria-label="CLI commands" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Reference</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">CLI commands</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">CLI commands<a href="#tvt-10-p7" aria-label="Link to CLI commands" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">Everything the <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">halcyon</code> binary can do. Run any command with <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">--help</code> for flags.</p>
              <dl class="mt-5 divide-y divide-tvt10-line overflow-hidden rounded-xl ring-1 ring-tvt10-line">
                <div class="grid gap-1 px-4 py-3 sm:grid-cols-[9rem_1fr]"><dt class="font-tvt10-mono text-[13px] font-semibold text-tvt10-acc-ink">halcyon dev</dt><dd class="text-[13.5px] text-tvt10-mut">Start the dev server with hot reload</dd></div>
                <div class="grid gap-1 px-4 py-3 sm:grid-cols-[9rem_1fr]"><dt class="font-tvt10-mono text-[13px] font-semibold text-tvt10-acc-ink">halcyon build</dt><dd class="text-[13.5px] text-tvt10-mut">Render every page to static HTML</dd></div>
                <div class="grid gap-1 px-4 py-3 sm:grid-cols-[9rem_1fr]"><dt class="font-tvt10-mono text-[13px] font-semibold text-tvt10-acc-ink">halcyon check</dt><dd class="text-[13.5px] text-tvt10-mut">Find broken links and missing alt text</dd></div>
              </dl>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Cap groups at five or six links. Past that, split the category &mdash; a rail is a map, and a map with no landmarks is just a list.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p6" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← Caching</span></a><a href="#tvt-10-p8" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none text-end"><span class="text-[12px] text-tvt10-mut">Next</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">Configuration →</span></a></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">dev</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">build</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Group size</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>

        <section id="tvt-10-p8" aria-label="Configuration" class="hidden h-[35rem] scroll-mt-6 grid-cols-[15.5rem_minmax(0,1fr)_11rem] target:grid target:animate-tvt10-in motion-reduce:target:animate-none @max-[56rem]:grid-cols-[15rem_minmax(0,1fr)] @max-[40rem]:h-auto @max-[40rem]:grid-cols-1">

          <nav aria-label="Documentation" class="flex min-h-0 flex-col border-e border-tvt10-line bg-tvt10-rail @max-[40rem]:border-e-0 @max-[40rem]:border-b">
            <div class="flex items-center gap-2 border-b border-tvt10-line px-4 py-3">
              <p class="flex min-h-9 flex-1 items-center gap-2 rounded-lg bg-tvt10-card px-2.5 text-[13px] text-tvt10-mut ring-1 ring-tvt10-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m13 13 3.5 3.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span class="flex-1">Search docs</span><kbd class="rounded bg-tvt10-rail px-1.5 font-tvt10-mono text-[10.5px] ring-1 ring-tvt10-line">⌘K</kbd></p>
            </div>
            <div class="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 pb-4 [scroll-padding-block:3rem] [scrollbar-width:thin] @max-[40rem]:max-h-56">
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Getting started</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p1" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Introduction</a></li>
                <li><a href="#tvt-10-p2" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Installation</a></li>
                <li><a href="#tvt-10-p3" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Project structure</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Core concepts</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p4" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Routing</a></li>
                <li><a href="#tvt-10-p5" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Data fetching</a></li>
                <li><a href="#tvt-10-p6" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Caching</a></li>
              </ul>
              <p class="sticky top-0 z-10 -mx-3 bg-tvt10-rail/90 px-5 pt-4 pb-2 font-tvt10-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt10-mut uppercase supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">Reference</p>
              <ul class="ms-2 border-s border-tvt10-line ps-2.5">
                <li><a href="#tvt-10-p7" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">CLI commands</a></li>
                <li><a href="#tvt-10-p8" aria-current="page" class="relative flex min-h-9 items-center rounded-lg px-2.5 text-[13.5px] font-medium text-tvt10-mut transition-[color,background-color] duration-150 hover:bg-tvt10-ink/[0.045] hover:text-tvt10-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tvt10-ring before:absolute before:inset-y-2 before:-start-[11.5px] before:w-0.5 before:rounded-full before:bg-transparent before:transition-colors hover:before:bg-tvt10-mut/40 aria-[current=page]:bg-tvt10-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-tvt10-acc-ink aria-[current=page]:before:bg-tvt10-acc motion-reduce:transition-none">Configuration</a></li>
              </ul>
            </div>
          </nav>
          <article class="min-h-0 min-w-0 overflow-y-auto overscroll-contain px-8 py-7 @max-[40rem]:px-5 @max-[40rem]:py-6">
            <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tvt10-mono text-[11.5px] text-tvt10-mut"><li>Docs</li><li aria-hidden="true">/</li><li>Reference</li><li aria-hidden="true">/</li><li class="text-tvt10-acc-ink">Configuration</li></ol></nav>
            <h3 class="group mt-3 flex items-baseline gap-2 text-[clamp(24px,3vw,31px)] leading-tight font-bold tracking-[-0.03em] text-balance">Configuration<a href="#tvt-10-p8" aria-label="Link to Configuration" class="font-tvt10-mono text-[0.6em] font-medium text-tvt10-mut no-underline opacity-0 transition-opacity group-hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tvt10-ring">#</a></h3>
            <p class="mt-3 max-w-[62ch] text-[15px] leading-[1.7] text-tvt10-mut text-pretty">One typed file controls the sidebar, search and theme. Groups render in the order you list them.</p>
              <figure class="mt-5 overflow-hidden rounded-xl bg-tvt10-code shadow-tvt10-code ring-1 ring-tvt10-code-line">
                <figcaption class="flex items-center gap-2 border-b border-tvt10-code-line px-3.5 py-2 font-tvt10-mono text-[11.5px] text-tvt10-code-mut"><span aria-hidden="true" class="flex gap-1"><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i><i class="size-2 rounded-full bg-tvt10-code-line"></i></span>halcyon.config.ts</figcaption>
                <pre class="overflow-x-auto px-4 py-3.5 font-tvt10-mono text-[12.5px] leading-[1.75] text-tvt10-code-ink"><code><span class="text-tvt10-tk">export default</span> <span class="text-tvt10-tf">defineConfig</span>({
  sidebar: [
    { label: <span class="text-tvt10-ts">'Getting started'</span>, dir: <span class="text-tvt10-ts">'start'</span> },
    { label: <span class="text-tvt10-ts">'Core concepts'</span>, dir: <span class="text-tvt10-ts">'concepts'</span> },
  ],
});</code></pre>
              </figure>
              <p class="mt-5 flex gap-3 rounded-xl border border-tvt10-acc/25 bg-tvt10-acc/[0.06] px-4 py-3 text-[13.5px] leading-relaxed text-tvt10-ink"><svg viewBox="0 0 20 20" width="17" height="17" aria-hidden="true" focusable="false" class="mt-0.5 shrink-0 text-tvt10-acc-ink"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 9v4.5M10 6.5v.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Real routing is a markup swap: these links are already <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">&lt;a href&gt;</code> with <code class="whitespace-nowrap rounded bg-tvt10-ink/[0.07] px-1.5 py-px font-tvt10-mono text-[0.86em]">aria-current</code>; on a multi-page site the fragment becomes a path.</span></p>
            <div class="mt-8 grid gap-3 border-t border-tvt10-line pt-5 sm:grid-cols-2"><a href="#tvt-10-p7" class="group flex min-h-16 flex-col justify-center rounded-xl px-4 py-3 ring-1 ring-tvt10-line transition-[box-shadow,background-color] duration-200 hover:bg-tvt10-acc/[0.05] hover:ring-tvt10-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt10-ring motion-reduce:transition-none "><span class="text-[12px] text-tvt10-mut">Previous</span><span class="text-[14px] font-semibold text-tvt10-ink group-hover:text-tvt10-acc-ink">← CLI commands</span></a><span class="hidden sm:block"></span></div>
          </article>
          <aside aria-label="On this page" class="border-s border-tvt10-line px-5 py-7 @max-[56rem]:hidden">
            <p class="font-tvt10-mono text-[10.5px] tracking-[0.16em] text-tvt10-mut uppercase">On this page</p>
            <ul class="mt-3 grid gap-2 border-s border-tvt10-line"><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-tvt10-acc font-semibold text-tvt10-acc-ink">Sidebar</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Search</li><li class="-ms-px border-s-2 ps-3 text-[13px] leading-snug border-transparent text-tvt10-mut">Theme</li></ul>
            <p class="mt-6 rounded-xl bg-tvt10-rail p-3 text-[12px] leading-relaxed text-tvt10-mut ring-1 ring-tvt10-line">Last updated <b class="font-semibold text-tvt10-ink">Oct 2026</b><br>Edit this page ↗</p>
          </aside>
        </section>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt10-card px-3.5 py-2 text-center font-tvt10-mono text-[11.5px] text-tvt10-mut ring-1 ring-tvt10-line">sticky top-0 · overscroll-contain · aria-[current=page]:before:bg-tvt10-acc</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt10-bg: #eef8f4;
  --color-tvt10-bg: oklch(0.97 0.012 170);
  --color-tvt10-glow: #b1eed599;
  --color-tvt10-glow: oklch(0.9 0.07 168 / 0.6);
  --color-tvt10-glow2: #bfeef780;
  --color-tvt10-glow2: oklch(0.92 0.05 210 / 0.5);
  --color-tvt10-card: #fcfffe;
  --color-tvt10-card: oklch(0.997 0.003 170);
  --color-tvt10-rail: #f2faf7;
  --color-tvt10-rail: oklch(0.978 0.009 170);
  --color-tvt10-ink: #071f1e;
  --color-tvt10-ink: oklch(0.22 0.03 190);
  --color-tvt10-mut: #48615d;
  --color-tvt10-mut: oklch(0.47 0.03 185);
  --color-tvt10-line: #d7e5e1;
  --color-tvt10-line: oklch(0.91 0.016 175);
  --color-tvt10-acc: #009e77;
  --color-tvt10-acc: oklch(0.62 0.13 168);
  --color-tvt10-acc2: #008287;
  --color-tvt10-acc2: oklch(0.55 0.11 200);
  --color-tvt10-acc-ink: #006850;
  --color-tvt10-acc-ink: oklch(0.46 0.1 170);
  --color-tvt10-hl: #008665;
  --color-tvt10-hl: oklch(0.55 0.12 168);
  --color-tvt10-hl2: #006f83;
  --color-tvt10-hl2: oklch(0.5 0.12 215);
  --color-tvt10-ring: #008568;
  --color-tvt10-ring: oklch(0.55 0.12 170);
  --color-tvt10-code: #091c1c;
  --color-tvt10-code: oklch(0.21 0.025 195);
  --color-tvt10-code-line: #203838;
  --color-tvt10-code-line: oklch(0.32 0.03 195);
  --color-tvt10-code-ink: #e0ebe8;
  --color-tvt10-code-ink: oklch(0.93 0.012 180);
  --color-tvt10-code-mut: #879e9c;
  --color-tvt10-code-mut: oklch(0.68 0.025 190);
  --color-tvt10-tk: #e9a1e3;
  --color-tvt10-tk: oklch(0.8 0.12 330);
  --color-tvt10-ts: #93e4a4;
  --color-tvt10-ts: oklch(0.85 0.12 150);
  --color-tvt10-tf: #65dfed;
  --color-tvt10-tf: oklch(0.84 0.11 205);
  --font-tvt10-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tvt10-mono: 'Source Code Pro', ui-monospace, monospace;
  --shadow-tvt10-card: 0 1px 2px oklch(0.25 0.04 190 / 0.06), 0 36px 80px -36px oklch(0.35 0.08 185 / 0.4);
  --shadow-tvt10-pill: 0 8px 18px -8px oklch(0.55 0.13 170 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.25);
  --shadow-tvt10-code: 0 12px 28px -18px oklch(0.2 0.04 195 / 0.6);
  --animate-tvt10-in: tvt10-in 0.4s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tvt10-in {
    from {
      opacity: 0;
      translate: 0 6px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-10 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-10:not([data-theme="light"]) {
    --color-tvt10-bg: #040f0f;
    --color-tvt10-bg: oklch(0.155 0.018 195);
    --color-tvt10-glow: #00372873;
    --color-tvt10-glow: oklch(0.3 0.07 168 / 0.45);
    --color-tvt10-glow2: #02283766;
    --color-tvt10-glow2: oklch(0.26 0.05 230 / 0.4);
    --color-tvt10-card: #091818;
    --color-tvt10-card: oklch(0.195 0.02 195);
    --color-tvt10-rail: #071313;
    --color-tvt10-rail: oklch(0.175 0.018 195);
    --color-tvt10-ink: #ebf4f1;
    --color-tvt10-ink: oklch(0.96 0.01 175);
    --color-tvt10-mut: #9db3b0;
    --color-tvt10-mut: oklch(0.75 0.025 185);
    --color-tvt10-line: #1f3232;
    --color-tvt10-line: oklch(0.3 0.025 195);
    --color-tvt10-acc: #40cd9b;
    --color-tvt10-acc: oklch(0.76 0.14 165);
    --color-tvt10-acc2: #10a6ad;
    --color-tvt10-acc2: oklch(0.66 0.11 200);
    --color-tvt10-acc-ink: #77e3b7;
    --color-tvt10-acc-ink: oklch(0.84 0.12 165);
    --color-tvt10-hl: #70e9b9;
    --color-tvt10-hl: oklch(0.85 0.13 165);
    --color-tvt10-hl2: #66cfe1;
    --color-tvt10-hl2: oklch(0.8 0.1 210);
    --color-tvt10-ring: #5ed8a9;
    --color-tvt10-ring: oklch(0.8 0.13 165);
    --color-tvt10-code: #030b0b;
    --color-tvt10-code: oklch(0.14 0.015 195);
    --color-tvt10-code-line: #1b2a29;
    --color-tvt10-code-line: oklch(0.27 0.02 195);
    --color-tvt10-code-ink: #e0ebe8;
    --color-tvt10-code-ink: oklch(0.93 0.012 180);
    --color-tvt10-code-mut: #879e9c;
    --color-tvt10-code-mut: oklch(0.68 0.025 190);
    --color-tvt10-tk: #e9a1e3;
    --color-tvt10-tk: oklch(0.8 0.12 330);
    --color-tvt10-ts: #93e4a4;
    --color-tvt10-ts: oklch(0.85 0.12 150);
    --color-tvt10-tf: #65dfed;
    --color-tvt10-tf: oklch(0.84 0.11 205);
  }
}

.tvt-10[data-theme="dark"] {
  --color-tvt10-bg: #040f0f;
  --color-tvt10-bg: oklch(0.155 0.018 195);
  --color-tvt10-glow: #00372873;
  --color-tvt10-glow: oklch(0.3 0.07 168 / 0.45);
  --color-tvt10-glow2: #02283766;
  --color-tvt10-glow2: oklch(0.26 0.05 230 / 0.4);
  --color-tvt10-card: #091818;
  --color-tvt10-card: oklch(0.195 0.02 195);
  --color-tvt10-rail: #071313;
  --color-tvt10-rail: oklch(0.175 0.018 195);
  --color-tvt10-ink: #ebf4f1;
  --color-tvt10-ink: oklch(0.96 0.01 175);
  --color-tvt10-mut: #9db3b0;
  --color-tvt10-mut: oklch(0.75 0.025 185);
  --color-tvt10-line: #1f3232;
  --color-tvt10-line: oklch(0.3 0.025 195);
  --color-tvt10-acc: #40cd9b;
  --color-tvt10-acc: oklch(0.76 0.14 165);
  --color-tvt10-acc2: #10a6ad;
  --color-tvt10-acc2: oklch(0.66 0.11 200);
  --color-tvt10-acc-ink: #77e3b7;
  --color-tvt10-acc-ink: oklch(0.84 0.12 165);
  --color-tvt10-hl: #70e9b9;
  --color-tvt10-hl: oklch(0.85 0.13 165);
  --color-tvt10-hl2: #66cfe1;
  --color-tvt10-hl2: oklch(0.8 0.1 210);
  --color-tvt10-ring: #5ed8a9;
  --color-tvt10-ring: oklch(0.8 0.13 165);
  --color-tvt10-code: #030b0b;
  --color-tvt10-code: oklch(0.14 0.015 195);
  --color-tvt10-code-line: #1b2a29;
  --color-tvt10-code-line: oklch(0.27 0.02 195);
  --color-tvt10-code-ink: #e0ebe8;
  --color-tvt10-code-ink: oklch(0.93 0.012 180);
  --color-tvt10-code-mut: #879e9c;
  --color-tvt10-code-mut: oklch(0.68 0.025 190);
  --color-tvt10-tk: #e9a1e3;
  --color-tvt10-tk: oklch(0.8 0.12 330);
  --color-tvt10-ts: #93e4a4;
  --color-tvt10-ts: oklch(0.85 0.12 150);
  --color-tvt10-tf: #65dfed;
  --color-tvt10-tf: oklch(0.84 0.11 205);
}
```
