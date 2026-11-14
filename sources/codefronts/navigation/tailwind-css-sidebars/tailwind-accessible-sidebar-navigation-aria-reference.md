---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-accessible-sidebar-navigation-aria-reference/"
title: "Tailwind Accessible Sidebar Navigation ARIA Reference"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The reference build the other nineteen borrow from, ported to variants."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible Sidebar Navigation ARIA Reference
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-accessible-sidebar-navigation-aria-reference/

The reference build the other nineteen borrow from, ported to variants. A <nav> with an accessible name, a real <ul> of links, and the active item marked with aria-current="page" &mdash; styled with aria-[current=page]:, so the visual state is generated from the announced state and cannot drift from it. The disclosure is native <details>, so the whole demo needs no script at all.
## HTML
```html
<section class="tsb-01 block relative w-full min-h-svh bg-tsb01-bg text-tsb01-ink font-tsb01-sans leading-[1.55]" aria-label="Basalt developer console">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-01-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-01-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb01-line bg-tsb01-surf text-tsb01-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb01-acc peer-focus-visible:outline-offset-2" for="tsb-01-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh md:grid-cols-[16.25rem_minmax(0,1fr)]">
    <nav class="min-w-0 px-3 py-4 bg-tsb01-surf border-b border-tsb01-line md:border-b-0 md:border-r md:border-tsb01-line" aria-label="Basalt documentation">
      <p class="m-0 mb-4 px-2.5 font-tsb01-mono text-[0.82rem] tracking-[0.14em] uppercase text-tsb01-mut">Basalt</p>
      <ul class="list-none m-0 p-0">
        <li class="min-w-0"><a class="relative flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.92rem] text-tsb01-ink no-underline border-l-2 border-transparent [&>svg]:w-4.5 [&>svg]:h-4.5 [&>svg]:flex-none [&>svg]:text-tsb01-mut hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb01-accsoft aria-[current=page]:border-l-tsb01-acc aria-[current=page]:text-tsb01-acc aria-[current=page]:font-semibold aria-[current=page]:[&>svg]:text-tsb01-acc" href="#tsb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          Overview</a></li>
        <li class="min-w-0"><a class="relative flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.92rem] text-tsb01-ink no-underline border-l-2 border-transparent [&>svg]:w-4.5 [&>svg]:h-4.5 [&>svg]:flex-none [&>svg]:text-tsb01-mut hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb01-accsoft aria-[current=page]:border-l-tsb01-acc aria-[current=page]:text-tsb01-acc aria-[current=page]:font-semibold aria-[current=page]:[&>svg]:text-tsb01-acc" href="#tsb-01-main" aria-current="page">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19V9l7-5 7 5v10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          Deployments</a></li>
        <li class="min-w-0"><a class="relative flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.92rem] text-tsb01-ink no-underline border-l-2 border-transparent [&>svg]:w-4.5 [&>svg]:h-4.5 [&>svg]:flex-none [&>svg]:text-tsb01-mut hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb01-accsoft aria-[current=page]:border-l-tsb01-acc aria-[current=page]:text-tsb01-acc aria-[current=page]:font-semibold aria-[current=page]:[&>svg]:text-tsb01-acc" href="#tsb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="7.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 8v8M8 12h8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          API keys <span class="ml-auto px-1.5 py-0.5 font-tsb01-mono text-[0.72rem] bg-tsb01-surf2 text-tsb01-mut">4</span></a></li>
        <li class="min-w-0"><a class="relative flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.92rem] text-tsb01-ink no-underline border-l-2 border-transparent [&>svg]:w-4.5 [&>svg]:h-4.5 [&>svg]:flex-none [&>svg]:text-tsb01-mut hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb01-accsoft aria-[current=page]:border-l-tsb01-acc aria-[current=page]:text-tsb01-acc aria-[current=page]:font-semibold aria-[current=page]:[&>svg]:text-tsb01-acc" href="#tsb-01-main">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 17V7l8-3 8 3v10l-8 3Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          Environments</a></li>
      </ul>

      <details class="group mt-2.5 border-t border-tsb01-line" open>
        <summary class="relative flex items-center gap-2.5 min-h-11 px-2.5 py-2 text-[0.92rem] font-semibold cursor-pointer list-none [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2" aria-controls="tsb-01-sublist">
          <svg class="w-4 h-4 flex-none text-tsb01-mut transition-transform duration-150 ease-out group-open:rotate-90 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Team settings
        </summary>
        <ul class="list-none m-0 p-0" id="tsb-01-sublist">
          <li class="min-w-0"><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-9.5 text-[0.88rem] text-tsb01-mut no-underline border-l-2 border-transparent hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2" href="#tsb-01-main">Members</a></li>
          <li class="min-w-0"><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-9.5 text-[0.88rem] text-tsb01-mut no-underline border-l-2 border-transparent hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2" href="#tsb-01-main">Audit log</a></li>
          <li class="min-w-0"><a class="flex items-center min-w-0 min-h-11 py-2 pr-2.5 pl-9.5 text-[0.88rem] text-tsb01-mut no-underline border-l-2 border-transparent hover:bg-tsb01-surf2 focus-visible:outline-2 focus-visible:outline-tsb01-acc focus-visible:-outline-offset-2" href="#tsb-01-main">Billing</a></li>
        </ul>
      </details>
    </nav>

    <main class="min-w-0 grid grid-rows-[auto_minmax(0,1fr)] content-start" id="tsb-01-main">
      <header class="px-5 pt-6 pb-4.5 border-b border-tsb01-line md:px-9 md:pt-8 md:pb-5.5">
        <p class="m-0 mb-1.5 font-tsb01-mono text-[0.74rem] tracking-[0.06em] text-tsb01-mut">northwind-api / production</p>
        <h2 class="m-0 text-[clamp(1.35rem,3.4vw,1.9rem)] leading-[1.15] tracking-[-0.02em]">Deployments</h2>
      </header>

      <div class="p-5 overflow-x-auto md:px-9 md:pt-7 md:pb-10">
        <table class="w-full border-collapse text-[0.88rem] bg-tsb01-surf border border-tsb01-line">
          <thead><tr class="[&>th]:px-3.5 [&>th]:py-2.5 [&>th]:text-start [&>th]:border-b [&>th]:border-tsb01-line [&>th]:font-tsb01-mono [&>th]:text-[0.72rem] [&>th]:tracking-[0.08em] [&>th]:uppercase [&>th]:font-semibold [&>th]:text-tsb01-mut"><th scope="col">Build</th><th scope="col">Commit</th><th scope="col">Duration</th><th scope="col">State</th></tr></thead>
          <tbody class="[&>tr>td]:px-3.5 [&>tr>td]:py-2.5 [&>tr>td]:border-b [&>tr>td]:border-tsb01-line [&>tr>td]:font-tsb01-mono [&>tr>td]:text-[0.82rem] [&>tr>td]:text-tsb01-mut [&>tr:last-child>td]:border-b-0">
            <tr><td>#2481</td><td>a17f0c9</td><td>1m 42s</td><td><span class="inline-block px-1.5 py-0.5 bg-tsb01-accsoft text-tsb01-acc font-semibold">Live</span></td></tr>
            <tr><td>#2480</td><td>7b3d114</td><td>1m 39s</td><td>Rolled back</td></tr>
            <tr><td>#2479</td><td>0c92ae4</td><td>2m 04s</td><td>Superseded</td></tr>
            <tr><td>#2478</td><td>d4418f2</td><td>1m 51s</td><td>Superseded</td></tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb01-bg: #f3f5f8;
  --color-tsb01-bg: oklch(96.5% 0.006 260);
  --color-tsb01-surf: #ffffff;
  --color-tsb01-surf: oklch(100% 0 0);
  --color-tsb01-surf2: #e8ecf1;
  --color-tsb01-surf2: oklch(93% 0.008 260);
  --color-tsb01-line: #d2d8e0;
  --color-tsb01-line: oklch(87% 0.012 260);
  --color-tsb01-ink: #101419;
  --color-tsb01-ink: oklch(18% 0.012 260);
  --color-tsb01-mut: #5a6472;
  --color-tsb01-mut: oklch(48% 0.02 260);
  --color-tsb01-acc: #1b56d6;
  --color-tsb01-acc: oklch(48% 0.19 264);
  --color-tsb01-accsoft: #e3eafd;
  --color-tsb01-accsoft: oklch(94% 0.03 264);
  --font-tsb01-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb01-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tsb-01 {
  width: 100%;
  min-height: 100svh;
}

.tsb-01 *,
.tsb-01 *::before,
.tsb-01 *::after {
  box-sizing: border-box;
}
/* The theme toggle cannot be utilities: it redefines tokens for a whole subtree, and a
   utility sets one property on one element. Because v4 utilities compile to
   var(--color-tsb01-*), overriding the variables here re-themes every utility below. */

.tsb-01:has(.tsb-01-theme-input:checked) {
  --color-tsb01-bg: #0c1015;
  --color-tsb01-surf: #141a21;
  --color-tsb01-surf2: #1b222c;
  --color-tsb01-line: #29323d;
  --color-tsb01-ink: #eef1f5;
  --color-tsb01-mut: #97a2b2;
  --color-tsb01-acc: #8fa8ff;
  --color-tsb01-acc: oklch(78% 0.13 267);
  --color-tsb01-accsoft: #1a2340;
  --color-tsb01-accsoft: oklch(30% 0.07 267);
}

@media (prefers-color-scheme: dark) {
  .tsb-01 {
    --color-tsb01-bg: #0c1015;
    --color-tsb01-surf: #141a21;
    --color-tsb01-surf2: #1b222c;
    --color-tsb01-line: #29323d;
    --color-tsb01-ink: #eef1f5;
    --color-tsb01-mut: #97a2b2;
    --color-tsb01-acc: #8fa8ff;
    --color-tsb01-acc: oklch(78% 0.13 267);
    --color-tsb01-accsoft: #1a2340;
    --color-tsb01-accsoft: oklch(30% 0.07 267);
  }

  .tsb-01:has(.tsb-01-theme-input:checked) {
    --color-tsb01-bg: #f3f5f8;
    --color-tsb01-surf: #ffffff;
    --color-tsb01-surf2: #e8ecf1;
    --color-tsb01-line: #d2d8e0;
    --color-tsb01-ink: #101419;
    --color-tsb01-mut: #5a6472;
    --color-tsb01-acc: #1b56d6;
    --color-tsb01-acc: oklch(48% 0.19 264);
    --color-tsb01-accsoft: #e3eafd;
    --color-tsb01-accsoft: oklch(94% 0.03 264);
  }
}

@media (prefers-color-scheme: light) {
  .tsb-01:has(.tsb-01-theme-input:checked) {
    --color-tsb01-bg: #0c1015;
    --color-tsb01-surf: #141a21;
    --color-tsb01-surf2: #1b222c;
    --color-tsb01-line: #29323d;
    --color-tsb01-ink: #eef1f5;
    --color-tsb01-mut: #97a2b2;
    --color-tsb01-acc: #8fa8ff;
    --color-tsb01-acc: oklch(78% 0.13 267);
    --color-tsb01-accsoft: #1a2340;
    --color-tsb01-accsoft: oklch(30% 0.07 267);
  }
}
```
