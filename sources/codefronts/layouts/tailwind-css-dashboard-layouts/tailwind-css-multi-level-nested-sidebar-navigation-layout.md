---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-multi-level-nested-sidebar-navigation-layout/"
title: "Tailwind CSS Multi-Level Nested Sidebar Navigation Layout"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The cloud-console pattern: a dark icon rail, a secondary drawer whose links swap with the rail selection, and the work area."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Multi-Level Nested Sidebar Navigation Layout
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-multi-level-nested-sidebar-navigation-layout/

The cloud-console pattern: a dark icon rail, a secondary drawer whose links swap with the rail selection, and the work area. Rail selection is a radio group &mdash; group-has-[#tdl11-r2:checked]/console:flex swaps the sub-nav, the breadcrumb and the page heading &mdash; and a checkbox folds the drawer by animating grid-template-columns from 14.25rem to 0rem. Zero JavaScript.
## HTML
```html
<section class="tdl-11 @container/c w-full min-h-svh bg-tdl11-panel font-tdl11-sans text-tdl11-ink antialiased" aria-label="Nested sidebar console demo">
  <div class="group/console relative grid h-svh min-h-[32rem] grid-cols-[4rem_14.25rem_minmax(0,1fr)] overflow-hidden transition-[grid-template-columns] duration-300 ease-[cubic-bezier(.2,.7,.2,1)] has-[#tdl11-fold:checked]:grid-cols-[4rem_0rem_minmax(0,1fr)] @max-[40rem]/c:grid-cols-[4rem_0rem_minmax(0,1fr)] @max-[40rem]/c:has-[#tdl11-fold:checked]:grid-cols-[4rem_14.25rem_minmax(0,1fr)]">
    <input class="sr-only" type="radio" name="tdl11" id="tdl11-r1" checked><input class="sr-only" type="radio" name="tdl11" id="tdl11-r2"><input class="sr-only" type="radio" name="tdl11" id="tdl11-r3"><input class="sr-only" type="radio" name="tdl11" id="tdl11-r4"><input class="sr-only" type="checkbox" id="tdl11-fold">
    <nav aria-label="Sections" class="z-10 flex flex-col items-center gap-1.5 bg-tdl11-rail py-3 [&>label]:relative [&>label]:grid [&>label]:size-11 [&>label]:cursor-pointer [&>label]:place-items-center [&>label]:rounded-xl [&>label]:text-tdl11-railmut [&>label]:transition-colors [&>label:hover]:bg-tdl11-railhover [&>label:hover]:text-white [&>label]:before:absolute [&>label]:before:top-1/2 [&>label]:before:-left-2.5 [&>label]:before:h-0 [&>label]:before:w-0.75 [&>label]:before:-translate-y-1/2 [&>label]:before:rounded-full [&>label]:before:bg-tdl11-acc [&>label]:before:transition-[height] [&>label]:before:content-[''] [&>label]:after:pointer-events-none [&>label]:after:absolute [&>label]:after:top-1/2 [&>label]:after:left-[calc(100%+12px)] [&>label]:after:z-30 [&>label]:after:-translate-y-1/2 [&>label]:after:scale-90 [&>label]:after:rounded-lg [&>label]:after:bg-tdl11-tip [&>label]:after:px-2.5 [&>label]:after:py-1.25 [&>label]:after:text-[11.5px] [&>label]:after:font-semibold [&>label]:after:whitespace-nowrap [&>label]:after:text-white [&>label]:after:opacity-0 [&>label]:after:transition [&>label]:after:content-[attr(data-tip)] [&>label:hover]:after:scale-100 [&>label:hover]:after:opacity-100 [&_svg]:size-5 [&_svg]:fill-none [&_svg]:stroke-current [&_svg]:stroke-[1.7] [&_svg]:[stroke-linecap:round] [&_svg]:[stroke-linejoin:round]">
      <span aria-hidden="true" class="mb-2.5 size-6.5 rounded-lg bg-[conic-gradient(from_210deg,var(--color-tdl11-acc),var(--color-tdl11-acc2),var(--color-tdl11-acc))]"></span>
      <label for="tdl11-r1" data-tip="Overview" class="group-has-[#tdl11-r1:checked]/console:bg-tdl11-railon group-has-[#tdl11-r1:checked]/console:text-white group-has-[#tdl11-r1:checked]/console:before:h-5.5 group-has-[#tdl11-r1:focus-visible]/console:outline-2 group-has-[#tdl11-r1:focus-visible]/console:outline-tdl11-acc"><span class="sr-only">Overview</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12 12 4l9 8"/><path d="M5 10v10h14V10"/></svg></label>
      <label for="tdl11-r2" data-tip="Compute" class="group-has-[#tdl11-r2:checked]/console:bg-tdl11-railon group-has-[#tdl11-r2:checked]/console:text-white group-has-[#tdl11-r2:checked]/console:before:h-5.5 group-has-[#tdl11-r2:focus-visible]/console:outline-2 group-has-[#tdl11-r2:focus-visible]/console:outline-tdl11-acc"><span class="sr-only">Compute</span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg></label>
      <label for="tdl11-r3" data-tip="Storage" class="group-has-[#tdl11-r3:checked]/console:bg-tdl11-railon group-has-[#tdl11-r3:checked]/console:text-white group-has-[#tdl11-r3:checked]/console:before:h-5.5 group-has-[#tdl11-r3:focus-visible]/console:outline-2 group-has-[#tdl11-r3:focus-visible]/console:outline-tdl11-acc"><span class="sr-only">Storage</span><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></label>
      <label for="tdl11-r4" data-tip="Security" class="group-has-[#tdl11-r4:checked]/console:bg-tdl11-railon group-has-[#tdl11-r4:checked]/console:text-white group-has-[#tdl11-r4:checked]/console:before:h-5.5 group-has-[#tdl11-r4:focus-visible]/console:outline-2 group-has-[#tdl11-r4:focus-visible]/console:outline-tdl11-acc"><span class="sr-only">Security</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 3v6c0 4.4-3 7.4-7 9-4-1.6-7-4.6-7-9V6Z"/><path d="m9 12 2 2 4-4"/></svg></label>
      <label for="tdl11-fold" data-tip="Toggle panel" class="mt-auto group-has-[#tdl11-fold:focus-visible]/console:outline-2 group-has-[#tdl11-fold:focus-visible]/console:outline-tdl11-acc"><span class="sr-only">Toggle section panel</span><svg viewBox="0 0 24 24" aria-hidden="true" class="transition-[rotate] duration-300 group-has-[#tdl11-fold:checked]/console:rotate-180 @max-[40rem]/c:rotate-180 @max-[40rem]/c:group-has-[#tdl11-fold:checked]/console:rotate-0"><path d="m14 6-6 6 6 6"/></svg></label>
    </nav>
    <div class="min-w-0 overflow-hidden border-r border-tdl11-edge bg-tdl11-drawer transition-[visibility] group-has-[#tdl11-fold:checked]/console:invisible group-has-[#tdl11-fold:checked]/console:delay-300 @max-[40rem]/c:invisible @max-[40rem]/c:group-has-[#tdl11-fold:checked]/console:visible @max-[40rem]/c:group-has-[#tdl11-fold:checked]/console:delay-0 *:w-57 *:flex-col *:gap-0.75 *:px-3 *:py-4.5 *:transition-[opacity,translate] *:duration-300 *:starting:translate-y-2 *:starting:opacity-0 [&_h2]:mb-2.5 [&_h2]:px-2.5 [&_h2]:text-[11px] [&_h2]:font-bold [&_h2]:tracking-[0.12em] [&_h2]:text-tdl11-mut [&_h2]:uppercase [&_a]:flex [&_a]:h-10 [&_a]:items-center [&_a]:justify-between [&_a]:gap-2 [&_a]:rounded-lg [&_a]:px-2.75 [&_a]:text-[13px] [&_a]:font-semibold [&_a]:text-tdl11-mut [&_a]:no-underline [&_a]:transition-colors [&_a:hover]:bg-tdl11-drawerhover [&_a:hover]:text-tdl11-ink [&_a:focus-visible]:outline-2 [&_a:focus-visible]:-outline-offset-2 [&_a:focus-visible]:outline-tdl11-acc [&_a[aria-current=page]]:bg-tdl11-acc/12 [&_a[aria-current=page]]:text-tdl11-accink [&_b]:rounded-full [&_b]:bg-tdl11-acc [&_b]:px-1.75 [&_b]:text-[10.5px] [&_b]:text-white">
      <div class="hidden group-has-[#tdl11-r1:checked]/console:flex"><h2>Overview</h2><a href="#dash" aria-current="page">Dashboard</a><a href="#usage">Usage &amp; cost</a><a href="#quotas">Quotas</a><a href="#activity">Activity log</a></div>
      <div class="hidden group-has-[#tdl11-r2:checked]/console:flex"><h2>Compute</h2><a href="#instances" aria-current="page">Instances <b>12</b></a><a href="#images">Machine images</a><a href="#groups">Instance groups</a><a href="#lb">Load balancers</a><a href="#autoscale">Autoscaling</a></div>
      <div class="hidden group-has-[#tdl11-r3:checked]/console:flex"><h2>Storage</h2><a href="#buckets" aria-current="page">Buckets <b>8</b></a><a href="#disks">Disks</a><a href="#snapshots">Snapshots</a><a href="#lifecycle">Lifecycle rules</a></div>
      <div class="hidden group-has-[#tdl11-r4:checked]/console:flex"><h2>Security</h2><a href="#iam" aria-current="page">IAM &amp; roles</a><a href="#keys">API keys</a><a href="#firewall">Firewall</a><a href="#audit">Audit trail</a></div>
    </div>
    <main class="flex min-w-0 flex-col gap-3.5 overflow-y-auto overscroll-contain px-5 py-4.5">
      <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-[12.5px] text-tdl11-mut"><span>console</span><span aria-hidden="true" class="opacity-60">›</span><b class="font-semibold text-tdl11-ink"><span class="hidden group-has-[#tdl11-r1:checked]/console:inline">Overview</span><span class="hidden group-has-[#tdl11-r2:checked]/console:inline">Compute</span><span class="hidden group-has-[#tdl11-r3:checked]/console:inline">Storage</span><span class="hidden group-has-[#tdl11-r4:checked]/console:inline">Security</span></b></nav>
      <div class="flex flex-wrap items-end justify-between gap-3">
        <div><h1 class="text-xl font-bold tracking-tight"><span class="hidden group-has-[#tdl11-r1:checked]/console:inline">Project dashboard</span><span class="hidden group-has-[#tdl11-r2:checked]/console:inline">VM instances</span><span class="hidden group-has-[#tdl11-r3:checked]/console:inline">Buckets</span><span class="hidden group-has-[#tdl11-r4:checked]/console:inline">IAM &amp; roles</span></h1><p class="text-[13px] text-tdl11-mut">acme-prod · 4 regions</p></div>
        <button type="button" class="h-10 rounded-lg bg-tdl11-acc px-4 text-[13px] font-semibold text-white transition hover:bg-tdl11-acc/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl11-acc">Create</button>
      </div>
      <div class="grid gap-2.5 [&>article]:grid [&>article]:grid-cols-[minmax(0,1fr)_auto] [&>article]:items-center [&>article]:gap-x-3 [&>article]:gap-y-0.5 [&>article]:rounded-xl [&>article]:border [&>article]:border-tdl11-edge [&>article]:bg-tdl11-panel [&>article]:px-4 [&>article]:py-3.25 [&>article]:transition [&>article:hover]:border-tdl11-acc/45 [&>article:hover]:shadow-[0_8px_20px_-16px_var(--color-tdl11-shadow)] [&_b]:truncate [&_b]:font-tdl11-mono [&_b]:text-[13.5px] [&_b]:font-medium [&_span]:col-start-1 [&_span]:text-xs [&_span]:text-tdl11-mut [&_i]:col-start-2 [&_i]:row-span-2 [&_i]:row-start-1 [&_i]:rounded-full [&_i]:px-2.75 [&_i]:py-1 [&_i]:text-[11px] [&_i]:font-bold [&_i]:not-italic">
        <article><b>prod-api-01</b><span>us-east1 · e2-standard-4</span><i class="bg-tdl11-ok/14 text-tdl11-okink">Running</i></article>
        <article><b>prod-api-02</b><span>us-east1 · e2-standard-4</span><i class="bg-tdl11-ok/14 text-tdl11-okink">Running</i></article>
        <article><b>staging-worker</b><span>eu-west2 · e2-small</span><i class="bg-tdl11-drawer text-tdl11-mut">Stopped</i></article>
        <article><b>batch-runner</b><span>us-central1 · c3-highcpu-8</span><i class="bg-tdl11-ok/14 text-tdl11-okink">Running</i></article>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl11-rail: #161a2e;
  --color-tdl11-rail: oklch(0.21 0.035 270);
  --color-tdl11-railhover: #232842;
  --color-tdl11-railhover: oklch(0.27 0.04 270);
  --color-tdl11-railon: #2d3463;
  --color-tdl11-railon: oklch(0.32 0.07 272);
  --color-tdl11-railmut: #a3a9c4;
  --color-tdl11-railmut: oklch(0.74 0.03 270);
  --color-tdl11-tip: #22263a;
  --color-tdl11-tip: oklch(0.25 0.025 270);
  --color-tdl11-drawer: #f3f4f8;
  --color-tdl11-drawer: oklch(0.965 0.008 270);
  --color-tdl11-drawerhover: #e8eaf1;
  --color-tdl11-drawerhover: oklch(0.935 0.012 270);
  --color-tdl11-panel: #ffffff;
  --color-tdl11-panel: oklch(1 0 0);
  --color-tdl11-edge: #e0e2ea;
  --color-tdl11-edge: oklch(0.905 0.012 270);
  --color-tdl11-ink: #252a3c;
  --color-tdl11-ink: oklch(0.27 0.025 270);
  --color-tdl11-mut: #5b6176;
  --color-tdl11-mut: oklch(0.49 0.025 270);
  --color-tdl11-acc: #5160e6;
  --color-tdl11-acc: oklch(0.56 0.19 272);
  --color-tdl11-accink: #3240b4;
  --color-tdl11-accink: oklch(0.45 0.17 272);
  --color-tdl11-acc2: #45c0dc;
  --color-tdl11-acc2: oklch(0.75 0.11 210);
  --color-tdl11-ok: #2aa766;
  --color-tdl11-ok: oklch(0.65 0.15 155);
  --color-tdl11-okink: #157a45;
  --color-tdl11-okink: oklch(0.5 0.12 155);
  --color-tdl11-shadow: #4a5590;
  --color-tdl11-shadow: oklch(0.42 0.08 272 / 0.6);
  --font-tdl11-sans: 'DM Sans', system-ui, sans-serif;
  --font-tdl11-mono: 'DM Mono', ui-monospace, monospace;
}

.tdl-11 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-11 * {
    transition-duration: 0.01s !important;
  }
}
```
