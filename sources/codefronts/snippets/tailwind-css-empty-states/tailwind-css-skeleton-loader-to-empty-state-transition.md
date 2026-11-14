---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-skeleton-loader-to-empty-state-transition/"
title: "Tailwind CSS Skeleton Loader to Empty State Transition"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "The moment most products get wrong: a skeleton that resolves to nothing."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Skeleton Loader to Empty State Transition
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-skeleton-loader-to-empty-state-transition/

The moment most products get wrong: a skeleton that resolves to nothing. Here the shimmer rows fade out and the empty state fades in at the same footprint, the status chip and repo dot change in step, and aria-busy tells screen readers when the wait is over. Refetch replays it.
## HTML
```html
<div class="tes-16 group/root w-full min-h-svh bg-tes16-bg font-tes16-sans text-tes16-ink antialiased [color-scheme:dark]" data-state="loading">
  <div class="mx-auto grid w-full max-w-3xl gap-5 px-[clamp(1rem,4vw,2.5rem)] py-[clamp(1.5rem,5vw,3.5rem)]">
    <header class="flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-2.5">
        <i aria-hidden="true" class="size-2.5 animate-pulse rounded-full bg-tes16-warn group-data-[state=empty]/root:animate-none group-data-[state=empty]/root:bg-tes16-ok motion-reduce:animate-none"></i>
        <span class="font-tes16-mono text-sm font-medium">payments-core</span>
        <span class="rounded-md border border-tes16-line2 px-1.5 py-0.5 font-tes16-mono text-[11px] text-tes16-mut">main</span>
      </div>
      <button type="button" id="tes16-reload" class="group/btn inline-flex min-h-11 items-center gap-2 rounded-lg border border-tes16-line2 px-3.5 text-sm transition hover:bg-tes16-panel2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes16-acc"><svg class="size-4 group-data-[state=loading]/root:animate-spin motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M19 12a7 7 0 1 1-2.05-4.95M19 4v4h-4"/></svg>Refetch</button>
    </header>
    <section aria-labelledby="tes16-qt" class="overflow-hidden rounded-2xl border border-tes16-line bg-tes16-panel">
      <div class="flex items-center justify-between border-b border-tes16-line px-5 py-3.5">
        <span id="tes16-qt" class="text-sm font-medium">Review queue</span>
        <span id="tes16-state" role="status" class="rounded-full bg-tes16-warn/12 px-2.5 py-1 font-tes16-mono text-[11px] text-tes16-warn group-data-[state=empty]/root:bg-tes16-ok/12 group-data-[state=empty]/root:text-tes16-ok">loading</span>
      </div>
      <div id="tes16-slot" aria-busy="true" class="grid min-h-64">
        <div aria-hidden="true" class="grid content-start divide-y divide-tes16-line group-data-[state=empty]/root:hidden">
          <div class="flex items-center gap-3.5 px-5 py-4"><i class="size-9 flex-none animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] motion-reduce:animate-none"></i><span class="grid flex-1 gap-2"><i class="h-3 w-[62%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] motion-reduce:animate-none"></i><i class="h-2.5 w-[38%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] motion-reduce:animate-none"></i></span><i class="h-6 w-16 animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] motion-reduce:animate-none"></i></div>
          <div class="flex items-center gap-3.5 px-5 py-4"><i class="size-9 flex-none animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:120ms] motion-reduce:animate-none"></i><span class="grid flex-1 gap-2"><i class="h-3 w-[74%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:120ms] motion-reduce:animate-none"></i><i class="h-2.5 w-[44%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:120ms] motion-reduce:animate-none"></i></span><i class="h-6 w-16 animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:120ms] motion-reduce:animate-none"></i></div>
          <div class="flex items-center gap-3.5 px-5 py-4"><i class="size-9 flex-none animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:240ms] motion-reduce:animate-none"></i><span class="grid flex-1 gap-2"><i class="h-3 w-[56%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:240ms] motion-reduce:animate-none"></i><i class="h-2.5 w-[33%] animate-tes16-shimmer rounded bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:240ms] motion-reduce:animate-none"></i></span><i class="h-6 w-16 animate-tes16-shimmer rounded-full bg-[linear-gradient(90deg,var(--color-tes16-panel2)_25%,var(--color-tes16-line2)_50%,var(--color-tes16-panel2)_75%)] bg-size-[200%_100%] [animation-delay:240ms] motion-reduce:animate-none"></i></div>
        </div>
        <div class="hidden place-items-center p-8 transition-[opacity,translate] duration-500 ease-[cubic-bezier(.2,.8,.2,1)] group-data-[state=empty]/root:grid starting:translate-y-1 starting:opacity-0">
          <div class="grid max-w-sm justify-items-center text-center">
            <span aria-hidden="true" class="grid size-14 place-items-center rounded-2xl border border-tes16-line2 bg-tes16-panel2 text-tes16-acc shadow-[0_16px_40px_-12px_color-mix(in_oklab,var(--color-tes16-acc)_45%,transparent)]"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6z"/><circle cx="12" cy="12" r="2.6"/></svg></span>
            <p class="mt-4 font-semibold">No reviews assigned to you</p>
            <p class="mt-1.5 text-[13px]/5 text-tes16-mut text-pretty">Two teammates are on rotation this week. You will be paged here when something needs a second pair of eyes.</p>
            <div class="mt-5 flex flex-wrap justify-center gap-2">
              <button type="button" class="min-h-11 rounded-lg bg-tes16-ink px-4 text-sm font-medium text-tes16-bg transition hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes16-acc">Open the rotation</button>
              <button type="button" class="min-h-11 rounded-lg border border-tes16-line2 px-4 text-sm hover:bg-tes16-panel2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes16-acc">Watch this repository</button>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section aria-labelledby="tes16-ct" class="rounded-2xl border border-tes16-line bg-tes16-panel">
      <div class="flex items-center justify-between border-b border-tes16-line px-5 py-3.5"><span id="tes16-ct" class="text-sm font-medium">Checks</span><span class="rounded-full bg-tes16-ok/12 px-2.5 py-1 font-tes16-mono text-[11px] text-tes16-ok">passing</span></div>
      <ul class="grid gap-2.5 px-5 py-4 font-tes16-mono text-[12.5px] text-tes16-mut">
        <li class="flex items-center gap-2.5"><i aria-hidden="true" class="size-2 rounded-full bg-tes16-ok"></i>unit — 1m 42s</li>
        <li class="flex items-center gap-2.5"><i aria-hidden="true" class="size-2 rounded-full bg-tes16-ok"></i>contract — 3m 07s</li>
        <li class="flex items-center gap-2.5"><i aria-hidden="true" class="size-2 rounded-full bg-tes16-ok"></i>lint — 21s</li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes16-bg: #0d0f13;
  --color-tes16-bg: oklch(0.155 0.01 260);
  --color-tes16-panel: #13161c;
  --color-tes16-panel: oklch(0.195 0.012 260);
  --color-tes16-panel2: #1b1f27;
  --color-tes16-panel2: oklch(0.235 0.014 260);
  --color-tes16-line: #252a33;
  --color-tes16-line: oklch(0.285 0.014 260);
  --color-tes16-line2: #343a46;
  --color-tes16-line2: oklch(0.35 0.017 260);
  --color-tes16-ink: #eef1f6;
  --color-tes16-ink: oklch(0.96 0.006 260);
  --color-tes16-mut: #a2a9b8;
  --color-tes16-mut: oklch(0.74 0.02 260);
  --color-tes16-acc: #b69cff;
  --color-tes16-acc: oklch(0.76 0.13 295);
  --color-tes16-ok: #5fd69a;
  --color-tes16-ok: oklch(0.8 0.14 158);
  --color-tes16-warn: #f0b562;
  --color-tes16-warn: oklch(0.81 0.11 72);
  --font-tes16-sans: 'Geist', system-ui, sans-serif;
  --font-tes16-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tes16-shimmer: tes16-shimmer 1.4s linear infinite;

  @keyframes tes16-shimmer {
    from {
      background-position: 100% 0;
    }

    to {
      background-position: -100% 0;
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-16 {
  width: 100%;
  min-height: 100svh;
}

.tes-16 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-16');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const slot = root.querySelector('#tes16-slot'), state = root.querySelector('#tes16-state'), reload = root.querySelector('#tes16-reload');
  let t = 0;
  const settle = () => { root.dataset.state = 'empty'; slot.setAttribute('aria-busy', 'false'); state.textContent = 'no items'; reload.disabled = false; };
  const load = (ms) => {
    clearTimeout(t);
    root.dataset.state = 'loading'; slot.setAttribute('aria-busy', 'true'); state.textContent = 'loading'; reload.disabled = true;
    t = setTimeout(settle, ms);
  };
  reload.addEventListener('click', () => load(1500));
  load(1700);
})();
```
