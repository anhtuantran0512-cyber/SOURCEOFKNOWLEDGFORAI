---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-scroll-containment-with-overscroll-behavior/"
title: "Tailwind Sidebar Scroll Containment with Overscroll Behavior"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Two panes, two scrollbars, and the bug everyone has felt: you reach the bottom of the channel list and the page starts scrolling instead."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Scroll Containment with Overscroll Behavior
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-scroll-containment-with-overscroll-behavior/

Two panes, two scrollbars, and the bug everyone has felt: you reach the bottom of the channel list and the page starts scrolling instead. overscroll-behavior: contain fixes it in one declaration &mdash; which Tailwind has no utility for, correctly &mdash; so this demo is the collection's clearest case for arbitrary properties, alongside the min-h-0 that makes an overflowing flex child possible at all.
## HTML
```html
<section class="tsb-08 block relative w-full min-h-svh bg-tsb08-bg text-tsb08-ink font-tsb08-sans leading-[1.55]" aria-label="Talon chat">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-08-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-08-theme">
    <label class="grid place-items-center w-11 h-11 border-2 border-tsb08-ink bg-tsb08-surf text-tsb08-ink cursor-pointer shadow-[4px_4px_0_var(--color-tsb08-ink)] peer-focus-visible:outline-2 peer-focus-visible:outline-tsb08-acc peer-focus-visible:outline-offset-3" for="tsb-08-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="flex min-w-0 h-svh bg-tsb08-surf">
    <nav class="flex-none flex flex-col w-52 min-w-0 min-h-0 overflow-y-auto bg-tsb08-surf2 border-r-2 border-tsb08-ink [overscroll-behavior:contain] [scrollbar-gutter:stable]" aria-label="Talon channels">
      <p class="sticky top-0 z-2 m-0 px-2.5 py-2.5 bg-tsb08-surf2 border-b border-tsb08-line font-tsb08-display text-[0.78rem] tracking-[0.08em] uppercase text-tsb08-mut">Channels</p>
      <ul class="list-none m-0 p-1 [&_a]:flex [&_a]:items-center [&_a]:min-w-0 [&_a]:min-h-11 [&_a]:px-2 [&_a]:py-1.5 [&_a]:font-tsb08-mono [&_a]:text-[0.88rem] [&_a]:text-tsb08-ink [&_a]:no-underline [&_a:hover]:bg-tsb08-accsoft [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-tsb08-acc [&_a:focus-visible]:-outline-offset-2 [&_a[aria-current=page]]:bg-tsb08-acc [&_a[aria-current=page]]:text-tsb08-bg [&_a[aria-current=page]]:font-bold">
        <li><a href="#tsb-08-thread" aria-current="page">#deployments</a></li>
        <li><a href="#tsb-08-thread">#incidents</a></li>
        <li><a href="#tsb-08-thread">#billing</a></li>
        <li><a href="#tsb-08-thread">#design-review</a></li>
        <li><a href="#tsb-08-thread">#hiring</a></li>
        <li><a href="#tsb-08-thread">#audit-log</a></li>
        <li><a href="#tsb-08-thread">#api-keys</a></li>
        <li><a href="#tsb-08-thread">#field-notes</a></li>
        <li><a href="#tsb-08-thread">#vendor-desk</a></li>
        <li><a href="#tsb-08-thread">#support-escalations</a></li>
        <li><a href="#tsb-08-thread">#release-notes</a></li>
        <li><a href="#tsb-08-thread">#retro</a></li>
        <li><a href="#tsb-08-thread">#status-page</a></li>
        <li><a href="#tsb-08-thread">#certificates</a></li>
        <li><a href="#tsb-08-thread">#on-call</a></li>
        <li><a href="#tsb-08-thread">#runbooks</a></li>
        <li><a href="#tsb-08-thread">#postmortems</a></li>
        <li><a href="#tsb-08-thread">#capacity</a></li>
        <li><a href="#tsb-08-thread">#data-platform</a></li>
        <li><a href="#tsb-08-thread">#mobile</a></li>
        <li><a href="#tsb-08-thread">#design-system</a></li>
        <li><a href="#tsb-08-thread">#localisation</a></li>
        <li><a href="#tsb-08-thread">#partners</a></li>
        <li><a href="#tsb-08-thread">#recruiting</a></li>
        <li><a href="#tsb-08-thread">#social</a></li>
        <li><a href="#tsb-08-thread">#random</a></li>
      </ul>
    </nav>

    <main class="flex-1 min-w-0 min-h-0 overflow-y-auto grid gap-3 content-start px-5 pt-4.5 pb-8 [overscroll-behavior:contain] r46:px-8 r46:pt-6.5 r46:pb-10" id="tsb-08-thread">
      <p class="m-0 mb-1.5 font-tsb08-display text-[1.15rem] tracking-[0.02em] text-tsb08-acc">#deployments</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Priya Sharma</b> Rollback finished, pointer is back on 4c19f.</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Jordan Lee</b> Confirmed on the status page.</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Sam Rivera</b> Retention window is 90 days now &mdash; runbook updated.</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Ada Okafor</b> Token exchange p99 is back under 200ms.</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Tomas Vidal</b> Staging snapshot is rebuilding, ETA 10 minutes.</p>
      <p class="m-0 max-w-[44rem] text-[0.92rem] text-tsb08-mut text-pretty"><b class="block text-[0.82rem] tracking-[0.02em] text-tsb08-ink">Priya Sharma</b> Nice. I'll close the incident once staging is green.</p>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb08-bg: #211d19;
  --color-tsb08-bg: oklch(24% 0.012 60);
  --color-tsb08-surf: #2b2521;
  --color-tsb08-surf: oklch(29% 0.014 60);
  --color-tsb08-surf2: #362e28;
  --color-tsb08-surf2: oklch(34% 0.016 60);
  --color-tsb08-line: #453b33;
  --color-tsb08-line: oklch(40% 0.018 60);
  --color-tsb08-ink: #f4ece3;
  --color-tsb08-ink: oklch(95% 0.014 80);
  --color-tsb08-mut: #b3a496;
  --color-tsb08-mut: oklch(73% 0.02 75);
  --color-tsb08-acc: #e0a13c;
  --color-tsb08-acc: oklch(76% 0.14 72);
  --color-tsb08-accsoft: #3d3021;
  --color-tsb08-accsoft: oklch(33% 0.03 70);
  --font-tsb08-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb08-display: 'Roboto Slab', Rockwell, 'Bookman Old Style', Georgia, serif;
  --font-tsb08-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. */

.tsb-08 {
  width: 100%;
  min-height: 100svh;
}

.tsb-08 *,
.tsb-08 *::before,
.tsb-08 *::after {
  box-sizing: border-box;
}
/* This demo is dark by default, so the flip is inverted: the @theme block above IS the
   dark palette, and the light mirror lives in prefers-color-scheme: light. */

.tsb-08:has(.tsb-08-theme-input:checked) {
  --color-tsb08-bg: #f7f2ea;
  --color-tsb08-surf: #ffffff;
  --color-tsb08-surf2: #efe7dc;
  --color-tsb08-line: #ddd0c0;
  --color-tsb08-ink: #241d17;
  --color-tsb08-mut: #6c5c4e;
  --color-tsb08-acc: #8a5210;
  --color-tsb08-acc: oklch(48% 0.11 68);
  --color-tsb08-accsoft: #f2e3cf;
}

@media (prefers-color-scheme: light) {
  .tsb-08 {
    --color-tsb08-bg: #f7f2ea;
    --color-tsb08-surf: #ffffff;
    --color-tsb08-surf2: #efe7dc;
    --color-tsb08-line: #ddd0c0;
    --color-tsb08-ink: #241d17;
    --color-tsb08-mut: #6c5c4e;
    --color-tsb08-acc: #8a5210;
    --color-tsb08-acc: oklch(48% 0.11 68);
    --color-tsb08-accsoft: #f2e3cf;
  }

  .tsb-08:has(.tsb-08-theme-input:checked) {
    --color-tsb08-bg: #211d19;
    --color-tsb08-surf: #2b2521;
    --color-tsb08-surf2: #362e28;
    --color-tsb08-line: #453b33;
    --color-tsb08-ink: #f4ece3;
    --color-tsb08-mut: #b3a496;
    --color-tsb08-acc: #e0a13c;
    --color-tsb08-acc: oklch(76% 0.14 72);
    --color-tsb08-accsoft: #3d3021;
  }
}

@media (prefers-color-scheme: dark) {
  .tsb-08:has(.tsb-08-theme-input:checked) {
    --color-tsb08-bg: #f7f2ea;
    --color-tsb08-surf: #ffffff;
    --color-tsb08-surf2: #efe7dc;
    --color-tsb08-line: #ddd0c0;
    --color-tsb08-ink: #241d17;
    --color-tsb08-mut: #6c5c4e;
    --color-tsb08-acc: #8a5210;
    --color-tsb08-acc: oklch(48% 0.11 68);
    --color-tsb08-accsoft: #f2e3cf;
  }
}
```
