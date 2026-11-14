---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-breadcrumb-navigation-examples/"
title: "Tailwind CSS Breadcrumb Navigation Examples"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "Seven breadcrumb patterns in one sheet: chevron, slash, icon, filled pill, arrow steps cut with clip-path, a collapsed trail with a native <details> overflow…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Breadcrumb Navigation Examples
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-breadcrumb-navigation-examples/

Seven breadcrumb patterns in one sheet: chevron, slash, icon, filled pill, arrow steps cut with clip-path, a collapsed trail with a native <details> overflow menu, and a mobile back link. The documentation example ships Schema.org BreadcrumbList microdata for rich results. Every trail is a <nav aria-label="Breadcrumb"> with aria-current="page". Zero JavaScript.
## HTML
```html
<div class="tnv-09 grid min-h-svh w-full content-center justify-items-center gap-10 bg-tnv09-bg px-5 py-16 font-tnv09-sans text-tnv09-ink antialiased selection:bg-tnv09-acc selection:text-white [&_section]:w-full [&_section]:max-w-2xl [&_h2]:mb-3 [&_h2]:text-[11px] [&_h2]:font-bold [&_h2]:tracking-[0.12em] [&_h2]:text-tnv09-acc-ink [&_h2]:uppercase">
  <section>
    <h2>Chevron</h2>
    <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center rounded-xl border border-tnv09-line bg-white px-4 py-2.5 text-[15px] font-medium [&_a]:rounded-md [&_a]:px-1.5 [&_a]:py-1 [&_a]:text-tnv09-acc-ink [&_a]:transition-colors [&_a:hover]:bg-tnv09-line [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-tnv09-acc [&>li]:flex [&>li]:items-center [&>li+li]:before:mx-0.5 [&>li+li]:before:size-4 [&>li+li]:before:bg-tnv09-ink/35 [&>li+li]:before:content-[''] [&>li+li]:before:[mask:url('data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2024%2024%22%20fill=%22none%22%20stroke=%22black%22%20stroke-width=%222.5%22%3E%3Cpath%20d=%22M9%2018l6-6-6-6%22/%3E%3C/svg%3E')_center/contain_no-repeat]">
      <li><a href="#">Home</a></li><li><a href="#">Documentation</a></li><li><a href="#">CSS Guides</a></li><li><span aria-current="page" class="px-1.5 font-semibold">Navigation Patterns</span></li>
    </ol></nav>
  </section>
  <section>
    <h2>Slash</h2>
    <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center rounded-xl border border-tnv09-line bg-white px-4 py-2.5 text-[15px] font-medium [&_a]:rounded-md [&_a]:px-1 [&_a]:text-tnv09-acc-ink [&_a]:underline-offset-4 [&_a:hover]:underline [&>li+li]:before:mx-2 [&>li+li]:before:text-tnv09-ink/30 [&>li+li]:before:content-['/']">
      <li><a href="#">Dashboard</a></li><li><a href="#">Projects</a></li><li><a href="#">Website Redesign</a></li><li><span aria-current="page" class="px-1 font-semibold">Assets</span></li>
    </ol></nav>
  </section>
  <section>
    <h2>Filled pills with icons</h2>
    <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 text-sm font-semibold [&_a]:flex [&_a]:min-h-10 [&_a]:items-center [&_a]:gap-1.5 [&_a]:rounded-lg [&_a]:border [&_a]:border-tnv09-line [&_a]:bg-white [&_a]:px-3 [&_a]:text-tnv09-acc-ink [&_a]:transition-colors [&_a:hover]:border-teal-300 [&_a:hover]:bg-tnv09-line [&_svg]:size-4 [&>li]:flex [&>li]:items-center [&>li+li]:before:mr-1.5 [&>li+li]:before:text-tnv09-ink/30 [&>li+li]:before:content-['›']">
      <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>Home</a></li>
      <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>Components</a></li>
      <li><span aria-current="page" class="flex min-h-10 items-center gap-1.5 rounded-lg bg-tnv09-acc-ink px-3 text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>Navigation</span></li>
    </ol></nav>
  </section>
  <section>
    <h2>Arrow steps</h2>
    <nav aria-label="Checkout progress"><ol class="flex text-sm font-semibold [&>li]:-ml-1.5 [&>li:first-child]:ml-0 [&_a]:flex [&_a]:h-11 [&_a]:items-center [&_a]:bg-white [&_a]:pr-6 [&_a]:pl-7 [&_a]:text-tnv09-acc-ink [&_a]:transition-colors [&_a]:[clip-path:polygon(0_0,calc(100%-12px)_0,100%_50%,calc(100%-12px)_100%,0_100%,12px_50%)] [&_a:hover]:bg-tnv09-line [&>li:first-child_a]:rounded-l-lg [&>li:first-child_a]:pl-5 [&>li:first-child_a]:[clip-path:polygon(0_0,calc(100%-12px)_0,100%_50%,calc(100%-12px)_100%,0_100%)]">
      <li><a href="#">✓ Cart</a></li><li><a href="#">✓ Shipping</a></li><li><a href="#" aria-current="step" class="bg-tnv09-acc-ink! text-white!">Payment</a></li><li><a href="#" class="text-tnv09-ink/55!">Review</a></li>
    </ol></nav>
  </section>
  <section>
    <h2>Collapsed trail</h2>
    <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center rounded-xl border border-tnv09-line bg-white px-4 py-2 text-[15px] font-medium [&_a]:rounded-md [&_a]:px-1.5 [&_a]:py-1 [&_a]:text-tnv09-acc-ink [&_a:hover]:bg-tnv09-line [&>li]:flex [&>li]:items-center [&>li+li]:before:mx-1.5 [&>li+li]:before:text-tnv09-ink/30 [&>li+li]:before:content-['/']">
      <li><a href="#">Home</a></li>
      <li><details class="group/x relative"><summary aria-label="Show 3 more levels" class="grid h-8 w-9 cursor-pointer list-none place-items-center rounded-md text-tnv09-acc-ink hover:bg-tnv09-line group-open/x:bg-tnv09-line [&::-webkit-details-marker]:hidden">•••</summary><ul class="absolute top-full left-0 z-10 mt-1.5 grid w-48 gap-0.5 rounded-xl border border-tnv09-line bg-white p-1.5 shadow-[0_16px_40px_-12px_rgb(15_23_42/0.25)] transition-[opacity,translate] duration-200 starting:-translate-y-1 starting:opacity-0 [&_a]:flex [&_a]:min-h-10 [&_a]:items-center [&_a]:px-2.5"><li><a href="#">Workspace</a></li><li><a href="#">Engineering</a></li><li><a href="#">Platform team</a></li></ul></details></li>
      <li><a href="#">Q4 Roadmap</a></li>
      <li><span aria-current="page" class="px-1.5 font-semibold">Navigation audit</span></li>
    </ol></nav>
  </section>
  <section>
    <h2>Mobile back link</h2>
    <a href="#" class="group/bk inline-flex min-h-11 items-center gap-2 rounded-lg border border-tnv09-line bg-white px-4 text-[15px] font-semibold text-tnv09-acc-ink transition-colors hover:border-teal-300 hover:bg-tnv09-line"><svg class="size-4 transition-transform group-hover/bk:-translate-x-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M19 12H5M12 5l-7 7 7 7"/></svg><span><span class="sr-only">Back to </span>CSS Guides</span></a>
  </section>
  <section>
    <h2>In context · with Schema.org markup</h2>
    <article class="overflow-hidden rounded-2xl border border-tnv09-line bg-white">
      <nav aria-label="Breadcrumb" class="border-b border-tnv09-line px-6 py-3.5"><ol itemscope itemtype="https://schema.org/BreadcrumbList" class="flex flex-wrap items-center text-sm font-medium [&_a]:text-tnv09-acc-ink [&_a:hover]:underline [&>li+li]:before:mx-2 [&>li+li]:before:text-tnv09-ink/30 [&>li+li]:before:content-['›']">
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="#"><span itemprop="name">Docs</span></a><meta itemprop="position" content="1"></li>
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="#"><span itemprop="name">Navigation</span></a><meta itemprop="position" content="2"></li>
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><span itemprop="name" aria-current="page" class="font-semibold">Breadcrumbs</span><meta itemprop="position" content="3"></li>
      </ol></nav>
      <div class="p-6"><h3 class="text-[22px] font-bold tracking-[-0.01em]">Breadcrumb navigation</h3><p class="mt-2 text-[15px]/[1.7] text-tnv09-mut">Breadcrumbs show where a page sits in the hierarchy and let readers jump to any ancestor. With <code class="rounded bg-tnv09-line px-1 text-[0.9em]">BreadcrumbList</code> markup, search engines can display the same trail in results.</p></div>
    </article>
  </section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv09-bg: #f0fdfa;
  --color-tnv09-bg: oklch(0.984 0.014 181);
  --color-tnv09-line: #ccfbf1;
  --color-tnv09-line: oklch(0.953 0.051 181);
  --color-tnv09-ink: #0f172a;
  --color-tnv09-ink: oklch(0.208 0.042 266);
  --color-tnv09-mut: #475569;
  --color-tnv09-mut: oklch(0.446 0.043 257);
  --color-tnv09-acc: #0d9488;
  --color-tnv09-acc: oklch(0.6 0.118 185);
  --color-tnv09-acc-ink: #0f766e;
  --color-tnv09-acc-ink: oklch(0.511 0.096 186);
  --font-tnv09-sans: 'Source Sans 3', system-ui, sans-serif;
}

.tnv-09 {
  width: 100%;
  min-height: 100svh;
}
```
