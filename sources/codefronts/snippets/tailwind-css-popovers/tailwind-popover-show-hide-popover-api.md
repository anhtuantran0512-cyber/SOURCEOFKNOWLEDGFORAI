---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-show-hide-popover-api/"
title: "Tailwind Popover Show and Hide with the Popover API"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "The reference build the collection reuses: one button with popovertarget, one panel with popover, zero script."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Popover Show and Hide with the Popover API
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-show-hide-popover-api/

The reference build the collection reuses: one button with popovertarget, one panel with popover, zero script. In v4 the open state is just the open: variant — it already matches :popover-open — so the panel's closed, open and entry states live in one class list, and the trigger's chevron flips via group-has-[#tpop-01-panel:popover-open]/root:rotate-180.
## HTML
```html
<section class="tpop-01 transition-[--tpop01-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop01-d:1] [[data-theme=dark]_&]:[--tpop01-d:1] [[data-theme=light]_&]:[--tpop01-d:0] group/root w-full min-h-svh bg-tpop01-paper bg-[radial-gradient(90%_60%_at_50%_0%,var(--color-tpop01-glow),transparent_70%)] px-4.5 py-10 font-tpop01-sans text-tpop01-ink antialiased" aria-label="Tailwind popover show and hide demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="isolate w-full min-w-0 max-w-[40rem] overflow-hidden rounded-2xl border border-tpop01-rule bg-tpop01-surface shadow-[0_1px_2px_oklch(0.2_0.02_70/0.06),0_24px_48px_-32px_oklch(0.2_0.02_70/0.4)]">
      <header class="flex flex-wrap items-center justify-between gap-3 border-b border-tpop01-rule px-4 py-2">
        <div class="flex min-w-0 items-center gap-2.5">
          <span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-tpop01-ink text-tpop01-surface">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h12M4 10h12M4 15h7"/></svg>
          </span>
          <span class="text-[13.5px] font-semibold tracking-[-0.01em]">Atlas Docs</span>
        </div>
        <nav class="flex min-w-0 flex-wrap items-center gap-1" aria-label="Documentation">
          <span class="px-2.5 text-[13px] text-tpop01-mut">Guides</span>
          <span class="px-2.5 text-[13px] text-tpop01-mut">Reference</span>
          <button id="tpop-01-trigger" type="button" popovertarget="tpop-01-panel" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl bg-tpop01-ink px-3.5 text-[13px] font-semibold text-tpop01-surface transition-colors hover:bg-tpop01-ink/85 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop01-acc group-has-[#tpop-01-panel:popover-open]/root:bg-tpop01-ink/80">
            Release notes
            <span class="rounded-full bg-tpop01-acc px-1.5 py-0.5 font-tpop01-mono text-[10px] leading-none text-tpop01-surface">3</span>
            <svg class="transition-transform duration-200 motion-reduce:transition-none group-has-[#tpop-01-panel:popover-open]/root:rotate-180" viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
          </button>
        </nav>
      </header>
      <article class="px-5 pt-7 pb-8">
        <p class="mb-2.5 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop01-acc">Platform</p>
        <h2 class="mb-3.5 text-[clamp(22px,4.6vw,30px)] font-semibold leading-[1.15] tracking-[-0.025em] text-balance">Floating panels, no positioning library</h2>
        <p class="mb-3 text-[15px] leading-[1.7] text-tpop01-mut text-pretty">The button above is an invoker: it carries <code class="rounded bg-tpop01-ink/6 px-1.5 py-0.5 font-tpop01-mono text-[0.86em] text-tpop01-ink">popovertarget</code> and points at an element with the <code class="rounded bg-tpop01-ink/6 px-1.5 py-0.5 font-tpop01-mono text-[0.86em] text-tpop01-ink">popover</code> attribute. Open it, then click anywhere on this paragraph — the panel closes itself.</p>
        <p class="text-[15px] leading-[1.7] text-tpop01-mut text-pretty">This card has <code class="rounded bg-tpop01-ink/6 px-1.5 py-0.5 font-tpop01-mono text-[0.86em] text-tpop01-ink">overflow-hidden</code> and its own stacking context, and the panel still paints over it. That is the top layer, not a large z-index.</p>
      </article>
      <div popover="auto" id="tpop-01-panel" role="group" aria-labelledby="tpop-01-title" class="fixed m-auto w-[min(30rem,calc(100vw-32px))] rounded-2xl border border-tpop01-rule bg-tpop01-surface p-4.5 text-tpop01-ink opacity-0 scale-[0.98] shadow-[0_32px_64px_-24px_oklch(0.2_0.02_70/0.45)] transition-[opacity,scale,display,overlay] duration-200 ease-out transition-discrete open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-[0.98] motion-reduce:transition-none">
        <div class="mb-3 flex items-center justify-between gap-2.5">
          <h3 id="tpop-01-title" class="text-[13.5px] font-semibold">Release notes</h3>
          <button type="button" popovertarget="tpop-01-panel" popovertargetaction="hide" aria-label="Close release notes" class="-my-3 -mr-2.5 inline-flex size-11 cursor-pointer items-center justify-center rounded-lg text-tpop01-mut transition-colors hover:bg-tpop01-ink/6 hover:text-tpop01-ink focus-visible:outline-3 focus-visible:outline-offset-1 focus-visible:outline-tpop01-acc">
            <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
          </button>
        </div>
        <ul class="grid gap-px overflow-hidden rounded-xl border border-tpop01-rule bg-tpop01-rule">
          <li class="flex min-w-0 items-baseline gap-3 bg-tpop01-surface px-3 py-3 text-[13.5px] leading-normal"><span class="flex-none rounded-md bg-tpop01-acc/12 px-1.5 py-0.5 font-tpop01-mono text-[11px] font-semibold text-tpop01-acc">4.2.0</span> Query cache keys are now stable across workers.</li>
          <li class="flex min-w-0 items-baseline gap-3 bg-tpop01-surface px-3 py-3 text-[13.5px] leading-normal"><span class="flex-none rounded-md bg-tpop01-ink/6 px-1.5 py-0.5 font-tpop01-mono text-[11px] font-semibold text-tpop01-mut">4.1.6</span> Fixed a regression in the CSV importer on Windows line endings.</li>
          <li class="flex min-w-0 items-baseline gap-3 bg-tpop01-surface px-3 py-3 text-[13.5px] leading-normal"><span class="flex-none rounded-md bg-tpop01-ink/6 px-1.5 py-0.5 font-tpop01-mono text-[11px] font-semibold text-tpop01-mut">4.1.5</span> Audit log entries keep the actor when a token is rotated.</li>
        </ul>
        <p class="mt-3 flex flex-wrap items-center gap-1.5 text-[12.5px] leading-relaxed text-tpop01-mut"><kbd class="rounded-md border border-tpop01-rule border-b-2 px-1.5 py-0.5 font-tpop01-mono text-[11px] text-tpop01-ink">Esc</kbd> or a click outside closes this. Neither needed a line of JavaScript.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop01-paper: #f7f5f1;
  --color-tpop01-paper: oklch(0.97 0.006 85);
  --color-tpop01-glow: #fffdfa;
  --color-tpop01-glow: oklch(0.995 0.004 85);
  --color-tpop01-surface: #ffffff;
  --color-tpop01-surface: oklch(1 0 0);
  --color-tpop01-ink: #1e1a14;
  --color-tpop01-ink: oklch(0.22 0.012 75);
  --color-tpop01-mut: #605a51;
  --color-tpop01-mut: oklch(0.47 0.016 75);
  --color-tpop01-rule: #e4e1da;
  --color-tpop01-rule: oklch(0.91 0.01 85);
  --color-tpop01-acc: #be4b13;
  --color-tpop01-acc: oklch(0.56 0.16 42);
  --font-tpop01-sans: 'Geist', system-ui, sans-serif;
  --font-tpop01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop01-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-01 {
  width: 100%;
  min-height: 100svh;
  --color-tpop01-paper: color-mix(in oklch, oklch(0.17 0.008 75) calc(var(--tpop01-d) * 100%), oklch(0.97 0.006 85));
  --color-tpop01-glow: color-mix(in oklch, oklch(0.21 0.012 75) calc(var(--tpop01-d) * 100%), oklch(0.995 0.004 85));
  --color-tpop01-surface: color-mix(in oklch, oklch(0.205 0.01 75) calc(var(--tpop01-d) * 100%), oklch(1 0 0));
  --color-tpop01-ink: color-mix(in oklch, oklch(0.95 0.008 85) calc(var(--tpop01-d) * 100%), oklch(0.22 0.012 75));
  --color-tpop01-mut: color-mix(in oklch, oklch(0.74 0.016 80) calc(var(--tpop01-d) * 100%), oklch(0.47 0.016 75));
  --color-tpop01-rule: color-mix(in oklch, oklch(0.3 0.012 75) calc(var(--tpop01-d) * 100%), oklch(0.91 0.01 85));
  --color-tpop01-acc: color-mix(in oklch, oklch(0.72 0.14 45) calc(var(--tpop01-d) * 100%), oklch(0.56 0.16 42));
}
```
