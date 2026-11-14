---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-onboarding-wizard-sidebar-step-progress/"
title: "Tailwind Onboarding Wizard Sidebar with Step Progress Tracking"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The setup-wizard rail: done / current / upcoming steps, checkmark badges, a connector that fills with accent behind you, and CSS counters numbering the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Onboarding Wizard Sidebar with Step Progress Tracking
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-onboarding-wizard-sidebar-step-progress/

The setup-wizard rail: done / current / upcoming steps, checkmark badges, a connector that fills with accent behind you, and CSS counters numbering the pending steps automatically. Add or remove a step and numbering, line and states all recompute.
## HTML
```html
<section class="tsl-26 w-full h-svh min-h-svh grid grid-cols-[300px_1fr] font-tsl26-sans bg-tsl26-bg text-tsl26-ink">
  <aside aria-label="Setup progress" class="bg-tsl26-panel border-r border-tsl26-line px-[22px] py-[26px] overflow-y-auto [scrollbar-gutter:stable]">
    <h2 class="mb-6 text-[15px] font-bold tracking-tight">Workspace setup</h2>
    <ol class="tsl-26-steps list-none m-0 p-0 flex flex-col [counter-reset:tsl26]">
      <li data-state="done" class="relative grid grid-cols-[28px_1fr] gap-3.5 pb-7 [counter-increment:tsl26] after:content-[''] after:absolute after:left-[13.5px] after:top-8 after:bottom-1 after:w-0.5 after:rounded-sm after:bg-tsl26-line after:z-0 last:after:hidden last:pb-0 data-[state=done]:after:bg-tsl26-accent">
        <span aria-hidden="true" class="tsl-26-badge relative z-[1] grid place-items-center w-7 h-7 rounded-full border-2 border-tsl26-accent bg-tsl26-accent text-xs font-bold"></span>
        <div><strong class="block text-[13.5px] font-semibold leading-snug">Create account</strong><small class="text-xs leading-[1.45] text-tsl26-mut">[email protected] verified</small></div>
      </li>
      <li data-state="done" class="relative grid grid-cols-[28px_1fr] gap-3.5 pb-7 [counter-increment:tsl26] after:content-[''] after:absolute after:left-[13.5px] after:top-8 after:bottom-1 after:w-0.5 after:rounded-sm after:bg-tsl26-line after:z-0 last:after:hidden last:pb-0 data-[state=done]:after:bg-tsl26-accent">
        <span aria-hidden="true" class="tsl-26-badge relative z-[1] grid place-items-center w-7 h-7 rounded-full border-2 border-tsl26-accent bg-tsl26-accent text-xs font-bold"></span>
        <div><strong class="block text-[13.5px] font-semibold leading-snug">Invite your team</strong><small class="text-xs leading-[1.45] text-tsl26-mut">4 teammates joined</small></div>
      </li>
      <li data-state="current" aria-current="step" class="relative grid grid-cols-[28px_1fr] gap-3.5 pb-7 [counter-increment:tsl26] after:content-[''] after:absolute after:left-[13.5px] after:top-8 after:bottom-1 after:w-0.5 after:rounded-sm after:bg-tsl26-line after:z-0 last:after:hidden last:pb-0">
        <span aria-hidden="true" class="tsl-26-badge relative z-[1] grid place-items-center w-7 h-7 rounded-full border-2 border-tsl26-accent bg-white text-xs font-bold text-tsl26-accent shadow-[0_0_0_4px_var(--color-tsl26-halo)] before:content-[counter(tsl26)]"></span>
        <div><strong class="block text-[13.5px] font-semibold leading-snug text-tsl26-accent">Connect data source</strong><small class="text-xs leading-[1.45] text-tsl26-mut">Postgres, BigQuery or CSV</small></div>
      </li>
      <li data-state="todo" class="relative grid grid-cols-[28px_1fr] gap-3.5 pb-7 [counter-increment:tsl26] after:content-[''] after:absolute after:left-[13.5px] after:top-8 after:bottom-1 after:w-0.5 after:rounded-sm after:bg-tsl26-line after:z-0 last:after:hidden last:pb-0">
        <span aria-hidden="true" class="tsl-26-badge relative z-[1] grid place-items-center w-7 h-7 rounded-full border-2 border-tsl26-line bg-white text-xs font-bold text-tsl26-mut before:content-[counter(tsl26)]"></span>
        <div><strong class="block text-[13.5px] font-semibold leading-snug text-tsl26-mut">Build first dashboard</strong><small class="text-xs leading-[1.45] text-tsl26-mut">From a template or scratch</small></div>
      </li>
      <li data-state="todo" class="relative grid grid-cols-[28px_1fr] gap-3.5 pb-7 [counter-increment:tsl26] after:content-[''] after:absolute after:left-[13.5px] after:top-8 after:bottom-1 after:w-0.5 after:rounded-sm after:bg-tsl26-line after:z-0 last:after:hidden last:pb-0">
        <span aria-hidden="true" class="tsl-26-badge relative z-[1] grid place-items-center w-7 h-7 rounded-full border-2 border-tsl26-line bg-white text-xs font-bold text-tsl26-mut before:content-[counter(tsl26)]"></span>
        <div><strong class="block text-[13.5px] font-semibold leading-snug text-tsl26-mut">Set up alerts</strong><small class="text-xs leading-[1.45] text-tsl26-mut">Slack or email digests</small></div>
      </li>
    </ol>
  </aside>
  <main class="p-9 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="mb-2.5 text-[22px] font-bold leading-tight">Connect data source</h1>
    <p class="max-w-[52ch] mb-[22px] text-sm leading-[1.65] text-tsl26-mut text-pretty">The rail is an ordered list with three data-states &mdash; counters number the todos, checkmarks replace done numbers, and the connector fills behind you.</p>
    <button type="button" class="min-h-12 px-[22px] rounded-[11px] border-0 bg-tsl26-accent text-white text-sm font-semibold cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tsl26-accent focus-visible:outline-offset-[3px]">Connect Postgres</button>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl26-bg: #fcfcfe;
  --color-tsl26-bg: oklch(0.99 0.002 275);
  --color-tsl26-panel: #f3f3f7;
  --color-tsl26-panel: oklch(0.965 0.006 275);
  --color-tsl26-ink: #3a3b46;
  --color-tsl26-ink: oklch(0.26 0.02 275);
  --color-tsl26-mut: #6f7180;
  --color-tsl26-mut: oklch(0.5 0.015 275);
  --color-tsl26-line: #dcdce3;
  --color-tsl26-line: oklch(0.88 0.008 275);
  --color-tsl26-accent: #5b4bd6;
  --color-tsl26-accent: oklch(0.55 0.18 285);
  --color-tsl26-halo: rgb(91 75 214 / 0.18);
  --color-tsl26-halo: color-mix(in oklab, oklch(0.55 0.18 285) 18%, transparent);
  --font-tsl26-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-26 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
/* A masked checkmark replacing generated content: the mask URL is a data
   URI with its own quotes and commas, which no arbitrary value survives. */

.tsl-26 li[data-state="done"] .tsl-26-badge::before {
  content: "";
  width: 12px;
  height: 12px;
  background: #fff;
  -webkit-mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5.5 5.5L20 6.5"/></svg>') center/contain no-repeat;
  mask: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5.5 5.5L20 6.5"/></svg>') center/contain no-repeat;
}
```
