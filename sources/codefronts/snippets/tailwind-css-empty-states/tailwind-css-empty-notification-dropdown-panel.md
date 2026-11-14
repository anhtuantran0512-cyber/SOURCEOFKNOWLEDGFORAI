---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-notification-dropdown-panel/"
title: "Tailwind CSS Empty Notification Dropdown Panel"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A fintech top bar with its notification flyout open on \"you are up to date\" — toggled by a checkbox, tabbed by radios, animated in with starting:, all…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Notification Dropdown Panel
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-notification-dropdown-panel/

A fintech top bar with its notification flyout open on "you are up to date" — toggled by a checkbox, tabbed by radios, animated in with starting:, all without JavaScript. Each tab has its own reason-specific empty copy, because "no approvals" and "no mentions" mean different things.
## HTML
```html
<div class="tes-10 group/bar w-full min-h-svh bg-tes10-bg font-tes10-sans text-tes10-ink antialiased">
  <header class="relative z-10 flex items-center gap-6 border-b border-tes10-line bg-tes10-card px-[clamp(1rem,4vw,2.5rem)] py-3">
    <span class="flex items-center gap-2 font-semibold tracking-tight"><span aria-hidden="true" class="size-6 rounded-lg bg-tes10-acc"></span>Ledgerline</span>
    <nav aria-label="Main" class="hidden gap-1 text-sm sm:flex">
      <a href="#" class="rounded-lg px-3 py-2 text-tes10-mut hover:bg-tes10-sunk hover:text-tes10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes10-acc">Accounts</a><a href="#" class="rounded-lg px-3 py-2 text-tes10-mut hover:bg-tes10-sunk hover:text-tes10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes10-acc">Transfers</a><a href="#" class="rounded-lg px-3 py-2 text-tes10-mut hover:bg-tes10-sunk hover:text-tes10-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes10-acc">Reports</a>
    </nav>
    <div class="relative ml-auto flex items-center gap-2">
      <input type="checkbox" id="tes10-open" checked class="peer sr-only" aria-controls="tes10-panel">
      <label for="tes10-open" class="grid size-11 cursor-pointer place-items-center rounded-full text-tes10-mut transition hover:bg-tes10-sunk hover:text-tes10-ink peer-checked:bg-tes10-acc/10 peer-checked:text-tes10-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes10-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15zM10 20.5h4"/></svg><span class="sr-only">Notifications</span></label>
      <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-tes10-ink text-xs font-semibold text-white">JS</span>
      <div id="tes10-panel" role="dialog" aria-label="Notifications" class="absolute top-[calc(100%+0.75rem)] right-0 hidden w-[min(24rem,calc(100vw-2rem))] origin-top-right overflow-hidden rounded-2xl bg-tes10-card shadow-[0_24px_60px_-16px_oklch(0.25_0.04_250/0.35),0_2px_6px_oklch(0.25_0.04_250/0.08)] ring-1 ring-tes10-line transition-[opacity,scale] duration-200 ease-out group-has-[#tes10-open:checked]/bar:grid starting:scale-95 starting:opacity-0">
        <div class="flex items-center justify-between px-4 pt-3.5 pb-1">
          <span class="text-[15px] font-semibold">Notifications</span>
          <label for="tes10-open" aria-label="Close notifications" class="grid size-11 cursor-pointer place-items-center rounded-full text-tes10-mut hover:bg-tes10-sunk hover:text-tes10-ink"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></label>
        </div>
        <div role="radiogroup" aria-label="Filter notifications" class="flex gap-4 border-b border-tes10-line px-4 text-sm">
          <label class="-mb-px inline-flex min-h-11 cursor-pointer items-center border-b-2 border-transparent text-tes10-mut has-checked:border-tes10-acc has-checked:font-medium has-checked:text-tes10-ink has-focus-visible:outline-2 has-focus-visible:outline-tes10-acc"><input type="radio" name="tes10-tab" id="tes10-a" checked class="sr-only">All</label>
          <label class="-mb-px inline-flex min-h-11 cursor-pointer items-center border-b-2 border-transparent text-tes10-mut has-checked:border-tes10-acc has-checked:font-medium has-checked:text-tes10-ink has-focus-visible:outline-2 has-focus-visible:outline-tes10-acc"><input type="radio" name="tes10-tab" id="tes10-b" class="sr-only">Approvals</label>
          <label class="-mb-px inline-flex min-h-11 cursor-pointer items-center border-b-2 border-transparent text-tes10-mut has-checked:border-tes10-acc has-checked:font-medium has-checked:text-tes10-ink has-focus-visible:outline-2 has-focus-visible:outline-tes10-acc"><input type="radio" name="tes10-tab" id="tes10-c" class="sr-only">Mentions</label>
        </div>
        <div class="hidden justify-items-center px-8 py-10 text-center group-has-[#tes10-a:checked]/bar:grid">
          <span aria-hidden="true" class="grid size-14 place-items-center rounded-full bg-tes10-ok/10 text-tes10-ok ring-1 ring-tes10-ok/20"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>
          <p class="mt-4 font-semibold">You are up to date</p>
          <p class="mt-1 text-[13px]/5 text-tes10-mut text-pretty">Everything since Monday has been read. New activity lands here as it happens.</p>
        </div>
        <div class="hidden justify-items-center px-8 py-10 text-center group-has-[#tes10-b:checked]/bar:grid">
          <span aria-hidden="true" class="grid size-14 place-items-center rounded-full bg-tes10-acc/10 text-tes10-acc ring-1 ring-tes10-acc/20"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3.5 19 6v5.5c0 4.2-3 7.4-7 9-4-1.6-7-4.8-7-9V6z"/><path d="m9 12 2 2 4-4"/></svg></span>
          <p class="mt-4 font-semibold">No approvals waiting</p>
          <p class="mt-1 text-[13px]/5 text-tes10-mut text-pretty">Transfers above your limit appear here for a second signature.</p>
        </div>
        <div class="hidden justify-items-center px-8 py-10 text-center group-has-[#tes10-c:checked]/bar:grid">
          <span aria-hidden="true" class="grid size-14 place-items-center rounded-full bg-tes10-sunk text-tes10-mut ring-1 ring-tes10-line"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3.5"/><path d="M15.5 12v1.5a2.5 2.5 0 0 0 5 0V12a8.5 8.5 0 1 0-3.4 6.8"/></svg></span>
          <p class="mt-4 font-semibold">Nobody has tagged you</p>
          <p class="mt-1 text-[13px]/5 text-tes10-mut text-pretty">Mentions in comments and reconciliation notes show up here.</p>
        </div>
        <div class="border-t border-tes10-line bg-tes10-sunk/60 px-4 py-1"><a href="#" class="inline-flex min-h-11 items-center text-[13px] font-medium text-tes10-acc hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes10-acc">Notification settings</a></div>
      </div>
    </div>
  </header>
  <main aria-hidden="true" class="mx-auto grid w-full max-w-6xl gap-5 px-[clamp(1rem,4vw,2.5rem)] py-8 md:grid-cols-[minmax(0,2fr)_minmax(0,1fr)]">
    <div class="grid content-start gap-3 rounded-2xl bg-tes10-card p-5 ring-1 ring-tes10-line">
      <span class="h-5 w-40 rounded-md bg-tes10-sunk"></span>
      <span class="flex gap-3 border-t border-tes10-line pt-3"><i class="size-9 rounded-full bg-tes10-sunk"></i><i class="h-3 w-1/2 self-center rounded bg-tes10-sunk"></i><i class="ml-auto h-3 w-16 self-center rounded bg-tes10-sunk"></i></span>
      <span class="flex gap-3 border-t border-tes10-line pt-3"><i class="size-9 rounded-full bg-tes10-sunk"></i><i class="h-3 w-2/5 self-center rounded bg-tes10-sunk"></i><i class="ml-auto h-3 w-14 self-center rounded bg-tes10-sunk"></i></span>
      <span class="flex gap-3 border-t border-tes10-line pt-3"><i class="size-9 rounded-full bg-tes10-sunk"></i><i class="h-3 w-3/5 self-center rounded bg-tes10-sunk"></i><i class="ml-auto h-3 w-20 self-center rounded bg-tes10-sunk"></i></span>
    </div>
    <div class="grid content-start gap-5"><span class="h-44 rounded-2xl bg-tes10-card ring-1 ring-tes10-line"></span><span class="h-24 rounded-2xl bg-tes10-card ring-1 ring-tes10-line"></span></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes10-bg: #f4f6f9;
  --color-tes10-bg: oklch(0.97 0.005 250);
  --color-tes10-card: #ffffff;
  --color-tes10-card: oklch(1 0 0);
  --color-tes10-sunk: #edf0f4;
  --color-tes10-sunk: oklch(0.951 0.007 250);
  --color-tes10-line: #dfe3ea;
  --color-tes10-line: oklch(0.907 0.01 250);
  --color-tes10-ink: #141a24;
  --color-tes10-ink: oklch(0.2 0.02 255);
  --color-tes10-mut: #566074;
  --color-tes10-mut: oklch(0.47 0.03 260);
  --color-tes10-acc: #1d5fd1;
  --color-tes10-acc: oklch(0.5 0.18 260);
  --color-tes10-ok: #148a5c;
  --color-tes10-ok: oklch(0.56 0.12 160);
  --font-tes10-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-10 {
  width: 100%;
  min-height: 100svh;
}

.tes-10 [hidden] {
  display: none !important;
}
```
