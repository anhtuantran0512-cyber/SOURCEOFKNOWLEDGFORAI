---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-master-detail-split-view-inbox-layout/"
title: "Tailwind CSS Master-Detail Split View Inbox Layout"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The inbox trinity &mdash; folder rail, scrollable conversation list, fluid detail pane &mdash; as one grid-cols-[13.5rem_20rem_minmax(0,1fr)] row. Selection…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Master-Detail Split View Inbox Layout
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-master-detail-split-view-inbox-layout/

The inbox trinity &mdash; folder rail, scrollable conversation list, fluid detail pane &mdash; as one grid-cols-[13.5rem_20rem_minmax(0,1fr)] row. Selection is a native radio group: has-checked: highlights the row, group-has-[#tdl04-r2:checked]/split:flex swaps the pane, and the pane now fades in with starting:opacity-0. Arrow keys work out of the box, and the reply box is a real labelled textarea.
## HTML
```html
<section class="tdl-04 @container/split w-full min-h-svh bg-tdl04-bg font-tdl04-sans text-tdl04-ink antialiased" aria-label="Master-detail split pane demo">
  <div class="group/split grid h-svh min-h-[34rem] grid-cols-[13.5rem_20rem_minmax(0,1fr)] overflow-hidden bg-tdl04-panel @max-[52rem]/split:grid-cols-[17.5rem_minmax(0,1fr)] @max-[34rem]/split:grid-cols-1 @max-[34rem]/split:grid-rows-[40%_minmax(0,1fr)]">
    <nav aria-label="Folders" class="flex flex-col gap-0.75 border-r border-tdl04-edge bg-tdl04-rail p-2.5 pt-4 @max-[52rem]/split:hidden [&>a]:flex [&>a]:h-10 [&>a]:items-center [&>a]:justify-between [&>a]:rounded-lg [&>a]:px-3 [&>a]:text-[13px] [&>a]:font-semibold [&>a]:text-tdl04-mut [&>a]:no-underline [&>a]:transition-colors [&>a:hover]:bg-tdl04-hover [&>a:hover]:text-tdl04-ink [&>a:focus-visible]:outline-2 [&>a:focus-visible]:-outline-offset-2 [&>a:focus-visible]:outline-tdl04-acc [&>a[aria-current=page]]:bg-tdl04-acc/11 [&>a[aria-current=page]]:text-tdl04-acc">
      <strong class="mb-3.5 flex items-center gap-2.5 px-2.5 text-[15px] font-bold"><span aria-hidden="true" class="size-5 rounded-md bg-[conic-gradient(from_210deg,var(--color-tdl04-acc),var(--color-tdl04-acc2),var(--color-tdl04-acc))]"></span>Helpdesk</strong>
      <a href="#inbox" aria-current="page">Inbox<b class="rounded-full bg-tdl04-acc px-1.75 text-[10.5px] text-white">3</b></a>
      <a href="#assigned">Assigned to me<b class="rounded-full bg-tdl04-chip px-1.75 text-[10.5px]">1</b></a>
      <a href="#snoozed">Snoozed</a>
      <a href="#done">Resolved</a>
      <a href="#spam">Spam</a>
    </nav>
    <div role="radiogroup" aria-label="Conversations" class="min-h-0 overflow-y-auto overscroll-contain border-r border-tdl04-edge bg-tdl04-bg [scrollbar-gutter:stable] @max-[34rem]/split:border-r-0 @max-[34rem]/split:border-b">
      <p class="sticky top-0 z-10 bg-tdl04-bg/85 px-4 pt-3.5 pb-2.5 text-[10.5px] font-bold tracking-[0.12em] text-tdl04-mut uppercase backdrop-blur-md">Inbox · 3 open</p>
      <label class="group/row relative flex cursor-pointer items-center gap-2.5 border-b border-l-3 border-b-tdl04-edge/60 border-l-transparent px-3.5 py-3.25 transition-colors hover:bg-tdl04-hover has-checked:border-l-tdl04-acc has-checked:bg-tdl04-sel has-focus-visible:outline-2 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tdl04-acc"><input class="sr-only" type="radio" name="tdl04" id="tdl04-r1" checked>
        <i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl04-acc transition-[scale,opacity] duration-300 group-has-checked/row:scale-0 group-has-checked/row:opacity-0"></i><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-140 from-tdl04-av1a to-tdl04-av1b text-[11px] font-bold text-white">MK</span>
        <span class="grid min-w-0 gap-px"><b class="text-[13px]">Maya Krishnan</b><em class="truncate text-[12.5px] not-italic">Checkout fails on step 3</em><small class="text-[11px] text-tdl04-mut">Payments · 12m</small></span>
      </label>
      <label class="group/row relative flex cursor-pointer items-center gap-2.5 border-b border-l-3 border-b-tdl04-edge/60 border-l-transparent px-3.5 py-3.25 transition-colors hover:bg-tdl04-hover has-checked:border-l-tdl04-acc has-checked:bg-tdl04-sel has-focus-visible:outline-2 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tdl04-acc"><input class="sr-only" type="radio" name="tdl04" id="tdl04-r2">
        <i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl04-acc transition-[scale,opacity] duration-300 group-has-checked/row:scale-0 group-has-checked/row:opacity-0"></i><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-140 from-tdl04-av2a to-tdl04-av2b text-[11px] font-bold text-white">TW</span>
        <span class="grid min-w-0 gap-px"><b class="text-[13px]">Tom Whitely</b><em class="truncate text-[12.5px] not-italic">Export CSV missing columns</em><small class="text-[11px] text-tdl04-mut">Reports · 41m</small></span>
      </label>
      <label class="group/row relative flex cursor-pointer items-center gap-2.5 border-b border-l-3 border-b-tdl04-edge/60 border-l-transparent px-3.5 py-3.25 transition-colors hover:bg-tdl04-hover has-checked:border-l-tdl04-acc has-checked:bg-tdl04-sel has-focus-visible:outline-2 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tdl04-acc"><input class="sr-only" type="radio" name="tdl04" id="tdl04-r3">
        <i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl04-acc transition-[scale,opacity] duration-300 group-has-checked/row:scale-0 group-has-checked/row:opacity-0"></i><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-140 from-tdl04-av3a to-tdl04-av3b text-[11px] font-bold text-white">LB</span>
        <span class="grid min-w-0 gap-px"><b class="text-[13px]">Lena Brandt</b><em class="truncate text-[12.5px] not-italic">Upgrade to annual plan</em><small class="text-[11px] text-tdl04-mut">Billing · 2h</small></span>
      </label>
      <label class="group/row relative flex cursor-pointer items-center gap-2.5 border-b border-l-3 border-b-tdl04-edge/60 border-l-transparent py-3.25 pr-3.5 pl-7.5 text-tdl04-mut transition-colors hover:bg-tdl04-hover has-checked:border-l-tdl04-acc has-checked:bg-tdl04-sel has-checked:text-tdl04-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tdl04-acc"><input class="sr-only" type="radio" name="tdl04" id="tdl04-r4">
        <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-140 from-tdl04-av4a to-tdl04-av4b text-[11px] font-bold text-white">JP</span>
        <span class="grid min-w-0 gap-px"><b class="text-[13px] text-tdl04-ink">Jonas Peel</b><em class="truncate text-[12.5px] not-italic">Thanks — all sorted!</em><small class="text-[11px]">Resolved · 1d</small></span>
      </label>
      <label class="group/row relative flex cursor-pointer items-center gap-2.5 border-b border-l-3 border-b-tdl04-edge/60 border-l-transparent py-3.25 pr-3.5 pl-7.5 text-tdl04-mut transition-colors hover:bg-tdl04-hover has-checked:border-l-tdl04-acc has-checked:bg-tdl04-sel has-checked:text-tdl04-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tdl04-acc"><input class="sr-only" type="radio" name="tdl04" id="tdl04-r5">
        <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-140 from-tdl04-av1a to-tdl04-av1b text-[11px] font-bold text-white">SR</span>
        <span class="grid min-w-0 gap-px"><b class="text-[13px] text-tdl04-ink">Sofia Reyes</b><em class="truncate text-[12.5px] not-italic">API key rotation question</em><small class="text-[11px]">Resolved · 2d</small></span>
      </label>
    </div>
    <main class="min-h-0 min-w-0 bg-tdl04-panel *:h-full *:flex-col *:transition-[opacity,translate] *:duration-300 *:starting:translate-y-1 *:starting:opacity-0">
      <article class="hidden group-has-[#tdl04-r1:checked]/split:flex">
        <header class="border-b border-tdl04-edge px-6 pt-5 pb-3.5"><h2 class="mb-2.5 text-lg font-bold tracking-tight">Checkout fails on step 3</h2><div class="flex flex-wrap gap-1.75 text-[11px] font-semibold"><span class="rounded-full border border-tdl04-hot/35 bg-tdl04-hot/8 px-2.5 py-1 text-tdl04-hot">Urgent</span><span class="rounded-full border border-tdl04-edge bg-tdl04-bg px-2.5 py-1 text-tdl04-mut">Payments</span><span class="rounded-full border border-tdl04-edge bg-tdl04-bg px-2.5 py-1 text-tdl04-mut">Pro plan</span></div></header>
        <div class="flex min-h-0 flex-1 flex-col gap-3 overflow-y-auto overscroll-contain px-6 py-5 text-[13.5px]/[1.55] *:max-w-[78%] *:rounded-[14px_14px_14px_4px] *:border *:border-tdl04-edge *:bg-tdl04-bg *:px-3.75 *:py-2.75">
          <p>Hi — card entry works but the confirm button spins forever on step 3. Console shows a 402 from /charge. Started this morning.</p>
          <p class="self-end rounded-[14px_14px_4px_14px]! border-tdl04-acc/25! bg-tdl04-mine!">Thanks Maya — we shipped a payments change at 09:20 UTC and are rolling it back now. Can you retry in ~10 minutes?</p>
          <p>Will do. Appreciate the fast reply!</p>
        </div>
        <form class="mx-6 mb-5 flex items-end gap-2.5 rounded-xl border border-tdl04-edge bg-tdl04-bg p-2 pl-4 transition focus-within:border-tdl04-acc focus-within:ring-3 focus-within:ring-tdl04-acc/15" onsubmit="return false"><label class="sr-only" for="tdl04-m1">Reply to Maya</label><textarea id="tdl04-m1" rows="1" placeholder="Reply to Maya…" class="field-sizing-content max-h-28 min-h-10 flex-1 resize-none bg-transparent py-2.5 text-[13px] outline-none placeholder:text-tdl04-mut"></textarea><button type="submit" class="h-10 rounded-lg bg-tdl04-acc px-4 text-[12.5px] font-semibold text-white transition hover:bg-tdl04-acc/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl04-acc">Send</button></form>
      </article>
      <article class="hidden group-has-[#tdl04-r2:checked]/split:flex">
        <header class="border-b border-tdl04-edge px-6 pt-5 pb-3.5"><h2 class="mb-2.5 text-lg font-bold tracking-tight">Export CSV missing columns</h2><div class="flex flex-wrap gap-1.75 text-[11px] font-semibold"><span class="rounded-full border border-tdl04-edge bg-tdl04-bg px-2.5 py-1 text-tdl04-mut">Reports</span><span class="rounded-full border border-tdl04-edge bg-tdl04-bg px-2.5 py-1 text-tdl04-mut">Team plan</span></div></header>
        <div class="flex min-h-0 flex-1 flex-col gap-3 overflow-y-auto overscroll-contain px-6 py-5 text-[13.5px]/[1.55] *:max-w-[78%] *:rounded-[14px_14px_14px_4px] *:border *:border-tdl04-edge *:bg-tdl04-bg *:px-3.75 *:py-2.75">
          <p>The order export dropped the “tax region” and “SKU” columns after the last update. We rely on both for reconciliation.</p>
          <p class="self-end rounded-[14px_14px_4px_14px]! border-tdl04-acc/25! bg-tdl04-mine!">Confirmed — a regression in the new exporter. Fix is in review; I'll attach a corrected export for the meantime.</p>
        </div>
        <form class="mx-6 mb-5 flex items-end gap-2.5 rounded-xl border border-tdl04-edge bg-tdl04-bg p-2 pl-4 transition focus-within:border-tdl04-acc focus-within:ring-3 focus-within:ring-tdl04-acc/15" onsubmit="return false"><label class="sr-only" for="tdl04-m2">Reply to Tom</label><textarea id="tdl04-m2" rows="1" placeholder="Reply to Tom…" class="field-sizing-content max-h-28 min-h-10 flex-1 resize-none bg-transparent py-2.5 text-[13px] outline-none placeholder:text-tdl04-mut"></textarea><button type="submit" class="h-10 rounded-lg bg-tdl04-acc px-4 text-[12.5px] font-semibold text-white transition hover:bg-tdl04-acc/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl04-acc">Send</button></form>
      </article>
      <article class="hidden group-has-[#tdl04-r3:checked]/split:flex">
        <header class="border-b border-tdl04-edge px-6 pt-5 pb-3.5"><h2 class="mb-2.5 text-lg font-bold tracking-tight">Upgrade to annual plan</h2><div class="flex flex-wrap gap-1.75 text-[11px] font-semibold"><span class="rounded-full border border-tdl04-edge bg-tdl04-bg px-2.5 py-1 text-tdl04-mut">Billing</span><span class="rounded-full border border-tdl04-nice/35 bg-tdl04-nice/8 px-2.5 py-1 text-tdl04-nice">Expansion</span></div></header>
        <div class="flex min-h-0 flex-1 flex-col gap-3 overflow-y-auto overscroll-contain px-6 py-5 text-[13.5px]/[1.55] *:max-w-[78%] *:rounded-[14px_14px_14px_4px] *:border *:border-tdl04-edge *:bg-tdl04-bg *:px-3.75 *:py-2.75">
          <p>We'd like to move our 14 seats to annual billing — is there a discount, and can the switch happen mid-cycle?</p>
          <p class="self-end rounded-[14px_14px_4px_14px]! border-tdl04-acc/25! bg-tdl04-mine!">Absolutely: annual is 2 months free, and we prorate the remainder of your current cycle automatically. I can apply it today if you confirm.</p>
        </div>
        <form class="mx-6 mb-5 flex items-end gap-2.5 rounded-xl border border-tdl04-edge bg-tdl04-bg p-2 pl-4 transition focus-within:border-tdl04-acc focus-within:ring-3 focus-within:ring-tdl04-acc/15" onsubmit="return false"><label class="sr-only" for="tdl04-m3">Reply to Lena</label><textarea id="tdl04-m3" rows="1" placeholder="Reply to Lena…" class="field-sizing-content max-h-28 min-h-10 flex-1 resize-none bg-transparent py-2.5 text-[13px] outline-none placeholder:text-tdl04-mut"></textarea><button type="submit" class="h-10 rounded-lg bg-tdl04-acc px-4 text-[12.5px] font-semibold text-white transition hover:bg-tdl04-acc/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl04-acc">Send</button></form>
      </article>
      <article class="hidden items-center justify-center group-has-[#tdl04-r4:checked]/split:flex"><div class="grid max-w-sm gap-2 p-6 text-center"><span aria-hidden="true" class="mx-auto mb-1 grid size-11 place-items-center rounded-full bg-tdl04-nice/12 text-lg text-tdl04-nice">✓</span><b class="text-sm">Resolved · Jonas Peel</b><p class="text-[13px]/[1.55] text-tdl04-mut">“Thanks — all sorted!” This conversation is closed. Reopen it from the ··· menu.</p></div></article>
      <article class="hidden items-center justify-center group-has-[#tdl04-r5:checked]/split:flex"><div class="grid max-w-sm gap-2 p-6 text-center"><span aria-hidden="true" class="mx-auto mb-1 grid size-11 place-items-center rounded-full bg-tdl04-nice/12 text-lg text-tdl04-nice">✓</span><b class="text-sm">Resolved · Sofia Reyes</b><p class="text-[13px]/[1.55] text-tdl04-mut">API keys can be rotated under Settings → Developers. This conversation is closed.</p></div></article>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl04-bg: #f8f9fb;
  --color-tdl04-bg: oklch(0.98 0.004 250);
  --color-tdl04-rail: #f1f3f7;
  --color-tdl04-rail: oklch(0.963 0.008 250);
  --color-tdl04-hover: #ebeef3;
  --color-tdl04-hover: oklch(0.945 0.01 250);
  --color-tdl04-panel: #ffffff;
  --color-tdl04-panel: oklch(1 0 0);
  --color-tdl04-edge: #e1e5eb;
  --color-tdl04-edge: oklch(0.915 0.01 250);
  --color-tdl04-chip: #d5dae2;
  --color-tdl04-chip: oklch(0.88 0.015 250);
  --color-tdl04-ink: #252c38;
  --color-tdl04-ink: oklch(0.27 0.02 250);
  --color-tdl04-mut: #5c6575;
  --color-tdl04-mut: oklch(0.49 0.02 250);
  --color-tdl04-acc: #2f62d8;
  --color-tdl04-acc: oklch(0.53 0.18 260);
  --color-tdl04-acc2: #3fb4c6;
  --color-tdl04-acc2: oklch(0.71 0.11 205);
  --color-tdl04-sel: #eef3fd;
  --color-tdl04-sel: oklch(0.96 0.02 260);
  --color-tdl04-mine: #e9f0fd;
  --color-tdl04-mine: oklch(0.95 0.025 260);
  --color-tdl04-hot: #c43a2c;
  --color-tdl04-hot: oklch(0.55 0.19 28);
  --color-tdl04-nice: #187d4b;
  --color-tdl04-nice: oklch(0.52 0.13 155);
  --color-tdl04-av1a: #5b7fe0;
  --color-tdl04-av1a: oklch(0.62 0.15 262);
  --color-tdl04-av1b: #7a52c9;
  --color-tdl04-av1b: oklch(0.53 0.16 295);
  --color-tdl04-av2a: #2fa8a8;
  --color-tdl04-av2a: oklch(0.66 0.11 195);
  --color-tdl04-av2b: #3a6fc4;
  --color-tdl04-av2b: oklch(0.55 0.14 255);
  --color-tdl04-av3a: #e39a3b;
  --color-tdl04-av3a: oklch(0.73 0.14 65);
  --color-tdl04-av3b: #d0493a;
  --color-tdl04-av3b: oklch(0.59 0.17 30);
  --color-tdl04-av4a: #7d8696;
  --color-tdl04-av4a: oklch(0.6 0.02 255);
  --color-tdl04-av4b: #545c6a;
  --color-tdl04-av4b: oklch(0.45 0.02 255);
  --font-tdl04-sans: 'Figtree', system-ui, sans-serif;
}

.tdl-04 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-04 * {
    transition: none !important;
  }
}
```
