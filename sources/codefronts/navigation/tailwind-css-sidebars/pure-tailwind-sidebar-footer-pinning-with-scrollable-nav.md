---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-sidebar-footer-pinning-with-scrollable-nav/"
title: "Pure Tailwind Sidebar Footer Pinning with Scrollable Nav"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Nineteen nav items and a user card that has to stay visible: a three-row flex column where the middle row scrolls and the outer two do not."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Sidebar Footer Pinning with Scrollable Nav
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-sidebar-footer-pinning-with-scrollable-nav/

Nineteen nav items and a user card that has to stay visible: a three-row flex column where the middle row scrolls and the outer two do not. The whole mechanism is flex-none / flex-1 min-h-0 / flex-none, and min-h-0 is the utility that makes it work &mdash; the same one demo 08 needs, in the vertical direction.
## HTML
```html
<section class="tsb-20 block relative w-full min-h-svh bg-tsb20-bg text-tsb20-ink font-tsb20-sans leading-[1.55]" aria-label="Orbit workspace">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-20-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-20-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb20-line bg-tsb20-surf text-tsb20-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb20-acc peer-focus-visible:outline-offset-2" for="tsb-20-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="flex min-w-0 h-svh bg-tsb20-surf max-r34:flex-col max-r34:h-auto max-r34:min-h-svh">
    <aside class="flex-none flex flex-col w-60 min-w-0 min-h-0 bg-tsb20-surf2 border-r border-tsb20-line max-r34:w-full max-r34:h-[60vh] max-r34:border-r-0 max-r34:border-b">
      <div class="flex-none px-4 py-3.5 border-b border-tsb20-line"><p class="m-0 font-tsb20-display text-[1.15rem] tracking-[-0.01em]">Orbit</p></div>
      <nav class="flex-1 min-h-0 overflow-y-auto px-1.5 py-1.5 [overscroll-behavior:contain] [scrollbar-gutter:stable]" aria-label="Orbit workspace">
        <ul class="list-none m-0 p-0 [&_a]:flex [&_a]:items-center [&_a]:min-w-0 [&_a]:min-h-11 [&_a]:px-2.5 [&_a]:py-2 [&_a]:text-[0.9rem] [&_a]:text-tsb20-ink [&_a]:no-underline [&_a:hover]:bg-tsb20-surf [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-tsb20-acc [&_a:focus-visible]:-outline-offset-2 [&_a[aria-current=page]]:bg-tsb20-accsoft [&_a[aria-current=page]]:text-tsb20-acc [&_a[aria-current=page]]:font-semibold [&_a[aria-current=page]]:shadow-[inset_3px_0_0_var(--color-tsb20-acc)]">
          <li><a href="#tsb-20-main" aria-current="page">Overview</a></li>
          <li><a href="#tsb-20-main">Projects</a></li>
          <li><a href="#tsb-20-main">Deployments</a></li>
          <li><a href="#tsb-20-main">Team settings</a></li>
          <li><a href="#tsb-20-main">Audit log</a></li>
          <li><a href="#tsb-20-main">Billing</a></li>
          <li><a href="#tsb-20-main">API keys</a></li>
          <li><a href="#tsb-20-main">Integrations</a></li>
          <li><a href="#tsb-20-main">Webhooks</a></li>
          <li><a href="#tsb-20-main">Regions</a></li>
          <li><a href="#tsb-20-main">Certificates</a></li>
          <li><a href="#tsb-20-main">Environments</a></li>
          <li><a href="#tsb-20-main">Secrets</a></li>
          <li><a href="#tsb-20-main">Usage</a></li>
          <li><a href="#tsb-20-main">Invoices</a></li>
          <li><a href="#tsb-20-main">Support</a></li>
          <li><a href="#tsb-20-main">Status</a></li>
          <li><a href="#tsb-20-main">Changelog</a></li>
          <li><a href="#tsb-20-main">Archive</a></li>
        </ul>
      </nav>
      <div class="flex-none flex items-center gap-2.5 px-3.5 py-3 border-t border-tsb20-line">
        <span class="flex-none grid place-items-center w-9 h-9 bg-tsb20-acc text-tsb20-onacc text-[0.76rem] font-bold tracking-[0.04em]" aria-hidden="true">JL</span>
        <span class="grid min-w-0 text-[0.76rem] text-tsb20-mut"><b class="text-[0.88rem] font-semibold text-tsb20-ink truncate">Jordan Lee</b>Operations</span>
      </div>
    </aside>

    <main class="flex-1 min-w-0 min-h-0 overflow-y-auto px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12 max-r34:overflow-visible" id="tsb-20-main">
      <h2 class="m-0 mb-5 font-tsb20-display text-[clamp(1.45rem,3.6vw,2.1rem)] leading-[1.1]">Overview</h2>
      <div class="grid grid-cols-[minmax(0,1fr)] gap-3 mb-5 max-w-[46rem] r34:grid-cols-3">
        <div class="min-w-0 px-4 py-3.5 border border-tsb20-line"><p class="m-0 mb-1 text-[0.72rem] tracking-[0.1em] uppercase text-tsb20-mut">Open projects</p><p class="m-0 font-tsb20-display text-[1.5rem] tabular-nums">14</p></div>
        <div class="min-w-0 px-4 py-3.5 border border-tsb20-line"><p class="m-0 mb-1 text-[0.72rem] tracking-[0.1em] uppercase text-tsb20-mut">Deployments today</p><p class="m-0 font-tsb20-display text-[1.5rem] tabular-nums">9</p></div>
        <div class="min-w-0 px-4 py-3.5 border border-tsb20-line"><p class="m-0 mb-1 text-[0.72rem] tracking-[0.1em] uppercase text-tsb20-mut">Members</p><p class="m-0 font-tsb20-display text-[1.5rem] tabular-nums">38</p></div>
      </div>
      <ul class="list-none m-0 p-0 grid gap-px max-w-[46rem] bg-tsb20-line border border-tsb20-line [&>li]:flex [&>li]:gap-3 [&>li]:min-w-0 [&>li]:px-3.5 [&>li]:py-2.5 [&>li]:bg-tsb20-surf [&>li]:text-[0.9rem] [&>li>span]:min-w-0 [&>li>span]:truncate [&>li>em]:ml-auto [&>li>em]:not-italic [&>li>em]:text-[0.82rem] [&>li>em]:text-tsb20-mut">
        <li><span>northwind-api</span><em>Promoted 09:14</em></li>
        <li><span>ledger-web</span><em>Building</em></li>
        <li><span>fern-cms</span><em>Promoted 07:41</em></li>
        <li><span>talon-editor</span><em>Rolled back</em></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb20-bg: #f6f4ef;
  --color-tsb20-bg: oklch(96% 0.01 90);
  --color-tsb20-surf: #fffdf9;
  --color-tsb20-surf: oklch(99% 0.006 90);
  --color-tsb20-surf2: #ece7dd;
  --color-tsb20-surf2: oklch(92.5% 0.014 85);
  --color-tsb20-line: #d9d2c5;
  --color-tsb20-line: oklch(86% 0.018 85);
  --color-tsb20-ink: #1e1c18;
  --color-tsb20-ink: oklch(23% 0.008 80);
  --color-tsb20-mut: #665f54;
  --color-tsb20-mut: oklch(46% 0.014 85);
  --color-tsb20-acc: #2f4f7a;
  --color-tsb20-acc: oklch(42% 0.1 250);
  --color-tsb20-accsoft: #dde5f0;
  --color-tsb20-accsoft: oklch(91% 0.02 250);
  --color-tsb20-onacc: #fffdf9;
  --color-tsb20-onacc: oklch(99% 0.006 90);
  --font-tsb20-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb20-display: 'Roboto Slab', Rockwell, 'Bookman Old Style', Georgia, serif;
  --breakpoint-r34: 34rem;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract. The app shell inside it is h-svh — a bounded
   height is what lets the middle flex row scroll and the footer stay pinned. */

.tsb-20 {
  width: 100%;
  min-height: 100svh;
}

.tsb-20 *,
.tsb-20 *::before,
.tsb-20 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-20:has(.tsb-20-theme-input:checked) {
  --color-tsb20-bg: #131210;
  --color-tsb20-surf: #1a1916;
  --color-tsb20-surf2: #221f1b;
  --color-tsb20-line: #302c26;
  --color-tsb20-ink: #efece5;
  --color-tsb20-mut: #a29a8d;
  --color-tsb20-acc: #93b4dd;
  --color-tsb20-acc: oklch(78% 0.08 250);
  --color-tsb20-accsoft: #1c2635;
  --color-tsb20-onacc: #131210;
}

@media (prefers-color-scheme: dark) {
  .tsb-20 {
    --color-tsb20-bg: #131210;
    --color-tsb20-surf: #1a1916;
    --color-tsb20-surf2: #221f1b;
    --color-tsb20-line: #302c26;
    --color-tsb20-ink: #efece5;
    --color-tsb20-mut: #a29a8d;
    --color-tsb20-acc: #93b4dd;
    --color-tsb20-acc: oklch(78% 0.08 250);
    --color-tsb20-accsoft: #1c2635;
    --color-tsb20-onacc: #131210;
  }

  .tsb-20:has(.tsb-20-theme-input:checked) {
    --color-tsb20-bg: #f6f4ef;
    --color-tsb20-surf: #fffdf9;
    --color-tsb20-surf2: #ece7dd;
    --color-tsb20-line: #d9d2c5;
    --color-tsb20-ink: #1e1c18;
    --color-tsb20-mut: #665f54;
    --color-tsb20-acc: #2f4f7a;
    --color-tsb20-acc: oklch(42% 0.1 250);
    --color-tsb20-accsoft: #dde5f0;
    --color-tsb20-onacc: #fffdf9;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-20:has(.tsb-20-theme-input:checked) {
    --color-tsb20-bg: #131210;
    --color-tsb20-surf: #1a1916;
    --color-tsb20-surf2: #221f1b;
    --color-tsb20-line: #302c26;
    --color-tsb20-ink: #efece5;
    --color-tsb20-mut: #a29a8d;
    --color-tsb20-acc: #93b4dd;
    --color-tsb20-acc: oklch(78% 0.08 250);
    --color-tsb20-accsoft: #1c2635;
    --color-tsb20-onacc: #131210;
  }
}
```
