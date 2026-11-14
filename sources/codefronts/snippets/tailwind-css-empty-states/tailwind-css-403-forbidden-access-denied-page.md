---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-403-forbidden-access-denied-page/"
title: "Tailwind CSS 403 Forbidden / Access Denied Page"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A restricted document rendered as a blurred silhouette behind a calm access card — the user can see the file exists, not what it says."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 403 Forbidden / Access Denied Page
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-403-forbidden-access-denied-page/

A restricted document rendered as a blurred silhouette behind a calm access card — the user can see the file exists, not what it says. "Request access" swaps the actions for a pending confirmation naming the two owners, and a withdraw link reverses it, all through one data-pending attribute.
## HTML
```html
<div class="tes-13 group/root relative isolate w-full min-h-svh overflow-hidden bg-tes13-bg font-tes13-sans text-tes13-ink antialiased">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 select-none">
    <div class="flex items-center gap-4 border-b border-tes13-line bg-tes13-card px-6 py-3.5 text-sm"><span class="font-semibold">Vellum</span><span class="truncate text-tes13-mut">Legal / Vendor agreements / Northline MSA</span></div>
    <div class="mx-auto mt-10 grid max-w-3xl gap-3.5 rounded-xl bg-tes13-card p-12 shadow-sm blur-[6px]">
      <span class="mb-4 h-7 w-2/3 rounded bg-tes13-ink/70"></span>
      <span class="h-3 w-[92%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[84%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[96%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[61%] rounded bg-tes13-ink/25"></span>
      <span class="mt-5 mb-2 h-5 w-1/3 rounded bg-tes13-ink/50"></span>
      <span class="h-3 w-[88%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[79%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[93%] rounded bg-tes13-ink/25"></span><span class="h-3 w-[48%] rounded bg-tes13-ink/25"></span>
    </div>
  </div>
  <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[radial-gradient(60%_60%_at_50%_50%,transparent,var(--color-tes13-bg))]"></div>
  <div class="grid min-h-svh place-items-center px-5 py-16">
    <section role="region" aria-labelledby="tes13-h" class="grid w-full max-w-md justify-items-center rounded-3xl bg-tes13-card p-[clamp(1.5rem,4vw,2.25rem)] text-center shadow-[0_40px_90px_-30px_oklch(0.25_0.04_280/0.4)] ring-1 ring-tes13-line supports-[backdrop-filter:blur(1px)]:bg-tes13-card/80 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
      <span aria-hidden="true" class="grid size-16 place-items-center rounded-2xl bg-tes13-ink text-white shadow-[0_12px_30px_-8px_oklch(0.25_0.04_280/0.5)] group-data-pending/root:bg-tes13-acc"><svg class="size-7 group-data-pending/root:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5M12 14.5v2.5"/></svg><svg class="hidden size-7 group-data-pending/root:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8"/><path d="M12 7.5V12l3 2"/></svg></span>
      <p class="mt-5 font-tes13-mono text-xs font-medium tracking-[0.2em] text-tes13-mut">ERROR 403</p>
      <h1 id="tes13-h" class="mt-2 text-[clamp(1.4rem,3vw,1.75rem)] font-semibold tracking-tight text-balance">This document is restricted</h1>
      <p id="tes13-p" aria-live="polite" class="mt-2 text-sm/6 text-tes13-mut text-pretty">Northline MSA is limited to the legal group. Your account can see the file exists, but not its contents.</p>
      <div class="mt-6 flex flex-wrap justify-center gap-2.5 group-data-pending/root:hidden">
        <button type="button" id="tes13-req" class="min-h-11 rounded-xl bg-tes13-ink px-5 text-sm font-medium text-white transition hover:bg-tes13-acc active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes13-acc">Request access</button>
        <button type="button" class="min-h-11 rounded-xl border border-tes13-line2 px-4 text-sm hover:bg-tes13-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes13-acc">Ask in #legal</button>
      </div>
      <div class="mt-6 hidden w-full gap-3 group-data-pending/root:grid">
        <p class="flex items-center justify-center gap-2 rounded-xl bg-tes13-acc/10 px-4 py-3 text-sm font-medium text-tes13-acc"><svg class="size-4 flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Request sent to both document owners</p>
        <button type="button" id="tes13-undo" class="min-h-11 text-xs text-tes13-mut underline-offset-4 hover:text-tes13-ink hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes13-acc">Withdraw request</button>
      </div>
      <dl class="mt-6 flex w-full items-center justify-between gap-4 border-t border-tes13-line pt-5 text-left text-xs">
        <div class="flex items-center gap-2.5"><dt class="sr-only">Owners</dt><dd class="flex -space-x-2"><span title="Priya Raman" class="grid size-8 place-items-center rounded-full bg-[#f2c9a6] text-[11px] font-semibold text-[#6b3a14] ring-2 ring-tes13-card">PR</span><span title="Marc Delacroix" class="grid size-8 place-items-center rounded-full bg-[#c9d6f7] text-[11px] font-semibold text-[#253f87] ring-2 ring-tes13-card">MD</span></dd><dd class="text-tes13-mut">Priya Raman, Marc Delacroix</dd></div>
        <div class="text-right"><dt class="text-tes13-mut">Group</dt><dd class="font-tes13-mono">legal-core</dd></div>
      </dl>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes13-bg: #f1f1f5;
  --color-tes13-bg: oklch(0.96 0.005 285);
  --color-tes13-card: #ffffff;
  --color-tes13-card: oklch(1 0 0);
  --color-tes13-sunk: #ededf2;
  --color-tes13-sunk: oklch(0.95 0.006 285);
  --color-tes13-line: #e0e0e8;
  --color-tes13-line: oklch(0.905 0.009 285);
  --color-tes13-line2: #c6c6d2;
  --color-tes13-line2: oklch(0.83 0.015 285);
  --color-tes13-ink: #1b1a24;
  --color-tes13-ink: oklch(0.21 0.017 285);
  --color-tes13-mut: #5d5c6b;
  --color-tes13-mut: oklch(0.48 0.022 285);
  --color-tes13-acc: #4f46c8;
  --color-tes13-acc: oklch(0.49 0.19 278);
  --font-tes13-sans: 'Geist', system-ui, sans-serif;
  --font-tes13-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-13 {
  width: 100%;
  min-height: 100svh;
}

.tes-13 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-13');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const p = root.querySelector('#tes13-p');
  const base = p.textContent;
  root.querySelector('#tes13-req').addEventListener('click', () => {
    root.setAttribute('data-pending', '');
    p.textContent = 'Priya or Marc can approve it. You will get a notification the moment one of them does.';
    root.querySelector('#tes13-undo').focus();
  });
  root.querySelector('#tes13-undo').addEventListener('click', () => {
    root.removeAttribute('data-pending');
    p.textContent = base;
    root.querySelector('#tes13-req').focus();
  });
})();
```
