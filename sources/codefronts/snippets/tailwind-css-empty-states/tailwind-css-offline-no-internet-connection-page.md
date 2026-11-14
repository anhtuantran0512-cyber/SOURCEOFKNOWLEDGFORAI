---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-offline-no-internet-connection-page/"
title: "Tailwind CSS Offline / No Internet Connection Page"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A notes app that has lost its connection and says exactly what that means: edits are safe on this device, three are queued, nothing will be overwritten."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Offline / No Internet Connection Page
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-offline-no-internet-connection-page/

A notes app that has lost its connection and says exactly what that means: edits are safe on this device, three are queued, nothing will be overwritten. The queue rows tick to "synced" one by one when the connection returns — and the demo listens to the browser's real online/offline events, so it reacts to your network too.
## HTML
```html
<div class="tes-12 group/root w-full min-h-svh bg-tes12-bg font-tes12-sans text-tes12-ink antialiased">
  <div class="grid min-h-svh md:grid-cols-[14rem_minmax(0,1fr)]">
    <aside class="flex flex-col gap-5 border-b border-tes12-line bg-tes12-side p-4 md:border-r md:border-b-0">
      <span class="px-2 font-tes12-serif text-2xl">Quill</span>
      <nav class="hidden gap-0.5 text-sm md:grid">
        <a href="#" aria-current="page" class="flex min-h-10 items-center rounded-lg bg-tes12-card px-3 font-medium shadow-xs focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">All notes</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes12-mut hover:bg-tes12-card focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">Shared with me</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes12-mut hover:bg-tes12-card focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">Templates</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes12-mut hover:bg-tes12-card focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">Trash</a>
      </nav>
      <p role="status" class="mt-auto flex items-center gap-2 rounded-full bg-tes12-warn/12 px-3 py-2 text-xs font-medium text-tes12-warn group-data-online/root:bg-tes12-ok/12 group-data-online/root:text-tes12-ok"><i aria-hidden="true" class="size-2 rounded-full bg-current group-data-busy/root:animate-pulse"></i><span id="tes12-conn">Offline</span></p>
    </aside>
    <main class="grid place-items-center px-[clamp(1rem,5vw,3rem)] py-12">
      <div class="grid w-full max-w-lg gap-6">
        <span aria-hidden="true" class="relative grid h-20 w-24 place-items-center overflow-hidden rounded-2xl bg-tes12-card text-tes12-warn ring-1 ring-tes12-line group-data-online/root:text-tes12-ok">
          <svg class="size-10 animate-tes12-drift group-data-online/root:hidden motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.2 9.1 4.5 4.5 0 0 0 7 18zM4 4l16 16"/></svg>
          <svg class="hidden size-10 group-data-online/root:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.2 9.1 4.5 4.5 0 0 0 7 18z"/><path d="m9.5 13.5 2 2 3.5-3.5"/></svg>
        </span>
        <div class="grid gap-2">
          <h1 id="tes12-h" class="font-tes12-serif text-[clamp(2rem,4.5vw,2.8rem)] leading-[1.05] tracking-tight text-balance">You are working offline</h1>
          <p id="tes12-p" class="text-[15px]/7 text-tes12-mut text-pretty">Everything you type is saved on this device. Three edits are waiting to sync and nothing will be overwritten.</p>
        </div>
        <ul class="divide-y divide-tes12-line overflow-hidden rounded-2xl bg-tes12-card ring-1 ring-tes12-line">
          <li data-q class="group/q flex items-center gap-3 px-4 py-3"><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tes12-warn transition-colors group-data-synced/q:bg-tes12-ok"></i><span class="flex-1 text-sm font-medium">Q3 supplier review</span><span class="text-xs text-tes12-mut group-data-synced/q:hidden">edited 4 min ago</span><span class="hidden items-center gap-1 text-xs font-medium text-tes12-ok group-data-synced/q:inline-flex"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>synced</span></li>
          <li data-q class="group/q flex items-center gap-3 px-4 py-3"><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tes12-warn transition-colors group-data-synced/q:bg-tes12-ok"></i><span class="flex-1 text-sm font-medium">Warehouse handover</span><span class="text-xs text-tes12-mut group-data-synced/q:hidden">edited 11 min ago</span><span class="hidden items-center gap-1 text-xs font-medium text-tes12-ok group-data-synced/q:inline-flex"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>synced</span></li>
          <li data-q class="group/q flex items-center gap-3 px-4 py-3"><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tes12-warn transition-colors group-data-synced/q:bg-tes12-ok"></i><span class="flex-1 text-sm font-medium">Interview notes — Dee O.</span><span class="text-xs text-tes12-mut group-data-synced/q:hidden">created offline</span><span class="hidden items-center gap-1 text-xs font-medium text-tes12-ok group-data-synced/q:inline-flex"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>synced</span></li>
        </ul>
        <div class="flex flex-wrap gap-2.5">
          <button type="button" id="tes12-retry" class="min-h-11 rounded-full bg-tes12-ink px-5 text-sm font-medium text-white transition hover:bg-tes12-acc active:scale-[.98] disabled:opacity-60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">Check connection</button>
          <button type="button" class="min-h-11 rounded-full border border-tes12-line2 px-5 text-sm hover:bg-tes12-side focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes12-acc">Keep writing offline</button>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes12-bg: #fbfaf7;
  --color-tes12-bg: oklch(0.984 0.005 90);
  --color-tes12-side: #f3f1ec;
  --color-tes12-side: oklch(0.957 0.008 90);
  --color-tes12-card: #ffffff;
  --color-tes12-card: oklch(1 0 0);
  --color-tes12-line: #e5e2da;
  --color-tes12-line: oklch(0.91 0.01 90);
  --color-tes12-line2: #cfcabe;
  --color-tes12-line2: oklch(0.83 0.016 90);
  --color-tes12-ink: #1e1d19;
  --color-tes12-ink: oklch(0.22 0.008 90);
  --color-tes12-mut: #5f5c53;
  --color-tes12-mut: oklch(0.47 0.013 90);
  --color-tes12-acc: #2d5bd0;
  --color-tes12-acc: oklch(0.5 0.18 265);
  --color-tes12-warn: #a2560a;
  --color-tes12-warn: oklch(0.55 0.13 60);
  --color-tes12-ok: #157a52;
  --color-tes12-ok: oklch(0.52 0.11 160);
  --font-tes12-sans: 'Geist', system-ui, sans-serif;
  --font-tes12-serif: 'Instrument Serif', Georgia, serif;
  --animate-tes12-drift: tes12-drift 4s ease-in-out infinite;

  @keyframes tes12-drift {
    0%,
        100% {
      translate: -3px 0;
    }

    50% {
      translate: 3px -2px;
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-12 {
  width: 100%;
  min-height: 100svh;
}

.tes-12 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-12');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const retry = $('#tes12-retry'), conn = $('#tes12-conn');
  const rows = [...root.querySelectorAll('[data-q]')];
  const goOnline = () => {
    root.removeAttribute('data-busy'); root.setAttribute('data-online', '');
    conn.textContent = 'Online';
    $('#tes12-h').textContent = 'Back online, everything synced';
    $('#tes12-p').textContent = 'All three edits reached the server in order. Nothing needed merging.';
    rows.forEach((r, i) => setTimeout(() => r.setAttribute('data-synced', ''), 220 * (i + 1)));
    retry.disabled = false; retry.textContent = 'Open Q3 supplier review';
  };
  const goOffline = () => {
    root.removeAttribute('data-online'); root.removeAttribute('data-busy');
    conn.textContent = 'Offline';
    $('#tes12-h').textContent = 'You are working offline';
    $('#tes12-p').textContent = 'Everything you type is saved on this device. Three edits are waiting to sync and nothing will be overwritten.';
    rows.forEach((r) => r.removeAttribute('data-synced'));
    retry.disabled = false; retry.textContent = 'Check connection';
  };
  retry.addEventListener('click', () => {
    if (root.hasAttribute('data-online')) return;
    retry.disabled = true; retry.textContent = 'Reconnecting\u2026';
    root.setAttribute('data-busy', ''); conn.textContent = 'Reconnecting';
    setTimeout(() => {
      if (navigator.onLine === false) { goOffline(); conn.textContent = 'Still offline'; }
      else goOnline();
    }, 1400);
  });
  window.addEventListener('online', goOnline);
  window.addEventListener('offline', goOffline);
})();
```
