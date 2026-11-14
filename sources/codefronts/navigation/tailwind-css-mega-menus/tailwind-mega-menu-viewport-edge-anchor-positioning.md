---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-viewport-edge-anchor-positioning/"
title: "Tailwind Mega Menu Viewport Edge Positioning with Anchor Positioning"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A docs utility bar whose only mega item sits at the far right &mdash; exactly where panels fall off the viewport."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu Viewport Edge Positioning with Anchor Positioning
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-viewport-edge-anchor-positioning/

A docs utility bar whose only mega item sits at the far right &mdash; exactly where panels fall off the viewport. The panel is end-aligned to its trigger, capped at min(34rem, 100vw - 2rem), and, where CSS anchor positioning exists, tethered to the trigger with position-try-fallbacks: flip-inline so it flips rather than clips. An invisible hover bridge closes the 8px gap. Zero JavaScript.
## HTML
```html
<section class="tmm-05 relative w-full min-h-svh overflow-x-clip bg-tmm05-bg font-tmm05-sans leading-relaxed text-tmm05-ink [&_:focus-visible]:rounded [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm05-acc" aria-labelledby="tmm05-title">
  <h2 class="sr-only" id="tmm05-title">Sable developer documentation</h2>

  <div class="absolute top-[11px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm05-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-lg border border-tmm05-line bg-tmm05-surf text-tmm05-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm05-acc" for="tmm05-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm05-line bg-tmm05-surf">
    <div class="mx-auto flex min-h-[66px] w-[min(76rem,calc(100%-2rem))] flex-wrap items-center gap-3 pr-15 max-[56rem]:flex-col max-[56rem]:items-stretch max-[56rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm05-display text-base/none font-bold tracking-[-0.03em] text-tmm05-ink" href="#tmm05-title">
        <svg class="size-5 text-tmm05-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16v12H4Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 10h8M8 14h5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        Sable <span class="font-medium text-tmm05-mut">docs</span>
      </a>
      <span class="inline-flex h-[22px] w-fit items-center gap-1 rounded-full border border-tmm05-line px-2 font-tmm05-display text-[0.68rem]/none font-semibold text-tmm05-mut"><span aria-hidden="true" class="size-1.5 rounded-full bg-tmm05-acc"></span>v4.2</span>
      <span class="inline-flex min-h-[38px] min-w-0 flex-[0_1_17rem] items-center gap-2 rounded-lg border border-tmm05-line bg-tmm05-ink/4 px-3 text-[0.83rem] text-tmm05-mut" aria-hidden="true">
        <svg class="size-[15px] flex-none" viewBox="0 0 24 24" focusable="false"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <span class="truncate">Search the docs</span>
        <kbd class="ml-auto rounded border border-tmm05-line bg-tmm05-surf px-1.5 font-tmm05-display text-[0.68rem]/[1.5] font-semibold">&#8984;K</kbd>
      </span>

      <nav class="ml-auto min-w-0 max-[56rem]:ml-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-0.5 max-[56rem]:flex-col">
          <li><a class="inline-flex min-h-11 items-center rounded-lg px-3 text-[0.88rem]/none font-semibold text-tmm05-ink hover:text-tmm05-acc" href="#tmm05-title">Guides</a></li>
          <li><a class="inline-flex min-h-11 items-center rounded-lg px-3 text-[0.88rem]/none font-semibold text-tmm05-ink hover:text-tmm05-acc" href="#tmm05-title">API</a></li>
          <li data-tmm05-item class="relative">
            <button type="button" aria-expanded="false" aria-controls="tmm05-panel-resources" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-lg px-3 text-[0.88rem]/none font-semibold text-tmm05-ink [anchor-name:--tmm05-a] transition-colors hover:text-tmm05-acc tmm05-open:bg-tmm05-acc/14 tmm05-open:text-tmm05-acc!">Resources
              <svg class="size-3.5 transition-transform duration-200 tmm05-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="invisible absolute top-full right-0 z-30 mt-2 grid w-[min(34rem,calc(100vw-2rem))] -translate-y-1.5 gap-3 rounded-xl border border-tmm05-line bg-tmm05-surf p-[clamp(0.9rem,2.4vw,1.2rem)] opacity-0 shadow-tmm05-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 before:absolute before:inset-x-0 before:-top-3.5 before:h-3.5 tmm05-open:visible tmm05-open:translate-y-0 tmm05-open:opacity-100 tmm05-open:pointer-events-auto supports-[anchor-name:--a]:tmm05-open:fixed supports-[anchor-name:--a]:tmm05-open:[position-anchor:--tmm05-a] supports-[anchor-name:--a]:tmm05-open:top-[calc(anchor(bottom)+8px)] supports-[anchor-name:--a]:tmm05-open:right-[anchor(right)] supports-[anchor-name:--a]:tmm05-open:left-auto supports-[anchor-name:--a]:tmm05-open:[position-try-fallbacks:flip-inline] motion-reduce:transition-none max-[56rem]:static! max-[56rem]:hidden max-[56rem]:w-full max-[56rem]:visible max-[56rem]:translate-y-0 max-[56rem]:opacity-100 max-[56rem]:shadow-none max-[56rem]:tmm05-open:grid" id="tmm05-panel-resources" aria-label="Resources">
              <div class="grid origin-top-right scale-97 grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-x-5 gap-y-2 opacity-0 transition-[opacity,scale] duration-[180ms,300ms] ease-tmm05-out tmm05-open:scale-100 tmm05-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none">
                <section class="min-w-0" aria-labelledby="tmm05-h-learn">
                    <h3 class="mb-1 font-tmm05-display text-[0.66rem]/none font-bold tracking-[0.16em] text-tmm05-mut uppercase" id="tmm05-h-learn">Learn</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">01</span>Quickstart</a></li>
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">02</span>Tutorials</a></li>
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">{}</span>Example repos</a></li>
                    </ul>
                  </section>
                <section class="min-w-0" aria-labelledby="tmm05-h-ref">
                    <h3 class="mb-1 font-tmm05-display text-[0.66rem]/none font-bold tracking-[0.16em] text-tmm05-mut uppercase" id="tmm05-h-ref">Reference</h3>
                    <ul class="grid gap-px">
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">&gt;_</span>CLI commands</a></li>
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">!</span>Error codes</a></li>
                      <li><a href="#tmm05-title" class="-mx-2 flex min-h-11 items-center gap-2.5 rounded-md px-2 text-[0.88rem] text-tmm05-ink transition-colors hover:bg-tmm05-acc/10 hover:text-tmm05-acc"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-md border border-tmm05-line font-tmm05-mono text-[0.62rem] text-tmm05-mut">%</span>Rate limits</a></li>
                    </ul>
                  </section>
              </div>
              <a class="group/cta grid gap-0.5 rounded-[10px] bg-tmm05-acc/12 px-3.5 py-3 text-tmm05-ink opacity-0 transition-[opacity,background-color] delay-90 duration-220 hover:bg-tmm05-acc/18 tmm05-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none" href="#tmm05-title">
                <b class="flex items-center gap-2 font-tmm05-display text-[0.88rem]/tight font-semibold text-tmm05-acc"><span class="rounded-full bg-tmm05-acc px-1.5 py-0.5 text-[0.6rem] tracking-[0.08em] text-tmm05-on-acc uppercase">New</span>Release notes &mdash; v4.2<span aria-hidden="true" class="ml-auto transition-transform group-hover/cta:translate-x-1">&rarr;</span></b>
                <span class="text-[0.8rem] text-tmm05-mut text-pretty">Regional read replicas and a smaller CLI binary.</span>
              </a>
            </div>
          </li>
        </ul>
      </nav>
      <a class="inline-flex min-h-10 w-fit items-center rounded-lg border border-tmm05-line px-3.5 text-[0.85rem]/none font-semibold text-tmm05-ink transition-colors hover:border-tmm05-acc hover:text-tmm05-acc" href="#tmm05-title">Console</a>
    </div>
  </header>

  <main class="mx-auto grid w-[min(48rem,calc(100%-2rem))] gap-3.5 py-[clamp(2.5rem,8vw,5rem)]">
    <nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-1.5 font-tmm05-display text-[0.8rem]/none font-medium text-tmm05-mut">
      <li><a class="hover:text-tmm05-acc" href="#tmm05-title">Docs</a></li><li aria-hidden="true">/</li>
      <li><a class="hover:text-tmm05-acc" href="#tmm05-title">Guides</a></li><li aria-hidden="true">/</li>
      <li aria-current="page" class="text-tmm05-ink">Deploy</li>
    </ol></nav>
    <h1 class="font-tmm05-display text-[clamp(1.9rem,5.5vw,3rem)]/[1.08] font-bold tracking-[-0.035em] text-balance">Deploying to the edge</h1>
    <p class="text-[clamp(0.95rem,2.2vw,1.08rem)] text-tmm05-mut text-pretty">A first deploy takes one command and about ninety seconds. This guide covers the build step, region selection and rollback.</p>
    <pre class="mt-1.5 overflow-x-auto rounded-[10px] border border-tmm05-line bg-tmm05-surf px-4.5 py-4 font-tmm05-mono text-[0.85rem]/relaxed font-medium"><code><span class="text-tmm05-mut select-none" aria-hidden="true">$ </span><span class="text-tmm05-acc">sable deploy</span> --region eu-west-2 --canary 25</code></pre>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm05-bg: #f1f5f9;
  --color-tmm05-bg: oklch(0.968 0.007 248);
  --color-tmm05-surf: #ffffff;
  --color-tmm05-surf: oklch(1 0 0);
  --color-tmm05-line: #cbd5e1;
  --color-tmm05-line: oklch(0.87 0.02 253);
  --color-tmm05-ink: #0f172a;
  --color-tmm05-ink: oklch(0.21 0.04 266);
  --color-tmm05-mut: #5a687d;
  --color-tmm05-mut: oklch(0.5 0.035 257);
  --color-tmm05-acc: #0f766e;
  --color-tmm05-acc: oklch(0.48 0.1 180);
  --color-tmm05-on-acc: #ffffff;
  --color-tmm05-on-acc: oklch(1 0 0);
  --font-tmm05-display: 'Space Grotesk', system-ui, sans-serif;
  --font-tmm05-sans: 'Geist', system-ui, sans-serif;
  --font-tmm05-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tmm05-panel: 0 24px 54px -30px rgb(15 23 42 / 0.55);
  --ease-tmm05-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm05-open: instead of a repeated selector list. */

@custom-variant tmm05-open {
  &:where([data-tmm05-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm05-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-05 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-05:has(#tmm05-theme:checked) {
  --color-tmm05-bg: #060a12;
  --color-tmm05-bg: oklch(0.14 0.02 260);
  --color-tmm05-surf: #0f1729;
  --color-tmm05-surf: oklch(0.2 0.035 265);
  --color-tmm05-line: #253046;
  --color-tmm05-line: oklch(0.31 0.04 262);
  --color-tmm05-ink: #e6edf7;
  --color-tmm05-ink: oklch(0.94 0.014 255);
  --color-tmm05-mut: #94a3b8;
  --color-tmm05-mut: oklch(0.71 0.035 257);
  --color-tmm05-acc: #2dd4bf;
  --color-tmm05-acc: oklch(0.8 0.13 180);
  --color-tmm05-on-acc: #04201c;
  --color-tmm05-on-acc: oklch(0.2 0.04 180);
}

@media (prefers-color-scheme: dark) {
  .tmm-05 {
    --color-tmm05-bg: #060a12;
    --color-tmm05-bg: oklch(0.14 0.02 260);
    --color-tmm05-surf: #0f1729;
    --color-tmm05-surf: oklch(0.2 0.035 265);
    --color-tmm05-line: #253046;
    --color-tmm05-line: oklch(0.31 0.04 262);
    --color-tmm05-ink: #e6edf7;
    --color-tmm05-ink: oklch(0.94 0.014 255);
    --color-tmm05-mut: #94a3b8;
    --color-tmm05-mut: oklch(0.71 0.035 257);
    --color-tmm05-acc: #2dd4bf;
    --color-tmm05-acc: oklch(0.8 0.13 180);
    --color-tmm05-on-acc: #04201c;
    --color-tmm05-on-acc: oklch(0.2 0.04 180);
  }

  .tmm-05:has(#tmm05-theme:checked) {
    --color-tmm05-bg: #f1f5f9;
    --color-tmm05-bg: oklch(0.968 0.007 248);
    --color-tmm05-surf: #ffffff;
    --color-tmm05-surf: oklch(1 0 0);
    --color-tmm05-line: #cbd5e1;
    --color-tmm05-line: oklch(0.87 0.02 253);
    --color-tmm05-ink: #0f172a;
    --color-tmm05-ink: oklch(0.21 0.04 266);
    --color-tmm05-mut: #5a687d;
    --color-tmm05-mut: oklch(0.5 0.035 257);
    --color-tmm05-acc: #0f766e;
    --color-tmm05-acc: oklch(0.48 0.1 180);
    --color-tmm05-on-acc: #ffffff;
    --color-tmm05-on-acc: oklch(1 0 0);
  }
}
```
