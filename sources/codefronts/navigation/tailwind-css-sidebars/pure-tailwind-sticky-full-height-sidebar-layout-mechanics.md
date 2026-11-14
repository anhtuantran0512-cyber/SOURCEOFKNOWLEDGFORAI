---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-sticky-full-height-sidebar-layout-mechanics/"
title: "Pure Tailwind Sticky Full Height Sidebar Layout Mechanics"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "&ldquo;My sticky sidebar is not sticking&rdquo; is almost always the same two-line bug, and this demo is the fix stated as utilities: self-start so the rail…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Sticky Full Height Sidebar Layout Mechanics
Source: https://codefronts.com/navigation/tailwind-css-sidebars/pure-tailwind-sticky-full-height-sidebar-layout-mechanics/

&ldquo;My sticky sidebar is not sticking&rdquo; is almost always the same two-line bug, and this demo is the fix stated as utilities: self-start so the rail is shorter than its containing block, and a scroll container that is the GRID, not the page. The rail never declares a height &mdash; the stretched grid column gives it one.
## HTML
```html
<section class="tsb-17 block relative w-full min-h-svh bg-tsb17-bg text-tsb17-ink font-tsb17-sans leading-[1.55]" aria-label="Talon editor">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-17-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-17-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb17-line bg-tsb17-surf2 text-tsb17-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb17-acc peer-focus-visible:outline-offset-2" for="tsb-17-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] h-dvh overflow-y-auto bg-tsb17-surf r40:grid-cols-[minmax(0,13rem)_minmax(0,1fr)]">
    <nav class="min-w-0 self-start sticky top-0 z-2 px-1.5 py-2.5 bg-tsb17-surf2 border-r border-tsb17-line" aria-label="Talon explorer">
      <p class="m-0 mb-1.5 px-2 font-tsb17-mono text-[0.7rem] tracking-[0.1em] uppercase text-tsb17-mut">Explorer</p>
      <ul class="list-none m-0 p-0">
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb17-accsoft aria-[current=page]:text-tsb17-acc" href="#tsb-17-code" aria-current="page">index.ts</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2" href="#tsb-17-code">router.ts</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2" href="#tsb-17-code">tokens.css</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2" href="#tsb-17-code">shell.tsx</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2" href="#tsb-17-code">rail.tsx</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2 py-1.5 font-tsb17-mono text-[0.8rem] text-tsb17-ink no-underline hover:bg-tsb17-surf focus-visible:outline-2 focus-visible:outline-tsb17-acc focus-visible:-outline-offset-2" href="#tsb-17-code">measure.ts</a></li>
      </ul>
    </nav>

    <div class="min-w-0 px-4 pt-3 pb-12" id="tsb-17-code">
      <p class="m-0 mb-3 font-tsb17-mono text-[0.72rem] tracking-[0.06em] text-tsb17-acc">shell.tsx</p>
      <pre class="m-0 font-tsb17-mono text-[0.78rem] leading-[1.85] text-tsb17-mut whitespace-pre">.shell {
  display: grid;
  grid-template-columns:
    minmax(0, 13rem) minmax(0, 1fr);
  block-size: 100dvh;
  overflow-y: auto;
}

/* no height utility on the rail:
   grid's align-items: stretch already
   gives the column its full height */
.rail {
  align-self: start;
  position: sticky;
  inset-block-start: 0;
}

.code { min-inline-size: 0; }

export function mount(root) {
  const rail = root.querySelector('.rail');
  const routes = ['overview', 'deploy'];
  render(routes[0]);
  return () =&gt; rail.remove();
}

observe(rail, () =&gt; {
  measure(rail).height;
});

// keep scrolling — the rail holds its
// position because its containing block
// is taller than it is
scroll(0);
flush();
teardown();

const active = routes[0];
render(active);
observe(rail, () =&gt; measure(rail));
scroll(240);
flush();</pre>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb17-bg: #06070a;
  --color-tsb17-bg: oklch(12% 0.008 260);
  --color-tsb17-surf: #0d0f14;
  --color-tsb17-surf: oklch(16% 0.01 260);
  --color-tsb17-surf2: #13161d;
  --color-tsb17-surf2: oklch(19% 0.012 260);
  --color-tsb17-line: #1e2330;
  --color-tsb17-line: oklch(25% 0.016 260);
  --color-tsb17-ink: #e7ecf4;
  --color-tsb17-ink: oklch(93% 0.01 260);
  --color-tsb17-mut: #8b95a8;
  --color-tsb17-mut: oklch(65% 0.02 260);
  --color-tsb17-acc: #45e2e0;
  --color-tsb17-acc: oklch(85% 0.13 190);
  --color-tsb17-accsoft: #0d2b30;
  --color-tsb17-accsoft: oklch(26% 0.04 195);
  --font-tsb17-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb17-mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --breakpoint-r40: 40rem;
}
/* Root rule: the full-bleed contract. Note the app shell uses h-dvh, not min-height —
   a sticky child needs a bounded, scrolling containing block. */

.tsb-17 {
  width: 100%;
  min-height: 100svh;
}

.tsb-17 *,
.tsb-17 *::before,
.tsb-17 *::after {
  box-sizing: border-box;
}
/* Dark-first demo: the @theme block IS the dark palette, light mirror below. */

.tsb-17:has(.tsb-17-theme-input:checked) {
  --color-tsb17-bg: #f5f7fa;
  --color-tsb17-surf: #ffffff;
  --color-tsb17-surf2: #eaeef4;
  --color-tsb17-line: #d3dae4;
  --color-tsb17-ink: #0d1117;
  --color-tsb17-mut: #566072;
  --color-tsb17-acc: #0a6d72;
  --color-tsb17-acc: oklch(45% 0.09 195);
  --color-tsb17-accsoft: #d6eef0;
}

@media (prefers-color-scheme: light) {
  .tsb-17 {
    --color-tsb17-bg: #f5f7fa;
    --color-tsb17-surf: #ffffff;
    --color-tsb17-surf2: #eaeef4;
    --color-tsb17-line: #d3dae4;
    --color-tsb17-ink: #0d1117;
    --color-tsb17-mut: #566072;
    --color-tsb17-acc: #0a6d72;
    --color-tsb17-acc: oklch(45% 0.09 195);
    --color-tsb17-accsoft: #d6eef0;
  }

  .tsb-17:has(.tsb-17-theme-input:checked) {
    --color-tsb17-bg: #06070a;
    --color-tsb17-surf: #0d0f14;
    --color-tsb17-surf2: #13161d;
    --color-tsb17-line: #1e2330;
    --color-tsb17-ink: #e7ecf4;
    --color-tsb17-mut: #8b95a8;
    --color-tsb17-acc: #45e2e0;
    --color-tsb17-acc: oklch(85% 0.13 190);
    --color-tsb17-accsoft: #0d2b30;
  }
}

@media (prefers-color-scheme: dark) {
  .tsb-17:has(.tsb-17-theme-input:checked) {
    --color-tsb17-bg: #f5f7fa;
    --color-tsb17-surf: #ffffff;
    --color-tsb17-surf2: #eaeef4;
    --color-tsb17-line: #d3dae4;
    --color-tsb17-ink: #0d1117;
    --color-tsb17-mut: #566072;
    --color-tsb17-acc: #0a6d72;
    --color-tsb17-acc: oklch(45% 0.09 195);
    --color-tsb17-accsoft: #d6eef0;
  }
}
```
