---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-timeline-accordion-changelog/"
title: "Tailwind CSS Timeline Accordion for Changelogs"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A product changelog built as a vertical timeline: one gradient spine, a dot per release that fills emerald and fires a single ring pulse when its <details>…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Timeline Accordion for Changelogs
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-timeline-accordion-changelog/

A product changelog built as a vertical timeline: one gradient spine, a dot per release that fills emerald and fires a single ring pulse when its <details> opens, mono version badges and colour-coded New / Improved / Fixed rows. The spine is a before: line on the list, the dots are row-relative so they never drift, and the panel height animates with the details-content: variant plus [interpolate-size:allow-keywords].
## HTML
```html
<section class="tac-13 w-full min-h-svh grid place-items-center bg-tac13-bg bg-[radial-gradient(70%_50%_at_10%_0%,var(--color-tac13-glow),transparent_70%),radial-gradient(60%_40%_at_100%_100%,var(--color-tac13-glow2),transparent_70%)] px-5 py-14 font-tac13-sans text-tac13-ink [interpolate-size:allow-keywords]" aria-label="Timeline changelog accordion demo">
  <div class="grid w-full max-w-2xl gap-9">
    <header class="grid gap-3">
      <p class="inline-flex w-fit items-center gap-2 rounded-full bg-tac13-acc/10 px-3 py-1 text-xs font-semibold tracking-wide text-tac13-acc ring-1 ring-tac13-acc/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac13-acc shadow-[0_0_8px_var(--color-tac13-acc)]"></span>Changelog</p>
      <h2 class="text-[clamp(28px,5vw,38px)] leading-tight font-bold tracking-[-0.025em] text-balance">What’s new in Northwind</h2>
      <p class="max-w-lg text-[15px] leading-relaxed text-tac13-mut">New features, improvements and fixes, shipped every Tuesday. Expand a release for the full notes.</p>
    </header>

    <ol class="relative grid gap-1.5 before:absolute before:inset-y-4 before:left-[11px] before:w-0.5 before:rounded-full before:bg-linear-to-b before:from-tac13-acc/80 before:via-tac13-line before:to-transparent">
      <li class="relative pl-10">
        <details class="group rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 hover:bg-white/[0.025] open:bg-tac13-card open:shadow-[0_1px_0_inset_oklch(1_0_0/0.06),0_24px_48px_-24px_oklch(0_0_0/0.7)] open:ring-white/8 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none" open>
          <summary class="grid min-h-11 cursor-pointer list-none grid-cols-[1fr_auto] items-center gap-x-4 rounded-2xl px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac13-acc [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="absolute top-[22px] left-[5px] size-3.5 rounded-full border-2 border-tac13-dot bg-tac13-bg transition-[background-color,border-color,box-shadow] duration-300 after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-tac13-acc after:opacity-0 group-open:border-tac13-acc group-open:bg-tac13-acc group-open:shadow-[0_0_0_4px_oklch(0.79_0.15_163/0.15),0_0_14px_oklch(0.79_0.15_163/0.6)] group-open:after:animate-tac13-pulse motion-reduce:transition-none motion-reduce:group-open:after:animate-none"></span>
            <span class="grid gap-1.5">
              <span class="flex flex-wrap items-center gap-x-2.5 gap-y-1.5">
                <span class="rounded-md bg-white/6 px-2 py-0.5 font-tac13-mono text-[12px] font-medium text-tac13-ink ring-1 ring-white/10">v4.2.0</span>
                <span class="rounded-full bg-tac13-acc px-2 py-0.5 text-[11px] font-bold tracking-wide text-tac13-bg uppercase">Latest</span>
                <time datetime="2026-10-06" class="font-tac13-mono text-[12px] text-tac13-mut">Oct 6, 2026</time>
              </span>
              <span class="text-[17px] leading-snug font-semibold tracking-[-0.01em]">Offline-first sync engine</span>
            </span>
            <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-white/5 text-tac13-mut ring-1 ring-white/10 transition duration-300 group-open:rotate-180 group-open:bg-tac13-acc/12 group-open:text-tac13-acc group-open:ring-tac13-acc/30 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-4 px-4 pt-1 pb-5">
            <p class="text-[14.5px] leading-relaxed text-tac13-mut">Every workspace now resolves conflicts locally with CRDTs, so edits made on a plane merge cleanly the moment you land.</p>
            <ul class="grid gap-2.5 text-[14px] leading-snug">
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-new/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-new uppercase ring-1 ring-tac13-new/25">New</span><span>Full offline mode for docs, boards and comments</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-imp/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-imp uppercase ring-1 ring-tac13-imp/25">Improved</span><span>Initial load is 38% faster on large workspaces</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-fix/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-fix uppercase ring-1 ring-tac13-fix/25">Fixed</span><span>Cursor no longer jumps when a teammate pastes a table</span></li>
            </ul>
            <div class="flex flex-wrap items-center gap-3 border-t border-white/8 pt-4 text-[12.5px] text-tac13-mut">
              <span aria-hidden="true" class="flex -space-x-2"><span class="size-6 rounded-full bg-linear-to-br from-tac13-acc to-tac13-imp ring-2 ring-tac13-card"></span><span class="size-6 rounded-full bg-linear-to-br from-tac13-fix to-tac13-rose ring-2 ring-tac13-card"></span><span class="size-6 rounded-full bg-linear-to-br from-tac13-imp to-tac13-acc ring-2 ring-tac13-card"></span></span>
              <span>Shipped by Priya, Tomás and Ama · 14 pull requests</span>
            </div>
          </div>
        </details>
      </li>

      <li class="relative pl-10">
        <details class="group rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 hover:bg-white/[0.025] open:bg-tac13-card open:shadow-[0_1px_0_inset_oklch(1_0_0/0.06),0_24px_48px_-24px_oklch(0_0_0/0.7)] open:ring-white/8 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
          <summary class="grid min-h-11 cursor-pointer list-none grid-cols-[1fr_auto] items-center gap-x-4 rounded-2xl px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac13-acc [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="absolute top-[22px] left-[5px] size-3.5 rounded-full border-2 border-tac13-dot bg-tac13-bg transition-[background-color,border-color,box-shadow] duration-300 after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-tac13-acc after:opacity-0 group-open:border-tac13-acc group-open:bg-tac13-acc group-open:shadow-[0_0_0_4px_oklch(0.79_0.15_163/0.15),0_0_14px_oklch(0.79_0.15_163/0.6)] group-open:after:animate-tac13-pulse motion-reduce:transition-none motion-reduce:group-open:after:animate-none"></span>
            <span class="grid gap-1.5">
              <span class="flex flex-wrap items-center gap-x-2.5 gap-y-1.5">
                <span class="rounded-md bg-white/6 px-2 py-0.5 font-tac13-mono text-[12px] font-medium text-tac13-ink ring-1 ring-white/10">v4.1.0</span>
                <time datetime="2026-09-22" class="font-tac13-mono text-[12px] text-tac13-mut">Sep 22, 2026</time>
              </span>
              <span class="text-[17px] leading-snug font-semibold tracking-[-0.01em]">Shared workspaces &amp; live cursors</span>
            </span>
            <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-white/5 text-tac13-mut ring-1 ring-white/10 transition duration-300 group-open:rotate-180 group-open:bg-tac13-acc/12 group-open:text-tac13-acc group-open:ring-tac13-acc/30 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-4 px-4 pt-1 pb-5">
            <p class="text-[14.5px] leading-relaxed text-tac13-mut">Invite your whole team into one space with granular roles, workspace templates and real-time presence.</p>
            <ul class="grid gap-2.5 text-[14px] leading-snug">
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-new/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-new uppercase ring-1 ring-tac13-new/25">New</span><span>Live cursors and selection highlights for every member</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-new/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-new uppercase ring-1 ring-tac13-new/25">New</span><span>Viewer, editor and admin roles per workspace</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-fix/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-fix uppercase ring-1 ring-tac13-fix/25">Fixed</span><span>Invite emails no longer land in Gmail’s Promotions tab</span></li>
            </ul>
          </div>
        </details>
      </li>

      <li class="relative pl-10">
        <details class="group rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 hover:bg-white/[0.025] open:bg-tac13-card open:shadow-[0_1px_0_inset_oklch(1_0_0/0.06),0_24px_48px_-24px_oklch(0_0_0/0.7)] open:ring-white/8 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
          <summary class="grid min-h-11 cursor-pointer list-none grid-cols-[1fr_auto] items-center gap-x-4 rounded-2xl px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac13-acc [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="absolute top-[22px] left-[5px] size-3.5 rounded-full border-2 border-tac13-dot bg-tac13-bg transition-[background-color,border-color,box-shadow] duration-300 after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-tac13-acc after:opacity-0 group-open:border-tac13-acc group-open:bg-tac13-acc group-open:shadow-[0_0_0_4px_oklch(0.79_0.15_163/0.15),0_0_14px_oklch(0.79_0.15_163/0.6)] group-open:after:animate-tac13-pulse motion-reduce:transition-none motion-reduce:group-open:after:animate-none"></span>
            <span class="grid gap-1.5">
              <span class="flex flex-wrap items-center gap-x-2.5 gap-y-1.5">
                <span class="rounded-md bg-white/6 px-2 py-0.5 font-tac13-mono text-[12px] font-medium text-tac13-ink ring-1 ring-white/10">v4.0.0</span>
                <span class="rounded-full px-2 py-0.5 text-[11px] font-bold tracking-wide text-tac13-imp uppercase ring-1 ring-tac13-imp/40">Major</span>
                <time datetime="2026-09-01" class="font-tac13-mono text-[12px] text-tac13-mut">Sep 1, 2026</time>
              </span>
              <span class="text-[17px] leading-snug font-semibold tracking-[-0.01em]">A rebuilt editor, from the ground up</span>
            </span>
            <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-white/5 text-tac13-mut ring-1 ring-white/10 transition duration-300 group-open:rotate-180 group-open:bg-tac13-acc/12 group-open:text-tac13-acc group-open:ring-tac13-acc/30 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-4 px-4 pt-1 pb-5">
            <p class="text-[14.5px] leading-relaxed text-tac13-mut">Northwind 4 replaces the legacy renderer with a block-based engine. Existing documents migrate automatically on first open.</p>
            <ul class="grid gap-2.5 text-[14px] leading-snug">
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-new/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-new uppercase ring-1 ring-tac13-new/25">New</span><span>Slash commands, nested toggles and synced blocks</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-imp/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-imp uppercase ring-1 ring-tac13-imp/25">Improved</span><span>Typing latency under 8ms on 10,000-line documents</span></li>
            </ul>
          </div>
        </details>
      </li>

      <li class="relative pl-10">
        <details class="group rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 hover:bg-white/[0.025] open:bg-tac13-card open:shadow-[0_1px_0_inset_oklch(1_0_0/0.06),0_24px_48px_-24px_oklch(0_0_0/0.7)] open:ring-white/8 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
          <summary class="grid min-h-11 cursor-pointer list-none grid-cols-[1fr_auto] items-center gap-x-4 rounded-2xl px-4 py-3.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac13-acc [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="absolute top-[22px] left-[5px] size-3.5 rounded-full border-2 border-tac13-dot bg-tac13-bg transition-[background-color,border-color,box-shadow] duration-300 after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-tac13-acc after:opacity-0 group-open:border-tac13-acc group-open:bg-tac13-acc group-open:shadow-[0_0_0_4px_oklch(0.79_0.15_163/0.15),0_0_14px_oklch(0.79_0.15_163/0.6)] group-open:after:animate-tac13-pulse motion-reduce:transition-none motion-reduce:group-open:after:animate-none"></span>
            <span class="grid gap-1.5">
              <span class="flex flex-wrap items-center gap-x-2.5 gap-y-1.5">
                <span class="rounded-md bg-white/6 px-2 py-0.5 font-tac13-mono text-[12px] font-medium text-tac13-ink ring-1 ring-white/10">v3.9.4</span>
                <time datetime="2026-08-18" class="font-tac13-mono text-[12px] text-tac13-mut">Aug 18, 2026</time>
              </span>
              <span class="text-[17px] leading-snug font-semibold tracking-[-0.01em]">Keyboard-first command palette</span>
            </span>
            <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-white/5 text-tac13-mut ring-1 ring-white/10 transition duration-300 group-open:rotate-180 group-open:bg-tac13-acc/12 group-open:text-tac13-acc group-open:ring-tac13-acc/30 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-4 px-4 pt-1 pb-5">
            <p class="text-[14.5px] leading-relaxed text-tac13-mut">Press <kbd class="rounded border border-white/15 bg-white/5 px-1.5 py-px font-tac13-mono text-[12px] text-tac13-ink">⌘K</kbd> anywhere to jump to a page, run an action or change a setting without touching the mouse.</p>
            <ul class="grid gap-2.5 text-[14px] leading-snug">
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-imp/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-imp uppercase ring-1 ring-tac13-imp/25">Improved</span><span>Fuzzy search ranks recent pages first</span></li>
              <li class="flex items-start gap-3"><span class="mt-px w-[74px] flex-none rounded-md bg-tac13-fix/12 py-0.5 text-center text-[11px] font-bold tracking-wide text-tac13-fix uppercase ring-1 ring-tac13-fix/25">Fixed</span><span>Shortcuts now work with non-US keyboard layouts</span></li>
            </ul>
          </div>
        </details>
      </li>
    </ol>

    <p aria-hidden="true" class="justify-self-center rounded-full px-3.5 py-2 font-tac13-mono text-[11.5px] text-tac13-mut ring-1 ring-white/10">before: spine · group-open:after:animate-tac13-pulse · details-content:h-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac13-bg: #080f1c;
  --color-tac13-bg: oklch(0.17 0.03 260);
  --color-tac13-glow: #00473059;
  --color-tac13-glow: oklch(0.35 0.08 165 / 0.35);
  --color-tac13-glow2: #1b2a5266;
  --color-tac13-glow2: oklch(0.3 0.07 265 / 0.4);
  --color-tac13-card: #0f1828;
  --color-tac13-card: oklch(0.21 0.035 260);
  --color-tac13-ink: #e6ecf3;
  --color-tac13-ink: oklch(0.94 0.012 255);
  --color-tac13-mut: #9eacbe;
  --color-tac13-mut: oklch(0.74 0.03 255);
  --color-tac13-line: #3b485e;
  --color-tac13-line: oklch(0.4 0.04 260);
  --color-tac13-dot: #3b485e;
  --color-tac13-dot: oklch(0.4 0.04 260);
  --color-tac13-acc: #44d89f;
  --color-tac13-acc: oklch(0.79 0.15 163);
  --color-tac13-new: #44d89f;
  --color-tac13-new: oklch(0.79 0.15 163);
  --color-tac13-imp: #82d7ff;
  --color-tac13-imp: oklch(0.84 0.1 230);
  --color-tac13-fix: #f5c252;
  --color-tac13-fix: oklch(0.84 0.14 84);
  --color-tac13-rose: #fb9890;
  --color-tac13-rose: oklch(0.78 0.12 25);
  --font-tac13-sans: 'Manrope', system-ui, sans-serif;
  --font-tac13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tac13-pulse: tac13-pulse 0.8s cubic-bezier(0.2, 0.6, 0.3, 1);

  @keyframes tac13-pulse {
    from {
      opacity: 0.9;
      transform: scale(1);
    }

    to {
      opacity: 0;
      transform: scale(2.6);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-13 {
  width: 100%;
  min-height: 100svh;
}
```
