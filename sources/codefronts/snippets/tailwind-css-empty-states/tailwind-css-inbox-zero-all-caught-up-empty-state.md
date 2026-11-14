---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-inbox-zero-all-caught-up-empty-state/"
title: "Tailwind CSS Inbox Zero / All Caught Up Empty State"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A three-pane mail client at inbox zero: a celebratory but calm badge in the list, a quiet \"no message selected\" reader, and an undo path."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Inbox Zero / All Caught Up Empty State
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-inbox-zero-all-caught-up-empty-state/

A three-pane mail client at inbox zero: a celebratory but calm badge in the list, a quiet "no message selected" reader, and an undo path. Archive the restored thread and the badge draws itself back in with starting: — the moment of zero is the reward, so it gets the only animation on screen.
## HTML
```html
<div class="tes-04 group/root w-full min-h-svh bg-tes04-bg font-tes04-sans text-tes04-ink antialiased" data-mail="none">
  <div class="grid min-h-svh md:grid-cols-[13rem_minmax(0,21rem)_minmax(0,1fr)]">
    <aside aria-label="Mailboxes" class="hidden flex-col gap-5 border-r border-tes04-line p-4 md:flex">
      <button type="button" class="flex min-h-11 items-center gap-2 rounded-xl bg-tes04-ink px-4 text-sm font-medium text-white shadow-sm transition hover:bg-tes04-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>Compose</button>
      <nav class="grid gap-0.5 text-sm">
        <a href="#" aria-current="page" class="flex min-h-10 items-center justify-between rounded-lg bg-tes04-acc/10 px-3 font-medium text-tes04-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Inbox<span id="tes04-n" class="font-tes04-mono text-xs">0</span></a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Starred</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Snoozed</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Sent</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Archive</a>
      </nav>
      <div class="grid gap-0.5 text-sm">
        <p class="px-3 pb-1 text-[11px] font-medium tracking-[0.12em] text-tes04-mut uppercase">Labels</p>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><i aria-hidden="true" class="size-2 rounded-full bg-tes04-l1"></i>Customers</a>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><i aria-hidden="true" class="size-2 rounded-full bg-tes04-l2"></i>Suppliers</a>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-tes04-mut hover:bg-tes04-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><i aria-hidden="true" class="size-2 rounded-full bg-tes04-l3"></i>Finance</a>
      </div>
    </aside>
    <section aria-label="Inbox" class="flex flex-col border-r border-tes04-line bg-tes04-card">
      <header class="flex min-h-15 items-center justify-between border-b border-tes04-line px-4">
        <span class="text-[15px] font-semibold">Inbox</span>
        <div class="flex">
          <button type="button" aria-label="Refresh" class="grid size-11 place-items-center rounded-lg text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><svg class="size-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M19 12a7 7 0 1 1-2.05-4.95M19 4v4h-4"/></svg></button>
          <button type="button" aria-label="Filter" class="grid size-11 place-items-center rounded-lg text-tes04-mut hover:bg-tes04-sunk hover:text-tes04-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc"><svg class="size-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 6h16M7 12h10M10 18h4"/></svg></button>
        </div>
      </header>
      <div aria-live="polite" class="flex flex-1 flex-col">
        <div class="grid flex-1 place-items-center p-8 group-data-[mail=some]/root:hidden">
          <div class="grid justify-items-center text-center transition-[opacity,scale] duration-500 ease-[cubic-bezier(.2,.8,.2,1)] starting:scale-90 starting:opacity-0">
            <span aria-hidden="true" class="relative grid size-20 place-items-center rounded-full bg-[radial-gradient(circle_at_30%_25%,var(--color-tes04-card),color-mix(in_oklab,var(--color-tes04-ok)_15%,transparent))] text-tes04-ok ring-1 ring-tes04-ok/25 before:absolute before:-inset-3 before:rounded-full before:border before:border-dashed before:border-tes04-ok/30 before:animate-[spin_24s_linear_infinite] motion-reduce:before:animate-none"><svg class="size-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 13.5h5l1.5 2.5h4l1.5-2.5h5"/><path d="M5.5 6.5h13l2 7v4.5a1.5 1.5 0 0 1-1.5 1.5h-14A1.5 1.5 0 0 1 3.5 18v-4.5z"/><path d="m9.5 10 2 2 3.5-3.5"/></svg></span>
            <p id="tes04-zero" tabindex="-1" class="mt-6 font-tes04-serif text-[2rem] leading-none tracking-tight outline-none">Inbox zero</p>
            <p class="mt-2.5 max-w-[26ch] text-sm/6 text-tes04-mut text-pretty">Last message cleared at 09:14. Nothing new until the next sync.</p>
            <button type="button" id="tes04-undo" class="mt-5 min-h-11 rounded-full border border-tes04-line px-4 text-sm transition hover:border-tes04-ink/30 hover:bg-tes04-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Undo last archive</button>
          </div>
        </div>
        <ol class="hidden group-data-[mail=some]/root:block">
          <li class="flex gap-3 border-b border-l-2 border-tes04-line border-l-tes04-acc bg-tes04-acc/5 px-4 py-3.5 transition-opacity duration-300 starting:opacity-0">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-tes04-l2 text-xs font-semibold text-white">RB</span>
            <span class="grid min-w-0 gap-0.5"><span class="flex justify-between gap-2 text-sm"><b class="font-semibold">Rosa Bianchi</b><span class="font-tes04-mono text-xs text-tes04-mut">09:12</span></span><span class="truncate text-[13px]">Re: Q3 supplier contract — signed copy</span><span class="truncate text-xs text-tes04-mut">Attaching the countersigned version. One clause moved to page four…</span></span>
          </li>
        </ol>
      </div>
    </section>
    <section aria-label="Message" class="flex min-h-80 flex-col">
      <div class="grid flex-1 place-items-center p-8 group-data-[mail=some]/root:hidden">
        <div class="grid justify-items-center gap-3 text-center text-tes04-mut">
          <span aria-hidden="true" class="grid h-14 w-20 grid-rows-3 gap-1.5 rounded-xl border border-tes04-line p-3"><i class="rounded-full bg-tes04-line"></i><i class="w-3/4 rounded-full bg-tes04-line"></i><i class="w-1/2 rounded-full bg-tes04-line"></i></span>
          <p class="text-sm">No message selected</p>
        </div>
      </div>
      <article class="hidden flex-1 flex-col group-data-[mail=some]/root:flex">
        <header class="grid gap-4 border-b border-tes04-line px-[clamp(1rem,3vw,2rem)] py-6">
          <h1 id="tes04-subj" tabindex="-1" class="font-tes04-serif text-[clamp(1.5rem,2.6vw,2rem)] leading-tight tracking-tight outline-none text-balance">Re: Q3 supplier contract — signed copy</h1>
          <div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-tes04-l2 text-xs font-semibold text-white">RB</span><span class="grid text-sm"><b class="font-semibold">Rosa Bianchi</b><span class="text-xs text-tes04-mut">to me · 09:12</span></span></div>
        </header>
        <div class="grid max-w-prose gap-4 px-[clamp(1rem,3vw,2rem)] py-6 text-[15px]/7">
          <p>Attaching the countersigned version. One clause moved to page four, everything else is as agreed on the call.</p>
          <p>If the finance team needs the original stamped copy I can courier it this week.</p>
          <p>Rosa</p>
        </div>
        <div class="mt-auto flex gap-2.5 border-t border-tes04-line px-[clamp(1rem,3vw,2rem)] py-4">
          <button type="button" class="min-h-11 rounded-full bg-tes04-ink px-5 text-sm font-medium text-white transition hover:bg-tes04-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Reply</button>
          <button type="button" id="tes04-arch" class="inline-flex min-h-11 items-center gap-2 rounded-full border border-tes04-line px-4 text-sm transition hover:bg-tes04-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes04-acc">Archive<kbd class="rounded border border-tes04-line px-1 font-tes04-mono text-[11px] text-tes04-mut">E</kbd></button>
        </div>
      </article>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes04-bg: #f6f6f3;
  --color-tes04-bg: oklch(0.97 0.004 100);
  --color-tes04-card: #ffffff;
  --color-tes04-card: oklch(1 0 0);
  --color-tes04-sunk: #efefeb;
  --color-tes04-sunk: oklch(0.946 0.005 100);
  --color-tes04-line: #e2e2dc;
  --color-tes04-line: oklch(0.904 0.007 100);
  --color-tes04-ink: #1d1e1b;
  --color-tes04-ink: oklch(0.22 0.006 110);
  --color-tes04-mut: #5f615a;
  --color-tes04-mut: oklch(0.47 0.01 110);
  --color-tes04-acc: #2f63d8;
  --color-tes04-acc: oklch(0.53 0.18 262);
  --color-tes04-ok: #19885f;
  --color-tes04-ok: oklch(0.56 0.12 160);
  --color-tes04-l1: #d9822b;
  --color-tes04-l1: oklch(0.67 0.15 60);
  --color-tes04-l2: #8a5cd6;
  --color-tes04-l2: oklch(0.56 0.18 295);
  --color-tes04-l3: #1f9aa8;
  --color-tes04-l3: oklch(0.62 0.1 205);
  --font-tes04-sans: 'Geist', system-ui, sans-serif;
  --font-tes04-serif: 'Instrument Serif', Georgia, serif;
  --font-tes04-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-04 {
  width: 100%;
  min-height: 100svh;
}

.tes-04 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-04');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const show = (has, move) => {
    root.dataset.mail = has ? 'some' : 'none';
    root.querySelector('#tes04-n').textContent = has ? '1' : '0';
    if (move) requestAnimationFrame(() => root.querySelector(has ? '#tes04-subj' : '#tes04-zero').focus());
  };
  root.querySelector('#tes04-undo').addEventListener('click', () => show(true, true));
  root.querySelector('#tes04-arch').addEventListener('click', () => show(false, true));
  root.addEventListener('keydown', (e) => {
    if (e.key.toLowerCase() === 'e' && root.dataset.mail === 'some' && !e.target.closest('input,textarea')) show(false, true);
  });
  show(false, false);
})();
```
